#!/bin/bash
#
# run_local.sh
#
# Executes the OSCAL generation pipeline locally for development purposes.
#
# This script sets environment variables to simulate the Cloud Run environment
# and runs the main Python application via uv. TEST=true in the environment
# limits every stage to a few items.
#
# Usage:
# ./scripts/run_local.sh [--stage <stage_name>] [--fresh] [--clear-all] [--clear-ai-cache]
#
# Example:
# ./scripts/run_local.sh                                       # Runs the full pipeline
# ./scripts/run_local.sh --stage stage_match_bausteine
# ./scripts/run_local.sh --stage stage_ED23_profiles_enhanced
#

# Change to the application's root directory (the parent of the scripts directory)
# This makes the script runnable from any location.
# BASH_SOURCE[0] is the path to the script itself.
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd "$SCRIPT_DIR/.."

# --- Argument Parsing for --clear-all ---
if [[ " $@ " =~ " --clear-all " ]]; then
    echo "--- Clearing Generated Files (--clear-all) ---"
    # Paid LLM output first: harvest the maturity alters of the existing enhanced profiles
    # into hilfsdateien/ed23_maturity_cache.json before anything is deleted.
    uv run python scripts/harvest_maturity_alters.py || echo "Warning: harvest failed; continuing."

    # Define directories to be cleared.
    # Note: Paths are relative to the project root where this script cd's into,
    # so "../" resolves to REPO_ROOT. These mirror the output directories defined
    # in src/constants.py (SDT_HELPER_OUTPUT_DIR, SDT_PROFILES_*_DIR, ED23_PROFILES_*_DIR).
    declare -a DIRS_TO_CLEAR=(
        "../hilfsdateien"
        "../Zielobjektkategorien/profile/regular"
        "../Zielobjektkategorien/profile/process"
        "../ED23-Baustein-profile/DE"
    )

    for dir in "${DIRS_TO_CLEAR[@]}"; do
        if [ -d "$dir" ]; then
            echo "Clearing contents of '$dir/'..."
            # Delete the generated files, but keep the AI caches (maturity cache, abgleich,
            # checkpoints) — those are paid output; --clear-ai-cache removes them explicitly.
            find "$dir" -maxdepth 1 -type f \
                ! -name 'ed23_maturity_cache.json' \
                ! -name 'ed23_baustein_abgleich.json' \
                ! -name '*.partial' \
                -delete
        else
            echo "Warning: Directory '$dir' not found. Skipping."
        fi
    done
    cp src/assets/json/prozessbausteine_mapping.json ../hilfsdateien/
    echo "--- Finished Clearing Files ---"
fi
if [[ " $@ " =~ " --clear-ai-cache " ]]; then
    echo "--- Clearing AI caches (--clear-ai-cache): maturity cache, abgleich, checkpoints ---"
    rm -f ../hilfsdateien/ed23_maturity_cache.json ../hilfsdateien/ed23_baustein_abgleich.json ../hilfsdateien/*.partial
fi

# --- Configuration ---
# Set the script to exit immediately if any command fails.
set -e

STAGE_INFO=${1:-"full pipeline"}
echo "--- Starting Local Pipeline Execution for: $STAGE_INFO ---"
echo "Working Directory: $(pwd)"

# --- Environment Setup ---
# Credentials come from .env (GEMINI_API_KEY) or the environment (GCP_PROJECT_ID + ADC);
# nothing is defaulted here so a missing credential fails loudly with the reason.
export TEST="${TEST:-false}"
# Default to false so stages keep existing outputs (they skip files that
# already exist). Override with OVERWRITE_TEMP_FILES=true ./scripts/run_local.sh
# to force regeneration, or pass --clear-all to wipe outputs first.
export OVERWRITE_TEMP_FILES="${OVERWRITE_TEMP_FILES:-false}"

# Ensure that Python output is unbuffered, so logs appear immediately.
export PYTHONUNBUFFERED=1

echo "Environment Variables:"
echo "GCP_PROJECT_ID: ${GCP_PROJECT_ID:-<unset, GEMINI_API_KEY aus .env?>}"
echo "TEST: $TEST"
echo "OVERWRITE_TEMP_FILES: $OVERWRITE_TEMP_FILES"
echo "---------------------------------------"

# --- Execution ---
# Run the main Python application from the application root.
# Forward all arguments to the Python script, except "--clear-all" / "--clear-ai-cache",
# which are handled by this wrapper above and not understood by main.py's argparse.
declare -a PYTHON_ARGS=()
for arg in "$@"; do
    if [ "$arg" != "--clear-all" ] && [ "$arg" != "--clear-ai-cache" ]; then
        PYTHON_ARGS+=("$arg")
    fi
done
# uv keeps the pinned environment (.venv) in sync with pyproject.toml / uv.lock.
uv run python src/main.py "${PYTHON_ARGS[@]}"

echo "--- Local Pipeline Execution Finished ---"