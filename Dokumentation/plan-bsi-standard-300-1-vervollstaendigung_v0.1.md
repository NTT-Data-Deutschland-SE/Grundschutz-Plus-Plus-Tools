# Plan zur Vervollständigung des BSI-Standards 300-1 „Methodik Grundschutz++“

**Version 0.1 (Entwurf)** · Stand: 2026-10-28 · Zweck: Was dem Standard 300-1 (Version 1.0 vom 20.10.2026) fehlt, damit er die Methodik vollständig beschreibt, und in welcher Reihenfolge das BSI die Lücken schließen könnte. Grundlage sind der Standard selbst, der Anwenderkatalog im Build 2026-10-22, das Handbuch zur Grundschutz++-Methodik und alle 81 Issues des Repositories BSI-Bund/Stand-der-Technik-Bibliothek.

Geprüfte Quellen:

| Quelle | Stand | Rolle |
|---|---|---|
| BSI-Standard 300-1, Version 1.0 vom 20.10.2026, 42 Seiten, Referat S 13 | PDF (`standard_300-1.pdf`), Text mit pypdf extrahiert; die Abbildungen 1 bis 6 liefert die Extraktion nicht | Prüfobjekt |
| Anwenderkatalog Grundschutz++, Methodik-Katalog, Risikomanagement-Katalog | Build 2026-10-22, Commit 160c177 vom 23.10.2026; am 28.10.2026 weiterhin der jüngste Commit auf `main` | Ground Truth für Zahlen und Control-IDs |
| Issues BSI-Bund/Stand-der-Technik-Bibliothek | 81 Issues (48 offen, 33 geschlossen), vollständig gelesen am 28.10.2026 | Fragen der Anwender, die der Standard beantworten müsste |
| Handbuch zur Grundschutz++-Methodik, Kapitel 1 bis 10, Anhänge A bis D | Version 0.2 vom 26.10.2026, Anhang D Version 0.13 (D1 bis D52) | Vergleichsbasis Fachtext und offene Fragen |
| Abgleich `abgleich-bsi-standard-300-1_v0.2.md` und Issue #116 | 26.10.2026 | die sieben Widersprüche zwischen Standard und Katalog, die hier nicht wiederholt werden |
| BSI-Standard 200-2, Auditierungsschema 2.5, Zertifizierungsschema | historischer Vergleich, Prüf- und Zertifizierungsfolgen | Was es vor Grundschutz++ gab und was die Prüfwelt verlangt |

Alle Katalogzahlen sind skriptgestützt aus dem JSON des Builds 2026-10-22 erhoben; Zitate aus dem Standard sind wörtlich, Seitenangaben beziehen sich auf die PDF-Seiten. Die Zählungen von Wörtern im Standard laufen über den extrahierten Text mit bereinigter Silbentrennung.

## 0. Ergebnis

Der Standard 300-1 beschreibt den Vollausbau eines Grundschutz++-ISMS in fünf Prozessschritten, und er tut das an mehreren Stellen präziser als der Katalog: drei Statuswerte statt zwei, Folgen der Nichterfüllung nach Modalverb, 35 Mindestkriterien für jede Risikomethode, Mindestfelder für Geschäftsprozesse und Umsetzungsplan. Was er nicht beschreibt, ist alles, was zwischen zwei Durchläufen passiert, und alles, was eine zweite Partei prüfen können muss. Welcher Katalogstand gilt. Wie ein Umsetzungsstatus je Asset gezählt wird. Wann eine Nichterfüllung dauerhaft ist und was eine Ausnahme ist. Welche Prozesse ein Informationsverbund hat. Wie ein Asset seinen Schutzbedarf erbt. Was zertifizierbar ist. Wie ein bestehendes ISMS nach 200-2 herüberkommt. Womit eine kleine Institution anfängt.

Die Zählung dieses Plans: 29 Lücken, davon neun mit Rang 1 (L1 bis L9), ohne deren Schließung die Methodik nicht eindeutig anwendbar oder prüfbar ist, vierzehn mit Rang 2 (L10 bis L23), die die Prozessschritte vervollständigen, und sechs mit Rang 3 (L24 bis L29), die Lesbarkeit und Redaktion betreffen. Dazu kommen die sieben Widersprüche zwischen Standard und Katalog aus Issue #116, die hier vorausgesetzt werden. Von den 105 Controls der Methodik und des Risikomanagement-Katalogs haben elf keinen Abschnitt im Standard und sieben nur einen Nebensatz (Anhang A). Von den 81 Issues des Repositories betreffen zehn den Standard, 37 die Bibliothek, 25 sind erledigt und neun geschlossen, fünf davon, weil der Standard die Frage entschieden hat (Anhang B).

Mein Urteil: Die Version 1.0 ist als Verfahrensbeschreibung für Early Adopters brauchbar. Als Prüfgrundlage fehlen ihr die Definitionen, als Einstiegshilfe fehlt ihr der Einstieg, und als Nachfolger des 200-2 fehlt ihr der Übergang. Keine dieser Lücken braucht eine neue Idee; die meisten brauchen einen Absatz, der eine Entscheidung festhält, die im Katalog, in der Guidance oder in den Issues längst diskutiert ist. Die Reihenfolge in Abschnitt 6 beginnt deshalb mit dem, was ohne Katalogänderung geht.

## 1. Vorgehen

Vier Wege führen zu den Lücken, und jede Lücke trägt ihren Beleg.

Erstens die Controls: Jedes der 95 Methodik-Controls und der zehn RISK-Controls wurde dem Abschnitt des Standards zugeordnet, der seinen Gegenstand behandelt (Anhang A). Ein Control ohne Abschnitt ist ein Teil der Methodik, den der Standard nicht beschreibt. Umgekehrt stehen die Pflichten des Standards ohne Control schon in Anhang D47 des Handbuchs und in Issue #116.

Zweitens die Issues: Alle 81 Issues des Repositories wurden gelesen und eingeordnet (Anhang B). Die Fragen, die nur ein Standard beantworten kann, sind hier Lücken; die Fragen an Datenformat, Pipeline und Namespaces gehören in die Bibliothek und stehen in Abschnitt 7. Die 20 offenen Issues des AG-1-Forks wurden am 26.10.2026 gesichtet und hier nicht erneut gelesen; ihre Befunde zu Begriffen und Rollen sind über das Handbuch eingeflossen.

Drittens der 200-2: Was der alte Standard regelte und der neue weglässt, ist entweder eine bewusste Entscheidung oder eine Lücke. Der Standard 300-1 nennt den 200-2 nicht, den 200-3 nicht und die Basis-Absicherung nicht (je null Treffer im Text); er trifft also auch keine Entscheidung darüber.

Viertens der Standard selbst: Begriffe ohne Definition, Verweise ohne Ziel, Pflichten ohne Zuständigkeit, Abbildungen ohne Text.

Was nicht bewertet wurde: die sechs Abbildungen, weil der Text sie nicht hergibt; die Frage, ob das BSI ein Prüfschema oder einen Standard 300-2 plant, weil dazu nichts veröffentlicht ist.

Jede Lücke hat dieselbe Form: Was fehlt. Beleg. Vorschlag. Priorität und Aufwand. Die Vorschläge sind Formulierungsvorschläge eines Anwenders und keine Texte des BSI; wo sie eine Entscheidung vorwegnehmen, steht es dabei.

## 2. Lücken mit Rang 1: Anwendbarkeit und Prüfbarkeit

### L1 Verbindlichkeit des Standards und Verhältnis zum Anwenderkatalog

**Was fehlt.** Der Standard sagt in 3.4.1 (S. 15), die normativen Inhalte der Methodik seien „in Anforderungen überführt und in Methodik Praktiken strukturiert“ worden; damit wäre der Anwenderkatalog die verbindliche Form. Zugleich trägt der Standard Pflichten, die im Katalog kein Control haben: die Asset-Abhängigkeiten nach Schutzbedarf (3.2, S. 14), die Mindestfelder je Maßnahme und die Nachweisregeln (4.3, S. 20), die jährliche Überprüfung der Risikobetrachtung (4.2.3, S. 19, Kriterium 35), die drei Monitoring-Verfahren (5.4, S. 24 f.) und 24 der 35 Mindestkriterien (Anhang D42 und D47 des Handbuchs). An sieben Stellen widerspricht er dem Build 2026-10-22 (Issue #116, Teil A). Eine Regel, welche Quelle bei Widerspruch gilt und ob ein „muss“ des Standards ohne Control im Audit prüfbar ist, fehlt. Der Standard verwendet 13-mal „muss“, 11-mal „müssen“, 44-mal „sollte“ oder „sollten“, 8-mal „ist zu“ oder „sind zu“ und 69-mal „kann“ oder „können“, ohne zu sagen, ob diese Wörter die Verbindlichkeit der Katalog-Modalverben MUSS, SOLLTE und KANN tragen.

**Beleg.** Standard 3.4.1 (S. 15); Abgleich v0.2, Abschnitte 3.1 und 3.2; Anhang D47; Issue #116.

**Vorschlag.** Neuer Abschnitt 1.1 „Verbindlichkeit“ mit vier Sätzen. Der Anwenderkatalog ist die normative Form der Methodik-Anforderungen, der Standard beschreibt das Verfahren. Jede Pflicht des Standards hat ein Control im Anwenderkatalog oder ist als Empfehlung gekennzeichnet; die Pflichten aus Anhang D47 bekommen Controls oder werden zu Empfehlungen. Bei Widerspruch zwischen Standard und Katalog gilt bis zur Angleichung der Katalog, und der Standard nennt den Katalogstand, ab dem er gilt. Schreibkonvention: „muss“ und „ist zu“ entsprechen MUSS, „sollte“ entspricht SOLLTE, „kann“ entspricht KANN, alles andere ist Erläuterung. Dazu ein Anhang, der die Abschnitte des Standards den Controls zuordnet; Anhang A dieses Plans ist die Vorlage.

**Priorität** hoch. Aufwand: ein Abschnitt und ein Anhang. Abhängigkeit: der an den Standard angepasste Katalog-Build.

### L2 Granularität und maschinenlesbare Abbildung des Umsetzungsstatus

**Was fehlt.** 4.1.1 (S. 18) nennt drei Werte, 4.1.2 (S. 18 f.) zwei Zustände der Nichterfüllung, zusammen vier Zustände je Anforderung: erfüllt, temporär nicht erfüllt, dauerhaft nicht erfüllt, nicht anwendbar. Nicht geregelt ist erstens, ob der Status je Anforderung oder je Anforderung und Asset geführt wird. 3.4 (S. 15) verlangt: „Anforderungen, die mehreren Assets und denselben Zielobjektkategorien zugeordnet werden, sind nur einmalig im Anforderungspaket zu berücksichtigen.“ Wörtlich genommen gibt es dann einen Status für alle Server, auch wenn einer gehärtet ist und drei nicht; der IT-Grundschutz-Check des 200-2 lief je Zielobjekt. Zweitens fehlt die Abbildung der vier Zustände auf das Datenmodell. OSCAL kennt `implemented`, `planned`, `not-applicable`; „dauerhaft nicht erfüllt“ hat keinen Standardwert, der Upstream-Vorschlag `not-implemented` (usnistgov/OSCAL#2273) ist in `develop` gemerged und in keinem Release. Drittens verlangt die Guidance zu UMS.1.1 die Erfüllung „aller in Abhängigkeit stehenden Anforderungen“, ohne dass Standard oder Katalog sagen, woher Abhängigkeiten zwischen Anforderungen kommen; 4.3 (S. 20) kennt nur Abhängigkeiten zwischen Anforderungen und Maßnahmen. Viertens fehlt der ausdrückliche Satz, dass eine teilweise umgesetzte Anforderung „nicht erfüllt“ ist; das steht bisher nur in unserer Auslegung.

**Beleg.** Standard 3.4 (S. 15), 4.1.1 (S. 18), 4.1.2 (S. 18 f.), 4.3 (S. 20); Guidance UMS.1.1; Issues #95, #96, #103 (Punktbasis), AG-1 #64; Anhang D3, D32, D38.

**Vorschlag.** 4.1.1 ergänzen: Der Status wird je Anforderung und Asset oder Gruppe (L10) geführt; der Satz zur einmaligen Berücksichtigung in 3.4 bezieht sich auf das Paket und wird so umformuliert; teilweise umgesetzt ist nicht erfüllt. Neuer Anhang „Maschinenlesbare Abbildung“: die vier Zustände mit ihren OSCAL-Werten (erfüllt = `implemented`; temporär nicht erfüllt = `planned` mit Zieldatum; dauerhaft nicht erfüllt = `not-implemented` als Interimswert bis zum OSCAL-Release; nicht anwendbar = `not-applicable` mit Begründung), die Pflichtfelder Begründung, Zieldatum und Zuständigkeit. Abhängigkeiten zwischen Anforderungen entweder mit Quelle und Semantik definieren oder den Satz in der Guidance zu UMS.1.1 streichen.

**Priorität** hoch. Aufwand: zwei Absätze und ein Anhang. Abhängigkeit: Katalog (UMS.1.1), OSCAL-Release.

### L3 Temporäre und dauerhafte Nichterfüllung, Restrisiko und Ausnahmen

**Was fehlt.** „Temporär“ und „dauerhaft“ sind nur über Beispielsätze definiert (4.1.2, S. 19). „Restrisikobetrachtung“ (2.11, S. 11) ist nicht definiert und kollidiert mit 4.1.2: „Eine temporäre Nichterfüllung löst keine Risikobetrachtung aus.“ Nicht geregelt: wann aus temporär dauerhaft wird (nach Fristablauf, nach einer Höchstdauer, nach einer Zahl von Verlängerungen), wer die Einordnung trifft und wie sie dokumentiert wird. Der Katalog führt das Ausnahmemanagement als MUSS (UMS.5.1 Autorisierung, UMS.5.2 Dokumentation); der Standard hat dafür keinen Abschnitt, nur den Ausschluss für MUSS-Anforderungen (4.1.2) und das Wort „Ausnahmegenehmigung“ in Kriterium 27 (S. 38) für ein Risiko außerhalb der Akzeptanzkriterien, das die Leitung trotzdem nicht weiter behandeln lässt. Was eine Ausnahme im Grundschutz++ ist (dauerhafte SOLLTE-Nichterfüllung mit akzeptiertem Risiko, Abweichung von einer Compliance-Verpflichtung, beides), wer sie autorisiert (Kriterium 27: Institutionsleitung; UMS.5.1: `{{eine zuständige Person oder Rolle}}`), wie sie befristet (Kriterium 28) und dokumentiert wird (UMS.5.2, Kriterium 29), steht nirgends zusammen.

**Beleg.** Standard 2.11 (S. 11), 4.1.1 (S. 18), 4.1.2 (S. 18 f.), Anhang 3 Kriterien 27 bis 30 (S. 38); UMS.1.2, UMS.5.1, UMS.5.2, RISK.1.9; Issues #78, #116 A.3 und A.4; Anhang D9, D40, D41, D46.

**Vorschlag.** 4.1.2 mit Definitionen: temporär heißt im Umsetzungsplan mit Zieldatum und Zuständigkeit; dauerhaft heißt ohne Zieldatum oder nach Ablauf des Zieldatums ohne Verlängerungsentscheidung der Leitung; Restrisikobetrachtung heißt Risikoidentifikation mit Mitteilung an die Leitung ohne vollständige Betrachtung nach Anhang 3 (so die vermutete Absicht von 4.1.1). Neuer Abschnitt 4.1.3 „Ausnahmen“: Definition, zulässige Gegenstände (SOLLTE-Anforderungen, Compliance-Verpflichtungen), Ausschluss der MUSS-Anforderungen, autorisierende Rolle, Befristung, Dokumentation, Überprüfung in jedem Zyklus. Im Katalog UMS.1.2 auf MUSS und die Guidance zu UMS.5.1 mit Modalverb-Bezug, wie in #116 vorgeschlagen.

**Priorität** hoch. Aufwand: drei Definitionen und ein Abschnitt. Abhängigkeit: Katalog.

### L4 Prozessbezogene Anforderungen: welche Prozesse hat ein Informationsverbund?

**Was fehlt.** 265 der 901 Kernel-Controls tragen keine Zielobjektkategorie. Sie bilden die Verfahrens-, Zuständigkeits- und Bekanntgabe-Anforderungen der prozessförmigen Praktiken: REA 23 von 23, TEST 35 von 36, BER 68 von 92, DET 43 von 82, NOT 25 von 37, PERS 20 von 30. 3.4.1 (S. 16) nimmt sie verpflichtend ins Anforderungspaket, 4.1.1 (S. 18) lässt sie einzeln mit Begründung als „nicht anwendbar“ führen. Eine Regel, mit der ein Verbund einen Prozess als nicht vorhanden erklärt, bevor dessen Anforderungen ins Paket fallen, gibt es nicht. Am Beispiel Softwareentwicklung: 34 DEV-Controls, 25 davon über die Kategorie „Anwendungen“, die jeder Verbund hat, neun kategorielos. Ein Verbund ohne eigene Entwicklung begründet 34 Einzelentscheidungen. Das Wort „Prozess-Owner“ kommt im Standard nicht vor, im Katalog nur in der Guidance zu STM.2.1.5; Anhang 1 kennt sieben Wurzeln und keine für Prozesse.

**Beleg.** Standard 3.4 und 3.4.1 (S. 15 f.), 4.1.1 (S. 18), Anhang 1 (S. 28 bis 33); Guidance STM.2.1.1 und STM.2.1.5; Issues #81 (am 26.10. wieder geöffnet), #32, #116 A.2; Anhang D29.

**Vorschlag.** Neuer Abschnitt 3.4.4 „Prozessbezogene Anforderungen“: Die Institution legt die im Informationsverbund vorhandenen Prozesse fest, mit einer Kandidatenliste je Kernel-Praktik (Entwicklung, Notfallplanung, Vorfallsbehandlung, Änderungen und Tests, Beschaffung, Personal, Dienstleistersteuerung, Detektion); je Prozess ein Prozess-Owner; prozessbezogene Anforderungen werden dem Prozess zugeordnet; ein nicht vorhandener Prozess wird einmal begründet erklärt, seine Anforderungen gelten als nicht anwendbar. Technisch eine Wurzel „Geschäftsprozesse“ in Anhang 1 mit Unterkategorien je Praktik, oder eine Zuordnungstabelle Praktik zu Prozess. Die Begründungspflicht bleibt; sie wandert von 34 Stellen an eine.

**Priorität** hoch. Aufwand: ein Abschnitt und eine Erweiterung von Anhang 1. Abhängigkeit: Namespace und Katalog-Props.

### L5 Schutzbedarf der Assets, Vererbung und die Rolle von „erhöht“

**Was fehlt.** 2.6 (S. 8 f.) stellt den Schutzbedarf je Geschäftsprozess fest. 3.4.2 (S. 17) wählt die Anforderungen nach dem „Schutzbedarf des betrachteten Geschäftsprozess“ für das Sicherheitsniveau „normal-SdT“ oder „erhöht“ aus und erklärt im nächsten Satz: „Anforderungen mit dem Sicherheitsniveau ‚erhöht‘ beinhalten das Modalverb ‚KANN‘ und sind optional zu erfüllen.“ Offen bleibt erstens, wie ein Asset, das mehreren Prozessen dient, seinen Schutzbedarf bekommt; der 200-2 regelte das in Kapitel 8.2 mit Maximumprinzip, Kumulations- und Verteilungseffekt, der Standard 300-1 kennt keines der drei Wörter. Zweitens, ob hoher Schutzbedarf die Aufnahme der „erhöht“-Anforderungen verlangt oder nur ihre Heranziehung in der Risikobetrachtung; der erste Satz legt die Aufnahme nahe, der zweite die Option. Drittens hat die Überprüfung des gesetzten Niveaus (STM.3.1, SOLLTE) im Standard keinen Platz. Viertens sagt der Standard nicht, was aus der Kategorie „sehr hoch“ bestehender Konzepte wird, außer dass eigene Kategorien auf die zwei Stufen abzubilden sind.

**Beleg.** Standard 2.6 (S. 8 f.), 3.2 (S. 14), 3.4.2 (S. 17); GC.7.1.2, STM.3.1; BES.1.4, DET.4.12.1, REA.2.5 (die drei „erhöht“-Controls mit SOLLTE); Issues #47, #116 A.7; Handbuch 4.7 und 5.3; Anhang D44.

**Vorschlag.** 2.6 ergänzen um einen Absatz „Vererbung auf Assets“: Ein Asset erbt den höchsten Schutzbedarf der Geschäftsprozesse, die es nutzen; Abweichungen nach unten (Verteilung) oder oben (Kumulation) sind möglich und zu begründen. 3.4.2 klarstellen: Bei hohem Schutzbedarf bilden die „erhöht“-Anforderungen des betroffenen Kategorienstrangs den Vorrat der Risikobehandlung; die Risikobetrachtung entscheidet, welche davon ins Paket kommen, und mit welcher Verbindlichkeit; ohne Risikobetrachtung bleiben sie KANN. Im Katalog die drei SOLLTE-Controls auf „erhöht“ angleichen.

**Priorität** hoch. Aufwand: zwei Absätze. Abhängigkeit: keine.

### L6 Verbindliche Katalogstände, Kennungen und Übergangsfristen

**Was fehlt.** Der Standard setzt versionierte Artefakte voraus: Die Auswahl der Blaupausen ist „inkl. Version“ zu dokumentieren (3.3, S. 14), die Validierung berücksichtigt „Anpassungen an den Anforderungen in der Stand der Technik Bibliothek“ und „Änderungen in der Methodik GS++“ (5.5, S. 25). Er sagt nicht, was ein Stand des Anwenderkatalogs ist, wo er veröffentlicht wird, wie eine Institution ihn im Anforderungspaket festhält, wie lange ein älterer Stand Prüfgrundlage bleibt und welche Frist nach einem neuen Stand läuft. Die Bibliothek hat weder Tag noch Release (Issues #53, #99), nur rollierende Builds auf `main`; im Sommer 2026 wurden Control-IDs zweimal gegenläufig umnummeriert (Issue #73), im Februar änderten sich UUIDs (#38), Entwürfe liegen neben Freigegebenem (#99). „Release“ kommt im Standard nicht vor.

**Beleg.** Standard 3.3 (S. 14), 5.5 (S. 25); Issues #20, #38, #39, #53, #59, #66, #73, #99; Skill-Regel 8 (Importe auf Commit und Hash pinnen).

**Vorschlag.** Neuer Abschnitt 1.2 „Katalogstände“: Das BSI veröffentlicht den Anwenderkatalog in benannten, unveränderlichen Ständen (Release mit Datum, Commit und Hash); das Anforderungspaket nennt den Stand; ein neuer Stand löst die Validierung nach 5.5 binnen einer Frist aus (Vorschlag: zwölf Monate); Audits akzeptieren den Vorgängerstand während der Frist; Control-IDs bleiben innerhalb eines Hauptstands stabil, Änderungen tragen ein Änderungsprotokoll; die `alt-identifier`-UUID ist die versionsfeste Referenz. Die Bibliothek liefert dazu Tags, Releases, ein Changelog und einen Freigabestatus je Artefakt.

**Priorität** hoch. Aufwand: ein Abschnitt. Abhängigkeit: Release-Prozess der Bibliothek.

### L7 Zertifizierung und Prüfschema

**Was fehlt.** Der Standard berührt die Zertifizierung an drei Stellen: „für ein zertifizierbares ISMS“ gilt in der niedrigsten Kategorie der Stand der Technik (2.6, S. 9); die Mindestkriterien machen die Risikomethode „im Rahmen einer Zertifizierung vergleichbar und überprüfbar“ (2.11, S. 11); bei gehäufter dauerhafter Nichterfüllung „könnte eine erhebliche Abweichung festgestellt werden“ (4.1.2, S. 19). Keiner der drei Sätze hat ein Verfahren hinter sich. Auditierungs- und Zertifizierungsschema prüfen gegen 200-2, Kompendium und die Referenzdokumente A.0 bis A.6; AudS 6 verlangt für Überwachungsaudits die Standard- oder Kern-Absicherung nach 200-2; die Abweichungsklassen heißen dort geringfügig und schwerwiegend, nicht erheblich. „Prüfschema“ und „Auditierungsschema“ kommen im Standard nicht vor. Issue #41 fragt nach Prüfzielen und Prüfverfahren im Katalog; der Assessment Layer der Bibliothek ist leer.

**Beleg.** Standard 2.6 (S. 9), 2.11 (S. 11), 4.1.2 (S. 19); Handbuch 9.0 bis 9.4 (zehn Übertragungslücken); Anhang D2, D13, D45; Issue #41; AudS 2, 4.3, 4.5, 4.6 und 6.

**Vorschlag.** Neues Kapitel 7 „Audit und Zertifizierung nach Grundschutz++“ oder ein eigener Standard 300-2 mit: Prüfgrundlage (Katalogstand plus Standard, L6); zertifizierbare Konstellation (Mindestabdeckung des Anwendungsbereichs, L14); Referenzdokumente nach dem Dokumentenmodell (L19); Abweichungsklassen nach Modalverb (MUSS nicht erfüllt ohne Maßnahme ist schwerwiegend; dauerhafte SOLLTE-Nichterfüllung ohne Risikobetrachtung ist geringfügig, gehäuft schwerwiegend; „erheblich“ entfällt); Stichprobe über Praktiken und Zielobjektkategorien statt über Bausteine; Prüfung der Begründungen für „nicht anwendbar“; Übergang bestehender Zertifikate (L9). Bis dahin ein Satz im Standard, dass die Zertifizierung weiter nach den Schemata zur ISO 27001 auf der Basis von IT-Grundschutz läuft und Grundschutz++ dort noch nicht anerkannt ist.

**Priorität** hoch. Aufwand: ein eigenes Dokument. Abhängigkeit: Zertifizierungsstelle des BSI.

### L8 Der Einstieg: Basis-Absicherung als Blaupause

**Was fehlt.** Die Basis-Absicherung des 200-2 (dort Kapitel 6) ist ersatzlos entfallen; der Standard erwähnt sie nicht. Der Einstieg besteht aus „wichtigster Geschäftsprozess zuerst“ (2.6, S. 9) und der Iteration. Die Edition 2023 hatte 563 Basis-Anforderungen in 108 Bausteinen; der Kernel hat 69 MUSS-Anforderungen unter 901, je fünf pro Praktik nach derselben Schablone (Verfahren verankern, Dokumentation, Zuweisung, Bekanntgabe, Überprüfung; SENS mit vier), und keine einzige technische Anforderung mit MUSS (Issue #104). Wer die 69 als Einstieg nimmt, hat eine Pflichtliste ohne Sicherheitsniveau. Das Basis-Phasenmodell der Community (Issue #27) sucht genau diesen Platz und findet im Standard keinen Mechanismus für vorbereitende Aufgaben.

**Beleg.** Standard 2.6 (S. 9), 3.3 (S. 14 f.); Issues #27, #37, #104; Handbuch 10.1; LinkedIn-Entwurf vom 26.10.2026 mit Belegstellen der Zahlen.

**Vorschlag.** 3.3 ergänzen um das Einstiegsprofil: Das BSI veröffentlicht eine Blaupause „Einstieg“ als Profil über den Anwenderkatalog, einige hundert IDs, zusammengesetzt aus den 69 MUSS-Anforderungen des Kernels, den SOLLTE-Anforderungen mit `effort_level` 1 bis 2 und hoher Schutzzielwirkung sowie den Grundlagen-Controls jeder Praktik. Der erste Zyklus darf mit dem Einstiegsprofil laufen; die Zertifizierung verlangt das volle Niveau normal-SdT. Die Guidance zu GC.1.1 (erster vollständiger Durchlauf) wird entsprechend gestuft. Die Zusammensetzung ist ein Vorschlag; ob das Einstiegsprofil ein eigenes Sicherheitsniveau trägt, muss das BSI entscheiden.

**Priorität** hoch. Aufwand: ein Absatz und eine Blaupause. Abhängigkeit: Blaupausen-Mechanik (L15).

### L9 Übergang aus 200-2 und Edition 2023

**Was fehlt.** Zielgruppe der Version 1.0 sind „Early Adopters“, also Institutionen mit bestehendem ISMS (Kap. 1, S. 5). Der Standard sagt nichts darüber, wie ein ISMS nach 200-2 mit Strukturanalyse, dreistufigem Schutzbedarf, Grundschutz-Check mit vier Statuswerten, Realisierungsplan und Zertifikat nach Grundschutz++ überführt wird, ob beide Methodiken parallel gelten, ob ein 200-2-Zertifikat bei Umstellung weiterläuft und welche Nachweise übernommen werden können. „Migration“ und „Übergang“ kommen nicht vor, 200-2 und 200-3 werden nicht genannt. Die Mapping-Sammlung ITGS→GS++ der Bibliothek deckt 510 von 1.834 aktiven Anforderungen der Edition 2023 ab (27,8 Prozent) und zielt auf einen Build vom April 2026 (Issues #98, #61).

**Beleg.** Standard Kap. 1 (S. 5); Handbuch 10.3 (Migrationspfad als Auslegung); Issues #98, #61; AudS 6.

**Vorschlag.** Neuer Anhang „Übergang von IT-Grundschutz nach Grundschutz++“: Übersetzung der Artefakte (A.0 bis A.6 zu den Dokumenten des Grundschutz++), Regeln für den Schutzbedarf (sehr hoch wird hoch plus Risikobetrachtung), für die Statuswerte (teilweise wird nicht erfüllt plus Maßnahme; entbehrlich wird nicht anwendbar mit Begründung), für den Realisierungsplan (wird Umsetzungsplan) und für die Risikoanalyse nach 200-3 (Prüfung gegen Anhang 3); Stellung der Mapping-Sammlung als Hilfsmittel mit Angabe ihrer Abdeckung; Übergang der Zertifikate.

**Priorität** hoch für Bestandsanwender. Aufwand: ein Anhang. Abhängigkeit: Prüfschema (L7), Pflege der Mapping-Sammlung.

## 3. Lücken mit Rang 2: die Prozessschritte vervollständigen

### L10 Gruppenbildung von Assets

**Was fehlt.** 3.2 (S. 13) erlaubt die Gruppierung in einem Satz: „Ähneln sich die Eigenschaften und der Einsatzzweck von Assets, ist eine Gruppierung möglich.“ Der 200-2 hatte in Kapitel 8.1.1 fünf Kriterien (gleicher Typ, gleiche oder nahezu gleiche Konfiguration, gleiche Netzeinbindung, gleiche administrative und infrastrukturelle Rahmenbedingungen, gleiche Anwendungen). Offen sind die Kriterien, ob die Gruppe ein Anforderungspaket und einen Status trägt (L2), wie abweichende Mitglieder behandelt werden, wie die Gruppenbildung dokumentiert und im Audit geprüft wird. „Gruppierung“ kommt in keinem Methodik-Statement vor.

**Beleg.** Standard 3.2 (S. 13); STM.2.1.2 bis STM.2.1.4.2; Issue #106; 200-2 Kapitel 8.1.1.

**Vorschlag.** 3.2 um einen Absatz: Kriterien (gleiche Zielobjektkategorien, gleiche Konfiguration und gleicher Betrieb, gleiches Sicherheitsniveau, gleiche Netzeinbindung, gleiche Zuständigkeit), ein Paket und ein Status je Gruppe, Herauslösen abweichender Assets, Dokumentation der Gruppenkriterien. Im Katalog ein KANN-Control unter STM.2.1.2, wie in #106 vorgeschlagen.

**Priorität** mittel bis hoch. Aufwand: ein Absatz.

### L11 Bezugsart-Kategorien: IT-Produkte, Dienstleistungen, Outsourcing

**Was fehlt.** Die Beschaffungsanforderungen des Kernels sind an die Kategorie „IT-Produkte“ gebunden (etwa BES.2.1.1), die Dienstleister-Anforderungen an „Dienstleistungen“, „Outsourcing“ und „Cloud-Dienste“. 3.4.2 (S. 16 f.) regelt die Zuordnung der Elternknoten, aber nicht, dass ein gekaufter Server neben „Hostsysteme“ auch „IT-Produkte“ bekommt und ein gemieteter Dienst „Outsourcing“ oder „Cloud-Dienste“. Anhang 1 definiert die Kategorien ohne Zuweisungsregel; „IT-Produkte“ fehlt in allen 95 Methodik-Controls. Ohne die Regel fehlen Beschaffungs- und Dienstleisteranforderungen im Paket, und kein Prüfschritt bemerkt es.

**Beleg.** Standard 3.4.2 (S. 16 f.), Anhang 1 (S. 30 f.); STM.2.1.3; Issue #82; Anhang D31.

**Vorschlag.** 3.4.2 ergänzen: Assets erhalten neben der funktionalen Kategorie die Kategorie ihrer Bezugsart, also „IT-Produkte“ bei Kauf oder Miete von Komponenten, „Dienstleistungen“ bei Leistungsbezug, „Outsourcing“ und „Cloud-Dienste“ bei ausgelagertem Betrieb; dazu eine Beispielzeile in Anhang 1.

**Priorität** mittel bis hoch. Aufwand: zwei Sätze.

### L12 Mehrere Informationsverbünde je Anwendungsbereich

**Was fehlt.** 3.1 (S. 13) erlaubt es: „Der Anwendungsbereich kann einen oder mehrere Informationsverbünde enthalten.“ Offen ist, ob jeder Verbund ein eigenes Anforderungspaket, einen eigenen Umsetzungsplan und eine eigene Risikobetrachtung hat; ob die Methodik-Anforderungen, die nach 3.4 verbundweit gelten, je Verbund oder je Anwendungsbereich erfüllt werden; wie gemeinsam genutzte Assets und die Schnittstellen zwischen Verbünden behandelt werden, deren Dokumentation 3.1 verlangt; und ob ein Zertifikat den Anwendungsbereich oder einen Verbund umfasst.

**Beleg.** Standard 2.3 (S. 7), 3.1 (S. 13), 3.4 (S. 15); GC.6.1, STM.1.1; Handbuch 4.6.

**Vorschlag.** 3.1 ergänzen: Die Methodik-Anforderungen gelten je Anwendungsbereich einmal; Anforderungspaket, Status und Umsetzungsplan werden je Verbund geführt; gemeinsame Assets werden einem Verbund zugeordnet und von den anderen als externe Schnittstelle behandelt; Zertifizierungsgegenstand ist der Anwendungsbereich, ein einzelner Verbund nur mit ausdrücklicher Abgrenzung.

**Priorität** mittel. Aufwand: ein Absatz.

### L13 Wirksame Abgrenzung an der Grenze des Anwendungsbereichs

**Was fehlt.** 2.3 (S. 7) und 3.1 (S. 13) verlangen die Dokumentation der Abgrenzung und der Schnittstellen. Eine Anforderung, dass an der Grenze eine wirksame organisatorische oder technische Trennung besteht, wenn innerhalb und außerhalb unterschiedliche Sicherheitsanforderungen gelten, fehlt. Ein Verbund im selben VLAN und derselben Domäne wie der ausgeschlossene Rest der Institution ist nach dem Wortlaut sauber abgegrenzt.

**Beleg.** Standard 2.3 (S. 7), 3.1 (S. 13); GC.6.1, STM.1.2; Issue #77.

**Vorschlag.** 3.1 ergänzen: Ausschlüsse setzen eine dokumentierte, wirksame Trennung voraus; fehlt sie, gehört der Bereich zum Verbund oder die Schnittstelle wird als Risiko behandelt. Ist der Verzicht auf die Trennung gewollt, sagt der Standard das ausdrücklich.

**Priorität** mittel. Aufwand: zwei Sätze.

### L14 Zyklus, Erstzyklus und Mindestabdeckung

**Was fehlt.** Kapitel 1 (S. 5) macht die Iteration zur Voraussetzung, 2.6 (S. 9) beginnt beim wichtigsten Geschäftsprozess und verlangt, „sukzessive“ alle zu untersuchen. Nicht definiert: was ein Zyklus ist (je Prozess, je Verbund, je Jahr), wann der erste Zyklus abgeschlossen ist (die Guidance zu GC.1.1 verlangt einen vollständigen Durchlauf), welche Abdeckung des Anwendungsbereichs für eine Zertifizierung mindestens erreicht sein muss und wie lange ein teilweise bearbeiteter Anwendungsbereich zulässig ist.

**Beleg.** Standard Kap. 1 (S. 5), 2.6 (S. 9); Guidance GC.1.1 und STM.2.1.2; Handbuch 2.2 und 2.6.

**Vorschlag.** Neuer Abschnitt 3.6 „Zyklus und Abdeckung“: Definition des Zyklus als Durchlauf der Prozessschritte 1 bis 5 für den bearbeiteten Teil des Anwendungsbereichs; Erstzyklus mit dem wichtigsten Prozess; Zielabdeckung aller Geschäftsprozesse binnen einer Frist (Vorschlag: drei Jahre, analog zur Zertifikatslaufzeit); Zertifizierung bei vollständiger Abdeckung oder mit dokumentiertem Ausschluss.

**Priorität** mittel. Aufwand: ein Abschnitt.

### L15 Blaupausen: Herausgeber, Form, Verbindlichkeit, Konflikte

**Was fehlt.** 3.3 (S. 14 f.) definiert die Blaupause als vorgefertigten Katalog mit Parametern und sagt: „Es kann für bestimmte Institutionen verpflichtende Blaupausen geben.“ Offen: wer Blaupausen herausgibt und freigibt, ihre technische Form (in der Bibliothek ein OSCAL-Profil über den Anwenderkatalog), welche Institutionen wodurch verpflichtet werden, wie Konflikte zwischen Blaupausen und mit eigenen Parametern aufgelöst werden, ob Blaupausen Aufgaben außerhalb von Anforderungen tragen dürfen (Issue #27) und wie sie versioniert werden (L6). Issue #55 zeigt, was ohne Kompositionsregel passiert: zwei Kataloge mit denselben Control-IDs lassen sich nicht gemeinsam auflösen.

**Beleg.** Standard 3.3 (S. 14 f.), 5.5 (S. 25); Issues #27, #53, #55; Handbuch 3.8.

**Vorschlag.** 3.3 erweitern: Definition als Profil über den Anwenderkatalog mit Auswahl, Parametern und optionalen Ergänzungen in einem eigenen Katalog; Herausgeber und Freigabe; Register der Blaupausen beim BSI; Verbindlichkeit nur durch Rechtsgrundlage oder Vertrag; Konfliktregel (der strengere Parameter gilt, eigene Werte nur strenger); Versionspflicht.

**Priorität** mittel. Aufwand: ein Abschnitt.

### L16 Parameter-Governance

**Was fehlt.** 3.5 (S. 17) beschreibt Parameter als „variabel gestaltbare Elemente innerhalb einer Anforderung“ und verlangt ihre Konkretisierung. Offen: wer Werte festlegt und freigibt (STM.5.1 sagt nur „setzen“), ob es Mindestwerte gibt (ist „regelmäßig“ gleich alle fünf Jahre zulässig?), ob das BSI Vorgabewerte veröffentlicht, wie Werte dokumentiert und geprüft werden, und was bei Abweichung zwischen dem Satz der Anforderung und ihrer Zerlegung gilt (Issue #113). Die Methodik hat 15 Parameter, neun davon Varianten von `{{regelmäßig}}`.

**Beleg.** Standard 3.5 (S. 17); STM.5.1; Issues #56, #113.

**Vorschlag.** 3.5 ergänzen: Parameterwerte werden begründet, dokumentiert und mit dem Anforderungspaket freigegeben; das BSI veröffentlicht Empfehlungs- und Mindestwerte je Parameter, als Blaupause oder als Namespace; der Satz der Anforderung ist maßgeblich.

**Priorität** mittel. Aufwand: ein Absatz.

### L17 Compliance über die Prozessschritte 3 bis 5

**Was fehlt.** Der Katalog führt die Compliance-Kette GC.3.1 (MUSS), UMS.7.1 (MUSS), PERF.2.1 (SOLLTE), VRB.7.1 (SOLLTE). Der Standard hat 2.2 (S. 7) für die Einbindung des Compliance-Managements in Schritt 1 und einen Aufzählungspunkt in Kapitel 6 (S. 26); Abschnitte für die Wahrung der Compliance in der Umsetzung, die Überprüfung der Einhaltung von Verpflichtungen und die Behandlung von Verstößen fehlen. Drei Controls haben damit keinen Abschnitt (Anhang A).

**Beleg.** Standard 2.2 (S. 7), Kap. 6 (S. 26); GC.3.1, UMS.7.1, PERF.2.1, VRB.7.1; Anhang D5.

**Vorschlag.** Drei kurze Abschnitte: 4.6 „Compliance in der Umsetzung“, 5.6 „Überprüfung der Einhaltung von Verpflichtungen“, 6.5 „Behandlung von Compliance-Verstößen“. Dazu die Verbindlichkeitsfrage: PERF.2.1 und VRB.7.1 sind SOLLTE, obwohl die Verpflichtungen selbst MUSS sind.

**Priorität** mittel. Aufwand: drei Absätze.

### L18 Rollenmodell und Entscheidungen

**Was fehlt.** 2.8 (S. 9 f.) nennt drei Aspekte und als Beispiele „ISB, IT-Betrieb“. Über den Standard verteilt: Institutionsleitung (Freigaben in 2.10, 4.4, 4.2.3 und den Kriterien 9, 27, 30), Risikoeigentümer (4.2.1, Kriterium 16), Geschäftsprozesseigentümer (4.2.1), Umsetzungszuständige und Fortschrittsverfolgung mit Interessenkonflikt (4.4, 4.5), Auditteamleiter (5.2.2). Keine Stelle fasst zusammen, welche Rollen mindestens besetzt sein müssen, welche Entscheidung bei wem liegt und welche Rollen unvereinbar sind. Der Katalog ist konkreter: GC.9 verlangt den ISB nach `{{einer unabhängigen Person}}`, Ressourcen, Vorspracherecht und Stellvertretung; drei dieser Controls haben im Standard keinen Abschnitt (Anhang A). Der 200-2 hatte das Rollenmodell in Kapitel 4. Die AG-1-Issues #60 und #73 fragen nach Verantwortlichkeiten und nach der Mehrdeutigkeit von „Autorisierung“.

**Beleg.** Standard 2.8 (S. 9 f.), 4.2.1 (S. 19), 4.4 und 4.5 (S. 21), 5.2.2 (S. 23), Anhang 3; GC.9.1.1.1 bis GC.9.1.1.4; Anhang A dieses Plans.

**Vorschlag.** Neuer Anhang „Rollen und Entscheidungen“: Tabelle Rolle gegen Entscheidung (Freigabe, Autorisierung, Kenntnisnahme, Durchführung) über die fünf Prozessschritte, Mindestrollen, Unvereinbarkeiten (ISB und IT-Leitung, Umsetzung und Fortschrittsverfolgung, Auditor und Geprüfter), Stellvertretung; die Begriffe „Freigabe“, „Autorisierung“ und „Genehmigung“ einheitlich verwenden.

**Priorität** mittel. Aufwand: ein Anhang.

### L19 Dokumentenmodell des ISMS

**Was fehlt.** 2.9 (S. 10) regelt die Dokumentenlenkung. Dokumente nennt der Standard beiläufig: Informationssicherheitsleitlinie, Anforderungspaket, Umsetzungsplan, Risikoregister, Auditbericht, Managementbericht, Korrektur- und Verbesserungsplan, Statusberichte (4.5, S. 21). Mindestinhalte definiert er nur für Geschäftsprozesse (Anhang 2), den Umsetzungsplan (4.3) und das Risikoregister (Kriterium 15). Der Katalog fordert über `documentation`-Props 20 Methodik-Dokumente an 59 Controls; 36 Controls haben keine Zuordnung (Issue #80), der Namespace hat Dubletten und Platzhalter (#44, #46), die Statusliste nach UMS.1.1 hat kein Dokument, obwohl sie das Gegenstück zum Referenzdokument A.4 ist. Betriebsartefakte wie Statusbericht, Änderungsmitteilung, Vorfallsbericht und Schwachstellenregister haben keine Struktur (Issue #110).

**Beleg.** Standard 2.9 (S. 10), 4.3 (S. 20), 4.5 (S. 21), Anhang 2 (S. 34 f.), Kriterium 15 (S. 37); Handbuch Anhang B (Dokumentenlandkarte); Issues #44, #46, #80, #110; Anhang D10.

**Vorschlag.** Neuer Anhang „Dokumente des ISMS“: je Dokument Zweck, Mindestinhalt, forderndes Control, Prozessschritt, Pflicht oder Empfehlung; darunter Anforderungspaket, Statusliste, Ausnahmen, Informationsverbund, Managementbericht, Statusbericht; Vokabular identisch mit `documentation_guidelines.csv`. Maschinenlesbare Formen (SSP, POA&M) als Empfehlung mit Verweis auf die Bibliothek.

**Priorität** mittel bis hoch. Aufwand: ein Anhang.

### L20 Leistungsbewertung: Mindestkennzahlen

**Was fehlt.** 5.1 (S. 22) sagt es selbst: „Da die Entwicklung einheitlicher Vorgaben zur Leistungsbewertung im GS++ noch aussteht, sind die Institutionen frei in der Ausgestaltung.“ PERF.1.1 verlangt als MUSS ein Verfahren. Ohne Mindestkennzahlen sind Managementberichte und Prüfergebnisse zwischen Institutionen nicht vergleichbar. Issue #103 schlägt Gewichte je Control und einen Score nach dem Vorbild der DoD-Assessment-Methodik zu NIST SP 800-171 vor; Issue #104 zeigt, dass `effort_level` 0 keine Aufwandsangabe ist und 148 MUSS-Controls ohne Aufwandswert dastehen.

**Beleg.** Standard 5.1 (S. 22), 5.3 (S. 24); PERF.1.1, PERF.4.2; Issues #103, #104.

**Vorschlag.** 5.1 ergänzen um einen Mindestsatz: Umsetzungsgrad je Modalverb, Anteil dauerhaft nicht erfüllter SOLLTE-Anforderungen, Zahl offener Ausnahmen, Fristtreue des Umsetzungsplans, Zahl und Behandlungsdauer von Sicherheitsvorfällen, Abdeckung des Anwendungsbereichs; je Kennzahl eine Berechnungsregel. Eine Gewichtung als Namespace bleibt optional.

**Priorität** mittel. Aufwand: ein Absatz, die Kennzahlen selbst sind Arbeitsgruppenarbeit.

### L21 Risikobetrachtung: Verhältnis zu 200-3, Kriterien ohne Control

**Was fehlt.** 2.11 (S. 11) nennt als Beispiele „ISO/IEC 27005, ISO 31000“, den BSI-Standard 200-3 nicht, obwohl die Guidance zu GC.7.2 ihn nennt und Bestandsanwender ihn nutzen. Ob eine Risikoanalyse nach 200-3 die 35 Kriterien erfüllt, sagt niemand. 21 der 35 Kriterien haben in keinem der beiden Kataloge ein Control (10 bis 29 und 35); drei weitere (6, 7, 8) und der Kriterienkatalog als Ganzes hängen an nicht importierten RISK-Controls (RISK.1.2, RISK.1.4, RISK.1.6, RISK.1.7, RISK.1.8), Kriterium 30 teilweise an RISK.1.9. Kriterium 17 (elementare Gefährdungen bei dauerhafter SOLLTE-Nichterfüllung) setzt die `threats`-Props des Katalogs voraus, die Anhang 4 (S. 41) als „G0-Kennung hinter einer Anforderung“ beschreibt, ohne den Prop zu nennen.

**Beleg.** Standard 2.11 (S. 11), 4.2 (S. 19 f.), Anhang 3 (S. 36 bis 39), Anhang 4 (S. 41); GC.12.1, RISK.1.2 bis RISK.1.9; Abgleich 3.1; Issue #116 A.5; AG-1 #71.

**Vorschlag.** 2.11 ergänzen um eine Konformitätsaussage zu 200-3 und zu ISO/IEC 27005 (Tabelle der Verfahrensschritte gegen die Kriterien); die Kriterien 10 bis 29 und 35 als Controls in den Anwenderkatalog, durch Import der RISK-Controls oder Ergänzung in GC.12; Kriterium 17 mit Verweis auf den Prop.

**Priorität** mittel; die Katalogarbeit dahinter hat Rang 1 (Issue #116 A.5). Aufwand: ein Absatz und eine Tabelle.

### L22 Monitoring und die Kernel-Praktiken

**Was fehlt.** 5.4 (S. 24 f.) verlangt mit „müssen“ drei Verfahren: Erkennung von Sicherheitsvorfällen, Umgang mit Schwachstellen, Erfassung neuer Bedrohungen. PERF.5.1 nennt nur „Methoden und Tools“; die Verfahren selbst stehen im Kernel bei Detektion (DET) und Sicherheitsvorfallsbehandlung (REA). Der Standard erklärt nicht, dass Prozessschritt 4 hier auf technische Praktiken zugreift, und nennt die Praktiken nicht. Die Begriffe „Überwachung“ für den Prozessschritt und „Monitoring“ für die Verfahren liegen eng beieinander (AG-1 #74).

**Beleg.** Standard 5.4 (S. 24 f.); PERF.5.1; DET.1.1 und REA.1.1 im Kernel; Abgleich 3.2.

**Vorschlag.** 5.4 ergänzen um den Verweis auf die Kernel-Praktiken Detektion und Sicherheitsvorfallsbehandlung und auf die Schnittstelle zur Risikobetrachtung (Kriterium 35, Einleitung zu Kapitel 6); Praktiken-Übersicht nach L27.

**Priorität** niedrig bis mittel. Aufwand: zwei Sätze.

### L23 Eigene Anforderungen: Format und Rückmeldung an das BSI

**Was fehlt.** 3.4.3 (S. 17) verlangt die „Formulierung der eigenen Anforderung in das vom GS++ vorgesehene Format“, ohne das Format zu beschreiben: die Satzschablone mit Praktik, Modalverb, Handlungswort, Ergebnis und Präzisierung, die Props für Zielobjektkategorie, Schutzzielwirkung, Aufwand und Gefährdungen. Die Guidance zu STM.2.1.6 erwähnt eine Zustellung eigener Anforderungen an das BSI; Verfahren und Adresse fehlen (Anhang D6).

**Beleg.** Standard 3.4.3 (S. 17); STM.2.1.6, STM.2.1.7; `documentation/datamodel/oscal_satzschablone_schema.json`; Issues #7, #58; Anhang D6.

**Vorschlag.** 3.4.3 ergänzen: Mindestfelder einer eigenen Anforderung, Ablage in einem eigenen Katalog neben dem Anwenderkatalog, Kennzeichnung im Paket, Rückmeldeweg an das BSI mit Adresse und Hinweis auf die Community-Kanäle.

**Priorität** niedrig bis mittel. Aufwand: ein Absatz.

## 4. Lücken mit Rang 3: Lesbarkeit und Redaktion

### L24 Glossar

**Was fehlt.** Der Standard hat kein Glossar. Begriffe mit Abweichung oder Mehrdeutigkeit: „Anwendungsbereich“ (Standard, 24 Treffer) gegen „Geltungsbereich“ (GC.6.1; im Standard null Treffer); „erfüllt“ gegen „umgesetzt“ (UMS.1.1); „erhebliche Abweichung“ (4.1.2) gegen „schwerwiegende Abweichung“ (AudS 4.6); allgemeine, explizite und Restrisikobetrachtung; temporär und dauerhaft; Nicht-Konformität, Abweichung und Fehler (VRB.2, VRB.4.1); Überwachung und Monitoring; Freigabe, Autorisierung und Genehmigung; Asset und Zielobjekt; Praktik, Anforderungspaket, Blaupause, Elternknoten, Sicherheitsniveau und Schutzbedarf, Untersuchungsobjekt und kritisches Asset.

**Beleg.** Standard durchgehend; Issue #116 B.2; Anhang D8, D45, D46; AG-1 #73, #74.

**Vorschlag.** Anhang „Begriffe“ mit Definitionen, abgestimmt mit den Namespaces der Bibliothek; je Begriffspaar eine Form festlegen und im Katalog nachziehen.

**Priorität** mittel bis hoch bei geringem Aufwand.

### L25 Vollständige Zuordnung zur ISO/IEC 27001

**Was fehlt.** Prozessschritt 1 ist den Kapiteln 4 und 5 der ISO/IEC 27001 zugeordnet (Kap. 2, S. 6), Prozessschritt 2 den Kapiteln „6 und 10“ (Kap. 3, S. 12); Kapitel 10 ist dort die Verbesserung, gemeint ist vermutlich 8. Die Schritte 3 bis 5 haben keine Zuordnung; 3.4 (S. 15) sagt pauschal, die Methodik-Praktiken bildeten die Kapitel 4 bis 10 ab.

**Beleg.** Standard Kap. 2 (S. 6), Kap. 3 (S. 12), 3.4 (S. 15); Anhang D48; Mapping-Sammlung ISO 27001 Annex A zu GS++.

**Vorschlag.** Tabelle Prozessschritt zu ISO-Kapitel als Auslegungsvorschlag: Schritt 1 zu 4, 5, 6.2, 7.1, 7.4, 7.5; Schritt 2 zu 6.1.2, 6.1.3 und 8.2; Schritt 3 zu 6.1.3, 8.1 und 8.3; Schritt 4 zu 9; Schritt 5 zu 10; dazu der Hinweis auf die Annex-A-Mapping-Sammlung; Korrektur in Kapitel 3.

**Priorität** mittel bei geringem Aufwand.

### L26 Abbildungen als Text, Hierarchie der Zielobjektkategorien, Namen

**Was fehlt.** Sechs Abbildungen tragen Inhalt, der sonst nirgends im Text steht: Abbildung 1 (PDCA-Zuordnung), 2 (Praktiken), 3 und 4 (Asset-Abhängigkeiten), 5 (Prozess des Anforderungspakets), 6 (Hierarchie der Zielobjektkategorien). Die Hierarchie ist die Grundlage der MUSS-Vererbung (STM.2.1.4.1) und steht normativ nur in der Grafik, maschinenlesbar nur im Namespace-CSV. Drei Kategorienamen weichen zwischen Anhang 1 und Namespace ab (Datenträgerarchiv gegen Archiv, Fax(-anwendungen) gegen Faxanwendungen, Interpersonelle Kommunikationsanwendungen gegen Interpersonelle Kommunikation), die Definition von „Räume“ ebenfalls; im Namespace ist die Spalte „Typ“ an zwei Stellen fehlerhaft.

**Beleg.** Standard 3.4.2 (S. 16), Anhang 1 (S. 28 bis 33); `target_object_categories.csv`; Issues #111, #116 B.1 und B.3; Anhang D30, D50.

**Vorschlag.** Anhang 1 um eine Spalte „Elternknoten“ ergänzen, Namen und Definitionen mit dem Namespace gleichziehen, die Inhalte der Abbildungen 1, 3, 4 und 5 als Text oder Tabelle führen.

**Priorität** mittel bei geringem Aufwand.

### L27 Praktiken-Übersicht

**Was fehlt.** Kapitel 3 (S. 12) sagt, Praktiken seien in Methodik, Technisch und Organisatorisch unterteilt, und verweist auf Abbildung 2. Eine Liste der 20 Gruppen des Anwenderkatalogs mit Kürzel, Name, Kategorie und Zahl der Anforderungen fehlt; der Standard nennt die Kürzel nicht, mit der einen Ausnahme „Umsetzung (UMS)“ in Kriterium 31.

**Beleg.** Standard Kap. 3 (S. 12), Kriterium 31 (S. 38); `practices.csv`; resolved Anwenderkatalog mit 20 Gruppen und 1000 Controls.

**Vorschlag.** Anhang „Praktiken“ mit Tabelle; Kürzel im Text verwenden, damit Standard und Katalog dieselbe Sprache sprechen.

**Priorität** niedrig bei geringem Aufwand.

### L28 Pflege des Standards und Rückmeldekanal

**Was fehlt.** Kapitel 1 (S. 5) kündigt an, die Erfahrungen der Early Adopters flössen in die Weiterentwicklung ein; einen Kanal nennt der Standard nicht. Das Repository bearbeitet Issues laut README nicht (Issue #1), die CONTRIBUTING.md verweist auf zwei archivierte und einen inaktiven AG-Fork (Issue #79). Erscheinungsrhythmus, Kopplung der Standard-Version an Katalogstände (L6) und ein Errata-Verfahren fehlen.

**Beleg.** Standard Kap. 1 (S. 5), Änderungshistorie (S. 2); Issues #1, #23, #79.

**Vorschlag.** Abschnitt 1.3 „Pflege“: Rückmeldekanal (Adresse des Referats, Service Center, Community-Portal), Erscheinungsrhythmus, Verhältnis der Standard-Version zum Katalogstand, Errata.

**Priorität** niedrig. Aufwand: ein Absatz.

### L29 Redaktionelle Funde

Die Funde stehen in Issue #116 und in Anhang D48 bis D51 des Handbuchs: die ISO-Zuordnung „Kapitel 6 und 10“ (S. 12); die Querverweise in den Hinweisen zu Kriterium 27 (nennt 34, gemeint ist 30) und Kriterium 30 (nennt 31 für die Ausnahmegenehmigung, die in 27 steht); der doppelte Absatz am Übergang von 3.4.1 zu 3.4.2 (S. 16); der Satz ohne Prädikat zur temporären Nichterfüllung (S. 19); „Kapiteln 4, und 5“ (S. 6), „berücksichtig“ (S. 7), „mit Ihnen“ (S. 14), „gewährleisteten“ (S. 22), „Informationssicherheitsrisken“ (S. 23), „Netzte“ (S. 29), „Messangeranwendungen“ (S. 32), „Prozessschritt Evaluation“ für einen Teilschritt (S. 27). Priorität: mit der nächsten Version, Aufwand gering.

## 5. Gliederungsvorschlag für eine Version 1.1

| Stelle im Standard | Änderung | Lücke |
|---|---|---|
| 1 Einleitung | neu 1.1 Verbindlichkeit und Verhältnis zum Anwenderkatalog; neu 1.2 Katalogstände und Übergangsfristen; neu 1.3 Pflege und Rückmeldung | L1, L6, L28 |
| 2.3 Anwendungsbereich | Begriff mit dem Katalog vereinheitlichen; mehrere Verbünde | L12, L24 |
| 2.6 Schutzbedarfsfeststellung | Absatz Vererbung auf Assets | L5 |
| 2.8 Rollen und Zuständigkeiten | Verweis auf den neuen Anhang Rollen | L18 |
| 2.9 Dokumentation und Kommunikation | Verweis auf den neuen Anhang Dokumente | L19 |
| 2.11 Initiierung der Risikobetrachtung | Konformität zu 200-3 und ISO/IEC 27005; Kriterien mit Controls | L21 |
| 3.1 Informationsverbund | wirksame Abgrenzung; Regeln für mehrere Verbünde | L12, L13 |
| 3.2 Erfassung der Assets | Absatz Gruppenbildung | L10 |
| 3.3 Blaupausen | Herausgeber, Form, Verbindlichkeit, Konflikte; Einstiegsprofil | L8, L15 |
| 3.4 Anforderungspaket | Satz zur einmaligen Berücksichtigung umformulieren; neu 3.4.4 Prozessbezogene Anforderungen | L2, L4 |
| 3.4.2 Zuordnung der Zielobjektkategorien | Bezugsart-Kategorien; Rolle von „erhöht“ | L5, L11 |
| 3.4.3 Ergänzung von Anforderungen | Format und Rückmeldung | L23 |
| 3.5 Gestaltungsentscheidungen | Parameter-Governance | L16 |
| neu 3.6 Zyklus und Abdeckung | | L14 |
| 4.1.1 Ermittlung des Umsetzungsstatus | Granularität; teilweise ist nicht erfüllt | L2 |
| 4.1.2 Bewertung fehlender Umsetzungen | Definitionen temporär, dauerhaft, Restrisikobetrachtung | L3 |
| neu 4.1.3 Ausnahmen | | L3 |
| neu 4.6 Compliance in der Umsetzung | | L17 |
| 5.1 Leistungsbewertung | Mindestkennzahlen | L20 |
| 5.4 Monitoring | Verweis auf die Kernel-Praktiken | L22 |
| neu 5.6 Überprüfung der Einhaltung von Verpflichtungen | | L17 |
| neu 6.5 Behandlung von Compliance-Verstößen | | L17 |
| neu Kapitel 7 Audit und Zertifizierung, oder eigener Standard 300-2 | | L7 |
| Anhang 1 Zielobjektkategorien | Spalte Elternknoten; Namen und Definitionen wie Namespace; Wurzel Geschäftsprozesse | L4, L26 |
| Anhang 3 Mindestkriterien | Querverweise 27 und 30 korrigieren | L29 |
| neu Anhang 5 Rollen und Entscheidungen | | L18 |
| neu Anhang 6 Dokumente des ISMS | | L19 |
| neu Anhang 7 Begriffe | | L24 |
| neu Anhang 8 Zuordnung zur ISO/IEC 27001 | | L25 |
| neu Anhang 9 Praktiken des Anwenderkatalogs | | L27 |
| neu Anhang 10 Zuordnung der Abschnitte zu Controls | | L1 |
| neu Anhang 11 Maschinenlesbare Abbildung | | L2 |
| neu Anhang 12 Übergang von IT-Grundschutz nach Grundschutz++ | | L9 |
| Abbildungen 1 bis 6 | Inhalt zusätzlich als Text oder Tabelle | L26 |

## 6. Reihenfolge in drei Stufen

**Stufe 1, Version 1.1 ohne Katalogänderung.** Alles, was eine Entscheidung festhält und keinen neuen Build braucht: die Verbindlichkeitsregel und der Zuordnungsanhang (L1), die Definitionen aus L3, die Vererbungsregel (L5), die Abgrenzungs- und Verbundregeln (L12, L13), Gruppenbildung (L10), Bezugsart-Kategorien (L11), Parameter (L16), Format eigener Anforderungen (L23), Glossar (L24), ISO-Zuordnung (L25), Abbildungen und Namen (L26), Praktiken (L27), Pflege (L28), Redaktion (L29). Das ist Schreibarbeit von Wochen, keine Abstimmung mit der Zertifizierungsstelle.

**Stufe 2, mit dem an den Standard angepassten Build.** Alles, was Katalog und Standard gleichzeitig ändert: Statusmodell und Datenmodell (L2), Ausnahmen (L3), prozessbezogene Anforderungen und die Wurzel in Anhang 1 (L4), Zyklus und Abdeckung (L14), Compliance-Kette (L17), Rollen (L18), Dokumente (L19), Kriterien mit Controls (L21), Monitoring (L22), Katalogstände (L6), sobald die Bibliothek Releases hat. Die sieben Widersprüche aus Issue #116 gehören in dieselbe Stufe.

**Stufe 3, eigene Dokumente und Arbeitsgruppen.** Prüfschema (L7), Einstiegsprofil als Blaupause (L8), Übergangsleitfaden (L9), Blaupausen-Register (L15), Kennzahlen (L20). Von diesen fünf trägt das Prüfschema am meisten, denn ohne Prüfschema bleiben die drei Zertifizierungssätze des Standards Versprechen.

Wer nur eines tun kann: Stufe 1 zuerst, denn sie kostet nichts außer Entscheidungen, die bereits gefallen sind.

## 7. Was nicht in den Standard gehört

37 der 81 Issues betreffen Datenformat, Pipeline, Namespaces und Repository-Betrieb. Sie sind berechtigt und gehören in die Bibliothek, in `documentation/OSCAL.md` oder in ein technisches Begleitdokument, und der Standard sollte sie weder beantworten noch erwähnen, mit zwei Ausnahmen: Die Versionsfrage (L6) und das Datenmodell des Status (L2) brauchen einen Satz im Standard, damit die Bibliothek eine Vorgabe hat. Die Tabelle nennt zusätzlich #53 (Standard-Lücke L6) und #92 (erledigt), weil sie zum Thema Versionierung gehören.

| Thema | Issues | Vorgeschlagener Ort |
|---|---|---|
| OSCAL-Konformität und Datenmodell (Props, Parameter, Namespaces, Hashes, Provenienz, Component Definitions, Profil-Auflösung) | #55, #56, #57, #58, #68, #70, #71, #83, #84, #85, #100, #101, #107, #113 | Bibliothek, `documentation/OSCAL.md`, Metaschema-Constraints |
| Namespaces und Vokabular (Dokumentbegriffe, Bindestriche, CSV-Format, Typ-Spalte, Aufwandsstufe 0) | #37, #44, #45, #46, #49, #104, #111 | Bibliothek, Namespace-Pflege; Dokumentbegriffe folgen dem Anhang aus L19 |
| Versionierung, Publikation, Änderungsprotokoll, Freigabestatus, Auffindbarkeit | #20, #38, #39, #53, #59, #66, #73, #92, #99, #114 | Release-Prozess der Bibliothek; Regel im Standard nach L6 |
| Mapping-Sammlungen (Abdeckung, veraltete Ziel-IDs, fehlende Quelle) | #61, #98 | Bibliothek; Einordnung im Übergangsanhang nach L9 |
| Inhalte einzelner Controls und Guidance | #60, #80, #109 | Katalogpflege |
| Community und Repository-Betrieb | #1, #31, #79 | README, CONTRIBUTING.md; Rückmeldekanal nach L28 |

## 8. Unsicherheiten und offene Fragen

1. Die Abbildungen 1 bis 6 wurden nicht ausgewertet. Falls Abbildung 5 oder 6 eine der hier als fehlend genannten Regeln zeigt (etwa eine Prozess-Wurzel oder die Granularität des Status), ist die Lücke eine Textlücke und keine Regelungslücke; sie bleibt dann als L26.
2. Die Kapitelangaben zum 200-2 (Kapitel 4, 6, 8.1.1, 8.2) stammen aus dem Handbuch und aus dem Gedächtnis; vor einer Weitergabe an das BSI gegen das PDF des 200-2 prüfen.
3. Die Zuordnung in Anhang A und die ISO-Tabelle in L25 sind Auslegung; der Standard nennt weder Control-IDs noch Kapitel der ISO für die Schritte 3 bis 5.
4. Die Issues des AG-1-Forks wurden am 26.10.2026 gesichtet und hier nicht neu gelesen; die zitierten Nummern (#60, #64, #71, #73, #74) beziehen sich auf diesen Stand.
5. Ob das BSI ein Prüfschema, einen Standard 300-2 oder ein Einstiegsprofil plant, ist nicht veröffentlicht; die Vorschläge zu L7 und L8 setzen voraus, dass nichts davon in Arbeit ist.
6. Die Wortzählungen laufen über den extrahierten Text; Silbentrennungen wurden bereinigt, Abweichungen um einzelne Treffer sind möglich.
7. Nächster Schritt für die Verwendung: Aus L1 bis L9 ein Issue oder eine Rückmeldung an das Referat S 13 formen, Anhang A als Beilage, Issue #116 als Referenz für die Katalogseite.

## Anhang A: Zuordnung der Methodik- und RISK-Controls zu den Abschnitten des Standards

Auslegung dieses Plans; der Standard nennt keine Control-IDs. Katalog-Build 2026-10-22 (Commit 160c177): 95 Methodik-Controls und die zehn Controls des Risikomanagement-Katalogs. Seitenangaben sind PDF-Seiten des Standards 300-1, Version 1.0. „kein“ heißt: kein Abschnitt des Standards behandelt den Gegenstand des Controls.

| Control | Titel | Modalverb | Abschnitt im Standard | Bemerkung |
|---|---|---|---|---|
| GC.1.1 | Errichtung und Aufrechterhaltung eines ISMS | MUSS | Kap. 1 (S. 5), 2.10 (S. 10) | Zyklus als Voraussetzung; Freigabe der Vorgehensweise |
| GC.1.2 | Freigabe des ISMS | MUSS | 2.10 (S. 10), 5.3 (S. 24) | Leitungsfreigaben, Managementbewertung |
| GC.2.1 | Festlegung des externen Kontextes der Institution | MUSS | 2.1.1 (S. 6) |  |
| GC.2.2 | Festlegung des internen Kontextes der Institution | MUSS | 2.1.2 (S. 6) |  |
| GC.3.1 | Verfahren und Regelungen | MUSS | 2.2 (S. 7) |  |
| GC.3.1.1 | Gesetzliche Verpflichtungen | MUSS | 2.2 (S. 7) |  |
| GC.3.1.2 | Anhörung zuständiger Stellen | SOLLTE | 2.2 (S. 7) | Anhörung der Compliance-Stellen als Aufzählungspunkt |
| GC.3.1.3 | Vertragliche Verpflichtungen | SOLLTE | 2.2 (S. 7) |  |
| GC.3.1.4 | Prävention von Verstößen | SOLLTE | kein | Prävention von Verstößen hat keinen Satz im Standard |
| GC.4.1 | Analyse der externen interessierten Parteien | MUSS | 2.4 (S. 8) |  |
| GC.4.2 | Analyse der internen interessierten Parteien | MUSS | 2.4 (S. 8) |  |
| GC.5.1 | Festlegung von Zielen für die Informationssicherheit | MUSS | 2.7 (S. 9) | SMART-Ziele |
| GC.5.1.1 | Festlegung einer Sicherheitsstrategie | MUSS | 2.7 (S. 9) |  |
| GC.5.1.2 | Verpflichtung der Institutionsleitung | MUSS | 2.7 (S. 9), 2.10 (S. 10) |  |
| GC.5.1.3 | Erstellung einer Sicherheitsleitlinie | MUSS | 2.7 (S. 9) |  |
| GC.5.1.4 | Freigabe der Sicherheitsleitlinie | MUSS | 2.7 (S. 9), 2.10 (S. 10) |  |
| GC.6.1 | Festlegung des Geltungsbereichs | MUSS | 2.3 (S. 7) | Standard sagt Anwendungsbereich, Katalog Geltungsbereich (L24) |
| GC.7.1 | Vorgehen bei der Informationssicherheitseinstufung | MUSS | 2.6 (S. 8 f.) |  |
| GC.7.1.1 | Festlegung der Geschäftsprozesse | MUSS | 2.5 (S. 8), Anhang 2 (S. 34 f.) |  |
| GC.7.1.2 | Festlegung des Schutzbedarfs | MUSS | 2.6 (S. 8 f.) | zwei Kategorien, eigene Kategorien mit Abbildung |
| GC.7.2 | Geschäftsprozesse mit hohem Schutzbedarf | MUSS | 2.6 (S. 9), 2.11 (S. 11), Kriterium 32 (S. 38) |  |
| GC.8.1 | Verfahren zur Ressourcenplanung | MUSS | 2.10 (S. 10), nur Stichwort | Freigabe der Ressourcen als Entscheidungsvorlage; kein Abschnitt zur Ressourcenplanung |
| GC.9.1 | Festlegung einer Sicherheitsorganisation | MUSS | 2.8 (S. 9) |  |
| GC.9.1.1 | Festlegung von Rollen und Zuständigkeiten | MUSS | 2.8 (S. 9) |  |
| GC.9.1.1.1 | Informationssicherheitsbeauftragter | MUSS | 2.8 (S. 9 f.) | ISB genannt; Unabhängigkeit nur als Interessenkonflikt |
| GC.9.1.1.1.1 | Ressourcen für den Informationssicherheitsbeauftragten | MUSS | kein | Ressourcen für den ISB |
| GC.9.1.1.1.2 | Vorspracherecht | MUSS | kein | Vorspracherecht |
| GC.9.1.1.2 | Stellvertreterregelungen | MUSS | kein | Stellvertretung |
| GC.9.1.1.3 | Vermeidung von Interessenkonflikten | MUSS | 2.8 (S. 9) | Vermeidung von Interessenkonflikten |
| GC.9.1.1.4 | Sicherstellung der Qualifikation | MUSS | 2.8 (S. 9) | Qualifikationen und Kompetenzen |
| GC.10.1 | Festlegung eines Verfahrens zum Kommunikationsmanagement | MUSS | 2.9 (S. 10) |  |
| GC.10.1.1 | Externer Austausch zur Informationssicherheit | SOLLTE | kein | externer Austausch zur Informationssicherheit |
| GC.10.1.2 | Kommunikation im Projektmanagement | MUSS | 2.8 (S. 10), 2.9 (S. 10) | ISB in Projekten; Kommunikation bei Projekten |
| GC.11.1 | Dokumentenlenkung | MUSS | 2.9 (S. 10) |  |
| GC.12.1 | Methodik für das Risikomanagement | MUSS | 2.11 (S. 10 f.) |  |
| STM.1.1 | Definition und Abgrenzung des Informationsverbunds | MUSS | 3.1 (S. 12 f.) |  |
| STM.1.2 | Dokumentation der externen Schnittstellen | MUSS | 3.1 (S. 13) | Absatz Dokumentation und Schnittstellen |
| STM.2.1 | Erstellung eines Anforderungspakets | MUSS | 3.4 (S. 15) |  |
| STM.2.1.1 | ISMS-Anforderungen | MUSS | 3.4, 3.4.1 (S. 15 f.) | Methodik-Anforderungen verbundweit |
| STM.2.1.2 | Erfassung relevanter Assets | MUSS | 3.1, 3.2 (S. 13 f.) | Asset-Abhängigkeiten nach Schutzbedarf nur im Standard |
| STM.2.1.3 | Mapping der Assets auf Zielobjektkategorien | MUSS | 3.2 (S. 14), 3.4.2 (S. 16 f.) |  |
| STM.2.1.4 | Modellierung der Anforderungen mit Zielobjektkategorie | MUSS | 3.4.2 (S. 16 f.) |  |
| STM.2.1.4.1 | Vererbung von Zielobjektkategorien | MUSS | 3.4.2 (S. 16 f.) | Elternknoten |
| STM.2.1.4.2 | Konsolidierung und Redundanzprüfung | MUSS | 3.4 (S. 15) | Dedupliziergebot |
| STM.2.1.5 | Modellierung der Anforderungen ohne Zielobjektkategorie | MUSS | 3.4, 3.4.1 (S. 15 f.) | Widerspruch: Streichung (Guidance) gegen Pflichtaufnahme (Standard), siehe L4 |
| STM.2.1.6 | Aufgrund anforderungsloser Assets | MUSS | 3.4.3 (S. 17) | ergänzende Anforderungen entwickeln |
| STM.2.1.7 | Aufgrund externer Verpflichtungen | MUSS | 2.2 (S. 7), 3.4.3 (S. 17) |  |
| STM.3.1 | Überprüfung des gesetzten Sicherheitsniveaus | SOLLTE | 3.4.2 (S. 17), teilweise | Standard: erhöht ist KANN und optional; Überprüfung des Niveaus fehlt, siehe L5 |
| STM.4.1 | Durchführung der Risikobetrachtung | MUSS | 4.2 (S. 19 f.), Anhang 3 (S. 36 ff.) |  |
| STM.5.1 | Setzen von Parametern | MUSS | 3.5 (S. 17) |  |
| UMS.1.1 | Ermittlung des Umsetzungsstatus | MUSS | 4.1.1 (S. 18) | drei Werte gegen zwei, siehe L2 |
| UMS.1.2 | Bewertung des Restrisikos | SOLLTE | 2.11 (S. 11), 4.1.1 (S. 18) | Pflicht im Standard, SOLLTE im Katalog, siehe L3 |
| UMS.2.1 | Umsetzungsplanung | MUSS | 4.3 (S. 20) |  |
| UMS.2.2 | Priorisierung von Maßnahmen | MUSS | 4.3 (S. 20) |  |
| UMS.3.1 | Benennung von Umsetzungszuständigen | MUSS | 4.4 (S. 21) |  |
| UMS.4.1 | Festlegung von Umsetzungsfristen | MUSS | 4.4 (S. 21) |  |
| UMS.5.1 | Autorisierung von Ausnahmen | MUSS | kein | nur Ausschluss für MUSS in 4.1.2 und Kriterium 27, siehe L3 |
| UMS.5.2 | Dokumentation von Ausnahmen | MUSS | kein | Kriterium 29 (akzeptierte Risiken), siehe L3 |
| UMS.6.1 | Nachverfolgung des Umsetzungsfortschritts | MUSS | 4.5 (S. 21) |  |
| UMS.6.2 | Fortschreibung des Umsetzungsplans | MUSS | 4.5 (S. 21) |  |
| UMS.7.1 | Wahrung von Compliance in der Umsetzung | MUSS | kein | 2.2 betrifft nur das Anforderungspaket, siehe L17 |
| VRB.1.1 | Verfahren zur kontinuierlichen Verbesserung | MUSS | Kap. 6 (S. 26), Einleitung |  |
| VRB.2.1 | Umgang mit Nicht-Konformitäten | MUSS | 6.1 (S. 26) |  |
| VRB.2.2 | Anpassung des ISMS | MUSS | 6.1 (S. 26) | grundlegende Anpassungen des ISMS |
| VRB.3.1 | Identifikation von Verbesserungspotenzialen | MUSS | 6.2 (S. 26 f.) |  |
| VRB.4.1 | Korrekturmaßnahmen | MUSS | 6.1, 6.3 (S. 26 f.) |  |
| VRB.4.2 | Verbesserungsmaßnahmen | MUSS | 6.2, 6.3 (S. 26 f.) |  |
| VRB.5.1 | Priorisierung von Maßnahmen | MUSS | 6.3 (S. 27) | Korrektur- und Verbesserungsplan geht in den Umsetzungsplan |
| VRB.6.1 | Überprüfung der erreichten Verbesserung | MUSS | 6.4 (S. 27) |  |
| VRB.6.2 | Bewertung der erreichten Verbesserung | SOLLTE | 6.4 (S. 27) |  |
| VRB.7.1 | Behandlung von Compliance-Verstößen | SOLLTE | Kap. 6 (S. 26), nur Aufzählungspunkt | kein Abschnitt, siehe L17 |
| PERF.1.1 | Verfahren und Regelungen | MUSS | 5.1 (S. 22) | Inhalt laut Standard offen, siehe L20 |
| PERF.1.2 | Evaluation des Umsetzungsplans | MUSS | 4.5 (S. 21), 6.2 (S. 27) |  |
| PERF.1.3 | Aktualität der Anforderungen | MUSS | 5.5 (S. 25) |  |
| PERF.2.1 | Überprüfung der Einhaltung von Verpflichtungen | SOLLTE | kein | siehe L17 |
| PERF.3.1 | Aufbau und Pflege eines Auditprogramms | MUSS | 5.2.1 (S. 22 f.) |  |
| PERF.3.1.1 | Erstellen eines Auditsplans | SOLLTE | 5.2.1 (S. 22 f.) |  |
| PERF.3.1.2 | Planen von internen Audits | MUSS | 5.2.1 (S. 22 f.) |  |
| PERF.3.1.3 | Auswahl des Auditteams | MUSS | 5.2.2 (S. 23) |  |
| PERF.3.1.4 | Umfang von Audits | MUSS | 5.2.1 (S. 23) | Ausmaß des Auditprogramms |
| PERF.3.2 | Dokumentation von Auditergebnissen | MUSS | 5.2.2 (S. 24) |  |
| PERF.3.2.1 | Einheitliches Bewertungsschema | SOLLTE | kein | einheitliches Bewertungsschema |
| PERF.3.2.2 | Kommunikation an Stakeholder | MUSS | 5.2.2 (S. 24) | Verteilung des Auditberichts |
| PERF.4.1 | Eignungsprüfung | MUSS | 5.3 (S. 24) |  |
| PERF.4.1.1 | Ergebnisse von Folgemaßnahmen | SOLLTE | 5.3 (S. 24) | Status früherer Managemententscheidungen |
| PERF.4.1.2 | Geänderte Rahmenbedingungen | SOLLTE | 5.3 (S. 24) |  |
| PERF.4.1.3 | Erfolge und Probleme | SOLLTE | 5.3 (S. 24), teilweise |  |
| PERF.4.1.4 | Interne Überprüfungen und Audits | SOLLTE | 5.3 (S. 24) |  |
| PERF.4.1.5 | Eignungsprüfung bisheriger Sicherheitsmaßnahmen | SOLLTE | 5.3 (S. 24), teilweise |  |
| PERF.4.1.6 | Rückmeldung von Stakeholdern | SOLLTE | kein | Rückmeldung von Stakeholdern |
| PERF.4.1.7 | Status des Realisierungsplans | SOLLTE | 4.5 (S. 21), 5.3 (S. 24) |  |
| PERF.4.1.8 | Verbesserungen | SOLLTE | 5.3 (S. 24), teilweise |  |
| PERF.4.1.9 | Maßnahmenvorschläge | MUSS | 5.3 (S. 24), teilweise | Maßnahmenvorschläge nur mittelbar |
| PERF.4.2 | Bericht an die Institutionsleitung | MUSS | 4.5 (S. 21), 5.3 (S. 24) | Managementbericht als Grundlage |
| PERF.5.1 | Methoden und Tools | MUSS | 5.4 (S. 24 f.) | drei Verfahren nur im Standard, siehe L22 |
| RISK.1.1 | Methodik für das Risikomanagement | MUSS | 2.11 (S. 11), Kriterien 1 bis 4 | importiert |
| RISK.1.2 | Einhaltung der BSI-Kriterien | MUSS | 2.11 (S. 11), Anhang 3 als Ganzes | nicht importiert |
| RISK.1.3 | Risikoeigentümer | MUSS | 2.11 (S. 11), Kriterien 5 und 16 | importiert |
| RISK.1.4 | Risikoappetit | MUSS | 2.11 (S. 11), Kriterium 7 | nicht importiert |
| RISK.1.5 | Freigabe des Risikomanagements | MUSS | 2.11 (S. 11), Kriterium 9 | importiert |
| RISK.1.6 | Kritikalitätskriterien für Geschäftsprozesse | MUSS | Kriterium 6 | nicht importiert |
| RISK.1.7 | Kriterien für die Risikobeurteilung | MUSS | Kriterien 6, 18 bis 20 | nicht importiert |
| RISK.1.8 | Kriterien für die Risikoakzeptanz | MUSS | Kriterien 8 und 22 | nicht importiert |
| RISK.1.9 | Bestätigung des Restrisikos | SOLLTE | 2.11 (S. 11), 4.1.1 (S. 18), Kriterium 30 | nicht importiert; SOLLTE |
| RISK.1.10 | Freigabe der Umsetzungsplanung | MUSS | 4.2.3 (S. 19), Kriterium 31 | importiert |

Controls ohne Abschnitt im Standard (11): GC.3.1.4, GC.9.1.1.1.1, GC.9.1.1.1.2, GC.9.1.1.2, GC.10.1.1, UMS.5.1, UMS.5.2, UMS.7.1, PERF.2.1, PERF.3.2.1, PERF.4.1.6. Nur teilweise oder nur als Stichwort behandelt (7): GC.8.1, STM.3.1, VRB.7.1, PERF.4.1.3, PERF.4.1.5, PERF.4.1.8, PERF.4.1.9.
## Anhang B: Alle Issues des Repositories BSI-Bund/Stand-der-Technik-Bibliothek

Stand 2026-10-28, gelesen mit `gh issue list --state all`: 81 Issues, davon 48 offen und 33 geschlossen. Einordnung: „Standard-Lücke“ (der Standard müsste es regeln, Nummer der Lücke in Spalte Bezug), „Bibliothek“ (Datenformat, Pipeline, Namespaces; gehört in die Bibliothek, nicht in den Standard), „erledigt“ (vom BSI umgesetzt oder gegenstandslos), „geschlossen“ (von uns am 26.10.2026 geschlossen, weil der Standard die Frage entscheidet, oder aus anderem Grund geschlossen).

| Nr. | Status | Titel | Autor | Einordnung | Bezug |
|---|---|---|---|---|---|
| #1 | offen | Disclaimer zu GitHub Issues & Discussions | FriedsamDario | Bibliothek, Community | L28 |
| #3 | geschl. | Typos oder/und fehlende Dateien | RonnyDo | erledigt |  |
| #6 | geschl. | Inkonsistenzen und Formatfehler in den namespaces CSV-Dateien | juergenpabel | erledigt |  |
| #7 | geschl. | ITGS++ spezifisches OSCAL-schema | juergenpabel | erledigt (Beta-Schema) | L23 |
| #11 | geschl. | Formatierung der JSON- / XML-Datei | DanielRuf | erledigt |  |
| #13 | geschl. | Dateien sind teilweise nicht UTF-8 enkodiert | DanielRuf | erledigt |  |
| #18 | geschl. | GitHub Action für Validierung der OSCAL-Dateien | DanielRuf | geschlossen, Bibliothek |  |
| #20 | offen | Feature-Vorschlag: Prüfmechanismus Katalog-Updates | juergenpabel | Bibliothek | L6 |
| #22 | geschl. | XML / JSON inhaltliche Inkonsistenzen | Rusty-Weasel | erledigt |  |
| #23 | geschl. | Vorschlag: Link / Übersicht zu den Arbeitsgruppen in CONTRIBUTING.md | DanielRuf | erledigt |  |
| #26 | geschl. | Übernahme der noch nicht abgeschlossenen Issues aus dem nicht öffentlichen GitHub | LarsSaenger | erledigt |  |
| #27 | offen | "Vorbereitende Aufgaben" des Basis Phasenmodells | LarsSaenger | Standard-Lücke | L8, L15 |
| #31 | offen | Typo in Plan-Do-Check-Act-Zyklus Grafik in der Dokumentation zu OSCAL | ljrk0 | Bibliothek, redaktionell |  |
| #32 | geschl. | Zielobjekt "ISMS"? | Christoph-Puppe-Work | geschlossen, Standard 3.4 entscheidet | Rest in L4 |
| #33 | geschl. | Bereitstellungsprozess | sluetze | geschlossen, Bibliothek |  |
| #37 | offen | Stufe 0 | LarsSaenger | Bibliothek (effort_level), siehe #104 |  |
| #38 | offen | Neue UUID | Christoph-Puppe-Work | Bibliothek | L6 |
| #39 | offen | Versionierung | Christoph-Puppe-Work | Bibliothek | L6 |
| #40 | geschl. | Fehlender Link in Guidance zu STM 9.2 | dfurater | erledigt |  |
| #41 | offen | Assessment methods & Control objectives? | Christoph-Puppe-Work | Standard-Lücke | L7 |
| #42 | geschl. | action_words.csv -> Synonyme schneidet "n" als letzten char ab | dfurater | erledigt |  |
| #43 | geschl. | Falsche Dateinamen in Dokumentation/namespaces/readme.md | sdierkes | erledigt |  |
| #44 | offen | Mismatch zwischen documentation-Werten im Grundschutz++-Katalog und Dokumentation/names… | dfurater | Bibliothek | L19 |
| #45 | offen | Vewendung UTF-8 "Bindestriche" in BSI-Stand-der-Technik-Kernel-catalog.json | sdierkes | Bibliothek |  |
| #46 | offen | documentation_guidelines - mögliche Dublette | sdierkes | Bibliothek | L19 |
| #47 | geschl. | Maßnahme ist erhöht und SOLL | christoph-puppe | geschlossen, Standard 3.4.2 entscheidet | L5 (Katalog zieht nach) |
| #48 | geschl. | doppelte Leerzeichen | DanielRuf | erledigt |  |
| #49 | offen | Kodierung u. Formatierung der CSV-Datei-Inhalte | Ste-Ri | Bibliothek |  |
| #50 | geschl. | Dublette in Namespace tags.csv | sdierkes | erledigt |  |
| #51 | geschl. | Proposal: ATR detection rule mapping for Grundschutz++ AI module (OSCAL profile contrib… | eeee2345 | geschlossen, ohne Bezug |  |
| #52 | geschl. | Updates als PR? | Christoph-Puppe-Work | erledigt |  |
| #53 | offen | Releases? | Christoph-Puppe-Work | Standard-Lücke | L6 |
| #54 | geschl. | security_targets.csv / Erläuterung der möglichen Werte? | Stephan-Huettinger | erledigt |  |
| #55 | offen | OSCAL: Identische Control-IDs in Anwenderkatalog (Grundschutz++) und Mindeststandard-TL… | Christoph-Puppe-Work | Bibliothek | L15 (Kompositionsregel) |
| #56 | offen | OSCAL: Mehrwertige Angaben als kommaseparierte Strings statt als native OSCAL-Konstrukt… | Christoph-Puppe-Work | Bibliothek |  |
| #57 | offen | OSCAL: Instabile ns-URIs (tree/main-Links auf CSV-Dateien) statt stabiler Namespace-Ide… | Christoph-Puppe-Work | Bibliothek |  |
| #58 | offen | Vorschlag: Erweiterungs-Vokabular als externe Metaschema-Constraints formalisieren (Ers… | Christoph-Puppe-Work | Bibliothek | L23 |
| #59 | offen | UUID↔ID Zuordnung in Mapping-Dateien nicht konform zu aktuellem Anwenderkatalog und zu … | Stephan-Huettinger | Bibliothek | L6 |
| #60 | offen | Vollkonvertierungs-Experiment über GS++ und MS TLS: 49.804 Feldwerte, 100 % Abdeckung, … | christoph-puppe | Bibliothek |  |
| #61 | offen | Mapping source ISMS.1.A10-UA.7 nicht vorhanden | Stephan-Huettinger | Bibliothek | L9 |
| #62 | geschl. | basethreats.csv: Spalte uuid enthält keine echten (zufälligen) UUIDs, sondern hochgezäh… | dfurater | erledigt |  |
| #66 | offen | Gedanken zu den neuen PRs | christoph-puppe | Bibliothek | L6 |
| #68 | offen | OSCAL 1.2.2: Zusätzliche QA-Felder in der Mapping-Provenienz verhindern Schema-Validierung | dfurater | Bibliothek |  |
| #69 | geschl. | OSCAL 1.1.3: ISO-27001-Annex-A-Katalog verletzt TokenDatatype für IDs und Klassen | dfurater | erledigt (Artefakt entfernt) |  |
| #70 | offen | OSCAL 1.1.2: GA-Lotse-Component-Import enthält unzulässiges remarks-Feld | dfurater | Bibliothek |  |
| #71 | offen | OSCAL 1.1.2: Lieferkettensicherheit-Component-Definition verwendet links-Objekte statt … | dfurater | Bibliothek |  |
| #72 | geschl. | Vorschlag: Change Log | Christoph-Puppe-Work | geschlossen, durch #73 ersetzt |  |
| #73 | offen | Updated Changelog Vorschlag | Christoph-Puppe-Work | Bibliothek | L6 |
| #74 | geschl. | GC.4.2 interne / externe Stellen | Christoph-Puppe-Work | erledigt |  |
| #75 | geschl. | GC.7 Tippfehler "Infomationssicherheitseinstufung" | Christoph-Puppe-Work | erledigt |  |
| #76 | geschl. | GC.3.1.1 Falscher Name des Gesetzes | Christoph-Puppe-Work | erledigt |  |
| #77 | offen | GC.6.1 Abgrenzung des Geltungsbereiches | Christoph-Puppe-Work | Standard-Lücke | L13 |
| #78 | geschl. | RISK.1.10 Nicht im Anwenderkatalog | Christoph-Puppe-Work | geschlossen, Standard 2.11 und 4.1.1 entscheiden | L3 |
| #79 | offen | CONTRIBUTING.md: zwei der vier verlinkten AG-Forks sind archiviert, ein dritter seit Mo… | Christoph-Puppe-Work | Bibliothek, Community | L28 |
| #80 | offen | Methodik-Katalog: 36 von 95 Controls ohne `documentation`-Prop, obwohl mehrere davon au… | Christoph-Puppe-Work | Bibliothek | L19 |
| #81 | offen | Modellierung von Prozessen ist nicht geregelt: 265 Kernel-Controls ohne Zielobjektkateg… | Christoph-Puppe-Work | Standard-Lücke | L4 |
| #82 | offen | Zuweisung der Zielobjektkategorie „IT-Produkte" für beschaffte Zielobjekte ist nirgends… | Christoph-Puppe-Work | Standard-Lücke | L11 |
| #83 | offen | MD5 als Hash-Algo | christoph-puppe | Bibliothek |  |
| #84 | offen | Resolved Catalogs ohne Resolution-Provenienz (source-profile / resolution-tool) | christoph-puppe | Bibliothek |  |
| #85 | offen | OSCAL: scope_*-Props verwenden den OSCAL-Dokumentnamespace statt eines BSI-Namespaces | dfurater | Bibliothek |  |
| #87 | geschl. | OSCAL 1.1.3: WLAN-Profil enthält unzulässiges leeres metadata.links-Array | dfurater | erledigt |  |
| #89 | geschl. | KONF.6.1.2 - Isolierung von Anwendungen | sluetze | erledigt |  |
| #90 | geschl. | KONF.4.1.1 - Weiterleitung von Anmeldeinformationen | sluetze | erledigt |  |
| #92 | offen | Planned repository history rewrite | app/sdt-publication-bot | erledigt |  |
| #94 | geschl. | KONF.7.14 - Code-Signierung im Betriebssystemkern | sluetze | erledigt |  |
| #95 | offen | Umsetzungsstatus „nicht umgesetzt“ (UMS.1.1) ist in OSCAL nicht standardkonform abbildb… | Christoph-Puppe-Work | Standard-Lücke (Abbildung des Status) | L2 |
| #96 | geschl. | Binärer Umsetzungsstatus (UMS.1.1) verschenkt die OSCAL-Statuswerte; der Umsetzungsplan… | Christoph-Puppe-Work | geschlossen, Standard 4.1.1 entscheidet | L2 |
| #98 | offen | ITGS-zu-GS++-Mapping: 1.324 von 1.834 aktiven ED23-Anforderungen ohne Zuordnung, 17 GS+… | Christoph-Puppe-Work | Bibliothek | L9 |
| #99 | offen | Unfertige Artefakte liegen im `main`-Branch | Christoph-Puppe-Work | Bibliothek | L6 |
| #100 | offen | Implementation Layer: `control-implementation.source` verweist in keiner Component Defi… | dfurater | Bibliothek |  |
| #101 | offen | Implementation Layer: `implemented-requirement.control-id` trägt `alt-identifier`-Werte… | dfurater | Bibliothek |  |
| #103 | offen | Vorschlag: Gewichtungs-Prop `weight` und Scoring-Methodik für den Anwenderkatalog Grund… | Christoph-Puppe-Work | Standard-Lücke, optional | L20 |
| #104 | offen | Katalogfund: `effort_level` 0 kodiert Verbindlichkeit statt Aufwand (148 MUSS-Controls … | Christoph-Puppe-Work | Bibliothek |  |
| #106 | geschl. | Gruppenbildung von Assets ist in der Strukturmodellierung nicht geregelt: STM modellier… | christoph-puppe | geschlossen, Standard 3.2 entscheidet | L10 (Kriterien fehlen) |
| #107 | offen | Implementation Layer: Component Definitions sind nicht auflösbar, Control-IDs uneinheit… | christoph-puppe | Bibliothek |  |
| #109 | offen | Control 'REA.2.6.1' and 'REA.2.6.2.1' have no 'guidance' part with prose. | ManuelHaas | Bibliothek |  |
| #110 | offen | Laufzeit-Artefakte fehlen: Änderungsmitteilung, periodischer Statusbericht, Vorfallsber… | Christoph-Puppe-Work | Standard-Lücke, teilweise | L19 |
| #111 | offen | Die Zielobjektkategorie "Externe Netzanschlüsse" hat keinen Typ | ManuelHaas | Bibliothek | L26 |
| #113 | offen | Profil-Parameter werden nicht in `result`/`result_specification` übernommen (5 Anforder… | dfurater | Bibliothek | L16 |
| #114 | offen | GitHub Pages deployment | codikyo | Bibliothek |  |
| #116 | offen | Anwenderkatalog Grundschutz++ (Build 2026-10-22) gegen BSI-Standard 300-1 v1.0: Prüflis… | Christoph-Puppe-Work | Standard und Katalog | L1, L3, L5, L26, L29 |

Verteilung: Bibliothek 37, erledigt 25, geschlossen 9, Standard-Lücke 9, Standard und Katalog 1.
