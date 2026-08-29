"""
Official BSI XML-Kompendium 2023 (DocBook 5.0): pinned download and requirement parser.

Single source of truth for everything that reads the AMTLICHE Edition 2023 — the
gap-analysis script (scripts/analyze_ed23_coverage.py) and the per-sentence coverage
stage (pipeline/stage_ed23_satz_abdeckung.py) share this module so requirement
detection, sentence numbering (via utils.sentence_split) and modal-verb semantics are
identical by construction. Stdlib-only.

The v=4 URL parameter selects the published Edition-2023 file; the sha256 pin is the
real reproducibility guarantee (supply-chain gate, Grundregel 8): a mismatch aborts.
"""

import hashlib
import logging
import os
import re
import urllib.request
import xml.etree.ElementTree as ET

from utils.sentence_split import split_sentences

logger = logging.getLogger(__name__)

BSI_XML_URL = (
    "https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium/"
    "XML_Kompendium_2023.xml?__blob=publicationFile&v=4"
)
BSI_XML_SHA256 = "dd41a7467464982a79307a322be9abb7a07356a1104dd64583bab29138e410ae"
BSI_XML_CACHE_NAME = "XML_Kompendium_2023.xml"

# Shared download cache for the ED23 analyses (gitignored via Gpp-ai-tool/.cache/).
ED23_CACHE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", ".cache", "ed23_gap")
)

DB = "{http://docbook.org/ns/docbook}"
REQ_ID_RE = re.compile(r"^\s*([A-Z]{2,7}(?:\.\d+)+\.A\d+)\s+(.*)$", re.S)
# BSI-Verbindlichkeitssprache: only fully uppercase modal verbs are normative.
NORMATIVE_RE = re.compile(r"\b(MUSS|MÜSSEN|DARF|DÜRFEN|SOLLTE|SOLLTEN)\b")
KANN_RE = re.compile(r"\b(KANN|KÖNNEN)\b")

SUBSECTION_LEVEL = {
    "Basis-Anforderungen": "B",
    "Standard-Anforderungen": "S",
    "Anforderungen bei erhöhtem Schutzbedarf": "H",
}


def fetch_cached(url, cache_name, expected_sha256, cache_dir, offline=False):
    """Returns (bytes, sha256) of a pinned remote source, downloading at most once.

    The cache file is the reproducibility unit: once present and hash-matching it is never
    re-fetched. A pinned hash mismatch is fatal (supply-chain gate); an unpinned source
    logs its computed hash so the pin can be filled in.
    """
    os.makedirs(cache_dir, exist_ok=True)
    path = os.path.join(cache_dir, cache_name)
    data = None
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = f.read()
        actual = hashlib.sha256(data).hexdigest()
        if expected_sha256 and actual != expected_sha256:
            if offline:
                raise SystemExit(
                    f"FEHLER: Cache {cache_name} weicht vom Pin ab ({actual}) und --offline "
                    "verhindert den Neu-Download."
                )
            logger.warning(f"Cache {cache_name} weicht vom Pin ab — lade neu.")
            data = None
    if data is None:
        if offline:
            raise SystemExit(f"FEHLER: --offline gesetzt, aber {cache_name} fehlt im Cache.")
        logger.info(f"Lade {url} ...")
        # bsi.bund.de sits behind a CDN that answers 403 to the default Python-urllib agent.
        request = urllib.request.Request(
            url, headers={"User-Agent": "Mozilla/5.0 (compatible; GSpp-Tools ed23-gap-analyse)"}
        )
        last_error = None
        for attempt in range(1, 4):
            try:
                with urllib.request.urlopen(request, timeout=60) as response:
                    data = response.read()
                break
            except Exception as e:  # noqa: BLE001 - retry on any transient network failure
                last_error = e
                logger.warning(f"Download-Versuch {attempt}/3 fehlgeschlagen: {e}")
        if data is None:
            raise SystemExit(f"FEHLER: Download von {url} endgültig fehlgeschlagen: {last_error}")
        tmp = path + ".tmp"
        with open(tmp, "wb") as f:
            f.write(data)
        os.replace(tmp, path)
    actual = hashlib.sha256(data).hexdigest()
    if expected_sha256:
        if actual != expected_sha256:
            raise SystemExit(
                f"FEHLER: SHA-256 von {cache_name} weicht vom Pin ab: erwartet "
                f"{expected_sha256}, ist {actual}. Quelle hat sich geändert — Abbruch."
            )
    else:
        logger.info(f"HINWEIS: kein SHA-256-Pin für {cache_name}; berechnet: {actual}")
    return data, actual


def fetch_official_xml(cache_dir=ED23_CACHE_DIR, offline=False):
    """Downloads (or reuses) the pinned official Kompendium XML; returns (bytes, sha256)."""
    return fetch_cached(BSI_XML_URL, BSI_XML_CACHE_NAME, BSI_XML_SHA256, cache_dir, offline)


def parse_requirement_title(title):
    """Parses 'APP.3.2.A1 Titel (B) [Rolle]' into (id, titel, level, rolle) or None.

    Order-independent: the LAST '(B|S|H)' token is the level, the LAST '[...]' token the
    role (so mid-title parentheses like '(VPNs)' survive), and exactly those spans are cut
    out of the title — nothing requirement-looking is silently dropped.
    """
    m = REQ_ID_RE.match(title or "")
    if not m:
        return None
    req_id, tail = m.group(1), " ".join(m.group(2).split())
    level_matches = list(re.finditer(r"\(([BSH])\)", tail))
    rolle_matches = list(re.finditer(r"\[([^\]]+)\]", tail))
    level_m = level_matches[-1] if level_matches else None
    rolle_m = rolle_matches[-1] if rolle_matches else None
    titel = tail
    for span in sorted((x.span() for x in (level_m, rolle_m) if x), reverse=True):
        titel = titel[: span[0]] + " " + titel[span[1]:]
    return (
        req_id,
        " ".join(titel.split()).strip(),
        level_m.group(1) if level_m else None,
        rolle_m.group(1) if rolle_m else None,
    )


def load_official_xml(xml_bytes):
    """Parses the official DocBook Kompendium into ({req_id: record}, rejected_titles).

    A section is a requirement iff its title matches the ID pattern AND an ancestor section
    is titled '...Anforderungen...' (keeps Gefährdungslage/Kreuzreferenz prose out). Prose is
    every non-title descendant text in document order; sentences use the shared splitter, so
    the numbering semantics match satz_nr production.
    """
    root = ET.fromstring(xml_bytes)
    parent_of = {child: parent for parent in root.iter() for child in parent}
    requirements = {}
    rejected_titles = []

    for el in root.iter():
        if el.tag not in (DB + "section", DB + "chapter"):
            continue
        title_el = el.find(DB + "title")
        if title_el is None:
            continue
        title_text = " ".join("".join(title_el.itertext()).split())
        parsed = parse_requirement_title(title_text)
        if not parsed:
            continue
        req_id, titel, level, rolle = parsed

        ancestor_titles = []
        node = el
        while node in parent_of:
            node = parent_of[node]
            t = node.find(DB + "title") if node.tag in (DB + "section", DB + "chapter") else None
            if t is not None:
                ancestor_titles.append(" ".join("".join(t.itertext()).split()))
        if not any("Anforderungen" in t for t in ancestor_titles):
            rejected_titles.append(title_text)
            continue

        sublevel = None
        for t in ancestor_titles:
            for key, value in SUBSECTION_LEVEL.items():
                if key in t:
                    sublevel = value
                    break
            if sublevel:
                break

        prose_parts = []
        has_lists = False
        nested_sections = 0
        for child in el:
            if child.tag == DB + "title":
                continue
            if child.tag in (DB + "section", DB + "chapter"):
                nested_sections += 1
                continue
            if child.tag in (DB + "itemizedlist", DB + "orderedlist"):
                has_lists = True
            prose_parts.append(" ".join("".join(child.itertext()).split()))
        prose = " ".join(p for p in prose_parts if p)
        prose = prose.replace("\xa0", " ").replace("­", "")

        entfallen = titel.strip().upper().startswith("ENTFALLEN") or prose.strip().startswith(
            "Diese Anforderung ist entfallen"
        )
        saetze = split_sentences(prose)
        normative_idx = [i for i, s in enumerate(saetze, 1) if NORMATIVE_RE.search(s)]
        kann_idx = [
            i for i, s in enumerate(saetze, 1)
            if KANN_RE.search(s) and i not in set(normative_idx)
        ]

        if req_id in requirements:
            raise SystemExit(f"FEHLER: Anforderungs-ID {req_id} kommt im XML doppelt vor.")
        requirements[req_id] = {
            "id": req_id,
            "baustein": req_id.rsplit(".A", 1)[0],
            "schicht": req_id.split(".", 1)[0],
            "titel": titel,
            "level": level or sublevel,
            "sublevel": sublevel,
            "rolle": rolle,
            "entfallen": entfallen,
            "saetze": saetze,
            "normative_idx": normative_idx,
            "kann_idx": kann_idx,
            "has_lists": has_lists,
            "nested_sections": nested_sections,
        }
    return requirements, rejected_titles
