# Kapitel 10: Herkunft und Vergleich – von 200-2 und Edition 2023 zu Grundschutz++

**Handbuch zur Grundschutz++ Methodik · Kapitel-Version 0.3 (Entwurf)**
Stand: 2026-08-02 · Quellen: BSI-Standard 200-2 (180 Seiten), Katalog-Build 2026-07-29, Repository `BSI-Bund/Stand-der-Technik-Bibliothek` (Klon vom 2026-08-02: resolved Anwenderkatalog und Mapping-Sammlungen) · Gliederungsbezug: Kapitel 10 gemäß `00_gliederung_v0.1.md`

**Dieses gesamte Kapitel ist ein historischer Vergleich.** Es beschreibt, was aus den Konzepten der 200-x-Welt und des IT-Grundschutz-Kompendiums (Edition 2023) in Grundschutz++ geworden ist. Nichts hierin ist normative Aussage über Grundschutz++ selbst; maßgeblich bleibt allein der Katalog. Wo Zahlen aus den Mapping-Sammlungen stammen, sind sie am Repository-Snapshot vom 2026-08-02 nachgerechnet.

## 10.0 Einordnung: warum der Vergleich ein eigenes Kapitel braucht

Die Zielgruppe dieses Handbuchs bringt 200-2-Vorwissen mit, und genau das ist die Gefahr: Die vertrauten Begriffe existieren fast alle weiter, aber viele bedeuten etwas anderes oder hängen an anderer Stelle. Wer „Modellierung" hört und Bausteine denkt, wer „Grundschutz-Check" hört und „teilweise umgesetzt" ankreuzen will, importiert Altlasten in ein System, das anders gebaut ist. Dieses Kapitel ist die Übersetzungshilfe, und es ist bewusst das einzige, in dem die alte Welt gleichberechtigt neben der neuen steht.

Zur Größenordnung: Der aufgelöste Anwenderkatalog Grundschutz++ (resolved catalog, Build 2026-07-29) umfasst 1000 Controls in 20 Gruppen. Davon entfallen 95 auf die fünf Methodik-Praktiken dieses Handbuchs, 4 auf eine eigenständige Gruppe RISK (Risikomanagement) und 901 auf die vierzehn Kernel-Praktiken von ASST bis TEST samt weiterer Gruppen, die Sicherheitsanforderungen tragen und nicht Gegenstand dieses Handbuchs sind.

## 10.1 Was aus dem 200-2-Vorgehen wurde

Der BSI-Standard 200-2 kennt drei Vorgehensweisen: Basis-Absicherung als Einstieg mit reduziertem Anforderungsumfang, Kern-Absicherung für die Konzentration auf die wichtigsten Werte, Standard-Absicherung als Vollausbau. Grundschutz++ kennt keine benannten Vorgehensweisen mehr. Ihre Funktionen verteilen sich auf drei Mechanismen des Katalogs: Die Priorisierung der Kern-Absicherung lebt im iterativen Vorgehen weiter, denn die Modellierung beginnt beim wichtigsten Geschäftsprozess und erweitert zyklisch (STM.2.1.2, Guidance); die Abstufung des Anforderungsniveaus lebt im Control-Attribut `sec_level` („normal-SdT" / „erhöht") und dessen Überprüfung (STM.3.1); und einen reduzierten Basis-Einstieg unterhalb von „normal-SdT" gibt es nicht mehr, sein nächster Verwandter ist die Aufwandsorientierung über `effort_level` 0 bis 5, die Reihenfolgen nahelegt, aber keine Anforderungen erlässt.

Das Phasenmodell des 200-2 (Initiierung, Organisation, Konzeption, Umsetzung, Aufrechterhaltung) wird zu fünf adressierbaren Praktiken mit maschinenlesbaren Anforderungen:

| 200-2 | Grundschutz++ | Handbuch |
|---|---|---|
| Kap. 3 bis 6: Initiierung, Organisation, Leitlinie, Ressourcen | GC – Governance und Compliance (35 Controls) | Kapitel 4 |
| Kap. 8.1 bis 8.3: Strukturanalyse, Schutzbedarfsfeststellung, Modellierung | GC.7 (Einstufung) und STM – Strukturmodellierung (15 Controls) | Kapitel 4.7, 5 |
| Kap. 8.4: IT-Grundschutz-Check | UMS.1 – Umsetzungsstatus | Kapitel 6.1 |
| Kap. 8.5: Risikoanalyse (nach 200-3) | GC.12, GC.7.2, STM.4 – Methodik frei wählbar | Kapitel 4.12, 5.4 |
| Kap. 9: Umsetzung des Sicherheitskonzepts (Realisierungsplan) | UMS – Umsetzung (11 Controls, Umsetzungsplan) | Kapitel 6 |
| Kap. 10: Aufrechterhaltung und kontinuierliche Verbesserung | PERF – Monitoring-Evaluation (24 Controls) und VRB – Verbesserung (10 Controls) | Kapitel 8, 7 |

Die auffälligste Strukturentscheidung: Was in 200-2 ein einziges Kapitel 10 war, sind in Grundschutz++ zwei Praktiken mit zusammen 34 Controls, mehr als ein Drittel der Methodik. Messung und Verbesserung sind vom Anhängsel zum Schwerpunkt geworden; wer aus der alten Welt kommt und PDCA vor allem als P und D gelebt hat, findet die Rechnung in Kapitel 7 und 8.

## 10.2 Begriffsverschiebungen

| Begriff alt (200-2 / Edition 2023) | Grundschutz++ | Verschiebung |
|---|---|---|
| Geltungsbereich = Informationsverbund (im Zertifizierungskontext synonym) | Geltungsbereich (GC.6.1) und Informationsverbund (STM.1.1) getrennt | formale Leitungsentscheidung vs. technische Ausgestaltung |
| Strukturanalyse | Informationsverbund-Dokument plus Asset-Erfassung (STM.1, STM.2.1.2) | Inventar wandert in die Modellierung, iterativ je Geschäftsprozess |
| Modellierung nach Bausteinen | Anforderungspaket über Zielobjektkategorien mit Vererbung (STM.2) | Baustein entfällt als Einheit; Anforderung wird einzeln modelliert |
| Schutzbedarfskategorien normal / hoch / sehr hoch | Einstufung normal / hoch (GC.7.1.2) | „sehr hoch" entfällt; erhöhter Bedarf läuft über Risikobetrachtung und `sec_level` |
| IT-Grundschutz-Check, Status entbehrlich / ja / teilweise / nein | Ermittlung des Umsetzungsstatus, binär (UMS.1.1) | „entbehrlich" wird zur Streichung mit Begründung (STM.2.1.5), „teilweise" entfällt |
| Realisierungsplan | Umsetzungsplan (UMS.2 ff., VRB.5.1) | gleiches Instrument, erweitert um VRB-Zufluss; Altbegriff überlebt als Relikt in PERF.4.1.7 |
| Risikoanalyse nach 200-3 | Risikomanagement mit freier Methodikwahl (GC.12.1) | 200-3 wird eine Option unter mehreren |
| Basis- / Standard- / Kern-Absicherung | entfällt; iterativer Einstieg plus `sec_level` / `effort_level` | siehe 10.1 |
| Baustein-Kreuzreferenztabelle, elementare Gefährdungen | `threats`-Props (G 0.x) an Kernel-Controls; im Methodik-Teil nicht belegt | Gefährdungsbezug wandert ans einzelne Control |
| Sicherheitskonzept als Dokumentgattung | Dokumentenlandschaft über `documentation`-Props (16 Dokumente allein in GC) | ein Konzeptdokument wird zu vielen gelenkten Einzeldokumenten |
| ISB, Institutionsleitung | unverändert, mit verschärfter Unabhängigkeit (GC.9.1.1.1: `{{einer unabhängigen Person}}`, MUSS) | Kontinuität |

## 10.3 Die Mapping-Sammlungen als Migrationshilfe

Das Repository enthält im Control Layer zwei Mapping-Sammlungen im OSCAL-Format, beide mit `method: human` und `matching-rationale: semantic` erstellt. Sie sind die offiziellen Brücken in die alte und die ISO-Welt, und sie verdienen einen nüchternen Blick auf das, was sie leisten und was nicht.

**ISO/IEC 27001:2022 Annex A → GS++** (Version 1.0.1-qa, Stand 2026-07-27, Status: complete). 96 Map-Einträge übersetzen alle 93 Annex-A-Controls auf die beiden Zielkataloge Methodik und Kernel; die Relationen: 75 subset-of, 16 equivalent-to, 5 intersects-with. Die Leserichtung ist wichtig: Ein Annex-A-Control ist meist „subset-of" mehrerer GS++-Controls, die ISO-Anforderung geht also im breiteren GS++-Anforderungsbestand auf. Praktischer Nutzen: Wer parallel eine native ISO-27001-Zertifizierung bedient oder ein Statement of Applicability pflegt, kann Nachweise aus dem GS++-Anforderungspaket systematisch auf Annex A abbilden, statt doppelt zu dokumentieren.

**IT-Grundschutz Edition 2023 → GS++** (GSMap-Export, Stand 2026-07-21, Status: **draft**). Mit 1185 Map-Einträgen für 824 Kompendiums-Teilanforderungen die eigentliche Migrationshilfe für Bestandsanwender. Die Quell-IDs sind feingranular bis auf Teilanforderungsebene (etwa APP.3.6.A1-UA.2), die Relationen differenziert: 464 subset-of, 395 intersects-with, 187 superset-of, 118 equivalent-to, 21 equal-to. Damit lässt sich für einen bestehenden Grundschutz-Check abschätzen, welche Alt-Nachweise welche GS++-Anforderungen ganz, teilweise oder gar nicht abdecken. Der Draft-Status ist ernst zu nehmen: Die Sammlung entstammt den Review-Entscheidungen des GSMap-Projekts und ist erkennbar in Arbeit.

> **Befund Versionsstand (nachgerechnet am Snapshot 2026-08-02):** Beide Sammlungen referenzieren Methodik-Control-IDs, die es im Katalog-Build 2026-07-29 nicht gibt, auch nicht im resolved catalog desselben Builds. Im ISO-Mapping existieren nur 8 von 23 referenzierten Methodik-IDs, 15 sind veraltet (darunter GC.6.1.3, GC.8.1.1, PERF.7.1); im ITGS-Mapping existieren 20 von 33, 13 sind veraltet (darunter UMS.3.2, VRB.1.2, PERF.5.2). Die Mappings zielen also auf einen älteren, feiner untergliederten Stand der Methodik. Zwei Konsequenzen: Vor jeder produktiven Nutzung gehört ein ID-Abgleich gegen den aktuellen Build ins Werkzeug; und die Differenz belegt, dass die Methodik-Struktur zwischen den Builds noch in Bewegung ist, was für versionsfeste Referenzen die `alt-identifier`-UUIDs statt der sprechenden IDs nahelegt.

**Empfohlener Migrationspfad** (Auslegung dieses Handbuchs, aus den Quellen kombiniert): Erstens Geltungsbereich und Informationsverbund nach GC.6/STM.1 neu festlegen statt die alte Strukturanalyse fortzuschreiben. Zweitens die Schutzbedarfsfeststellung aktiv auf die Zweistufigkeit überführen (Kapitel 4.7). Drittens das Anforderungspaket frisch modellieren (STM.2) und erst dann das ITGS-Mapping nutzen, um Alt-Nachweise den neuen Anforderungen zuzuordnen; die Relationstypen sagen, wo Nachweise genügen (equal-to, equivalent-to), wo sie zu schmal sind (superset-of aus GS++-Sicht) und wo nachgearbeitet werden muss. Viertens den alten Realisierungsplan in den Umsetzungsplan überführen und dabei jedes „teilweise" in nicht umgesetzt plus Maßnahme übersetzen, jedes „entbehrlich" in eine Streichbegründung nach STM.2.1.5 oder eine Ausnahme nach UMS.5.

## 10.4 Konsolidierte Abweichungen zu 200-2 aus den Praktik-Kapiteln

| Thema | 200-2 | Grundschutz++ | Fundstelle |
|---|---|---|---|
| Schutzbedarf | drei Kategorien (normal, hoch, sehr hoch) | zwei Stufen (normal, hoch), GC.7.1.2 | 4.7 |
| Umsetzungsstatus | entbehrlich / ja / teilweise / nein | binär umgesetzt / nicht umgesetzt, UMS.1.1 | 6.1 |
| Modellierung | Baustein-Zuordnung zu Zielobjekten | Anforderungspaket über Zielobjektkategorien mit deterministischer Vererbung, STM.2 | 5.2 |
| Abdeckungsanspruch | Standard-Absicherung: gesamter Informationsverbund | iterativ, wichtigster Geschäftsprozess zuerst, STM.2.1.2 | 5.2 |
| Risikomethodik | 200-3 gesetzt | frei wählbar nach anerkannten Standards, GC.12.1 | 4.12 |
| Vorgehensweisen | Basis / Standard / Kern | entfallen; `sec_level` und Iteration übernehmen die Funktion | 10.1 |
| Verbesserung und Messung | ein Kapitel Aufrechterhaltung | zwei Praktiken (PERF 24, VRB 10 Controls) | 7, 8 |
| Zertifizierungsbezug | Schemata prüfen 200-2-Artefakte A.0 bis A.6 | Dokumentenlandschaft über `documentation`-Props; kein GS++-Prüfschema | 9.2, 9.4 |

## 10.5 Offene Fragen

1. **Zertifizierungsfähige GS++-Konstellation.** Solange die Schemata die Standard- oder Kern-Absicherung nach 200-2 voraussetzen (AudS 6), ist formal ungeklärt, welche GS++-Umsetzung ein Zertifikat trägt (vgl. 9.4, Punkt 7).
2. **Aktualisierung der Mappings.** Beide Sammlungen hinken dem Katalog-Build hinterher; offen ist, ob das BSI die Methodik-Ziel-IDs nachzieht oder auf UUID-Referenzen umstellt. Bis dahin gilt der ID-Abgleich als Pflichtschritt.
3. **Status des ITGS-Mappings.** Draft mit 824 abgedeckten Teilanforderungen; die Gesamtzählung liegt inzwischen vor (Stand 2026-08-29): Gemessen am offiziellen XML-Kompendium 2023 — 1.834 aktive Anforderungen in 111 Bausteinen, zuzüglich 290 entfallene — berührt das ITGS-Mapping 510 Anforderungen (27,8 %), 1.324 bleiben ohne GSMap-Zuordnung. Die Kreuzanalyse mit dem GS++→ED23-Mapping der Werkzeugsammlung (3.046 Zuordnungen nach der Maker-Checker-Verifikation) und dem Prozessbaustein-Mapping ergibt 416 Anforderungen (22,7 %) ohne jede Zuordnung aus irgendeiner der drei Quellen, konzentriert in produktspezifischen SYS-, APP-, INF- und NET-Bausteinen (Spitzenreiter SYS.1.7 IBM Z mit 26 von 34 aktiven Anforderungen); die fünf Prozess-Schichten sind über das Prozessbaustein-Mapping vollständig abgedeckt. Zahlen, Methode und vollständige ID-Listen: `hilfsdateien/ed23_gap_report.md`, deterministisch reproduzierbar via `Gpp-ai-tool/scripts/analyze_ed23_coverage.py`. Offen bleibt der Draft-Status der Sammlung selbst.
4. **RISK-Gruppe.** Die Gruppe RISK im Anwenderkatalog stammt aus dem Katalog „BSI Anforderungen zum Risikomanagement" im Control Layer (10 Controls, RISK.1.1 bis RISK.1.10, Build 2026-07-29), aus dem vier Controls importiert wurden (RISK.1.1, RISK.1.3, RISK.1.5, RISK.1.10); sie sind kein Methodik-Bestandteil, gelten aber im Anwenderkatalog (Exkurs in Kapitel 4.12). Offen bleiben die Doppelregelung RISK.1.1 gegenüber GC.12.1, die Auswahllogik des Imports und die Einordnung als Methodik-Praktik Nr. 6 im Namespace `practices.csv` (Anhang D, D11).

---

*Ende Kapitel 10 (v0.1). Review-Anmerkungen bitte gegen Control-IDs, Schema-Abschnitte und die genannten Repository-Pfade.*
