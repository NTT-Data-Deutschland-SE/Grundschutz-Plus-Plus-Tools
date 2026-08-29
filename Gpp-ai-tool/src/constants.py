"""
Defines application-wide constants.

This module centralizes all static, non-configurable values used across the
application. This improves maintainability by providing a single, authoritative
source for these constants.
"""

import os
import re

# --- Path Configuration ---
# All paths are resolved as absolute paths to ensure the application runs
# correctly regardless of the current working directory.
SRC_ROOT = os.path.dirname(os.path.abspath(__file__))
# REPO_ROOT is the parent directory of the 'Gpp-ai-tool' project folder. It can be
# overridden with OUTPUT_ROOT so the generated artifacts can be written somewhere other
# than the repository's sibling-directory layout (issue 3.5).
REPO_ROOT = os.path.abspath(os.path.join(SRC_ROOT, "..", ".."))
OUTPUT_ROOT = os.path.abspath(os.environ.get("OUTPUT_ROOT", REPO_ROOT))

# ANFORDERUNG_ID_PATTERN = re.compile(r"^[A-Z]{2,}(\.\d+)+(?:.A\d+)?$")
ANFORDERUNG_ID_PATTERN = re.compile(r"^.*$")

# --- Data Source URLs ---
# Input data is fetched directly from the upstream GitHub repositories (raw
# content) rather than from local submodule checkouts. The loaders in
# utils/data_loader.py and utils/file_utils.py transparently download these.
ZIELOBJEKTKATEGORIEN_CSV_PATH = "https://raw.githubusercontent.com/BSI-Bund/Stand-der-Technik-Bibliothek/refs/heads/main/documentation/namespaces/target_object_categories.csv"
BSI_2023_JSON_PATH = "https://raw.githubusercontent.com/NTTDATA-DACH/BSI-GS-Benutzerdefinierte-Edition23-OSCAL/refs/heads/main/BS_GK_OSCAL_JSON_DATA/BSI_GS_OSCAL_current_2023_benutzerdefinierte.json"

# --- G++ Catalog Pin (Handbuch 3.13/3.14, Katalogarbeit-Skill Grundregel 8) ---
# The G++ catalog is consumed at a pinned commit and verified against a known SHA-256 —
# the same pin the generated OSCAL profiles carry in their back-matter (see
# scripts/pin_profile_imports.py). A catalog update is a conscious pin change: update
# these two values together (or override both via env), re-run the pin script over the
# profile directories, and commit the result as one change.
GPP_CATALOG_PIN_COMMIT = os.environ.get(
    "GPP_CATALOG_PIN_COMMIT", "36a0fac473c630dd76c83fdfb13a201770b4e1bd"
)
GPP_CATALOG_PIN_SHA256 = os.environ.get(
    "GPP_CATALOG_PIN_SHA256",
    "7c3c5172806d60b219bd210f7b51a8b492c5d18dd603c95039a8ed2d35a41146",
)
GPP_KOMPENDIUM_JSON_PATH = (
    "https://raw.githubusercontent.com/BSI-Bund/Stand-der-Technik-Bibliothek/"
    f"{GPP_CATALOG_PIN_COMMIT}/control_layer/Grundschutz%2B%2B/Grundschutz%2B%2B-resolved_catalog.json"
)

# --- Filtering ---
ALLOWED_MAIN_GROUPS = ["SYS", "INF", "IND", "APP", "NET"]
ALLOWED_PROCESS_BAUSTEINE = ["OPS.2.2", "OPS.2.3", "OPS.3.2"]
# The prozessorientierte layers of the BSI ED2023 Kompendium; every Anforderung below them
# is mapped 1:1 to a G++ control by stage_prozessbausteine. Note: the OPS Bausteine listed
# in ALLOWED_PROCESS_BAUSTEINE above are *also* routed through the per-Baustein profile flow
# — the two mappings coexist deliberately (flat ED23→G++ lookup here vs. per-Zielobjekt
# OSCAL profiles there) and may differ, as they are produced by independent AI runs.
PROZESSBAUSTEINE_LAYERS = ["ISMS", "ORP", "CON", "OPS", "DER"]

# --- Output File Paths ---
# Output roots default to the repository's sibling-directory layout under OUTPUT_ROOT
# (== REPO_ROOT unless overridden), but each can be pointed elsewhere via an env var so
# the tool is portable to other deployment contexts (issue 3.5).
SDT_HELPER_OUTPUT_DIR = os.path.abspath(
    os.environ.get("SDT_HELPER_OUTPUT_DIR", os.path.join(OUTPUT_ROOT, "hilfsdateien"))
)
BAUSTEIN_ZIELOBJEKT_JSON_PATH = os.path.join(SDT_HELPER_OUTPUT_DIR, "baustein_zielobjekt.json")
ZIELOBJEKT_CONTROLS_JSON_PATH = os.path.join(SDT_HELPER_OUTPUT_DIR, "zielobjekt_controls.json")
BAUSTEIN_ZIELOBJEKTKATEGORIE_JSON_PATH = os.path.join(SDT_HELPER_OUTPUT_DIR, "baustein_zielobjektkategorien.json")
ZIELOBJEKTKATEGORIE_CONTROLS_JSON_PATH = os.path.join(SDT_HELPER_OUTPUT_DIR, "zielobjektkategorien_controls.json")
PROZZESSBAUSTEINE_CONTROLS_JSON_PATH = os.path.join(SDT_HELPER_OUTPUT_DIR, "prozessbausteine_mapping.json")
# Per-G++-control mapping to matching BSI Edition-2023 Anforderungen (stage_ed23_anforderungen).
# Consumed by the GS++-oscal-app to show the "Zeige BSI ED23 Anforderungen" panel.
GPP_ED23_ANFORDERUNGEN_JSON_PATH = os.path.join(SDT_HELPER_OUTPUT_DIR, "gpp_ed23_anforderungen.json")
# A compact projection of the ED23 catalog (id | name | prose) used as the cached grounding corpus.
ED23_ANFORDERUNGEN_STRIPPED_JSON_PATH = os.path.join(SDT_HELPER_OUTPUT_DIR, "ed23_anforderungen_stripped.json")
# Per-sentence coverage judgment of the OFFICIAL ED23 Kompendium (amtliches XML) against the
# G++ catalog (stage_ed23_satz_abdeckung). Consumed by scripts/analyze_ed23_coverage.py.
ED23_SATZ_ABDECKUNG_JSON_PATH = os.path.join(SDT_HELPER_OUTPUT_DIR, "ed23_satz_abdeckung.json")
SDT_PROFILES_REGULAR_DIR = os.path.abspath(
    os.environ.get("SDT_PROFILES_REGULAR_DIR", os.path.join(OUTPUT_ROOT, "Zielobjektkategorien/profile/regular"))
)
SDT_PROFILES_PROCESS_DIR = os.path.abspath(
    os.environ.get("SDT_PROFILES_PROCESS_DIR", os.path.join(OUTPUT_ROOT, "Zielobjektkategorien/profile/process"))
)
ED23_PROFILES_DIR = os.path.abspath(
    os.environ.get("ED23_PROFILES_DIR", os.path.join(OUTPUT_ROOT, "ED23-Baustein-profile/DE"))
)



# --- Asset Paths ---
PROMPT_CONFIG_PATH = os.path.join(SRC_ROOT, "assets/json/prompt_config.json")
BAUSTEIN_TO_ZIELOBJEKT_SCHEMA_PATH = os.path.join(SRC_ROOT, "assets/schemas/baustein_to_zielobjekt_schema.json")
ENHANCED_CONTROL_RESPONSE_SCHEMA_PATH = os.path.join(SRC_ROOT, "assets/schemas/enhanced_control_response_schema.json")
ED23_ANFORDERUNGEN_RESPONSE_SCHEMA_PATH = os.path.join(SRC_ROOT, "assets/schemas/ed23_anforderungen_response_schema.json")
ED23_VERIFY_RESPONSE_SCHEMA_PATH = os.path.join(SRC_ROOT, "assets/schemas/ed23_verify_response_schema.json")
ED23_SATZ_RESPONSE_SCHEMA_PATH = os.path.join(SRC_ROOT, "assets/schemas/ed23_satz_response_schema.json")
ED23_SATZ_VERIFY_RESPONSE_SCHEMA_PATH = os.path.join(SRC_ROOT, "assets/schemas/ed23_satz_verify_response_schema.json")
ED23_RELATION_RESPONSE_SCHEMA_PATH = os.path.join(SRC_ROOT, "assets/schemas/ed23_relation_response_schema.json")
PROZESSBAUSTEINE_RESPONSE_SCHEMA_PATH = os.path.join(SRC_ROOT, "assets/schemas/prozessbausteine_response_schema.json")

# --- AI Model Configuration ---
# These default to current Gemini preview identifiers. They are env-overridable so a stable,
# versioned Vertex AI model id can be pinned for reproducibility without a code change
# (issue 4.1).
GROUND_TRUTH_MODEL = os.environ.get("GROUND_TRUTH_MODEL", "gemini-3.7-flash")
GROUND_TRUTH_MODEL_PRO = os.environ.get("GROUND_TRUTH_MODEL_PRO", "gemini-3.1-pro-preview")
# Maker model for the ED23 candidate pass (stage_ed23_anforderungen). Deliberately a
# different model than the verifier: gemini-3-flash-preview nominates candidates far more
# generously (high recall), while the strict verification pass on GROUND_TRUTH_MODEL
# (gemini-3.7-flash) restores precision. Measured on a 23-control sample: the 3.7 maker
# never nominates certain valid candidates, so no checker could recover them.
ED23_MAKER_MODEL = os.environ.get("ED23_MAKER_MODEL", "gemini-3-flash-preview")
# How many ED2023 Anforderungen stage_prozessbausteine sends per request. The whole G++
# catalog is the (cached) grounding corpus, so the chunk only bounds the *output* size and
# keeps each 1:1 decision inside a context the model can still reason over reliably.
PROZESSBAUSTEINE_CHUNK_SIZE = int(os.environ.get("PROZESSBAUSTEINE_CHUNK_SIZE", "15"))
# The stage keeps re-querying Anforderungen that came back without a (valid) match until
# every single one is mapped — this caps the number of query rounds so a systematic failure
# (e.g. schema drift, model refusing an ID) cannot loop forever. On exhaustion the stage
# fails loudly instead of publishing an incomplete mapping.
PROZESSBAUSTEINE_MAX_ROUNDS = int(os.environ.get("PROZESSBAUSTEINE_MAX_ROUNDS", "10"))

# --- API Configuration ---
# Constants for external API interactions, such as retry logic parameters.
API_MAX_RETRIES = 5
API_RETRY_BACKOFF_FACTOR = 2
API_RETRY_JITTER = 0.5  # 50% jitter
API_TEMPERATURE = 1
API_MAX_OUTPUT_TOKEN = 65536

# --- Logging ---
LOG_LEVEL_TEST = "DEBUG"
LOG_LEVEL_PRODUCTION = "INFO"
THIRD_PARTY_LOG_LEVEL_PRODUCTION = "WARNING"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# --- OSCAL Metadata ---
# Default values and namespaces for OSCAL artifact generation.
OSCAL_VERSION = "1.2.2"
# The OSCAL namespace is pinned at /1.0 across all model versions (it identifies the
# OSCAL naming system, not the model version) — do not bump it with OSCAL_VERSION.
OSCAL_NAMESPACE = "http://csrc.nist.gov/ns/oscal/1.0"
# Naming-system identifier (OSCAL prop `ns`) for the custom enhancement props
# (control_class, phase) added by the enhanced-profile stages. These are
# neither OSCAL- nor BSI-defined, so they carry this dedicated, documented namespace; the URI
# resolves to the file describing the allowed values.
GPP_ENHANCEMENT_PROPS_NS = "https://github.com/NTT-Data-Deutschland-SE/Grundschutz-Plus-Plus-Tools/tree/main/Dokumentation/namespaces/gpp_enhancement_props.md"

# --- Praktiken (Practices) ---
# Maps a practice abbreviation (Kürzel, e.g. "ARCH") to its full German term (Begriff,
# e.g. "Architektur"). The process-Zielobjekt ids are these Kürzel suffixed with
# "_prozesse" (e.g. "ARCH_prozesse"), so resolving them yields readable profile titles.
# Source of truth (keep in sync):
# https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek/blob/main/documentation/namespaces/practices.csv
PRACTICE_ABBREVIATIONS = {
    "GC": "Governance und Compliance",
    "STM": "Strukturmodellierung",
    "UMS": "Umsetzung",
    "VRB": "Verbesserung",
    "PERF": "Monitoring-Evaluation",
    "RISK": "Risikomanagement",
    "ASST": "Informationen und Assets",
    "PERS": "Personal",
    "BES": "Beschaffungsmanagement",
    "DLS": "Dienstleistersteuerung",
    "TEST": "Änderungen und Tests",
    "GEB": "Gebäudemanagement",
    "SENS": "Sensibilisierung",
    "ARCH": "Architektur",
    "BER": "Berechtigung",
    "NOT": "Notfallplanung",
    "DET": "Detektion",
    "REA": "Sicherheitsvorfallsbehandlung",
    "KONF": "Konfiguration",
    "DEV": "Entwicklung",
    # Not a practice per se, but used as a process-Zielobjekt id for the methodology pool.
    "METHODIK": "Methodik",
}
