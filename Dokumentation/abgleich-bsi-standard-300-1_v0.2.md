# Abgleich: BSI-Standard 300-1 „Methodik Grundschutz++" gegen Katalog, Skill und Handbuch

**Version 0.2** · Stand: 2026-10-26 · Changelog: 26.10. abends: Definitionsvergleich der Zielobjektkategorien präzisiert (36 von 39 wortgleich). Korrekturen gegenüber v0.1 (in `_superseded/`): Abdeckung der 35 Mindestkriterien gegen den vollständigen Risikomanagement-Katalog nachgerechnet, Zielobjektkategorien gegen den Build 2026-10-22 statt 2026-08-26 verglichen, Kernel-Zahlen auf den Kernel beschränkt, D9 als teilweise entschieden eingestuft, zweiter defekter Querverweis in Anhang 3 ergänzt. Neu: Repository-Stand 2026-10-23 mit Build 2026-10-22 ausgewertet und das Dokument als Übergangsstand bis zum vom BSI angekündigten Katalog-Update eingeordnet.

Geprüfte Quellen:

| Quelle | Stand | Rolle in diesem Abgleich |
|---|---|---|
| BSI-Standard 300-1, Version 1.0 vom 20.10.2026, 42 Seiten, Referat S 13 | PDF von bsi.bund.de (`?v=3`), Text per pypdf extrahiert, Abbildungen 1 bis 6 nicht auswertbar | Prüfobjekt |
| Stand-der-Technik-Bibliothek, Commit 160c177 vom 2026-10-23 („rolling-publication") | Anwenderkatalog Build 2026-10-22 (1000 Controls, 20 Gruppen), Methodik-Katalog, Kernel, Risikomanagement-Katalog (RISK.1.1 bis RISK.1.10), Profil, Namespaces | Ground Truth nach Skill-Regel 1 |
| Projekt-Build 2026-08-26 (`gpp-resolved_catalog@36a0fac473c6.json`) | Stand der Werkzeuge und des Handbuchs | Vergleichsbasis für den Build-Diff |
| Skill `gs-plusplus-katalogarbeit` (SKILL.md, quellenlage.md) | 2026-08-03 | Vergleichsbasis Arbeitsregeln und Kernbefunde |
| Handbuch zur Grundschutz++-Methodik, Kapitel 1 bis 10, Anhänge A bis D | 2026-08-02 bis 2026-10-16 | Vergleichsbasis Fachtext |

Alle Katalogzahlen sind skriptgestützt aus dem JSON erhoben. Zitate aus dem Standard sind wörtlich, Seitenangaben beziehen sich auf die PDF-Seiten.

## 0. Ausgangslage und Lesart dieses Dokuments

Das BSI hat angekündigt, den Anwenderkatalog an den Standard anzupassen. Der Build vom 2026-10-22, zwei Tage nach dem Standard veröffentlicht, ist diese Anpassung noch nicht: Gegenüber dem Projekt-Build 2026-08-26 sind keine Control-IDs hinzugekommen oder entfallen, zwei Methodik-Controls und 24 Kernel-Controls haben sich geändert (Abschnitt 7). Die inhaltlichen Punkte, an denen der Standard vom Katalog abweicht (Umsetzungsstatus, kategorielose Anforderungen, Restrisiko, Risikobetrachtungs-Auslöser, RISK-Import), stehen im Build unverändert.

Daraus folgt die Lesart: Der Standard beschreibt den Zielzustand, der Build den Ist-Zustand. Abschnitt 3 listet deshalb die Änderungen, die mit dem nächsten Build zu erwarten sind, und benennt je Punkt, was das Handbuch jetzt schreiben kann und was auf den Build warten sollte. Die Rückmeldung an das BSI (Abschnitt 6) beschränkt sich auf das, was der Standard selbst nicht entscheidet: Fehler im Standard, Namens- und Begriffsdifferenzen, Lücken im Profil-Import.

## 1. Was der Standard ist, und was er nicht ist

Der Standard 300-1 übernimmt für Grundschutz++ die Rolle, die der 200-2 für den klassischen IT-Grundschutz hatte: Er beschreibt den Vorgehenszyklus in Prosa. Zielgruppe der Version 1.0 sind laut Einleitung „Early Adopters", die Methodik wurde in Pilotierungsinstitutionen erprobt. Der Zyklus hat fünf Prozessschritte: Erhebung und Planung, Anforderungsanalyse, Realisierung, Überwachung, kontinuierliche Verbesserung. Vier Anhänge liefern die Zielobjektkategorien mit Definitionen, eine vereinfachte Geschäftsprozessanalyse, 35 verbindliche Mindestkriterien für die Risikobetrachtung und die 47 elementaren Gefährdungen.

Drei Eigenschaften des Dokuments bestimmen den ganzen Abgleich. Erstens nennt der Standard keine einzige Control-ID; ein Praktik-Kürzel kommt genau einmal vor, als Klammerzusatz „Umsetzung (UMS)" in Mindestkriterium 31. Zweitens erwähnt er weder OSCAL noch Build-Stände noch die Parameter-Syntax; „Stand der Technik Bibliothek" und GitHub werden je einmal genannt. Drittens trägt er eigene normative Festlegungen, die im Anwenderkatalog kein Control haben (ein Teil der Mindestkriterien, der Statuswert „nicht anwendbar", Mindestfelder für Geschäftsprozesse und Umsetzungsplan, drei Monitoring-Verfahren). Der Katalog kennt den Standard allerdings schon: Die Guidance zu GC.7.1.1 verweist in beiden Builds auf „Prozessschritt 2 - Anforderungsanalyse", und der Build 2026-10-22 benennt das von GC.12.1 geforderte Dokument in „Risikobetrachtung" um, den Begriff des Standards.

## 2. Prozessschritte des Standards und Praktiken des Katalogs

Der Standard ordnet seine Schritte den Praktiken nicht zu. Die Zuordnung unten ist Auslegung anhand der Inhalte.

| Prozessschritt (Standard) | Praktik/Controls (Katalog) | Bemerkung |
|---|---|---|
| 1 Erhebung und Planung (Kap. 2) | GC vollständig, dazu GC.7 Schutzbedarf und die „Initiierung der Risikobetrachtung" (GC.12.1, RISK.1.1/1.3/1.5) | Standard: ISO 27001 Kapitel 4 und 5 |
| 2 Anforderungsanalyse (Kap. 3) | STM.1, STM.2, STM.3, STM.5; neu: Blaupausen (3.3) | Standard: ISO 27001 „Kapitel 6 und 10"; Kapitel 10 ist in ISO 27001:2022 „Verbesserung", vermutlich Fehler (Abschnitt 6) |
| 3 Realisierung (Kap. 4) | UMS vollständig, dazu die Durchführung der Risikobetrachtung (im Katalog STM.4.1) und RISK.1.10 | Die Risikobetrachtung wandert von der Strukturmodellierung in die Realisierung |
| 4 Überwachung (Kap. 5) | PERF.1 bis PERF.5; 5.5 „Validierung der Anforderungen" entspricht PERF.1.3 | Überwachung vor Verbesserung, wie der Wirkfluss im Handbuch 2.2 |
| 5 Kontinuierliche Verbesserung (Kap. 6) | VRB.1 bis VRB.7; 6.4 „Evaluation" entspricht VRB.6 | Standard nennt 6.4 „Prozessschritt Evaluation", obwohl es ein Teilschritt ist |

Der Standard bestätigt damit die These aus Handbuch-Kapitel 2.2: Die Katalogreihenfolge VRB vor PERF ist eine Eigenheit des Katalogs, der Wirkfluss läuft Messung vor Verbesserung.

## 3. Abweichungen zwischen Standard und Build 2026-10-22

### 3.1 Erwartete Katalogänderungen (Standard und Katalog widersprechen sich)

**Umsetzungsstatus: drei Werte statt zwei.** Guidance zu UMS.1.1: „Der Umsetzungsstatus einer Anforderung kann grundsätzlich nur ‚umgesetzt' (‚ja') oder ‚nicht umgesetzt' (‚nein') sein." Standard 4.1.1 (S. 18): „erfüllt" („ja"), „nicht erfüllt" („nein"), „nicht anwendbar", letzterer mit Begründungspflicht, wenn „die Anforderung funktional nicht erfüllt werden kann oder die zugrunde liegende Komponente nicht im Informationsverbund existiert". Das „entbehrlich" des 200-2 ist unter neuem Namen zurück, als Statuswert in der Realisierung. Für OSCAL heißt das: Der Statuswert „not-applicable", den das Handbuch in Kapitel 6.1 und Anhang D (D32, D33) als offenen zweiten Weg beschreibt, ist der vom Standard gedeckte Weg (Auslegung; der Standard sagt nichts zu OSCAL). Erwartung an den Build: Guidance UMS.1.1 mit drittem Wert. Handbuch jetzt: Kasten mit beiden Fassungen; nach dem Build: Kapitel 6.1, 9.3, 9.4 Nr. 5, 10.2, 10.4, Anhang C „Umsetzungsstatus", D32/D33 umschreiben. Der Statuswert heißt im Standard „erfüllt", im Katalog „umgesetzt".

**Anforderungen ohne Zielobjektkategorie: verpflichtend statt Relevanzentscheidung.** Guidance zu STM.2.1.5: Für jede kategorielose Anforderung „ist eine Relevanzentscheidung vorzunehmen", nicht relevante „werden aus dem Anforderungspaket gestrichen, was mit einer Begründung zu dokumentieren ist". Standard 3.4 und 3.4.1 (S. 15 f.): Anforderungen ohne Zielobjektkategorie „sind verpflichtend in das Anforderungspaket aufzunehmen"; die Nichtanwendbarkeit wird erst beim Umsetzungsstatus festgestellt. Beide Wege verlangen eine Begründung, der Ort der Entscheidung wandert aus der Modellierung in die Realisierung. Betroffen sind 265 Kernel-Controls ohne Kategorie (Handbuch D29) und die Streichungslogik des SSP-Generators, der gestrichene Controls über ein Profil mit Positivliste ausblendet. Erwartung an den Build: STM.2.1.5-Guidance ohne Streichung oder mit Verweis auf den Status. Handbuch jetzt: Kasten; Werkzeuge: Statuswert N/A mit Begründungsfeld wird zum Regelweg.

**MUSS-Anforderungen: keine Ausnahme, keine Risikoakzeptanz.** Standard 4.1.2 (S. 19): „Die Durchführung einer Risikobetrachtung kann die Erfüllung einer MUSS-Anforderung nicht ersetzen. Eine Ausnahmegenehmigung oder Risikoakzeptanz ist nicht möglich." Der Katalog kennt in UMS.5.1 „Ausnahmegenehmigungen für Verpflichtungen" und in der Guidance zu STM.4.1 die „Nicht-Umsetzung von Anforderungen" als Auslöser, beides ohne Unterscheidung nach Modalverb. Der Standard verwendet „Ausnahmegenehmigung" außerdem in Mindestkriterium 27 für ein Risiko außerhalb der Akzeptanzkriterien, das die Leitung trotzdem nicht weiter behandeln lässt. Damit ist die Handbuch-Frage D9 (Begriffsumfang „Verpflichtungen" in UMS.5.1) zur Hälfte beantwortet: Ausnahmen von MUSS-Anforderungen gibt es nicht. Ob UMS.5 nur Compliance-Verpflichtungen (GC.3) oder auch SOLLTE-Anforderungen meint, bleibt offen; die Lesart „dauerhafte SOLLTE-Nichterfüllung plus Risikoakzeptanz nach Kriterium 27" ist Auslegung. Die Handbuch-Formulierung in 6.5 und 9.3 („nicht umgesetzte MUSS-Anforderung ohne autorisierte Ausnahme nach UMS.5") ist überholt. Erwartung an den Build: Guidance UMS.5.1 mit Modalverb-Bezug.

**SOLLTE-Anforderungen: temporär oder dauerhaft, Restrisiko als Pflicht.** Standard 4.1.2 (S. 18 f.): Jede nicht erfüllte SOLLTE-Anforderung ist als temporär (vorgesehen, absehbarer Zeitpunkt) oder dauerhaft einzuordnen; dauerhaft löst eine Risikobetrachtung aus (Kriterium 34), die Restrisiken gehen an die Leitung (Kriterium 30). Standard 2.11 (S. 11): „Für SOLLTE-Anforderungen, die in der Umsetzungsplanung enthalten, aber noch nicht erfüllt sind, muss eine Restrisikobetrachtung durchgeführt werden. Das identifizierte Risiko muss durch die Institutionsleitung freigegeben werden." Im Katalog ist die Restrisiko-Bewertung SOLLTE (UMS.1.2), die Kenntnisnahme durch den Risikoeigentümer SOLLTE (RISK.1.9, nicht importiert). Die offene Frage D4 des Handbuchs ist damit im Sinn des Auditierungsschemas entschieden. Eine Unschärfe bleibt im Standard: 2.11 verlangt für temporär nicht erfüllte SOLLTE-Anforderungen eine „Restrisikobetrachtung", 4.1.2 sagt „Eine temporäre Nichterfüllung löst keine Risikobetrachtung aus"; gemeint ist offenbar Risikoidentifikation mit Leitungsinformation (4.1.1) ohne die vollständige Betrachtung nach Anhang 3, definiert ist keiner der beiden Begriffe. Erwartung an den Build: UMS.1.2 als MUSS mit Leitungsfreigabe, oder Import von RISK.1.9 in verschärfter Form.

**Risikomethodik: frei wählbar, aber 35 verbindliche Mindestkriterien.** Guidance GC.12.1: „Die Risikomanagementmethodik kann frei gewählt werden, sollte aber anerkannte Standards erfüllen." Standard 2.11 (S. 11): Verfahren frei wählbar, „sofern die im Anhang [...] festgelegten verbindlichen Mindestkriterien erfüllt werden". Der Risikomanagement-Katalog kennt den Kriterienkatalog bereits: RISK.1.2 „Risikomanagement MUSS die Einhaltung des BSI-Kriterienkatalogs bei der Methodenauswahl anweisen", Guidance „Im Anhang des BSI-Dokuments zur Risikobetrachtung befinden sich einschlägige Kriterien". Das Profil des Anwenderkatalogs importiert RISK.1.2 nicht, ebenso wenig RISK.1.4 (Risikoappetit), RISK.1.6 (Kritikalitätskriterien), RISK.1.7 (Bewertungskriterien), RISK.1.8 (Akzeptanzkriterien) und RISK.1.9 (Restrisiko). Die Abdeckung der Kriterien, nachgerechnet gegen beide Kataloge:

| Mindestkriterium (Anhang 3) | Control im Quellkatalog | Im Anwenderkatalog |
|---|---|---|
| 1, 2 Verfahren verankern | RISK.1.1, GC.12.1 | ja |
| 3, 4 Verfahren dokumentieren | RISK.1.1 (Dokument „Richtlinie zur Risikoanalyse"), GC.12.1 (Dokument „Risikobetrachtung") | ja |
| 5 Rollen, Risikoeigentümer | RISK.1.3 | ja |
| 6 Kriterien für Identifikation und Bewertung | RISK.1.7, RISK.1.6 | nein |
| 7 Risikoappetit | RISK.1.4 | nein |
| 8 Risikoakzeptanzkriterien | RISK.1.8 | nein |
| 9 Autorisierung durch die Leitung | RISK.1.5 | ja |
| 10 methodische Grundlage der Identifikation | keines | – |
| 11 bis 16, 18 bis 29 (Register, Schutzziele, Bewertung, Behandlungsoptionen, Befristung) | keines; 18 bis 22 setzen die Kriterien aus RISK.1.7 und RISK.1.8 voraus | – |
| 17 elementare Gefährdungen bei dauerhaft nicht erfüllten SOLLTE-Anforderungen | keines; Datenbasis sind die `threats`-Props der Kernel-Controls | – |
| 30 Restrisiken durch die Leitung autorisieren | RISK.1.9 (SOLLTE, Risikoeigentümer), UMS.1.2 (SOLLTE) | RISK.1.9 nein, UMS.1.2 ja |
| 31 Umsetzungsplanung durch Risikoeigentümer | RISK.1.10 | ja |
| 32 hoher Schutzbedarf | GC.7.2, STM.4.1 | ja |
| 33 nicht hinreichend abgedeckte Assets | STM.4.1 (Guidance), STM.2.1.6 | ja |
| 34 dauerhafte SOLLTE-Nichterfüllung | STM.4.1 (Guidance „Nicht-Umsetzung", ohne Modalverb-Bezug) | ja |
| 35 jährliche Überprüfung | keines | – |
| Kriterienkatalog als Ganzes | RISK.1.2 | nein |

Der Satz des Handbuchs „200-3 ist eine Option unter mehreren" bleibt richtig, der Satz „frei wählbar" braucht den Zusatz „innerhalb der 35 Mindestkriterien". Die Handbuch-Frage D11 (Auswahllogik des RISK-Imports, vier von zehn) ist damit schärfer gestellt: Der Import lässt genau die Controls aus, die den Anhang 3 des Standards binden. Erwartung an den Build: Import von RISK.1.2 und den Kriterien-Controls, oder Ergänzung in GC.12; bis dahin gilt der Anhang 3 über den Standard, nicht über den Katalog.

**Auslöser der Risikobetrachtung: drei statt vier.** Guidance STM.4.1 nennt hoher Schutzbedarf, Herabstufung des Sicherheitsniveaus von „erhöht" auf „normal-SdT", Nicht-Umsetzung von Anforderungen, Assets ohne passende Anforderungen. Standard 2.11 und Kriterien 32 bis 34 nennen hoher Schutzbedarf „bei mindestens einem Schutzziel", nicht hinreichend abgedecktes Asset, dauerhafte Nichterfüllung einer SOLLTE-Anforderung. Die Herabstufung fehlt, weil der Standard „erhöht"-Anforderungen als optional behandelt (nächster Punkt). Erwartung an den Build: STM.4.1-Guidance mit den drei Auslösern des Standards.

**Sicherheitsniveau „erhöht" = KANN.** Standard 3.4.2 (S. 17): „Anforderungen mit dem Sicherheitsniveau ‚erhöht' beinhalten das Modalverb ‚KANN' und sind optional zu erfüllen. Sie können für die Durchführung der Risikobetrachtung herangezogen werden." Kernel im Build 2026-10-22: 224 Controls mit `sec_level` „erhöht" tragen KANN, drei tragen SOLLTE (BES.1.4 Outsourcing-Strategie, DET.4.12.1 Auslastung des Netzes, REA.2.5 IT-Forensik). Die Verteilung im Kernel insgesamt: 69 MUSS, 608 SOLLTE, 224 KANN; die Temporär/Dauerhaft-Regel aus 4.1.2 trifft also zwei Drittel des Anwenderkatalogs. Das Handbuch beschreibt in 3.6 und 5.3 die „erhöht"-Anforderungen als Zusatzstufe, die bei hohem Schutzbedarf über STM.3.1 hinzugenommen wird; der Standard macht sie zu Kandidaten der Risikobehandlung ohne Pflicht zur Aufnahme. Beide Lesarten sind mit dem Katalog vereinbar, das Handbuch sollte die des Standards als maßgeblich nennen. Erwartung an den Build: die drei Controls auf KANN oder auf „normal-SdT".

### 3.2 Ergänzungen des Standards ohne Widerspruch zum Katalog

**Schutzbedarf.** Standard 2.6 (S. 8 f.) bestätigt „Normal" und „Hoch". Neu: Institutionen dürfen eigene Kategorien definieren, müssen sie aber auf die zwei Stufen abbilden und „in der niedrigsten Kategorie stets der Stand der Technik" einhalten. Die Hoch-Szenarien gehen über die Guidance zu GC.7.1.2 hinaus (Gesetzesverstoß mit existenzbedrohender Folge, informationelles Selbstbestimmungsrecht, persönliche Unversehrtheit, Reputation, Finanzen). Handbuch 4.7 und 10.2.

**Anwendungsbereich, Geltungsbereich, Informationsverbund.** Der Standard sagt durchgehend „Anwendungsbereich (Scope)" (2.3, S. 7) und erlaubt mehrere Informationsverbünde je Anwendungsbereich (3.1, S. 13). GC.6.1 sagt „Geltungsbereich", die Guidance „Scope"; „Anwendungsbereich" kommt in der Methodik nur in Guidances zum Umsetzungsplan vor. Das Handbuch folgt dem Katalog. Begriffsgleichung ins Handbuch (4.6, 10.2, Anhang C), Begriffsdifferenz in die Rückmeldung.

**Zielobjektkategorien.** Anhang 1 des Standards definiert 39 Kategorien unter sieben Wurzeln (Standorte, Nutzende, Netze, IT-Systeme, Informationen, Einkäufe, Anwendungen); der Namespace `target_object_categories.csv` hat 39 Zeilen mit denselben sieben Wurzeln, und der Build 2026-10-22 verwendet in den Props exakt die Namen des Namespace (der Build 2026-08-26 wich an drei Stellen davon ab: „Endgeräte", „Faxe", „Datenträgerarchiv"; die Umbenennung ist Teil der 24 Kernel-Änderungen). Zwischen Standard und Namespace bleiben drei Namen verschieden:

| Standard Anhang 1 | Namespace und Build 2026-10-22 |
|---|---|
| Datenträgerarchiv | Archiv |
| Fax(-anwendungen) | Faxanwendungen |
| Interpersonelle Kommunikationsanwendungen | Interpersonelle Kommunikation |

Die Hierarchie steht im Standard als Abbildung 6 (nicht extrahierbar) und implizit in den Definitionen („Räume: Standorte, die ..."); die Definitionen von Anhang 1 und Namespace sind in 36 von 39 Fällen wortgleich; „Räume" ist im Namespace anders definiert, „Netze" endet anders (Namespace: Beispiele, Standard: „soweit sie Teil des Informationsverbundes sind"), „Outsourcing" unterscheidet sich nur in der Schreibweise „substantiellem"/„substanziellem". Damit ist D30 (Hierarchie nur im Namespace-CSV) teilweise beantwortet: normativ verankert in einem BSI-Standard, maschinenlesbar weiterhin nur im CSV. Nebenbefund im Namespace: Die Spalte „Typ" ist bei „Externe Netzanschlüsse" leer und bei „Institutionsleitung" mit „Mitarbeitende" statt der Wurzel belegt. Handbuch 3.7, Anhang D D30; Werkzeuge mit Kategorienlisten.

**Blaupausen.** Standard 3.3 (S. 14 f.): „ein vorgefertigter Katalog von Anforderungen", auf Anwendungsszenarien zugeschnitten, mit vorgegebenen Parametern; Auswahl inklusive Version, Zuordnung und Anpassungen sind zu dokumentieren; es „kann für bestimmte Institutionen verpflichtende Blaupausen geben". Der Katalog erwähnt Blaupausen einmal, in der Praktik-Beschreibung von STM. Das Handbuch beschreibt sie in 3.8 technisch korrekt als Profile. Neu sind Dokumentationspflicht und mögliche Verpflichtung. Handbuch 3.8, 5.2, Anhang C „Profil".

**Leistungsbewertung und Monitoring.** Standard 5.1 (S. 22): „Da die Entwicklung einheitlicher Vorgaben zur Leistungsbewertung im GS++ noch aussteht, sind die Institutionen frei in der Ausgestaltung." PERF.1.1 verlangt als MUSS ein Verfahren; der Standard bestätigt die Pflicht und erklärt den Inhalt für offen. Standard 5.4 (S. 24 f.) verlangt drei Verfahren mit „müssen": Erkennung von Sicherheitsvorfällen, Umgang mit Schwachstellen, Erfassung neuer Bedrohungen. PERF.5.1 nennt nur „Monitoring-Methoden und -tools"; die drei Verfahren haben im Methodik-Teil kein Control, im Kernel liegen sie in DET und REA. Handbuch 8.1, 8.5.

**Umsetzungsplan und Nachweise.** Standard 4.3 (S. 20): Mindestangaben je Maßnahme sind Anforderung, Datum der Umsetzung oder Überprüfung, dokumentierende oder prüfende Person; Nachweise sind der Maßnahme zuzuordnen; bei automatisierter Prüfung Tool, Zeitpunkt und Ergebnis; Historie empfohlen; Abhängigkeiten zwischen Anforderungen und Maßnahmen kenntlich machen; Elternknoten-Anforderungen priorisieren. Die Guidance zu VRB.5.1 und RISK.1.10 nennt die längere Feldliste (Zuständige, Fristen, Prioritäten, Risiken, Unterschrift des Risikoeigentümers). Der Standard ist das Minimum, die Guidance das Maximum. Die Abhängigkeitsregel beantwortet D3 teilweise: Abhängigkeiten werden im Umsetzungsplan geführt, ihre Quelle bleibt offen; der Namespace definiert in `dependency.txt` den Begriff („zwingende Reihenfolgen"), ohne dass der Methodik-Teil ihn belegt. Handbuch 6.2, 7.5, Anhang D D3; Werkzeug abarbeiten_POAM_generator.html.

**Neue Pflichten ohne Katalog-Control.** Asset-Abhängigkeiten nach Schutzbedarf (3.2: bei normalem Schutzbedarf mindestens Anwendung zu IT-System und IT-System zu Raum, bei hohem der Ressourcenpfad des Geschäftsprozesses), Mindestfelder je Geschäftsprozess (Anhang 2: ID, Name, Verantwortung, Kurzbeschreibung, wesentliche Anwendungen), Risikobetrachtung mindestens jährlich (4.2.3, Kriterium 35), Risikoeigentümer ist standardmäßig der Geschäftsprozesseigentümer (4.2.1, Kriterium 16), Dedupliziergebot für Anforderungen über mehrere Assets derselben Kategorie (3.4). Alle gehören ins Handbuch, markiert als „nur im Standard".

## 4. Abweichungen zum Skill

| Skill-Stelle | Aussage | Stand nach 300-1 | Änderung |
|---|---|---|---|
| SKILL.md, Grundregel 1 | „Katalog vor allem", bei Widerspruch gewinnt der Katalog | Zwei normative Quellen, der Katalog wird nachgezogen | Übergangsregel: Standard = Zielzustand, Build = Ist-Zustand; beide zitieren, Übergang kennzeichnen, nach jedem Build gegen Abschnitt 7 prüfen |
| quellenlage.md, Rangfolge 2 | „Auslegungshilfe bei Lücken: BSI-Standard 200-2" | 300-1 ist die amtliche Methodikbeschreibung, 200-2 Historie | 300-1 auf Rang 2, 200-2 auf einen neuen Rang „historischer Vergleich" |
| quellenlage.md, Rangfolge 3 | „ein GS++-Prüfschema existiert nicht" | Unverändert; 300-1 ist kein Prüfschema, spricht aber von „erheblicher Abweichung" bei gehäufter SOLLTE-Nichterfüllung | Satz ergänzen |
| Kernbefund „Umsetzungsstatus binär" | „teilweise und entbehrlich existieren nicht mehr; Entbehrlich wird zur begründeten Streichung in der Modellierung (STM.2.1.5)" | Drei Werte, „nicht anwendbar" mit Begründung im Status; Streichung in der Modellierung widerspricht dem Standard | Umschreiben, als erwartete Katalogänderung kennzeichnen |
| Kernbefund „Risikomethodik frei wählbar" | „200-3 ist eine Option unter mehreren" | Frei innerhalb der 35 Mindestkriterien; RISK.1.2 bindet sie, ist aber nicht importiert | Ergänzen |
| Kernbefund „RISK ist nicht Methodik, aber gültig" | vier importierte Controls, RISK.1.9 nicht importiert | Der Quellkatalog hat zehn Controls; sechs nicht importierte tragen die Kriterien des Standards | Liste der zehn Controls mit Importstatus aufnehmen |
| Kernbefund „Schutzbedarf zweistufig" | normal/hoch | Bestätigt; eigene Kategorien mit Mapping erlaubt | Ergänzen |
| Kernbefund „Modellierung ohne Bausteine" | Anforderungspaket über Zielobjektkategorien | Bestätigt; Blaupausen als vorgefertigte Kataloge mit Parametern | Ergänzen |
| Kernbefund „Vorgehensweisen entfallen" | Basis/Standard/Kern weg | Bestätigt | Keine |
| Struktur-Abschnitt | „kein KANN" | Gilt für die 95 Methodik-Controls; der Kernel hat 224 KANN auf „erhöht" | Klarstellen |
| Struktur-Abschnitt | Build 2026-07-29 | Build 2026-10-22 mit identischen Methodik-Zahlen (95, 76/19, 14 Parameter plus `gc.12.1-prm1` neu: 15) | Zahlen und Parameterliste nachziehen |
| Grundregel 2 | „Jede normative Aussage trägt eine Control-ID" | Der Standard hat keine IDs; Aussagen aus 300-1 brauchen Kapitel und Seite und, wo vorhanden, das Control | Regel erweitern; `verify_kapitel.py` prüft nur Katalogbezug |
| Typische Fallen | Liste der 200-2-Gewohnheiten | Neu: Prozessschritte des Standards sind keine Praktiken; „Anwendungsbereich" im Standard ist „Geltungsbereich" im Katalog; „erfüllt" im Standard ist „umgesetzt" im Katalog; drei Kategorienamen weichen ab | Ergänzen |

Die Skripte sind nicht betroffen, sie arbeiten gegen das JSON. Eine Zuordnungstabelle Standard-Kapitel zu Control-IDs (Abschnitt 2, verfeinert) wäre ein sinnvolles neues Skript-Produkt oder ein Handbuch-Anhang.

## 5. Abweichungen zum Handbuch, nach Kapiteln

„Jetzt" heißt: vor dem angepassten Build schreibbar, weil nur der Standard betroffen ist. „Nach Build" heißt: der Katalogtext wird sich ändern, bis dahin Kasten mit beiden Fassungen.

| Kapitel | Aussage im Handbuch | Befund 300-1 | Handlungsbedarf | Wann |
|---|---|---|---|---|
| 1.4, readme | Quellenrangfolge: Katalog, dann 200-2 | 300-1 fehlt als Quelle | Rangfolge wie Abschnitt 4; Einleitung um „Early Adopters" und Pilotierung ergänzen | jetzt |
| 2.2 | Wirkfluss PERF vor VRB | Standard bestätigt (Schritte 4 und 5) | Beleg ergänzen | jetzt |
| 2.5, 3.6, 5.3 | Niveau-Weiche: hoher Schutzbedarf nimmt „erhöht" über STM.3.1 hinzu | Standard: „erhöht" ist KANN, optional, dient der Risikobehandlung | Lesart des Standards als maßgeblich | jetzt |
| 3.6, 5.2 | Kategorielose Anforderungen über Relevanzentscheidung mit Streichung | Standard: verpflichtend aufnehmen, Nichtanwendbarkeit im Status | Kasten „Standard und Katalog" | jetzt Kasten, nach Build Text |
| 3.7, D30 | Hierarchie nur im Namespace-CSV | Anhang 1 definiert alle 39; drei Namen weichen ab | Namenstabelle, D30 teilweise erledigt | jetzt |
| 3.8, Glossar | Blaupause = weiteres Profil | Fachliche Definition, Dokumentationspflicht, mögliche Verpflichtung | Ergänzen | jetzt |
| 4.6, 10.2, Glossar | „Geltungsbereich" | „Anwendungsbereich", mehrere Informationsverbünde | Begriffsgleichung | jetzt |
| 4.7 | Hoch-Kriterien aus Guidance GC.7.1.2 | Erweiterte Szenarien, eigene Kategorien | Kasten ergänzen | jetzt |
| 4.12 | GC.12.1 ohne Parameter, Dokument „Risikobewertung" | Build 2026-10-22: Parameter `{{eine einheitliche Methodik}}`, Dokument „Risikobetrachtung" | Nachziehen (D25 teilweise erledigt) | jetzt |
| 4.12, 10.2, 10.4, D11 | Risikomethodik frei; RISK-Import vier von zehn | 35 Mindestkriterien; sechs nicht importierte RISK-Controls tragen sie | Abschnitt mit der Kriterientabelle aus 3.1 | jetzt Tabelle, nach Build Import |
| 5.4 | Vier Auslöser nach STM.4.1 | Drei, Herabstufung fehlt | Kasten | jetzt Kasten, nach Build Text |
| 6.1, 9.3, 9.4 Nr. 5, 10.2, 10.4, Glossar, D32/D33 | Status binär | Drei Werte | Kasten, dann umschreiben | jetzt Kasten, nach Build Text |
| 6.1, 6.9 Nr. 2, 9.4 Nr. 6, Glossar, D4 | Restrisiko nur SOLLTE | Restrisikobetrachtung und Leitungsfreigabe Pflicht | D4 als durch 300-1 entschieden markieren | jetzt |
| 6.5, 9.3, D9 | UMS.5 deckt Ausnahmen auch von MUSS | Keine Ausnahme für MUSS; Ausnahmegenehmigung = Kriterium 27 | 6.5 neu fassen, D9 teilweise | jetzt |
| 6.2, 7.5, D3 | Planfelder aus Guidance VRB.5.1 | Mindestfelder, Nachweisregeln, Abhängigkeiten im Plan | Ergänzen | jetzt |
| 8.1, 8.5 | PERF.1.1 Rahmen, PERF.5.1 Monitoring | Inhalt der Leistungsbewertung offen; drei Verfahren | Ergänzen | jetzt |
| 8.2 | PERF.2.1 „Überwachung der Einhaltung" | Build 2026-10-22: Titel „Überprüfung der Einhaltung" | Titel nachziehen | jetzt |
| 9.3 | Abweichungsklassen aus AudS 4.6 | Standard: „erhebliche Abweichung" | Terminologie-Fund | Rückmeldung |
| 10.1 | 200-2-Phasen zu fünf Praktiken | Dreigliedrig: 200-2, 300-1-Prozessschritte, Praktiken | Spalte 300-1 (Abschnitt 2) | jetzt |
| Anhang A, B | generiert aus Build 2026-07-29 | Build 2026-10-22 | Neu generieren (Skill-Schritt 5) | jetzt |
| Anhang D | D3, D4, D9, D11, D25, D30 offen | D4 entschieden; D3, D9, D11, D25, D30 teilweise | Status nachziehen, Funde aus Abschnitt 6 aufnehmen | jetzt |

## 6. Funde für die Rückmeldung an das BSI

Nur Punkte, die der Standard nicht selbst entscheidet. Die erwarteten Katalogänderungen aus 3.1 gehören nicht hinein, solange die Anpassung läuft; sie stehen in Abschnitt 7 als Prüfliste.

Sachliche Punkte:

1. Profil-Import des Anwenderkatalogs: RISK.1.2 (Einhaltung des BSI-Kriterienkatalogs, MUSS), RISK.1.4, RISK.1.6, RISK.1.7, RISK.1.8 und RISK.1.9 sind nicht importiert; damit haben die Mindestkriterien 6, 7, 8, 30 und der Kriterienkatalog als Ganzes im Anwenderkatalog kein Control (Tabelle in 3.1).
2. Drei Kernel-Controls mit `sec_level` „erhöht" und SOLLTE (BES.1.4, DET.4.12.1, REA.2.5) verletzen die Regel aus 3.4.2 („erhöht beinhaltet KANN").
3. Drei Namen der Zielobjektkategorien weichen zwischen Anhang 1 und Namespace ab (Datenträgerarchiv/Archiv, Fax(-anwendungen)/Faxanwendungen, Interpersonelle Kommunikationsanwendungen/Interpersonelle Kommunikation); die Definitionen von „Räume" und „Netze" unterscheiden sich, „Outsourcing" nur in der Schreibweise.
4. ISO-Zuordnung in Kapitel 3 (S. 12): Prozessschritt 2 soll „Kapitel 6 und 10" der ISO 27001 abdecken; Kapitel 10 ist „Verbesserung" und gehört zu Prozessschritt 5, vermutlich ist Kapitel 8 gemeint. Die Prozessschritte 3 bis 5 haben keine ISO-Zuordnung.
5. Querverweise in Anhang 3: Der Hinweis zu Kriterium 27 nennt eine Überschneidung mit Kriterium 34 (dauerhafte SOLLTE-Nichterfüllung), der Hinweis zu Kriterium 30 sagt „Kriterium 31 regelt ausdrücklich die Ausnahmegenehmigung". Die Ausnahmegenehmigung steht in Kriterium 27, die Überschneidung von 27 besteht mit 30; beide Verweise passen zu einer früheren Nummerierung.
6. Begriffe: „Anwendungsbereich" (Standard) gegen „Geltungsbereich" (GC.6.1); „erfüllt" (Standard) gegen „umgesetzt" (UMS.1.1); „erhebliche Abweichung" (4.1.2) gegen „schwerwiegende Abweichung" (Auditierungsschema 4.6).
7. Unschärfe temporäre Nichterfüllung: 2.11 verlangt eine „Restrisikobetrachtung", 4.1.2 schließt eine „Risikobetrachtung" aus; beide Begriffe sind nicht definiert.
8. Namespace `target_object_categories.csv`: Spalte „Typ" bei „Externe Netzanschlüsse" leer, bei „Institutionsleitung" mit „Mitarbeitende" belegt.

Redaktionelle Punkte: „Kapiteln 4, und 5" (S. 6); „Welche externen Partner oder Dienstleister vom ISMS berücksichtig werden?" (S. 7, Verb und Schreibweise); „mit Ihnen kann" statt „mit ihnen" (S. 14); doppelter Absatz „Durch eine Zuordnung der Zielobjektkategorien ..." am Ende von 3.4.1 und Anfang von 3.4.2 (S. 16); „Die temporäre Nichterfüllung mit einer stichhaltigen Begründung zu dokumentieren" ohne Prädikat (S. 19); „gewährleisteten" (S. 22); „Informationssicherheitsrisken" (S. 23); „sollten mindestens für folgende Aspekte berücksichtigt werden" (S. 23); „Netzte" (S. 29); „Messangeranwendungen" (S. 32); „Prozessschritt Evaluation" für einen Teilschritt (S. 27).

## 7. Build 2026-10-22 und Prüfliste für den angepassten Build

**Was der Build 2026-10-22 ändert** (gegen 2026-08-26, keine ID hinzu oder weg):

- GC.12.1: Statement parametrisiert („MUSS `{{eine einheitliche Methodik}}` für das Informationssicherheitsrisikomanagement [...] verankern", neuer Parameter `gc.12.1-prm1`), gefordertes Dokument „Risikobewertung" wird „Risikobetrachtung".
- PERF.2.1: Titel „Überwachung der Einhaltung von Verpflichtungen" wird „Überprüfung der Einhaltung von Verpflichtungen".
- 24 Kernel-Controls: BER.5.1, BER.5.1.1, BER.5.13, BER.5.2 (Titel und Statements zu Authentifizierungsmitteln), GEB.8.2 und GEB.8.4 (Kategorie „Datenträgerarchiv" wird „Archiv"), KONF.2.6, KONF.3.4, KONF.3.6, KONF.3.6.1, KONF.5.1.2, KONF.6.1.3, KONF.6.3, KONF.12.13, KONF.14.4, SENS.7.12 bis SENS.7.14, SENS.7.18, SENS.7.19, SENS.7.21 bis SENS.7.23, SENS.8.3 (Statement-Texte und Props, darunter die Umbenennungen „Endgeräte" zu „Mobile Endgeräte" und „Faxe" zu „Faxanwendungen").

**Folgen für das Projekt:** Die Werkzeuge pinnen den Bibliotheks-Commit a128311 (Release 4.3); der Build 2026-10-22 liegt auf Commit 160c177 oder später. Mit dem angepassten Build steht das Repin-Verfahren an (`Gpp-ai-tool/scripts/check_pins.py`, Commit 2 neu bauen), außerdem Anhang A und B neu generieren und `verify_kapitel.py` über alle Kapitel laufen lassen.

**Prüfliste für den angepassten Build** (je Zeile: ja/nein eintragen):

| Erwartete Änderung | Fundstelle Standard | Katalogstelle |
|---|---|---|
| Umsetzungsstatus mit „nicht anwendbar" plus Begründung | 4.1.1 | Guidance UMS.1.1 |
| Kategorielose Anforderungen ohne Streichung in der Modellierung | 3.4, 3.4.1 | Guidance STM.2.1.5 |
| Keine Ausnahme für MUSS; Ausnahme als Risikoakzeptanz durch die Leitung | 4.1.2, Kriterium 27 | UMS.5.1, Guidance |
| Restrisiko-Bewertung und Leitungsfreigabe als MUSS | 2.11, 4.1.1, Kriterium 30 | UMS.1.2 oder RISK.1.9-Import |
| Temporäre und dauerhafte Nichterfüllung als Begriffe | 4.1.2 | UMS.1, STM.4.1 |
| Mindestkriterien gebunden | 2.11, Anhang 3 | Import RISK.1.2, RISK.1.4, RISK.1.6 bis RISK.1.9 oder GC.12 |
| Drei Auslöser der Risikobetrachtung | 2.11, Kriterien 32 bis 34 | Guidance STM.4.1 |
| „erhöht" durchgängig KANN | 3.4.2 | BES.1.4, DET.4.12.1, REA.2.5 |
| Jährliche Überprüfung der Risikobetrachtung | 4.2.3, Kriterium 35 | neues Control oder Parameter |
| Drei Monitoring-Verfahren | 5.4 | PERF.5.1 oder Kernel-Verweis |
| Mindestfelder Umsetzungsplan, Nachweiszuordnung | 4.3 | UMS.2, Guidance VRB.5.1 |
| Blaupausen-Dokumentation | 3.3 | STM.2 oder STM.5 |
| Begriff Anwendungsbereich oder Geltungsbereich vereinheitlicht | 2.3 | GC.6.1 |
| Kategorienamen angeglichen | Anhang 1 | Namespace, Props |

## 8. Offene Fragen

1. Abbildung 1 (PDCA-Zuordnung der fünf Schritte) und Abbildung 6 (Hierarchie der Zielobjektkategorien) ließen sich aus dem PDF nicht extrahieren; die Zuordnung Plan/Do/Check/Act in Handbuch 2.2 und die Elternknoten von WLANs (Namespace: Interne Netzsegmente) sind gegen die Grafiken zu prüfen.
2. Wann der angepasste Build erscheint und ob er IDs ändert, ist offen; Referenzen über die `alt-identifier`-UUIDs führen (Skill-Regel 6).
3. Ob die Mindestkriterien über den RISK-Import oder über GC.12 in den Anwenderkatalog kommen, entscheidet das BSI; bis dahin gilt Anhang 3 nur über den Standard.
