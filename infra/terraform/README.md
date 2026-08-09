# Testumgebung für das Datenbank-Backend (GCP)

Baut die Referenzinstallation aus [`PLAN_Datenbank-Backend.md`](../../PLAN_Datenbank-Backend.md)
auf einer einzelnen Compute-Engine-VM: PostgreSQL, GoTrue und PostgREST als
Supabase-Compose-Stack, davor optional Caddy als TLS-Endpunkt und statischer
Host für die Werkzeuge aus `GS++-oscal-app/`.

Bewusst **kein** Cloud SQL und **kein** Cloud Run: das wären VPC-Connector,
Cloud-SQL-Proxy und zwei Dienstbereitstellungen zusätzlich — und der Aufbau
wiche von dem ab, was Anwender nach Phase 5 selbst betreiben. Fehler, die hier
auftreten, sollen dieselben sein, die dort auftreten.

## Was entsteht

| Ressource | Zweck |
|---|---|
| VPC + Subnetz `10.10.0.0/24` | eigenes Netz, Flow-Logs an |
| Firewall `allow-iap` | 22, 5432, 8000 **nur** aus `35.235.240.0/20` (IAP) |
| Firewall `allow-kong-external` | Port 8000 für externe Test-Agenten freigegeben |
| Firewall `allow-acme` / `allow-https` | nur mit `domain`: 80 offen für Let's Encrypt, 443 für `allowed_cidrs` |
| Feste externe IP | damit `API_EXTERNAL_URL` ein Stop/Start überlebt (`35.246.185.192`) |
| VM `gpp-supabase` | Debian 12, Shielded VM, Docker + Compose-Stack |
| Dienstkonto | `logWriter`, `metricWriter`, `secretAccessor` auf genau drei Secrets |
| Drei Secrets | Postgres-Passwort, `JWT_SECRET`, Studio-Passwort |

---

## 1. Installation & Infrastructure Provisioning

### Voraussetzungen
* Ein GCP-Projekt mit aktiver Abrechnung (`project_id="gpp-agentic-3"`).
* Lokale Werkzeuge: `terraform`, `gcloud`, und `gcloud auth application-default login`.

### Anlegen der Infrastruktur
```bash
cd infra/terraform
cp terraform.tfvars.example terraform.tfvars
# project_id = "gpp-agentic-3" eintragen
terraform init
terraform apply -auto-approve
```

Fortschritt des ersten Boots prüfen:
```bash
gcloud compute ssh gpp-supabase --zone europe-west3-b --tunnel-through-iap -- 'sudo tail -f /var/log/gpp-startup.log'
```

---

## 2. Datenbank-Schema & Testbenutzer anlegen

### Schema einspielen (`schema.sql`)
Kopiere `schema.sql` auf die VM und spiele Tabellen, RLS-Policies und Helper-Funktionen ein:

```bash
gcloud compute scp --tunnel-through-iap --zone europe-west3-b schema.sql gpp-supabase:/tmp/schema.sql
gcloud compute ssh gpp-supabase --zone europe-west3-b --tunnel-through-iap -- 'sudo docker exec -i supabase-db psql -U postgres -d postgres < /tmp/schema.sql'
```

### Testbenutzer erzeugen (`seed_users.sh`)
Verwende das mitgelieferte Skript `seed_users.sh`, um `bearbeiter@example.com` und `leser@example.com` anzulegen:

```bash
# Option A: Direkt über SSH auf der VM ausführen (empfohlen)
./seed_users.sh --vm --zone europe-west3-b --project gpp-agentic-3

# Option B: Direkt über die öffentliche API (mit Service Role Key)
./seed_users.sh --url http://35.246.185.192:8000 --service-key <SERVICE_ROLE_KEY>
```

#### Erstellte Testkonten
| Email | Passwort | Rolle (`gpp_role`) | Zweck |
|---|---|---|---|
| `bearbeiter@example.com` | `TestPassword123!` | `bearbeiter` | Kann Sets sperren & Artefakte schreiben (außer `ap`/`ar`). |
| `leser@example.com` | `TestPassword123!` | `leser` | Nur-Lese-Zugriff. Schreibversuche scheitern an RLS. |

---

## 3. Testen & Anbindung für Entwicklung/Agenten

### A. Direktes Testen über die öffentliche IP (für externe Agenten)

* **Öffentliche Basis-URL**: `http://35.246.185.192:8000`
* **GoTrue Auth**: `POST http://35.246.185.192:8000/auth/v1/token?grant_type=password`
* **PostgREST API**: `http://35.246.185.192:8000/rest/v1/`
* **`ANON_KEY`**:
  `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlzcyI6InN1cGFiYXNlIiwiaWF0IjoxNzg2MjY0NTM0LCJleHAiOjIxMDE2MjQ1MzR9.uB71k-N3jfAH1EPP98zSf_9ijK5CUMo0xHCTlXmgXjo`

#### Auth-Token anfordern (`curl` Example)
```bash
curl -s -X POST "http://35.246.185.192:8000/auth/v1/token?grant_type=password" \
  -H "Content-Type: application/json" \
  -H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlzcyI6InN1cGFiYXNlIiwiaWF0IjoxNzg2MjY0NTM0LCJleHAiOjIxMDE2MjQ1MzR9.uB71k-N3jfAH1EPP98zSf_9ijK5CUMo0xHCTlXmgXjo" \
  -d '{
    "email": "bearbeiter@example.com",
    "password": "TestPassword123!"
  }'
```

#### Artefakte abfragen (Authentifiziert)
```bash
curl -s -X GET "http://35.246.185.192:8000/rest/v1/artefacts" \
  -H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlzcyI6InN1cGFiYXNlIiwiaWF0IjoxNzg2MjY0NTM0LCJleHAiOjIxMDE2MjQ1MzR9.uB71k-N3jfAH1EPP98zSf_9ijK5CUMo0xHCTlXmgXjo" \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

### B. Testen über IAP-Tunnel (Lokale Entwicklung)

Kong per Tunnel auf den eigenen Rechner holen:
```bash
gcloud compute start-iap-tunnel gpp-supabase 8000 --local-host-port=localhost:8000 --zone europe-west3-b
```

PostgreSQL Tunnel für `psql` (Port 5432 → Local 5433):
```bash
gcloud compute start-iap-tunnel gpp-supabase 5432 --local-host-port=localhost:5433 --zone europe-west3-b
```

---

## 4. Kosten und Aufräumen

Rund 45–55 € im Monat in `europe-west3` für `e2-standard-2`, 50 GB Platte und die feste IP.
VM stoppen zwischen Testtagen:
```bash
gcloud compute instances stop gpp-supabase --zone europe-west3-b
```

Vollständig entfernen:
```bash
terraform destroy
```
