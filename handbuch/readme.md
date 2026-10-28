# Handbuch zur Grundschutz++ Methodik – Gliederung

**Version 0.2 (Entwurf zur Abstimmung)** · Stand: 2026-10-26 · Änderung 0.2: Quellenrangfolge um den BSI-Standard 300-1 (Version 1.0, 20.10.2026) ergänzt, normative Basis auf den Katalog-Build 2026-10-22 gehoben, neuer Abschnitt 2.7 zu den Prozessschritten des Standards.

Normative Basis: `BSI-Methodik-Grundschutz++-catalog.json`, Build 2026-10-22 (Stand-der-Technik-Bibliothek, Commit 160c177 vom 2026-10-23). Der Katalog enthält 95 Methodik-Controls in fünf Praktiken: GC (35), STM (15), UMS (11), VRB (10), PERF (24). Verbindlichkeit im Bestand: 76 MUSS, 19 SOLLTE, kein KANN. Alle 95 Controls tragen `sec_level: normal-SdT`. Zweite normative Quelle ist seit dem 20.10.2026 der BSI-Standard 300-1 „Methodik Grundschutz++" (Version 1.0, 42 Seiten). Das BSI passt den Anwenderkatalog an den Standard an; der Build 2026-10-22 enthält diese Anpassung noch nicht (Kapitel 1.4).

Abgestimmte Vorentscheidungen (2026-08-02):

1. PERF (Monitoring-Evaluation) ist im Katalog enthalten und wird als fünfte Praktik mit eigenem Kapitel behandelt, obwohl die ursprüngliche Projektbeschreibung nur GC/STM/UMS/VRB nannte. Der Katalog ist Ground Truth.
2. Kapitelschnitt: ein Fachkapitel pro Praktik, Untergruppen als Abschnitte. Jedes Kapitel ist ein eigenes Markdown-Dokument mit Versionsnummer.

Das Handbuch folgt der Katalogreihenfolge GC, STM, UMS, VRB, PERF. Dass damit die Verbesserung (VRB) vor der Messung (PERF) steht, ist eine Eigenheit des Katalogs; Kapitel 2 erklärt den tatsächlichen Wirkzyklus, die Kapitelfolge harmonisiert nichts still.

---

## Teil I – Grundlagen

### Kapitel 1: Einleitung – Grundschutz++ und die Stand-der-Technik-Bibliothek

- 1.1 Was Grundschutz++ ist: maschinenlesbarer Anforderungskatalog statt Kompendium; Einordnung in die Stand-der-Technik-Bibliothek (Control Layer, Nachbarkataloge, Mapping-Sammlungen)
- 1.2 Gegenstand und Abgrenzung dieses Handbuchs: nur die Methodik-Praktiken; die Kernel-Sicherheitsanforderungen (ASST bis TEST) werden ausschließlich dort erwähnt, wo die Methodik auf sie verweist
- 1.3 Zielgruppe und Lesarten: ISBs, Auditoren, Berater mit IT-Grundschutz-Vorwissen ohne Grundschutz++-Erfahrung
- 1.4 Quellen und Rangfolge: Katalog normativ; BSI-Standard 300-1 als zweite normative Quelle und Zielzustand des angekündigten Katalog-Updates; Auditierungs- und Zertifizierungsschema für Prüf- und Zertifizierungsfolgen; BSI-Standard 200-2 nur noch als historischer Vergleich (Kapitel 10). Umgang mit Widersprüchen: Kästen „Standard 300-1 und Katalog-Build 2026-10-22" beziehungsweise „Abweichung zu 200-2 / Schema", nie stille Harmonisierung

### Kapitel 2: Die Methodik im Überblick

- 2.1 Fünf Praktiken, ein Verfahren: Aufgabenteilung und Zusammenspiel von GC, STM, UMS, VRB und PERF
- 2.2 Der Wirkzyklus: GC und STM legen fest, UMS setzt um, PERF misst, VRB korrigiert. Zuordnung zum PDCA-Modell als Lesehilfe, mit Hinweis auf die abweichende Katalogreihenfolge
- 2.3 Die Praktik als Adressat: Anforderungssubjekt ist die Praktik selbst („Governance und Compliance MUSS …"), nicht eine Rolle oder Person; Konsequenzen für Zuständigkeitszuordnung (Bezug GC.9 Sicherheitsorganisation)
- 2.4 Das Dokumentenmodell: die über `documentation`-Props geforderten ISMS-Dokumente (u. a. ISMS-Regelwerk, Informationssicherheitsleitlinie, Informationsverbund, Anforderungspaket, Umsetzungsplan, Auditbericht, Managementbericht); 59 der 95 Controls fordern ein zugeordnetes Dokument
- 2.5 Wie ein Grundschutz++-ISMS in der Praxis anläuft: typische Reihenfolge der ersten Schritte entlang der Controls (GC.1.1 als Ausgangs- und Endpunkt)
- 2.7 Die fünf Prozessschritte des Standards 300-1 und ihre Zuordnung zu den Praktiken

### Kapitel 3: Den Katalog lesen – OSCAL-Lesart der Methodik

- 3.1 Struktur: Praktiken als `groups`, Untergruppen, Controls bis Ebene 4 (tiefster Fall: GC.9.1.1.1.1/GC.9.1.1.1.2; weitere Verschachtelung in GC.3, GC.5, GC.7, GC.10, STM.2, PERF.3, PERF.4)
- 3.2 Die Satzschablone am `statement`: `modal_verb` (MUSS/SOLLTE nach RFC 2119 / DIN 820-2), `action_word`, `result`, `result_specification` mit `{{…}}`-Platzhaltern, `documentation`; Belegung im Methodik-Bestand: `modal_verb`, `action_word`, `result` durchgängig (95/95), `result_specification` 61, `documentation` 59
- 3.3 Parametrisierung: `params` und `{{…}}`-Platzhalter am Beispiel GC.1.1 („nach {{einem anerkannten Standard}}"); Zusammenspiel mit STM.5.1 (Setzen von Parametern)
- 3.4 Control-Eigenschaften: `sec_level` (durchgängig normal-SdT), `effort_level` 0–5 (Verteilung: 75× Stufe 0, 8× 1, 5× 2, 6× 3, 1× 4), `alt-identifier` (stabile UUID), `tags` (9 Controls); nicht belegt im Methodik-Teil: Schutzzielwirkung, `threats`, `target_object_categories` – der Unterschied zu den Kernel-Controls wird benannt
- 3.5 `guidance`-Parts: Stellenwert der Erläuterungen, Verhältnis zur normativen Aussage
- 3.6 Zitierkonventionen dieses Handbuchs: Control-IDs, Modalverben unverändert, Parameter in Originalschreibweise

---

## Teil II – Die fünf Praktiken

Jedes Praktik-Kapitel folgt derselben Schablone. Pro Untergruppe: **Anforderungsbezug** (Controls mit ID, Modalverb, Parametern und gefordertem Dokument), **Umsetzungshinweise** (Praxis), **Audit-Perspektive** (Prüf- und Zertifizierungsfolgen nach Auditierungs-/Zertifizierungsschema), **typische Fehler**. Am Kapitelende: Dokumenten-Output der Praktik und offene Fragen.

### Kapitel 4: GC – Governance und Compliance (35 Controls)

- 4.1 GC.1 Grundlagen (GC.1.1 Errichtung und Aufrechterhaltung eines ISMS, GC.1.2 Freigabe des ISMS)
- 4.2 GC.2 Institutionskontext (GC.2.1 externer, GC.2.2 interner Kontext)
- 4.3 GC.3 Compliance-Management (GC.3.1 mit vier Sub-Controls)
- 4.4 GC.4 Stakeholder (GC.4.1 externe, GC.4.2 interne interessierte Parteien)
- 4.5 GC.5 Informationssicherheitsleitlinie (GC.5.1 Ziele mit vier Sub-Controls)
- 4.6 GC.6 Geltungsbereich (GC.6.1)
- 4.7 GC.7 Informationssicherheitseinstufung (GC.7.1 Vorgehen mit zwei Sub-Controls, GC.7.2 Geschäftsprozesse mit hohem Schutzbedarf) – Katalogtitel lautet „Infomationssicherheitseinstufung" [sic]
- 4.8 GC.8 Ressourcen (GC.8.1 Ressourcenplanung)
- 4.9 GC.9 Sicherheitsorganisation (GC.9.1, tiefste Verschachtelung des Katalogs bis Ebene 4; 8 Controls)
- 4.10 GC.10 Kommunikation (GC.10.1 mit zwei Sub-Controls)
- 4.11 GC.11 Dokumentenlenkung (GC.11.1)
- 4.12 GC.12 Risiko (GC.12.1 Methodik für das Risikomanagement)

### Kapitel 5: STM – Strukturmodellierung (15 Controls)

- 5.1 STM.1 Informationsverbund (STM.1.1 Definition und Abgrenzung, STM.1.2 externe Schnittstellen)
- 5.2 STM.2 Anforderungspaket (STM.2.1 mit sieben Sub-Controls, darunter STM.2.1.4 mit zwei weiteren Ebenen; 10 Controls, fachlicher Kern der Praktik)
- 5.3 STM.3 Sicherheitsniveau (STM.3.1 Überprüfung des gesetzten Sicherheitsniveaus)
- 5.4 STM.4 Risiko (STM.4.1 Durchführung der Risikobetrachtung; Schnittstelle zu GC.12.1)
- 5.5 STM.5 Parametrisierung (STM.5.1 Setzen von Parametern; Rückbezug auf Kapitel 3.3)

### Kapitel 6: UMS – Umsetzung (11 Controls)

- 6.1 UMS.1 Umsetzungsstatus (UMS.1.1 Ermittlung, UMS.1.2 Bewertung des Restrisikos)
- 6.2 UMS.2 Umsetzungsplanung (UMS.2.1 Planung, UMS.2.2 Priorisierung)
- 6.3 UMS.3 Umsetzungszuständige (UMS.3.1 Benennung)
- 6.4 UMS.4 Umsetzungsfristen (UMS.4.1 Festlegung)
- 6.5 UMS.5 Ausnahmemanagement (UMS.5.1 Autorisierung, UMS.5.2 Dokumentation)
- 6.6 UMS.6 Umsetzungsfortschrittsverfolgung (UMS.6.1 Nachverfolgung, UMS.6.2 Fortschreibung des Umsetzungsplans)
- 6.7 UMS.7 Compliance-Management (UMS.7.1 Wahrung von Compliance in der Umsetzung)

### Kapitel 7: VRB – Verbesserung (10 Controls)

- 7.1 VRB.1 Kontinuierliche Verbesserung (VRB.1.1 Verfahren)
- 7.2 VRB.2 Umgang mit Nicht-Konformitäten (VRB.2.1 Umgang, VRB.2.2 Anpassung des ISMS)
- 7.3 VRB.3 Verbesserungspotenziale (VRB.3.1 Identifikation)
- 7.4 VRB.4 Korrektur- und Verbesserungsvorschläge (VRB.4.1 Korrekturmaßnahmen, VRB.4.2 Verbesserungsmaßnahmen)
- 7.5 VRB.5 Korrektur- und Verbesserungsplan (VRB.5.1 Priorisierung)
- 7.6 VRB.6 Wirksamkeitsprüfung (VRB.6.1 Überprüfung, VRB.6.2 Bewertung der erreichten Verbesserung)
- 7.7 VRB.7 Compliance-Management (VRB.7.1 Behandlung von Compliance-Verstößen)

### Kapitel 8: PERF – Monitoring-Evaluation (24 Controls)

- 8.1 PERF.1 Leistungsbewertung des ISMS (PERF.1.1 Verfahren und Regelungen, PERF.1.2 Evaluation des Umsetzungsplans, PERF.1.3 Aktualität der Anforderungen)
- 8.2 PERF.2 Compliance-Management (PERF.2.1 Überwachung der Einhaltung von Verpflichtungen)
- 8.3 PERF.3 Audits (PERF.3.1 Auditprogramm mit vier Sub-Controls, PERF.3.2 Dokumentation von Auditergebnissen mit zwei Sub-Controls; 8 Controls)
- 8.4 PERF.4 Managementbewertungen (PERF.4.1 Eignungsprüfung mit neun Sub-Controls, PERF.4.2 Bericht an die Institutionsleitung; 11 Controls)
- 8.5 PERF.5 Monitoring (PERF.5.1 Methoden und Tools)
- 8.6 Schnittstelle zu VRB: wie Audit- und Bewertungsergebnisse in die Verbesserung fließen

---

## Teil III – Querschnitt

### Kapitel 9: Audit und Zertifizierung der Methodik

- 9.1 Prüfsystematik: wie Auditierungs- und Zertifizierungsschema mit den Methodik-Controls umgehen
- 9.2 Nachweisführung: die geforderten ISMS-Dokumente als Auditevidenz (Rückgriff auf die Dokumentenlandkarte, Anhang B)
- 9.3 Konsequenzen von MUSS- vs. SOLLTE-Abweichungen im Zertifizierungsverfahren
- 9.4 Abweichungen zwischen Katalog und Schemata (konsolidierte Kästen aus den Praktik-Kapiteln)

### Kapitel 10: Herkunft und Vergleich – 200-2 und Edition 2023 (historischer Vergleich, explizit gekennzeichnet)

- 10.1 Was aus BSI-Standard 200-2 wurde: Vorgehensweisen Basis-/Standard-/Kern-Absicherung vs. Praktiken-Modell; dreigliedrige Zuordnung 200-2-Phasen, 300-1-Prozessschritte, Praktiken
- 10.2 Begriffsverschiebungen (u. a. Informationsverbund, Anforderungspaket statt Modellierung, Sicherheitsniveau statt Schutzbedarfskategorien-Logik)
- 10.3 Mapping-Sammlungen der Bibliothek (ISO 27001 → GS++, IT-GS 2023 → GS++) als Migrationshilfe
- 10.4 Konsolidierte Abweichungen zu 200-2 aus den Praktik-Kapiteln

---

## Anhänge

- **Anhang A – Control-Register**: alle 95 Methodik-Controls mit ID, Titel, Modalverb, `effort_level`, gefordertem Dokument (generiert aus dem Katalog, Build-Datum im Kopf)
- **Anhang B – Dokumentenlandkarte**: jedes geforderte ISMS-Dokument mit den Controls, die es fordern
- **Anhang C – Glossar** der Methodik-Begriffe (nur katalogbelegte Begriffe; Definitionen aus `guidance`, Lücken als offene Fragen markiert)
- **Anhang D – Offene Fragen und Abweichungen**: fortlaufende Sammlung aus allen Kapiteln

---

## Arbeitskonventionen

- Dateibenennung: `NN_kuerzel_vX.Y.md` (z. B. `04_gc_v0.1.md`); dieses Dokument ist `00_gliederung_v0.1.md`
- Jede normative Aussage trägt eine Control-ID; Zahlen und Prop-Werte werden bei jeder Kapitelerstellung gegen den Katalog geprüft, nie aus dem Gedächtnis übernommen
- Anhänge A und B werden per Skript aus dem Katalog generiert, nicht von Hand gepflegt
- Aussagen aus dem Standard 300-1 tragen Kapitel und Seite („Standard 300-1, Kap. 4.1.1 (S. 18)"); wo Standard und Katalog-Build sich widersprechen, steht ein Kasten mit beiden Fassungen und der erwarteten Katalogänderung, Anhang D führt die Stellen als D38 bis D44
- Vorgeschlagene Schreibreihenfolge: Kapitel 4 (GC) zuerst, weil dort alle Schablonen-Elemente vorkommen und sich die Kapitelvorlage bewähren muss; danach 5 bis 8, dann 9 und 10; Teil I zuletzt, wenn der Stoff steht

## Offene Punkte zur Abstimmung

1. Tippfehler im Katalog: GC.7 heißt dort „Infomationssicherheitseinstufung". Vorschlag: im Handbuch einmal mit [sic] zitieren, danach korrekte Schreibweise verwenden.
2. Kapitel 10 braucht die Mapping-Sammlungen aus dem Repository (liegen noch nicht im Projektordner). Beschaffen oder Kapitel 10 auf 10.1, 10.2 und 10.4 reduzieren?
3. Umfangsschätzung GC: mit 35 Controls und der Kapitelschablone wird Kapitel 4 voraussichtlich 25 bis 40 Seiten. Falls das zu viel wird, greift die Rückfalloption Splittung (GC.1 bis GC.6 / GC.7 bis GC.12).
