# Kapitel 8: PERF – Monitoring-Evaluation

**Handbuch zur Grundschutz++ Methodik · Kapitel-Version 0.4 (Entwurf)**
Stand: 2026-10-26 · Normative Basis: `BSI-Methodik-Grundschutz++-catalog.json`, Build 2026-10-22; BSI-Standard 300-1 (Version 1.0, 20.10.2026) · Gliederungsbezug: Kapitel 8 gemäß `00_gliederung_v0.1.md`
Änderung 0.4: Standard 300-1 eingearbeitet (Prozessschritt 4 in 8.0, Leistungsbewertung und Validierung in 8.1, internes Auditprogramm in 8.3, Managementbewertung in 8.4, drei Monitoring-Verfahren in 8.5); PERF.2.1 auf den neuen Titel des Builds 2026-10-22 nachgezogen; offene Fragen ergänzt.

## 8.0 Einordnung: die unterschätzte Check-Phase

PERF ist mit 24 Controls die zweitgrößte Praktik der Methodik und zugleich die am leichtesten übersehene: Wer PDCA aus der alten Welt vor allem als Planen und Umsetzen gelebt hat, unterschätzt, wie viel Gewicht der Katalog auf die Messung legt. Inhaltlich ist PERF die Check-Phase des Zyklus: Leistungsbewertung des ISMS (PERF.1), Compliance-Überwachung (PERF.2), interne Audits (PERF.3), Managementbewertung (PERF.4) und technisches Monitoring (PERF.5). Die Verbindlichkeitsverteilung ist mit 13 MUSS und 11 SOLLTE die ausgeglichenste aller Praktiken, und die SOLLTE-Controls konzentrieren sich auffällig: Acht davon sind die Berichtsinhalte der Managementbewertung (PERF.4.1.1 bis PERF.4.1.8, alle `effort_level` 1), dazu kommen Compliance-Überwachung (PERF.2.1), Auditplan (PERF.3.1.1) und Bewertungsschema (PERF.3.2.1, beide `effort_level` 3, die teuersten Controls der Praktik).

Im Standard 300-1 ist PERF „Prozessschritt 4 – Überwachung" (Standard 300-1, Kap. 5 (S. 22 bis 25)): Leistungsbewertung des ISMS, internes Auditprogramm und -durchführung, Managementbewertungen, Monitoring-Methoden und -Tools, Validierung der Anforderungen. Das ist PERF.1 bis PERF.5 in anderer Reihenfolge, mit PERF.1.3 als eigenem Abschnitt 5.5; die Compliance-Überprüfung (PERF.2) hat im Standard keinen eigenen Abschnitt.

Die Praktik produziert die beiden Dokumente, von denen der Rest der Methodik lebt: den Auditbericht (PERF.3.2) und den Managementbericht (PERF.4.1). Der Auditbericht speist VRB.2 (Nicht-Konformitäten) und den Umsetzungsplan; der Managementbericht ist das Vehikel, mit dem GC.1.2 die Freigabe des ISMS einholt und PERF.4.2 die Leitung informiert. Wer den Zyklus von GC.1.1 her denkt (erfüllt erst nach einem vollständigen Durchlauf), erkennt in PERF den Taktgeber: Ohne Audit, Managementbewertung und Bericht gibt es keinen belegbaren Durchlauf. Die neun Unter-Controls von PERF.4.1 lesen sich dabei erkennbar als Katalogisierung der klassischen Management-Review-Eingaben, wie sie auch ISO 27001 im Kapitel zur Managementbewertung kennt; diese Einordnung ist Kommentar dieses Handbuchs, keine Katalogaussage.

## 8.1 PERF.1 Leistungsbewertung des ISMS: messen, was das ISMS leistet

**Anforderungsbezug.**

| Control | Verbindlichkeit | Kern | Dokument |
|---|---|---|---|
| PERF.1.1 Verfahren und Regelungen | MUSS | Verfahren zur Messung und Bewertung der ISMS-Leistung verankern | keines zugeordnet |
| PERF.1.2 Evaluation des Umsetzungsplans | MUSS | `{{regelmäßige}}` Überprüfung und Fortschreibung des Umsetzungsplans verankern | keines zugeordnet |
| PERF.1.3 Aktualität der Anforderungen | MUSS | Aktualität der Anforderungen `{{regelmäßig}}` überprüfen | keines zugeordnet |

PERF.1.1 ist die Rahmenanforderung; die Inhalte ergeben sich laut Guidance aus den übrigen Controls der Praktik, die Ergebnisse sind strukturiert zu dokumentieren und an die Stakeholder zu kommunizieren. PERF.1.2 prüft den Umsetzungsplan auf Fortschritt, Fristeinhaltung und inhaltliche Korrektheit; die Guidance verlangt die systematische Auswertung von Umsetzungsstand, Abweichungen, Restrisiken und Wirksamkeit für Managemententscheidungen und macht Auditergebnisse, Sicherheitsvorfälle und Veränderungen der Bedrohungslage zu Pflicht-Eingaben der Fortschreibung. PERF.1.3 schließlich hält das Anforderungspaket aktuell: laut Guidance im Regelfall jährlich, unter Berücksichtigung veränderter Geschäftsprozesse, neuer IT-Komponenten, organisatorischer Änderungen und neuer Regulierung; signifikante Anpassungen können eine Neumodellierung auslösen und damit den gesamten Zyklus der Strukturmodellierung und Umsetzung erneut anstoßen.

Der Standard 300-1 lässt den Inhalt der Leistungsbewertung ausdrücklich offen: „Da die Entwicklung einheitlicher Vorgaben zur Leistungsbewertung im GS++ noch aussteht, sind die Institutionen frei in der Ausgestaltung", und die Bewertung „sollte nachvollziehbar der Institutionsleitung vorgelegt werden" (Standard 300-1, Kap. 5.1 (S. 22)). PERF.1.1 verlangt das Verfahren als MUSS, der Standard bestätigt die Pflicht und vertagt den Maßstab. Für die Aktualitätsprüfung nach PERF.1.3 beschreibt Kap. 5.5 (S. 25) die „Validierung der Anforderungen" mit sechs Aspekten: Änderungen im Informationsverbund, Abstimmung mit den zuständigen Organisationseinheiten und Rollen, Anpassungen an den Anforderungen in der Stand-der-Technik-Bibliothek, Anpassungen an verwendeten Blaupausen, Änderungen in der Methodik GS++ und gegebenenfalls die Anpassung des Anforderungspakets; die Ergebnisse sind zu dokumentieren und fließen in die kontinuierliche Verbesserung.

**Umsetzungshinweise.** Hier schließt sich der Kreis zur Zielmesslogik aus GC.5.1: Die messbaren Ziele von dort sind die Kennzahlen, die PERF.1.1 erheben muss; wer dort Prosa formuliert hat, steht hier ohne Messgröße da. Legen Sie die drei Prüftakte bewusst und unterschiedlich fest: Umsetzungsplan-Evaluation im Quartalstakt passend zu UMS.6, Aktualitätsprüfung des Anforderungspakets jährlich passend zum Katalog-Release-Zyklus, ISMS-Leistungsmessung laufend über die Monitoring-Daten aus PERF.5.1. Und nehmen Sie PERF.1.3 als Kalenderereignis ernst: Die Überprüfung gegen einen neuen Katalog-Build ist genau der Moment, in dem gestrichene, geänderte und neue Anforderungen ins Paket einfließen; wer das versäumt, betreibt sein ISMS gegen einen veralteten Stand der Technik, und der Name der Bibliothek ist Programm.

**Audit-Perspektive.** PERF.1.2 und PERF.1.3 sind für den Auditor Konsistenzprüfungen mit hoher Trefferquote: Er vergleicht das Datum des letzten Katalog-Builds mit dem Stand des Anforderungspakets und die Fortschreibungshistorie des Umsetzungsplans mit den Terminen von Audits und Vorfällen. Ein Paket auf dem Stand von vor zwei Jahren bei drei zwischenzeitlichen Builds beantwortet die Frage nach PERF.1.3 von selbst.

**Typische Fehler.** Die Leistungsbewertung misst Aktivität (Anzahl Schulungen, Anzahl Tickets) statt Wirkung gegen die Ziele aus GC.5.1. Die Aktualitätsprüfung wird mit der Statusprüfung aus UMS.1.1 verwechselt: Dort geht es um die Umsetzung, hier um die Frage, ob noch die richtigen Anforderungen im Paket stehen. Und die Bedrohungslage ändert sich nur in den Nachrichten, nie im Umsetzungsplan.

## 8.2 PERF.2 Compliance-Überwachung: das überraschende SOLLTE

**Anforderungsbezug.**

| Control | Verbindlichkeit | Kern | Dokument |
|---|---|---|---|
| PERF.2.1 Überprüfung der Einhaltung von Verpflichtungen | SOLLTE | Einhaltung von Verpflichtungen `{{regelmäßig}}` sowie anlassbezogen überprüfen | keines zugeordnet |

Der Titel lautet seit dem Build 2026-10-22 „Überprüfung der Einhaltung von Verpflichtungen" (vorher „Überwachung ..."); Statement und Guidance sind unverändert. Die Guidance beschreibt ein vollständiges Überwachungsprogramm: regelmäßige Kontrollen gegen die dokumentierten gesetzlichen und vertraglichen Anforderungen, anlassbezogene Prüfungen bei Regulierungsänderungen, Verstoßhinweisen oder Systemänderungen, die systematische Dokumentation von Compliance-Lücken und Maßnahmen zu deren Schließung.

Die Verbindlichkeit überrascht: Die Erfassung der Verpflichtungen ist MUSS (GC.3.1), die Wahrung in der Umsetzung ist MUSS (UMS.7.1), die Überwachung der Einhaltung ist SOLLTE. Das Compliance-Management der Methodik ist damit an seiner Kontrollstelle am weichsten formuliert; für Institutionen mit Aufsichtsrecht im Nacken ist das SOLLTE praktisch bedeutungslos, denn die Aufsicht fragt nicht nach der Katalogverbindlichkeit. Als offene Frage in Abschnitt 8.8 vermerkt.

**Umsetzungshinweise.** Bauen Sie die Überwachung als Prüfplan über das Kataster aus GC.3.1: je Verpflichtung ein Prüfintervall, ein Prüfverfahren und ein Verantwortlicher, dazu die anlassbezogenen Trigger aus der Guidance. Identifizierte Lücken gehören als Nicht-Konformitäten in den VRB.2-Prozess und Verstöße in das Verfahren nach VRB.7.1; PERF.2.1 liefert die Fälle, die beiden VRB-Controls verarbeiten sie.

**Audit-Perspektive.** Der Auditor prüft die Kette Kataster, Prüfplan, Prüfnachweis, Lückenbehandlung. Als SOLLTE-Control gilt: Nichtumsetzung braucht die dokumentierte Begründung, und die dürfte schwerfallen, wenn das Kataster aufsichtspflichtige Verpflichtungen enthält.

**Typische Fehler.** Die Überwachung beschränkt sich auf die jährliche Datenschutz-Selbstauskunft. Anlassbezogene Prüfungen finden nicht statt, weil niemand die Regulierungsänderungen an das ISMS meldet (der Trigger aus GC.3.1 fehlt). Gefundene Lücken werden dokumentiert und nie geschlossen, womit die Dokumentation zur Selbstbelastung wird.

## 8.3 PERF.3 Audits: das interne Prüfwerk

**Anforderungsbezug.**

| Control | Verbindlichkeit | Kern | Dokument |
|---|---|---|---|
| PERF.3.1 Aufbau und Pflege eines Auditprogramms | MUSS | Verfahren für ein oder mehrere Auditprogramme verankern | keines zugeordnet |
| PERF.3.1.1 Erstellen eines Auditsplans | SOLLTE | für jedes Audit einen Auditplan festlegen | keines zugeordnet |
| PERF.3.1.2 Planen von internen Audits | MUSS | Planung der internen Audits risikoorientiert ausführen | keines zugeordnet |
| PERF.3.1.3 Auswahl des Auditteams | MUSS | fachlich geeignete und unabhängige Auditoren anweisen | keines zugeordnet |
| PERF.3.1.4 Umfang von Audits | MUSS | Audits in angemessenem Umfang ausführen | keines zugeordnet |
| PERF.3.2 Dokumentation von Auditergebnissen | MUSS | Verfahren zur Erstellung aussagekräftiger Auditberichte verankern | Auditbericht |
| PERF.3.2.1 Einheitliches Bewertungsschema | SOLLTE | einheitliches Bewertungsschema für Feststellungen festlegen | Auditbericht |
| PERF.3.2.2 Kommunikation an Stakeholder | MUSS | alle relevanten Stakeholder über Auditergebnisse informieren | Auditbericht |

Der Kern der Untergruppe steckt in einem Adjektiv:

> „Monitoring-Evaluation MUSS die Planung der internen Audits im Auditprogramm risikoorientiert ausführen." (PERF.3.1.2)

Risikoorientiert heißt laut Guidance: Prüfobjekte und Prüftiefe folgen einer Risikobetrachtung, besonders risikorelevante Fragen werden vertieft. Das Beispiel der Guidance verdient das Zitat im Sinngehalt: Bei automatisierten Richtlinien ist nicht nur deren Aktivierung zu prüfen, sondern vor allem die erlaubten Ausnahmeregelungen auf Begründung, Befristung und Umfang, damit wirksam scheinende Maßnahmen nicht durch zu weite Ausnahmen ausgehöhlt werden. Wer Kapitel 6 gelesen hat, erkennt die Pointe: Das interne Audit prüft genau die Stelle, an der das Ausnahmemanagement aus UMS.5 schlampig geworden sein könnte. Die Guidance zu PERF.3.1.1 beschreibt zudem das methodische Handwerkszeug (Interviews, Dokumentendurchsicht, Beobachtung, technische Analysen) und verweist für Details auf die ISO/IEC-19011-Reihe.

Der Standard 300-1 widmet dem internen Auditprogramm seinen längsten Abschnitt (Standard 300-1, Kap. 5.2 (S. 22 bis 24)) und setzt den Ton anders als die Zertifizierungswelt: Der Fokus des internen Audits liege „nicht auf dem Aufweisen von Nichtkonformitäten", es diene „dem Aufweisen von Verbesserungspotentialen" und der Selbstkontrolle der Organisation. Inhaltlich deckt er PERF.3.1 bis PERF.3.2.2 als Sollen ab: Auditprogrammziele (Anforderungen, Leistungsfähigkeit von Detektion und Vorfallbehandlung, identifizierte Risiken, Prozessmerkmale, Reifegrad, frühere Audits), die Risiken des Auditprogramms selbst, das Ausmaß nach Systemen, Standorten, Komplexität, Personen und Risikobedeutung, Ressourcen, Vor-Ort- oder Remote-Anteile, Auswahl und Kompetenz des Auditteams, Verantwortung des Auditteamleiters, Nachbereitung mit Maßnahmen, Berichtsfreigabe, Verteilung und Berichterstattung an die Leitung, Auditaufzeichnungen und die Verbesserung des Programms selbst. Wer die Guidance zu PERF.3 knapp findet, bekommt hier die Checkliste.

> **Katalogfund:** Der Titel von PERF.3.1.1 lautet „Erstellen eines Auditsplans" (statt „Auditplans"); in der Guidance zu PERF.3.1.2 steht „ausgehölt" (statt „ausgehöhlt"). Beides für die Katalogpflege vermerkt.

**Umsetzungshinweise.** Das Auditprogramm ist der Mehrjahresblick (welche Bereiche, in welchem Turnus, mit welchen Ressourcen), der Auditplan das Drehbuch des einzelnen Audits; verwechseln Sie die Ebenen nicht. Für die Risikoorientierung genügt eine einfache Heuristik: hohe Schutzbedarfe, viele Ausnahmen, schlechte Vorbefunde und neue Systeme ziehen Prüftiefe an. Die Unabhängigkeit des Auditteams (PERF.3.1.3) ist in kleinen Institutionen die härteste Nuss; wer intern niemanden hat, der nicht in die geprüften Prozesse involviert ist, holt sich die Unabhängigkeit extern oder im Ringtausch mit einer Partnerinstitution. Und definieren Sie das Bewertungsschema nach PERF.3.2.1, bevor der erste Bericht entsteht; nachträglich vereinheitlichte Feststellungen sind keine.

**Audit-Perspektive.** Hier prüft der externe Auditor die internen Auditoren, und die Prüfkette ist explizit: Programm, Pläne, Berichte, Stakeholder-Kommunikation, Maßnahmen im Umsetzungsplan (die Guidance zu PERF.3.2.2 verlangt genau diese Einspeisung). Interne Audits, die Jahr für Jahr nichts finden, sind kein Qualitätsbeweis, sondern ein Indiz gegen die Risikoorientierung; das Zertifizierungsschema kennt dieselbe Logik, wenn es die Wirksamkeit des ISMS über die Auditergebnisse bewertet. Ein einheitliches Bewertungsschema erleichtert dem externen Prüfer übrigens die Anerkennung interner Ergebnisse, was den eigenen Prüfaufwand senkt; PERF.3.2.1 ist eines der SOLLTEs mit dem besten Kosten-Nutzen-Verhältnis der Methodik.

**Typische Fehler.** Das Auditprogramm prüft jedes Jahr dieselben unkritischen Bereiche, weil dort die Zusammenarbeit angenehm ist. Der ISB auditiert seine eigenen Konzepte. Feststellungen werden mündlich besprochen und nie in den Umsetzungsplan überführt. Die Berichte enthalten nur Mängel, obwohl die Guidance zu PERF.3.2 ausdrücklich auch positive Feststellungen verlangt, um ein ausgewogenes Bild zu vermitteln.

## 8.4 PERF.4 Managementbewertungen: der Bericht, der die Leitung erreicht

**Anforderungsbezug.**

| Control | Verbindlichkeit | Kern | Dokument |
|---|---|---|---|
| PERF.4.1 Eignungsprüfung | MUSS | Eignung, Angemessenheit und Wirksamkeit des ISMS `{{regelmäßig}}` sowie anlassbezogen im Managementbericht dokumentieren | Managementbericht |
| PERF.4.1.1 Ergebnisse von Folgemaßnahmen | SOLLTE | Status der Folgemaßnahmen früherer Bewertungen dokumentieren | Managementbericht |
| PERF.4.1.2 Geänderte Rahmenbedingungen | SOLLTE | veränderte Rahmenbedingungen dokumentieren | Managementbericht |
| PERF.4.1.3 Erfolge und Probleme | SOLLTE | Erfolge und Probleme (z. B. Sicherheitsvorfälle) dokumentieren | Managementbericht |
| PERF.4.1.4 Interne Überprüfungen und Audits | SOLLTE | Auditberichte als Ergebnis der Überprüfung dokumentieren | Managementbericht |
| PERF.4.1.5 Eignungsprüfung bisheriger Sicherheitsmaßnahmen | SOLLTE | Eignung umgesetzter Maßnahmen zur Zielerreichung dokumentieren | Managementbericht |
| PERF.4.1.6 Rückmeldung von Stakeholdern | SOLLTE | Bewertung von Rückmeldungen zu Sicherheitsaspekten dokumentieren | Managementbericht |
| PERF.4.1.7 Status des Realisierungsplans | SOLLTE | Umsetzung von Maßnahmen und verringertes Risiko (Status des Umsetzungsplans) dokumentieren | Managementbericht |
| PERF.4.1.8 Verbesserungen | SOLLTE | abgeleitete Verbesserungen des ISMS dokumentieren | Managementbericht |
| PERF.4.1.9 Maßnahmenvorschläge | MUSS | priorisierte Maßnahmenvorschläge mit realistischen Aufwandsschätzungen dokumentieren | Managementbericht |
| PERF.4.2 Bericht an die Institutionsleitung | MUSS | Leitung `{{regelmäßig}}` anhand des Managementberichts informieren | keines zugeordnet |

Elf Controls, ein Dokument. Die Architektur ist bemerkenswert: Der Rahmen (PERF.4.1), die Maßnahmenvorschläge mit Aufwandsschätzung (PERF.4.1.9) und die Übergabe an die Leitung (PERF.4.2) sind MUSS; die acht inhaltlichen Berichtsbausteine dazwischen sind durchgängig SOLLTE mit `effort_level` 1. Der Katalog erzwingt also, dass berichtet wird und dass die Leitung entscheidungsfähige Vorschläge samt Preisschild bekommt, und empfiehlt die Vollständigkeit der Eingaben. Die Guidance zu PERF.4.1 gibt dem Bericht eine klare Stilvorgabe: kurz, klar, verständlich, nicht überfrachtet, mit Fokus auf das Wesentliche, damit die Leitung priorisieren und Ressourcen steuern kann; erkennbar werden muss, ob der beabsichtigte Sicherheitszweck wirksam erfüllt wird. PERF.4.2 ergänzt den Takt (etwa quartalsweise oder anlassbezogen nach einem schweren Vorfall) und empfiehlt Kennzahlen und Trenddarstellungen. Der Standard 300-1 beschreibt die Managementbewertung in Kap. 5.3 (S. 24) mit sieben Aspekten, die sich auf PERF.4.1.1 bis PERF.4.1.8 legen lassen: Auditergebnisse, Ergebnisse der Leistungsbewertung, Sicherheitsvorfälle, Status der Risikobehandlung, Änderungen in der Institution oder der Bedrohungslage, Status früherer Managemententscheidungen, Regelmäßigkeit der Bewertung; „Der Managementbewertung liegt der Managementbericht zugrunde", und die Leitung prüft, „ob das ISMS geeignet, angemessen und wirksam ist", die Trias aus PERF.4.1.

> **Katalogfund:** Der Titel von PERF.4.1.7 verwendet den 200-2-Begriff „Realisierungsplan", während das Statement vom Umsetzungsplan spricht; ein Begriffs-Relikt aus der alten Welt. In der Guidance zu PERF.4.1 steht zudem ein großgeschriebenes „SOLL" („Der Bericht SOLL: kurz, klar und verständlich sein"), das wie ein normatives Modalverb aussieht, aber in einer Guidance steht und nicht zum Modalverb-Satz der Methodik (MUSS/SOLLTE) gehört. Achtmal wiederholt sich außerdem der Formelsatz, die Ergebnisse basierten „auf den vorab erstellten Auditberichten sowie der geforderten Eignungsprüfung", auch dort, wo er wenig erklärt.

**Umsetzungshinweise.** Bauen Sie den Managementbericht als feste Vorlage entlang der neun Unterpunkte; dann ist die SOLLTE-Vollständigkeit ein Abhakvorgang statt einer Jahresendüberraschung, und der Bericht bleibt vergleichbar über die Zyklen. Widerstehen Sie der Versuchung, den Bericht zur Fleißarbeit zu machen: Die Guidance verlangt Verdichtung, und eine Leitung, die zwanzig Seiten Statusprosa bekommt, liest keine davon. Zwei Seiten Kennzahlen und Trends, eine Seite Entscheidungsbedarfe mit Aufwandsschätzung (PERF.4.1.9 verlangt genau das), fertig. Und schließen Sie den Kreis zu GC: Der Managementbericht ist das Dokument, mit dem GC.1.2 die Autorisierung der ISMS-Verfahren einholt; wer PERF.4 sauber betreibt, erledigt die Governance-Nachweise gleich mit.

**Audit-Perspektive.** Die Managementbewertung ist einer der ersten Blicke jedes Zertifizierungsauditors, denn sie belegt gleich dreierlei: dass die Leitung informiert ist, dass sie entscheidet, und dass der Zyklus lebt (PERF.4.1.1 verlangt den Status der Folgemaßnahmen der letzten Bewertung, womit sich die Berichte verketten). Fehlende oder inhaltsleere Managementberichte treffen das Funktionieren des ISMS im Kern und wiegen nach der Schema-Systematik schwer. Die acht SOLLTE-Bausteine prüft der Auditor als Vollständigkeitsraster; jede Auslassung braucht die übliche Begründung.

**Typische Fehler.** Der Bericht entsteht eine Woche vor dem Audit für das Audit, nicht für die Leitung. Er enthält Statusberichte, aber keine Entscheidungsvorlagen, womit ausgerechnet das MUSS aus PERF.4.1.9 fehlt. Die Leitung nimmt zur Kenntnis, statt zu entscheiden, und niemand dokumentiert die Entscheidungen. Oder die Folgemaßnahmen der letzten Bewertung tauchen nie wieder auf, womit die Verkettung reißt und PERF.4.1.1 leerläuft.

## 8.5 PERF.5 Monitoring: die technische Sinneswahrnehmung des ISMS

**Anforderungsbezug.**

| Control | Verbindlichkeit | Kern | Dokument |
|---|---|---|---|
| PERF.5.1 Methoden und Tools | MUSS | effektive Monitoring-Methoden und -tools zur `{{regelmäßigen}}` Überwachung verankern | keines zugeordnet |

Die Guidance skaliert den Anspruch nach Institutionsgröße (einfachere Lösungen für kleine, automatisierte für große Umgebungen), verlangt die systematische Auswertung der Monitoring-Daten für Kennzahlen, Früherkennung, Incident Response und kontinuierliche Verbesserung, und nennt als Beispiele SIEM-Systeme, IDS/IPS, Vulnerability-Management und Configuration-Monitoring.

Der Standard 300-1 geht über das eine Control hinaus und macht drei Verfahren zur Pflicht: „Im Rahmen des Monitorings müssen folgende Verfahren verankert werden": ein Verfahren zur Erkennung von Sicherheitsvorfällen mit frühzeitiger Identifikation und Meldung, von manuellen Prozessen bis zu automatisierten Erkennungssystemen; ein Verfahren für den Umgang mit Schwachstellen und ihre Berücksichtigung in der Risikobetrachtung, mit Identifikation, Bewertung, Behandlung und Nachverfolgung; ein Verfahren für die Erfassung neu auftretender Bedrohungen und deren Berücksichtigung in der Risikobetrachtung (Standard 300-1, Kap. 5.4 (S. 24 f.)). Im Methodik-Teil des Katalogs hat keines der drei Verfahren ein eigenes Control; im Kernel liegen sie in den Praktiken DET und REA, die über die Zielobjektkategorien ins Anforderungspaket kommen. Die Pflicht gilt über den Standard (Anhang D, D47).

**Umsetzungshinweise.** Das eine Control täuscht über den Aufwand hinweg: PERF.5.1 ist die Anforderung mit dem größten technischen und personellen Rattenschwanz der ganzen Praktik. Aus langjähriger SOC- und SIEM-Erfahrung: Kaufen Sie das Ergebnis, nicht das Tool. Ein SIEM ohne Menschen, die seine Alarme lesen, Parser pflegen und Use Cases fortschreiben, erfüllt PERF.5.1 nur auf dem Papier und im Budgetbericht. Beginnen Sie bei der Frage, welche Kennzahlen die Leistungsbewertung (PERF.1.1) und der Managementbericht (PERF.4.2 nennt beispielhaft Vorfallzahlen, Zeit bis zur Entdeckung, Erfüllungsgrad von Maßnahmen) tatsächlich brauchen, und dimensionieren Sie das Monitoring von dort rückwärts; das schützt vor dem Datengrab, das alles sammelt und nichts beantwortet. Für kleine Institutionen ist die Guidance ausdrücklich gnädig: Ein gepflegtes Schwachstellenmanagement plus zentrale Log-Auswertung ist ein legitimer Anfang, ein ungelesenes Enterprise-SIEM ist keiner.

**Audit-Perspektive.** Der Auditor fragt nicht, welches Tool installiert ist, sondern was mit den Daten geschieht: Wer sieht die Alarme, in welcher Zeit, mit welchem Eskalationsweg, und welche Kennzahlen erreichen den Managementbericht. Ein Monitoring, dessen Erkenntnisse nachweislich in Vorfallbehandlung und Verbesserung fließen, trägt die halbe PERF-Praktik; eines, das seit Monaten unbeachtete Alarme sammelt, ist die Vor-Ort-Feststellung, die sich am schnellsten finden lässt.

**Typische Fehler.** Das Monitoring endet bei der Infrastruktur und sieht die fachlichen Systeme nicht. Alarme sind auf die Mailbox des ISB abonniert und dort stumm. Der Parameter `{{regelmäßigen}}` bleibt ungesetzt, sodass niemand sagen kann, welches Überwachungsintervall eigentlich vereinbart ist.

## 8.6 Schnittstelle zu VRB: wie Messung zu Verbesserung wird

Die Katalogreihenfolge stellt VRB vor PERF, der Wirkfluss läuft umgekehrt, und er läuft über konkrete Übergabepunkte: Auditfeststellungen aus PERF.3.2 werden laut Guidance zu PERF.3.2.2 in den Umsetzungsplan eingefügt und nachverfolgt, womit sie im Territorium von UMS.6 und VRB.5.1 landen. Nicht-Konformitäten aus Audits und Compliance-Überwachung (PERF.2.1) sind der Haupteingang von VRB.2. Die Managementbewertung dokumentiert die abgeleiteten Verbesserungen (PERF.4.1.8) und deren Folgestatus (PERF.4.1.1), womit sie die Wirksamkeitskette von VRB.6 auf Leitungsebene spiegelt. Wer die beiden Praktiken getrennt betreibt, produziert Berichte ohne Konsequenz und Verbesserungen ohne Evidenz; wer sie verzahnt, hat den PDCA-Zyklus, dessen Abschluss die Guidance zu VRB.1.1 verspricht.

## 8.7 Dokumenten-Output der Praktik

| Dokument | Gefordert durch |
|---|---|
| Auditbericht | PERF.3.2, PERF.3.2.1, PERF.3.2.2 |
| Managementbericht | PERF.4.1, PERF.4.1.1, PERF.4.1.2, PERF.4.1.3, PERF.4.1.4, PERF.4.1.5, PERF.4.1.6, PERF.4.1.7, PERF.4.1.8, PERF.4.1.9 |

Elf Controls fordern kein Dokument (PERF.1.1, PERF.1.2, PERF.1.3, PERF.2.1, PERF.3.1, PERF.3.1.1, PERF.3.1.2, PERF.3.1.3, PERF.3.1.4, PERF.4.2, PERF.5.1). Auffällig: Auditprogramm und Auditplan haben keine Dokumentzuordnung, obwohl die Guidance zu PERF.3.1.1 und PERF.3.1.2 die Dokumentation ausdrücklich verlangt („Der Plan muss dokumentiert werden", „Die Planung muss dokumentiert werden"); es gilt die freie Form unter der Lenkung von GC.11.1.

## 8.8 Offene Fragen und Katalogfunde

1. **Compliance-Überwachung nur SOLLTE.** PERF.2.1 ist das weichste Glied der Compliance-Kette (GC.3.1 MUSS, UMS.7.1 MUSS, PERF.2.1 SOLLTE). Ob das Absicht ist oder eine Verbindlichkeitslücke, sollte an den Katalog zurückgemeldet werden (vgl. Abschnitt 8.2).
2. **Dokumentationspflichten ohne Dokumentzuordnung.** Auditprogramm, Auditplan und Auditplanung verlangen in Guidance beziehungsweise Statement Dokumentation, tragen aber keine `documentation`-Props; gleiches Muster wie in VRB (Abschnitt 7.9, Punkt 3).
3. **Begriffs-Relikt „Realisierungsplan"** im Titel von PERF.4.1.7 neben „Umsetzungsplan" im Statement; dazu das „SOLL" in der Guidance zu PERF.4.1 außerhalb des Modalverb-Systems (vgl. Abschnitt 8.4).
4. **Tippfehler:** „Auditsplans" (Titel PERF.3.1.1), „ausgehölt" (Guidance PERF.3.1.2), „mitein" (Guidance PERF.1.2), sowie die Kongruenz „in Bezug auf … inhaltlicher Korrektheit" im Statement von PERF.1.2.
5. **Auslegung der ISO-Nähe.** Die Deutung der neun PERF.4.1-Unterpunkte als Management-Review-Eingaben nach ISO-27001-Muster ist Handbuch-Kommentar; der Standard 300-1 nennt in Kap. 5.3 sieben nahezu deckungsgleiche Aspekte, ohne die ISO zu zitieren (Abschnitt 8.4).
6. **Drei Monitoring-Verfahren ohne Methodik-Control.** Vorfallerkennung, Schwachstellenbehandlung und Erfassung neuer Bedrohungen sind nach Standard 300-1, Kap. 5.4 Pflicht; PERF.5.1 nennt nur Methoden und Tools (Abschnitt 8.5; Anhang D, D47).
7. **Leistungsbewertung inhaltlich offen.** Der Standard vertagt einheitliche Vorgaben (Kap. 5.1); PERF.1.1 verlangt das Verfahren trotzdem als MUSS (Abschnitt 8.1).
8. **Titeländerung PERF.2.1** im Build 2026-10-22 („Überprüfung" statt „Überwachung"); Statement unverändert, Handbuch nachgezogen (Abschnitt 8.2).

---

*Ende Kapitel 8 (v0.4). Review-Anmerkungen bitte gegen die Control-IDs und die Kapitel des Standards 300-1.*
