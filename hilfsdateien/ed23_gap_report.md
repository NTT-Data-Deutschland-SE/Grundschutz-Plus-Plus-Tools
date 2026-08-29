# ED23-Lücken-Kreuzanalyse: Welche Anforderungen der Edition 2023 deckt Grundschutz++ nicht ab?

*Generiert am 2026-08-29 von `Gpp-ai-tool/scripts/analyze_ed23_coverage.py` (Repo-Stand 8fd1e10). Deterministisch reproduzierbar, siehe Abschnitt 8.*

## 1. Kernaussage

Das offizielle IT-Grundschutz-Kompendium Edition 2023 enthält 1.834 aktive Anforderungen in 111 Bausteinen (zuzüglich 290 entfallene). 629 davon (34,3 %) haben im GS++→ED23-Mapping (3.046 Zuordnungen nach der strengen Prüfung) keine Maßnahme, die auf sie zeigt; nach dem BSI-eigenen GSMap-Mapping sind es 1.324 (72,2 %). Über alle drei Quellen zusammen (unser Mapping, BSI-GSMap, Prozessbaustein-Mapping) bleiben 416 Anforderungen (22,7 %) ohne jede Zuordnung. Die strenge Prüfung (5.521 → 3.046 Zuordnungen) hat auf Anforderungsebene 236 Anforderungen ihre letzte Zuordnung gekostet (vorher 1.306, nachher 1.205 abgedeckt); 135 kamen neu hinzu. Auf Teilanforderungsebene (normative Sätze des offiziellen Wortlauts: 6.611) ist die Projektion methodisch unschärfer — Details in Abschnitt 5. In der Gegenrichtung haben 180 von 1.000 GS++-Maßnahmen keine ED23-Entsprechung.

## 2. Fragestellung und Quellen

Gap-Analyse in der Gegenrichtung: nicht „wohin zeigt jede GS++-Maßnahme?“, sondern „auf welche ED23-Anforderung zeigt *keine* Maßnahme?“ — die Frage aus Handbuch-Kapitel 10.5 (Punkt 3) bzw. Anhang D12.

| Quelle | Richtung | Umfang | Methode | Pin |
|---|---|---|---|---|
| Offizielles BSI-XML-Kompendium 2023 | (Nenner) | 1.834 aktive + 290 entfallene Anforderungen | amtlicher Wortlaut | sha256 `dd41a7467464…` |
| Unser Mapping (`gpp_ed23_anforderungen.json`) | GS++ → ED23 | 3.046 Maps, 820 Maßnahmen, 1.329 Ziele | LLM Maker-Checker, status draft | Repo `8fd1e10` |
| BSI GSMap (`ITGS-to-GS++-mapping_collection.json`) | ED23-UA → GS++ | 1.185 Maps, 824 Teilanforderungen | menschlich (GSMap-Tool) | Commit `8f0bcd1fbb4f…` |
| Prozessbaustein-Mapping | ED23 → GS++ (1:1) | 687 Einträge, nur ISMS/ORP/CON/OPS/DER | LLM, vollständigkeitsgetrieben | Repo `8fd1e10` |
| GS++-Katalog (resolved) | (Universum) | 1.000 Maßnahmen | — | Commit `36a0fac473c6…` |

## 3. Methode und Ehrlichkeitsgrenzen

- Ebene (a): Nenner sind die aktiven Anforderungen des offiziellen BSI-XML-Kompendiums 2023; ENTFALLEN-Anforderungen werden separat gezählt.
- Ebene (b) ours: Teilanforderung = Satz-Index (statement-sentence) im stripped-Korpus (NTT-Maturity-Level-3-Paraphrase, nicht BSI-Wortlaut).
- Ebene (b) ITGS: Das UA-Universum des BSI-GSMap-Mappings ist unveröffentlicht; max. beobachteter UA-Index je Anforderung dient als Untergrenze, ungemappte Indizes darunter sind beweisbare Lücken.
- Ebene (c): Projektion der Satz-Abdeckung auf die normativen XML-Sätze via Ähnlichkeits-Alignment (Schwelle 0.5, Fallback 'grob' unter 0.4 bzw. bei Satzzahl-Faktor > 2.0); Headline-Zahlen hängen nie am Alignment.
- Normativ = Satz mit MUSS/MÜSSEN/DARF/DÜRFEN/SOLLTE/SOLLTEN in Großschreibung; KANN/KÖNNEN wird separat gezählt.
- Eine fehlende Zuordnung ist zunächst eine **Mapping-Lücke**, keine bewiesene inhaltliche Lücke von Grundschutz++: unser Mapping ist automatisiert erzeugt (status: draft), das BSI-Mapping deckt erklärtermaßen nur einen Ausschnitt ab. Wo aber *beide* unabhängigen Verfahren nichts finden, ist die Lücke ein starkes Signal.

## 4. Ergebnisse auf Anforderungsebene

| | abgedeckt | ohne Zuordnung | Anteil ohne |
|---|---|---|---|
| Unser Mapping (3.046er) | 1.205 | 629 | 34,3 % |
| BSI GSMap | 510 | 1.324 | 72,2 % |
| Prozessbaustein-Mapping | 558 | 1.276 | 69,6 % |
| **mindestens eine Quelle** | **1.418** | **416** | **22,7 %** |

Kreuztabelle unser Mapping × BSI GSMap (aktive Anforderungen):

| | GSMap: ja | GSMap: nein |
|---|---|---|
| **Unser Mapping: ja** | 397 | 808 |
| **Unser Mapping: nein** | 113 | 516 |

Nach Verbindlichkeit (Titel-Suffix im offiziellen XML):

| Level | aktiv | ohne jede Zuordnung | ohne unser Mapping | ohne GSMap |
|---|---|---|---|---|
| Basis (B) | 563 | 74 (13,1 %) | 113 | 392 |
| erhöht (H) | 404 | 101 (25,0 %) | 164 | 289 |
| Standard (S) | 867 | 241 (27,8 %) | 352 | 643 |

Nach Schicht:

| Schicht | aktiv | ohne jede Zuordnung | ohne unser Mapping | ohne GSMap |
|---|---|---|---|---|
| APP | 301 | 102 (33,9 %) | 125 | 205 |
| CON | 114 | 0 (0,0 %) | 23 | 87 |
| DER | 128 | 0 (0,0 %) | 29 | 75 |
| IND | 69 | 26 (37,7 %) | 38 | 43 |
| INF | 219 | 66 (30,1 %) | 74 | 192 |
| ISMS | 16 | 0 (0,0 %) | 2 | 4 |
| NET | 227 | 56 (24,7 %) | 90 | 117 |
| OPS | 246 | 0 (0,0 %) | 66 | 175 |
| ORP | 54 | 0 (0,0 %) | 1 | 41 |
| SYS | 460 | 166 (36,1 %) | 181 | 385 |

Top-20-Bausteine nach Anforderungen ohne jede Zuordnung:

| Baustein | aktiv | ohne jede Zuordnung |
|---|---|---|
| SYS.1.7 | 34 | 26 (76,5 %) |
| INF.14 | 30 | 17 (56,7 %) |
| INF.13 | 30 | 15 (50,0 %) |
| APP.4.6 | 22 | 13 (59,1 %) |
| APP.4.2 | 30 | 13 (43,3 %) |
| APP.2.1 | 18 | 12 (66,7 %) |
| SYS.1.8 | 23 | 11 (47,8 %) |
| SYS.3.2.3 | 13 | 10 (76,9 %) |
| SYS.2.2.3 | 21 | 10 (47,6 %) |
| SYS.1.5 | 26 | 10 (38,5 %) |
| SYS.1.6 | 26 | 9 (34,6 %) |
| SYS.3.2.1 | 28 | 9 (32,1 %) |
| SYS.2.4 | 12 | 8 (66,7 %) |
| SYS.2.6 | 16 | 8 (50,0 %) |
| APP.2.2 | 17 | 8 (47,1 %) |
| INF.11 | 17 | 8 (47,1 %) |
| APP.5.4 | 18 | 8 (44,4 %) |
| NET.2.1 | 18 | 8 (44,4 %) |
| NET.3.4 | 27 | 8 (29,6 %) |
| INF.1 | 31 | 8 (25,8 %) |

### 4.1 Auswirkung der strengen Prüfung (5.521 → 3.046)

Vor der Maker-Checker-Verifikation deckte das Mapping 1.306 der 1.834 aktiven Anforderungen ab, danach 1.205. 236 Anforderungen verloren ihre letzte Zuordnung, 135 kamen neu hinzu. Genau diese Differenz ist der Preis der Präzision — die vollständigen ID-Listen stehen in `ed23_gap_analyse.json` unter `summary.vergleich_5521_vs_3046`.

## 5. Ergebnisse auf Teilanforderungsebene

**Unsere Zerlegung** (Satz-Indizes des stripped-Korpus, nur aktive offizielle Anforderungen): 3.789 Sätze, davon 1.692 von mindestens einer Zuordnung referenziert und 2.097 (55,3 %) ohne Referenz.

**BSI GSMap (UA-Ebene):** 824 Unteranforderungen gemappt. Das UA-Universum ist unveröffentlicht; aus den maximal beobachteten Indizes ergibt sich eine Untergrenze von 1.430 UAs in den berührten Anforderungen — darunter 606 beweisbar ungemappte (Index kleiner als ein gemappter Nachbar).

**Projektion auf den offiziellen Wortlaut:** Das XML enthält 6.611 normative Sätze (MUSS/SOLLTE/DARF, zzgl. 0 KANN-Sätze). Projiziert über das Satz-Alignment sind 3.166 davon (47,9 %) abgedeckt. Alignment-Qualität je Anforderung: 668× aligned, 66× teilweise, 471× grob (= Anforderungs-Abdeckung pauschal auf alle Sätze übertragen). Diese Ebene ist eine transparente Näherung — belastbar sind die Ebenen (a) und (b).

### 5.1 Deterministischer Zerlegungs-Vergleich der Teilanforderungs-Indizes

Bei 397 Anforderungen tragen beide Mappings Teilanforderungs-Indizes (unsere `statement-sentence` vs. BSI-`UA.n`). Mengenvergleich der Indizes: 111 identisch (28,0 %), 171 überlappend (43,1 %), 115 disjunkt (29,0 %). Die beiden Nummerierungen zählen verschiedene Zerlegungen (NTT-Paraphrase-Sätze bzw. das unveröffentlichte UA-Schema des GSMap) — Index-Gleichheit ist ein Strukturindiz, keine bewiesene inhaltliche Übereinstimmung.

Kardinalitäten-Abgleich gegen den amtlichen Wortlaut: Bei 2 Anforderungen übersteigt schon die UA-Untergrenze des GSMap die Zahl der normativen XML-Sätze (das BSI zerlegt dort feiner als die Modalverb-Satzzählung, oder zählt Kontextsätze mit). Unsere Paraphrase-Zerlegung trifft die amtliche Satzzahl bei 416 von 1.205 gemappten Anforderungen (34,5 %). Vollständige ID-Listen im JSON unter `summary.teilanforderungen.zerlegungsvergleich`.

## 6. Gegenrichtung: GS++-Maßnahmen ohne ED23-Entsprechung

| Quelle | GS++-Maßnahmen ohne Treffer (von 1.000) |
|---|---|
| Unser Mapping | 180 |
| BSI GSMap | 678 |
| Prozessbaustein-Mapping | 684 |
| **in keiner der drei Quellen** | **136** |

Verteilung der 180 Maßnahmen ohne Treffer in unserem Mapping nach Praktik-Gruppe: ARCH 5, ASST 5, BER 21, BES 20, DET 20, DEV 7, DLS 2, GC 5, GEB 14, KONF 20, NOT 7, PERF 7, PERS 2, REA 2, RISK 4, SENS 21, STM 9, TEST 6, UMS 2, VRB 1. Vollständige Listen in `ed23_gap_analyse.json` unter `forward_gaps`.

## 7. Kreuzbefunde zwischen den Quellen

- Ziel-Klassen unseres Mappings: {"ntt-custom": 124, "official": 1205}. NTT-eigene (nicht-amtliche) Ziele: 124, Ziele auf ENTFALLENE Anforderungen: 0, dangling: 0.
- Quell-Klassen des BSI GSMap: {"official": 510}; ENTFALLEN-gemappt: 0, dangling: 0.
- Veraltete GS++-Ziel-IDs im BSI GSMap (existieren im gepinnten GS++-Katalog nicht): 17 — DET.3.1.13, GC.6.1.1, GC.6.1.2, GC.6.1.3, GC.8.1.1, GC.8.1.1.1, GC.8.1.2, GC.9.1.3, KONF.11.9, KONF.2.5.1.1, PERF.5.1.4, PERF.5.1.9, PERF.5.2, TEST.4.1.1.1, UMS.3.2, UMS.4.2, VRB.1.2.
- Prozessbaustein-Mapping: 0 dangling Quellen, 0 außerhalb der Prozess-Schichten, 0 dangling GS++-Ziele.
- satz_nr außerhalb des Satzbereichs: 0; Duplikate: 0 (unser Mapping) / 0 (GSMap).
- Level-Widersprüche Titel vs. Abschnitt im XML: 0.
- Amtliche Anforderungen ohne Eintrag im stripped-Korpus: 0.
- NTT-eigene Bausteine im Korpus (nicht Teil des amtlichen Kompendiums): 12 — APP.4.10, APP.4.5, APP.4.7, APP.4.8, APP.4.9, DER.7, OPS.1.1.8, ORP.6, SYS.1.10, SYS.1.11, SYS.1.2.4, SYS.5.1.
- NTT-eigene Zusatz-Anforderungen innerhalb amtlicher Bausteine: 1 (OPS.2.3 1).
- Alle dokumentierten Anker-Zahlen (Handbuch 10.3, Release Notes 4.0) wurden reproduziert.

## 8. Reproduktion

```bash
uv run Gpp-ai-tool/scripts/analyze_ed23_coverage.py --date 2026-08-29
```

Alle Fremdquellen sind commit- bzw. sha256-gepinnt (siehe Konstanten im Script und `meta.sources` im JSON); Downloads landen im gitignorierten Cache `Gpp-ai-tool/.cache/ed23_gap/`. Gleicher `--date`-Wert ⇒ byte-identische Ausgaben.

## Anhang A: Aktive Anforderungen ohne jede Zuordnung

416 Anforderungen, gruppiert nach Baustein:

- **APP.1.1** (2): APP.1.1.A14, APP.1.1.A6
- **APP.2.1** (12): APP.2.1.A13, APP.2.1.A14, APP.2.1.A15, APP.2.1.A16, APP.2.1.A18, APP.2.1.A19, APP.2.1.A20, APP.2.1.A21, APP.2.1.A5, APP.2.1.A6, APP.2.1.A8, APP.2.1.A9
- **APP.2.2** (8): APP.2.2.A15, APP.2.2.A17, APP.2.2.A18, APP.2.2.A19, APP.2.2.A20, APP.2.2.A21, APP.2.2.A6, APP.2.2.A8
- **APP.2.3** (5): APP.2.3.A1, APP.2.3.A10, APP.2.3.A4, APP.2.3.A5, APP.2.3.A9
- **APP.3.1** (1): APP.3.1.A9
- **APP.3.2** (2): APP.3.2.A13, APP.3.2.A9
- **APP.3.3** (4): APP.3.3.A13, APP.3.3.A2, APP.3.3.A6, APP.3.3.A7
- **APP.3.4** (6): APP.3.4.A10, APP.3.4.A2, APP.3.4.A6, APP.3.4.A7, APP.3.4.A8, APP.3.4.A9
- **APP.3.6** (7): APP.3.6.A14, APP.3.6.A17, APP.3.6.A19, APP.3.6.A20, APP.3.6.A21, APP.3.6.A22, APP.3.6.A6
- **APP.4.2** (13): APP.4.2.A11, APP.4.2.A15, APP.4.2.A16, APP.4.2.A17, APP.4.2.A18, APP.4.2.A19, APP.4.2.A20, APP.4.2.A22, APP.4.2.A23, APP.4.2.A25, APP.4.2.A26, APP.4.2.A3, APP.4.2.A8
- **APP.4.3** (6): APP.4.3.A13, APP.4.3.A17, APP.4.3.A18, APP.4.3.A19, APP.4.3.A21, APP.4.3.A4
- **APP.4.4** (4): APP.4.4.A14, APP.4.4.A17, APP.4.4.A21, APP.4.4.A6
- **APP.4.6** (13): APP.4.6.A1, APP.4.6.A13, APP.4.6.A14, APP.4.6.A15, APP.4.6.A16, APP.4.6.A17, APP.4.6.A2, APP.4.6.A21, APP.4.6.A3, APP.4.6.A4, APP.4.6.A7, APP.4.6.A8, APP.4.6.A9
- **APP.5.2** (6): APP.5.2.A10, APP.5.2.A11, APP.5.2.A12, APP.5.2.A17, APP.5.2.A2, APP.5.2.A3
- **APP.5.3** (4): APP.5.3.A5, APP.5.3.A6, APP.5.3.A7, APP.5.3.A8
- **APP.5.4** (8): APP.5.4.A10, APP.5.4.A12, APP.5.4.A15, APP.5.4.A16, APP.5.4.A17, APP.5.4.A18, APP.5.4.A3, APP.5.4.A5
- **APP.7** (1): APP.7.A8
- **IND.1** (7): IND.1.A14, IND.1.A21, IND.1.A22, IND.1.A3, IND.1.A5, IND.1.A7, IND.1.A9
- **IND.2.1** (3): IND.2.1.A13, IND.2.1.A17, IND.2.1.A8
- **IND.2.2** (1): IND.2.2.A3
- **IND.2.3** (3): IND.2.3.A1, IND.2.3.A2, IND.2.3.A3
- **IND.2.7** (7): IND.2.7.A10, IND.2.7.A11, IND.2.7.A2, IND.2.7.A4, IND.2.7.A7, IND.2.7.A8, IND.2.7.A9
- **IND.3.2** (5): IND.3.2.A11, IND.3.2.A13, IND.3.2.A2, IND.3.2.A6, IND.3.2.A9
- **INF.1** (8): INF.1.A10, INF.1.A16, INF.1.A19, INF.1.A2, INF.1.A31, INF.1.A32, INF.1.A34, INF.1.A36
- **INF.10** (2): INF.10.A5, INF.10.A7
- **INF.11** (8): INF.11.A12, INF.11.A13, INF.11.A14, INF.11.A15, INF.11.A16, INF.11.A17, INF.11.A7, INF.11.A9
- **INF.12** (5): INF.12.A11, INF.12.A12, INF.12.A13, INF.12.A16, INF.12.A9
- **INF.13** (15): INF.13.A10, INF.13.A11, INF.13.A13, INF.13.A14, INF.13.A15, INF.13.A19, INF.13.A20, INF.13.A24, INF.13.A26, INF.13.A27, INF.13.A28, INF.13.A29, INF.13.A5, INF.13.A7, INF.13.A9
- **INF.14** (17): INF.14.A10, INF.14.A12, INF.14.A14, INF.14.A15, INF.14.A16, INF.14.A19, INF.14.A2, INF.14.A20, INF.14.A21, INF.14.A22, INF.14.A23, INF.14.A24, INF.14.A3, INF.14.A30, INF.14.A4, INF.14.A8, INF.14.A9
- **INF.2** (3): INF.2.A22, INF.2.A23, INF.2.A29
- **INF.5** (7): INF.5.A11, INF.5.A13, INF.5.A14, INF.5.A19, INF.5.A25, INF.5.A26, INF.5.A5
- **INF.7** (1): INF.7.A3
- **NET.1.1** (3): NET.1.1.A27, NET.1.1.A36, NET.1.1.A9
- **NET.1.2** (8): NET.1.2.A16, NET.1.2.A2, NET.1.2.A24, NET.1.2.A27, NET.1.2.A31, NET.1.2.A36, NET.1.2.A37, NET.1.2.A8
- **NET.2.1** (8): NET.2.1.A11, NET.2.1.A12, NET.2.1.A15, NET.2.1.A16, NET.2.1.A6, NET.2.1.A7, NET.2.1.A8, NET.2.1.A9
- **NET.2.2** (1): NET.2.2.A2
- **NET.3.1** (4): NET.3.1.A12, NET.3.1.A22, NET.3.1.A27, NET.3.1.A9
- **NET.3.2** (4): NET.3.2.A22, NET.3.2.A26, NET.3.2.A31, NET.3.2.A32
- **NET.3.3** (5): NET.3.3.A12, NET.3.3.A13, NET.3.3.A6, NET.3.3.A7, NET.3.3.A8
- **NET.3.4** (8): NET.3.4.A1, NET.3.4.A17, NET.3.4.A2, NET.3.4.A20, NET.3.4.A25, NET.3.4.A26, NET.3.4.A5, NET.3.4.A8
- **NET.4.1** (2): NET.4.1.A11, NET.4.1.A17
- **NET.4.2** (6): NET.4.2.A13, NET.4.2.A14, NET.4.2.A15, NET.4.2.A5, NET.4.2.A7, NET.4.2.A9
- **NET.4.3** (7): NET.4.3.A10, NET.4.3.A13, NET.4.3.A14, NET.4.3.A3, NET.4.3.A4, NET.4.3.A7, NET.4.3.A8
- **SYS.1.1** (3): SYS.1.1.A35, SYS.1.1.A38, SYS.1.1.A9
- **SYS.1.2.2** (7): SYS.1.2.2.A11, SYS.1.2.2.A12, SYS.1.2.2.A14, SYS.1.2.2.A2, SYS.1.2.2.A5, SYS.1.2.2.A6, SYS.1.2.2.A8
- **SYS.1.2.3** (2): SYS.1.2.3.A2, SYS.1.2.3.A5
- **SYS.1.3** (1): SYS.1.3.A6
- **SYS.1.5** (10): SYS.1.5.A14, SYS.1.5.A19, SYS.1.5.A22, SYS.1.5.A23, SYS.1.5.A24, SYS.1.5.A25, SYS.1.5.A26, SYS.1.5.A27, SYS.1.5.A3, SYS.1.5.A7
- **SYS.1.6** (9): SYS.1.6.A10, SYS.1.6.A13, SYS.1.6.A19, SYS.1.6.A2, SYS.1.6.A23, SYS.1.6.A25, SYS.1.6.A4, SYS.1.6.A7, SYS.1.6.A9
- **SYS.1.7** (26): SYS.1.7.A11, SYS.1.7.A14, SYS.1.7.A17, SYS.1.7.A18, SYS.1.7.A19, SYS.1.7.A20, SYS.1.7.A21, SYS.1.7.A22, SYS.1.7.A23, SYS.1.7.A24, SYS.1.7.A25, SYS.1.7.A26, SYS.1.7.A27, SYS.1.7.A28, SYS.1.7.A29, SYS.1.7.A3, SYS.1.7.A30, SYS.1.7.A31, SYS.1.7.A32, SYS.1.7.A34, SYS.1.7.A35, SYS.1.7.A36, SYS.1.7.A37, SYS.1.7.A38, SYS.1.7.A4, SYS.1.7.A5
- **SYS.1.8** (11): SYS.1.8.A10, SYS.1.8.A13, SYS.1.8.A14, SYS.1.8.A15, SYS.1.8.A18, SYS.1.8.A21, SYS.1.8.A22, SYS.1.8.A24, SYS.1.8.A26, SYS.1.8.A6, SYS.1.8.A8
- **SYS.1.9** (6): SYS.1.9.A1, SYS.1.9.A16, SYS.1.9.A18, SYS.1.9.A5, SYS.1.9.A7, SYS.1.9.A8
- **SYS.2.1** (5): SYS.2.1.A20, SYS.2.1.A21, SYS.2.1.A37, SYS.2.1.A40, SYS.2.1.A9
- **SYS.2.2.3** (10): SYS.2.2.3.A1, SYS.2.2.3.A13, SYS.2.2.3.A18, SYS.2.2.3.A2, SYS.2.2.3.A20, SYS.2.2.3.A21, SYS.2.2.3.A24, SYS.2.2.3.A25, SYS.2.2.3.A4, SYS.2.2.3.A5
- **SYS.2.3** (4): SYS.2.3.A12, SYS.2.3.A20, SYS.2.3.A4, SYS.2.3.A9
- **SYS.2.4** (8): SYS.2.4.A1, SYS.2.4.A11, SYS.2.4.A4, SYS.2.4.A5, SYS.2.4.A6, SYS.2.4.A7, SYS.2.4.A8, SYS.2.4.A9
- **SYS.2.5** (5): SYS.2.5.A10, SYS.2.5.A11, SYS.2.5.A3, SYS.2.5.A6, SYS.2.5.A9
- **SYS.2.6** (8): SYS.2.6.A1, SYS.2.6.A13, SYS.2.6.A2, SYS.2.6.A3, SYS.2.6.A5, SYS.2.6.A7, SYS.2.6.A8, SYS.2.6.A9
- **SYS.3.1** (2): SYS.3.1.A11, SYS.3.1.A8
- **SYS.3.2.1** (9): SYS.3.2.1.A13, SYS.3.2.1.A16, SYS.3.2.1.A19, SYS.3.2.1.A27, SYS.3.2.1.A29, SYS.3.2.1.A30, SYS.3.2.1.A31, SYS.3.2.1.A33, SYS.3.2.1.A9
- **SYS.3.2.2** (6): SYS.3.2.2.A12, SYS.3.2.2.A14, SYS.3.2.2.A21, SYS.3.2.2.A5, SYS.3.2.2.A6, SYS.3.2.2.A7
- **SYS.3.2.3** (10): SYS.3.2.3.A12, SYS.3.2.3.A13, SYS.3.2.3.A14, SYS.3.2.3.A15, SYS.3.2.3.A18, SYS.3.2.3.A2, SYS.3.2.3.A21, SYS.3.2.3.A25, SYS.3.2.3.A26, SYS.3.2.3.A7
- **SYS.3.2.4** (2): SYS.3.2.4.A3, SYS.3.2.4.A5
- **SYS.3.3** (2): SYS.3.3.A8, SYS.3.3.A9
- **SYS.4.1** (3): SYS.4.1.A1, SYS.4.1.A14, SYS.4.1.A5
- **SYS.4.3** (6): SYS.4.3.A15, SYS.4.3.A17, SYS.4.3.A5, SYS.4.3.A6, SYS.4.3.A7, SYS.4.3.A9
- **SYS.4.4** (7): SYS.4.4.A10, SYS.4.4.A11, SYS.4.4.A15, SYS.4.4.A16, SYS.4.4.A19, SYS.4.4.A6, SYS.4.4.A7
- **SYS.4.5** (4): SYS.4.5.A15, SYS.4.5.A4, SYS.4.5.A5, SYS.4.5.A6
