# Kapitel 2: Die Methodik im Überblick

**Handbuch zur Grundschutz++ Methodik · Kapitel-Version 0.6 (Entwurf)**
Stand: 2026-10-26 · Normative Basis: `BSI-Methodik-Grundschutz++-catalog.json`, Build 2026-10-22; Praktik-Definitionen aus `documentation/namespaces/practices.csv` (Repo-Snapshot 2026-10-23); BSI-Standard 300-1 (Version 1.0, 20.10.2026) · Gliederungsbezug: Kapitel 2 gemäß `00_gliederung_v0.1.md`
Änderung 0.6: neuer Abschnitt 2.7 mit der Zuordnung der fünf Prozessschritte des Standards 300-1 zu den Praktiken; Wirkfluss in 2.2 durch den Standard belegt; Parameter- und Dokumentzahlen auf den Build 2026-10-22 nachgerechnet.

## 2.1 Fünf Praktiken, ein Verfahren

Die Grundschutz++-Methodik besteht aus fünf Praktiken mit zusammen 95 Controls; hinzu kommen die vier RISK-Controls (RISK.1.1, RISK.1.3, RISK.1.5, RISK.1.10), die der Anwenderkatalog aus dem Katalog „BSI Anforderungen zum Risikomanagement" importiert und die neben der Methodik gelten (Exkurs in Kapitel 4.12). Der Namespace `practices.csv` definiert jede Praktik und ordnet ihr eine Nummer und einen Alternativnamen zu; die Kurzfassung:

| Praktik | Controls | Aufgabe (nach Namespace-Definition) | Handbuch |
|---|---|---|---|
| GC – Governance und Compliance | 35 (31 MUSS / 4 SOLLTE) | strategischer Rahmen: das „Was" und „Warum", Einbindung der Führungsebene, Integration externer und interner Anforderungen | Kapitel 4 |
| STM – Strukturmodellierung | 15 (14 / 1) | aus dem Katalog ein individuelles Anforderungspaket für die Institution generieren; auch bekannt als „Modellierung" | Kapitel 5 |
| UMS – Umsetzung | 11 (10 / 1) | systematische Planung, Implementierung und Dokumentation der Maßnahmen; „Realisierung von Sicherheitsmaßnahmen" | Kapitel 6 |
| VRB – Verbesserung | 10 (8 / 2) | kontinuierliche Weiterentwicklung; schließt den PDCA-Zyklus ab und stößt den neuen an | Kapitel 7 |
| PERF – Monitoring-Evaluation | 24 (13 / 11) | Überwachung und Bewertung; laut Namespace ausdrücklich die „Check-Phase" im PDCA-Zyklus | Kapitel 8 |

Die Arbeitsteilung in einem Satz: GC entscheidet, was gelten soll; STM übersetzt es in ein konkretes Anforderungspaket; UMS arbeitet das Paket ab; PERF misst, ob es wirkt; VRB macht aus den Messergebnissen Veränderung, und der Zyklus beginnt von vorn.

## 2.2 Der Wirkzyklus: PDCA mit einer Eigenheit in der Reihenfolge

Auf das klassische PDCA-Modell abgebildet: Plan sind GC und STM, Do ist UMS, Check ist PERF, Act ist VRB. Der Katalog selbst benennt die Zuordnung in den Namespace-Definitionen (PERF als Check-Phase, VRB als Abschluss und Neustart des Zyklus) und in der Guidance zu VRB.1.1. Die Eigenheit: Die Katalogreihenfolge stellt VRB vor PERF, der Wirkfluss läuft umgekehrt. Der Standard 300-1 bestätigt den Wirkfluss: Die Überwachung ist dort Prozessschritt 4, die kontinuierliche Verbesserung Prozessschritt 5, und als Ergebnis der Verbesserung werden Schwachstellen und geänderte Bedrohungslagen identifiziert, die einen neuen Zyklus der Risikobetrachtung auslösen (Standard 300-1, Kap. 5 und 6 (S. 22 bis 27)). Dieses Handbuch folgt der Katalogreihenfolge in der Kapitelfolge und beschreibt den Wirkfluss in Kapitel 8.6 im Detail; die Übergabepunkte sind konkret benannt: Auditfeststellungen und Monitoring-Befunde aus PERF landen als Nicht-Konformitäten und Verbesserungspotenziale in VRB (VRB.2, VRB.3), dessen Maßnahmen fließen in den Umsetzungsplan (VRB.5.1) und damit zurück in die Maschinerie von UMS, und der Managementbericht (PERF.4) verkettet die Zyklen, weil er den Status der Folgemaßnahmen der jeweils letzten Bewertung dokumentiert (PERF.4.1.1).

Zwei Takte halten den Zyklus zusammen. Der große: GC.1.1 gilt laut Guidance erst als erfüllt, wenn die komplette Vorgehensweise mindestens einmal vollständig durchlaufen wurde; der erste Zyklus ist also das Abnahmekriterium des ganzen ISMS. Der kleine: Neun der 15 Parameter der Methodik sind `{{regelmäßig}}`-Varianten (Kapitel 3.3), und jede Institution bestimmt mit ihrer Belegung selbst, wie schnell ihr Zyklus schlägt.

## 2.3 Die Praktik als Adressat

Jedes Statement der Methodik adressiert die Praktik selbst: „Governance und Compliance MUSS …", „Strukturmodellierung MUSS …". Das ist die auffälligste sprachliche Neuerung gegenüber der 200-2-Welt, und sie hat einen praktischen Sinn: Der Katalog schreibt nicht vor, welche Person oder Organisationseinheit die Leistung erbringt, sondern dass die Institution die Praktik so organisieren muss, dass das Ergebnis entsteht. Die Zuordnung zu Rollen geschieht an zwei definierten Stellen: strukturell über die Sicherheitsorganisation (GC.9: Rollen, Zuständigkeiten, Befugnisse, Stellvertretung, Interessenkonflikte) und fein über Zuständigkeits-Parameter (STM.5.1). Für ISBs heißt das umgekehrt: Wer im Audit gefragt wird, „wer ist bei Ihnen Strukturmodellierung?", muss auf Organigramm, Rollenbeschreibungen und Parameterwerte zeigen können, nicht auf sich selbst.

## 2.4 Das Dokumentenmodell: 20 Dokumente statt eines Sicherheitskonzepts

59 der 95 Controls fordern über die `documentation`-Prop ein konkretes ISMS-Dokument, insgesamt 20 verschiedene (bis zum Build 2026-08-26 waren es 21; seit dem Build 2026-10-22 fordert GC.12.1 statt der „Risikobewertung" die „Risikobetrachtung", die GC.7.2 ohnehin verlangt). An die Stelle des monolithischen Sicherheitskonzepts der alten Welt tritt eine Landschaft gelenkter Einzeldokumente, deren Lenkung selbst eine MUSS-Anforderung ist (GC.11.1). Die tragenden Stücke: das ISMS-Regelwerk als Klammer (GC.1.1), die Informationssicherheitsleitlinie samt Strategie und Zielen (GC.5), der Informationsverbund (STM.1), das Anforderungspaket als Arbeitsvorrat des gesamten Systems (STM.2), der Umsetzungsplan als gemeinsames Steuerungsdokument von UMS und VRB, sowie Auditbericht und Managementbericht als Produkte von PERF, mit denen sich der Zyklus gegenüber Leitung und Prüfern belegt. Die vollständige Landkarte mit fordernden Controls, Namespace-Kategorie und Zielgruppe ist Anhang B; die Übersetzung in die Referenzdokumente A.0 bis A.6 der Zertifizierungswelt steht in Kapitel 9.2.

## 2.5 Das Maschinenzimmer: Anwenderkatalog, Kategorien, OSCAL

Unter der Methodik liegt eine Katalogmaschine, und wer sie einmal im Überblick gesehen hat, liest die Praktik-Kapitel mit anderen Augen; die Details trägt Kapitel 3 in den Abschnitten 3.5 bis 3.9.

Der Anwenderkatalog mit seinen 1000 Controls ist ein gebautes Produkt: Ein OSCAL-Profil importiert den Methodik-Katalog und den Kernel vollständig sowie vier RISK-Controls gezielt, setzt erste Parameter und wird zum Gesamtkatalog aufgelöst (3.8). Die 901 Kernel-Anforderungen tragen dabei drei Property-Familien, die die Methodik selbst nicht braucht: ein vierwertiges Schutzziel-Wirkprofil, die elementaren Gefährdungen G 0.1 bis G 0.47 und Zielobjektkategorien (3.5). Diese Kategorien sind die Erben der Bausteine, mit umgekehrter Blickrichtung: Nicht mehr der Baustein bündelt Anforderungen für einen Zielobjekttyp, sondern jede Anforderung trägt ihre Kategorie selbst, und eine Hierarchie mit 39 Kategorien unter sieben Wurzeln vererbt deterministisch von der Wurzel bis zum Blatt (3.7). Die Selektion fürs Anforderungspaket läuft dann über vier Zahnräder: verbundweite Methodik-Grundlast, Kategorien-Auswahl mit Vererbung, die Niveau-Weiche über `sec_level` und die Analyse-Metadaten für Risiko und Priorisierung (3.6). Und über allem steht eine OSCAL-Dokumentfamilie, die vom Katalog über Profil und System-Sicherheitsplan bis zu Prüfplan, Prüfergebnissen und Maßnahmenplan reicht; für die komplette Staffel existieren browserbasierte Werkzeuge; die Umsetzungsebene der Bibliothek ist mit ersten Komponenten-Vorlagen gefüllt, die Prüfebene noch leer (3.9).

## 2.6 Wie ein Grundschutz++-ISMS anläuft

Die Reihenfolge des ersten Zyklus ergibt sich aus den Abhängigkeiten der Controls; als Wegweiser für die ersten Monate, mit den Kapiteln, die die Details tragen:

Zuerst der Rahmen: ISMS-Verfahren verankern und den Standard-Parameter setzen (GC.1.1), Kontext und Stakeholder analysieren (GC.2, GC.4), Compliance-Kataster aufbauen (GC.3), messbare Ziele, Strategie und Leitlinie festlegen und von der Leitung autorisieren lassen (GC.5), Geltungsbereich nach Leitungsfreigabe abgrenzen (GC.6.1), Sicherheitsorganisation mit unabhängigem ISB aufstellen (GC.9), Dokumentenlenkung und Risikomethodik verankern (GC.11, GC.12), Ressourcen und Kommunikationswege regeln (GC.8, GC.10). Dann die Einstufung: Geschäftsprozesse festlegen, Schutzbedarf zweistufig einstufen, den wichtigsten Prozess durch die Leitung bestimmen lassen (GC.7). Dann die Modellierung: Informationsverbund abgrenzen (STM.1), für den wichtigsten Prozess Assets erfassen, Zielobjektkategorien zuweisen und das Anforderungspaket erzeugen (STM.2), Sicherheitsniveau prüfen (STM.3), nötige Risikobetrachtungen ausführen (STM.4, GC.7.2), Parameter setzen (STM.5). Dann die Umsetzung: Status erheben (zum Statusmodell Kapitel 6.1), Maßnahmen planen, priorisieren, Zuständige und Fristen festlegen, Ausnahmen regeln, Fortschritt verfolgen (UMS.1 bis UMS.7). Schließlich Messung und Verbesserung: Monitoring und Auditprogramm aufsetzen, erstes internes Audit, Managementbericht an die Leitung (PERF), Feststellungen in Korrekturen und Verbesserungen übersetzen und deren Wirksamkeit testen (VRB). Mit dem Managementbericht und der Leitungsentscheidung darüber ist der erste Zyklus belegt, GC.1.1 erfüllt und GC.1.2 bedient.

Der wichtigste Unterschied zum alten Vorgehen steckt im dritten Schritt: Es ist kein Vollausbau. Der erste Zyklus gilt dem wichtigsten Geschäftsprozess (STM.2.1.2, Guidance), die weiteren Prozesse folgen in den nächsten Zyklen. Der Standard 300-1 sagt es genauso und präzisiert den Einstieg: Begonnen wird mit dem wichtigsten Geschäftsprozess aus der höchsten Schutzbedarfskategorie, bei mehreren Kandidaten wählt die Institutionsleitung, und sukzessive sind alle Geschäftsprozesse des Anwendungsbereichs zu untersuchen (Standard 300-1, Kap. 2.6 (S. 9)). Klein anfangen ist hier nicht Pragmatismus gegen die Methode, sondern die Methode.

## 2.7 Die fünf Prozessschritte des Standards 300-1

Seit dem 20.10.2026 beschreibt der BSI-Standard 300-1 „Methodik Grundschutz++" (Version 1.0) den Vorgehenszyklus in Prosa, so wie es der 200-2 für den klassischen IT-Grundschutz tat. Er gliedert den Zyklus in fünf Prozessschritte und ordnet sie dem PDCA-Modell zu (Standard 300-1, Kap. 1 (S. 5)); die Zuordnungsgrafik (Abbildung 1) war aus dem PDF nicht auswertbar. Control-IDs nennt der Standard nicht, ein Praktik-Kürzel kommt genau einmal vor („Umsetzung (UMS)" in Mindestkriterium 31). Die Zuordnung zu den Praktiken ist deshalb Auslegung dieses Handbuchs anhand der Inhalte:

| Prozessschritt (Standard 300-1) | Praktiken und Controls (Katalog) | Bemerkung |
|---|---|---|
| 1 Erhebung und Planung (Kap. 2, S. 6 bis 11) | GC vollständig, einschließlich Schutzbedarf (GC.7) und „Initiierung der Risikobetrachtung" (GC.12.1, RISK.1.1, RISK.1.3, RISK.1.5) | Der Standard ordnet den Schritt den Kapiteln 4 und 5 der ISO 27001 zu |
| 2 Anforderungsanalyse (Kap. 3, S. 12 bis 17) | STM.1, STM.2, STM.3, STM.5; neu: Auswahl von Blaupausen (Kap. 3.3) | Der Standard nennt die Kapitel „6 und 10" der ISO 27001; Kapitel 10 ist dort die Verbesserung, vermutlich ist Kapitel 8 gemeint (Anhang D, D48) |
| 3 Realisierung (Kap. 4, S. 18 bis 21) | UMS vollständig, dazu die Durchführung der Risikobetrachtung (im Katalog STM.4.1) und RISK.1.10 | Die Risikobetrachtung wandert von der Strukturmodellierung in die Realisierung |
| 4 Überwachung (Kap. 5, S. 22 bis 25) | PERF.1 bis PERF.5; Abschnitt 5.5 „Validierung der Anforderungen" entspricht PERF.1.3 | Überwachung vor Verbesserung, wie der Wirkfluss in 2.2 |
| 5 Kontinuierliche Verbesserung (Kap. 6, S. 26 bis 27) | VRB.1 bis VRB.7; Abschnitt 6.4 „Evaluation" entspricht VRB.6 | Der Standard nennt 6.4 „Prozessschritt Evaluation", obwohl es ein Teilschritt ist |

Für Leser mit 200-2-Vorwissen ist der Standard der bequemere Einstieg, für die Umsetzung bleibt der Katalog maßgeblich: Nur dort stehen Modalverben, Parameter und Dokumentzuordnungen. Der Katalog kennt den Standard übrigens schon länger als umgekehrt: Die Guidance zu GC.7.1.1 verweist in jedem Build seit August 2026 auf „Prozessschritt 2 - Anforderungsanalyse", und der Build 2026-10-22 benennt das von GC.12.1 geforderte Dokument in „Risikobetrachtung" um, den Begriff des Standards. An sieben Stellen widersprechen sich Standard und Katalog-Build 2026-10-22: Umsetzungsstatus, kategorielose Anforderungen, Ausnahmen von MUSS-Anforderungen, Restrisiko, Mindestkriterien der Risikobetrachtung, Auslöser der Risikobetrachtung und Sicherheitsniveau „erhöht". Das BSI hat angekündigt, den Anwenderkatalog nachzuziehen. Die Praktik-Kapitel führen diese Stellen als Kästen mit beiden Fassungen, Anhang D sammelt sie als D38 bis D44.

---

*Ende Kapitel 2 (v0.6). Review-Anmerkungen bitte gegen die Control-IDs und die Kapitel des Standards 300-1.*
