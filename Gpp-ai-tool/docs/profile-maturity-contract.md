# Enhanced Profile ↔ One-Page-App contract

This document is the single source of truth for the structure that the `Gpp-ai-tool`
enhancement stages emit and that the `GS++-oscal-app` consume. It exists because that
structure is an **implicit contract**: a rename on either side silently breaks consumption
(issue 3.9). Keep this file in sync with `build_oscal_maturity_statements` in
`src/pipeline/stage_ED23_profiles_enhanced.py` and `…/stage_base_process_enhanced.py`.

## Where the data lives

An enhanced profile is a normal OSCAL 1.2.2 **profile**:

- `profile.imports[].include-controls[].with-ids[]` — the G++ control IDs in scope. The
  actual control title/prose/baseline live in the imported **G++ catalog**
  (`profile.imports[].href`), not in the profile.
- `profile.modify.alters[]` — one entry per enriched control (`control-id`).
- `alters[].adds[]` — a single `adds` block per control with:
  - `position`: `"ending"`
  - `by-id`: the control's real **statement part id** (looked up from the catalog — the id
    of the part whose `name == "statement"`, e.g. `ARCH.7.1_stm`). Controls with no
    statement part are skipped (issue 3.4).
  - `parts[]`: the five maturity-level parts.

## The maturity part shape (current, post issue 3.1)

Each maturity level is one `statement` part:

```jsonc
{
  "id": "ARCH.7.1-m1_custom",      // "{control_id}-m{level}_custom", unique
  "name": "statement",
  "props": [
    { "name": "control_class",  "value": "Technical",      "ns": "<G++ ns>" },
    { "name": "phase",          "value": "Implementation", "ns": "<G++ ns>" },
    { "name": "label",          "value": "m1" }
  ],
  "prose": "<the maturity-level statement text>",   // the real per-level statement
  "parts": [                                         // optional, omitted if empty
    { "id": "ARCH.7.1-m1_custom_gdn", "name": "guidance",   "prose": "<guidance text>" },
    { "id": "ARCH.7.1-m1_custom_asm", "name": "assessment", "prose": "<assessment text>" }
  ]
}
```

- `ns` = `GPP_ENHANCEMENT_PROPS_NS` (`src/constants.py`) =
  `https://github.com/NTT-Data-Deutschland-SE/Grundschutz-Plus-Plus-Tools/tree/main/Dokumentation/namespaces/gpp_enhancement_props.md`
  — used by **both** enhancement stages.
- **`prose` is the statement** (so generic OSCAL renderers show the real content).
- **Guidance and assessment are nested `parts`** (`name: "guidance"` / `"assessment"`), not
  props.
- **Props carry only metadata**: classification (`control_class`, `phase`) and the level
  `label` (`m1`…`m5`). Schutzziel impact is **not** part of this contract anymore: the
  former `effective_on_{c,i,a}` props were removed (2026-08) in favor of the authoritative
  BSI control-level props `confidentiality` / `integrity` / `availability` / `authenticity`
  (values `0`–`2`, ns `…/documentation/namespaces/security_targets.csv`) in the imported
  G++ catalog. Migration: `scripts/migrate_remove_effective_on_props.py`.
- **Level 3 (`m3`)** `prose` is the original G++ control prose verbatim (injected
  deterministically, issue 2.2). Levels 1/2/4/5 are AI-generated and may be absent.

## Reading it (consumer recipe)

For each `alters[]` entry, for each `adds[].parts[]` with `name === "statement"`:

```js
const props = Object.fromEntries((pt.props || []).map(p => [p.name, p.value]));
const sub   = Object.fromEntries((pt.parts || []).map(np => [np.name, np.prose]));

const level      = props.label;            // "m1".."m5"
const statement  = pt.prose;               // per-level statement
const guidance   = sub.guidance   || "";
const assessment = sub.assessment || "";
const cls        = props.control_class;
// Schutzziel impact: read confidentiality/integrity/availability/authenticity (0-2)
// from the catalog control's own props, NOT from the maturity statement.
```

Reference implementations: `parseProfileEntry` in `GS++-oscal-app/pruefung_ap_ar.html` and the
`modify.alters` loop in `GS++-oscal-app/ssp_ausfuellen.html`.

## Legacy shape (pre issue 3.1) — fallback only

Older profiles stored the per-level text in props (`statement`, `guidance`,
`assessment-method`) and duplicated the original description into `prose`. The consuming apps
read the new shape first and **fall back** to these props if present, so legacy artifacts
still render. A one-time, idempotent migration to the new shape is available at
`scripts/migrate_maturity_parts_to_prose.py`.

## Change discipline

If you change a prop name, a part `name`, the `by-id` convention, or move text between
`prose`/`props`/nested parts, update **all** of: both `build_oscal_maturity_statements`
implementations, the migration script, the consuming apps, and this document.
