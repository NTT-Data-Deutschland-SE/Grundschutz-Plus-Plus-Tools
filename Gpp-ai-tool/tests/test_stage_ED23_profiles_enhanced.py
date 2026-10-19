"""Tests of the ED23 profile builders, the maturity cache and one offline run."""

import hashlib
import json
import os
import tempfile
from unittest.mock import patch

from constants import ED23_BAUSTEIN_NS
from pipeline import stage_ED23_profiles_enhanced as st
from utils.oscal_utils import validate_ed23_profile_structure


def _rec(aid, level, text="Es MUSS a.", entfallen=False, herkunft="BSI", rolle=None):
    return {"id": aid, "baustein": aid.rsplit(".A", 1)[0], "titel": f"Titel {aid}", "level": level,
            "level_num": {"B": "1", "S": "3", "H": "5"}[level], "rolle": rolle, "herkunft": herkunft,
            "entfallen": entfallen, "text": text, "saetze": [text], "normative_idx": [1], "kann_idx": [],
            "text_quelle": "xml", "modalverb": "MUSS", "kann_only": False}


RECORDS = [_rec("SYS.1.1.A10", "S"), _rec("SYS.1.1.A1", "B"), _rec("SYS.1.1.A2", "B", entfallen=True),
           _rec("SYS.1.1.A3", "B"), _rec("SYS.1.1.A4", "H", rolle="ISB"), _rec("SYS.1.1.A5", "S")]
Z = lambda cid, quelle="gpp_ed23_anforderungen", **k: dict({"control_id": cid, "quelle": quelle, "quellen": [quelle],
                                                            "relation": "superset-of", "satz_nr": [1], "begruendung": "(Teilanforderung 1) weil",
                                                            "konfidenz": None, "checker": None}, **k)
ABGLEICH = {
    "SYS.1.1.A1": {"zuordnungen": [Z("KONF.1.1"), Z("GC.1.1", "satz_abdeckung")], "neues_control": None, "ohne_control": None, "pruefung": None},
    "SYS.1.1.A3": {"zuordnungen": [Z("KONF.1.1", "prozessbausteine_mapping")], "neues_control": None, "ohne_control": None,
                   "pruefung": {"art": "umsetzungsanforderung"}},
    "SYS.1.1.A4": {"zuordnungen": [], "neues_control": {"id": "NG-SYS.1.1.A4", "titel": "x"}, "ohne_control": None, "pruefung": None},
    "SYS.1.1.A5": {"zuordnungen": [], "neues_control": None, "ohne_control": {"art": "hinweis", "begruendung": "nur Hinweis"}, "pruefung": {"art": "hinweis"}},
    "SYS.1.1.A10": {"zuordnungen": [Z("DET.1.1", "ki", konfidenz="hoch", checker="bestaetigt")], "neues_control": None, "ohne_control": None, "pruefung": None},
}
CTX = {"baustein_id": "SYS.1.1", "baustein_title": "Allgemeiner Server", "zielobjekt_name": "IT-Systeme", "herkunft": "BSI",
       "ordered": st.order_anforderungen(RECORDS), "abgleich": ABGLEICH, "version": "2026-10-18",
       "ng_sha256": "ab" * 32, "ng_total": 7, "ng_title": "NG Ergänzungskatalog"}
MATURITY = {"KONF.1.1": {"position": "ending", "by-id": "KONF.1.1_stm", "parts": [
    {"id": "KONF.1.1-m3_custom", "name": "statement", "prose": "Konfiguration MUSS k.", "props": [{"name": "label", "value": "m3"}]}]}}


def test_ordering_and_placement():
    ordered = st.order_anforderungen(RECORDS)
    assert [r["id"] for r in ordered] == ["SYS.1.1.A1", "SYS.1.1.A2", "SYS.1.1.A3", "SYS.1.1.A5", "SYS.1.1.A10", "SYS.1.1.A4"]
    first, by_anf, prov = st.control_placement(ordered, ABGLEICH)
    assert first == {"KONF.1.1": "SYS.1.1.A1", "GC.1.1": "SYS.1.1.A1", "DET.1.1": "SYS.1.1.A10", "NG-SYS.1.1.A4": "SYS.1.1.A4"}
    assert by_anf["SYS.1.1.A3"] == ["KONF.1.1"] and [a for a, _ in prov["KONF.1.1"]] == ["SYS.1.1.A1", "SYS.1.1.A3"]


def test_herkunft_remark_grammar():
    assert st.herkunft_remark(Z("K")) == "Herkunft: gpp_ed23_anforderungen (superset-of, Teilanforderung 1): weil"
    assert st.herkunft_remark(Z("K", "satz_abdeckung", quellen=["satz_abdeckung", "gsmap"])) == \
        "Herkunft: satz_abdeckung (superset-of, Satz 1): weil [auch: gsmap]"
    assert st.herkunft_remark(Z("K", "prozessbausteine_mapping", begruendung="")) == "Herkunft: prozessbausteine_mapping (1:1-Zuordnung)"
    assert st.herkunft_remark(Z("K", "gsmap", begruendung="")) == "Herkunft: BSI-GSMap ITGS→GS++ (superset-of)"
    assert st.herkunft_remark(Z("K", "ki", konfidenz="hoch", checker="fraglich", begruendung="b")) == \
        "Herkunft: KI-Vorschlag (superset-of, Konfidenz hoch, Checker fraglich): b"


def test_profile_structure_plain_and_enhanced():
    plain = st.build_profile(CTX, "plain", MATURITY)
    enhanced = st.build_profile(CTX, "enhanced", MATURITY)
    for doc, name in ((plain, "it-systeme_SYS.1.1_allgemeiner_server.json"), (enhanced, "it-systeme_SYS.1.1_allgemeiner_server_enhanced.json")):
        assert validate_ed23_profile_structure(doc, {"NG-SYS.1.1.A4"}, name) == []
    p = enhanced["profile"]
    assert p["metadata"]["title"] == "SYS.1.1 – Allgemeiner Server (IT-Systeme) – Enhanced (ED2023)"
    assert p["imports"][0]["include-controls"][0]["with-ids"] == ["DET.1.1", "GC.1.1", "KONF.1.1"]
    assert p["imports"][1]["include-controls"][0]["with-ids"] == ["NG-SYS.1.1.A4"]
    assert p["merge"]["combine"] == {"method": "use-first"}
    levels = p["merge"]["custom"]["groups"]
    assert [g["id"] for g in levels] == ["SYS.1.1-B", "SYS.1.1-S", "SYS.1.1-H"]
    b_groups = {g["id"]: g for g in levels[0]["groups"]}
    assert b_groups["SYS.1.1.A1"]["insert-controls"][0]["include-controls"][0]["with-ids"] == ["KONF.1.1", "GC.1.1"]
    assert b_groups["SYS.1.1.A1"]["parts"][0] == {"id": "SYS.1.1.A1_anforderung", "name": "overview", "prose": "Es MUSS a."}
    assert b_groups["SYS.1.1.A2"]["title"] == "SYS.1.1.A2 ENTFALLEN" and "parts" not in b_groups["SYS.1.1.A2"]
    assert b_groups["SYS.1.1.A3"]["links"] == [{"href": "#KONF.1.1", "rel": "related", "text": "KONF.1.1 steht unter SYS.1.1.A1"}]
    s_groups = {g["id"]: g for g in levels[1]["groups"]}
    oc = [x for x in s_groups["SYS.1.1.A5"]["props"] if x["name"] == "ohne-control"][0]
    assert oc["value"] == "hinweis" and oc["remarks"] == "nur Hinweis"
    h = levels[2]["groups"][0]
    assert {x["name"]: x["value"] for x in h["props"]}["rolle"] == "ISB" and h["insert-controls"][0]["include-controls"][0]["with-ids"] == ["NG-SYS.1.1.A4"]
    alters = {a["control-id"]: a for a in p["modify"]["alters"]}
    konf = alters["KONF.1.1"]["adds"]
    assert konf[0]["by-id"] == "KONF.1.1_stm" and konf[1]["props"][0]["name"] == "ed23-anforderung"
    assert [x["value"] for x in konf[1]["props"]] == ["SYS.1.1.A1", "SYS.1.1.A3"]
    assert alters["DET.1.1"]["adds"][0]["props"][0]["remarks"].startswith("Herkunft: KI-Vorschlag")
    plain_alters = {a["control-id"]: a for a in plain["profile"]["modify"]["alters"]}
    assert "parts" not in plain_alters["KONF.1.1"]["adds"][0] and len(plain_alters["KONF.1.1"]["adds"]) == 1
    assert plain["profile"]["uuid"] != p["uuid"] and plain["profile"]["metadata"]["title"].endswith("(IT-Systeme)")
    assert len(p["back-matter"]["resources"]) == 3 and p["back-matter"]["resources"][2]["rlinks"][0]["href"] == "NG-ergaenzungskatalog.json"


def test_ng_baustein_profile_has_prefixes_and_no_ng_import_without_new_controls():
    ctx = dict(CTX, baustein_id="APP.4.10", baustein_title="KI", herkunft="NG",
               ordered=[_rec("APP.4.10.A1", "B", herkunft="NG")], abgleich={"APP.4.10.A1": ABGLEICH["SYS.1.1.A1"]})
    doc = st.build_profile(ctx, "plain")
    assert doc["profile"]["metadata"]["title"] == "NG APP.4.10 – KI (IT-Systeme)" and len(doc["profile"]["imports"]) == 1
    assert validate_ed23_profile_structure(doc, set(), "NG_it-systeme_APP.4.10_ki.json") == []
    assert {x["name"]: x["value"] for x in doc["profile"]["metadata"]["props"]}["herkunft"] == "NG"


def test_harvest_and_maturity_for(tmp_path):
    old = {"profile": {"metadata": {"title": "APP.3.6 - DNS-Server - Enhanced (ED2023)"}, "modify": {"alters": [
        {"control-id": "KONF.1.1", "adds": [{"position": "ending", "by-id": "KONF.1.1_stm", "parts": [
            {"id": "KONF.1.1-m3_custom", "name": "statement", "prose": "alt"}]}]}]}}}
    (tmp_path / "dns-server_APP.3.6_dns-server_enhanced.json").write_text(json.dumps(old), encoding="utf-8")
    cache = {"_meta": {}}
    assert st.harvest_existing_maturity(str(tmp_path), cache, {"APP.3.6"}) == 1
    assert "KONF.1.1" in cache["APP.3.6"]
    assert st.harvest_existing_maturity(str(tmp_path), cache, {"APP.3.6"}) == 0  # never overwrites
    assert st.maturity_for(cache, "APP.3.6", "KONF.1.1", "alt")["by-id"] == "KONF.1.1_stm"
    assert st.maturity_for(cache, "SYS.1.1", "KONF.1.1", "alt") is not None  # cross-Baustein reuse
    assert st.maturity_for(cache, "APP.3.6", "KONF.1.1", "neu") is None  # m3 prose changed → invalid


class FakeClient:
    def __init__(self, *_):
        self.calls = 0

    async def generate_validated_json_response(self, prompt, json_schema, request_context_log, **kw):
        self.calls += 1
        return [{"id": "GC.1.1", "class": "Management", "phase": "Operation", "level_1_statement": "wenig", "level_4_statement": "mehr"}]

    def log_usage_summary(self, label=""):
        pass


def _control(cid, title, statement):
    return {"id": cid, "title": title, "props": [{"name": "level", "value": "1"}],
            "parts": [{"id": f"{cid}-m3", "class": "maturity-level-defined", "parts": [{"name": "statement", "prose": statement}]}]}


async def test_run_writes_profiles_idempotently(tmp_path):
    bd = {"catalog": {"groups": [{"id": "SYS", "title": "SYS", "groups": [
        {"id": "SYS.1.1", "class": "baustein", "title": "Server", "parts": [{"name": "Zielsetzung", "prose": "z"}],
         "controls": [_control("SYS.1.1.A1", "A (B)", "Es MUSS a."), _control("SYS.1.1.A2", "B (B)", "Es MUSS b.")]}]}]}}
    official = {"SYS.1.1.A1": {"titel": "A", "level": "B", "rolle": None, "entfallen": False, "saetze": ["Es MUSS a."], "normative_idx": [1], "kann_idx": []},
                "SYS.1.1.A2": {"titel": "B", "level": "B", "rolle": None, "entfallen": False, "saetze": ["Es MUSS b."], "normative_idx": [1], "kann_idx": []}}
    gpp = {"catalog": {"groups": [{"id": "GC", "groups": [{"id": "GC.1", "controls": [
        {"id": "GC.1.1", "title": "G", "parts": [{"id": "GC.1.1_stm", "name": "statement", "prose": "Governance MUSS g."}]}]}]}]}}
    abgleich = {"ed23_baustein_abgleich": {"meta": {"version": "2026-10-18"}, "anforderungen": {
        "SYS.1.1.A1": {"zuordnungen": [Z("GC.1.1")], "neues_control": None, "ohne_control": None, "pruefung": None},
        "SYS.1.1.A2": {"zuordnungen": [], "neues_control": {"id": "NG-SYS.1.1.A2"}, "ohne_control": None, "pruefung": None}}}}
    ng_catalog = {"catalog": {"metadata": {"title": "NG Ergänzungskatalog"}, "groups": [{"id": "SYS", "groups": [
        {"id": "SYS.1.1", "controls": [{"id": "NG-SYS.1.1.A2"}]}]}]}}
    out_dir = tmp_path / "DE"
    out_dir.mkdir()
    ng_path = out_dir / "NG-ergaenzungskatalog.json"
    ng_path.write_text(json.dumps(ng_catalog), encoding="utf-8")
    cache_path = tmp_path / "cache.json"
    fake = FakeClient()
    reads = {"map": {"baustein_zielobjekt_map": {"SYS.1.1": "u1"}}, "abgleich": abgleich,
             str(ng_path): ng_catalog, "prompt": {"generate_enhanced_controls_prompt": "p"}, "schema": {"type": "array"}}

    def read(path, expected_sha256=None):
        if path in reads:
            return reads[path]
        with open(path, encoding="utf-8") as f:
            return json.load(f)

    patches = [
        patch.object(st, "BAUSTEIN_ZIELOBJEKT_JSON_PATH", "map"), patch.object(st, "ED23_BAUSTEIN_ABGLEICH_JSON_PATH", "abgleich"),
        patch.object(st, "PROMPT_CONFIG_PATH", "prompt"), patch.object(st, "ENHANCED_CONTROL_RESPONSE_SCHEMA_PATH", "schema"),
        patch.object(st, "ED23_PROFILES_DIR", str(out_dir)), patch.object(st, "NG_KATALOG_PATH", str(ng_path)),
        patch.object(st, "ED23_MATURITY_CACHE_JSON_PATH", str(cache_path)),
        patch.object(st, "read_json_file", read), patch.object(st.os.path, "exists", lambda p: p in ("abgleich",) or os.path.lexists(p)),
        patch.object(st, "read_csv_file", lambda _p: [{"UUID": "u1", "Zielobjekt": "IT-Systeme"}]),
        patch.object(st, "load_ed23_catalogs", lambda: (bd, bd)),
        patch.object(st, "fetch_official_xml", lambda: (b"", "s")), patch.object(st, "load_official_xml", lambda _b: (official, [])),
        patch.object(st, "load_json_file", lambda path, expected_sha256=None: gpp),
        patch.object(st, "load_maturity_cache", lambda: {"_meta": {}}),
        patch.object(st, "save_maturity_cache", lambda cache: cache_path.write_text(json.dumps({"ed23_maturity_cache": cache}))),
        patch.object(st, "AiClient", lambda cfg: fake),
        patch.object(st.app_config, "overwrite_temp_files", False), patch.object(st.app_config, "is_test_mode", False),
    ]
    for p in patches:
        p.start()
    try:
        await st.run_stage_ED23_profiles_enhanced()
        names = sorted(f.name for f in out_dir.iterdir())
        assert names == ["NG-ergaenzungskatalog.json", "it-systeme_SYS.1.1_server.json", "it-systeme_SYS.1.1_server_enhanced.json"]
        assert fake.calls == 1
        enhanced = json.loads((out_dir / "it-systeme_SYS.1.1_server_enhanced.json").read_text(encoding="utf-8"))
        sha = hashlib.sha256(ng_path.read_bytes()).hexdigest()
        assert enhanced["profile"]["back-matter"]["resources"][2]["rlinks"][0]["hashes"][0]["value"] == sha
        assert enhanced["profile"]["modify"]["alters"][0]["adds"][0]["parts"][1]["prose"] == "Governance MUSS g."  # m3 injected
        assert validate_ed23_profile_structure(enhanced, {"NG-SYS.1.1.A2"}, "it-systeme_SYS.1.1_server_enhanced.json") == []
        mtimes = {f.name: f.stat().st_mtime_ns for f in out_dir.iterdir()}
        # second run: cache hit, no call, no rewrite
        cached = json.loads(cache_path.read_text())["ed23_maturity_cache"]
        with patch.object(st, "load_maturity_cache", lambda: cached):
            await st.run_stage_ED23_profiles_enhanced()
        assert fake.calls == 1 and {f.name: f.stat().st_mtime_ns for f in out_dir.iterdir()} == mtimes
    finally:
        for p in patches:
            p.stop()
