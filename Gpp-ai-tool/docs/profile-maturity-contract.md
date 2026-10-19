# Enhanced Profile ↔ One-Page-App contract

This document is the single source of truth for the structure that the `Gpp-ai-tool`
enhancement stages emit and that the `GS++-oscal-app` consume. It exists because that
structure is an **implicit contract**: a rename on either side silently breaks consumption
(issue 3.9). Keep this file in sync with `build_oscal_maturity_statements` in
`src/pipeline/stage_ED23_profiles_enhanced.py` and `…/stage_base_process_enhanced.py`.

## Profile shape since 2026-10 (Mindeststandard pattern)

An ED23-Baustein profile (`ED23-Baustein-profile/DE/*.json`) is a normal OSCAL 1.2.2 **profile**
whose structure is the Baustein itself (full description: `Dokumentation/namespaces/ed23_baustein_props.md`):

- `profile.imports[0]` — the pinned G++ catalog; `with-ids` = **only the G++ controls assigned
  to the Baustein's Anforderungen** (no longer the whole Zielobjektkategorie pool).
- `profile.imports[1]` — present only when the Baustein has NG controls: the shared
  `NG-ergaenzungskatalog.json` next to the profile (back-matter resource with a *relative*
  rlink and the file's SHA-256; resolve relative to the profile URI, refuse on a hash mismatch).
- `profile.merge.combine.method = "use-first"`; `profile.merge.custom.groups` = level groups
  (class `ed23-stufe`) → one group per Anforderung (class `ed23-anforderung`, part `overview`
  with the original text, `insert-controls` with its controls). Consumers that only need the
  control pool can ignore `merge`.
- `profile.modify.alters[]` — one entry per **G++** control (`control-id`); NG controls carry
  no alters. `adds[]` holds, in this order:
  1. *(enhanced variant only)* the maturity block: `position: "ending"`, `by-id` = the
     control's real **statement part id** (the part whose `name == "statement"`, e.g.
     `ARCH.7.1_stm`; controls without one are skipped), `parts[]` = the maturity-level parts;
  2. a props-only block (`position: "ending"`, `props[]` = one `ed23-anforderung` prop per
     assigned Anforderung, remark `Herkunft: …`).

  **Consumers must select the `adds` entry that has `parts`** (not `adds[0]` blindly) — the
  plain variant has only the props block. `Baustein_2_Profile.html` reads `adds[0].parts[0]`,
  which is why the maturity block comes first.
- Metadata props (ns `…/ns/ed23-baustein`): `herkunft` (`BSI` | `NG`), `ed23-baustein`,
  `ed23-baustein-titel`, `zielobjektkategorie`, `ed23-katalog-pin`, `ed23-schicht`. Profiles of
  the 12 NG Bausteine are named `NG_…` and titled `NG …`.
- Maturity texts are reused from `hilfsdateien/ed23_maturity_cache.json` (harvested from the
  previous profiles, also across Bausteine; valid only while the m3 prose equals the control's
  current prose). The model is called only for controls without a cache entry.

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
