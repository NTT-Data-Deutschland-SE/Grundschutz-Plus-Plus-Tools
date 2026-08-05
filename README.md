# Grundschutz++ Tools

Dieses Repository bündelt Werkzeuge, OSCAL-Artefakte, Zielobjektkategorien, Hilfsdateien und Beispielkataloge für die praktische Arbeit mit Grundschutz++.

Es dient als technische Arbeitsbasis, als zitierfähige Referenz für Publikationen und als zentrale Heimat für wiederverwendbare Inhalte rund um Profile, Komponenten, Prüfunterlagen, Kataloge und unterstützende Automatisierung.

## Werbeblock

In meinem Buch gibt es umfangreiche Analysen und Einen Ausblick auf die Zukunft: [1 Jahr Grundschutz++](https://www.amazon.de/dp/B0GY1HPT89)

## Ziel des Repositories

`Grundschutz-Plus-Plus-Tools` verfolgt vier Ziele:

- **Werkzeuge bereitstellen**, die den operativen Umgang mit Grundschutz++ und OSCAL vereinfachen.
- **Strukturierte Inhalte bündeln**, damit Profile, Komponenten und Hilfsdateien an einem konsistenten Ort liegen.
- **Wiederverwendbare Artefakte veröffentlichen**, die direkt in Projekten, Prüfungen, Workshops oder Veröffentlichungen eingesetzt werden können.
- **Eine stabile Referenz schaffen**, auf die aus Artikeln, Vorträgen, Schulungen und Büchern verwiesen werden kann.

## Inhalt auf einen Blick

Das Repository umfasst insbesondere folgende Bereiche:

- [`Gpp-ai-tool`](./Gpp-ai-tool) – Python-basiertes KI-Werkzeug zur automatisierten Erstellung und Anreicherung von OSCAL-Komponentendefinitionen
- [`GS++-oscal-app`](./GS++-oscal-app) – browserbasierte HTML/JS-Werkzeuge für Modellierung, SSP-Bearbeitung, Audit und Maßnahmenplanung
- [`kataloge`](./kataloge) – produktive OSCAL-Kataloge zu anderen Themen
- [`ED23-Baustein-komponenten`](./ED23-Baustein-komponenten) – produktive OSCAL-Kataloge (Komponentendefinitionen) auf Basis des IT-Grundschutz Edition 2023
- [`zielobjektkategorien`](./zielobjektkategorien) – strukturierte OSCAL-Profile und OSCAL-Komponenten auf Basis von Zielobjektkategorien
- [`hilfsdateien`](./hilfsdateien) – Mapping-, Referenz- und Arbeitsdateien zur Unterstützung der Werkzeuge und Inhalte
- [`beispiel-kataloge`](./beispiel-kataloge) – Beispielkataloge im OSCAL-Format für Demonstration, Tests und Experimente

## Repository-Struktur

```text
Grundschutz-Plus-Plus-Tools/
├── Gpp-ai-tool/
├── GS++-oscal-app/
├── ED23-Baustein-komponenten/
├── zielobjektkategorien/
│   ├── profile/
│   └── komponenten/
├── hilfsdateien/
└── beispiel-kataloge/
```

## Die Verzeichnisse im Detail

### `Gpp-ai-tool`

Dieses Verzeichnis enthält ein Python-basiertes Automatisierungswerkzeug zur Erstellung von OSCAL-Komponentendefinitionen mit KI-Unterstützung.

Im Zentrum steht eine mehrstufige Pipeline zur Ableitung und Anreicherung von Grundschutz++-Artefakten. Das Werkzeug ist darauf ausgelegt, vorhandene fachliche Strukturen maschinell auszuwerten, semantisch zuzuordnen und daraus verwertbare OSCAL-Komponenten zu erzeugen.

#### Zweck

`Gpp-ai-tool` dient insbesondere dazu,

- Zielobjekte und Kontrollen semantisch zuzuordnen,
- Kontrollmengen für Zielobjekte deterministisch zusammenzustellen,
- Komponentendefinitionen automatisiert zu erzeugen,
- generierte Inhalte mit zusätzlichen Implementierungsdetails anzureichern,
- KI-gestützte Verarbeitung in reproduzierbare Verarbeitungsschritte einzubetten.

#### Inhalt von `Gpp-ai-tool`

##### `docs/`
Technische Dokumentation und generierte API-Dokumente.

Beispielhaft liegt hier eine HTML-Dokumentation zur GenAI-API-Nutzung. Das Verzeichnis ist damit die erste Anlaufstelle für technische Detailinformationen zur internen Architektur oder zu einzelnen Schnittstellen.

##### `scripts/`
Hilfs- und Betriebs-Skripte für Entwicklung, Ausführung und Wartung.

Dazu gehören unter anderem Skripte für:

- lokalen Start,
- Cloud-Ausführung,
- Deployment,
- Zurücksetzen von Datastores,
- Code-Status-Extraktion für KI-gestützte Analyse,
- Statistik- und Auswertungsläufe zu Zielobjekten und Controls,
- Statistik- und Auswertungsläufe zu Zielobjektkategorien und Controls,
- kleinere Wartungsaufgaben wie URL-Korrekturen oder Zeilenstatistiken.

Dieses Verzeichnis ist damit der operative Werkzeugkasten für Entwicklung und Betrieb.

##### `src/`
Der eigentliche Anwendungscode.

Die interne Struktur zeigt klar, wie das Werkzeug aufgebaut ist:

- `assets/` – unterstützende Ressourcen und eingebundene Arbeitsdaten
- `clients/` – externe oder interne Client-Abstraktionen, insbesondere für KI-Zugriffe
- `pipeline/` – Orchestrierung der mehrstufigen Verarbeitungslogik
- `utils/` – Hilfsfunktionen für Parsing, Textverarbeitung und technische Unterstützung
- `main.py` – Einstiegspunkt der Anwendung
- `config.py` – Konfiguration
- `constants.py` – zentrale Konstanten und Definitionslisten
- `Dockerfile` / `.dockerignore` – Containerisierung
- `requirements.txt` – Python-Abhängigkeiten

##### `tests/`
Tests, Mock-Daten und Qualitätssicherung.

Hier liegen unter anderem:

- Mock-Datensätze für Testläufe,
- Strukturtests,
- Tests für Parsing und Textverarbeitung,
- Tests für einzelne Pipeline-Stages,
- Prüfungen für Chunking, Matching und Komponentenaufbau.

Das Verzeichnis dokumentiert, dass das Werkzeug nicht nur experimentell gedacht ist, sondern auf reproduzierbare Verarbeitung und technische Nachvollziehbarkeit zielt.

##### Weitere Dateien im Wurzelverzeichnis

- technische oder konzeptionelle Hintergrunddokumente,
- offene Punkte und bekannte Themen,
- projektspezifische Metadaten.

#### Einordnung

`Gpp-ai-tool` ist der Bereich für automatisierte, KI-unterstützte Verarbeitung. Während die browserbasierten Apps vor allem interaktive Facharbeit unterstützen, adressiert dieses Verzeichnis die systematische, programmatische Erzeugung und Anreicherung von OSCAL-Artefakten.

---

### `GS++-oscal-app`

Dieses Verzeichnis enthält browserbasierte Anwendungen als eigenständige HTML/JS-Werkzeuge. Sie sind auf direkte Nutzung ohne komplexes Setup ausgelegt und bilden einen praktischen Workflow von der Modellierung über die Dokumentation bis hin zu Audit und Maßnahmenverfolgung ab.

#### Zweck

`GS++-oscal-app` bündelt Werkzeuge für:

- Modellierung eines Informationsverbunds,
- Erstellung von Profilen und Muster-SSPs,
- Bearbeitung und Pflege von SSPs,
- Planung und Durchführung von Audits,
- Erstellung von Assessment Plans und Assessment Results,
- Überführung offener Feststellungen in einen POA&M,
- Sichtung von Kataloginhalten.

#### Inhalt von `GS++-oscal-app`

##### `blaupausen_generator.html`
Werkzeug zur Modellierung und Erstellung einer Blaupause.

Die Anwendung unterstützt insbesondere:

- Pflege von Metadaten,
- Auswahl eines Basis-ISMS,
- Einbindung von Assets,
- Tailoring von Controls und Parametern,
- Risikoanalyse,
- Export eines OSCAL-Profils,
- optionalen Export eines Muster-SSP.

Diese App ist der typische Einstiegspunkt für neue Vorhaben.

##### `ssp_ausfuellen.html`
Werkzeug zur detaillierten Bearbeitung eines System Security Plans.

Es dient dazu,

- Umsetzungsstände zu dokumentieren,
- Verantwortlichkeiten und Termine zu pflegen,
- referenzierte Ressourcen nachzuladen,
- Parameterwerte zu setzen,
- Risiken mit Maßnahmen zu verknüpfen,
- Inhalte per Suche und Filtern gezielt zu bearbeiten,
- optional KI-Unterstützung für Verständnis, Umsetzung und Einordnung zu verwenden.

##### `pruefung_ap_ar.html`
Werkzeug für Auditplanung und Auditergebnisse.

Die Anwendung unterstützt:

- Import eines ausgefüllten SSP,
- Aufbau eines Assessment Plans,
- Festlegung von Prüfumfang, Zeitplan und Methodik,
- Zuordnung von Prüfmethoden,
- Erfassung von Befunden, Beobachtungen und Risiken,
- Export von Assessment Plan und Assessment Results.

##### `abarbeiten_POAM_generator.html`
Werkzeug zur Bearbeitung von Feststellungen und zum Aufbau eines Maßnahmenplans.

Es überführt offene oder nicht erfüllte Befunde in einen strukturierten POA&M und unterstützt damit die systematische Nachverfolgung der Mängelbehebung.

##### `GSpp-Viewer.html`
Viewer zur Betrachtung von Katalog- oder Anwenderinhalten.

Diese Anwendung ist auf schnelle Sichtung und Navigation durch strukturierte Inhalte ausgerichtet und eignet sich insbesondere für Workshops, Reviews und fachliche Orientierung.

##### `archiv/`
Archivierte oder ältere Anwendungsstände.

Dieses Unterverzeichnis enthält historische oder abgelöste Varianten einzelner Werkzeuge, zum Beispiel frühere Generatoren oder Viewer. Es ist hilfreich, wenn ältere Arbeitsstände nachvollzogen oder Konzepte verglichen werden sollen, gehört aber nicht zum primären empfohlenen Standard-Workflow.

#### Typischer Workflow mit den GS++-oscal-app

1. Mit `blaupausen_generator.html` ein Profil und optional einen Muster-SSP erzeugen.
2. Mit `ssp_ausfuellen.html` die reale Umsetzung dokumentieren und anreichern.
3. Mit `pruefung_ap_ar.html` die Prüfung planen, durchführen und dokumentieren.
4. Mit `abarbeiten_POAM_generator.html` offene Feststellungen in einen Maßnahmenplan überführen.
5. Mit `GSpp-Viewer.html` Inhalte sichten, erläutern oder für Reviews nutzen.

---

### `kataloge`

Dieses Verzeichnis enthält produktive OSCAL-Kataloge aus anderen Quellen.

#### Zweck

Diese Kataloge sind in das OSCAL Katalog Format konvertierte Sicherheitsstandards, die aktuell gültig sind, aber vom Herausgeber nicht als OSCAL bereitgestellt wurden. Es wird keine Garantie übernommen, dass immer die aktuellste Version hier abgelegt ist oder das die Dateien ohne Fehler sind!

---

### `ED23-Baustein-komponenten`

Dieses Verzeichnis enthält produktive OSCAL-Kataloge in Form von Komponentendefinitionen, die auf den Bausteinen des BSI IT-Grundschutz Edition 2023 basieren.

#### Zweck

Die Komponenten in diesem Verzeichnis dienen als produktive Grundlage für:

- Die automatisierte Erstellung und Anreicherung von System Security Plans (SSP).
- Die detaillierte Dokumentation von Umsetzungsmaßnahmen.
- Die Durchführung von Audits auf Basis von Reifegraden (Maturity Levels).

#### Inhalt

Die Dateien sind nach den Bausteinen der Edition 2023 benannt und enthalten "enhanced" Beschreibungen, die über die reinen Anforderungen hinausgehen und konkrete Implementierungsvorschläge sowie Prüfhinweise liefern.

---

### `zielobjektkategorien`

Dieses Verzeichnis enthält die fachlich strukturierte Sammlung von OSCAL-Dateien auf Basis von GS++ Zielobjektkategorien wie sie in der offiziellen Methodik definiert sind.

Es ist der inhaltliche Kernbestand für wiederverwendbare Grundschutz++-Artefakte. Die Dateien sind so benannt, dass sie die jeweilige Zielobjektkategorie klar erkennen lassen und direkt in Werkzeugen, Referenzen oder eigenen Arbeitsabläufen verwendet werden können.

#### Zweck

`zielobjektkategorien` dient dazu,

- Zielobjektkategorien in strukturierter Form bereitzustellen,
- OSCAL-Profile pro Kategorie verfügbar zu machen,
- OSCAL-Komponentendefinitionen pro Kategorie verfügbar zu machen,
- eine nachvollziehbare Zuordnung zwischen fachlicher Kategorie und technischem Artefakt zu schaffen.

#### Inhalt von `zielobjektkategorien`

##### `profile/`
Hier liegen OSCAL-Profile pro Zielobjektkategorie.

Die Benennung folgt einem klaren Muster wie zum Beispiel:

- `administrierende_profile.json`
- `cloud-dienste_profile.json`
- `daten_profile.json`
- `it-systeme_profile.json`
- `webserver_profile.json`
- `wlans_profile.json`

Diese Profile eignen sich als Ausgangspunkt für Modellierung, Tailoring, SSP-Erstellung und Prüfvorbereitung.

##### `komponenten/`
Hier liegen OSCAL-Komponentendefinitionen pro Zielobjektkategorie.

Die Benennung folgt einem parallelen Schema, zum Beispiel:

- `administrierende-component.json`
- `cloud-dienste-component.json`
- `daten-component.json`
- `it-systeme-component.json`
- `office-anwendungen-component.json`
- `serverraeume-component.json`

Diese Dateien sind vor allem dann relevant, wenn mit konkreten Komponenten, wiederverwendbaren Implementierungsbausteinen oder standardisierten Umsetzungsbeschreibungen gearbeitet wird.

#### Einordnung

Während `profile/` stärker den anwendbaren Kontrollrahmen einer Zielobjektkategorie abbildet, liefern `komponenten/` eher umsetzungsnahe und wiederverwendbare Beschreibungen für die praktische Anwendung in Sicherheitskonzepten, Prüfungen oder Automatisierung.

---

### `hilfsdateien`

Dieses Verzeichnis enthält unterstützende Dateien, die in den Werkzeugen, bei der Vorbereitung von OSCAL-Artefakten oder für Mapping- und Referenzzwecke verwendet werden können.

Es ist die technische und fachliche Materialsammlung für wiederkehrende Hintergrunddaten.

#### Zweck

`hilfsdateien` bündelt insbesondere:

- Referenz- und Arbeitsfassungen von Textbeständen,
- Mapping-Dateien,
- strukturierte JSON-Hilfsdaten,
- vorbereitete Kataloge,
- Zuordnungen zwischen Zielobjekten, Controls und Anforderungen.

#### Inhalt von `hilfsdateien`

Die vorhandenen Dateien lassen sich in mehrere Gruppen einordnen:

##### Mapping- und Strukturdateien

- `baustein_zielobjekt.json`
- `prozessbausteine_mapping.json`
- `zielobjekt_controls.json`

Diese Dateien unterstützen die Zuordnung zwischen Bausteinen, Zielobjekten, Controls und Anforderungen. Sie sind besonders wichtig für Automatisierung, Ableitungen und konsistente Referenzierung.

##### Katalog- und Arbeitsdateien im OSCAL-Umfeld

- `c5-2026-oscal-catalog.json`
- `dsgvo_oscal_catalog.json`
- `kritis_oscal_catalog.json`

Diese Dateien liefern zusätzliche, strukturierte Kataloginhalte im OSCAL-Format und können als Grundlage für Beispiele, Tests oder weiterführende Verarbeitung dienen.

#### Einordnung

`hilfsdateien` ist kein Randbereich, sondern das unterstützende Fundament des Repositories. Viele der anderen Inhalte werden erst durch diese Mapping-, Referenz- und Arbeitsdateien effizient nutzbar.

---

### `beispiel-kataloge`

Dieses Verzeichnis enthält beispielhafte OSCAL-Kataloge, die direkt für Demonstrationen, Tests, Vorlagen oder prototypische Ableitungen genutzt werden können.

#### Inhalt von `beispiel-kataloge`

##### `dsgvo_oscal_catalog.json`
Beispielkatalog für die Verarbeitung eines DSGVO-bezogenen Katalogs im OSCAL-Format.

##### `kritis_oscal_catalog.json`
Beispielkatalog für die Verarbeitung eines KRITIS-bezogenen Katalogs im OSCAL-Format.

#### Zweck

Die Beispielkataloge sind besonders nützlich für:

- Demonstrationen,
- Tool-Tests,
- Schulungen,
- Prototyping,
- Validierung von Import- und Exportpfaden,
- Vergleich unterschiedlicher Katalogquellen.

---

## Zusammenspiel der Bereiche

Die Verzeichnisse sind bewusst so angelegt, dass sie zusammen einen nachvollziehbaren Arbeitsfluss unterstützen:

1. **Katalog wählen** – Basiskatalog in `kataloge/` identifizieren.
2. **Inhalte auswählen** – passende Zielobjektkategorie in `zielobjektkategorien/` identifizieren.
3. **Umsetzung festlegen** – produktive Implementierungsbausteine aus `ED23-Baustein-komponenten/` wählen.
4. **Grundlage modellieren** – mit den Apps in `GS++-oscal-app/` Profile und SSPs erzeugen bzw. bearbeiten.
5. **Hilfsdaten einbinden** – Referenz- und Mapping-Dateien aus `hilfsdateien/` zur Unterstützung von Zuordnung, Parsing oder Kontextualisierung nutzen.
6. **Automatisieren und anreichern** – mit `Gpp-ai-tool/` Komponenten, Zuordnungen oder ergänzende Beschreibungen programmatisch erzeugen.
7. **Beispiele und Tests durchführen** – mit den Dateien in `beispiel-kataloge/` Workflows demonstrieren und validieren.

## Für wen dieses Repository gedacht ist

Dieses Repository richtet sich insbesondere an:

- Autorinnen und Autoren fachlicher Publikationen,
- Beraterinnen und Berater im Umfeld von Informationssicherheit,
- Auditorinnen und Auditoren,
- Personen, die mit OSCAL arbeiten,
- Teams, die Grundschutz++-Artefakte praktisch anwenden oder weiterentwickeln,
- Entwicklerinnen und Entwickler, die Automatisierung und Fachlogik verbinden möchten.

## Nutzungshinweise

- Die Verzeichnisse sind bewusst fachlich getrennt, damit Werkzeuge, Inhalte und Hilfsdaten unabhängig voneinander nutzbar bleiben.
- Die GS++-oscal-app eignen sich für direkte interaktive Nutzung im Browser.
- Die Artefakte unter `zielobjektkategorien/`, `hilfsdateien/` und `beispiel-kataloge/` eignen sich für Import, Weiterverarbeitung, Analyse und Referenzierung.
- `Gpp-ai-tool/` ist der technische Bereich für reproduzierbare, skript- und pipelinegestützte Verarbeitung.

## Haftungsausschluss

Die in diesem Repository bereitgestellten Werkzeuge, Kataloge, Profile und sonstigen OSCAL-Artefakte dienen der Unterstützung bei der praktischen Umsetzung von Informationssicherheitsstandards. Trotz sorgfältiger Erstellung und Prüfung kann keine Gewähr für die Richtigkeit, Vollständigkeit, Aktualität oder Fehlerfreiheit der Inhalte und Werkzeuge übernommen werden.

Insbesondere gilt:

- Die Nutzung der bereitgestellten Inhalte erfolgt auf eigene Gefahr.
- Die bereitgestellten OSCAL-Dateien ersetzen keine fachliche Beratung oder offizielle Prüfung/Zertifizierung.
- Die Haftung für Schäden, die aus der Nutzung der Werkzeuge oder Daten entstehen, ist ausgeschlossen, soweit gesetzlich zulässig.
- Für die Übereinstimmung mit offiziellen Publikationen des BSI oder anderer Stellen wird keine Gewähr übernommen; im Zweifelsfall sind die Originaldokumente der Herausgeber maßgeblich.
- Es wird keine Garantie übernommen, dass konvertierte oder angereicherte Kataloge stets dem aktuellsten Stand der zugrunde liegenden Standards entsprechen.

## Referenzierung

Für Verweise in Artikeln, Vorträgen, Büchern oder Dokumentationen empfiehlt es sich, direkt auf:

- das gesamte Repository,
- ein konkretes Unterverzeichnis,
- oder eine einzelne Datei

zu verlinken. Durch die klare Verzeichnisstruktur sind Inhalte dauerhaft fachlich einordenbar und präzise zitierbar.

## Weiterentwicklung

Das Repository ist auf fortlaufende Erweiterung ausgelegt. Neue Zielobjektkategorien, Komponenten, Hilfsdateien, Apps oder Automatisierungsschritte können ergänzt werden, ohne die Grundstruktur zu verändern.
