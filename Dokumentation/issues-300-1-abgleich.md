# Issues, die der BSI-Standard 300-1 erledigt oder beantwortet

**Stand: 2026-10-26** · Grundlage: BSI-Standard 300-1 „Methodik Grundschutz++" (Version 1.0 vom 20.10.2026, Seitenangaben nach PDF), Abgleich `abgleich-bsi-standard-300-1_v0.2.md`, Katalog-Build 2026-10-22 (Repo-Commit 160c177). Recherche lesend mit `gh` (Konto Christoph-Puppe-Work); nichts ausgeführt.

Urteile: **(a)** durch den Standard entschieden, **(b)** durch die angekündigte Katalogänderung erledigt, im Build 2026-10-22 noch nicht enthalten, **(c)** nicht betroffen. Regel: eigene Issues schließen, fremde kommentieren. Eigene Konten: Christoph-Puppe-Work, christoph-puppe. Der Platzhalter `https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek/issues/116` steht für das neue Sammel-Issue zu den Katalogabweichungen.

**Ausgeführt am 2026-10-26:** Sammel-Issue angelegt als https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek/issues/116. Geschlossen mit Kommentar: BSI #96, #81, #78, #32 (Konto Christoph-Puppe-Work), #106, #47 (Konto christoph-puppe). Kommentiert: BSI #95, #27; AG-1 #74, #71, #64. Nicht ausgeführt (optional): BSI #77, #53, BSI-Audit-AI #193. Nachtrag 26.10.: #81 wieder geöffnet (Datei `bsi-81-reopen.md`), weil die Pflichtaufnahme kategorieloser Anforderungen die Frage der Prozessmodellierung nicht beantwortet. Dazu Nachtrag in #116 unter A.2 (Datei `bsi-116-a2.md`, https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek/issues/116#issuecomment-6427868754).

## 1. Geprüfte Issues und Discussions

### 1.1 NTT-Data-Deutschland-SE/Grundschutz-Plus-Plus-Tools (1 offen, 20 geschlossen)

| Nr. | Titel | Autor | unser/fremd | Urteil | Aktion |
|---|---|---|---|---|---|
| #47 | Verweis auf Sätze in ED23 aus dem G++ Mapping | christoph-puppe | unser | (c) Mapping-Datenformat, vom Standard nicht berührt | keine |

Die 20 geschlossenen Issues wurden gesichtet (Werkzeugthemen, Mapping-QS); keines wird durch den Standard wieder relevant.

### 1.2 BSI-Bund/Stand-der-Technik-Bibliothek (52 offen, 28 geschlossen, 1 Discussion)

| Nr. | Titel | Autor | unser/fremd | Urteil | Aktion |
|---|---|---|---|---|---|
| #114 | GitHub Pages deployment | codikyo | fremd | (c) Bereitstellungsfrage | keine |
| #113 | Profil-Parameter nicht in result/result_specification | dfurater | fremd | (c) Auflösungstechnik | keine |
| #111 | Zielobjektkategorie „Externe Netzanschlüsse" hat keinen Typ | ManuelHaas | fremd | (c) Anhang 1 des Standards kennt keine Typ-Spalte; Namespace-Fund bleibt | keine |
| #110 | Laufzeit-Artefakte fehlen | Christoph-Puppe-Work | unser | (c) Standard verlangt Statusberichte (4.5, S. 21) und Tool-Nachweise (4.3, S. 20), aber kein Format | keine |
| #109 | REA.2.6.1 / REA.2.6.2.1 ohne guidance | ManuelHaas | fremd | (c) | keine |
| #107 | Implementation Layer: Component Definitions nicht auflösbar | christoph-puppe | unser | (c) | keine |
| #106 | Gruppenbildung von Assets nicht geregelt | christoph-puppe | unser | (a) Kapitel 3.2, S. 13: „ist eine Gruppierung möglich"; (b) STM.2.1.2 ff. im Build unverändert | schließen mit Kommentar (Konto christoph-puppe) |
| #104 | effort_level 0 kodiert Verbindlichkeit | Christoph-Puppe-Work | unser | (c) Standard nennt Aufwand nur als Priorisierungskriterium (4.3, S. 20) | keine |
| #103 | Gewichtungs-Prop weight und Scoring | Christoph-Puppe-Work | unser | (c) Priorisierung bleibt frei (4.3, S. 20) | keine |
| #101 | implemented-requirement.control-id trägt alt-identifier | dfurater | fremd | (c) | keine |
| #100 | control-implementation.source nicht auflösbar | dfurater | fremd | (c) | keine |
| #99 | Unfertige Artefakte im main-Branch | Christoph-Puppe-Work | unser | (c) Standard setzt Versionen voraus (3.3, S. 14), entscheidet aber nichts zur Publikation | keine |
| #98 | ITGS-zu-GS++-Mapping Abdeckung | Christoph-Puppe-Work | unser | (c) | keine |
| #96 | Binärer Umsetzungsstatus verschenkt OSCAL-Werte | Christoph-Puppe-Work | unser | (a) 4.1.1, S. 18: drei Werte inkl. „nicht anwendbar"; 4.1.2: temporär/dauerhaft; „teilweise" und „alternative" nicht übernommen; (b) UMS.1.1-Guidance im Build unverändert | schließen mit Kommentar |
| #95 | „nicht umgesetzt" in OSCAL nicht abbildbar; Upstream | Christoph-Puppe-Work | unser | (b) teilweise: Standard bestätigt den dritten Zustand „dauerhaft nicht erfüllt" (4.1.2, S. 19); Interims-Token bleibt offen | kommentieren, offen lassen |
| #92 | Planned repository history rewrite | sdt-publication-bot | fremd | (c) | keine |
| #85 | scope_*-Props im OSCAL-Namespace | dfurater | fremd | (c) | keine |
| #84 | Resolved Catalogs ohne Resolution-Provenienz | christoph-puppe | unser | (c) | keine |
| #83 | MD5 als Hash-Algo | christoph-puppe | unser | (c) | keine |
| #82 | Zuweisung „IT-Produkte" nicht geregelt | Christoph-Puppe-Work | unser | (c) Anhang 1 behält die Definition, keine Zuweisungsregel (3.4.2, S. 16 f.) | keine |
| #81 | Modellierung von Prozessen: 265 Controls ohne Kategorie | Christoph-Puppe-Work | unser | (a) 3.4 und 3.4.1, S. 15 f.: verpflichtend aufnehmen, Nichtanwendbarkeit im Status (4.1.1); (b) STM.2.1.5-Guidance im Build unverändert; die Pflichtaufnahme löst die Prozessfrage nicht (DEV: 25 Controls über „Anwendungen", 9 kategorielos) | geschlossen und am 26.10. wieder geöffnet, Kommentar in Abschnitt 3 |
| #80 | 36 von 95 Methodik-Controls ohne documentation-Prop | Christoph-Puppe-Work | unser | (c) Standard macht keine Aussage zu Props | keine |
| #79 | CONTRIBUTING.md: AG-Forks archiviert | Christoph-Puppe-Work | unser | (c) | keine |
| #78 | RISK.1.9 nicht im Anwenderkatalog, Restrisiko nur SOLLTE | Christoph-Puppe-Work | unser | (a) 2.11, S. 11; 4.1.1, S. 18; Kriterium 30, S. 38: Restrisiko-Pflicht mit Leitungsfreigabe; (b) UMS.1.2 SOLLTE, RISK.1.9 nicht importiert | schließen mit Kommentar |
| #77 | GC.6.1 Abgrenzung des Geltungsbereiches | Christoph-Puppe-Work | unser | (c) Standard verlangt Dokumentation der Schnittstellen (3.1, S. 13), keine wirksame Barriere; Begriff „Anwendungsbereich" | kommentieren, offen lassen (optional) |
| #73 | Updated Changelog Vorschlag | Christoph-Puppe-Work | unser | (c) | keine |
| #71 | Lieferkettensicherheit: links-Objekte statt Arrays | dfurater | fremd | (c) | keine |
| #70 | GA-Lotse: unzulässiges remarks-Feld | dfurater | fremd | (c) | keine |
| #68 | QA-Felder in Mapping-Provenienz | dfurater | fremd | (c) | keine |
| #66 | Gedanken zu den neuen PRs | christoph-puppe | unser | (c) | keine |
| #61 | Mapping source ISMS.1.A10-UA.7 nicht vorhanden | Stephan-Huettinger | fremd | (c) | keine |
| #60 | Vollkonvertierungs-Experiment | christoph-puppe | unser | (c) | keine |
| #59 | UUID↔ID in Mapping-Dateien | Stephan-Huettinger | fremd | (c) | keine |
| #58 | Erweiterungs-Vokabular als Metaschema-Constraints | Christoph-Puppe-Work | unser | (c) | keine |
| #57 | Instabile ns-URIs | Christoph-Puppe-Work | unser | (c) | keine |
| #56 | Mehrwertige Angaben als kommaseparierte Strings | Christoph-Puppe-Work | unser | (c) | keine |
| #55 | Identische Control-IDs Anwenderkatalog / Mindeststandard-TLS | Christoph-Puppe-Work | unser | (c) | keine |
| #53 | Releases? | Christoph-Puppe-Work | unser | (c) gestärkt: 3.3, S. 14 verlangt Dokumentation der Blaupausen-Version; 5.5, S. 25 Validierung gegen Bibliotheksänderungen | kommentieren, offen lassen (optional) |
| #49 | Kodierung und Formatierung der CSV-Inhalte | Ste-Ri | fremd | (c) | keine |
| #47 | Maßnahme ist erhöht und SOLL | christoph-puppe | unser | (a) 3.4.2, S. 17: „erhöht" beinhaltet KANN; im Build verletzen noch BES.1.4, DET.4.12.1, REA.2.5 die Regel | schließen mit Kommentar (Konto christoph-puppe) |
| #46 | documentation_guidelines mögliche Dublette | sdierkes | fremd | (c) | keine |
| #45 | UTF-8-Bindestriche im Kernel | sdierkes | fremd | (c) | keine |
| #44 | Mismatch documentation-Werte / Namespace | dfurater | fremd | (c) | keine |
| #41 | Assessment methods und Control objectives? | Christoph-Puppe-Work | unser | (c) kein Prüfschema im Standard | keine |
| #39 | Versionierung | Christoph-Puppe-Work | unser | (c) siehe #53 | keine |
| #38 | Neue UUID | Christoph-Puppe-Work | unser | (c) | keine |
| #37 | Stufe 0 | LarsSaenger | fremd | (c) Standard schweigt zu effort_level | keine |
| #32 | Zielobjekt „ISMS"? | Christoph-Puppe-Work | unser | (a) 3.4, S. 15 und 3.4.1, S. 16: Methodik gilt für den ganzen Informationsverbund, kategorielose Anforderungen verpflichtend | schließen mit Kommentar |
| #31 | Typo in PDCA-Grafik der OSCAL-Doku | ljrk0 | fremd | (c) | keine |
| #27 | „Vorbereitende Aufgaben" des Basis Phasenmodells | LarsSaenger | fremd | (a) teilweise: 2.5, S. 8; 3.1, S. 13; Anhang 2, S. 34 f. nennen die Vorbereitungsquellen; Blaupausen in 3.3 | kommentieren |
| #20 | Prüfmechanismus Katalog-Updates | juergenpabel | fremd | (c) | keine |
| #1 | Disclaimer zu Issues & Discussions | FriedsamDario | fremd | (c) | keine |
| D#2 | Discussion: Disclaimer (einzige Discussion) | FriedsamDario | fremd | (c) | keine |

Geschlossene Issues (28) gesichtet; #75 (GC.7-Tippfehler), #74, #76 sind erledigt, kein Wiederaufleben durch den Standard.

### 1.3 AG-1-Sicherheitskuration/Stand-der-Technik-Bibliothek-Fork-AG-1 (20 offen; BSI-Mitarbeiter @ChrisWeissenborn antwortet dort)

| Nr. | Titel | Autor | unser/fremd | Urteil | Aktion |
|---|---|---|---|---|---|
| #77 | Sicherheitskonzept pro eingesetzter Technologie fehlt | Christoph-Puppe-Work | unser | (c) Standard fordert kein Technologie-Konzept | keine |
| #76 | Dokumentationsanforderungen | MarkusAlbertFITKO | fremd | (c) | keine |
| #75 | Muster Verfahren und Regelungen erzeugt 29 Nachweise | MarkusAlbertFITKO | fremd | (c) | keine |
| #74 | Überwachung bezeichnet Angriffserkennung und Managementbewertung | MarkusAlbertFITKO | fremd | (a) Standard verwendet „Überwachung" für Prozessschritt 4 (Kap. 5, S. 22) und „Monitoring" für die technischen Verfahren (5.4, S. 24 f.) | kommentieren |
| #73 | Begriff Autorisierung bezeichnet drei Vorgänge | MarkusAlbertFITKO | fremd | (c) | keine |
| #72 | Kryptografische Vorgaben verstreut | MarkusAlbertFITKO | fremd | (c) | keine |
| #71 | Risikomethodik in GC.12.1 und RISK.1.1 doppelt? | MarkusAlbertFITKO | fremd | (a) teilweise: 2.11, S. 11 und Anhang 3; Import-Lücke RISK.1.2 ff.; GC.12.1 im Build parametrisiert, Dokument „Risikobetrachtung" | kommentieren |
| #70, #69, #68 | Implementierungsbeschreibungen (WLAN, Netzarchitektur, Passwortrichtlinie) | HansVedderOBK | fremd | (c) | keine |
| #67 | isms # PERF | MarkusAlbertFITKO | fremd | (c) nicht gelesen im Detail; Begriffsfrage in #74 behandelt | keine |
| #66 | Org # BES | MarkusAlbertFITKO | fremd | (c) | keine |
| #65 | isms # VRB | MarkusAlbertFITKO | fremd | (c) | keine |
| #64 | isms # UMS | MarkusAlbertFITKO | fremd | (a) offene Frage „Status in 4 Stufen vs Ja/Nein" durch 4.1.1, S. 18 beantwortet | kommentieren |
| #63 | isms # STM | MarkusAlbertFITKO | fremd | (c) offene Fragen betreffen Werkzeuge und Rollen | keine |
| #62 | isms # GC | MarkusAlbertFITKO | fremd | (c) | keine |
| #60 | Verantwortlichkeiten | MarkusAlbertFITKO | fremd | (c) Standard 2.8 legt keine Rollenprops fest; BSI-Antwort liegt vor | keine |
| #58, #57, #56 | Mindeststandard TLS | MarkusAlbertFITKO | fremd | (c) | keine |

### 1.4 Weitere Fundstellen

| Repo / Nr. | Titel | Autor | unser/fremd | Urteil | Aktion |
|---|---|---|---|---|---|
| AG-3-Nutzergenerierte-Inhalte/Stand-der-Technik-Bibliothek#6 | Praxisbeispiel für die Anwendung des Grundschutz++ | hapela | fremd | (c) | keine |
| Stand-der-Technik/Qualitaetssicherung#201 | UMS.2.1 Irreführende Vereinfachung im Guidance-Text | Christoph-Puppe-Work | unser | (a) durch 4.1.1 entschieden, Repo ist archiviert (read-only) | keine möglich |
| Stand-der-Technik/Praxisbeispiele#5, Massnahmenplaene#9, Nutzerprofile#6, Threat-Modeling#4 | Vorarbeiten 2025 | LarsSaenger u. a. | fremd | (c) alle Repos der Organisation archiviert | keine möglich |
| Christoph-Puppe-Work/BSI-Audit-AI#193 | UMS.2.1 Irreführende Vereinfachung im Guidance-Text | Christoph-Puppe-Work | unser | (a) 4.1.1, S. 18: drei Werte, kein „teilweise" | schließen mit Kommentar (optional, eigenes Repo) |
| bsi-community/Stand-der-Technik-Viewer | nur #1 „Mapping JSON", geschlossen; keine Discussions | KQBC54C4IJ | fremd | (c) | keine |
| BSI-Bund/Stand-der-Technik-Radar | keine Issues | – | – | – | keine |
| usnistgov/OSCAL#2272 | not-implemented als implementation-status | Christoph-Puppe-Work | unser | nur erwähnt: OSCAL-Thema, vom Standard nicht berührt; PR #2273 in develop gemerged | keine |
| eclipse-fennec/common.models#54, #55; intuitem/ciso-assistant-community#2866; sig-bsi-grundschutz/RH-GSplusplus#6; chicagoist/BSI.AzCompliance (Bot-Issues); SamuelBlickle/grundschutz-mcp#64 (Bot) | Fremdprojekte, die GS++ verwenden | diverse | fremd | (c) nicht betroffen; #54 nutzt die Zielobjektkategorien, könnte Anhang 1 interessieren | keine |

GitHub-weite Suchen: „Grundschutz++" (50 Treffer, überwiegend Schülerprojekte und Bot-Issues), „GS++" (0), „Stand-der-Technik-Bibliothek" (33), „Umsetzungsstatus" (11), „Zielobjektkategorie" (9), „Risikobetrachtung" (4), „Anwenderkatalog" und „Grundschutz Plus Plus" ohne neue Treffer.

## 2. Zusammenfassung der Aktionen

| Aktion | Issues |
|---|---|
| Schließen mit Kommentar (unsere) | BSI #106, #96, #81, #78, #47, #32; optional BSI-Audit-AI #193 |
| Kommentieren, offen lassen (unsere) | BSI #95; optional #77, #53 |
| Kommentieren (fremde) | BSI #27; AG-1 #74, #71, #64 |

Konten: #106 und #47 wurden mit `christoph-puppe` eröffnet; Schließen geht nur mit diesem Konto (`gh auth switch --user christoph-puppe`, danach zurück). Alle übrigen mit `Christoph-Puppe-Work`.

## 3. Kommentartexte

Die Texte liegen zusätzlich als Dateien unter `C:\Users\micro\AppData\Local\Temp\claude\C--Users-micro-Documents-DEV-Projects-Claude-Working-Grundschutz-Plus-Plus-Tools\00b7c1a2-cf7f-4164-8051-c9e1daf7fc70\scratchpad\issue-comments\`.

### BSI #106 (schließen, Datei `bsi-106.md`)

Der BSI-Standard 300-1 „Methodik Grundschutz++" (Version 1.0 vom 20.10.2026) beantwortet die Frage. Kapitel 3.2 „Erfassung der Assets" (S. 13): „Ähneln sich die Eigenschaften und der Einsatzzweck von Assets, ist eine Gruppierung möglich." Die Gruppenbildung ist damit wieder zulässig; die Kriterienliste aus 200-2 Kapitel 8.1.1 übernimmt der Standard nicht, die beiden Merkmale „Eigenschaften" und „Einsatzzweck" treten an ihre Stelle. Der Katalog-Build vom 22.10.2026 enthält noch keine Änderung an STM.2.1.2 bis STM.2.1.4.2; das BSI hat angekündigt, den Anwenderkatalog an den Standard anzupassen. Die erwarteten Katalogänderungen sind in https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek/issues/116 gesammelt. Ich schließe das Issue.

### BSI #96 (schließen, Datei `bsi-96.md`)

Der BSI-Standard 300-1 (Version 1.0 vom 20.10.2026) hat das Statusmodell entschieden. Kapitel 4.1.1 (S. 18): „Der Umsetzungsstatus einer Anforderung kann sein: ‚erfüllt' (‚ja'), ‚nicht erfüllt' (‚nein'), ‚nicht anwendbar'", mit Begründungspflicht für jede nicht anwendbare Anforderung. Kapitel 4.1.2 (S. 18 f.) unterscheidet bei SOLLTE-Anforderungen die temporäre von der dauerhaften Nichterfüllung; für MUSS-Anforderungen gilt: „Eine Ausnahmegenehmigung oder Risikoakzeptanz ist nicht möglich" (S. 19). Von den hier vorgeschlagenen Werten ist `not-applicable` übernommen, und die temporäre Nichterfüllung entspricht fachlich `planned`. `partial` und `alternative` übernimmt der Standard nicht; der binäre Audit-Befund bleibt. Die Guidance zu UMS.1.1 im Build vom 22.10.2026 nennt weiterhin zwei Werte; die Anpassung des Anwenderkatalogs hat das BSI angekündigt, die erwarteten Änderungen sind in https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek/issues/116 gesammelt. Die Abbildung der drei Statuswerte und der temporären und dauerhaften Nichterfüllung auf OSCAL bleibt Gegenstand von #95. Ich schließe dieses Issue.

### BSI #95 (kommentieren, offen lassen, Datei `bsi-95.md`)

Stand nach dem BSI-Standard 300-1 (Version 1.0 vom 20.10.2026): Der Standard bestätigt den Zustand, den OSCAL nicht ausdrücken kann. Kapitel 4.1.2 (S. 19): „Eine dauerhafte Nichterfüllung liegt vor, wenn die Anforderung auf absehbare Zeit oder endgültig nicht erfüllt wird." Daneben stehen „nicht anwendbar" mit Begründung (4.1.1, S. 18) und die temporäre Nichterfüllung mit vorgesehenem Zeitpunkt (4.1.2, S. 19). Abbildung auf die OSCAL-Werte: temporär nicht erfüllt entspricht `planned`, nicht anwendbar entspricht `not-applicable`, dauerhaft nicht erfüllt braucht `not-implemented`. Der Upstream-PR usnistgov/OSCAL#2273 ist in `develop` gemerged und in keinem Release. Punkt 2 dieses Issues, eine Interims-Festlegung des Tokens für dauerhaft nicht erfüllte Anforderungen, bleibt offen und wird mit dem Standard dringender, weil jedes Werkzeug den dritten Zustand jetzt speichern muss. Die erwarteten Katalogänderungen zum Statusmodell sind in https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek/issues/116 gesammelt.

### BSI #81 (schließen, Datei `bsi-81.md`)

Der BSI-Standard 300-1 (Version 1.0 vom 20.10.2026) regelt den Weg der kategorielosen Anforderungen ins Anforderungspaket. Kapitel 3.4 (S. 15) unterscheidet drei Arten von Anforderungen: Methodik-Anforderungen, die „auf den gesamten Informationsverbund anzuwenden" sind; Anforderungen der technischen und organisatorischen Praktiken ohne Zielobjektkategorie, die „verpflichtend in das Anforderungspaket aufzunehmen" sind; Anforderungen mit Zielobjektkategorie, die über die Zuordnung der Assets greifen. Kapitel 3.4.1 (S. 16) wiederholt: „Alle weiteren Anforderungen ohne zugewiesene Zielobjektkategorie sind verpflichtend in das Anforderungspaket aufzunehmen." Nichtanwendbarkeit wird erst beim Umsetzungsstatus festgestellt, mit Begründung (4.1.1, S. 18). Die Relevanzentscheidung mit Streichung aus der Guidance zu STM.2.1.5 steht damit im Widerspruch zum Standard; der Build vom 22.10.2026 enthält sie unverändert, die Anpassung des Anwenderkatalogs hat das BSI angekündigt. Eine Prozess-Wurzel im Namespace führt der Standard nicht ein; die Zuordnung an Geschäftsprozesse bleibt Sache der Guidance. Nachverfolgung in https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek/issues/116. Ich schließe das Issue.

### BSI #78 (schließen, Datei `bsi-78.md`)

Der BSI-Standard 300-1 (Version 1.0 vom 20.10.2026) macht die Restrisiko-Übernahme zur Pflicht. Kapitel 2.11 (S. 11): „Für SOLLTE-Anforderungen, die in der Umsetzungsplanung enthalten, aber noch nicht erfüllt sind, muss eine Restrisikobetrachtung durchgeführt werden. Das identifizierte Risiko muss durch die Institutionsleitung freigegeben werden." Kapitel 4.1.1 (S. 18): „Das durch die nicht erfüllte Anforderung bestehende Risiko muss von der Institutionsleitung getragen werden." Anhang 3, Mindestkriterium 30 (S. 38): „Die nach der Risikobehandlung verbleibenden Risiken (Restrisiken) sind durch die Institutionsleitung zu autorisieren." Der Widerspruch zum Auditierungsschema ist damit aufgelöst, in Richtung der Pflicht. Im Katalog-Build vom 22.10.2026 ist UMS.1.2 weiterhin SOLLTE und RISK.1.9 weiterhin nicht importiert; das BSI hat die Anpassung des Anwenderkatalogs angekündigt. Nachverfolgung in https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek/issues/116. Ich schließe das Issue.

### BSI #47 (schließen, Konto christoph-puppe, Datei `bsi-47.md`)

Der BSI-Standard 300-1 (Version 1.0 vom 20.10.2026) legt in Kapitel 3.4.2 (S. 17) fest: „Anforderungen mit dem Sicherheitsniveau ‚erhöht' beinhalten das Modalverb ‚KANN' und sind optional zu erfüllen." KONF.7.3 ist inzwischen korrigiert. Im Build vom 22.10.2026 verletzen noch drei Controls die Regel: BES.1.4 (Outsourcing-Strategie), DET.4.12.1 (Auslastung des Netzes) und REA.2.5 (IT-Forensik), alle drei mit `sec_level` erhöht und SOLLTE. Die drei sind in https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek/issues/116 aufgeführt. Ich schließe dieses Issue.

### BSI #32 (schließen, Datei `bsi-32.md`)

Der BSI-Standard 300-1 (Version 1.0 vom 20.10.2026) beantwortet beide Fragen. Zum Zielobjekt „ISMS": Kapitel 3.4 (S. 15) ordnet die Methodik-Anforderungen keiner Zielobjektkategorie zu, sie „sind auf den gesamten Informationsverbund anzuwenden"; Kapitel 3.4.1 (S. 16): „Die Methodik Anforderungen gelten für alle Institutionen und sind verpflichtend auf jeden Informationsverbund anzuwenden. Ein individuelles Vorgehen ist nicht vorgesehen." Ein Zielobjekt ISMS braucht es dafür nicht. Zur Modellierung der Controls ohne Zielobjektkategorie: „Alle weiteren Anforderungen ohne zugewiesene Zielobjektkategorie sind verpflichtend in das Anforderungspaket aufzunehmen" (3.4.1, S. 16); nicht anwendbare Anforderungen werden beim Umsetzungsstatus mit Begründung als „nicht anwendbar" geführt (4.1.1, S. 18). Das Heraussuchen entfällt, die Begründungspflicht bleibt. Nachverfolgung der Katalogänderungen in https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek/issues/116. Ich schließe das Issue.

### BSI #77 (kommentieren, offen lassen, optional, Datei `bsi-77.md`)

Stand nach dem BSI-Standard 300-1 (Version 1.0 vom 20.10.2026): Der Standard nennt den Geltungsbereich „Anwendungsbereich (Scope)" (Kapitel 2.3, S. 7) und verlangt für die Festlegung die Klärung der formalen, organisatorischen und infrastrukturellen Abgrenzung sowie der externen Partner. Zum Informationsverbund (3.1, S. 13): „Der Informationsverbund stellt die inhaltlich-technische Abbildung des Anwendungsbereichs dar. Der Anwendungsbereich kann einen oder mehrere Informationsverbünde enthalten." Seine Schnittstellen „zu externen Prozessen und Systemen oder anderen Informationsverbünden" sind „eindeutig zu dokumentieren – organisatorisch, technisch sowie infrastrukturell". Eine wirksame Barriere an der Grenze verlangt auch der Standard nicht. Die Frage bleibt offen; der Begriffsunterschied Anwendungsbereich (Standard) gegen Geltungsbereich (GC.6.1) ist in https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek/issues/116 vermerkt.

### BSI #53 (kommentieren, offen lassen, optional, Datei `bsi-53.md`)

Der BSI-Standard 300-1 (Version 1.0 vom 20.10.2026) setzt versionierte Artefakte voraus. Kapitel 3.3 (S. 14): „Die Auswahl (inkl. Version), Zuordnung und gegebenenfalls vorgenommene Anpassung der Blaupausen sind nachvollziehbar zu dokumentieren." Kapitel 5.5 (S. 25) verlangt in der Validierung der Anforderungen die Berücksichtigung von „Anpassungen an den Anforderungen in der Stand der Technik Bibliothek", „Anpassungen an verwendeten Blaupausen" und „Änderungen in der Methodik GS++". Ohne Tags oder Releases kann eine Institution die Version einer Blaupause nur über den Commit-SHA angeben. Das Issue bleibt damit aktuell.

### BSI #27 (kommentieren, fremd, Datei `bsi-27.md`)

Der BSI-Standard 300-1 „Methodik Grundschutz++" (Version 1.0 vom 20.10.2026) nimmt einen Teil der hier beschriebenen vorbereitenden Aufgaben in den Prozessschritt 1 auf. Kapitel 2.5 (S. 8) verweist für die Identifizierung der Geschäftsprozesse auf „Prozesslandkarten und bestehende Managementsysteme (z. B. BCMS, DSMS)" und für Behörden auf die gesetzlichen Aufträge; fehlen Prozesslandkarten, gilt die vereinfachte Geschäftsprozessanalyse aus Anhang 2 (S. 34 f.), die als Quellen Organigramme und Geschäftsverteilungspläne, das Verzeichnis von Verarbeitungstätigkeiten, Anwendungs- und Systemübersichten (CMDB), Prozessverzeichnisse, ISMS-Tools sowie Vertrags- und Dienstleisterübersichten nennt. Kapitel 3.1 (S. 13) erlaubt für die Asset-Erfassung den Rückgriff auf „vorhandene Assetdaten/-register und digitale erfasste Systemdaten". Blaupausen definiert Kapitel 3.3 (S. 14 f.) als vorgefertigte Anforderungskataloge mit vorgegebenen Parametern; Aufgaben außerhalb von Anforderungen sieht der Standard in Blaupausen nicht vor. Eine eigene Anforderung „vorbereitende Aufgaben" enthält weder der Standard noch der Katalog-Build vom 22.10.2026.

### AG-1 #74 (kommentieren, fremd, Datei `ag1-74.md`)

Der BSI-Standard 300-1 „Methodik Grundschutz++" (Version 1.0 vom 20.10.2026) legt die Begriffsverwendung selbst fest. Der vierte Prozessschritt heißt „Überwachung" (Kapitel 5, S. 22) und umfasst die Leistungsbewertung des ISMS (5.1), das interne Auditprogramm (5.2), die Managementbewertungen (5.3), die Monitoring-Methoden und -Tools (5.4) und die Validierung der Anforderungen (5.5). „Überwachung" bezeichnet im Standard also die Check-Phase des ISMS, das Gegenstück der Praktik PERF. „Monitoring" steht in 5.4 (S. 24 f.) für die technischen Verfahren, die „verankert werden" müssen: „Ein Verfahren zur Erkennung von Sicherheitsvorfällen", „Ein Verfahren für den Umgang mit Schwachstellen" und „Ein Verfahren für die Erfassung und die Reaktion auf neu auftretende Bedrohungen". Die Kollision der Titel DET.4.1 und PERF.2.1 besteht im Katalog-Build vom 22.10.2026 weiter; PERF.2.1 heißt dort inzwischen „Überprüfung der Einhaltung von Verpflichtungen". Die Abweichungen zwischen Standard und Katalog-Build sind in https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek/issues/116 gesammelt.

### AG-1 #71 (kommentieren, fremd, Datei `ag1-71.md`)

Ergänzung nach dem BSI-Standard 300-1 (Version 1.0 vom 20.10.2026): Der Standard bestätigt die Einordnung von @ChrisWeissenborn und schärft sie. Kapitel 2.11 (S. 11): „Anwenderinnen und Anwender können das Verfahren für die Risikoidentifikation, Risikobewertung und Risikobehandlung selbst wählen, sofern die im Anhang [...] festgelegten verbindlichen Mindestkriterien erfüllt werden." Anhang 3 (S. 36 ff.) enthält 35 Mindestkriterien. Die Kriterien 1 bis 5 und 9 entsprechen GC.12.1, RISK.1.1, RISK.1.3 und RISK.1.5; die Kriterien 6 bis 8 (Bewertungskriterien, Risikoappetit, Akzeptanzkriterien) entsprechen RISK.1.6 bis RISK.1.8, die nicht in den Anwenderkatalog importiert sind. Das Control, das die Mindestkriterien bindet, ist RISK.1.2 („Risikomanagement MUSS die Einhaltung des BSI-Kriterienkatalogs bei der Methodenauswahl anweisen"), ebenfalls nicht importiert. Im Build vom 22.10.2026 ist GC.12.1 außerdem parametrisiert („MUSS {{eine einheitliche Methodik}} für das Informationssicherheitsrisikomanagement [...] verankern") und fordert das Dokument „Risikobetrachtung" statt „Risikobewertung"; die dritte Dokumentbezeichnung aus dem Issue entfällt damit. Die Import-Lücke ist in https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek/issues/116 gemeldet.

### AG-1 #64 (kommentieren, fremd, Datei `ag1-64.md`)

Zur offenen Frage in den Quick Wins („Status pro Anforderung in 4 Stufen ... vs Ja / Nein"): Der BSI-Standard 300-1 (Version 1.0 vom 20.10.2026) legt in Kapitel 4.1.1 (S. 18) drei Werte fest: „‚erfüllt' (‚ja')", „‚nicht erfüllt' (‚nein')" und „‚nicht anwendbar'", letzterer mit Begründungspflicht. Einen Wert „teilweise" gibt es nicht; eine teilweise umgesetzte Anforderung ist „nicht erfüllt". Kapitel 4.1.2 (S. 18 f.) unterscheidet bei nicht erfüllten SOLLTE-Anforderungen die temporäre Nichterfüllung (Erfüllung vorgesehen, Begründung dokumentieren) von der dauerhaften (Risikobetrachtung nach Anhang 3, Mindestkriterium 34). Für MUSS-Anforderungen gilt: „Eine Ausnahmegenehmigung oder Risikoakzeptanz ist nicht möglich" (S. 19). Das Ausnahmen-Formular aus den Quick Wins betrifft damit SOLLTE-Anforderungen und Risiken außerhalb der Akzeptanzkriterien (Mindestkriterium 27). Die Guidance zu UMS.1.1 im Katalog-Build vom 22.10.2026 nennt noch zwei Werte; die Anpassung des Anwenderkatalogs hat das BSI angekündigt.

### BSI-Audit-AI #193 (schließen, optional, Datei `audit-ai-193.md`)

Durch den BSI-Standard 300-1 (Version 1.0 vom 20.10.2026), Kapitel 4.1.1 (S. 18) entschieden: drei Werte „erfüllt", „nicht erfüllt", „nicht anwendbar", kein „teilweise"; temporäre und dauerhafte Nichterfüllung nach Kapitel 4.1.2. Der Fund betrifft die Guidance zu UMS.1.1, nicht UMS.2.1. Geschlossen.

### BSI #81 (wieder geöffnet am 26.10., Datei `bsi-81-reopen.md`)

Wiedereröffnet. Der Standard 300-1 regelt in Kapitel 3.4.1 (S. 16) nur den Weg der kategorielosen Anforderungen ins Anforderungspaket („verpflichtend in das Anforderungspaket aufzunehmen"); die Frage dieses Issues bleibt offen: Welche Prozesse hat ein Informationsverbund, und wie werden die Anforderungen der prozessförmigen Praktiken ausgewählt?

Nachgerechnet am Build 2026-10-22: 265 der 901 Kernel-Controls tragen keine Zielobjektkategorie, darunter REA vollständig (23 von 23), TEST 35 von 36, BER 68 von 92, DET 43 von 82, NOT 25 von 37. Am Beispiel Softwareentwicklung greift keiner der beiden Mechanismen: Von den 34 DEV-Controls hängen 25 an der Kategorie „Anwendungen", die jeder Informationsverbund hat, und 9 tragen keine Kategorie. Ein Verbund ohne eigene Entwicklung bekommt damit alle 34 ins Anforderungspaket und müsste sie nach Kapitel 4.1.1 (S. 18) einzeln mit Begründung als „nicht anwendbar" führen. Dasselbe gilt für Notfallplanung, Vorfallsbehandlung oder Änderungen und Tests, wenn der Prozess außerhalb des Verbunds liegt oder in einem anderen Managementsystem geführt wird.

Der Standard verlagert die Relevanzentscheidung aus der Modellierung (STM.2.1.5) in den Umsetzungsstatus; eine Regel, mit der ein Verbund einen Prozess als nicht vorhanden erklärt, bevor dessen Anforderungen ins Paket fallen, fehlt in beiden. Der Vorschlag bleibt: eine Prozess-Wurzel im Namespace der Zielobjektkategorien oder eine Zuordnung von Praktiken zu Prozessen, sodass die Nichtexistenz eines Prozesses eine einzige begründete Entscheidung ist und nicht 34. Bezug: #116, Punkt A.2.

### BSI #116, Nachtrag zu A.2 (26.10., Datei `bsi-116-a2.md`)

Nachtrag zu A.2: Die Pflichtaufnahme kategorieloser Anforderungen nach Kapitel 3.4.1 (S. 16) löst die Prozessfrage nicht, sie verlagert sie in den Umsetzungsstatus. Ein Informationsverbund ohne eigene Softwareentwicklung bekommt alle 34 DEV-Controls ins Anforderungspaket, 25 über die Kategorie „Anwendungen" und 9 kategorielos, und muss sie nach Kapitel 4.1.1 (S. 18) einzeln als „nicht anwendbar" begründen. Für REA (23 von 23 kategorielos), TEST (35 von 36) und NOT (25 von 37) gilt dasselbe, wenn der Prozess außerhalb des Verbunds liegt oder in einem anderen Managementsystem geführt wird. Der Vorschlag in A.2, die Guidance zu STM.2.1.5 an 3.4.1 anzugleichen, ist deshalb nur die halbe Anpassung. Die fehlende Regel, mit der ein Verbund einen Prozess als nicht vorhanden erklärt, bevor dessen Anforderungen ins Paket fallen, ist in #81 beschrieben; das Issue ist dafür wieder geöffnet.

## 4. Befehle (am 26.10. ausgeführt, ohne die optionalen)

Platzhalter `https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek/issues/116` vorher in allen Dateien ersetzen, zum Beispiel mit `sed -i 's#https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek/issues/116#https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek/issues/NNN#' .../issue-comments/*.md`.

```bash
C="C:/Users/micro/AppData/Local/Temp/claude/C--Users-micro-Documents-DEV-Projects-Claude-Working-Grundschutz-Plus-Plus-Tools/00b7c1a2-cf7f-4164-8051-c9e1daf7fc70/scratchpad/issue-comments"
R="BSI-Bund/Stand-der-Technik-Bibliothek"
A="AG-1-Sicherheitskuration/Stand-der-Technik-Bibliothek-Fork-AG-1"

# Konto Christoph-Puppe-Work (aktiv)
gh auth switch --user Christoph-Puppe-Work
gh issue close 96 --repo "$R" --comment "$(cat "$C/bsi-96.md")"
gh issue close 81 --repo "$R" --comment "$(cat "$C/bsi-81.md")"
gh issue close 78 --repo "$R" --comment "$(cat "$C/bsi-78.md")"
gh issue close 32 --repo "$R" --comment "$(cat "$C/bsi-32.md")"
gh issue comment 95 --repo "$R" --body-file "$C/bsi-95.md"
gh issue comment 27 --repo "$R" --body-file "$C/bsi-27.md"
gh issue comment 74 --repo "$A" --body-file "$C/ag1-74.md"
gh issue comment 71 --repo "$A" --body-file "$C/ag1-71.md"
gh issue comment 64 --repo "$A" --body-file "$C/ag1-64.md"
# optional
gh issue comment 77 --repo "$R" --body-file "$C/bsi-77.md"
gh issue comment 53 --repo "$R" --body-file "$C/bsi-53.md"
gh issue close 193 --repo Christoph-Puppe-Work/BSI-Audit-AI --comment "$(cat "$C/audit-ai-193.md")"

# Konto christoph-puppe (Autor von #106 und #47)
gh auth switch --user christoph-puppe
gh issue close 106 --repo "$R" --comment "$(cat "$C/bsi-106.md")"
gh issue close 47 --repo "$R" --comment "$(cat "$C/bsi-47.md")"
gh auth switch --user Christoph-Puppe-Work
```

## 5. Unsicherheiten

1. Die Zuordnung „temporäre Nichterfüllung entspricht `planned`" (#95, #96) ist Auslegung; der Standard nennt OSCAL nicht.
2. Ob #96 als „entschieden" geschlossen werden soll, obwohl `partial` und `alternative` nicht übernommen wurden, ist eine Ermessensfrage; der Kommentar hält beides fest.
3. #77 und #53 (unsere, Kommentar ohne Schließen) sind optional; sie erzeugen Benachrichtigungen ohne neuen Entscheidungsbedarf.
4. Für AG-1 #67 (PERF) und #62 (GC) wurden die Issue-Texte nicht im Detail gelesen; sie gehören zur selben Serie wie #63/#64 und tragen nach Titel keine vom Standard entschiedene Frage.
5. Abbildung 1 und 6 des Standards waren nicht auswertbar; keine der Aussagen in den Kommentaren stützt sich auf eine Abbildung.
