# Plan: Genauigkeit der KI-Dokumentanalyse im SSP-Generator

Stand 2026-09-14, Fassung 2 nach Klärung der offenen Fragen. Anlass: Vier Läufe des SSP-Generators (V5.14.1)
über `Beschreibung_Recplast.pdf` mit vier Modellen (qwen3.5 9B lokal, gemini-3.8-flash,
gpt-6-astra, claude-fable-5.1) und das Vergleichsgutachten v1.2 vom 2026-09-13 dazu.
Kriterium laut Auftrag: Genauigkeit. Tokens und Laufzeit sind kein Kriterium.

Befangenheitshinweis: Dieser Plan wurde von demselben Modell geschrieben, das den Lauf
SSP-4 erzeugt hat. Alle Code-Befunde sind mit Zeilenverweis belegt und skriptgestützt
gegen die vier Exporte geprüft; die Katalogaussagen stammen aus dem gepinnten Build
(Commit `4e11779`, SHA-256 `691e8ca0…969df`, identisch mit der Back-Matter aller vier SSPs).

## 1. Kernaussage

Die Streuung zwischen den vier Läufen kommt zum größten Teil aus dem Werkzeug, nicht aus
den Modellen. Drei von vier Modellen haben die Schutzbedarfstabellen nachweislich gelesen
und konnten die Werte nicht an den Assets unterbringen, weil der Generator ein einmal
angelegtes Asset aus einem späteren Chunk nicht mehr aktualisiert und den Schutzbedarf
auf `normal-SdT` vorbelegt. Vier Normalisierer machen aus unbekannten Werten stille
Defaults (Status `planned`, Risiko `medium`, Schutzbedarf `normal-SdT`, Komponententyp
Freitext). Der Katalog gibt für Status und Schutzbedarf feste Regeln vor, die das Werkzeug
heute dem Modell überlässt.

Reihenfolge deshalb: erst messbar machen, dann alles Deterministische, dann erst neue
Modellaufrufe.

## 2. Befund

### 2.1 Kennzahlen der vier Läufe (aus dem Gutachten v1.2)

| Kennzahl | qwen lokal | gemini-3.8-flash | gpt-6-astra | claude-fable-5.1 |
|---|---|---|---|---|
| Bewertete Zielobjekte / Komponenten | 88 / 128 | 129 / 157 | 213 / 269 | 151 / 177 |
| Schutzbedarf: Treffer / falsch / fehlt (25 explizite Objekte) | 14 / 5 / 5 | 10 / 13 / 2 | 2 / 22 / 1 | 4 / 21 / 0 |
| Control-Zuordnungen: tragfähig / schwach / falsch | 12 / 6 / 12 | 32 / 2 / 0 | 52 / 4 / 0 | 33 / 2 / 0 |
| Kompendiums-Anforderungen ohne Zuordnung | 0 von 17 | 28 von 86 | 35 von 93 | 42 von 100 |
| Umsetzungsstatus korrekt (49 Anforderungen) | 1 | 35 | 4 | 48 |
| Risiken, davon mit Skalenwert laut PDF | 5 / 0 | 14 / 0 | 45 / 0 | 70 / 0 |
| Dublettenverhältnis Komponenten zu realen Zielobjekten | n. b. | n. b. | 2,5 : 1 | 1,4 : 1 |
| Verworfene Objekte (ohne Kategorie) | 3 | 5 | 6 | 2 |

Ground Truth: die Tabellen 1 bis 14 (Strukturanalyse), 15 bis 19 (Schutzbedarf), 21 bis 23
(Grundschutz-Check), 24 bis 30 (Risikoanalyse) und 31 (Realisierungsplan) des PDF.

### 2.2 Ursachen im Werkzeug, mit Zeilenverweis

| Nr. | Befund | Stelle in `GS++-oscal-app/ssp_generator.html` | Wirkung |
|---|---|---|---|
| W1 | Zusammenführung der Chunks: erster Eintrag je Dokument, Quell-ID und Name gewinnt; ein späterer Chunk kann nichts aktualisieren | `normalizeAIDocumentAnalysis`, Zeilen 2777 (Assets) und 2798 (Prozesse) | Schutzbedarf aus Tabelle 16 bis 19 erreicht Assets aus Chunk 2 und 3 nie; Fließtext (Kap. 3.4) und Tabellen (Kap. 5.3) erzeugen Dubletten |
| W2 | Schutzbedarf-Default `normal-SdT`; alles ohne „erhöht/hoch/high/sehr" wird normal | `normalizeSchutzbedarf`, Zeile 2706 | „nicht in diesem Chunk angegeben" wird zur Einstufung |
| W3 | Status-Aliase kennen weder ja, nein noch entbehrlich; Unbekanntes wird `planned` | `normalizeImplementationStatus`, Zeile 2683 | Grundschutz-Check-Werte gehen verloren; SSP-3 mit 160 von 165 auf planned zum Teil Werkzeug |
| W4 | Risikoskalen: nur niedrig/mittel/hoch/sehr hoch; die 200-3-Begriffe (selten … sehr häufig, vernachlässigbar … existenzbedrohend) fehlen; Unbekanntes wird `medium` | `normalizeRiskLevel`, Zeile 2699 | alle Risiken aller vier Läufe „medium/medium" |
| W5 | Assets ohne Zielobjektkategorie werden übersprungen und nie exportiert | `applyAIMappingsToWorkspace`, Zeile 3111 | Firewall N002, Serverraum R009 u. a. fehlen im SSP |
| W6 | Mapping-Prompt erhält nur Kategorie-Slugs, keine Definitionen, Synonyme, Hierarchie | `mapAIDocumentAnalysis`, Zeile 3055 | „Firewall" findet keine Kategorie, obwohl „Externe Netzanschlüsse" (Synonym Internetanschluss) existiert |
| W7 | Abdeckungsprüfung zeigt je Kandidat 160 Zeichen Statement | `checkAIControlCoverage`, Zeile 3238 | Modell ordnet nach Titel statt nach Statement zu (Fehlerklasse von SSP-1) |
| W8 | Kompendiums-IDs (ISMS.1.A5 …) werden Custom Controls im eingebetteten Katalog, obwohl das Repo ein GS++-zu-ED23-Mapping mit 5.086 Zuordnungen hat | `activateAIDocumentAnalysis`, Zeile 3286; `hilfsdateien/gpp_ed23_anforderungen.json` | 28 bis 42 Anforderungen je Lauf bleiben ohne Zuordnung, Kompendiumsanforderungen erscheinen unter fremder ID |
| W9 | Geschäftsprozesse kommen als Komponenten an, aber ohne Schutzbedarf-Prop und ohne Verweis auf ihre Assets | Export, Komponentenschleife | Schutzbedarf der Prozesse, in GS++ der Ausgangspunkt, steht nirgends im SSP |
| W10 | Die Zuordnung ordnet auch Geschäftsprozesse und Einzelmaßnahmen einer Praktik zu (qwen: E-Mail-Client auf BER, Virenschutz auf DET); jede Zuweisung importiert das kuratierte Praktik-Profil (BER 63 von 92 Controls, DET 38 von 82, TEST 30 von 36) | `mapAIDocumentAnalysis`, Zeile 3055; Profile unter `Zielobjektkategorien/profile/process/` | SSP-1: 169 Platzhalter, davon 131 aus BER, DET, TEST ohne Dokumentbezug. Der Import ist gewollt (E7), die Zuweisung ist das Problem |
| W11 | Komponententyp, AI-IDs, Sprache sind frei | Extraktionsschema ab Zeile 1134 | 24 bis 58 Typbezeichnungen je Lauf, AI-002 neben AI-2FA, englische Felder bei qwen |
| W12 | System-Prop `schutzbedarf-system` trägt „hoch/normal" unter dem Namespace `security_level.csv`, der nur `normal-SdT` und `erhöht` kennt | Zeile 6684 | ungültiger Namespace-Wert |
| W13 | PLACEHOLDER-Requirement steht neben echten Requirements | Zeile 6702 erzeugt ihn nur bei leerer Liste; Herkunft zu klären | Schema-Ballast |
| W14 | Seitenmarken werden nicht angefordert, obwohl `gppDocText` sie kann | Textextraktion im Generator | keine Fundstellen mit Seite (SSP-2, SSP-4) |

### 2.3 Wo der Katalog das Gutachten korrigiert

Der Katalog gewinnt (Skill-Grundregel 1). Drei Maßstäbe des Gutachtens stammen aus der
200-2-Welt:

- **Umsetzungsstatus ist binär.** Guidance zu UMS.1.1: nur „umgesetzt" oder „nicht
  umgesetzt". „Teilweise" und „entbehrlich" existieren in GS++ nicht. Entbehrlich ist eine
  begründete Streichung aus dem Anforderungspaket (Guidance zu STM.2.1.5), bewusste
  Nichtumsetzung eine Ausnahme nach UMS.5.1 und UMS.5.2. Das Ergebnis des Gutachtens
  (entbehrlich auf `not-applicable`) stimmt, die Herleitung ist eine andere. Beides ist
  Guidance, nicht Statement. Die Werkzeugsammlung behält das OSCAL-Vokabular mit `partial`
  bewusst bei und wendet das binäre Modell nirgends an (E6); die Abweichung ist damit
  benannt, nicht harmonisiert.
- **Schutzbedarf hängt am Geschäftsprozess.** GC.7.1.2:

  > Governance und Compliance MUSS eine Einstufung des Schutzbedarfs der relevanten Geschäftsprozesse oder Informationen unter Berücksichtigung der Geschäftsziele und in Absprache mit der Institutionsleitung festlegen.

  Die Guidance nennt die Stufen „normal" und „hoch" (Namespace: `normal-SdT`, `erhöht`).
  Wie das Sicherheitsniveau eines Assets daraus folgt, sagt der Katalog nicht: STM.2.1.4.1
  vererbt Zielobjektkategorien, nicht Schutzbedarf; STM.3.1 lässt Anpassungen „auch bei
  einzelnen Assets" zu (Guidance). Das Maximumprinzip ist 200-2-Auslegung und wird im
  Werkzeug als solche gekennzeichnet.
- **Risikomethodik ist frei.** GC.12.1 verlangt eine einheitliche Methodik; die Guidance zu
  GC.7.2 nennt 200-3 als eine Option neben ISO 27005 und ISO 31000. Das Werkzeug darf
  200-3-Skalen abbilden, aber nicht voraussetzen: die Quellskala bleibt wörtlich erhalten.

## 3. Entscheidungen

Getroffen (Christoph, 2026-09-13/14):

| Nr. | Entscheidung |
|---|---|
| E1 | Kriterium ist Genauigkeit. Tokens und Laufzeit sind kein Kriterium. |
| E2 | Geschäftsprozesse gehören genau einmal in den SSP; Komponente ist zulässig, aber nicht Pflicht. |
| E3 | Schutzbedarf-Vererbung vom Geschäftsprozess auf Assets wird übernommen, gekennzeichnet als 200-2-Auslegung. |
| E4 | Gefährdungsübersichten aus Dokumenten werden als unbewertete Risiken übernommen, gekennzeichnet. |
| E5 | Die RECPLAST-Ground-Truth und die Skripte des Gutachtens kommen in einen QS-Ordner (`QS/`), nur für die Entwicklung, nicht Teil der Auslieferung. Ziel ist die Qualität der Extraktion insgesamt; Dokumente anderer Kunden sehen anders aus. RECPLAST ist Regressionsfixture, nicht Optimierungsziel. |
| E6 | Status-Modell: OSCAL-Vokabular mit `partial` bleibt in allen Werkzeugen. Das binäre Modell des BSI (Guidance zu UMS.1.1) wird nirgends angewendet, nur dokumentiert. |
| E7 | Prozesse bleiben über die kuratierten Praktik-Profile unter `Zielobjektkategorien/profile/process/` im SSP; einige Praktiken sind selbst Prozesse. Der Profil-Import bleibt unverändert. Genauigkeit kommt aus der richtigen Zuweisung, nicht aus einem anderen Import. |

Offene Entscheidungen: keine. Offene Fragen mit Katalogbezug stehen in Abschnitt 7.

## 4. Messgrößen und Zielwerte

Alle Messgrößen werden von einem Skript aus dem Export berechnet, ohne Modellaufruf.
Baseline sind die vier Läufe vom 2026-09-13. Zwei Klassen (E5): Die ersten sechs Zeilen
der Tabelle brauchen eine Ground Truth und gelten nur für RECPLAST. Die übrigen sind
dokumentunabhängig und laufen über jedes Fixture, auch über Kundendokumente ohne
Ground Truth; sie sind der eigentliche Maßstab für die Extraktionsqualität insgesamt.

| Messgröße | Definition | Baseline (beste / schlechteste) | Ziel nach Stufe 1 | Ziel nach Stufe 3 |
|---|---|---|---|---|
| Zielobjekt-Recall | Anteil der Kennungen aus Tabelle 1 bis 14, die als Komponente mit dieser Quell-ID vorliegen | n. b. (Gutachten zählt Bestand) | ≥ 95 % | ≥ 98 % |
| Dublettenverhältnis | Komponenten geteilt durch reale Zielobjekte | 1,4 / 2,5 | ≤ 1,2 | ≤ 1,05 |
| Verworfene Objekte | Assets der Analyse ohne Komponente im SSP | 2 / 6 | 0 | 0 |
| Schutzbedarf explizit | Treffer über die 25 explizit eingestuften Objekte | 14 / 2 | 25 | 25 |
| Schutzbedarf vererbt | Assets von Prozessen mit hohem Schutzbedarf, die `erhöht` tragen und die Herkunft „vererbt" ausweisen | 0 | vollständig | vollständig |
| Umsetzungsstatus | Treffer über die 49 Anforderungen aus Tabelle 21 bis 23, feste Abbildung | 48 / 1 | 49 | 49 |
| Zuordnung deterministisch | Kompendiums-Anforderungen, die über das ED23-Mapping ohne Modell aufgelöst werden | 0 | alle im Mapping vorhandenen | dito |
| Zuordnung Modell | tragfähig / schwach / falsch über die vom Gutachten geprüften Zuordnungen (feste Liste) | 52/4/0 bis 12/6/12 | 0 falsch | 0 falsch |
| Risikoskalen | Risiken mit Skalenwert aus dem PDF, wörtlich und abgebildet | 0 | alle aus Tabelle 28 und 29 | dito |
| Fabrikation | Verantwortliche und Nachweise, die im PDF nicht vorkommen | 0 bis „ja" | 0 | 0 mit Belegprüfung |
| Sprache | Felder mit englischem Text oder ae/oe/ue-Schreibweise | qwen, gemini | 0 | 0 |
| Unbestimmt-Quote | Anteil Assets ohne Schutzbedarf, Maßnahmen ohne Status, Risiken ohne Skala nach der Extraktion; misst, was das Dokument nicht hergibt, statt es zu raten | n. b. | sichtbar | sichtbar |
| Vokabular-Konformität | Anteil Feldwerte, die im Schema-Enum oder Namespace liegen | 24 bis 58 Typbezeichnungen je Lauf | 100 % | 100 % |
| Belegquote | Anteil Entitäten mit lokal verifiziertem Zitat | 0 | n. a. | ≥ 95 % |

## 5. Stufen

Jede Stufe ist einzeln lieferbar und wird mit dem Skript aus Stufe 0 gemessen.

### Stufe 0: Messen

1. Ground Truth als CSV unter `QS/recplast/` (E5): Zielobjekte (Kennung, Name,
   Tabelle), Schutzbedarf (Kennung, Wert, Fundstelle), Grundschutz-Check (Anforderung,
   Wert), Risiken (Gefährdung, Zielobjekt, Häufigkeit, Auswirkung, Kategorie), geprüfte
   Zuordnungen (Anforderung, GS++-Control, Urteil). Quelle: das Gutachten. Das PDF
   selbst nur als Verweis mit Adresse und SHA-256. Der Ordner ist von der Auslieferung
   (ZIP) ausgenommen.
2. `QS/score_ssp.py`: liest einen Export samt Analyse-Payload aus der Back-Matter und
   gibt die Tabelle aus Abschnitt 4 aus; die dokumentunabhängigen Zeilen für jedes
   Fixture, die RECPLAST-Zeilen nur bei vorhandener Ground Truth. Läuft ohne Netz.
3. Rohmaterial sichern: eine Exportfunktion für den Chunk-Cache (IndexedDB) im Generator,
   damit die je Modell gecachten Chunk-Ergebnisse als JSON unter `QS/fixtures/` liegen.
   Damit lassen sich Stufe 1 und 2 im Replay gegen dieselben Modellantworten messen, ohne
   neue Aufrufe.
4. Analyse-Payload erhält Generator-Version, Prompt-Hash je Schritt und Chunkgröße
   (Reproduzierbarkeit; Tokens und Dauer nicht, siehe E1).

### Stufe 1: Deterministisch härten, kein neuer Modellaufruf

| Nr. | Änderung | Behebt | Katalogbezug |
|---|---|---|---|
| S1.1 | Zusammenführung je Quell-ID statt je Name: gleiche Quell-ID im späteren Chunk aktualisiert den Eintrag feldweise, leere Felder verlieren, explizite Schutzbedarfswerte überschreiben „unbestimmt". Ohne Quell-ID: normalisierter Name (Standort-Suffixe, Klammern, Stückzahlen entfernt) als Schlüssel, Aliasnamen bleiben erhalten | W1 | STM.2.1.2 (eindeutige Bezeichnung/ID je Asset, Guidance) |
| S1.2 | Schutzbedarf dreiwertig: `erhöht`, `normal-SdT`, unbestimmt. Unbestimmt wird exportiert als fehlende Prop mit Remark und in der Oberfläche als offener Punkt gezählt. Namespace-Werte auch für die System-Prop | W2, W12 | GC.7.1.2; `security_level.csv` |
| S1.3 | Vererbung (E3): Assets, die einem Geschäftsprozess mit hohem Schutzbedarf zugeordnet sind, erhalten `erhöht`, sofern das Dokument nichts Niedrigeres explizit sagt. Prop `schutzbedarf-herkunft` mit den Werten explizit, vererbt (Auslegung 200-2, Maximumprinzip), unbestimmt | W9 | GC.7.1.2; nicht im Katalog geregelt, Auslegung gekennzeichnet |
| S1.4 | Feste Statustabelle: ja → `implemented`, nein → `not-implemented`, teilweise → `partial`, entbehrlich → `not-applicable`, geplant → `planned`, sonst unbestimmt. Quellwort als Prop `source-status`. Keine binäre Ableitung (E6). `not-applicable` trägt die Begründung aus dem Dokument als Remark. Schema-Enum statt Freitext; das Modell kopiert das Wort des Dokuments | W3 | E6; STM.2.1.5 nur als Herkunft der Begründungspflicht (Guidance) |
| S1.5 | Risiken: Quellskala wörtlich in `likelihoodSource`/`impactSource`; Abbildung der vierstufigen 200-3-Skalen; sonst „unbewertet". Risikokategorie aus dem Dokument als eigenes Feld. Gefährdungsübersichten (E4) mit Kennzeichen „nicht bewertet" | W4 | GC.12.1, GC.7.2 (Guidance: Methodik frei) |
| S1.6 | Assets ohne Kategorie bleiben als Komponente ohne Controls im SSP, mit Remark und Zählung als offener Punkt | W5 | STM.2.1.3 (MUSS allen relevanten Assets Zielobjektkategorien zuweisen) |
| S1.7 | Mapping-Prompt erhält die 39 Kategorien mit Definition (gekürzt), Synonymen und Elternknoten aus `target_object_categories.csv` (gepinnter Commit); Elternkategorien rechnet das Werkzeug, nicht das Modell | W6 | STM.2.1.3, STM.2.1.4.1 (Vererbung deterministisch, Guidance) |
| S1.8 | Geschäftsprozesse (E2): Extraktionsschema trennt `businessProcesses` (Kennung, Schutzbedarf, Owner, Asset-Verweise) von `securityProcesses`. Geschäftsprozesse werden genau einmal Komponente vom Typ `process-procedure` mit Schutzbedarf-Prop und Links auf ihre Assets; sie bekommen nie eine Praktik | W9, W10 | GC.7.1.1, STM.2.1.2 |
| S1.9 | Praktik-Zuweisung (E7) nur für Sicherheitsprozesse: „keine Praktik" ist eine gültige Antwort und die Vorgabe; eine Praktik nur, wenn der Prozess die Tätigkeit der Praktik selbst beschreibt, nicht eine Einzelmaßnahme daraus. Das Mapping-Prompt erhält die Praktik-Definitionen aus dem Namespace `practices.csv`. Der Profil-Import bleibt, wie er ist | W10 | STM.2.1.1 für die ISMS-Praktiken; Profile unter `Zielobjektkategorien/profile/process/` |
| S1.10 | Kompendiums-IDs vor der Abdeckungsprüfung über `gpp_ed23_anforderungen.json` auflösen (Rückrichtung ED23 → GS++, Vorrang equal-to, equivalent-to, dann subset-of, superset-of, intersects-with, Beziehung als Prop). Nur der Rest geht ans Modell, und zwar mit vollem Statement statt 160 Zeichen, in Paketen nach Anzahl | W7, W8 | Mapping-Status draft, wird als Herkunft ausgewiesen |
| S1.11 | Enums: Komponententyp auf das OSCAL-Vokabular; AI-IDs vergibt das Werkzeug fortlaufend, das Modell liefert nur Titel und Kurzform; Systemprompt erzwingt Deutsch mit Umlauten und verbietet Meta-Kommentare in Feldern („Fiktive Beispieldaten.") | W11 | |
| S1.12 | PLACEHOLDER-Herkunft klären und beseitigen | W13 | |
| S1.13 | Chunks an Kapitelgrenzen schneiden, Tabellen nicht zerteilen, Tabellenkopf im Folgechunk wiederholen; heute wird nach 28.000 Zeichen am nächsten Absatz getrennt | W1 (Tabellenkontext) | |

Erwartung nach Stufe 1 im Replay: Schutzbedarf 25/25, Status 49/49, verworfene Objekte 0,
deterministische Zuordnungen für ISMS.1 (14 im Mapping), APP.1.1 (9), SYS.2.2.3 (18),
NET.3.2 (25), SYS.2.1 (33). Lücken bleiben dort, wo das Mapping nichts hat (INF.4: 0).

### Stufe 2: Register-Kontext

Ein billiger Vorlauf je Chunk liefert nur Kandidaten (Quell-ID, Name, Typ, Abschnitt).
Das Werkzeug führt sie deterministisch zum Register zusammen (Quell-ID vor Name). Die
eigentliche Extraktion bekommt das Register im Prompt: bekannte Zielobjekte mit IDs
verwenden, keine neuen anlegen, außer sie fehlen im Register. Bleibt parallel. Behebt die
Fließtext-gegen-Tabelle-Dubletten (W1, zweiter Teil), die Stufe 1 nur über Namensregeln
mildert. Alternative mit rollierendem Register (Chunk n sieht 1 bis n-1) ist billiger,
aber seriell; nicht empfohlen.

### Stufe 3: Belegpflicht

Jede Entität (Asset, Prozess, Maßnahme, Risiko, Verantwortlicher, Nachweis) trägt ein
wörtliches Zitat und die Seitenmarke; `gppDocText` liefert Seitenmarken bereits. Das
Werkzeug prüft das Zitat als Teilstring gegen den Chunk. Ohne Beleg: Kennzeichen
„unbelegt", kein stiller Import. Verantwortliche werden zusätzlich gegen die Rollen des
Dokuments geprüft. Muster aus dem SSP-Editor (Issue #41). Kein zweiter Modellaufruf.

### Stufe 4: Neu messen

Alle vier Modelle erneut, Tabelle aus Abschnitt 4 je Stufe. Dazu ein zweites Fixture
eines anderen Dokumenttyps ohne Ground Truth, etwa ein Sicherheitskonzept zu Active
Directory, damit die dokumentunabhängigen Messgrößen nicht nur an RECPLAST hängen (E5).
Chunkgröße je Backend festlegen (lokal kleiner), Modellklasse im Readme benennen. Erst
hier wird ein Modellvergleich aussagekräftig.

## 6. Nicht Teil des Plans

- Prompts je Modell tunen: die Prompts sind editierbar und gelten für alle Backends.
- Zweiter Prüf-Aufruf (Checker) je Chunk als Standard: verdoppelt die Aufrufe; die
  Belegpflicht aus Stufe 3 leistet das Wesentliche ohne ihn. Als Option über die
  Checker-Route aus `config.html` denkbar, nur für den Mapping-Schritt.
- Audit-Aussagen: es gibt kein GS++-Prüfschema; jede Aussage dazu ist Auslegung.

## 7. Offene Fragen mit Katalogbezug

- Ableitung des Asset-Sicherheitsniveaus aus dem Prozess-Schutzbedarf steht nicht im
  Katalog (siehe 2.3). Kandidat für die zentrale Fundeliste.
- Das ED23-Mapping hat Status draft; SYS.2.2.3.A10 und der gesamte Baustein INF.4 fehlen.
  Auflösungen daraus werden mit Herkunft ausgewiesen, nicht als geprüft.
- `information-types` verwenden „hoch/normal" in Feldern, die OSCAL für FIPS-199-Werte
  vorsieht. Ob eine Abbildung auf `fips-199-high` sinnvoll ist, ist offen.
- Profilauflösung: Kompendiums-IDs als Custom Controls im eingebetteten Katalog lösen
  auf, sind aber semantisch Dubletten zu GS++-Controls. Nach S1.10 verbleiben nur noch
  IDs ohne Mapping dort.

## 8. Nächste Schritte

1. Issue im Repo mit diesem Plan als Referenz.
2. Erster PR: Stufe 0 und Stufe 1, gemessen im Replay gegen die vier Exporte.
3. Zweiter PR: Stufe 2. Dritter PR: Stufe 3. Danach Stufe 4 als Messlauf, kein Code.

## 9. Prüfmethode dieses Plans

Vier Exporte aus `Downloads` per Python gelesen (Analyse-Payload aus der Back-Matter
dekodiert), Kennzahlen gezählt. Katalog vom gepinnten Commit per `curl` geladen, SHA-256
gegen die Back-Matter geprüft, Praktiken GC, STM, UMS mit `dump_praktik.py` gedumpt.
Namespace-CSVs vom selben Commit. Zeilenverweise aus `ssp_generator.html` Stand
Commit `ab711fd`. Zitierte Control-IDs mit `verify_kapitel.py` gegen den Build geprüft.
