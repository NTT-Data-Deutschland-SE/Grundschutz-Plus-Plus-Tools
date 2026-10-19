"""
This module contains the logic for matching BSI Bausteine to G++ Zielobjekte.
"""
import asyncio
import json
import logging
import os
from typing import Dict, Any, List, Optional, Tuple

from config import app_config
from clients.ai_client import AiClient
from utils.data_loader import load_json_file, save_json_file, load_zielobjekte_csv, zielobjekt_row_name
from utils.data_parser import find_bausteine_with_prose
from constants import *

logger = logging.getLogger(__name__)


async def match_baustein_to_zielobjekt(
    ai_client: AiClient,
    baustein: Dict[str, Any],
    zielobjekte_map: Dict[str, Any],
    prompt_instruction: str,
    schema: Dict[str, Any],
    semaphore: asyncio.Semaphore,
) -> tuple[str, str | None]:
    """
    Matches a BSI Baustein to the best G++ Zielobjekt using an AI model.

    Args:
        ai_client: The AI client instance.
        baustein: The Baustein object to match.
        zielobjekte_map: A map of available Zielobjekte.
        prompt_instruction: The base prompt instruction.
        schema: The JSON schema for the expected response.
        semaphore: The asyncio semaphore for concurrency control.

    Returns:
        A tuple of (baustein_id, matched_zielobjekt_uuid) or (baustein_id, None).
    """
    baustein_id = baustein.get("id", "unknown")
    zielobjekte_choices = "\n".join(
        [
            f"* {data.get('Zielobjekt', '')}: {data.get('Definition', '')}"
            + (f" Beispiele: {data['Beispiel']}" if data.get("Beispiel") else "")
            for data in zielobjekte_map.values()
        ]
    )

    prompt = (
        f"{prompt_instruction}\n\n"
        f"**BSI Baustein to Match:**\n"
        f"* Title: {baustein.get('title', '')}\n"
        f"* Description: {baustein.get('description', '')}\n\n"
        f"**Available G++ Zielobjekte:**\n"
        f"{zielobjekte_choices}\n\n"
        "Based on the information above, which is the best match?"
    )

    zielobjekt_names = [data.get("Zielobjekt", "") for data in zielobjekte_map.values()]
    
    # logger.info(f"PROMPT: {prompt}")

    response_json = None
    async with semaphore:
        response_json = await ai_client.generate_validated_json_response(
            prompt=prompt,
            json_schema=schema,
            request_context_log=f"BausteinToZielobjekt-{baustein_id}",
            thinking="low",  # one classification per Baustein: bulk work
        )

    if not response_json:
        logger.warning(
            f"No valid AI response for Baustein '{baustein_id}'. Skipping."
        )
        return baustein_id, None

    matched_zielobjekt_name = response_json.get("matched_zielobjekt")

    if matched_zielobjekt_name:
        for uuid, data in zielobjekte_map.items():
            if data.get("Zielobjekt") == matched_zielobjekt_name:
                logger.debug(
                    f"Successfully matched Baustein '{baustein.get('title')}' to "
                    f"Zielobjekt '{matched_zielobjekt_name}' (UUID: {uuid})."
                )
                return baustein_id, uuid

    logger.warning(f"Could not find a suitable match for Baustein '{baustein_id}'.")
    return baustein_id, None


def _load_existing_map(path: str) -> Dict[str, str]:
    """Reads the published map directly (not via the lru-cached loader: it changes on disk)."""
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return dict((json.load(f) or {}).get("baustein_zielobjekt_map", {}) or {})
    except Exception as e:  # noqa: BLE001 — a corrupt map is regenerated, with the reason logged
        logger.warning(f"Could not read existing map '{path}' ({e}); starting from an empty map.")
        return {}


async def run_stage_match_bausteine() -> None:
    """
    Main function to run the Baustein-to-Zielobjekt matching stage.

    Incremental: Bausteine that already have a mapping are kept (unless OVERWRITE_TEMP_FILES
    / --fresh), only the missing ones are sent to the model, entries whose Baustein no longer
    exists in the catalog are dropped. Adding a Baustein upstream therefore costs one call.
    """
    logger.info("Starting stage_match_bausteine...")

    # Load all necessary data
    bsi_data = load_json_file(BSI_2023_JSON_PATH, expected_sha256=ED23_BD_CATALOG_PIN_SHA256)
    zielobjekte_data = load_zielobjekte_csv(ZIELOBJEKTKATEGORIEN_CSV_PATH)
    prompt_config = load_json_file(PROMPT_CONFIG_PATH)
    schema = load_json_file(BAUSTEIN_TO_ZIELOBJEKT_SCHEMA_PATH)

    bausteine_with_prose = find_bausteine_with_prose(bsi_data)
    catalog_ids = {b["id"] for b in bausteine_with_prose}
    existing = {} if app_config.overwrite_temp_files else _load_existing_map(BAUSTEIN_ZIELOBJEKT_JSON_PATH)
    stale = sorted(set(existing) - catalog_ids)
    if stale:
        logger.info(f"Dropping {len(stale)} mapped Bausteine no longer in the catalog selection: {', '.join(stale)}")
        existing = {k: v for k, v in existing.items() if k in catalog_ids}
    try:
        from utils.ed23_baustein import detect_ng
        plain = load_json_file(BSI_2023_PLAIN_JSON_PATH, expected_sha256=ED23_PLAIN_CATALOG_PIN_SHA256)
        ng_bausteine = detect_ng(bsi_data, plain)["bausteine"]
    except Exception as e:  # noqa: BLE001 — the NG flag is informational here; the match must not depend on it
        logger.warning(f"NG detection unavailable ({e}); matching continues without NG labels.")
        ng_bausteine = set()

    missing = [b for b in bausteine_with_prose if b["id"] not in existing]
    logger.info(
        f"resume: {len(existing)} Bausteine already mapped, {len(missing)} pending "
        f"(catalog selection {len(catalog_ids)}; NG among pending: "
        f"{', '.join(b['id'] for b in missing if b['id'] in ng_bausteine) or 'none'})."
    )
    if not missing:
        if stale:
            from utils.ed23_baustein import baustein_sort_key
            pruned = {k: existing[k] for k in sorted(existing, key=baustein_sort_key)}
            save_json_file({"baustein_zielobjekt_map": pruned}, BAUSTEIN_ZIELOBJEKT_JSON_PATH)
            logger.info(f"Wrote the pruned map ({len(existing)} Bausteine) to '{BAUSTEIN_ZIELOBJEKT_JSON_PATH}'.")
        logger.info("All Bausteine mapped; nothing to query.")
        return

    zielobjekte_map = {
        z["UUID"]: {
            "Zielobjekt": zielobjekt_row_name(z),
            "Definition": z.get("Definition", ""),
            # Since SdT a128311 the examples live in their own column, not in the definition.
            "Beispiel": (z.get("Beispiel") or "").strip(),
        }
        for z in zielobjekte_data
        if "UUID" in z and zielobjekt_row_name(z)
    }
    prompt_instruction = prompt_config["baustein_to_zielobjekt_prompt"]

    ai_client = AiClient(app_config)
    semaphore = asyncio.Semaphore(app_config.max_concurrent_ai_requests)

    # Respect Test Mode: only a few Bausteine.
    bausteine_to_process = missing[:3] if app_config.is_test_mode else missing
    logger.info(f"Starting AI matching for {len(bausteine_to_process)} Bausteine...")

    tasks = [
        match_baustein_to_zielobjekt(
            ai_client, baustein, zielobjekte_map, prompt_instruction, schema, semaphore,
        )
        for baustein in bausteine_to_process
    ]
    results = await asyncio.gather(*tasks)

    matched = 0
    for baustein_id, zielobjekt_uuid in results:
        if zielobjekt_uuid is None:
            continue
        existing[baustein_id] = zielobjekt_uuid
        matched += 1
        if baustein_id in ng_bausteine:
            logger.info(f"NG-Baustein {baustein_id} matched to Zielobjekt {zielobjekt_uuid}.")

    # Stable order (by Baustein id) so reruns produce a minimal diff.
    from utils.ed23_baustein import baustein_sort_key
    ordered = {k: existing[k] for k in sorted(existing, key=baustein_sort_key)}
    save_json_file({"baustein_zielobjekt_map": ordered}, BAUSTEIN_ZIELOBJEKT_JSON_PATH)
    ai_client.log_usage_summary("stage_match_bausteine")
    logger.info(
        f"Stage_match_bausteine finished. Newly matched {matched} of {len(bausteine_to_process)}; "
        f"map now holds {len(ordered)} Bausteine."
    )
