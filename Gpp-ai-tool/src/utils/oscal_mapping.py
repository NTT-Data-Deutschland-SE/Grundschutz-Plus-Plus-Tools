"""
OSCAL Control Mapping model serialization (OSCAL 1.2.2).

Converts the internal per-control match map produced by
``stage_ed23_anforderungen`` — ``{control_id: [{id, name, begruendung}, ...]}`` —
into a standards-conformant OSCAL ``mapping-collection`` document:
https://pages.nist.gov/OSCAL-Reference/models/v1.2.2/mapping/

Modelling choices (see the mapping metaschema for the authoritative vocabulary):

* One ``mapping`` whose source is the Grundschutz++ catalog and whose target is
  the BSI IT-Grundschutz Edition 2023 catalog.
* One ``map`` per (G++ control, ED2023 Anforderung) pair, so every match keeps
  its own justification: the Anforderung ``name`` becomes a ``label`` prop on the
  target item and the ``begruendung`` becomes the map's ``remarks``. When the
  match carries a validated ``satz_nr`` (the number of the "Teilanforderung" —
  the numbered sentence of the Anforderung's prose that carries the match), it
  is additionally recorded as a ``statement-sentence`` prop on the target item
  (the Begründung text already starts with ``(Teilanforderung n)``). The term
  "Teilanforderung" appears in no BSI standard; it is used only in one
  paragraph of the BSI Auditierungsschema.
* ``relationship`` defaults to ``intersects-with`` — the LLM identifies related /
  overlapping requirements, not proven equality (allowed tokens: equivalent-to,
  equal-to, subset-of, superset-of, intersects-with, no-relationship). A match may
  carry its own ``relationship`` (set by stage_ed23_relationen's classification pass,
  OSCAL semantics: the token describes the SOURCE — the G++ control — relative to the
  target Anforderung); it then overrides the default for that map entry.
* ``provenance`` records that this is an automated, semantic, draft mapping
  (method=automation, matching-rationale=semantic, status=draft).

UUIDs are derived deterministically (uuid5) from the pair identifiers so
re-generation produces stable diffs instead of churning every identifier.
"""
from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

from constants import GPP_KOMPENDIUM_JSON_PATH, OSCAL_VERSION, GPP_ENHANCEMENT_PROPS_NS
from utils.ed23_xml import BSI_XML_URL

# Internal (pre-OSCAL) top-level key of the bespoke lookup this module replaces.
MAP_KEY = "gpp_ed23_anforderungen_map"

# Stable namespace UUID so the uuid5-derived identifiers never change between runs.
_NS = uuid.uuid5(uuid.NAMESPACE_DNS, "grundschutz-plus-plus.gpp-ed23-anforderungen")


def _uuid(*parts: str) -> str:
    """A deterministic RFC-4122 v5 UUID derived from the given identifier parts."""
    return str(uuid.uuid5(_NS, "|".join(parts)))


def to_oscal_mapping_collection(
    per_control_map: Dict[str, List[Dict[str, str]]],
    *,
    source_href: str = GPP_KOMPENDIUM_JSON_PATH,
    target_href: str = BSI_XML_URL,
    relationship: str = "intersects-with",
    last_modified: Optional[str] = None,
    version: Optional[str] = None,
) -> Dict[str, Any]:
    """Build an OSCAL 1.2.2 ``mapping-collection`` from the internal control→Anforderungen map.

    Args:
        per_control_map: Maps each G++ control id to a list of matching ED2023
            Anforderungen, each ``{"id", "name", "begruendung"}`` plus an
            optional ``satz_nr`` (validated matching-sentence number).
        source_href / target_href: Hrefs recorded on the source/target catalog
            resource references (default to the project's catalog URLs).
        relationship: Mapping relationship token applied to every map entry.
        last_modified / version: Metadata values. Pass fixed values to make the
            whole document reproducible; otherwise the current UTC time / date is
            used (UUIDs are deterministic regardless).

    Returns:
        The OSCAL document as a ``dict`` ready to be JSON-serialized.
    """
    now = datetime.now(timezone.utc)
    last_modified = last_modified or now.replace(microsecond=0).isoformat()
    version = version or now.strftime("%Y-%m-%d")

    maps: List[Dict[str, Any]] = []
    for control_id in sorted(per_control_map):
        matches = sorted(
            per_control_map[control_id],
            key=lambda m: (m.get("id", ""), m.get("satz_nr") or 0),
        )
        for match in matches:
            target_id = match.get("id")
            if not target_id:
                continue
            target: Dict[str, Any] = {"type": "control", "id-ref": target_id}
            props: List[Dict[str, str]] = []
            name = (match.get("name") or "").strip()
            if name:
                props.append({"name": "label", "value": name})
            satz_nr = match.get("satz_nr")
            if isinstance(satz_nr, int) and satz_nr > 0:
                props.append({"name": "statement-sentence", "value": str(satz_nr)})
            if props:
                target["props"] = props

            # The uuid includes the satz_nr: since the merge of the ED23-seitige
            # Satz-Abdeckung a (control, Anforderung) pair may legitimately carry several
            # map entries, one per covered Teilanforderung.
            entry: Dict[str, Any] = {
                "uuid": _uuid("map", control_id, target_id, str(satz_nr or 0)),
                "relationship": match.get("relationship") or relationship,
                "sources": [{"type": "control", "id-ref": control_id}],
                "targets": [target],
            }
            richtung = (match.get("richtung") or "").strip()
            if richtung:
                # Provenance of the pair: which matching direction found it
                # (gpp-seitig, ed23-seitig, beide). Custom prop, documented namespace.
                entry["props"] = [{
                    "name": "matching-direction", "value": richtung,
                    "ns": GPP_ENHANCEMENT_PROPS_NS,
                }]
            begruendung = (match.get("begruendung") or "").strip()
            if begruendung:
                entry["remarks"] = begruendung
            maps.append(entry)

    mapping = {
        "uuid": _uuid("mapping", source_href, target_href),
        "source-resource": {"type": "catalog", "href": source_href},
        "target-resource": {"type": "catalog", "href": target_href},
        "maps": maps,
    }

    return {
        "mapping-collection": {
            "uuid": _uuid("mapping-collection"),
            "metadata": {
                "title": "Grundschutz++ → BSI IT-Grundschutz Edition 2023 Anforderungen",
                "last-modified": last_modified,
                "version": version,
                "oscal-version": OSCAL_VERSION,
            },
            "provenance": {
                "method": "automation",
                "matching-rationale": "semantic",
                "status": "draft",
                "mapping-description": (
                    "Automatisch erzeugte Zuordnung jeder Grundschutz++ Control zu den "
                    "inhaltlich passenden BSI IT-Grundschutz Edition 2023 Anforderungen "
                    "(LLM-gestützter semantischer Abgleich in zwei Stufen — Kandidatensuche "
                    "und strenge Einzelprüfung —, jede ID gegen den ED2023-Katalog validiert). "
                    "Jede Zuordnung nennt die tragende „Teilanforderung“: den nummerierten "
                    "Satz der ED23-Anforderung (Begründungs-Präfix „(Teilanforderung n)“, "
                    "Prop statement-sentence). Der Begriff „Teilanforderung“ stammt aus "
                    "keinem BSI-Standard; er wird lediglich in einem Absatz des "
                    "BSI-Auditierungsschemas verwendet."
                ),
            },
            "mappings": [mapping],
        }
    }
