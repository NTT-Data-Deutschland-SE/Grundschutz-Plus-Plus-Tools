"""
Pipeline Stage: the shared NG Ergänzungskatalog (deterministic, no model).

Collects every `neues_control` of hilfsdateien/ed23_baustein_abgleich.json into ONE OSCAL
1.2.2 catalog, ED23-Baustein-profile/DE/NG-ergaenzungskatalog.json, grouped layer → Baustein.
A profile cannot define controls (Handbuch 3.15), so the NG controls live here and every
profile that needs them imports this file as its second import with a relative rlink and the
file's SHA-256 (fail closed). Everything in here is nutzergeneriert: ids `NG-<AnforderungsID>`,
titles `NG: …`, class `ng-ergaenzung`, prop herkunft=NG.

Idempotent: the document is rebuilt and only written when it differs from the file on disk
(ignoring last-modified), so the hash the profiles embed stays stable across no-op runs.
"""

import datetime
import logging
import os
import uuid
from typing import Any, Dict, List, Optional

from utils.data_loader import load_json_file
from utils.file_utils import read_csv_file, read_json_file, write_json_file
from utils.ed23_baustein import anforderung_sort_key, baustein_sort_key, iter_bausteine, load_ed23_catalogs, ng_title
from utils.oscal_utils import (
    make_prop as _prop,
    extract_all_gpp_controls,
    json_equal_ignoring,
    pinned_catalog_resource,
    pinned_ed23_catalog_resource,
    pinned_ed23_plain_catalog_resource,
    sha256_of_file,
)
from constants import (
    BSI_2023_JSON_PATH,
    BSI_2023_PLAIN_JSON_PATH,
    BSI_GRUNDSCHUTZ_NS,
    BUILD_VERSION,
    ED23_BAUSTEIN_ABGLEICH_JSON_PATH,
    ED23_BAUSTEIN_NS,
    ED23_CATALOG_PIN_COMMIT,
    GPP_CATALOG_PIN_COMMIT,
    GPP_CATALOG_PIN_SHA256,
    GPP_KOMPENDIUM_JSON_PATH,
    NG_KATALOG_PATH,
    OSCAL_VERSION,
    PRACTICE_ABBREVIATIONS,
    SDT_MODAL_VERB_NS,
    SDT_SECURITY_LEVEL_CSV_PATH,
    SDT_SECURITY_LEVEL_NS,
    SDT_TARGET_OBJECT_NS,
)

logger = logging.getLogger(__name__)

NG_KATALOG_TITLE = (
    "NG Ergänzungskatalog zu den ED23-Baustein-Profilen – Anforderungen ohne Entsprechung im "
    "Anwenderkatalog Grundschutz++"
)
NG_KATALOG_UUID = str(uuid.uuid5(uuid.NAMESPACE_URL, "ng-ergaenzungskatalog"))
SEC_LEVEL_NORMAL = "normal-SdT"


def sec_level_for(level_num: Optional[str], hoch_token: Optional[str]) -> str:
    """BSI level 1/3 (Basis/Standard) form the normal baseline; 5 (erhöht) maps to the SdT token
    for the raised level when the pinned vocabulary has one."""
    if level_num == "5" and hoch_token:
        return hoch_token
    return SEC_LEVEL_NORMAL


def build_ng_control(anf_id: str, rec: Dict[str, Any], gpp_titles: Dict[str, str], hoch_token: Optional[str]) -> Dict[str, Any]:
    nc = rec["neues_control"]
    cid = nc["id"]
    herkunft_remark = (
        f"Herkunft: vom Modell formuliert (Konfidenz {nc.get('konfidenz') or 'n/a'}, Checker "
        f"{nc.get('checker') or 'nicht geprüft'}); kein passendes Control im Anwenderkatalog Grundschutz++ "
        f"(Pin {GPP_CATALOG_PIN_COMMIT[:12]})"
    )
    props = [
        _prop("alt-identifier", str(uuid.uuid5(uuid.NAMESPACE_URL, f"ng-ergaenzungskatalog:control:{cid}"))),
        _prop("ed23-anforderung", anf_id, ED23_BAUSTEIN_NS, herkunft_remark),
        _prop("herkunft", "NG", ED23_BAUSTEIN_NS),
        _prop("praktik", nc["praktik"], ED23_BAUSTEIN_NS,
              f"Praktik des Anwenderkatalogs: {PRACTICE_ABBREVIATIONS.get(nc['praktik'], nc['praktik'])}"),
        _prop("sec_level", sec_level_for(rec.get("level_num"), hoch_token), SDT_SECURITY_LEVEL_NS),
    ]
    if rec.get("level_num"):
        props.append(_prop("level", str(rec["level_num"]), BSI_GRUNDSCHUTZ_NS))
    # OSCAL allows no `remarks` on a control: the checker's verdict and reasoning live in a prop.
    checker_remark = " ".join(
        s for s in (f"Checker: {nc['checker_begruendung']}" if nc.get("checker_begruendung") else "",
                    f"Hinweis: {nc['hinweis']}" if nc.get("hinweis") else "") if s) or None
    props.append(_prop("checker", nc.get("checker") or "nicht geprüft", ED23_BAUSTEIN_NS, checker_remark))
    stm_props = []
    if nc.get("zielobjektkategorien"):
        stm_props.append(_prop("target_object_categories", ", ".join(nc["zielobjektkategorien"]), SDT_TARGET_OBJECT_NS))
    stm_props.append(_prop("modal_verb", nc["modalverb"], SDT_MODAL_VERB_NS))
    parts = [{"id": f"{cid}_stm", "name": "statement", "props": stm_props, "prose": nc["statement"]}]
    if nc.get("guidance"):
        parts.append({"id": f"{cid}_gdn", "name": "guidance", "prose": nc["guidance"]})
    control = {"id": cid, "class": "ng-ergaenzung", "title": ng_title(nc["titel"]), "props": props, "parts": parts}
    links = [
        {"href": f"{GPP_KOMPENDIUM_JSON_PATH}#{rel}", "rel": "related",
         "text": f"{rel} {gpp_titles.get(rel, '')} (Anwenderkatalog Grundschutz++)".strip()}
        for rel in nc.get("verwandte_controls") or []
    ]
    if links:
        control["links"] = links
    return control


def build_ng_katalog(
    abgleich: Dict[str, Any], bd: Dict[str, Any], gpp_titles: Dict[str, str],
    hoch_token: Optional[str], last_modified: str,
) -> Dict[str, Any]:
    """Pure builder: the catalog document from the abgleich file (no I/O)."""
    root = abgleich.get("ed23_baustein_abgleich", abgleich)
    meta = root.get("meta", {}) or {}
    ng_bausteine = set(meta.get("ng_bausteine") or [])
    bausteine = {b["id"]: b for b in iter_bausteine(bd)}
    with_new = {aid: r for aid, r in (root.get("anforderungen") or {}).items() if r.get("neues_control")}

    layers: Dict[str, Dict[str, Any]] = {}
    for aid in sorted(with_new, key=anforderung_sort_key):
        rec = with_new[aid]
        bid = rec["baustein"]
        b = bausteine.get(bid, {"layer_id": bid.split(".")[0], "layer_title": bid.split(".")[0], "title": bid})
        layer = layers.setdefault(b["layer_id"], {"id": b["layer_id"], "class": "layer", "title": b["layer_title"], "groups": {}})
        is_ng = bid in ng_bausteine
        group = layer["groups"].setdefault(bid, {
            "id": bid, "class": "ng-baustein" if is_ng else "baustein",
            "title": f"{'NG ' if is_ng else ''}{bid} – {b['title']}",
            "props": [_prop("herkunft", "NG" if is_ng else "BSI", ED23_BAUSTEIN_NS,
                            "Herkunft des Bausteins; die Controls dieser Gruppe sind in jedem Fall NG")],
            "controls": [],
        })
        group["controls"].append(build_ng_control(aid, rec, gpp_titles, hoch_token))

    groups = []
    for lid in sorted(layers, key=lambda x: baustein_sort_key(x)):
        layer = layers[lid]
        layer["groups"] = [layer["groups"][bid] for bid in sorted(layer["groups"], key=baustein_sort_key)]
        groups.append(layer)
    n = len(with_new)
    model_note = (f"Modell {meta.get('model', '?')} (Maker thinking {meta.get('maker_thinking', '?')}, "
                  f"Checker thinking {meta.get('checker_thinking', '?')})")
    catalog = {
        "catalog": {
            "uuid": NG_KATALOG_UUID,
            "metadata": {
                "title": NG_KATALOG_TITLE,
                "last-modified": last_modified,
                "version": str(meta.get("version") or datetime.date.today().isoformat()),
                "oscal-version": OSCAL_VERSION,
                "props": [
                    _prop("herkunft", "NG", ED23_BAUSTEIN_NS),
                    _prop("ed23-katalog-pin", ED23_CATALOG_PIN_COMMIT, ED23_BAUSTEIN_NS),
                    _prop("keywords", "NG, Nutzergenerierte Inhalte, ED23, IT-Grundschutz, Grundschutz++"),
                ],
                "links": [
                    {"href": BSI_2023_JSON_PATH, "rel": "source",
                     "text": "BSI IT-Grundschutz Edition 2023 als OSCAL, benutzerdefinierte Ausgabe (NTT DATA DACH)"},
                    {"href": BSI_2023_PLAIN_JSON_PATH, "rel": "source",
                     "text": "BSI IT-Grundschutz Edition 2023 als OSCAL, nur BSI-Bausteine (NTT DATA DACH)"},
                    {"href": GPP_KOMPENDIUM_JSON_PATH, "rel": "reference", "text": "Anwenderkatalog Grundschutz++ (BSI)"},
                ],
                "remarks": (
                    f"Erzeugt von Gpp-ai-tool {BUILD_VERSION} (stage_ed23_baustein_abgleich, stage_ng_katalog). "
                    f"Enthält {n} Controls für Anforderungen der ED23-Bausteine, für die der Anwenderkatalog "
                    f"Grundschutz++ (Pin {GPP_CATALOG_PIN_COMMIT[:12]}) keine Entsprechung bietet, gruppiert nach "
                    f"Schicht und Baustein. Die Statements sind Formulierungen des Modells ({model_note}), vom "
                    f"Checker beurteilt, keine amtlichen Texte des BSI; jedes Control nennt seine Anforderung, "
                    f"Herkunft und Praktik als Props. Nutzergenerierte Inhalte (NG): kein Dokument des BSI. "
                    f"ED23-Katalog Pin {ED23_CATALOG_PIN_COMMIT[:12]}."
                ),
            },
            "groups": groups,
            "back-matter": {"resources": [
                pinned_catalog_resource(), pinned_ed23_catalog_resource(), pinned_ed23_plain_catalog_resource(),
            ]},
        }
    }
    return catalog


def load_hoch_token() -> Optional[str]:
    """The raised-security-level token of the pinned security_level.csv (e.g. 'erhöht')."""
    try:
        rows = read_csv_file(SDT_SECURITY_LEVEL_CSV_PATH) or []
    except Exception as e:  # noqa: BLE001 — the vocabulary is a nicety; normal-SdT stays the fallback
        logger.warning(f"security_level.csv unavailable ({e}); using {SEC_LEVEL_NORMAL} for every level.")
        return None
    tokens = [(r.get("Begriff") or "").strip() for r in rows]
    others = [t for t in tokens if t and t != SEC_LEVEL_NORMAL]
    return others[0] if others else None


def run_stage_ng_katalog() -> None:
    logger.info("Starting stage_ng_katalog...")
    if not os.path.exists(ED23_BAUSTEIN_ABGLEICH_JSON_PATH):
        raise RuntimeError(f"{ED23_BAUSTEIN_ABGLEICH_JSON_PATH} missing — run stage_ed23_baustein_abgleich first.")
    abgleich = read_json_file(ED23_BAUSTEIN_ABGLEICH_JSON_PATH)
    bd, _plain = load_ed23_catalogs()
    gpp_catalog = load_json_file(GPP_KOMPENDIUM_JSON_PATH, expected_sha256=GPP_CATALOG_PIN_SHA256)
    gpp_titles = {cid: (c.get("title") or "") for cid, c in extract_all_gpp_controls(gpp_catalog).items()}
    hoch_token = load_hoch_token()

    existing = read_json_file(NG_KATALOG_PATH) if os.path.exists(NG_KATALOG_PATH) else None
    previous_ts = ((existing or {}).get("catalog", {}).get("metadata", {}) or {}).get("last-modified")
    new_doc = build_ng_katalog(abgleich, bd, gpp_titles, hoch_token, previous_ts or "")
    n = sum(len(g["controls"]) for layer in new_doc["catalog"]["groups"] for g in layer["groups"])
    if n == 0:
        if existing:
            os.remove(NG_KATALOG_PATH)
            logger.info("No NG controls in the abgleich; removed the existing NG catalog.")
        else:
            logger.info("No NG controls in the abgleich; no NG catalog written.")
        return
    if existing and json_equal_ignoring(new_doc, existing):
        logger.info(f"NG catalog unchanged ({n} controls); SHA-256 {sha256_of_file(NG_KATALOG_PATH)}.")
        return
    new_doc["catalog"]["metadata"]["last-modified"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    write_json_file(NG_KATALOG_PATH, new_doc)
    logger.info(f"NG catalog written: {n} controls, SHA-256 {sha256_of_file(NG_KATALOG_PATH)} → {NG_KATALOG_PATH}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    run_stage_ng_katalog()
