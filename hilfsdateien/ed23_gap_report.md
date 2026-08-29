# ED23-Lücken-Kreuzanalyse: Welche Anforderungen der Edition 2023 deckt Grundschutz++ nicht ab?

*Generiert am 2026-08-29 von `Gpp-ai-tool/scripts/analyze_ed23_coverage.py` (Repo-Stand ee9cf89). Deterministisch reproduzierbar, siehe Abschnitt 9.*

## 1. Kernaussage

Das offizielle IT-Grundschutz-Kompendium Edition 2023 enthält 1.834 aktive Anforderungen in 111 Bausteinen (zuzüglich 290 entfallene). 227 davon (12,4 %) haben im GS++→ED23-Mapping (5.145 verifizierte Zuordnungen, amtliche Satz-Nummerierung) keine Maßnahme, die auf sie zeigt; nach dem BSI-eigenen GSMap-Mapping sind es 1.324 (72,2 %). Über alle drei Quellen zusammen (unser Mapping, BSI-GSMap, Prozessbaustein-Mapping) bleiben 139 Anforderungen (7,6 %) ohne jede Zuordnung. Gegenüber dem ungeprüften Erststand (5.521 Zuordnungen) deckt der aktuelle Stand 1.607 statt 1.306 Anforderungen ab (94 verloren, 395 hinzugekommen). Die satzgenaue Beurteilung jedes normativen Satzes des amtlichen Wortlauts gegen den GS++-Katalog (LLM-Maker-Checker) ergibt: 3.615 von 6.611 normativen Teilanforderungen (54,7 %) sind durch mindestens eine GS++-Maßnahme abgedeckt; 273 Anforderungen haben keinen einzigen abgedeckten normativen Satz. In der Gegenrichtung haben 133 von 1.000 GS++-Maßnahmen keine ED23-Entsprechung.

## 2. Fragestellung und Quellen

Gap-Analyse in der Gegenrichtung: nicht „wohin zeigt jede GS++-Maßnahme?“, sondern „auf welche ED23-Anforderung zeigt *keine* Maßnahme?“ — die Frage aus Handbuch-Kapitel 10.5 (Punkt 3) bzw. Anhang D12.

| Quelle | Richtung | Umfang | Methode | Pin |
|---|---|---|---|---|
| Offizielles BSI-XML-Kompendium 2023 | (Nenner) | 1.834 aktive + 290 entfallene Anforderungen | amtlicher Wortlaut | sha256 `dd41a7467464…` |
| Unser Mapping (`gpp_ed23_anforderungen.json`) | GS++ → ED23 | 5.145 Maps, 867 Maßnahmen, 1.607 Ziele | LLM Maker-Checker, status draft | Repo `ee9cf89` |
| BSI GSMap (`ITGS-to-GS++-mapping_collection.json`) | ED23-UA → GS++ | 1.185 Maps, 824 Teilanforderungen | menschlich (GSMap-Tool) | Commit `8f0bcd1fbb4f…` |
| Prozessbaustein-Mapping | ED23 → GS++ (1:1) | 687 Einträge, nur ISMS/ORP/CON/OPS/DER | LLM, vollständigkeitsgetrieben | Repo `ee9cf89` |
| GS++-Katalog (resolved) | (Universum) | 1.000 Maßnahmen | — | Commit `36a0fac473c6…` |
| Satz-Beurteilung (`ed23_satz_abdeckung.json`) | ED23-Satz → GS++ | 1.834 Anforderungen, 4.600 verifizierte Zuordnungen | LLM Maker-Checker (gemini-3-flash-preview / gemini-3.7-flash), amtliches XML | Repo `ee9cf89` |

## 3. Methode und Ehrlichkeitsgrenzen

- Ebene (a): Nenner sind die aktiven Anforderungen des offiziellen BSI-XML-Kompendiums 2023; ENTFALLEN-Anforderungen werden separat gezählt.
- Ebene (b) ours: Teilanforderung = Satz-Index (statement-sentence) in der AMTLICHEN Satz-Nummerierung des XML-Wortlauts (seit dem XML-Umbau der Mapping-Erstellung; keine Paraphrase mehr beteiligt).
- Ebene (b) ITGS: Das UA-Universum des BSI-GSMap-Mappings ist unveröffentlicht; max. beobachteter UA-Index je Anforderung dient als Untergrenze, ungemappte Indizes darunter sind beweisbare Lücken.
- Normativ = Satz mit MUSS/MÜSSEN/DARF/DÜRFEN/SOLLTE/SOLLTEN in Großschreibung; KANN/KÖNNEN wird separat gezählt.
- Ebene (d): Jeder normative Satz des amtlichen Wortlauts wurde einzeln gegen den vollständigen GS++-Katalog beurteilt (großzügige Kandidatensuche je Anforderung, danach strenge Einzelprüfung jedes (Satz, Maßnahme)-Paars mit den Praktik-Nachbarn als Negativkontext). Ein Satz ohne verifizierte Maßnahme wurde also GESEHEN und trotzdem leer beurteilt — das ist ein inhaltliches Urteil, keine bloße Mapping-Lücke. Es bleibt ein LLM-Urteil im Status draft.
- Eine fehlende Zuordnung ist zunächst eine **Mapping-Lücke**, keine bewiesene inhaltliche Lücke von Grundschutz++: unser Mapping ist automatisiert erzeugt (status: draft), das BSI-Mapping deckt erklärtermaßen nur einen Ausschnitt ab. Wo aber *beide* unabhängigen Verfahren nichts finden, ist die Lücke ein starkes Signal.

## 4. Ergebnisse auf Anforderungsebene

| | abgedeckt | ohne Zuordnung | Anteil ohne |
|---|---|---|---|
| Unser Mapping (3.046er) | 1.607 | 227 | 12,4 % |
| BSI GSMap | 510 | 1.324 | 72,2 % |
| Prozessbaustein-Mapping | 558 | 1.276 | 69,6 % |
| **mindestens eine Quelle** | **1.695** | **139** | **7,6 %** |

Kreuztabelle unser Mapping × BSI GSMap (aktive Anforderungen):

| | GSMap: ja | GSMap: nein |
|---|---|---|
| **Unser Mapping: ja** | 475 | 1.132 |
| **Unser Mapping: nein** | 35 | 192 |

Nach Verbindlichkeit (Titel-Suffix im offiziellen XML):

| Level | aktiv | ohne jede Zuordnung | ohne unser Mapping | ohne GSMap |
|---|---|---|---|---|
| Basis (B) | 563 | 22 (3,9 %) | 43 | 392 |
| erhöht (H) | 404 | 54 (13,4 %) | 74 | 289 |
| Standard (S) | 867 | 63 (7,3 %) | 110 | 643 |

Nach Schicht:

| Schicht | aktiv | ohne jede Zuordnung | ohne unser Mapping | ohne GSMap |
|---|---|---|---|---|
| APP | 301 | 38 (12,6 %) | 48 | 205 |
| CON | 114 | 0 (0,0 %) | 11 | 87 |
| DER | 128 | 0 (0,0 %) | 16 | 75 |
| IND | 69 | 10 (14,5 %) | 11 | 43 |
| INF | 219 | 33 (15,1 %) | 33 | 192 |
| ISMS | 16 | 0 (0,0 %) | 2 | 4 |
| NET | 227 | 15 (6,6 %) | 25 | 117 |
| OPS | 246 | 0 (0,0 %) | 32 | 175 |
| ORP | 54 | 0 (0,0 %) | 2 | 41 |
| SYS | 460 | 43 (9,3 %) | 47 | 385 |

Top-20-Bausteine nach Anforderungen ohne jede Zuordnung:

| Baustein | aktiv | ohne jede Zuordnung |
|---|---|---|
| APP.4.6 | 22 | 7 (31,8 %) |
| INF.14 | 30 | 7 (23,3 %) |
| INF.11 | 17 | 6 (35,3 %) |
| APP.4.4 | 21 | 6 (28,6 %) |
| SYS.1.6 | 26 | 6 (23,1 %) |
| APP.3.6 | 20 | 5 (25,0 %) |
| INF.13 | 30 | 5 (16,7 %) |
| SYS.2.6 | 16 | 4 (25,0 %) |
| APP.2.2 | 17 | 4 (23,5 %) |
| SYS.1.5 | 26 | 4 (15,4 %) |
| NET.1.1 | 36 | 4 (11,1 %) |
| APP.2.3 | 9 | 3 (33,3 %) |
| APP.5.2 | 10 | 3 (30,0 %) |
| SYS.3.2.3 | 13 | 3 (23,1 %) |
| IND.3.2 | 14 | 3 (21,4 %) |
| INF.12 | 17 | 3 (17,6 %) |
| SYS.2.2.3 | 21 | 3 (14,3 %) |
| SYS.1.9 | 22 | 3 (13,6 %) |
| INF.5 | 25 | 3 (12,0 %) |
| INF.1 | 31 | 3 (9,7 %) |

### 4.1 Vergleich mit dem Vor-Review-Stand (5.521 → 5.145 Zuordnungen)

Der ungeprüfte Erststand (Commit `d188329`, 5.521 Zuordnungen) deckte 1.306 der 1.834 aktiven Anforderungen ab, der aktuelle Stand 1.607. 94 Anforderungen verloren gegenüber damals ihre letzte Zuordnung, 395 kamen hinzu — die vollständigen ID-Listen stehen in `ed23_gap_analyse.json` unter `summary.vergleich_5521_vs_3046`.

## 5. Ergebnisse auf Teilanforderungsebene

**Unser Mapping (amtliche Satz-Nummerierung):** 6.643 Sätze in den aktiven offiziellen Anforderungen, davon 3.813 von mindestens einer Zuordnung referenziert und 2.830 (42,6 %) ohne Referenz.

**BSI GSMap (UA-Ebene):** 824 Unteranforderungen gemappt. Das UA-Universum ist unveröffentlicht; aus den maximal beobachteten Indizes ergibt sich eine Untergrenze von 1.430 UAs in den berührten Anforderungen — darunter 606 beweisbar ungemappte (Index kleiner als ein gemappter Nachbar).

**Normative Teilanforderungen des amtlichen Wortlauts:** Das XML enthält 6.611 normative Sätze (MUSS/SOLLTE/DARF, zzgl. 0 KANN-Sätze). Unser Mapping referenziert davon 3.810 direkt (57,6 %) — seit dem XML-Umbau eine exakte Zählung in derselben Nummerierung, kein Alignment mehr nötig.

### 5.1 Beurteilte Satz-Abdeckung (amtlicher Wortlaut, je Teilanforderung)

Jeder der 6.611 normativen Sätze der 1.834 beurteilten Anforderungen wurde einzeln gegen den GS++-Katalog geprüft: **3.615 abgedeckt (54,7 %), 2.996 ohne jede GS++-Maßnahme (45,3 %).** 273 Anforderungen haben keinen einzigen abgedeckten normativen Satz (Anhang B).

| Level | normative Sätze | abgedeckt | ohne Abdeckung |
|---|---|---|---|
| Basis (B) | 2.400 | 1.359 (56,6 %) | 1.041 |
| erhöht (H) | 1.081 | 585 (54,1 %) | 496 |
| Standard (S) | 3.130 | 1.671 (53,4 %) | 1.459 |

| Schicht | normative Sätze | abgedeckt | ohne Abdeckung |
|---|---|---|---|
| APP | 1.074 | 588 (54,7 %) | 486 |
| CON | 458 | 233 (50,9 %) | 225 |
| DER | 538 | 272 (50,6 %) | 266 |
| IND | 217 | 118 (54,4 %) | 99 |
| INF | 869 | 440 (50,6 %) | 429 |
| ISMS | 84 | 53 (63,1 %) | 31 |
| NET | 777 | 444 (57,1 %) | 333 |
| OPS | 916 | 488 (53,3 %) | 428 |
| ORP | 218 | 144 (66,1 %) | 74 |
| SYS | 1.460 | 835 (57,2 %) | 625 |

Top-20-Bausteine nach unabgedeckten normativen Sätzen:

| Baustein | normative Sätze | ohne Abdeckung |
|---|---|---|
| INF.14 | 135 | 74 (54,8 %) |
| INF.13 | 134 | 67 (50,0 %) |
| INF.2 | 126 | 65 (51,6 %) |
| SYS.1.7 | 133 | 65 (48,9 %) |
| OPS.1.1.1 | 123 | 62 (50,4 %) |
| NET.1.1 | 124 | 60 (48,4 %) |
| CON.11.1 | 86 | 55 (64,0 %) |
| DER.3.1 | 100 | 54 (54,0 %) |
| NET.3.4 | 109 | 54 (49,5 %) |
| DER.2.1 | 121 | 51 (42,1 %) |
| INF.12 | 81 | 51 (63,0 %) |
| APP.4.2 | 124 | 50 (40,3 %) |
| DER.3.2 | 82 | 46 (56,1 %) |
| NET.1.2 | 83 | 45 (54,2 %) |
| SYS.1.1 | 91 | 44 (48,4 %) |
| SYS.2.1 | 122 | 44 (36,1 %) |
| INF.1 | 99 | 42 (42,4 %) |
| SYS.1.6 | 75 | 42 (56,0 %) |
| SYS.1.8 | 90 | 42 (46,7 %) |
| INF.11 | 69 | 41 (59,4 %) |

Quervergleich mit Ebene (a): 46 Anforderungen sind in unserem Mapping abgedeckt, überstehen die satzgenaue Prüfung aber mit null Sätzen; umgekehrt findet die Satz-Beurteilung bei 0 Anforderungen Substanz, auf die kein einziges Mapping zeigt. Beide ID-Listen stehen im JSON unter `summary.teilanforderungen.beurteilt`.

### 5.2 Deterministischer Zerlegungs-Vergleich der Teilanforderungs-Indizes

Bei 475 Anforderungen tragen beide Mappings Teilanforderungs-Indizes (unsere `statement-sentence` in amtlicher Satz-Nummerierung vs. BSI-`UA.n`). Mengenvergleich der Indizes: 109 identisch (22,9 %), 310 überlappend (65,3 %), 56 disjunkt (11,8 %). Das UA-Schema des GSMap ist unveröffentlicht — Index-Gleichheit bleibt ein Strukturindiz, keine bewiesene inhaltliche Übereinstimmung. Bei 2 Anforderungen übersteigt die UA-Untergrenze die Zahl der normativen amtlichen Sätze. Vollständige ID-Listen im JSON unter `summary.teilanforderungen.zerlegungsvergleich`.

**Relationstypen:** Unser Mapping: equal-to 15, equivalent-to 125, intersects-with 1.093, subset-of 809, superset-of 3.103. BSI GSMap: equal-to 21, equivalent-to 118, intersects-with 395, subset-of 464, superset-of 187. Achtung Leserichtung: Unser Mapping beschreibt die GS++-Maßnahme relativ zur ED23-Anforderung, das GSMap die ED23-Unteranforderung relativ zur GS++-Maßnahme — subset-of und superset-of sind beim Vergleich zu spiegeln.

**Deutung (Befund, LLM-klassifiziert, Status draft):** 3.103 der 5.145 Zuordnungen (60,3 %) sind superset-of: Wo Grundschutz++ eine ED23-Anforderung überhaupt abdeckt, deckt es sie überwiegend als die allgemeinere Fassung ab — das WAS der Anforderung überlebt, die technologiespezifische Ausprägung (das WIE) hat im Katalog keinen eigenen Träger mehr. Wörtliche Übernahmen sind mit 15× equal-to die absolute Ausnahme. Zusammen mit Abschnitt 4 (die Anforderungen ohne jede Zuordnung konzentrieren sich in den produktspezifischen SYS-, APP-, INF- und NET-Bausteinen, während die Prozess-Schichten vollständig abgedeckt sind) ergibt sich: Der Übergang auf Grundschutz++ generalisiert das Kompendiumswissen; die produktspezifischen Festlegungen der Edition 2023 sind im veröffentlichten GS++-Bestand ohne Nachfolger. Konzeptionell ist dieses Wissen in die Stand-der-Technik-Bibliothek verlagert; dort liegen derzeit WLAN, Mindeststandard-TLS, Lieferkettensicherheit und Risikomanagement — produktspezifische Inhalte im Umfang der 111 ED23-Bausteine existieren dort nicht.

## 6. Gegenrichtung: GS++-Maßnahmen ohne ED23-Entsprechung

| Quelle | GS++-Maßnahmen ohne Treffer (von 1.000) |
|---|---|
| Unser Mapping | 133 |
| BSI GSMap | 678 |
| Prozessbaustein-Mapping | 684 |
| **in keiner der drei Quellen** | **100** |

Verteilung der 133 Maßnahmen ohne Treffer in unserem Mapping nach Praktik-Gruppe: ARCH 5, ASST 5, BER 18, BES 16, DET 17, DEV 3, DLS 2, GC 6, GEB 10, KONF 11, NOT 6, PERF 2, PERS 1, REA 2, RISK 3, SENS 13, STM 8, TEST 2, UMS 1, VRB 2. Vollständige Listen in `ed23_gap_analyse.json` unter `forward_gaps`.

## 7. Einordnung: Migrationsfolgen und Bürokratiekosten

**Bewertung der Autoren, aus den Messwerten dieses Reports abgeleitet:**

Ein gepflegter Grundschutz-Check trägt Umsetzungsstatus und Nachweise zu den 1.834 aktiven Anforderungen; dazu kommen Sicherheitskonzepte, Verträge und Zertifikatsauflagen, die wörtlich auf Kompendiums-IDs verweisen. Für den Übertrag dieser Arbeit nach Grundschutz++ ist die amtliche Brücke das GSMap-Mapping — und das deckt 510 Anforderungen (27,8 %); allein 392 der 563 Basis-Anforderungen bleiben dort ohne Zuordnung, das UA-Zerlegungsschema ist unveröffentlicht, und der Status ist draft. Was die amtliche Brücke nicht trägt, ist beim Umstieg neu zu erbringen: Neuzuordnung von Nachweisen von Hand, Anforderung für Anforderung, in jeder Institution einzeln — ein Community-Draft wie das hier vermessene Gegen-Mapping ersetzt gegenüber Auditoren keine amtliche Tabelle, so vollständig es auch ist. Diese Bürokratiekosten entstehen an der fehlenden Brücke; der neue Standard selbst kann nichts dafür.

Dazu kommt der Substanzverlust aus Abschnitt 5.2: Das technologiespezifische WIE der 111 Bausteine hat im veröffentlichten GS++-Bestand keinen Träger, und die als Ersatzort vorgesehenen Stand-der-Technik-Kataloge decken diesen Umfang bisher nicht. Konsequenz aus beidem: Mapping und WIE-Kataloge gehören als Pflichtartefakte zu jedem Katalog-Release — sonst bezahlt jede Institution die fehlende Brücke einzeln, mit eigener Arbeitszeit.

## 8. Kreuzbefunde zwischen den Quellen

- Ziel-Klassen unseres Mappings: {"official": 1607}. NTT-eigene (nicht-amtliche) Ziele: 0, Ziele auf ENTFALLENE Anforderungen: 0, dangling: 0.
- Quell-Klassen des BSI GSMap: {"official": 510}; ENTFALLEN-gemappt: 0, dangling: 0.
- Veraltete GS++-Ziel-IDs im BSI GSMap (existieren im gepinnten GS++-Katalog nicht): 17 — DET.3.1.13, GC.6.1.1, GC.6.1.2, GC.6.1.3, GC.8.1.1, GC.8.1.1.1, GC.8.1.2, GC.9.1.3, KONF.11.9, KONF.2.5.1.1, PERF.5.1.4, PERF.5.1.9, PERF.5.2, TEST.4.1.1.1, UMS.3.2, UMS.4.2, VRB.1.2.
- Prozessbaustein-Mapping: 53 dangling Quellen, 0 außerhalb der Prozess-Schichten, 0 dangling GS++-Ziele.
- satz_nr außerhalb des Satzbereichs: 0; Duplikate: 0 (unser Mapping) / 0 (GSMap).
- Level-Widersprüche Titel vs. Abschnitt im XML: 0.
- Satz-Nummerierung Beurteilung vs. XML abweichend: 0.
- Amtliche Anforderungen ohne Eintrag im stripped-Korpus: 290 — APP.1.1.A1, APP.1.1.A4, APP.1.1.A5, APP.1.1.A7, APP.1.1.A8, APP.1.1.A9, APP.1.2.A4, APP.1.2.A5, APP.1.2.A8, APP.1.4.A10, APP.1.4.A11, APP.1.4.A13, APP.1.4.A2, APP.1.4.A4, APP.1.4.A6, APP.1.4.A9, APP.2.1.A10, APP.2.1.A4, APP.2.1.A7, APP.2.2.A10, APP.2.2.A11, APP.2.2.A13, APP.2.2.A14, APP.2.2.A2, APP.2.2.A4, APP.2.3.A12, APP.2.3.A13, APP.2.3.A2, APP.2.3.A7, APP.3.1.A10, APP.3.1.A13, APP.3.1.A15, APP.3.1.A16, APP.3.1.A17, APP.3.1.A18, APP.3.1.A19, APP.3.1.A2, APP.3.1.A23, APP.3.1.A24, APP.3.1.A25, APP.3.1.A3, APP.3.1.A5, APP.3.1.A6, APP.3.2.A17, APP.3.2.A19, APP.3.2.A6, APP.3.3.A1, APP.3.3.A10, APP.3.3.A4, APP.3.3.A5, APP.3.4.A11, APP.3.4.A14, APP.3.6.A12, APP.3.6.A5, APP.4.2.A10, APP.4.2.A21, APP.4.3.A10, APP.4.3.A14, APP.4.3.A15, APP.4.3.A2, APP.4.3.A5, APP.4.3.A6, APP.4.3.A7, APP.4.3.A8, APP.5.2.A13, APP.5.2.A14, APP.5.2.A15, APP.5.2.A16, APP.5.2.A18, APP.5.2.A19, APP.5.2.A4, APP.5.2.A6, APP.5.2.A8, CON.1.A12, CON.1.A13, CON.1.A14, CON.1.A3, CON.1.A6, CON.1.A7, CON.1.A8, CON.3.A10, CON.3.A11, CON.3.A3, CON.3.A8, CON.6.A10, CON.6.A3, CON.6.A5, CON.6.A6, CON.6.A7, CON.6.A9, CON.8.A13, CON.8.A15, CON.8.A4, CON.8.A9, DER.1.A8, DER.3.1.A28, DER.3.2.A23, DER.4.A11, IND.1.A2, IND.2.1.A10, IND.2.1.A12, IND.2.1.A14, IND.2.1.A15, IND.2.1.A3, IND.2.1.A5, IND.2.1.A9, IND.2.2.A2, INF.1.A11, INF.1.A21, INF.1.A28, INF.1.A29, INF.1.A33, INF.10.A10, INF.10.A2, INF.2.A18, INF.2.A20, INF.2.A27, INF.5.A21, INF.7.A4, ISMS.1.A14, NET.1.2.A19, NET.1.2.A20, NET.1.2.A23, NET.1.2.A3, NET.1.2.A34, NET.1.2.A4, NET.1.2.A5, NET.3.1.A2, NET.3.1.A3, NET.3.2.A11, NET.3.2.A12, NET.3.2.A13, NET.3.2.A5, NET.4.1.A3, NET.4.1.A4, NET.4.2.A10, NET.4.2.A2, NET.4.2.A6, NET.4.3.A5, OPS.1.1.2.A1, OPS.1.1.2.A10, OPS.1.1.2.A12, OPS.1.1.2.A13, OPS.1.1.2.A14, OPS.1.1.2.A15, OPS.1.1.2.A20, OPS.1.1.2.A3, OPS.1.1.2.A9, OPS.1.1.3.A16, OPS.1.1.3.A4, OPS.1.1.4.A15, OPS.1.1.4.A4, OPS.1.1.4.A8, OPS.1.1.5.A2, OPS.1.1.5.A7, OPS.1.1.6.A8, OPS.1.1.6.A9, OPS.1.2.4.A3, OPS.1.2.4.A4, OPS.1.2.5.A11, OPS.1.2.5.A12, OPS.1.2.5.A13, OPS.1.2.5.A15, OPS.1.2.5.A16, OPS.1.2.5.A18, OPS.1.2.5.A23, OPS.1.2.5.A4, ORP.1.A10, ORP.1.A11, ORP.1.A12, ORP.1.A14, ORP.1.A5, ORP.1.A6, ORP.1.A7, ORP.1.A9, ORP.2.A10, ORP.2.A11, ORP.2.A12, ORP.2.A6, ORP.2.A8, ORP.2.A9, ORP.3.A2, ORP.3.A5, ORP.5.A10, ORP.5.A11, ORP.5.A3, ORP.5.A6, ORP.5.A7, ORP.5.A9, SYS.1.1.A14, SYS.1.1.A17, SYS.1.1.A18, SYS.1.1.A20, SYS.1.1.A26, SYS.1.1.A29, SYS.1.1.A3, SYS.1.1.A32, SYS.1.1.A4, SYS.1.1.A7, SYS.1.1.A8, SYS.1.2.2.A10, SYS.1.2.2.A13, SYS.1.2.2.A7, SYS.1.2.2.A9, SYS.1.3.A1, SYS.1.3.A11, SYS.1.3.A12, SYS.1.3.A13, SYS.1.3.A15, SYS.1.3.A7, SYS.1.3.A9, SYS.1.5.A1, SYS.1.5.A18, SYS.1.7.A10, SYS.1.7.A12, SYS.1.7.A13, SYS.1.7.A15, SYS.1.8.A12, SYS.1.8.A3, SYS.1.8.A5, SYS.2.1.A12, SYS.2.1.A14, SYS.2.1.A17, SYS.2.1.A19, SYS.2.1.A2, SYS.2.1.A22, SYS.2.1.A25, SYS.2.1.A4, SYS.2.1.A5, SYS.2.1.A7, SYS.2.2.3.A10, SYS.2.2.3.A11, SYS.2.2.3.A3, SYS.2.2.3.A7, SYS.2.2.3.A8, SYS.2.3.A10, SYS.2.3.A13, SYS.2.3.A16, SYS.2.3.A3, SYS.3.1.A2, SYS.3.1.A4, SYS.3.1.A5, SYS.3.2.1.A14, SYS.3.2.1.A15, SYS.3.2.1.A17, SYS.3.2.1.A20, SYS.3.2.1.A21, SYS.3.2.1.A23, SYS.3.2.1.A24, SYS.3.2.2.A10, SYS.3.2.2.A11, SYS.3.2.2.A13, SYS.3.2.2.A15, SYS.3.2.2.A16, SYS.3.2.2.A18, SYS.3.2.2.A8, SYS.3.2.2.A9, SYS.3.2.3.A10, SYS.3.2.3.A11, SYS.3.2.3.A16, SYS.3.2.3.A19, SYS.3.2.3.A20, SYS.3.2.3.A22, SYS.3.2.3.A24, SYS.3.2.3.A27, SYS.3.2.3.A3, SYS.3.2.3.A4, SYS.3.2.3.A5, SYS.3.2.3.A6, SYS.3.2.3.A8, SYS.3.2.3.A9, SYS.3.2.4.A1, SYS.3.2.4.A4, SYS.3.2.4.A6, SYS.3.2.4.A7, SYS.4.1.A10, SYS.4.1.A12, SYS.4.1.A13, SYS.4.1.A19, SYS.4.1.A3, SYS.4.1.A6, SYS.4.1.A8, SYS.4.1.A9, SYS.4.4.A12, SYS.4.4.A14, SYS.4.4.A3, SYS.4.4.A4, SYS.4.5.A3, SYS.4.5.A8, SYS.4.5.A9.
- NTT-eigene Bausteine im Korpus (nicht Teil des amtlichen Kompendiums): 0 — keine.
- NTT-eigene Zusatz-Anforderungen innerhalb amtlicher Bausteine: 0.
- Alle dokumentierten Anker-Zahlen (Handbuch 10.3, Release Notes 4.0) wurden reproduziert.

## 9. Reproduktion

```bash
uv run Gpp-ai-tool/scripts/analyze_ed23_coverage.py --date 2026-08-29
```

Alle Fremdquellen sind commit- bzw. sha256-gepinnt (siehe Konstanten im Script und `meta.sources` im JSON); Downloads landen im gitignorierten Cache `Gpp-ai-tool/.cache/ed23_gap/`. Gleicher `--date`-Wert ⇒ byte-identische Ausgaben.

Die Satz-Beurteilung (Abschnitt 5.1) stammt aus dem AI-Pipeline-Lauf `python src/main.py --stage stage_ed23_satz_abdeckung` (Gpp-ai-tool, benötigt Vertex-AI-Zugang); sie ist als LLM-Lauf nicht byte-reproduzierbar, ihr Ergebnis liegt versioniert in `hilfsdateien/ed23_satz_abdeckung.json`.

## Anhang A: Aktive Anforderungen ohne jede Zuordnung

139 Anforderungen, gruppiert nach Baustein:

- **APP.1.1** (2): APP.1.1.A14, APP.1.1.A6
- **APP.2.1** (2): APP.2.1.A21, APP.2.1.A8
- **APP.2.2** (4): APP.2.2.A15, APP.2.2.A20, APP.2.2.A21, APP.2.2.A6
- **APP.2.3** (3): APP.2.3.A4, APP.2.3.A5, APP.2.3.A9
- **APP.3.3** (1): APP.3.3.A2
- **APP.3.4** (1): APP.3.4.A4
- **APP.3.6** (5): APP.3.6.A10, APP.3.6.A14, APP.3.6.A19, APP.3.6.A21, APP.3.6.A22
- **APP.4.2** (1): APP.4.2.A23
- **APP.4.3** (1): APP.4.3.A21
- **APP.4.4** (6): APP.4.4.A11, APP.4.4.A16, APP.4.4.A17, APP.4.4.A19, APP.4.4.A21, APP.4.4.A6
- **APP.4.6** (7): APP.4.6.A17, APP.4.6.A2, APP.4.6.A21, APP.4.6.A3, APP.4.6.A4, APP.4.6.A7, APP.4.6.A9
- **APP.5.2** (3): APP.5.2.A1, APP.5.2.A10, APP.5.2.A2
- **APP.5.4** (1): APP.5.4.A10
- **APP.7** (1): APP.7.A8
- **IND.1** (1): IND.1.A3
- **IND.2.1** (2): IND.2.1.A13, IND.2.1.A7
- **IND.2.3** (1): IND.2.3.A1
- **IND.2.4** (1): IND.2.4.A2
- **IND.2.7** (2): IND.2.7.A11, IND.2.7.A9
- **IND.3.2** (3): IND.3.2.A10, IND.3.2.A13, IND.3.2.A14
- **INF.1** (3): INF.1.A10, INF.1.A31, INF.1.A32
- **INF.10** (1): INF.10.A4
- **INF.11** (6): INF.11.A12, INF.11.A13, INF.11.A15, INF.11.A16, INF.11.A8, INF.11.A9
- **INF.12** (3): INF.12.A16, INF.12.A8, INF.12.A9
- **INF.13** (5): INF.13.A10, INF.13.A14, INF.13.A27, INF.13.A29, INF.13.A7
- **INF.14** (7): INF.14.A10, INF.14.A20, INF.14.A21, INF.14.A22, INF.14.A23, INF.14.A30, INF.14.A9
- **INF.2** (2): INF.2.A22, INF.2.A29
- **INF.5** (3): INF.5.A11, INF.5.A26, INF.5.A5
- **INF.7** (2): INF.7.A1, INF.7.A3
- **INF.9** (1): INF.9.A7
- **NET.1.1** (4): NET.1.1.A26, NET.1.1.A27, NET.1.1.A36, NET.1.1.A9
- **NET.1.2** (3): NET.1.2.A16, NET.1.2.A2, NET.1.2.A31
- **NET.2.1** (1): NET.2.1.A15
- **NET.3.1** (1): NET.3.1.A27
- **NET.3.2** (2): NET.3.2.A26, NET.3.2.A30
- **NET.3.3** (1): NET.3.3.A13
- **NET.3.4** (2): NET.3.4.A2, NET.3.4.A5
- **NET.4.2** (1): NET.4.2.A13
- **SYS.1.1** (2): SYS.1.1.A38, SYS.1.1.A9
- **SYS.1.2.2** (1): SYS.1.2.2.A14
- **SYS.1.2.3** (1): SYS.1.2.3.A8
- **SYS.1.3** (1): SYS.1.3.A6
- **SYS.1.5** (4): SYS.1.5.A13, SYS.1.5.A24, SYS.1.5.A25, SYS.1.5.A26
- **SYS.1.6** (6): SYS.1.6.A1, SYS.1.6.A10, SYS.1.6.A12, SYS.1.6.A23, SYS.1.6.A25, SYS.1.6.A7
- **SYS.1.7** (3): SYS.1.7.A27, SYS.1.7.A34, SYS.1.7.A36
- **SYS.1.8** (2): SYS.1.8.A10, SYS.1.8.A21
- **SYS.1.9** (3): SYS.1.9.A16, SYS.1.9.A18, SYS.1.9.A20
- **SYS.2.1** (2): SYS.2.1.A37, SYS.2.1.A9
- **SYS.2.2.3** (3): SYS.2.2.3.A24, SYS.2.2.3.A25, SYS.2.2.3.A26
- **SYS.2.4** (1): SYS.2.4.A6
- **SYS.2.5** (1): SYS.2.5.A11
- **SYS.2.6** (4): SYS.2.6.A13, SYS.2.6.A3, SYS.2.6.A5, SYS.2.6.A7
- **SYS.3.2.1** (2): SYS.3.2.1.A27, SYS.3.2.1.A31
- **SYS.3.2.3** (3): SYS.3.2.3.A18, SYS.3.2.3.A2, SYS.3.2.3.A26
- **SYS.3.3** (1): SYS.3.3.A9
- **SYS.4.3** (2): SYS.4.3.A17, SYS.4.3.A5
- **SYS.4.4** (1): SYS.4.4.A23

## Anhang B: Anforderungen ohne einen einzigen beurteilt abgedeckten normativen Satz

273 Anforderungen, gruppiert nach Baustein:

- **APP.1.1** (2): APP.1.1.A14, APP.1.1.A6
- **APP.1.2** (1): APP.1.2.A12
- **APP.1.4** (5): APP.1.4.A1, APP.1.4.A12, APP.1.4.A14, APP.1.4.A16, APP.1.4.A3
- **APP.2.1** (2): APP.2.1.A21, APP.2.1.A8
- **APP.2.2** (4): APP.2.2.A15, APP.2.2.A20, APP.2.2.A21, APP.2.2.A6
- **APP.2.3** (3): APP.2.3.A4, APP.2.3.A5, APP.2.3.A9
- **APP.3.3** (2): APP.3.3.A14, APP.3.3.A2
- **APP.3.4** (1): APP.3.4.A4
- **APP.3.6** (5): APP.3.6.A10, APP.3.6.A14, APP.3.6.A19, APP.3.6.A21, APP.3.6.A22
- **APP.4.2** (1): APP.4.2.A23
- **APP.4.3** (3): APP.4.3.A11, APP.4.3.A17, APP.4.3.A21
- **APP.4.4** (7): APP.4.4.A11, APP.4.4.A16, APP.4.4.A17, APP.4.4.A19, APP.4.4.A2, APP.4.4.A21, APP.4.4.A6
- **APP.4.6** (9): APP.4.6.A17, APP.4.6.A2, APP.4.6.A20, APP.4.6.A21, APP.4.6.A3, APP.4.6.A4, APP.4.6.A6, APP.4.6.A7, APP.4.6.A9
- **APP.5.2** (3): APP.5.2.A1, APP.5.2.A10, APP.5.2.A2
- **APP.5.4** (1): APP.5.4.A10
- **APP.6** (1): APP.6.A7
- **APP.7** (3): APP.7.A3, APP.7.A4, APP.7.A8
- **CON.1** (4): CON.1.A15, CON.1.A16, CON.1.A17, CON.1.A19
- **CON.10** (1): CON.10.A2
- **CON.11.1** (3): CON.11.1.A17, CON.11.1.A3, CON.11.1.A9
- **CON.3** (2): CON.3.A1, CON.3.A4
- **CON.7** (2): CON.7.A18, CON.7.A3
- **CON.8** (2): CON.8.A18, CON.8.A21
- **CON.9** (2): CON.9.A6, CON.9.A7
- **DER.2.2** (5): DER.2.2.A1, DER.2.2.A14, DER.2.2.A5, DER.2.2.A7, DER.2.2.A8
- **DER.2.3** (1): DER.2.3.A6
- **DER.3.1** (3): DER.3.1.A12, DER.3.1.A18, DER.3.1.A21
- **DER.3.2** (6): DER.3.2.A11, DER.3.2.A13, DER.3.2.A18, DER.3.2.A19, DER.3.2.A20, DER.3.2.A3
- **DER.4** (5): DER.4.A16, DER.4.A2, DER.4.A3, DER.4.A6, DER.4.A9
- **IND.1** (1): IND.1.A3
- **IND.2.1** (2): IND.2.1.A13, IND.2.1.A7
- **IND.2.3** (1): IND.2.3.A1
- **IND.2.4** (1): IND.2.4.A2
- **IND.2.7** (2): IND.2.7.A11, IND.2.7.A9
- **IND.3.2** (4): IND.3.2.A10, IND.3.2.A13, IND.3.2.A14, IND.3.2.A5
- **INF.1** (4): INF.1.A10, INF.1.A31, INF.1.A32, INF.1.A36
- **INF.10** (1): INF.10.A4
- **INF.11** (6): INF.11.A12, INF.11.A13, INF.11.A15, INF.11.A16, INF.11.A8, INF.11.A9
- **INF.12** (4): INF.12.A16, INF.12.A5, INF.12.A8, INF.12.A9
- **INF.13** (5): INF.13.A10, INF.13.A14, INF.13.A27, INF.13.A29, INF.13.A7
- **INF.14** (7): INF.14.A10, INF.14.A20, INF.14.A21, INF.14.A22, INF.14.A23, INF.14.A30, INF.14.A9
- **INF.2** (2): INF.2.A22, INF.2.A29
- **INF.5** (3): INF.5.A11, INF.5.A26, INF.5.A5
- **INF.7** (3): INF.7.A1, INF.7.A3, INF.7.A5
- **INF.9** (2): INF.9.A12, INF.9.A7
- **ISMS.1** (2): ISMS.1.A16, ISMS.1.A17
- **NET.1.1** (8): NET.1.1.A24, NET.1.1.A25, NET.1.1.A26, NET.1.1.A27, NET.1.1.A29, NET.1.1.A32, NET.1.1.A36, NET.1.1.A9
- **NET.1.2** (7): NET.1.2.A13, NET.1.2.A15, NET.1.2.A16, NET.1.2.A2, NET.1.2.A28, NET.1.2.A29, NET.1.2.A31
- **NET.2.1** (2): NET.2.1.A15, NET.2.1.A17
- **NET.3.1** (1): NET.3.1.A27
- **NET.3.2** (3): NET.3.2.A25, NET.3.2.A26, NET.3.2.A30
- **NET.3.3** (3): NET.3.3.A10, NET.3.3.A13, NET.3.3.A7
- **NET.3.4** (3): NET.3.4.A1, NET.3.4.A2, NET.3.4.A5
- **NET.4.2** (2): NET.4.2.A13, NET.4.2.A4
- **OPS.1.1.1** (3): OPS.1.1.1.A11, OPS.1.1.1.A24, OPS.1.1.1.A3
- **OPS.1.1.2** (3): OPS.1.1.2.A17, OPS.1.1.2.A2, OPS.1.1.2.A25
- **OPS.1.1.3** (2): OPS.1.1.3.A14, OPS.1.1.3.A3
- **OPS.1.1.4** (2): OPS.1.1.4.A1, OPS.1.1.4.A3
- **OPS.1.1.5** (3): OPS.1.1.5.A10, OPS.1.1.5.A13, OPS.1.1.5.A9
- **OPS.1.1.6** (1): OPS.1.1.6.A6
- **OPS.1.1.7** (5): OPS.1.1.7.A10, OPS.1.1.7.A13, OPS.1.1.7.A2, OPS.1.1.7.A8, OPS.1.1.7.A9
- **OPS.1.2.2** (7): OPS.1.2.2.A1, OPS.1.2.2.A14, OPS.1.2.2.A15, OPS.1.2.2.A21, OPS.1.2.2.A4, OPS.1.2.2.A5, OPS.1.2.2.A9
- **OPS.1.2.4** (1): OPS.1.2.4.A6
- **OPS.1.2.5** (3): OPS.1.2.5.A1, OPS.1.2.5.A2, OPS.1.2.5.A6
- **OPS.1.2.6** (5): OPS.1.2.6.A11, OPS.1.2.6.A5, OPS.1.2.6.A6, OPS.1.2.6.A7, OPS.1.2.6.A8
- **OPS.2.2** (1): OPS.2.2.A7
- **OPS.2.3** (2): OPS.2.3.A12, OPS.2.3.A18
- **OPS.3.2** (2): OPS.3.2.A21, OPS.3.2.A9
- **ORP.1** (2): ORP.1.A13, ORP.1.A2
- **ORP.2** (1): ORP.2.A5
- **ORP.4** (3): ORP.4.A14, ORP.4.A17, ORP.4.A4
- **SYS.1.1** (3): SYS.1.1.A12, SYS.1.1.A38, SYS.1.1.A9
- **SYS.1.2.2** (1): SYS.1.2.2.A14
- **SYS.1.2.3** (1): SYS.1.2.3.A8
- **SYS.1.3** (1): SYS.1.3.A6
- **SYS.1.5** (5): SYS.1.5.A13, SYS.1.5.A23, SYS.1.5.A24, SYS.1.5.A25, SYS.1.5.A26
- **SYS.1.6** (8): SYS.1.6.A1, SYS.1.6.A10, SYS.1.6.A11, SYS.1.6.A12, SYS.1.6.A15, SYS.1.6.A23, SYS.1.6.A25, SYS.1.6.A7
- **SYS.1.7** (3): SYS.1.7.A27, SYS.1.7.A34, SYS.1.7.A36
- **SYS.1.8** (2): SYS.1.8.A10, SYS.1.8.A21
- **SYS.1.9** (3): SYS.1.9.A16, SYS.1.9.A18, SYS.1.9.A20
- **SYS.2.1** (2): SYS.2.1.A37, SYS.2.1.A9
- **SYS.2.2.3** (3): SYS.2.2.3.A24, SYS.2.2.3.A25, SYS.2.2.3.A26
- **SYS.2.3** (2): SYS.2.3.A4, SYS.2.3.A9
- **SYS.2.4** (1): SYS.2.4.A6
- **SYS.2.5** (4): SYS.2.5.A10, SYS.2.5.A11, SYS.2.5.A16, SYS.2.5.A4
- **SYS.2.6** (4): SYS.2.6.A13, SYS.2.6.A3, SYS.2.6.A5, SYS.2.6.A7
- **SYS.3.1** (1): SYS.3.1.A10
- **SYS.3.2.1** (3): SYS.3.2.1.A27, SYS.3.2.1.A31, SYS.3.2.1.A5
- **SYS.3.2.2** (3): SYS.3.2.2.A1, SYS.3.2.2.A14, SYS.3.2.2.A17
- **SYS.3.2.3** (3): SYS.3.2.3.A18, SYS.3.2.3.A2, SYS.3.2.3.A26
- **SYS.3.3** (1): SYS.3.3.A9
- **SYS.4.3** (4): SYS.4.3.A15, SYS.4.3.A17, SYS.4.3.A18, SYS.4.3.A5
- **SYS.4.4** (1): SYS.4.4.A23
