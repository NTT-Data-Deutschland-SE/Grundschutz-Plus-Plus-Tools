# Grundschutz++ OSCAL Tools – Version 4.1

Version 4.0 hat die Zusammenarbeit über eine gemeinsame Datenbank gebracht. Version 4.1 schließt die Lücke zwischen Dokumentation und Grundschutzcheck: Der **SSP-Editor liest Nachweisdokumente** und schlägt je Zielobjekt vor, welche Controls damit belegt sind — mit Zitat und Fundstelle, geprüft vom Bearbeiter, bevor etwas ins SSP geschrieben wird (Issue #41). Möglich wurde das, weil die KI-Schicht des SSP-Generators in den gemeinsamen Kern gewandert ist: **eine Backend-Weiche, ein Pool, ein Cache, eine Textextraktion für alle Werkzeuge** (Kern v4). Dazu kommen die seit dem Tag v4.0 aufgelaufenen Nachträge (Quellen-Pins vom 10.09., BSI-Komponenten als Zielobjekte, UI-Feedback samt hellem Farbschema und Suchfeld in langen Listen).

Unverändert gilt: Ohne hinterlegten Server verhält sich alles wie bisher — offline, ohne Backend, nur der Browser. KI-Aufrufe gehen ausschließlich an den in `config.html` gewählten Anbieter, und nichts davon landet ohne Sichtung im SSP.

## Neu: Nachweis-Abgleich im SSP-Editor (Issue #41)

Am Kopf jeder Asset-Karte steht **„⎘ Nachweis prüfen“**. Der Dialog nimmt ein oder mehrere Dokumente (PDF, DOCX, Text, Markdown, CSV, JSON, XML, HTML), verlangt die Einwilligung zur Übermittlung an den KI-Anbieter und bietet vier Einstellungen: Mindest-Konfidenz (mittel oder nur hoch), Umgang mit bestehenden Kommentaren (anhängen oder ersetzen), Bearbeiter und Datum.

Der Abgleich läuft je Dokumentteil und Controls-Block (80 Controls je Aufruf) parallel über den Kern; die Controls kommen DOM-frei aus dem Komponentenmodell, also alle, nicht nur die gerade gezeichneten. Das Modell liefert per JSON-Schema je Control: Status, Konfidenz, einen Umsetzungstext aus dem Belegten und wörtliche Zitate mit Fundstelle (Seite, Abschnitt, Überschrift — PDFs bekommen dafür Seitenmarken). **Belegen mehrere Stellen dasselbe, werden alle genannt**; über alle Teile hinweg bestimmt die höchste Konfidenz Status und Text, die Fundstellen werden zusammengeführt und dedupliziert. Controls ohne Zitat oder unter der Schwelle sind kein Vorschlag, ein Nachweis deckt nie alle Controls ab. Nennt das Modell ein Control, das nicht zum Zielobjekt gehört, wird es ignoriert und im Log genannt.

Vor dem Schreiben zeigt eine **Review-Tabelle** die Vorschläge: bisheriger Stand, vorgeschlagener Status als Auswahl, Reifegrad-Stufe (falls das Profil welche kennt), Konfidenz mit Zahl der Fundstellen und der Kommentar als editierbarer Text — Umsetzung plus Fundstellenliste je Datei. Jede Zeile ist abwählbar. Erst **„Übernehmen“** schreibt, und zwar mit derselben Semantik wie Formular und Excel-Import. Je Datei entsteht eine Resource in der `back-matter` (Titel, SHA-256, Größe, Medientyp, `rlink` auf den Dateinamen; die Datei selbst bleibt beim Anwender, Props im Namespace `…/ns/evidence`), am `by-component` ein Link `rel="evidence"`. Die Control-Karte zeigt den Nachweis als Chip unter dem Kommentar.

Geladene Dokumente bleiben in der Sitzung und lassen sich nacheinander gegen mehrere Zielobjekte prüfen — eine Richtlinie belegt oft mehrere Assets. Ergebnisse werden je Dokumentteil und Controls-Block lokal gecacht (IndexedDB `gpp-ai-cache`); ein Wiederholungslauf nach Abbruch oder mit anderer Schwelle kostet nur die fehlenden Aufrufe. Beide Prompts (System-Instruktion und Abgleich) sind in `config.html` editierbar. Dokumentinhalte gelten dem Modell ausdrücklich als Daten, nie als Anweisung; die Review vor dem Schreiben ist die zweite Sicherung.

## Kern v4: eine KI-Schicht für alle Werkzeuge

Bisher trug jedes Werkzeug eine eigene Kopie der Gemini- und OpenRouter-Aufrufe; der Generator zusätzlich Chunking, Worker-Pool, Retry und Chunk-Cache. Das liegt jetzt einmal in `gpp-core.js`:

* **`gppAi.call()`** — Backend-Weiche für Gemini, OpenRouter und den eigenen OpenAI-kompatiblen Endpoint aus `config.html`. Mit JSON-Schema kommt geparstes JSON (Structured Output, bei Gemini mit Fallback auf die ältere Schemaform, beim eigenen Endpoint mit Fallback auf Text), ohne Schema der Antworttext. Retry mit Backoff, Abbruch-Token, Unternehmenskontext aus `config.html`, Token-Statistik über einen Haken. Bewusst ohne Sampling-Parameter.
* **`gppAi.pool()`, `gppAi.chunk()`, `gppAi.cacheKey()`, `gppAi.cache`** — Worker-Pool mit Fortschritt und Abbruch, Zerlegung nach Zeichen an Absatzgrenzen, SHA-256-Schlüssel, Ergebnis-Cache in IndexedDB.
* **`gppDocText()`** — Text aus PDF, DOCX, Text, JSON, XML und HTML. pdf.js und mammoth lädt der Kern erst bei Bedarf vom CDN; die Seiten tragen keine Script-Tags mehr dafür. Optional mit Seitenmarken, damit ein Modell Fundstellen nennen kann.

Der **SSP-Generator (V5.14.0)** und der **SSP-Editor (v1.7.0)** nutzen den Kern statt eigener Kopien — zusammen rund 600 Zeilen weniger, bei gleichem Verhalten (die Chunk-Cache-Schlüssel des Generators bleiben gültig). Der Generator kann damit erstmals auch den eigenen OpenAI-kompatiblen Endpoint nutzen. Im Editor ist der versteckte Konfigurations-Shim in der Seitenleiste entfallen; Umsetzungsvorschlag und Risiken laufen über denselben Aufruf. Die übrigen fünf Werkzeuge behalten vorerst ihre Kopien und folgen in einem späteren Schritt.

## Seit dem Tag v4.0 außerdem enthalten

Die Nachträge zu 4.0 vom 10. und 11.09. (beschrieben in `RELEASE_NOTES_v4.0.md`) liegen erstmals unter einem Tag:

* **Quellen-Pins auf der Rolling-Publication vom 10.09.** der Stand-der-Technik-Bibliothek (`4e117794`), Pin-Prüfung als Skript `Gpp-ai-tool/scripts/check_pins.py`.
* **BSI-Komponenten sind Zielobjekte wie alle anderen** (#42, #43, #44): Name, Status, Schutzbedarf beim Anlegen; dieselbe Component Definition mehrfach als eigenes Zielobjekt; Vorlagentext nur als Referenz; Umsetzungsstatus startet mit „Offen“.
* **UI-Feedback (#40)**: gemeinsames Stylesheet mit Design-Tokens, Scrollbalken, Artefakte-Fläche mit Schließen-Knopf, Bearbeiter aus einer Vorschlagsliste, **helles Farbschema** (Übersicht und Einstellungen), **Suchfeld in Listen ab elf Einträgen**.

## Nicht im Umfang von 4.1

* Der Excel-Export des Grundschutzchecks führt die Nachweise noch nicht als Spalte.
* Die Nachweisdatei wird nicht ins SSP eingebettet (kein `base64`) — bewusst: Sie bliebe sonst in jedem Set und in der gemeinsamen Datenbank; die Resource trägt SHA-256, Größe und Medientyp, damit ein Prüfer die Datei identifizieren kann.
* Validator, Explorer, BSI → G++ Profil, Prüfung AP/AR und POA&M-Generator rufen ihre Modelle noch mit eigenem Code; die Umstellung auf `gppAi` folgt.

## Versionen der Anwendungen

| Anwendung | Version |
|---|---|
| gemeinsamer Kern (gpp-core.js) | 4 · Cache-Buster v4.1 |
| gemeinsames Stylesheet (gpp-core.css) | 2 · Cache-Buster v4.1 |
| Übersicht (index.html) | 1.7 |
| OSCAL Schema Validator | 1.11.2 |
| SSP-Generator (G++) | V5.14.0 |
| GS++ Explorer (GSpp-Viewer) | v9.8 |
| BSI → G++ Profil (Baustein_2_Profile) | 0.11.0 |
| SSP-Editor (ssp_ausfuellen) | v1.7.0 |
| Prüfung AP/AR (pruefung_ap_ar) | build 9.6.0 |
| POA&M-Generator | v2.4 |

Einzelwerkzeuge in `one-page-apps/` — eigenständig, ohne `gpp-core.js`, von der Datenbank unberührt:

| Anwendung | Version |
|---|---|
| SSP-Generator Edition 2023 | ED23 V1.5 |
| C5 → OSCAL Konverter | v1.1 |

## Hinweise zum Umstieg

- **Einmal mit Strg+F5 laden.** SSP-Generator und SSP-Editor verlangen Kern v4; ein alter Kern aus dem Browser-Cache wird beim Start gemeldet. Die Seiten binden Kern und Stylesheet jetzt mit Cache-Buster `v4.1` ein.
- **KI-Einstellungen nur noch in `config.html`.** Die Seitenleiste des SSP-Editors hat keine Felder für Backend, Key oder Modell mehr — sie waren seit 4.0 nur noch gespiegelt. Wer den eigenen OpenAI-kompatiblen Endpoint nutzt, braucht passende CORS-Header auf dem Server.
- **Nachweise im SSP** folgen einer Konvention dieser Sammlung: Resource in der `back-matter` mit `rlink` (Dateiname, Medientyp, SHA-256) und Props `source-type=evidence`, `size`, `uploaded` im Namespace `https://github.com/NTT-Data-Deutschland-SE/Grundschutz-Plus-Plus-Tools/ns/evidence`; Verweis am `by-component` als Link `rel="evidence"`. OSCAL lässt `rel` frei; der Validator meldet nichts. Fremde Werkzeuge sehen eine normale Resource mit Hash.
- Die Auslieferung bleibt `GS++-oscal-app.zip` (zwölf Dateien); eine einzelne HTML-Datei allein läuft nicht.
