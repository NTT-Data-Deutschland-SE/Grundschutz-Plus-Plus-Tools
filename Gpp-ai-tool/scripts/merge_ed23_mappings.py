#!/usr/bin/env python3
"""Merges the ED23-seitige Satz-Abdeckung into the GS++->ED23 mapping (deterministic).

Union of the two matching directions, both grounded on the OFFICIAL XML Kompendium:

  * hilfsdateien/gpp_ed23_anforderungen.json — GS++-seitig (stage_ed23_anforderungen,
    maker-checker per G++ control), official satz_nr since the XML-corpus rebuild.
  * hilfsdateien/ed23_satz_abdeckung.json — ED23-seitig (stage_ed23_satz_abdeckung,
    maker-checker per official normative sentence).

Every entry is keyed (control, Anforderung, satz_nr). Existing entries get the provenance
prop ``matching-direction: gpp-seitig`` (or ``beide`` when the Satz-Abdeckung confirms the
same triple); Satz-Abdeckung triples the mapping does not know become new entries with
``matching-direction: ed23-seitig``. Labels are rebuilt from the pinned official XML, so
new targets carry the same 'Titel (B) [Rolle]' labels as existing ones. New entries carry
no relationship yet — run stage_ed23_relationen AFTER this merge (its skip guard expects
the pre-classification state, so the intended order is: v2 mapping run -> this merge ->
relationship classification).

Deterministic and idempotent for a given input pair and --date. No AI involved.

Usage:
    uv run Gpp-ai-tool/scripts/merge_ed23_mappings.py [--date YYYY-MM-DD] [--dry-run]
"""

import argparse
import json
import logging
import os
import sys
from datetime import date

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(REPO_ROOT, "Gpp-ai-tool", "src"))

from utils.ed23_xml import fetch_official_xml, load_official_xml  # noqa: E402
from utils.oscal_mapping import to_oscal_mapping_collection  # noqa: E402
from pipeline.stage_ed23_anforderungen import anforderung_label  # noqa: E402
from pipeline.stage_ed23_relationen import load_mapping_matches  # noqa: E402
from constants import (  # noqa: E402
    GPP_ED23_ANFORDERUNGEN_JSON_PATH,
    ED23_SATZ_ABDECKUNG_JSON_PATH,
)


def main(argv=None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--date", default=date.today().isoformat(),
                        help="Metadata-Version (fixieren für byte-stabile Re-Runs)")
    parser.add_argument("--dry-run", action="store_true",
                        help="nur Statistik ausgeben, nichts schreiben")
    args = parser.parse_args(argv)

    with open(GPP_ED23_ANFORDERUNGEN_JSON_PATH, "r", encoding="utf-8") as f:
        per_control = load_mapping_matches(json.load(f))
    if not os.path.exists(ED23_SATZ_ABDECKUNG_JSON_PATH):
        print("FEHLER: hilfsdateien/ed23_satz_abdeckung.json fehlt — erst "
              "stage_ed23_satz_abdeckung laufen lassen.")
        return 1
    with open(ED23_SATZ_ABDECKUNG_JSON_PATH, "r", encoding="utf-8") as f:
        satz_doc = json.load(f)["ed23_satz_abdeckung"]

    xml_bytes, _sha = fetch_official_xml()
    official, _rejected = load_official_xml(xml_bytes)

    # Existing triples, provenance-tagged.
    index = {}
    for control_id, matches in per_control.items():
        for match in matches:
            match.setdefault("richtung", "gpp-seitig")
            index[(control_id, match["id"], match.get("satz_nr") or 0)] = match

    bestand = len(index)
    beide = neu = verworfen = 0
    for rid in sorted(satz_doc.get("anforderungen", {})):
        rec = satz_doc["anforderungen"][rid]
        req = official.get(rid)
        if req is None or req.get("entfallen"):
            verworfen += len(rec.get("treffer", []))
            continue
        for hit in rec.get("treffer", []) or []:
            control_id = hit["control_id"]
            satz_nr = int(hit["satz_nr"])
            key = (control_id, rid, satz_nr)
            existing = index.get(key)
            if existing is not None:
                existing["richtung"] = "beide"
                beide += 1
                continue
            begruendung = (hit.get("begruendung") or "").strip()
            match = {
                "id": rid,
                "name": anforderung_label(req),
                "begruendung": f"(Teilanforderung {satz_nr}) {begruendung}".strip(),
                "satz_nr": satz_nr,
                "relationship": None,   # classified by stage_ed23_relationen afterwards
                "richtung": "ed23-seitig",
            }
            per_control.setdefault(control_id, []).append(match)
            index[key] = match
            neu += 1

    gesamt = sum(len(m) for m in per_control.values())
    print(f"Bestand: {bestand} | davon beidseitig bestätigt: {beide} | "
          f"neu aus Satz-Abdeckung: {neu} | verworfen (entfallen/unbekannt): {verworfen} | "
          f"Gesamt nach Merge: {gesamt}")
    assert gesamt == bestand + neu, "Merge-Arithmetik verletzt"

    if args.dry_run:
        return 0
    output = to_oscal_mapping_collection(
        per_control, last_modified=f"{args.date}T00:00:00+00:00", version=args.date
    )
    with open(GPP_ED23_ANFORDERUNGEN_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Geschrieben: {os.path.relpath(GPP_ED23_ANFORDERUNGEN_JSON_PATH, REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
