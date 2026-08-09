#!/usr/bin/env bash
set -euo pipefail

# Skript zum Anlegen der Testbenutzer (bearbeiter@example.com, leser@example.com)
# Nutzung:
#   1. Direkt über IAP/SSH auf der VM (Standard):
#      ./seed_users.sh --vm
#   2. Gegen eine öffentliche IP oder URL:
#      ./seed_users.sh --url http://35.246.185.192:8000 --service-key <SERVICE_ROLE_KEY>

URL="http://localhost:8000"
SERVICE_KEY=""
USE_VM=false
ZONE="europe-west3-b"
PROJECT=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --url)
      URL="$2"
      shift 2
      ;;
    --service-key)
      SERVICE_KEY="$2"
      shift 2
      ;;
    --vm)
      USE_VM=true
      shift
      ;;
    --zone)
      ZONE="$2"
      shift 2
      ;;
    --project)
      PROJECT="$2"
      shift 2
      ;;
    *)
      echo "Unbekannter Parameter: $1"
      exit 1
      ;;
  esac
done

if [[ "$USE_VM" == "true" ]]; then
  echo "==> Erzeuge Testbenutzer via SSH auf der VM gpp-supabase..."
  
  PROJECT_FLAG=""
  if [[ -n "$PROJECT" ]]; then
    PROJECT_FLAG="--project $PROJECT"
  fi

  CLOUDSDK_METRICS_ENVIRONMENT=datacloud.antigravity gcloud compute ssh gpp-supabase --zone "$ZONE" $PROJECT_FLAG --tunnel-through-iap -- '
    SR_KEY=$(sudo grep "SERVICE_ROLE_KEY=" /opt/gpp/supabase/.env | cut -d= -f2)

    create_user() {
      local email="$1"
      local pass="$2"
      local role="$3"

      echo "--> Erstelle/Aktualisiere ${email} (${role})..."
      curl -s -X POST "http://localhost:8000/auth/v1/admin/users" \
        -H "Authorization: Bearer ${SR_KEY}" \
        -H "apikey: ${SR_KEY}" \
        -H "Content-Type: application/json" \
        -d "{
          \"email\": \"${email}\",
          \"password\": \"${pass}\",
          \"email_confirm\": true,
          \"user_metadata\": { \"gpp_role\": \"${role}\" },
          \"app_metadata\": { \"gpp_role\": \"${role}\" }
        }"
      echo ""
    }

    create_user "bearbeiter@example.com" "TestPassword123!" "bearbeiter"
    create_user "leser@example.com" "TestPassword123!" "leser"
  '
  echo "==> Abgeschlossen."
  exit 0
fi

if [[ -z "$SERVICE_KEY" ]]; then
  echo "Fehler: --service-key erforderlich, wenn nicht --vm genutzt wird."
  echo "Beispiel: ./seed_users.sh --url http://35.246.185.192:8000 --service-key <SERVICE_ROLE_KEY>"
  exit 1
fi

create_user_api() {
  local email="$1"
  local pass="$2"
  local role="$3"

  echo "--> Erstelle ${email} (${role}) über ${URL}..."
  curl -s -X POST "${URL}/auth/v1/admin/users" \
    -H "Authorization: Bearer ${SERVICE_KEY}" \
    -H "apikey: ${SERVICE_KEY}" \
    -H "Content-Type: application/json" \
    -d "{
      \"email\": \"${email}\",
      \"password\": \"${pass}\",
      \"email_confirm\": true,
      \"user_metadata\": { \"gpp_role\": \"${role}\" },
      \"app_metadata\": { \"gpp_role\": \"${role}\" }
    }"
  echo ""
}

create_user_api "bearbeiter@example.com" "TestPassword123!" "bearbeiter"
create_user_api "leser@example.com" "TestPassword123!" "leser"

echo "==> Fertig! Testbenutzer angelegt."
