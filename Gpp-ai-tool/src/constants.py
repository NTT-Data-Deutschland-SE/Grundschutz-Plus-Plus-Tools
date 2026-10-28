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

# --- Build ---
BUILD_VERSION = "5.0.1"

# --- Data Source URLs ---
# Input data is fetched directly from the upstream GitHub repositories (raw content), always
# at a pinned commit and verified against a pinned SHA-256 (Handbuch 3.13/3.14, Grundregel 8).

# --- ED23 catalog pin (NTT DATA DACH benutzerdefinierte OSCAL-Ausgabe der Edition 2023) ---
# Two files at the same commit: the benutzerdefinierte Gesamtkatalog (111 BSI-Bausteine plus
# the 12 NTT-eigenen "NG"-Bausteine) and the plain BSI file (111). The catalog itself carries
# no marker for the NTT-Bausteine — the difference of the two Baustein-ID sets IS the NG set
# (utils/ed23_baustein.detect_ng). Change commit and both hashes together.
ED23_CATALOG_PIN_COMMIT = os.environ.get(
    "ED23_CATALOG_PIN_COMMIT", "62f080393956331bb202f2c057eb416af8fcd4de"
)
ED23_BD_CATALOG_PIN_SHA256 = os.environ.get(
    "ED23_BD_CATALOG_PIN_SHA256",
    "ab94fb31de6dbbc64c5a0be5b51dd90a73a7400d78ce5f0ccc2261dd91a39b0c",
)
ED23_PLAIN_CATALOG_PIN_SHA256 = os.environ.get(
    "ED23_PLAIN_CATALOG_PIN_SHA256",
    "119e70545b896ff3b592af250097b960ed33d6e98ac775b7f230403a92b118a0",
)
_ED23_RAW = (
    "https://raw.githubusercontent.com/NTTDATA-DACH/BSI-GS-Benutzerdefinierte-Edition23-OSCAL/"
    f"{ED23_CATALOG_PIN_COMMIT}/BS_GK_OSCAL_JSON_DATA/"
)
BSI_2023_JSON_PATH = _ED23_RAW + "BSI_GS_OSCAL_current_2023_benutzerdefinierte.json"  # 123 Bausteine
BSI_2023_PLAIN_JSON_PATH = _ED23_RAW + "BSI_GS_OSCAL_current_2023.json"  # 111 Bausteine

# --- G++ Catalog Pin (Handbuch 3.13/3.14, Katalogarbeit-Skill Grundregel 8) ---
# The G++ catalog is consumed at a pinned commit and verified against a known SHA-256 —
# the same pin the generated OSCAL profiles carry in their back-matter (see
# scripts/pin_profile_imports.py). A catalog update is a conscious pin change: update
# these two values together (or override both via env), re-run the pin script over the
# profile directories, and commit the result as one change.
GPP_CATALOG_PIN_COMMIT = os.environ.get(
    "GPP_CATALOG_PIN_COMMIT", "160c177db6c84d3c621fff614559943b1de8c600"
)
GPP_CATALOG_PIN_SHA256 = os.environ.get(
    "GPP_CATALOG_PIN_SHA256",
    "7c3acebd0867724e8fc2e6ce73f942642fcd37e533600e0952699f130a8bca90",
)
GPP_KOMPENDIUM_JSON_PATH = (
    "https://raw.githubusercontent.com/BSI-Bund/Stand-der-Technik-Bibliothek/"
    f"{GPP_CATALOG_PIN_COMMIT}/control_layer/Grundschutz%2B%2B/Grundschutz%2B%2B-resolved_catalog.json"
)
# The Zielobjekt namespace CSV must come from the SAME commit as the catalog: stage_gpp
# joins the CSV names against the catalog's target_object_categories values, and the BSI
# renames categories in both places at once (e.g. Endgeräte → Mobile Endgeräte, a128311).
# Reading the CSV from main while the catalog is pinned silently empties renamed pools.
ZIELOBJEKTKATEGORIEN_CSV_PATH = (
    "https://raw.githubusercontent.com/BSI-Bund/Stand-der-Technik-Bibliothek/"
    f"{GPP_CATALOG_PIN_COMMIT}/documentation/namespaces/target_object_categories.csv"
)

# --- Filtering ---
ALLOWED_MAIN_GROUPS = ["SYS", "INF", "IND", "APP", "NET"]
# Prozess-Bausteine, die trotzdem ein eigenes Profil in ED23-Baustein-profile/DE bekommen:
# die drei OPS-Bausteine der ersten Fassung, die drei NTT-eigenen Prozess-Bausteine (NG), und die
# sieben BSI-Prozess-Bausteine, deren Thema in Grundschutz++ keine eigene Praktik hat
# (Satzabdeckung < 45 % oder >= 5 Anforderungen ohne jeden Treffer; Tabelle reproduzierbar mit
# scripts/prozess_luecken.py aus hilfsdateien/ed23_satz_abdeckung.json).
ALLOWED_PROCESS_BAUSTEINE = [
    "OPS.2.2", "OPS.2.3", "OPS.3.2",
    "ORP.6", "OPS.1.1.8", "DER.7",                                    # NG (NTT DATA)
    "DER.3.1", "DER.3.2", "DER.2.2", "DER.2.3", "DER.4", "OPS.1.2.2", "CON.11.1",  # ohne Praktik
]
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
# Per-Anforderung assignment of every Baustein that gets a profile: deterministic sources plus the
# maker-checker residual, incl. the proposed NG controls (stage_ed23_baustein_abgleich).
ED23_BAUSTEIN_ABGLEICH_JSON_PATH = os.path.join(SDT_HELPER_OUTPUT_DIR, "ed23_baustein_abgleich.json")
# Harvested maturity alter blocks (paid LLM output) keyed by Baustein and control, reused by
# stage_ED23_profiles_enhanced so a regeneration only pays for controls without an entry.
ED23_MATURITY_CACHE_JSON_PATH = os.path.join(SDT_HELPER_OUTPUT_DIR, "ed23_maturity_cache.json")
SDT_PROFILES_REGULAR_DIR = os.path.abspath(
    os.environ.get("SDT_PROFILES_REGULAR_DIR", os.path.join(OUTPUT_ROOT, "Zielobjektkategorien/profile/regular"))
)
SDT_PROFILES_PROCESS_DIR = os.path.abspath(
    os.environ.get("SDT_PROFILES_PROCESS_DIR", os.path.join(OUTPUT_ROOT, "Zielobjektkategorien/profile/process"))
)
ED23_PROFILES_DIR = os.path.abspath(
    os.environ.get("ED23_PROFILES_DIR", os.path.join(OUTPUT_ROOT, "ED23-Baustein-profile/DE"))
)
# The one shared NG Ergänzungskatalog next to the profiles (relative rlink in their back-matter).
NG_KATALOG_FILENAME = "NG-ergaenzungskatalog.json"
NG_KATALOG_PATH = os.path.join(ED23_PROFILES_DIR, NG_KATALOG_FILENAME)

# --- BSI GSMap (ITGS 2023 -> GS++), the official bridge; pinned, used as a deterministic source ---
ITGS_PIN_COMMIT = "8f0bcd1fbb4f47a7bec911fc20118ce6e8ef4dad"
ITGS_MAPPING_URL = (
    "https://raw.githubusercontent.com/BSI-Bund/Stand-der-Technik-Bibliothek/"
    f"{ITGS_PIN_COMMIT}/control_layer/Mappings/IT-GS2023-zu-GSpp/ITGS-to-GS%2B%2B-mapping_collection.json"
)
ITGS_MAPPING_PIN_SHA256 = "df7ea11261ace956a3ebb440f60928851a4815f5545775ac9b24e4d3d22f267f"
SDT_SECURITY_LEVEL_CSV_PATH = (
    "https://raw.githubusercontent.com/BSI-Bund/Stand-der-Technik-Bibliothek/"
    f"{GPP_CATALOG_PIN_COMMIT}/documentation/namespaces/security_level.csv"
)



# --- Asset Paths ---
PROMPT_CONFIG_PATH = os.path.join(SRC_ROOT, "assets/json/prompt_config.json")
BAUSTEIN_TO_ZIELOBJEKT_SCHEMA_PATH = os.path.join(SRC_ROOT, "assets/schemas/baustein_to_zielobjekt_schema.json")
ENHANCED_CONTROL_RESPONSE_SCHEMA_PATH = os.path.join(SRC_ROOT, "assets/schemas/enhanced_control_response_schema.json")
ED23_ANFORDERUNGEN_RESPONSE_SCHEMA_PATH = os.path.join(SRC_ROOT, "assets/schemas/ed23_anforderungen_response_schema.json")
ED23_VERIFY_RESPONSE_SCHEMA_PATH = os.path.join(SRC_ROOT, "assets/schemas/ed23_verify_response_schema.json")
ED23_BATCH_RESPONSE_SCHEMA_PATH = os.path.join(SRC_ROOT, "assets/schemas/ed23_batch_response_schema.json")
ED23_SATZ_RESPONSE_SCHEMA_PATH = os.path.join(SRC_ROOT, "assets/schemas/ed23_satz_response_schema.json")
ED23_SATZ_VERIFY_RESPONSE_SCHEMA_PATH = os.path.join(SRC_ROOT, "assets/schemas/ed23_satz_verify_response_schema.json")
ED23_RELATION_RESPONSE_SCHEMA_PATH = os.path.join(SRC_ROOT, "assets/schemas/ed23_relation_response_schema.json")
ED23_RELATION_CONTROL_RESPONSE_SCHEMA_PATH = os.path.join(SRC_ROOT, "assets/schemas/ed23_relation_control_response_schema.json")
PROZESSBAUSTEINE_RESPONSE_SCHEMA_PATH = os.path.join(SRC_ROOT, "assets/schemas/prozessbausteine_response_schema.json")
ED23_BAUSTEIN_ABGLEICH_MAKER_SCHEMA_PATH = os.path.join(SRC_ROOT, "assets/schemas/ed23_baustein_abgleich_maker_schema.json")
ED23_BAUSTEIN_ABGLEICH_CHECKER_SCHEMA_PATH = os.path.join(SRC_ROOT, "assets/schemas/ed23_baustein_abgleich_checker_schema.json")

# --- AI call tuning ---
# The model id and the thinking levels live in config.Settings (GEMINI_MODEL, MAKER_THINKING_LEVEL,
# CHECKER_THINKING_LEVEL, MAX_OUTPUT_TOKENS, API_MAX_RETRIES) — one model, no sampling params.
# Controls per maker call in stage_ed23_anforderungen (docs/token-kostenplan.md, Maßnahme 3):
# the cached corpus is billed per CALL, so batching divides the dominant cached-input cost
# by the batch size. Keep small — per-control attention (recall) must not suffer.
ED23_MAKER_BATCH_SIZE = int(os.environ.get("ED23_MAKER_BATCH_SIZE", "5"))
# How many ED2023 Anforderungen stage_prozessbausteine sends per request. The whole G++
# catalog is the (cached) grounding corpus, so the chunk only bounds the *output* size and
# keeps each 1:1 decision inside a context the model can still reason over reliably.
PROZESSBAUSTEINE_CHUNK_SIZE = int(os.environ.get("PROZESSBAUSTEINE_CHUNK_SIZE", "15"))
# The stage keeps re-querying Anforderungen that came back without a (valid) match until
# every single one is mapped — this caps the number of query rounds so a systematic failure
# (e.g. schema drift, model refusing an ID) cannot loop forever. On exhaustion the stage
# fails loudly instead of publishing an incomplete mapping.
PROZESSBAUSTEINE_MAX_ROUNDS = int(os.environ.get("PROZESSBAUSTEINE_MAX_ROUNDS", "10"))

# Anforderungen per maker call in stage_ed23_baustein_abgleich (never across Bausteine).
ED23_BAUSTEIN_ABGLEICH_BATCH_SIZE = int(os.environ.get("ED23_BAUSTEIN_ABGLEICH_BATCH_SIZE", "5"))
# Maturity texts describe the control, the Baustein is only prompt context: reuse an entry
# harvested under another Baustein instead of paying for a regeneration.
ED23_MATURITY_REUSE_ACROSS_BAUSTEINE = os.environ.get("ED23_MATURITY_REUSE_ACROSS_BAUSTEINE", "true").lower() == "true"
ED23_MATURITY_REGENERATE = os.environ.get("ED23_MATURITY_REGENERATE", "false").lower() == "true"

# --- Logging ---
LOG_FORMAT = "%(asctime)s %(levelname)s %(name)s: %(message)s"

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
# Naming system of the ED23-Baustein profiles and the NG Ergänzungskatalog (herkunft, ed23-baustein,
# ed23-anforderung, praktik, ohne-control, ...); documented in
# Dokumentation/namespaces/ed23_baustein_props.md. An identifier, not a dereferenceable file.
ED23_BAUSTEIN_NS = "https://github.com/NTT-Data-Deutschland-SE/Grundschutz-Plus-Plus-Tools/ns/ed23-baustein"
# The BSI's own namespace for the ED23 `level` prop (1 = Basis, 3 = Standard, 5 = erhöht).
BSI_GRUNDSCHUTZ_NS = "https://www.bsi.bund.de/ns/grundschutz"
# Stand-der-Technik-Bibliothek vocabularies (same ns strings the Anwenderkatalog uses).
SDT_NS_BASE = "https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek/tree/main/documentation/namespaces"
SDT_MODAL_VERB_NS = f"{SDT_NS_BASE}/modal_verbs.csv"
SDT_TARGET_OBJECT_NS = f"{SDT_NS_BASE}/target_object_categories.csv"
SDT_SECURITY_LEVEL_NS = f"{SDT_NS_BASE}/security_level.csv"

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
