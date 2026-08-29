"""
Pipeline Stage: G++ control → BSI Edition-2023 Anforderungen mapping.

For every G++ control this stage asks the AI which BSI ED2023 Anforderungen match it, and
writes the result as an OSCAL 1.2.2 Control Mapping document
(`hilfsdateien/gpp_ed23_anforderungen.json`, root `mapping-collection`) consumed by the
GS++-oscal-app to show a "Zeige BSI ED23 Anforderungen" panel per control — replacing the old
runtime, web-search-grounded AI call in GSpp-Viewer that frequently hallucinated IDs. The
internal per-control match map is serialized via `utils.oscal_mapping`.

Grounding: the full ED2023 OSCAL catalog (BSI_2023_JSON) is stripped to a compact
`id | name | numbered sentences` corpus of every Anforderung and supplied as the model's
context. Because that corpus is identical for every control query, it is put into an explicit
Vertex AI context cache once and reused per call (implicit caching does not engage for this
model/region). Every returned ID is post-filtered against the real corpus so hallucinated /
old-edition IDs cannot reach the output.

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
"""

import asyncio
import json
import logging
import os
import re
import tempfile
from typing import Any, Dict, List, Optional, Tuple

from config import app_config
from clients.ai_client import AiClient
from utils.data_loader import load_json_file, save_json_file
from utils.oscal_utils import normalize_id
from utils.oscal_mapping import to_oscal_mapping_collection
from constants import (
    GPP_KOMPENDIUM_JSON_PATH,
    GPP_CATALOG_PIN_SHA256,
    BSI_2023_JSON_PATH,
    GPP_ED23_ANFORDERUNGEN_JSON_PATH,
    ED23_ANFORDERUNGEN_STRIPPED_JSON_PATH,
    ED23_ANFORDERUNGEN_RESPONSE_SCHEMA_PATH,
    ED23_VERIFY_RESPONSE_SCHEMA_PATH,
    ED23_MAKER_MODEL,
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


def _statement_prose(control: Dict[str, Any]) -> str:
    """Returns the representative statement prose of a BSI ED2023 Anforderung.

    ED2023 controls carry maturity levels (m1 Partial … m5 Comprehensive) each with its own
    nested `statement` part. The canonical requirement text is Maturity Level 3 "Defined"
    (`class: maturity-level-defined`), so we prefer the statement under that level. We fall
    back to the first `statement` part found, then to the first available prose.
    """
    def statement_in(parts):
        for part in parts or []:
            if part.get("name") == "statement" and part.get("prose"):
                return part["prose"]
            nested = statement_in(part.get("parts"))
            if nested:
                return nested
        return None

    def first_prose(parts):
        for part in parts or []:
            if part.get("prose"):
                return part["prose"]
            nested = first_prose(part.get("parts"))
            if nested:
                return nested
        return ""

    parts = control.get("parts", []) or []

    # Prefer the "Defined" maturity level's statement.
    for part in parts:
        if part.get("class") == "maturity-level-defined":
            defined = statement_in(part.get("parts")) or (
                part.get("prose") if part.get("name") == "statement" else None
            )
            if defined:
                return defined

    return statement_in(parts) or first_prose(parts)


def build_ed23_corpus(bsi_catalog: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], Dict[str, Dict[str, Any]]]:
    """Strips the ED2023 catalog to every Anforderung as `{id, name, prose, saetze}`.

    `saetze` is the prose split into numbered sentences — the numbering the model references
    via `satz_nr`. Returns the stripped list and a lookup keyed by normalized id →
    `{id, name, n_saetze}` so the AI's returned IDs and sentence numbers can be validated and
    the canonical id/name restored. Nested sub-controls are included.
    """
    stripped: List[Dict[str, Any]] = []
    lookup: Dict[str, Dict[str, Any]] = {}

    def walk_controls(controls):
        for control in controls or []:
            cid = control.get("id")
            if cid:
                name = control.get("title", "") or ""
                prose = (_statement_prose(control) or "").replace("\n", " ").strip()
                saetze = _split_sentences(prose)
                stripped.append({"id": cid, "name": name, "prose": prose, "saetze": saetze})
                lookup[normalize_id(cid)] = {"id": cid, "name": name, "n_saetze": len(saetze)}
            if control.get("controls"):
                walk_controls(control["controls"])

    def walk_groups(groups):
        for group in groups or []:
            walk_controls(group.get("controls", []))
            if group.get("groups"):
                walk_groups(group["groups"])

    walk_groups(bsi_catalog.get("catalog", {}).get("groups", []))
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

    for members in praktik_members.values():
        for cid in members:
            lines = [
                f"- {sid} | {contexts[sid]['title']} | {contexts[sid]['prose']}"
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


async def _match_control(
    ai_client: AiClient,
    control_id: str,
    control: Dict[str, str],
    prompt_template: str,
    schema: Dict[str, Any],
    id_lookup: Dict[str, Dict[str, Any]],
    cached_content: str,
    inline_prefix: str,
    semaphore: asyncio.Semaphore,
) -> Tuple[str, List[Dict[str, Any]]]:
    """Asks the AI for ED23 Anforderungen *candidates* for one G++ control (recall pass).

    The prompt deliberately over-collects; every returned candidate is subsequently
    re-judged by `_verify_candidate` (precision pass). ID validation / dedup happens here.
    """
    user_prompt = prompt_template.format(
        control_id=control_id,
        title=control.get("title", ""),
        prose=control.get("prose", ""),
        guidance=control.get("guidance") or "(keine)",
        praktik=control.get("praktik", ""),
        siblings=control.get("siblings") or "(keine)",
    )
    # When the cache is unavailable, inline the system + corpus so grounding still applies.
    prompt = user_prompt if cached_content else f"{inline_prefix}\n\n{user_prompt}"

    async with semaphore:
        try:
            response = await ai_client.generate_validated_json_response(
                prompt=prompt,
                json_schema=schema,
                request_context_log=f"ED23Abgleich-{control_id}",
                cached_content=cached_content,
                model_override=ED23_MAKER_MODEL,
            )
        except Exception as e:
            logger.warning(f"AI matching failed for G++ control '{control_id}': {e}")
            return control_id, []

    matches = _filter_matches(response, id_lookup, control_id)
    logger.debug(f"Control '{control_id}': {len(matches)} ED23 candidate(s) found.")
    return control_id, matches


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


async def match_and_verify_control(
    ai_client: AiClient,
    control_id: str,
    control: Dict[str, str],
    prompt_template: str,
    schema: Dict[str, Any],
    verify_prompt_template: str,
    verify_schema: Dict[str, Any],
    id_lookup: Dict[str, Dict[str, Any]],
    saetze_by_id: Dict[str, List[str]],
    cached_content: str,
    inline_prefix: str,
    semaphore: asyncio.Semaphore,
) -> Tuple[str, List[Dict[str, Any]]]:
    """Full maker-checker flow for one G++ control: collect candidates, verify each, keep survivors."""
    _, candidates = await _match_control(
        ai_client, control_id, control, prompt_template, schema, id_lookup,
        cached_content, inline_prefix, semaphore,
    )
    verified = await asyncio.gather(*(
        _verify_candidate(
            ai_client, control_id, control, candidate, saetze_by_id,
            verify_prompt_template, verify_schema, semaphore,
        )
        for candidate in candidates
    ))
    matches = [m for m in verified if m]
    logger.debug(
        f"Control '{control_id}': {len(matches)} of {len(candidates)} candidate(s) verified."
    )
    return control_id, matches


# The checkpoint sits next to the final output and holds the per-control results accumulated
# so far, so a crashed run (e.g. cache/network failure) can be resumed instead of re-querying
# every control from scratch. It is deleted once the final output is written successfully.
CHECKPOINT_PATH = GPP_ED23_ANFORDERUNGEN_JSON_PATH + ".partial"


def _atomic_save_json(data: Dict[str, Any], path: str) -> None:
    """Writes JSON via a temp file + os.replace so a crash mid-write never corrupts `path`."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        os.replace(tmp, path)
    except Exception:
        if os.path.exists(tmp):
            os.remove(tmp)
        raise


def _load_checkpoint(path: str) -> Dict[str, List[Dict[str, Any]]]:
    """Loads the per-control results from a prior run. Returns {} if absent or unreadable."""
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        done = data.get("gpp_ed23_anforderungen_map", {})
        logger.info(f"Resuming from checkpoint '{path}': {len(done)} G++ controls already done.")
        return done
    except Exception as e:
        logger.warning(f"Could not read checkpoint '{path}' ({e}); starting fresh.")
        return {}


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

    # Load source catalogs (the loaders transparently download from GitHub).
    gpp_catalog = load_json_file(GPP_KOMPENDIUM_JSON_PATH, expected_sha256=GPP_CATALOG_PIN_SHA256)
    bsi_catalog = load_json_file(BSI_2023_JSON_PATH)
    if not gpp_catalog or not bsi_catalog:
        logger.error("Failed to load G++ Kompendium or BSI ED2023 catalog. Aborting stage.")
        return

    prompt_config = load_json_file(PROMPT_CONFIG_PATH)
    schema = load_json_file(ED23_ANFORDERUNGEN_RESPONSE_SCHEMA_PATH)
    verify_schema = load_json_file(ED23_VERIFY_RESPONSE_SCHEMA_PATH)
    system_instruction = prompt_config["ed23_abgleich_system"]
    prompt_template = prompt_config["ed23_abgleich_prompt"]
    verify_prompt_template = prompt_config["ed23_abgleich_verify_prompt"]

    # G++ controls to map (all of them), each with statement, guidance, and Praktik siblings.
    gpp_controls = build_gpp_match_contexts(gpp_catalog)
    logger.info(f"Extracted {len(gpp_controls)} G++ controls with Praktik context.")

    # Stripped ED2023 corpus used as the cached grounding context.
    stripped, id_lookup = build_ed23_corpus(bsi_catalog)
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

    # Resume support: load already-computed controls and only query the remaining ones. Each
    # completed control is appended to the checkpoint immediately, so a crash loses at most the
    # controls that were still in flight.
    final_map: Dict[str, List[Dict[str, Any]]] = _load_checkpoint(CHECKPOINT_PATH)
    pending = [(cid, control) for cid, control in control_items if cid not in final_map]
    checkpoint_lock = asyncio.Lock()

    semaphore = asyncio.Semaphore(app_config.max_concurrent_ai_requests)
    logger.info(
        f"Matching {len(pending)} of {len(control_items)} G++ controls against the ED2023 corpus "
        f"({len(final_map)} restored from checkpoint)..."
    )

    async def _match_and_checkpoint(cid: str, control: Dict[str, Any]) -> None:
        control_id, matches = await match_and_verify_control(
            ai_client, cid, control, prompt_template, schema,
            verify_prompt_template, verify_schema, id_lookup, saetze_by_id,
            cached_content, inline_prefix, semaphore,
        )
        # Serialize writes so the checkpoint file stays consistent under concurrency.
        async with checkpoint_lock:
            final_map[control_id] = matches
            _atomic_save_json({"gpp_ed23_anforderungen_map": final_map}, CHECKPOINT_PATH)

    if pending:
        try:
            await asyncio.gather(*(_match_and_checkpoint(cid, c) for cid, c in pending))
        finally:
            ai_client.delete_context_cache(cached_content)
    else:
        ai_client.delete_context_cache(cached_content)
        logger.info("All G++ controls already present in checkpoint; nothing to query.")

    # The .partial checkpoint stays in the internal {control_id: [matches]} shape (simple to
    # resume); only the final, published artifact is serialized as OSCAL.
    output_data = to_oscal_mapping_collection(final_map)
    save_json_file(output_data, GPP_ED23_ANFORDERUNGEN_JSON_PATH)
    # Final output is committed; the checkpoint is now redundant.
    if os.path.exists(CHECKPOINT_PATH):
        os.remove(CHECKPOINT_PATH)
    total = sum(len(m) for m in final_map.values())
    logger.info(
        f"stage_ed23_anforderungen finished. Mapped {len(final_map)} G++ controls "
        f"to {total} ED2023 Anforderung references."
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    asyncio.run(run_stage_ed23_anforderungen())
