"""
Pipeline Stage: Per-sentence coverage judgment of the OFFICIAL ED23 Kompendium by G++.

The inverse direction of stage_ed23_anforderungen, at Teilanforderung granularity: for
every normative sentence of every active Anforderung of the AMTLICHE Edition 2023 (the
BSI's published XML Kompendium — deliberately NOT the NTT OSCAL edition or the stripped
paraphrase corpus), the stage judges which G++ controls demand the same activity. The
result turns the reverse gap analysis (scripts/analyze_ed23_coverage.py) from a mapping
byproduct into an explicit content judgment per Teilanforderung: a sentence with zero
verified controls was SEEN by a generous candidate pass and still found nothing.

Method (maker-checker, mirroring the sister stage's proven precision measures):

* Query unit is one Anforderung (~1.8k queries), not one sentence — the maker sees all
  numbered sentences of the official wording (normative ones marked) and over-collects
  (satz_nr, control_id) candidates against the cached G++ corpus (recall pass, generous
  by instruction, on ED23_MAKER_MODEL).
* Every candidate pair is then re-judged by a strict, self-contained verification call
  (the sentence in its full requirement context + the candidate control's statement,
  guidance, and its Praktik siblings as explicit negative context) on the default
  GROUND_TRUTH_MODEL (precision pass). Only verified pairs reach the output.
* Control IDs are post-validated against the pinned G++ resolved catalog; satz numbers
  against the requirement's real sentence count. Sentence numbering uses the shared
  splitter (utils.sentence_split), so it is identical to every other ED23 artifact.

Output: hilfsdateien/ed23_satz_abdeckung.json — per Anforderung the sentence count, the
normative sentence numbers, and the verified (satz_nr -> G++ control) hits. The official
sentence TEXTS are deliberately not serialized (the repo does not republish Kompendium
prose); they are reproducible from the pinned XML via utils.ed23_xml.

Resume: a .partial checkpoint next to the output accumulates per-Anforderung results, so
a crashed run continues instead of re-querying everything. Not part of the full pipeline
(processing.py) — run explicitly via `python src/main.py --stage stage_ed23_satz_abdeckung`.
"""

import asyncio
import datetime
import json
import logging
import os
import tempfile
from typing import Any, Dict, List, Optional, Tuple

from config import app_config
from clients.ai_client import AiClient
from utils.data_loader import load_json_file, save_json_file
from utils.oscal_utils import normalize_id
from utils.ed23_xml import BSI_XML_URL, fetch_official_xml, load_official_xml
from pipeline.stage_ed23_anforderungen import build_gpp_match_contexts
from constants import (
    GPP_KOMPENDIUM_JSON_PATH,
    GPP_CATALOG_PIN_SHA256,
    ED23_SATZ_ABDECKUNG_JSON_PATH,
    ED23_SATZ_RESPONSE_SCHEMA_PATH,
    ED23_SATZ_VERIFY_RESPONSE_SCHEMA_PATH,
    ED23_MAKER_MODEL,
    GROUND_TRUTH_MODEL,
    PROMPT_CONFIG_PATH,
)

logger = logging.getLogger(__name__)

CHECKPOINT_PATH = ED23_SATZ_ABDECKUNG_JSON_PATH + ".partial"
CHECKPOINT_KEY = "ed23_satz_abdeckung_map"

_LEVEL_LABEL = {"B": "Basis (B)", "S": "Standard (S)", "H": "erhöhter Schutzbedarf (H)"}


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
    """Loads the per-Anforderung results from a prior run. Returns {} if absent/unreadable."""
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        done = data.get(CHECKPOINT_KEY, {})
        logger.info(f"Resuming from checkpoint '{path}': {len(done)} Anforderungen already done.")
        return done
    except Exception as e:
        logger.warning(f"Could not read checkpoint '{path}' ({e}); starting fresh.")
        return {}


def _numbered_saetze(req: Dict[str, Any]) -> str:
    """Renders the requirement's sentences as '(S1) [normativ] ...' lines for the prompts."""
    normative = set(req["normative_idx"])
    lines = []
    for i, satz in enumerate(req["saetze"], start=1):
        marker = " [normativ]" if i in normative else ""
        lines.append(f"(S{i}){marker} {satz}")
    return "\n".join(lines)


def _filter_candidates(
    raw: Any, req: Dict[str, Any], gpp_lookup: Dict[str, str], req_id: str
) -> List[Dict[str, Any]]:
    """Keeps only candidates with an existing G++ id and an in-range satz_nr; dedupes pairs.

    Restores the canonical G++ id casing. Out-of-range sentence numbers or unknown ids are
    dropped and logged — hallucinated references cannot reach the verification pass.
    """
    result: List[Dict[str, Any]] = []
    seen = set()
    if not isinstance(raw, list):
        return result
    n_saetze = len(req["saetze"])
    for item in raw:
        if not isinstance(item, dict):
            continue
        canonical = gpp_lookup.get(normalize_id(item.get("control_id", "")))
        satz_nr = item.get("satz_nr")
        if not canonical:
            logger.warning(
                f"Anforderung '{req_id}': unknown G++ id {item.get('control_id')!r}; dropping candidate."
            )
            continue
        if not isinstance(satz_nr, int) or not (1 <= satz_nr <= n_saetze):
            logger.warning(
                f"Anforderung '{req_id}': invalid satz_nr {satz_nr!r} for {canonical} "
                f"(has {n_saetze} sentence(s)); dropping candidate."
            )
            continue
        if (satz_nr, canonical) in seen:
            continue
        seen.add((satz_nr, canonical))
        result.append({
            "satz_nr": satz_nr,
            "control_id": canonical,
            "begruendung": (item.get("begruendung", "") or "").strip(),
        })
    return result


async def _collect_candidates(
    ai_client: AiClient,
    req: Dict[str, Any],
    prompt_template: str,
    schema: Dict[str, Any],
    gpp_lookup: Dict[str, str],
    cached_content,
    inline_prefix: str,
    semaphore: asyncio.Semaphore,
) -> List[Dict[str, Any]]:
    """Asks the AI for (satz, G++ control) *candidates* for one Anforderung (recall pass)."""
    user_prompt = prompt_template.format(
        anf_id=req["id"],
        anf_titel=req["titel"],
        level=_LEVEL_LABEL.get(req["level"], req["level"] or "unbestimmt"),
        rolle=req["rolle"] or "(keine)",
        saetze=_numbered_saetze(req),
    )
    prompt = user_prompt if cached_content else f"{inline_prefix}\n\n{user_prompt}"
    async with semaphore:
        try:
            response = await ai_client.generate_validated_json_response(
                prompt=prompt,
                json_schema=schema,
                request_context_log=f"ED23Satz-{req['id']}",
                cached_content=cached_content,
                model_override=ED23_MAKER_MODEL,
            )
        except Exception as e:
            logger.warning(f"AI candidate pass failed for Anforderung '{req['id']}': {e}")
            return []
    candidates = _filter_candidates(response, req, gpp_lookup, req["id"])
    logger.debug(f"Anforderung '{req['id']}': {len(candidates)} candidate pair(s) found.")
    return candidates


async def _verify_candidate(
    ai_client: AiClient,
    req: Dict[str, Any],
    candidate: Dict[str, Any],
    gpp_contexts: Dict[str, Dict[str, str]],
    verify_prompt_template: str,
    verify_schema: Dict[str, Any],
    semaphore: asyncio.Semaphore,
) -> Optional[Dict[str, Any]]:
    """Strictly re-judges one (satz, control) pair; returns the final hit or None (checker pass)."""
    control = gpp_contexts.get(candidate["control_id"], {})
    satz_nr = candidate["satz_nr"]
    prompt = verify_prompt_template.format(
        anf_id=req["id"],
        anf_titel=req["titel"],
        level=_LEVEL_LABEL.get(req["level"], req["level"] or "unbestimmt"),
        anf_saetze=_numbered_saetze(req),
        satz_nr=satz_nr,
        satz_text=req["saetze"][satz_nr - 1],
        control_id=candidate["control_id"],
        praktik=control.get("praktik", ""),
        control_title=control.get("title", ""),
        control_prose=control.get("prose", ""),
        control_guidance=control.get("guidance") or "(keine)",
        siblings=control.get("siblings") or "(keine)",
    )
    async with semaphore:
        try:
            verdict = await ai_client.generate_validated_json_response(
                prompt=prompt,
                json_schema=verify_schema,
                request_context_log=f"ED23SatzVerify-{req['id']}-S{satz_nr}-{candidate['control_id']}",
            )
        except Exception as e:
            logger.warning(
                f"Verification failed for '{req['id']}' S{satz_nr} -> "
                f"'{candidate['control_id']}': {e}; dropping candidate."
            )
            return None
    if not isinstance(verdict, dict) or not verdict.get("covers"):
        return None
    return {
        "satz_nr": satz_nr,
        "control_id": candidate["control_id"],
        "begruendung": (verdict.get("begruendung", "") or "").strip(),
    }


async def judge_requirement(
    ai_client: AiClient,
    req: Dict[str, Any],
    prompt_template: str,
    schema: Dict[str, Any],
    verify_prompt_template: str,
    verify_schema: Dict[str, Any],
    gpp_lookup: Dict[str, str],
    gpp_contexts: Dict[str, Dict[str, str]],
    cached_content,
    inline_prefix: str,
    semaphore: asyncio.Semaphore,
) -> Tuple[str, List[Dict[str, Any]]]:
    """Full maker-checker flow for one Anforderung: collect candidates, verify each pair."""
    if not req["normative_idx"]:
        # Nothing normative to judge (pure context prose) — record an explicit empty result.
        return req["id"], []
    candidates = await _collect_candidates(
        ai_client, req, prompt_template, schema, gpp_lookup, cached_content,
        inline_prefix, semaphore,
    )
    verified = await asyncio.gather(*(
        _verify_candidate(
            ai_client, req, candidate, gpp_contexts,
            verify_prompt_template, verify_schema, semaphore,
        )
        for candidate in candidates
    ))
    hits = sorted(
        (h for h in verified if h), key=lambda h: (h["satz_nr"], h["control_id"])
    )
    logger.debug(
        f"Anforderung '{req['id']}': {len(hits)} of {len(candidates)} candidate(s) verified."
    )
    return req["id"], hits


async def run_stage_ed23_satz_abdeckung() -> None:
    """Main entry point for the official-ED23 per-sentence coverage stage."""
    logger.info("Starting stage_ed23_satz_abdeckung...")

    # Idempotency (Rule 5.2.7): skip if output exists and overwriting is disabled.
    if os.path.exists(ED23_SATZ_ABDECKUNG_JSON_PATH) and not app_config.overwrite_temp_files:
        logger.info(
            "Output file already exists and OVERWRITE_TEMP_FILES is false. "
            "Skipping stage_ed23_satz_abdeckung."
        )
        return

    # ED23 side: exclusively the pinned OFFICIAL XML Kompendium.
    xml_bytes, xml_sha = fetch_official_xml()
    official, _rejected = load_official_xml(xml_bytes)
    active = sorted(
        (r for r in official.values() if not r["entfallen"]), key=lambda r: r["id"]
    )
    logger.info(
        f"Official XML: {len(active)} active Anforderungen "
        f"({sum(len(r['normative_idx']) for r in active)} normative sentences)."
    )

    # G++ side: the pinned resolved catalog, with the sister stage's context extractor.
    gpp_catalog = load_json_file(GPP_KOMPENDIUM_JSON_PATH, expected_sha256=GPP_CATALOG_PIN_SHA256)
    if not gpp_catalog:
        logger.error("Failed to load pinned G++ Kompendium. Aborting stage.")
        return
    gpp_contexts = build_gpp_match_contexts(gpp_catalog)
    gpp_lookup = {normalize_id(cid): cid for cid in gpp_contexts}
    corpus_text = "\n".join(
        f"{cid} | {ctx['title']} | {ctx['prose']}" for cid, ctx in gpp_contexts.items()
    )
    logger.info(f"Built G++ corpus with {len(gpp_contexts)} controls ({len(corpus_text)} chars).")

    prompt_config = load_json_file(PROMPT_CONFIG_PATH)
    schema = load_json_file(ED23_SATZ_RESPONSE_SCHEMA_PATH)
    verify_schema = load_json_file(ED23_SATZ_VERIFY_RESPONSE_SCHEMA_PATH)
    system_instruction = prompt_config["ed23_satz_system"]
    prompt_template = prompt_config["ed23_satz_prompt"]
    verify_prompt_template = prompt_config["ed23_satz_verify_prompt"]

    ai_client = AiClient(app_config)
    # The cache must live on the maker model — the candidate pass is the only cached caller.
    cached_content = ai_client.create_context_cache(
        content=corpus_text, system_instruction=system_instruction, model_override=ED23_MAKER_MODEL
    )
    inline_prefix = (
        f"{system_instruction}\n\nVerfügbare G++-Maßnahmen "
        f"(Format: ID | Titel | Beschreibung):\n{corpus_text}"
    )

    # Respect Test Mode (Rule 9.1): only the first 3 Anforderungen.
    if app_config.is_test_mode:
        active = active[:3]
        logger.info("TEST mode: limiting to the first 3 Anforderungen.")

    final_map: Dict[str, List[Dict[str, Any]]] = _load_checkpoint(CHECKPOINT_PATH)
    pending = [r for r in active if r["id"] not in final_map]
    checkpoint_lock = asyncio.Lock()
    semaphore = asyncio.Semaphore(app_config.max_concurrent_ai_requests)
    logger.info(
        f"Judging {len(pending)} of {len(active)} Anforderungen against the G++ corpus "
        f"({len(final_map)} restored from checkpoint)..."
    )

    async def _judge_and_checkpoint(req: Dict[str, Any]) -> None:
        req_id, hits = await judge_requirement(
            ai_client, req, prompt_template, schema, verify_prompt_template, verify_schema,
            gpp_lookup, gpp_contexts, cached_content, inline_prefix, semaphore,
        )
        async with checkpoint_lock:
            final_map[req_id] = hits
            _atomic_save_json({CHECKPOINT_KEY: final_map}, CHECKPOINT_PATH)

    if pending:
        try:
            await asyncio.gather(*(_judge_and_checkpoint(r) for r in pending))
        finally:
            ai_client.delete_context_cache(cached_content)
    else:
        ai_client.delete_context_cache(cached_content)
        logger.info("All Anforderungen already present in checkpoint; nothing to query.")

    # Serialize: per-Anforderung sentence bookkeeping + verified hits. Official sentence
    # texts are NOT written (no republication of Kompendium prose in the repo).
    anforderungen: Dict[str, Any] = {}
    for req in active:
        hits = final_map.get(req["id"], [])
        anforderungen[req["id"]] = {
            "titel": req["titel"],
            "level": req["level"],
            "n_saetze": len(req["saetze"]),
            "normative_saetze": req["normative_idx"],
            "treffer": hits,
        }
    total_hits = sum(len(a["treffer"]) for a in anforderungen.values())
    covered_norm = sum(
        len({h["satz_nr"] for h in a["treffer"]} & set(a["normative_saetze"]))
        for a in anforderungen.values()
    )
    total_norm = sum(len(a["normative_saetze"]) for a in anforderungen.values())
    output = {
        "ed23_satz_abdeckung": {
            "meta": {
                "generated": datetime.date.today().isoformat(),
                "quelle_ed23": {"url": BSI_XML_URL, "sha256": xml_sha},
                "quelle_gpp": {
                    "url": GPP_KOMPENDIUM_JSON_PATH, "sha256": GPP_CATALOG_PIN_SHA256,
                },
                "maker_model": ED23_MAKER_MODEL,
                "checker_model": GROUND_TRUTH_MODEL,
                "anforderungen": len(anforderungen),
                "normative_saetze": total_norm,
                "normative_saetze_abgedeckt": covered_norm,
                "zuordnungen": total_hits,
            },
            "anforderungen": anforderungen,
        }
    }
    save_json_file(output, ED23_SATZ_ABDECKUNG_JSON_PATH)
    if os.path.exists(CHECKPOINT_PATH):
        os.remove(CHECKPOINT_PATH)
    logger.info(
        f"stage_ed23_satz_abdeckung finished. {len(anforderungen)} Anforderungen judged, "
        f"{covered_norm}/{total_norm} normative sentences covered by {total_hits} verified "
        "(satz, control) pairs."
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    asyncio.run(run_stage_ed23_satz_abdeckung())
