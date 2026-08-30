#!/usr/bin/env python3
"""Issue #37 (Mapping-QS), deterministische Anteile: Streichliste + Tokenizer-Migration.

Zwei Phasen, beide ohne AI-Calls, beide auditierbar:

Phase A — Streichliste:
    Entfernt die 76 von der QS-Stichprobe beanstandeten Paare (Quelle:
    ``hilfsdateien/ed23_mapping_qs/tally.json``, Feld ``drop-ids`` je Control —
    das committete QS-Artefakt ist die Provenienz) aus dem Mapping UND die
    korrespondierenden ``treffer`` aus der Satz-Abdeckung (sonst wuerde ein
    kuenftiger Merge die Paare wieder einfuehren). Jeder Drop muss genau einen
    Mapping-Eintrag treffen, sonst Abbruch. Alle entfernten Eintraege werden
    vollstaendig nach ``hilfsdateien/ed23_mapping_qs/dropped_pairs.json``
    geschrieben (Audit + Wiederherstellbarkeit).

Phase B — Tokenizer-Migration:
    Der Satz-Splitter trennte "(engl. ..." mitten im Satz (Fix: "engl." in
    utils/sentence_split.ABBREVIATIONS). Diese Phase erzeugt die amtliche
    Satzliste neu (gepinntes BSI-XML aus dem Cache), berechnet je geaenderter
    Anforderung die Index-Abbildung alt->neu (nur Merges), migriert
    ``statement-sentence``-Props samt "(Teilanforderung n)"-Praefix der remarks
    im Mapping sowie ``n_saetze``/``normative_saetze``/``treffer[].satz_nr`` in
    der Satz-Abdeckung, dedupliziert dabei kollabierende Eintraege und schreibt
    das neue ``ed23_anforderungen_stripped.json``.

Validierung am Ende: Paarzahl == vorher - Drops - Dedupes; jede
``statement-sentence`` liegt in 1..n_saetze; kein Satz mit unbalancierten
Klammern mehr im Korpus; Praefix der remarks passt zur Satznummer.

Usage:
    uv run --with google-genai --with jsonschema \
        python Gpp-ai-tool/scripts/migrate_issue37_qs_fixes.py [--dry-run]
"""
import argparse
import json
import os
import re
import sys
from collections import defaultdict

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(REPO_ROOT, "Gpp-ai-tool", "src"))

from utils.ed23_xml import fetch_official_xml, load_official_xml  # noqa: E402
from utils.oscal_mapping import to_oscal_mapping_collection  # noqa: E402
from pipeline.stage_ed23_relationen import load_mapping_matches  # noqa: E402
from pipeline.stage_ed23_anforderungen import build_ed23_corpus  # noqa: E402

MAPPING_PATH = os.path.join(REPO_ROOT, "hilfsdateien", "gpp_ed23_anforderungen.json")
STRIPPED_PATH = os.path.join(REPO_ROOT, "hilfsdateien", "ed23_anforderungen_stripped.json")
ABDECKUNG_PATH = os.path.join(REPO_ROOT, "hilfsdateien", "ed23_satz_abdeckung.json")
TALLY_PATH = os.path.join(REPO_ROOT, "hilfsdateien", "ed23_mapping_qs", "tally.json")
DROPPED_OUT_PATH = os.path.join(REPO_ROOT, "hilfsdateien", "ed23_mapping_qs", "dropped_pairs.json")

TEILANF_PREFIX_RE = re.compile(r"^\(Teilanforderung (\d+)\)")


def load_drop_list():
    """Liest die drop-ids der QS-Reviewer aus tally.json -> {(control, anf_id, satz_nr), ...}."""
    with open(TALLY_PATH, "r", encoding="utf-8") as f:
        tally = json.load(f)
    drops = set()
    for control_id, ctrl in tally.get("ctrls", {}).items():
        raw = (ctrl.get("drop-ids") or "").strip()
        if not raw or raw == "-":
            continue
        for token in raw.split(","):
            token = token.strip()
            if not token:
                continue
            m = re.match(r"^([A-Z0-9.]+):S(\d+)$", token)
            if not m:
                raise SystemExit(f"FEHLER: drop-id '{token}' bei {control_id} nicht parsebar.")
            drops.add((control_id, m.group(1), int(m.group(2))))
    return drops


def phase_a_drops(per_control, abdeckung, drops):
    """Entfernt die Streichkandidaten aus Mapping und Satz-Abdeckung."""
    removed = []
    for control_id, anf_id, satz_nr in sorted(drops):
        matches = per_control.get(control_id, [])
        hits = [m for m in matches if m["id"] == anf_id and (m.get("satz_nr") or 0) == satz_nr]
        if len(hits) != 1:
            raise SystemExit(
                f"FEHLER: Drop {control_id} -> {anf_id}:S{satz_nr} trifft {len(hits)} "
                f"Eintraege (erwartet 1). QS-Liste gegen Mapping pruefen."
            )
        matches.remove(hits[0])
        removed.append({"control_id": control_id, **hits[0]})
        # Korrespondierenden Satz-Abdeckungs-Treffer mit entfernen (verhindert
        # Wiedereinfuehrung durch kuenftige Merges). Nicht jeder Drop hat einen:
        # gpp-seitig gefundene Paare stehen nicht in der Abdeckung.
        anf = abdeckung["anforderungen"].get(anf_id)
        if anf:
            before = len(anf.get("treffer", []))
            anf["treffer"] = [
                t for t in anf.get("treffer", [])
                if not (t.get("control_id") == control_id and t.get("satz_nr") == satz_nr)
            ]
            if len(anf["treffer"]) != before:
                removed[-1]["satz_abdeckung_treffer_entfernt"] = True
    return removed


def build_renumber_maps(old_saetze_by_id, new_saetze_by_id):
    """Je geaenderter Anforderung: {alt_idx: neu_idx}. Nur Merges (Fragment-Fix) erwartet."""
    renumber = {}
    for rid, old in old_saetze_by_id.items():
        new = new_saetze_by_id.get(rid)
        if new is None:
            raise SystemExit(f"FEHLER: Anforderung {rid} fehlt im neu erzeugten Korpus.")
        if old == new:
            continue
        if len(new) > len(old):
            raise SystemExit(f"FEHLER: {rid} hat MEHR Saetze als vorher — unerwarteter Split.")
        mapping = {}
        for i, old_satz in enumerate(old, start=1):
            found = None
            for j, new_satz in enumerate(new, start=1):
                if old_satz and old_satz in new_satz:
                    found = j
                    break
            if found is None:
                raise SystemExit(
                    f"FEHLER: {rid} alter Satz {i} nicht im neuen Korpus wiederfindbar: "
                    f"{old_satz[:80]!r}"
                )
            mapping[i] = found
        renumber[rid] = mapping
    return renumber


def phase_b_renumber(per_control, abdeckung, renumber):
    """Migriert Satznummern in Mapping (+remarks-Praefix) und Satz-Abdeckung; dedupliziert."""
    remapped, deduped = 0, []
    for control_id, matches in per_control.items():
        seen = {}
        for m in list(matches):
            rid = m["id"]
            if rid in renumber and m.get("satz_nr"):
                old_nr = m["satz_nr"]
                new_nr = renumber[rid].get(old_nr)
                if new_nr is None:
                    raise SystemExit(f"FEHLER: {control_id}->{rid}:S{old_nr} ohne Abbildung.")
                if new_nr != old_nr:
                    m["satz_nr"] = new_nr
                    remapped += 1
                b = m.get("begruendung") or ""
                if TEILANF_PREFIX_RE.match(b):
                    m["begruendung"] = TEILANF_PREFIX_RE.sub(f"(Teilanforderung {new_nr})", b, count=1)
            key = (m["id"], m.get("satz_nr") or 0)
            if key in seen:
                deduped.append({"control_id": control_id, **m})
                matches.remove(m)
            else:
                seen[key] = m
    return remapped, deduped


def phase_b_abdeckung(abdeckung, renumber, new_by_id, normative_re):
    """Satz-Abdeckung an die neue Nummerierung anpassen (n_saetze, normative, treffer)."""
    for rid, mapping in renumber.items():
        anf = abdeckung["anforderungen"].get(rid)
        if not anf:
            continue
        new_saetze = new_by_id[rid]
        anf["n_saetze"] = len(new_saetze)
        anf["normative_saetze"] = [
            i for i, s in enumerate(new_saetze, 1) if normative_re.search(s)
        ]
        seen = set()
        treffer_neu = []
        for t in anf.get("treffer", []):
            t = dict(t)
            t["satz_nr"] = mapping.get(t["satz_nr"], t["satz_nr"])
            key = (t.get("control_id"), t["satz_nr"])
            if key in seen:
                continue
            seen.add(key)
            treffer_neu.append(t)
        anf["treffer"] = treffer_neu


def validate(per_control, new_by_id):
    """Harte Endpruefungen; Rueckgabe der Paarzahl."""
    n_pairs = 0
    for control_id, matches in per_control.items():
        for m in matches:
            n_pairs += 1
            nr = m.get("satz_nr")
            if nr is not None:
                saetze = new_by_id.get(m["id"])
                if saetze is None:
                    raise SystemExit(f"FEHLER: {m['id']} nicht im neuen Korpus.")
                if not (1 <= nr <= len(saetze)):
                    raise SystemExit(
                        f"FEHLER: {control_id}->{m['id']}:S{nr} ausserhalb 1..{len(saetze)}."
                    )
                b = m.get("begruendung") or ""
                pm = TEILANF_PREFIX_RE.match(b)
                if pm and int(pm.group(1)) != nr:
                    raise SystemExit(
                        f"FEHLER: Praefix/satz_nr-Divergenz bei {control_id}->{m['id']}: "
                        f"Praefix {pm.group(1)}, Prop {nr}."
                    )
    for rid, saetze in new_by_id.items():
        for i, s in enumerate(saetze, 1):
            if s.count("(") != s.count(")"):
                raise SystemExit(f"FEHLER: {rid} S{i} weiterhin unbalancierte Klammern.")
    return n_pairs


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Nur berichten, nichts schreiben.")
    args = parser.parse_args(argv)

    with open(MAPPING_PATH, "r", encoding="utf-8") as f:
        mapping_doc = json.load(f)
    per_control = load_mapping_matches(mapping_doc)
    n_before = sum(len(v) for v in per_control.values())

    with open(ABDECKUNG_PATH, "r", encoding="utf-8") as f:
        abdeckung_doc = json.load(f)
    abdeckung = abdeckung_doc["ed23_satz_abdeckung"]

    with open(STRIPPED_PATH, "r", encoding="utf-8") as f:
        old_stripped = json.load(f)["ed23_anforderungen"]
    old_by_id = {a["id"]: a.get("saetze", []) for a in old_stripped}

    # Phase A
    drops = load_drop_list()
    print(f"Streichliste aus tally.json: {len(drops)} Paare.")
    removed = phase_a_drops(per_control, abdeckung, drops)

    # Phase B: amtlichen Korpus mit gefixtem Splitter neu erzeugen
    xml_bytes, _sha = fetch_official_xml(offline=True)
    official, _rejected = load_official_xml(xml_bytes)
    new_stripped, _lookup = build_ed23_corpus(official)
    new_by_id = {a["id"]: a.get("saetze", []) for a in new_stripped}
    renumber = build_renumber_maps(old_by_id, new_by_id)
    print(f"Anforderungen mit geaenderter Satzliste: {sorted(renumber)}")
    for rid, m in renumber.items():
        merged = [f"{a}->{b}" for a, b in m.items() if a != b or list(m.values()).count(b) > 1]
        print(f"  {rid}: {len(old_by_id[rid])} -> {len(new_by_id[rid])} Saetze; Abbildung {m}")

    from utils.ed23_xml import NORMATIVE_RE
    remapped, deduped = phase_b_renumber(per_control, abdeckung, renumber)
    phase_b_abdeckung(abdeckung, renumber, new_by_id, NORMATIVE_RE)

    n_after = validate(per_control, new_by_id)
    expected = n_before - len(removed) - len(deduped)
    if n_after != expected:
        raise SystemExit(f"FEHLER: Paarzahl {n_after} != erwartet {expected}.")
    print(
        f"OK: {n_before} -> {n_after} Paare "
        f"({len(removed)} Drops, {len(deduped)} Fragment-Dedupes, {remapped} umnummeriert)."
    )

    if args.dry_run:
        print("Dry-Run: keine Dateien geschrieben.")
        return

    out_mapping = to_oscal_mapping_collection(per_control)
    with open(MAPPING_PATH, "w", encoding="utf-8") as f:
        json.dump(out_mapping, f, ensure_ascii=False, indent=2)
    with open(STRIPPED_PATH, "w", encoding="utf-8") as f:
        json.dump({"ed23_anforderungen": new_stripped}, f, ensure_ascii=False, indent=2)
    abdeckung["meta"]["generated"] = out_mapping["mapping-collection"]["metadata"]["version"]
    with open(ABDECKUNG_PATH, "w", encoding="utf-8") as f:
        json.dump(abdeckung_doc, f, ensure_ascii=False, indent=2)
    audit = {
        "beschreibung": (
            "Issue #37 Phase A/B: von der QS-Stichprobe (hilfsdateien/ed23_mapping_qs/) "
            "beanstandete Paare, entfernt aus gpp_ed23_anforderungen.json, plus beim "
            "Tokenizer-Fix kollabierte Fragment-Duplikate. Vollstaendige Eintraege zur "
            "Wiederherstellung."
        ),
        "dropped": removed,
        "fragment_dedupes": deduped,
    }
    with open(DROPPED_OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(audit, f, ensure_ascii=False, indent=2)
    print(
        f"Geschrieben: {os.path.relpath(MAPPING_PATH, REPO_ROOT)}, "
        f"{os.path.relpath(STRIPPED_PATH, REPO_ROOT)}, "
        f"{os.path.relpath(ABDECKUNG_PATH, REPO_ROOT)}, "
        f"{os.path.relpath(DROPPED_OUT_PATH, REPO_ROOT)}."
    )


if __name__ == "__main__":
    main()
