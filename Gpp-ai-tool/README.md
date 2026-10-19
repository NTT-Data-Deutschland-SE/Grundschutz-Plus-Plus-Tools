# Gpp-ai-tool

Gpp-ai-tool is a Python-based automation framework designed to facilitate the migration from BSI IT-Grundschutz Edition 2023 (Ed2023) to the modernized Grundschutz++ (G++) methodology using OSCAL 1.2.2 profiles.

The tool uses Gemini 4 Argon on the Gemini Enterprise Agent Platform (or the Developer API) for semantic mapping and for AI-generated enrichment; everything computable is done in code first, the model only judges the residual.

## Key Features

- **Automated Migration (Mapping):** Maps Ed2023 "Bausteine" to G++ "Zielobjekte" and Ed2023 "Anforderungen" to G++ "Kontrollen".
- **AI-Powered Enrichment:** Generates detailed implementation descriptions for maturity levels 1-5 and performs automated classifications (NIST, ISMS, CIA), emitted as OSCAL `alter` blocks on the generated profiles.
- **Multi-Stage Pipeline:** Modular architecture allowing for individual stage execution or full pipeline runs.
- **Upstream Data Sources:** Reference data (BSI Ed2023 catalog, G++ catalog, target-object categories) is fetched from the upstream GitHub repositories at pinned commits with SHA-256 checks.

## Installation

### Prerequisites

- Python 3.12 or higher and [`uv`](https://docs.astral.sh/uv/)
- Either a Google Cloud project with the Gemini Enterprise Agent Platform (ex Vertex AI) enabled and `gcloud auth application-default login`, or a Gemini Developer API key
- Optional: `just` for the task shortcuts in `justfile`

### Setup

```bash
cd Gpp-ai-tool
uv sync            # creates .venv from pyproject.toml / uv.lock (google-genai >= 2.30.1)
cp .env.example .env   # fill in GCP_PROJECT_ID or GEMINI_API_KEY
uv run pytest -q   # offline test suite, no credentials needed
```

## Configuration

The tool is configured via environment variables, read by the typed `Settings` class in `src/config.py` (pydantic-settings). A `.env` file in `Gpp-ai-tool/` or the repository root (both gitignored) is read as well; real environment variables win. Every variable is listed in `.env.example`.

| Variable | Description | Default |
| :--- | :--- | :--- |
| `GCP_PROJECT_ID` | Google Cloud project for the Agent Platform via ADC | one of these two is required |
| `GEMINI_API_KEY` | Gemini Developer API key (AI Studio); no gcloud/ADC needed | one of these two is required |
| `REGION` | Location: `global`, `eu` or `us` (Argon is served on all three) | `global` |
| `GEMINI_MODEL` | The one model id. Cost and quality are set per call by the thinking level, never by a second model | `gemini-4-argon` |
| `MAKER_THINKING_LEVEL` | Thinking level (`low`/`medium`/`high`) of the maker and enrichment calls (candidates, maturity texts) | `medium` |
| `CHECKER_THINKING_LEVEL` | Thinking level of the checker/verifier calls and of judgment-heavy mapping (prozessbausteine); on Argon `high` buys little over `medium` and triples the wall-clock | `medium` |
| `MAX_OUTPUT_TOKENS` | Output budget per call, thinking tokens included (>= 32768; above 65536 the SDK runs long decode) | `65536` |
| `MAX_CONCURRENT_AI_REQUESTS` | Size of the parallel call pool (lower it on persistent 429s; 20 is fine on Argon pay-as-you-go and cuts the checker phase to a quarter) | `5` |
| `API_MAX_RETRIES` | Retries per call for transient errors and schema violations together (max 5) | `5` |
| `TEST` | `true`: a few items per stage, no credentials needed | `false` |
| `OVERWRITE_TEMP_FILES` | `true`: regenerate existing outputs (CLI alias `--fresh`) | `false` |
| `LOG_LEVEL` | `DEBUG` shows every backend call (httpx/httpcore, urllib3); read at process start | `INFO` |
| `URL_FETCH_TIMEOUT_SECONDS` / `URL_FETCH_RETRIES` | Remote source downloads (process environment only, not `.env`) | `30` / `3` |
| `GPP_CATALOG_PIN_COMMIT` / `GPP_CATALOG_PIN_SHA256` | Pinned G++ catalog commit and its SHA-256 (defaults in `src/constants.py`; change both together; process environment only, not `.env`) | see constants |
| `ED23_CATALOG_PIN_COMMIT` / `ED23_BD_CATALOG_PIN_SHA256` / `ED23_PLAIN_CATALOG_PIN_SHA256` | Pinned ED23 catalog commit (NTT DATA DACH edition) and the SHA-256 of its two files (process environment only, not `.env`) | see constants |
| `ED23_BAUSTEIN_ABGLEICH_BATCH_SIZE` | Anforderungen per maker call in `stage_ed23_baustein_abgleich` | `5` |
| `ED23_MATURITY_REUSE_ACROSS_BAUSTEINE` / `ED23_MATURITY_REGENERATE` | Reuse harvested maturity texts of another Baustein / force regeneration | `true` / `false` |
| `OUTPUT_ROOT` | Root directory for generated artifacts | repository root |
| `SDT_HELPER_OUTPUT_DIR` / `SDT_PROFILES_REGULAR_DIR` / `SDT_PROFILES_PROCESS_DIR` / `ED23_PROFILES_DIR` | Override individual output directories | under `OUTPUT_ROOT` |

> **Note:** The pipeline fetches input catalogs from GitHub at pinned commits and writes generated artifacts to local directories (`hilfsdateien/`, `Zielobjektkategorien/profile/`, `ED23-Baustein-profile/`) relative to the repository root. There is no explicit context cache any more (none exists on the current model generation): corpus-grounded stages put the corpus first and the varying item last, so the repeated prefix is cached implicitly. Debugging a failing call: `LOG_LEVEL=DEBUG` shows the real project/location/model in the request URL and the status code (403 = IAM/model access, 404 = wrong model, 429/5xx = transient).

## Usage

### Local Execution

Use the provided helper script to run the pipeline locally:

```bash
./scripts/run_local.sh --stage <stage_name>     # or: just dev --stage <stage_name>
```

To run the full pipeline, omit the stage argument:
```bash
./scripts/run_local.sh
```

`uv run python src/main.py --version` prints the build; `just test`, `just lint` and `just gemini-lint` run the offline tests, ruff and the Gemini migration lint.

### Data Sources (Inputs)

All input data is fetched from GitHub at runtime (see `src/constants.py`), always at a **pinned commit** and verified against a pinned **SHA-256** (Handbuch 3.13/3.14, Katalogarbeit-Skill Grundregel 8); a hash mismatch aborts the stage.

- **G++ catalog** — the Grundschutz++ Anwenderkatalog (the target catalog of the migration), `GPP_CATALOG_PIN_COMMIT` / `GPP_CATALOG_PIN_SHA256`. The generated OSCAL profiles carry the same pin in their back-matter (fragment import → resource with commit-pinned rlink + hash). A catalog update is a conscious pin change: update both values in `src/constants.py`, re-run `scripts/pin_profile_imports.py` over the profile directories, and commit both together.
- **BSI Ed2023 catalog** — the benutzerdefinierte OSCAL edition of NTT DATA DACH at `ED23_CATALOG_PIN_COMMIT`, two files with their own hashes: `BSI_GS_OSCAL_current_2023_benutzerdefinierte.json` (111 BSI-Bausteine plus 12 nutzergenerierte **NG**-Bausteine) and `BSI_GS_OSCAL_current_2023.json` (the 111 BSI-Bausteine only). The catalog carries no marker for the NTT-own Bausteine — **NG = benutzerdefinierte − plain** (`utils/ed23_baustein.detect_ng`). The official XML Kompendium (`utils/ed23_xml.py`, sha256-pinned) supplies the amtliche wording of BSI Anforderungen.
- **BSI GSMap** (ITGS 2023 → GS++, `ITGS_PIN_COMMIT`) — the official bridge, used as a deterministic source by `stage_ed23_baustein_abgleich` (optional: the stage continues without it when the download fails).
- **`target_object_categories.csv`** — the Zielobjektkategorien (UUID, name, and hierarchy via `ChildOfUUID`), read from the same commit as the G++ catalog.

### Herkunft: BSI vs. NG

Everything that is not from the BSI is marked **NG** ("Nutzergenerierte Inhalte") in id, title and props: NG controls are `NG-<AnforderungsID>` with title `NG: …` and live only in the shared `ED23-Baustein-profile/DE/NG-ergaenzungskatalog.json`; profiles of the 12 NG Bausteine are named `NG_…` and titled `NG …`; every profile and the catalog carry the metadata prop `herkunft` (`BSI` | `NG`) in the namespace `…/ns/ed23-baustein`, and every control assignment names its source in a `Herkunft: …` remark. The whole scheme is documented in `Dokumentation/namespaces/ed23_baustein_props.md`.

### Available Pipeline Stages

You can run specific stages using the `--stage` argument. The full pipeline runs them in the order below. Stage 1 is deterministic prep/mapping, stage 2 the AI-driven Baustein→Zielobjekt match, stage 3 the Zielobjektkategorie profiles, stages 4–5 the ED2023 cross-mappings, stage 6 the per-Anforderung abgleich, stage 7 the NG catalog, stages 8–9 the enriched profiles.

| # | Stage | AI? | What it does |
|---|---|---|---|
| 1 | `stage_gpp` | No | Deterministic mapping: walks the G++ catalog and the Zielobjektkategorien CSV (including the parent hierarchy) to compute, for each Zielobjekt, the set of applicable G++ controls. Writes `hilfsdateien/zielobjekt_controls.json`. |
| 2 | `stage_match_bausteine` | **Yes** (thinking low) | For each BSI Baustein that gets a profile (system layers plus `ALLOWED_PROCESS_BAUSTEINE`: the 3 OPS Bausteine, the 3 NG process Bausteine, the 7 process Bausteine without a GS++ Praktik), asks the model which G++ Zielobjekt it corresponds to. **Incremental**: only Bausteine missing from `hilfsdateien/baustein_zielobjekt.json` are queried; stale entries are dropped. |
| 3 | `stage_profiles` | No | Generates the **base OSCAL profiles** — one per Zielobjekt — each importing the G++ catalog and including **all** of that Zielobjektkategorie's controls. Output is split into `Zielobjektkategorien/profile/regular/` and `…/process/` (Methodik and `*_prozesse`). |
| 4 | `stage_ed23_anforderungen` | **Yes** | For every G++ control, finds the **precisely** matching BSI ED2023 Anforderungen via a **maker-checker** design: a generous candidate pass (`MAKER_THINKING_LEVEL`, the stripped ED2023 corpus as the stable prompt prefix) followed by a strict per-candidate verification pass (`CHECKER_THINKING_LEVEL`, self-contained prompt). Every verified match names the **Teilanforderung** it rests on (numbered ED23 sentence); IDs and sentence numbers are validated against the real catalog. Writes the OSCAL mapping collection `hilfsdateien/gpp_ed23_anforderungen.json`. |
| 5 | `stage_prozessbausteine` | **Yes** (thinking high) | The inverse direction, 1:1: maps **every** Anforderung of the process-oriented ED2023 layers (ISMS, ORP, CON, OPS, DER) to its single best G++ control, grounded on the full G++ catalog as prompt prefix. Runs in rounds until every Anforderung is mapped. Writes `hilfsdateien/prozessbausteine_mapping.json`. Completeness-driven, so it is **not** a gap measure. |
| 6 | `stage_ed23_baustein_abgleich` | **Yes** (maker-checker) | Per Anforderung of every Baustein in the map: first the deterministic sources (inverted stage-4 mapping, `ed23_satz_abdeckung.json`, GSMap, stage-5 mapping), then — only for Anforderungen without a covering source (a stage-5 hit alone does not count) — a maker call per batch of one Baustein's Anforderungen (assignments to G++ controls and/or one proposed new control, deterministic post-checks) and a checker call per proposal. A new control proposed next to assignments is kept as the checker's fallback: it is dropped once an assignment survives the checker, and stands when the checker rejects every assignment. Resumable (`.partial`). Writes `hilfsdateien/ed23_baustein_abgleich.json`. Anforderungen left without a control after the checker (`ohne_control.art = abgelehnt-durch-checker`) can be sent through maker and checker once more with `uv run python scripts/nachfass_abgleich.py --write` followed by a normal re-run of the stage. |
| 7 | `stage_ng_katalog` | No | Builds the one shared **NG Ergänzungskatalog** `ED23-Baustein-profile/DE/NG-ergaenzungskatalog.json` from the proposed new controls of stage 6 (layer → Baustein, `NG-<AnforderungsID>`, class `ng-ergaenzung`, `herkunft=NG`). Written only when its content changes, so the hash the profiles embed stays stable. |
| 8 | `stage_ED23_profiles_enhanced` | **Yes** (only for controls without cached maturity texts) | Per Baustein a plain and an `_enhanced` profile in the Mindeststandard pattern: the Anforderungen as `merge.custom` groups with the original text and `insert-controls`, two imports (pinned G++ catalog, NG catalog with relative rlink + SHA-256), `combine use-first`, provenance props per assignment, and in `_enhanced` the maturity parts (levels 1–5) reused from `hilfsdateien/ed23_maturity_cache.json`. Files are written only when they change. See `docs/profile-maturity-contract.md`. |
| 9 | `stage_base_process_enhanced` | **Yes** | Enriches the process profiles (`Zielobjektkategorien/profile/process/`) with maturity sub-statements plus classifications as `alter` blocks, writing `*_enhanced.json` next to each base process profile. |
| — | `stage_ed23_relationen` | **Yes** | Classification pass over the existing `gpp_ed23_anforderungen.json`: assigns every verified (G++ control, ED23 Anforderung) pair a differentiated OSCAL `relationship` instead of the constant `intersects-with`. Rewrites the file in place. Not part of the full pipeline; run explicitly. |
| — | `stage_ed23_satz_abdeckung` | **Yes** | Per-sentence coverage judgment of the **official** ED23 Kompendium: for every normative sentence of every active Anforderung, a maker-checker pass judges which G++ controls demand the same activity. Writes `hilfsdateien/ed23_satz_abdeckung.json` (no Kompendium prose is serialized). Not part of the full pipeline; run explicitly. Basis of `scripts/prozess_luecken.py`. |

#### Data flow

```
catalogs + CSV (GitHub, pinned)
        │
  1 gpp   ──► zielobjekt_controls.json        (Zielobjekt → all G++ controls)    [deterministic]
  2 match_bausteine ──► baustein_zielobjekt.json    (Baustein → Zielobjekt, incremental)   [AI]
  3 profiles ──► base profiles (import G++ catalog, all controls)   Zielobjektkategorien/profile/{regular,process}/
        │
  4 ed23_anforderungen ──► gpp_ed23_anforderungen.json   (G++ control → ED23 Anforderungen, 1:n)   [AI, maker+checker]
  5 prozessbausteine  ──► prozessbausteine_mapping.json  (ED23 Anforderung → G++ control, 1:1)     [AI]
        │
  6 ed23_baustein_abgleich ──► ed23_baustein_abgleich.json  (Anforderung → controls | NG control)  [deterministic first, AI residual]
  7 ng_katalog ──► ED23-Baustein-profile/DE/NG-ergaenzungskatalog.json                              [deterministic]
  8 ED23_profiles_enhanced ──► ED23-Baustein-profile/DE/<kat>_<ID>_<titel>[_enhanced].json       [deterministic + cached maturity AI]
  9 base_process_enhanced ──► enriched process profiles (*_enhanced.json)   …/profile/process/   [AI]
```

Verification: `python -I ../ED23-Baustein-profile/pruefe_export.py ../ED23-Baustein-profile/DE` (schema, imports, NG hash, control-only-once), `python scripts/check_pins.py` (pins against upstream), `python scripts/prozess_luecken.py` (which process Bausteine lack a GS++ carrier).

### Running a single stage locally

To (re)generate the G++ Zielobjektkategorien and process profiles locally:

```bash
./scripts/run_local.sh --stage stage_profiles
```

To regenerate the ED23-Baustein profiles after a catalog or mapping change (steps 6–8; each is resumable and idempotent):

```bash
./scripts/run_local.sh --stage stage_match_bausteine          # only Bausteine missing from the map
./scripts/run_local.sh --stage stage_ed23_baustein_abgleich   # deterministic sources + maker-checker residual
./scripts/run_local.sh --stage stage_ng_katalog
./scripts/run_local.sh --stage stage_ED23_profiles_enhanced   # maturity texts from the cache, model only for the rest
```

The same pattern works for any stage name listed above. By default `OVERWRITE_TEMP_FILES` is `false`, so stages reuse existing outputs — a re-run only fills the gaps and rewrites only files whose content changed. `--fresh` (or `OVERWRITE_TEMP_FILES=true`) starts over; `--clear-all` first harvests the maturity texts of the existing profiles into `hilfsdateien/ed23_maturity_cache.json` and then wipes the generated output directories (the AI caches `ed23_maturity_cache.json` and `ed23_baustein_abgleich.json` survive; `--clear-ai-cache` removes them explicitly).

## Deployment

The tool is designed to run as a Google Cloud Run Job. Use the deployment script:

```bash
./scripts/deploy.sh <GCP_PROJECT_ID> <GCP_REGION>
```

## How-To / Workflow

1.  **Preparation:** No manual upload is required — the source BSI Ed2023 catalog, the G++ catalog, and the target-object categories are fetched directly from their upstream GitHub repositories at pinned commits (see `src/constants.py`).
2.  **Mapping:** The tool establishes, per Zielobjektkategorie, the set of applicable G++ controls (deterministic), matches each Baustein to a Zielobjekt (AI) and maps G++ controls and ED23 Anforderungen in both directions (AI, maker-checker).
3.  **Abgleich:** For every Anforderung of a Baustein it collects the G++ controls that carry it from the existing mappings and sends only the uncovered rest to the model, which assigns controls or proposes one NG control, judged by a checker.
4.  **NG catalog and profiles:** The proposed controls become the shared NG Ergänzungskatalog; every Baustein becomes a plain and an enhanced profile with its Anforderungen as groups, the pinned G++ catalog and the NG catalog as imports, and (enhanced) the maturity-level descriptions, reused from the cache wherever possible.
5.  **Finalization:** The tool outputs valid OSCAL 1.2.2 profiles ready for the G++ tools; `ED23-Baustein-profile/pruefe_export.py` checks them.

---

For more technical details, refer to [G++ Automatisierte Erstellung Zielobjekte-Bausteine.md](./G++%20Automatisierte%20Erstellung%20Zielobjekte-Bausteine.md).
