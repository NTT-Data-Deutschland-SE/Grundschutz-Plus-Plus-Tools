#!/usr/bin/env bash
#
# Startskript der Supabase-Testinstanz. Läuft als root bei jedem Boot und ist
# idempotent: die .env wird genau einmal erzeugt, alles Weitere ist ein
# Abgleich. Protokoll: /var/log/gpp-startup.log, zusätzlich im Serial Port.
#
set -euo pipefail
exec > >(tee -a /var/log/gpp-startup.log | logger -t gpp-startup -s 2>/dev/console) 2>&1

STACK_DIR=/opt/gpp/supabase
APP_DIR=/opt/gpp/app
MD=http://metadata.google.internal/computeMetadata/v1

meta() {
  curl -sf -H "Metadata-Flavor: Google" "$MD/instance/attributes/$1" || true
}

PROJECT="$(curl -sf -H "Metadata-Flavor: Google" "$MD/project/project-id")"
DOMAIN="$(meta gpp-domain)"
SUPABASE_REF="$(meta gpp-supabase-ref)"
ADMIN_EMAIL="$(meta gpp-admin-email)"
SECRET_PG="$(meta gpp-secret-pg)"
SECRET_JWT="$(meta gpp-secret-jwt)"
SECRET_DASH="$(meta gpp-secret-dash)"
SECRET_ADMIN="$(meta gpp-secret-admin)"

secret() {
  local token
  token="$(curl -sf -H "Metadata-Flavor: Google" \
    "$MD/instance/service-accounts/default/token" \
    | python3 -c 'import sys,json;print(json.load(sys.stdin)["access_token"])')"
  curl -sf -H "Authorization: Bearer $token" \
    "https://secretmanager.googleapis.com/v1/projects/$PROJECT/secrets/$1/versions/latest:access" \
    | python3 -c 'import sys,json,base64;print(base64.b64decode(json.load(sys.stdin)["payload"]["data"]).decode(),end="")'
}

# Supabase erwartet ANON_KEY und SERVICE_ROLE_KEY als HS256-JWT über demselben
# JWT_SECRET, mit dem PostgREST prüft. Zehn Jahre Laufzeit ist das, was der
# offizielle Generator ausstellt — es sind Dienstschlüssel, keine Sitzungen.
gen_jwt() {
  python3 - "$1" "$2" <<'PY'
import base64, hmac, hashlib, json, sys, time

secret, role = sys.argv[1], sys.argv[2]

def b64(raw: bytes) -> str:
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode()

def part(obj) -> str:
    return b64(json.dumps(obj, separators=(",", ":")).encode())

iat = int(time.time())
head = part({"alg": "HS256", "typ": "JWT"})
body = part({"role": role, "iss": "supabase", "iat": iat, "exp": iat + 315360000})
sig = b64(hmac.new(secret.encode(), f"{head}.{body}".encode(), hashlib.sha256).digest())
print(f"{head}.{body}.{sig}", end="")
PY
}

# --------------------------------------------------------------------------
# Pakete
# --------------------------------------------------------------------------
export DEBIAN_FRONTEND=noninteractive

if ! command -v docker >/dev/null 2>&1; then
  echo "== Docker installieren"
  apt-get update -qq
  apt-get install -y -qq ca-certificates curl gnupg git
  install -m 0755 -d /etc/apt/keyrings
  curl -fsSL https://download.docker.com/linux/debian/gpg \
    | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
  chmod a+r /etc/apt/keyrings/docker.gpg
  echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian bookworm stable" \
    > /etc/apt/sources.list.d/docker.list
  apt-get update -qq
  apt-get install -y -qq docker-ce docker-ce-cli containerd.io docker-compose-plugin
  systemctl enable --now docker
fi

if [ -n "$DOMAIN" ] && ! command -v caddy >/dev/null 2>&1; then
  echo "== Caddy installieren"
  apt-get install -y -qq debian-keyring debian-archive-keyring apt-transport-https
  curl -fsSL https://dl.cloudsmith.io/public/caddy/stable/gpg.key \
    | gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
  echo "deb [signed-by=/usr/share/keyrings/caddy-stable-archive-keyring.gpg] https://dl.cloudsmith.io/public/caddy/stable/deb/debian any-version main" \
    > /etc/apt/sources.list.d/caddy-stable.list
  apt-get update -qq
  apt-get install -y -qq caddy
fi

# --------------------------------------------------------------------------
# Supabase-Compose-Verzeichnis holen (nur docker/, ohne Repo-Historie)
# --------------------------------------------------------------------------
mkdir -p /opt/gpp "$APP_DIR"

if [ ! -f /opt/gpp/.checked-out ]; then
  echo "== supabase/docker auschecken ($SUPABASE_REF)"
  rm -rf /opt/gpp/supabase-src
  # --depth 1 --branch klappt nur bei Zweigen und Tags; für einen Commit-SHA
  # greift der zweite Versuch ohne Tiefenbegrenzung.
  git clone --filter=blob:none --no-checkout --depth 1 \
    --branch "$SUPABASE_REF" https://github.com/supabase/supabase /opt/gpp/supabase-src \
    || git clone --filter=blob:none --no-checkout \
         https://github.com/supabase/supabase /opt/gpp/supabase-src
  git -C /opt/gpp/supabase-src sparse-checkout set --cone docker
  git -C /opt/gpp/supabase-src checkout "$SUPABASE_REF"
  mkdir -p "$STACK_DIR"
  cp -a /opt/gpp/supabase-src/docker/. "$STACK_DIR/"
  git -C /opt/gpp/supabase-src rev-parse HEAD > /opt/gpp/.checked-out
fi

cd "$STACK_DIR"

# --------------------------------------------------------------------------
# .env — einmalig aus der mitgelieferten Vorlage, dann gezielt überschrieben.
# Die Vorlage zu patchen statt sie zu ersetzen hält das Ganze über
# Supabase-Versionen hinweg am Leben: neue Pflichtvariablen kommen mit.
# --------------------------------------------------------------------------
if [ ! -f .env ]; then
  echo "== .env erzeugen"
  cp .env.example .env

  PG_PASS="$(secret "$SECRET_PG")"
  JWT_SECRET="$(secret "$SECRET_JWT")"
  DASH_PASS="$(secret "$SECRET_DASH")"
  ANON_KEY="$(gen_jwt "$JWT_SECRET" anon)"
  SERVICE_KEY="$(gen_jwt "$JWT_SECRET" service_role)"

  if [ -n "$DOMAIN" ]; then
    PUBLIC_URL="https://$DOMAIN"
  else
    PUBLIC_URL="http://localhost:8000"
  fi

  setenv() {
    local key="$1" value="$2"
    if grep -q "^$key=" .env; then
      python3 - "$key" "$value" <<'PY'
import sys, pathlib
key, value = sys.argv[1], sys.argv[2]
p = pathlib.Path(".env")
lines = p.read_text().splitlines()
p.write_text("\n".join(f"{key}={value}" if l.startswith(f"{key}=") else l for l in lines) + "\n")
PY
    else
      echo "$key=$value" >> .env
    fi
  }

  setenv POSTGRES_PASSWORD    "$PG_PASS"
  setenv JWT_SECRET           "$JWT_SECRET"
  setenv ANON_KEY             "$ANON_KEY"
  setenv SERVICE_ROLE_KEY     "$SERVICE_KEY"
  setenv DASHBOARD_USERNAME   "gpp"
  setenv DASHBOARD_PASSWORD   "$DASH_PASS"
  setenv SITE_URL             "$PUBLIC_URL"
  setenv API_EXTERNAL_URL     "$PUBLIC_URL"
  setenv SUPABASE_PUBLIC_URL  "$PUBLIC_URL"
  setenv SECRET_KEY_BASE      "$(head -c 48 /dev/urandom | base64 | tr -d '=+/' | head -c 64)"
  setenv VAULT_ENC_KEY        "$(head -c 32 /dev/urandom | base64 | tr -d '=+/' | head -c 32)"

  chmod 600 .env
fi

# --------------------------------------------------------------------------
# Stack starten
# --------------------------------------------------------------------------
echo "== Compose-Stack starten"
docker compose pull -q || true
docker compose up -d

cat > /etc/systemd/system/gpp-supabase.service <<'UNIT'
[Unit]
Description=GS++ Supabase-Stack
Requires=docker.service
After=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=/opt/gpp/supabase
ExecStart=/usr/bin/docker compose up -d
ExecStop=/usr/bin/docker compose down

[Install]
WantedBy=multi-user.target
UNIT
systemctl daemon-reload
systemctl enable gpp-supabase.service

# --------------------------------------------------------------------------
# Caddy: Werkzeuge und API unter demselben Ursprung. Damit erübrigt sich die
# CORS-Konfiguration, statt sie zu erfordern — und Phase-0-Frage 1 des Plans
# ist beantwortet, ohne den Offline-Betrieb per Doppelklick anzutasten.
# Studio bleibt bewusst draußen; es ist nur durch den IAP-Tunnel auf :8000
# erreichbar.
# --------------------------------------------------------------------------
if [ -n "$DOMAIN" ]; then
  echo "== Caddy konfigurieren für $DOMAIN"
  cat > /etc/caddy/Caddyfile <<CADDY
$DOMAIN {
	encode gzip

	@api path /rest/* /auth/* /realtime/* /storage/* /functions/*
	handle @api {
		reverse_proxy localhost:8000
	}

	handle {
		root * $APP_DIR
		file_server browse
	}

	log {
		output file /var/log/caddy/access.log
	}
}
CADDY
  mkdir -p /var/log/caddy
  chown -R caddy:caddy /var/log/caddy
  systemctl enable caddy
  systemctl reload-or-restart caddy
fi

# --------------------------------------------------------------------------
# Admin-Konto der Anwendung sicherstellen (Rolle admin, Plan §4). Läuft bei
# jedem Boot: Anlegen über die GoTrue-Admin-API ist idempotent (422 wenn es
# das Konto gibt), die Mitgliedschaft ist ein Upsert. Liegt das Schema noch
# nicht in der Datenbank (memberships fehlt), wird nur das Konto angelegt —
# seed_users.sh holt die Mitgliedschaft nach dem Schema-Einspielen nach.
# --------------------------------------------------------------------------
if [ -n "$ADMIN_EMAIL" ] && [ -n "$SECRET_ADMIN" ]; then
  echo "== Admin-Konto sicherstellen ($ADMIN_EMAIL)"
  SR_KEY="$(grep '^SERVICE_ROLE_KEY=' "$STACK_DIR/.env" | cut -d= -f2-)"
  ADMIN_PASS="$(secret "$SECRET_ADMIN")"

  for i in $(seq 1 30); do
    curl -sf -o /dev/null -H "apikey: $SR_KEY" http://localhost:8000/auth/v1/health && break
    sleep 2
  done

  curl -s -o /tmp/gpp-admin-create.json -X POST http://localhost:8000/auth/v1/admin/users \
    -H "Authorization: Bearer $SR_KEY" -H "apikey: $SR_KEY" \
    -H "Content-Type: application/json" \
    -d "{\"email\":\"$ADMIN_EMAIL\",\"password\":\"$ADMIN_PASS\",\"email_confirm\":true}" || true

  # Mitgliedschaft direkt in der DB — die Rolle lebt seit Schema v2 in
  # public.memberships, nicht in den Token-Claims.
  docker exec -i supabase-db psql -U postgres -d postgres -v ON_ERROR_STOP=0 <<SQL || true
DO \$\$
DECLARE v_id uuid;
BEGIN
  IF to_regclass('public.memberships') IS NULL THEN
    RAISE NOTICE 'Schema noch nicht eingespielt - Mitgliedschaft folgt mit seed_users.sh';
    RETURN;
  END IF;
  SELECT id INTO v_id FROM auth.users WHERE lower(email) = lower('$ADMIN_EMAIL');
  IF v_id IS NULL THEN
    RAISE NOTICE 'Admin-Konto nicht gefunden';
    RETURN;
  END IF;
  INSERT INTO public.memberships (user_id, org_id, gpp_role)
  VALUES (v_id, '00000000-0000-0000-0000-000000000001', 'admin')
  ON CONFLICT (user_id, org_id) DO UPDATE SET gpp_role = 'admin';
END
\$\$;
SQL
fi

echo "== fertig"
