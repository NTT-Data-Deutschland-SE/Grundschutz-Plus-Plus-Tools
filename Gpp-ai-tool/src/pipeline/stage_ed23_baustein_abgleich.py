"""
Pipeline Stage: per-Anforderung assignment of every Baustein that gets an ED23 profile.

For each Anforderung of each Baustein in hilfsdateien/baustein_zielobjekt.json this stage
decides which G++ controls of the Anwenderkatalog carry it and, where none does, proposes a
new NG control ("Nutzergenerierte Inhalte") for the shared NG Ergänzungskatalog.

Deterministic first, model on the residual:

* Deterministic sources (recomputed on every run, cheap): the inverted G++ → ED23 mapping
  collection (gpp_ed23_anforderungen.json), the verified sentence coverage
  (ed23_satz_abdeckung.json), the BSI GSMap (ITGS → GS++, pinned, optional) and the 1:1
  process mapping (prozessbausteine_mapping.json).
* Gate: an Anforderung counts as covered only with a source from the first three. A hit from
  the 1:1 process mapping ALONE does not — that mapping is completeness-driven and forces one
  control per Anforderung — so the Anforderung still goes to the model (the 1:1 assignment
  is kept as provenance). ENTFALLEN Anforderungen are never sent.
* Maker (MAKER_THINKING_LEVEL): batches of Anforderungen of ONE Baustein, the full G++ corpus
  as the stable prompt prefix (implicit caching), returns classification, assignments and at
  most one proposed new control per Anforderung. Deterministic post-checks drop unknown ids,
  invert the relation into OSCAL direction (control relative to Anforderung), and reject new
  controls that violate the rules (existing assignment, KANN-only, hinweis/verweis, modal
  verb count/weakening, unknown practice).
* Checker (CHECKER_THINKING_LEVEL): one self-contained call per Anforderung with a proposal.
  Maker output is immutable; the verdict is stored beside it. `abgelehnt` removes an
  assignment or the new control; `fraglich`/`unsicher` stay with the verdict visible.

Output: hilfsdateien/ed23_baustein_abgleich.json (see `_serialize`). Resume: a `.partial`
checkpoint next to it holds finished `ki` blocks and maker results awaiting the checker;
finished `ki` blocks of a published output are reused unless OVERWRITE_TEMP_FILES/--fresh.
"""

import asyncio
import datetime
import json
import logging
import os
from typing import Any, Dict, List, Optional, Tuple

from config import app_config
from clients.ai_client import AiClient
from utils.data_loader import load_json_file, load_zielobjekte_csv, save_json_file, zielobjekt_row_name
from utils.ed23_xml import fetch_cached, fetch_official_xml, load_official_xml, ED23_CACHE_DIR
from utils.file_utils import read_json_file
from utils.oscal_utils import normalize_id
from utils.ed23_baustein import (
    PROCESS_PRACTICES,
    anforderung_sort_key,
    build_anforderung_records,
    detect_ng,
    dominant_modal_verb,
    invert_mapping_collection,
    iter_bausteine,
    load_ed23_catalogs,
    load_gsmap_by_anforderung,
    load_prozess_mapping,
    load_satz_abdeckung,
    modal_weaker,
    ng_control_id,
    normalize_modal_verbs,
)
from pipeline.stage_ed23_anforderungen import _atomic_save_json, build_gpp_match_contexts
from pipeline.stage_prozessbausteine import build_gpp_corpus
from constants import (
    BAUSTEIN_ZIELOBJEKT_JSON_PATH,
    ED23_BAUSTEIN_ABGLEICH_BATCH_SIZE,
    ED23_BAUSTEIN_ABGLEICH_CHECKER_SCHEMA_PATH,
    ED23_BAUSTEIN_ABGLEICH_JSON_PATH,
    ED23_BAUSTEIN_ABGLEICH_MAKER_SCHEMA_PATH,
    ED23_CATALOG_PIN_COMMIT,
    ED23_BD_CATALOG_PIN_SHA256,
    ED23_SATZ_ABDECKUNG_JSON_PATH,
    GPP_CATALOG_PIN_COMMIT,
    GPP_CATALOG_PIN_SHA256,
    GPP_ED23_ANFORDERUNGEN_JSON_PATH,
    GPP_KOMPENDIUM_JSON_PATH,
    ITGS_MAPPING_PIN_SHA256,
    ITGS_MAPPING_URL,
    PRACTICE_ABBREVIATIONS,
    PROMPT_CONFIG_PATH,
    PROZZESSBAUSTEINE_CONTROLS_JSON_PATH,
    ZIELOBJEKTKATEGORIEN_CSV_PATH,
)

logger = logging.getLogger(__name__)

OUTPUT_KEY = "ed23_baustein_abgleich"
CHECKPOINT_PATH = ED23_BAUSTEIN_ABGLEICH_JSON_PATH + ".partial"
CHECKPOINT_DONE = "done"
CHECKPOINT_KANDIDATEN = "kandidaten"
COVERING_SOURCES = ("gpp_ed23_anforderungen", "satz_abdeckung", "gsmap")
MAX_ROUNDS = 3
_LEVEL_LABEL = {"B": "Basis-Anforderung", "S": "Standard-Anforderung", "H": "Anforderung bei erhöhtem Schutzbedarf"}
_INVERT_RELATION = {"subset-of": "superset-of", "superset-of": "subset-of"}


# ── deterministic assignment ──────────────────────────────────────────────────────────────
def assign_deterministic(
    anf_id: str,
    inverted: Dict[str, List[Dict[str, Any]]],
    satz: Dict[str, List[Dict[str, Any]]],
    prozess: Dict[str, str],
    gsmap: Dict[str, List[Dict[str, Any]]],
    gpp_lookup: Dict[str, str],
) -> List[Dict[str, Any]]:
    """All assignments the existing artifacts give for one Anforderung, one entry per control.

    Precedence of the recorded source when several agree: the mapping collection (has a
    relation and a Begründung), then the sentence coverage, then GSMap, then the 1:1
    process mapping. Unknown control ids (stale against the current pin) are dropped.
    """
    out: Dict[str, Dict[str, Any]] = {}

    def add(cid_raw: str, quelle: str, relation: str, satz_nr: List[int], begruendung: str):
        cid = gpp_lookup.get(normalize_id(cid_raw))
        if not cid:
            logger.debug(f"{anf_id}: dropping unknown G++ id {cid_raw!r} from {quelle}.")
            return
        slot = out.get(cid)
        if slot is None:
            out[cid] = {
                "control_id": cid, "quelle": quelle, "quellen": [quelle], "relation": relation,
                "satz_nr": sorted(set(satz_nr)), "begruendung": begruendung,
                "konfidenz": None, "checker": None, "checker_begruendung": None,
            }
            return
        if quelle not in slot["quellen"]:
            slot["quellen"].append(quelle)
        slot["satz_nr"] = sorted(set(slot["satz_nr"]) | set(satz_nr))
        if not slot["begruendung"] and begruendung:
            slot["begruendung"] = begruendung

    for e in inverted.get(anf_id, []):
        add(e["control_id"], "gpp_ed23_anforderungen", e.get("relation") or "intersects-with",
            e.get("satz_nr") or [], e.get("begruendung") or "")
    for e in satz.get(anf_id, []):
        add(e["control_id"], "satz_abdeckung", "intersects-with", e.get("satz_nr") or [], e.get("begruendung") or "")
    for e in gsmap.get(anf_id, []):
        add(e["control_id"], "gsmap", e.get("relation") or "intersects-with", [], "")
    if anf_id in prozess:
        add(prozess[anf_id], "prozessbausteine_mapping", "intersects-with", [], "")
    return [out[c] for c in sorted(out)]


def needs_model(record: Dict[str, Any], zuordnungen: List[Dict[str, Any]]) -> bool:
    """The gate: not ENTFALLEN and no covering source (the 1:1 process mapping alone is none)."""
    if record.get("entfallen"):
        return False
    return not any(q in COVERING_SOURCES for z in zuordnungen for q in z.get("quellen", [z.get("quelle")]))


# ── prompt rendering ──────────────────────────────────────────────────────────────────────
def render_anforderung_block(record: Dict[str, Any]) -> str:
    head = f"### {record['id']} {record['titel']}"
    if record.get("level"):
        head += f" ({record['level']})"
    if record.get("rolle"):
        head += f" [{record['rolle']}]"
    head += f" – Modalverb {record.get('modalverb') or 'keines'}"
    normative = set(record.get("normative_idx") or [])
    lines = [head]
    for i, s in enumerate(record.get("saetze") or [], start=1):
        lines.append(f"(S{i}){' [normativ]' if i in normative else ''} {s}")
    if not record.get("saetze"):
        lines.append("(kein Text)")
    return "\n".join(lines)


def herkunft_satz(record: Dict[str, Any]) -> str:
    return ("nutzergenerierter Baustein (NG, NTT DATA), kein amtlicher BSI-Text"
            if record.get("herkunft") == "NG" else "amtlicher Baustein des BSI")


def _praktiken_block() -> str:
    return "\n".join(f"{k} · {v}" for k, v in PRACTICE_ABBREVIATIONS.items() if k != "METHODIK")


# ── maker post-checks ─────────────────────────────────────────────────────────────────────
def filter_maker_result(
    item: Dict[str, Any],
    record: Dict[str, Any],
    gpp_lookup: Dict[str, str],
    praktik_ids: set,
    kategorie_names: set,
) -> Dict[str, Any]:
    """Deterministic post-checks of one maker result; returns the cleaned result plus `verworfen`.

    Relations are inverted into OSCAL direction (control relative to Anforderung) here, so the
    whole file speaks one language.
    """
    verworfen: List[str] = []
    pruefung = dict(item.get("pruefung") or {})
    zuordnungen: List[Dict[str, Any]] = []
    seen = set()
    for z in item.get("zuordnungen") or []:
        cid = gpp_lookup.get(normalize_id(str(z.get("control_id", ""))))
        if not cid:
            verworfen.append(f"Zuordnung {z.get('control_id')!r}: ID nicht im Anwenderkatalog")
            continue
        if cid in seen:
            continue
        seen.add(cid)
        rel = z.get("relation") or "intersects-with"
        zuordnungen.append({
            "control_id": cid, "quelle": "ki", "quellen": ["ki"],
            "relation": _INVERT_RELATION.get(rel, rel),
            "satz_nr": [], "begruendung": (z.get("begruendung") or "").strip(),
            "konfidenz": z.get("konfidenz"), "checker": None, "checker_begruendung": None,
        })

    neu = item.get("neues_control")
    neues_control: Optional[Dict[str, Any]] = None
    if neu:
        reasons = []
        if zuordnungen:
            reasons.append("Zuordnung vorhanden (Ergänzung statt neues Control)")
        if pruefung.get("control_noetig") is False:
            reasons.append("control_noetig=false")
        if pruefung.get("art") in ("hinweis", "verweis"):
            reasons.append(f"art={pruefung.get('art')}")
        if record.get("kann_only"):
            reasons.append("reine KANN-Anforderung")
        statement = (neu.get("statement") or "").strip()
        verbs = normalize_modal_verbs(statement)
        if len(verbs) != 1:
            reasons.append(f"Statement hat {len(verbs)} Modalverben statt genau eines")
        elif modal_weaker(verbs[0], record.get("modalverb")):
            reasons.append(f"Modalverb {verbs[0]} schwächer als {record.get('modalverb')} der Anforderung")
        praktik = str(neu.get("praktik") or "").strip().upper()
        if praktik not in praktik_ids:
            reasons.append(f"unbekannte Praktik {praktik!r}")
        if reasons:
            verworfen.append("neues Control verworfen: " + "; ".join(reasons))
        else:
            kategorien = [k for k in (neu.get("zielobjektkategorien") or []) if k in kategorie_names]
            dropped = [k for k in (neu.get("zielobjektkategorien") or []) if k not in kategorie_names]
            if dropped:
                verworfen.append(f"Zielobjektkategorien nicht im Vokabular: {dropped}")
            hinweis = ""
            if not kategorien and praktik not in PROCESS_PRACTICES:
                hinweis = "keine Zielobjektkategorie bei fachlicher Praktik"
            verwandte = []
            for v in (neu.get("verwandte_controls") or [])[:6]:
                cid = gpp_lookup.get(normalize_id(str(v)))
                if cid and cid not in verwandte:
                    verwandte.append(cid)
            neues_control = {
                "id": ng_control_id(record["id"]),
                "titel": (neu.get("titel") or "").strip(),
                "statement": statement,
                "guidance": (neu.get("guidance") or "").strip(),
                "modalverb": verbs[0],
                "praktik": praktik,
                "zielobjektkategorien": kategorien,
                "verwandte_controls": verwandte[:3],
                "konfidenz": None,
                "checker": None,
                "checker_begruendung": None,
                "hinweis": hinweis,
            }

    ohne_control = None
    if not zuordnungen and not neues_control:
        ohne_control = {
            "art": pruefung.get("art") or "unbestimmt",
            "begruendung": (pruefung.get("hinweis") or item.get("offen") or "").strip(),
        }
    return {
        "pruefung": {
            "art": pruefung.get("art"), "modalverb": pruefung.get("modalverb"),
            "control_noetig": pruefung.get("control_noetig"), "hinweis": (pruefung.get("hinweis") or "").strip(),
        },
        "zuordnungen": zuordnungen,
        "neues_control": neues_control,
        "ohne_control": ohne_control,
        "offen": (item.get("offen") or "").strip(),
        "verworfen": verworfen,
    }


def apply_checker_verdict(result: Dict[str, Any], verdict: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    """Records the checker's verdicts; removes rejected assignments / new control. Never rewrites."""
    if not isinstance(verdict, dict):
        for z in result["zuordnungen"]:
            z["checker"] = "nicht geprüft"
        if result.get("neues_control"):
            result["neues_control"]["checker"] = "nicht geprüft"
        return result
    urteile = {u.get("control_id"): u for u in verdict.get("urteile") or [] if isinstance(u, dict)}
    kept = []
    for z in result["zuordnungen"]:
        u = urteile.get(z["control_id"])
        z["checker"] = (u or {}).get("urteil") or "unsicher"
        z["checker_begruendung"] = ((u or {}).get("begruendung") or "").strip() or None
        if z["checker"] == "abgelehnt":
            result["verworfen"].append(f"Zuordnung {z['control_id']} vom Checker abgelehnt: {z['checker_begruendung'] or ''}")
        else:
            kept.append(z)
    result["zuordnungen"] = kept
    nc = result.get("neues_control")
    if nc:
        u = verdict.get("neues_control") or {}
        nc["checker"] = u.get("urteil") or "unsicher"
        nc["checker_begruendung"] = (u.get("begruendung") or "").strip() or None
        if nc["checker"] == "abgelehnt":
            result["verworfen"].append(f"neues Control vom Checker abgelehnt: {nc['checker_begruendung'] or ''}")
            result["neues_control"] = None
    if not result["zuordnungen"] and not result.get("neues_control") and not result.get("ohne_control"):
        result["ohne_control"] = {"art": "abgelehnt-durch-checker", "begruendung": (verdict.get("gesamt") or "").strip()}
    result["gesamt"] = (verdict.get("gesamt") or "").strip()
    return result


# ── model calls ───────────────────────────────────────────────────────────────────────────
async def _maker_batch(
    ai_client: AiClient, batch: List[Dict[str, Any]], baustein: Dict[str, Any], zielobjekt_name: str,
    prefix: str, template: str, system_instruction: str, schema: Dict[str, Any],
    praktiken_block: str, kategorien_block: str, semaphore: asyncio.Semaphore,
) -> Dict[str, Any]:
    """One maker call for a batch of Anforderungen of one Baustein; returns raw items by id."""
    user_prompt = template.format(
        praktiken=praktiken_block,
        zielobjektkategorien=kategorien_block,
        baustein_id=baustein["id"],
        baustein_titel=baustein["title"],
        herkunft_satz=herkunft_satz(batch[0]),
        zielsetzung=(baustein.get("zielsetzung") or "(keine)")[:2000],
        zielobjektkategorie=zielobjekt_name or "(keine)",
        n=len(batch),
        anforderungen="\n\n".join(render_anforderung_block(r) for r in batch),
    )
    prompt = f"{prefix}\n\n{user_prompt}"
    label = f"ED23Baustein-{batch[0]['id']}..{batch[-1]['id']}"
    async with semaphore:
        try:
            response = await ai_client.generate_validated_json_response(
                prompt=prompt, json_schema=schema, request_context_log=label,
                thinking=app_config.maker_thinking_level, system_instruction=system_instruction,
            )
        except Exception as e:  # noqa: BLE001 — logged with reason; the batch is retried next round
            logger.warning(f"Maker call failed for {label}: {e}")
            return {}
    requested = {r["id"] for r in batch}
    out: Dict[str, Any] = {}
    for item in (response or {}).get("ergebnisse") or []:
        aid = str(item.get("anforderung_id", "")).strip()
        if aid in requested and aid not in out:
            out[aid] = item
        elif aid not in requested:
            logger.warning(f"{label}: result for unknown Anforderung {aid!r} ignored.")
    return out


async def _checker(
    ai_client: AiClient, record: Dict[str, Any], baustein: Dict[str, Any], result: Dict[str, Any],
    contexts: Dict[str, Dict[str, str]], template: str, schema: Dict[str, Any], semaphore: asyncio.Semaphore,
) -> Optional[Dict[str, Any]]:
    vorschlag = {
        "pruefung": result["pruefung"],
        "zuordnungen": [{"control_id": z["control_id"], "relation": z["relation"], "konfidenz": z["konfidenz"],
                         "begruendung": z["begruendung"]} for z in result["zuordnungen"]],
    }
    if result.get("neues_control"):
        nc = result["neues_control"]
        vorschlag["neues_control"] = {k: nc[k] for k in ("titel", "statement", "guidance", "praktik",
                                                         "zielobjektkategorien", "verwandte_controls")}
    controls = []
    for z in result["zuordnungen"]:
        c = contexts.get(z["control_id"], {})
        controls.append(f"{z['control_id']} | {c.get('title', '')} | {c.get('praktik', '')}\n"
                        f"Statement: {c.get('prose', '')}\nGuidance: {c.get('guidance') or '(keine)'}")
    prompt = template.format(
        baustein_id=baustein["id"], baustein_titel=baustein["title"], herkunft_satz=herkunft_satz(record),
        anforderung=render_anforderung_block(record),
        vorschlag=json.dumps(vorschlag, ensure_ascii=False, indent=1),
        controls="\n\n".join(controls) or "(keine Zuordnung vorgeschlagen)",
    )
    async with semaphore:
        try:
            return await ai_client.generate_validated_json_response(
                prompt=prompt, json_schema=schema, request_context_log=f"ED23BausteinCheck-{record['id']}",
                thinking=app_config.checker_thinking_level,
            )
        except Exception as e:  # noqa: BLE001 — recorded as "nicht geprüft" on the result
            logger.warning(f"Checker call failed for {record['id']}: {e}")
            return None


# ── checkpoint / output ───────────────────────────────────────────────────────────────────
def _load_checkpoint(path: str) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    if not os.path.exists(path):
        return {}, {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        done, kand = data.get(CHECKPOINT_DONE, {}), data.get(CHECKPOINT_KANDIDATEN, {})
        logger.info(f"Resuming from checkpoint '{path}': {len(done)} done, {len(kand)} awaiting the checker.")
        return done, kand
    except Exception as e:  # noqa: BLE001 — a corrupt checkpoint is discarded, with the reason logged
        logger.warning(f"Could not read checkpoint '{path}' ({e}); starting fresh.")
        return {}, {}


def _load_published_ki(path: str) -> Dict[str, Any]:
    """`ki` blocks of a previously published output (reused unless --fresh)."""
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        anf = (data.get(OUTPUT_KEY) or {}).get("anforderungen") or {}
        return {aid: rec["ki"] for aid, rec in anf.items() if rec.get("ki")}
    except Exception as e:  # noqa: BLE001
        logger.warning(f"Could not read existing output '{path}' ({e}); ignoring it.")
        return {}


def _revalidate_ki(ki: Dict[str, Any], gpp_lookup: Dict[str, str]) -> Optional[Dict[str, Any]]:
    """Drops a stored ki block whose control ids no longer exist in the current catalog."""
    for z in ki.get("zuordnungen") or []:
        if normalize_id(z.get("control_id", "")) not in gpp_lookup:
            return None
    nc = ki.get("neues_control") or {}
    for v in nc.get("verwandte_controls") or []:
        if normalize_id(v) not in gpp_lookup:
            return None
    return ki


def _serialize(records, det_by_id, ki_by_id, meta) -> Dict[str, Any]:
    anforderungen = {}
    for aid in sorted(records, key=anforderung_sort_key):
        r = records[aid]
        ki = ki_by_id.get(aid)
        zuordnungen = list(det_by_id.get(aid, []))
        if ki:
            known = {z["control_id"] for z in zuordnungen}
            zuordnungen += [z for z in ki.get("zuordnungen", []) if z["control_id"] not in known]
        anforderungen[aid] = {
            "baustein": r["baustein"], "titel": r["titel"], "level": r["level"], "level_num": r["level_num"],
            "rolle": r["rolle"], "herkunft": r["herkunft"], "entfallen": r["entfallen"],
            "text_quelle": r["text_quelle"], "modalverb": r["modalverb"], "kann_only": r["kann_only"],
            "zuordnungen": zuordnungen,
            "pruefung": (ki or {}).get("pruefung"),
            "neues_control": (ki or {}).get("neues_control"),
            "ohne_control": (ki or {}).get("ohne_control") if ki else (
                None if (zuordnungen or r["entfallen"]) else {"art": "unbeantwortet", "begruendung": ""}),
            "ki": ({k: ki[k] for k in ("maker", "checker", "stand", "verworfen", "offen", "gesamt") if k in ki}
                   if ki else None),
        }
    return {OUTPUT_KEY: {"meta": meta, "anforderungen": anforderungen}}


# ── stage ─────────────────────────────────────────────────────────────────────────────────
async def run_stage_ed23_baustein_abgleich() -> None:
    logger.info("Starting stage_ed23_baustein_abgleich...")

    baustein_map = read_json_file(BAUSTEIN_ZIELOBJEKT_JSON_PATH) or {}
    baustein_ids = sorted((baustein_map.get("baustein_zielobjekt_map") or {}).keys())
    if not baustein_ids:
        raise RuntimeError("baustein_zielobjekt.json is empty — run stage_match_bausteine first.")
    zo_rows = load_zielobjekte_csv(ZIELOBJEKTKATEGORIEN_CSV_PATH)
    zo_names = {row["UUID"].strip(): zielobjekt_row_name(row) for row in zo_rows if "UUID" in row}
    kategorie_names = {zielobjekt_row_name(row) for row in zo_rows if zielobjekt_row_name(row)}

    bd, plain = load_ed23_catalogs()
    ng = detect_ng(bd, plain)
    bausteine = {b["id"]: b for b in iter_bausteine(bd)}
    xml_bytes, xml_sha = fetch_official_xml()
    official, _ = load_official_xml(xml_bytes)
    records = build_anforderung_records(bd, official, ng, bausteine=baustein_ids)
    missing_b = [b for b in baustein_ids if b not in bausteine]
    if missing_b:
        logger.warning(f"Bausteine in the map but not in the catalog (skipped): {missing_b}")

    gpp_catalog = load_json_file(GPP_KOMPENDIUM_JSON_PATH, expected_sha256=GPP_CATALOG_PIN_SHA256)
    corpus_text, gpp_lookup = build_gpp_corpus(gpp_catalog)
    contexts = build_gpp_match_contexts(gpp_catalog)

    inverted = invert_mapping_collection(read_json_file(GPP_ED23_ANFORDERUNGEN_JSON_PATH) or {})
    satz = load_satz_abdeckung(read_json_file(ED23_SATZ_ABDECKUNG_JSON_PATH) or {})
    prozess = load_prozess_mapping(read_json_file(PROZZESSBAUSTEINE_CONTROLS_JSON_PATH) or {})
    try:
        raw_gsmap, _ = fetch_cached(ITGS_MAPPING_URL, "ITGS-to-GSpp-mapping_collection.json",
                                    ITGS_MAPPING_PIN_SHA256, ED23_CACHE_DIR)
        gsmap = load_gsmap_by_anforderung(raw_gsmap)
    except Exception as e:  # noqa: BLE001 — GSMap is an optional source; the run continues without it
        logger.warning(f"BSI GSMap unavailable ({e}); continuing without it.")
        gsmap = {}

    det_by_id = {aid: assign_deterministic(aid, inverted, satz, prozess, gsmap, gpp_lookup) for aid in records}
    pending_ids = [aid for aid, r in records.items() if needs_model(r, det_by_id[aid])]
    logger.info(
        f"{len(records)} Anforderungen in {len(baustein_ids)} Bausteinen: "
        f"{len(records) - len(pending_ids)} resolved deterministically or ENTFALLEN, "
        f"{len(pending_ids)} go to the model."
    )

    # Resume state: published ki blocks (unless --fresh) + checkpoint.
    ki_by_id: Dict[str, Any] = {}
    if not app_config.overwrite_temp_files:
        for aid, ki in _load_published_ki(ED23_BAUSTEIN_ABGLEICH_JSON_PATH).items():
            if aid in records and _revalidate_ki(ki, gpp_lookup):
                ki_by_id[aid] = ki
    done_cp, kandidaten = _load_checkpoint(CHECKPOINT_PATH)
    for aid, ki in done_cp.items():
        if aid in records and _revalidate_ki(ki, gpp_lookup):
            ki_by_id[aid] = ki
    todo = [aid for aid in pending_ids if aid not in ki_by_id]
    logger.info(f"resume: {len(pending_ids) - len(todo)} ok (reused), {len(todo)} pending model work.")
    if app_config.is_test_mode:
        todo = todo[:3]
        logger.info("TEST mode: limiting to the first 3 pending Anforderungen; output is not published.")

    stand = datetime.date.today().isoformat()
    meta = {
        "version": stand, "gpp_pin": GPP_CATALOG_PIN_COMMIT, "ed23_pin": ED23_CATALOG_PIN_COMMIT,
        "ed23_bd_sha256": ED23_BD_CATALOG_PIN_SHA256, "xml_sha256": xml_sha,
        "model": app_config.gemini_model, "maker_thinking": app_config.maker_thinking_level,
        "checker_thinking": app_config.checker_thinking_level,
        "ng_bausteine": sorted(ng["bausteine"]), "bausteine": baustein_ids,
    }

    if todo:
        prompt_config = load_json_file(PROMPT_CONFIG_PATH)
        maker_schema = load_json_file(ED23_BAUSTEIN_ABGLEICH_MAKER_SCHEMA_PATH)
        checker_schema = load_json_file(ED23_BAUSTEIN_ABGLEICH_CHECKER_SCHEMA_PATH)
        system_instruction = prompt_config["ed23_baustein_abgleich_system"]
        maker_template = prompt_config["ed23_baustein_abgleich_maker_prompt"]
        checker_template = prompt_config["ed23_baustein_abgleich_checker_prompt"]
        prefix = f"ANWENDERKATALOG GRUNDSCHUTZ++ (Format: ID | Titel | Statement)\n{corpus_text}"
        praktiken_block = _praktiken_block()
        kategorien_block = "\n".join(sorted(kategorie_names))
        praktik_ids = {k for k in PRACTICE_ABBREVIATIONS if k != "METHODIK"}

        ai_client = AiClient(app_config)
        semaphore = asyncio.Semaphore(app_config.max_concurrent_ai_requests)
        lock = asyncio.Lock()
        since_save = 0
        # ki blocks finished in this or an interrupted earlier run (the checkpoint's `done`).
        done_cp_new: Dict[str, Any] = {a: ki for a, ki in done_cp.items() if a in ki_by_id}

        def save_checkpoint(force: bool = False) -> None:
            # Throttled full-file writes (always called under `lock`): a crash costs at most
            # the last few steps, a write per step invites transient file locks.
            nonlocal since_save
            since_save += 1
            if force or since_save >= 10:
                _atomic_save_json({CHECKPOINT_DONE: done_cp_new, CHECKPOINT_KANDIDATEN: kandidaten}, CHECKPOINT_PATH)
                since_save = 0
        model_label = f"{app_config.gemini_model} (thinking {app_config.maker_thinking_level})"
        checker_label = f"{app_config.gemini_model} (thinking {app_config.checker_thinking_level})"

        async def check_and_store(aid: str) -> None:
            record = records[aid]
            result = kandidaten[aid]
            verdict = None
            if result["zuordnungen"] or result.get("neues_control"):
                verdict = await _checker(ai_client, record, bausteine[record["baustein"]], result, contexts,
                                         checker_template, checker_schema, semaphore)
            result = apply_checker_verdict(result, verdict)
            ki = {
                "pruefung": result["pruefung"], "zuordnungen": result["zuordnungen"],
                "neues_control": result.get("neues_control"), "ohne_control": result.get("ohne_control"),
                "offen": result.get("offen", ""), "gesamt": result.get("gesamt", ""),
                "verworfen": result.get("verworfen", []),
                "maker": model_label, "checker": checker_label, "stand": stand,
            }
            async with lock:
                ki_by_id[aid] = ki
                done_cp_new[aid] = ki
                kandidaten.pop(aid, None)
                save_checkpoint()

        rounds = 0
        remaining = [aid for aid in todo if aid not in kandidaten]
        while remaining and rounds < MAX_ROUNDS:
            rounds += 1
            size = ED23_BAUSTEIN_ABGLEICH_BATCH_SIZE if rounds == 1 else 1
            batches: List[List[Dict[str, Any]]] = []
            by_baustein: Dict[str, List[Dict[str, Any]]] = {}
            for aid in remaining:
                by_baustein.setdefault(records[aid]["baustein"], []).append(records[aid])
            for bid, recs in by_baustein.items():
                recs.sort(key=lambda r: anforderung_sort_key(r["id"]))
                batches += [recs[i:i + size] for i in range(0, len(recs), size)]
            logger.info(f"Maker round {rounds}: {len(remaining)} Anforderungen in {len(batches)} batches (size {size}).")

            async def run_batch(batch):
                baustein = bausteine[batch[0]["baustein"]]
                zo_name = zo_names.get(baustein_map["baustein_zielobjekt_map"].get(baustein["id"], ""), "")
                raw = await _maker_batch(ai_client, batch, baustein, zo_name, prefix, maker_template,
                                         system_instruction, maker_schema, praktiken_block, kategorien_block, semaphore)
                async with lock:
                    for aid, item in raw.items():
                        kandidaten[aid] = filter_maker_result(item, records[aid], gpp_lookup, praktik_ids, kategorie_names)
                    save_checkpoint()

            await asyncio.gather(*(run_batch(b) for b in batches))
            remaining = [aid for aid in todo if aid not in kandidaten and aid not in ki_by_id]

        for aid in remaining:
            logger.warning(f"{aid}: no maker result after {MAX_ROUNDS} rounds; recorded as unbeantwortet.")
            kandidaten[aid] = {"pruefung": {"art": None, "modalverb": None, "control_noetig": None, "hinweis": ""},
                               "zuordnungen": [], "neues_control": None,
                               "ohne_control": {"art": "unbeantwortet", "begruendung": f"kein Maker-Ergebnis in {MAX_ROUNDS} Runden"},
                               "offen": "", "verworfen": []}

        await asyncio.gather(*(check_and_store(aid) for aid in list(kandidaten) if aid in records))
        async with lock:
            save_checkpoint(force=True)
        ai_client.log_usage_summary("stage_ed23_baustein_abgleich")
        if app_config.is_test_mode:
            logger.info(f"TEST mode: checkpoint kept at '{CHECKPOINT_PATH}', output not published.")
            return

    n_new = sum(1 for ki in ki_by_id.values() if ki.get("neues_control"))
    n_ohne = sum(1 for ki in ki_by_id.values() if ki.get("ohne_control"))
    verdicts: Dict[str, int] = {}
    for ki in ki_by_id.values():
        for z in ki.get("zuordnungen", []):
            verdicts[z.get("checker") or "-"] = verdicts.get(z.get("checker") or "-", 0) + 1
        if ki.get("neues_control"):
            k = "neu:" + (ki["neues_control"].get("checker") or "-")
            verdicts[k] = verdicts.get(k, 0) + 1
    meta.update({"anforderungen": len(records), "modell_anforderungen": len(pending_ids),
                 "neue_controls": n_new, "ohne_control": n_ohne, "checker_urteile": verdicts})
    save_json_file(_serialize(records, det_by_id, ki_by_id, meta), ED23_BAUSTEIN_ABGLEICH_JSON_PATH)
    if os.path.exists(CHECKPOINT_PATH):
        os.remove(CHECKPOINT_PATH)
    logger.info(
        f"stage_ed23_baustein_abgleich finished: {len(records)} Anforderungen, {n_new} new NG controls, "
        f"{n_ohne} ohne Control, checker verdicts {verdicts}."
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    asyncio.run(run_stage_ed23_baustein_abgleich())
