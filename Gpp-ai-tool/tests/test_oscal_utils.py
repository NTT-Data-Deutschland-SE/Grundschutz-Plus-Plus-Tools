"""Tests of the back-matter helpers and the ED23 profile structure validator."""

from constants import ED23_BAUSTEIN_NS, NG_KATALOG_FILENAME
from utils import oscal_utils as ou


def test_resources_are_deterministic_and_pinned():
    r = ou.pinned_ed23_catalog_resource()
    assert r["uuid"] == ou.pinned_ed23_catalog_resource_uuid()
    assert r["rlinks"][0]["hashes"][0]["algorithm"] == "SHA-256"
    ng = ou.ng_katalog_resource("ab" * 32, 3, "NG Ergänzungskatalog")
    assert ng["rlinks"][0]["href"] == NG_KATALOG_FILENAME
    assert ng["uuid"] == ou.ng_katalog_resource_uuid("ab" * 32) != ou.ng_katalog_resource_uuid("cd" * 32)


def test_json_equal_ignoring():
    assert ou.json_equal_ignoring({"a": [{"last-modified": 1, "x": 2}]}, {"a": [{"last-modified": 9, "x": 2}]})
    assert not ou.json_equal_ignoring({"a": 1}, {"a": 2})


def _profile(ng=True):
    gpp_uuid, ng_uuid = ou.pinned_catalog_resource_uuid(), ou.ng_katalog_resource_uuid("ff" * 32)
    prof = {
        "uuid": "u", "metadata": {"title": "NG APP.4.10 – X", "oscal-version": "1.2.2", "props": [
            {"name": "herkunft", "ns": ED23_BAUSTEIN_NS, "value": "NG"},
            {"name": "ed23-baustein", "ns": ED23_BAUSTEIN_NS, "value": "APP.4.10"}]},
        "imports": [{"href": f"#{gpp_uuid}", "include-controls": [{"with-ids": ["KONF.1.1", "GC.1.1"]}]}],
        "merge": {"combine": {"method": "use-first"}, "custom": {"groups": [{"id": "APP.4.10-B", "class": "ed23-stufe", "groups": [
            {"id": "APP.4.10.A1", "class": "ed23-anforderung",
             "insert-controls": [{"include-controls": [{"with-ids": ["KONF.1.1", "GC.1.1"]}]}]},
            {"id": "APP.4.10.A2", "class": "ed23-anforderung", "links": [{"href": "#KONF.1.1", "rel": "related"}]},
            {"id": "APP.4.10.A3", "class": "ed23-anforderung",
             "props": [{"name": "ohne-control", "ns": ED23_BAUSTEIN_NS, "value": "hinweis"}]},
        ]}]}},
        "modify": {"alters": [{"control-id": "KONF.1.1", "adds": [
            {"position": "ending", "by-id": "KONF.1.1_stm", "parts": [{"id": "KONF.1.1-m1_custom", "name": "statement", "prose": "p"}]},
            {"position": "ending", "props": [{"name": "ed23-anforderung", "ns": ED23_BAUSTEIN_NS, "value": "APP.4.10.A1"}]},
        ]}]},
        "back-matter": {"resources": [ou.pinned_catalog_resource()]},
    }
    if ng:
        prof["imports"].append({"href": f"#{ng_uuid}", "include-controls": [{"with-ids": ["NG-APP.4.10.A4"]}]})
        prof["merge"]["custom"]["groups"][0]["groups"].append(
            {"id": "APP.4.10.A4", "class": "ed23-anforderung",
             "insert-controls": [{"include-controls": [{"with-ids": ["NG-APP.4.10.A4"]}]}]})
        prof["back-matter"]["resources"].append(ou.ng_katalog_resource("ff" * 32, 1, "NG"))
    return {"profile": prof}


def test_validator_accepts_a_well_formed_profile():
    assert ou.validate_ed23_profile_structure(_profile(), {"NG-APP.4.10.A4"}, "NG_anwendungen_APP.4.10_x.json") == []


def test_validator_flags_the_invariants():
    p = _profile()
    p["profile"]["merge"]["custom"]["groups"][0]["groups"][1]["insert-controls"] = [{"include-controls": [{"with-ids": ["KONF.1.1"]}]}]
    p["profile"]["imports"][0]["include-controls"][0]["with-ids"].append("NG-X")
    p["profile"]["merge"]["combine"]["method"] = "keep"
    problems = ou.validate_ed23_profile_structure(p, {"NG-APP.4.10.A4"}, "anwendungen_APP.4.10_x.json")
    text = "\n".join(problems)
    assert "inserted twice" in text and "must not hold NG- ids" in text and "use-first" in text
    assert "filename prefix NG_" in text and "never inserted" in text
