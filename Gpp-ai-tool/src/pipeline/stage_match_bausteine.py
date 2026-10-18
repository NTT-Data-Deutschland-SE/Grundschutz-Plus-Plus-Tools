"""
This module contains the logic for matching BSI Bausteine to G++ Zielobjekte.
"""
import asyncio
import logging
import os
from typing import Dict, Any, List, Optional, Tuple

from config import app_config
from clients.ai_client import AiClient
from utils.data_loader import load_json_file, save_json_file, load_zielobjekte_csv, zielobjekt_row_name
from utils.data_parser import find_bausteine_with_prose
from utils.file_utils import json_mapping_is_populated
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


async def run_stage_match_bausteine() -> None:
    """
    Main function to run the Baustein-to-Zielobjekt matching stage.
    """
    logger.info("Starting stage_match_bausteine...")

    # Idempotency Check (Rule 5.2.7): skip only if a VALID, non-empty map already exists.
    # An empty/corrupt file (e.g. left behind by a manual "clear") must be regenerated — otherwise
    # the downstream ED23 stage silently produces no per-Baustein profiles (the regression this fixes).
    if (
        json_mapping_is_populated(BAUSTEIN_ZIELOBJEKT_JSON_PATH, "baustein_zielobjekt_map")
        and not app_config.overwrite_temp_files
    ):
        logger.info(
            "Output file already exists with a non-empty map and OVERWRITE_TEMP_FILES is false. "
            "Skipping Baustein-to-Zielobjekt matching stage."
        )
        return

    # Load all necessary data
    bsi_data = load_json_file(BSI_2023_JSON_PATH)
    zielobjekte_data = load_zielobjekte_csv(ZIELOBJEKTKATEGORIEN_CSV_PATH)
    prompt_config = load_json_file(PROMPT_CONFIG_PATH)
    schema = load_json_file(BAUSTEIN_TO_ZIELOBJEKT_SCHEMA_PATH)

    # Prepare data for matching
    bausteine_with_prose = find_bausteine_with_prose(bsi_data)
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
    

    # Initialize AI client and Semaphore (Rule 5.3.1)
    ai_client = AiClient(app_config)
    semaphore = asyncio.Semaphore(app_config.max_concurrent_ai_requests)

    # Respect Test Mode (Rule 9.1)
    bausteine_to_process = (
        bausteine_with_prose[:3]
        if app_config.is_test_mode
        else bausteine_with_prose
    )

    # Run the asynchronous matching process
    logger.info(
        f"Starting AI matching for {len(bausteine_to_process)} Bausteine..."
    )

    tasks = [
        match_baustein_to_zielobjekt(
            ai_client,
            baustein,
            zielobjekte_map,
            prompt_instruction,
            schema,
            semaphore,
        )
        for baustein in bausteine_to_process
    ]
    results = await asyncio.gather(*tasks)

    # Filter out None results and construct the final map
    final_map = {
        baustein_id: zielobjekt_uuid
        for baustein_id, zielobjekt_uuid in results
        if zielobjekt_uuid is not None
    }

    # Save the results
    output_data = {"baustein_zielobjekt_map": final_map}
    logger.debug(
        f"Saving the final Baustein-Zielobjekt map to {BAUSTEIN_ZIELOBJEKT_JSON_PATH}..."
    )
    save_json_file(output_data, BAUSTEIN_ZIELOBJEKT_JSON_PATH)

    logger.info(
        f"Stage_match_bausteine finished. Matched {len(final_map)} Bausteine."
    )