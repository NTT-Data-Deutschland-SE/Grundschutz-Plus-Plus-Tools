"""Smoke test of ED23-Baustein-profile/pruefe_export.py on a synthetic profile pair + NG catalog."""

import hashlib
import importlib.util
import json
import pathlib
import uuid

from constants import ED23_BAUSTEIN_NS
from utils import oscal_utils as ou

REPO = pathlib.Path(__file__).resolve().parents[2]


def _load_script():
    spec = importlib.util.spec_from_file_location("pruefe_export_ed23", REPO / "ED23-Baustein-profile" / "pruefe_export.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _write(tmp_path):
    ng = {"catalog": {"uuid": str(uuid.uuid4()), "metadata": {"title": "NG Ergänzungskatalog x", "last-modified": "2026-01-01T00:00:00Z",
                                                "version": "1", "oscal-version": "1.2.2",
                                                "props": [{"name": "herkunft", "ns": ED23_BAUSTEIN_NS, "value": "NG"}]},
                      "groups": [{"id": "SYS", "title": "SYS", "groups": [{"id": "SYS.1.1", "title": "S", "controls": [
                          {"id": "NG-SYS.1.1.A4", "class": "ng-ergaenzung", "title": "NG: X",
                           "props": [{"name": "herkunft", "ns": ED23_BAUSTEIN_NS, "value": "NG"},
                                     {"name": "ed23-anforderung", "ns": ED23_BAUSTEIN_NS, "value": "SYS.1.1.A4"}],
                           "parts": [{"id": "NG-SYS.1.1.A4_stm", "name": "statement", "prose": "Es MUSS x."}]}]}]}]}}
    ng_path = tmp_path / "NG-ergaenzungskatalog.json"
    ng_path.write_text(json.dumps(ng, ensure_ascii=False), encoding="utf-8")
    sha = hashlib.sha256(ng_path.read_bytes()).hexdigest()
    gpp_res = ou.pinned_catalog_resource()

    def profile(variant):
        p = {"uuid": str(uuid.uuid5(uuid.NAMESPACE_URL, variant)), "metadata": {"title": "SYS.1.1 – S (IT-Systeme)", "last-modified": "2026-01-01T00:00:00Z", "version": "1",
                                                  "oscal-version": "1.2.2", "props": [
                {"name": "herkunft", "ns": ED23_BAUSTEIN_NS, "value": "BSI"}, {"name": "ed23-baustein", "ns": ED23_BAUSTEIN_NS, "value": "SYS.1.1"}]},
             "imports": [{"href": f"#{gpp_res['uuid']}", "include-controls": [{"with-ids": ["GC.1.1"]}]},
                         {"href": f"#{ou.ng_katalog_resource_uuid(sha)}", "include-controls": [{"with-ids": ["NG-SYS.1.1.A4"]}]}],
             "merge": {"combine": {"method": "use-first"}, "custom": {"groups": [{"id": "SYS.1.1-B", "class": "ed23-stufe", "title": "B", "groups": [
                 {"id": "SYS.1.1.A1", "class": "ed23-anforderung", "title": "A1", "parts": [{"id": "SYS.1.1.A1_anforderung", "name": "overview", "prose": "t"}],
                  "insert-controls": [{"include-controls": [{"with-ids": ["GC.1.1"]}]}]},
                 {"id": "SYS.1.1.A4", "class": "ed23-anforderung", "title": "A4", "parts": [{"id": "SYS.1.1.A4_anforderung", "name": "overview", "prose": "t"}],
                  "insert-controls": [{"include-controls": [{"with-ids": ["NG-SYS.1.1.A4"]}]}]}]}]}},
             "modify": {"alters": [{"control-id": "GC.1.1", "adds": [{"position": "ending", "props": [{"name": "ed23-anforderung", "ns": ED23_BAUSTEIN_NS, "value": "SYS.1.1.A1"}]}]}]},
             "back-matter": {"resources": [gpp_res, ou.ng_katalog_resource(sha, 1, "NG")]}}
        return {"profile": p}

    (tmp_path / "it-systeme_SYS.1.1_s.json").write_text(json.dumps(profile("plain")), encoding="utf-8")
    (tmp_path / "it-systeme_SYS.1.1_s_enhanced.json").write_text(json.dumps(profile("enhanced")), encoding="utf-8")
    gpp = {"catalog": {"groups": [{"id": "GC", "controls": [{"id": "GC.1.1"}]}]}}
    (tmp_path / "src").mkdir()
    gpp_path = tmp_path / "src" / "gpp.json"
    gpp_path.write_text(json.dumps(gpp), encoding="utf-8")
    return ng_path, gpp_path


def test_script_passes_on_a_consistent_pair_and_flags_a_hash_mismatch(tmp_path, capsys):
    mod = _load_script()
    ng_path, gpp_path = _write(tmp_path)
    rc = mod.main(["x", str(tmp_path), "--gpp-catalog", str(gpp_path)])
    out = capsys.readouterr().out
    # the synthetic G++ catalog does not match the pinned hash → that is reported, nothing else
    assert "Hash des Anwenderkatalogs weicht ab" in out
    assert rc == 0, out
    ng_path.write_text(ng_path.read_text(encoding="utf-8") + " ", encoding="utf-8")
    rc = mod.main(["x", str(tmp_path), "--offline"])
    out = capsys.readouterr().out
    assert rc == 1 and "Hash des NG-Katalogs weicht ab" in out
