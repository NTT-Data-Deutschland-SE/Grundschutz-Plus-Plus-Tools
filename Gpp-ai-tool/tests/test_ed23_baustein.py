"""Unit tests of the deterministic ED23-Baustein helpers (NG detection, records, inversion, ids)."""

from utils import ed23_baustein as m


def _control(cid, title, level="1", statement="Die Institution MUSS x tun.", guidance="g"):
    return {
        "id": cid, "title": title,
        "props": [{"name": "level", "value": level, "ns": "https://www.bsi.bund.de/ns/grundschutz"}],
        "parts": [
            {"id": f"{cid}-m1", "class": "maturity-level-partial", "parts": [{"name": "statement", "prose": "weniger"}]},
            {"id": f"{cid}-m3", "class": "maturity-level-defined",
             "parts": [{"name": "statement", "prose": statement}, {"name": "guidance", "prose": guidance}]},
        ],
    }


def _catalog(bausteine):
    layers = {}
    for bid, controls in bausteine.items():
        layers.setdefault(bid.split(".")[0], []).append({
            "id": bid, "class": "baustein", "title": f"Titel {bid}",
            "parts": [{"name": "Zielsetzung", "prose": f"Ziel von {bid}"}],
            "controls": controls,
        })
    return {"catalog": {"groups": [
        {"id": lid, "class": "layer", "title": f"{lid}: Schicht", "groups": groups} for lid, groups in layers.items()
    ]}}


PLAIN = _catalog({
    "SYS.1.1": [_control("SYS.1.1.A1", "Aufstellung (B)"), _control("SYS.1.1.A2", "ENTFALLEN")],
    "OPS.2.2": [_control("OPS.2.2.A1", "Strategie (B) [ISB]")],
})
BD = _catalog({
    "SYS.1.1": [_control("SYS.1.1.A1", "Aufstellung (B)"), _control("SYS.1.1.A2", "ENTFALLEN"),
                _control("SYS.1.1.A99", "NTT-Zusatz (S)", level="3")],
    "OPS.2.2": [_control("OPS.2.2.A1", "Strategie (B) [ISB]")],
    "APP.4.10": [_control("APP.4.10.A1", "Planung KI (B) [ISB]", statement="Es MUSS eine Richtlinie geben. Sie KANN mehr."),
                 _control("APP.4.10.A2", "Erhöht (H)", level="5", statement="Die Institution SOLLTE y.")],
})
OFFICIAL = {
    "SYS.1.1.A1": {"id": "SYS.1.1.A1", "titel": "Geeignete Aufstellung", "level": "B", "rolle": None, "entfallen": False,
                   "saetze": ["Server MÜSSEN geschützt stehen.", "Sie DÜRFEN NICHT offen stehen."],
                   "normative_idx": [1, 2], "kann_idx": []},
    "SYS.1.1.A2": {"id": "SYS.1.1.A2", "titel": "ENTFALLEN", "level": "B", "rolle": None, "entfallen": True,
                   "saetze": ["Diese Anforderung ist entfallen."], "normative_idx": [], "kann_idx": []},
    "OPS.2.2.A1": {"id": "OPS.2.2.A1", "titel": "Strategie", "level": "B", "rolle": "ISB", "entfallen": False,
                   "saetze": ["Es KANN eine Strategie geben."], "normative_idx": [], "kann_idx": [1]},
}


def test_detect_ng_finds_whole_bausteine_and_extra_anforderungen():
    ng = m.detect_ng(BD, PLAIN)
    assert ng["bausteine"] == {"APP.4.10"}
    assert ng["anforderungen"] == {"APP.4.10.A1", "APP.4.10.A2", "SYS.1.1.A99"}


def test_records_prefer_xml_for_bsi_and_bd_m3_for_ng():
    recs = m.build_anforderung_records(BD, OFFICIAL, m.detect_ng(BD, PLAIN))
    a1 = recs["SYS.1.1.A1"]
    assert a1["herkunft"] == "BSI" and a1["text_quelle"] == "xml"
    assert a1["modalverb"] == "DARF NICHT" and a1["level"] == "B" and a1["level_num"] == "1"
    assert recs["SYS.1.1.A2"]["entfallen"] is True
    assert recs["OPS.2.2.A1"]["kann_only"] is True and recs["OPS.2.2.A1"]["rolle"] == "ISB"
    ki = recs["APP.4.10.A1"]
    assert ki["herkunft"] == "NG" and ki["text_quelle"] == "bd-m3" and ki["titel"] == "Planung KI"
    assert ki["modalverb"] == "MUSS" and ki["rolle"] == "ISB" and ki["normative_idx"] == [1]
    assert recs["APP.4.10.A2"]["level"] == "H" and recs["APP.4.10.A2"]["modalverb"] == "SOLLTE"
    extra = recs["SYS.1.1.A99"]
    assert extra["herkunft"] == "NG" and extra["level"] == "S" and extra["text_quelle"] == "bd-m3"


def test_records_can_be_limited_to_bausteine():
    recs = m.build_anforderung_records(BD, OFFICIAL, m.detect_ng(BD, PLAIN), bausteine=["APP.4.10"])
    assert set(recs) == {"APP.4.10.A1", "APP.4.10.A2"}


def test_invert_mapping_collection_dedupes_and_collects_sentences():
    doc = {"mapping-collection": {"mappings": [{"maps": [
        {"relationship": "subset-of", "remarks": "r1", "sources": [{"id-ref": "KONF.1.1"}],
         "targets": [{"id-ref": "SYS.1.1.A1", "props": [{"name": "statement-sentence", "value": "2"}]}],
         "props": [{"name": "matching-direction", "value": "beide"}]},
        {"relationship": "intersects-with", "remarks": "r2", "sources": [{"id-ref": "KONF.1.1"}],
         "targets": [{"id-ref": "SYS.1.1.A1", "props": [{"name": "statement-sentence", "value": "1"}]}]},
        {"relationship": "equal-to", "sources": [{"id-ref": "GC.1.1"}], "targets": [{"id-ref": "SYS.1.1.A1"}]},
    ]}]}}
    inv = m.invert_mapping_collection(doc)
    assert [e["control_id"] for e in inv["SYS.1.1.A1"]] == ["GC.1.1", "KONF.1.1"]
    konf = inv["SYS.1.1.A1"][1]
    assert konf["relation"] == "subset-of" and konf["satz_nr"] == [2, 1] and konf["richtung"] == "beide"
    assert inv["SYS.1.1.A1"][0]["satz_nr"] == []


def test_load_satz_abdeckung_and_gsmap():
    satz = m.load_satz_abdeckung({"ed23_satz_abdeckung": {"anforderungen": {
        "SYS.1.1.A1": {"treffer": [{"satz_nr": 1, "control_id": "KONF.1.1", "begruendung": "b"},
                                   {"satz_nr": 2, "control_id": "KONF.1.1"}]},
        "SYS.1.1.A2": {"treffer": []},
    }}})
    assert satz == {"SYS.1.1.A1": [{"control_id": "KONF.1.1", "satz_nr": [1, 2], "begruendung": "b"}]}
    gs = m.load_gsmap_by_anforderung(b'{"mapping-collection": {"mappings": [{"maps": [{"relationship": "subset-of", '
                                     b'"sources": [{"id-ref": "SYS.1.1.A1-UA.2"}], "targets": [{"id-ref": "ARCH.1.1"}]}]}]}}')
    assert gs == {"SYS.1.1.A1": [{"control_id": "ARCH.1.1", "relation": "subset-of", "ua_idx": [2]}]}


def test_modal_verbs_and_ordering():
    assert m.normalize_modal_verbs("MÜSSEN, SOLLTEN und DÜRFEN NICHT, aber kann") == ["MUSS", "SOLLTE", "DARF NICHT"]
    assert m.dominant_modal_verb(["Es KANN.", "Es SOLLTE."]) == "SOLLTE"
    assert m.dominant_modal_verb("nichts normatives") is None
    assert m.modal_weaker("SOLLTE", "MUSS") and not m.modal_weaker("MUSS", "SOLLTE")
    ids = ["SYS.1.1.A10", "SYS.1.1.A2", "APP.4.10.A1", "SYS.1.1.A1"]
    assert sorted(ids, key=m.anforderung_sort_key) == ["APP.4.10.A1", "SYS.1.1.A1", "SYS.1.1.A2", "SYS.1.1.A10"]
    assert sorted(["SYS.1.10", "SYS.1.2.4", "SYS.1.1"], key=m.baustein_sort_key) == ["SYS.1.1", "SYS.1.2.4", "SYS.1.10"]


def test_id_and_title_scheme():
    assert m.ng_control_id("SYS.1.1.A5") == "NG-SYS.1.1.A5"
    assert m.ng_title("Krypto-Kataster") == "NG: Krypto-Kataster"
    assert m.profile_file_stem("Anwendungen", "APP.4.10", "Sicherheit von KI-Systemen", True) == \
        "NG_anwendungen_APP.4.10_sicherheit_von_ki-systemen"
    assert m.profile_file_stem("DNS-Server", "APP.3.6", "DNS-Server", False) == "dns-server_APP.3.6_dns-server"
