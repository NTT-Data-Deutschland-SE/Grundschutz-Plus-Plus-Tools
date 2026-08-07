# Plan: Datenbank-Backend für die GS++-oscal-app

Stand: 2026-08-07 · Status: Entwurf, nicht beschlossen

## 1. Ausgangslage

Die Sammlung in `GS++-oscal-app/` besteht aus neun HTML-Werkzeugen plus dem
gemeinsamen Kern `gpp-core.js`. Aller Zustand liegt heute im Browserprofil:

* **Konfiguration** — `localStorage`, Präfix `gpp:cfg:`
* **Artefakte** — IndexedDB `gpp-artefacts`, ein Datensatz je OSCAL-Dokument
* **Arbeitseinheit** — das *Set* (`GPP_DEFAULT_SET = "standard"`), also ein
  zusammengehöriger Stand aus Profil, SSP, AP/AR und POA&M

Der Austausch zwischen Menschen läuft über ZIP-Export und -Import in
`index.html`. Das soll ergänzt werden: Wer Zugangsdaten hinterlegt, dessen
Speichervorgänge gehen zusätzlich in eine gemeinsame Datenbank, und wer ein Set
bearbeitet, sperrt es dort für andere.

### Randbedingungen, die das Projekt sich selbst gesetzt hat

| Regel | Fundstelle | Konsequenz für dieses Vorhaben |
|---|---|---|
| Offline und ohne Backend lauffähig | `GS++-oscal-app/readme.md:55` | Die DB ist **optional**. Ohne hinterlegten Server verhalten sich alle Werkzeuge exakt wie heute. |
| Keine Fremdbibliotheken | ZIP-Writer/-Reader in `gpp-core.js:456` sind handgebaut | Die DB muss über blankes HTTPS+JSON erreichbar sein, `fetch()` muss reichen. Kein SDK, kein Treiber, kein OIDC-Client-Paket. |
| Quellen sind commit-gepinnt | Grundregel 8, Katalogarbeit-Skill | Unberührt — Kataloge kommen weiter von GitHub, nicht aus der DB. |

### Der eine Umstand, der die Umsetzung billig macht

Sämtliche Schreibvorgänge aller neun Werkzeuge laufen durch vier Funktionen in
`gpp-core.js`: `gppArtefacts.save`, `.remove`, `.removeSet` und `.setActiveSet`.
Rund 28 Aufrufstellen, aber genau ein Nadelöhr. **Die Synchronisierung wird
vollständig in `gpp-core.js` gebaut; die HTML-Werkzeuge werden bis auf die
Sperr-Anzeige nicht angefasst.**

Nicht im Umfang: `one-page-apps/c5-oscal-converter.html` und
`one-page-apps/ssp_generator_ed23.html`. Die sind bewusst eigenständige
Einzeldateien ohne `gpp-core.js` und bleiben es.

## 2. Produktentscheidung: Supabase (PostgreSQL + PostgREST + GoTrue)

Self-hosted per Docker-Compose **oder** als gehosteter Dienst — derselbe Stack,
derselbe Client-Code, kein Umbau beim Wechsel. Das ist für den BSI-Kontext der
ausschlaggebende Punkt.

* **PostgreSQL** — Row-Level-Security als serverseitig durchgesetztes RBAC,
  `jsonb` für die OSCAL-Dokumente (das `data`-Feld wandert unverändert hinein).
* **PostgREST** — REST über HTTPS, mit `fetch()` bedienbar. Erfüllt die
  Bibliotheksregel.
* **GoTrue** — stellt JWTs aus, **und zwar in derselben Form für beide
  Anmeldewege**. Genau das brauchen wir (Abschnitt 3).

Ohne Supabase geht es auch: PostgREST akzeptiert jedes JWT, das gegen den
konfigurierten Schlüssel bzw. die JWKS-URL verifiziert. Wer seinen IdP direkt
anbinden will, tauscht den Aussteller aus — der Rest bleibt.

Verworfen: **CouchDB/PouchDB** (Synchronisation wäre fast ein Drop-in, aber das
Rechtemodell ist grob und die Konfliktsemantik arbeitet gegen das Sperrkonzept),
**MongoDB Atlas** (browser-direkt nur über Atlas App Services, das es
self-hosted nicht gibt), **eigenes Backend** (Mehraufwand ohne Gegenwert,
solange RLS die Anforderungen abbildet — bleibt der Fallback für
Freigabe-Workflows mit Vier-Augen-Prinzip).

## 3. Die tragende Entscheidung: ein Token-Kontrakt, zwei Anmeldewege

Es wird Anwender ohne IdP geben und solche, die zwingend einen anbinden müssen.
Damit das nicht zwei Produkte werden, wird **die Naht sauber gelegt**: Beide
Wege münden in ein JWT mit identischen Claims. Alles hinter dieser Naht —
Policies, Sperren, Sync-Schicht, sämtliche Werkzeuge — kennt nur das Token und
weiß nicht, woher es kommt.

```jsonc
{
  "sub":  "<uuid>",              // Benutzer, stabil
  "email": "person@firma.de",
  "org":  "<uuid>",              // Mandant — trennt Datenbestände
  "gpp_role": "bearbeiter",      // leser | bearbeiter | pruefer | admin
  "exp":  1770000000             // kurzlebig, ≤ 1 h
}
```

**Pfad A — ohne IdP.** GoTrue mit E-Mail und Passwort, Benutzer in der DB. Eine
Person mit Rolle `admin` legt Konten an und vergibt Rollen. Zielgruppe: kleine
Teams, Beratungsprojekte, Einzelinstallationen.

**Pfad B — mit IdP.** GoTrue als OIDC-Relying-Party gegen Entra ID, Keycloak
o. ä. Der Browser wird auf `/auth/v1/authorize` umgeleitet, GoTrue führt den
Code-Austausch serverseitig durch und liefert dasselbe Token zurück. **Das ist
der Grund, den OIDC-Tanz nicht selbst zu bauen** — Authorization Code mit PKCE
von Hand wäre zwar mit `crypto.subtle` machbar, aber die fehleranfälligste
Stelle des ganzen Vorhabens, und sie fiele beim härtesten Anwenderkreis an.
`gpp_role` und `org` kommen entweder aus Gruppen-Claims des IdP (Mapping-Tabelle
in der DB) oder bleiben lokal gepflegt; beides wird unterstützt.

Im Client unterscheidet sich beides in genau einer Funktion und einem
Konfigurationswert: `db:auth:mode = passwort | oidc`.

## 4. Rollenmodell

Angelehnt an die Workflow-Stufen aus `GPP_STAGES`, damit die Rechte den
tatsächlichen Arbeitsteilungen folgen:

| Rolle | Darf |
|---|---|
| `leser` | Alle Sets der Organisation lesen. Keine Sperre, kein Schreiben. |
| `bearbeiter` | Sets sperren und darin schreiben — Kataloge, Profile, SSP, Workspaces. Nicht: `ap`, `ar`. |
| `pruefer` | Wie `leser`, zusätzlich `ap`, `ar` und `poam` schreiben. Trennt Prüfung von Erstellung. |
| `admin` | Alles, plus Benutzerverwaltung, plus Sperren fremder Sitzungen brechen. |

Die Trennung `bearbeiter`/`pruefer` ist der Grund, RLS überhaupt feingranular zu
machen — sie fällt auf die Spalte `kind` und ist in einer Policy ausdrückbar.

## 5. Phasen

### Phase 0 — Entscheidungen festzurren *(keine Codeänderung)*

1. **Bleibt der Doppelklick aus dem ZIP?** Bei `file://` sendet der Browser
   `Origin: null`; ein Endpunkt, der das zulässt, lässt faktisch jede lokale
   HTML-Datei auf jedem Rechner zu. Empfehlung: Wer die DB nutzt, bekommt den
   Ordner über HTTP ausgeliefert (ein statischer Host neben PostgREST genügt);
   der Offline-Betrieb per Doppelklick bleibt für alle anderen unangetastet.
2. Token-Claims und Rollennamen aus Abschnitt 3/4 bestätigen.
3. Referenzinstallation festlegen (self-hosted Compose als Standard).

**Ergebnis:** dieser Abschnitt, abgenommen.

### Phase 1 — Datenbank, komplett ohne Client

Alles hier ist per `curl` testbar, bevor eine Zeile Frontend entsteht.

* Tabellen `orgs`, `memberships`, `artefacts`, `set_locks`, `audit`.
  `artefacts` bildet den Record aus `gppArtefacts.save()` eins zu eins ab:
  `id, set_name, stage, kind, title, filename, tool, created_at, updated_at,
  size, sha256, meta jsonb, data jsonb, org, updated_by`.
* RLS-Policies je Rolle, inklusive der `kind`-Bedingung für `bearbeiter`
  gegenüber `pruefer`.
* `set_locks` mit `heartbeat_at` und atomarem Erwerb:

  ```sql
  insert into set_locks (set_name, org, holder, holder_name)
  values ($1, auth_org(), auth.uid(), $2)
  on conflict (set_name) do update
     set holder = excluded.holder, holder_name = excluded.holder_name,
         acquired_at = now(), heartbeat_at = now()
   where set_locks.holder = excluded.holder
      or set_locks.heartbeat_at < now() - interval '5 minutes'
  returning *;
  ```

  Leeres Ergebnis heißt: jemand anderes hält es. Ein Roundtrip, keine
  Race Condition, kein Deadlock. **Bewusst keine Advisory Locks** — die hängen
  an der Verbindung, und PostgREST poolt kurzlebige Verbindungen; die Sperre
  wäre weg, bevor das erste Feld ausgefüllt ist.
* Funktion `artefact_save(...)`, die Schreiben und das Verdrängen älterer
  Einzelstück-Sorten (`GPP_SINGLETON_KINDS`) in **einer** Transaktion erledigt.
  Die heutige Reihenfolge in `gpp-core.js:392` — erst schreiben, dann
  aufräumen — ist lokal unkritisch, über zwei Browser hinweg ein Rennen.
* Jeder Schreibvorgang und jeder Sperrbruch erzeugt eine `audit`-Zeile.

**Abnahme:** Zwei parallele `curl`-Sitzungen; die zweite bekommt die Sperre
nicht, nach Ablauf der TTL bekommt sie sie. `leser` scheitert am Schreiben,
`bearbeiter` an `kind = 'ar'`.

### Phase 2 — Sync-Schicht in `gpp-core.js`

Neues Modul `gppRemote`, eingehängt in die vier bestehenden Schreibfunktionen.
Leitprinzip: **IndexedDB bleibt die Wahrheit für den laufenden Vorgang, die
Datenbank ist ein Ziel, kein Nadelöhr.**

* **Lokal zuerst.** `save()` schreibt wie heute in IndexedDB und liefert zurück.
  Der DB-Push hängt daran, nicht davor. Netzausfall verliert nichts und blockiert
  nichts.
* **Outbox.** Fehlgeschlagene Pushes landen in einem IndexedDB-Store und werden
  bei Verbindung erneut versucht. Ohne das kostet ein DB-Schluckauf Arbeit.
* **Zusammenfassen.** `abarbeiten_POAM_generator.html:871` speichert bei jeder
  Änderung automatisch. Ungebremst wären das Dutzende Anfragen pro Minute.
  Entprellung je `(set, id)`, etwa zwei Sekunden.
* **Konflikte.** Der bereits berechnete `sha256` dient als Version; der Push
  schickt den zuletzt bekannten Wert mit. Passt er nicht, gewinnt niemand
  automatisch — das Werkzeug meldet „fremde Änderung" und bietet Übernehmen
  oder Verwerfen an. Bei gehaltener Sperre darf das praktisch nie auftreten;
  tritt es doch auf, ist es ein echter Befund und kein Grund für stilles
  Überschreiben.
* **Herunterladen.** Beim Setwechsel und beim Sperrerwerb wird der Serverstand
  in die lokale IndexedDB gezogen.

**Nicht synchronisiert — ausdrücklich:** `gpp:cfg:ai:key:*` und `gh:token`
verlassen den Browser nicht. API-Schlüssel sind persönlich; sie gehören nicht in
einen geteilten Bestand. Prompts und Quellen-Pins organisationsweit zu
verteilen, ist dagegen sinnvoll — als eigener, späterer Schritt.

**Aufwand:** geschätzt +300 bis 400 Zeilen in `gpp-core.js` (heute 448).

### Phase 3 — Anmeldung in `config.html`

Neuer Abschnitt **„Zusammenarbeit"** zwischen „Quellen und Pins" und
„Speicher" (`config.html:239` bzw. `:259`):

* Server-URL, Modus (`passwort` / `oidc`), Anmelde-Schaltfläche, Anzeige von
  angemeldeter Person, Organisation und Rolle.
* Ohne Server-URL bleibt der Abschnitt eingeklappt und alles verhält sich wie
  heute — der Offline-Betrieb ist der Normalfall, nicht die Ausnahme.
* **Kein DB-Passwort im `localStorage`.** Dort liegt allenfalls das
  Refresh-Token; der kurzlebige Access-Token lebt im Speicher. Das ist der
  übliche Kompromiss und soll im Text der Seite auch so benannt werden — die
  bestehende Zusage „Beides gehört diesem Browserprofil und verlässt es nicht"
  (`config.html:260`) muss ohnehin neu formuliert werden, sobald Daten das
  Profil verlassen.
* Der Hinweisbanner-Mechanismus `gppConfigBanner` (`gpp-core.js:789`) bekommt
  ein Gegenstück für „nicht angemeldet, Änderungen bleiben lokal".

### Phase 4 — Sperre sichtbar machen

* **`index.html`, Set-Verwaltung:** je Set der Sperrzustand mit Halter und
  Zeitpunkt; Schaltflächen „Bearbeiten (sperren)" und „Freigeben".
* **Alle Werkzeuge:** Ein Banner aus `gpp-core.js` — kein Eingriff in die
  einzelnen Dateien nötig — zeigt „Set *X* ist seit 14:05 von *Y* gesperrt,
  Nur-Lesen". Bei gehaltener Sperre ein unauffälliger grüner Hinweis.
* **Heartbeat** alle 60 s, solange das Dokument sichtbar ist
  (`visibilitychange`), Freigabe per `navigator.sendBeacon` bei `pagehide`.
* **„Sperre übernehmen"** für `admin`, mit Protokolleintrag und Anzeige beim
  Verdrängten.

Klar benennen, auch in der Doku: **Eine Sperre aus dem Browser ist beratend.**
Der Tab stürzt ab, das Notebook klappt zu, niemand gibt etwas frei — dafür
Heartbeat, TTL und die Übernahme. Gegen böswillige Umgehung schützt nicht die
Sperre, sondern die RLS-Policy.

### Phase 5 — Einführung

1. `docker-compose.yml` plus Migrationsskripte im Repo, dazu eine
   Betriebsanleitung für beide Anmeldewege.
2. „Bestehende Sets in die Datenbank hochladen" als einmalige Aktion in
   `index.html` — der vorhandene ZIP-Import-Pfad (`index.html:575`) liefert die
   Vorlage.
3. `readme.md` und `RELEASE_NOTES` fortschreiben. Die Aussage „funktioniert auch
   offline und ohne Backend" bleibt richtig und muss richtig bleiben.

## 6. Offene Punkte

* **Phase-0-Frage 1** (`file://` aufgeben?) blockiert die CORS-Konfiguration und
  damit Phase 1. Alles andere kann parallel laufen.
* Kommen `org` und `gpp_role` bei Pfad B aus IdP-Gruppen oder bleiben sie lokal
  gepflegt? Beides ist vorgesehen, die Voreinstellung ist zu wählen.
* Sollen Prompts und Quellen-Pins organisationsweit verteilbar sein? Sinnvoll,
  aber ein eigenes Vorhaben nach Phase 4.
* Aufbewahrung und Löschfristen der `audit`-Tabelle.
