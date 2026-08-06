# Code Review Issues and Recommendations

This document outlines issues identified during the end-to-end review of the OSCAL
generation pipeline (`Gpp-ai-tool`) **and** its downstream consumers (`GS++-oscal-app`),
categorized by severity.

> **Status (branch `fix/oscal-issues`):** Most items are resolved and marked
> **✅ RESOLVED** inline (some with a smaller follow-up noted). The two still **OPEN** items
> — 2.1 (AI "slop") and 3.6 (single-step AI generation) — both concern AI-generation
> behaviour that cannot be runtime-verified without live Gemini/Vertex AI access, so they are
> left documented with concrete recommendations rather than changed blind. Issue 1.1
> (temperature) was closed as not-an-issue (intentional for Gemini). Every resolved item was
> verified (unit/structural checks, the live G++ catalog, or a headless browser preview).

> **Note on history:** The 1:1 Anforderung→Control mapping stage (`stage_matching`) was
> removed; an ED2023 profile now includes **all** controls of the matched
> Zielobjektkategorie and is enriched per Baustein. The enhancement stage is
> `stage_ED23_profiles_enhanced.py` (formerly `stage_profiles_enhanced.py`, originally
> `stage_component.py`); it enriches profiles with OSCAL `alter` blocks driven by best
> practices and the Baustein description. A parallel stage,
> `stage_base_process_enhanced.py`, enriches the process profiles.

## 0. Verified OK — the profile `alter`/`adds` mechanism is OSCAL-conformant

The migration away from component-definitions is **correct**. Enrichment is injected via
`profile.modify.alters[].adds[]` using:
- `position: "ending"` with `by-id: "{control_id}_stm"`, which makes the maturity parts
  **children** of the control's statement part;
- `parts[].name == "statement"` and unique part ids `"{control_id}-m{1..5}_custom"`.

This was validated against the live G++ catalog
(`…/Grundschutz%2B%2B/Grundschutz%2B%2B-catalog.json`): every Anforderung has a
`"{control_id}_stm"` statement part (998 `_stm` parts; e.g. `ARCH.7.1_stm`), so all `by-id`
anchors resolve and the generated profiles are structurally OSCAL 1.2.2-conformant. This
correctly solves the original problem (OSCAL does not allow creating new statements inside a
component-definition's `implemented-requirements`). The remaining items below are quality,
interoperability, and reliability concerns — not a regression of the refactor.

## 1. Critical Issues

*None currently open.*

> **Resolved / not-an-issue — `API_TEMPERATURE = 1`:** Deliberately kept at 1. Gemini is
> tuned to perform well at this temperature, and the structured-output schema constrains the
> JSON shape, so the earlier "deterministic tasks need low temperature" concern does not
> apply here.

## 2. High Priority Issues

### 2.1. High Risk of "AI Slop" in Enhanced Profiles — OPEN (inherent; partially mitigated)
**Location:** `src/pipeline/stage_ED23_profiles_enhanced.py`, `src/assets/json/prompt_config.json`
**Description:** The enhanced-profile stage relies on AI to generate the prose (statement,
guidance, assessment) for maturity levels 1, 2, 4, and 5 for *every* control. This carries an
inherent risk of generic, vague, or hallucinated guidance that needs human review.
**Already mitigated by this branch:** Level 3 (the baseline) is now injected verbatim, not
AI-copied (2.2); the schema no longer forces invented levels (4.5); and a structural
validator gates the output (3.3).
**Remaining recommendation (needs live Gemini to validate, so not done here):** add a
deterministic post-generation "slop" gate — flag near-duplicate adjacent levels, empty or
placeholder prose, and commercial-product-name leaks (prompt Rule E) — and keep a
human-in-the-loop review step. This is partly inherent to AI generation and cannot be fully
eliminated in code.

### 2.2. AI Reliability for Baseline (Level 3) Content — ✅ RESOLVED
**Location:** `src/pipeline/stage_ED23_profiles_enhanced.py`, `src/pipeline/stage_base_process_enhanced.py` (`build_oscal_maturity_statements`)
**Was:** The prompt told the AI to use an *exact copy* of the input prose for Level 3 ("You
do not change a single character"); relying on the model to copy perfectly risked altered
formatting or variable definitions.
**Fix:** `build_oscal_maturity_statements` now sets the Level 3 statement deterministically
from `original_description` (the verbatim G++ prose already in scope), ignoring the AI's
copy; it falls back to the AI value only if no original prose exists. Applied identically in
both enhancement stages and covered by an isolated function test (L3 == original prose,
other levels still AI-generated, guard edge-cases hold).

### 2.3. Inconsistent Profile Consumption in GS++-oscal-app — ✅ RESOLVED
**Location:** `GS++-oscal-app/GSpp-Viewer.html` (and the documented contract)
**Re-assessment:** The original framing was partly overstated. Of the three "imports-only"
apps, two **should** read only control IDs by design: `ssp_generator.html` *generates* an SSP
that references the profile (the maturity is consumed downstream in `ssp_ausfuellen.html`),
and `Baustein_2_Profile.html` *authors* a profile. `GSpp-Viewer.html` was the one genuine gap
— a catalog viewer that ignored the maturity in an enhanced profile.
**Fix:** `GSpp-Viewer.html` now parses `modify.alters[].adds[].parts` (new prose+nested-parts
shape with old-props fallback, per the contract) into `activeProfileMaturity`, and renders a
collapsible "Reifegrade (ED2023)" box per control (`renderMaturity` /
`refreshMaturityDisplay`) showing the m1–m5 statement plus guidance/assessment. The two
maturity-displaying apps (`pruefung_ap_ar.html`, `ssp_ausfuellen.html`) were already updated
in the 3.1 work. **Verified live** (headless preview): loading the G++ catalog + an enhanced
profile renders 70 maturity boxes; ARCH.7.1 shows all five distinct levels with guidance
("Hinweis") and assessment ("Prüfung").
**Still open (low):** the parser is now duplicated across three apps; extracting one shared
helper would be cleaner, but each app is a standalone single-file tool, so the contract doc
(3.9) is the pragmatic single source of truth for now.

### 2.4. Apps Do Not Resolve the Imported Catalog — ✅ RESOLVED (re-assessed)
**Location:** `GS++-oscal-app/{pruefung_ap_ar,ssp_ausfuellen,GSpp-Viewer}.html`
**Re-assessment:** Also overstated. Every app that actually **displays** control content
already resolves a catalog: `pruefung_ap_ar.html` fetches the G++ catalog (`CATALOG_URL`,
building a `cid → {title, prose}` map); `ssp_ausfuellen.html` follows `import-profile.href` →
the profile's `imports[].href` → `processCatalogData` (building `catalogControlMap` /
`catalogParamMap`); and `GSpp-Viewer.html` is catalog-first (it loads the full catalog and
uses the profile only as an ID filter). The apps that *don't* fetch the catalog
(`ssp_generator.html`, `Baustein_2_Profile.html`) only need IDs.
**Outcome:** No code change required for the display apps beyond 2.3; the premise "most apps
never fetch the catalog" did not hold on inspection. Documented here so it isn't re-litigated.

## 3. Medium Priority Issues

### 3.1. Primary Maturity Content Hidden in Custom `props` Instead of `prose` — ✅ RESOLVED
**Location:** both `stage_*_enhanced.py` (`build_oscal_maturity_statements`), `scripts/migrate_maturity_parts_to_prose.py`, `GS++-oscal-app/{pruefung_ap_ar,ssp_ausfuellen}.html`
**Was:** Each maturity part's `prose` was the *original* control description (identical for
all five levels, prefixed `(BSI Baustein X)`), while the real per-level text sat in custom
props (`statement`, `guidance`, `assessment-method`). A generic OSCAL renderer shows
`part.prose` and would display the same duplicated text for m1–m5, missing the real content.
**Fix (pipeline):** `build_oscal_maturity_statements` now puts the per-level statement in
`part.prose` and models guidance/assessment as nested parts (`name: "guidance"` /
`"assessment"`, ids `…_gdn` / `…_asm`). Only classification + `label` remain as props.
**Fix (existing artifacts):** added a deterministic, idempotent migration
(`scripts/migrate_maturity_parts_to_prose.py`) and ran it over the 116 generated profiles —
34,444 parts converted, 0 parse failures, 0 residual prose-props.
**Fix (consumers):** the two prop-reading apps now read `prose` + nested parts first and fall
back to the old props for legacy profiles. Verified end-to-end: both parsers extract the real
per-level statement/guidance/assessment from a migrated profile and agree with each other,
and the old-shape fallback still works.

### 3.2. Duplicated Prose Across All Five Maturity Parts — ✅ RESOLVED (by 3.1)
**Was:** The same `enriched_prose` string was written into all five maturity parts of a
control.
**Fix:** Each part's `prose` is now its own distinct per-level statement, so the duplication
is gone (resolved together with 3.1).

### 3.3. OSCAL Validation Never Ran — ✅ RESOLVED (structural validation wired in); full-schema validation still open
**Location:** `src/utils/oscal_utils.py` (`validate_enhanced_profile_structure`), both `stage_*_enhanced.py`, `src/constants.py`
**Was:** Generated profiles were never validated. `validate_oscal()` existed but was never
called; the only OSCAL schema path (`OSCAL_COMPONENT_SCHEMA_PATH`) pointed at a *component*
schema that isn't even in the repo; and `validate_oscal` strips the `TokenDatatype` pattern,
weakening validation.
**Fix:** Added `validate_enhanced_profile_structure(profile)` — a focused structural
validator checking the invariants the `alters`/`adds` mechanism and the apps rely on
(required top-level fields, each alter has a control-id + adds, each add has a valid
`position` and a `by-id`, each added part is a `statement` with an id and non-empty prose,
all part ids unique). Both enhancement stages now run it before writing (warn-only, so one
glitch doesn't abort a batch). Removed the dead, misleading `OSCAL_COMPONENT_SCHEMA_PATH`
constant. Verified: the validator catches injected uuid/position/by-id/prose/duplicate-id
defects, and **all 116 generated profiles pass clean (0 problems)**.
**Still open (medium):** validation against the *full* OSCAL 1.2.2 profile JSON schema
(would need the schema bundled and the `TokenDatatype`/Unicode-regex limitation addressed,
e.g. via the `regex` module). The structural validator covers the pipeline-specific
invariants in the meantime.

### 3.4. `by-id` Anchor Assumed but Not Validated — ✅ RESOLVED
**Location:** `src/utils/oscal_utils.py` (`extract_all_gpp_controls`, `_find_statement_part_id`), both `stage_*_enhanced.py`
**Was:** `by-id: f"{gpp_control_id}_stm"` was emitted without checking the imported catalog.
The convention holds for Anforderungen, but any included control lacking a `_stm` statement
part (e.g. ISMS/container controls) would produce an unresolvable `adds`.
**Fix:** `extract_all_gpp_controls` now records each control's real `statement_part_id` (the
id of the part whose `name == "statement"`) and sources the baseline prose from that part.
Both stages use that id for `by-id` and **skip + log** any control with no statement part
instead of emitting a broken anchor. Verified against the live G++ catalog: all 651 controls
resolve to their `_stm` part (0 broken), so the change is behaviour-preserving today while
robust against non-conforming controls.

### 3.5. Non-Portable Output Paths — ✅ RESOLVED
**Location:** `src/constants.py`, `README.md`
**Was:** Output paths were built only from `REPO_ROOT` with hardcoded relative segments, so
placement broke if the surrounding directory layout changed or the tool was deployed
elsewhere.
**Fix:** Added an `OUTPUT_ROOT` env var (defaults to `REPO_ROOT`) that relocates all
generated artifacts at once, plus per-directory overrides (`SDT_HELPER_OUTPUT_DIR`,
`SDT_PROFILES_REGULAR_DIR`, `SDT_PROFILES_PROCESS_DIR`, `ED23_PROFILES_DIR`) that take
precedence. Defaults are unchanged, so existing runs behave identically. Documented in the
README env-var table. Verified: defaults unchanged, `OUTPUT_ROOT` moves everything, and a
per-dir override beats `OUTPUT_ROOT`.

### 3.6. Ambitious Single-Step AI Generation — OPEN (needs live-AI validation)
**Location:** `src/pipeline/stage_ED23_profiles_enhanced.py`, `src/assets/json/prompt_config.json`
**Description:** The AI generates the per-level prose (now 4 levels × statement/guidance/
assessment after 2.2) **and** classifies the control (class, ISMS phase, CIA) in a single
request. Combining complex generation with classification can lower quality in both.
**Recommendation (deferred):** split into two passes — a cheap, low-temperature
classification call and a separate prose call — or run classification deterministically where
possible. **Not done here** because the quality impact can only be judged against live Gemini
output, which isn't available in this environment; doing it blind would risk a regression
with no way to verify. Tracked for a follow-up with Vertex AI access.

### 3.7. Dead Google Cloud Storage Configuration — ✅ RESOLVED (config + dependency); `gcs_uris` param still open
**Location:** `src/config.py`, `src/requirements.txt`, `README.md`
**Was:** `BUCKET_NAME`, `SOURCE_PREFIX`, and `OUTPUT_PREFIX` were validated as **required** at
startup (the app refused to start without them unless `TEST=true`) but no code read them; the
`google-cloud-storage` dependency was never imported. New users had to invent dummy values.
**Fix:** Removed the three dead config fields and their startup validation — only
`GCP_PROJECT_ID` is now required (region defaults to `global`; `AI_ENDPOINT_ID` is optional).
Dropped `google-cloud-storage` from `requirements.txt` and updated the README env-var table.
Verified config now starts with just `GCP_PROJECT_ID` and the missing-var error names only it.
**Still open (low):** the unused `gcs_uris` parameter on
`AiClient.generate_validated_json_response` (never passed) — left for the same future sweep
as the other dead-code items.

### 3.8. No Timeout on Remote Data Fetch — ✅ RESOLVED (timeout + retry); offline fallback still open
**Location:** `src/utils/file_utils.py` (`read_source_text`)
**Was:** Input catalogs were downloaded with `urllib.request.urlopen(path)` with no
`timeout=`, so a network hang could block the entire pipeline indefinitely.
**Fix:** `read_source_text` now passes an explicit `timeout=URL_FETCH_TIMEOUT_SECONDS`
(default 30s) and retries with linear backoff (`URL_FETCH_RETRIES`, default 3), re-raising
the last error after exhausting attempts. All three are env-configurable
(`URL_FETCH_TIMEOUT_SECONDS`, `URL_FETCH_RETRIES`, `URL_FETCH_BACKOFF_SECONDS`). Verified
with a mocked `urlopen` (timeout forwarded, retries exhaust then raise, recovery on a later
attempt, local-file path unaffected).
**Still open (lower priority):** no cached **local fallback** if an upstream file is
renamed/moved — a 404 is still a hard failure. Consider bundling a last-known-good copy.

### 3.9. Undocumented Pipeline ↔ App Contract — ✅ RESOLVED (documented); automated roundtrip test still open
**Location:** `docs/profile-maturity-contract.md`, both `stage_*_enhanced.py`, `GS++-oscal-app/*.html`
**Was:** The structure the apps depend on (prop names, part names, `by-id` convention,
namespace, which text lives in prose vs props) was an implicit contract with no shared
documentation — a rename on either side broke consumption silently.
**Fix:** Added `docs/profile-maturity-contract.md` as the single source of truth: it
specifies the current prose+nested-parts shape, the metadata props, the `by-id`/statement
convention, a consumer reading recipe, the legacy-fallback shape, and a change-discipline
checklist that names every file to update together.
**Still open (low):** an *automated* roundtrip test (profile produced by
`Baustein_2_Profile.html` → consumed by `ssp_ausfuellen.html`) — manual Python replicas of
both parsers were verified during the 3.1 work, but a committed test harness would be nicer.

## 4. Low Priority Issues

### 4.1. Model Naming Conventions — ✅ RESOLVED (made configurable)
**Location:** `src/constants.py`, `README.md`
**Was:** Model names (`gemini-3-flash-preview`, `gemini-3.1-pro-preview`) were hardcoded
preview identifiers, so pinning a stable/versioned id required a code edit.
**Fix:** `GROUND_TRUTH_MODEL` and `GROUND_TRUTH_MODEL_PRO` are now env-overridable (defaults
unchanged), so a stable Vertex AI model id can be pinned via environment without touching
code. The current preview defaults are intentional until stable ids are published.

### 4.2. Manual Retry Implementation vs. Tenacity — ✅ RESOLVED (dependency removed)
**Location:** `src/clients/ai_client.py`, `src/requirements.txt`
**Was:** `tenacity` was listed in requirements but never imported; a manual async retry loop
is used instead.
**Fix:** Dropped the unused `tenacity` dependency. The existing retry loop in
`generate_validated_json_response` is intentionally kept — it is well-instrumented
(per-exception-type logging, exponential backoff, a clear non-retryable fallthrough) and a
`tenacity` rewrite could not be exercised here without the live `google-genai` SDK, so
removing the dead dependency is the lower-risk resolution the issue allowed for.

### 4.3. Dead Code from Removed `stage_matching` — ✅ RESOLVED
**Location:** `src/utils/data_parser.py`
**Was:** `parse_zielobjekte_hierarchy` and `parse_bsi_2023_controls` were no longer called by
any stage (no callers, no tests).
**Fix:** Both functions removed. (Note: `parse_gpp_kompendium_controls` and `filter_markdown`
also appear to have no callers but are intentionally left for now — `parse_gpp_kompendium_controls`
still has a unit test; revisit as a separate dead-code sweep.)

### 4.4. Dead Patch Scripts — ✅ RESOLVED
**Location:** `src/patch_main.py`, `src/patch_processing.py`
**Was:** One-shot scripts that string-replaced `main.py` / `pipeline/processing.py` to add
`stage_base_process_enhanced`; the edits were already applied to the live files, so the
scripts were dead code (and re-running them would corrupt the files).
**Fix:** Both patch scripts deleted.

### 4.5. Response Schema Forced All 5 Levels, Contradicting the Prompt — ✅ RESOLVED
**Location:** `src/assets/schemas/enhanced_control_response_schema.json`, `src/pipeline/stage_*_enhanced.py` (`process_chunk` prompt)
**Was:** The response schema marked **all 21 fields** as `required` — every
`level_{1..5}_{statement,guidance,assessment}` plus the classification fields. But the prompt
told the model to "only create prose for a level if a technically sound and distinct
implementation can be described." The conflict forced the model to invent levels (or the
whole 10-control chunk was discarded on a `ValidationError` in `process_chunk`).
**Fix:** `required` now lists only `id`, `class`, `phase`, `effective_on_c/i/a`; the
`level_*` fields are optional (the builder already guards each with `if statement_text`).
The inline chunk prompt now tells the model to produce levels 1, 2, 4, 5 and that Level 3 is
injected automatically (it may omit `level_3_*`), removing the misleading "exact copy"
instruction. This eliminates the chunk-discard data-loss path and dovetails with 2.2.

### 4.6. Leftover Component-Definition Wording in Apps — ✅ RESOLVED
**Location:** `GS++-oscal-app/ssp_ausfuellen.html`, `ssp_generator.html`
**Was:** After the migration the function `processComponentDefinitions()`, the
`componentDefinitions` map, and several "Komponentendefinition" comments/labels remained
even though the apps now consume profiles.
**Fix:** Renamed `processComponentDefinitions` → `processProfiles` and `componentDefinitions`
→ `loadedProfiles` in `ssp_ausfuellen.html`, and updated the stale "Komponentendefinition"
strings/comments in both apps to "Profil". The two remaining "Komponenten" references denote
genuine OSCAL SSP components and are correct.

### 4.7. `effective_on_*` Props Superseded by BSI Schutzziel Props — ✅ RESOLVED (2026-08-01)
**Location:** both `stage_*_enhanced.py`, `enhanced_control_response_schema.json`,
`prompt_config.json`, all 95 generated `*_enhanced.json`, `ssp_ausfuellen.html`
**Was:** The enhancement stages asked the AI to estimate CIA impact per maturity statement
(`effective_on_c/i/a`, high/medium/low). Since 2026-07-03 the BSI SdT catalog carries
authoritative control-level Schutzziel props (`confidentiality`, `integrity`, `availability`,
`authenticity`, values 0–2, ns `…/documentation/namespaces/security_targets.csv`) —
our AI-estimated props duplicated (and could contradict) them. Decision: SdT is
authoritative; redundant G++ props are removed.
**Fix:** Removed `effective_on_*` from the response schema (`required` now `id`, `class`,
`phase`), prompt Rule F, and both `build_oscal_maturity_statements` implementations;
`stage_base_process_enhanced` now uses `GPP_ENHANCEMENT_PROPS_NS` (was: hardcoded stale BSI
ns — closes the generator ns divergence). One-time idempotent migration
`scripts/migrate_remove_effective_on_props.py` stripped the props from all 95 generated
profiles (33,438 parts) and normalized `control_class`/`phase` ns. `ssp_ausfuellen.html`
renders Schutzziel badges from the catalog props instead (value 0 hidden, value 2
highlighted). Docs updated: `gpp_enhancement_props.md`, `profile-maturity-contract.md`.
