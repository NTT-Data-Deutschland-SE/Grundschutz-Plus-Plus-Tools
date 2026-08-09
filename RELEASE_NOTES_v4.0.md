# Grundschutz++ OSCAL Tools – Version 4.0

Version 3 hat die neun Werkzeuge auf eine gemeinsame Basis gestellt und einen geteilten Artefaktbestand im Browser eingeführt. Version 4 öffnet diesen Bestand über den einzelnen Rechner hinaus: eine **optionale gemeinsame Datenbank**, in der ein Team an denselben Sets arbeitet, mit serverseitig durchgesetzten Rechten und einer beratenden Sperre gegen gleichzeitiges Schreiben. Der entscheidende Satz bleibt gültig und bleibt richtig: **ohne hinterlegten Server verhält sich alles exakt wie bisher — offline, ohne Backend, nur der Browser.**

Umgesetzt sind damit die Phasen 2 und 3 aus `PLAN_Datenbank-Backend.md`.

## Neu: Zusammenarbeit über eine gemeinsame Datenbank

Wer in `config.html` eine Server-URL hinterlegt und sich anmeldet, dessen Speichervorgänge gehen **zusätzlich** in eine gemeinsame PostgreSQL-Datenbank (PostgREST + GoTrue, als Supabase-Stack — self-hosted oder gehostet, derselbe Client-Code). Alles andere bleibt, wie es war.

**Lokal zuerst — die Datenbank ist ein Ziel, kein Nadelöhr.** Jedes Werkzeug speichert wie bisher in die IndexedDB und liefert zurück; der Push an den Server hängt daran, nicht davor. Ein Netzausfall verliert nichts und blockiert nichts: fehlgeschlagene Übertragungen warten in einer Outbox und gehen bei nächster Verbindung raus. Das automatische Dauerspeichern des POA&M-Generators wird dabei entprellt, damit aus Dutzenden Änderungen pro Minute nicht Dutzende Anfragen werden.

**Konflikte werden benannt, nicht überschrieben.** Der ohnehin berechnete `sha256` dient als Version. Trägt der Server inzwischen eine fremde Änderung, gewinnt niemand automatisch — das Werkzeug meldet den Konflikt und bietet Übernehmen oder Erzwingen an. Bei gehaltener Sperre tritt das praktisch nie auf; tritt es doch auf, ist es ein echter Befund.

**Ein Status-Chip** unten in jedem Werkzeug zeigt den Zustand: lokal, ausstehend, synchron oder Konflikt. Er hängt sich selbst ein — kein Eingriff in die einzelnen Werkzeuge.

**Zwei Anmeldewege, ein Token.** E-Mail und Passwort für kleine Teams und Einzelinstallationen; alternativ der Unternehmens-IdP über OIDC (der Browser wird umgeleitet, GoTrue führt den Code-Austausch serverseitig — der fehleranfälligste Teil wird bewusst nicht selbst gebaut). Für die Werkzeuge dahinter ist beides dasselbe Token.

**Was den Browser nie verlässt:** API-Schlüssel, GitHub-Token und Prompts. Die sind persönlich und gehören nicht in einen geteilten Bestand. Vom Sitzungszustand liegt nur das kurzlebige Refresh-Token im Browser; das Passwort wird nirgends gespeichert.

## Neu: Rollen und Rechte — in der Datenbank durchgesetzt

Vier Rollen, angelehnt an die tatsächliche Arbeitsteilung (Plan §4):

| Rolle | Darf |
|---|---|
| `leser` | Alle Sets der Organisation lesen. Kein Schreiben, keine Sperre. |
| `bearbeiter` | Sets sperren und darin schreiben — Kataloge, Profile, SSP, Workspaces. **Nicht** `ap`/`ar`. |
| `pruefer` | Wie `leser`, zusätzlich `ap`, `ar`, `poam` schreiben. Trennt Prüfung von Erstellung. |
| `admin` | Alles, plus Benutzerverwaltung, plus fremde Sperren brechen. |

Der springende Punkt: **Durchgesetzt wird in der Datenbank, nicht im Client.** Jedes Werkzeug ließe sich manipulieren oder durch `curl` ersetzen — wer was darf, entscheidet PostgreSQL über Row-Level-Security und geprüfte Funktionen. Die Rechte liegen in Tabellen (`memberships`, `set_permissions`), nicht in den Token-Claims: Eine Änderung des Admins greift mit der nächsten Anfrage, nicht erst nach Ablauf des Tokens. Ein **Set-Recht** kann die globale Rolle für ein einzelnes Set feiner setzen.

**Benutzerverwaltung für den Admin** direkt in `config.html` → „Zusammenarbeit" (nur sichtbar, wenn die Datenbank die Rolle `admin` meldet): Konten anlegen und löschen, globale Rollen ändern, Set-Rechte vergeben und entziehen. Jede Aktion prüft serverseitig auf `admin`, bevor sie irgendetwas tut.

**Nachvollziehbarkeit:** Jede Schreiboperation und jeder Sperrvorgang erzeugt eine Audit-Zeile (Wer, Was, Wann — ohne Dokumentinhalt), die nur der Admin liest.

Was ein Unauthentifizierter kann: **nichts Datenrelevantes.** Ohne Anmeldung gibt es kein Lesen und kein Schreiben; der öffentliche Anon-Key ist kein Vertrauensmerkmal. Das Berechtigungsmodell ist in der Betriebsanleitung (`infra/terraform/README.md`, Abschnitt 4) vollständig beschrieben, samt curl-Abnahme der Grenzen.

## Sperren gegen gleichzeitiges Schreiben

Wer ein Set bearbeitet, sperrt es für andere — atomar erworben, mit Heartbeat und einer Zeitüberschreitung von fünf Minuten, damit ein abgestürzter Tab kein Set dauerhaft blockiert. Die Sperre ist **beratend**: Gegen böswillige Umgehung schützt nicht sie, sondern die RLS-Policy. Fremde Sperren brechen darf nur der Admin. Der Client bringt Erwerb, Freigabe und Statusabfrage bereits mit; die sichtbare Sperranzeige in jedem Werkzeug folgt in Phase 4.

## Betrieb: Testumgebung als Terraform

Neu im Repository unter `infra/terraform/`: die Referenzinstallation als Infrastruktur-als-Code — eine einzelne Compute-Engine-VM mit dem Supabase-Compose-Stack, wahlweise mit Caddy als TLS-Endpunkt und statischem Host, sodass Werkzeuge und API unter demselben Ursprung liegen und die CORS-Frage entfällt. Das Startskript spielt das Datenbankschema beim ersten Boot ein und legt das Admin-Konto an (Passwort im Secret Manager). Bewusst kein Cloud SQL und kein Cloud Run: Der Aufbau soll dem entsprechen, was Anwender später selbst betreiben.

Das `schema.sql` liegt als eigene Datei bei — Tabellen, RLS-Policies, die Rollen-Auflösung, die Sperr- und Admin-Funktionen und die Audit-Trigger. Es ist idempotent und gegen die Testinstanz verifiziert.

## Nicht im Umfang von 4.0

* **Phase 4** — die sichtbare Sperranzeige und „Sperre übernehmen" in den Werkzeugen und der Übersicht.
* **Phase 5** — das einmalige Hochladen bestehender Sets in die Datenbank.
* Die produktive Härtung des Backends (TLS auf dem öffentlichen Port, GoTrue-Admin-API statt direkter `auth.users`-Schreibzugriff bei der Konto-Anlage) — die Terraform-Umgebung ist eine Testinstanz.

## Versionen der Anwendungen

| Anwendung | Version |
|---|---|
| gemeinsamer Kern (gpp-core.js) | 3 · Cache-Buster v3.6 |
| Übersicht (index.html) | 1.4 |
| OSCAL Schema Validator | 1.11.2 |
| SSP-Generator (G++) | V5.10.0 |
| GS++ Explorer (GSpp-Viewer) | v9.8 |
| BSI → G++ Profil (Baustein_2_Profile) | 0.9.2 |
| SSP-Editor (ssp_ausfuellen) | v1.3.0 |
| Prüfung AP/AR (pruefung_ap_ar) | build 9.5.2 |
| POA&M-Generator | v2.4 |

Einzelwerkzeuge in `one-page-apps/` — eigenständig, ohne `gpp-core.js`, von der Datenbank unberührt:

| Anwendung | Version |
|---|---|
| SSP-Generator Edition 2023 | ED23 V1.5 |
| C5 → OSCAL Konverter | v1.1 |

## Hinweise zum Umstieg

- **Die Datenbank ist optional und aus.** Ohne Server-URL in `config.html` ändert sich für bestehende Nutzung nichts; der Artefaktbestand bleibt lokal im Browser.
- Wer die gemeinsame Datenbank nutzt, braucht die Sammlung über HTTP ausgeliefert (nicht per Doppelklick über `file://`) — die Terraform-Umgebung liefert dafür den statischen Host gleich mit.
- **Für Betreiber:** Nach dem Einspielen des Schemas müssen Konten eine Mitgliedschaft erhalten (`seed_users.sh` bzw. die Benutzerverwaltung), sonst sehen sie nichts — das ist die Durchsetzung, kein Fehler. Signup am Identity-Provider gehört auf der Testinstanz abgeschaltet; Konten legt der Admin an.
