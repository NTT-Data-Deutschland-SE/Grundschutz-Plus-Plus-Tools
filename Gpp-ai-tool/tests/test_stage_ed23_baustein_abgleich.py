"""Tests of the Baustein abgleich stage: deterministic sources, gate, maker post-checks, checker verdicts, resume."""

import json
import os
import tempfile
from unittest.mock import patch

from pipeline import stage_ed23_baustein_abgleich as st

LOOKUP = {"konf.1.1": "KONF.1.1", "gc.1.1": "GC.1.1", "det.3.4": "DET.3.4", "perf.5.1": "PERF.5.1"}
REC = {"id": "SYS.1.1.A5", "baustein": "SYS.1.1", "titel": "T", "level": "B", "level_num": "1", "rolle": None,
       "herkunft": "BSI", "entfallen": False, "saetze": ["Es MUSS a.", "Es KANN b."], "normative_idx": [1],
       "kann_idx": [2], "text_quelle": "xml", "modalverb": "MUSS", "kann_only": False}


def test_assign_deterministic_merges_sources_and_drops_unknown_ids():
    inv = {"SYS.1.1.A5": [{"control_id": "KONF.1.1", "relation": "superset-of", "satz_nr": [1], "begruendung": "b"}]}
    satz = {"SYS.1.1.A5": [{"control_id": "KONF.1.1", "satz_nr": [1, 2], "begruendung": "s"},
                           {"control_id": "OLD.9.9", "satz_nr": [1], "begruendung": ""}]}
    gs = {"SYS.1.1.A5": [{"control_id": "gc.1.1", "relation": "subset-of", "ua_idx": [1]}]}
    out = st.assign_deterministic("SYS.1.1.A5", inv, satz, {"SYS.1.1.A5": "DET.3.4"}, gs, LOOKUP)
    by = {z["control_id"]: z for z in out}
    assert set(by) == {"KONF.1.1", "GC.1.1", "DET.3.4"}
    assert by["KONF.1.1"]["quelle"] == "gpp_ed23_anforderungen" and by["KONF.1.1"]["quellen"] == ["gpp_ed23_anforderungen", "satz_abdeckung"]
    assert by["KONF.1.1"]["satz_nr"] == [1, 2] and by["KONF.1.1"]["relation"] == "superset-of"
    assert by["GC.1.1"]["quelle"] == "gsmap" and by["DET.3.4"]["quelle"] == "prozessbausteine_mapping"


def test_gate_ignores_the_forced_process_mapping_alone():
    only_prozess = [{"control_id": "DET.3.4", "quelle": "prozessbausteine_mapping", "quellen": ["prozessbausteine_mapping"]}]
    assert st.needs_model(REC, only_prozess)
    assert not st.needs_model(REC, only_prozess + [{"control_id": "GC.1.1", "quelle": "gsmap", "quellen": ["gsmap"]}])
    assert not st.needs_model(dict(REC, entfallen=True), [])
    assert st.needs_model(REC, [])


def _item(**over):
    base = {"anforderung_id": "SYS.1.1.A5",
            "pruefung": {"art": "umsetzungsanforderung", "modalverb": "MUSS", "control_noetig": True, "hinweis": ""},
            "zuordnungen": [], "neues_control": {"titel": "Neu", "statement": "Die Institution MUSS x.", "guidance": "g",
                                                "praktik": "KONF", "zielobjektkategorien": ["IT-Systeme", "Quatsch"],
                                                "verwandte_controls": ["konf.1.1", "XX.1"]}}
    base.update(over)
    return base


def test_filter_accepts_a_clean_new_control_and_inverts_relations():
    res = st.filter_maker_result(_item(zuordnungen=[{"control_id": "gc.1.1", "relation": "subset-of", "konfidenz": "hoch", "begruendung": "b"},
                                                     {"control_id": "nope", "relation": "subset-of", "konfidenz": "hoch", "begruendung": "b"}],
                                       neues_control=None), REC, LOOKUP, {"KONF", "GC"}, {"IT-Systeme"})
    assert [z["control_id"] for z in res["zuordnungen"]] == ["GC.1.1"]
    assert res["zuordnungen"][0]["relation"] == "superset-of" and res["zuordnungen"][0]["quelle"] == "ki"
    assert any("nicht im Anwenderkatalog" in v for v in res["verworfen"]) and res["ohne_control"] is None

    res = st.filter_maker_result(_item(), REC, LOOKUP, {"KONF", "GC"}, {"IT-Systeme"})
    nc = res["neues_control"]
    assert nc["id"] == "NG-SYS.1.1.A5" and nc["modalverb"] == "MUSS" and nc["zielobjektkategorien"] == ["IT-Systeme"]
    assert nc["verwandte_controls"] == ["KONF.1.1"] and any("Vokabular" in v for v in res["verworfen"])


def test_filter_rejects_new_controls_by_each_rule():
    def rejected(**over):
        res = st.filter_maker_result(_item(**over), over.pop("_rec", REC), LOOKUP, {"KONF", "GC"}, {"IT-Systeme"})
        return res["neues_control"] is None and res["ohne_control"] is not None
    assert rejected(zuordnungen=[{"control_id": "gc.1.1", "relation": "equivalent-to", "konfidenz": "hoch", "begruendung": ""}]) is False  # has a zuordnung → no ohne_control
    # With a Zuordnung the new control is kept as the checker's fallback, not dropped.
    res = st.filter_maker_result(_item(zuordnungen=[{"control_id": "gc.1.1", "relation": "equivalent-to", "konfidenz": "hoch", "begruendung": ""}]),
                                 REC, LOOKUP, {"KONF"}, set())
    assert res["neues_control"]["fallback"] is True and not any("Zuordnung vorhanden" in v for v in res["verworfen"])
    assert rejected(pruefung={"art": "hinweis", "modalverb": "keines", "control_noetig": False, "hinweis": "h"})
    assert rejected(neues_control=dict(_item()["neues_control"], statement="Es MUSS a und SOLLTE b."))
    assert rejected(neues_control=dict(_item()["neues_control"], statement="Die Institution SOLLTE x."))  # weaker than MUSS
    assert rejected(neues_control=dict(_item()["neues_control"], praktik="XYZ"))
    res = st.filter_maker_result(_item(), dict(REC, kann_only=True, modalverb="KANN"), LOOKUP, {"KONF"}, set())
    assert res["neues_control"] is None and "KANN" in res["verworfen"][0]


def test_checker_verdicts_remove_rejected_and_keep_doubtful():
    res = st.filter_maker_result(_item(zuordnungen=[
        {"control_id": "gc.1.1", "relation": "equivalent-to", "konfidenz": "hoch", "begruendung": ""},
        {"control_id": "konf.1.1", "relation": "intersects-with", "konfidenz": "niedrig", "begruendung": ""}]),
        REC, LOOKUP, {"KONF", "GC"}, set())
    res = st.apply_checker_verdict(res, {"urteile": [{"control_id": "GC.1.1", "urteil": "abgelehnt", "begruendung": "nein"},
                                                     {"control_id": "KONF.1.1", "urteil": "fraglich", "begruendung": "hm"}],
                                         "gesamt": "ok"})
    assert [z["control_id"] for z in res["zuordnungen"]] == ["KONF.1.1"] and res["zuordnungen"][0]["checker"] == "fraglich"
    assert any("abgelehnt" in v for v in res["verworfen"])
    res2 = st.apply_checker_verdict(st.filter_maker_result(_item(), REC, LOOKUP, {"KONF"}, set()),
                                    {"urteile": [], "neues_control": {"urteil": "abgelehnt", "begruendung": "gibt es"}, "gesamt": "g"})
    assert res2["neues_control"] is None and res2["ohne_control"]["art"] == "abgelehnt-durch-checker"
    res3 = st.apply_checker_verdict(st.filter_maker_result(_item(), REC, LOOKUP, {"KONF"}, set()), None)
    assert res3["neues_control"]["checker"] == "nicht geprüft"


def _with_fallback():
    return st.filter_maker_result(_item(zuordnungen=[
        {"control_id": "gc.1.1", "relation": "equivalent-to", "konfidenz": "hoch", "begruendung": ""}]), REC, LOOKUP, {"KONF"}, set())


def test_fallback_control_is_dropped_when_a_zuordnung_survives():
    res = st.apply_checker_verdict(_with_fallback(), {"urteile": [{"control_id": "GC.1.1", "urteil": "fraglich", "begruendung": "hm"}],
                                                      "neues_control": {"urteil": "bestaetigt", "begruendung": "ok"}, "gesamt": ""})
    assert res["neues_control"] is None and [z["control_id"] for z in res["zuordnungen"]] == ["GC.1.1"]
    assert any("Zuordnung vom Checker bestätigt" in v for v in res["verworfen"]) and res["ohne_control"] is None


def test_fallback_control_stands_when_all_zuordnungen_are_rejected():
    res = st.apply_checker_verdict(_with_fallback(), {"urteile": [{"control_id": "GC.1.1", "urteil": "abgelehnt", "begruendung": "nein"}],
                                                      "neues_control": {"urteil": "bestaetigt", "begruendung": "ok"}, "gesamt": ""})
    assert res["zuordnungen"] == [] and res["neues_control"]["id"] == "NG-SYS.1.1.A5"
    assert res["neues_control"]["checker"] == "bestaetigt" and "fallback" not in res["neues_control"] and res["ohne_control"] is None
    # ... but not when the checker rejects it too
    res = st.apply_checker_verdict(_with_fallback(), {"urteile": [{"control_id": "GC.1.1", "urteil": "abgelehnt", "begruendung": "nein"}],
                                                      "neues_control": {"urteil": "abgelehnt", "begruendung": "nein"}, "gesamt": "g"})
    assert res["neues_control"] is None and res["ohne_control"]["art"] == "abgelehnt-durch-checker"


def test_fallback_control_is_dropped_without_checker():
    res = st.apply_checker_verdict(_with_fallback(), None)
    assert res["neues_control"] is None and res["zuordnungen"][0]["checker"] == "nicht geprüft"
    assert any("Checker nicht erreichbar" in v for v in res["verworfen"])


def test_render_block_marks_normative_sentences():
    block = st.render_anforderung_block(REC)
    assert block.startswith("### SYS.1.1.A5 T (B) – Modalverb MUSS") and "(S1) [normativ] Es MUSS a." in block and "(S2) Es KANN b." in block


class FakeClient:
    """Maker answers with a new control for every Anforderung; checker confirms."""

    def __init__(self, *_):
        self.calls = []

    async def generate_validated_json_response(self, prompt, json_schema, request_context_log, **kw):
        self.calls.append(request_context_log)
        if request_context_log.startswith("ED23BausteinCheck"):
            return {"urteile": [], "neues_control": {"urteil": "bestaetigt", "begruendung": "ok"}, "gesamt": ""}
        ids = [l.split()[1] for l in prompt.splitlines() if l.startswith("### ")]
        return {"ergebnisse": [{"anforderung_id": aid,
                                "pruefung": {"art": "umsetzungsanforderung", "modalverb": "MUSS", "control_noetig": True, "hinweis": ""},
                                "zuordnungen": [],
                                "neues_control": {"titel": f"Neu {aid}", "statement": "Die Institution MUSS x.", "guidance": "g",
                                                  "praktik": "KONF", "zielobjektkategorien": ["IT-Systeme"], "verwandte_controls": []}}
                               for aid in ids]}

    def log_usage_summary(self, label=""):
        pass


def _control(cid, title, statement):
    return {"id": cid, "title": title, "props": [{"name": "level", "value": "1"}],
            "parts": [{"id": f"{cid}-m3", "class": "maturity-level-defined", "parts": [{"name": "statement", "prose": statement}]}]}


BD = {"catalog": {"groups": [{"id": "SYS", "title": "SYS", "groups": [
    {"id": "SYS.1.1", "class": "baustein", "title": "Server", "parts": [{"name": "Zielsetzung", "prose": "z"}],
     "controls": [_control("SYS.1.1.A1", "Gedeckt (B)", "Es MUSS a."), _control("SYS.1.1.A2", "Lücke (B)", "Es MUSS b."),
                  _control("SYS.1.1.A3", "ENTFALLEN", "Diese Anforderung ist entfallen.")]}]}]}}
PLAIN = BD
OFFICIAL = {"SYS.1.1.A1": {"titel": "Gedeckt", "level": "B", "rolle": None, "entfallen": False, "saetze": ["Es MUSS a."], "normative_idx": [1], "kann_idx": []},
            "SYS.1.1.A2": {"titel": "Lücke", "level": "B", "rolle": None, "entfallen": False, "saetze": ["Es MUSS b."], "normative_idx": [1], "kann_idx": []},
            "SYS.1.1.A3": {"titel": "ENTFALLEN", "level": "B", "rolle": None, "entfallen": True, "saetze": [], "normative_idx": [], "kann_idx": []}}
GPP = {"catalog": {"groups": [{"id": "KONF", "title": "Konfiguration", "groups": [{"id": "KONF.1", "title": "Grund", "controls": [
    {"id": "KONF.1.1", "title": "K", "parts": [{"id": "KONF.1.1_stm", "name": "statement", "prose": "Konfiguration MUSS k."}]}]}]}]}}
MAPPING = {"mapping-collection": {"mappings": [{"maps": [{"relationship": "equal-to", "sources": [{"id-ref": "KONF.1.1"}],
                                                          "targets": [{"id-ref": "SYS.1.1.A1", "props": [{"name": "statement-sentence", "value": "1"}]}]}]}]}}


async def test_run_publishes_output_and_resumes_without_calls():
    with tempfile.TemporaryDirectory() as tmp:
        out = os.path.join(tmp, "ed23_baustein_abgleich.json")
        fake = FakeClient()
        loads = {st.GPP_KOMPENDIUM_JSON_PATH: GPP, st.PROMPT_CONFIG_PATH: {
            "ed23_baustein_abgleich_system": "s", "ed23_baustein_abgleich_maker_prompt": "{praktiken}{zielobjektkategorien}{baustein_id}{baustein_titel}{herkunft_satz}{zielsetzung}{zielobjektkategorie}{n}\n{anforderungen}",
            "ed23_baustein_abgleich_checker_prompt": "{baustein_id}{baustein_titel}{herkunft_satz}{anforderung}{vorschlag}{controls}"},
            st.ED23_BAUSTEIN_ABGLEICH_MAKER_SCHEMA_PATH: {"type": "object"}, st.ED23_BAUSTEIN_ABGLEICH_CHECKER_SCHEMA_PATH: {"type": "object"}}
        reads = {st.BAUSTEIN_ZIELOBJEKT_JSON_PATH: {"baustein_zielobjekt_map": {"SYS.1.1": "u1"}},
                 st.GPP_ED23_ANFORDERUNGEN_JSON_PATH: MAPPING, st.ED23_SATZ_ABDECKUNG_JSON_PATH: {},
                 st.PROZZESSBAUSTEINE_CONTROLS_JSON_PATH: {}}
        patches = [
            patch.object(st, "load_json_file", lambda path, expected_sha256=None: loads.get(path, {})),
            patch.object(st, "read_json_file", lambda path, expected_sha256=None: reads.get(path, {})),
            patch.object(st, "load_zielobjekte_csv", lambda _p: [{"UUID": "u1", "Zielobjekt": "IT-Systeme"}]),
            patch.object(st, "load_ed23_catalogs", lambda: (BD, PLAIN)),
            patch.object(st, "fetch_official_xml", lambda: (b"", "sha")),
            patch.object(st, "load_official_xml", lambda _b: (OFFICIAL, [])),
            patch.object(st, "fetch_cached", lambda *a, **k: (_ for _ in ()).throw(RuntimeError("offline"))),
            patch.object(st, "AiClient", lambda cfg: fake),
            patch.object(st, "ED23_BAUSTEIN_ABGLEICH_JSON_PATH", out),
            patch.object(st, "CHECKPOINT_PATH", out + ".partial"),
            patch.object(st.app_config, "overwrite_temp_files", False),
            patch.object(st.app_config, "is_test_mode", False),
        ]
        for p in patches:
            p.start()
        try:
            await st.run_stage_ed23_baustein_abgleich()
            assert sorted(fake.calls) == ["ED23Baustein-SYS.1.1.A2..SYS.1.1.A2", "ED23BausteinCheck-SYS.1.1.A2"]
            with open(out, encoding="utf-8") as f:
                doc = json.load(f)["ed23_baustein_abgleich"]
            a1, a2, a3 = (doc["anforderungen"][k] for k in ("SYS.1.1.A1", "SYS.1.1.A2", "SYS.1.1.A3"))
            assert a1["zuordnungen"][0]["control_id"] == "KONF.1.1" and a1["ki"] is None and a1["neues_control"] is None
            assert a2["neues_control"]["id"] == "NG-SYS.1.1.A2" and a2["neues_control"]["checker"] == "bestaetigt"
            assert a3["entfallen"] and a3["ohne_control"] is None
            assert doc["meta"]["neue_controls"] == 1 and not os.path.exists(out + ".partial")
            fake.calls.clear()
            await st.run_stage_ed23_baustein_abgleich()
            assert fake.calls == []
            # Resume must keep the model results, not just the provenance block.
            with open(out, encoding="utf-8") as f:
                doc2 = json.load(f)["ed23_baustein_abgleich"]
            assert doc2["anforderungen"]["SYS.1.1.A2"]["neues_control"]["id"] == "NG-SYS.1.1.A2"
            assert doc2["anforderungen"]["SYS.1.1.A2"]["pruefung"]["modalverb"] == "MUSS"
            assert doc2["meta"]["neue_controls"] == 1
            assert doc2["anforderungen"] == doc["anforderungen"]
            # A stale checkpoint candidate for an already published Anforderung is not re-checked.
            with open(out + ".partial", "w", encoding="utf-8") as f:
                json.dump({st.CHECKPOINT_DONE: {}, st.CHECKPOINT_KANDIDATEN: {
                    "SYS.1.1.A2": {"pruefung": {}, "zuordnungen": [], "neues_control": {"id": "NG-SYS.1.1.A2"},
                                   "ohne_control": None, "offen": "", "verworfen": []}}}, f)
            fake.calls.clear()
            await st.run_stage_ed23_baustein_abgleich()
            assert fake.calls == [] and not os.path.exists(out + ".partial")
        finally:
            for p in patches:
                p.stop()
