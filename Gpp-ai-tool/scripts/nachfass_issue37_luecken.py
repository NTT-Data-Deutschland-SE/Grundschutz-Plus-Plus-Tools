#!/usr/bin/env python3
"""Issue #37, Massnahme 5: gerichteter Luecken-Nachfass ueber die QS-Verdachtsliste.

Die QS-Stichprobe (hilfsdateien/ed23_mapping_qs/bericht.md, Abschnitt 8) benennt
kanonische ED23-Anker, die in den Paarlisten sonst guter Controls fehlen. Dieses
Skript prueft GENAU diese Kandidaten — kein Vollauf: je Kandidat ein strenger
Urteils-Call mit vollem Kontext beider Seiten (G++-Statement + Guidance; amtliche
Satzliste der Anforderung bzw. aller Anforderungen des genannten Bausteins) und
der Subsumtionsregel aus Issue #37. Ein leeres ``treffer`` ist ein zulaessiges und
erwuenschtes Ergebnis ("kein Treffer" schlaegt duenne Scheinpaare).

Akzeptierte Treffer werden dem Mapping mit ``matching-direction = qs-nachfass``
hinzugefuegt (Provenienz: weder gpp- noch ed23-seitige Kandidatensuche, sondern
QS-Beifang; Namespace-Doku aktualisiert) und in
``hilfsdateien/ed23_mapping_qs/nachfass_ergebnis.json`` protokolliert —
einschliesslich der Kandidaten OHNE Treffer.

WICHTIG: Erst nach Abschluss von stage_ed23_relationen laufen lassen (das Skript
schreibt das Mapping neu; parallel laufende Stages wuerden sich ueberschreiben).

Usage:
    cd Gpp-ai-tool/src && uv run --with google-genai --with jsonschema \
        python ../scripts/nachfass_issue37_luecken.py [--dry-run]
"""
import argparse
import asyncio
import json
import logging
import os
import re
import sys

SRC_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, SRC_ROOT)

from config import app_config  # noqa: E402
from clients.ai_client import AiClient  # noqa: E402
from utils.data_loader import load_json_file, save_json_file  # noqa: E402
from utils.oscal_mapping import to_oscal_mapping_collection  # noqa: E402
from pipeline.stage_ed23_anforderungen import build_gpp_match_contexts  # noqa: E402
from pipeline.stage_ed23_relationen import load_mapping_matches  # noqa: E402
from constants import (  # noqa: E402
    GPP_KOMPENDIUM_JSON_PATH,
    GPP_CATALOG_PIN_SHA256,
    GPP_ED23_ANFORDERUNGEN_JSON_PATH,
    ED23_ANFORDERUNGEN_STRIPPED_JSON_PATH,
)

logger = logging.getLogger(__name__)

NACHFASS_SCHEMA_PATH = os.path.join(SRC_ROOT, "assets/schemas/ed23_nachfass_response_schema.json")
ERGEBNIS_PATH = os.path.join(REPO_ROOT, "hilfsdateien", "ed23_mapping_qs", "nachfass_ergebnis.json")

# QS-Verdachtsliste (bericht.md Abschnitt 8 + CTRL-luecken-Felder der Reviewer-Protokolle).
# Ziel ist entweder eine konkrete Anforderungs-ID oder ein Baustein-Praefix (endet ohne .A).
CANDIDATES = [
    ("KONF.7.4", "SYS.1.1.A27"),
    ("KONF.10.2", "APP.3.2.A11"),
    ("KONF.10.2", "APP.4.3.A24"),
    ("GC.1.2", "ISMS.1.A3"),
    ("DET.3.1.6", "SYS.1.1.A10"),
    ("DET.3.1.8", "OPS.1.1.7.A25"),
    ("BER.2.4", "OPS.1.1.5.A3"),
    ("BER.7.6", "CON.1.A1"),
    ("VRB.4.1", "DER.3.1.A5"),
    ("REA.2.6", "DER.2.1.A6"),
    ("REA.2.2", "OPS.1.1.4.A9"),
    ("SENS.9.6", "INF.9.A2"),
    ("SENS.2.4", "SYS.4.5.A1"),
    ("UMS.2.2", "ISMS.1.A10"),
    ("UMS.2.2", "OPS.1.1.3.A15"),
    ("UMS.6.1", "ISMS.1.A12"),
    ("VRB.6.2", "ORP.3.A8"),
    ("NOT.3.1", "DER.4.A1"),
    ("NOT.4.14", "CON.3.A12"),
    ("NOT.4.2", "APP.3.6.A9"),
    ("NOT.4.2", "OPS.1.1.7.A16"),
    ("PERS.4.2", "ORP.3.A1"),
    ("PERS.6.1.2", "ISMS.1.A6"),
    ("PERS.2.3.2", "SYS.1.5.A12"),
    # Baustein-weite Verdachte (Reviewer nannten das Thema, keine konkrete ID):
    ("ASST.4.2", "NET.3.3"),
    ("ASST.5.2", "OPS.1.1.3"),
    ("PERS.1.1.2", "OPS.1.1.3"),
]

PROMPT = """Du pruefst EINEN Verdachtsfall auf eine fehlende Zuordnung zwischen einer Grundschutz++-Massnahme und dem BSI-IT-Grundschutz-Kompendium Edition 2023. Der Verdacht stammt aus einer Qualitaetspruefung; er kann sich auch NICHT bestaetigen — ein leeres Ergebnis ist voellig legitim und besser als ein duennes Scheinpaar.

Quelle — Grundschutz++-Massnahme aus der Praktik "{praktik}":
ID: {control_id}
Titel: {title}
Anforderungstext (normativ): {prose}
Erlaeuterung (nicht normativ, praezisiert den Scope): {guidance}

Verdacht: In den Zuordnungen dieser Massnahme fehlt moeglicherweise ein Anker in: {target_desc}

Amtliche Saetze der Kandidaten-Anforderung(en), nummeriert:

{anf_block}

Bereits vorhandene Zuordnungen dieser Massnahme zu den Kandidaten-Anforderungen (nicht doppeln!): {existing}

Aufgabe: Benenne NUR belastbare Treffer — Saetze, deren geforderte Taetigkeit oder Pflicht sich mit dem Anforderungstext der Massnahme substanziell ueberschneidet oder in einem Teilmengenverhaeltnis steht. Regeln:
1. Subsumtionsregel: superset-of nur, wenn die Massnahme die Forderung des Satzes VOLLSTAENDIG einschliesst; enthaelt der Satz eine zusaetzliche Pflicht (zweites Verb, andere Phase, breiterer Gegenstand), waehle intersects-with bzw. subset-of.
2. Keine Keyword-Treffer: gleiche Woerter ohne gleiche Pflicht sind KEIN Treffer.
3. Massgeblich ist der normative Anforderungstext; die Erlaeuterung praezisiert nur den Scope.
4. Begruendung: 1-2 Saetze, beide Seiten ehrlich; "deckt ... ab" nur bei superset-of/equal-to/equivalent-to; Verbindlichkeit der Massnahme (MUSS/SOLLTE/KANN) nie verschaerfen; kein "(Teilanforderung n)"-Praefix.
5. Hoechstens die 1-3 staerksten Saetze je Anforderung, nicht jeden entfernt passenden.

Gib ausschliesslich JSON nach Schema: treffer = Liste (ggf. leer) mit anf_id, satz_nr, relationship, begruendung."""


def _anf_block(anf_list):
    lines = []
    for a in anf_list:
        lines.append(f"### {a['id']} — {a['name']}")
        lines.extend(f"(S{i}) {s}" for i, s in enumerate(a["saetze"], 1))
        lines.append("")
    return "\n".join(lines).strip()


async def main_async(dry_run: bool) -> None:
    with open(GPP_ED23_ANFORDERUNGEN_JSON_PATH, "r", encoding="utf-8") as f:
        mapping_doc = json.load(f)
    per_control = load_mapping_matches(mapping_doc)
    n_before = sum(len(v) for v in per_control.values())

    gpp_catalog = load_json_file(GPP_KOMPENDIUM_JSON_PATH, expected_sha256=GPP_CATALOG_PIN_SHA256)
    stripped = load_json_file(ED23_ANFORDERUNGEN_STRIPPED_JSON_PATH)["ed23_anforderungen"]
    by_id = {a["id"]: a for a in stripped}
    gpp_contexts = build_gpp_match_contexts(gpp_catalog)
    schema = load_json_file(NACHFASS_SCHEMA_PATH)
    ai_client = AiClient(app_config)
    semaphore = asyncio.Semaphore(app_config.max_concurrent_ai_requests)

    async def judge(control_id: str, target: str):
        control = gpp_contexts.get(control_id)
        if control is None:
            return control_id, target, None, f"Control {control_id} nicht im Katalog"
        if re.search(r"\.A\d+$", target):
            anf_list = [by_id[target]] if target in by_id else []
        else:
            anf_list = [a for a in stripped if a["id"].startswith(target + ".A")]
        if not anf_list:
            return control_id, target, None, f"Ziel {target} nicht im Korpus"
        existing = sorted(
            f"{m['id']}:S{m.get('satz_nr') or 0}"
            for m in per_control.get(control_id, [])
            if any(m["id"] == a["id"] for a in anf_list)
        )
        prompt = PROMPT.format(
            praktik=control.get("praktik", ""),
            control_id=control_id,
            title=control.get("title", ""),
            prose=control.get("prose", ""),
            guidance=control.get("guidance") or "(keine)",
            target_desc=target if re.search(r"\.A\d+$", target) else f"Baustein {target}",
            anf_block=_anf_block(anf_list),
            existing=", ".join(existing) or "(keine)",
        )
        async with semaphore:
            try:
                verdict = await ai_client.generate_validated_json_response(
                    prompt=prompt,
                    json_schema=schema,
                    request_context_log=f"ED23Nachfass-{control_id}-{target}",
                )
            except Exception as e:
                return control_id, target, None, str(e)
        valid_ids = {a["id"] for a in anf_list}
        rows = []
        for t in verdict.get("treffer", []):
            if t.get("anf_id") not in valid_ids:
                continue
            n_s = len(by_id[t["anf_id"]]["saetze"])
            if not (isinstance(t.get("satz_nr"), int) and 1 <= t["satz_nr"] <= n_s):
                continue
            rows.append(t)
        return control_id, target, rows, None

    results = await asyncio.gather(*(judge(c, t) for c, t in CANDIDATES))

    protokoll, added, skipped = [], [], []
    for control_id, target, rows, err in results:
        if err or rows is None:
            protokoll.append({"control": control_id, "ziel": target, "fehler": err})
            continue
        accepted = []
        for t in rows:
            key_exists = any(
                m["id"] == t["anf_id"] and (m.get("satz_nr") or 0) == t["satz_nr"]
                for m in per_control.get(control_id, [])
            )
            if key_exists:
                skipped.append({"control": control_id, **t, "grund": "existiert bereits"})
                continue
            match = {
                "id": t["anf_id"],
                "name": by_id[t["anf_id"]]["name"],
                "satz_nr": t["satz_nr"],
                "relationship": t["relationship"],
                "begruendung": f"(Teilanforderung {t['satz_nr']}) {t['begruendung']}",
                "richtung": "qs-nachfass",
            }
            per_control.setdefault(control_id, []).append(match)
            added.append({"control": control_id, **t})
            accepted.append(t)
        protokoll.append({
            "control": control_id, "ziel": target,
            "treffer": accepted, "kein_treffer": not accepted,
        })

    n_after = sum(len(v) for v in per_control.values())
    print(f"Kandidaten: {len(CANDIDATES)}, neue Paare: {len(added)}, "
          f"schon vorhanden: {len(skipped)}, Paare {n_before} -> {n_after}.")
    for a in added:
        print(f"  + {a['control']} -> {a['anf_id']}:S{a['satz_nr']} [{a['relationship']}]")
    ohne = [p for p in protokoll if p.get("kein_treffer")]
    print(f"Kandidaten ohne Treffer: {len(ohne)} -> " + ", ".join(
        f"{p['control']}->{p['ziel']}" for p in ohne))

    if dry_run:
        print("Dry-Run: nichts geschrieben.")
        return
    save_json_file(to_oscal_mapping_collection(per_control), GPP_ED23_ANFORDERUNGEN_JSON_PATH)
    with open(ERGEBNIS_PATH, "w", encoding="utf-8") as f:
        json.dump({
            "beschreibung": (
                "Issue #37 Massnahme 5: gerichteter Luecken-Nachfass ueber die "
                "QS-Verdachtsliste (bericht.md Abschnitt 8). Neue Paare tragen "
                "matching-direction=qs-nachfass."
            ),
            "protokoll": protokoll, "uebersprungen": skipped,
        }, f, ensure_ascii=False, indent=2)
    print(f"Geschrieben: Mapping + {os.path.relpath(ERGEBNIS_PATH, REPO_ROOT)}")
    ai_client.log_usage_summary("nachfass_issue37_luecken")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    asyncio.run(main_async(args.dry_run))


if __name__ == "__main__":
    main()
