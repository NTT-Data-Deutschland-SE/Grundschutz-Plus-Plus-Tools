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

## 2. Automatische Inhalts-Einrichtung (Schema & Admin-Konto)

Das Startskript der VM (`startup.sh`) übernimmt beim Erststart automatisch:
1. **Schema-Einspielung**: `schema.sql` wird aus den Instanz-Metadaten gelesen und direkt beim ersten Boot in die PostgreSQL-Datenbank eingespielt.
2. **Admin-Konto**: Das Anwendungskonto `admin@example.com` (konfigurierbar über `var.admin_email`) wird über GoTrue angelegt. Das zugehörige Admin-Passwort wird von Terraform zufällig erzeugt und im Secret Manager abgelegt:
   ```bash
   gcloud secrets versions access latest --secret=gpp-admin-password
   ```
3. **Optionale Testbenutzer**: Über die Variable `seed_test_users = true` (Voreinstellung: `false`) in `terraform.tfvars` können die Testkonten `bearbeiter@example.com` und `leser@example.com` automatisch mit-angelegt werden.

### Testbenutzer manuell/nachträglich anlegen (`seed_users.sh`)
Über das Skript `seed_users.sh` lassen sich `bearbeiter@example.com` und `leser@example.com` auch jederzeit manuell nachpflegen:

```bash
# Direkt über SSH auf der VM ausführen:
./seed_users.sh --vm --zone europe-west3-b --project gpp-agentic-3
```

#### Standard-Testkonten (wenn aktiviert oder ge-seedet)
| Email | Passwort | Rolle (`gpp_role`) | Zweck |
|---|---|---|---|
| `admin@example.com` | *(Secret Manager)* | `admin` | Admin-Zugriff, Benutzerverwaltung in `config.html`. |
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
