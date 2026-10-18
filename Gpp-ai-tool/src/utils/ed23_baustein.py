"""
Deterministic ED23-Baustein helpers shared by the abgleich, NG-catalog and profile stages.

Sources (all pinned, see constants):
* the benutzerdefinierte ED23 catalog (bd, 123 Bausteine) and the plain BSI file (111) —
  their Baustein-ID difference is the set of nutzergenerierte (NG) Bausteine, the only
  data-level marker there is;
* the official XML Kompendium for the amtliche wording of BSI Anforderungen (same sentence
  numbering as every mapping artifact);
* the existing mapping artifacts in hilfsdateien/ (G++ → ED23 collection, sentence coverage,
  1:1 process mapping) and the BSI GSMap.

Everything here is pure data shaping: no model, no I/O beyond the loaders at the top.
"""

import json
import logging
import re
from typing import Any, Dict, Iterable, List, Optional, Tuple

from constants import (
    BSI_2023_JSON_PATH,
    BSI_2023_PLAIN_JSON_PATH,
    ED23_BD_CATALOG_PIN_SHA256,
    ED23_PLAIN_CATALOG_PIN_SHA256,
)
from utils.data_loader import load_json_file
from utils.ed23_xml import KANN_RE, NORMATIVE_RE, parse_requirement_title
from utils.sentence_split import split_sentences
from utils.text_utils import sanitize_filename

logger = logging.getLogger(__name__)

LEVEL_CODE = {"1": "B", "3": "S", "5": "H"}
LEVEL_NUM = {"B": "1", "S": "3", "H": "5"}
LEVEL_TITLE = {
    "B": "Basis-Anforderungen",
    "S": "Standard-Anforderungen",
    "H": "Anforderungen bei erhöhtem Schutzbedarf",
}
LEVEL_ORDER = {"B": 0, "S": 1, "H": 2}

# BSI-Verbindlichkeitssprache: only fully upper-case modal verbs are normative.
MODAL_RE = re.compile(r"\b(DARF NICHT|DÜRFEN NICHT|DARF NUR|DÜRFEN NUR|MUSS|MÜSSEN|SOLLTE|SOLLTEN|KANN|KÖNNEN)\b")
_MODAL_CANON = {
    "DÜRFEN NICHT": "DARF NICHT", "DÜRFEN NUR": "DARF NUR",
    "MÜSSEN": "MUSS", "SOLLTEN": "SOLLTE", "KÖNNEN": "KANN",
}
MODAL_RANK = {"DARF NICHT": 4, "DARF NUR": 4, "MUSS": 3, "SOLLTE": 2, "KANN": 1}
PROCESS_PRACTICES = {"GC", "STM", "UMS", "VRB", "PERF", "RISK"}
ANF_ID_RE = re.compile(r"^[A-Z]{2,7}(?:\.\d+)+\.A\d+$")
UA_RE = re.compile(r"^(?P<req>.+?)-UA\.(?P<idx>\d+)$")


# ── loaders ───────────────────────────────────────────────────────────────────────────────
def load_ed23_catalogs() -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """Returns (benutzerdefinierte catalog, plain BSI catalog), both hash-checked (fail closed)."""
    bd = load_json_file(BSI_2023_JSON_PATH, expected_sha256=ED23_BD_CATALOG_PIN_SHA256)
    plain = load_json_file(BSI_2023_PLAIN_JSON_PATH, expected_sha256=ED23_PLAIN_CATALOG_PIN_SHA256)
    return bd, plain


def iter_bausteine(catalog: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Flattens layer → Baustein groups of an ED23 catalog into one list of Baustein dicts."""
    out = []
    for layer in (catalog.get("catalog", {}).get("groups", []) or []):
        for group in (layer.get("groups", []) or []):
            if group.get("class") != "baustein" and not group.get("controls"):
                continue
            out.append({
                "layer_id": str(layer.get("id", "")).upper(),
                "layer_title": _title_str(layer.get("title")),
                "id": group.get("id"),
                "title": _title_str(group.get("title")),
                "zielsetzung": baustein_zielsetzung(group),
                "parts": group.get("parts", []) or [],
                "controls": group.get("controls", []) or [],
            })
    return out


def baustein_ids(catalog: Dict[str, Any]) -> set:
    return {b["id"] for b in iter_bausteine(catalog) if b.get("id")}


def anforderung_ids(catalog: Dict[str, Any]) -> set:
    return {c.get("id") for b in iter_bausteine(catalog) for c in b["controls"] if c.get("id")}


def detect_ng(bd: Dict[str, Any], plain: Dict[str, Any]) -> Dict[str, set]:
    """NG = everything in the benutzerdefinierte catalog that the plain BSI file lacks.

    `bausteine`: whole NTT-own Bausteine; `anforderungen`: every control id absent from the
    plain file — the controls of those Bausteine plus any extra Anforderung NTT added inside
    an official Baustein (currently none, detected anyway).
    """
    ng_b = baustein_ids(bd) - baustein_ids(plain)
    ng_a = anforderung_ids(bd) - anforderung_ids(plain)
    return {"bausteine": ng_b, "anforderungen": ng_a}


def baustein_zielsetzung(group: Dict[str, Any]) -> str:
    """The Baustein's objective prose: part named Zielsetzung/objective, else Einleitung/introduction."""
    for keyword in ("zielsetzung", "objective", "usage", "einleitung", "introduction"):
        for part in group.get("parts", []) or []:
            name = (str(part.get("name") or "") + " " + str(part.get("title") or "")).lower()
            if keyword in name and part.get("prose"):
                return part["prose"]
    return ""


def bd_m3_statement(control: Dict[str, Any]) -> str:
    """The normative text of a bd-catalog control: nested `statement` of the m3 (defined) part."""
    for part in control.get("parts", []) or []:
        if part.get("class") == "maturity-level-defined" or str(part.get("id", "")).endswith("-m3"):
            for sub in part.get("parts", []) or []:
                if sub.get("name") == "statement" and sub.get("prose"):
                    return sub["prose"].strip()
    # Legacy/plain shape: a direct statement part.
    for part in control.get("parts", []) or []:
        if part.get("name") == "statement" and part.get("prose"):
            return part["prose"].strip()
    return ""


def bd_level(control: Dict[str, Any]) -> Optional[str]:
    for prop in control.get("props", []) or []:
        if prop.get("name") == "level":
            return str(prop.get("value", "")).strip() or None
    return None


# ── modal verbs, ordering, ids ────────────────────────────────────────────────────────────
def normalize_modal_verbs(text: str) -> List[str]:
    """Distinct canonical upper-case modal verbs in `text`, in order of first appearance."""
    seen: List[str] = []
    for m in MODAL_RE.finditer(text or ""):
        canon = _MODAL_CANON.get(m.group(1), m.group(1))
        if canon not in seen:
            seen.append(canon)
    return seen


def dominant_modal_verb(text_or_saetze) -> Optional[str]:
    """The strongest modal verb (DARF NICHT > MUSS > SOLLTE > KANN) or None without any."""
    text = " ".join(text_or_saetze) if isinstance(text_or_saetze, (list, tuple)) else (text_or_saetze or "")
    verbs = normalize_modal_verbs(text)
    return max(verbs, key=lambda v: MODAL_RANK.get(v, 0)) if verbs else None


def modal_weaker(new: Optional[str], reference: Optional[str]) -> bool:
    """True when `new` is a weaker modal verb than `reference` (KANN < SOLLTE < MUSS/DARF NICHT)."""
    if not new or not reference:
        return False
    return MODAL_RANK.get(new, 0) < MODAL_RANK.get(reference, 0)


def _id_parts(ident: str) -> List:
    return [int(p) if p.isdigit() else p for p in re.split(r"[.]", ident.replace(".A", ".A."))]


def anforderung_sort_key(anf_id: str) -> Tuple:
    """Numeric-aware ordering: SYS.1.1.A2 < SYS.1.1.A10, Bausteine by their numeric parts."""
    baustein, _, num = anf_id.rpartition(".A")
    try:
        n = int(num)
    except ValueError:
        n = 10 ** 6
    return (baustein_sort_key(baustein), n)


def baustein_sort_key(baustein_id: str) -> Tuple:
    parts = baustein_id.split(".")
    return (parts[0],) + tuple(int(p) if p.isdigit() else p for p in parts[1:])


def ng_control_id(anf_id: str) -> str:
    return f"NG-{anf_id}"


def ng_title(title: str) -> str:
    return f"NG: {title}"


def profile_file_stem(zielobjekt_name: str, baustein_id: str, baustein_title: str, is_ng: bool) -> str:
    """`<kategorie>_<ID>_<titel>` as today, prefixed `NG_` for nutzergenerierte Bausteine."""
    stem = f"{sanitize_filename(zielobjekt_name)}_{baustein_id}_{sanitize_filename(baustein_title)}"
    return f"NG_{stem}" if is_ng else stem


# ── Anforderung records ───────────────────────────────────────────────────────────────────
def build_anforderung_records(
    bd: Dict[str, Any], official: Dict[str, Dict[str, Any]], ng: Dict[str, set],
    bausteine: Optional[Iterable[str]] = None,
) -> Dict[str, Dict[str, Any]]:
    """One record per Anforderung of the selected Bausteine (default: all of the bd catalog).

    The Baustein's Anforderung list is the bd catalog's control list (the pinned source the
    SSP generators use). Wording: official XML sentences for BSI ids (amtlicher Wortlaut, the
    numbering every mapping uses), the bd m3 statement for NG ids and as a logged fallback.
    """
    wanted = set(bausteine) if bausteine is not None else None
    records: Dict[str, Dict[str, Any]] = {}
    for baustein in iter_bausteine(bd):
        bid = baustein["id"]
        if wanted is not None and bid not in wanted:
            continue
        baustein_is_ng = bid in ng["bausteine"]
        for control in baustein["controls"]:
            anf_id = control.get("id")
            if not anf_id:
                continue
            parsed = parse_requirement_title(f"{anf_id} {_title_str(control.get('title'))}")
            _, bd_titel, bd_level_letter, bd_rolle = parsed if parsed else (anf_id, _title_str(control.get("title")), None, None)
            level_num = bd_level(control)
            herkunft = "NG" if (baustein_is_ng or anf_id in ng["anforderungen"]) else "BSI"
            xml = official.get(anf_id) if herkunft == "BSI" else None
            if herkunft == "BSI" and xml is None:
                logger.warning(f"{anf_id}: nicht im amtlichen XML — Wortlaut aus dem bd-Katalog (m3).")
            if xml:
                saetze = list(xml.get("saetze") or [])
                normative_idx = list(xml.get("normative_idx") or [])
                kann_idx = list(xml.get("kann_idx") or [])
                titel = xml.get("titel") or bd_titel
                level = xml.get("level") or bd_level_letter or LEVEL_CODE.get(level_num or "", None)
                rolle = xml.get("rolle") or bd_rolle
                entfallen = bool(xml.get("entfallen"))
                text_quelle = "xml"
                if level_num and LEVEL_CODE.get(level_num) and level and LEVEL_CODE[level_num] != level:
                    logger.warning(f"{anf_id}: level im bd-Katalog ({level_num}) ≠ XML ({level}); XML gilt.")
            else:
                text = bd_m3_statement(control)
                saetze = split_sentences(text) if text else []
                normative_idx = [i for i, s in enumerate(saetze, 1) if NORMATIVE_RE.search(s)]
                kann_idx = [i for i, s in enumerate(saetze, 1) if KANN_RE.search(s) and i not in set(normative_idx)]
                titel = bd_titel
                level = bd_level_letter or LEVEL_CODE.get(level_num or "", None)
                rolle = bd_rolle
                entfallen = _title_str(control.get("title")).strip().upper().startswith("ENTFALLEN")
                text_quelle = "bd-m3"
            level = level if level in LEVEL_ORDER else None
            normative_text = " ".join(saetze[i - 1] for i in normative_idx if 0 < i <= len(saetze))
            records[anf_id] = {
                "id": anf_id,
                "baustein": bid,
                "layer": baustein["layer_id"],
                "titel": titel,
                "level": level,
                "level_num": level_num or (LEVEL_NUM.get(level) if level else None),
                "rolle": rolle,
                "herkunft": herkunft,
                "entfallen": entfallen,
                "text": " ".join(saetze),
                "saetze": saetze,
                "normative_idx": normative_idx,
                "kann_idx": kann_idx,
                "text_quelle": text_quelle,
                "modalverb": dominant_modal_verb(normative_text) or (dominant_modal_verb(saetze) if saetze else None),
                "kann_only": bool(kann_idx) and not normative_idx,
            }
    return records


# ── existing mapping artifacts as deterministic sources ───────────────────────────────────
def invert_mapping_collection(doc: Dict[str, Any]) -> Dict[str, List[Dict[str, Any]]]:
    """G++→ED23 mapping collection → {anforderung_id: [{control_id, relation, satz_nr[], begruendung, richtung}]}.

    One entry per (Anforderung, control), the first relation wins, the sentence numbers of all
    maps of that pair are collected.
    """
    inverted: Dict[str, Dict[str, Dict[str, Any]]] = {}
    for mapping in (doc.get("mapping-collection", {}).get("mappings", []) or []):
        for entry in (mapping.get("maps", []) or []):
            sources = [s.get("id-ref") for s in entry.get("sources", []) or [] if s.get("id-ref")]
            richtung = next((p.get("value") for p in entry.get("props", []) or []
                             if p.get("name") == "matching-direction"), None)
            for target in entry.get("targets", []) or []:
                tid = target.get("id-ref")
                if not tid:
                    continue
                satz = next((p.get("value") for p in target.get("props", []) or []
                             if p.get("name") == "statement-sentence"), None)
                try:
                    satz_nr = int(satz) if satz is not None else None
                except (TypeError, ValueError):
                    satz_nr = None
                for cid in sources:
                    slot = inverted.setdefault(tid, {}).setdefault(cid, {
                        "control_id": cid,
                        "relation": entry.get("relationship") or "intersects-with",
                        "satz_nr": [],
                        "begruendung": (entry.get("remarks") or "").strip(),
                        "richtung": richtung,
                    })
                    if satz_nr is not None and satz_nr not in slot["satz_nr"]:
                        slot["satz_nr"].append(satz_nr)
    return {aid: [slots[c] for c in sorted(slots)] for aid, slots in inverted.items()}


def load_satz_abdeckung(doc: Dict[str, Any]) -> Dict[str, List[Dict[str, Any]]]:
    """ed23_satz_abdeckung.json → {anforderung_id: [{control_id, satz_nr[], begruendung}]} (verified hits only)."""
    root = doc.get("ed23_satz_abdeckung", doc)
    out: Dict[str, List[Dict[str, Any]]] = {}
    for aid, rec in (root.get("anforderungen", {}) or {}).items():
        slots: Dict[str, Dict[str, Any]] = {}
        for hit in rec.get("treffer", []) or []:
            cid = hit.get("control_id")
            if not cid:
                continue
            slot = slots.setdefault(cid, {"control_id": cid, "satz_nr": [], "begruendung": ""})
            if isinstance(hit.get("satz_nr"), int) and hit["satz_nr"] not in slot["satz_nr"]:
                slot["satz_nr"].append(hit["satz_nr"])
            if not slot["begruendung"] and hit.get("begruendung"):
                slot["begruendung"] = hit["begruendung"].strip()
        if slots:
            out[aid] = [slots[c] for c in sorted(slots)]
    return out


def load_prozess_mapping(doc: Dict[str, Any]) -> Dict[str, str]:
    """prozessbausteine_mapping.json → {anforderung_id: control_id}."""
    return dict((doc or {}).get("prozessbausteine_mapping", {}) or {})


def load_gsmap_by_anforderung(raw: bytes) -> Dict[str, List[Dict[str, Any]]]:
    """BSI GSMap (ITGS-UA → GS++) → {anforderung_id: [{control_id, relation, ua_idx[]}]}.

    UA-level sources (`APP.3.6.A1-UA.2`) collapse to their Anforderung; targets are G++ ids
    (17 of them are stale against the current pin and are dropped by the caller's id check).
    """
    doc = json.loads(raw)
    out: Dict[str, Dict[str, Dict[str, Any]]] = {}
    for mapping in (doc.get("mapping-collection", {}).get("mappings", []) or []):
        for entry in (mapping.get("maps", []) or []):
            sources = [s.get("id-ref") for s in entry.get("sources", []) or [] if s.get("id-ref")]
            targets = [t.get("id-ref") for t in entry.get("targets", []) or [] if t.get("id-ref")]
            for source in sources:
                ua = UA_RE.match(source)
                req = ua.group("req") if ua else source
                idx = int(ua.group("idx")) if ua else None
                for cid in targets:
                    slot = out.setdefault(req, {}).setdefault(cid, {
                        "control_id": cid,
                        "relation": entry.get("relationship") or "intersects-with",
                        "ua_idx": [],
                    })
                    if idx is not None and idx not in slot["ua_idx"]:
                        slot["ua_idx"].append(idx)
    return {aid: [slots[c] for c in sorted(slots)] for aid, slots in out.items()}


def _title_str(value: Any) -> str:
    if isinstance(value, list):
        return str(value[0]) if value else ""
    return str(value or "")
