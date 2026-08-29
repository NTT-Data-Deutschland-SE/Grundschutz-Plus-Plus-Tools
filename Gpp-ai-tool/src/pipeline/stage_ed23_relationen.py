"""
Pipeline Stage: OSCAL relationship classification for the GS++ -> ED23 mapping.

Upgrades hilfsdateien/gpp_ed23_anforderungen.json in place: every one of the verified
(G++ control, ED23 Anforderung) map entries gets a differentiated OSCAL ``relationship``
token (equal-to / equivalent-to / subset-of / superset-of / intersects-with) instead of
the constant ``intersects-with``. The relationship makes the mapping usable for evidence
migration the way the BSI's GSMap collection is: the token tells whether an existing
Nachweis suffices (equal-to/equivalent-to), is too narrow (subset-of from the G++ side),
or only overlaps.

Method: one strict, self-contained classification call per existing pair (~3k calls, no
corpus cache needed) on GROUND_TRUTH_MODEL. Context per call: the G++ control (statement,
guidance, Praktik) and the ED23 Anforderung's numbered sentences from the stripped corpus
(the same corpus satz_nr indexes into), the carrying sentence marked. The mapping itself
is NOT changed — same pairs, same satz refs, same remarks; only the relationship field
per map entry differs, so the diff stays reviewable. OSCAL direction semantics: the token
describes the SOURCE (G++ control) relative to the TARGET (ED23 Anforderung). Note that
the BSI GSMap maps the opposite direction (ED23-UA -> GS++), so subset-of/superset-of
histograms of the two collections must be mirrored before comparing.

Resume: .partial checkpoint per control id. Skip guard: a mapping whose entries already
carry more than one distinct relationship value counts as classified (an unclassified
build is constantly intersects-with); OVERWRITE_TEMP_FILES=true forces reclassification.
Not part of the full pipeline — run explicitly via
`python src/main.py --stage stage_ed23_relationen`.
"""

import asyncio
import json
import logging
import os
import tempfile
import time
from typing import Any, Dict, List, Optional, Tuple

from config import app_config
from clients.ai_client import AiClient
from utils.data_loader import load_json_file, save_json_file
from utils.oscal_mapping import to_oscal_mapping_collection
from pipeline.stage_ed23_anforderungen import build_gpp_match_contexts
from constants import (
    GPP_KOMPENDIUM_JSON_PATH,
    GPP_CATALOG_PIN_SHA256,
    GPP_ED23_ANFORDERUNGEN_JSON_PATH,
    ED23_ANFORDERUNGEN_STRIPPED_JSON_PATH,
    ED23_RELATION_RESPONSE_SCHEMA_PATH,
    PROMPT_CONFIG_PATH,
)

logger = logging.getLogger(__name__)

CHECKPOINT_PATH = GPP_ED23_ANFORDERUNGEN_JSON_PATH + ".relationen.partial"
CHECKPOINT_KEY = "ed23_relationen_map"
DEFAULT_RELATIONSHIP = "intersects-with"


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


def _load_checkpoint(path: str) -> Dict[str, Any]:
    """Loads per-pair relationships from a prior run. Returns {} if absent/unreadable."""
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        done = data.get(CHECKPOINT_KEY, {})
        logger.info(f"Resuming from checkpoint '{path}': {len(done)} pairs already classified.")
        return done
    except Exception as e:
        logger.warning(f"Could not read checkpoint '{path}' ({e}); starting fresh.")
        return {}


def load_mapping_matches(doc: Dict[str, Any]) -> Dict[str, List[Dict[str, Any]]]:
    """Parses the OSCAL mapping-collection back into the internal per-control match map.

    Inverse of utils.oscal_mapping.to_oscal_mapping_collection: label prop -> name,
    statement-sentence prop -> satz_nr, remarks -> begruendung, relationship kept.
    """
    per_control: Dict[str, List[Dict[str, Any]]] = {}
    for mapping in doc.get("mapping-collection", {}).get("mappings", []) or []:
        for entry in mapping.get("maps", []) or []:
            sources = [s.get("id-ref") for s in entry.get("sources", []) if s.get("id-ref")]
            richtung = next(
                (p.get("value") for p in entry.get("props", []) or []
                 if p.get("name") == "matching-direction"),
                None,
            )
            for target in entry.get("targets", []) or []:
                target_id = target.get("id-ref")
                if not target_id:
                    continue
                name, satz_nr = "", None
                for prop in target.get("props", []) or []:
                    if prop.get("name") == "label":
                        name = prop.get("value", "")
                    elif prop.get("name") == "statement-sentence":
                        try:
                            satz_nr = int(prop.get("value"))
                        except (TypeError, ValueError):
                            satz_nr = None
                for source in sources:
                    match: Dict[str, Any] = {
                        "id": target_id,
                        "name": name,
                        "begruendung": (entry.get("remarks") or "").strip(),
                        "satz_nr": satz_nr,
                        "relationship": entry.get("relationship"),
                    }
                    if richtung:
                        match["richtung"] = richtung
                    per_control.setdefault(source, []).append(match)
    return per_control


def _pair_key(control_id: str, match: Dict[str, Any]) -> str:
    # Includes the satz_nr: after the merge with the ED23-seitige Satz-Abdeckung one
    # (control, Anforderung) pair may carry several entries, one per Teilanforderung,
    # each classified on its own carrying sentence.
    return f"{control_id}|{match['id']}|{match.get('satz_nr') or 0}"


def _numbered_saetze(saetze: List[str], carrying: Optional[int]) -> str:
    lines = []
    for i, satz in enumerate(saetze, start=1):
        marker = " [tragend]" if carrying == i else ""
        lines.append(f"(S{i}){marker} {satz}")
    return "\n".join(lines) or "(keine)"


async def _classify_pair(
    ai_client: AiClient,
    control_id: str,
    control: Dict[str, str],
    match: Dict[str, Any],
    saetze_by_id: Dict[str, List[str]],
    prompt_template: str,
    schema: Dict[str, Any],
    semaphore: asyncio.Semaphore,
) -> Tuple[str, Optional[str]]:
    """Classifies one pair; returns (pair_key, relationship or None on failure)."""
    prompt = prompt_template.format(
        praktik=control.get("praktik", ""),
        control_id=control_id,
        title=control.get("title", ""),
        prose=control.get("prose", ""),
        guidance=control.get("guidance") or "(keine)",
        anf_id=match["id"],
        anf_name=match["name"],
        anf_saetze=_numbered_saetze(saetze_by_id.get(match["id"], []), match.get("satz_nr")),
        begruendung=match.get("begruendung") or "(keine)",
    )
    async with semaphore:
        try:
            verdict = await ai_client.generate_validated_json_response(
                prompt=prompt,
                json_schema=schema,
                request_context_log=f"ED23Relation-{control_id}-{match['id']}",
            )
        except Exception as e:
            logger.warning(
                f"Relation classification failed for '{control_id}' -> '{match['id']}': {e}; "
                f"keeping {DEFAULT_RELATIONSHIP}."
            )
            return _pair_key(control_id, match), None
    relationship = verdict.get("relationship") if isinstance(verdict, dict) else None
    return _pair_key(control_id, match), relationship


async def run_stage_ed23_relationen() -> None:
    """Main entry point for the relationship classification pass."""
    logger.info("Starting stage_ed23_relationen...")

    with open(GPP_ED23_ANFORDERUNGEN_JSON_PATH, "r", encoding="utf-8") as f:
        mapping_doc = json.load(f)
    per_control = load_mapping_matches(mapping_doc)
    all_pairs = [(cid, m) for cid, matches in per_control.items() for m in matches]
    distinct_relations = {m.get("relationship") for _, m in all_pairs}
    if len(distinct_relations - {None}) > 1 and not app_config.overwrite_temp_files:
        logger.info(
            "Mapping already carries differentiated relationships "
            f"({sorted(r for r in distinct_relations if r)}) and OVERWRITE_TEMP_FILES is "
            "false. Skipping stage_ed23_relationen."
        )
        return
    logger.info(f"Loaded mapping: {len(per_control)} controls, {len(all_pairs)} pairs.")

    gpp_catalog = load_json_file(GPP_KOMPENDIUM_JSON_PATH, expected_sha256=GPP_CATALOG_PIN_SHA256)
    stripped_doc = load_json_file(ED23_ANFORDERUNGEN_STRIPPED_JSON_PATH)
    if not gpp_catalog or not stripped_doc:
        logger.error("Failed to load G++ catalog or stripped ED23 corpus. Aborting stage.")
        return
    gpp_contexts = build_gpp_match_contexts(gpp_catalog)
    saetze_by_id = {
        a["id"]: a.get("saetze", []) or []
        for a in stripped_doc.get("ed23_anforderungen", [])
    }

    prompt_config = load_json_file(PROMPT_CONFIG_PATH)
    prompt_template = prompt_config["ed23_relation_prompt"]
    schema = load_json_file(ED23_RELATION_RESPONSE_SCHEMA_PATH)
    ai_client = AiClient(app_config)

    # Respect Test Mode (Rule 9.1): only the pairs of the first 3 controls.
    if app_config.is_test_mode:
        test_controls = sorted(per_control)[:3]
        all_pairs = [(cid, m) for cid, m in all_pairs if cid in test_controls]
        logger.info(f"TEST mode: limiting to {len(all_pairs)} pairs of 3 controls.")

    classified: Dict[str, str] = _load_checkpoint(CHECKPOINT_PATH)
    pending = [
        (cid, m) for cid, m in all_pairs if _pair_key(cid, m) not in classified
    ]
    checkpoint_lock = asyncio.Lock()
    semaphore = asyncio.Semaphore(app_config.max_concurrent_ai_requests)
    logger.info(
        f"Classifying {len(pending)} of {len(all_pairs)} pairs "
        f"({len(classified)} restored from checkpoint)..."
    )

    # Checkpoint every N classifications instead of every single one: 3k full-file writes
    # in quick succession invite transient Windows file locks and buy no extra safety.
    checkpoint_every = 25
    since_checkpoint = 0

    async def _classify_and_checkpoint(cid: str, match: Dict[str, Any]) -> None:
        nonlocal since_checkpoint
        control = gpp_contexts.get(cid)
        if control is None:
            logger.warning(f"Control '{cid}' not in pinned G++ catalog; keeping default relation.")
            return
        key, relationship = await _classify_pair(
            ai_client, cid, control, match, saetze_by_id, prompt_template, schema, semaphore,
        )
        if relationship:
            async with checkpoint_lock:
                classified[key] = relationship
                since_checkpoint += 1
                if since_checkpoint >= checkpoint_every:
                    _atomic_save_json({CHECKPOINT_KEY: classified}, CHECKPOINT_PATH)
                    since_checkpoint = 0

    if pending:
        await asyncio.gather(*(_classify_and_checkpoint(cid, m) for cid, m in pending))

    # Apply classifications and re-serialize. Pairs without a verdict keep the default,
    # explicitly, so the output never contains a null relationship.
    histogram: Dict[str, int] = {}
    for cid, match in all_pairs:
        relationship = classified.get(_pair_key(cid, match)) or DEFAULT_RELATIONSHIP
        match["relationship"] = relationship
        histogram[relationship] = histogram.get(relationship, 0) + 1

    output = to_oscal_mapping_collection(per_control)
    save_json_file(output, GPP_ED23_ANFORDERUNGEN_JSON_PATH)
    if os.path.exists(CHECKPOINT_PATH) and len(classified) >= len(all_pairs):
        os.remove(CHECKPOINT_PATH)
    logger.info(
        f"stage_ed23_relationen finished. {len(classified)} of {len(all_pairs)} pairs "
        f"classified; distribution: {dict(sorted(histogram.items()))}."
    )
    ai_client.log_usage_summary("stage_ed23_relationen")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    asyncio.run(run_stage_ed23_relationen())
