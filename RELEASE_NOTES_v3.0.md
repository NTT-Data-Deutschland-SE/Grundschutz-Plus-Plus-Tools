# Grundschutz++ OSCAL Tools – Version 3.0

Version 3 räumt auf, was mit neun eigenständigen Werkzeugen gewachsen ist: eine gemeinsame Basis statt neun Einzelkonfigurationen, gepinnte Quellen statt beweglicher Branch-URLs, und ein Artefaktbestand, der zeigt, was im Arbeitsablauf schon vorliegt. Dazu die Fehlerbehebungen aus Issue #29.

## Behobene Fehler (Issue #29)

**Mehrere Referenzkataloge im Validator.** Ein SSP schöpft seine Controls in der Praxis aus mehreren Quellen — G++-Anwenderkatalog, ED23-Bausteine und Zusatzkataloge wie DSGVO. Der Validator konnte bisher nur eine Referenz halten; alle Controls der übrigen Kataloge galten als unauflösbar. Im gemeldeten Prüfbericht waren das 89 von 182 Befunden. Jetzt werden beliebig viele Referenzdokumente gleichzeitig gehalten und gegen ihre Vereinigungsmenge geprüft. Gegenprobe an einem Dokument aus zwei Katalogen und einem Profil: mit einer Referenz 3 Fehler, mit allen dreien 1 — nämlich der tatsächlich unauflösbare.

**Verlinkte Kataloge werden gefunden und geladen.** „Load linked sources" folgt jetzt allen Verweisen statt beim ersten Treffer abzubrechen, und findet zusätzlich die Katalogzeiger außerhalb der Import-Mechanik: die Props `source-catalog` und `referenced-catalog` sowie Komponenten-Links mit `rel="catalog"`. Relative rlinks werden gegen die Seiten-URL aufgelöst.

**Ungültige UUIDs aus den SSP-Generatoren.** Die Komponente eines Zusatzkatalogs trug eine ID der Form `catalog-<uuid>` und verletzte damit das OSCAL-uuid-Pattern an jeder referenzierenden Stelle — 54 Schema-Fehler je erzeugtem SSP.

**Zusatzkataloge sind jetzt nachladbar.** Jeder Katalog, aus dem Controls stammen, bekommt eine eigene Back-Matter-Resource mit absoluter URL und SHA-256-Pin; die Katalog-Komponente verlinkt das Fragment. Vorher standen Zusatzkataloge nur als Props im Dokument und waren für Prüfwerkzeuge unsichtbar.

**Zweiter, getrennter KI-Durchgang im Validator.** „AI audit of deterministic findings" legt dem Modell jeden mechanischen Befund samt Quelltextausschnitt und Referenz-Digest vor und lässt ihn bestätigen oder widerlegen (`confirmed` / `refuted` / `setup_artefact` / `uncertain`). Artefakte einer unvollständigen Prüfumgebung werden dadurch als solche sichtbar, statt als Dokumentfehler zu gelten. Der bisherige „AI rules check" bleibt unverändert und prüft weiterhin unabhängig davon das ganze Dokument.

**Qualität der erzeugten SSP.** Komponententypen folgen dem OSCAL-Vokabular statt pauschal `service` zu sein; deutsche Freitexttypen werden abgebildet statt zeichenweise verstümmelt (aus `Raum/Gebäude` wurde vorher `Raum-Geb-ude`). ISMS-Rollen stehen als `metadata/roles`, erkannte Verantwortliche als `responsible-roles`. Schutzbedarf wird nach dem Maximumprinzip auf Systemebene hochgezogen. Assets werden über die `source-id` der Dokumentanalyse abgeglichen statt nur über den Namen, Props und Links beim Zusammenführen dedupliziert. Controls, die nur über ein Prozess-Profil oder einen Zusatzkatalog in den Geltungsbereich kommen, tragen einen expliziten Status statt gar keinen.

Bewusst nicht geändert: das Wertepaar `normal-SdT` / `erhöht`. Das ist das BSI-Vokabular aus `security_level.csv`; der entsprechende Befund im Prüfbericht ist eine Falschmeldung.

## Neu: gemeinsame Basis

**`gpp-core.js`** — Konfiguration, Artefaktspeicher, Prompt-Registrierung, Quellen-Pins und ein ZIP-Writer, einmal vorhanden statt neunmal kopiert.

> **Wichtig für die Weitergabe:** Die Sammlung ist ab Version 3 nur noch als Ganzes lauffähig. Eine einzelne HTML-Datei weiterzureichen genügt nicht mehr — es braucht den Ordner beziehungsweise dieses `GS++-oscal-app.zip`. Fehlt `gpp-core.js`, sagt das jede Anwendung beim Start deutlich, statt still zu scheitern.

**`config.html`** — Backend, API-Schlüssel je Anbieter, Modelle, Thinking-Level, Grounding, Parallelität, Chunk-Größen, Retries und Checker-Route gelten ab jetzt für die gesamte Sammlung. Vorher war derselbe Schlüssel bis zu fünfmal einzutragen, weil jedes Werkzeug ihn unter einem anderen Namen speicherte. Die Werkzeuge haben keine Eingabefelder für Zugangsdaten mehr; sie zeigen nur noch, was gerade gilt, und verlinken hierher. Fehlt ein Schlüssel, sagt jedes Werkzeug, was ohne ihn trotzdem geht — Kataloge laden, tailoren, exportieren und validieren funktionieren durchweg ohne KI.

**37 Prompts aus acht Werkzeugen** werden ebenfalls dort gepflegt. Die Standardtexte bleiben im jeweiligen Werkzeug und werden beim Start angemeldet; bearbeitet wird also immer der aktuelle Stand, statt eine zweite Kopie zu pflegen, die auseinanderläuft.

**Quellen gepinnt — und trotzdem aktuell.** Alle 11 Kataloge und Hilfsdateien hängen an einem festen Commit (Handbuch 3.13/3.14, Grundregel 8). In `config.html` steht je Quelle der Pin, und „Nach Updates suchen" holt den neuesten Commit samt Datum und Commit-Message; übernommen wird er erst auf Klick. Vorher hingen 18 URLs an `refs/heads/main` — ein Upstream-Commit konnte Ergebnisse unter unverändertem Katalog verschieben.

**Artefaktbestand und Übersicht.** Jedes erzeugte OSCAL-Dokument landet zusätzlich zum gewohnten Download in einem gemeinsamen Bestand (IndexedDB, im Browser dieses Rechners, nicht auf einem Server). Die Übersicht zeigt je Workflow-Stufe, was vorliegt, und exportiert den Gesamtbestand als Einzeldateien oder als ZIP mit `manifest.json` samt Prüfsummen. Die Download-Buttons in den Werkzeugen bleiben unverändert.

## Neu: Ordnername, Hilfe und Handbuch

Der App-Ordner heißt ab dieser Version **`GS++-oscal-app`** (vorher `One-Page-Apps`), das Auslieferungsarchiv entsprechend **`GS++-oscal-app.zip`**. Die Übersicht (`index.html`) hat zwei neue Schaltflächen: **Hilfe** rendert das readme der Sammlung direkt im Browser (eigener Markdown-Renderer, keine externen Bibliotheken), **Handbuch** zeigt die Kapitel des Grundschutz++-Handbuchs aus `handbuch/` mit Kapitelnavigation. Geladen wird zuerst lokal, mit GitHub als Fallback für den Betrieb aus dem ZIP.

## Härtung nach internem Review

Vor dem Release lief ein mehrstufiger Review über den gesamten Umbau; alle bestätigten Befunde sind behoben:

* **Baustein_2_Profile war nach dem Umbau funktionsunfähig** (Verweis auf ein entferntes Element brach das Skript beim Laden ab) und hätte mit leerem Gemini-Modell gearbeitet — beides behoben; Testdrive- und Vier-Augen-Checker-Schalter sind wieder sichtbare Run-Optionen.
* **Quellen-Umpinnen wirkt jetzt wirklich:** Alle Werkzeuge lesen ihre registrierten Quellen über die zentrale Registry, statt den Pin nur anzuzeigen. Inhaltsgepinnte Quellen (SHA-256 im Tool) sind in `config.html` als solche markiert und vom Umpinnen ausgenommen.
* **Zentrale Einstellungen greifen überall:** Der Validator übernimmt die Backend-Wahl aus `config.html` (vorher gewann ein alter tool-eigener Schlüssel), zentrale Gemini-Modelle werden nicht mehr still durch Tool-Defaults ersetzt oder verworfen, Grounding/Retries/Thinking gelten auch im Explorer, und die ED23-System-Instruktion ist als editierbarer Prompt registriert.
* **Kein Rückfluss von Schlüsseln:** Zwei Werkzeuge schrieben den zentralen API-Key in alte tool-eigene Speicherplätze zurück; diese Alt-Speicher werden jetzt bereinigt statt befüllt.
* **Prüfsummen stimmen:** `sha256`/`size` im Artefaktbestand und im Export-Manifest passen jetzt byteweise zu den ausgelieferten Dateien.

## Versionen der Anwendungen

| Anwendung | Version |
|---|---|
| Übersicht (index.html) | 1.1 |
| OSCAL Schema Validator | 1.10.1 |
| SSP-Generator (G++) | V5.8.1 |
| SSP-Generator Edition 2023 | ED23 V1.3.1 |
| GS++ Explorer (GSpp-Viewer) | v9.5.2 |
| BSI → G++ Profil (Baustein_2_Profile) | 0.8.5 |
| SSP-Editor (ssp_ausfuellen) | v1.1.1 |
| Prüfung AP/AR (pruefung_ap_ar) | build 9.4.1 |
| POA&M-Generator | v2.2.1 |
| C5 → OSCAL Konverter | unverändert (deterministisch) |

## Hinweise zum Umstieg

- Bereits eingetragene API-Schlüssel der Vorversionen werden **nicht** automatisch übernommen — sie lagen unter tool-eigenen Namen. Einmal in `config.html` neu eintragen.
- Angepasste Prompts der Vorversionen bleiben in ihren alten Speicherplätzen liegen und werden nicht migriert; die Werkzeuge starten mit den Standardtexten, die in `config.html` sichtbar und bearbeitbar sind.
- Wer die Werkzeuge über `file://` öffnet: Der Ordner muss vollständig bleiben. Bei CORS-Fehlern hilft weiterhin `python -m http.server`.
