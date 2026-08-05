# Tools der NTT zur Bearbeitung von OSCAL Dateien im Kontext BSI Grundschutz++

Diese Sammlung enthält Werkzeuge zur Erstellung, Verwaltung und Dokumentation von **Systemsicherheitsprofilen (SSP)** im Kontext nutzergenerierter Inhalte. Die Tools sind webbasiert (HTML/JS) und ermöglichen einen durchgängigen Workflow von der Planung bis zur Zertifizierung und dem Abarbeiten der Festellungen.

Und es gibt auch eine Anwendung den Anwenderkatalog zu betrachten: [GSpp-Viewer.html](./GSpp-Viewer.html).

**Katalog-Pinning (Handbuch 3.13/3.14, Katalogarbeit-Skill Grundregel 8):** Alle Tools laden den G++-Anwenderkatalog von einer Commit-gepinnten URL und verifizieren den Inhalt per SHA-256 gegen den im Repo hinterlegten Pin (gleiche Werte wie `Gpp-ai-tool/src/constants.py` und die Back-Matter-Resources der 229 gepinnten Profile). Fragment-Importe (`href: "#uuid"`) werden über die Back-Matter aufgelöst und — wo ein Hash hinterlegt ist — geprüft; erzeugte OSCAL-Artefakte (Profile, SSPs, AP/AR, POA&M) schreiben ihre Referenzen selbst im Pin-Muster. Ein Katalog-Update ist ein bewusster Pin-Wechsel: neue Werte in `Gpp-ai-tool/src/constants.py`, Skript-Neulauf über die Profile und Aktualisierung der Pin-Konstanten in den hier liegenden Apps — in einem Commit.

**Gemeinsame Konventionen aller Apps:** Jede Anwendung ist eine einzelne `.html`-Datei ohne Build-Schritt und trägt eine sichtbare Build-Version. Wo KI eingesetzt wird, gilt: deterministisch lösbare Schritte (Parsen, Joins, Zählen, Rechnen, UUIDs, Schema-Prüfung, OSCAL-Montage) laufen in JavaScript, das Modell bekommt nur die Fälle, die echtes Urteilsvermögen brauchen. Als Backend stehen **Gemini** und **OpenRouter** zur Wahl; der API-Key bleibt im `localStorage` des Browsers und wird nie fest in die Datei geschrieben. **Alle Prompts sind in der Oberfläche editierbar** — mit Zurücksetzen-Button, lokaler Speicherung und Platzhalter-Prüfung —, damit nachvollziehbar bleibt, was dem Modell tatsächlich gesagt wird, und Fachleute die Vorgaben an ihre Domäne anpassen können. Läuft eine App über `file://` und meldet der Browser einen CORS-Fehler, hilft ein lokaler Server: `python -m http.server` und dann `http://localhost:8000/…` aufrufen. KI-Vorschläge sind grundsätzlich Entwürfe und vor produktiver Nutzung fachlich zu prüfen.

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
## [OSCAL Schema Validator](./oscal-schema-validator.html)

Ein vollständig im Browser laufender Validator für OSCAL-1.2.2-Dateien (Catalog, Profile, Component Definition, SSP, Assessment Plan/Results, POA&M) — alle sieben NIST-Schemas sind eingebettet, das Tool funktioniert daher auch offline und ohne Backend. Jeder Schema-Fehler wird mit exakter Zeilennummer und JSON-Pointer angezeigt, per Klick springt die Quelltextansicht zur Fehlerstelle; ein zweistufiger Fix-Workflow (erst Vorschau, dann Anwenden mit automatischer Revalidierung) behebt Standardfälle wie fehlende Pflichtfelder, ungültige UUIDs oder abgerissene Strings deterministisch lokal, komplexere Fälle per Gemini-Vorschlag. Der integrierte „Rules Check" prüft zusätzlich die Regeln, die das JSON Schema nicht ausdrücken kann: UUID-Eindeutigkeit, Auflösung von Fragment-, Rollen- und Party-Referenzen, das Import-Pinning nach Grundregel 8 des Katalogarbeit-Skills (Import als Fragment auf eine Back-Matter-Resource mit Commit-gepinnter rlink-URL und genau einem SHA-256-Hash; ungepinnte Branch-URLs werden als Warnung gemeldet) sowie — bei geladenem Quell-Katalog oder -Profile — ob referenzierte `control-id`s, `param-id`s und `statement-id`s dort tatsächlich existieren. Der Dateityp wird direkt beim Laden der Eingabedatei erkannt (Datei-Button, Drag&Drop oder Einfügen); Schema-Auswahl und Rules-Prompt folgen automatisch. Im Dokument verlinkte Quell-Kataloge/-Profile (`imports` bzw. `import-profile`, auch über das Pin-Muster mit Back-Matter-Resource) lädt das Tool selbstständig als Referenzdokument nach — manuell per „Load linked source", bei Dateiladung automatisch, sofern die verlinkte Quelle eine abrufbare URL ist. Semantische Prüfungen (Beschreibungsqualität, Konventionen, Props-Konsistenz) übernimmt ein editierbarer KI-Prompt je Dateityp. Wie bei allen Tools dieser Sammlung gilt: KI-Vorschläge sind Entwürfe und vor produktiver Nutzung fachlich zu prüfen.

---
## [C5 zu OSCAL Konverter](./c5-oscal-converter.html)

Wandelt die YAML-Kriteriendateien des BSI C5:2026 in einen NIST-OSCAL-1.2.2-Katalog um. Das Tool ist **vollständig deterministisch**: Parsing, Gruppierung, Joins zwischen Kriterium und Guidance, UUID-Vergabe und der Aufbau der OSCAL-Hülle passieren komplett in JavaScript. Es gibt deshalb kein API-Key-Feld, keine Modellauswahl und keine Prompts — dieselbe Eingabe erzeugt bei jedem Lauf byteweise dasselbe Ergebnis. Die YAML-Bibliothek ist in die Datei eingebettet, das Tool läuft daher auch offline.

---
## [SSP-Generator Edition 2023](./ssp_generator_ed23.html)

Die Schwester-Anwendung zum [SSP-Generator](./ssp_generator.html), aber für den **BSI IT-Grundschutz Edition 2023** statt für den G++-Anwenderkatalog. Gleicher Ablauf — Metadaten, ISMS- und Asset-Auswahl, Tailoring, Risikoanalyse, OSCAL-Export — nur gegen den ED23-Katalog und dessen Bausteinstruktur.

---

# Workflow-Übersicht: G++ Compliance Management

Der Prozess folgt einer klaren Kette von der Modellierung über die Umsetzung bis hin zur finalen Prüfung.

### 1. Modellierung mit dem [SSP-Generator](./ssp_generator.html)
In dieser Phase legen Sie das Fundament für Ihren Informationsverbund.
* **Profil-Erstellung**: Das Tool generiert ein OSCAL-Profil auf Basis des gewählten ISMS-Typs.
* **Asset-Management**: Sie integrieren Muster-Assets oder laden eigene Zielobjekte direkt aus der GitHub-Bibliothek.
* **Einfügen eigener Profiles**: Die mit [BSI 2 Profile](./Baustein_2_Profile.html) erstellten Profile hinzufügen.
* **Risikoanalyse**: Die Anwendung enthält ein integriertes Risikomanagement inklusive der Erstellung von Custom Controls.
* **Tailoring**: Sie passen Anforderungstexte und Parameter (z. B. Fristen oder Rollen) bereits hier an die lokale Situation an.
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

### 2. ISMS & Assets wählen
* Wähle ein Basis-ISMS (Standard oder Enhanced), um die Pflicht-Controls zu laden.
* Importiere Muster-Assets aus der GitHub-Bibliothek, wodurch die App deren Anforderungen automatisch extrahiert.

### 3. Tailoring (Anpassung)
* Nutze den Button "⚙️ Modify", um Parameter-Werte innerhalb der Controls zu definieren.
* Ergänze eigene Texte am Anfang oder Ende der Original-Anforderungen, um lokale Besonderheiten abzubilden.
* Füge zusätzliche Control-IDs bei Bedarf manuell hinzu.

### 4. Risikoanalyse durchführen
* Erstelle Risiko-Einträge und ordne diese entweder dem gesamten System oder spezifischen Assets zu.
* Verknüpfe mitigierende Maßnahmen aus dem Katalog oder erstelle eigene "Custom Controls".

### 5. OSCAL-Paket exportieren
* Aktiviere optional das Häkchen für den Muster-SSP (System Security Plan).
* Klicke auf "Paket generieren", um die resultierenden JSON-Dateien für Profil und SSP herunterzuladen.

# Kurzanleitung: Anforderungen Ausfüllen (Basissicherheitscheck - OSCAL SSP Editor & Workspace)

Dieses Tool dient der detaillierten Bearbeitung von **System Security Plans (SSP)**. Es ermöglicht die Dokumentation der Umsetzung von Sicherheitsmaßnahmen (Controls) für spezifische Komponenten.

### 1. Workspace initialisieren
* **SSP laden**: Lade deine zentrale SSP-JSON-Datei hoch.
* **Assoziierte Dateien**: Lade Profile, Kataloge oder Komponenten-Definitionen hoch, um den Workspace mit Inhalten (Anforderungstexten, Parametern) zu füllen.
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
