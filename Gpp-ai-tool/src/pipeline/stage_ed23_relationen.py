"""
Pipeline Stage: OSCAL relationship classification for the GS++ -> ED23 mapping.

Re-klassifiziert hilfsdateien/gpp_ed23_anforderungen.json in place: jedes verifizierte
(G++ control, ED23 Anforderung, Teilanforderung)-Paar erhaelt einen differenzierten
OSCAL ``relationship``-Token (equal-to / equivalent-to / subset-of / superset-of /
intersects-with); Begruendungen werden ersetzt, wo sie den Typ nicht tragen.

Umbau nach Issue #37 (Mapping-QS vom 30.08.2026): Die v2-Klassifikation lief pro Paar
isoliert und ohne Subsumtionsregel — Ergebnis waren 15,9 % nicht haltbare Relationstypen
(fast immer superset-of statt intersects-with), Familien-Inkonsistenzen und
"deckt ... ab"-Begruendungen im Widerspruch zum eigenen Label. Diese Fassung hebt die
Urteilseinheit auf das CONTROL:

* Ein Call je Control (Chunks ab ED23_RELATION_CHUNK_MAX Paaren, Ziel-Anforderungen
  werden nie ueber Chunks geteilt): alle Paare als Familie, gruppiert nach
  Ziel-Anforderung mit der vollen amtlichen Satzliste — Familien-Konsistenz und
  Dedup-Blick, die pro-Paar-Prompts strukturell nicht haben.
* Prompt mit expliziter Subsumtionsregel (zweites Verb / zweite Pflicht / andere
  Phase -> intersects-with), Familien-Konsistenzregel und Begruendungs-Stilregel;
  die bisherige Begruendung ist ausdruecklich nur Kontext.
* Rueckgabe je Paar: relationship + optional begruendung_neu (nur wenn die alte
  Begruendung den Typ nicht traegt); das "(Teilanforderung n)"-Praefix wird
  maschinell wieder vorangestellt.
* Ein gemeinsamer Prefix je Control statt 5er-Batches quer ueber Controls — weniger
  Calls, cache-freundlich (vgl. docs/token-kostenplan.md).

OSCAL direction semantics: the token describes the SOURCE (G++ control) relative to
the TARGET (ED23 Anforderung / tragender Satz). The BSI GSMap maps the opposite
direction, so subset-of/superset-of histograms must be mirrored before comparing.

Resume: .partial checkpoint je Control-Chunk. Skip guard: ein Mapping, dessen
Eintraege bereits mehr als einen Relationstyp tragen, gilt als klassifiziert;
OVERWRITE_TEMP_FILES=true erzwingt die Re-Klassifikation (der Normalfall dieser
Fassung). Kostenprobe: ED23_RELATION_CONTROLS="KONF.2.4,BER.4.1,..." beschraenkt
den Lauf auf die genannten Controls. Not part of the full pipeline — run explicitly
via `python -m pipeline.stage_ed23_relationen`.
"""

import asyncio
import json
import logging
import os
import re
import tempfile
import time
from collections import Counter
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
    ED23_RELATION_CONTROL_RESPONSE_SCHEMA_PATH,
    PROMPT_CONFIG_PATH,
)

logger = logging.getLogger(__name__)

CHECKPOINT_PATH = GPP_ED23_ANFORDERUNGEN_JSON_PATH + ".relationen.partial"
CHECKPOINT_KEY = "ed23_relationen_controls"
DEFAULT_RELATIONSHIP = "intersects-with"
CHUNK_MAX = int(os.environ.get("ED23_RELATION_CHUNK_MAX", "60"))
CONTROLS_FILTER = os.environ.get("ED23_RELATION_CONTROLS", "").strip()

TEILANF_PREFIX_RE = re.compile(r"^\(Teilanforderung (\d+)\)\s*")


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
    """Loads per-chunk verdicts from a prior run. Returns {} if absent/unreadable."""
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        done = data.get(CHECKPOINT_KEY, {})
        logger.info(f"Resuming from checkpoint '{path}': {len(done)} chunks already classified.")
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
    return f"{control_id}|{match['id']}|{match.get('satz_nr') or 0}"


def _chunk_matches(matches: List[Dict[str, Any]]) -> List[List[Dict[str, Any]]]:
    """Splits a control's matches into chunks of <= CHUNK_MAX pairs.

    Grouped by target Anforderung first and never splitting a group, so every chunk
    still judges whole requirement families together.
    """
    groups: Dict[str, List[Dict[str, Any]]] = {}
    order: List[str] = []
    for m in matches:
        if m["id"] not in groups:
            groups[m["id"]] = []
            order.append(m["id"])
        groups[m["id"]].append(m)
    chunks: List[List[Dict[str, Any]]] = [[]]
    for rid in order:
        group = sorted(groups[rid], key=lambda m: m.get("satz_nr") or 0)
        if chunks[-1] and len(chunks[-1]) + len(group) > CHUNK_MAX:
            chunks.append([])
        chunks[-1].extend(group)
    return [c for c in chunks if c]


def _render_pairs_block(
    chunk: List[Dict[str, Any]], saetze_by_id: Dict[str, List[str]]
) -> str:
    """Renders the chunk as requirement-grouped blocks with numbered official sentences."""
    lines: List[str] = []
    current_rid = None
    for n, m in enumerate(chunk, start=1):
        if m["id"] != current_rid:
            current_rid = m["id"]
            lines.append(f"### Ziel-Anforderung {m['id']} — {m.get('name') or '(ohne Titel)'}")
            saetze = saetze_by_id.get(m["id"], [])
            if saetze:
                lines.extend(f"(S{i}) {satz}" for i, satz in enumerate(saetze, start=1))
            else:
                lines.append("(keine Saetze im amtlichen Korpus)")
        satz_ref = f"S{m['satz_nr']}" if m.get("satz_nr") else "(keiner — gesamte Anforderung)"
        begruendung = TEILANF_PREFIX_RE.sub("", m.get("begruendung") or "(keine)")
        lines.append(
            f"[P{n}] tragender Satz: {satz_ref} | bisheriger Typ: "
            f"{m.get('relationship') or DEFAULT_RELATIONSHIP}"
        )
        lines.append(f"      bisherige Begruendung: {begruendung}")
    return "\n".join(lines)


def _validate_verdicts(
    verdict: Any, n_pairs: int
) -> Optional[List[Tuple[int, str, Optional[str]]]]:
    """Checks the structured response covers each pair exactly once; None if not."""
    if not isinstance(verdict, dict) or not isinstance(verdict.get("pairs"), list):
        return None
    seen: Dict[int, Tuple[int, str, Optional[str]]] = {}
    for item in verdict["pairs"]:
        if not isinstance(item, dict):
            return None
        nr, rel = item.get("nr"), item.get("relationship")
        if not isinstance(nr, int) or not (1 <= nr <= n_pairs) or nr in seen:
            return None
        if not isinstance(rel, str):
            return None
        neu = item.get("begruendung_neu")
        seen[nr] = (nr, rel, neu.strip() if isinstance(neu, str) and neu.strip() else None)
    if len(seen) != n_pairs:
        return None
    return [seen[i] for i in range(1, n_pairs + 1)]


async def _classify_control_chunk(
    ai_client: AiClient,
    control_id: str,
    control: Dict[str, str],
    chunk: List[Dict[str, Any]],
    saetze_by_id: Dict[str, List[str]],
    prompt_template: str,
    schema: Dict[str, Any],
    semaphore: asyncio.Semaphore,
) -> Optional[List[Dict[str, Any]]]:
    """Classifies one control chunk; returns per-pair verdicts or None on failure."""
    prompt = prompt_template.format(
        praktik=control.get("praktik", ""),
        control_id=control_id,
        title=control.get("title", ""),
        prose=control.get("prose", ""),
        guidance=control.get("guidance") or "(keine)",
        n_pairs=len(chunk),
        pairs_block=_render_pairs_block(chunk, saetze_by_id),
    )
    async with semaphore:
        for attempt in (1, 2):
            try:
                verdict = await ai_client.generate_validated_json_response(
                    prompt=prompt,
                    json_schema=schema,
                    request_context_log=f"ED23RelationCtrl-{control_id}-n{len(chunk)}",
                )
            except Exception as e:
                logger.warning(
                    f"Relation classification failed for '{control_id}' "
                    f"(attempt {attempt}): {e}"
                )
                verdict = None
            rows = _validate_verdicts(verdict, len(chunk)) if verdict else None
            if rows is not None:
                return [
                    {"key": _pair_key(control_id, m), "relationship": rel, "begruendung_neu": neu}
                    for m, (_, rel, neu) in zip(chunk, rows)
                ]
            if verdict is not None:
                logger.warning(
                    f"Incomplete/inconsistent verdict set for '{control_id}' "
                    f"(attempt {attempt}); retrying." if attempt == 1 else
                    f"Giving up on '{control_id}': keeping previous relations."
                )
    return None


async def run_stage_ed23_relationen() -> None:
    """Main entry point for the control-grouped relationship re-classification."""
    logger.info("Starting stage_ed23_relationen (control-grouped, Issue #37)...")

    with open(GPP_ED23_ANFORDERUNGEN_JSON_PATH, "r", encoding="utf-8") as f:
        mapping_doc = json.load(f)
    per_control = load_mapping_matches(mapping_doc)
    all_pairs = [(cid, m) for cid, matches in per_control.items() for m in matches]
    distinct_relations = {m.get("relationship") for _, m in all_pairs}
    if len(distinct_relations - {None}) > 1 and not app_config.overwrite_temp_files:
        logger.info(
            "Mapping already carries differentiated relationships "
            f"({sorted(r for r in distinct_relations if r)}) and OVERWRITE_TEMP_FILES is "
            "false. Skipping stage_ed23_relationen (set OVERWRITE_TEMP_FILES=true to "
            "re-classify)."
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
    prompt_template = prompt_config["ed23_relation_control_prompt"]
    schema = load_json_file(ED23_RELATION_CONTROL_RESPONSE_SCHEMA_PATH)
    ai_client = AiClient(app_config)

    control_ids = sorted(per_control)
    if CONTROLS_FILTER:
        wanted = {c.strip() for c in CONTROLS_FILTER.split(",") if c.strip()}
        missing = wanted - set(control_ids)
        if missing:
            logger.warning(f"ED23_RELATION_CONTROLS unbekannt im Mapping: {sorted(missing)}")
        control_ids = [c for c in control_ids if c in wanted]
        logger.info(f"Kostenprobe: beschraenkt auf {len(control_ids)} Controls: {control_ids}")
    if app_config.is_test_mode:
        control_ids = control_ids[:3]
        logger.info(f"TEST mode: limiting to controls {control_ids}.")

    chunks: List[Tuple[str, int, List[Dict[str, Any]]]] = []
    for cid in control_ids:
        for i, chunk in enumerate(_chunk_matches(per_control[cid])):
            chunks.append((cid, i, chunk))

    classified: Dict[str, List[Dict[str, Any]]] = _load_checkpoint(CHECKPOINT_PATH)
    pending = [(cid, i, c) for cid, i, c in chunks if f"{cid}#{i}" not in classified]
    checkpoint_lock = asyncio.Lock()
    semaphore = asyncio.Semaphore(app_config.max_concurrent_ai_requests)
    n_scope = sum(len(c) for _, _, c in chunks)
    logger.info(
        f"Classifying {len(pending)} of {len(chunks)} control chunks "
        f"({n_scope} pairs in scope, {len(classified)} chunks from checkpoint)..."
    )

    async def _classify_and_checkpoint(cid: str, idx: int, chunk: List[Dict[str, Any]]) -> None:
        control = gpp_contexts.get(cid)
        if control is None:
            logger.warning(f"Control '{cid}' not in pinned G++ catalog; keeping relations.")
            return
        rows = await _classify_control_chunk(
            ai_client, cid, control, chunk, saetze_by_id, prompt_template, schema, semaphore,
        )
        if rows is not None:
            async with checkpoint_lock:
                classified[f"{cid}#{idx}"] = rows
                _atomic_save_json({CHECKPOINT_KEY: classified}, CHECKPOINT_PATH)

    if pending:
        await asyncio.gather(*(_classify_and_checkpoint(cid, i, c) for cid, i, c in pending))

    # Apply verdicts. Pairs without a verdict keep their previous relationship.
    by_key: Dict[str, Dict[str, Any]] = {
        row["key"]: row for rows in classified.values() for row in rows
    }
    transitions: Counter = Counter()
    histogram: Counter = Counter()
    n_applied = n_new_remarks = 0
    for cid, match in all_pairs:
        row = by_key.get(_pair_key(cid, match))
        old_rel = match.get("relationship") or DEFAULT_RELATIONSHIP
        if row:
            new_rel = row["relationship"]
            match["relationship"] = new_rel
            n_applied += 1
            if new_rel != old_rel:
                transitions[f"{old_rel} -> {new_rel}"] += 1
            neu = row.get("begruendung_neu")
            if neu:
                prefix = f"(Teilanforderung {match['satz_nr']}) " if match.get("satz_nr") else ""
                match["begruendung"] = prefix + neu
                n_new_remarks += 1
        histogram[match.get("relationship") or DEFAULT_RELATIONSHIP] += 1

    output = to_oscal_mapping_collection(per_control)
    save_json_file(output, GPP_ED23_ANFORDERUNGEN_JSON_PATH)
    n_chunks_expected = len(chunks)
    if os.path.exists(CHECKPOINT_PATH) and len(classified) >= n_chunks_expected and not CONTROLS_FILTER:
        os.remove(CHECKPOINT_PATH)
    logger.info(
        f"stage_ed23_relationen finished. {n_applied} of {n_scope} in-scope pairs applied; "
        f"{n_new_remarks} remarks replaced; distribution now: {dict(sorted(histogram.items()))}."
    )
    if transitions:
        logger.info("Relation transitions: " + ", ".join(
            f"{k}: {v}" for k, v in transitions.most_common()
        ))
    ai_client.log_usage_summary("stage_ed23_relationen")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    asyncio.run(run_stage_ed23_relationen())
