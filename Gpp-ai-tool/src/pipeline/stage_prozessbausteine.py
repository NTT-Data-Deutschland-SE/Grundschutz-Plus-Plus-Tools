"""
Pipeline Stage: BSI Edition-2023 Prozessbaustein-Anforderung → G++ control mapping.

For every Anforderung in the prozessorientierte ED2023 layers (ISMS, ORP, CON, OPS, DER) this
stage asks the AI for the *single* best-matching G++ control and writes the result to
`hilfsdateien/prozessbausteine_mapping.json` (root key `prozessbausteine_mapping`, a flat
`{ed23_anforderung_id: gpp_control_id}` object). That file used to be a hand-maintained asset
in `src/assets/json/`; this stage regenerates it from the two upstream catalogs instead.

Direction: this is the inverse of `stage_ed23_anforderungen`, which maps G++ → many ED2023.
Here the mapping is 1:1 and ED2023-driven.

Completeness: the stage runs in rounds until *every* Anforderung has exactly one valid G++
match. Round 1 lets the model decline a match; the following rounds re-query only the
unmatched remainder with a stricter prompt that requires choosing the closest available
control. The final artifact is only written (and the checkpoint only deleted) once coverage
is complete — a run that cannot reach completeness within PROZESSBAUSTEINE_MAX_ROUNDS keeps
its checkpoint and raises, so an incomplete mapping is never published and never blocks a
later resume via the idempotency guard. In TEST mode no final artifact is written at all.

Grounding: the full G++ catalog is stripped to a compact `id | title | prose` corpus and put
into an explicit Vertex AI context cache once, then reused by every chunk request. The ED2023
Anforderungen are sent in chunks so each request's *output* stays small and every 1:1 decision
is made in a context the model can still reason over reliably. Because the mapping requires
weighing near-miss candidates, the chunks are answered by the Pro model, which runs with
thinking enabled (see `AiClient.generate_validated_json_response`).

Every returned G++ ID is post-filtered against the real corpus, so hallucinated IDs cannot
reach the output.
"""

import asyncio
import json
import logging
import os
from typing import Any, Dict, List, Tuple

from config import app_config
from clients.ai_client import AiClient
from utils.data_loader import load_json_file, save_json_file
from utils.oscal_utils import extract_all_gpp_controls, normalize_id
from utils.ed23_xml import fetch_official_xml, load_official_xml
# Reused from the sibling ED2023 stage: display-label builder and the crash-safe
# checkpoint writer. Duplicating either would risk them drifting apart.
from pipeline.stage_ed23_anforderungen import anforderung_label, _atomic_save_json
from constants import (
    GPP_KOMPENDIUM_JSON_PATH,
    GPP_CATALOG_PIN_SHA256,
    PROZZESSBAUSTEINE_CONTROLS_JSON_PATH,
    PROZESSBAUSTEINE_RESPONSE_SCHEMA_PATH,
    PROZESSBAUSTEINE_LAYERS,
    PROZESSBAUSTEINE_CHUNK_SIZE,
    PROZESSBAUSTEINE_MAX_ROUNDS,
    GROUND_TRUTH_MODEL_PRO,
    PROMPT_CONFIG_PATH,
)

logger = logging.getLogger(__name__)

# Holds the per-Anforderung results accumulated so far, so a crashed or interrupted run can be
# resumed instead of re-querying every chunk. Deleted once the final output is written.
CHECKPOINT_PATH = PROZZESSBAUSTEINE_CONTROLS_JSON_PATH + ".partial"


def collect_prozess_anforderungen(official: Dict[str, Any]) -> List[Dict[str, str]]:
    """Returns every active Anforderung of the prozessorientierte layers as `{id, name, prose}`.

    Input is the `{req_id: record}` map from utils.ed23_xml.load_official_xml — the amtliche
    Wortlaut of the Kompendium, no derived edition. Filtered to the Schichten listed in
    `PROZESSBAUSTEINE_LAYERS`; ENTFALLEN requirements are skipped.
    """
    collected: List[Dict[str, str]] = []
    for req in sorted(official.values(), key=lambda r: r["id"]):
        if req.get("entfallen") or req.get("schicht") not in PROZESSBAUSTEINE_LAYERS:
            continue
        collected.append({
            "id": req["id"],
            "name": anforderung_label(req),
            "prose": " ".join(req.get("saetze") or []),
        })
    return collected


def build_gpp_corpus(gpp_catalog: Dict[str, Any]) -> Tuple[str, Dict[str, str]]:
    """Renders the G++ catalog as an `id | title | prose` corpus plus a normalized-id lookup.

    The lookup maps `normalize_id(id) → canonical id` so IDs the model returns in a different
    case or with stray whitespace still validate, while anything not in the catalog is dropped.
    """
    controls = extract_all_gpp_controls(gpp_catalog)
    lines = []
    lookup: Dict[str, str] = {}
    for cid, data in controls.items():
        prose = (data.get("prose", "") or "").replace("\n", " ").strip()
        lines.append(f"{cid} | {data.get('title', '')} | {prose}")
        lookup[normalize_id(cid)] = cid
    return "\n".join(lines), lookup


def _chunk_text(chunk: List[Dict[str, str]]) -> str:
    """Renders one chunk of ED2023 Anforderungen as compact `id | name | prose` lines."""
    return "\n".join(f"{a['id']} | {a['name']} | {a['prose']}" for a in chunk)


def _filter_chunk_response(
    raw: Any,
    chunk: List[Dict[str, str]],
    gpp_lookup: Dict[str, str],
) -> Dict[str, str]:
    """Validates one chunk's response into `{ed23_id: gpp_id}`, dropping anything unusable.

    Guards against the three ways a response can be wrong: an ED2023 ID that was not in the
    chunk (the model inventing or mangling a key), a G++ ID that does not exist in the catalog,
    and a deliberate "no match" empty string. All three are skipped rather than written out.
    """
    result: Dict[str, str] = {}
    if not isinstance(raw, list):
        logger.warning("Chunk response was not a list; discarding it.")
        return result

    requested = {a["id"] for a in chunk}
    for item in raw:
        if not isinstance(item, dict):
            continue
        bsi_id = str(item.get("bsi_control_id", "")).strip()
        gpp_raw = str(item.get("matched_gpp_control_id", "")).strip()
        if bsi_id not in requested:
            logger.warning(f"Response contained ED2023 ID '{bsi_id}' that was not in the chunk; skipping.")
            continue
        if not gpp_raw:
            logger.debug(f"No G++ match reported for '{bsi_id}'.")
            continue
        canonical = gpp_lookup.get(normalize_id(gpp_raw))
        if not canonical:
            logger.warning(f"Discarding hallucinated G++ ID '{gpp_raw}' for ED2023 '{bsi_id}'.")
            continue
        result[bsi_id] = canonical
    return result


async def _match_chunk(
    ai_client: AiClient,
    index: int,
    chunk: List[Dict[str, str]],
    prompt_template: str,
    schema: Dict[str, Any],
    gpp_lookup: Dict[str, str],
    cached_content,
    inline_prefix: str,
    semaphore: asyncio.Semaphore,
) -> Dict[str, str]:
    """Asks the AI for the best G++ match for every Anforderung in one chunk."""
    user_prompt = prompt_template.format(chunk=_chunk_text(chunk))
    # When the cache is unavailable, inline the system instruction + corpus so grounding still applies.
    prompt = user_prompt if cached_content else f"{inline_prefix}\n\n{user_prompt}"

    async with semaphore:
        try:
            response = await ai_client.generate_validated_json_response(
                prompt=prompt,
                json_schema=schema,
                request_context_log=f"Prozessbausteine-chunk{index}",
                model_override=GROUND_TRUTH_MODEL_PRO,
                cached_content=cached_content,
            )
        except Exception as e:
            logger.warning(f"AI matching failed for chunk {index} ({len(chunk)} Anforderungen): {e}")
            return {}

    matched = _filter_chunk_response(response, chunk, gpp_lookup)
    logger.info(f"Chunk {index}: {len(matched)}/{len(chunk)} Anforderungen mapped.")
    return matched


def _load_mapping_file(path: str) -> Dict[str, str]:
    """Loads a `{prozessbausteine_mapping: {...}}` file. Returns {} if absent or unreadable.

    Reads the file directly (not via the lru_cached `load_json_file`) because checkpoint and
    output files change on disk during/between runs, and a stale cached copy here would make
    the resume logic reason about the wrong state.
    """
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return dict((data or {}).get("prozessbausteine_mapping", {}))
    except Exception as e:
        logger.warning(f"Could not read mapping file '{path}' ({e}); ignoring it.")
        return {}


def _revalidate_mapping(
    mapping: Dict[str, str],
    valid_bsi_ids: set,
    gpp_lookup: Dict[str, str],
    source: str,
) -> Dict[str, str]:
    """Filters a previously stored mapping against the *current* catalogs.

    Checkpoints and prior outputs may have been produced against older catalog versions, so
    every entry is re-checked: the ED2023 ID must still exist in the current layer selection
    and the G++ ID must still exist in the current catalog (case-normalized to its canonical
    form). Anything else is dropped and will simply be re-queried — this keeps the module's
    guarantee that no stale or hallucinated ID can reach the output, even across resumes.
    """
    result: Dict[str, str] = {}
    dropped = 0
    for bsi_id, gpp_id in mapping.items():
        canonical = gpp_lookup.get(normalize_id(gpp_id))
        if bsi_id in valid_bsi_ids and canonical:
            result[bsi_id] = canonical
        else:
            dropped += 1
    if dropped:
        logger.info(f"Revalidated {source}: kept {len(result)}, dropped {dropped} stale entries.")
    elif result:
        logger.info(f"Revalidated {source}: all {len(result)} entries still valid.")
    return result


async def run_stage_prozessbausteine() -> None:
    """Main entry point for the ED2023 Prozessbaustein → G++ mapping stage."""
    logger.info("Starting stage_prozessbausteine...")

    gpp_catalog = load_json_file(GPP_KOMPENDIUM_JSON_PATH, expected_sha256=GPP_CATALOG_PIN_SHA256)
    if not gpp_catalog:
        logger.error("Failed to load G++ Kompendium. Aborting stage.")
        return
    # OFFICIAL ED23 XML Kompendium (sha256-pinned) — the amtliche Wortlaut is the only basis.
    xml_bytes, _xml_sha = fetch_official_xml()
    official, _rejected = load_official_xml(xml_bytes)

    prompt_config = load_json_file(PROMPT_CONFIG_PATH)
    schema = load_json_file(PROZESSBAUSTEINE_RESPONSE_SCHEMA_PATH)
    system_instruction = prompt_config["prozessbausteine_system"]
    prompt_template = prompt_config["prozessbausteine_prompt"]
    prompt_template_force = prompt_config["prozessbausteine_prompt_force"]

    anforderungen = collect_prozess_anforderungen(official)
    if not anforderungen:
        logger.error(
            f"No Anforderungen found in ED2023 layers {PROZESSBAUSTEINE_LAYERS}. Aborting stage."
        )
        return
    valid_bsi_ids = {a["id"] for a in anforderungen}
    logger.info(
        f"Collected {len(anforderungen)} Anforderungen from ED2023 layers "
        f"{', '.join(PROZESSBAUSTEINE_LAYERS)}."
    )

    corpus_text, gpp_lookup = build_gpp_corpus(gpp_catalog)
    logger.info(f"Built G++ corpus with {len(gpp_lookup)} controls ({len(corpus_text)} chars).")

    # Resume state: the checkpoint of an interrupted run, plus — unless a fresh mapping was
    # requested via OVERWRITE_TEMP_FILES — the previously published output. Both are
    # revalidated against the *current* catalogs so stale entries get re-queried, never reused.
    final_map: Dict[str, str] = {}
    if not app_config.overwrite_temp_files:
        final_map.update(_revalidate_mapping(
            _load_mapping_file(PROZZESSBAUSTEINE_CONTROLS_JSON_PATH),
            valid_bsi_ids, gpp_lookup, "existing output",
        ))
    final_map.update(_revalidate_mapping(
        _load_mapping_file(CHECKPOINT_PATH), valid_bsi_ids, gpp_lookup, "checkpoint",
    ))

    # Idempotency (Rule 5.2.7), completeness-aware: only a *fully covering* existing output
    # may short-circuit the stage. An incomplete file (e.g. from an older version that
    # published partial results) is treated as resume state instead of blocking forever.
    if not app_config.overwrite_temp_files and valid_bsi_ids <= set(final_map):
        logger.info(
            "Existing output already maps every Anforderung and OVERWRITE_TEMP_FILES is "
            "false. Skipping stage_prozessbausteine."
        )
        return

    ai_client = AiClient(app_config)

    # The corpus is identical for every chunk, so it is cached once against the Pro model and
    # attached per request instead of being re-sent (and re-billed) each time.
    cached_content = ai_client.create_context_cache(
        content=corpus_text,
        system_instruction=system_instruction,
        model_override=GROUND_TRUTH_MODEL_PRO,
    )
    inline_prefix = (
        f"{system_instruction}\n\nVerfügbare G++-Maßnahmen "
        f"(Format: ID | Titel | Beschreibung):\n{corpus_text}"
    )

    checkpoint_lock = asyncio.Lock()
    semaphore = asyncio.Semaphore(app_config.max_concurrent_ai_requests)

    async def _match_and_checkpoint(index: int, chunk: List[Dict[str, str]], template: str) -> None:
        matched = await _match_chunk(
            ai_client, index, chunk, template, schema, gpp_lookup,
            cached_content, inline_prefix, semaphore,
        )
        # Serialize writes so the checkpoint file stays consistent under concurrency.
        async with checkpoint_lock:
            final_map.update(matched)
            _atomic_save_json({"prozessbausteine_mapping": final_map}, CHECKPOINT_PATH)

    # Query rounds: round 1 offers the model a "no match" escape hatch (best judgment
    # quality); every later round re-queries only the unmatched remainder with the force
    # prompt, which requires picking the closest available control. Failed chunks simply
    # leave their Anforderungen unmatched, so transient API errors are retried in the next
    # round instead of silently truncating the result (review finding: incomplete publish).
    try:
        rounds = 0
        while True:
            pending = [a for a in anforderungen if a["id"] not in final_map]
            if not pending:
                break
            rounds += 1
            if rounds > PROZESSBAUSTEINE_MAX_ROUNDS:
                unmatched_ids = [a["id"] for a in pending]
                logger.critical(
                    f"{len(unmatched_ids)} Anforderungen still unmapped after "
                    f"{PROZESSBAUSTEINE_MAX_ROUNDS} rounds: {', '.join(unmatched_ids)}. "
                    f"Keeping checkpoint '{CHECKPOINT_PATH}' for resume; NOT publishing an "
                    f"incomplete mapping."
                )
                raise RuntimeError(
                    f"stage_prozessbausteine could not map {len(unmatched_ids)} Anforderungen "
                    f"within {PROZESSBAUSTEINE_MAX_ROUNDS} rounds."
                )

            template = prompt_template if rounds == 1 else prompt_template_force
            # Stubborn items get smaller chunks in retry rounds so each decision stands alone.
            chunk_size = PROZESSBAUSTEINE_CHUNK_SIZE if rounds == 1 else max(1, min(PROZESSBAUSTEINE_CHUNK_SIZE, 5))
            chunks = [pending[i:i + chunk_size] for i in range(0, len(pending), chunk_size)]

            # Respect Test Mode (Rule 9.1): only the first 2 chunks of a single round.
            if app_config.is_test_mode:
                chunks = chunks[:2]
                logger.info("TEST mode: limiting to the first 2 chunks of round 1.")

            logger.info(
                f"Round {rounds}: mapping {len(pending)} pending Anforderungen in "
                f"{len(chunks)} chunk(s) of {chunk_size} using {GROUND_TRUTH_MODEL_PRO} "
                f"({len(final_map)} already mapped)."
            )
            await asyncio.gather(
                *(_match_and_checkpoint(i, c, template) for i, c in enumerate(chunks))
            )

            if app_config.is_test_mode:
                logger.info(
                    "TEST mode: stopping after one round; final artifact is NOT written "
                    f"(checkpoint kept at '{CHECKPOINT_PATH}')."
                )
                return
    finally:
        ai_client.delete_context_cache(cached_content)

    # Complete coverage reached — publish. Emit in catalog order rather than completion
    # order, so reruns produce a stable diff.
    ordered = {a["id"]: final_map[a["id"]] for a in anforderungen}
    save_json_file({"prozessbausteine_mapping": ordered}, PROZZESSBAUSTEINE_CONTROLS_JSON_PATH)
    if os.path.exists(CHECKPOINT_PATH):
        os.remove(CHECKPOINT_PATH)

    logger.info(
        f"stage_prozessbausteine finished. Mapped all {len(ordered)} Anforderungen to "
        f"G++ controls in {rounds} round(s)."
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    asyncio.run(run_stage_prozessbausteine())
