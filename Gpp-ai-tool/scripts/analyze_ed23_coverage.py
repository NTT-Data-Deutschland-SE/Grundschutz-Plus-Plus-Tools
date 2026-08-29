#!/usr/bin/env python3
"""Multi-source ED23 coverage/gap cross-analysis (Handbuch D12 / Kapitel 10.5 Punkt 3).

Answers, with defensible numbers: which Anforderungen and Teilanforderungen of the BSI
IT-Grundschutz-Kompendium Edition 2023 have NO GS++ measure pointing at them — the reverse
direction of hilfsdateien/gpp_ed23_anforderungen.json. Cross-references four independent
sources and reports at three granularities, each honestly labeled:

  (a) Anforderungsebene   — denominator = active requirements of the official BSI XML
                            Kompendium 2023 (authoritative); rock solid, the headline.
  (b) Teilanforderungen   — per source, internally consistent: our satz_nr refs against the
                            stripped corpus; BSI GSMap UA indexes with max-index lower bounds.
  (c) XML-Satzebene       — best effort: our satz coverage projected onto the official
                            normative sentences via similarity alignment, with per-requirement
                            quality buckets (aligned / teilweise / grob).

Sources (all pinned; downloads cached under Gpp-ai-tool/.cache/ed23_gap/, gitignored):
  1. Official BSI XML Kompendium 2023 (DocBook 5.0)                      [download]
  2. Ours: hilfsdateien/gpp_ed23_anforderungen.json (GS++ -> ED23)       [repo]
     plus the pre-review 5521-entry version from git history for the before/after view.
  3. BSI GSMap: ITGS-to-GS++-mapping_collection.json (ED23-UA -> GS++)   [download]
  4. hilfsdateien/prozessbausteine_mapping.json (ED23 -> GS++, 1:1)      [repo]
Corpora: hilfsdateien/ed23_anforderungen_stripped.json (satz_nr universe) and the pinned
GS++ resolved catalog (GS++ measure universe, forward direction).

Deterministic and idempotent: same inputs + same --date produce byte-identical outputs.
No third-party packages (stdlib only), so it runs without a venv:

Usage:
    uv run Gpp-ai-tool/scripts/analyze_ed23_coverage.py [--offline] [--cache-dir DIR]
        [--json PATH] [--report PATH] [--date YYYY-MM-DD] [--strict] [--skip-vergleich]

Exit codes: 0 = OK (soft anchor drift is warned), 1 = hard invariant violated or
(--strict) soft anchor drift.
"""

import argparse
import difflib
import json
import logging
import os
import re
import subprocess
import sys
from collections import Counter
from datetime import date

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(REPO_ROOT, "Gpp-ai-tool", "src"))

from constants import (  # noqa: E402
    GPP_KOMPENDIUM_JSON_PATH,
    GPP_CATALOG_PIN_COMMIT,
    GPP_CATALOG_PIN_SHA256,
    PROZESSBAUSTEINE_LAYERS,
)
# XML parsing, modal-verb semantics and the pinned download live in utils.ed23_xml (shared
# with pipeline/stage_ed23_satz_abdeckung); re-imported names keep this module's public
# surface (tests) unchanged.
from utils.ed23_xml import (  # noqa: E402,F401
    BSI_XML_URL,
    NORMATIVE_RE,
    KANN_RE,
    fetch_cached,
    fetch_official_xml,
    load_official_xml,
    parse_requirement_title,
)

# --- Pinned sources ------------------------------------------------------------------------
# Commit that last touched the GSMap mapping file (2026-07-27) — pinned instead of `main`.
ITGS_PIN_COMMIT = "8f0bcd1fbb4f47a7bec911fc20118ce6e8ef4dad"
ITGS_MAPPING_URL = (
    "https://raw.githubusercontent.com/BSI-Bund/Stand-der-Technik-Bibliothek/"
    f"{ITGS_PIN_COMMIT}/control_layer/Mappings/IT-GS2023-zu-GSpp/"
    "ITGS-to-GS%2B%2B-mapping_collection.json"
)
ITGS_MAPPING_SHA256 = "df7ea11261ace956a3ebb440f60928851a4815f5545775ac9b24e4d3d22f267f"
# Last commit before the strict maker-checker re-run — its mapping file is the 5521-entry
# pre-review state used for the before/after comparison (5521 -> 3046).
OLD_MAPPING_GIT_REF = "d188329"

OURS_PATH = os.path.join(REPO_ROOT, "hilfsdateien", "gpp_ed23_anforderungen.json")
STRIPPED_PATH = os.path.join(REPO_ROOT, "hilfsdateien", "ed23_anforderungen_stripped.json")
PROZESS_PATH = os.path.join(REPO_ROOT, "hilfsdateien", "prozessbausteine_mapping.json")
# Per-sentence coverage judgment from pipeline/stage_ed23_satz_abdeckung (optional input;
# when absent, tier (d) is omitted from JSON and report).
SATZ_ABDECKUNG_PATH = os.path.join(REPO_ROOT, "hilfsdateien", "ed23_satz_abdeckung.json")
DEFAULT_CACHE_DIR = os.path.join(REPO_ROOT, "Gpp-ai-tool", ".cache", "ed23_gap")
DEFAULT_JSON_OUT = os.path.join(REPO_ROOT, "hilfsdateien", "ed23_gap_analyse.json")
DEFAULT_REPORT_OUT = os.path.join(REPO_ROOT, "hilfsdateien", "ed23_gap_report.md")

# Face-validity anchors: independently documented figures the run must reproduce
# (Handbuch Kapitel 10.3 for ITGS, Commit-Message 5bc9612 / RELEASE_NOTES_v4.0 for ours).
# Drift is a warning by default and fatal under --strict.
EXPECTED_ANCHORS = {
    "ours_maps": 3046,
    "ours_distinct_sources": 820,
    "ours_distinct_targets": 1329,
    "old_maps": 5521,
    "itgs_maps": 1185,
    "itgs_distinct_teilanforderungen": 824,
    "itgs_relationships": {
        "subset-of": 464, "intersects-with": 395, "superset-of": 187,
        "equivalent-to": 118, "equal-to": 21,
    },
    "gpp_controls": 1000,
    "forward_gap_ours": 180,
    # Handbuch 10.3 nennt 13 veraltete unter den 33 GS++-Ziel-IDs der Methodik-Maps;
    # über ALLE 1185 Maps gerechnet sind es 17 distinct veraltete Ziel-IDs.
    "itgs_dangling_gpp_targets": 17,
    "official_bausteine": 111,
}

UA_RE = re.compile(r"^(?P<req>.+?)-UA\.(?P<idx>\d+)$")
# Modal verbs are stripped before similarity scoring: the stripped corpus is the NTT
# maturity-level-3 paraphrase which systematically rewrites "MUSS ... übernehmen" as
# "übernimmt", so keeping them would depress every score.
MODAL_STOPWORDS = frozenset(
    "muss müssen darf dürfen sollte sollten kann können".split()
)
ALIGN_THRESHOLD = 0.5   # minimum similarity for a satz-to-satz assignment
GROB_MEAN_SCORE = 0.4   # below this mean best score the whole requirement falls back to "grob"
GROB_LEN_FACTOR = 2.0   # sentence-count mismatch beyond this factor also falls back


def log(msg: str) -> None:
    print(msg, flush=True)


def warn(msg: str) -> None:
    print(f"WARNUNG: {msg}", flush=True)


# --- Layer 1: acquisition (fetch_cached/load_official_xml come from utils.ed23_xml) --------

def git_bytes(ref_and_path: str):
    """Returns the bytes of `<ref>:<path>` from git history, or None with a warning."""
    try:
        result = subprocess.run(
            ["git", "-C", REPO_ROOT, "show", ref_and_path],
            capture_output=True, check=True,
        )
        return result.stdout
    except (subprocess.CalledProcessError, OSError) as e:
        warn(f"git show {ref_and_path} fehlgeschlagen ({e}); Vorher/Nachher-Vergleich entfällt.")
        return None


def git_head() -> str:
    try:
        result = subprocess.run(
            ["git", "-C", REPO_ROOT, "rev-parse", "--short", "HEAD"],
            capture_output=True, check=True, text=True,
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, OSError):
        return "unbekannt"


# --- Layer 1b: loaders ---------------------------------------------------------------------

def _iter_maps(mapping_collection: dict):
    for mapping in mapping_collection.get("mapping-collection", {}).get("mappings", []) or []:
        for entry in mapping.get("maps", []) or []:
            yield entry


def load_ours(raw: bytes):
    """Loads our GS++->ED23 mapping into flat entries {source, target, satz, label, relationship}."""
    doc = json.loads(raw)
    entries = []
    for entry in _iter_maps(doc):
        sources = [s.get("id-ref") for s in entry.get("sources", []) if s.get("id-ref")]
        for target in entry.get("targets", []) or []:
            tid = target.get("id-ref")
            if not tid:
                continue
            satz = None
            label = None
            for prop in target.get("props", []) or []:
                if prop.get("name") == "statement-sentence":
                    try:
                        satz = int(prop.get("value"))
                    except (TypeError, ValueError):
                        satz = None
                elif prop.get("name") == "label":
                    label = prop.get("value")
            for source in sources:
                entries.append({
                    "source": source, "target": tid, "satz": satz, "label": label,
                    "relationship": entry.get("relationship"),
                })
    return entries


def load_itgs(raw: bytes):
    """Loads the BSI GSMap mapping into flat entries {ua_id, req, ua_idx, target, relationship, gefaehrdungen}."""
    doc = json.loads(raw)
    entries = []
    for entry in _iter_maps(doc):
        relationship = entry.get("relationship")
        gefaehrdungen = sorted({
            p.get("value") for p in entry.get("props", []) or []
            if p.get("name") == "elementare_gefaehrdung" and p.get("value")
        })
        sources = [s.get("id-ref") for s in entry.get("sources", []) if s.get("id-ref")]
        targets = [t.get("id-ref") for t in entry.get("targets", []) if t.get("id-ref")]
        for source in sources:
            ua = UA_RE.match(source)
            req = ua.group("req") if ua else source
            ua_idx = int(ua.group("idx")) if ua else None
            for target in targets:
                entries.append({
                    "ua_id": source, "req": req, "ua_idx": ua_idx,
                    "target": target, "relationship": relationship,
                    "gefaehrdungen": gefaehrdungen,
                })
    return entries


def load_stripped(path: str):
    with open(path, "r", encoding="utf-8") as f:
        doc = json.load(f)
    result = {}
    for item in doc.get("ed23_anforderungen", []):
        result[item["id"]] = {
            "name": item.get("name", ""),
            "saetze": item.get("saetze", []) or [],
            "entfallen": (item.get("name", "") or "").startswith("ENTFALLEN"),
        }
    return result


def load_prozess(path: str):
    with open(path, "r", encoding="utf-8") as f:
        doc = json.load(f)
    return doc.get("prozessbausteine_mapping", {}) or {}


def load_satz_abdeckung(path: str):
    """Loads the per-sentence coverage judgment (stage_ed23_satz_abdeckung), or None.

    Returns {"meta": ..., "per_req": {norm_id: {n_saetze, normative, by_satz{int: [gpp ids]}}}}.
    """
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        doc = json.load(f)
    root = doc.get("ed23_satz_abdeckung", {})
    per_req = {}
    for rid, rec in (root.get("anforderungen") or {}).items():
        by_satz = {}
        for hit in rec.get("treffer", []) or []:
            try:
                by_satz.setdefault(int(hit["satz_nr"]), set()).add(hit["control_id"])
            except (KeyError, TypeError, ValueError):
                continue
        per_req[norm(rid)] = {
            "n_saetze": rec.get("n_saetze"),
            "normative": rec.get("normative_saetze", []) or [],
            "by_satz": {k: sorted(v) for k, v in by_satz.items()},
        }
    return {"meta": root.get("meta", {}), "per_req": per_req}


def load_gpp_controls(raw: bytes):
    """Returns {control_id: title} of every control in the pinned GS++ resolved catalog."""
    doc = json.loads(raw)
    controls = {}

    def walk_controls(items):
        for control in items or []:
            if control.get("id"):
                controls[control["id"]] = control.get("title", "") or ""
            walk_controls(control.get("controls"))

    def walk_groups(groups):
        for group in groups or []:
            walk_controls(group.get("controls"))
            walk_groups(group.get("groups"))

    walk_groups(doc.get("catalog", {}).get("groups", []))
    return controls


# --- Layer 2: joins and metrics ------------------------------------------------------------

def norm(s: str) -> str:
    return (s or "").strip().lower()


def classify_target(req_id: str, official, stripped):
    n = norm(req_id)
    if n in official:
        return "official-entfallen" if official[n]["entfallen"] else "official"
    if n in stripped:
        return "ntt-custom"
    return "dangling"


def index_ours(entries):
    """target(norm) -> {'gpp': set, 'saetze': set}"""
    by_req = {}
    for e in entries:
        slot = by_req.setdefault(norm(e["target"]), {"gpp": set(), "saetze": set()})
        slot["gpp"].add(e["source"])
        if e["satz"] is not None:
            slot["saetze"].add(e["satz"])
    return by_req
def index_itgs(entries):
    """req(norm) -> {'uas': set, 'gpp': set, 'relationships': set, 'req_level_maps': int}"""
    by_req = {}
    for e in entries:
        slot = by_req.setdefault(
            norm(e["req"]), {"uas": set(), "gpp": set(), "relationships": set(), "req_level_maps": 0}
        )
        if e["ua_idx"] is not None:
            slot["uas"].add(e["ua_idx"])
        else:
            slot["req_level_maps"] += 1
        slot["gpp"].add(e["target"])
        if e["relationship"]:
            slot["relationships"].add(e["relationship"])
    return by_req


def ua_definite_gaps(uas):
    """UA.j is provably unmapped when j < max(mapped indexes): the BSI's own numbering
    guarantees UA.j exists, we just never saw a map for it. Indexes above the max are
    unknowable (the UA universe is unpublished)."""
    if not uas:
        return []
    return sorted(set(range(1, max(uas) + 1)) - set(uas))


def align_sentences(stripped_saetze, xml_saetze):
    """Greedy 1:1 alignment stripped index -> best xml index. Returns {i: (j, score)}.

    Both similarity views are taken (character ratio and token Jaccard, modal verbs
    stripped) and the better one wins; xml sentences are consumed once.
    """
    def norm_tokens(s):
        return [t for t in re.findall(r"\w+", s.casefold()) if t not in MODAL_STOPWORDS]

    def similarity(a_tokens, b_tokens):
        if not a_tokens or not b_tokens:
            return 0.0
        ratio = difflib.SequenceMatcher(None, " ".join(a_tokens), " ".join(b_tokens)).ratio()
        sa, sb = set(a_tokens), set(b_tokens)
        jaccard = len(sa & sb) / len(sa | sb)
        return max(ratio, jaccard)

    stripped_tok = {i: norm_tokens(s) for i, s in enumerate(stripped_saetze, 1)}
    xml_tok = {j: norm_tokens(s) for j, s in enumerate(xml_saetze, 1)}
    assignment = {}
    taken = set()
    for i in sorted(stripped_tok):
        best_j, best_score = None, 0.0
        for j in sorted(xml_tok):
            if j in taken:
                continue
            score = similarity(stripped_tok[i], xml_tok[j])
            if score > best_score:
                best_j, best_score = j, score
        if best_j is not None:
            assignment[i] = (best_j, round(best_score, 3))
            if best_score >= ALIGN_THRESHOLD:
                taken.add(best_j)
    return assignment


def xml_projection(req, stripped_entry, ours_slot):
    """Projects our satz coverage onto the official XML sentences of one requirement.

    Returns {covered_normative, quality, mean_score} or None when the requirement has no
    coverage from our mapping at all. Quality buckets:
      aligned   — every covering satz found an XML partner >= threshold
      teilweise — some did
      grob      — alignment not trustworthy (paraphrase drift / count mismatch / no satz
                  refs): requirement-level coverage is propagated to ALL normative sentences.
    """
    if ours_slot is None:
        return None
    covering = sorted(ours_slot["saetze"])
    normative = set(req["normative_idx"])
    stripped_saetze = stripped_entry["saetze"] if stripped_entry else []
    if not covering or not stripped_saetze or not req["saetze"]:
        return {
            "covered_normative": sorted(normative), "quality": "grob", "mean_score": None,
        }
    ns, nx = len(stripped_saetze), len(req["saetze"])
    assignment = align_sentences(stripped_saetze, req["saetze"])
    scores = [assignment[i][1] for i in covering if i in assignment]
    mean_score = round(sum(scores) / len(scores), 3) if scores else 0.0
    len_mismatch = max(ns, nx) / max(1, min(ns, nx)) > GROB_LEN_FACTOR
    if mean_score < GROB_MEAN_SCORE or len_mismatch:
        return {
            "covered_normative": sorted(normative), "quality": "grob", "mean_score": mean_score,
        }
    covered = set()
    hits = 0
    for i in covering:
        pair = assignment.get(i)
        if pair and pair[1] >= ALIGN_THRESHOLD:
            hits += 1
            if pair[0] in normative:
                covered.add(pair[0])
    quality = "aligned" if hits == len(covering) else ("teilweise" if hits else "grob")
    if quality == "grob":
        covered = normative
    return {
        "covered_normative": sorted(covered), "quality": quality, "mean_score": mean_score,
    }


# --- Layer 3: result assembly --------------------------------------------------------------

def build_result(args, official, rejected_titles, ours, ours_old, itgs, prozess,
                 stripped, gpp_controls, source_meta, satz_urteil=None):
    ours_by_req = index_ours(ours)
    old_by_req = index_ours(ours_old) if ours_old is not None else None
    itgs_by_req = index_itgs(itgs)
    prozess_by_req = {norm(k): v for k, v in prozess.items()}
    stripped_by_norm = {norm(k): v for k, v in stripped.items()}
    official_by_norm = {norm(k): v for k, v in official.items()}
    gpp_ids = set(gpp_controls)

    active = [r for r in official.values() if not r["entfallen"]]
    entfallen = [r for r in official.values() if r["entfallen"]]

    # --- per-requirement records (official requirements only, active AND entfallen) ---
    records = []
    for req in sorted(official.values(), key=lambda r: r["id"]):
        n = norm(req["id"])
        ours_slot = ours_by_req.get(n)
        itgs_slot = itgs_by_req.get(n)
        prozess_hit = prozess_by_req.get(n)
        stripped_entry = stripped_by_norm.get(n)

        record = {
            "id": req["id"], "baustein": req["baustein"], "schicht": req["schicht"],
            "titel": req["titel"], "level": req["level"], "rolle": req["rolle"],
            "entfallen": req["entfallen"],
            "n_saetze_xml": len(req["saetze"]),
            "normative_saetze_xml": req["normative_idx"],
            "kann_saetze_xml": req["kann_idx"],
            "has_lists": req["has_lists"],
            "covered_by": {
                "ours": ours_slot is not None,
                "itgs": itgs_slot is not None,
                "prozessbausteine": prozess_hit is not None,
            },
        }
        record["covered_by"]["any"] = any(record["covered_by"].values())
        if old_by_req is not None:
            record["covered_by"]["ours_5521"] = n in old_by_req
        if ours_slot:
            n_stripped = len(stripped_entry["saetze"]) if stripped_entry else 0
            referenced = sorted(ours_slot["saetze"])
            record["ours"] = {
                "gpp_controls": sorted(ours_slot["gpp"]),
                "n_saetze_stripped": n_stripped,
                "saetze_referenziert": referenced,
                "saetze_nicht_referenziert": sorted(
                    set(range(1, n_stripped + 1)) - set(referenced)
                ),
            }
        if itgs_slot:
            uas = sorted(itgs_slot["uas"])
            record["itgs"] = {
                "gpp_targets": sorted(itgs_slot["gpp"]),
                "uas_mapped": uas,
                "ua_lower_bound": max(uas) if uas else 0,
                "definite_ua_gaps": ua_definite_gaps(uas),
                "relationships": sorted(itgs_slot["relationships"]),
                "req_level_maps": itgs_slot["req_level_maps"],
            }
        if prozess_hit:
            record["prozessbausteine"] = {"gpp_control": prozess_hit}
        projection = xml_projection(req, stripped_entry, ours_slot)
        if projection is not None:
            record["xml_projektion"] = projection
        if satz_urteil is not None and not req["entfallen"]:
            su = satz_urteil["per_req"].get(n)
            if su is not None:
                normative = set(req["normative_idx"])
                covered = sorted(i for i in su["by_satz"] if i in normative)
                record["satz_urteil"] = {
                    "abgedeckte_normative_saetze": covered,
                    "nicht_abgedeckte_normative_saetze": sorted(normative - set(covered)),
                    "treffer": {str(i): su["by_satz"][i] for i in sorted(su["by_satz"])},
                    "nummerierung_ok": su["n_saetze"] == len(req["saetze"]),
                }
        records.append(record)

    active_records = [r for r in records if not r["entfallen"]]

    # --- tier (a) summary ---
    def covered_count(key):
        return sum(1 for r in active_records if r["covered_by"][key])

    crosstab = Counter()
    for r in active_records:
        o, i = r["covered_by"]["ours"], r["covered_by"]["itgs"]
        crosstab["both" if o and i else "only_ours" if o else "only_itgs" if i else "neither"] += 1
    assert sum(crosstab.values()) == len(active_records), "Kreuztabelle summiert nicht zum Nenner"

    def slice_by(keyfunc):
        out = {}
        for r in active_records:
            slot = out.setdefault(keyfunc(r), {
                "aktiv": 0, "ohne_jede_zuordnung": 0, "ohne_ours": 0, "ohne_itgs": 0,
            })
            slot["aktiv"] += 1
            if not r["covered_by"]["any"]:
                slot["ohne_jede_zuordnung"] += 1
            if not r["covered_by"]["ours"]:
                slot["ohne_ours"] += 1
            if not r["covered_by"]["itgs"]:
                slot["ohne_itgs"] += 1
        return dict(sorted(out.items(), key=lambda kv: str(kv[0])))

    by_level = slice_by(lambda r: r["level"] or "ohne")
    by_schicht = slice_by(lambda r: r["schicht"])
    by_baustein = slice_by(lambda r: r["baustein"])
    top_gaps = sorted(
        ((b, s) for b, s in by_baustein.items() if s["ohne_jede_zuordnung"]),
        key=lambda kv: (-kv[1]["ohne_jede_zuordnung"],
                        -kv[1]["ohne_jede_zuordnung"] / kv[1]["aktiv"], kv[0]),
    )[:20]

    neither_ids = [r["id"] for r in active_records if not r["covered_by"]["any"]]

    # --- before/after (5521 vs 3046), requirement level, official active only ---
    vergleich = None
    if old_by_req is not None:
        covered_old = {r["id"] for r in active_records if r["covered_by"].get("ours_5521")}
        covered_new = {r["id"] for r in active_records if r["covered_by"]["ours"]}
        vergleich = {
            "alt_maps": len(ours_old),
            "neu_maps": len(ours),
            "abgedeckt_alt": len(covered_old),
            "abgedeckt_neu": len(covered_new),
            "verloren": sorted(covered_old - covered_new),
            "gewonnen": sorted(covered_new - covered_old),
        }

    # --- tier (b) totals ---
    satz_universe = referenced_total = 0
    for r in active_records:
        if "ours" in r:
            satz_universe += r["ours"]["n_saetze_stripped"]
            referenced_total += len(r["ours"]["saetze_referenziert"])
    # Requirements without any ours coverage contribute their full satz count as unreferenced.
    for r in active_records:
        if "ours" not in r:
            entry = stripped_by_norm.get(norm(r["id"]))
            if entry:
                satz_universe += len(entry["saetze"])

    ua_mapped_total = sum(len(r["itgs"]["uas_mapped"]) for r in active_records if "itgs" in r)
    ua_lb_total = sum(r["itgs"]["ua_lower_bound"] for r in active_records if "itgs" in r)
    ua_gaps_total = sum(len(r["itgs"]["definite_ua_gaps"]) for r in active_records if "itgs" in r)

    # --- tier (c) totals ---
    normative_total = sum(len(r["normative_saetze_xml"]) for r in active_records)
    kann_total = sum(len(r["kann_saetze_xml"]) for r in active_records)
    covered_normative_total = 0
    quality_counter = Counter()
    for r in active_records:
        projection = r.get("xml_projektion")
        if projection is None:
            continue
        quality_counter[projection["quality"]] += 1
        covered_normative_total += len(projection["covered_normative"])

    # --- deterministic decomposition cross-compare: ours satz_nr vs. BSI UA indexes -------
    # Only where BOTH mappings touch the same requirement can the two Teilanforderung
    # numberings be compared. They index different decompositions (NTT paraphrase sentences
    # vs. the GSMap's unpublished UA split), so index equality is a structural indication,
    # not proven content agreement — reported as such.
    beide = [r for r in active_records
             if "ours" in r and "itgs" in r
             and r["ours"]["saetze_referenziert"] and r["itgs"]["uas_mapped"]]
    identisch, ueberlappend, disjunkt = [], [], []
    for r in beide:
        ours_idx = set(r["ours"]["saetze_referenziert"])
        ua_idx = set(r["itgs"]["uas_mapped"])
        if ours_idx == ua_idx:
            identisch.append(r["id"])
        elif ours_idx & ua_idx:
            ueberlappend.append(r["id"])
        else:
            disjunkt.append(r["id"])
    ua_feiner_als_normativ = sorted(
        r["id"] for r in active_records
        if "itgs" in r and r["itgs"]["ua_lower_bound"] > len(r["normative_saetze_xml"])
    )
    satzzahl_gleich = sum(
        1 for r in active_records
        if "ours" in r and r["ours"]["n_saetze_stripped"] == r["n_saetze_xml"]
    )
    zerlegungsvergleich = {
        "anforderungen_in_beiden_mappings_mit_indizes": len(beide),
        "indizes_identisch": len(identisch),
        "indizes_ueberlappend": len(ueberlappend),
        "indizes_disjunkt": len(disjunkt),
        "disjunkt_ids": sorted(disjunkt),
        "ua_untergrenze_uebersteigt_normative_xml_saetze": ua_feiner_als_normativ,
        "stripped_satzzahl_gleich_xml": satzzahl_gleich,
        "stripped_satzzahl_basis": sum(1 for r in active_records if "ours" in r),
    }

    # Relationship-type histograms of both collections. Direction note: ours describes the
    # G++ control relative to the ED23 target, the GSMap the ED23-UA relative to the G++
    # target — subset-of/superset-of must be mirrored before comparing.
    relationen = {
        "ours": dict(sorted(Counter(
            e.get("relationship") or "(ohne)" for e in ours
        ).items())),
        "itgs": dict(sorted(Counter(e.get("relationship") for e in itgs).items())),
        "ours_klassifiziert": len({e.get("relationship") for e in ours} - {None}) > 1,
    }

    # --- tier (d): judged per-sentence coverage (stage_ed23_satz_abdeckung, official XML) ---
    beurteilt = None
    satz_numbering_mismatch = []
    if satz_urteil is not None:
        judged = [r for r in active_records if "satz_urteil" in r]
        satz_numbering_mismatch = sorted(
            r["id"] for r in judged if not r["satz_urteil"]["nummerierung_ok"]
        )
        denom_norm = sum(len(r["normative_saetze_xml"]) for r in judged)
        covered_norm = sum(
            len(r["satz_urteil"]["abgedeckte_normative_saetze"]) for r in judged
        )
        ohne_satz = sorted(
            r["id"] for r in judged
            if r["normative_saetze_xml"] and not r["satz_urteil"]["abgedeckte_normative_saetze"]
        )

        def satz_slice(keyfunc):
            out = {}
            for r in judged:
                slot = out.setdefault(keyfunc(r), {"normative_saetze": 0, "abgedeckt": 0})
                slot["normative_saetze"] += len(r["normative_saetze_xml"])
                slot["abgedeckt"] += len(r["satz_urteil"]["abgedeckte_normative_saetze"])
            return dict(sorted(out.items(), key=lambda kv: str(kv[0])))

        satz_by_baustein = satz_slice(lambda r: r["baustein"])
        beurteilt = {
            "anforderungen_beurteilt": len(judged),
            "anforderungen_ohne_urteil": len(active_records) - len(judged),
            "denominator_normative_saetze": denom_norm,
            "abgedeckt": covered_norm,
            "nicht_abgedeckt": denom_norm - covered_norm,
            "by_level": satz_slice(lambda r: r["level"] or "ohne"),
            "by_schicht": satz_slice(lambda r: r["schicht"]),
            "top_gap_bausteine": [
                {"baustein": b, **s} for b, s in sorted(
                    ((b, s) for b, s in satz_by_baustein.items()
                     if s["normative_saetze"] > s["abgedeckt"]),
                    key=lambda kv: (kv[1]["abgedeckt"] - kv[1]["normative_saetze"], kv[0]),
                )[:20]
            ],
            "anforderungen_ohne_einzigen_abgedeckten_satz": ohne_satz,
            # Cross-checks against tier (a): mapping says covered but no sentence survives
            # the judgment, and the judgment finds substance where no mapping points.
            "gemappt_aber_satzlos": sorted(
                r["id"] for r in judged
                if r["covered_by"]["ours"] and r["normative_saetze_xml"]
                and not r["satz_urteil"]["abgedeckte_normative_saetze"]
            ),
            "ungemappt_aber_satz_gefunden": sorted(
                r["id"] for r in judged
                if not r["covered_by"]["any"]
                and r["satz_urteil"]["abgedeckte_normative_saetze"]
            ),
        }

    # --- forward direction ---
    ours_sources = {e["source"] for e in ours}
    itgs_targets = {e["target"] for e in itgs}
    prozess_values = set(prozess.values())
    forward = {
        "gpp_controls": len(gpp_ids),
        "ohne_ed23_treffer": {
            "ours": sorted(gpp_ids - ours_sources),
            "itgs": sorted(gpp_ids - itgs_targets),
            "prozessbausteine": sorted(gpp_ids - prozess_values),
            "alle_drei": sorted(gpp_ids - ours_sources - itgs_targets - prozess_values),
        },
    }

    # --- consistency findings ---
    ours_target_classes = Counter()
    ours_class_examples = {}
    for tid in sorted({e["target"] for e in ours}):
        cls = classify_target(tid, official_by_norm, stripped_by_norm)
        ours_target_classes[cls] += 1
        ours_class_examples.setdefault(cls, []).append(tid)
    itgs_req_classes = Counter()
    itgs_class_examples = {}
    for rid in sorted({e["req"] for e in itgs}):
        cls = classify_target(rid, official_by_norm, stripped_by_norm)
        itgs_req_classes[cls] += 1
        itgs_class_examples.setdefault(cls, []).append(rid)
    itgs_dangling_gpp = sorted(itgs_targets - gpp_ids)
    prozess_dangling_keys = sorted(
        k for k in prozess if norm(k) not in official_by_norm and norm(k) not in stripped_by_norm
    )
    prozess_outside_layers = sorted(
        k for k in prozess if k.split(".", 1)[0] not in PROZESSBAUSTEINE_LAYERS
    )
    prozess_dangling_values = sorted(v for v in prozess_values if v not in gpp_ids)
    satz_range_violations = []
    for e in ours:
        if e["satz"] is None:
            continue
        entry = stripped_by_norm.get(norm(e["target"]))
        if entry and not (1 <= e["satz"] <= len(entry["saetze"])):
            satz_range_violations.append(f"{e['source']} -> {e['target']} (Satz {e['satz']})")
    duplicate_ours = [
        f"{s} -> {t} (Satz {z})" for (s, t, z), c in
        Counter((e["source"], e["target"], e["satz"]) for e in ours).items() if c > 1
    ]
    duplicate_itgs = [
        f"{u} -> {t}" for (u, t), c in
        Counter((e["ua_id"], e["target"]) for e in itgs).items() if c > 1
    ]
    level_mismatches = [
        f"{r['id']}: Titel ({r['level']}) vs. Abschnitt ({r['sublevel']})"
        for r in official.values()
        if r["level"] and r["sublevel"] and r["level"] != r["sublevel"]
    ]
    xml_missing_in_stripped = sorted(
        r["id"] for r in official.values() if norm(r["id"]) not in stripped_by_norm
    )
    # NTT-only requirement ids split by whether their Baustein itself is official:
    # a truly custom Baustein vs. extra NTT requirements inside an official Baustein.
    official_baustein_set = {r["baustein"] for r in official.values()}
    stripped_only = [
        rid for rid in stripped if norm(rid) not in official_by_norm and ".A" in rid
    ]
    ntt_custom_bausteine = sorted({
        b for b in (rid.rsplit(".A", 1)[0] for rid in stripped_only)
        if b not in official_baustein_set
    })
    ntt_zusatz_in_amtlichen = sorted(
        rid for rid in stripped_only if rid.rsplit(".A", 1)[0] in official_baustein_set
    )
    nested_section_reqs = sorted(r["id"] for r in official.values() if r["nested_sections"])

    konsistenz = {
        "ours_zielklassen": dict(sorted(ours_target_classes.items())),
        "ours_ziele_entfallen": ours_class_examples.get("official-entfallen", []),
        "ours_ziele_ntt_custom": ours_class_examples.get("ntt-custom", []),
        "ours_ziele_dangling": ours_class_examples.get("dangling", []),
        "itgs_quellklassen": dict(sorted(itgs_req_classes.items())),
        "itgs_quellen_entfallen": itgs_class_examples.get("official-entfallen", []),
        "itgs_quellen_dangling": itgs_class_examples.get("dangling", []),
        "itgs_dangling_gpp_ziele": itgs_dangling_gpp,
        "prozess_dangling_quellen": prozess_dangling_keys,
        "prozess_ausserhalb_layer": prozess_outside_layers,
        "prozess_dangling_gpp_ziele": prozess_dangling_values,
        "satz_nr_ausser_bereich": satz_range_violations,
        "duplikate_ours": duplicate_ours,
        "duplikate_itgs": duplicate_itgs,
        "level_mismatches": sorted(level_mismatches),
        "xml_anforderungen_ohne_stripped_eintrag": xml_missing_in_stripped,
        "ntt_custom_bausteine": ntt_custom_bausteine,
        "ntt_zusatz_anforderungen_in_amtlichen_bausteinen": ntt_zusatz_in_amtlichen,
        "xml_sections_mit_untersektionen": nested_section_reqs,
        "xml_verworfene_titel": sorted(rejected_titles),
        "satz_urteil_nummerierung_abweichend": satz_numbering_mismatch,
    }

    # --- soft anchors ---
    itgs_relationship_hist = dict(sorted(Counter(e["relationship"] for e in itgs).items()))
    anchor_values = {
        "ours_maps": len(ours),
        "ours_distinct_sources": len(ours_sources),
        "ours_distinct_targets": len({e["target"] for e in ours}),
        "old_maps": len(ours_old) if ours_old is not None else None,
        "itgs_maps": len(itgs),
        "itgs_distinct_teilanforderungen": len({e["ua_id"] for e in itgs}),
        "itgs_relationships": itgs_relationship_hist,
        "gpp_controls": len(gpp_ids),
        "forward_gap_ours": len(forward["ohne_ed23_treffer"]["ours"]),
        "itgs_dangling_gpp_targets": len(itgs_dangling_gpp),
        "official_bausteine": len({r["baustein"] for r in official.values()}),
    }
    anchor_drift = []
    for key, expected in EXPECTED_ANCHORS.items():
        actual = anchor_values.get(key)
        if actual is not None and actual != expected:
            anchor_drift.append(f"{key}: erwartet {expected}, ist {actual}")

    summary = {
        "anforderungen": {
            "denominator_aktiv": len(active_records),
            "entfallen": len(entfallen),
            "abgedeckt": {
                "ours": covered_count("ours"),
                "itgs": covered_count("itgs"),
                "prozessbausteine": covered_count("prozessbausteine"),
                "mindestens_eine_quelle": covered_count("any"),
            },
            "ohne_zuordnung": {
                "ours": len(active_records) - covered_count("ours"),
                "itgs": len(active_records) - covered_count("itgs"),
                "keine_einzige_quelle": len(neither_ids),
            },
            "crosstab_ours_itgs": dict(crosstab),
            "by_level": by_level,
            "by_schicht": by_schicht,
            "top_gap_bausteine": [
                {"baustein": b, **s} for b, s in top_gaps
            ],
            "ohne_jede_zuordnung_ids": neither_ids,
        },
        "vergleich_5521_vs_3046": vergleich,
        "teilanforderungen": {
            "ours": {
                "satz_universum_aktive_anforderungen": satz_universe,
                "referenziert": referenced_total,
                "nicht_referenziert": satz_universe - referenced_total,
            },
            "itgs": {
                "ua_gemappt": ua_mapped_total,
                "ua_untergrenze_summe": ua_lb_total,
                "beweisbare_ua_luecken": ua_gaps_total,
            },
            "xml_normativ": {
                "denominator_normative_saetze": normative_total,
                "kann_saetze": kann_total,
                "abgedeckt_projiziert": covered_normative_total,
                "qualitaet": dict(sorted(quality_counter.items())),
            },
            "zerlegungsvergleich": zerlegungsvergleich,
            "relationen": relationen,
            "beurteilt": beurteilt,
        },
        "gegenrichtung": {
            "gpp_controls": forward["gpp_controls"],
            "ohne_ed23_treffer": {
                k: len(v) for k, v in forward["ohne_ed23_treffer"].items()
            },
        },
    }

    result = {
        "ed23_gap_analyse": {
            "meta": {
                "generated": args.date,
                "script": "Gpp-ai-tool/scripts/analyze_ed23_coverage.py",
                "repo_head": git_head(),
                "sources": source_meta,
                "method_notes": [
                    "Ebene (a): Nenner sind die aktiven Anforderungen des offiziellen BSI-XML-"
                    "Kompendiums 2023; ENTFALLEN-Anforderungen werden separat gezählt.",
                    "Ebene (b) ours: Teilanforderung = Satz-Index (statement-sentence) im "
                    "stripped-Korpus (NTT-Maturity-Level-3-Paraphrase, nicht BSI-Wortlaut).",
                    "Ebene (b) ITGS: Das UA-Universum des BSI-GSMap-Mappings ist unveröffentlicht; "
                    "max. beobachteter UA-Index je Anforderung dient als Untergrenze, ungemappte "
                    "Indizes darunter sind beweisbare Lücken.",
                    "Ebene (c): Projektion der Satz-Abdeckung auf die normativen XML-Sätze via "
                    f"Ähnlichkeits-Alignment (Schwelle {ALIGN_THRESHOLD}, Fallback 'grob' unter "
                    f"{GROB_MEAN_SCORE} bzw. bei Satzzahl-Faktor > {GROB_LEN_FACTOR}); "
                    "Headline-Zahlen hängen nie am Alignment.",
                    "Normativ = Satz mit MUSS/MÜSSEN/DARF/DÜRFEN/SOLLTE/SOLLTEN in Großschreibung; "
                    "KANN/KÖNNEN wird separat gezählt.",
                ],
            },
            "summary": summary,
            "anforderungen": records,
            "forward_gaps": forward["ohne_ed23_treffer"],
            "konsistenz": konsistenz,
            "anker": {"erwartet": EXPECTED_ANCHORS, "ist": anchor_values, "drift": anchor_drift},
        }
    }
    return result


# --- Layer 4: report -----------------------------------------------------------------------

def de(n) -> str:
    """1234 -> '1.234' (deutsche Tausenderpunkte)."""
    return f"{n:,}".replace(",", ".")


def pct(part, whole) -> str:
    if not whole:
        return "0,0 %"
    return f"{100.0 * part / whole:.1f} %".replace(".", ",")


def render_report(result: dict) -> str:
    d = result["ed23_gap_analyse"]
    meta, s = d["meta"], d["summary"]
    a = s["anforderungen"]
    t = s["teilanforderungen"]
    g = s["gegenrichtung"]
    k = d["konsistenz"]
    v = s["vergleich_5521_vs_3046"]
    denom = a["denominator_aktiv"]
    lines = []
    add = lines.append

    add("# ED23-Lücken-Kreuzanalyse: Welche Anforderungen der Edition 2023 deckt Grundschutz++ nicht ab?")
    add("")
    add(f"*Generiert am {meta['generated']} von `{meta['script']}` (Repo-Stand {meta['repo_head']}). "
        "Deterministisch reproduzierbar, siehe Abschnitt 8.*")
    add("")
    add("## 1. Kernaussage")
    add("")
    neither = a["ohne_zuordnung"]["keine_einzige_quelle"]
    ohne_ours = a["ohne_zuordnung"]["ours"]
    ohne_itgs = a["ohne_zuordnung"]["itgs"]
    kern = (
        f"Das offizielle IT-Grundschutz-Kompendium Edition 2023 enthält {de(denom)} aktive "
        f"Anforderungen in {de(meta['sources']['official_xml']['bausteine'])} Bausteinen "
        f"(zuzüglich {de(a['entfallen'])} entfallene). "
        f"{de(ohne_ours)} davon ({pct(ohne_ours, denom)}) haben im GS++→ED23-Mapping "
        f"({de(EXPECTED_ANCHORS['ours_maps'])} Zuordnungen nach der strengen Prüfung) keine "
        f"Maßnahme, die auf sie zeigt; nach dem BSI-eigenen GSMap-Mapping sind es "
        f"{de(ohne_itgs)} ({pct(ohne_itgs, denom)}). "
        f"Über alle drei Quellen zusammen (unser Mapping, BSI-GSMap, Prozessbaustein-Mapping) "
        f"bleiben {de(neither)} Anforderungen ({pct(neither, denom)}) ohne jede Zuordnung."
    )
    if v:
        kern += (
            f" Die strenge Prüfung (5.521 → 3.046 Zuordnungen) hat auf Anforderungsebene "
            f"{de(len(v['verloren']))} Anforderungen ihre letzte Zuordnung gekostet "
            f"(vorher {de(v['abgedeckt_alt'])}, nachher {de(v['abgedeckt_neu'])} abgedeckt)"
        )
        if v["gewonnen"]:
            kern += f"; {de(len(v['gewonnen']))} kamen neu hinzu"
        kern += "."
    bt = t.get("beurteilt")
    if bt:
        kern += (
            f" Die satzgenaue Beurteilung jedes normativen Satzes des amtlichen Wortlauts "
            f"gegen den GS++-Katalog (LLM-Maker-Checker) ergibt: {de(bt['abgedeckt'])} von "
            f"{de(bt['denominator_normative_saetze'])} normativen Teilanforderungen "
            f"({pct(bt['abgedeckt'], bt['denominator_normative_saetze'])}) sind durch "
            f"mindestens eine GS++-Maßnahme abgedeckt; "
            f"{de(len(bt['anforderungen_ohne_einzigen_abgedeckten_satz']))} Anforderungen "
            "haben keinen einzigen abgedeckten normativen Satz."
        )
    else:
        kern += (
            f" Auf Teilanforderungsebene (normative Sätze des offiziellen Wortlauts: "
            f"{de(t['xml_normativ']['denominator_normative_saetze'])}) ist die Projektion "
            "methodisch unschärfer — Details in Abschnitt 5."
        )
    kern += (
        f" In der Gegenrichtung haben {de(g['ohne_ed23_treffer']['ours'])} von "
        f"{de(g['gpp_controls'])} GS++-Maßnahmen keine ED23-Entsprechung."
    )
    add(kern)
    add("")

    add("## 2. Fragestellung und Quellen")
    add("")
    add("Gap-Analyse in der Gegenrichtung: nicht „wohin zeigt jede GS++-Maßnahme?“, sondern "
        "„auf welche ED23-Anforderung zeigt *keine* Maßnahme?“ — die Frage aus Handbuch-"
        "Kapitel 10.5 (Punkt 3) bzw. Anhang D12.")
    add("")
    add("| Quelle | Richtung | Umfang | Methode | Pin |")
    add("|---|---|---|---|---|")
    src = meta["sources"]
    add(f"| Offizielles BSI-XML-Kompendium 2023 | (Nenner) | {de(src['official_xml']['anforderungen_aktiv'])} aktive + "
        f"{de(src['official_xml']['anforderungen_entfallen'])} entfallene Anforderungen | amtlicher Wortlaut | "
        f"sha256 `{src['official_xml']['sha256'][:12]}…` |")
    add(f"| Unser Mapping (`gpp_ed23_anforderungen.json`) | GS++ → ED23 | {de(src['ours']['maps'])} Maps, "
        f"{de(src['ours']['distinct_sources'])} Maßnahmen, {de(src['ours']['distinct_targets'])} Ziele | "
        f"LLM Maker-Checker, status draft | Repo `{meta['repo_head']}` |")
    add(f"| BSI GSMap (`ITGS-to-GS++-mapping_collection.json`) | ED23-UA → GS++ | {de(src['itgs']['maps'])} Maps, "
        f"{de(src['itgs']['distinct_teilanforderungen'])} Teilanforderungen | menschlich (GSMap-Tool) | "
        f"Commit `{ITGS_PIN_COMMIT[:12]}…` |")
    add(f"| Prozessbaustein-Mapping | ED23 → GS++ (1:1) | {de(src['prozessbausteine']['entries'])} Einträge, "
        f"nur {'/'.join(PROZESSBAUSTEINE_LAYERS)} | LLM, vollständigkeitsgetrieben | Repo `{meta['repo_head']}` |")
    add(f"| GS++-Katalog (resolved) | (Universum) | {de(src['gpp_catalog']['controls'])} Maßnahmen | — | "
        f"Commit `{GPP_CATALOG_PIN_COMMIT[:12]}…` |")
    if src.get("satz_abdeckung"):
        sa = src["satz_abdeckung"]
        add(f"| Satz-Beurteilung (`ed23_satz_abdeckung.json`) | ED23-Satz → GS++ | "
            f"{de(sa.get('anforderungen') or 0)} Anforderungen, {de(sa.get('zuordnungen') or 0)} "
            f"verifizierte Zuordnungen | LLM Maker-Checker ({sa.get('maker_model')} / "
            f"{sa.get('checker_model')}), amtliches XML | Repo `{meta['repo_head']}` |")
    add("")

    add("## 3. Methode und Ehrlichkeitsgrenzen")
    add("")
    for note in meta["method_notes"]:
        add(f"- {note}")
    if bt:
        add("- Ebene (d): Jeder normative Satz des amtlichen Wortlauts wurde einzeln gegen den "
            "vollständigen GS++-Katalog beurteilt (großzügige Kandidatensuche je Anforderung, "
            "danach strenge Einzelprüfung jedes (Satz, Maßnahme)-Paars mit den Praktik-Nachbarn "
            "als Negativkontext). Ein Satz ohne verifizierte Maßnahme wurde also GESEHEN und "
            "trotzdem leer beurteilt — das ist ein inhaltliches Urteil, keine bloße Mapping-Lücke. "
            "Es bleibt ein LLM-Urteil im Status draft.")
    add("- Eine fehlende Zuordnung ist zunächst eine **Mapping-Lücke**, keine bewiesene "
        "inhaltliche Lücke von Grundschutz++: unser Mapping ist automatisiert erzeugt "
        "(status: draft), das BSI-Mapping deckt erklärtermaßen nur einen Ausschnitt ab. "
        "Wo aber *beide* unabhängigen Verfahren nichts finden, ist die Lücke ein starkes Signal.")
    add("")

    add("## 4. Ergebnisse auf Anforderungsebene")
    add("")
    ab = a["abgedeckt"]
    add("| | abgedeckt | ohne Zuordnung | Anteil ohne |")
    add("|---|---|---|---|")
    add(f"| Unser Mapping (3.046er) | {de(ab['ours'])} | {de(denom - ab['ours'])} | {pct(denom - ab['ours'], denom)} |")
    add(f"| BSI GSMap | {de(ab['itgs'])} | {de(denom - ab['itgs'])} | {pct(denom - ab['itgs'], denom)} |")
    add(f"| Prozessbaustein-Mapping | {de(ab['prozessbausteine'])} | {de(denom - ab['prozessbausteine'])} | "
        f"{pct(denom - ab['prozessbausteine'], denom)} |")
    add(f"| **mindestens eine Quelle** | **{de(ab['mindestens_eine_quelle'])}** | **{de(neither)}** | "
        f"**{pct(neither, denom)}** |")
    add("")
    ct = a["crosstab_ours_itgs"]
    add("Kreuztabelle unser Mapping × BSI GSMap (aktive Anforderungen):")
    add("")
    add("| | GSMap: ja | GSMap: nein |")
    add("|---|---|---|")
    add(f"| **Unser Mapping: ja** | {de(ct.get('both', 0))} | {de(ct.get('only_ours', 0))} |")
    add(f"| **Unser Mapping: nein** | {de(ct.get('only_itgs', 0))} | {de(ct.get('neither', 0))} |")
    add("")
    add("Nach Verbindlichkeit (Titel-Suffix im offiziellen XML):")
    add("")
    add("| Level | aktiv | ohne jede Zuordnung | ohne unser Mapping | ohne GSMap |")
    add("|---|---|---|---|---|")
    label = {"B": "Basis (B)", "S": "Standard (S)", "H": "erhöht (H)", "ohne": "ohne Level"}
    for lvl, slot in a["by_level"].items():
        add(f"| {label.get(lvl, lvl)} | {de(slot['aktiv'])} | {de(slot['ohne_jede_zuordnung'])} "
            f"({pct(slot['ohne_jede_zuordnung'], slot['aktiv'])}) | {de(slot['ohne_ours'])} | {de(slot['ohne_itgs'])} |")
    add("")
    add("Nach Schicht:")
    add("")
    add("| Schicht | aktiv | ohne jede Zuordnung | ohne unser Mapping | ohne GSMap |")
    add("|---|---|---|---|---|")
    for schicht, slot in a["by_schicht"].items():
        add(f"| {schicht} | {de(slot['aktiv'])} | {de(slot['ohne_jede_zuordnung'])} "
            f"({pct(slot['ohne_jede_zuordnung'], slot['aktiv'])}) | {de(slot['ohne_ours'])} | {de(slot['ohne_itgs'])} |")
    add("")
    add("Top-20-Bausteine nach Anforderungen ohne jede Zuordnung:")
    add("")
    add("| Baustein | aktiv | ohne jede Zuordnung |")
    add("|---|---|---|")
    for row in a["top_gap_bausteine"]:
        add(f"| {row['baustein']} | {de(row['aktiv'])} | {de(row['ohne_jede_zuordnung'])} "
            f"({pct(row['ohne_jede_zuordnung'], row['aktiv'])}) |")
    add("")
    if v:
        add("### 4.1 Auswirkung der strengen Prüfung (5.521 → 3.046)")
        add("")
        add(f"Vor der Maker-Checker-Verifikation deckte das Mapping {de(v['abgedeckt_alt'])} der "
            f"{de(denom)} aktiven Anforderungen ab, danach {de(v['abgedeckt_neu'])}. "
            f"{de(len(v['verloren']))} Anforderungen verloren ihre letzte Zuordnung, "
            f"{de(len(v['gewonnen']))} kamen neu hinzu. Genau diese Differenz ist der Preis der "
            "Präzision — die vollständigen ID-Listen stehen in `ed23_gap_analyse.json` unter "
            "`summary.vergleich_5521_vs_3046`.")
        add("")

    add("## 5. Ergebnisse auf Teilanforderungsebene")
    add("")
    to = t["ours"]
    add(f"**Unsere Zerlegung** (Satz-Indizes des stripped-Korpus, nur aktive offizielle "
        f"Anforderungen): {de(to['satz_universum_aktive_anforderungen'])} Sätze, davon "
        f"{de(to['referenziert'])} von mindestens einer Zuordnung referenziert und "
        f"{de(to['nicht_referenziert'])} ({pct(to['nicht_referenziert'], to['satz_universum_aktive_anforderungen'])}) "
        "ohne Referenz.")
    add("")
    ti = t["itgs"]
    add(f"**BSI GSMap (UA-Ebene):** {de(ti['ua_gemappt'])} Unteranforderungen gemappt. Das "
        f"UA-Universum ist unveröffentlicht; aus den maximal beobachteten Indizes ergibt sich "
        f"eine Untergrenze von {de(ti['ua_untergrenze_summe'])} UAs in den berührten "
        f"Anforderungen — darunter {de(ti['beweisbare_ua_luecken'])} beweisbar ungemappte "
        "(Index kleiner als ein gemappter Nachbar).")
    add("")
    tx = t["xml_normativ"]
    q = tx["qualitaet"]
    add(f"**Projektion auf den offiziellen Wortlaut:** Das XML enthält "
        f"{de(tx['denominator_normative_saetze'])} normative Sätze (MUSS/SOLLTE/DARF, "
        f"zzgl. {de(tx['kann_saetze'])} KANN-Sätze). Projiziert über das Satz-Alignment sind "
        f"{de(tx['abgedeckt_projiziert'])} davon ({pct(tx['abgedeckt_projiziert'], tx['denominator_normative_saetze'])}) "
        f"abgedeckt. Alignment-Qualität je Anforderung: {de(q.get('aligned', 0))}× aligned, "
        f"{de(q.get('teilweise', 0))}× teilweise, {de(q.get('grob', 0))}× grob (= Anforderungs-"
        "Abdeckung pauschal auf alle Sätze übertragen). Diese Ebene ist eine transparente "
        "Näherung — belastbar sind die Ebenen (a) und (b)"
        + (" sowie die beurteilte Abdeckung in 5.1." if bt else "."))
    add("")
    if bt:
        add("### 5.1 Beurteilte Satz-Abdeckung (amtlicher Wortlaut, je Teilanforderung)")
        add("")
        add(f"Jeder der {de(bt['denominator_normative_saetze'])} normativen Sätze der "
            f"{de(bt['anforderungen_beurteilt'])} beurteilten Anforderungen wurde einzeln gegen "
            f"den GS++-Katalog geprüft: **{de(bt['abgedeckt'])} abgedeckt "
            f"({pct(bt['abgedeckt'], bt['denominator_normative_saetze'])}), "
            f"{de(bt['nicht_abgedeckt'])} ohne jede GS++-Maßnahme "
            f"({pct(bt['nicht_abgedeckt'], bt['denominator_normative_saetze'])}).** "
            f"{de(len(bt['anforderungen_ohne_einzigen_abgedeckten_satz']))} Anforderungen haben "
            "keinen einzigen abgedeckten normativen Satz (Anhang B)."
            + (f" {de(bt['anforderungen_ohne_urteil'])} Anforderungen ohne Urteil."
               if bt["anforderungen_ohne_urteil"] else ""))
        add("")
        add("| Level | normative Sätze | abgedeckt | ohne Abdeckung |")
        add("|---|---|---|---|")
        for lvl, slot in bt["by_level"].items():
            miss = slot["normative_saetze"] - slot["abgedeckt"]
            add(f"| {label.get(lvl, lvl)} | {de(slot['normative_saetze'])} | {de(slot['abgedeckt'])} "
                f"({pct(slot['abgedeckt'], slot['normative_saetze'])}) | {de(miss)} |")
        add("")
        add("| Schicht | normative Sätze | abgedeckt | ohne Abdeckung |")
        add("|---|---|---|---|")
        for schicht, slot in bt["by_schicht"].items():
            miss = slot["normative_saetze"] - slot["abgedeckt"]
            add(f"| {schicht} | {de(slot['normative_saetze'])} | {de(slot['abgedeckt'])} "
                f"({pct(slot['abgedeckt'], slot['normative_saetze'])}) | {de(miss)} |")
        add("")
        add("Top-20-Bausteine nach unabgedeckten normativen Sätzen:")
        add("")
        add("| Baustein | normative Sätze | ohne Abdeckung |")
        add("|---|---|---|")
        for row in bt["top_gap_bausteine"]:
            miss = row["normative_saetze"] - row["abgedeckt"]
            add(f"| {row['baustein']} | {de(row['normative_saetze'])} | {de(miss)} "
                f"({pct(miss, row['normative_saetze'])}) |")
        add("")
        add(f"Quervergleich mit Ebene (a): {de(len(bt['gemappt_aber_satzlos']))} Anforderungen "
            "sind in unserem Mapping abgedeckt, überstehen die satzgenaue Prüfung aber mit null "
            f"Sätzen; umgekehrt findet die Satz-Beurteilung bei {de(len(bt['ungemappt_aber_satz_gefunden']))} "
            "Anforderungen Substanz, auf die kein einziges Mapping zeigt. Beide ID-Listen stehen "
            "im JSON unter `summary.teilanforderungen.beurteilt`.")
        add("")
    zv = t.get("zerlegungsvergleich")
    if zv:
        add(f"### 5.{'2' if bt else '1'} Deterministischer Zerlegungs-Vergleich der Teilanforderungs-Indizes")
        add("")
        nb = zv["anforderungen_in_beiden_mappings_mit_indizes"]
        add(f"Bei {de(nb)} Anforderungen tragen beide Mappings Teilanforderungs-Indizes "
            f"(unsere `statement-sentence` vs. BSI-`UA.n`). Mengenvergleich der Indizes: "
            f"{de(zv['indizes_identisch'])} identisch ({pct(zv['indizes_identisch'], nb)}), "
            f"{de(zv['indizes_ueberlappend'])} überlappend ({pct(zv['indizes_ueberlappend'], nb)}), "
            f"{de(zv['indizes_disjunkt'])} disjunkt ({pct(zv['indizes_disjunkt'], nb)}). "
            "Die beiden Nummerierungen zählen verschiedene Zerlegungen (NTT-Paraphrase-Sätze "
            "bzw. das unveröffentlichte UA-Schema des GSMap) — Index-Gleichheit ist ein "
            "Strukturindiz, keine bewiesene inhaltliche Übereinstimmung.")
        add("")
        add(f"Kardinalitäten-Abgleich gegen den amtlichen Wortlaut: Bei "
            f"{de(len(zv['ua_untergrenze_uebersteigt_normative_xml_saetze']))} Anforderungen "
            "übersteigt schon die UA-Untergrenze des GSMap die Zahl der normativen XML-Sätze "
            "(das BSI zerlegt dort feiner als die Modalverb-Satzzählung, oder zählt "
            "Kontextsätze mit). Unsere Paraphrase-Zerlegung trifft die amtliche Satzzahl bei "
            f"{de(zv['stripped_satzzahl_gleich_xml'])} von {de(zv['stripped_satzzahl_basis'])} "
            f"gemappten Anforderungen ({pct(zv['stripped_satzzahl_gleich_xml'], zv['stripped_satzzahl_basis'])}). "
            "Vollständige ID-Listen im JSON unter `summary.teilanforderungen.zerlegungsvergleich`.")
        add("")
    rel = t.get("relationen")
    if rel:
        itgs_hist = ", ".join(f"{k} {de(v)}" for k, v in rel["itgs"].items())
        if rel["ours_klassifiziert"]:
            ours_hist = ", ".join(f"{k} {de(v)}" for k, v in rel["ours"].items())
            add(f"**Relationstypen:** Unser Mapping: {ours_hist}. BSI GSMap: {itgs_hist}. "
                "Achtung Leserichtung: Unser Mapping beschreibt die GS++-Maßnahme relativ zur "
                "ED23-Anforderung, das GSMap die ED23-Unteranforderung relativ zur GS++-Maßnahme "
                "— subset-of und superset-of sind beim Vergleich zu spiegeln.")
            add("")
            total_rel = sum(rel["ours"].values())
            sup = rel["ours"].get("superset-of", 0)
            eq = rel["ours"].get("equal-to", 0)
            add(f"**Deutung (Befund, LLM-klassifiziert, Status draft):** {de(sup)} der "
                f"{de(total_rel)} Zuordnungen ({pct(sup, total_rel)}) sind superset-of: Wo "
                "Grundschutz++ eine ED23-Anforderung überhaupt abdeckt, deckt es sie "
                "überwiegend als die allgemeinere Fassung ab — das WAS der Anforderung "
                "überlebt, die technologiespezifische Ausprägung (das WIE) hat im Katalog "
                f"keinen eigenen Träger mehr. Wörtliche Übernahmen sind mit {de(eq)}× "
                "equal-to die absolute Ausnahme. Zusammen mit Abschnitt 4 (die Anforderungen "
                "ohne jede Zuordnung konzentrieren sich in den produktspezifischen SYS-, APP-, "
                "INF- und NET-Bausteinen, während die Prozess-Schichten vollständig abgedeckt "
                "sind) ergibt sich: Der Übergang auf Grundschutz++ generalisiert das "
                "Kompendiumswissen; die produktspezifischen Festlegungen der Edition 2023 "
                "sind im veröffentlichten GS++-Bestand ohne Nachfolger. Konzeptionell ist "
                "dieses Wissen in die Stand-der-Technik-Bibliothek verlagert; dort liegen "
                "derzeit WLAN, Mindeststandard-TLS, Lieferkettensicherheit und "
                "Risikomanagement — produktspezifische Inhalte im Umfang der 111 "
                "ED23-Bausteine existieren dort nicht.")
        else:
            add(f"**Relationstypen:** Das BSI GSMap differenziert ({itgs_hist}); unser Mapping "
                "trägt derzeit durchgehend `intersects-with` — die Relationsklassifikation "
                "(`stage_ed23_relationen`) ist noch nicht gelaufen.")
        add("")

    add("## 6. Gegenrichtung: GS++-Maßnahmen ohne ED23-Entsprechung")
    add("")
    fg = d["forward_gaps"]
    go = g["ohne_ed23_treffer"]
    add(f"| Quelle | GS++-Maßnahmen ohne Treffer (von {de(g['gpp_controls'])}) |")
    add("|---|---|")
    add(f"| Unser Mapping | {de(go['ours'])} |")
    add(f"| BSI GSMap | {de(go['itgs'])} |")
    add(f"| Prozessbaustein-Mapping | {de(go['prozessbausteine'])} |")
    add(f"| **in keiner der drei Quellen** | **{de(go['alle_drei'])}** |")
    add("")
    grouped = {}
    for cid in fg["ours"]:
        grouped.setdefault(cid.split(".", 1)[0], []).append(cid)
    parts = [f"{grp} {de(len(ids))}" for grp, ids in sorted(grouped.items())]
    add(f"Verteilung der {de(go['ours'])} Maßnahmen ohne Treffer in unserem Mapping nach "
        f"Praktik-Gruppe: {', '.join(parts)}. Vollständige Listen in `ed23_gap_analyse.json` "
        "unter `forward_gaps`.")
    add("")

    add("## 7. Kreuzbefunde zwischen den Quellen")
    add("")
    add(f"- Ziel-Klassen unseres Mappings: {json.dumps(k['ours_zielklassen'], ensure_ascii=False)}. "
        f"NTT-eigene (nicht-amtliche) Ziele: {de(len(k['ours_ziele_ntt_custom']))}, "
        f"Ziele auf ENTFALLENE Anforderungen: {de(len(k['ours_ziele_entfallen']))}, "
        f"dangling: {de(len(k['ours_ziele_dangling']))}.")
    add(f"- Quell-Klassen des BSI GSMap: {json.dumps(k['itgs_quellklassen'], ensure_ascii=False)}; "
        f"ENTFALLEN-gemappt: {de(len(k['itgs_quellen_entfallen']))}, dangling: {de(len(k['itgs_quellen_dangling']))}.")
    add(f"- Veraltete GS++-Ziel-IDs im BSI GSMap (existieren im gepinnten GS++-Katalog nicht): "
        f"{de(len(k['itgs_dangling_gpp_ziele']))} — {', '.join(k['itgs_dangling_gpp_ziele']) or 'keine'}.")
    add(f"- Prozessbaustein-Mapping: {de(len(k['prozess_dangling_quellen']))} dangling Quellen, "
        f"{de(len(k['prozess_ausserhalb_layer']))} außerhalb der Prozess-Schichten, "
        f"{de(len(k['prozess_dangling_gpp_ziele']))} dangling GS++-Ziele.")
    add(f"- satz_nr außerhalb des Satzbereichs: {de(len(k['satz_nr_ausser_bereich']))}; "
        f"Duplikate: {de(len(k['duplikate_ours']))} (unser Mapping) / {de(len(k['duplikate_itgs']))} (GSMap).")
    add(f"- Level-Widersprüche Titel vs. Abschnitt im XML: {de(len(k['level_mismatches']))}.")
    if bt:
        add(f"- Satz-Nummerierung Beurteilung vs. XML abweichend: "
            f"{de(len(k['satz_urteil_nummerierung_abweichend']))}"
            + (f" — {', '.join(k['satz_urteil_nummerierung_abweichend'][:10])}"
               if k["satz_urteil_nummerierung_abweichend"] else "")
            + ".")
    add(f"- Amtliche Anforderungen ohne Eintrag im stripped-Korpus: "
        f"{de(len(k['xml_anforderungen_ohne_stripped_eintrag']))}"
        + (f" — {', '.join(k['xml_anforderungen_ohne_stripped_eintrag'])}" if k["xml_anforderungen_ohne_stripped_eintrag"] else "")
        + ".")
    add(f"- NTT-eigene Bausteine im Korpus (nicht Teil des amtlichen Kompendiums): "
        f"{de(len(k['ntt_custom_bausteine']))} — {', '.join(k['ntt_custom_bausteine']) or 'keine'}.")
    zusatz = k["ntt_zusatz_anforderungen_in_amtlichen_bausteinen"]
    zusatz_by_b = Counter(rid.rsplit(".A", 1)[0] for rid in zusatz)
    zusatz_txt = ", ".join(f"{b} {c}" for b, c in sorted(zusatz_by_b.items()))
    add(f"- NTT-eigene Zusatz-Anforderungen innerhalb amtlicher Bausteine: {de(len(zusatz))}"
        + (f" ({zusatz_txt})" if zusatz else "") + ".")
    drift = d["anker"]["drift"]
    if drift:
        add(f"- **Anker-Drift** (dokumentierte Erwartungswerte nicht reproduziert): {'; '.join(drift)}.")
    else:
        add("- Alle dokumentierten Anker-Zahlen (Handbuch 10.3, Release Notes 4.0) wurden reproduziert.")
    add("")

    add("## 8. Reproduktion")
    add("")
    add("```bash")
    add("uv run Gpp-ai-tool/scripts/analyze_ed23_coverage.py --date " + meta["generated"])
    add("```")
    add("")
    add("Alle Fremdquellen sind commit- bzw. sha256-gepinnt (siehe Konstanten im Script und "
        "`meta.sources` im JSON); Downloads landen im gitignorierten Cache "
        "`Gpp-ai-tool/.cache/ed23_gap/`. Gleicher `--date`-Wert ⇒ byte-identische Ausgaben.")
    add("")
    if bt:
        add("Die Satz-Beurteilung (Abschnitt 5.1) stammt aus dem AI-Pipeline-Lauf "
            "`python src/main.py --stage stage_ed23_satz_abdeckung` (Gpp-ai-tool, benötigt "
            "Vertex-AI-Zugang); sie ist als LLM-Lauf nicht byte-reproduzierbar, ihr Ergebnis "
            "liegt versioniert in `hilfsdateien/ed23_satz_abdeckung.json`.")
        add("")

    add("## Anhang A: Aktive Anforderungen ohne jede Zuordnung")
    add("")
    add(f"{de(neither)} Anforderungen, gruppiert nach Baustein:")
    add("")
    by_b = {}
    for rid in a["ohne_jede_zuordnung_ids"]:
        by_b.setdefault(rid.rsplit(".A", 1)[0], []).append(rid)
    for baustein in sorted(by_b):
        ids = by_b[baustein]
        add(f"- **{baustein}** ({de(len(ids))}): {', '.join(ids)}")
    add("")
    if bt:
        add("## Anhang B: Anforderungen ohne einen einzigen beurteilt abgedeckten normativen Satz")
        add("")
        add(f"{de(len(bt['anforderungen_ohne_einzigen_abgedeckten_satz']))} Anforderungen, "
            "gruppiert nach Baustein:")
        add("")
        by_b2 = {}
        for rid in bt["anforderungen_ohne_einzigen_abgedeckten_satz"]:
            by_b2.setdefault(rid.rsplit(".A", 1)[0], []).append(rid)
        for baustein in sorted(by_b2):
            ids = by_b2[baustein]
            add(f"- **{baustein}** ({de(len(ids))}): {', '.join(ids)}")
        add("")
    return "\n".join(lines)


# --- main ----------------------------------------------------------------------------------

def main(argv=None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--offline", action="store_true",
                        help="nur Cache verwenden, nichts herunterladen")
    parser.add_argument("--cache-dir", default=DEFAULT_CACHE_DIR)
    parser.add_argument("--json", dest="json_out", default=DEFAULT_JSON_OUT)
    parser.add_argument("--report", dest="report_out", default=DEFAULT_REPORT_OUT)
    parser.add_argument("--date", default=date.today().isoformat(),
                        help="Datum im meta-Block (fixieren für byte-stabile Re-Runs)")
    parser.add_argument("--strict", action="store_true",
                        help="Anker-Drift ist fatal statt Warnung")
    parser.add_argument("--skip-vergleich", action="store_true",
                        help="Vorher/Nachher-Vergleich (5521er-Version) auslassen")
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    xml_bytes, xml_sha = fetch_official_xml(args.cache_dir, args.offline)
    itgs_bytes, itgs_sha = fetch_cached(
        ITGS_MAPPING_URL, f"ITGS-to-GSpp-mapping_collection@{ITGS_PIN_COMMIT[:12]}.json",
        ITGS_MAPPING_SHA256, args.cache_dir, args.offline,
    )
    gpp_bytes, gpp_sha = fetch_cached(
        GPP_KOMPENDIUM_JSON_PATH, f"gpp-resolved_catalog@{GPP_CATALOG_PIN_COMMIT[:12]}.json",
        GPP_CATALOG_PIN_SHA256, args.cache_dir, args.offline,
    )

    official, rejected_titles = load_official_xml(xml_bytes)
    ours = load_ours(open(OURS_PATH, "rb").read())
    itgs = load_itgs(itgs_bytes)
    stripped = load_stripped(STRIPPED_PATH)
    prozess = load_prozess(PROZESS_PATH)
    gpp_controls = load_gpp_controls(gpp_bytes)

    ours_old = None
    if not args.skip_vergleich:
        old_bytes = git_bytes(f"{OLD_MAPPING_GIT_REF}:hilfsdateien/gpp_ed23_anforderungen.json")
        if old_bytes:
            ours_old = load_ours(old_bytes)

    satz_urteil = load_satz_abdeckung(SATZ_ABDECKUNG_PATH)
    if satz_urteil is None:
        log("HINWEIS: hilfsdateien/ed23_satz_abdeckung.json fehlt — Stufe (d), die beurteilte "
            "Satz-Abdeckung, entfällt in diesem Lauf.")

    # Hard structural invariants — fail loud before publishing anything.
    bausteine = {r["baustein"] for r in official.values()}
    if len(bausteine) != EXPECTED_ANCHORS["official_bausteine"]:
        raise SystemExit(
            f"FEHLER: {len(bausteine)} Bausteine im offiziellen XML erkannt, erwartet "
            f"{EXPECTED_ANCHORS['official_bausteine']}. Parser oder Quelle prüfen."
        )
    empty = [r["id"] for r in official.values() if not r["entfallen"] and not r["saetze"]]
    if empty:
        raise SystemExit(f"FEHLER: aktive Anforderungen ohne Prosa/Sätze: {empty[:10]}")

    active_count = sum(1 for r in official.values() if not r["entfallen"])
    log(f"Offizielles XML: {len(bausteine)} Bausteine, {active_count} aktive + "
        f"{len(official) - active_count} entfallene Anforderungen.")
    log(f"Mappings: ours {len(ours)} | ITGS {len(itgs)} | Prozessbausteine {len(prozess)} | "
        f"GS++-Katalog {len(gpp_controls)} Maßnahmen.")

    source_meta = {
        "official_xml": {
            "url": BSI_XML_URL, "sha256": xml_sha, "bausteine": len(bausteine),
            "anforderungen_aktiv": active_count,
            "anforderungen_entfallen": len(official) - active_count,
        },
        "ours": {
            "path": "hilfsdateien/gpp_ed23_anforderungen.json",
            "maps": len(ours),
            "distinct_sources": len({e["source"] for e in ours}),
            "distinct_targets": len({e["target"] for e in ours}),
        },
        "ours_5521": (
            {"git_ref": OLD_MAPPING_GIT_REF, "maps": len(ours_old)} if ours_old else None
        ),
        "itgs": {
            "url": ITGS_MAPPING_URL, "sha256": itgs_sha, "maps": len(itgs),
            "distinct_teilanforderungen": len({e["ua_id"] for e in itgs}),
        },
        "prozessbausteine": {
            "path": "hilfsdateien/prozessbausteine_mapping.json", "entries": len(prozess),
        },
        "gpp_catalog": {
            "url": GPP_KOMPENDIUM_JSON_PATH, "sha256": gpp_sha, "controls": len(gpp_controls),
        },
        "stripped_corpus": {
            "path": "hilfsdateien/ed23_anforderungen_stripped.json",
            "entries": len(stripped),
            "entfallen": sum(1 for v in stripped.values() if v["entfallen"]),
        },
        "satz_abdeckung": (
            {
                "path": "hilfsdateien/ed23_satz_abdeckung.json",
                **{k: satz_urteil["meta"].get(k) for k in (
                    "generated", "maker_model", "checker_model",
                    "anforderungen", "zuordnungen",
                )},
            }
            if satz_urteil is not None else None
        ),
    }

    result = build_result(args, official, rejected_titles, ours, ours_old, itgs, prozess,
                          stripped, gpp_controls, source_meta, satz_urteil=satz_urteil)

    with open(args.json_out, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        f.write("\n")
    report = render_report(result)
    with open(args.report_out, "w", encoding="utf-8", newline="\n") as f:
        f.write(report)
    log(f"Geschrieben: {os.path.relpath(args.json_out, REPO_ROOT)} und "
        f"{os.path.relpath(args.report_out, REPO_ROOT)}")

    s = result["ed23_gap_analyse"]["summary"]["anforderungen"]
    log(
        f"Ergebnis: {s['denominator_aktiv']} aktive ED23-Anforderungen; ohne Zuordnung — "
        f"ours {s['ohne_zuordnung']['ours']}, ITGS {s['ohne_zuordnung']['itgs']}, "
        f"keine einzige Quelle {s['ohne_zuordnung']['keine_einzige_quelle']}."
    )
    bt = result["ed23_gap_analyse"]["summary"]["teilanforderungen"].get("beurteilt")
    if bt:
        log(
            f"Satz-Beurteilung: {bt['abgedeckt']}/{bt['denominator_normative_saetze']} normative "
            f"Saetze abgedeckt; {len(bt['anforderungen_ohne_einzigen_abgedeckten_satz'])} "
            "Anforderungen ohne einen einzigen abgedeckten Satz."
        )
    drift = result["ed23_gap_analyse"]["anker"]["drift"]
    for entry in drift:
        warn(f"Anker-Drift: {entry}")
    if drift and args.strict:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
