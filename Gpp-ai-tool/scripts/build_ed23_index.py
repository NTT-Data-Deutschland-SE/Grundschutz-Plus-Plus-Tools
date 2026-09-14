#!/usr/bin/env python3
"""Kompakter Index ED23-Anforderung -> GS++-Controls fuer den SSP-Generator.

Quelle: hilfsdateien/gpp_ed23_anforderungen.json (OSCAL mapping-collection,
Richtung GS++ -> ED23, rund 5.000 Maps, Status draft). Der Generator braucht
die Rueckrichtung je Kompendiums-ID und nur ID plus Relation; die volle Datei
waere 6,8 MB je Seitenaufruf.

Aufruf:  python Gpp-ai-tool/scripts/build_ed23_index.py
Ausgabe: hilfsdateien/ed23_gpp_index.json
"""
import json, pathlib, collections, datetime

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = ROOT / "hilfsdateien" / "gpp_ed23_anforderungen.json"
OUT = ROOT / "hilfsdateien" / "ed23_gpp_index.json"
REL_ORDER = ["equal-to", "equivalent-to", "subset-of", "superset-of", "intersects-with"]


def main():
    data = json.load(open(SRC, encoding="utf-8"))
    coll = data["mapping-collection"]
    index = collections.defaultdict(list)
    for mapping in coll.get("mappings", []):
        for m in mapping.get("maps", []):
            rel = m.get("relationship", "")
            sources = [s.get("id-ref") for s in m.get("sources", []) if s.get("type") == "control"]
            for t in m.get("targets", []):
                if t.get("type") != "control":
                    continue
                key = str(t.get("id-ref", "")).upper()
                for sid in sources:
                    entry = {"id": sid, "rel": rel}
                    if entry not in index[key]:
                        index[key].append(entry)
    for key in index:
        index[key].sort(key=lambda e: (REL_ORDER.index(e["rel"]) if e["rel"] in REL_ORDER else 99, e["id"]))
    out = {
        "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "source": {"file": SRC.name, "version": coll.get("metadata", {}).get("version"),
                   "status": coll.get("provenance", {}).get("status"), "maps": sum(len(m.get("maps", [])) for m in coll.get("mappings", []))},
        "relationships": REL_ORDER,
        "index": dict(sorted(index.items())),
    }
    OUT.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"{OUT.name}: {len(index)} ED23-Anforderungen, {OUT.stat().st_size / 1024:.0f} kB")


if __name__ == "__main__":
    main()
