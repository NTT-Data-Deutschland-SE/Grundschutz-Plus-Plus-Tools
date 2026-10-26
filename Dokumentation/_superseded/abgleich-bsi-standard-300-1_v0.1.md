# Abgleich: BSI-Standard 300-1 „Methodik Grundschutz++" gegen Katalog, Skill und Handbuch

**Version 0.1** · Stand: 2026-10-26 · Changelog: Erstfassung nach Veröffentlichung des Standards.

Geprüfte Quellen:

| Quelle | Stand | Rolle in diesem Abgleich |
|---|---|---|
| BSI-Standard 300-1, Version 1.0 vom 20.10.2026, 42 Seiten, Referat S 13 | PDF von bsi.bund.de (`?v=3`), Text per pypdf extrahiert, Abbildungen 1 bis 6 nicht auswertbar | Prüfobjekt |
| Anwenderkatalog Grundschutz++ (resolved catalog) | Build 2026-08-26 (`gpp-resolved_catalog@36a0fac473c6.json`), 1000 Controls, 20 Gruppen; Methodik-Zahlen identisch mit Build 2026-07-29 | Ground Truth nach Skill-Regel 1 |
| Skill `gs-plusplus-katalogarbeit` (SKILL.md, quellenlage.md) | 2026-08-03 | Vergleichsbasis Arbeitsregeln und Kernbefunde |
| Handbuch zur Grundschutz++-Methodik, Kapitel 1 bis 10, Anhänge A bis D | 2026-08-02 bis 2026-10-16 (Kapitel 3 und Anhang D zuletzt) | Vergleichsbasis Fachtext |

Alle Katalogzahlen in diesem Dokument sind skriptgestützt aus dem JSON erhoben. Zitate aus dem Standard sind wörtlich, Seitenangaben beziehen sich auf die PDF-Seiten.

## 1. Was der Standard ist, und was er nicht ist

Der Standard 300-1 ersetzt für Grundschutz++ die Rolle, die der 200-2 für den klassischen IT-Grundschutz hatte: Er beschreibt den Vorgehenszyklus in Prosa. Zielgruppe der Version 1.0 sind laut Einleitung „Early Adopters", die Methodik wurde in Pilotierungsinstitutionen erprobt. Der Zyklus hat fünf Prozessschritte: Erhebung und Planung, Anforderungsanalyse, Realisierung, Überwachung, kontinuierliche Verbesserung. Vier Anhänge liefern die Zielobjektkategorien mit Definitionen, eine vereinfachte Geschäftsprozessanalyse, 35 verbindliche Mindestkriterien für die Risikobetrachtung und die 47 elementaren Gefährdungen.

Drei Eigenschaften des Dokuments bestimmen den ganzen Abgleich. Erstens nennt der Standard keine einzige Control-ID; die Praktik-Kürzel kommen nur einmal vor, als Klammerzusatz „Umsetzung (UMS)" in Mindestkriterium 31. Zweitens erwähnt er weder OSCAL noch Build-Stände noch die Parameter-Syntax; „Stand der Technik Bibliothek" und GitHub werden je einmal genannt. Drittens trägt er eigene normative Festlegungen, die im Katalog kein Control haben (Mindestkriterien, Statuswert „nicht anwendbar", Mindestfelder für Geschäftsprozesse und Umsetzungsplan, drei Monitoring-Verfahren). Damit entsteht eine zweite normative Quelle neben dem Katalog, und Skill-Regel 1 („der Katalog gewinnt") braucht eine Ergänzung: Wo der Standard mehr verlangt als der Katalog, ist das kein Widerspruch, sondern eine Lücke im Katalog; wo er anderes verlangt, ist es ein Widerspruch und gehört in die Rückmeldung ans BSI.

## 2. Prozessschritte des Standards und Praktiken des Katalogs

Der Standard ordnet seine Schritte nicht den Praktiken zu. Die Zuordnung unten ist Auslegung anhand der Inhalte.

| Prozessschritt (Standard) | Praktik/Controls (Katalog) | Bemerkung |
|---|---|---|
| 1 Erhebung und Planung (Kap. 2) | GC vollständig, dazu GC.7 Schutzbedarf, GC.12.1 und RISK.1.1/1.3/1.5 als „Initiierung der Risikobetrachtung" | Standard: ISO 27001 Kapitel 4 und 5 |
| 2 Anforderungsanalyse (Kap. 3) | STM.1, STM.2, STM.3, STM.5; neu: Blaupausen (3.3) | Standard: ISO 27001 Kapitel „6 und 10"; Kapitel 10 ist in ISO 27001:2022 „Verbesserung", vermutlich Fehler, siehe Abschnitt 6 |
| 3 Realisierung (Kap. 4) | UMS vollständig, dazu Durchführung der Risikobetrachtung (im Katalog STM.4.1, nicht UMS) und RISK.1.10 | Risikobetrachtung wandert von STM nach „Realisierung" |
| 4 Überwachung (Kap. 5) | PERF.1 bis PERF.5; 5.5 „Validierung der Anforderungen" entspricht PERF.1.3 | Reihenfolge Überwachung vor Verbesserung, wie der Wirkfluss im Handbuch 2.2 |
| 5 Kontinuierliche Verbesserung (Kap. 6) | VRB.1 bis VRB.7; 6.4 „Evaluation" entspricht VRB.6 | Standard nennt 6.4 „Prozessschritt Evaluation", obwohl es ein Teilschritt ist |

Der Standard bestätigt damit die Handbuch-These aus Kapitel 2.2: Die Katalogreihenfolge VRB vor PERF ist eine Eigenheit des Katalogs, der Wirkfluss läuft Messung vor Verbesserung.

## 3. Abweichungen zwischen Standard und Katalog

Jede Zeile nennt die Katalogstelle, die betroffene Stelle im Standard, und wer davon im Projekt betroffen ist (S = Skill, H = Handbuch mit Kapitel).

### 3.1 Umsetzungsstatus: drei Werte statt zwei

Guidance zu UMS.1.1: „Der Umsetzungsstatus einer Anforderung kann grundsätzlich nur ‚umgesetzt' (‚ja') oder ‚nicht umgesetzt' (‚nein') sein." Standard 4.1.1 (S. 18): Status „erfüllt (ja)", „nicht erfüllt (nein)", „nicht anwendbar", letzterer mit Begründungspflicht, wenn „die Anforderung funktional nicht erfüllt werden kann oder die zugrunde liegende Komponente nicht im Informationsverbund existiert".

Folgen: Das „entbehrlich" des 200-2 ist unter neuem Namen zurück, und zwar als Statuswert in der Realisierung, nicht als Streichung in der Modellierung. Der OSCAL-Statuswert „not-applicable", den das Handbuch in Kapitel 6.1 und Anhang D (D32, D33) als offenen zweiten Weg beschreibt, ist damit der vom Standard gedeckte Weg. Betroffen: S (Kernbefund „Umsetzungsstatus binär"), H 2.6, 6.1, 9.3, 9.4 Nr. 5, 10.2, 10.4, Anhang C „Umsetzungsstatus", Anhang D D32/D33. Der Statuswert heißt im Standard „erfüllt", im Katalog „umgesetzt"; das Handbuch sollte beide Begriffe nennen.

### 3.2 Anforderungen ohne Zielobjektkategorie: verpflichtend statt Relevanzentscheidung

Guidance zu STM.2.1.5: Für jede kategorielose Anforderung „ist eine Relevanzentscheidung vorzunehmen", nicht relevante „werden aus dem Anforderungspaket gestrichen, was mit einer Begründung zu dokumentieren ist". Standard 3.4 und 3.4.1 (S. 15 f.): Anforderungen ohne Zielobjektkategorie „sind verpflichtend in das Anforderungspaket aufzunehmen". Die Nichtanwendbarkeit wird erst beim Umsetzungsstatus festgestellt (3.1 oben).

Das ist ein echter Widerspruch zwischen Standard und Katalog, kein Mehr an Anforderungen. Er trifft 265 Kernel-Controls ohne Kategorie (Handbuch D29) und die gesamte Streichungslogik des SSP-Generators, der gestrichene Controls über ein Profil mit Positivliste ausblendet. Betroffen: S (Kernbefund „Entbehrlich wird zur begründeten Streichung in der Modellierung"), H 3.6, 5.2, 6.1, 9.4 Nr. 5, Anhang D D29/D33; Werkzeug ssp_generator.html (Statuswert N/A wird zum Regelweg).

### 3.3 MUSS-Anforderungen: keine Ausnahme, keine Risikoakzeptanz

Standard 4.1.2 (S. 19): „Die Durchführung einer Risikobetrachtung kann die Erfüllung einer MUSS-Anforderung nicht ersetzen. Eine Ausnahmegenehmigung oder Risikoakzeptanz ist nicht möglich." Der Katalog kennt in UMS.5.1 „Ausnahmegenehmigungen für Verpflichtungen" und in der Guidance zu STM.4.1 die „Nicht-Umsetzung von Anforderungen" als Risikobetrachtungs-Auslöser, ohne nach Modalverb zu unterscheiden.

Der Standard beantwortet damit die Handbuch-Frage D9 (Begriffsumfang „Verpflichtungen" in UMS.5.1): Ausnahmen gibt es für SOLLTE-Anforderungen (als dauerhafte Nichterfüllung mit Risikobetrachtung) und für Risiken außerhalb der Akzeptanzkriterien (Mindestkriterium 27, dort ausdrücklich „Ausnahmegenehmigung" genannt), für MUSS-Anforderungen nicht. Die Handbuch-Lesart in 6.5 und 9.3 („nicht umgesetzte MUSS-Anforderung ohne autorisierte Ausnahme nach UMS.5") ist damit überholt. Betroffen: H 6.5, 9.3, Anhang C „Ausnahmegenehmigung", Anhang D D9.

### 3.4 SOLLTE-Anforderungen: temporär oder dauerhaft, Restrisiko als Pflicht

Standard 4.1.2 (S. 18 f.): Jede nicht erfüllte SOLLTE-Anforderung ist als temporär (vorgesehen, absehbarer Zeitpunkt) oder dauerhaft einzuordnen; dauerhaft löst eine Risikobetrachtung aus (Mindestkriterium 34), die Restrisiken gehen an die Leitung (Kriterium 30). Standard 2.11 (S. 11): „Für SOLLTE-Anforderungen, die in der Umsetzungsplanung enthalten, aber noch nicht erfüllt sind, muss eine Restrisikobetrachtung durchgeführt werden. Das identifizierte Risiko muss durch die Institutionsleitung freigegeben werden." Im Katalog ist die Restrisiko-Bewertung nur SOLLTE (UMS.1.2).

Damit ist die offene Frage D4 des Handbuchs im Sinn des Auditierungsschemas entschieden: Restrisiko-Darstellung und Leitungsfreigabe sind Pflicht. Der Katalog hinkt hinterher. Zugleich enthält der Standard eine Unschärfe: 2.11 verlangt für temporär nicht erfüllte SOLLTE-Anforderungen eine „Restrisikobetrachtung", 4.1.2 sagt „Eine temporäre Nichterfüllung löst keine Risikobetrachtung aus". Gemeint ist offenbar Risikoidentifikation mit Leitungsinformation (4.1.1) ohne vollständige Risikobetrachtung nach Anhang 3; die Begriffe sind im Standard nicht definiert. Betroffen: H 6.1, 6.9 Nr. 2, 7.9, 9.3, 9.4 Nr. 6, Anhang C „Restrisiko", Anhang D D4.

### 3.5 Risikomethodik: frei wählbar, aber 35 verbindliche Mindestkriterien

Guidance GC.12.1: „Die Risikomanagementmethodik kann frei gewählt werden, sollte aber anerkannte Standards erfüllen." Standard 2.11 (S. 11): Verfahren frei wählbar, „sofern die im Anhang [...] festgelegten verbindlichen Mindestkriterien erfüllt werden"; Anhang 3 enthält 35 Kriterien in den Phasen Initiierung (1 bis 10), Identifikation (11 bis 17), Bewertung (18 bis 22), Behandlung (23 bis 31) und phasenübergreifend (32 bis 35).

Die Kriterien 1 bis 10 decken sich inhaltlich mit den vier importierten RISK-Controls (RISK.1.1 Methode, RISK.1.3 Risikoeigentümer, RISK.1.5 Autorisierung durch die Leitung) und Kriterium 31 mit RISK.1.10 (Freigabe der Umsetzungsplanung durch die Risikoeigentümer). Die übrigen Kriterien haben kein Control im Anwenderkatalog, insbesondere nicht die Pflichtfelder des Risikoregisters (15), die Zuordnung elementarer Gefährdungen bei dauerhaft nicht erfüllten SOLLTE-Anforderungen (17), die vier Behandlungsoptionen (23), die Befristung temporärer Akzeptanz (28) und die jährliche Überprüfung (35). Der Satz des Handbuchs „200-3 ist eine Option unter mehreren" bleibt richtig, der Satz „frei wählbar" ist ohne den Zusatz „innerhalb der 35 Mindestkriterien" falsch. Betroffen: S (Kernbefund „Risikomethodik frei wählbar"), H 4.12, 5.4, 10.2, 10.4, Anhang D D11 (die Auswahllogik des RISK-Imports ist über die Kriterien 1 bis 10 und 31 jetzt teilweise nachvollziehbar).

### 3.6 Auslöser der Risikobetrachtung: drei statt vier

Guidance STM.4.1 nennt vier Auslöser: hoher Schutzbedarf, Herabstufung des Sicherheitsniveaus von „erhöht" auf „normal-SdT", Nicht-Umsetzung von Anforderungen, Assets ohne passende Anforderungen. Standard 2.11 und Kriterien 32 bis 34 nennen drei: hoher Schutzbedarf „bei mindestens einem Schutzziel", nicht hinreichend abgedecktes Asset, dauerhafte Nichterfüllung einer SOLLTE-Anforderung. Die Herabstufung fehlt, weil der Standard „erhöht"-Anforderungen als optional behandelt (3.7). Betroffen: H 3.6, 5.3, 5.4.

### 3.7 Sicherheitsniveau „erhöht" = KANN

Standard 3.4.2 (S. 17): „Anforderungen mit dem Sicherheitsniveau ‚erhöht' beinhalten das Modalverb ‚KANN' und sind optional zu erfüllen. Sie können für die Durchführung der Risikobetrachtung herangezogen werden." Katalog-Build 2026-08-26: 224 Controls mit `sec_level` „erhöht" tragen KANN, drei tragen SOLLTE: BES.1.4 Outsourcing-Strategie, DET.4.12.1 Auslastung des Netzes, REA.2.5 IT-Forensik. Das ist ein Katalogfund gegen die Regel des Standards. Außerdem: 624 „normal-SdT"-Controls tragen SOLLTE, 149 MUSS; die Kernel-Welt ist also überwiegend SOLLTE, und die Temporär/Dauerhaft-Regel aus 3.4 trifft den Großteil des Anwenderkatalogs.

Das Handbuch beschreibt in 3.6 und 5.3 die „erhöht"-Anforderungen als Zusatzstufe, die bei hohem Schutzbedarf über STM.3.1 hinzugenommen wird. Der Standard macht sie zu Kandidaten für die Risikobehandlung, ohne Pflicht zur Aufnahme. Beide Lesarten sind mit dem Katalog vereinbar; das Handbuch sollte die Lesart des Standards als die maßgebliche nennen. Betroffen: H 3.4, 3.6, 5.3, Anhang C „sec_level"; Katalogfund (drei Controls) für Anhang D Teil 2.

### 3.8 Schutzbedarf: zwei Stufen bestätigt, eigene Stufen erlaubt

Standard 2.6 (S. 8 f.) bestätigt „Normal" und „Hoch". Neu: Institutionen dürfen eigene Kategorien definieren, müssen sie aber auf die zwei Stufen abbilden, und „in der niedrigsten Kategorie stets der Stand der Technik" einhalten. Die Hoch-Szenarien sind gegenüber der Guidance zu GC.7.1.2 erweitert (Gesetzesverstoß mit existenzbedrohender Folge, informationelles Selbstbestimmungsrecht, persönliche Unversehrtheit, Reputation, Finanzen). Betroffen: H 4.7 (Kasten „Abweichung zu 200-2" ergänzen), 10.2.

### 3.9 Anwendungsbereich, Geltungsbereich, Informationsverbund

Der Standard verwendet durchgehend „Anwendungsbereich (Scope)" (2.3, S. 7) und erlaubt ausdrücklich mehrere Informationsverbünde je Anwendungsbereich (3.1, S. 13). Der Katalog sagt in GC.6.1 „Geltungsbereich" (Guidance: „Scope"); „Anwendungsbereich" kommt in der Methodik nur in Guidances zum Umsetzungsplan vor. Das Handbuch folgt dem Katalog („Geltungsbereich", Glossar, 10.2). Terminologie-Fund für die Rückmeldung; Handbuch braucht einen Satz, dass beide Begriffe dasselbe meinen. Betroffen: H 4.6, 10.2, Anhang C.

### 3.10 Zielobjektkategorien: 39 gleich 39, drei Namen weichen ab

Anhang 1 des Standards definiert 39 Kategorien unter sieben Wurzeln (Standorte, Nutzende, Netze, IT-Systeme, Informationen, Einkäufe, Anwendungen); der Katalog trägt 39 Kategorienamen in den `target_object_categories`-Props. Abweichende Namen:

| Standard Anhang 1 | Katalog-Prop |
|---|---|
| Mobile Endgeräte | Endgeräte |
| Fax(-anwendungen) | Faxe |
| Interpersonelle Kommunikationsanwendungen | Interpersonelle Kommunikation |

Die Hierarchie steht im Standard als Abbildung 6 (nicht extrahierbar) und implizit in den Definitionen („Räume: Standorte, die ..."). Damit ist die Handbuch-Frage D30 (Zielobjekthierarchie nur im Namespace-CSV) teilweise beantwortet: Die Hierarchie ist jetzt in einem BSI-Standard normativ verankert, maschinenlesbar bleibt sie nur im CSV. Betroffen: H 3.7, Anhang D D30; Werkzeuge mit Kategorienlisten (Zuordnung der drei Namen).

### 3.11 Blaupausen

Standard 3.3 (S. 14 f.): Eine Blaupause ist „ein vorgefertigter Katalog von Anforderungen", auf Anwendungsszenarien zugeschnitten, mit vorgegebenen Parametern; Auswahl inklusive Version, Zuordnung und Anpassungen sind zu dokumentieren; es „kann für bestimmte Institutionen verpflichtende Blaupausen geben". Der Katalog erwähnt Blaupausen einmal in einer Guidance. Das Handbuch beschreibt sie in 3.8 technisch korrekt als Profile. Neu ist die Dokumentationspflicht und die Möglichkeit verpflichtender Blaupausen. Betroffen: H 3.8, 5.2, Anhang C „Profil".

### 3.12 Leistungsbewertung und Monitoring

Standard 5.1 (S. 22): „Da die Entwicklung einheitlicher Vorgaben zur Leistungsbewertung im GS++ noch aussteht, sind die Institutionen frei in der Ausgestaltung." PERF.1.1 verlangt als MUSS ein Verfahren; der Standard bestätigt die Pflicht und erklärt den Inhalt für offen. Standard 5.4 (S. 24 f.) verlangt drei Verfahren mit „müssen": Erkennung von Sicherheitsvorfällen, Umgang mit Schwachstellen, Erfassung neuer Bedrohungen. PERF.5.1 nennt nur „Monitoring-Methoden und -tools"; die drei Verfahren haben im Methodik-Teil kein Control (im Kernel liegen sie in DET und REA). Betroffen: H 8.1, 8.5.

### 3.13 Umsetzungsplan und Nachweise

Standard 4.3 (S. 20): Mindestangaben je Maßnahme sind Anforderung, Datum der Umsetzung oder Überprüfung, dokumentierende oder prüfende Person; Nachweise sind der Maßnahme zuzuordnen; bei automatisierter Prüfung Tool, Zeitpunkt und Ergebnis; Historie empfohlen; Abhängigkeiten zwischen Anforderungen und Maßnahmen sind kenntlich zu machen; Elternknoten-Anforderungen sollen priorisiert werden. Die Guidance zu VRB.5.1 und RISK.1.10 nennt eine längere Feldliste (Zuständige, Fristen, Prioritäten, Risiken, Unterschrift des Risikoeigentümers). Der Standard ist hier das Minimum, die Guidance das Maximum. Die Abhängigkeitsregel beantwortet die Handbuch-Frage D3 teilweise: Abhängigkeiten werden im Umsetzungsplan geführt, ihre Quelle bleibt offen. Betroffen: H 6.2, 7.5, Anhang D D3; Werkzeug abarbeiten_POAM_generator.html (Nachweisfelder).

### 3.14 Neue Pflichten ohne Katalog-Control

Für die Vollständigkeit, ohne Handbuch-Widerspruch: Asset-Abhängigkeiten nach Schutzbedarf (3.2, bei normalem Schutzbedarf mindestens Anwendung zu IT-System und IT-System zu Raum), Mindestfelder je Geschäftsprozess (Anhang 2: ID, Name, Verantwortung, Kurzbeschreibung, wesentliche Anwendungen), Risikobetrachtung mindestens jährlich (4.2.3, Kriterium 35), Risikoeigentümer ist standardmäßig der Geschäftsprozesseigentümer (4.2.1, Kriterium 16), Dedupliziergebot für Anforderungen über mehrere Assets derselben Kategorie (3.4). Alle gehören in das Handbuch als „nur im Standard, nicht im Katalog" markiert.

## 4. Abweichungen zum Skill

| Skill-Stelle | Aussage | Stand nach 300-1 | Änderung |
|---|---|---|---|
| quellenlage.md, Rangfolge 2 | „Auslegungshilfe bei Lücken: BSI-Standard 200-2, nur wo der Katalog schweigt" | 300-1 ist die amtliche Methodikbeschreibung; 200-2 ist Historie | 300-1 auf Rang 2, 200-2 auf einen neuen Rang „historischer Vergleich" |
| quellenlage.md, Rangfolge 3 | „ein GS++-Prüfschema existiert nicht" | Unverändert; 300-1 ist kein Prüfschema, nennt aber „erhebliche Abweichung" bei gehäufter SOLLTE-Nichterfüllung | Satz ergänzen: Auditfolgen weiterhin Auslegung, mit dem Hinweis aus 4.1.2 |
| Kernbefund „Umsetzungsstatus binär" | „teilweise und entbehrlich existieren nicht mehr; Entbehrlich wird zur begründeten Streichung in der Modellierung (STM.2.1.5)" | Drei Werte; „nicht anwendbar" mit Begründung im Status (3.1, 3.2) | Umschreiben; Widerspruch Standard vs. STM.2.1.5 als Katalogfund führen |
| Kernbefund „Risikomethodik frei wählbar" | „200-3 ist eine Option unter mehreren" | Frei innerhalb der 35 Mindestkriterien aus Anhang 3 | Ergänzen |
| Kernbefund „Schutzbedarf zweistufig" | normal/hoch | Bestätigt; eigene Kategorien mit Mapping erlaubt | Ergänzen |
| Kernbefund „Modellierung ohne Bausteine" | Anforderungspaket über Zielobjektkategorien | Bestätigt; dazu Blaupausen als vorgefertigte Kataloge mit Parametern | Ergänzen |
| Kernbefund „Vorgehensweisen entfallen" | Basis/Standard/Kern weg | Bestätigt, der Standard erwähnt sie nicht | Keine |
| Struktur-Abschnitt | „kein KANN" | Gilt für die 95 Methodik-Controls; der Kernel hat 224 KANN auf „erhöht" | Klarstellen, damit niemand den Satz auf den Anwenderkatalog überträgt |
| Grundregel 2 | „Jede normative Aussage trägt eine Control-ID" | Der Standard selbst hat keine IDs; Aussagen aus 300-1 brauchen eine Seitenangabe und, wo vorhanden, das zugehörige Control | Regel um „oder Fundstelle 300-1 Kap./S." erweitern; `verify_kapitel.py` prüft nur Katalogbezug |
| Typische Fallen | Liste der 200-2-Gewohnheiten | Neu: Prozessschritte des Standards sind keine Praktiken; „Anwendungsbereich" im Standard ist „Geltungsbereich" im Katalog; „erfüllt" im Standard ist „umgesetzt" im Katalog | Ergänzen |

Die Skripte des Skills sind nicht betroffen; sie arbeiten gegen das JSON. Eine Zuordnungstabelle Standard-Kapitel zu Control-IDs (Abschnitt 2 oben, verfeinert) wäre ein sinnvolles neues Skript-Produkt oder ein Handbuch-Anhang.

## 5. Abweichungen zum Handbuch, nach Kapiteln

| Kapitel | Aussage im Handbuch | Befund 300-1 | Handlungsbedarf |
|---|---|---|---|
| 1.4, readme | Quellenrangfolge: Katalog, dann 200-2 | 300-1 fehlt als Quelle | Rangfolge wie in Abschnitt 4 ändern; Einleitung um Zielgruppe „Early Adopters" und Pilotierung ergänzen |
| 2.2 | Wirkfluss PERF vor VRB, Katalogreihenfolge umgekehrt | Standard bestätigt den Wirkfluss (Überwachung ist Schritt 4, Verbesserung Schritt 5) | Beleg ergänzen |
| 2.5, 3.6 | Niveau-Weiche: hoher Schutzbedarf nimmt „erhöht"-Anforderungen über STM.3.1 hinzu | Standard: „erhöht" ist KANN und optional, dient der Risikobehandlung | Lesart des Standards als maßgeblich benennen (3.7) |
| 3.6, 5.2 | Kategorielose Anforderungen über Relevanzentscheidung mit Streichung (STM.2.1.5) | Standard: verpflichtend aufnehmen, Nichtanwendbarkeit im Status | Widerspruchskasten „Abweichung Standard vs. Katalog" (3.2) |
| 3.7, D30 | Hierarchie nur im Namespace-CSV | Anhang 1 des Standards definiert alle 39 Kategorien; drei Namen weichen ab | Namenstabelle, D30 als teilweise erledigt markieren (3.10) |
| 3.8, Glossar | Blaupause = weiteres Profil | Standard definiert Blaupausen fachlich, mit Dokumentationspflicht und möglicher Verpflichtung | Ergänzen (3.11) |
| 4.6, 10.2, Glossar | „Geltungsbereich" | Standard: „Anwendungsbereich", mehrere Informationsverbünde erlaubt | Begriffsgleichung aufnehmen (3.9) |
| 4.7 | Hoch-Kriterien aus Guidance GC.7.1.2 | Erweiterte Szenarienliste, eigene Kategorien mit Mapping | Kasten ergänzen (3.8) |
| 4.12, 10.2, 10.4 | Risikomethodik frei wählbar | 35 verbindliche Mindestkriterien | Neuer Abschnitt oder Anhang mit Zuordnung Kriterien zu RISK/GC-Controls (3.5) |
| 5.4 | Vier Auslöser nach STM.4.1 | Standard nennt drei, Herabstufung fehlt | Abweichungskasten (3.6) |
| 6.1, 9.3, 9.4 Nr. 5, 10.2, 10.4, Glossar | Status binär | Drei Werte, „nicht anwendbar" mit Begründung | Kasten umschreiben, D32/D33 fortschreiben (3.1) |
| 6.1, 6.9 Nr. 2, 9.4 Nr. 6, Glossar, D4 | Restrisiko nur SOLLTE | Standard: Restrisikobetrachtung und Leitungsfreigabe Pflicht | D4 als durch 300-1 entschieden markieren; Katalogfund „UMS.1.2 müsste MUSS sein" (3.4) |
| 6.5, 9.3, D9 | UMS.5 deckt Ausnahmen von beliebigen Anforderungen, auch MUSS | Standard: keine Ausnahme für MUSS; Ausnahmegenehmigung = Kriterium 27 | Abschnitt 6.5 neu fassen (3.3) |
| 6.2, 7.5 | Planfelder aus Guidance VRB.5.1 | Standard setzt Mindestfelder und Nachweisregeln | Ergänzen (3.13) |
| 8.1 | PERF.1.1 Rahmenanforderung | Standard: Inhalt der Leistungsbewertung noch offen | Hinweis ergänzen (3.12) |
| 8.5 | PERF.5.1 Monitoring | Standard verlangt drei konkrete Verfahren | Ergänzen (3.12) |
| 9.3 | Abweichungsklassen Empfehlung/geringfügig/schwerwiegend aus AudS 4.6 | Standard spricht von „erhebliche Abweichung" | Terminologie-Fund in die Rückmeldung |
| 10.1 | Phasenmodell 200-2 zu fünf Praktiken | Jetzt dreigliedrig: 200-2-Phasen, 300-1-Prozessschritte, Katalog-Praktiken | Tabelle um die Spalte 300-1 erweitern (Abschnitt 2) |
| Anhang D | D3, D4, D9, D11, D30 offen | D4 und D9 entschieden, D3, D11, D30 teilweise | Status nachziehen, neue Funde aus Abschnitt 6 aufnehmen |

## 6. Funde im Standard (für die Rückmeldung ans BSI)

Sachliche Punkte:

1. Widerspruch zum Katalog bei kategorielosen Anforderungen: Standard 3.4.1 („verpflichtend aufzunehmen") gegen Guidance STM.2.1.5 (Relevanzentscheidung mit Streichung). Eine der beiden Stellen muss geändert werden.
2. Widerspruch zum Katalog beim Umsetzungsstatus: Standard 4.1.1 (drei Werte) gegen Guidance UMS.1.1 (zwei Werte).
3. Verbindlichkeitslücke: Standard 2.11 macht die Restrisikobetrachtung zur Pflicht, UMS.1.2 ist SOLLTE.
4. Drei Kernel-Controls mit `sec_level` „erhöht" und SOLLTE (BES.1.4, DET.4.12.1, REA.2.5) verletzen die Regel aus 3.4.2 („erhöht beinhaltet KANN").
5. ISO-Zuordnung in 3 (S. 12): Prozessschritt 2 soll „Kapitel 6 und 10" der ISO 27001 abdecken; Kapitel 10 ist „Verbesserung" und gehört zu Prozessschritt 5. Vermutlich ist Kapitel 8 (Betrieb) gemeint. Die Prozessschritte 3 bis 5 haben keine ISO-Zuordnung.
6. Begriffe: „Anwendungsbereich" (Standard) gegen „Geltungsbereich" (GC.6.1); „erfüllt" (Standard) gegen „umgesetzt" (UMS.1.1); „erhebliche Abweichung" (4.1.2) gegen „schwerwiegende Abweichung" (Auditierungsschema 4.6).
7. Unschärfe temporäre Nichterfüllung: 2.11 verlangt eine „Restrisikobetrachtung", 4.1.2 schließt eine „Risikobetrachtung" aus; beide Begriffe sind nicht definiert.
8. Querverweise in Anhang 3: Der Hinweis zu Kriterium 30 sagt „Kriterium 31 regelt ausdrücklich die Ausnahmegenehmigung"; die Ausnahmegenehmigung steht in Kriterium 27, Kriterium 31 regelt die Freigabe der Umsetzungsplanung.
9. Drei Namen der Zielobjektkategorien weichen zwischen Anhang 1 und den Katalog-Props ab (3.10).
10. Die Mindestkriterien 11 bis 30 und 32 bis 35 haben kein Control im Anwenderkatalog; der RISK-Import (vier von zehn Controls) deckt nur Initiierung und Freigabe.

Redaktionelle Punkte: „Kapiteln 4, und 5" (S. 6); „Welche externen Partner oder Dienstleister vom ISMS berücksichtig werden?" (S. 7, Verb und Schreibweise); „mit Ihnen kann" statt „mit ihnen" (S. 14); doppelter Absatz „Durch eine Zuordnung der Zielobjektkategorien ..." am Ende von 3.4.1 und Anfang von 3.4.2 (S. 16); „Die temporäre Nichterfüllung mit einer stichhaltigen Begründung zu dokumentieren" ohne Prädikat (S. 19); „gewährleisteten" (S. 22); „Informationssicherheitsrisken" (S. 23); „sollten mindestens für folgende Aspekte berücksichtigt werden" (S. 23); „Netzte" (S. 29); „Messangeranwendungen" (S. 32); „Prozessschritt Evaluation" für einen Teilschritt (S. 27).

## 7. Offene Fragen

1. Abbildung 1 (PDCA-Zuordnung der fünf Schritte) und Abbildung 6 (Hierarchie der Zielobjektkategorien) ließen sich aus dem PDF nicht extrahieren; die Zuordnung Plan/Do/Check/Act in Handbuch 2.2 ist gegen die Grafik zu prüfen.
2. Ob der Katalog an UMS.1.1, STM.2.1.5 und UMS.1.2 nachgezogen wird oder der Standard, entscheidet das BSI; bis dahin gilt im Projekt: Standard und Katalog beide zitieren, Widerspruch kennzeichnen.
3. Die Werkzeuge (SSP-Generator, POAM-Generator) müssen den Statuswert „not-applicable" mit Begründungsfeld als Regelweg anbieten; das ist Werkzeugarbeit, kein Handbuchpunkt.
