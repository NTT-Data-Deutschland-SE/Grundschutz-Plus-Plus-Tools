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
| Firewall `allow-acme` / `allow-https` | nur mit `domain`: 80 offen für Let's Encrypt, 443 für `allowed_cidrs` |
| Feste externe IP | damit `API_EXTERNAL_URL` ein Stop/Start überlebt |
| VM `gpp-supabase` | Debian 12, Shielded VM, Docker + Compose-Stack |
| Dienstkonto | `logWriter`, `metricWriter`, `secretAccessor` auf genau drei Secrets |
| Drei Secrets | Postgres-Passwort, `JWT_SECRET`, Studio-Passwort |
| A-Record | optional, nur bei Cloud DNS im selben Projekt |
| Budget-Alarm | optional, 50/90/100 Prozent |

Port 5432 ist **nicht** öffentlich erreichbar — er steht nur im IAP-Bereich
offen, damit Migrationen per `psql` durch den Tunnel laufen können.

## Voraussetzungen

* Ein GCP-Projekt mit aktiver Abrechnung.
* Auf dem eigenen Rechner: `terraform`, `gcloud`, und
  `gcloud auth application-default login`.
* Eigene Rolle im Projekt: `roles/owner` genügt fürs Erste; minimal sind
  `compute.admin`, `iam.serviceAccountAdmin`, `secretmanager.admin`,
  `serviceusage.serviceUsageAdmin` und `resourcemanager.projectIamAdmin`.
* Für SSH zusätzlich `roles/compute.osLogin` und `roles/iap.tunnelResourceAccessor`.
* Das Budget nur mit `roles/billing.costsManager` auf dem Abrechnungskonto.

## Anlegen

```bash
cd infra/terraform && cp terraform.tfvars.example terraform.tfvars && terraform init && terraform apply
```

Der erste Boot lädt Docker-Images und braucht ein paar Minuten. Fortschritt:

```bash
gcloud compute ssh gpp-supabase --zone europe-west3-b --tunnel-through-iap -- 'sudo tail -f /var/log/gpp-startup.log'
```

## Phase 1 abnehmen — ohne einen offenen Port

`domain` bleibt leer. Kong per Tunnel auf den eigenen Rechner holen:

```bash
gcloud compute start-iap-tunnel gpp-supabase 8000 --local-host-port=localhost:8000 --zone europe-west3-b
```

`ANON_KEY` und `SERVICE_ROLE_KEY` stehen in `/opt/gpp/supabase/.env` auf der VM.
Danach ist die Abnahme aus dem Plan — zwei parallele `curl`-Sitzungen um die
Sperre, `leser` scheitert am Schreiben, `bearbeiter` an `kind = 'ar'` — direkt
gegen `http://localhost:8000/rest/v1/...` fahrbar. Studio liegt unter
`http://localhost:8000` (Benutzer `gpp`, Passwort aus dem Secret).

Migrationen einspielen, zweiter Tunnel:

```bash
gcloud compute start-iap-tunnel gpp-supabase 5432 --local-host-port=localhost:5433 --zone europe-west3-b
```

```bash
psql "postgresql://postgres:$(gcloud secrets versions access latest --secret=gpp-postgres-password)@localhost:5433/postgres" -f schema.sql
```

## Phase 2 vorbereiten — Hostname und statischer Host

`domain` und `allowed_cidrs` setzen, `terraform apply`, dann die Werkzeuge
hochladen:

```bash
gcloud compute scp --recurse --tunnel-through-iap --zone europe-west3-b ../../GS++-oscal-app/. gpp-supabase:/opt/gpp/app/
```

Caddy liefert `/` aus diesem Verzeichnis und reicht `/rest/*`, `/auth/*`,
`/realtime/*` und `/storage/*` an Kong weiter. Werkzeuge und API liegen damit
unter **demselben Ursprung**: die CORS-Frage entfällt, statt konfiguriert zu
werden, und `Origin: null` aus `file://` muss nirgends zugelassen werden — die
Phase-0-Frage 1 des Plans ist damit praktisch beantwortet, ohne dass der
Doppelklick-Betrieb für alle anderen etwas verliert.

Studio ist über den öffentlichen Namen absichtlich **nicht** erreichbar; dafür
bleibt der Tunnel.

## Kosten und Aufräumen

Rund 45–55 € im Monat in `europe-west3` für `e2-standard-2`, 50 GB Platte und
die feste IP. Zwischen den Testtagen:

```bash
gcloud compute instances stop gpp-supabase --zone europe-west3-b
```

Der Stack kommt beim nächsten Start über `gpp-supabase.service` von selbst
wieder hoch; es fallen dann nur Platte und IP an. Vollständig entfernen mit
`terraform destroy` — die aktivierten APIs bleiben absichtlich stehen.

## Was hier nicht drin ist

* **Ein IdP für Pfad B.** Zum Testen genügt ein Keycloak-Container neben dem
  Stack — kein GCP-Bedarf, und Gruppen-Claims für `org`/`gpp_role` lassen sich
  frei erfinden. Entra ID erst, wenn gegen das getestet werden soll, was
  Anwender tatsächlich betreiben; dafür wird der Hostname von oben gebraucht.
* **Sicherung.** Für eine Wegwerfinstanz absichtlich nicht eingebaut. Sobald
  Inhalte drin stehen, die weh tun: Snapshot-Zeitplan auf die Bootplatte.
* **Härtung fürs Produktivsystem.** Das hier ist eine Testinstanz. Die
  Zufallspasswörter liegen im Terraform-State — der gehört entsprechend
  behandelt (Remote-State im GCS-Bucket mit Versionierung, nicht ins Git).
