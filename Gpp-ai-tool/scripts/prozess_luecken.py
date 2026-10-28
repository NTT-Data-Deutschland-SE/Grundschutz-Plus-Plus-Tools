#!/usr/bin/env python3
"""prozess_luecken.py -- v1.0.0

Reproduziert die Tabelle „Prozess-Bausteine ohne GS++-Gegenstück" aus den Hilfsdateien:
je Prozess-Baustein (ISMS/ORP/CON/OPS/DER) die Zahl der aktiven Anforderungen, der
normativen Sätze, der durch die satzgenaue Beurteilung gedeckten Sätze, der Anteil, die
Anforderungen ohne einen einzigen gedeckten Satz und die Praktiken des 1:1-Mappings.

Das 1:1-Mapping (prozessbausteine_mapping.json) ist vollständigkeitsgetrieben und taugt
NICHT als Lückenmaß; das Lückenmaß ist die Satzabdeckung (ed23_satz_abdeckung.json).
Auswahlkriterium für ALLOWED_PROCESS_BAUSTEINE in src/constants.py: Satzabdeckung < 45 %
oder >= 5 trägerlose Anforderungen, und das Thema hat keine eigene Praktik.

Aufruf (aus Gpp-ai-tool/):
  uv run python scripts/prozess_luecken.py [--json] [--alle]
--alle zeigt alle Schichten, nicht nur die Prozess-Schichten.
"""

import argparse
import collections
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "src"))

from constants import (  # noqa: E402
    ALLOWED_PROCESS_BAUSTEINE,
    BSI_2023_JSON_PATH,
    ED23_BD_CATALOG_PIN_SHA256,
    ED23_SATZ_ABDECKUNG_JSON_PATH,
    PROZZESSBAUSTEINE_CONTROLS_JSON_PATH,
    PROZESSBAUSTEINE_LAYERS,
)
from utils.data_loader import load_json_file  # noqa: E402
from utils.ed23_baustein import baustein_sort_key, iter_bausteine  # noqa: E402


def analyse(layers):
    satz = load_json_file(ED23_SATZ_ABDECKUNG_JSON_PATH)["ed23_satz_abdeckung"]["anforderungen"]
    prozess = load_json_file(PROZZESSBAUSTEINE_CONTROLS_JSON_PATH).get("prozessbausteine_mapping", {})
    bd = load_json_file(BSI_2023_JSON_PATH, expected_sha256=ED23_BD_CATALOG_PIN_SHA256)
    titles = {b["id"]: b["title"] for b in iter_bausteine(bd)}

    per = {}
    for aid, a in satz.items():
        bid = aid.rsplit(".A", 1)[0]
        if layers and bid.split(".")[0] not in layers:
            continue
        norm = set(a.get("normative_saetze", []) or [])
        if not norm:
            continue
        cov = {t["satz_nr"] for t in a.get("treffer", []) or [] if t.get("satz_nr") in norm}
        row = per.setdefault(bid, {
            "baustein": bid, "titel": titles.get(bid, ""), "anforderungen": 0, "saetze": 0,
            "gedeckt": 0, "ohne_traeger": [], "praktiken": collections.Counter(),
        })
        row["anforderungen"] += 1
        row["saetze"] += len(norm)
        row["gedeckt"] += len(cov)
        if not cov:
            row["ohne_traeger"].append({"id": aid, "titel": a.get("titel", ""), "level": a.get("level")})
        if aid in prozess:
            row["praktiken"][prozess[aid].split(".")[0]] += 1
    rows = []
    for bid in sorted(per, key=baustein_sort_key):
        r = per[bid]
        r["anteil"] = round(100 * r["gedeckt"] / r["saetze"]) if r["saetze"] else 0
        r["praktiken"] = dict(r["praktiken"].most_common())
        r["kriterium"] = r["anteil"] < 45 or len(r["ohne_traeger"]) >= 5
        r["uebertragen"] = bid in ALLOWED_PROCESS_BAUSTEINE
        rows.append(r)
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true", help="Ergebnis als JSON auf stdout")
    ap.add_argument("--alle", action="store_true", help="alle Schichten statt nur ISMS/ORP/CON/OPS/DER")
    args = ap.parse_args()
    rows = analyse(None if args.alle else PROZESSBAUSTEINE_LAYERS)
    if args.json:
        json.dump(rows, sys.stdout, ensure_ascii=False, indent=1)
        return
    print("| Baustein | Titel | Anf | Sätze | gedeckt | % | ohne Träger | Kriterium | übertragen | Praktiken (1:1) |")
    print("|---|---|---:|---:|---:|---:|---:|:---:|:---:|---|")
    for r in rows:
        praks = ", ".join(f"{k}:{v}" for k, v in list(r["praktiken"].items())[:4])
        print(f"| {r['baustein']} | {r['titel'][:45]} | {r['anforderungen']} | {r['saetze']} | {r['gedeckt']} | "
              f"{r['anteil']} | {len(r['ohne_traeger'])} | {'ja' if r['kriterium'] else ''} | "
              f"{'ja' if r['uebertragen'] else ''} | {praks} |")
    n = sum(r["saetze"] for r in rows)
    c = sum(r["gedeckt"] for r in rows)
    print(f"\nSumme: {sum(r['anforderungen'] for r in rows)} Anforderungen, {n} normative Sätze, "
          f"{c} gedeckt ({round(100 * c / n) if n else 0} %), "
          f"{sum(len(r['ohne_traeger']) for r in rows)} Anforderungen ohne Träger.")
    print("\nAnforderungen ohne einen einzigen gedeckten normativen Satz:")
    for r in rows:
        for z in r["ohne_traeger"]:
            print(f"  {z['id']} {z['titel'][:60]} ({z['level']})")


if __name__ == "__main__":
    main()
