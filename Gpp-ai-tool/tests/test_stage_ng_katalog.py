"""Tests of the deterministic NG Ergänzungskatalog builder."""

from constants import ED23_BAUSTEIN_NS
from pipeline import stage_ng_katalog as st

BD = {"catalog": {"groups": [
    {"id": "SYS", "title": "SYS: Systeme", "groups": [{"id": "SYS.1.1", "class": "baustein", "title": "Server", "controls": []}]},
    {"id": "APP", "title": "APP: Anwendungen", "groups": [{"id": "APP.4.10", "class": "baustein", "title": "KI", "controls": []}]},
]}}


def _rec(bid, level_num="1", **nc):
    base = {"id": f"NG-{bid}.A9", "titel": "Krypto-Kataster", "statement": "Die Institution MUSS ein Kataster führen.",
            "guidance": "g", "modalverb": "MUSS", "praktik": "ASST", "zielobjektkategorien": ["IT-Systeme"],
            "verwandte_controls": ["ASST.3.1"], "konfidenz": "mittel", "checker": "bestaetigt", "checker_begruendung": "ok", "hinweis": ""}
    base.update(nc)
    return {"baustein": bid, "level_num": level_num, "neues_control": base}


ABGLEICH = {"ed23_baustein_abgleich": {"meta": {"version": "2026-10-18", "ng_bausteine": ["APP.4.10"], "model": "gemini-4-argon"},
            "anforderungen": {"SYS.1.1.A9": _rec("SYS.1.1"), "APP.4.10.A9": _rec("APP.4.10", level_num="5", zielobjektkategorien=[], praktik="GC"),
                              "SYS.1.1.A1": {"baustein": "SYS.1.1", "neues_control": None}}}}


def test_builder_groups_marks_and_formats_controls():
    doc = st.build_ng_katalog(ABGLEICH, BD, {"ASST.3.1": "Inventar"}, "erhöht", "2026-01-01T00:00:00Z")
    cat = doc["catalog"]
    assert cat["metadata"]["title"].startswith("NG Ergänzungskatalog") and cat["metadata"]["oscal-version"] == "1.2.2"
    assert [l["id"] for l in cat["groups"]] == ["APP", "SYS"]
    app = cat["groups"][0]["groups"][0]
    assert app["class"] == "ng-baustein" and app["title"].startswith("NG APP.4.10")
    sys_g = cat["groups"][1]["groups"][0]
    assert sys_g["class"] == "baustein" and sys_g["title"] == "SYS.1.1 – Server"
    c = sys_g["controls"][0]
    assert c["id"] == "NG-SYS.1.1.A9" and c["class"] == "ng-ergaenzung" and c["title"] == "NG: Krypto-Kataster"
    props = {p["name"]: p for p in c["props"]}
    assert props["herkunft"]["value"] == "NG" and props["herkunft"]["ns"] == ED23_BAUSTEIN_NS
    assert props["ed23-anforderung"]["value"] == "SYS.1.1.A9" and props["ed23-anforderung"]["remarks"].startswith("Herkunft:")
    assert props["sec_level"]["value"] == "normal-SdT" and props["level"]["value"] == "1"
    stm = c["parts"][0]
    assert stm["id"] == "NG-SYS.1.1.A9_stm" and {p["name"]: p["value"] for p in stm["props"]} == {
        "target_object_categories": "IT-Systeme", "modal_verb": "MUSS"}
    assert c["links"][0]["href"].endswith("#ASST.3.1") and "Inventar" in c["links"][0]["text"]
    ki = app["controls"][0]
    assert {p["name"]: p["value"] for p in ki["props"]}["sec_level"] == "erhöht"
    assert [p["name"] for p in ki["parts"][0]["props"]] == ["modal_verb"]  # no categories for a process practice
    assert len(cat["back-matter"]["resources"]) == 3


def test_builder_is_deterministic():
    a = st.build_ng_katalog(ABGLEICH, BD, {}, None, "x")
    b = st.build_ng_katalog(ABGLEICH, BD, {}, None, "y")
    from utils.oscal_utils import json_equal_ignoring
    assert json_equal_ignoring(a, b) and a["catalog"]["uuid"] == b["catalog"]["uuid"]
    assert st.sec_level_for("5", None) == "normal-SdT" and st.sec_level_for("3", "erhöht") == "normal-SdT"
