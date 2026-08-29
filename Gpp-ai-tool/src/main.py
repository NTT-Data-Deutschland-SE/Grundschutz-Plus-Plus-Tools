"""
Main entry point for the OSCAL generation pipeline.

This script initializes the application's configuration and logging, then
starts the main processing pipeline. It is designed to be executed as the
entry point for the GCP Cloud Run job.
"""

import logging
import asyncio
import argparse

from pipeline import stage_ED23_profiles_enhanced, stage_base_process_enhanced, stage_gpp, stage_match_bausteine, stage_profiles, stage_ed23_anforderungen, stage_ed23_satz_abdeckung, stage_prozessbausteine, processing
from utils.logger import setup_logging


async def main() -> None:
    """
    Orchestrates the OSCAL generation pipeline.

    This function executes the main steps of the pipeline based on the
    provided command-line arguments.
    """
    setup_logging()
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description="OSCAL Generation Pipeline")
    parser.add_argument(
        "--stage",
        type=str,
        required=False,
        choices=["stage_gpp", "stage_match_bausteine", "stage_profiles", "stage_ED23_profiles_enhanced", "stage_base_process_enhanced", "stage_ed23_anforderungen", "stage_ed23_satz_abdeckung", "stage_prozessbausteine"],
        help="The pipeline stage to execute. If not provided, the full pipeline will run.",
    )
    args = parser.parse_args()


    if args.stage:
        logger.info(f"Starting OSCAL generation pipeline for stage: {args.stage}...")
        if args.stage == "stage_gpp":
            stage_gpp.run_stage_gpp()
        elif args.stage == "stage_match_bausteine":
            await stage_match_bausteine.run_stage_match_bausteine()
        elif args.stage == "stage_profiles":
            stage_profiles.run_stage_profiles()
        elif args.stage == "stage_ED23_profiles_enhanced":
            await stage_ED23_profiles_enhanced.run_stage_ED23_profiles_enhanced()
        elif args.stage == "stage_base_process_enhanced":
            await stage_base_process_enhanced.run_stage_base_process_enhanced()
        elif args.stage == "stage_ed23_anforderungen":
            await stage_ed23_anforderungen.run_stage_ed23_anforderungen()
        elif args.stage == "stage_ed23_satz_abdeckung":
            await stage_ed23_satz_abdeckung.run_stage_ed23_satz_abdeckung()
        elif args.stage == "stage_prozessbausteine":
            await stage_prozessbausteine.run_stage_prozessbausteine()
    else:
        logger.info("No stage specified. Starting full pipeline execution...")
        await processing.run_full_pipeline()


    logger.debug("OSCAL generation pipeline finished successfully.")


if __name__ == "__main__":
    asyncio.run(main())