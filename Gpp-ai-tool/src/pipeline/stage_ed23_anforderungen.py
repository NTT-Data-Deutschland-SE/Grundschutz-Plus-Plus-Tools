"""
Pipeline Stage: G++ control → BSI Edition-2023 Anforderungen mapping.

For every G++ control this stage asks the AI which BSI ED2023 Anforderungen match it, and
writes the result as an OSCAL 1.2.2 Control Mapping document
(`hilfsdateien/gpp_ed23_anforderungen.json`, root `mapping-collection`) consumed by the
GS++-oscal-app to show a "Zeige BSI ED23 Anforderungen" panel per control — replacing the old
runtime, web-search-grounded AI call in GSpp-Viewer that frequently hallucinated IDs. The
internal per-control match map is serialized via `utils.oscal_mapping`.

Grounding: the full ED2023 OSCAL catalog (BSI_2023_JSON) is stripped to a compact
`id | name | prose` corpus of every Anforderung and supplied as the model's context. Because
that corpus is identical for every control query, it is put into an explicit Vertex AI context
cache once and reused per call (implicit caching does not engage for this model/region). Every
returned ID is post-filtered against the real corpus so hallucinated / old-edition IDs cannot
reach the output.
"""

import asyncio
import json
import logging
import os
import tempfile
from typing import Any, Dict, List, Tuple

from config import app_config
from clients.ai_client import AiClient
from utils.data_loader import load_json_file, save_json_file
from utils.oscal_utils import extract_all_gpp_controls, normalize_id
from utils.oscal_mapping import to_oscal_mapping_collection
from constants import (
    GPP_KOMPENDIUM_JSON_PATH,
    GPP_CATALOG_PIN_SHA256,
    BSI_2023_JSON_PATH,
    GPP_ED23_ANFORDERUNGEN_JSON_PATH,
    ED23_ANFORDERUNGEN_STRIPPED_JSON_PATH,
    ED23_ANFORDERUNGEN_RESPONSE_SCHEMA_PATH,
    PROMPT_CONFIG_PATH,
)

logger = logging.getLogger(__name__)


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


def build_ed23_corpus(bsi_catalog: Dict[str, Any]) -> Tuple[List[Dict[str, str]], Dict[str, Dict[str, str]]]:
    """Strips the ED2023 catalog to every Anforderung as `{id, name, prose}`.

    Returns the stripped list and a lookup keyed by normalized id → `{id, name}` so the AI's
    returned IDs can be validated and their canonical id/name restored. Nested sub-controls
    are included.
    """
    stripped: List[Dict[str, str]] = []
    lookup: Dict[str, Dict[str, str]] = {}

    def walk_controls(controls):
        for control in controls or []:
            cid = control.get("id")
            if cid:
                name = control.get("title", "") or ""
                prose = (_statement_prose(control) or "").replace("\n", " ").strip()
                stripped.append({"id": cid, "name": name, "prose": prose})
                lookup[normalize_id(cid)] = {"id": cid, "name": name}
            if control.get("controls"):
                walk_controls(control["controls"])

    def walk_groups(groups):
        for group in groups or []:
            walk_controls(group.get("controls", []))
            if group.get("groups"):
                walk_groups(group["groups"])

    walk_groups(bsi_catalog.get("catalog", {}).get("groups", []))
    return stripped, lookup


def _corpus_text(stripped: List[Dict[str, str]]) -> str:
    """Renders the stripped corpus as one compact `id | name | prose` line per Anforderung."""
    return "\n".join(f"{a['id']} | {a['name']} | {a['prose']}" for a in stripped)


def _filter_matches(raw_matches: Any, id_lookup: Dict[str, Dict[str, str]]) -> List[Dict[str, str]]:
    """Keeps only matches whose ID really exists in the ED23 corpus; restores canonical id/name."""
    result: List[Dict[str, str]] = []
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
        result.append({
            "id": canonical["id"],
            "name": canonical["name"],
            "begruendung": item.get("begruendung", ""),
        })
    return result


async def _match_control(
    ai_client: AiClient,
    control_id: str,
    control: Dict[str, Any],
    prompt_template: str,
    schema: Dict[str, Any],
    id_lookup: Dict[str, Dict[str, str]],
    cached_content: str,
    inline_prefix: str,
    semaphore: asyncio.Semaphore,
) -> Tuple[str, List[Dict[str, str]]]:
    """Asks the AI for the ED23 Anforderungen matching one G++ control; returns filtered matches."""
    user_prompt = prompt_template.format(
        title=control.get("title", ""),
        prose=control.get("prose", ""),
        guidance="",
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
            )
        except Exception as e:
            logger.warning(f"AI matching failed for G++ control '{control_id}': {e}")
            return control_id, []

    matches = _filter_matches(response, id_lookup)
    logger.debug(f"Control '{control_id}': {len(matches)} ED23 Anforderung(en) matched.")
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


def _load_checkpoint(path: str) -> Dict[str, List[Dict[str, str]]]:
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
    system_instruction = prompt_config["ed23_abgleich_system"]
    prompt_template = prompt_config["ed23_abgleich_prompt"]

    # G++ controls to map (all of them).
    gpp_controls = extract_all_gpp_controls(gpp_catalog)
    logger.info(f"Extracted {len(gpp_controls)} G++ controls.")

    # Stripped ED2023 corpus used as the cached grounding context.
    stripped, id_lookup = build_ed23_corpus(bsi_catalog)
    corpus_text = _corpus_text(stripped)
    logger.info(f"Built ED2023 corpus with {len(stripped)} Anforderungen ({len(corpus_text)} chars).")
    save_json_file({"ed23_anforderungen": stripped}, ED23_ANFORDERUNGEN_STRIPPED_JSON_PATH)

    ai_client = AiClient(app_config)

    # Explicit context cache: the corpus is the cached content, the short ED23 system prompt the
    # cached system instruction. Reused across every per-control call.
    cached_content = ai_client.create_context_cache(content=corpus_text, system_instruction=system_instruction)
    # Fallback prefix inlined into each prompt when caching is unavailable (system + corpus).
    inline_prefix = (
        f"{system_instruction}\n\nVerfügbare BSI ED2023 Anforderungen "
        f"(Format: ID | Name | Beschreibung):\n{corpus_text}"
    )

    # Respect Test Mode (Rule 9.1): only the first 3 controls.
    control_items = list(gpp_controls.items())
    if app_config.is_test_mode:
        control_items = control_items[:3]
        logger.info("TEST mode: limiting to the first 3 G++ controls.")

    # Resume support: load already-computed controls and only query the remaining ones. Each
    # completed control is appended to the checkpoint immediately, so a crash loses at most the
    # controls that were still in flight.
    final_map: Dict[str, List[Dict[str, str]]] = _load_checkpoint(CHECKPOINT_PATH)
    pending = [(cid, control) for cid, control in control_items if cid not in final_map]
    checkpoint_lock = asyncio.Lock()

    semaphore = asyncio.Semaphore(app_config.max_concurrent_ai_requests)
    logger.info(
        f"Matching {len(pending)} of {len(control_items)} G++ controls against the ED2023 corpus "
        f"({len(final_map)} restored from checkpoint)..."
    )

    async def _match_and_checkpoint(cid: str, control: Dict[str, Any]) -> None:
        control_id, matches = await _match_control(
            ai_client, cid, control, prompt_template, schema, id_lookup,
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
