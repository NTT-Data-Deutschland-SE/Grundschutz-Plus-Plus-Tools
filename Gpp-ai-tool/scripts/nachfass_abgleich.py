"""Nachfass-Runde für hilfsdateien/ed23_baustein_abgleich.json.

Setzt die KI-Ergebnisse der Anforderungen zurück, die nach dem Checker ohne Control geblieben
sind (`ohne_control.art == "abgelehnt-durch-checker"`), damit der nächste Lauf von
`stage_ed23_baustein_abgleich` genau diese neu an Maker und Checker gibt (Resume: alles andere
wird aus der Datei übernommen, kein --fresh). Deterministische Zuordnungen bleiben stehen.

Hintergrund: Bis 5.0.1 verwarf der Filter ein vom Maker vorgeschlagenes neues Control, sobald
eine Zuordnung vorlag; lehnte der Checker dann alle Zuordnungen ab, blieb nichts. Seit dem Fix
bleibt das neue Control als Rückfalloption bis zum Checker-Urteil erhalten.

Aufruf (aus Gpp-ai-tool/):
    uv run python scripts/nachfass_abgleich.py            # zeigt, was zurückgesetzt würde
    uv run python scripts/nachfass_abgleich.py --write    # schreibt die Datei
    ./scripts/run_local.sh --stage stage_ed23_baustein_abgleich
"""

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))

from constants import ED23_BAUSTEIN_ABGLEICH_JSON_PATH  # noqa: E402

ART = "abgelehnt-durch-checker"


def reset_record(rec: dict) -> None:
    rec["zuordnungen"] = [z for z in rec.get("zuordnungen") or [] if z.get("quelle") != "ki"]
    rec["pruefung"] = None
    rec["neues_control"] = None
    rec["ohne_control"] = None
    rec["ki"] = None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true", help="Datei wirklich schreiben (sonst nur anzeigen)")
    ap.add_argument("--path", default=ED23_BAUSTEIN_ABGLEICH_JSON_PATH)
    args = ap.parse_args()
    if not os.path.exists(args.path):
        print(f"FEHLER: {args.path} nicht gefunden (Stage noch nicht gelaufen?)", file=sys.stderr)
        return 2
    with open(args.path, "r", encoding="utf-8") as f:
        data = json.load(f)
    anf = data["ed23_baustein_abgleich"]["anforderungen"]
    hits = [aid for aid, rec in anf.items() if (rec.get("ohne_control") or {}).get("art") == ART]
    print(f"{len(hits)} Anforderungen ohne Control nach Checker-Ablehnung:")
    for aid in hits:
        verworfen = (anf[aid].get("ki") or {}).get("verworfen") or []
        print(f"  {aid}: {len(verworfen)} verworfene Vorschläge")
    if not args.write:
        print("Trockenlauf; mit --write zurücksetzen.")
        return 0
    for aid in hits:
        reset_record(anf[aid])
    tmp = args.path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    os.replace(tmp, args.path)
    print(f"{len(hits)} Anforderungen zurückgesetzt; jetzt: ./scripts/run_local.sh --stage stage_ed23_baustein_abgleich")
    return 0


if __name__ == "__main__":
    sys.exit(main())
