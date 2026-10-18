"""Tests of the incremental Baustein → Zielobjekt match stage (offline, fake client)."""

import json
import os
import tempfile
from unittest.mock import patch

from pipeline import stage_match_bausteine as st


CATALOG = {"catalog": {"groups": [{"id": "SYS", "groups": [
    {"id": "SYS.1.1", "class": "baustein", "title": "Server", "parts": [{"name": "Zielsetzung", "prose": "z"}], "controls": []},
    {"id": "SYS.1.2", "class": "baustein", "title": "Neu", "parts": [{"name": "Zielsetzung", "prose": "z"}], "controls": []},
    {"id": "SYS.1.3", "class": "baustein", "title": "Neu2", "parts": [{"name": "Zielsetzung", "prose": "z"}], "controls": []},
]}]}}
CSV = [{"UUID": "u1", "Zielobjekt": "Server", "Definition": "d"}, {"UUID": "u2", "Zielobjekt": "Clients", "Definition": "d"}]


class FakeClient:
    def __init__(self, *_):
        self.calls = []

    async def generate_validated_json_response(self, prompt, json_schema, request_context_log, **kw):
        self.calls.append(request_context_log)
        return {"matched_zielobjekt": "Clients"}

    def log_usage_summary(self, label=""):
        pass


async def test_only_missing_bausteine_are_queried_and_stale_entries_dropped():
    with tempfile.TemporaryDirectory() as tmp:
        out = os.path.join(tmp, "baustein_zielobjekt.json")
        with open(out, "w", encoding="utf-8") as f:
            json.dump({"baustein_zielobjekt_map": {"SYS.1.1": "u1", "OLD.9": "u1"}}, f)
        fake = FakeClient()
        loads = {st.BSI_2023_JSON_PATH: CATALOG, st.PROMPT_CONFIG_PATH: {"baustein_to_zielobjekt_prompt": "p"},
                 st.BAUSTEIN_TO_ZIELOBJEKT_SCHEMA_PATH: {"type": "object"}}
        with patch.object(st, "load_json_file", lambda path, expected_sha256=None: loads.get(path, {})), \
             patch.object(st, "load_zielobjekte_csv", lambda _p: CSV), \
             patch.object(st, "AiClient", lambda cfg: fake), \
             patch.object(st, "BAUSTEIN_ZIELOBJEKT_JSON_PATH", out), \
             patch.object(st.app_config, "overwrite_temp_files", False), \
             patch.object(st.app_config, "is_test_mode", False):
            await st.run_stage_match_bausteine()
            assert sorted(fake.calls) == ["BausteinToZielobjekt-SYS.1.2", "BausteinToZielobjekt-SYS.1.3"]
            with open(out, encoding="utf-8") as f:
                saved = json.load(f)["baustein_zielobjekt_map"]
            assert saved == {"SYS.1.1": "u1", "SYS.1.2": "u2", "SYS.1.3": "u2"}
            # second run: nothing pending, no call
            fake.calls.clear()
            await st.run_stage_match_bausteine()
            assert fake.calls == []
            # a stale entry with nothing pending is still pruned from the file
            with open(out, "w", encoding="utf-8") as f:
                json.dump({"baustein_zielobjekt_map": {"SYS.1.1": "u1", "SYS.1.2": "u2", "SYS.1.3": "u2", "OLD.9": "u1"}}, f)
            await st.run_stage_match_bausteine()
            assert fake.calls == []
            with open(out, encoding="utf-8") as f:
                assert json.load(f)["baustein_zielobjekt_map"] == {"SYS.1.1": "u1", "SYS.1.2": "u2", "SYS.1.3": "u2"}
