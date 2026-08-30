# Grundschutz++ Enhancement Property Namespace

This file is the OSCAL property **naming-system identifier** (`ns`) for the custom properties
that the `Gpp-ai-tool` ED2023 enhancement stage (`stage_ED23_profiles_enhanced`) attaches to each
maturity-level `statement` part of an *enhanced* OSCAL profile.

**Namespace URI** (use verbatim as the prop `ns`):

```
https://github.com/NTT-Data-Deutschland-SE/Grundschutz-Plus-Plus-Tools/tree/main/Dokumentation/namespaces/gpp_enhancement_props.md
```

These properties are **not** defined by OSCAL (whose namespace `http://csrc.nist.gov/ns/oscal` is
reserved for OSCAL-defined names) and are **not** part of the BSI Stand-der-Technik-Bibliothek
namespaces, so they carry this dedicated namespace to avoid collisions — the same `ns`-per-naming-system
convention the BSI catalogs use for `modal_verbs.csv`, `security_level.csv`, etc.

## Properties

| prop `name`      | meaning                                                       | allowed values |
|------------------|--------------------------------------------------------------|----------------|
| `control_class`  | Functional class of the control (NIST-style)                 | `Technical`, `Operational`, `Management` |
| `phase`          | ISMS lifecycle phase the control primarily applies to        | `Initiation`, `Risk Assessment`, `Risk Treatment`, `Implementation`, `Operation`, `Audit`, `Improvement` |
| `matching-direction` | Provenance of a map entry in `hilfsdateien/gpp_ed23_anforderungen.json`: which candidate-search direction found the pair | `gpp-seitig`, `ed23-seitig`, `beide`, `qs-nachfass` |

**Note on `matching-direction` (Issue #37, QS-Stichprobe 2026-08-30):** the value is a
*confidence* signal about the candidate search, **not** a quality seal for the pair's content.
`beide` means both search directions independently proposed the pair — it does not imply the
relationship type or the remark were verified against the exact wording (the QS found a
fabricated remark detail on a `beide` pair, see `hilfsdateien/ed23_mapping_qs/bericht.md`,
Befund B). Consumers weighing evidence should treat `beide` as higher recall confidence only.

**Removed (2026-08):** the former `effective_on_c` / `effective_on_i` / `effective_on_a` props
(AI-estimated Schutzziel impact per maturity statement) were dropped. The authoritative source
for Schutzziel impact are the BSI control-level props `confidentiality`, `integrity`,
`availability`, `authenticity` (values `0`–`2`) carried by the imported G++ catalog itself, ns
`https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek/tree/main/documentation/namespaces/security_targets.csv`
(value semantics: `security_targets_levels.csv`). Consumers must read those instead.

The maturity level itself is carried by the **standard OSCAL `label` property** (`m1` … `m5`, no
custom `ns`) on the same `statement` part, and is therefore intentionally not listed here.

The allowed values above are enforced by the AI response schema
`Gpp-ai-tool/src/assets/schemas/enhanced_control_response_schema.json`.
