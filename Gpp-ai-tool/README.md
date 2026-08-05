# Gpp-ai-tool

Gpp-ai-tool is a Python-based automation framework designed to facilitate the migration from BSI IT-Grundschutz Edition 2023 (Ed2023) to the modernized Grundschutz++ (G++) methodology using OSCAL 1.2.2 profiles.

The tool leverages Google Vertex AI (Gemini) to perform semantic mapping and enrich OSCAL components with AI-generated implementation details.

## Key Features

- **Automated Migration (Mapping):** Maps Ed2023 "Bausteine" to G++ "Zielobjekte" and Ed2023 "Anforderungen" to G++ "Kontrollen".
- **AI-Powered Enrichment:** Generates detailed implementation descriptions for maturity levels 1-5 and performs automated classifications (NIST, ISMS, CIA), emitted as OSCAL `alter` blocks on the generated profiles.
- **Multi-Stage Pipeline:** Modular architecture allowing for individual stage execution or full pipeline runs.
- **Upstream Data Sources:** Reference data (BSI Ed2023 catalog, G++ catalog, target-object categories) is fetched directly from the upstream GitHub repositories; AI enrichment runs on Google Vertex AI (Gemini).

## Installation

### Prerequisites

- Python 3.9 or higher
- Access to a Google Cloud Project with Vertex AI and Cloud Storage enabled
- `gcloud` CLI installed and authenticated

### Setup

1.  **Clone the repository and navigate to the project directory:**
    ```bash
    cd Gpp-ai-tool
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r src/requirements.txt
    ```

## Configuration

The tool is configured via environment variables. Create a `.env` file or export them in your shell:

| Variable | Description | Required |
| :--- | :--- | :--- |
| `GCP_PROJECT_ID` | Your Google Cloud Project ID (for Vertex AI / Gemini) | Yes |
| `REGION` | GCP Region (default: `global`) | No |
| `AI_ENDPOINT_ID` | Optional Vertex AI endpoint/model override (model id otherwise comes from `constants.GROUND_TRUTH_MODEL`) | No |
| `GROUND_TRUTH_MODEL` / `GROUND_TRUTH_MODEL_PRO` | Override the default Gemini model ids (default: current preview ids) | No |
| `TEST` | Set to `true` for test mode (default: `false`) | No |
| `MAX_CONCURRENT_AI_REQUESTS` | Limit parallel AI calls (default: `5`) | No |
| `OVERWRITE_TEMP_FILES` | Regenerate existing output files (default: `false`) | No |
| `URL_FETCH_TIMEOUT_SECONDS` | Timeout for remote source downloads (default: `30`) | No |
| `URL_FETCH_RETRIES` | Retry attempts for remote source downloads (default: `3`) | No |
| `GPP_CATALOG_PIN_COMMIT` / `GPP_CATALOG_PIN_SHA256` | Override the pinned G++ catalog commit and its SHA-256 (defaults in `src/constants.py`; always change both together) | No |
| `OUTPUT_ROOT` | Root directory for generated artifacts (default: repository root) | No |
| `SDT_HELPER_OUTPUT_DIR` / `SDT_PROFILES_REGULAR_DIR` / `SDT_PROFILES_PROCESS_DIR` / `ED23_PROFILES_DIR` | Override individual output directories (default: under `OUTPUT_ROOT`) | No |

> **Note:** The pipeline fetches input catalogs from GitHub and writes generated artifacts to local directories (`hilfsdateien/`, `Zielobjektkategorien/profile/`, `ED23-Baustein-profile/`) relative to the repository root. The former GCS variables (`BUCKET_NAME`, `SOURCE_PREFIX`, `OUTPUT_PREFIX`) and the `google-cloud-storage` dependency have been removed — only `GCP_PROJECT_ID` is required to start the tool.

## Usage

### Local Execution

Use the provided helper script to run the pipeline locally:

```bash
./scripts/run_local.sh --stage <stage_name>
```

To run the full pipeline, omit the stage argument:
```bash
./scripts/run_local.sh
```

### Data Sources (Inputs)

All input data is fetched from GitHub at runtime (see `src/constants.py`):

- **G++ catalog** — the Grundschutz++ Kompendium (the target catalog of the migration). Fetched at a **pinned commit** and verified against a pinned **SHA-256** (Handbuch 3.13/3.14, Katalogarbeit-Skill Grundregel 8); a hash mismatch aborts the stage. The generated OSCAL profiles carry the same pin in their back-matter (fragment import → resource with commit-pinned rlink + hash). A catalog update is a conscious pin change: update `GPP_CATALOG_PIN_COMMIT` and `GPP_CATALOG_PIN_SHA256` in `src/constants.py`, re-run `scripts/pin_profile_imports.py` over the profile directories, and commit both together.
- **BSI Ed2023 catalog** — the source BSI IT-Grundschutz Edition 2023 requirements.
- **`target_object_categories.csv`** — the Zielobjektkategorien (UUID, name, and hierarchy via `ChildOfUUID`).

### Available Pipeline Stages

You can run specific stages using the `--stage` argument. The full pipeline runs them in the order below. Stage 1 is deterministic prep/mapping, stage 2 is the AI-driven Baustein→Zielobjekt match, stages 3–5 build and enrich the OSCAL output, and stages 6–7 produce the ED2023 cross-mappings consumed by the GS++-oscal-app.

| # | Stage | AI? | What it does |
|---|---|---|---|
| 1 | `stage_gpp` | No | Deterministic mapping: walks the G++ catalog and the Zielobjektkategorien CSV (including the parent hierarchy) to compute, for each Zielobjekt, the set of applicable G++ controls. Writes `hilfsdateien/zielobjekt_controls.json`. |
| 2 | `stage_match_bausteine` | **Yes** | For each BSI Baustein, asks the model which G++ Zielobjekt it corresponds to (title + description → best match). Writes the Baustein→Zielobjekt map (`hilfsdateien/baustein_zielobjekt.json`). |
| 3 | `stage_profiles` | No | Generates the **base OSCAL profiles** — one per Zielobjekt — each importing the G++ catalog and including **all** of that Zielobjektkategorie's controls. Output is split into `Zielobjektkategorien/profile/regular/` and `…/process/` (Methodik and `*_prozesse`). |
| 4 | `stage_ED23_profiles_enhanced` | **Yes** | For each matched Baustein, takes the base profile (all controls of the Zielobjektkategorie) and enriches every control with maturity-level statements (levels 1–5) plus classifications (NIST class, ISMS phase, CIA) as OSCAL `alter` blocks. The enrichment is driven by best practices and the **description of the BSI Baustein** the profile is based on. Writes per-Baustein profiles to `ED23-Baustein-profile/DE/` as `[Zielobjektkategorie]_[Baustein-ID]_[Baustein-Name].json`. |
| 5 | `stage_base_process_enhanced` | **Yes** | Enriches the process profiles (`Zielobjektkategorien/profile/process/`) the same way — maturity sub-statements plus classifications as `alter` blocks — writing `*_enhanced.json` next to each base process profile. |
| 6 | `stage_ed23_anforderungen` | **Yes** | For every G++ control, finds **all** matching BSI ED2023 Anforderungen (grounded on a cached, stripped ED2023 corpus; returned IDs are validated against the real catalog). Writes the OSCAL mapping collection `hilfsdateien/gpp_ed23_anforderungen.json`, which the GS++-oscal-app use for the "Zeige BSI ED23 Anforderungen" panel. |
| 7 | `stage_prozessbausteine` | **Yes** | The inverse direction, 1:1: maps **every** Anforderung of the process-oriented ED2023 layers (ISMS, ORP, CON, OPS, DER) to its single best G++ control (Gemini Pro with thinking, grounded on the cached full G++ catalog). Runs in rounds until every Anforderung is mapped — unmatched ones are re-queried with a stricter prompt — and only publishes on full coverage. Writes `hilfsdateien/prozessbausteine_mapping.json`. |

#### Data flow

```
catalogs + CSV (GitHub)
        │
  1 gpp   ──► zielobjekt_controls.json        (Zielobjekt → all G++ controls)    [deterministic]
  2 match_bausteine ──► baustein_zielobjekt.json    (Baustein → Zielobjekt)      [AI]
        │
  3 profiles ──► base profiles (import G++ catalog, all controls)   Zielobjektkategorien/profile/{regular,process}/
        │
  4 ED23_profiles_enhanced ──► enriched profiles (+ alter blocks)   ED23-Baustein-profile/DE/   [AI, per Baustein]
  5 base_process_enhanced ──► enriched process profiles (*_enhanced.json)   …/profile/process/   [AI]
        │
  6 ed23_anforderungen ──► gpp_ed23_anforderungen.json   (G++ control → ED23 Anforderungen, 1:n)   [AI]
  7 prozessbausteine  ──► prozessbausteine_mapping.json  (ED23 Anforderung → G++ control, 1:1)     [AI]
```

### Running a single stage locally

To (re)generate the G++ Zielobjektkategorien and process profiles locally:

```bash
./scripts/run_local.sh --stage stage_profiles
```

To then enrich them with the ED2023 maturity statements:

```bash
./scripts/run_local.sh --stage stage_ED23_profiles_enhanced
```

The same pattern works for any stage name listed above (e.g. `--stage stage_match_bausteine`). By default `OVERWRITE_TEMP_FILES` is `false`, so stages skip outputs that already exist — a re-run only fills the gaps. Set `OVERWRITE_TEMP_FILES=true ./scripts/run_local.sh …` to force regeneration, or pass `--clear-all` to first wipe the generated output directories.

## Deployment

The tool is designed to run as a Google Cloud Run Job. Use the deployment script:

```bash
./scripts/deploy.sh <GCP_PROJECT_ID> <GCP_REGION>
```

## How-To / Workflow

1.  **Preparation:** No manual upload is required — the source BSI Ed2023 catalog, the G++ catalog, and the target-object categories are fetched directly from their upstream GitHub repositories at runtime (see `src/constants.py`).
2.  **Mapping:** The tool establishes, per Zielobjektkategorie, the set of applicable G++ controls (deterministic) and matches each BSI Baustein to a Zielobjekt (AI).
3.  **Profiles:** It generates a base OSCAL profile per Zielobjekt that imports the G++ catalog and includes all of that Zielobjektkategorie's controls.
4.  **Enrichment:** For each matched Baustein, Gemini generates implementation guidance and maturity-level descriptions for every control, based on best practices and the Baustein's description.
5.  **Finalization:** The tool outputs valid OSCAL 1.2.2 profiles (enriched with `alter` blocks) ready for use in G++ compatible tools.

---

For more technical details, refer to [G++ Automatisierte Erstellung Zielobjekte-Bausteine.md](./G++%20Automatisierte%20Erstellung%20Zielobjekte-Bausteine.md).
