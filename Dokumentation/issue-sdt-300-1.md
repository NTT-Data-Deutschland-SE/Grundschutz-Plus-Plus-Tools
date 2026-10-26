Anwenderkatalog Grundschutz++ (Build 2026-10-22) gegen BSI-Standard 300-1 v1.0: Prüfliste der Abweichungen und offene Punkte

> Angelegt am 2026-10-26 als https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek/issues/116

## Zusammenfassung

Der BSI-Standard 300-1 „Methodik Grundschutz++" (Version 1.0, 20.10.2026) ist veröffentlicht; der Anwenderkatalog soll an ihn angepasst werden. Der Build vom 2026-10-22 (Commit 160c177) enthält diese Anpassung noch nicht. Dieses Issue ist die aus Anwendersicht nachgerechnete Prüfliste: Teil A nennt die Stellen, an denen Standard und Katalog sich widersprechen und der Katalog voraussichtlich nachzieht. Teil B nennt Punkte, die der Standard selbst nicht entscheidet. Ein kurzer dritter Teil listet redaktionelle Funde am Standard; falls das Repository dafür der falsche Kanal ist, gehen sie an das Referat S 13.

Querverweis: Das Statusmodell wird bereits in #95 und #96 diskutiert; Teil A.1 ergänzt dort nur die Fassung des Standards.

Die ausführliche Herleitung mit Zitaten und Zahlen liegt im Repository NTT-Data-Deutschland-SE/Grundschutz-Plus-Plus-Tools unter `Dokumentation/abgleich-bsi-standard-300-1_v0.2.md`.

## Betroffene Artefakte

| Artefakt | Stand | Kennung |
|---|---|---|
| Anwenderkatalog Grundschutz++ (resolved catalog) | Build 2026-10-22, Commit 160c177 | Katalog-UUID `81573937-c2ea-4021-8833-a555856e2ac9` |
| Profil `Grundschutz++-profile.json` | 2026-10-22 | Profil-UUID `110d3a0c-2d64-4922-b3ea-3e2599f1a489`; Import Risikomanagement mit `with-ids` RISK.1.1, RISK.1.3, RISK.1.5, RISK.1.10 |
| Katalog „BSI Anforderungen zum Risikomanagement" | 2026-10-22 | Katalog-UUID `1044214b-a7b5-41e5-bb81-58165006be60` |
| Namespace `documentation/namespaces/target_object_categories.csv` | Commit 160c177 | 39 Zeilen |
| BSI-Standard 300-1 | Version 1.0, 20.10.2026 | Seitenangaben beziehen sich auf das PDF (`standard_300-1.pdf?v=3`) |

Controls (ID, Titel, `alt-identifier`):

| ID | Titel | alt-identifier |
|---|---|---|
| UMS.1.1 | Ermittlung des Umsetzungsstatus | `e2c90fc0-e6e5-4a89-8099-39360b6e8eb9` |
| STM.2.1.5 | Modellierung der Anforderungen ohne Zielobjektkategorie | `6fa942b2-8081-4a68-8b37-60ae5e4dc081` |
| UMS.5.1 | Autorisierung von Ausnahmen | `c3e9f936-827a-4af2-a750-0777a082477d` |
| UMS.1.2 | Bewertung des Restrisikos | `8b7626ab-3fcf-45bd-a7ba-45705436c909` |
| STM.4.1 | Durchführung der Risikobetrachtung | `42cc5d6f-e4f8-4247-a8fa-f90988af02cb` |
| GC.12.1 | Methodik für das Risikomanagement | `0567f921-f474-4060-9a64-11e5148ebe09` |
| GC.6.1 | Festlegung des Geltungsbereichs | `ebff4c7b-77b1-4d08-bc57-37d3ca16242c` |
| RISK.1.2 | Einhaltung der BSI-Kriterien (nicht importiert) | `3ac69ca1-773a-4605-83e8-fc3a63388a2d` |
| RISK.1.4 | Risikoappetit (nicht importiert) | `162c1099-8bc3-4bc7-851a-636291308bb1` |
| RISK.1.6 | Kritikalitätskriterien für Geschäftsprozesse (nicht importiert) | `b092d4cb-5c4e-49bc-a1ce-f40d22d3b5ec` |
| RISK.1.7 | Kriterien für die Risikobeurteilung (nicht importiert) | `f6e125dc-4554-4ad9-82d7-5b0bca97521a` |
| RISK.1.8 | Kriterien für die Risikoakzeptanz (nicht importiert) | `a687403b-f8ca-4f15-8978-ceb295106f62` |
| RISK.1.9 | Bestätigung des Restrisikos (nicht importiert) | `3e515ecc-0f01-4a43-90c8-c165ae3d28ee` |
| BES.1.4 | Outsourcing-Strategie | `302952ea-72e1-4104-9cbb-678717a267db` |
| DET.4.12.1 | Auslastung des Netzes | `c17dd877-0922-4ca8-a38b-1d2f9ae04f0d` |
| REA.2.5 | IT-Forensik | `6de9ac83-2280-4fbd-ac54-f570faa7b211` |

## Teil A: Erwartete Katalogänderungen

- [ ] **A.1 Umsetzungsstatus: drei Werte statt zwei.**
  Standard 4.1.1 (S. 18) nennt drei Werte: „erfüllt" („ja"), „nicht erfüllt" („nein"), „nicht anwendbar"; dazu: „Für jede ‚nicht anwendbare' Anforderung ist eine Begründung zu dokumentieren."
  Katalog, Guidance UMS.1.1: „Der Umsetzungsstatus einer Anforderung kann grundsätzlich nur ‚umgesetzt' (‚ja') oder ‚nicht umgesetzt' (‚nein') sein."
  Auswirkung: Werkzeuge und Prüfungen, die auf dem binären Modell aufsetzen, kennen den dritten Wert nicht; in OSCAL entspricht er `not-applicable`.
  Vorschlag: Guidance UMS.1.1 um „nicht anwendbar" mit Begründungspflicht ergänzen; Begriffe „erfüllt" (Standard) und „umgesetzt" (Katalog) angleichen.

- [ ] **A.2 Anforderungen ohne Zielobjektkategorie: Aufnahmepflicht statt Streichung.**
  Standard 3.4.1 (S. 16): „Alle weiteren Anforderungen ohne zugewiesene Zielobjektkategorie sind verpflichtend in das Anforderungspaket aufzunehmen." Die Nichtanwendbarkeit wird nach 4.1.1 erst im Umsetzungsstatus festgestellt.
  Katalog, Guidance STM.2.1.5: „Für die vorliegenden Geschäftsprozesse nicht relevante Anforderungen werden aus dem Anforderungspaket gestrichen, was mit einer Begründung zu dokumentieren ist".
  Auswirkung: Betrifft 265 Kernel-Controls ohne `target_object_categories`; der Ort der Relevanzentscheidung (Modellierung oder Realisierung) bestimmt, ob ein Profil mit Positivliste oder der Statuswert im SSP der richtige Weg ist.
  Vorschlag: Guidance STM.2.1.5 an 3.4.1 angleichen und auf den Status „nicht anwendbar" verweisen.

- [ ] **A.3 MUSS-Anforderungen: keine Ausnahme, keine Risikoakzeptanz.**
  Standard 4.1.2 (S. 19): „Die Durchführung einer Risikobetrachtung kann die Erfüllung einer MUSS-Anforderung nicht ersetzen. Eine Ausnahmegenehmigung oder Risikoakzeptanz ist nicht möglich."
  Katalog: UMS.5.1 „Umsetzung MUSS Ausnahmegenehmigungen für Verpflichtungen durch {{eine zuständige Person oder Rolle}} autorisieren", Guidance ohne Bezug auf das Modalverb; Guidance STM.4.1 nennt „Nicht-Umsetzung von Anforderungen" als Auslöser ohne Einschränkung.
  Auswirkung: Der Geltungsbereich von UMS.5 ist unklar (Compliance-Verpflichtungen, SOLLTE-Anforderungen oder beides); der Standard verwendet „Ausnahmegenehmigung" in Mindestkriterium 27 für ein Risiko außerhalb der Akzeptanzkriterien.
  Vorschlag: Guidance UMS.5.1 um den Satz ergänzen, dass MUSS-Anforderungen ausgenommen sind, und den Begriff „Verpflichtungen" definieren.

- [ ] **A.4 SOLLTE-Anforderungen: temporär oder dauerhaft, Restrisiko als Pflicht.**
  Standard 4.1.2 (S. 18 f.): „Für jede nicht erfüllte SOLLTE-Anforderung ist die Nichterfüllung als temporär oder dauerhaft einzuordnen"; dauerhaft löst eine Risikobetrachtung aus. Standard 2.11 (S. 11): „Für SOLLTE-Anforderungen, die in der Umsetzungsplanung enthalten, aber noch nicht erfüllt sind, muss eine Restrisikobetrachtung durchgeführt werden. Das identifizierte Risiko muss durch die Institutionsleitung freigegeben werden."
  Katalog: UMS.1.2 „Umsetzung SOLLTE das bestehende Restrisiko durch die nicht umgesetzten Anforderungen festlegen" (SOLLTE, ohne Leitungsfreigabe); RISK.1.9 (Kenntnisnahme durch Risikoeigentümer, SOLLTE) ist nicht importiert.
  Auswirkung: Die Leitungsfreigabe des Restrisikos ist im Standard Pflicht, im Katalog nirgends als MUSS verankert.
  Vorschlag: UMS.1.2 auf MUSS mit Freigabe durch die Institutionsleitung heben; die Begriffe „temporäre" und „dauerhafte Nichterfüllung" in UMS.1 einführen.

- [ ] **A.5 Mindestkriterien für die Risikobetrachtung: Bindung fehlt im Anwenderkatalog.**
  Standard 2.11 (S. 11): Das Verfahren ist frei wählbar, „sofern die im Anhang (siehe Anhang 3: Mindestkriterien für die Risikobetrachtung in GS++) festgelegten verbindlichen Mindestkriterien erfüllt werden"; Anhang 3 enthält 35 Kriterien.
  Katalog: Guidance GC.12.1 „Die Risikomanagementmethodik kann frei gewählt werden, sollte aber anerkannte Standards erfüllen." Der Risikomanagement-Katalog bindet den Kriterienkatalog in RISK.1.2 („Risikomanagement MUSS die Einhaltung des BSI-Kriterienkatalogs bei der Methodenauswahl anweisen"); das Profil importiert nur RISK.1.1, RISK.1.3, RISK.1.5 und RISK.1.10.
  Abdeckung der Kriterien durch Controls im Anwenderkatalog, nachgerechnet:

  | Kriterium | Control im Quellkatalog | Im Anwenderkatalog |
  |---|---|---|
  | 1 bis 4 Verfahren verankern und dokumentieren | RISK.1.1, GC.12.1 | ja |
  | 5 Rollen, Risikoeigentümer | RISK.1.3 | ja |
  | 6 Kriterien für Identifikation und Bewertung | RISK.1.7, RISK.1.6 | nein |
  | 7 Risikoappetit | RISK.1.4 | nein |
  | 8 Risikoakzeptanzkriterien | RISK.1.8 | nein |
  | 9 Autorisierung durch die Leitung | RISK.1.5 | ja |
  | 10 bis 16, 18 bis 29, 35 | keines | nein |
  | 17 elementare Gefährdungen bei dauerhafter SOLLTE-Nichterfüllung | keines (Datenbasis: `threats`-Props) | nein |
  | 30 Restrisiken durch die Leitung | RISK.1.9 (SOLLTE), UMS.1.2 (SOLLTE) | teilweise |
  | 31 Umsetzungsplanung durch Risikoeigentümer | RISK.1.10 | ja |
  | 32 bis 34 Auslöser | GC.7.2, STM.4.1 | ja |
  | Kriterienkatalog als Ganzes | RISK.1.2 | nein |

  Auswirkung: Im Anwenderkatalog sind die Mindestkriterien nicht verbindlich; sie gelten nur über den Standard.
  Vorschlag: RISK.1.2, RISK.1.4, RISK.1.6 bis RISK.1.9 in das Profil aufnehmen oder GC.12 entsprechend ergänzen; Kriterium 35 (jährliche Überprüfung) als Control oder Parameter abbilden.

- [ ] **A.6 Auslöser der Risikobetrachtung: drei statt vier.**
  Standard 2.11 (S. 11): hoher Schutzbedarf „bei mindestens einem Schutzziel", nicht hinreichend abgedecktes Asset, dauerhafte Nichterfüllung einer anwendbaren SOLLTE-Anforderung (Kriterien 32 bis 34).
  Katalog, Guidance STM.4.1: „bei Geschäftsprozessen oder Assets mit hohem Schutzbedarf, bei Herabstufung des Sicherheitsniveaus (von erhöht auf normal- SdT) oder bei Nicht-Umsetzung von Anforderungen" sowie bei Assets ohne passende Anforderungen.
  Auswirkung: Die Herabstufung als Auslöser fehlt im Standard, die „Nicht-Umsetzung" ist im Standard auf dauerhafte SOLLTE-Nichterfüllung eingegrenzt.
  Vorschlag: Guidance STM.4.1 auf die drei Auslöser des Standards umstellen.

- [ ] **A.7 Sicherheitsniveau „erhöht" durchgängig KANN.**
  Standard 3.4.2 (S. 17): „Anforderungen mit dem Sicherheitsniveau ‚erhöht' beinhalten das Modalverb ‚KANN' und sind optional zu erfüllen."
  Katalog: 224 Kernel-Controls mit `sec_level` „erhöht" tragen KANN, drei tragen SOLLTE: BES.1.4, DET.4.12.1, REA.2.5.
  Auswirkung: Für diese drei Controls greift die Temporär/Dauerhaft-Regel aus 4.1.2, obwohl sie laut Standard optional sein müssten.
  Vorschlag: Modalverb oder `sec_level` der drei Controls angleichen.

## Teil B: Punkte, die der Standard nicht entscheidet

- [ ] **B.1 Namen der Zielobjektkategorien.** Anhang 1 des Standards und der Namespace `target_object_categories.csv` haben je 39 Kategorien unter denselben sieben Wurzeln; der Build 2026-10-22 verwendet in den Props die Namen des Namespace. Drei Namen weichen zwischen Standard und Namespace ab:

  | Standard, Anhang 1 | Namespace und Katalog-Props |
  |---|---|
  | Datenträgerarchiv | Archiv |
  | Fax(-anwendungen) | Faxanwendungen |
  | Interpersonelle Kommunikationsanwendungen | Interpersonelle Kommunikation |

  Die Definitionen von „Räume" und „Netze" lauten im Namespace anders als in Anhang 1 (Namespace „Räume": „Orte, an denen sich Arbeitsplätze oder Anlagen zur Datenverarbeitung im Informationsverbund befinden."; Anhang 1: „Standorte, die durch eine bauliche Abgrenzung unterteilt sind und einer bestimmten Nutzung dienen."; Namespace „Netze" endet mit Beispielen, Anhang 1 mit „soweit sie Teil des Informationsverbundes sind"); „Outsourcing" unterscheidet sich nur in der Schreibweise „substantiellem" gegen „substanziellem". Die übrigen 36 Definitionen sind wortgleich. Vorschlag: eine Schreibweise und eine Definition je Kategorie festlegen und in Standard, Namespace und Props verwenden.

- [ ] **B.2 Begriffe.** Standard 2.3 (S. 7): „legt die Institutionsleitung den Anwendungsbereich (Scope) fest"; 3.1 (S. 13): „Der Anwendungsbereich kann einen oder mehrere Informationsverbünde enthalten." Katalog: GC.6.1 „Governance und Compliance MUSS den nachvollziehbar abgegrenzten Geltungsbereich nach Freigabe der Institutionsleitung festlegen", Guidance „(Scope)". Ebenso „erfüllt" (Standard 4.1.1) gegen „umgesetzt" (UMS.1.1) und „erhebliche Abweichung" (Standard 4.1.2, S. 19) gegen „schwerwiegende Abweichung" (Auditierungsschema). Vorschlag: je Begriffspaar eine Form festlegen.

- [ ] **B.3 Namespace, Spalte „Typ".** In `target_object_categories.csv` ist „Typ" bei „Externe Netzanschlüsse" leer und bei „Institutionsleitung" mit „Mitarbeitende" belegt, während die übrigen Zeilen die Wurzelkategorie tragen.

## Redaktionelle Funde am Standard 300-1

Falls das Repository dafür der falsche Kanal ist, gehen diese Punkte an das Referat S 13 (referat-s13@bsi.bund.de).

1. Kapitel 3 (S. 12): „In diesem Prozessschritt werden die Aktivitäten aus den Kapiteln 6 und 10 der DIN EN ISO/IEC 27001 durchgeführt." Kapitel 10 der ISO/IEC 27001:2022 ist „Verbesserung" und gehört zu Prozessschritt 5; vermutlich ist Kapitel 8 gemeint. Die Prozessschritte 3 bis 5 haben keine ISO-Zuordnung.
2. Anhang 3, Querverweise: Der Hinweis zu Kriterium 27 nennt eine Überschneidung mit Kriterium 34; der Hinweis zu Kriterium 30 sagt „Kriterium 31 regelt ausdrücklich die Ausnahmegenehmigung". Die Ausnahmegenehmigung steht in Kriterium 27, die Überschneidung von 27 besteht mit 30; Kriterium 31 regelt die Freigabe der Umsetzungsplanung.
3. Kapitel 2.11 verlangt für temporär nicht erfüllte SOLLTE-Anforderungen eine „Restrisikobetrachtung", Kapitel 4.1.2 sagt „Eine temporäre Nichterfüllung löst keine Risikobetrachtung aus"; beide Begriffe sind nicht definiert.
4. Der Absatz „Durch eine Zuordnung der Zielobjektkategorien auf die Assets ergeben sich die zu erfüllenden Anforderungen. [...]" steht doppelt, am Ende von 3.4.1 und am Anfang von 3.4.2 (S. 16).
5. Satz ohne Prädikat (S. 19): „Die temporäre Nichterfüllung mit einer stichhaltigen Begründung zu dokumentieren."
6. Schreibfehler: „Kapiteln 4, und 5" (S. 6); „Welche externen Partner oder Dienstleister vom ISMS berücksichtig werden?" (S. 7); „mit Ihnen kann" statt „mit ihnen" (S. 14); „gewährleisteten" (S. 22); „Informationssicherheitsrisken" (S. 23); „sollten mindestens für folgende Aspekte berücksichtigt werden" (S. 23); „Netzte" (S. 29); „Messangeranwendungen" (S. 32); „Prozessschritt Evaluation" für einen Teilschritt (S. 27).

## Erhebungsmethode

Skriptgestützt über die JSON-Dateien des Commits 160c177: Diff des Builds 2026-10-22 gegen den Build 2026-08-26 (keine IDs hinzu oder entfallen; Änderungen an GC.12.1, PERF.2.1 und 24 Kernel-Controls), Auszählung `sec_level` × Modalverb im Kernel (69 MUSS, 608 SOLLTE, 224 KANN; davon „erhöht": 224 KANN, 3 SOLLTE), Kernel-Controls ohne `target_object_categories` (265 von 901), Kategorienamen aus Props und Namespace (je 39), Import-Auswahl aus `Grundschutz++-profile.json` (vier von zehn RISK-Controls). Standard-Zitate aus dem PDF-Text der Version 1.0 mit Seitenangabe; die Abbildungen 1 und 6 (PDCA-Zuordnung, Hierarchie der Zielobjektkategorien) wurden nicht ausgewertet.
