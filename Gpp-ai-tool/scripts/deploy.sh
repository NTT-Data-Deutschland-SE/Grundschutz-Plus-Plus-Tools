#!/bin/bash
#
# deploy.sh
#
# Builds the Docker container and deploys it to Google Cloud Run.
#
# This script automates the process of packaging the application into a
# container and deploying it as a Cloud Run job. It requires the gcloud
# SDK to be authenticated and configured.
#
# Usage:
#   ./scripts/deploy.sh <GCP_PROJECT_ID> <GCP_REGION>
#

# --- Configuration ---
set -e

# --- Variables ---
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <GCP_PROJECT_ID> <GCP_REGION>"
    exit 1
fi

GCP_PROJECT_ID="$1"
GCP_REGION="$2"
IMAGE_NAME="oscal-generator"
GCR_HOSTNAME="gcr.io"
IMAGE_TAG="$GCR_HOSTNAME/$GCP_PROJECT_ID/$IMAGE_NAME:latest"

# Build context is the tool root (Dockerfile lives there; one image serves every stage).
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd "$SCRIPT_DIR/.."

echo "--- Starting Deployment Process ---"
echo "Working Directory: $(pwd)"


# --- Build ---
echo "Building Docker image: $IMAGE_TAG"
docker build -t "$IMAGE_TAG" .

# --- Push to Google Container Registry (GCR) ---
echo "Pushing image to GCR..."
gcloud auth configure-docker
docker push "$IMAGE_TAG"

# --- Deploy to Cloud Run ---
# This deploys the container as a Cloud Run Job.
echo "Deploying to Cloud Run..."
gcloud beta run jobs deploy "$IMAGE_NAME" \
  --image "$IMAGE_TAG" \
  --region "$GCP_REGION" \
  --project "$GCP_PROJECT_ID"

echo "--- Deployment Process Finished ---"
