# Tools der NTT zur Bearbeitung von OSCAL Dateien im Kontext BSI Grundschutz++

Diese Sammlung enthält Werkzeuge zur Erstellung, Verwaltung und Dokumentation von **Systemsicherheitsprofilen (SSP)** im Kontext nutzergenerierter Inhalte. Die Tools sind webbasiert (HTML/JS) und ermöglichen einen durchgängigen Workflow von der Planung bis zur Zertifizierung und dem Abarbeiten der Festellungen.

Und es gibt auch eine Anwendung den Anwenderkatalog zu betrachten: [GSpp-Viewer.html](./GSpp-Viewer.html).

**Katalog-Pinning (Handbuch 3.13/3.14, Katalogarbeit-Skill Grundregel 8):** Alle Tools laden den G++-Anwenderkatalog von einer Commit-gepinnten URL und verifizieren den Inhalt per SHA-256 gegen den im Repo hinterlegten Pin (gleiche Werte wie `Gpp-ai-tool/src/constants.py` und die Back-Matter-Resources der 229 gepinnten Profile). Fragment-Importe (`href: "#uuid"`) werden über die Back-Matter aufgelöst und — wo ein Hash hinterlegt ist — geprüft; erzeugte OSCAL-Artefakte (Profile, SSPs, AP/AR, POA&M) schreiben ihre Referenzen selbst im Pin-Muster. Ein Katalog-Update ist ein bewusster Pin-Wechsel: neue Werte in `Gpp-ai-tool/src/constants.py`, Skript-Neulauf über die Profile und Aktualisierung der Pin-Konstanten in den hier liegenden Apps — in einem Commit.

**Gemeinsame Konventionen aller Apps:** Jede Anwendung ist eine `.html`-Datei ohne Build-Schritt und trägt eine sichtbare Build-Version; seit Version 3 teilen sich alle die Bibliothek [gpp-core.js](./gpp-core.js) im selben Ordner — die Sammlung wird als Ganzes ausgeliefert (`GS++-oscal-app.zip`), eine einzelne Datei allein läuft nicht mehr. Wo KI eingesetzt wird, gilt: deterministisch lösbare Schritte (Parsen, Joins, Zählen, Rechnen, UUIDs, Schema-Prüfung, OSCAL-Montage) laufen in JavaScript, das Modell bekommt nur die Fälle, die echtes Urteilsvermögen brauchen. Als Backend stehen **Gemini** und **OpenRouter** zur Wahl; Schlüssel, Modelle und Laufzeitwerte werden einmal zentral in [config.html](./config.html) gesetzt, bleiben im `localStorage` des Browsers und stehen nie fest in einer Datei. **Alle Prompts sind editierbar** — mit Zurücksetzen auf den Standardtext und Platzhalter-Prüfung, ebenfalls in `config.html` —, damit nachvollziehbar bleibt, was dem Modell tatsächlich gesagt wird, und Fachleute die Vorgaben an ihre Domäne anpassen können. Läuft eine App über `file://` und meldet der Browser einen CORS-Fehler, hilft ein lokaler Server: `python -m http.server` und dann `http://localhost:8000/…` aufrufen. KI-Vorschläge sind grundsätzlich Entwürfe und vor produktiver Nutzung fachlich zu prüfen.

[Dieses Video erklärt die Tools](https://www.youtube.com/watch?v=lY3wi6qHTRc)

## [BSI zu G++ OSCAL Generator](./Baustein_2_Profile.html)

Eine serverlose, vollständig im Browser laufende Single-Page Application (SPA), die BSI IT-Grundschutz-Bausteine (PDF) in das moderne G++ (Grundschutz Plus Plus) Format mappt und als OSCAL Profile exportiert. Sie portiert die Kernfunktionen des Python `Gpp-ai-tools` in eine interaktive, leicht bedienbare Benutzeroberfläche.

> ⚠️ **BETA STATUS**  
> Diese App befindet sich aktuell in der **Beta-Phase**. Die von der KI (Gemini) erstellten Mappings und generierten OSCAL-JSON-Dateien dienen als Entwurf und Basis zur Beschleunigung der Arbeit. Sie sollten vor der produktiven Nutzung in einem Audit-Prozess zwingend fachlich geprüft werden.

### ✨ Features
* **Zero-Setup:** Keine Python-Umgebung oder Backend nötig. Besteht aus einer einzigen `.html`-Datei.
* **Lokale PDF-Verarbeitung:** BSI-Bausteine werden direkt im Browser (via PDF.js) ausgelesen – der Text verlässt das System nur für die LLM-Verarbeitung.
* **Transparente Pipeline:** Führt die Stages `stage_match_bausteine`, `stage_matching` und `stage_profiles` schrittweise und parallelisiert aus.
* **Anpassbare Prompts:** Alle an die KI gesendeten Prompts können direkt in der Benutzeroberfläche editiert und getestet werden.
* **Live-Feedback:** Integrierte Log-Konsole, Fortschrittsbalken und visuelle Auswertung der Mapping-Konfidenz.

### 🚀 Benutzung
1. Die Datei `Baustein_2_Profile.html` herunterladen und mit einem modernen Webbrowser (Chrome, Edge, Firefox) öffnen.
   *(Hinweis: Bei lokalen CORS-Problemen die Datei über einen lokalen Server starten, z. B. `python -m http.server`).*
2. Einen gültigen **Google Gemini API Key** (z. B. via Google AI Studio) in den Einstellungen hinterlegen. Der Key bleibt lokal im Browser.
3. Ein **BSI Baustein-PDF** (oder den reinen Text) per Drag & Drop in den Input-Bereich ziehen.
4. Pipeline starten, Mappings überprüfen und als fertiges **OSCAL JSON** exportieren.
---
# Version 3: gemeinsame Basis statt neun Einzelkonfigurationen

Bis Version 2 war jede Anwendung für sich allein lauffähig — und verlangte ihre eigene Einrichtung. Wer alle Werkzeuge benutzte, trug denselben API-Key bis zu fünfmal ein, weil jede Datei ihn unter einem anderen Namen speicherte. Mit Version 3 teilen sich alle neun Anwendungen eine gemeinsame Basis.

**[gpp-core.js](./gpp-core.js) — die geteilte Bibliothek.** Konfiguration, Artefaktspeicher, Prompt-Registrierung, Quellen-Pins und ein ZIP-Writer, einmal vorhanden statt neunmal kopiert. Die Datei wird als Geschwisterdatei eingebunden und funktioniert ohne Server, auch per `file://`. **Damit ist die Sammlung nur noch als Ganzes lauffähig:** Eine einzelne HTML-Datei weiterzugeben genügt nicht mehr — es braucht den Ordner beziehungsweise `GS++-oscal-app.zip`. Fehlt `gpp-core.js`, sagt das jede Anwendung beim Start deutlich, statt still zu scheitern.

**[config.html](./config.html) — alle Einstellungen an einer Stelle.** Backend, API-Schlüssel je Anbieter, Modelle, Thinking-Level, Grounding, Parallelität, Chunk-Größen, Retries und die Checker-Route gelten ab jetzt für die gesamte Sammlung. Die Werkzeuge selbst haben keine Eingabefelder für Zugangsdaten mehr; sie zeigen nur noch eine Zeile „was gilt gerade" und verlinken hierher. Fehlt ein Schlüssel, sagt jedes Werkzeug, was ohne ihn trotzdem geht — Kataloge laden, tailoren, exportieren und validieren funktionieren durchweg ohne KI.

Auch die **37 Prompts aus acht Werkzeugen** werden hier gepflegt. Die Standardtexte bleiben dabei im jeweiligen Werkzeug und werden beim Start angemeldet; `config.html` bearbeitet also immer den aktuellen Stand, statt eine zweite Kopie zu pflegen, die auseinanderläuft. Jedes Werkzeug zeigt in seinem Prompt-Abschnitt weiterhin an, welche seiner Prompts vom Standard abweichen.

**Quellen bleiben gepinnt — und trotzdem aktuell.** Alle 11 Kataloge und Hilfsdateien hängen an einem festen Commit (Handbuch 3.13/3.14, Grundregel 8), damit dieselbe Eingabe morgen dasselbe Ergebnis liefert. In `config.html` steht je Quelle der Pin, und „Nach Updates suchen" holt den neuesten Commit samt Datum und Commit-Message. Übernommen wird er erst auf Klick — Aktualität ist ein sichtbarer Schritt, kein stilles Nachziehen.

**Ein Satz Artefakte statt neun Inseln.** Jedes erzeugte OSCAL-Dokument landet in einem gemeinsamen Bestand (IndexedDB `gpp-artefacts`, im Browser dieses Rechners, nicht auf einem Server) — zusätzlich zum gewohnten Download. Entscheidend ist: **alle Werkzeuge arbeiten auf demselben Bestand.** Was der SSP-Generator erzeugt, liegt beim nächsten Öffnen des SSP-Editors schon da; die Prüfung zieht sich SSP und Kataloge von selbst, der POA&M-Generator die Assessment Results. Deshalb gibt es in den Werkzeugen keine „SSP laden"-Knöpfe und keine eigenen Zwischenspeicher mehr — der einzige Ausnahme-Fall ist der Validator, der weiterhin beliebige Dateien von außen prüfen kann und zusätzlich einen Knopf **„Alle Artefakte prüfen"** hat: er prüft den kompletten Bestand deterministisch durch und legt den Bericht wieder als Artefakt ab.

**Mehrere Arbeitsstände nebeneinander.** Ein **Set** ist ein zusammengehöriger Stand — Profil, SSP, Prüfung, POA&M eines Vorhabens. In der [Übersicht](./index.html) lassen sich Sets anlegen, wechseln, als ZIP (mit `manifest.json` samt Prüfsummen) herunterladen und wieder hochladen; einzelne JSON-Dateien lassen sich ebenso in ein Set legen. Die Werkzeuge folgen immer dem aktiven Set.

**Zusammenarbeit über eine gemeinsame Datenbank (optional).** Wer in `config.html` unter „Zusammenarbeit" eine Server-URL hinterlegt und sich anmeldet (E-Mail/Passwort oder Unternehmens-IdP per OIDC), dessen Speichervorgänge gehen **zusätzlich** in eine gemeinsame PostgreSQL-Datenbank (PostgREST + GoTrue, z. B. als Supabase-Stack — self-hosted oder gehostet, derselbe Client-Code). Lokal bleibt dabei die Wahrheit: Jedes Werkzeug speichert erst in die IndexedDB und liefert zurück; der Abgleich hängt daran, gescheiterte Übertragungen warten in einer Outbox auf die nächste Verbindung. Kollidiert ein Stand mit einer fremden Änderung, gewinnt niemand automatisch — der Konflikt wird angezeigt und bewusst entschieden (übernehmen oder erzwingen). Ein Status-Chip unten rechts zeigt in jedem Werkzeug den Zustand (nur lesen / ausstehend / synchron / Konflikt / 🔒 fremde Sperre). **Bearbeiten setzt die Sperre voraus:** Wer schreiben will, sperrt das Set in der Übersicht („Bearbeiten (sperren)" / „Freigeben") — ohne Sperre blockiert schon das lokale Speichern, und die Datenbank lehnt serverseitig ab. Fremde Sperren werden mit Halter und Uhrzeit angezeigt; brechen darf sie nur der Admin. Neue Sets legt in der Zusammenarbeit nur der Admin an, und nur er löscht oder leert ganze Sets; nach der Anmeldung erscheinen alle geteilten Sets, auf die Zugriff besteht, automatisch in der Set-Auswahl — und **gelöschte Sets verschwinden beim nächsten Abgleich überall**, landen dabei aber im lokalen Papierkorb (`config.html` → Speicher) statt im Nichts; eigene, noch nicht übertragene Arbeit bleibt geschützt. Ohne Server-URL verhält sich alles exakt wie bisher: offline, ohne Backend, nur dieser Browser. API-Schlüssel, GitHub-Token und Passwörter werden **nie** übertragen oder gespeichert; von der Sitzung liegt nur das Refresh-Token im Browser.

**Das Backend dahinter: PostgreSQL hinter Gateway, Rechte in der Datenbank.** Der Server-Stack besteht aus PostgreSQL, GoTrue (Anmeldung) und PostgREST (API), davor das Kong-Gateway als einziger Zugang — ohne `apikey`-Header endet jede Anfrage schon dort. Entscheidend für die Sicherheit: **Durchgesetzt werden Rechte in der Datenbank, nicht im Client.** Jedes der HTML-Werkzeuge könnte manipuliert oder durch `curl` ersetzt sein — wer was darf, entscheiden Row-Level-Security-Policies (default-deny) und geprüfte Datenbankfunktionen auf dem Server. Auch die Sperr-Pflicht gilt serverseitig: Schreiben ohne gehaltene Sperre lehnt die Datenbank ab. Der öffentlich sichtbare Anon-Key ist kein Geheimnis und öffnet keine Daten; die Selbstregistrierung ist abgeschaltet, Konten legt der Admin an. Jede Schreiboperation landet in einem Audit-Log (wer, was, wann — ohne Dokumentinhalt), das nur der Admin liest.

**Vier Rollen (RBAC).** Jedes Konto hat eine globale Rolle; je Set kann der Admin abweichende Set-Rechte vergeben, die für genau dieses Set die globale Rolle überschreiben:

| Rolle | Lesen | Schreiben | Sperren | Verwaltung |
|---|---|---|---|---|
| `leser` | alle Sets der Org | — | — | — |
| `bearbeiter` | alle Sets der Org | alles **außer** Prüfdokumente (`ap`/`ar`) | ja | — |
| `pruefer` | alle Sets der Org | nur `ap`/`ar`/`poam` | ja | — |
| `admin` | alle Sets der Org | alles | ja, plus fremde brechen | Konten, Rollen, Set-Rechte |

Die Trennung von `bearbeiter` und `pruefer` bildet das Vier-Augen-Prinzip ab: Wer die Umsetzung dokumentiert, schreibt nicht die Prüfergebnisse — und umgekehrt.

**Benutzerverwaltung in [config.html](./config.html).** Angemeldete Admins sehen unter „Zusammenarbeit" die Kontenverwaltung: Konten anlegen und löschen, globale Rollen setzen, Set-Rechte vergeben und entziehen, ganze Sets löschen. Jede dieser Aktionen prüft der Server als erste Anweisung erneut auf die Admin-Rolle — die Sichtbarkeit der Oberfläche ist Komfort, keine Schranke.

**Eigenes Backend aufsetzen.** Eine vollständige Referenzinstallation (Terraform für eine einzelne VM mit Docker-Compose-Stack, automatischer Schema-Einspielung und Admin-Konto, inklusive Abnahmetests der Berechtigungsgrenzen per `curl`) steht in [infra/terraform/README.md](../infra/terraform/README.md). Wer bereits einen Supabase-Stack betreibt — self-hosted oder gehostet —, braucht nur das dort beschriebene Schema und trägt die URL in `config.html` ein; der Client-Code ist derselbe.

**Hilfe und Handbuch eingebaut.** Die Übersicht rendert dieses readme unter „Hilfe" direkt im Browser (eigener Markdown-Renderer, keine externen Bibliotheken) und zeigt unter „Handbuch" die Kapitel aus dem Repository-Ordner `handbuch/` mit Kapitelnavigation. Geladen wird zuerst lokal; wo das nicht geht (typisch `file://` oder das ZIP ohne Repo drumherum), kommen die Texte von GitHub.

---
## [OSCAL Schema Validator](./oscal-schema-validator.html)

Ein vollständig im Browser laufender Validator für OSCAL-1.2.2-Dateien (Catalog, Profile, Component Definition, SSP, Assessment Plan/Results, POA&M) — alle sieben NIST-Schemas sind eingebettet, das Tool funktioniert daher auch offline und ohne Backend. Jeder Schema-Fehler wird mit exakter Zeilennummer und JSON-Pointer angezeigt, per Klick springt die Quelltextansicht zur Fehlerstelle; ein zweistufiger Fix-Workflow (erst Vorschau, dann Anwenden mit automatischer Revalidierung) behebt Standardfälle wie fehlende Pflichtfelder, ungültige UUIDs oder abgerissene Strings deterministisch lokal, komplexere Fälle per Gemini-Vorschlag. Der integrierte „Rules Check" prüft zusätzlich die Regeln, die das JSON Schema nicht ausdrücken kann: UUID-Eindeutigkeit, Auflösung von Fragment-, Rollen- und Party-Referenzen, das Import-Pinning nach Grundregel 8 des Katalogarbeit-Skills (Import als Fragment auf eine Back-Matter-Resource mit Commit-gepinnter rlink-URL und genau einem SHA-256-Hash; ungepinnte Branch-URLs werden als Warnung gemeldet) sowie — bei geladenem Quell-Katalog oder -Profile — ob referenzierte `control-id`s, `param-id`s und `statement-id`s dort tatsächlich existieren. Der Dateityp wird direkt beim Laden der Eingabedatei erkannt (Datei-Button, Drag&Drop oder Einfügen); Schema-Auswahl und Rules-Prompt folgen automatisch.

**Mehrere Referenzdokumente gleichzeitig (ab v1.9.0).** Ein SSP schöpft seine Controls in der Praxis aus mehreren Quellen — G++-Anwenderkatalog, ED23-Bausteine und Zusatzkataloge wie DSGVO oder C5. Das Tool hält deshalb beliebig viele Referenzdokumente gleichzeitig und prüft `control-id`s, `param-id`s und `statement-id`s gegen deren **Vereinigungsmenge**; eine Control-ID gilt als bekannt, sobald irgendeine geladene Referenz sie definiert. „Load linked sources" lädt dazu *alle* im Dokument verlinkten Quellen: `imports` / `import-profile` / `import-ssp` / `import-ap` (auch über das Pin-Muster mit Back-Matter-Resource), zusätzlich die Props `source-catalog` und `referenced-catalog` sowie Komponenten-Links mit `rel="catalog"`. Geladene Referenzen sind einzeln entfernbar und stehen mit Herkunft und Umfang im Report. Wird nur gegen eine einzelne Referenz geprüft, sind alle Controls der übrigen Kataloge Falschmeldungen — genau das war der Befund aus Issue #29.

**Zwei getrennte KI-Durchgänge.** „AI rules check" prüft das gesamte Dokument semantisch (Beschreibungsqualität, Konventionen, Props-Konsistenz) über einen editierbaren Prompt je Dateityp — unabhängig davon, was die deterministische Prüfung gefunden hat. „AI audit of deterministic findings" ist ein davon getrennter zweiter Durchgang: Er legt dem Modell jeden deterministischen Fund samt Quelltextausschnitt und Referenz-Digest vor und lässt ihn bestätigen oder widerlegen (`confirmed` / `refuted` / `setup_artefact` / `uncertain`). So werden Artefakte einer unvollständigen Prüfumgebung — etwa nicht geladene Kataloge — als solche sichtbar, statt als Dokumentfehler zu gelten. Wie bei allen Tools dieser Sammlung gilt: KI-Vorschläge sind Entwürfe und vor produktiver Nutzung fachlich zu prüfen.

---
## Nicht mehr Teil dieser Sammlung

Zwei Werkzeuge lösen abgegrenzte Sonderaufgaben und stehen deshalb außerhalb des durchgängigen Ablaufs, in [`../one-page-apps/`](../one-page-apps/readme.md):

* **SSP-Generator Edition 2023** — derselbe Ablauf wie der [SSP-Generator](./ssp_generator.html), aber gegen den BSI IT-Grundschutz Edition 2023 statt gegen den G++-Anwenderkatalog.
* **YAML → OSCAL Konverter (C5:2026)** — deterministische Umwandlung von YAML-Kriteriendateien in einen OSCAL-Katalog, ohne KI.

Beide sind **vollständig eigenständig**: eine einzelne HTML-Datei ohne `gpp-core.js`, mit eigenem KI-Zugang und eigenen Prompts. Sie arbeiten weder auf dem gemeinsamen Artefakt-Set noch mit der zentralen `config.html`. Ihr Ergebnis ist eine heruntergeladene Datei, die sich hier unter „Artefakte" in ein Set laden lässt.

---

## Zum OSCAL-Export beider SSP-Generatoren (Issue #29)

Beide Generatoren schreiben seit V5.8 bzw. ED23 V1.3 einen SSP, der sich ohne Nacharbeit prüfen lässt:

* **Quellen sind nachladbar.** Jeder Katalog, aus dem Controls stammen — Basis wie Zusatzkatalog —, bekommt eine eigene Back-Matter-Resource mit absoluter URL und SHA-256-Pin (Grundregel 8); die Katalog-Komponente verlinkt das Fragment. Vorher standen Zusatzkataloge nur als Props im Dokument, und jede daraus übernommene Control-ID galt bei der Prüfung als unauflösbar. Der `import-profile`-rlink bleibt relativ: Die Profildatei ist die Schwesterdatei des SSP und wird beim Prüfen mitgeladen.
* **UUIDs sind UUIDs.** Die Komponente eines Zusatzkatalogs trug bis V5.7 eine ID der Form `catalog-<uuid>` und verletzte damit das OSCAL-uuid-Pattern an jeder Stelle, an der sie referenziert wurde.
* **Komponententypen folgen dem OSCAL-Vokabular.** Zielobjektkategorie bzw. Baustein-Schicht bestimmen den Typ (`hardware`, `software`, `network`, `physical`, `process-procedure`); deutsche Freitexttypen aus der Dokumentanalyse werden abgebildet statt zeichenweise „bereinigt" — aus `Raum/Gebäude` wurde vorher `Raum-Geb-ude`. Die Originalbezeichnung bleibt als Prop erhalten.
* **Verantwortlichkeiten sind auflösbar.** `metadata/roles` enthält die ISMS-Rollen (Institutionsleitung, ISB, ICS-ISB, IS-Management-Team, IT-Betrieb, Fachverantwortung); erkannte Verantwortliche werden als `responsible-roles` geführt, der Freitext bleibt als Beleg. Parteien werden bewusst **nicht** erzeugt — konkrete Personen und Organisationen sind aus einer Blaupause nicht bekannt.
* **Der Schutzbedarf steht auch auf Systemebene.** `security-sensitivity-level`, `security-impact-level` und die Impacts am Informationstyp werden nach dem Maximumprinzip aus den Assets abgeleitet und begründet.
* **Offene Stellen sind als offen markiert.** Controls, die nur über ein Prozess-Profil oder einen Zusatzkatalog in den Geltungsbereich kommen, tragen `implementation-status: planned` mit Hinweis, statt ohne Status dazustehen.
* **Keine Dubletten.** Assets werden über die `source-id` der Dokumentanalyse abgeglichen, nicht nur über den Namen; Props und Links werden beim Zusammenführen dedupliziert.

---

# Workflow-Übersicht: G++ Compliance Management

Der Prozess folgt einer klaren Kette von der Modellierung über die Umsetzung bis hin zur finalen Prüfung.

### 1. Modellierung mit dem [SSP-Generator](./ssp_generator.html)
In dieser Phase legen Sie das Fundament für Ihren Informationsverbund.
* **Profil-Erstellung**: Das Tool generiert ein OSCAL-Profil auf Basis des gewählten ISMS-Typs.
* **KI-Dokumentanalyse**: Vorhandene Dokumente (Strukturanalysen, Sicherheitskonzepte, Netzpläne — PDF, DOCX, TXT, Markdown, CSV, JSON, XML, HTML) werden per Drag & Drop eingelesen und in einer mehrstufigen Pipeline ausgewertet: Die KI **klassifiziert** jedes Dokument (Dokumenttyp und Extraktionsplan, ein Aufruf je Dokument), **extrahiert** anschließend chunk-weise Assets, Prozesse, Risiken, Maßnahmen und Implementierungsaussagen — nur Belegtes, nichts Erfundenes —, **ordnet** die Funde den G++-Zielobjektkategorien und Praktiken zu und prüft per **Abdeckungsprüfung**, welche extrahierten Maßnahmen bereits durch Katalog-Controls abgedeckt sind (exakte ID-Treffer werden vorher lokal aufgelöst, die KI sieht nur den Rest). So entsteht die Strukturanalyse aus dem, was die Organisation schon dokumentiert hat, statt bei null zu beginnen.
* **KI-Ergebnisse bleiben erhalten**: Extraktionen werden je Chunk in der IndexedDB gecacht und die übernommene Analyse in die Back-Matter des SSP geschrieben — Re-Import und Cache-Restore kommen ohne erneute (kostenpflichtige) KI-Aufrufe aus. Aus der Analyse übernommene Assets und Controls tragen sichtbar ein ◉-KI-Badge.
* **SSP-Beschreibung per KI**: Der Abschnitt „Zweck & Geltungsbereich" wird auf Wunsch aus dem Workspace-Kontext (Assets, Prozesse, Schutzbedarf, Methodik) generiert.
* **Asset-Management**: Sie integrieren Muster-Assets oder laden eigene Zielobjekte direkt aus der GitHub-Bibliothek.
* **Einfügen eigener Profiles**: Die mit [BSI 2 Profile](./Baustein_2_Profile.html) erstellten Profile hinzufügen.
* **Risikoanalyse**: Die Anwendung enthält ein integriertes Risikomanagement inklusive der Erstellung von Custom Controls. Die **KI-Risikoanalyse** nach BSI-Standard 200-3 schlägt aus SSP-Beschreibung, Assets, Prozessen und Katalog die wichtigsten Risiken samt mitigierender Controls vor — Schwerpunkt sind Assets mit erhöhtem Schutzbedarf, für die eine Risikoanalyse Pflicht ist; Duplikate zu bereits erfassten Risiken werden vermieden.
* **Tailoring**: Sie passen Anforderungstexte und Parameter (z. B. Fristen oder Rollen) bereits hier an die lokale Situation an.
* **Transparenz & Kontrolle**: Alle sechs KI-Prompts (System-Instruktion, Klassifikation, Extraktion, Zuordnung, Abdeckungsprüfung, Beschreibung/Risikoanalyse) sind über [config.html](./config.html) editierbar; Dokumentinhalte gehen erst nach ausdrücklicher Einwilligung an den KI-Provider, und eine Token-Anzeige zeigt den Verbrauch der Sitzung.
* **Export**: Sie erhalten die Blaupause als Profil und einen darauf basierenden Muster-SSP.

### 2. Grundschutzcheck mit [SSP-Ausfüllen](./ssp_ausfuellen.html)
Hier dokumentieren Sie die tatsächliche Umsetzung der Maßnahmen im Betrieb.
* **Umsetzungsstatus**: Sie erfassen den Status (z. B. "umgesetzt", "geplant") sowie Verantwortliche und Termine für jedes Control.
* **Workspace-Konzept**: Sie können begonnene Arbeiten jederzeit speichern und durch Laden der bearbeiteten JSON-Datei fortsetzen.
* **AI-Assistent**: Die Anwendung nutzt KI-Unterstützung für tiefere Einblicke:
    * **Verständnis**: Erklärungen helfen, komplexe Control-Texte zu interpretieren.
    * **Risikofokus**: Die KI zeigt Gefahren bei Nicht-Umsetzung auf.
    * **Referenzierung**: Das Tool mappt Anforderungen auf die BSI Grundschutz Edition 2023.

### 3. Audit & Reporting mit [Assessment Plan & Results](./pruefung_ap_ar.html)
Die letzte Phase dient der formalen Prüfung und dem Nachweis der Compliance.
* **Prüfplanung (AP)**: Sie erstellen einen Assessment Plan, der Zeitpläne, Assessoren und die gewählten Prüfmethoden (Dokumentenprüfung, Interview, Test) festlegt.
* **Durchführung**: Sie bewerten die im SSP dokumentierte Umsetzung und halten Befunde (satisfied/not-satisfied) fest.
* **KI-Audit-Support**: 
    * **Befundvorschlag**: Die KI analysiert den SSP-Eintrag und schlägt eine Bewertung vor.
    * **Reifegrade**: Der Assistent generiert Prüfungshandlungen für verschiedene Reifegrade.
* **Ergebnis-Export (AR)**: Sie generieren die formalen Assessment Results (AR) als Beleg für die Wirksamkeit Ihres ISMS.

### 4. Feststellungen Abarbeiten: [POA&M-Generator](./abarbeiten_POAM_generator.html)
Das Tool überführt ungelöste Mängel in einen verbindlichen Maßnahmenplan, damit keine Sicherheitslücke unbehandelt bleibt.
* **Mängel-Import**: Sobald du die Assessment Results lädst, übernimmt die Anwendung automatisch alle nicht erfüllten Controls.
* **Meilenstein-Planung**: Du legst detaillierte Phasenpläne fest, damit die Sanierung der Schwachstellen termingerecht erfolgt.
* **Dashboard**: Du behältst überfällige Deadlines und den allgemeinen Fortschritt der Mängelbeseitigung permanent im Blick.

# Kurzanleitung: Informationsverbund erstellen (Modellieren, Strukturanalyse, Risiko Analyse - OSCAL Blaupausen Generator)

### 1. Metadaten festlegen
* Trage Titel, Version und Zweck deiner Blaupause ein.
* Das Tool übernimmt diese Angaben direkt in die Metadaten des späteren OSCAL-Profils.

### 2. KI-Dokumentanalyse (optional, empfohlen bei vorhandener Dokumentation)
* Ziehe vorhandene Dokumente (PDF, DOCX, TXT, Markdown, CSV, JSON, XML, HTML) in den Analyse-Bereich und bestätige die Einwilligung zur Übermittlung an den KI-Provider (Backend und Key kommen aus `config.html`).
* Starte die Analyse: Die KI klassifiziert jedes Dokument, extrahiert Assets, Prozesse, Risiken und Maßnahmen chunk-weise (mit Cache in der IndexedDB) und ordnet die Funde den G++-Zielobjektkategorien und Praktiken zu.
* Prüfe die Vorschläge und übernimm sie in den Workspace — übernommene Einträge tragen ein ◉-KI-Badge und bleiben nach Export/Re-Import ohne neue KI-Aufrufe erhalten.

### 3. ISMS & Assets wählen
* Wähle ein Basis-ISMS (Standard oder Enhanced), um die Pflicht-Controls zu laden.
* Importiere Muster-Assets aus der GitHub-Bibliothek, wodurch die App deren Anforderungen automatisch extrahiert.

### 4. Tailoring (Anpassung)
* Nutze den Button "⚙️ Modify", um Parameter-Werte innerhalb der Controls zu definieren.
* Ergänze eigene Texte am Anfang oder Ende der Original-Anforderungen, um lokale Besonderheiten abzubilden.
* Füge zusätzliche Control-IDs bei Bedarf manuell hinzu.

### 5. Risikoanalyse durchführen
* Erstelle Risiko-Einträge und ordne diese entweder dem gesamten System oder spezifischen Assets zu.
* Verknüpfe mitigierende Maßnahmen aus dem Katalog oder erstelle eigene "Custom Controls".
* Oder starte die **KI-Risikoanalyse** (BSI 200-3): Sie nutzt SSP-Beschreibung, Assets und Katalog als Kontext, priorisiert Assets mit erhöhtem Schutzbedarf und schlägt Risiken mit passenden mitigierenden Controls vor — fehlt die SSP-Beschreibung, wird sie zuerst generiert.

### 6. OSCAL-Paket exportieren
* Aktiviere optional das Häkchen für den Muster-SSP (System Security Plan).
* Klicke auf "Paket generieren", um die resultierenden JSON-Dateien für Profil und SSP herunterzuladen.

# Kurzanleitung: Anforderungen Ausfüllen (Basissicherheitscheck - OSCAL SSP Editor & Workspace)

Dieses Tool dient der detaillierten Bearbeitung von **System Security Plans (SSP)**. Es ermöglicht die Dokumentation der Umsetzung von Sicherheitsmaßnahmen (Controls) für spezifische Komponenten.

### 1. Workspace initialisieren
* **SSP laden**: Lade deine zentrale SSP-JSON-Datei hoch.
* **Assoziierte Dateien**: Lade Profile und Kataloge hoch, um den Workspace mit Inhalten (Anforderungstexten, Parametern) zu füllen. Komponenten-Definitionen werden nicht nachgeladen — ihre Inhalte sind bereits bei der Generierung per Kopie in den SSP instanziiert.
* **Status-Check**: Das Tool zeigt im Bereich "Ressourcen-Status" an, ob alle referenzierten Dateien korrekt geladen wurden oder ob Quellen fehlen.

### 2. KI-Assistent konfigurieren (Optional)
* Wähle ein **Backend** — **Gemini** (Key aus Google AI Studio, `AIza…`) oder **OpenRouter** (Key `sk-or-…`, ein Zugang für Modelle vieler Anbieter, inklusive Anthropic). Key und Modell werden je Backend getrennt lokal im Browser gespeichert.
* Definiere einen **System Kontext** (z. B. "Wir sind ein KRITIS-Unternehmen"), damit die KI-Vorschläge auf deine Organisation zugeschnitten sind.
* Du kannst generierte KI-Antworten exportieren und importieren, um sie ohne erneute API-Kosten zu teilen.

### 3. Navigation & Filter
* Nutze die **Globalen Filter**, um Controls nach Umsetzungsstatus (z. B. "Offen", "Geplant"), Kritikalität (CIA) oder Dokumentationspflicht zu sortieren.
* Die **Suche** erlaubt das schnelle Auffinden von Control-IDs oder Stichworten über alle Komponenten hinweg.

### 4. Umsetzung dokumentieren (Implementation)
* **Status & Details**: Wähle pro Maßnahme den Umsetzungsstatus und trage Bearbeiter sowie Datum ein.
* **Reifegrade**: Wähle bei Bedarf vordefinierte Umsetzungs-Level (Statements) aus, um die Beschreibung automatisch zu füllen.
* **KI-Features**:
    * **Umsetzungsvorschlag**: Generiert konkrete Praxisbeispiele.
    * **Risikoanalyse**: Zeigt Gefahren bei Nicht-Umsetzung auf.
    * **Edition 2023**: Mappt die G++ Maßnahme auf das klassische IT-Grundschutz-Kompendium.

### 5. Parameter & Risiken
* **Parameter**: Trage Werte für Platzhalter (z. B. Zeitfristen, Rollen) direkt ein. Das Tool erkennt, ob Werte aus dem Profil übernommen oder lokal überschrieben wurden.
* **Risikoanalyse**: Das Tool extrahiert identifizierte Risiken aus dem SSP und verknüpft sie direkt mit den mitigierenden Maßnahmen.

### 6. Speichern
* Klicke auf **SSP speichern**, um das vollständig ausgefüllte Sicherheitskonzept als OSCAL-konforme JSON-Datei herunterzuladen.

# Kurzanleitung: Audit Planen und Durchführen (OSCAL Assessment Plan & Results Generator)

Dieses Tool dient der Auditierung und Prüfung von Sicherheitskonzepten. Es transformiert einen System Security Plan (SSP) in formale Prüfpläne (**Assessment Plan**) und dokumentiert die Ergebnisse (**Assessment Results**) im OSCAL-Format.

### 1. Import & Initialisierung
* **SSP laden**: Importiere deine ausgefüllte `*_SSP-edited.json`. Das Tool extrahiert automatisch alle Controls, den Umsetzungsstatus und die beteiligten Komponenten.
* **Katalog & Defs**: Die Anwendung lädt im Hintergrund den Grundschutz++ Katalog sowie externe Komponentendefinitionen (Defs), um Reifegrade und Prüfhinweise anzuzeigen.
* **Session laden**: Über die "Session laden"-Funktion kannst du einen bereits begonnenen Prüfprozess jederzeit fortsetzen.

### 2. Rahmenbedingungen festlegen
* **Metadaten & Assessor**: Hinterlege Titel, Version und die Kontaktdaten des Prüfers.
* **Zeitplan & Methodik**: Definiere den Prüfzeitraum sowie die *Rules of Engagement* (ROE) und die angewandte Audit-Methodik.
* **Tasks**: Erstelle spezifische Aufgaben oder Meilensteine für das Audit-Team.

### 3. Durchführung der Prüfung (Audit)
* **Scope-Management**: Wähle aus, welche Controls geprüft werden. Du kannst einzelne Maßnahmen ein- oder ausschließen.
* **Prüfmethoden**: Weise jedem Control eine oder mehrere Methoden zu: **EX** (Examine/Dokumentenprüfung), **IN** (Interview) oder **TE** (Test).
* **Befunde erfassen**: Dokumentiere für jedes Control:
    * **Status**: Erfüllt (satisfied), Nicht erfüllt (not-satisfied) oder Sonstiges.
    * **Beobachtung**: Beschreibe deine Feststellungen während der Prüfung.
    * **Risiko**: Formuliere bei Nicht-Erfüllung das resultierende Risiko.

### 4. KI-Audit-Assistenz
* **Befundvorschlag (🤖)**: Die KI analysiert den SSP-Eintrag sowie die Reifegrade und schlägt einen passenden Prüfbefund vor.
* **Control-Erklärung (📖)**: Die KI erläutert die Anforderung, definiert 5 Reifegrade und schlägt konkrete Prüfungshandlungen (Nachweise, Fragen, Tests) vor.

### 5. Export der Ergebnisse
* **Session speichern**: Sichere den aktuellen Arbeitsstand inklusive aller KI-Analysen in einer Session-Datei.
* **AP exportieren**: Erzeuge den *Assessment Plan*, der den Prüfumfang und die geplanten Aktivitäten beschreibt.
* **AR exportieren**: Erzeuge die *Assessment Results*, die alle Befunde, Beobachtungen und Risiken für das offizielle Reporting enthalten.

# Kurzanleitung: Beheben der Feststellungen (OSCAL POA&M Generator)

Dieses Werkzeug schließt die Lücke zwischen der Feststellung von Mängeln und ihrer systematischen Behebung. Es überführt die Ergebnisse aus dem Assessment direkt in einen verbindlichen Maßnahmenplan.

### 1. Datenimport und Initialisierung
* **AR laden**: Importieren Sie die Datei `*_AR.json`, um alle Befunde in den POA&M zu überführen.
* **Automatische Erfassung**: Die Anwendung identifiziert sofort alle als "nicht erfüllt" (not-satisfied) markierten Befunde und legt dafür POA&M-Items an.
* **Session-Verwaltung**: Speichern Sie Ihren Arbeitsstand regelmäßig als Session-Datei, um die Planung später nahtlos fortzusetzen.

### 2. Metadaten und Zuständigkeiten
* **Verantwortlichkeiten**: Hinterlegen Sie Namen und E-Mail der verantwortlichen Personen, etwa des ISSO oder System Owners.
* **Stammdaten**: Passen Sie Titel und Version des Plans an, wobei das Tool den Systemnamen bereits aus dem AR übernimmt.

### 3. Maßnahmenplanung und Überwachung
* **Priorisierung**: Ordnen Sie jeder Maßnahme eine Priorität (Hoch, Mittel, Niedrig) zu, um die Ressourcensteuerung zu optimieren.
* **Status-Tracking**: Verfolgen Sie den Fortschritt von "Offen" über "In Arbeit" bis hin zum Abschluss.
* **Fristenmanagement**: Setzen Sie Deadlines für jede Aufgabe. Das Dashboard warnt Sie visuell bei Überfälligkeit.
* **Abweichungen**: Dokumentieren Sie Begründungen für Risikoakzeptanz oder genehmigte Abweichungen direkt am betroffenen Item.

### 4. KI-gestützte Sanierung (🤖)
* **Vorschlag zur Behebung**: Die KI analysiert Anforderung und Risiko, um einen konkreten Text für die Mängelbeseitigung zu formulieren.
* **Meilenstein-Planer**: Lassen Sie die KI einen zeitlichen Phasenplan mit konkreten Meilensteinen für die Umsetzung erstellen.

### 5. Export
* **POA&M-Datei**: Generieren Sie die finale `*_POAM.json`. Diese enthält alle Maßnahmen, Meilensteine und Risikoprotokolle im OSCAL-Standard.

---
# Daten-Management-Guide: Die OSCAL-Toolchain

Verwalte deine OSCAL-Daten wie einen Staffellauf. Jedes Werkzeug übergibt den Stab an das nächste, damit deine Compliance-Kette lückenlos bleibt.

---

## 1. Die Ordnerstruktur
Trenne die Phasen deines Projekts konsequent. Lege vier nummerierte Verzeichnisse an, da diese Struktur den Lebenszyklus deines Informationsverbunds widerspiegelt.

* **01_Modellierung**: Reserviere diesen Ordner für Profile und initiale SSPs aus dem Blaupausen-Generator.
* **02_Umsetzung**: Speichere hier deinen aktiv bearbeiteten SSP sowie die zugehörigen KI-Cache-Exporte.
* **03_Audit**: Dieses Verzeichnis nimmt den Assessment Plan (AP), die Assessment Results (AR) und die Audit-Sessions auf.
* **04_Sanierung**: Hier verwaltest du den Plan of Action and Milestones (POA&M) und die Sanierungs-Sessions.

---

## 2. Der Dateifluss (Input/Output-Matrix)

Halte dich strikt an diese Übergabepunkte. Falls du die Namen der exportierten JSON-Dateien manuell änderst, riskierst du kaputte interne Referenzen (href) innerhalb des Workspace.

| Phase | Werkzeug | Input | Output (Beispielname) |
| :--- | :--- | :--- | :--- |
| **1. Modell** | Blaupausen-Generator | (Katalog-URL) | `*_Profile.json`, `*_SSP.json` |
| **2. Umsetzung** | SSP-Ausfüllen | `*_SSP.json` + `*_Profile.json` | `*_SSP-edited.json` |
| **3. Audit** | Assessment Plan/Results | `*_SSP-edited.json` | `*_AP.json`, `*_AR.json` |
| **4. Sanierung** | POA&M Generator | `*_AR.json` | `*_POAM.json` |

---

## 3. Goldene Regeln für den Workspace

* **Sessions sind Pflicht**: Nutze im Audit- und POA&M-Tool konsequent die Funktion **Session speichern**. Nur die Session-Datei enthält deine gesamten Bearbeitungsstände inklusive aller Kommentare und KI-Analysen.
* **KI-Cache sichern**: Exportiere im SSP-Tool regelmäßig deinen KI-Cache. Du vermeidest dadurch, dass bei einem Browser-Reset bereits generierte KI-Antworten verloren gehen und Kosten für eine erneute Anfrage verursachen.
* **Referenz-Integrität**: Lade im Audit-Tool zwingend die `*_SSP-edited.json`, damit die Anwendung die dokumentierten Umsetzungsdetails gegen den Katalog prüfen kann.
* **Keine manuellen Datei-Eingriffe**: Bearbeite die JSON-Dateien niemals händisch in einem Texteditor. Nutze ausschließlich die grafischen Editoren, um die OSCAL-Konformität zu wahren.
---

## Technische Hinweise

* **Datenschutz:** Alle Tools arbeiten rein clientseitig. Es werden keine Daten an einen Server übertragen; die Speicherung erfolgt lokal über den JSON-Export.
* **KI Nutzung:** Sollte ein API Key eingetragen sein, werden Daten an die KI-Cloud übermittelt.
* **Beiträge:** Fehler oder Verbesserungsvorschläge können über die [GitHub Issues](https://github.com/NTT-Data-Deutschland-SE/Grundschutz-Plus-Plus-Tools/issues) gemeldet werden.
