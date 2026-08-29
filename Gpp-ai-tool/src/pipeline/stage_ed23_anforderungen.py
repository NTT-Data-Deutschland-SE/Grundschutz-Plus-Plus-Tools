"""
Pipeline Stage: G++ control → BSI Edition-2023 Anforderungen mapping.

For every G++ control this stage asks the AI which BSI ED2023 Anforderungen match it, and
writes the result as an OSCAL 1.2.2 Control Mapping document
(`hilfsdateien/gpp_ed23_anforderungen.json`, root `mapping-collection`) consumed by the
GS++-oscal-app to show a "Zeige BSI ED23 Anforderungen" panel per control — replacing the old
runtime, web-search-grounded AI call in GSpp-Viewer that frequently hallucinated IDs. The
internal per-control match map is serialized via `utils.oscal_mapping`.

Grounding: the OFFICIAL BSI XML Kompendium 2023 (sha256-pinned download, parsed by
utils.ed23_xml — deliberately no derived OSCAL edition) is stripped to a compact
`id | name | numbered sentences` corpus of every active Anforderung in the amtliche
Wortlaut and supplied as the model's context. Because that corpus is identical for every
control query, it is put into an explicit context cache once and reused per call. Every
returned ID is post-filtered against the real corpus so hallucinated / old-edition IDs
cannot reach the output; every satz_nr refers to the official sentence numbering.

Precision measures (issue #28 — mappings were too broad and unspecific):

* Per-control context is the full picture, not just the title: the statement prose with all
  OSCAL `{{ insert: param, ... }}` directives resolved to their values, plus the control's
  `guidance` part.
* The sibling controls of the same Praktik (leaf group) are listed in the prompt as explicit
  negative context — they are mapped separately, so content belonging primarily to a sibling
  must not be matched to this control.
* Each ED2023 Anforderung's prose is rendered as numbered sentences `(S1) ... (S2) ...`; the
  model must name the sentence number carrying each match (`satz_nr`). The number is validated
  against the real sentence count and prefixed to the Begründung as `(Teilanforderung n)`.
  We call these numbered sentences "Teilanforderungen" — a term that appears in no BSI
  standard and is only used in one paragraph of the BSI Auditierungsschema.
* Maker-checker: the corpus-grounded query deliberately over-collects *candidates* (recall),
  and every candidate is then re-judged by a strict, self-contained verification call
  (control context + that one Anforderung's sentences — no corpus needed) that decides
  match / satz_nr / Begründung (precision). Only verified candidates reach the output.
  The two passes intentionally use different models (see ED23_MAKER_MODEL in constants):
  the maker model nominates generously, the stricter default model judges.

Cost measures (docs/token-kostenplan.md): the maker runs in BATCHES of
ED23_MAKER_BATCH_SIZE controls per call (the cached corpus is billed per call); sibling
negative context carries id+title only; candidates already verified by the ED23-seitige
Satz-Abdeckung (same criteria, opposite direction, official numbering) skip the verify
call; maker candidate lists are checkpointed before verification so a crash in either
phase loses almost nothing; the client logs a token totals line at the end.
"""

import asyncio
import json
import logging
import os
import re
import tempfile
import time
from typing import Any, Dict, List, Optional, Tuple

from config import app_config
from clients.ai_client import AiClient
from utils.data_loader import load_json_file, save_json_file
from utils.oscal_utils import normalize_id
from utils.oscal_mapping import to_oscal_mapping_collection
from utils.ed23_xml import fetch_official_xml, load_official_xml
from constants import (
    GPP_KOMPENDIUM_JSON_PATH,
    GPP_CATALOG_PIN_SHA256,
    GPP_ED23_ANFORDERUNGEN_JSON_PATH,
    ED23_ANFORDERUNGEN_STRIPPED_JSON_PATH,
    ED23_BATCH_RESPONSE_SCHEMA_PATH,
    ED23_VERIFY_RESPONSE_SCHEMA_PATH,
    ED23_SATZ_ABDECKUNG_JSON_PATH,
    ED23_MAKER_MODEL,
    ED23_MAKER_BATCH_SIZE,
    PROMPT_CONFIG_PATH,
)

logger = logging.getLogger(__name__)

# OSCAL parameter insert directive as it appears verbatim in catalog prose.
_PARAM_INSERT_PATTERN = re.compile(r"\{\{\s*insert:\s*param,\s*([^}\s]+)\s*\}\}")

# Sentence splitting lives in utils.sentence_split (stdlib-only, shared with
# scripts/analyze_ed23_coverage.py); the aliases preserve this module's original
# private names for existing imports (tests) and call sites.
from utils.sentence_split import (  # noqa: E402
    ABBREVIATIONS as _ABBREVIATIONS,
    SENTENCE_SPLIT as _SENTENCE_SPLIT,
    split_sentences as _split_sentences,
)


def _resolve_param_inserts(text: str, params: Dict[str, Dict[str, Any]]) -> str:
    """Replaces `{{ insert: param, <id> }}` directives with the parameter's value.

    The G++ resolved catalog keeps OSCAL insert directives in the prose while defining the
    concrete values on the control itself (`params[].values`, `label` as fallback). Without
    this substitution the model would see the raw directive instead of the most specific part
    of the sentence. Unresolvable references are left verbatim.
    """
    def _replace(match: "re.Match[str]") -> str:
        param = params.get(match.group(1))
        if not param:
            return match.group(0)
        values = param.get("values") or ([param["label"]] if param.get("label") else [])
        return ", ".join(values) if values else match.group(0)

    return _PARAM_INSERT_PATTERN.sub(_replace, text or "")


def anforderung_label(req: Dict[str, Any]) -> str:
    """Rebuilds the display label 'Titel (B) [Rolle]' from an official-XML requirement record."""
    label = req.get("titel", "") or ""
    if req.get("level"):
        label = f"{label} ({req['level']})"
    if req.get("rolle"):
        label = f"{label} [{req['rolle']}]"
    return label


def build_ed23_corpus(official: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], Dict[str, Dict[str, Any]]]:
    """Builds the grounding corpus from the OFFICIAL XML Kompendium requirement records.

    Input is the `{req_id: record}` map from utils.ed23_xml.load_official_xml — the amtliche
    Wortlaut, deliberately NOT any derived OSCAL edition. Only active (non-ENTFALLEN)
    Anforderungen are included; `saetze` is the official prose split by the shared splitter,
    so every `satz_nr` the pipeline emits refers to the official sentence numbering. Returns
    the stripped list plus a lookup keyed by normalized id → `{id, name, n_saetze}` for
    validating the AI's returned IDs and sentence numbers.
    """
    stripped: List[Dict[str, Any]] = []
    lookup: Dict[str, Dict[str, Any]] = {}
    for req in sorted(official.values(), key=lambda r: r["id"]):
        if req.get("entfallen"):
            continue
        name = anforderung_label(req)
        saetze = list(req.get("saetze") or [])
        stripped.append({
            "id": req["id"], "name": name, "prose": " ".join(saetze), "saetze": saetze,
        })
        lookup[normalize_id(req["id"])] = {
            "id": req["id"], "name": name, "n_saetze": len(saetze),
        }
    return stripped, lookup


def _corpus_text(stripped: List[Dict[str, Any]]) -> str:
    """Renders the corpus as one `id | name | (S1) ... (S2) ...` line per Anforderung."""
    lines = []
    for a in stripped:
        numbered = " ".join(f"(S{i}) {s}" for i, s in enumerate(a["saetze"], start=1))
        lines.append(f"{a['id']} | {a['name']} | {numbered}")
    return "\n".join(lines)


def build_gpp_match_contexts(gpp_catalog: Dict[str, Any]) -> Dict[str, Dict[str, str]]:
    """Extracts every G++ control with the full context the matching prompt needs.

    Per control id this returns title, param-resolved statement prose and guidance, a
    human-readable Praktik label (Baustein / Praktik), and `siblings`: the other controls of
    the same Praktik (leaf group, nested sub-controls included) as `id | title | statement`
    lines. The siblings are sent as negative context — they are mapped in their own queries,
    so the model must not assign their content to this control (issue #28: matches were not
    specific to the control within its Praktik).
    """
    contexts: Dict[str, Dict[str, str]] = {}
    praktik_members: Dict[str, List[str]] = {}

    def walk_control(control, praktik_key: str, praktik_label: str):
        cid = control.get("id")
        if cid:
            params = {p.get("id"): p for p in control.get("params") or []}
            statement, guidance = "", ""
            for part in control.get("parts") or []:
                if part.get("name") == "statement" and not statement:
                    statement = part.get("prose", "") or ""
                elif part.get("name") == "guidance" and not guidance:
                    guidance = part.get("prose", "") or ""
            if not statement and control.get("parts"):
                statement = control["parts"][0].get("prose", "") or ""
            contexts[cid] = {
                "title": control.get("title", "") or "",
                "prose": _resolve_param_inserts(statement, params).strip(),
                "guidance": _resolve_param_inserts(guidance, params).strip(),
                "praktik": praktik_label,
            }
            praktik_members.setdefault(praktik_key, []).append(cid)
        for sub in control.get("controls") or []:
            walk_control(sub, praktik_key, praktik_label)

    def walk_groups(groups, baustein_title: Optional[str]):
        for group in groups or []:
            title = group.get("title", "") or ""
            baustein = baustein_title or title
            if group.get("controls"):
                gid = group.get("id") or title
                label = f"{baustein} / {title} ({gid})" if baustein != title else f"{title} ({gid})"
                for control in group["controls"]:
                    walk_control(control, gid, label)
            walk_groups(group.get("groups"), baustein)

    walk_groups(gpp_catalog.get("catalog", {}).get("groups", []), None)

    # Sibling-Diät (docs/token-kostenplan.md, Maßnahme 4): the negative context only needs
    # to make the neighbours NAMEABLE — id and title suffice for "belongs primarily to a
    # sibling". Full statements here were the single biggest uncached token driver
    # (Praktiken like BER carry 92 controls, repeated in every maker AND verify prompt).
    for members in praktik_members.values():
        for cid in members:
            lines = [
                f"- {sid} | {contexts[sid]['title']}"
                for sid in members if sid != cid
            ]
            contexts[cid]["siblings"] = "\n".join(lines) if lines else "(keine)"
    return contexts


def _filter_matches(raw_matches: Any, id_lookup: Dict[str, Dict[str, Any]], control_id: str) -> List[Dict[str, Any]]:
    """Keeps only matches whose ID really exists in the ED23 corpus; restores canonical id/name.

    The model's `satz_nr` is validated against the Anforderung's real sentence count; a valid
    number is kept and prefixed to the Begründung as `(Satz n)`, an invalid one is dropped
    (the match itself is kept) and logged.
    """
    result: List[Dict[str, Any]] = []
    seen = set()
    if not isinstance(raw_matches, list):
        return result
    for item in raw_matches:
        if not isinstance(item, dict):
            continue
        canonical = id_lookup.get(normalize_id(item.get("id", "")))
        if not canonical or canonical["id"] in seen:
            continue
        seen.add(canonical["id"])
        satz_nr = item.get("satz_nr")
        if not isinstance(satz_nr, int) or not (1 <= satz_nr <= canonical["n_saetze"]):
            logger.warning(
                f"Control '{control_id}': invalid satz_nr {satz_nr!r} for {canonical['id']} "
                f"(has {canonical['n_saetze']} sentence(s)); keeping match without sentence ref."
            )
            satz_nr = None
        begruendung = (item.get("begruendung", "") or "").strip()
        if satz_nr:
            begruendung = f"(Satz {satz_nr}) {begruendung}".strip()
        result.append({
            "id": canonical["id"],
            "name": canonical["name"],
            "begruendung": begruendung,
            "satz_nr": satz_nr,
        })
    return result


def batch_controls_block(batch: List[Tuple[str, Dict[str, str]]]) -> str:
    """Renders the per-control context blocks of one maker batch prompt."""
    blocks = []
    for control_id, control in batch:
        blocks.append(
            f"### {control_id} — {control.get('title', '')} "
            f"(Praktik \"{control.get('praktik', '')}\")\n"
            f"Anforderungstext: {control.get('prose', '')}\n"
            f"Erläuterung: {control.get('guidance') or '(keine)'}\n"
            f"Nachbar-Maßnahmen (Negativkontext):\n{control.get('siblings') or '(keine)'}"
        )
    return "\n\n".join(blocks)


def distribute_batch_response(response: Any, batch_ids: List[str]) -> Dict[str, Optional[list]]:
    """Maps a batch maker response back to {control_id: raw_treffer or None}.

    None marks a requested control the model failed to answer for — the caller records an
    empty candidate list and a warning instead of silently treating it as "no matches".
    Unknown control_ids in the response are ignored.
    """
    wanted = {cid: None for cid in batch_ids}
    if isinstance(response, dict):
        for block in response.get("ergebnisse") or []:
            if not isinstance(block, dict):
                continue
            cid = (block.get("control_id") or "").strip()
            if cid in wanted and wanted[cid] is None:
                wanted[cid] = block.get("treffer") or []
    return wanted


async def _match_batch(
    ai_client: AiClient,
    batch: List[Tuple[str, Dict[str, str]]],
    prompt_template: str,
    schema: Dict[str, Any],
    id_lookup: Dict[str, Dict[str, Any]],
    cached_content: str,
    inline_prefix: str,
    semaphore: asyncio.Semaphore,
) -> Dict[str, List[Dict[str, Any]]]:
    """Maker recall pass for a BATCH of controls in one call (Kostenplan Maßnahme 3).

    The cached corpus is billed per call, so batching divides the dominant cost by the
    batch size. Each control is answered independently; ID/satz validation and dedup run
    per control via `_filter_matches`.
    """
    batch_ids = [cid for cid, _ in batch]
    user_prompt = prompt_template.format(
        n=len(batch), controls_block=batch_controls_block(batch)
    )
    prompt = user_prompt if cached_content else f"{inline_prefix}\n\n{user_prompt}"
    label = f"ED23Abgleich-Batch-{batch_ids[0]}..{batch_ids[-1]}"
    async with semaphore:
        try:
            response = await ai_client.generate_validated_json_response(
                prompt=prompt,
                json_schema=schema,
                request_context_log=label,
                cached_content=cached_content,
                model_override=ED23_MAKER_MODEL,
            )
        except Exception as e:
            logger.warning(f"AI matching failed for batch {batch_ids}: {e}")
            return {cid: [] for cid in batch_ids}

    distributed = distribute_batch_response(response, batch_ids)
    result: Dict[str, List[Dict[str, Any]]] = {}
    for cid in batch_ids:
        raw = distributed[cid]
        if raw is None:
            logger.warning(f"Batch response missing control '{cid}'; recording no candidates.")
            raw = []
        result[cid] = _filter_matches(raw, id_lookup, cid)
    return result


def load_satz_bestaetigt(path: str) -> Dict[Tuple[str, int, str], str]:
    """Loads verified (Anforderung, satz_nr, control) triples from the Satz-Abdeckung.

    Those pairs were already strictly verified by stage_ed23_satz_abdeckung (same criteria,
    opposite direction, official sentence numbering) — re-verifying them would buy nothing
    (Kostenplan Maßnahme 6: die bezahlten Urteile wiederverwenden). Returns {} when the
    artifact is absent.
    """
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            doc = json.load(f)["ed23_satz_abdeckung"]
    except (OSError, KeyError, json.JSONDecodeError) as e:
        logger.warning(f"Could not read Satz-Abdeckung '{path}' ({e}); no verify skips.")
        return {}
    lookup: Dict[Tuple[str, int, str], str] = {}
    for rid, rec in (doc.get("anforderungen") or {}).items():
        for hit in rec.get("treffer") or []:
            try:
                key = (normalize_id(rid), int(hit["satz_nr"]), hit["control_id"])
            except (KeyError, TypeError, ValueError):
                continue
            lookup[key] = (hit.get("begruendung") or "").strip()
    return lookup


def split_bestaetigte(
    control_id: str,
    candidates: List[Dict[str, Any]],
    bestaetigt: Dict[Tuple[str, int, str], str],
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Splits candidates into (already verified by the Satz-Abdeckung, still to verify)."""
    uebernommen: List[Dict[str, Any]] = []
    zu_pruefen: List[Dict[str, Any]] = []
    for candidate in candidates:
        satz_nr = candidate.get("satz_nr")
        key = (normalize_id(candidate["id"]), satz_nr or 0, control_id)
        if satz_nr and key in bestaetigt:
            begruendung = bestaetigt[key]
            uebernommen.append({
                "id": candidate["id"],
                "name": candidate["name"],
                "begruendung": f"(Teilanforderung {satz_nr}) {begruendung}".strip(),
                "satz_nr": satz_nr,
            })
        else:
            zu_pruefen.append(candidate)
    return uebernommen, zu_pruefen


async def _verify_candidate(
    ai_client: AiClient,
    control_id: str,
    control: Dict[str, str],
    candidate: Dict[str, Any],
    saetze_by_id: Dict[str, List[str]],
    verify_prompt_template: str,
    verify_schema: Dict[str, Any],
    semaphore: asyncio.Semaphore,
) -> Optional[Dict[str, Any]]:
    """Strictly re-judges one candidate pair; returns the final match or None (checker pass).

    The verification prompt is self-contained (control context + the candidate Anforderung's
    numbered sentences), so it needs no corpus cache. The verifier's verdict replaces the
    candidate's satz_nr and Begründung; an out-of-range satz_nr is dropped but the match kept.
    """
    saetze = saetze_by_id.get(candidate["id"], [])
    numbered = "\n".join(f"(S{i}) {s}" for i, s in enumerate(saetze, start=1))
    prompt = verify_prompt_template.format(
        praktik=control.get("praktik", ""),
        control_id=control_id,
        title=control.get("title", ""),
        prose=control.get("prose", ""),
        guidance=control.get("guidance") or "(keine)",
        siblings=control.get("siblings") or "(keine)",
        anf_id=candidate["id"],
        anf_name=candidate["name"],
        anf_saetze=numbered or "(keine)",
    )
    async with semaphore:
        try:
            verdict = await ai_client.generate_validated_json_response(
                prompt=prompt,
                json_schema=verify_schema,
                request_context_log=f"ED23Verify-{control_id}-{candidate['id']}",
            )
        except Exception as e:
            logger.warning(
                f"Verification failed for '{control_id}' -> '{candidate['id']}': {e}; dropping candidate."
            )
            return None

    if not isinstance(verdict, dict) or not verdict.get("match"):
        return None
    satz_nr = verdict.get("satz_nr")
    if not isinstance(satz_nr, int) or not (1 <= satz_nr <= len(saetze)):
        logger.warning(
            f"Control '{control_id}': verifier returned invalid satz_nr {satz_nr!r} for "
            f"{candidate['id']} (has {len(saetze)} sentence(s)); keeping match without sentence ref."
        )
        satz_nr = None
    begruendung = (verdict.get("begruendung", "") or "").strip()
    if satz_nr:
        # "Teilanforderung" is the project's term for a numbered sentence of an ED23
        # Anforderung (not a BSI-standard term; used once in the BSI Auditierungsschema).
        begruendung = f"(Teilanforderung {satz_nr}) {begruendung}".strip()
    return {
        "id": candidate["id"],
        "name": candidate["name"],
        "begruendung": begruendung,
        "satz_nr": satz_nr,
    }


# The checkpoint sits next to the final output. It holds BOTH the finished per-control
# results and the maker candidate lists still awaiting verification, so a crash in either
# phase loses at most a handful of calls (docs/token-kostenplan.md, Maßnahme 7 — the
# 265M-token maker phase of the crashed v2 run lived only in RAM).
CHECKPOINT_PATH = GPP_ED23_ANFORDERUNGEN_JSON_PATH + ".partial"
CHECKPOINT_KEY = "gpp_ed23_anforderungen_map"
CANDIDATES_KEY = "ed23_maker_kandidaten"


def _atomic_save_json(data: Dict[str, Any], path: str) -> None:
    """Writes JSON via a temp file + os.replace so a crash mid-write never corrupts `path`.

    os.replace is retried with backoff: on Windows a virus scanner or indexer can hold a
    transient lock on the freshly written target, making the rename fail with WinError 5.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        for attempt in range(5):
            try:
                os.replace(tmp, path)
                break
            except PermissionError:
                if attempt == 4:
                    raise
                time.sleep(0.2 * (attempt + 1))
    except Exception:
        if os.path.exists(tmp):
            os.remove(tmp)
        raise


def _load_checkpoint(path: str) -> Tuple[Dict[str, List[Dict[str, Any]]], Dict[str, List[Dict[str, Any]]]]:
    """Loads finished results and pending maker candidates from a prior run."""
    if not os.path.exists(path):
        return {}, {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        done = data.get(CHECKPOINT_KEY, {})
        kandidaten = data.get(CANDIDATES_KEY, {})
        logger.info(
            f"Resuming from checkpoint '{path}': {len(done)} controls done, "
            f"{len(kandidaten)} with maker candidates awaiting verification."
        )
        return done, kandidaten
    except Exception as e:
        logger.warning(f"Could not read checkpoint '{path}' ({e}); starting fresh.")
        return {}, {}


async def run_stage_ed23_anforderungen() -> None:
    """Main entry point for the G++ → ED2023 Anforderungen mapping stage."""
    logger.info("Starting stage_ed23_anforderungen...")

    # Idempotency (Rule 5.2.7): skip if output exists and overwriting is disabled.
    if os.path.exists(GPP_ED23_ANFORDERUNGEN_JSON_PATH) and not app_config.overwrite_temp_files:
        logger.info(
            "Output file already exists and OVERWRITE_TEMP_FILES is false. "
            "Skipping stage_ed23_anforderungen."
        )
        return

    # Load sources: the pinned G++ catalog plus the OFFICIAL ED23 XML Kompendium (sha256-
    # pinned download via utils.ed23_xml) — the amtliche Wortlaut is the only ED23 basis.
    gpp_catalog = load_json_file(GPP_KOMPENDIUM_JSON_PATH, expected_sha256=GPP_CATALOG_PIN_SHA256)
    if not gpp_catalog:
        logger.error("Failed to load G++ Kompendium. Aborting stage.")
        return
    xml_bytes, _xml_sha = fetch_official_xml()
    official, _rejected = load_official_xml(xml_bytes)

    prompt_config = load_json_file(PROMPT_CONFIG_PATH)
    batch_schema = load_json_file(ED23_BATCH_RESPONSE_SCHEMA_PATH)
    verify_schema = load_json_file(ED23_VERIFY_RESPONSE_SCHEMA_PATH)
    system_instruction = prompt_config["ed23_abgleich_system"]
    batch_prompt_template = prompt_config["ed23_abgleich_batch_prompt"]
    verify_prompt_template = prompt_config["ed23_abgleich_verify_prompt"]

    # Verified triples from the ED23-seitige Satz-Abdeckung: identical criteria, opposite
    # direction, same official numbering — candidates it already confirmed skip the verify
    # call entirely (Kostenplan: die bezahlten Urteile wiederverwenden).
    satz_bestaetigt = load_satz_bestaetigt(ED23_SATZ_ABDECKUNG_JSON_PATH)
    if satz_bestaetigt:
        logger.info(f"Satz-Abdeckung loaded: {len(satz_bestaetigt)} pre-verified triples usable as verify skips.")

    # G++ controls to map (all of them), each with statement, guidance, and Praktik siblings.
    gpp_controls = build_gpp_match_contexts(gpp_catalog)
    logger.info(f"Extracted {len(gpp_controls)} G++ controls with Praktik context.")

    # Stripped ED2023 corpus (official wording) used as the cached grounding context.
    stripped, id_lookup = build_ed23_corpus(official)
    saetze_by_id = {a["id"]: a["saetze"] for a in stripped}
    corpus_text = _corpus_text(stripped)
    logger.info(f"Built ED2023 corpus with {len(stripped)} Anforderungen ({len(corpus_text)} chars).")
    save_json_file({"ed23_anforderungen": stripped}, ED23_ANFORDERUNGEN_STRIPPED_JSON_PATH)

    ai_client = AiClient(app_config)

    # Explicit context cache: the corpus is the cached content, the short ED23 system prompt the
    # cached system instruction. Reused across every per-control call.
    # The cache must live on the maker model — the candidate pass is the only cached caller.
    cached_content = ai_client.create_context_cache(
        content=corpus_text, system_instruction=system_instruction, model_override=ED23_MAKER_MODEL
    )
    # Fallback prefix inlined into each prompt when caching is unavailable (system + corpus).
    inline_prefix = (
        f"{system_instruction}\n\nVerfügbare BSI ED2023 Anforderungen "
        f"(Format: ID | Name | Beschreibung als nummerierte Sätze (S1) (S2) ...):\n{corpus_text}"
    )

    # Respect Test Mode (Rule 9.1): only the first 3 controls.
    control_items = list(gpp_controls.items())
    if app_config.is_test_mode:
        control_items = control_items[:3]
        logger.info("TEST mode: limiting to the first 3 G++ controls.")

    # Resume support: finished controls and pending maker candidate lists both live in the
    # checkpoint, so a crash in either phase costs at most the last few (throttled) steps.
    final_map, kandidaten_map = _load_checkpoint(CHECKPOINT_PATH)
    pending = [(cid, control) for cid, control in control_items if cid not in final_map]
    checkpoint_lock = asyncio.Lock()
    semaphore = asyncio.Semaphore(app_config.max_concurrent_ai_requests)

    since_save = 0

    def _save_checkpoint(force: bool = False) -> None:
        # Throttled full-file writes (always called under checkpoint_lock): a write per
        # step invites transient Windows locks and buys no extra safety.
        nonlocal since_save
        since_save += 1
        if force or since_save >= 10:
            _atomic_save_json(
                {CHECKPOINT_KEY: final_map, CANDIDATES_KEY: kandidaten_map}, CHECKPOINT_PATH
            )
            since_save = 0

    # --- Phase A: maker recall in batches over the cached corpus ---
    to_match = [(cid, c) for cid, c in pending if cid not in kandidaten_map]
    batches = [
        to_match[i:i + ED23_MAKER_BATCH_SIZE]
        for i in range(0, len(to_match), ED23_MAKER_BATCH_SIZE)
    ]
    logger.info(
        f"Phase A: {len(to_match)} of {len(control_items)} controls need maker candidates "
        f"({len(batches)} batches à ≤{ED23_MAKER_BATCH_SIZE}; "
        f"{len(final_map)} done + {len(kandidaten_map)} candidate lists restored)."
    )

    async def _match_and_store(batch) -> None:
        result = await _match_batch(
            ai_client, batch, batch_prompt_template, batch_schema, id_lookup,
            cached_content, inline_prefix, semaphore,
        )
        async with checkpoint_lock:
            kandidaten_map.update(result)
            _save_checkpoint()

    try:
        if batches:
            await asyncio.gather(*(_match_and_store(b) for b in batches))
    finally:
        # The cache serves only the maker phase; release it before the (long) verify phase.
        ai_client.delete_context_cache(cached_content)
    async with checkpoint_lock:
        _save_checkpoint(force=True)

    # --- Phase B: strict verification per candidate, skipping pre-verified triples ---
    gespart = 0
    logger.info(f"Phase B: verifying candidates for {len(pending)} controls...")

    async def _verify_and_checkpoint(cid: str, control: Dict[str, Any]) -> None:
        nonlocal gespart
        candidates = kandidaten_map.get(cid, [])
        uebernommen, zu_pruefen = split_bestaetigte(cid, candidates, satz_bestaetigt)
        verified = await asyncio.gather(*(
            _verify_candidate(
                ai_client, cid, control, candidate, saetze_by_id,
                verify_prompt_template, verify_schema, semaphore,
            )
            for candidate in zu_pruefen
        ))
        matches = sorted(
            uebernommen + [m for m in verified if m],
            key=lambda m: (m["id"], m.get("satz_nr") or 0),
        )
        async with checkpoint_lock:
            gespart += len(uebernommen)
            final_map[cid] = matches
            kandidaten_map.pop(cid, None)
            _save_checkpoint()

    if pending:
        await asyncio.gather(*(_verify_and_checkpoint(cid, c) for cid, c in pending))
    else:
        logger.info("All G++ controls already present in checkpoint; nothing to verify.")
    logger.info(f"Verify skips via Satz-Abdeckung: {gespart} candidate pair(s) reused without a call.")

    # The .partial checkpoint stays in the internal {control_id: [matches]} shape (simple to
    # resume); only the final, published artifact is serialized as OSCAL.
    output_data = to_oscal_mapping_collection(final_map)
    save_json_file(output_data, GPP_ED23_ANFORDERUNGEN_JSON_PATH)
    # Final output is written; the checkpoint is redundant once every control is covered.
    if os.path.exists(CHECKPOINT_PATH) and len(final_map) >= len(control_items):
        os.remove(CHECKPOINT_PATH)
    total = sum(len(m) for m in final_map.values())
    logger.info(
        f"stage_ed23_anforderungen finished. Mapped {len(final_map)} G++ controls "
        f"to {total} ED2023 Anforderung references ({gespart} verifies saved via Satz-Abdeckung)."
    )
    ai_client.log_usage_summary("stage_ed23_anforderungen")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    asyncio.run(run_stage_ed23_anforderungen())
