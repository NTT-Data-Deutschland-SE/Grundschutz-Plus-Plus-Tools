"""
Core data processing logic for the OSCAL generation pipeline.

This module contains the orchestrator function for running the entire pipeline
from start to finish, executing each stage in the correct sequence. Every stage reads
its inputs from disk and persists its own output, so any stage can be rerun alone.
"""

import logging

from pipeline import (
    stage_gpp,
    stage_match_bausteine,
    stage_profiles,
    stage_ed23_anforderungen,
    stage_prozessbausteine,
    stage_ed23_baustein_abgleich,
    stage_ng_katalog,
    stage_ED23_profiles_enhanced,
    stage_base_process_enhanced,
)

logger = logging.getLogger(__name__)


async def run_full_pipeline() -> None:
    """Executes the entire pipeline in dependency order.

    1 gpp (deterministic) → 2 match_bausteine (AI) → 3 profiles (deterministic) →
    4 ed23_anforderungen (AI) → 5 prozessbausteine (AI) → 6 ed23_baustein_abgleich (AI,
    deterministic sources first) → 7 ng_katalog (deterministic) → 8 ED23_profiles_enhanced
    (deterministic structure + cached maturity AI) → 9 base_process_enhanced (AI).
    stage_profiles is no longer an input of the ED23 profile stage; it still produces the
    Zielobjektkategorie profiles the GS++ apps use.
    """
    logger.info("--- Starting Full Pipeline Execution ---")
    steps = [
        ("GPP", stage_gpp.run_stage_gpp),
        ("MATCH BAUSTEINE", stage_match_bausteine.run_stage_match_bausteine),
        ("PROFILES", stage_profiles.run_stage_profiles),
        ("ED23_ANFORDERUNGEN", stage_ed23_anforderungen.run_stage_ed23_anforderungen),
        ("PROZESSBAUSTEINE", stage_prozessbausteine.run_stage_prozessbausteine),
        ("ED23_BAUSTEIN_ABGLEICH", stage_ed23_baustein_abgleich.run_stage_ed23_baustein_abgleich),
        ("NG_KATALOG", stage_ng_katalog.run_stage_ng_katalog),
        ("ED23_PROFILES_ENHANCED", stage_ED23_profiles_enhanced.run_stage_ED23_profiles_enhanced),
        ("BASE_PROCESS_ENHANCED", stage_base_process_enhanced.run_stage_base_process_enhanced),
    ]
    try:
        for name, fn in steps:
            logger.info(f"--- STAGE: {name} ---")
            result = fn()
            if hasattr(result, "__await__"):
                await result
            logger.info(f"--- STAGE: {name} - COMPLETE ---")
    except Exception:
        logger.critical("A critical error occurred during the full pipeline execution.", exc_info=True)
        raise
    logger.info("--- Full Pipeline Execution Finished Successfully ---")
