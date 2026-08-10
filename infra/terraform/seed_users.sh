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

  # Das Remote-Skript geht per stdin auf die VM — kein Quoting-Ringkampf mit
  # der äußeren Shell, Single-Quotes im SQL bleiben erlaubt.
  TMP_SCRIPT="$(mktemp)"
  cat > "$TMP_SCRIPT" <<'REMOTE'
set -euo pipefail
SR_KEY=$(sudo grep "^SERVICE_ROLE_KEY=" /opt/gpp/supabase/.env | cut -d= -f2-)

create_user() {
  local email="$1"
  local pass="$2"

  echo "--> Erstelle/Aktualisiere ${email}..."
  curl -s -X POST "http://localhost:8000/auth/v1/admin/users" \
    -H "Authorization: Bearer ${SR_KEY}" \
    -H "apikey: ${SR_KEY}" \
    -H "Content-Type: application/json" \
    -d "{\"email\": \"${email}\", \"password\": \"${pass}\", \"email_confirm\": true}"
  echo ""
}

create_user "bearbeiter@example.com" "TestPassword123!"
create_user "leser@example.com" "TestPassword123!"

# Seit Schema v2 lebt die Rolle in public.memberships — ohne Zeile dort sieht
# ein Konto NICHTS (kein Fallback, das ist die Durchsetzung). Upsert für die
# Testkonten und das Admin-Konto aus den Instanz-Metadaten (gpp-admin-email).
if [ "$(sudo docker exec supabase-db psql -U postgres -d postgres -tAc "SELECT count(*) FROM pg_tables WHERE schemaname='public' AND tablename='memberships'")" != "1" ]; then
  echo "FEHLER: Schema fehlt — erst schema.sql einspielen (README Abschnitt 2)."
  exit 1
fi

ADMIN_EMAIL=$(curl -sf -H "Metadata-Flavor: Google" "http://metadata.google.internal/computeMetadata/v1/instance/attributes/gpp-admin-email" || true)
echo "--> Mitgliedschaften upserten (admin: ${ADMIN_EMAIL:-keiner})..."
# Admin-E-Mail als psql-Variable übergeben und mit :'admin_email' einsetzen
# (psql quotet selbst) — kein Splicing in die SQL-Zeichenkette, sonst bräche ein
# Apostroph (o'brien@…) die Anweisung oder schleuste SQL ein. Quoted Heredoc
# (<<'SQL'), damit die Shell nichts im Rumpf ersetzt.
sudo docker exec -i supabase-db psql -U postgres -d postgres -v ON_ERROR_STOP=1 \
  -v admin_email="${ADMIN_EMAIL:-niemand@invalid}" <<'SQL'
INSERT INTO public.memberships (user_id, org_id, gpp_role)
SELECT u.id, '00000000-0000-0000-0000-000000000001', v.rolle
  FROM (VALUES ('bearbeiter@example.com', 'bearbeiter'),
               ('leser@example.com', 'leser'),
               (:'admin_email', 'admin')) AS v(email, rolle)
  JOIN auth.users u ON lower(u.email) = lower(v.email)
ON CONFLICT (user_id, org_id) DO UPDATE SET gpp_role = EXCLUDED.gpp_role;
SELECT m.gpp_role, u.email FROM public.memberships m JOIN auth.users u ON u.id = m.user_id ORDER BY 1, 2;
SQL
REMOTE

  CLOUDSDK_METRICS_ENVIRONMENT=datacloud.antigravity gcloud compute ssh gpp-supabase --zone "$ZONE" $PROJECT_FLAG --tunnel-through-iap -- 'bash -s' < "$TMP_SCRIPT"
  rm -f "$TMP_SCRIPT"
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

  echo "--> Erstelle ${email} über ${URL}..."
  curl -s -X POST "${URL}/auth/v1/admin/users" \
    -H "Authorization: Bearer ${SERVICE_KEY}" \
    -H "apikey: ${SERVICE_KEY}" \
    -H "Content-Type: application/json" \
    -d "{\"email\": \"${email}\", \"password\": \"${pass}\", \"email_confirm\": true}"
  echo ""
}

create_user_api "bearbeiter@example.com" "TestPassword123!"
create_user_api "leser@example.com" "TestPassword123!"

echo "==> Konten angelegt."
echo "ACHTUNG: Seit Schema v2 brauchen die Konten zusätzlich Zeilen in"
echo "public.memberships, sonst sehen sie nichts. Die legt nur der --vm-Pfad"
echo "an (braucht psql auf der VM) — diesen einmal nachziehen:"
echo "  ./seed_users.sh --vm --zone <zone> --project <projekt>"
