# Review-Dossier Praktik VRB

Praktik VRB: 8 Controls mit Mapping, 55 Paare gesamt. Gesampelt: 5 Controls (max/min/median Paarzahl + 2 zufällig).

## VRB.3.1 — Identifikation von Verbesserungspotenzialen  [3 Paare]

**Statement (normativ):** Verbesserung MUSS eine Methode zur Überprüfung und Bewertung von Verbesserungspotentialen unter Berücksichtigung der damit verbundenen Vor- und Nachteile festlegen.
**Klasse:** BSI-Methodik-Grundschutz-plus-plus | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Im Gegensatz zum reaktiven Umgang mit Nicht-Konformitäten zielt die Identifikation von Verbesserungspotentialen darauf ab, auch ohne vorangegangene Probleme oder Abweichungen Optimierungsmöglichkeiten zu erkennen und zu nutzen. Für Verbesserungen zur Nutzung identifizierter Potenziale wird ein strukturierter Ansatz verfolgt. Die Methode beinhaltet beispielsweise die Bewertung des Umfelds der Institution (einschließlich der Bewertung der Gefährdungslage), die Auswertung des Umsetzungsplans, die Auswertung von Auditergebnissen und Sicherheitsvorfällen sowie die Berücksichtigung von Ad hoc-Eingaben (z. B. akute Verbesserungspotentiale). Die Verbesserungspotenziale zielen auf die proaktive Weiterentwicklung des ISMS ab. Sie können beispielsweise den Einsatz neuer oder verbesserter Technologien und Methoden, die Stärkung der Sicherheitskultur und des Sicherheitsbewusstseins, die Erweiterung des Anwendungsbereiches des ISMS oder die Verbesserung der Integration des ISMS in andere Managementsysteme und Geschäftsprozesse betreffen. Nicht jede Verbesserungsmöglichkeit bietet denselben Mehrwert für die Institution. Die Bewertung sollte das Potenzial zur Risikoreduktion, den erwarteten Ressourcenaufwand, die strategische Bedeutung für die Informationssicherheitsziele, mögliche Synergien mit anderen Verbesserungsmaßnahmen oder Projekten und die Nachhaltigkeit der Verbesserung berücksichtigen.

### → DER.2.1.A18 — Weiterentwicklung der Prozesse durch Erkenntnisse aus Sicherheitsvorfällen und Branchenentwicklungen (S) [Fachverantwortliche]
  1. Nachdem ein Sicherheitsvorfall analysiert wurde, SOLLTE untersucht werden, ob die Prozesse und Abläufe im Rahmen der Behandlung von Sicherheitsvorfällen geändert oder weiterentwickelt werden müssen.
  2. Dabei SOLLTEN alle Personen, die an dem Vorfall beteiligt waren, über ihre jeweiligen Erfahrungen berichten.
  3. Es SOLLTE geprüft werden, ob es neue Entwicklungen im Bereich Incident Management und in der Forensik gibt und ob diese in die jeweiligen Dokumente und Abläufe eingebracht werden können. **◀ ZITIERT**
  4. Werden Hilfsmittel und Checklisten eingesetzt, z. B. für Service-Desk-Mitarbeitende, SOLLTE geprüft werden, ob diese um relevante Fragen und Informationen zu erweitern sind.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 3) VRB.3.1 deckt die Prüfung neuer Entwicklungen und Methoden als allgemeinen Prozess zur systematischen Identifikation und Bewertung von Verbesserungspotenzialen im ISMS ab.

### → OPS.3.2.A12 — Durchführung einer risikoorientierten Betrachtung von Prozessen, Anwendungen und IT-Systemen (S)
  1. Werden Prozesse, Anwendungen oder IT-Systeme neu aufgebaut und Kunden bereitgestellt, SOLLTEN diese regelmäßig und anlassbezogen risikoorientiert betrachtet und dokumentiert werden.
  2. Aus den sich daraus ergebenen Ergebnissen SOLLTEN geeignete Maßnahmen festgelegt werden.
  3. Darüber hinaus SOLLTEN die Resultate dazu verwendet werden, um das Informationssicherheitsmanagement weiter zu verbessern. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme VRB.3.1 deckt die Forderung als allgemeinere Fassung ab, indem sie eine strukturierte Methode zur Identifikation und Bewertung von Verbesserungspotenzialen für die Weiterentwicklung des ISMS vorschreibt.

### → ISMS.1.A12 — Management-Berichte zur Informationssicherheit (S) [Institutionsleitung]
  1. Die Institutionsleitung SOLLTE sich regelmäßig über den Stand der Informationssicherheit informieren, insbesondere über die aktuelle Gefährdungslage sowie die Wirksamkeit und Effizienz des Sicherheitsprozesses.
  2. Dazu SOLLTEN Management-Berichte geschrieben werden, welche die wesentlichen relevanten Informationen über den Sicherheitsprozess enthalten, insbesondere über Probleme, Erfolge und Verbesserungsmöglichkeiten. **◀ ZITIERT**
  3. Die Management-Berichte SOLLTEN klar priorisierte Maßnahmenvorschläge enthalten.
  4. Die Maßnahmenvorschläge SOLLTEN mit realistischen Abschätzungen zum erwarteten Umsetzungsaufwand versehen sein.
  5. Die Management-Berichte SOLLTEN revisionssicher archiviert werden.
  6. Die Management-Entscheidungen über erforderliche Aktionen, den Umgang mit Restrisiken und mit Veränderungen von sicherheitsrelevanten Prozessen SOLLTEN dokumentiert sein.
  7. Die Management-Entscheidungen SOLLTEN revisionssicher archiviert werden.
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 2) Satz 2 fordert die Berichterstattung über Verbesserungsmöglichkeiten im Sicherheitsprozess, was sich mit der Erfassung und Aufbereitung von Verbesserungspotenzialen überschneidet.


## VRB.4.1 — Korrekturmaßnahmen  [22 Paare]

**Statement (normativ):** Verbesserung MUSS angemessene Korrekturmaßnahmen zur Beseitigung der Ursachen von Fehlern festlegen.
**Klasse:** BSI-Methodik-Grundschutz-plus-plus | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Bei der Entwicklung von Korrekturvorschlägen zur Beseitigung von Fehlerursachen sollten folgende Aspekte berücksichtigt werden: Die vorgeschlagenen Korrekturen müssen die identifizierten Grundursachen adressieren und nicht nur die Symptome beheben. Die Korrekturen sollten angemessen und verhältnismäßig sein, also in einem sinnvollen Verhältnis zum Risiko oder zur Bedeutung der Nicht-Konformität stehen. Die Korrekturen sollten nachhaltig wirken und wiederkehrende Probleme verhindern. Je nach Ursache können unterschiedliche Arten von Korrekturen erforderlich sein bspw. organisatorische Anpassungen wie die Überarbeitung von Prozessen, Richtlinien oder Zuständigkeiten; personelle oder disziplinarische Maßnahmen; infrastrukturelle Änderungen wie bauliche Anpassungen oder Verbesserungen der physischen Sicherheit; technische Anpassungen an Hardware, Software oder Netzwerkinfrastruktur; strategische Maßnahmen, die eine Entscheidung oder Unterstützung der Institutionsleitung erfordern.

### → APP.3.1.A22 — Penetrationstest und Revision (S)
  1. Webanwendungen und Webservices SOLLTEN regelmäßig auf Sicherheitsprobleme hin überprüft werden.
  2. Insbesondere SOLLTEN regelmäßig Revisionen durchgeführt werden.
  3. Die Ergebnisse SOLLTEN nachvollziehbar dokumentiert, ausreichend geschützt und vertraulich behandelt werden.
  4. Abweichungen SOLLTE nachgegangen werden. **◀ ZITIERT**
  5. Die Ergebnisse SOLLTEN dem ISB vorgelegt werden.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Das Festlegen von Korrekturmaßnahmen zur Beseitigung von Fehlerursachen deckt das Nachgehen von festgestellten Abweichungen auf allgemeiner Ebene direkt ab.

### → APP.3.2.A16 — Penetrationstest und Revision (S)
  1. Webserver SOLLTEN regelmäßig auf Sicherheitsprobleme hin überprüft werden.
  2. Auch SOLLTEN regelmäßig Revisionen durchgeführt werden.
  3. Die Ergebnisse SOLLTEN nachvollziehbar dokumentiert, ausreichend geschützt und vertraulich behandelt werden.
  4. Abweichungen SOLLTE nachgegangen werden. **◀ ZITIERT**
  5. Die Ergebnisse SOLLTEN dem ISB vorgelegt werden.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Das Festlegen von Korrekturmaßnahmen zur Beseitigung von Fehlerursachen deckt das Nachgehen von festgestellten Abweichungen inhaltlich ab.

### → DER.1.A13 — Regelmäßige Audits der Detektionssysteme (S)
  1. Die vorhandenen Detektionssysteme und getroffenen Maßnahmen SOLLTEN in regelmäßigen Audits daraufhin überprüft werden, ob sie noch aktuell und wirksam sind.
  2. Es SOLLTEN die Messgrößen ausgewertet werden, die beispielsweise anfallen, wenn sicherheitsrelevante Ereignisse aufgenommen, gemeldet und eskaliert werden.
  3. Die Ergebnisse der Audits SOLLTEN nachvollziehbar dokumentiert und mit dem Soll-Zustand abgeglichen werden.
  4. Abweichungen SOLLTE nachgegangen werden. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Das Nachgehen von Abweichungen wird durch das Festlegen von Korrekturmaßnahmen zur Behebung von Fehlerursachen in VRB.4.1 materiell abgedeckt.

### → DER.2.3.A5 — Schließen des initialen Einbruchswegs (B)
  1. Wurde durch eine forensische Untersuchung herausgefunden, dass die Angreifenden durch eine technische Schwachstelle in das Netz der Institution eingedrungen sind, MUSS diese Schwachstelle geschlossen werden. **◀ ZITIERT**
  2. Konnten die Angreifenden die IT-Systeme durch menschliche Fehlhandlungen kompromittieren, MÜSSEN organisatorische, personelle und technische Maßnahmen ergriffen werden, um ähnliche Vorfälle künftig zu verhindern. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Das Schließen einer ausgenutzten technischen Schwachstelle stellt die allgemeine Beseitigung der Fehlerursache durch eine Korrekturmaßnahme gemäß VRB.4.1 dar.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme VRB.4.1 fordert allgemeingültig die Festlegung angemessener organisatorischer, personeller und technischer Korrekturmaßnahmen zur Beseitigung von Fehlerursachen, um das Wiederkehren von Vorfällen zu verhindern.

### → DER.3.1.A25 — Nachbereitung eines Audits (S)
  1. Die Institution SOLLTE die im Auditbericht oder bei einer Revision festgestellten Abweichungen oder Mängel in einer angemessenen Zeit abstellen. **◀ ZITIERT**
  2. Die durchzuführenden Korrekturmaßnahmen inklusive Zeitpunkt und Zuständigkeiten SOLLTEN dokumentiert werden.
  3. Auch abgeschlossene Korrekturmaßnahmen SOLLTEN dokumentiert werden.
  4. Die Institution SOLLTE dazu ein definiertes Verfahren etablieren und einsetzen.
  5. Gab es schwerwiegende Abweichungen oder Mängel, SOLLTE das Audit- bzw. Revisionsteam überprüfen, ob die Korrekturmaßnahmen durchgeführt wurden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) VRB.4.1 fordert das Festlegen angemessener Korrekturmaßnahmen zur Beseitigung von Fehlerursachen und deckt damit das Abstellen von festgestellten Mängeln inhaltlich ab.

### → DER.3.1.A4 — Durchführung einer Revision (B)
  1. Bei einer Revision MUSS das Revisionsteam prüfen, ob die Anforderungen vollständig, korrekt, angemessen und aktuell umgesetzt sind.
  2. Die Institution MUSS festgestellte Abweichungen so schnell wie möglich korrigieren. **◀ ZITIERT**
  3. Die jeweiligen Revisionen MÜSSEN mit einer Änderungsverfolgung dokumentiert werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) VRB.4.1 fordert die Festlegung von Korrekturmaßnahmen zur Beseitigung von Fehlerursachen und deckt damit die Korrektur festgestellter Abweichungen inhaltlich ab.

### → DER.4.A14 — Regelmäßige Überprüfung und Verbesserung der Notfallmaßnahmen (H) [Institutionsleitung]
  1. Alle Notfallmaßnahmen SOLLTEN regelmäßig oder bei größeren Änderungen daraufhin überprüft werden, ob sie noch eingehalten und korrekt umgesetzt werden.
  2. Es SOLLTE geprüft werden, ob sie sich noch dazu eignen, die definierten Ziele zu erreichen.
  3. Dabei SOLLTE untersucht werden, ob technische Maßnahmen korrekt implementiert und konfiguriert wurden und ob organisatorische Maßnahmen effektiv und effizient umgesetzt sind.
  4. Bei Abweichungen SOLLTEN die Ursachen für die Mängel ermittelt und Verbesserungsmaßnahmen veranlasst werden. **◀ ZITIERT**
  5. Diese Ergebnisübersicht SOLLTE von der Institutionsleitung freigegeben werden.
  6. Es SOLLTE zudem ein Prozess etabliert werden, der steuert und überwacht, ob und wie die Verbesserungsmaßnahmen umgesetzt werden.
  7. Verzögerungen SOLLTEN frühzeitig an die Institutionsleitung gemeldet werden.
  8. Es SOLLTE von der Institutionsleitung festgelegt sein, wie die Überprüfungen koordiniert werden.
  9. Die Überprüfungen SOLLTEN so geplant werden, dass kein relevanter Teil ausgelassen wird.
  10. Insbesondere SOLLTEN die im Bereich der Revision, der IT, des Sicherheitsmanagements, des Informationssicherheitsmanagements und des Notfallmanagements durchgeführten Überprüfungen miteinander koordiniert werden.
  11. Dazu SOLLTE geregelt werden, welche Maßnahmen wann und von wem überprüft werden.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) VRB.4.1 fordert die Festlegung von Korrekturmaßnahmen zur Beseitigung von Fehlerursachen, was der Ursachenermittlung und Maßnahmenveranlassung bei Mängeln und Abweichungen entspricht.

### → DER.4.A15 — Bewertung der Leistungsfähigkeit des Notfallmanagementsystems (H) [Institutionsleitung]
  1. Es SOLLTE regelmäßig bewertet werden, wie leistungsfähig und effektiv das Notfallmanagement-System ist.
  2. Als Grundlage SOLLTEN Mess- und Bewertungskriterien wie z. B. Leistungskennzahlen definiert werden.
  3. Diese Messgrößen SOLLTEN regelmäßig ermittelt und mit geeigneten vorangegangenen Werten, mindestens aber mit den Vorjahreswerten, verglichen werden.
  4. Weichen die Werte negativ ab, SOLLTEN die Ursachen ermittelt und Verbesserungsmaßnahmen definiert werden. **◀ ZITIERT**
  5. Die Ergebnisse der Bewertung SOLLTEN an die Leitung berichtet werden.
  6. Die Leitung SOLLTE entscheiden, mit welchen Maßnahmen das Notfallmanagement weiterentwickelt werden soll.
  7. Alle Entscheidungen der Institutionsleitung SOLLTEN dokumentiert und die bisherigen Aufzeichnungen aktualisiert werden.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) VRB.4.1 fordert die Festlegung von Maßnahmen zur Beseitigung von Fehlerursachen, was die Ursachenermittlung und Maßnahmenfestlegung bei negativen Abweichungen inhaltlich abdeckt.

### → INF.13.A12 — Sichere Konfiguration der TGM-Systeme (S)
  1. Alle Systeme des TGM sowie die Systeme, die durch das TGM betrieben werden, SOLLTEN sicher konfiguriert werden.
  2. Die Konfiguration SOLLTE mindestens vor Inbetriebnahme eines Systems getestet werden.
  3. Konfigurationsänderungen während des Produktivbetriebs SOLLTEN vor Aktivierung auf einer Testinstanz getestet oder nur im Vier-Augen-Prinzip durchgeführt werden.
  4. Die Konfiguration von Systemen SOLLTE gesichert werden, um ein schnelles Wiedereinspielen einer fehlerfreien Version zu ermöglichen (Rollback).
  5. Rollback-Tests SOLLTEN auf einem Testsystem eingerichtet oder während Wartungsfenstern durchgeführt werden.
  6. Die Konfigurationen SOLLTEN zentral gespeichert werden.
  7. Für gleichartige Systeme, inklusive der Geräte der Automations- und Feldebene (siehe Kapitel 4.1 Genutzte TGM-spezifische Fachbegriffe), SOLLTE eine automatisierte Verteilung von Software-Updates und Konfigurationen eingerichtet werden.
  8. Konfigurationsänderungen SOLLTEN allen Beteiligten an Betriebs- und Serviceprozessen (Entstörung, Rufbereitschaft, Wartungen etc.) bekannt gemacht werden, insbesondere Änderungen der Zugangsmechanismen oder der Passwörter sowie Änderungen an Kommunikations- und Steuerparametern für die eingebundenen Systeme.
  9. Es SOLLTE sichergestellt werden, dass im Störungsfall beispielsweise eine Wartungstechnikerin oder ein Wartungstechniker das System bedienen bzw. parametrieren kann.
  10. Außerdem SOLLTE regelmäßig und zusätzlich bei Bedarf geprüft werden, ob die Systeme gemäß den Vorgaben konfiguriert sind.
  11. Die Ergebnisse SOLLTEN nachvollziehbar dokumentiert werden.
  12. Abweichungen von den Vorgaben SOLLTEN behoben werden. **◀ ZITIERT**
- **Satz 12** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 12) G++ VRB.4.1 fordert das Festlegen angemessener Korrekturmaßnahmen zur Beseitigung von Fehlern bzw. Nicht-Konformitäten und deckt damit die Behebung festgestellter Abweichungen von Vorgaben allgemein ab.

### → INF.13.A6 — Erstellung eines TGM-Konzepts (S) [Planende]
  1. Ausgehend von der Sicherheitsrichtlinie für das TGM SOLLTE ein TGM-Konzept erstellt und gepflegt werden.
  2. Dabei SOLLTEN mindestens folgende Aspekte bedarfsgerecht berücksichtigt werden: Methoden, Techniken und Werkzeuge für das TGM Absicherung des Zugangs und der Kommunikation Absicherung auf Ebene des Netzes, insbesondere Zuordnung von TGM-Komponenten zu Netzsegmenten Umfang des Monitorings und der Alarmierung Protokollierung von Ereignissen und administrativen Zugriffen Meldeketten bei Störungen und Sicherheitsvorfällen benötigte Prozesse für das TGM Bereitstellung von TGM-Informationen für andere Betriebsbereiche Einbindung des TGM in die Notfallplanung Das TGM-Konzept SOLLTE regelmäßig und zusätzlich bei Bedarf geprüft und gegebenenfalls aktualisiert werden, um dem aktuellen Stand der Technik zu entsprechen und auch neue Erkenntnisse abdecken zu können.
  3. Außerdem SOLLTE regelmäßig ein Soll-Ist-Vergleich zwischen den Vorgaben des Konzepts und dem aktuellen Zustand durchgeführt werden.
  4. Dabei SOLLTE insbesondere geprüft werden, ob die Systeme gemäß den Vorgaben konfiguriert sind.
  5. Die Ergebnisse SOLLTEN nachvollziehbar dokumentiert werden.
  6. Abweichungen SOLLTEN behoben werden. **◀ ZITIERT**
- **Satz 6** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 6) G++-Maßnahme VRB.4.1 fordert die Festlegung von Korrekturmaßnahmen zur Behebung von Fehlern und Nichtkonformitäten, was die generelle Entsprechung zur Behebung festgestellter Abweichungen darstellt.

### → INF.14.A3 — Sichere Anbindung von TGA-Anlagen und GA-Systemen (B)
  1. Für alle TGA-Anlagen, GA-Systeme und GA-relevanten Komponenten MUSS festgelegt werden, ob durch andere TGA-Anlagen, GA-Systeme oder GA-relevante Komponenten Aktionen ausgelöst werden dürfen.
  2. Falls eine solche Integration zulässig ist, SOLLTE reglementiert werden, welche automatisierten Aktionen durch welche Informationen eines GA-Systems ausgelöst werden dürfen.
  3. Falls eine TGA-Anlage nicht in ein GA-System integriert werden kann oder darf, diese jedoch an ein GA-System gekoppelt werden soll, MUSS festgelegt werden, welche Informationen der TGA-Anlage an das GA-System gemeldet werden.
  4. Sowohl die Integration von TGA-Anlagen in ein GA-System als auch die rückwirkungsfreie Kopplung von TGA-Anlagen an GA-Systeme MÜSSEN angemessen abgesichert sein.
  5. Ebenfalls MUSS die Anbindung von GA-Systemen untereinander angemessen abgesichert werden.
  6. Hierzu MÜSSEN insbesondere die Ablauf- und Funktionsketten innerhalb eines GA-Systems bzw. zwischen GA-Systemen angemessen geplant werden.
  7. Hierbei MÜSSEN alle Übergänge zwischen Gewerken und Techniken berücksichtigt werden.
  8. Diese Ablauf- und Funktionsketten MÜSSEN umfassend getestet und bei Fehlverhalten nachjustiert werden.
  9. Die Festlegungen MÜSSEN vollumfänglich dokumentiert werden.
  10. Sowohl regelmäßig als auch ergänzend bei Bedarf SOLLTE geprüft werden, ob die Dokumentation noch aktuell ist.
  11. Bei Abweichungen MUSS die Ursache für die Abweichungen eruiert und behoben werden. **◀ ZITIERT**
- **Satz 11** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 11) Die G++-Maßnahme VRB.4.1 fordert die Beseitigung der Ursachen von Fehlern durch angemessene Korrekturmaßnahmen und deckt damit die Ursachenermittlung und -behebung bei Abweichungen allgemein ab.

### → ISMS.1.A11 — Aufrechterhaltung der Informationssicherheit (S)
  1. Der Sicherheitsprozess, die Sicherheitskonzepte, die Leitlinie zur Informationssicherheit und die Organisationsstruktur für Informationssicherheit SOLLTEN regelmäßig auf Wirksamkeit und Angemessenheit überprüft und aktualisiert werden.
  2. Dazu SOLLTEN regelmäßig Vollständigkeits- bzw. Aktualisierungsprüfungen des Sicherheitskonzeptes durchgeführt werden.
  3. Ebenso SOLLTEN regelmäßig Sicherheitsrevisionen durchgeführt werden.
  4. Dazu SOLLTE geregelt sein, welche Bereiche und Sicherheitsmaßnahmen wann und von wem zu überprüfen sind.
  5. Überprüfungen des Sicherheitsniveaus SOLLTEN regelmäßig (mindestens jährlich) sowie anlassbezogen durchgeführt werden.
  6. Die Prüfungen SOLLTEN von qualifizierten und unabhängigen Personen durchgeführt werden.
  7. Die Ergebnisse der Überprüfungen SOLLTEN nachvollziehbar dokumentiert sein.
  8. Darauf aufbauend SOLLTEN Mängel beseitigt und Korrekturmaßnahmen ergriffen werden. **◀ ZITIERT**
- **Satz 8** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 8) Die Maßnahme VRB.4.1 fordert explizit das Festlegen von Korrekturmaßnahmen zur Beseitigung von Fehlerursachen und deckt damit die Forderung nach Mängelbeseitigung und Korrekturmaßnahmen inhaltlich direkt ab.

### → NET.2.1.A10 — Erstellung einer Sicherheitsrichtlinie für den Betrieb von WLANs (S)
  1. Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution SOLLTEN die wesentlichen Kernaspekte für einen sicheren Einsatz von WLANs konkretisiert werden.
  2. Die Richtlinie SOLLTE allen Verantwortlichen bekannt sein, die an Aufbau und Betrieb von WLANs beteiligt sind.
  3. Sie SOLLTE zudem Grundlage für ihre Arbeit sein.
  4. Die Umsetzung der in der Richtlinie geforderten Inhalte SOLLTE regelmäßig überprüft werden.
  5. Werden die Inhalte der Richtlinie nicht umgesetzt, MUSS geeignet reagiert werden. **◀ ZITIERT**
  6. Die Ergebnisse SOLLTEN geeignet dokumentiert werden.
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) VRB.4.1 fordert die Festlegung angemessener Korrekturmaßnahmen bei Fehlern bzw. Nicht-Konformitäten und deckt damit die geforderte angemessene Reaktion bei Nicht-Umsetzung von Richtlinienvorgaben ab.

### → NET.2.2.A1 — Erstellung einer Nutzungsrichtlinie für WLAN (B) [IT-Betrieb]
  1. Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution MÜSSEN die wesentlichen Kernaspekte für eine sichere WLAN-Nutzung in einer WLAN-Nutzungsrichtlinie konkretisiert werden.
  2. In einer solchen Nutzungsrichtlinie MÜSSEN die Besonderheiten bei der WLAN-Nutzung beschrieben sein, z. B. ob, wie und mit welchen Geräten Hotspots genutzt werden dürfen.
  3. Die Richtlinie MUSS Angaben dazu enthalten, welche Daten im WLAN genutzt und übertragen werden dürfen und welche nicht.
  4. Es MUSS beschrieben sein, wie mit clientseitigen Sicherheitslösungen umzugehen ist.
  5. Die Nutzungsrichtlinie MUSS ein klares Verbot enthalten, ungenehmigte Access Points an das Netz der Institution anzuschließen.
  6. Außerdem MUSS in der Richtlinie darauf hingewiesen werden, dass die WLAN-Schnittstelle deaktiviert werden muss, wenn sie über einen längeren Zeitraum nicht genutzt wird.
  7. Es MUSS regelmäßig überprüft werden, ob die in der Richtlinie geforderten Inhalte richtig umgesetzt werden.
  8. Ist dies nicht der Fall, MUSS geeignet reagiert werden. **◀ ZITIERT**
  9. Die Ergebnisse SOLLTEN sinnvoll dokumentiert werden.
- **Satz 8** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 8) VRB.4.1 fordert das Festlegen angemessener Korrekturmaßnahmen bei festgestellten Abweichungen bzw. Fehlern und deckt damit die allgemeinere Fassung der geforderten Reaktion bei mangelhafter Richtlinienumsetzung ab.

### → NET.3.1.A23 — Revision und Penetrationstests (S)
  1. Router und Switches SOLLTEN regelmäßig auf bekannte Sicherheitsprobleme hin überprüft werden.
  2. Auch SOLLTEN regelmäßig Revisionen durchgeführt werden.
  3. Dabei SOLLTE unter anderem geprüft werden, ob der Ist-Zustand der festgelegten sicheren Grundkonfiguration entspricht.
  4. Die Ergebnisse SOLLTEN nachvollziehbar dokumentiert und mit dem Soll-Zustand abgeglichen werden.
  5. Abweichungen SOLLTE nachgegangen werden. **◀ ZITIERT**
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) Die Forderung nach angemessenen Korrekturmaßnahmen zur Beseitigung von Fehlerursachen deckt das Nachgehen und Beheben von festgestellten Abweichungen inhaltlich als übergeordnete Managementtätigkeit ab.

### → OPS.1.1.3.A9 — Test- und Abnahmeverfahren für neue Hardware (S)
  1. Wenn neue Hardware ausgewählt wird, SOLLTE geprüft werden, ob die eingesetzte Software und insbesondere die relevanten Betriebssysteme mit der Hardware und deren Treibersoftware kompatibel sind.
  2. Neue Hardware SOLLTE getestet werden, bevor sie eingesetzt wird.
  3. Diese SOLLTE ausschließlich in einer isolierten Umgebung getestet werden.
  4. Für IT-Systeme SOLLTE es ein Abnahmeverfahren und eine Freigabeerklärung geben.
  5. Die Zuständigen SOLLTEN die Freigabeerklärungen an geeigneter Stelle schriftlich hinterlegen.
  6. Für den Fall, dass trotz der Abnahme- und Freigabeverfahren im laufenden Betrieb Fehler festgestellt werden, SOLLTE es ein Verfahren zur Fehlerbehebung geben. **◀ ZITIERT**
- **Satz 6** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 6) VRB.4.1 fordert allgemeingültig die Festlegung angemessener Korrekturmaßnahmen zur Behebung von Fehlern und deren Ursachen, was das geforderte Verfahren zur Fehlerbehebung im laufenden Betrieb inhaltlich abdeckt.

### → OPS.1.2.2.A13 — Regelmäßige Revision der Archivierungsprozesse (S)
  1. Es SOLLTE regelmäßig überprüft werden, ob die Archivierungsprozesse noch korrekt und ordnungsgemäß funktionieren.
  2. Dazu SOLLTE eine Checkliste erstellt werden, die Fragen zu Verantwortlichkeiten, Organisationsprozessen, zum Einsatz der Archivierung, zur Redundanz der Archivdaten, zur Administration und zur technischen Beurteilung des Archivsystems enthält.
  3. Die Auditergebnisse SOLLTEN nachvollziehbar dokumentiert und mit dem Soll-Zustand abgeglichen werden.
  4. Abweichungen SOLLTE nachgegangen werden. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) VRB.4.1 verlangt die Festlegung von Korrekturmaßnahmen zur Beseitigung von Fehlerursachen, was das Nachgehen und Behandeln identifizierter Abweichungen auf allgemeiner Ebene abdeckt.

### → ORP.5.A2 — Beachtung der Rahmenbedingungen (B) [Vorgesetzte, Zentrale Verwaltung, Institutionsleitung]
  1. Die als sicherheitsrelevant identifizierten Anforderungen MÜSSEN bei der Planung und Konzeption von Geschäftsprozessen, Anwendungen und IT-Systemen oder bei der Beschaffung neuer Komponenten einfließen.
  2. Führungskräfte, die eine rechtliche Verantwortung für die Institution tragen, MÜSSEN für die Einhaltung der gesetzlichen, vertraglichen und sonstigen Vorgaben sorgen.
  3. Die Verantwortlichkeiten und Zuständigkeiten für die Einhaltung dieser Vorgaben MÜSSEN festgelegt sein.
  4. Es MÜSSEN geeignete Maßnahmen identifiziert und umgesetzt werden, um Verstöße gegen relevante Anforderungen zu vermeiden.
  5. Wenn solche Verstöße erkannt werden, MÜSSEN sachgerechte Korrekturmaßnahmen ergriffen werden, um die Abweichungen zu beheben. **◀ ZITIERT**
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 5) Die G++-Maßnahme VRB.4.1 fordert explizit das Festlegen angemessener Korrekturmaßnahmen zur Behebung von Fehlern und Nicht-Konformitäten und deckt damit die Forderung von Satz 5 inhaltlich ab.

### → SYS.1.5.A19 — Regelmäßige Audits der Virtualisierungsinfrastruktur (S)
  1. Es SOLLTE regelmäßig auditiert werden, ob der Ist-Zustand der virtuellen Infrastruktur dem in der Planung festgelegten Zustand entspricht.
  2. Auch SOLLTE regelmäßig auditiert werden, ob die Konfiguration der virtuellen Komponenten die vorgegebene Standardkonfiguration einhält.
  3. Die Auditergebnisse SOLLTEN nachvollziehbar dokumentiert werden.
  4. Abweichungen SOLLTEN behoben werden. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) VRB.4.1 fordert die Festlegung von Korrekturmaßnahmen zur Beseitigung von Fehlern bzw. Nicht-Konformitäten und deckt damit die Behebung festgestellter Abweichungen ab.

### → SYS.3.2.2.A20 — Regelmäßige Überprüfung des MDM (B)
  1. Sicherheitseinstellungen MÜSSEN regelmäßig überprüft werden.
  2. Bei neuen Betriebssystemversionen der mobilen Endgeräte MUSS vorab geprüft werden, ob das MDM diese vollständig unterstützt und die Konfigurationsprofile und Sicherheitseinstellungen weiterhin wirksam und ausreichend sind.
  3. Abweichungen MÜSSEN korrigiert werden. **◀ ZITIERT**
  4. Die zugeteilten Berechtigungen für Benutzende und Administrierende MÜSSEN regelmäßig daraufhin überprüft werden, ob sie weiterhin angemessen sind (Minimalprinzip).
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) G++-Maßnahme VRB.4.1 verlangt allgemein die Festlegung von Korrekturmaßnahmen zur Beseitigung von Fehlern und deckt damit die Korrektur festgestellter Abweichungen ab.

### → DER.3.2.A22 — Nachbereitung einer IS-Revision (S)
  1. Die im IS-Revisionsbericht festgestellten Abweichungen SOLLTEN in einer angemessenen Zeit durch die Institution korrigiert werden. **◀ ZITIERT**
  2. Die durchzuführenden Korrekturmaßnahmen SOLLTEN mit Zuständigkeiten, Umsetzungstermin und dem jeweiligen Status dokumentiert sein.
  3. Die Umsetzung SOLLTE kontinuierlich nachverfolgt und der Umsetzungsstatus fortgeschrieben werden.
  4. Grundsätzlich SOLLTE geprüft werden, ob ergänzende IS-Revisionen notwendig sind.
  5. Die Institution SOLLTE die Grob- und Detailplanung zur IS-Revision anpassen.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) VRB.4.1 fordert die Festlegung angemessener Korrekturmaßnahmen zur Beseitigung von Fehlerursachen und deckt damit die Korrektur festgestellter Abweichungen auf allgemeiner Ebene inhaltlich ab.


## VRB.6.2 — Bewertung der erreichten Verbesserung  [1 Paare]

**Statement (normativ):** Verbesserung SOLLTE ein Verfahren zur Bewertung der erreichten Verbesserung unter Berücksichtigung der damit verbundenen Vor- und Nachteile verankern.
**Klasse:** BSI-Methodik-Grundschutz-plus-plus | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Die Bewertung kann beispielsweise durch interne Audits, die Messung von Key Performance Indicators (KPIs) vor und nach der Maßnahmenumsetzung oder durch technische Überprüfungen erfolgen. Im Ergebnis ist das Sicherheitsniveau der Institution transparent dargestellt und Trends der Verbesserung des Sicherheitsniveaus, insbesondere auch durch die Vergleichbarkeit mit vorigen Bewertungen, ableitbar.

### → DER.4.A15 — Bewertung der Leistungsfähigkeit des Notfallmanagementsystems (H) [Institutionsleitung]
  1. Es SOLLTE regelmäßig bewertet werden, wie leistungsfähig und effektiv das Notfallmanagement-System ist.
  2. Als Grundlage SOLLTEN Mess- und Bewertungskriterien wie z. B. Leistungskennzahlen definiert werden.
  3. Diese Messgrößen SOLLTEN regelmäßig ermittelt und mit geeigneten vorangegangenen Werten, mindestens aber mit den Vorjahreswerten, verglichen werden. **◀ ZITIERT**
  4. Weichen die Werte negativ ab, SOLLTEN die Ursachen ermittelt und Verbesserungsmaßnahmen definiert werden.
  5. Die Ergebnisse der Bewertung SOLLTEN an die Leitung berichtet werden.
  6. Die Leitung SOLLTE entscheiden, mit welchen Maßnahmen das Notfallmanagement weiterentwickelt werden soll.
  7. Alle Entscheidungen der Institutionsleitung SOLLTEN dokumentiert und die bisherigen Aufzeichnungen aktualisiert werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 3) Satz 3 fordert den regelmäßigen Vergleich von Messgrößen mit vorangegangenen Werten zur Leistungsbewertung, was dem KPI-basierten Bewertungsverfahren aus VRB.6.2 entspricht.


## VRB.1.1 — Verfahren zur kontinuierlichen Verbesserung  [6 Paare]

**Statement (normativ):** Verbesserung MUSS ein Verfahren zur kontinuierlichen Verbesserung des ISMS verankern.
**Klasse:** BSI-Methodik-Grundschutz-plus-plus | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Im Verfahren zur Verbesserung werden Erkenntnisse aus der Überwachung in konkrete Verbesserungsmaßnahmen umgesetzt. Die kontinuierliche Verbesserung schließt den PDCA-Zyklus der Methodik ab und stellt sicher, dass die Informationssicherheit stetig weiterentwickelt und verbessert wird. Hierbei erfolgen Änderungen im ISMS geplant und strukturiert und werden systematisch dokumentiert, um die Vergleichbarkeit und Nachvollziehbarkeit sowie die kohärente Managementbewertung sicherzustellen.

### → DER.3.1.A1 — Definition von Verantwortlichkeiten (B) [Institutionsleitung]
  1. Die Institutionsleitung MUSS eine Person benennen, die dafür zuständig ist, Audits bzw. Revisionen zu planen und zu initiieren.
  2. Dabei MUSS die Institutionsleitung darauf achten, dass keine Interessenkonflikte entstehen.
  3. Die Institution MUSS die Ergebnisse der Audits und Revisionen dazu verwenden, um die Sicherheitsmaßnahmen zu verbessern. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) VRB.1.1 verlangt ein Verfahren zur kontinuierlichen Verbesserung des ISMS, welches Erkenntnisse aus Prüfungen und Überwachungen systematisch zur Verbesserung der Sicherheitsmaßnahmen nutzt.

### → DER.3.1.A25 — Nachbereitung eines Audits (S)
  1. Die Institution SOLLTE die im Auditbericht oder bei einer Revision festgestellten Abweichungen oder Mängel in einer angemessenen Zeit abstellen.
  2. Die durchzuführenden Korrekturmaßnahmen inklusive Zeitpunkt und Zuständigkeiten SOLLTEN dokumentiert werden.
  3. Auch abgeschlossene Korrekturmaßnahmen SOLLTEN dokumentiert werden.
  4. Die Institution SOLLTE dazu ein definiertes Verfahren etablieren und einsetzen. **◀ ZITIERT**
  5. Gab es schwerwiegende Abweichungen oder Mängel, SOLLTE das Audit- bzw. Revisionsteam überprüfen, ob die Korrekturmaßnahmen durchgeführt wurden.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) VRB.1.1 verlangt die Etablierung eines systematischen Verfahrens zur Umsetzung von Erkenntnissen in Verbesserungs- und Korrekturmaßnahmen, was die Forderung nach einem definierten Nachbereitungsverfahren abdeckt.

### → DER.3.1.A5 — Integration in den Informationssicherheitsprozess (S)
  1. Die Institution SOLLTE eine Richtlinie zur internen ISMS-Auditierung vorgeben.
  2. Außerdem sollte sie eine Richtlinie zur Lenkung von Korrekturmaßnahmen erstellen.
  3. Die Richtlinien SOLLTEN vorgeben, dass regelmäßige Audits und Revisionen ein Teil des Sicherheitsprozesses sind und durch diesen initiiert werden.
  4. Der oder die ISB SOLLTE sicherstellen, dass die Ergebnisse der Audits und Revisionen in das ISMS zurückfließen und dieses verbessern. **◀ ZITIERT**
  5. Der oder die ISB SOLLTE die durchgeführten Audits und Revisionen und deren Ergebnisse in den regelmäßigen Bericht an die Institutionsleitung aufnehmen.
  6. Auch SOLLTE dort festgehalten werden, welche Mängel beseitigt wurden und wie die Qualität verbessert wurde.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 4) Die G++-Maßnahme VRB.1.1 etabliert das allgemeine Verfahren zur kontinuierlichen Verbesserung des ISMS, bei dem Erkenntnisse aus Überprüfungen und Audits systematisch in Verbesserungsmaßnahmen des ISMS überführt werden.

### → DER.3.2.A9 — Integration in den Informationssicherheitsprozess (S)
  1. Die Institution SOLLTE sicherstellen, dass IS-Revisionen ein Teil des Sicherheitsprozesses sind.
  2. Außerdem SOLLTEN die Ergebnisse von IS-Revisionen in das ISMS zurückfließen und zu dessen Verbesserung beitragen. **◀ ZITIERT**
  3. Weiter SOLLTEN die Ergebnisse der IS-Revisionen sowie die Aktivitäten, um Mängel zu beseitigen und um die Qualität zu verbessern, in den regelmäßigen Bericht des oder der ISB an die Institutionsleitung aufgenommen werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) VRB.1.1 verankert das allgemeine Verfahren zur kontinuierlichen Verbesserung des ISMS, in dem Erkenntnisse aus Überprüfungen und Revisionen zur stetigen Weiterentwicklung und Verbesserung verarbeitet werden.

### → OPS.3.2.A12 — Durchführung einer risikoorientierten Betrachtung von Prozessen, Anwendungen und IT-Systemen (S)
  1. Werden Prozesse, Anwendungen oder IT-Systeme neu aufgebaut und Kunden bereitgestellt, SOLLTEN diese regelmäßig und anlassbezogen risikoorientiert betrachtet und dokumentiert werden.
  2. Aus den sich daraus ergebenen Ergebnissen SOLLTEN geeignete Maßnahmen festgelegt werden.
  3. Darüber hinaus SOLLTEN die Resultate dazu verwendet werden, um das Informationssicherheitsmanagement weiter zu verbessern. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) G++ VRB.1.1 fordert die Verankerung eines Verfahrens zur kontinuierlichen Verbesserung des ISMS, in dem Erkenntnisse und Resultate systematisch zur Weiterentwicklung des Informationssicherheitsmanagements genutzt werden.

### → ISMS.1.A11 — Aufrechterhaltung der Informationssicherheit (S)
  1. Der Sicherheitsprozess, die Sicherheitskonzepte, die Leitlinie zur Informationssicherheit und die Organisationsstruktur für Informationssicherheit SOLLTEN regelmäßig auf Wirksamkeit und Angemessenheit überprüft und aktualisiert werden. **◀ ZITIERT**
  2. Dazu SOLLTEN regelmäßig Vollständigkeits- bzw. Aktualisierungsprüfungen des Sicherheitskonzeptes durchgeführt werden.
  3. Ebenso SOLLTEN regelmäßig Sicherheitsrevisionen durchgeführt werden.
  4. Dazu SOLLTE geregelt sein, welche Bereiche und Sicherheitsmaßnahmen wann und von wem zu überprüfen sind.
  5. Überprüfungen des Sicherheitsniveaus SOLLTEN regelmäßig (mindestens jährlich) sowie anlassbezogen durchgeführt werden.
  6. Die Prüfungen SOLLTEN von qualifizierten und unabhängigen Personen durchgeführt werden.
  7. Die Ergebnisse der Überprüfungen SOLLTEN nachvollziehbar dokumentiert sein.
  8. Darauf aufbauend SOLLTEN Mängel beseitigt und Korrekturmaßnahmen ergriffen werden.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 1) Satz 1 fordert die regelmäßige Überprüfung und Aktualisierung des Sicherheitsprozesses und der zugehörigen Konzepte, was die kontinuierliche Weiterentwicklung und Verbesserung des ISMS operationalisiert.


## VRB.4.2 — Verbesserungsmaßnahmen  [5 Paare]

**Statement (normativ):** Verbesserung MUSS angemessene Maßnahmen zur Nutzung von Verbesserungspotentialen unter Berücksichtigung der damit verbundenen Vor- und Nachteile festlegen.
**Klasse:** BSI-Methodik-Grundschutz-plus-plus | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Verbesserungen zielen nicht primär auf die Behebung von Problemen, sondern auf die proaktive Weiterentwicklung des ISMS ab. Sie können beispielsweise folgende Bereiche adressieren: Optimierung von Prozessen und Abläufen im ISMS; Einführung neuer oder verbesserter Technologien und Methoden; Stärkung der Sicherheitskultur und des Sicherheitsbewusstseins; Erweiterung des Anwendungsbereiches des ISMS; Verbesserung der Integration des ISMS in andere Managementsysteme und Geschäftsprozesse.

### → DER.2.1.A18 — Weiterentwicklung der Prozesse durch Erkenntnisse aus Sicherheitsvorfällen und Branchenentwicklungen (S) [Fachverantwortliche]
  1. Nachdem ein Sicherheitsvorfall analysiert wurde, SOLLTE untersucht werden, ob die Prozesse und Abläufe im Rahmen der Behandlung von Sicherheitsvorfällen geändert oder weiterentwickelt werden müssen.
  2. Dabei SOLLTEN alle Personen, die an dem Vorfall beteiligt waren, über ihre jeweiligen Erfahrungen berichten.
  3. Es SOLLTE geprüft werden, ob es neue Entwicklungen im Bereich Incident Management und in der Forensik gibt und ob diese in die jeweiligen Dokumente und Abläufe eingebracht werden können. **◀ ZITIERT**
  4. Werden Hilfsmittel und Checklisten eingesetzt, z. B. für Service-Desk-Mitarbeitende, SOLLTE geprüft werden, ob diese um relevante Fragen und Informationen zu erweitern sind.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 3) Satz 3 fordert die Prüfung und Einbringung neuer Entwicklungen und Methoden in Prozesse und Dokumente, was der Festlegung von Verbesserungsmaßnahmen zur Nutzung von Verbesserungspotenzialen entspricht.

### → DER.3.1.A5 — Integration in den Informationssicherheitsprozess (S)
  1. Die Institution SOLLTE eine Richtlinie zur internen ISMS-Auditierung vorgeben.
  2. Außerdem sollte sie eine Richtlinie zur Lenkung von Korrekturmaßnahmen erstellen.
  3. Die Richtlinien SOLLTEN vorgeben, dass regelmäßige Audits und Revisionen ein Teil des Sicherheitsprozesses sind und durch diesen initiiert werden.
  4. Der oder die ISB SOLLTE sicherstellen, dass die Ergebnisse der Audits und Revisionen in das ISMS zurückfließen und dieses verbessern. **◀ ZITIERT**
  5. Der oder die ISB SOLLTE die durchgeführten Audits und Revisionen und deren Ergebnisse in den regelmäßigen Bericht an die Institutionsleitung aufnehmen.
  6. Auch SOLLTE dort festgehalten werden, welche Mängel beseitigt wurden und wie die Qualität verbessert wurde.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 4) Satz 4 fordert die Nutzung von Audit- und Revisionsergebnissen zur kontinuierlichen Verbesserung des ISMS, was eine konkrete Maßnahme zur Nutzung von Verbesserungspotenzialen darstellt.

### → DER.4.A15 — Bewertung der Leistungsfähigkeit des Notfallmanagementsystems (H) [Institutionsleitung]
  1. Es SOLLTE regelmäßig bewertet werden, wie leistungsfähig und effektiv das Notfallmanagement-System ist.
  2. Als Grundlage SOLLTEN Mess- und Bewertungskriterien wie z. B. Leistungskennzahlen definiert werden.
  3. Diese Messgrößen SOLLTEN regelmäßig ermittelt und mit geeigneten vorangegangenen Werten, mindestens aber mit den Vorjahreswerten, verglichen werden.
  4. Weichen die Werte negativ ab, SOLLTEN die Ursachen ermittelt und Verbesserungsmaßnahmen definiert werden.
  5. Die Ergebnisse der Bewertung SOLLTEN an die Leitung berichtet werden.
  6. Die Leitung SOLLTE entscheiden, mit welchen Maßnahmen das Notfallmanagement weiterentwickelt werden soll. **◀ ZITIERT**
  7. Alle Entscheidungen der Institutionsleitung SOLLTEN dokumentiert und die bisherigen Aufzeichnungen aktualisiert werden.
- **Satz 6** | Relation GS++→ED23: `superset-of` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 6) Satz 6 fordert die Entscheidung über Maßnahmen zur Weiterentwicklung des Managementsystems, was der Festlegung von Verbesserungsmaßnahmen nach VRB.4.2 entspricht.

### → OPS.3.2.A12 — Durchführung einer risikoorientierten Betrachtung von Prozessen, Anwendungen und IT-Systemen (S)
  1. Werden Prozesse, Anwendungen oder IT-Systeme neu aufgebaut und Kunden bereitgestellt, SOLLTEN diese regelmäßig und anlassbezogen risikoorientiert betrachtet und dokumentiert werden.
  2. Aus den sich daraus ergebenen Ergebnissen SOLLTEN geeignete Maßnahmen festgelegt werden.
  3. Darüber hinaus SOLLTEN die Resultate dazu verwendet werden, um das Informationssicherheitsmanagement weiter zu verbessern. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) VRB.4.2 verlangt die Festlegung von Maßnahmen zur Hebung von Verbesserungspotenzialen zur Weiterentwicklung des ISMS, was die geforderte Nutzung der Resultate zur ISMS-Verbesserung direkt abdeckt.

### → ORP.3.A8 — Messung und Auswertung des Lernerfolgs (S) [Personalabteilung]
  1. Die Lernerfolge im Bereich Informationssicherheit SOLLTEN zielgruppenbezogen gemessen und ausgewertet werden, um festzustellen, inwieweit die in den Sensibilisierungs- und Schulungsprogrammen zur Informationssicherheit beschriebenen Ziele erreicht sind.
  2. Die Messungen SOLLTEN sowohl quantitative als auch qualitative Aspekte der Sensibilisierungs- und Schulungsprogramme zur Informationssicherheit berücksichtigen.
  3. Die Ergebnisse SOLLTEN bei der Verbesserung des Sensibilisierungs- und Schulungsangebots zur Informationssicherheit in geeigneter Weise einfließen. **◀ ZITIERT**
  4. Der oder die Informationssicherheitsbeauftragte SOLLTE sich regelmäßig mit der Personalabteilung und den anderen für die Sicherheit relevanten Ansprechpartnern (Datenschutz, Gesundheits- und Arbeitsschutz, Brandschutz etc.) über die Effizienz der Aus- und Weiterbildung austauschen.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) VRB.4.2 fordert als allgemeinere Fassung die Festlegung von Maßnahmen zur Nutzung von Verbesserungspotenzialen (u. a. im Bereich des Sicherheitsbewusstseins), was das Einfließen von Evaluationsergebnissen in die Verbesserung des Schulungsangebots abdeckt.

