import json
import os
import unittest

from pipeline.stage_ed23_anforderungen import (
    build_ed23_corpus,
    build_gpp_match_contexts,
    _corpus_text,
    _filter_matches,
    _resolve_param_inserts,
    _split_sentences,
)
from utils.oscal_mapping import to_oscal_mapping_collection

MOCK_BSI = os.path.join(os.path.dirname(__file__), "mock_bsi_2023.json")


class TestSplitSentences(unittest.TestCase):
    def test_splits_on_terminal_punctuation(self):
        self.assertEqual(
            _split_sentences("Erster Satz. Zweiter Satz! Dritter Satz?"),
            ["Erster Satz.", "Zweiter Satz!", "Dritter Satz?"],
        )

    def test_does_not_split_at_abbreviations(self):
        text = "Die Institution MUSS z. B. Server härten. Dazu SOLLTE sie bzw. der Betrieb Vorgaben machen."
        self.assertEqual(
            _split_sentences(text),
            [
                "Die Institution MUSS z. B. Server härten.",
                "Dazu SOLLTE sie bzw. der Betrieb Vorgaben machen.",
            ],
        )

    def test_normalizes_whitespace_and_handles_empty(self):
        self.assertEqual(_split_sentences("  Ein\n Satz.  "), ["Ein Satz."])
        self.assertEqual(_split_sentences(""), [])
        self.assertEqual(_split_sentences(None), [])


class TestResolveParamInserts(unittest.TestCase):
    def test_replaces_with_values_then_label(self):
        params = {
            "p1": {"id": "p1", "values": ["BSI Grundschutz++"], "label": "ignored"},
            "p2": {"id": "p2", "label": "regelmäßig"},
        }
        self.assertEqual(
            _resolve_param_inserts("nach {{ insert: param, p1 }} und {{ insert: param, p2 }}", params),
            "nach BSI Grundschutz++ und regelmäßig",
        )

    def test_unresolvable_reference_left_verbatim(self):
        self.assertEqual(
            _resolve_param_inserts("nach {{ insert: param, missing }}", {}),
            "nach {{ insert: param, missing }}",
        )


class TestBuildGppMatchContexts(unittest.TestCase):
    def setUp(self):
        self.catalog = {
            "catalog": {
                "groups": [
                    {
                        "id": "GC",
                        "title": "Governance und Compliance",
                        "groups": [
                            {
                                "id": "GC.1",
                                "title": "Grundlagen",
                                "controls": [
                                    {
                                        "id": "GC.1.1",
                                        "title": "Errichtung eines ISMS",
                                        "params": [{"id": "gc.1.1-prm1", "values": ["BSI Grundschutz++"]}],
                                        "parts": [
                                            {"name": "statement", "prose": "MUSS ein ISMS nach {{ insert: param, gc.1.1-prm1 }} verankern."},
                                            {"name": "guidance", "prose": "Erläuterung zu {{ insert: param, gc.1.1-prm1 }}."},
                                        ],
                                        "controls": [
                                            {
                                                "id": "GC.1.1.1",
                                                "title": "Sub-Maßnahme",
                                                "parts": [{"name": "statement", "prose": "Sub-Statement."}],
                                            }
                                        ],
                                    },
                                    {
                                        "id": "GC.1.2",
                                        "title": "Freigabe des ISMS",
                                        "parts": [{"name": "statement", "prose": "MUSS das ISMS autorisieren."}],
                                    },
                                ],
                            }
                        ],
                    }
                ]
            }
        }
        self.contexts = build_gpp_match_contexts(self.catalog)

    def test_extracts_all_controls_including_nested(self):
        self.assertEqual(set(self.contexts), {"GC.1.1", "GC.1.1.1", "GC.1.2"})

    def test_params_resolved_in_statement_and_guidance(self):
        ctx = self.contexts["GC.1.1"]
        self.assertEqual(ctx["prose"], "MUSS ein ISMS nach BSI Grundschutz++ verankern.")
        self.assertEqual(ctx["guidance"], "Erläuterung zu BSI Grundschutz++.")

    def test_praktik_label_names_baustein_and_leaf_group(self):
        self.assertEqual(
            self.contexts["GC.1.1"]["praktik"],
            "Governance und Compliance / Grundlagen (GC.1)",
        )

    def test_siblings_list_other_praktik_controls_only(self):
        siblings = self.contexts["GC.1.1"]["siblings"]
        self.assertNotIn("GC.1.1 |", siblings)  # never lists itself
        self.assertIn("- GC.1.1.1 | Sub-Maßnahme | Sub-Statement.", siblings)
        self.assertIn("- GC.1.2 | Freigabe des ISMS | MUSS das ISMS autorisieren.", siblings)

    def test_lone_control_has_no_siblings(self):
        lone = {
            "catalog": {
                "groups": [
                    {"id": "X", "title": "X", "groups": [{"id": "X.1", "title": "P", "controls": [
                        {"id": "X.1.1", "title": "t", "parts": [{"name": "statement", "prose": "s."}]}
                    ]}]}
                ]
            }
        }
        self.assertEqual(build_gpp_match_contexts(lone)["X.1.1"]["siblings"], "(keine)")


class TestBuildEd23Corpus(unittest.TestCase):
    def setUp(self):
        with open(MOCK_BSI, encoding="utf-8") as f:
            self.catalog = json.load(f)
        self.stripped, self.lookup = build_ed23_corpus(self.catalog)

    def test_extracts_every_anforderung(self):
        ids = {a["id"] for a in self.stripped}
        self.assertIn("ISMS.1.A1", ids)
        self.assertIn("SYS.1.1.A1", ids)

    def test_entries_have_name_prose_and_sentences(self):
        entry = next(a for a in self.stripped if a["id"] == "ISMS.1.A1")
        self.assertEqual(entry["name"], "BSI Test Control (ISMS)")
        self.assertTrue(entry["prose"])  # statement prose captured
        self.assertNotIn("\n", entry["prose"])  # newlines flattened
        self.assertEqual(len(entry["saetze"]), 2)  # mock prose has two sentences
        self.assertEqual(" ".join(entry["saetze"]), entry["prose"])  # lossless split

    def test_lookup_keyed_by_normalized_id_with_sentence_count(self):
        # normalize_id lowercases + strips, so a messy id still resolves.
        self.assertEqual(self.lookup["sys.1.1.a1"]["id"], "SYS.1.1.A1")
        self.assertEqual(self.lookup["sys.1.1.a1"]["n_saetze"], 1)
        self.assertEqual(self.lookup["isms.1.a1"]["n_saetze"], 2)

    def test_corpus_text_numbers_sentences_one_line_per_anforderung(self):
        text = _corpus_text(self.stripped)
        self.assertEqual(len(text.splitlines()), len(self.stripped))
        self.assertIn("SYS.1.1.A1 | BSI Test Control (SYS) | (S1)", text)
        isms_line = next(l for l in text.splitlines() if l.startswith("ISMS.1.A1"))
        self.assertIn("(S1)", isms_line)
        self.assertIn("(S2)", isms_line)


class TestFilterMatches(unittest.TestCase):
    def setUp(self):
        with open(MOCK_BSI, encoding="utf-8") as f:
            catalog = json.load(f)
        _, self.lookup = build_ed23_corpus(catalog)

    def test_drops_hallucinated_ids_and_restores_canonical(self):
        raw = [
            {"id": " sys.1.1.a1 ", "name": "wrong name from model", "satz_nr": 1, "begruendung": "passt"},
            {"id": "FAKE.9.A99", "name": "Hallucinated", "satz_nr": 1, "begruendung": "erfunden"},
        ]
        result = _filter_matches(raw, self.lookup, "GC.1.1")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], "SYS.1.1.A1")  # canonical casing restored
        self.assertEqual(result[0]["name"], "BSI Test Control (SYS)")  # canonical name, not model's
        self.assertEqual(result[0]["begruendung"], "(Satz 1) passt")
        self.assertEqual(result[0]["satz_nr"], 1)

    def test_invalid_satz_nr_kept_without_sentence_ref(self):
        # SYS.1.1.A1 has one sentence; 2 is out of range. The match survives, the ref does not.
        raw = [{"id": "SYS.1.1.A1", "name": "x", "satz_nr": 2, "begruendung": "zu weit"}]
        result = _filter_matches(raw, self.lookup, "GC.1.1")
        self.assertEqual(len(result), 1)
        self.assertIsNone(result[0]["satz_nr"])
        self.assertEqual(result[0]["begruendung"], "zu weit")

    def test_missing_or_non_integer_satz_nr_tolerated(self):
        raw = [
            {"id": "ISMS.1.A1", "name": "x", "begruendung": "ohne satz_nr"},
            {"id": "SYS.1.1.A1", "name": "y", "satz_nr": "S1", "begruendung": "string statt int"},
        ]
        result = _filter_matches(raw, self.lookup, "GC.1.1")
        self.assertEqual([m["satz_nr"] for m in result], [None, None])

    def test_dedupes_repeated_ids(self):
        raw = [
            {"id": "SYS.1.1.A1", "name": "x", "satz_nr": 1, "begruendung": "a"},
            {"id": "sys.1.1.a1", "name": "y", "satz_nr": 1, "begruendung": "b"},
        ]
        self.assertEqual(len(_filter_matches(raw, self.lookup, "GC.1.1")), 1)

    def test_non_list_returns_empty(self):
        self.assertEqual(_filter_matches({"id": "SYS.1.1.A1"}, self.lookup, "GC.1.1"), [])
        self.assertEqual(_filter_matches(None, self.lookup, "GC.1.1"), [])


class TestToOscalMappingCollection(unittest.TestCase):
    def setUp(self):
        self.sample = {
            "GC.1.1": [
                {"id": "ISMS.1.A1", "name": "Übernahme der Gesamtverantwortung", "begruendung": "(Satz 2) passt thematisch", "satz_nr": 2},
                {"id": "ORP.1.A1", "name": "Festlegung von Verantwortlichkeiten", "begruendung": "ergänzt", "satz_nr": None},
            ],
            "GC.2.1": [
                {"id": "SYS.1.1.A1", "name": "BSI Test Control (SYS)", "begruendung": ""},
            ],
            "GC.9.9": [],  # a control with no matches contributes no map entries
        }
        self.doc = to_oscal_mapping_collection(
            self.sample, last_modified="2026-01-01T00:00:00+00:00", version="2026-01-01"
        )
        self.mc = self.doc["mapping-collection"]

    def test_root_and_metadata(self):
        self.assertIn("mapping-collection", self.doc)
        self.assertTrue(self.mc["uuid"])
        self.assertEqual(self.mc["metadata"]["oscal-version"], "1.2.2")
        self.assertEqual(self.mc["metadata"]["version"], "2026-01-01")
        self.assertTrue(self.mc["metadata"]["title"])

    def test_provenance_uses_valid_tokens(self):
        prov = self.mc["provenance"]
        self.assertEqual(prov["method"], "automation")            # human|automation|hybrid
        self.assertEqual(prov["matching-rationale"], "semantic")  # syntactic|semantic|functional
        self.assertEqual(prov["status"], "draft")                 # complete|not-complete|draft|...
        self.assertTrue(prov["mapping-description"])               # required markup-multiline

    def test_single_mapping_with_catalog_resources(self):
        self.assertEqual(len(self.mc["mappings"]), 1)
        mp = self.mc["mappings"][0]
        self.assertEqual(mp["source-resource"]["type"], "catalog")
        self.assertEqual(mp["target-resource"]["type"], "catalog")
        self.assertTrue(mp["source-resource"]["href"])
        self.assertTrue(mp["target-resource"]["href"])

    def test_one_map_per_pair(self):
        # 2 (GC.1.1) + 1 (GC.2.1) + 0 (GC.9.9) = 3
        self.assertEqual(len(self.mc["mappings"][0]["maps"]), 3)

    def test_map_shape_name_begruendung_and_sentence_prop(self):
        maps = self.mc["mappings"][0]["maps"]
        by_target = {m["targets"][0]["id-ref"]: m for m in maps}
        m = by_target["ISMS.1.A1"]
        self.assertEqual(m["relationship"], "intersects-with")
        self.assertEqual(m["sources"][0], {"type": "control", "id-ref": "GC.1.1"})
        self.assertEqual(m["targets"][0]["type"], "control")
        self.assertEqual(
            m["targets"][0]["props"],
            [
                {"name": "label", "value": "Übernahme der Gesamtverantwortung"},
                {"name": "statement-sentence", "value": "2"},
            ],
        )
        self.assertEqual(m["remarks"], "(Satz 2) passt thematisch")

    def test_no_sentence_prop_without_satz_nr(self):
        maps = self.mc["mappings"][0]["maps"]
        by_target = {m["targets"][0]["id-ref"]: m for m in maps}
        for target_id in ("ORP.1.A1", "SYS.1.1.A1"):
            props = by_target[target_id]["targets"][0].get("props", [])
            self.assertNotIn("statement-sentence", [p["name"] for p in props])

    def test_empty_begruendung_omits_remarks(self):
        maps = self.mc["mappings"][0]["maps"]
        m = next(m for m in maps if m["targets"][0]["id-ref"] == "SYS.1.1.A1")
        self.assertNotIn("remarks", m)

    def test_deterministic_output(self):
        again = to_oscal_mapping_collection(
            self.sample, last_modified="2026-01-01T00:00:00+00:00", version="2026-01-01"
        )
        self.assertEqual(json.dumps(self.doc, sort_keys=True), json.dumps(again, sort_keys=True))


if __name__ == "__main__":
    unittest.main()
