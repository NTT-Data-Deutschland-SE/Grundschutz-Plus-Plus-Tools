# Mapping-QS ED23 ↔ GS++ — Stichprobenprüfung vom 30.08.2026

**Prüfgegenstand:** `hilfsdateien/gpp_ed23_anforderungen.json` (v2026-08-29, Union, 5.145 Zuordnungen) · Quelle: GS++-resolved-Catalog @ `36a0fac4` · Ziel: amtliches XML_Kompendium_2023 (v4)
**Stichprobe:** 96 Controls / 943 Paare über alle 20 Praktiken (18,3 % der Paare, 11,1 % der 867 gemappten Controls)

## Ergebnis in einem Absatz

**Das Mapping ist als Migrationshilfe brauchbar und in der Substanz richtig.** 86,9 % der geprüften Paare sind inhaltlich sauber, nur 4 von 943 sind echte Fehltreffer. Die Schwächen liegen nicht in der Paar*auswahl*, sondern in der *Klassifikation*: Jeder sechste Relationstyp ist falsch — fast immer ein zu großzügiges `superset-of`, wo `intersects-with` stünde — und jede zehnte Begründung übertreibt die Abdeckung. „Zu viel" ist es nur an klar benennbaren Stellen: 76 Paare (8,1 %) sind Streichkandidaten, mehr als ein Drittel davon konzentriert auf drei Methodik-Controls.

| Kennzahl | Wert |
|---|---|
| Paare geprüft | **943** (18,3 % von 5.145) |
| inhaltlich sauber (ja) | **819 = 86,9 %** |
| grenzwertig (vertretbar, aber dünn) | 120 = 12,7 % |
| echte Fehltreffer (nein) | **4 = 0,4 %** |
| Relationstyp falsch | **150 = 15,9 %** (131 davon → `intersects-with`) |
| Begründung geschönt/falsch | 101 = 10,7 % (davon 4 mit erfundenen Inhalten) |
| Streichkandidaten | **76 = 8,1 %** |
| Controls hilfreich (ja / teilweise / nein) | 80 / 14 / 2 |

## 1 Prüfaufbau

Je Praktik wurden 5 Controls stratifiziert gezogen (paarreichstes, paarärmstes, Median, plus 2 zufällige; Seed 23) — bewusst inklusive der beiden größten Controls des gesamten Mappings, an denen sich die „Zu viel?"-Frage entscheidet. Für jedes gezogene Control wurden **alle** seine Zuordnungen geprüft: 943 Paare, Abdeckung 100 %, keine Lücke.

Jedes Paar wurde gegen den gepinnten GS++-Katalog (Statement *und* Guidance) und die amtlichen ED23-Satztexte auf vier Achsen bewertet: **Inhalt** (trifft der zitierte Satz den Regelungsgegenstand?), **Relationstyp** (in der dokumentierten Leserichtung GS++ relativ zur ED23-Teilanforderung), **Satzwahl** (richtiger Träger innerhalb der Anforderung?) und **Begründungsehrlichkeit**. 18 unabhängige Reviewer-Agenten mit identischer Prüfanweisung (`review_instructions.md`); die härtesten Urteile — alle vier `inhalt=nein`, die beiden Massen-Streichlisten, alle Erfindungs-Vorwürfe — wurden anschließend adversarial gegen die Dossiers nachgeprüft und bestätigt (eine Nuancierung bei DEV.5.2, s. Abschnitt 7).

## 2 Ergebnis je Praktik

| Praktik | Paare | ja | grenzw. | nein | ja-Quote | Rel. falsch | Begr. | Drop |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| ARCH | 67 | 63 | 4 | 0 | 94,0 % | 5 | 7 | 3 |
| ASST | 97 | 91 | 6 | 0 | 93,8 % | 13 | 5 | 4 |
| BER | 91 | 81 | 10 | 0 | 89,0 % | 3 | 3 | 2 |
| BES | 51 | 45 | 6 | 0 | 88,2 % | 4 | 3 | 4 |
| DET | 51 | 45 | 6 | 0 | 88,2 % | 6 | 3 | 4 |
| DEV | 23 | 17 | 5 | 1 | 73,9 % | 1 | 3 | 2 |
| DLS | 22 | 17 | 5 | 0 | 77,3 % | 4 | 3 | 2 |
| **GC** | 28 | 17 | 10 | 1 | **60,7 %** | 10 | 11 | 7 |
| GEB | 24 | 23 | 1 | 0 | 95,8 % | 6 | 5 | 1 |
| KONF | 135 | 125 | 10 | 0 | 92,6 % | 17 | 8 | 5 |
| NOT | 49 | 46 | 3 | 0 | 93,9 % | **17** | **16** | 3 |
| **PERF** | 30 | 19 | 11 | 0 | **63,3 %** | 13 | 3 | 11 |
| PERS | 59 | 53 | 6 | 0 | 89,8 % | 9 | 7 | 4 |
| REA | 27 | 24 | 3 | 0 | 88,9 % | 2 | 4 | 2 |
| RISK | 1 | 0 | 1 | 0 | 0,0 % | 0 | 0 | 0 |
| SENS | 40 | 36 | 4 | 0 | 90,0 % | 2 | 4 | 2 |
| STM | 18 | 15 | 2 | 1 | 83,3 % | 6 | 3 | 2 |
| TEST | 42 | 32 | 10 | 0 | 76,2 % | 12 | 8 | 3 |
| UMS | 51 | 47 | 4 | 0 | 92,2 % | **16** | 4 | 2 |
| **VRB** | 37 | 23 | 13 | 1 | **62,2 %** | 4 | 1 | 13 |
| **GESAMT** | **943** | **819** | **120** | **4** | **86,9 %** | **150** | **101** | **76** |

Lesehilfe: *Rel. falsch* = Relationstyp nicht haltbar (Paar selbst meist korrekt); *Begr.* = Begründung geschönt oder falsch; *Drop* = Streichempfehlung der Reviewer. GC, PERF und VRB tragen zusammen 31 der 76 Streichkandidaten.

## 3 Befund A — `superset-of`-Inflation ist der systematische Fehler

150 von 943 Relationstypen (15,9 %) halten der Prüfung nicht stand; **131 davon müssten `intersects-with` heißen** (11 → `superset-of`, 7 → `equivalent-to`, 1 → `subset-of`). Der Maker generalisiert korrekt, subsumiert aber zu großzügig. Vier wiederkehrende Mechanismen:

- **Mehr-Pflichten-Sätze:** Der ED23-Satz bündelt zwei Pflichten, das GS++-Control deckt eine. Musterfall UMS.5.1 (Autorisierung von Ausnahmen): 11 von 13 superset-Labeln falsch, weil die Zielsätze „abgestimmt *und dokumentiert*" fordern — die Autorisierung deckt die Dokumentationspflicht nicht.
- **Verb-Subsumtionsfehler:** *Deaktivieren* subsumiert kein *Prüfen*, *Nicht-Installieren* oder *Entfernen* (KONF.2.4: u. a. SYS.2.2.3.A19:S4, SYS.1.2.2.A2:S1); *Überprüfen* subsumiert kein *Warten* (GEB.10.2.7: „geprüft *und gewartet*"-Sätze).
- **Teilphasen-Fehler:** NOT.3.1 (nur Wiederanlauf) vereinnahmt ganze Notfallplan-Forderungen — 13 von 28 Relationen; dazu die Verwechslung Wiederanlauf auf Notbetriebsniveau vs. Wiederherstellung des Normalbetriebs (OPS.1.2.5.A21:S4).
- **Familien-Inkonsistenz:** Strukturgleiche Sätze bekommen verschiedene Typen, weil jedes Paar isoliert bewertet wurde — ORP.4.A5/A6/A7 (Schulungssätze: mal superset, mal subset), NET.3.4.A16:S1 vs. NET.3.1.A7:S1, DER.3.2.A17:S3 vs. DER.3.1.A17:S2.

**Warum das zählt:** `superset-of` behauptet gegenüber ISB und Auditor: „GS++ deckt diese ED23-Pflicht vollständig mit ab." Bei tatsächlichem `intersects-with` bleibt eine Restpflicht offen. Die Inflation erzeugt also **falsche Vollständigkeits-Signale in der Migrationsbilanz** — genau dort, wo das Mapping Beweiskraft haben soll. Sie verzerrt auch die publizierte Relationsstatistik (60,3 % superset-of), die nach Korrektur eher bei ~50 % läge, mit entsprechend mehr intersects-with.

## 4 Befund B — Begründungen übertreiben, vier erfinden

101 Begründungen (10,7 %) sind geschönt oder falsch. Das häufigste Muster ist „deckt … ab"-Rhetorik im *Widerspruch zum eigenen Relationslabel*: Das Etikett sagt subset/intersects, der Text behauptet Volldeckung (konzentriert in NOT mit 16 und GC mit 11 Fällen). Vier Begründungen erfinden nachweislich Inhalte:

| Paar | Erfindung |
|---|---|
| ASST.7.7 → NET.4.2.A12:S4 | Begründung zitiert das Statement mit „vor deren Veräußerung **oder Entsorgung**" — „Entsorgung" steht weder in Statement noch Guidance (Statement: nur Veräußerung; ED23: nur Entsorgung — der reale Trigger-Unterschied wird überschrieben). **Das Paar war Fundrichtung „beide"** — beidseitige Bestätigung ist kein Qualitätssiegel. |
| GEB.10.2.7 → INF.2.A8:S4 | Behauptet, die Guidance nenne „explizit die Funktionsprüfung **und Wartung**"; die Guidance kennt nur die Überprüfung. |
| GC.11.1 → ISMS.1.A12:S5/S7 | Dichtet dem Control eine „revisionssichere" Archivierung an; Statement und Guidance kennen nur Nachvollziehbarkeit. |
| NOT.3.1 → DER.4.A7:S6 | Unterstellt dem Control die Forderung eines „zentralen Notfallplans". |

Weitere Muster:

- **Verbindlichkeit verwischt:** KANN-Controls werden als „fordert" ausgegeben (REA.2.2, BES.8.3); ein Abwägungs-SOLLTE wird zur Nutzungspflicht (ASST.5.2/Predictive Maintenance).
- **Template-Formeln:** 92 Paare mit *bulk-noise*-Flag — dieselbe Begründungsschablone unabhängig vom Ziel, teils ganz ohne Zielbezug (NET.4.1.A9:S1, INF.14.A29:S2). Inhaltlich oft trotzdem korrekt, aber ohne Gewichtungshilfe für den Leser.

## 5 Befund C — die Methodik-Praktiken sind die Schwachstelle

Die ja-Quoten trennen sauber: Technik-Praktiken liegen bei 88–96 %, die Methodik-Praktiken **GC (60,7 %), VRB (62,2 %) und PERF (63,3 %)** fallen ab. Der Mechanismus ist immer derselbe *Ebenen-Fehler*: Ein ISMS-Prozess-Control saugt baustein-spezifische Einzelsätze per Wortähnlichkeit ein.

- **GC.3.1.1** (Analyse rechtlicher Rahmenbedingungen): 6 von 10 Paaren streichen — jeder verstreute Halbsatz „rechtliche Rahmenbedingungen beachten" aus Fachbausteinen wird eingesammelt; *Analysieren* deckt kein *Einhalten*.
- **VRB.4.1** (Korrekturmaßnahmen): 13 von 22 streichen — jedes „Abweichungen SOLLTE nachgegangen werden" aus Technik-Revisionen hängt am ISMS-KVP-Control. Tiefpunkt OPS.1.1.3.A9:S6: ein *Hardware-Störungsverfahren* wird allein über den Doppelsinn von „Fehler" als abgedeckt begründet.
- **PERF.3.1.4** (Umfang von Audits): 10 von 21 streichen — System-Revisionen (Webanwendung, SAP, Router, Storage …) werden dem ISMS-Auditprogramm zugeschlagen; ein Webanwendungs-Pentest erfüllt kein ISMS-Audit-Control.
- **Homonym-Fänge:** STM.3.1 → ISMS.1.A11:S5 — „Sicherheitsniveau" meint im Control die normal-SdT/erhöht-*Einstufung* von Anforderungen, im ED23-Satz das *erreichte* Niveau der Institution. Einziges Paar des Controls, hilfreich=nein.

**Gegenbild:** Der Fehler ist selektiv, nicht flächig: VRB.1.1 (Audit-Rückfluss), UMS.1.2 (Restrisiko-Kette), PERF.4.1.9 (satzgenaue equal-to-Treffer auf ISMS.1.A12), GC.9.1.1.1.2 (Vorspracherecht) und STM.2.1.2 (Asset-Erfassung) sind vorbildlich gemappt. Die Methodik-Praktiken brauchen einen gezielten Nachlauf, keinen Neuanfang.

**Sonderfall RISK:** 1 Control, 1 Paar — und das ist ein Keyword-Match (CON.8.A16:S4 regelt das Risikomanagement des *Software-Entwicklungs-Vorgehensmodells*, nicht die institutionsweite Methodik-Verankerung). Das ist keine Mapping-Schwäche, sondern eine **strukturelle Korpus-Lücke**: Das ED23-Kompendium enthält kaum Methodik-Anforderungen, die Risikomethodik liegt im BSI-Standard 200-3 außerhalb des Mapping-Ziels. Empfehlung: in Report und Tools ehrlich als Lücke ausweisen statt mit einem dünnen Paar kaschieren.

## 6 Zu viel? — Nein im Großen, ja an drei Stellen

**Die beiden Mega-Controls bestehen.** KONF.2.4 (Deaktivierung nicht benötigter Funktionen, **88 Paare**): nur 3 Streichkandidaten. BER.4.1 (Least Privilege, **83 Paare**): nur 2, kein einziges inhalt=nein. Beide sind Prinzipien-Hubs — ED23 verstreut Minimierung und PoLP real über ~25 Bausteine, und fast jedes Ziel fordert wörtlich dasselbe. **Die Masse ist hier der Katalog, nicht das Mapping.** Für den migrierenden ISB sind das echte Wiederverwendungs-Landkarten; der lange technologiespezifische Schwanz (Fax, z/OS, EFS) ist korrekt, nur mit abnehmendem Grenznutzen.

Zu viel ist es dagegen an drei benennbaren Stellen:

1. **Methodik-Sauger** (Befund C): 31 der 76 Streichkandidaten stecken in GC.3.1.1, VRB.4.1, PERF.3.1.4 und PERF.4.1. Für den ISB sind diese Listen Prüfzeit ohne Ertrag.
2. **Anbieterseiten-Zwillinge:** OPS.3.2-Sätze (Anbieter-Baustein) spiegeln bereits gemappte, fast wortgleiche Nutzerseiten-Sätze (OPS.2.3) in kundenseitige BES/DLS-Controls — 4 Fälle, totes Gewicht mit Rollenverwechslungs-Risiko.
3. **Redundanz und Fragmente:** 13 *doppelt*-Paare auf Nachbarsätze gleicher Substanz; dazu Tokenizer-Fragmente, die eine Teilanforderung doppelt zählen (OPS.1.1.1.A26 S2 endet auf „(engl.", S3 ist nur „Predictive Maintenance) genutzt wird."; ebenso INF.13.A18 S3/S4).

**Boilerplate-Paradox:** Die wortgleiche Richtlinien-Abweichungsklausel („Wird die Richtlinie verändert oder von ihr abgewichen …") ist 10-mal in UMS.5.2 und 8-mal in UMS.5.1 gemappt — korrekt, aber Masse *und* Lücke zugleich, denn zahlreiche weitere Bausteine mit identischer Klausel fehlen. Solche Satz-Familien gehören entweder komplett erfasst oder einmal als Muster referenziert.

## 7 Korrektheit im engen Sinn: Satzzitate und die vier Fehltreffer

Die handwerkliche Basis ist solide: Nur **6 von 943 Satzangaben** zitieren den falschen Träger (z. B. APP.5.3.A7: inhaltsleerer Verweissatz S2 statt Substanzträger S1; SYS.1.5.A4: S3 statt des direkten Treffers S2). Alle geprüften IDs existieren im jeweiligen Katalogstand. Häufiger ist das Spiegelbild: **61 Paare mit fehlendem Zusatzträger** — der *stärkste* Satz derselben Anforderung blieb unzitiert (etwa APP.4.4.A3 S4 „MÜSSEN sehr restriktiv vergeben werden" bei BER.4.1, oder die Aktivierungs-Sätze in KONF.10.2, wo systematisch der Standards-Satz statt des „MUSS verschlüsselt werden"-Satzes zitiert wird).

Die vier echten Fehltreffer (inhalt=nein), alle adversarial bestätigt:

| Paar | Befund |
|---|---|
| STM.3.1 → ISMS.1.A11:S5 | Homonym „Sicherheitsniveau" (Einstufung vs. erreichtes Niveau); einziges Paar des Controls |
| VRB.4.1 → OPS.1.1.3.A9:S6 | Hardware-Störungsbeseitigung als ISMS-Korrekturmaßnahme, allein übers Wort „Fehler" |
| GC.11.1 → INF.12.A10:S8 | ISMS-Dokumentenlenkung subsumiert kein Dokumentenmanagement der Verkabelungs-Fachdoku |
| DEV.5.2 → SYS.3.2.1.A5:S1 | Rollenverwechslung: beschaffungsseitige Prüfpflicht als Pendant zur herstellerseitigen Informationspflicht — Begründung ehrlich („Pendant"), als Wiederverwendungssignal dennoch leer; strengstes der vier Urteile, grenzwertig wäre vertretbar |

## 8 Beifang: Lücken-Verdachte an sonst guten Controls

Nicht Prüfauftrag, aber zu auffällig zum Weglassen — kanonische ED23-Anker, die in der vollständigen Paarliste des jeweiligen Controls fehlen (Kandidaten für einen gerichteten Mini-Nachfass, kein Vollauf nötig):

- **KONF.7.4** (Angriffserkennung im Netzverkehr) ohne SYS.1.1.A27 — die kanonische Quelle „Hostbasierte Angriffserkennung"; ein ISB mit umgesetztem H-IDS sieht seine Vorarbeit nicht.
- **KONF.10.2** (Krypto in Anwendungen) ohne APP.3.2.A11 (Webserver-TLS) und APP.4.3.A24 (DB-Verschlüsselung) — ausgerechnet die naheliegendsten Treffer.
- **GC.1.2** (Freigabe durch die Leitung) ohne ISMS.1.A3 — die prominenteste Leitungsfreigabe des ED23 (Inkraftsetzung der Leitlinie).
- **DET.3.1.6** ohne SYS.1.1.A10 (fordert wörtlich „Systemstarts und Reboots"); **DET.3.1.8** ohne OPS.1.1.7.A25:S1.
- **BER.2.4** ohne OPS.1.1.5.A3 (Ereignisliste „Einrichten/Ändern von Benutzenden, Gruppen und Berechtigungen").
- **ASST.4.2** ohne NET.3.3 (VPN) und E-Mail-Verschlüsselung trotz PGP-Beispiel in der eigenen Guidance; **ASST.5.2** ohne OPS.1.1.3 (Patch/Firmware) trotz Guidance-Nennung.
- **VRB.4.1** ohne DER.3.1.A5:S2 (Richtlinie zur Lenkung von Korrekturmaßnahmen — der direkteste Anker fehlt, während 13 dünne hängen); **REA.2.6** ohne DER.2.1.A6 (Wiederherstellung).
- **PERS.1.1.2** ohne die Zuständigkeitsregelungen aus OPS.1.1.3, obwohl die eigene Guidance das Control an den Änderungsprozess bindet.

## 9 Empfehlungen, priorisiert

1. **Relationstypen-Nachlauf** — die wirkungsvollste Einzelmaßnahme: nur `relationship` und `remarks` neu bewerten, Paare bleiben. Prüfregel explizit: „Enthält der ED23-Satz eine Pflicht, die das GS++-Statement nicht subsumiert (zweites Verb, zweite Pflicht, andere Phase) → `intersects-with`." Plus Familien-Konsistenz: gleicher ED23-Satztyp ⇒ gleicher Relationstyp. Betroffen ~16 % der Paare; billig, weil Kandidatensuche und Verify entfallen.
2. **Begründungs-Stilregel:** „deckt … ab" nur bei superset/equal; bei subset/intersects Pflichtformel „trifft Teilaspekt X, Y bleibt offen". Kein Statement-/Guidance-Referat ohne Wortlaut-Deckung (schließt die vier Erfindungsfälle aus). KANN/SOLLTE des GS++-Controls nie als „fordert".
3. **Drop-Liste abarbeiten:** 76 Paare (Anhang), davon die 4 inhalt=nein sofort; Schwerpunkt GC.3.1.1, VRB.4.1, PERF.3.1.4/PERF.4.1 und die OPS.3.2-Zwillinge.
4. **Tokenizer-Fix + Dedup:** Klammer-Abkürzungen („(engl.") reißen Sätze auseinander und erzeugen Doppel-Paare; Nachbarsatz-Duplikate gleicher Substanz zusammenführen.
5. **Gerichteter Lücken-Nachfass** über die Verdachtsliste aus Abschnitt 8 — passt als erster Anwendungsfall für die noch offene Sparplan-Maßnahme „inkrementelle Läufe".
6. **RISK als Korpus-Lücke ausweisen** (Report-Abschnitt Migrationsfolgen + Tool-Anzeige), statt sie durch ein dünnes Paar zu verdecken.
7. **Doku-Notiz:** Fundrichtung „beide" ist ein Konfidenz-, kein Qualitätssiegel — der belegte Erfindungsfall ASST.7.7 war beidseitig bestätigt.

## 10 Grenzen der Prüfung

- Stichprobe: 18,3 % der Paare, 96 von 867 gemappten Controls (11,1 %). Die Stratifizierung übergewichtet paarreiche Controls bewusst; die Drop-Quote von 8,1 % ist auf das Gesamtmapping nur als Größenordnung übertragbar (~350–450 Paare), mit Schwerpunkt Methodik-Praktiken.
- Reviewer sind LLM-Instanzen (18 unabhängige, identische Anweisung, strenge Kalibrierung). Gegenmaßnahme: alle Extremurteile wurden adversarial gegen die Quelltexte nachgeprüft — 7 von 7 bestätigt, eine Abstufung (DEV.5.2).
- „Grenzwertig" ist bewusst streng kalibriert; wer die 120 grenzwertigen Paare als akzeptabel wertet, liest die Inhaltsqualität als 99,6 %.
- Lücken-Verdachte (Abschnitt 8) sind Verdachte aus Domänenwissen, nicht das Ergebnis einer Vollsuche.

## Anhang: Alle 76 Streichkandidaten

Streichung heißt: Empfehlung der Reviewer (inhalt=nein plus irreführend-grenzwertige Paare). Vor dem Entfernen je Paar kurz gegenprüfen — die Urteile der drei Methodik-Sauger sind belastbar, Einzelfälle wie DEV.5.2 sind Ermessenssache.

| GS++-Control | Streichkandidaten (ED23:Satz) |
|---|---|
| ARCH.5.1 | INF.14.A19:S4, SYS.1.5.A4:S3 |
| ARCH.8.1 | SYS.1.5.A9:S6 |
| ASST.4.2 | SYS.1.8.A24:S1 |
| ASST.5.2 | OPS.1.1.1.A26:S3, INF.13.A18:S4, INF.13.A17:S1 |
| BER.4.1 | APP.4.2.A16:S6, CON.11.1.A8:S2 |
| BES.4.2 | APP.6.A1:S2, CON.8.A17:S2 |
| BES.5.13.1 | OPS.3.2.A6:S2 |
| BES.7.1.1 | OPS.3.2.A13:S4 |
| DET.6.1.2 | NET.1.2.A26:S5, OPS.1.1.7.A15:S8, OPS.1.2.2.A8:S6, SYS.1.7.A16:S4 |
| DEV.1.1 | INF.14.A7:S4 |
| DEV.5.2 | SYS.3.2.1.A5:S1 |
| DLS.1.1 | OPS.3.2.A6:S1 |
| DLS.2.2 | OPS.3.2.A10:S1 |
| GC.11.1 | INF.12.A10:S8 |
| GC.3.1.1 | APP.3.2.A7:S1, APP.6.A2:S5, DER.1.A2:S3, NET.3.2.A21:S2, OPS.1.1.5.A8:S2, OPS.2.2.A2:S4 |
| GEB.10.2.7 | INF.2.A8:S4 |
| KONF.10.2 | APP.5.4.A16:S3, APP.4.2.A31:S3 |
| KONF.2.4 | APP.3.1.A12:S2, SYS.2.2.3.A19:S4, SYS.3.2.3.A13:S2 |
| NOT.3.1 | NET.1.2.A38:S1, OPS.1.2.5.A21:S4 |
| NOT.4.2 | SYS.3.3.A11:S1 |
| PERF.3.1.4 | APP.3.1.A22:S2, APP.3.2.A16:S2, APP.4.2.A27:S1, APP.4.3.A20:S1, DER.4.A14:S9, IND.1.A12:S5, NET.2.1.A14:S1, NET.3.1.A23:S2, SYS.1.5.A19:S1, SYS.1.8.A18:S1 |
| PERF.4.1 | ISMS.1.A6:S8 |
| PERS.1.1.2 | ISMS.1.A1:S5 |
| PERS.2.2 | APP.7.A5:S4 |
| PERS.4.2 | INF.11.A7:S7, ORP.2.A15:S3 |
| REA.2.1 | OPS.1.2.2.A8:S7 |
| REA.2.6.1 | INF.11.A6:S7 |
| SENS.7.1 | APP.5.3.A7:S2, SYS.4.4.A9:S2 |
| STM.1.2 | INF.14.A2:S3 |
| STM.3.1 | ISMS.1.A11:S5 |
| TEST.3.1 | APP.2.3.A10:S4, INF.14.A3:S8, OPS.1.2.2.A16:S2 |
| UMS.5.1 | CON.11.1.A1:S9 |
| UMS.5.2 | NET.3.4.A20:S4 |
| VRB.4.1 | APP.3.1.A22:S4, APP.3.2.A16:S4, DER.1.A13:S4, INF.13.A12:S12, INF.13.A6:S6, INF.14.A3:S11, NET.2.1.A10:S5, NET.2.2.A1:S8, NET.3.1.A23:S5, OPS.1.1.3.A9:S6, OPS.1.2.2.A13:S4, SYS.1.5.A19:S4, SYS.3.2.2.A20:S3 |

---

*Rohdaten in diesem Ordner: `results/` (18 Reviewer-Protokolle, 943 Einzelurteile), `tally.json` (maschinenlesbar), `dossiers/` (20 Praktik-Dossiers mit amtlichen Satztexten), `gen_dossiers.py`, `tally.py`, `review_instructions.md`. Interaktive Fassung: https://claude.ai/code/artifact/34d3632b-8fa7-4326-89c8-f26faeaf4d86 (privat, bei Bedarf teilen).*
