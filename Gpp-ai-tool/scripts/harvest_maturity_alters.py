#!/usr/bin/env python3
"""harvest_maturity_alters.py -- v1.0.0

Erntet die Reifegrad-Alters (m1–m5, bezahlte Modellausgabe) aller `*_enhanced.json` in
ED23-Baustein-profile/DE in hilfsdateien/ed23_maturity_cache.json. Idempotent: vorhandene
Cache-Einträge werden nie überschrieben. Braucht keine Credentials und kein Netz.

Aufruf (aus Gpp-ai-tool/): uv run python scripts/harvest_maturity_alters.py [<profil-verzeichnis> ...]
Ohne Argument: ED23-Baustein-profile/DE und Zielobjektkategorien/profile/process.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "src"))

from utils.logger import configure_logging  # noqa: E402
from constants import ED23_MATURITY_CACHE_JSON_PATH, ED23_PROFILES_DIR, SDT_PROFILES_PROCESS_DIR  # noqa: E402
from pipeline.stage_ED23_profiles_enhanced import (  # noqa: E402
    harvest_existing_maturity, load_maturity_cache, save_maturity_cache,
)


def main() -> None:
    configure_logging()
    dirs = sys.argv[1:] or [ED23_PROFILES_DIR, SDT_PROFILES_PROCESS_DIR]
    cache = load_maturity_cache()
    before = sum(len(v) for k, v in cache.items() if k != "_meta")
    added = sum(harvest_existing_maturity(d, cache, None) for d in dirs)
    save_maturity_cache(cache)
    after = sum(len(v) for k, v in cache.items() if k != "_meta")
    print(f"maturity cache: {before} -> {after} Eintraege (+{added}), {ED23_MATURITY_CACHE_JSON_PATH}")


if __name__ == "__main__":
    main()
