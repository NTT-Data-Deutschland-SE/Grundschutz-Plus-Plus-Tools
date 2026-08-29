"""Tests for scripts/analyze_ed23_coverage.py (stdlib + pytest only, no network).

The script lives outside the src package, so it is imported via importlib from its file
path; tests/__init__.py already puts Gpp-ai-tool/src on sys.path for utils.sentence_split.

Run just this module (the sibling pipeline tests need google-genai):
    uv run --with pytest pytest Gpp-ai-tool/tests/test_analyze_ed23_coverage.py -q
"""

import argparse
import importlib.util
import json
import os

SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "scripts", "analyze_ed23_coverage.py"
)
_spec = importlib.util.spec_from_file_location("analyze_ed23_coverage", SCRIPT_PATH)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def test_split_sentences_semantics():
    from utils.sentence_split import split_sentences
    assert split_sentences("") == []
    assert split_sentences(None) == []
    text = "Es MUSS geprüft werden, z. B. jährlich. Zudem SOLLTE dokumentiert werden."
    assert split_sentences(text) == [
        "Es MUSS geprüft werden, z. B. jährlich.",
        "Zudem SOLLTE dokumentiert werden.",
    ]
    # Whitespace collapse and abbreviation restoration
    assert split_sentences("Eins  bzw.\n zwei. Drei!") == ["Eins bzw. zwei.", "Drei!"]


def test_title_regex_variants():
    cases = {
        "ISMS.1.A1 Übernahme der Gesamtverantwortung (B) [Institutionsleitung]":
            ("ISMS.1.A1", "Übernahme der Gesamtverantwortung", "B", "Institutionsleitung"),
        "APP.4.4.A21 Regelmäßiger Restart von Pods (H)":
            ("APP.4.4.A21", "Regelmäßiger Restart von Pods", "H", None),
        "INF.14.A1 Planung der Gebäudeautomation (B)":
            ("INF.14.A1", "Planung der Gebäudeautomation", "B", None),
        "SYS.1.2.2.A27 Titel mit Nummer A27 (S)":
            ("SYS.1.2.2.A27", "Titel mit Nummer A27", "S", None),
        # Defensive: reversed order role-before-level still recovers both
        "NET.1.1.A9 Dokumentation [IT-Betrieb] (B)":
            ("NET.1.1.A9", "Dokumentation", "B", "IT-Betrieb"),
        "OPS.1.1.2.A2 ENTFALLEN (B)": ("OPS.1.1.2.A2", "ENTFALLEN", "B", None),
    }
    for title, expected in cases.items():
        assert mod.parse_requirement_title(title) == expected, title
    assert mod.parse_requirement_title("Gefährdungslage") is None
    assert mod.parse_requirement_title("2.1 Fehlende Regelung") is None


DOCBOOK_FRAGMENT = """<?xml version="1.0" encoding="UTF-8"?>
<book xmlns="http://docbook.org/ns/docbook">
  <chapter><title>TST.1 Testbaustein</title>
    <section><title>2. Gefährdungslage</title>
      <section><title>TST.9.A9 Sieht aus wie eine Anforderung (B)</title>
        <para>Darf nicht mitzählen, falscher Ahnen-Kontext.</para>
      </section>
    </section>
    <section><title>3. Anforderungen</title>
      <section><title>3.1. Basis-Anforderungen</title>
        <section><title>TST.1.A1 Erste Pflicht (B) [Rolle X]</title>
          <para>Die Institution MUSS planen. Sie MUSS z.&#160;B. dokumentieren.</para>
          <para>Hintergrundsatz ohne Modalverb.</para>
        </section>
        <section><title>TST.1.A2 ENTFALLEN (B)</title>
          <para>Diese Anforderung ist entfallen.</para>
        </section>
      </section>
      <section><title>3.2. Standard-Anforderungen</title>
        <section><title>TST.1.A3 Zweite Pflicht (S)</title>
          <para>Es SOLLTEN <emphasis>alle</emphasis> Systeme erfasst werden. Dazu gehören:</para>
          <itemizedlist>
            <listitem><para>Server.</para></listitem>
            <listitem><para>Clients.</para></listitem>
          </itemizedlist>
        </section>
      </section>
    </section>
  </chapter>
</book>
"""


def test_docbook_fragment_parse():
    reqs, rejected = mod.load_official_xml(DOCBOOK_FRAGMENT.encode("utf-8"))
    assert set(reqs) == {"TST.1.A1", "TST.1.A2", "TST.1.A3"}
    # The requirement-looking section under Gefährdungslage is rejected, not silently dropped
    assert any("TST.9.A9" in t for t in rejected)

    a1 = reqs["TST.1.A1"]
    assert (a1["level"], a1["sublevel"], a1["rolle"]) == ("B", "B", "Rolle X")
    assert a1["entfallen"] is False
    # &#160; is normalized so the abbreviation mask holds: 3 sentences, 2 normative
    assert len(a1["saetze"]) == 3
    assert a1["normative_idx"] == [1, 2]

    a2 = reqs["TST.1.A2"]
    assert a2["entfallen"] is True

    a3 = reqs["TST.1.A3"]
    assert a3["has_lists"] is True
    assert a3["level"] == "S"
    assert 1 in a3["normative_idx"]


def test_normative_detection():
    reqs, _ = mod.load_official_xml(DOCBOOK_FRAGMENT.encode("utf-8"))
    # lowercase "muss"/"kann" never counts as normative
    assert not mod.NORMATIVE_RE.search("Das muss man wissen.")
    assert mod.NORMATIVE_RE.search("Der Zugriff DARF NICHT erfolgen.")
    assert mod.NORMATIVE_RE.search("Alle MÜSSEN teilnehmen.")
    assert not mod.NORMATIVE_RE.search("Die Institution KANN erweitern.")
    assert mod.KANN_RE.search("Die Institution KANN erweitern.")


def test_ua_definite_gaps():
    assert mod.ua_definite_gaps([2, 5]) == [1, 3, 4]
    assert mod.ua_definite_gaps([1]) == []
    assert mod.ua_definite_gaps([]) == []
    assert mod.ua_definite_gaps([1, 2, 3]) == []


def test_alignment_and_projection_buckets():
    identical = ["Die Leitung übernimmt die Gesamtverantwortung.",
                 "Ressourcen werden bereitgestellt."]
    assignment = mod.align_sentences(identical, identical)
    assert assignment[1][0] == 1 and assignment[1][1] >= 0.9
    # Modal-verb paraphrase still crosses the threshold after stopword stripping
    stripped = ["Die Institutionsleitung übernimmt die Gesamtverantwortung für Informationssicherheit."]
    xml = ["Die Leitung der Institution MUSS die Gesamtverantwortung für Informationssicherheit übernehmen."]
    a = mod.align_sentences(stripped, xml)
    assert a[1][1] >= mod.ALIGN_THRESHOLD

    req = {"normative_idx": [1, 2], "saetze": identical}
    ours_slot = {"saetze": {1}, "gpp": {"GC.1.1"}}
    proj = mod.xml_projection(req, {"saetze": identical}, ours_slot)
    assert proj["quality"] == "aligned"
    assert proj["covered_normative"] == [1]
    # Unrelated prose falls back to "grob" and propagates requirement-level coverage
    proj_grob = mod.xml_projection(
        req, {"saetze": ["Völlig anderes Thema ohne jede Übereinstimmung im Wortlaut."]},
        {"saetze": {1}, "gpp": {"GC.1.1"}},
    )
    assert proj_grob["quality"] == "grob"
    assert proj_grob["covered_normative"] == [1, 2]
    # No coverage at all -> no projection
    assert mod.xml_projection(req, {"saetze": identical}, None) is None


def test_classify_target():
    official = {"app.1.1.a1": {"entfallen": False}, "app.1.1.a2": {"entfallen": True}}
    stripped = {"app.1.1.a1": {}, "app.1.1.a2": {}, "sys.9.9.a1": {}}
    assert mod.classify_target("APP.1.1.A1", official, stripped) == "official"
    assert mod.classify_target("APP.1.1.A2", official, stripped) == "official-entfallen"
    assert mod.classify_target("SYS.9.9.A1", official, stripped) == "ntt-custom"
    assert mod.classify_target("XXX.1.A1", official, stripped) == "dangling"


def _toy_inputs():
    def req(rid, level, saetze, entfallen=False):
        return {
            "id": rid, "baustein": rid.rsplit(".A", 1)[0], "schicht": rid.split(".", 1)[0],
            "titel": f"Titel {rid}", "level": level, "sublevel": level, "rolle": None,
            "entfallen": entfallen, "saetze": saetze,
            "normative_idx": [i for i, s in enumerate(saetze, 1) if "MUSS" in s],
            "kann_idx": [], "has_lists": False, "nested_sections": 0,
        }

    official = {
        "AAA.1.A1": req("AAA.1.A1", "B", ["Es MUSS geplant werden.", "Kontext."]),
        "AAA.1.A2": req("AAA.1.A2", "S", ["Es MUSS geprüft werden."]),
        "AAA.1.A3": req("AAA.1.A3", "H", ["Es MUSS getestet werden."]),
        "AAA.1.A4": req("AAA.1.A4", "B", ["Es MUSS dokumentiert werden."]),
        "AAA.1.A5": req("AAA.1.A5", "B", ["Diese Anforderung ist entfallen."], entfallen=True),
    }
    ours = [
        {"source": "GC.1.1", "target": "AAA.1.A1", "satz": 1, "label": None},
        {"source": "GC.1.2", "target": "AAA.1.A2", "satz": 1, "label": None},
    ]
    ours_old = ours + [{"source": "GC.1.3", "target": "AAA.1.A3", "satz": None, "label": None}]
    itgs = [
        {"ua_id": "AAA.1.A2-UA.1", "req": "AAA.1.A2", "ua_idx": 1, "target": "GC.1.2",
         "relationship": "subset-of", "gefaehrdungen": []},
        {"ua_id": "AAA.1.A3-UA.3", "req": "AAA.1.A3", "ua_idx": 3, "target": "GC.9.9",
         "relationship": "equal-to", "gefaehrdungen": []},
    ]
    stripped = {
        rid: {"name": r["titel"], "saetze": list(r["saetze"]), "entfallen": r["entfallen"]}
        for rid, r in official.items()
    }
    gpp_controls = {"GC.1.1": "t", "GC.1.2": "t", "GC.1.3": "t"}
    args = argparse.Namespace(date="2026-01-01")
    return args, official, ours, ours_old, itgs, stripped, gpp_controls


def test_crosstab_and_vergleich_math():
    args, official, ours, ours_old, itgs, stripped, gpp = _toy_inputs()
    result = mod.build_result(
        args, official, [], ours, ours_old, itgs, {}, stripped, gpp, {}
    )["ed23_gap_analyse"]
    a = result["summary"]["anforderungen"]
    assert a["denominator_aktiv"] == 4 and a["entfallen"] == 1
    ct = a["crosstab_ours_itgs"]
    # A1 only_ours, A2 both, A3 only_itgs, A4 neither
    assert (ct["both"], ct["only_ours"], ct["only_itgs"], ct["neither"]) == (1, 1, 1, 1)
    assert sum(ct.values()) == a["denominator_aktiv"]
    assert a["ohne_jede_zuordnung_ids"] == ["AAA.1.A4"]
    v = result["summary"]["vergleich_5521_vs_3046"]
    assert v["verloren"] == ["AAA.1.A3"] and v["gewonnen"] == []
    # ITGS UA lower bound: A3 mapped only UA.3 -> gaps [1, 2]
    rec_a3 = next(r for r in result["anforderungen"] if r["id"] == "AAA.1.A3")
    assert rec_a3["itgs"]["ua_lower_bound"] == 3
    assert rec_a3["itgs"]["definite_ua_gaps"] == [1, 2]
    # forward: GC.1.3 has no ED23 hit in the current mapping
    assert result["forward_gaps"]["ours"] == ["GC.1.3"]


def test_zerlegungsvergleich():
    args, official, ours, ours_old, itgs, stripped, gpp = _toy_inputs()
    # A2 is in both mappings: ours satz {1}, itgs UA {1} -> identisch.
    result = mod.build_result(
        args, official, [], ours, ours_old, itgs, {}, stripped, gpp, {}
    )["ed23_gap_analyse"]
    zv = result["summary"]["teilanforderungen"]["zerlegungsvergleich"]
    assert zv["anforderungen_in_beiden_mappings_mit_indizes"] == 1
    assert zv["indizes_identisch"] == 1
    assert zv["indizes_disjunkt"] == 0
    # A3: UA lower bound 3 > 1 normative XML sentence -> flagged as finer decomposition
    assert zv["ua_untergrenze_uebersteigt_normative_xml_saetze"] == ["AAA.1.A3"]
    # stripped copies the XML sentences in the toy inputs -> all mapped reqs match
    assert zv["stripped_satzzahl_gleich_xml"] == zv["stripped_satzzahl_basis"] == 2


def test_satz_urteil_integration():
    args, official, ours, ours_old, itgs, stripped, gpp = _toy_inputs()
    satz_urteil = {"meta": {}, "per_req": {
        "aaa.1.a1": {"n_saetze": 2, "normative": [1], "by_satz": {1: ["GC.1.1"]}},
        "aaa.1.a4": {"n_saetze": 1, "normative": [1], "by_satz": {}},
    }}
    result = mod.build_result(
        args, official, [], ours, ours_old, itgs, {}, stripped, gpp, {},
        satz_urteil=satz_urteil,
    )["ed23_gap_analyse"]
    bt = result["summary"]["teilanforderungen"]["beurteilt"]
    assert bt["anforderungen_beurteilt"] == 2
    assert bt["denominator_normative_saetze"] == 2
    assert bt["abgedeckt"] == 1 and bt["nicht_abgedeckt"] == 1
    assert bt["anforderungen_ohne_einzigen_abgedeckten_satz"] == ["AAA.1.A4"]
    # A4 is unmapped AND sentence-empty, so it must not appear as newly-found substance
    assert bt["ungemappt_aber_satz_gefunden"] == []
    # A1 is mapped and keeps a covered sentence -> not a contradiction
    assert bt["gemappt_aber_satzlos"] == []
    rec = next(r for r in result["anforderungen"] if r["id"] == "AAA.1.A1")
    assert rec["satz_urteil"]["abgedeckte_normative_saetze"] == [1]
    assert rec["satz_urteil"]["nummerierung_ok"] is True
    # Without the judgment input, the block stays absent
    result2 = mod.build_result(
        args, official, [], ours, ours_old, itgs, {}, stripped, gpp, {}
    )["ed23_gap_analyse"]
    assert result2["summary"]["teilanforderungen"]["beurteilt"] is None


def test_json_determinism():
    args, official, ours, ours_old, itgs, stripped, gpp = _toy_inputs()
    r1 = mod.build_result(args, official, [], ours, ours_old, itgs, {}, stripped, gpp, {})
    r2 = mod.build_result(args, official, [], ours, ours_old, itgs, {}, stripped, gpp, {})
    assert json.dumps(r1, ensure_ascii=False, sort_keys=True) == json.dumps(
        r2, ensure_ascii=False, sort_keys=True
    )
