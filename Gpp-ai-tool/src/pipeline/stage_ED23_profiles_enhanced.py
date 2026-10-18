"""
Pipeline Stage: ED23-Baustein profiles in the Mindeststandard pattern.

For every Baustein in hilfsdateien/baustein_zielobjekt.json this stage writes two OSCAL 1.2.2
profiles to ED23_PROFILES_DIR: a plain one and an `_enhanced` one. Both carry the Baustein's
own Anforderungen as the profile structure; the enhanced one adds the maturity-level parts.

Structure (Handbuch 3.15, mindeststandard-oscal.html):
* imports[0] = the pinned Anwenderkatalog Grundschutz++, with-ids = exactly the G++ controls
  assigned to the Baustein's Anforderungen (hilfsdateien/ed23_baustein_abgleich.json);
* imports[1] = the shared NG Ergänzungskatalog (relative rlink + SHA-256, fail closed), only
  when the Baustein has NG controls; `merge.combine.method = use-first` always;
* merge.custom: level groups (B/S/H, class `ed23-stufe`) → one group per Anforderung (class
  `ed23-anforderung`) with the original text as part `overview` and `insert-controls` for
  its controls. A control is inserted once (at its first Anforderung); later Anforderungen
  link to it (`rel=related`). Anforderungen without a control carry prop `ohne-control`,
  ENTFALLEN ones prop `entfallen`;
* modify.alters per G++ control: [enhanced only] the maturity block (by-id statement part,
  parts m1–m5, docs/profile-maturity-contract.md) FIRST, then a props-only `adds` with one
  `ed23-anforderung` prop per assigned Anforderung whose remark starts "Herkunft: …".
  Baustein_2_Profile.html reads adds[0].parts[0], so the order is a contract;
* metadata props (ns ed23-baustein): herkunft BSI|NG, ed23-baustein, ed23-baustein-titel,
  zielobjektkategorie, ed23-katalog-pin, ed23-schicht. NG Bausteine: filename `NG_…`,
  title `NG …`.

Maturity texts are paid LLM output: they are harvested from existing `_enhanced` files into
hilfsdateien/ed23_maturity_cache.json and reused (also across Bausteine, the texts describe
the control); the model is only called for controls without a valid cache entry. Files are
written only when their content changed (ignoring last-modified).
"""

import asyncio
import datetime
import glob
import json
import logging
import os
import re
import sys
import uuid
from typing import Any, Dict, List, Optional, Tuple

from config import app_config
from clients.ai_client import AiClient
from utils.data_loader import load_json_file, zielobjekt_row_name
from utils.ed23_xml import fetch_official_xml, load_official_xml
from utils.file_utils import create_dir_if_not_exists, read_csv_file, read_json_file, write_json_file
from utils.ed23_baustein import (
    LEVEL_ORDER,
    LEVEL_TITLE,
    anforderung_sort_key,
    build_anforderung_records,
    detect_ng,
    iter_bausteine,
    load_ed23_catalogs,
    profile_file_stem,
)
from utils.oscal_utils import (
    extract_all_gpp_controls,
    json_equal_ignoring,
    ng_katalog_resource,
    ng_katalog_resource_uuid,
    normalize_id,
    pinned_catalog_import_href,
    pinned_catalog_resource,
    pinned_ed23_catalog_resource,
    pinned_ed23_catalog_resource_uuid,
    sha256_of_file,
    validate_ed23_profile_structure,
)
from pipeline.stage_ed23_anforderungen import _atomic_save_json
from constants import (
    BAUSTEIN_ZIELOBJEKT_JSON_PATH,
    BSI_GRUNDSCHUTZ_NS,
    BUILD_VERSION,
    ED23_BAUSTEIN_ABGLEICH_JSON_PATH,
    ED23_BAUSTEIN_NS,
    ED23_CATALOG_PIN_COMMIT,
    ED23_MATURITY_CACHE_JSON_PATH,
    ED23_MATURITY_REGENERATE,
    ED23_MATURITY_REUSE_ACROSS_BAUSTEINE,
    ED23_PROFILES_DIR,
    ENHANCED_CONTROL_RESPONSE_SCHEMA_PATH,
    GPP_CATALOG_PIN_COMMIT,
    GPP_CATALOG_PIN_SHA256,
    GPP_ENHANCEMENT_PROPS_NS,
    GPP_KOMPENDIUM_JSON_PATH,
    NG_KATALOG_FILENAME,
    NG_KATALOG_PATH,
    OSCAL_VERSION,
    PROMPT_CONFIG_PATH,
    PROZESSBAUSTEINE_LAYERS,
    SDT_MODAL_VERB_NS,
    SDT_PROFILES_PROCESS_DIR,
    ZIELOBJEKTKATEGORIEN_CSV_PATH,
)

logger = logging.getLogger(__name__)

# Chunk controls to avoid overwhelming the model in a single request.
CHUNK_SIZE = 10
MATURITY_CACHE_KEY = "ed23_maturity_cache"
_BAUSTEIN_TOKEN_RE = re.compile(r"^[A-Z]{2,5}(\.\d+)+$")

# Stable namespace for deriving deterministic (UUIDv5) profile UUIDs. Re-running the
# pipeline must yield identical UUIDs for the same Baustein/Kategorie so the generated
# profiles don't churn in git.
ED23_PROFILE_UUID_NAMESPACE = uuid.uuid5(
    uuid.NAMESPACE_URL,
    "https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek/ED2023-enhanced-profiles",
)


def deterministic_profile_uuid(baustein_id: str, zielobjekt_name: str, variant: str = "enhanced") -> str:
    """Derives a stable UUIDv5 for a profile from its Baustein + Kategorie + variant (plain/enhanced)."""
    return str(uuid.uuid5(ED23_PROFILE_UUID_NAMESPACE, f"{baustein_id}|{zielobjekt_name}|{variant}"))


# ── maturity parts (unchanged contract, docs/profile-maturity-contract.md) ───────────────
def build_oscal_maturity_statements(control_id: str, generated_data: dict, original_description: str, baustein_id: str) -> list:
    """Constructs the OSCAL maturity sub-statements (parts) for the 'adds' block.

    Each maturity level becomes one `statement` part whose own per-level text lives in
    `prose`, with the guidance and assessment carried as nested `guidance` / `assessment`
    parts. Classification (class, phase) and the level `label` stay as props. Level 3 is the
    original G++ control prose verbatim, injected deterministically (issue 2.2).
    """
    parts = []
    props_ns = GPP_ENHANCEMENT_PROPS_NS
    base_props = [
        {"name": "control_class", "value": generated_data.get("class") or "Technical", "ns": props_ns},
        {"name": "phase", "value": generated_data.get("phase") or "N/A", "ns": props_ns},
    ]
    for level_num in ["1", "2", "3", "4", "5"]:
        if level_num == "3":
            statement_text = original_description or generated_data.get("level_3_statement")
        else:
            statement_text = generated_data.get(f"level_{level_num}_statement")
        if not statement_text:
            continue
        part_id = f"{control_id}-m{level_num}_custom"
        part = {
            "id": part_id,
            "name": "statement",
            "props": list(base_props) + [{"name": "label", "value": f"m{level_num}"}],
            "prose": statement_text,
        }
        nested = []
        guidance_text = generated_data.get(f"level_{level_num}_guidance", "")
        assessment_text = generated_data.get(f"level_{level_num}_assessment", "")
        if guidance_text:
            nested.append({"id": f"{part_id}_gdn", "name": "guidance", "prose": guidance_text})
        if assessment_text:
            nested.append({"id": f"{part_id}_asm", "name": "assessment", "prose": assessment_text})
        if nested:
            part["parts"] = nested
        parts.append(part)
    return parts


def _render_controls_table(control_ids: list, gpp_controls_lookup: dict) -> str:
    """Renders a markdown table of the G++ controls to enrich (ID, title, prose)."""
    header = "| ID | Title | Prose |\n|---|---|---|\n"
    rows = []
    for ctrl_id in control_ids:
        data = gpp_controls_lookup.get(ctrl_id, {})
        title = (data.get("title", "") or "").replace("\n", " ")
        prose = (data.get("prose", "") or "").replace("\n", " ")
        rows.append(f"| {ctrl_id} | {title} | {prose} |")
    return header + "\n".join(rows)


async def generate_maturity_blocks(
    baustein_id: str, baustein_title: str, baustein_description: str, control_ids: List[str],
    gpp_controls_lookup: dict, prompt_instruction: str, enhanced_schema: dict, ai_client: AiClient,
    semaphore: asyncio.Semaphore,
) -> Dict[str, Dict[str, Any]]:
    """Asks the model for maturity levels of the given controls; returns {cid: adds block}."""
    if not control_ids:
        return {}
    logger.info(f"Generating maturity levels for {len(control_ids)} controls of Baustein {baustein_id}")
    baustein_context = (
        f"**Context — the BSI IT-Grundschutz Baustein this profile is based on:**\n"
        f"* ID: {baustein_id}\n* Title: {baustein_title}\n* Description: {baustein_description or 'N/A'}\n\n"
    )
    chunks = [control_ids[i:i + CHUNK_SIZE] for i in range(0, len(control_ids), CHUNK_SIZE)]

    async def process_chunk(chunk):
        prompt = (
            f"{prompt_instruction}\n\n{baustein_context}"
            f"**G++ controls to enrich** (generate maturity levels 1, 2, 4 and 5 for each; "
            f"Level 3 is the control's prose and is injected automatically, so you may omit "
            f"level_3_* — only provide a level if a technically sound, distinct "
            f"implementation can be described):\n{_render_controls_table(chunk, gpp_controls_lookup)}\n\n"
            "Return a JSON array with one object per control, matching each by its original ID."
        )
        async with semaphore:
            try:
                result = await ai_client.generate_validated_json_response(
                    prompt=prompt, json_schema=enhanced_schema, request_context_log=f"ED23Enhance-{baustein_id}",
                )
                return result if isinstance(result, list) else []
            except Exception as e:  # noqa: BLE001 — the chunk's controls stay without maturity, reason logged
                logger.error(f"Maturity generation failed for a chunk of Baustein {baustein_id}: {e}")
                return []

    results = await asyncio.gather(*[process_chunk(c) for c in chunks])
    by_id = {normalize_id(item["id"]): item for res in results for item in res if isinstance(item, dict) and "id" in item}
    blocks: Dict[str, Dict[str, Any]] = {}
    for cid in control_ids:
        data = by_id.get(normalize_id(cid))
        meta = gpp_controls_lookup.get(cid, {})
        if not data:
            logger.warning(f"No maturity data for control {cid} in Baustein {baustein_id}")
            continue
        if not meta.get("statement_part_id"):
            logger.warning(f"Control {cid} has no statement part to anchor maturity additions to; skipping.")
            continue
        parts = build_oscal_maturity_statements(cid, data, meta.get("prose", ""), baustein_id)
        if parts:
            blocks[cid] = {"position": "ending", "by-id": meta["statement_part_id"], "parts": parts}
    return blocks


# ── maturity cache (harvest + reuse) ─────────────────────────────────────────────────────
def load_maturity_cache(path: str = ED23_MATURITY_CACHE_JSON_PATH) -> Dict[str, Any]:
    if not os.path.exists(path):
        return {"_meta": {"gpp_pin": GPP_CATALOG_PIN_COMMIT, "harvested_from": []}}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return (json.load(f) or {}).get(MATURITY_CACHE_KEY) or {"_meta": {}}
    except Exception as e:  # noqa: BLE001 — a corrupt cache is rebuilt, with the reason logged
        logger.warning(f"Could not read maturity cache '{path}' ({e}); starting with an empty cache.")
        return {"_meta": {}}


def save_maturity_cache(cache: Dict[str, Any], path: str = ED23_MATURITY_CACHE_JSON_PATH) -> None:
    _atomic_save_json({MATURITY_CACHE_KEY: cache}, path)


def _baustein_id_of_file(doc: Dict[str, Any], filename: str, known_ids: Optional[set]) -> str:
    """The cache key of an enhanced profile: its Baustein id, else (process profiles) `prozess:<stem>`."""
    meta = (doc.get("profile") or {}).get("metadata") or {}
    for p in meta.get("props", []) or []:
        if p.get("name") == "ed23-baustein" and p.get("ns") == ED23_BAUSTEIN_NS:
            return p.get("value")
    stem = filename.replace("_enhanced.json", "").replace(".json", "")
    for token in stem.split("_"):
        if _BAUSTEIN_TOKEN_RE.match(token) and (known_ids is None or token in known_ids):
            return token
    return f"prozess:{stem}"


def harvest_existing_maturity(profiles_dir: str, cache: Dict[str, Any], known_ids: Optional[set] = None) -> int:
    """Copies the maturity `adds` blocks of every `*_enhanced.json` into the cache (never overwrites).

    Works for the per-Baustein profiles and for the Praktiken process profiles
    (`<praktik>_process_profile_enhanced.json`, keyed `prozess:<stem>`): the process controls
    (GC, SENS, PERS, …) only ever had maturity texts there.
    """
    added = 0
    harvested = cache.setdefault("_meta", {}).setdefault("harvested_from", [])
    for path in sorted(glob.glob(os.path.join(profiles_dir, "*_enhanced.json"))):
        name = os.path.basename(path)
        try:
            with open(path, "r", encoding="utf-8") as f:
                doc = json.load(f)
        except Exception as e:  # noqa: BLE001 — one unreadable file must not stop the harvest
            logger.warning(f"Harvest: cannot read {name} ({e}); skipped.")
            continue
        bid = _baustein_id_of_file(doc, name, known_ids)
        slot = cache.setdefault(bid, {})
        for alter in ((doc.get("profile") or {}).get("modify") or {}).get("alters") or []:
            cid = alter.get("control-id")
            for add in alter.get("adds") or []:
                if cid and add.get("by-id") and add.get("parts") and cid not in slot:
                    slot[cid] = {"by-id": add["by-id"], "parts": add["parts"]}
                    added += 1
        if name not in harvested:
            harvested.append(name)
    if added:
        logger.info(f"Harvested {added} maturity blocks from {profiles_dir}.")
    return added


def _m3_prose(block: Dict[str, Any], cid: str) -> Optional[str]:
    for part in block.get("parts") or []:
        if part.get("id") == f"{cid}-m3_custom":
            return part.get("prose")
    return None


def maturity_for(cache: Dict[str, Any], baustein_id: str, cid: str, current_prose: str) -> Optional[Dict[str, Any]]:
    """A cached maturity block for the control: same Baustein first, else any Baustein.

    Valid only if its m3 prose equals the control's current prose (pin-change guard).
    """
    if ED23_MATURITY_REGENERATE:
        return None
    candidates = [cache.get(baustein_id, {}).get(cid)]
    if ED23_MATURITY_REUSE_ACROSS_BAUSTEINE:
        candidates += [slot.get(cid) for b, slot in cache.items() if b not in ("_meta", baustein_id) and isinstance(slot, dict)]
    for block in candidates:
        if block and _m3_prose(block, cid) == current_prose:
            return {"position": "ending", "by-id": block["by-id"], "parts": block["parts"]}
    return None


# ── pure builders ─────────────────────────────────────────────────────────────────────────
def order_anforderungen(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return sorted(records, key=lambda r: (LEVEL_ORDER.get(r.get("level"), 9), anforderung_sort_key(r["id"])))


def control_placement(ordered: List[Dict[str, Any]], abgleich: Dict[str, Any]) -> Tuple[Dict[str, str], Dict[str, List[str]], Dict[str, List[Tuple[str, Dict[str, Any]]]]]:
    """Returns (first placement per control, control ids per Anforderung, provenance per control)."""
    first: Dict[str, str] = {}
    by_anf: Dict[str, List[str]] = {}
    provenance: Dict[str, List[Tuple[str, Dict[str, Any]]]] = {}
    for rec in ordered:
        if rec.get("entfallen"):
            continue
        entry = abgleich.get(rec["id"], {}) or {}
        ids: List[str] = []
        for z in entry.get("zuordnungen") or []:
            cid = z["control_id"]
            if cid not in ids:
                ids.append(cid)
            provenance.setdefault(cid, []).append((rec["id"], z))
        nc = entry.get("neues_control")
        if nc and nc.get("id"):
            ids.append(nc["id"])
        by_anf[rec["id"]] = ids
        for cid in ids:
            first.setdefault(cid, rec["id"])
    return first, by_anf, provenance


def _strip_teilanforderung(text: str) -> str:
    return re.sub(r"^\(Teilanforderung [\d, ]+\)\s*", "", text or "").strip()


def herkunft_remark(z: Dict[str, Any]) -> str:
    """The `Herkunft:` remark grammar (parsed by the SSP generators — keep the forms stable)."""
    quelle = z.get("quelle")
    rel = z.get("relation") or "intersects-with"
    satz = ",".join(str(n) for n in (z.get("satz_nr") or []))
    beg = _strip_teilanforderung(z.get("begruendung") or "")
    if quelle == "gpp_ed23_anforderungen":
        head = f"Herkunft: gpp_ed23_anforderungen ({rel}" + (f", Teilanforderung {satz}" if satz else "") + ")"
    elif quelle == "satz_abdeckung":
        head = f"Herkunft: satz_abdeckung ({rel}" + (f", Satz {satz}" if satz else "") + ")"
    elif quelle == "prozessbausteine_mapping":
        head = "Herkunft: prozessbausteine_mapping (1:1-Zuordnung)"
    elif quelle == "gsmap":
        head = f"Herkunft: BSI-GSMap ITGS→GS++ ({rel})"
    else:
        head = (f"Herkunft: KI-Vorschlag ({rel}, Konfidenz {z.get('konfidenz') or 'n/a'}, "
                f"Checker {z.get('checker') or 'nicht geprüft'})")
    others = [q for q in (z.get("quellen") or []) if q != quelle]
    text = head + (f": {beg}" if beg else "")
    if others:
        text += f" [auch: {', '.join(others)}]"
    return text


def _prop(name: str, value: str, ns: Optional[str] = None, remarks: Optional[str] = None) -> Dict[str, Any]:
    p: Dict[str, Any] = {"name": name}
    if ns:
        p["ns"] = ns
    p["value"] = value
    if remarks:
        p["remarks"] = remarks
    return p


def build_merge_groups(baustein_id: str, ordered: List[Dict[str, Any]], abgleich: Dict[str, Any],
                       first: Dict[str, str], by_anf: Dict[str, List[str]]) -> List[Dict[str, Any]]:
    levels: Dict[str, Dict[str, Any]] = {}
    for rec in ordered:
        level = rec.get("level") if rec.get("level") in LEVEL_ORDER else "X"
        lg = levels.setdefault(level, {
            "id": f"{baustein_id}-{level}", "class": "ed23-stufe",
            "title": LEVEL_TITLE.get(level, "Anforderungen ohne Stufe"),
            "props": [{"name": "label", "value": level}], "groups": [],
        })
        aid = rec["id"]
        if rec.get("entfallen"):
            lg["groups"].append({
                "id": aid, "class": "ed23-anforderung", "title": f"{aid} ENTFALLEN",
                "props": [{"name": "label", "value": aid}, _prop("entfallen", "true", ED23_BAUSTEIN_NS)],
            })
            continue
        entry = abgleich.get(aid, {}) or {}
        props = [{"name": "label", "value": aid}]
        if rec.get("level_num"):
            props.append(_prop("level", str(rec["level_num"]), BSI_GRUNDSCHUTZ_NS))
        if rec.get("modalverb"):
            props.append(_prop("modal_verb", rec["modalverb"], SDT_MODAL_VERB_NS))
        props.append(_prop("herkunft", rec.get("herkunft", "BSI"), ED23_BAUSTEIN_NS))
        if rec.get("rolle"):
            props.append(_prop("rolle", rec["rolle"], ED23_BAUSTEIN_NS))
        art = ((entry.get("pruefung") or {}).get("art"))
        if art:
            props.append(_prop("anforderungsart", art, ED23_BAUSTEIN_NS, "Einordnung durch das Modell"))
        group: Dict[str, Any] = {
            "id": aid, "class": "ed23-anforderung", "title": f"{aid} {rec.get('titel') or ''}".strip(),
            "props": props,
            "parts": [{"id": f"{aid}_anforderung", "name": "overview", "prose": rec.get("text") or "(kein Text)"}],
        }
        own = [cid for cid in by_anf.get(aid, []) if first.get(cid) == aid]
        elsewhere = [cid for cid in by_anf.get(aid, []) if first.get(cid) != aid]
        if own:
            group["insert-controls"] = [{"include-controls": [{"with-ids": own}]}]
        if elsewhere:
            group["links"] = [{"href": f"#{cid}", "rel": "related", "text": f"{cid} steht unter {first[cid]}"}
                              for cid in elsewhere]
        if not own and not elsewhere:
            oc = entry.get("ohne_control") or {"art": "unbeantwortet", "begruendung": ""}
            group["props"].append(_prop("ohne-control", oc.get("art") or "unbestimmt", ED23_BAUSTEIN_NS,
                                        oc.get("begruendung") or None))
        lg["groups"].append(group)
    return [levels[k] for k in sorted(levels, key=lambda k: LEVEL_ORDER.get(k, 9))]


def build_alters(gpp_ids: List[str], provenance: Dict[str, List[Tuple[str, Dict[str, Any]]]],
                 maturity: Optional[Dict[str, Dict[str, Any]]]) -> List[Dict[str, Any]]:
    """One alter per included G++ control: [maturity block first (enhanced)], then provenance props."""
    alters = []
    for cid in gpp_ids:
        adds = []
        if maturity and maturity.get(cid):
            adds.append(maturity[cid])
        props = [_prop("ed23-anforderung", aid, ED23_BAUSTEIN_NS, herkunft_remark(z)) for aid, z in provenance.get(cid, [])]
        if props:
            adds.append({"position": "ending", "props": props})
        if adds:
            alters.append({"control-id": cid, "adds": adds})
    return alters


def build_profile(ctx: Dict[str, Any], variant: str, maturity: Optional[Dict[str, Dict[str, Any]]] = None) -> Dict[str, Any]:
    """The whole profile document for one Baustein (variant 'plain' | 'enhanced'), without I/O."""
    bid, btitle, zo = ctx["baustein_id"], ctx["baustein_title"], ctx["zielobjekt_name"]
    is_ng = ctx["herkunft"] == "NG"
    first, by_anf, provenance = control_placement(ctx["ordered"], ctx["abgleich"])
    gpp_ids = sorted(cid for cid in first if not cid.startswith("NG-"))
    ng_ids = sorted(cid for cid in first if cid.startswith("NG-"))
    title = f"{'NG ' if is_ng else ''}{bid} – {btitle} ({zo})" + (" – Enhanced (ED2023)" if variant == "enhanced" else "")
    schicht = "prozess" if bid.split(".")[0] in PROZESSBAUSTEINE_LAYERS else "system"
    remarks = (
        f"Erzeugt von Gpp-ai-tool {BUILD_VERSION} (stage_ED23_profiles_enhanced). Die Anforderungen des Bausteins "
        f"sind Gruppen mit dem Originaltext als Part „overview“ ({'Text des nutzergenerierten Bausteins (NG, NTT DATA), kein BSI-Text' if is_ng else 'amtlicher Wortlaut des XML-Kompendiums 2023'}); "
        f"die Controls stammen aus dem Anwenderkatalog Grundschutz++ (Pin {GPP_CATALOG_PIN_COMMIT[:12]})"
        + (f" und dem NG Ergänzungskatalog ({NG_KATALOG_FILENAME}, nutzergeneriert)" if ng_ids else "")
        + ". Jede Zuordnung nennt ihre Herkunft in der Prop ed23-anforderung des Controls."
        + (" Prozess-Baustein ohne eigene Praktik in Grundschutz++; die Zielobjektkategorie ist nur informativ." if schicht == "prozess" else "")
    )
    profile: Dict[str, Any] = {
        "uuid": deterministic_profile_uuid(bid, zo, variant),
        "metadata": {
            "title": title,
            "last-modified": ctx.get("last_modified") or "",
            "version": ctx["version"],
            "oscal-version": OSCAL_VERSION,
            "props": [
                _prop("herkunft", ctx["herkunft"], ED23_BAUSTEIN_NS),
                _prop("ed23-baustein", bid, ED23_BAUSTEIN_NS),
                _prop("ed23-baustein-titel", btitle, ED23_BAUSTEIN_NS),
                _prop("zielobjektkategorie", zo, ED23_BAUSTEIN_NS),
                _prop("ed23-katalog-pin", ED23_CATALOG_PIN_COMMIT, ED23_BAUSTEIN_NS),
                _prop("ed23-schicht", schicht, ED23_BAUSTEIN_NS),
                {"name": "keywords", "value": f"ED23, {bid}, {'NG, ' if is_ng else ''}Grundschutz++"},
            ],
            "links": [{"href": f"#{pinned_ed23_catalog_resource_uuid()}", "rel": "source",
                       "text": f"Baustein {bid} im BSI-IT-Grundschutz-Katalog Edition 2023 (benutzerdefinierte OSCAL-Ausgabe"
                               f"{', NG-Baustein' if is_ng else ''})"}],
            "remarks": remarks,
        },
        "imports": [{"href": pinned_catalog_import_href(), "include-controls": [{"with-ids": gpp_ids}]}],
        "merge": {
            "combine": {"method": "use-first"},
            "custom": {"groups": build_merge_groups(bid, ctx["ordered"], ctx["abgleich"], first, by_anf)},
        },
        "back-matter": {"resources": [pinned_catalog_resource(), pinned_ed23_catalog_resource()]},
    }
    if ng_ids:
        sha = ctx["ng_sha256"]
        profile["imports"].append({"href": f"#{ng_katalog_resource_uuid(sha)}", "include-controls": [{"with-ids": ng_ids}]})
        profile["back-matter"]["resources"].append(ng_katalog_resource(sha, ctx.get("ng_total", len(ng_ids)), ctx["ng_title"]))
    alters = build_alters(gpp_ids, provenance, maturity if variant == "enhanced" else None)
    if alters:
        profile["modify"] = {"alters": alters}
    return {"profile": profile}


# ── writing ───────────────────────────────────────────────────────────────────────────────
def write_if_changed(path: str, doc: Dict[str, Any]) -> bool:
    """Writes `doc` only when it differs from the file (ignoring last-modified); returns True if written."""
    existing = read_json_file(path) if os.path.exists(path) else None
    if existing and json_equal_ignoring(doc, existing):
        return False
    doc["profile"]["metadata"]["last-modified"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    write_json_file(path, doc)
    return True


# ── stage ─────────────────────────────────────────────────────────────────────────────────
async def run_stage_ED23_profiles_enhanced():
    """Executes the ED2023 profile generation stage."""
    logger.info("Starting Stage: ED2023 Baustein Profile Generation")
    create_dir_if_not_exists(ED23_PROFILES_DIR)

    baustein_map = (read_json_file(BAUSTEIN_ZIELOBJEKT_JSON_PATH) or {}).get("baustein_zielobjekt_map") or {}
    if not baustein_map:
        raise RuntimeError("baustein_zielobjekt.json is empty — run stage_match_bausteine first.")
    if not os.path.exists(ED23_BAUSTEIN_ABGLEICH_JSON_PATH):
        raise RuntimeError(f"{ED23_BAUSTEIN_ABGLEICH_JSON_PATH} missing — run stage_ed23_baustein_abgleich first.")
    abgleich_doc = (read_json_file(ED23_BAUSTEIN_ABGLEICH_JSON_PATH) or {}).get("ed23_baustein_abgleich") or {}
    abgleich = abgleich_doc.get("anforderungen") or {}
    version = str((abgleich_doc.get("meta") or {}).get("version") or datetime.date.today().isoformat())

    zo_rows = read_csv_file(ZIELOBJEKTKATEGORIEN_CSV_PATH)
    zielobjekt_name_map = {row["UUID"].strip(): zielobjekt_row_name(row) for row in zo_rows if "UUID" in row and zielobjekt_row_name(row)}
    bd, plain = load_ed23_catalogs()
    ng = detect_ng(bd, plain)
    bausteine = {b["id"]: b for b in iter_bausteine(bd)}
    xml_bytes, _ = fetch_official_xml()
    official, _ = load_official_xml(xml_bytes)
    records = build_anforderung_records(bd, official, ng, bausteine=list(baustein_map))
    gpp_catalog = load_json_file(GPP_KOMPENDIUM_JSON_PATH, expected_sha256=GPP_CATALOG_PIN_SHA256)
    gpp_controls_lookup = extract_all_gpp_controls(gpp_catalog)

    ng_sha = sha256_of_file(NG_KATALOG_PATH) if os.path.exists(NG_KATALOG_PATH) else None
    ng_total, ng_title = 0, "NG Ergänzungskatalog"
    if ng_sha:
        ng_doc = read_json_file(NG_KATALOG_PATH) or {}
        ng_title = ng_doc.get("catalog", {}).get("metadata", {}).get("title") or ng_title
        ng_total = sum(len(g.get("controls", [])) for layer in ng_doc.get("catalog", {}).get("groups", []) for g in layer.get("groups", []))
        ng_ids_available = {c["id"] for layer in ng_doc.get("catalog", {}).get("groups", []) for g in layer.get("groups", []) for c in g.get("controls", [])}
    else:
        ng_ids_available = set()

    cache = load_maturity_cache()
    harvest_existing_maturity(ED23_PROFILES_DIR, cache, set(baustein_map))
    harvest_existing_maturity(SDT_PROFILES_PROCESS_DIR, cache, set(baustein_map))
    prompt_config = read_json_file(PROMPT_CONFIG_PATH)
    enhanced_schema = read_json_file(ENHANCED_CONTROL_RESPONSE_SCHEMA_PATH)
    prompt_instruction = prompt_config["generate_enhanced_controls_prompt"]

    ai_client: Optional[AiClient] = None
    sem = asyncio.Semaphore(app_config.max_concurrent_ai_requests)
    cache_lock = asyncio.Lock()
    produced: List[str] = []
    stats = {"written": 0, "unchanged": 0, "maturity_cached": 0, "maturity_generated": 0, "skipped": 0}

    items = list(baustein_map.items())
    if app_config.is_test_mode:
        items = items[:3]
        logger.info("TEST mode: limiting to the first 3 Bausteine.")

    async def process_single_baustein(baustein_id: str, zielobjekt_uuid: str) -> None:
        nonlocal ai_client
        if zielobjekt_uuid == "Methodik" or str(zielobjekt_uuid).endswith("_prozesse"):
            return
        zo_name = zielobjekt_name_map.get(zielobjekt_uuid)
        baustein = bausteine.get(baustein_id)
        if not zo_name or not baustein:
            logger.warning(f"Baustein {baustein_id}: no Zielobjekt name ({zielobjekt_uuid}) or not in the catalog; skipped.")
            stats["skipped"] += 1
            return
        ordered = order_anforderungen([r for r in records.values() if r["baustein"] == baustein_id])
        if not ordered:
            logger.warning(f"Baustein {baustein_id} has no Anforderungen; skipped.")
            stats["skipped"] += 1
            return
        herkunft = "NG" if baustein_id in ng["bausteine"] else "BSI"
        first, _, _ = control_placement(ordered, abgleich)
        ng_needed = sorted(c for c in first if c.startswith("NG-"))
        if ng_needed and not ng_sha:
            raise RuntimeError(f"Baustein {baustein_id} needs NG controls but {NG_KATALOG_PATH} is missing — run stage_ng_katalog.")
        unknown = [c for c in ng_needed if c not in ng_ids_available]
        if unknown:
            raise RuntimeError(f"Baustein {baustein_id}: NG controls {unknown[:3]} not in the NG catalog — rerun stage_ng_katalog.")
        gpp_ids = sorted(c for c in first if not c.startswith("NG-"))

        # Maturity: cache first, model only for the rest.
        maturity: Dict[str, Dict[str, Any]] = {}
        missing: List[str] = []
        for cid in gpp_ids:
            block = maturity_for(cache, baustein_id, cid, gpp_controls_lookup.get(cid, {}).get("prose", ""))
            if block:
                maturity[cid] = block
            else:
                missing.append(cid)
        stats["maturity_cached"] += len(maturity)
        if missing:
            if ai_client is None:
                ai_client = AiClient(app_config)
            generated = await generate_maturity_blocks(
                baustein_id, baustein["title"], baustein.get("zielsetzung", ""), missing,
                gpp_controls_lookup, prompt_instruction, enhanced_schema, ai_client, sem,
            )
            stats["maturity_generated"] += len(generated)
            maturity.update(generated)
            async with cache_lock:
                slot = cache.setdefault(baustein_id, {})
                for cid, block in generated.items():
                    slot[cid] = {"by-id": block["by-id"], "parts": block["parts"]}
                save_maturity_cache(cache)

        ctx = {
            "baustein_id": baustein_id, "baustein_title": baustein["title"], "zielobjekt_name": zo_name,
            "herkunft": herkunft, "ordered": ordered, "abgleich": abgleich, "version": version,
            "ng_sha256": ng_sha, "ng_total": ng_total, "ng_title": ng_title,
        }
        stem = profile_file_stem(zo_name, baustein_id, baustein["title"], herkunft == "NG")
        for variant, suffix in (("plain", ".json"), ("enhanced", "_enhanced.json")):
            path = os.path.join(ED23_PROFILES_DIR, f"{stem}{suffix}")
            doc = build_profile(ctx, variant, maturity)
            problems = validate_ed23_profile_structure(doc, ng_ids_available or None, os.path.basename(path))
            if problems:
                logger.warning(f"Profile {os.path.basename(path)} has {len(problems)} structural issue(s): "
                               + "; ".join(problems[:10]) + (" ..." if len(problems) > 10 else ""))
            if write_if_changed(path, doc):
                stats["written"] += 1
                logger.info(f"Wrote {os.path.basename(path)} ({len(gpp_ids)} G++ + {len(ng_needed)} NG controls, "
                            f"{len(ordered)} Anforderungen).")
            else:
                stats["unchanged"] += 1
            produced.append(os.path.basename(path))

    await asyncio.gather(*(process_single_baustein(b, z) for b, z in items))

    if ai_client is not None:
        ai_client.log_usage_summary("stage_ED23_profiles_enhanced")
    if not app_config.is_test_mode:
        stale = [os.path.basename(p) for p in glob.glob(os.path.join(ED23_PROFILES_DIR, "*.json"))
                 if os.path.basename(p) not in produced and os.path.basename(p) != NG_KATALOG_FILENAME]
        if stale:
            if app_config.overwrite_temp_files:
                for name in stale:
                    os.remove(os.path.join(ED23_PROFILES_DIR, name))
                logger.info(f"Removed {len(stale)} stale profile file(s) (--fresh).")
            else:
                logger.warning(f"{len(stale)} file(s) in {ED23_PROFILES_DIR} were not produced by this run "
                               f"(remove with --fresh): {', '.join(stale[:5])}{' ...' if len(stale) > 5 else ''}")
    logger.info(f"Finished Stage: ED2023 Baustein Profile Generation — {stats}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    asyncio.run(run_stage_ED23_profiles_enhanced())
