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

## 4. Berechtigungsmodell und Absicherung

Der springende Punkt zuerst: **Durchgesetzt werden Rechte in der Datenbank, nicht
im Client.** Jede der neun HTML-Werkzeuge könnte manipuliert werden oder durch
`curl` ersetzt sein — die Antwort auf „wer darf was" fällt in PostgreSQL, in den
RLS-Policies und `SECURITY DEFINER`-Funktionen aus [`schema.sql`](./schema.sql).
Die UI-Weichen in `config.html` (etwa: Benutzerverwaltung nur für Admins sichtbar)
sind Komfort, keine Schranke.

### 4.1 Die Kette einer Anfrage

1. **Kong** (Gateway auf :8000) verlangt den `apikey`-Header. Fehlt er, endet die
   Anfrage hier mit `401 „No API key found"` — PostgREST wird nicht erreicht.
2. **PostgREST** verifiziert das JWT gegen `JWT_SECRET` und schaltet auf die
   DB-Rolle aus dem `role`-Claim: nur Anon-Key → Rolle `anon`; eingeloggter
   Benutzer → Rolle `authenticated`. Ohne gültige Signatur kein fremdes `sub`.
3. **GRANTs** entscheiden, ob die Rolle die Tabelle/Funktion überhaupt anfassen
   darf. In Schema v2 hat `anon` hier **kein** Tabellenrecht.
4. **RLS-Policies** filtern zeilenweise nach `auth.uid()`, `auth_org()` und der
   wirksamen Rolle. Default-deny: greift keine Policy, ist die Zeile unsichtbar.
5. **`SECURITY DEFINER`-Funktionen** (die `admin_*`-RPCs, `acquire_set_lock`)
   laufen als `postgres` und prüfen die Berechtigung als **erste** Anweisung,
   vor jeder Verwertung der Eingabe.

### 4.2 Wo die Rolle herkommt (v2 vs. v1)

**Schema v2 (aktueller Stand):** Die Rolle lebt in `public.memberships` (global je
Benutzer) und `public.set_permissions` (abweichend je Set). `auth_gpp_role()` liest
sie dort — **nicht** aus den Token-Claims. Folgen:

* Eine Rechteänderung des Admins greift mit der **nächsten Anfrage**, nicht erst
  nach Ablauf des bis zu einstündigen Access-Tokens.
* Ein Konto **ohne** `memberships`-Zeile hat keine Rolle und sieht nichts. Das ist
  die Durchsetzung, kein Versehen — deshalb `seed_users.sh --vm` nach dem
  Schema-Einspielen (Abschnitt 2).

**Schema v1 (Altstand — nur relevant, falls eine Instanz noch nicht migriert ist):**
`auth_gpp_role()` las die Rolle aus `app_metadata` **und `user_metadata`**. Das
`user_metadata` ist vom Benutzer selbst schreibbar (`PUT /auth/v1/user`, und beim
Signup über das `data`-Feld). Damit war eine **Privilege Escalation** möglich:
Rolle auf `admin` setzen und durchgreifen. v2 schließt das — Metadaten spielen für
Rechte keine Rolle mehr.

### 4.3 Rechte je Rolle (Plan §4)

| Rolle | Lesen | Schreiben | Sperren | Verwaltung |
|---|---|---|---|---|
| `leser` | alle Sets der Org | — | — | — |
| `bearbeiter` | alle Sets der Org | alles **außer** `ap`/`ar` | ja | — |
| `pruefer` | alle Sets der Org | nur `ap`/`ar`/`poam` | — | — |
| `admin` | alle Sets der Org | alles | ja, plus fremde brechen | Konten, Rollen, Set-Rechte |

Die `bearbeiter`/`pruefer`-Trennung fällt auf die Spalte `kind` und steckt in
`gpp_can_write(set_name, kind)`, das die INSERT/UPDATE/DELETE-Policies von
`artefacts` auswerten. Ein **Set-Recht** (`set_permissions`) schlägt für genau
dieses Set die globale Rolle; ein globaler `admin` lässt sich so nicht
herabstufen, und `admin` ist je Set nicht vergebbar.

### 4.4 Was ein Unauthentifizierter kann: nichts Datenrelevantes

| Zugang | Lesen `artefacts` | Schreiben |
|---|---|---|
| **kein `apikey`** | `401` an Kong — kommt nicht durch | `401` |
| **nur Anon-Key, kein Login** (v2) | Fehler: `anon` hat kein Tabellenrecht (`REVOKE ALL … FROM anon`) | Fehler (GRANT) |
| **nur Anon-Key, kein Login** (v1) | `200`, aber **0 Zeilen** — keine Policy für `anon`, RLS default-deny | `42501` (RLS) |

Der Anon-Key ist **öffentlich** (er steckt in jeder `config.html`); „kennt den
Anon-Key" ist also kein Vertrauensmerkmal. Er darf per Design an die
Auth-Endpunkte (`/auth/v1/token`, `/authorize`) — sonst könnte sich niemand
anmelden. Alles dahinter ist zu.

> **Signup abschalten.** Ist `/auth/v1/signup` offen, kann ein Unbekannter mit dem
> Anon-Key ein Konto anlegen. Unter **v2** ist das folgenlos (kein `membership`
> → keine Rechte). Unter **v1** wäre es die oben genannte Escalation, jetzt sogar
> ohne Bestandskonto. Auf der Testinstanz `GOTRUE_DISABLE_SIGNUP=true` setzen;
> Konten legt der Admin an.

### 4.5 Benutzerverwaltung durch den Admin

Über `config.html` → „Zusammenarbeit" (nur sichtbar, wenn `whoami` die Rolle
`admin` meldet). Jede Aktion ruft eine RPC, die als erste Zeile
`gpp_require_admin()` ausführt — ein `bearbeiter`, ein `leser` oder ein Konto ohne
Mitgliedschaft bekommt `„nur admin"` (HTTP 400), die Transaktion rollt zurück:

| RPC | Wirkung |
|---|---|
| `admin_list_users` | Konten der Org mit globaler Rolle und Set-Rechten |
| `admin_create_user` | Konto **und** `membership` anlegen (Startpasswort ≥ 10 Zeichen) |
| `admin_delete_user` | Konto löschen (nicht das eigene) |
| `admin_set_role` | globale Rolle setzen (eigene `admin`-Rolle nicht selbst abgeben) |
| `admin_set_set_role` / `admin_clear_set_role` | Set-Recht vergeben/entziehen |

`admin_create_user` schreibt direkt in `auth.users` — der pragmatische Weg für den
Test-Stack, weil der Browser den `SERVICE_ROLE_KEY` nie sehen darf. **Produktiv**
gehört dort die GoTrue-Admin-API hin (wie in `seed_users.sh`).

### 4.6 Nachvollziehbarkeit

Jede Schreiboperation auf `artefacts`, `set_locks`, `memberships` und
`set_permissions` erzeugt per Trigger eine Zeile in `public.audit` (Wer, Was,
Wann — ohne den Dokumentinhalt). `org` und `updated_by` stempelt der Server aus
der Sitzung; was der Client mitschickt, wird überschrieben. `audit` liest nur der
Admin.

### 4.7 Abnahme (curl, nach dem Einspielen von v2)

Kurzform — die Berechtigungsgrenzen einmal durchfahren. `$ANON` = Anon-Key,
`$B` = Basis-URL. Access-Token je Konto vorab über `/auth/v1/token` holen.

```bash
# 1. Ohne apikey → 401 an Kong
curl -s -o /dev/null -w "%{http_code}\n" "$B/rest/v1/artefacts"            # erwartet 401

# 2. Nur Anon-Key, kein Login → kein Datenzugriff
curl -s -H "apikey: $ANON" "$B/rest/v1/artefacts?limit=1"                  # v2: Fehler/leer, nie Daten
curl -s -H "apikey: $ANON" -X POST "$B/rest/v1/artefacts" -d '{...}'       # erwartet 401/42501

# 3. leser darf nicht schreiben
curl -s -H "apikey: $ANON" -H "Authorization: Bearer $LESER" \
  -X POST "$B/rest/v1/artefacts" -d '{...}'                                # erwartet 42501

# 4. bearbeiter darf kein ap/ar
curl -s -H "apikey: $ANON" -H "Authorization: Bearer $BEARB" \
  -X POST "$B/rest/v1/artefacts" -d '{"kind":"ar", ...}'                   # erwartet 42501

# 5. Nicht-Admin an der Verwaltung
curl -s -H "apikey: $ANON" -H "Authorization: Bearer $BEARB" \
  -X POST "$B/rest/v1/rpc/admin_create_user" \
  -d '{"p_email":"x@y.de","p_password":"0123456789","p_gpp_role":"leser"}' # erwartet "nur admin"

# 6. Fremde Sperre brechen als bearbeiter (nicht Halter) → verweigert
curl -s -H "apikey: $ANON" -H "Authorization: Bearer $BEARB" \
  -X DELETE "$B/rest/v1/set_locks?set_name=eq.fremdes-set"                 # löscht 0 Zeilen
```

---

## 5. Kosten und Aufräumen

Rund 45–55 € im Monat in `europe-west3` für `e2-standard-2`, 50 GB Platte und die feste IP.
VM stoppen zwischen Testtagen:
```bash
gcloud compute instances stop gpp-supabase --zone europe-west3-b
```

Vollständig entfernen:
```bash
terraform destroy
```
