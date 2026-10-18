#!/bin/bash
#
# run_cloud.sh
#
# Executes the deployed OSCAL generation pipeline on Google Cloud Run.
#
# This script invokes the Cloud Run job, passing the necessary environment
# variables for a production run. It assumes the job has already been deployed
# via the deploy.sh script.
#
# Usage:
#   ./scripts/run_cloud.sh <GCP_PROJECT_ID> <GCP_REGION> [<STAGE>]
#

# --- Configuration ---
set -e

# --- Variables ---
if [ "$#" -lt 2 ]; then
    echo "Usage: $0 <GCP_PROJECT_ID> <GCP_REGION> [<STAGE>]"
    exit 1
fi

GCP_PROJECT_ID="$1"
GCP_REGION="$2"
STAGE="${3:-}"
JOB_NAME="oscal-generator"


echo "--- Starting Cloud Run Job Execution ---"

# --- Execute Cloud Run Job ---
# The --update-env-vars flag sets the environment variables for this execution.
gcloud beta run jobs execute "$JOB_NAME" \
  --region "$GCP_REGION" \
  --project "$GCP_PROJECT_ID" \
  --wait \
  --update-env-vars "GCP_PROJECT_ID=$GCP_PROJECT_ID,REGION=global,TEST=false" \
  ${STAGE:+--args="--stage,$STAGE"}

echo "--- Cloud Run Job Execution Finished ---"
