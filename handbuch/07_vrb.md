# Kapitel 7: VRB – Verbesserung

**Handbuch zur Grundschutz++ Methodik · Kapitel-Version 0.6 (Entwurf)**
Stand: 2026-10-26 · Normative Basis: `BSI-Methodik-Grundschutz++-catalog.json`, Build 2026-10-22; BSI-Standard 300-1 (Version 1.0, 20.10.2026) · Gliederungsbezug: Kapitel 7 gemäß `00_gliederung_v0.1.md`
Änderung 0.6: Standard 300-1 eingearbeitet (Prozessschritt 5 in 7.0, Korrektur- und Verbesserungsplan in 7.5, Evaluation in 7.6); Restrisiko-Frage in 7.5 und 7.9 auf den Stand des Standards gebracht.

## 7.0 Einordnung: die Act-Phase des Zyklus

Der BSI-Standard 200-2 behandelt „Aufrechterhaltung und kontinuierliche Verbesserung der Informationssicherheit" als eigenes Kapitel 10, als Erzählung über den laufenden Betrieb. Grundschutz++ macht daraus die kleinste Praktik der Methodik: zehn Controls, 8 MUSS und 2 SOLLTE, Aufwandsstufen fast durchgängig null (nur VRB.6.2 und VRB.7.1 tragen `effort_level` 2). Klein heißt aber nicht nebensächlich: VRB ist die Act-Phase des Zyklus, und laut Guidance zu VRB.1.1 schließt die kontinuierliche Verbesserung „den PDCA-Zyklus der Methodik ab". Ohne einen nachweisbaren VRB-Durchlauf bleibt auch GC.1.1 unerfüllt, dessen Erfüllungskriterium der mindestens einmal vollständig durchlaufene Zyklus ist.

Die Praktik trennt sauber zwei Denkrichtungen, die in der Praxis gern verschwimmen: reaktiv und proaktiv. Reaktiv: Nicht-Konformitäten erfassen, Ursachen analysieren, Korrekturmaßnahmen festlegen (VRB.2, VRB.4.1). Proaktiv: Verbesserungspotenziale auch ohne vorangegangenes Problem identifizieren, bewerten und in Maßnahmen übersetzen (VRB.3, VRB.4.2). Beide Stränge laufen in der Priorisierung zusammen (VRB.5.1) und münden in dasselbe Dokument, das schon UMS führt: den Umsetzungsplan. VRB erzeugt also keine eigene Maßnahmenwelt, sondern speist die bestehende Umsetzungsmaschinerie; die Wirksamkeitsprüfung (VRB.6) kontrolliert anschließend, ob die Verbesserung tatsächlich eingetreten ist. In der Katalogreihenfolge steht VRB vor PERF; fachlich konsumiert VRB die Ergebnisse, die PERF produziert (Auditberichte, Managementbewertung, Monitoring-Daten). Das Überblickskapitel 2 ordnet diesen Zyklus ein. Der Standard 300-1 bestätigt die Reihenfolge: Die kontinuierliche Verbesserung ist dort Prozessschritt 5 nach der Überwachung (Standard 300-1, Kap. 6 (S. 26 f.)), mit denselben Bausteinen wie die Praktik: Umgang mit Nicht-Konformitäten (VRB.2), Identifikation von Verbesserungspotenzialen (VRB.3), Korrektur- und Verbesserungsplan (VRB.4, VRB.5), Evaluation (VRB.6); die Behandlung von Compliance-Verstößen (VRB.7) nennt die Einleitung des Kapitels. Als Ergebnis des Schritts „werden Schwachstellen und geänderte Bedrohungslagen identifiziert", die „einen Zyklus der Risikobetrachtung" auslösen.

## 7.1 VRB.1 Kontinuierliche Verbesserung: das Verfahren hinter dem Schlagwort

**Anforderungsbezug.**

| Control | Verbindlichkeit | Kern | Dokument |
|---|---|---|---|
| VRB.1.1 Verfahren zur kontinuierlichen Verbesserung | MUSS | Verfahren zur kontinuierlichen Verbesserung des ISMS verankern | keines zugeordnet |

> „Verbesserung MUSS ein Verfahren zur kontinuierlichen Verbesserung des ISMS verankern." (VRB.1.1)

Die Guidance präzisiert den Anspruch: Erkenntnisse aus der Überwachung werden in konkrete Verbesserungsmaßnahmen umgesetzt, Änderungen am ISMS erfolgen geplant, strukturiert und systematisch dokumentiert, damit Vergleichbarkeit, Nachvollziehbarkeit und eine kohärente Managementbewertung möglich bleiben.

**Umsetzungshinweise.** „Kontinuierliche Verbesserung" ist das meistgenannte und am seltensten belegte Versprechen der ISMS-Welt. VRB.1.1 verlangt das Gegenteil von guten Vorsätzen: ein Verfahren mit Eingängen (Auditberichte, Vorfälle, Monitoring, Managementbewertung), definierten Verarbeitungsschritten (die folgenden VRB-Controls) und dokumentierten Ausgängen (Maßnahmen im Umsetzungsplan). Bauen Sie das Verfahren als Kreislauf mit festem Takt, etwa quartalsweise, und führen Sie ein zentrales Register aller Verbesserungs- und Korrekturvorgänge; ohne Register lässt sich weder VRB.2.2 noch VRB.6.1 sinnvoll bedienen.

**Audit-Perspektive.** Das Auditierungsschema verlangt ausdrücklich, dass Abweichungen und Empfehlungen aus vorangegangenen Audits im Rahmen des kontinuierlichen Verbesserungsprozesses berücksichtigt und auditiert werden. Übertragen heißt das: Der Auditor bringt die Liste der Abweichungen und Empfehlungen aus dem Vorjahr mit und prüft, was daraus geworden ist. Ein Verbesserungsverfahren, das alte Auditfeststellungen nicht nachweisbar verarbeitet hat, fällt genau an dieser Stelle auf.

**Typische Fehler.** Verbesserung passiert nur als Reaktion auf Audits, nie aus eigenem Antrieb. Es gibt kein Register, sodass niemand sagen kann, welche Verbesserungen im letzten Jahr beschlossen, umgesetzt und geprüft wurden. Oder Änderungen am ISMS erfolgen ad hoc am Verfahren vorbei, womit die von der Guidance geforderte Nachvollziehbarkeit entfällt.

## 7.2 VRB.2 Nicht-Konformitäten: Ursachen statt Symptome

**Anforderungsbezug.**

| Control | Verbindlichkeit | Kern | Dokument |
|---|---|---|---|
| VRB.2.1 Umgang mit Nicht-Konformitäten | MUSS | Methode zur Überprüfung von Nicht-Konformitäten hinsichtlich Ursachen und Wiederauftreten festlegen | keines zugeordnet |
| VRB.2.2 Anpassung des ISMS | MUSS | Notwendigkeit zur ISMS-Anpassung wegen Nicht-Konformitäten `{{regelmäßig}}` überprüfen | keines zugeordnet |

Die Guidance zu VRB.2.1 verlangt die systematische Erfassung aller Nicht-Konformitäten unabhängig von der Quelle (interne Audits, externe Prüfungen, Vorfälle, Regelbetrieb) und eine Ursachenanalyse, die ausdrücklich bis zu den Grundursachen reicht (Root-Cause-Analysis). VRB.2.2 hebt den Blick: Wiederholte oder systematische Nicht-Konformitäten sind Anlass, die zugrundeliegenden Prozesse, Richtlinien oder Verantwortlichkeiten selbst anzupassen, nicht nur den Einzelfall zu flicken.

**Umsetzungshinweise.** Definieren Sie, was bei Ihnen als Nicht-Konformität gilt, und zwar breiter als „Auditfeststellung": auch der Vorfall, der eine nicht gelebte Regelung offenlegt, gehört hinein. Für die Ursachenanalyse genügt in den meisten Fällen ein diszipliniertes Fünf-Warum oder ein kurzes Ishikawa; entscheidend ist, dass die Analyse dokumentiert wird und die Korrektur (VRB.4.1) an der Grundursache ansetzt. Für VRB.2.2 hilft das Register aus VRB.1: Wer Nicht-Konformitäten kategorisiert erfasst, sieht Wiederholungsmuster im Quartalsblick; wer sie in Einzeltickets verstreut, sieht nichts. Setzen Sie den Parameter `{{regelmäßig}}` passend zum Takt des Verbesserungsverfahrens.

**Audit-Perspektive.** Der Auditor prüft die Kette an konkreten Fällen: Nicht-Konformität erfasst, Ursache analysiert, Korrektur abgeleitet, Wiederauftreten bewertet. Wiederholte gleichartige Feststellungen über mehrere Audits hinweg sind das stärkste Indiz, dass VRB.2.2 nicht funktioniert, und nach der Systematik des Auditierungsschemas können sich mehrere geringfügige Abweichungen zu einer schwerwiegenden summieren; genau dieses Muster entsteht, wenn Symptome geflickt und Ursachen ignoriert werden.

**Typische Fehler.** Die Ursachenanalyse endet beim schuldigen Administrator statt beim fehlenden Prozess. Nicht-Konformitäten aus Vorfällen und aus Audits leben in getrennten Welten (Ticketsystem hier, Auditbericht dort) und werden nie zusammen ausgewertet. Die ISMS-Anpassung nach VRB.2.2 unterbleibt, weil jede Feststellung als bedauerlicher Einzelfall gilt.

## 7.3 VRB.3 Verbesserungspotenziale: der proaktive Strang

**Anforderungsbezug.**

| Control | Verbindlichkeit | Kern | Dokument |
|---|---|---|---|
| VRB.3.1 Identifikation von Verbesserungspotenzialen | MUSS | Methode zur Überprüfung und Bewertung von Verbesserungspotentialen samt Vor- und Nachteilen festlegen | keines zugeordnet |

Die Guidance stellt den Gegensatz zum reaktiven Strang ausdrücklich heraus: Optimierungsmöglichkeiten erkennen, ohne dass vorher etwas schiefging. Als Quellen nennt sie die Bewertung des Umfelds einschließlich der Gefährdungslage, die Auswertung des Umsetzungsplans, Auditergebnisse und Sicherheitsvorfälle sowie Ad-hoc-Eingaben; als Stoßrichtungen neue Technologien und Methoden, Sicherheitskultur, Erweiterung des Anwendungsbereichs und bessere Integration in andere Managementsysteme. Und sie verlangt Bewertungsdisziplin: Risikoreduktion, Ressourcenaufwand, strategische Bedeutung, Synergien und Nachhaltigkeit der Verbesserung.

**Umsetzungshinweise.** Institutionalisieren Sie eine Eingangstür für Vorschläge (Fachbereiche, Betrieb, Externe) und einen festen Bewertungstermin im Verbesserungstakt. Die Bewertungskriterien aus der Guidance ergeben eine brauchbare Vier-Felder-Entscheidung: hoher Nutzen und geringer Aufwand wird gemacht, hoher Nutzen und hoher Aufwand wird geplant, der Rest wird dokumentiert abgelehnt. Wichtig ist das Ablehnen mit Begründung; ein Potenzialregister, in dem alles ewig „in Prüfung" steht, ist keine Methode, sondern ein Friedhof.

**Audit-Perspektive.** Als MUSS-Anforderung braucht VRB.3.1 den Nachweis der Methode und ihrer Anwendung. Der Auditor wird nach Beispielen fragen: Welche Potenziale wurden im letzten Zyklus identifiziert, wie bewertet, was wurde daraus? Eine leere Liste ist verdächtig, eine Liste ohne Bewertungsspur ebenso. Positiv gewendet: Ein gepflegtes Potenzialregister ist einer der einfachsten Belege für ein lebendiges ISMS.

**Typische Fehler.** Verbesserung wird mit Beschaffung verwechselt, und das Register füllt sich mit Toolwünschen ohne Bezug zu den Sicherheitszielen. Vorschläge aus dem Betrieb versanden, weil es keinen Bewertungstermin gibt. Die Vor- und Nachteile werden nicht dokumentiert, sodass dieselben Ideen jedes Jahr neu diskutiert werden.

## 7.4 VRB.4 Korrektur- und Verbesserungsmaßnahmen: zwei Sorten, ein Anspruch

**Anforderungsbezug.**

| Control | Verbindlichkeit | Kern | Dokument |
|---|---|---|---|
| VRB.4.1 Korrekturmaßnahmen | MUSS | angemessene Korrekturmaßnahmen zur Beseitigung der Ursachen von Fehlern festlegen | keines zugeordnet |
| VRB.4.2 Verbesserungsmaßnahmen | MUSS | angemessene Maßnahmen zur Nutzung von Verbesserungspotentialen samt Vor- und Nachteilen festlegen | keines zugeordnet |

Die Guidance zu VRB.4.1 setzt drei Qualitätskriterien: Korrekturen adressieren Grundursachen statt Symptome, sie sind verhältnismäßig zum Risiko, und sie wirken nachhaltig gegen Wiederholung. Als Maßnahmenarten nennt sie organisatorische Anpassungen, personelle oder disziplinarische Maßnahmen, infrastrukturelle und technische Änderungen sowie strategische Maßnahmen, die eine Entscheidung der Institutionsleitung erfordern. VRB.4.2 überträgt denselben Anspruch auf den proaktiven Strang.

> **Katalogfund:** VRB.2 spricht durchgängig von „Nicht-Konformitäten", das Statement von VRB.4.1 von „Ursachen von Fehlern". Ob „Fehler" bewusst weiter gefasst ist als „Nicht-Konformität" oder nur eine Formulierungsvariante, gibt der Katalog nicht her; dieses Handbuch liest beide Begriffe als denselben Gegenstand. Auffällig außerdem: Die Formel „unter Berücksichtigung der damit verbundenen Vor- und Nachteile" wandert wortgleich durch VRB.3.1, VRB.4.2 und VRB.6.2, wo sie im Kontext der Bewertung erreichter Verbesserungen semantisch nicht recht passt (vgl. Abschnitt 7.6).

**Umsetzungshinweise.** Halten Sie die Trennung Korrektur/Verbesserung im Register durch, denn sie steuert die Dringlichkeit: Korrekturen haben eine offene Wunde hinter sich und gehören priorisiert; Verbesserungen konkurrieren nach Nutzen. Bei disziplinarischen Maßnahmen gilt: Sie sind laut Guidance eine mögliche Maßnahmenart, aber wer regelmäßig bei der Person statt beim Prozess landet, hat meist die Ursachenanalyse abgekürzt, und die Fehlerkultur aus GC.3.1.4 gleich mit beschädigt. Strategische Maßnahmen mit Leitungsvorbehalt gehören über den Managementbericht (PERF.4.1.9) auf den Tisch der Leitung, nicht in die stille Warteschlange.

**Audit-Perspektive.** Geprüft wird die Passung: Steht die Korrektur in erkennbarem Verhältnis zur analysierten Ursache? Eine Schulungsmaßnahme als Antwort auf einen Architekturfehler ist die klassische Fehlpassung, die ein erfahrener Auditor sofort hinterfragt. Bei Verbesserungsmaßnahmen zählt die dokumentierte Abwägung der Vor- und Nachteile, die das Statement ausdrücklich verlangt.

**Typische Fehler.** Jede Korrektur heißt „Sensibilisierung", weil das billig ist und nach Maßnahme aussieht. Maßnahmen werden festgelegt, aber nie mit Prioritäten und Fristen versehen, womit VRB.5.1 leerläuft. Verbesserungen werden umgesetzt, ohne die Nachteile (Betriebsaufwand, neue Abhängigkeiten) je bewertet zu haben.

## 7.5 VRB.5 Korrektur- und Verbesserungsplan: zurück in den Umsetzungsplan

**Anforderungsbezug.**

| Control | Verbindlichkeit | Kern | Dokument |
|---|---|---|---|
| VRB.5.1 Priorisierung von Maßnahmen | MUSS | Maßnahmen zur Korrektur und Verbesserung Prioritäten zuweisen | Umsetzungsplan |

Die Guidance ist an dieser Stelle das heimliche Pflichtenheft des Umsetzungsplans: Verbesserungsmaßnahmen fließen in den Umsetzungsplan ein und werden dort mit Zuständigen, Anforderungsbeschreibung, Zielobjekt beziehungsweise Anwendungsbereich, verantwortlicher Stelle, Start- und Zieldatum, Prioritäten, Umsetzungsstatus, ergänzenden Aktivitäten wie Schulungen, Risiken inklusive Begründung (was bleibt offen, was wurde nicht umgesetzt und warum), Ressourcenplanung, Abhängigkeiten sowie Datum der Freigabe und Unterschrift des Risikoeigentümers nachverfolgt.

Der Standard 300-1 nennt das Instrument „Korrektur- und Verbesserungsplan": Die Vorschläge „müssen in einen Korrektur- und Verbesserungsplan eingebettet werden", priorisiert nach verfügbaren Ressourcen, Quick-Wins und größtem Verbesserungspotenzial, und „Der Korrektur- und Verbesserungsplan wird in den Umsetzungsplan aufgenommen" (Standard 300-1, Kap. 6.3 (S. 27)). Es bleibt also bei einem Plan. Die Mindestangaben, die der Standard je Maßnahme verlangt (Anforderung, Datum, Person, Nachweiszuordnung, Historie; Kap. 4.3, Kapitel 6.2), sind eine Teilmenge der Feldliste aus der Guidance.

**Umsetzungshinweise.** Es gibt genau einen Umsetzungsplan, und VRB schreibt in denselben Plan wie UMS; bauen Sie keine zweite Maßnahmenliste. Die Feldliste aus der Guidance taugt als Spaltendefinition für den Plan insgesamt und beantwortet nebenbei die in Kapitel 6 offene Frage nach der Quelle der Abhängigkeiten zumindest praktisch: Der Plan soll sie ausweisen. Bemerkenswert ist die Unterschrift des Risikoeigentümers als Nachverfolgungsfeld; das ist die operative Landestelle der Risikoübernahme, die das Auditierungsschema für nicht umgesetzte Anforderungen verlangt. Der Standard 300-1 hat die SOLLTE-Lücke von UMS.1.2 inzwischen geschlossen: Restrisiken gehen zur Freigabe an die Institutionsleitung, die Umsetzungsplanung autorisieren die Risikoeigentümer (Kap. 4.2.3 (S. 19), Mindestkriterien 30 und 31; Kapitel 6.1). Außerhalb der Methodik ist diese Stelle auch im Katalog unterfüttert: Der Anwenderkatalog importiert RISK.1.10 (Umsetzungsplanung durch die Risikoeigentümer autorisieren, MUSS, Dokument Umsetzungsplan) samt wortgleicher Feldliste in der Guidance sowie RISK.1.3 (Rolle des Risikoeigentümers, MUSS); Details im Exkurs in Kapitel 4.12.

**Audit-Perspektive.** Der Auditor liest den Umsetzungsplan als Integrationsnachweis: Finden sich die Korrekturen aus den letzten Auditfeststellungen und die Verbesserungen aus dem Potenzialregister mit Priorität, Frist und Zuständigem wieder? Fehlen die Freigaben und Unterschriften der Risikoeigentümer bei offenen Risiken, trifft die Feststellung VRB.5.1 und die Risikosteuerung insgesamt.

**Typische Fehler.** VRB führt eine eigene Excel neben dem Umsetzungsplan, und beide widersprechen sich. Prioritäten werden vergeben, aber nie gegen die laufenden UMS-Maßnahmen abgewogen, sodass Verbesserungen ewig hinter dem Tagesgeschäft stehen. Das Unterschriftenfeld des Risikoeigentümers bleibt leer, weil niemand die Rolle besetzt hat (GC.12.1 lässt grüßen).

## 7.6 VRB.6 Wirksamkeitsprüfung: hat es gewirkt, und woher wissen wir das?

**Anforderungsbezug.**

| Control | Verbindlichkeit | Kern | Dokument |
|---|---|---|---|
| VRB.6.1 Überprüfung der erreichten Verbesserung | MUSS | Wirksamkeit umgesetzter Korrektur- und Verbesserungsmaßnahmen `{{regelmäßig}}` testen | keines zugeordnet |
| VRB.6.2 Bewertung der erreichten Verbesserung | SOLLTE | Verfahren zur Bewertung der erreichten Verbesserung verankern | keines zugeordnet |

> „Verbesserung MUSS die Wirksamkeit der umgesetzten Korrektur- und Verbesserungsmaßnahmen `{{regelmäßig}}` testen." (VRB.6.1)

Das Modalverb-Gefälle ist bemerkenswert: Testen ist MUSS, das bewertende Verfahren darüber (KPIs vor und nach der Umsetzung, interne Audits, technische Überprüfungen, Trendvergleich mit früheren Bewertungen) nur SOLLTE mit `effort_level` 2. Der Katalog verlangt also zwingend den Einzelnachweis der Wirkung, und empfiehlt dringend die systematische Auswertung darüber. Der Standard 300-1 nennt den Schritt „Evaluation" und verlangt dafür klare, messbare Wirksamkeitskriterien je Maßnahme, gezielte Tests, Audits oder Überprüfungen nach Abschluss der Umsetzung, die Bewertung, ob Nicht-Konformitäten beseitigt und Verbesserungen erreicht wurden, und die Dokumentation der Ergebnisse (Standard 300-1, Kap. 6.4 (S. 27)); formuliert ist das als Sollen („sollten folgende Aspekte berücksichtigt werden"), also auf der Stufe von VRB.6.2.

**Umsetzungshinweise.** Definieren Sie das Wirksamkeitskriterium bei der Maßnahmenfestlegung, nicht erst beim Test; „Maßnahme umgesetzt" und „Maßnahme wirksam" sind zwei verschiedene Aussagen, und nur die zweite interessiert hier. Ein Test kann klein sein: die Stichprobe, ob die verschärfte Passwortrichtlinie technisch erzwungen wird; die Kontrolle, ob die Nicht-Konformität aus dem Vorjahr erneut auftritt. Für VRB.6.2 gilt: Wer die Ziele aus GC.5.1 messbar formuliert hat, bekommt die Vorher-nachher-KPIs fast geschenkt; die Ergebnisse fließen über UMS.6.2 in die Fortschreibung des Umsetzungsplans und über den Managementbericht (PERF.4.1.8) an die Leitung.

**Audit-Perspektive.** Die Wirksamkeitsprüfung ist der Unterschied zwischen einem Maßnahmen-Abhakregime und einem Managementsystem, und Auditoren prüfen sie genau deshalb gern an den unbequemsten Fällen: den Korrekturen zu früheren Auditfeststellungen. Eine als „umgesetzt" gemeldete Korrektur, deren Wirkung nie getestet wurde und die beim Nachtest versagt, ist doppelt teuer, als offene Nicht-Konformität und als Beleg gegen VRB.6.1.

**Typische Fehler.** Wirksamkeit wird mit Fertigstellung verwechselt und der Test durch den Statuswechsel im Ticket ersetzt. Getestet wird nur, was leicht zu testen ist. Die Bewertung nach VRB.6.2 unterbleibt kommentarlos, obwohl das SOLLTE eine dokumentierte Auseinandersetzung verlangt hätte.

## 7.7 VRB.7 Compliance-Verstöße: Konsequenz mit Augenmaß

**Anforderungsbezug.**

| Control | Verbindlichkeit | Kern | Dokument |
|---|---|---|---|
| VRB.7.1 Behandlung von Compliance-Verstößen | SOLLTE | Verfahren zur Behandlung von Verstößen unter Berücksichtigung der Betroffenenrechte verankern | Compliance-Verpflichtungen |

Die Guidance verlangt eine klare Definition und Kategorisierung von Verstößen, Melde- und Eskalationswege, einen systematischen Untersuchungs- und Dokumentationsprozess, eine Entscheidungsfindung über angemessene Reaktionen und Konsequenzen sowie die Nachverfolgung beschlossener Maßnahmen.

**Umsetzungshinweise.** Der Halbsatz „unter Berücksichtigung der Betroffenenrechte" im Statement verdient Beachtung: Verstoßbehandlung berührt Arbeitsrecht, Datenschutz und Mitbestimmung, und ein Verfahren, das Beschuldigtenrechte ignoriert, produziert am Ende mehr Rechtsrisiko, als es Compliance schafft. Binden Sie Personalabteilung, Datenschutzbeauftragte und Personalvertretung bei der Verfahrensdefinition ein, nicht erst im Anwendungsfall; die Anhörungslogik aus GC.3.1.2 gilt sinngemäß. Und trennen Sie die Meldewege sauber von der Sanktion: Wer jede Meldung reflexhaft mit Konsequenzen beantwortet, bekommt keine Meldungen mehr, sondern Vertuschung; die konstruktive Fehlerkultur aus GC.3.1.4 und die Verstoßbehandlung aus VRB.7.1 müssen zusammenpassen.

**Audit-Perspektive.** Als SOLLTE-Control mit eigenem Dokumentenbezug (Compliance-Verpflichtungen) gilt das übliche Muster: Verfahren vorhanden und angewendet, oder Nichtumsetzung nachvollziehbar begründet. Der Auditor wird die Brücke zu PERF.2.1 schlagen: Wer bei der Compliance-Überwachung Verstöße identifiziert, muss zeigen können, was mit ihnen geschehen ist.

**Typische Fehler.** Das Verfahren existiert, aber niemand kennt den Meldeweg. Verstöße von Führungskräften werden anders behandelt als die von Mitarbeitenden, was das Verfahren insgesamt entwertet. Die Dokumentation unterbleibt aus falsch verstandener Diskretion, und im Wiederholungsfall fehlt jede Historie.

## 7.8 Dokumenten-Output der Praktik

| Dokument | Gefordert durch |
|---|---|
| Umsetzungsplan | VRB.5.1 |
| Compliance-Verpflichtungen | VRB.7.1 |

Acht der zehn Controls fordern kein Dokument (VRB.1.1, VRB.2.1, VRB.2.2, VRB.3.1, VRB.4.1, VRB.4.2, VRB.6.1, VRB.6.2), so wenig wie in keiner anderen Praktik. Das ist konsequent, weil VRB in die Dokumente der anderen Praktiken schreibt (Umsetzungsplan, Managementbericht), verlangt aber Disziplin: Nicht-Konformitäten-Register, Potenzialregister, Ursachenanalysen und Wirksamkeitstests brauchen einen gelenkten Ablageort nach GC.11.1, auch ohne Katalogzuordnung; sie sind die Evidenz, an der die gesamte Praktik im Audit hängt.

## 7.9 Offene Fragen und Katalogfunde

1. **Begriffspaar „Nicht-Konformität" / „Fehler".** VRB.2 und VRB.4.1 verwenden unterschiedliche Begriffe für mutmaßlich denselben Gegenstand; eine Definitionsklärung im Katalog stünde dem zentralen Begriffsapparat der Praktik gut an (vgl. Abschnitt 7.4).
2. **Wandernde Formel „Vor- und Nachteile".** Die Formulierung „unter Berücksichtigung der damit verbundenen Vor- und Nachteile" erscheint in VRB.3.1, VRB.4.2 und VRB.6.2; in VRB.6.2 (Bewertung bereits erreichter Verbesserungen) passt sie semantisch nicht und wirkt wie ein Kopierrest.
3. **Fast dokumentenfreie Praktik.** Acht von zehn Controls ohne `documentation`-Prop, obwohl die Guidance durchgängig Dokumentation verlangt (Register, Analysen, Testergebnisse). Ein künftiger Katalog-Build könnte hier Dokumente zuordnen; bis dahin gilt die freie Form unter GC.11.1.
4. **Risikoeigentümer-Unterschrift nur in der Guidance des Methodik-Teils.** Die Guidance zu VRB.5.1 beschreibt Freigabedatum und Unterschrift des Risikoeigentümers als Nachverfolgungsfelder des Umsetzungsplans; im Methodik-Teil ist beides nirgends normativ gefordert. Der Anwenderkatalog schließt die Lücke inzwischen teilweise: Die importierten Controls RISK.1.10 (Autorisierung der Umsetzungsplanung durch die Risikoeigentümer) und RISK.1.3 (Rolle des Risikoeigentümers) sind MUSS, gehören aber nicht zur Methodik (Kapitel 4.12, Exkurs). Nicht importiert wurde RISK.1.9 (Bestätigung des Restrisikos, SOLLTE); zusammen mit dem SOLLTE von UMS.1.2 bleibt die Restrisiko-Übernahme im Katalog weicher formuliert, als das Auditierungsschema sie prüft. *Durch den Standard 300-1 entschieden:* Restrisiken sind der Institutionsleitung zur Freigabe vorzulegen, die Umsetzungsplanung autorisieren die Risikoeigentümer (Mindestkriterien 30 und 31); der Katalog muss nachziehen (vgl. Abschnitt 6.9, Punkt 2; Anhang D, D4, D41).
5. **Korrektur- und Verbesserungsplan.** Der Standard 300-1 führt den Begriff (Kap. 6.3) und löst ihn im Umsetzungsplan auf; im Katalog kommt er nicht vor. Anhang C führt ihn als Synonym.

---

*Ende Kapitel 7 (v0.6). Review-Anmerkungen bitte gegen die Control-IDs und die Kapitel des Standards 300-1.*
