# Review-Dossier Praktik PERF

Praktik PERF: 22 Controls mit Mapping, 141 Paare gesamt. Gesampelt: 5 Controls (max/min/median Paarzahl + 2 zufällig).

## PERF.3.1.4 — Umfang von Audits  [21 Paare]

**Statement (normativ):** Monitoring-Evaluation MUSS in angemessenem Umfang Audits ausführen.
**Klasse:** BSI-Methodik-Grundschutz-plus-plus | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Der Umfang eines Audits beschreibt, was, wie und in welchem Rahmen geprüft wird. Dazu gehören der organisatorische und technische Geltungsbereich (z. B. Standorte, Abteilungen, IT-Systeme), der Prüfzeitraum, sowie die eingesetzten Prüfmethoden wie Interviews, Dokumentensichtung oder Systemtests. Der Auditumfang wird vor Beginn des Audits klar definiert, um den Ablauf gezielt zu planen und die Ergebnisse nachvollziehbar zu dokumentieren.

### → APP.3.1.A22 — Penetrationstest und Revision (S)
  1. Webanwendungen und Webservices SOLLTEN regelmäßig auf Sicherheitsprobleme hin überprüft werden.
  2. Insbesondere SOLLTEN regelmäßig Revisionen durchgeführt werden. **◀ ZITIERT**
  3. Die Ergebnisse SOLLTEN nachvollziehbar dokumentiert, ausreichend geschützt und vertraulich behandelt werden.
  4. Abweichungen SOLLTE nachgegangen werden.
  5. Die Ergebnisse SOLLTEN dem ISB vorgelegt werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme fordert die Durchführung von Audits in angemessenem Umfang und deckt damit die Durchführung von Revisionen inhaltlich ab.

### → APP.3.2.A16 — Penetrationstest und Revision (S)
  1. Webserver SOLLTEN regelmäßig auf Sicherheitsprobleme hin überprüft werden.
  2. Auch SOLLTEN regelmäßig Revisionen durchgeführt werden. **◀ ZITIERT**
  3. Die Ergebnisse SOLLTEN nachvollziehbar dokumentiert, ausreichend geschützt und vertraulich behandelt werden.
  4. Abweichungen SOLLTE nachgegangen werden.
  5. Die Ergebnisse SOLLTEN dem ISB vorgelegt werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die Maßnahme fordert explizit die Durchführung von Audits (Revisionen) in angemessenem Umfang und deckt damit die geforderte regelmäßige Durchführung von Revisionen inhaltlich ab.

### → APP.4.2.A27 — Audit des SAP-ERP-Systems (S) [Fachabteilung]
  1. Damit sichergestellt ist, dass alle internen und externen Richtlinien sowie Vorgaben eingehalten werden, SOLLTEN alle SAP-ERP-Systeme regelmäßig auditiert werden. **◀ ZITIERT**
  2. Dafür SOLLTE der Security Optimization Service im SAP Solution Manager benutzt werden.
  3. Die Ergebnisse des Audits SOLLTEN ausgewertet und dokumentiert werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die Durchführung von Audits für SAP-ERP-Systeme stellt eine konkrete Ausprägung der allgemeinen Forderung nach der Durchführung von Audits in angemessenem technischem Umfang dar.

### → APP.4.3.A20 — Regelmäßige Audits (S)
  1. Bei allen Komponenten des Datenbanksystems SOLLTE regelmäßig überprüft werden, ob alle festgelegten Sicherheitsmaßnahmen umgesetzt und diese korrekt konfiguriert sind. **◀ ZITIERT**
  2. Dabei SOLLTE geprüft werden, ob der dokumentierte Stand dem Ist-Zustand entspricht und ob die Konfiguration des Datenbankmanagementsystems der dokumentierten Standardkonfiguration entspricht.
  3. Zudem SOLLTE geprüft werden, ob alle Datenbank-Skripte benötigt werden.
  4. Auch SOLLTE geprüft werden, ob sie dem Qualitätsstandard der Institution genügen.
  5. Zusätzlich SOLLTEN die Protokolldateien des Datenbanksystems und des Betriebssystems nach Auffälligkeiten untersucht werden (siehe DER.1 Detektion von sicherheitsrelevanten Ereignissen).
  6. Die Auditergebnisse SOLLTEN nachvollziehbar dokumentiert sein.
  7. Sie SOLLTEN mit dem Soll-Zustand abgeglichen werden.
  8. Abweichungen SOLLTE nachgegangen werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme PERF.3.1.4 verlangt die Durchführung von Audits in angemessenem Umfang (einschließlich IT-Systemen und Prüfmethoden) und deckt damit die allgemeine Durchführung von Konfigurations- und Sicherheitsüberprüfungen an Systemkomponenten auf übergeordneter Ebene ab.

### → DER.3.1.A15 — Auswahl von geeigneten Prüfmethoden (S) [Auditteam]
  1. Das Auditteam SOLLTE für die jeweils zu prüfenden Sachverhalte geeignete Methoden einsetzen.
  2. Außerdem SOLLTE darauf geachtet werden, dass alle Prüfungen verhältnismäßig sind. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die Forderung nach der Durchführung von Audits in angemessenem Umfang deckt das Kriterium der Verhältnismäßigkeit aller Prüfungen inhaltlich ab.

### → DER.3.1.A3 — Durchführung eines Audits (B) [Auditteam]
  1. Bei einem Audit MUSS das Auditteam prüfen, ob die Anforderungen aus Richtlinien, Normen, Standards und anderen relevanten Vorgaben erfüllt sind. **◀ ZITIERT**
  2. Die geprüfte Institution MUSS die Anforderungen kennen.
  3. Das Auditteam MUSS bei jedem Audit eine Dokumentenprüfung sowie eine Vor-Ort-Prüfung durchführen. **◀ ZITIERT**
  4. Beim Vor-Ort-Audit MUSS das Auditteam sicherstellen, dass es niemals selbst aktiv in Systeme eingreift und keine Handlungsanweisungen zu Änderungen am Prüfgegenstand erteilt.
  5. Das Auditteam MUSS sämtliche Ergebnisse eines Audits schriftlich dokumentieren und in einem Auditbericht zusammenfassen.
  6. Der Auditbericht MUSS der zuständigen Stelle in der Institution zeitnah übermittelt werden.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) PERF.3.1.4 fordert die Durchführung von Audits in angemessenem Umfang, was die inhaltliche Prüfung der Einhaltung von Vorgaben und Standards im Rahmen des Audits als Kernaktivität abdeckt.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) PERF.3.1.4 fordert die Durchführung von Audits in angemessenem Umfang und deckt als allgemeinere Fassung die Festlegung und Durchführung der konkreten Prüfmethoden wie Dokumenten- und Vor-Ort-Prüfungen ab.

### → DER.3.2.A14 — Auswahl der Zielobjekte und der zu prüfenden Anforderungen (S) [IS-Revisionsteam]
  1. In einer IS-Querschnittsrevision oder IS-Partialrevision SOLLTE das IS-Revisionsteam anhand der Ergebnisse der Dokumentenprüfung die Baustein-Zielobjekte für die Vor-Ort-Prüfung auswählen.
  2. Der Baustein zum Informationssicherheitsmanagement (siehe ISMS.1 Sicherheitsmanagement) des IT-Grundschutz-Kompendiums einschließlich aller zugehörigen Anforderungen SOLLTE jedoch immer vollständig geprüft werden.
  3. Weitere dreißig Prozent der modellierten Baustein-Zielobjekte SOLLTEN risikoorientiert zur Prüfung ausgewählt werden.
  4. Die Auswahl SOLLTE nachvollziehbar dokumentiert werden.
  5. Von den so ausgewählten Baustein-Zielobjekten SOLLTEN dreißig Prozent der jeweiligen Anforderungen bei der IS-Revision geprüft werden. **◀ ZITIERT**
  6. Darüber hinaus SOLLTEN bei der Auswahl der zu prüfenden Baustein-Zielobjekte die bemängelten Anforderungen aus vorhergehenden IS-Revisionen berücksichtigt werden.
  7. Alle Anforderungen mit schwerwiegenden Sicherheitsmängeln aus vorhergehenden IS-Revisionen SOLLTEN mit geprüft werden.
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) Die G++-Maßnahme PERF.3.1.4 fordert allgemein die Durchführung von Audits in angemessenem Umfang, was die konkrete Festlegung des Prüfungsumfangs (30 Prozent der Anforderungen) als methodische Ausprägung abstrahierend abdeckt.

### → DER.3.2.A15 — Auswahl von geeigneten Prüfmethoden (S) [IS-Revisionsteam]
  1. Das IS-Revisionsteam SOLLTE sicherstellen, dass geeignete Prüfmethoden eingesetzt werden, um die zu prüfenden Sachverhalte zu ermitteln. **◀ ZITIERT**
  2. Alle Prüfungen SOLLTEN verhältnismäßig sein. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) PERF.3.1.4 verlangt die Durchführung von Audits in angemessenem Umfang, was laut Erläuterung explizit die Festlegung und den Einsatz geeigneter Prüfmethoden zur Ermittlung des Sachverhalts umfasst.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die Forderung nach der Ausfÿhrung von Audits in angemessenem Umfang deckt die geforderte Verhältnismäßigkeit von Prüfungen direkt ab.

### → DER.3.2.A17 — Durchführung der Vor-Ort-Prüfung (S) [IS-Revisionsteam]
  1. Bei der Vor-Ort-Prüfung SOLLTE das IS-Revisionsteam untersuchen und feststellen, ob die ausgewählten Maßnahmen die Anforderungen des IT-Grundschutzes angemessen und praxistauglich erfüllen.
  2. Die Prüfung SOLLTE mit einem Eröffnungsgespräch beginnen.
  3. Danach SOLLTEN alle für die Prüfung ausgewählten Anforderungen des Prüfplans bzw. alle Themenfelder der Prüfthemenliste überprüft werden. **◀ ZITIERT**
  4. Dafür SOLLTEN die vorgesehenen Prüfmethoden angewandt werden.
  5. Werden bei einer ausgewählten Stichprobe Abweichungen zum dokumentierten Status festgestellt, SOLLTE die Stichprobe bedarfsorientiert erweitert werden, bis der Sachverhalt geklärt ist.
  6. Während der Vor-Ort-Prüfung SOLLTEN das IS-Revisionsteam niemals aktiv in IT-Systeme eingreifen und auch keine Handlungsanweisungen zu Änderungen am Revisionsgegenstand erteilen.
  7. Alle wesentlichen Sachverhalte und Angaben zu Quellen-, Auskunfts- und Vorlage-Ersuchen sowie durchgeführten Besprechungen SOLLTEN schriftlich festgehalten werden.
  8. In einem Abschlussgespräch SOLLTE das IS-Revisionsteam der geprüften Institution wesentliche Feststellungen kurz darstellen.
  9. Dabei SOLLTE das IS-Revisionsteam die Feststellungen nicht konkret bewerten, sondern Hinweise auf etwaige Mängel und die weitere Verfahrensweise geben.
  10. Auch dieses Abschlussgespräch SOLLTE protokolliert werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die Forderung, Audits in angemessenem Umfang auszuführen, deckt das tatsächliche Überprüfen aller im Prüfplan festgelegten Anforderungen und Themenfelder inhaltlich ab.

### → DER.4.A14 — Regelmäßige Überprüfung und Verbesserung der Notfallmaßnahmen (H) [Institutionsleitung]
  1. Alle Notfallmaßnahmen SOLLTEN regelmäßig oder bei größeren Änderungen daraufhin überprüft werden, ob sie noch eingehalten und korrekt umgesetzt werden.
  2. Es SOLLTE geprüft werden, ob sie sich noch dazu eignen, die definierten Ziele zu erreichen.
  3. Dabei SOLLTE untersucht werden, ob technische Maßnahmen korrekt implementiert und konfiguriert wurden und ob organisatorische Maßnahmen effektiv und effizient umgesetzt sind.
  4. Bei Abweichungen SOLLTEN die Ursachen für die Mängel ermittelt und Verbesserungsmaßnahmen veranlasst werden.
  5. Diese Ergebnisübersicht SOLLTE von der Institutionsleitung freigegeben werden.
  6. Es SOLLTE zudem ein Prozess etabliert werden, der steuert und überwacht, ob und wie die Verbesserungsmaßnahmen umgesetzt werden.
  7. Verzögerungen SOLLTEN frühzeitig an die Institutionsleitung gemeldet werden.
  8. Es SOLLTE von der Institutionsleitung festgelegt sein, wie die Überprüfungen koordiniert werden.
  9. Die Überprüfungen SOLLTEN so geplant werden, dass kein relevanter Teil ausgelassen wird. **◀ ZITIERT**
  10. Insbesondere SOLLTEN die im Bereich der Revision, der IT, des Sicherheitsmanagements, des Informationssicherheitsmanagements und des Notfallmanagements durchgeführten Überprüfungen miteinander koordiniert werden.
  11. Dazu SOLLTE geregelt werden, welche Maßnahmen wann und von wem überprüft werden.
- **Satz 9** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 9) Die G++-Maßnahme fordert die Definition und Ausführung eines angemessenen Prüfungsumfangs, was die lückenlose Einbindung aller relevanten Bereiche bei der Überprüfungsplanung abdeckt.

### → IND.1.A12 — Etablieren eines Schwachstellen-Managements (S)
  1. Für den sicheren Betrieb einer OT-Umgebung SOLLTE die Institution ein Schwachstellen-Management etablieren.
  2. Das Schwachstellen-Management SOLLTE Lücken in Software, Komponenten, Protokollen und Außenschnittstellen der Umgebung identifizieren.
  3. Außerdem SOLLTEN sich daraus erforderliche Handlungen ableiten, bewerten und umsetzen lassen.
  4. Grundlage dafür SOLLTEN Schwachstellenmeldungen von herstellenden Unternehmen oder öffentlich verfügbare CERT-Meldungen sein.
  5. Ergänzend hierzu SOLLTEN organisatorische und technische Audits zur Schwachstellenanalyse durchgeführt werden. **◀ ZITIERT**
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) Die Maßnahme fordert die Ausführung von Audits in angemessenem Umfang, was laut Erläuterung ausdrücklich sowohl den organisatorischen als auch den technischen Geltungsbereich umfasst.

### → NET.2.1.A14 — Regelmäßige Audits der WLAN-Komponenten (S)
  1. Bei allen Komponenten der WLAN-Infrastruktur SOLLTE regelmäßig überprüft werden, ob alle festgelegten Sicherheitsmaßnahmen umgesetzt sind. **◀ ZITIERT**
  2. Außerdem SOLLTE überprüft werden ob alle Komponenten korrekt konfiguriert sind.
  3. Öffentlich aufgestellte Access Points SOLLTEN regelmäßig stichprobenartig daraufhin geprüft werden, ob es gewaltsame Öffnungs- oder Manipulationsversuche gab.
  4. Die Auditergebnisse SOLLTEN nachvollziehbar dokumentiert und mit dem Soll-Zustand abgeglichen werden.
  5. Abweichungen SOLLTEN untersucht werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) PERF.3.1.4 fordert die Durchführung von Audits in angemessenem Umfang, was die regelmäßige Überprüfung der Umsetzung von Sicherheitsmaßnahmen auf den relevanten Infrastrukturkomponenten als allgemeinere Fassung abdeckt.

### → NET.3.1.A23 — Revision und Penetrationstests (S)
  1. Router und Switches SOLLTEN regelmäßig auf bekannte Sicherheitsprobleme hin überprüft werden.
  2. Auch SOLLTEN regelmäßig Revisionen durchgeführt werden. **◀ ZITIERT**
  3. Dabei SOLLTE unter anderem geprüft werden, ob der Ist-Zustand der festgelegten sicheren Grundkonfiguration entspricht.
  4. Die Ergebnisse SOLLTEN nachvollziehbar dokumentiert und mit dem Soll-Zustand abgeglichen werden.
  5. Abweichungen SOLLTE nachgegangen werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die Durchführung von Audits in angemessenem Umfang deckt die regelmäßige Durchführung von Revisionen inhaltlich ab.

### → SYS.1.5.A19 — Regelmäßige Audits der Virtualisierungsinfrastruktur (S)
  1. Es SOLLTE regelmäßig auditiert werden, ob der Ist-Zustand der virtuellen Infrastruktur dem in der Planung festgelegten Zustand entspricht. **◀ ZITIERT**
  2. Auch SOLLTE regelmäßig auditiert werden, ob die Konfiguration der virtuellen Komponenten die vorgegebene Standardkonfiguration einhält.
  3. Die Auditergebnisse SOLLTEN nachvollziehbar dokumentiert werden.
  4. Abweichungen SOLLTEN behoben werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme fordert die Durchführung von Audits in angemessenem Umfang und deckt damit als allgemeinere Formulierung die regelmäßige Prüfung des Ist-Zustands von Infrastrukturen gegen Planungszustände ab.

### → SYS.1.8.A18 — Sicherheitsaudits und Berichtswesen bei Speichersystemen (S)
  1. Alle eingesetzten Speichersysteme SOLLTEN regelmäßig auditiert werden. **◀ ZITIERT**
  2. Dafür SOLLTE ein entsprechender Prozess eingerichtet werden.
  3. Es SOLLTE geregelt werden, welche Sicherheitsreports mit welchen Inhalten regelmäßig zu erstellen sind.
  4. Zudem SOLLTE auch geregelt werden, wie mit Abweichungen von Vorgaben umgegangen wird und wie oft und in welcher Tiefe Audits durchgeführt werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) PERF.3.1.4 verlangt die Durchführung von Audits in angemessenem Umfang (inklusive des technischen Geltungsbereichs wie IT-Systeme) und deckt damit die regelmäßige Auditierung der Speichersysteme auf allgemeiner Ebene ab.

### → DER.3.1.A17 — Durchführung der Vor-Ort-Prüfung (S) [Auditteam]
  1. Zu Beginn der Vor-Ort-Prüfung SOLLTE das Auditteam ein Eröffnungsgespräch mit der betreffenden Institution führen.
  2. Danach SOLLTEN alle im Prüfplan festgelegten Anforderungen mit den vorgesehenen Prüfmethoden kontrolliert werden. **◀ ZITIERT**
  3. Weicht eine ausgewählte Stichprobe vom dokumentierten Status ab, SOLLTE die Stichprobe bedarfsorientiert erweitert werden, bis der Sachverhalt geklärt ist.
  4. Nach der Prüfung SOLLTE das Auditteam ein Abschlussgespräch führen.
  5. Darin SOLLTE es kurz die Ergebnisse ohne Bewertung sowie die weitere Vorgehensweise darstellen.
  6. Das Gespräch SOLLTE protokolliert werden.
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die Maßnahme PERF.3.1.4 verlangt die Durchführung von Audits in angemessenem Umfang unter Einsatz der definierten Prüfmethoden und deckt damit die tatsächliche Kontrolle der im Prüfplan festgelegten Anforderungen ab.

### → DER.3.1.A2 — Vorbereitung eines Audits oder einer Revision (B)
  1. Vor einem Audit oder einer Revision MUSS die Institution den Prüfgegenstand und die Prüfungsziele festlegen. **◀ ZITIERT**
  2. Das betroffene Personal MUSS unterrichtet werden.
  3. Abhängig vom Untersuchungsgegenstand MUSS die Personalvertretung über das geplante Audit oder die geplante Revision informiert werden.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) PERF.3.1.4 adressiert die Festlegung des Auditumfangs (organisatorischer und technischer Prüfgegenstand) vor Beginn des Audits inhaltlich passend zur Forderung des Satzes.

### → DER.3.1.A4 — Durchführung einer Revision (B)
  1. Bei einer Revision MUSS das Revisionsteam prüfen, ob die Anforderungen vollständig, korrekt, angemessen und aktuell umgesetzt sind. **◀ ZITIERT**
  2. Die Institution MUSS festgestellte Abweichungen so schnell wie möglich korrigieren.
  3. Die jeweiligen Revisionen MÜSSEN mit einer Änderungsverfolgung dokumentiert werden.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme fordert die Durchführung von Audits in angemessenem Umfang, was die inhaltliche Prüfung der Umsetzung von Anforderungen durch das Audit- bzw. Revisionsteam abdeckt.

### → DER.3.2.A7 — Durchführung einer IS-Revision (B) [IS-Revisionsteam]
  1. Im Rahmen einer IS-Revision MÜSSEN eine Dokumenten- und eine Vor-Ort-Prüfung durch das IS-Revisionsteam durchgeführt werden. **◀ ZITIERT**
  2. Sämtliche Ergebnisse dieser beiden Prüfungen MÜSSEN dokumentiert und in einem IS-Revisionsbericht zusammengefasst werden.
  3. Bevor erstmalig eine IS-Querschnittsrevision durchgeführt wird, MUSS als IS-Revisionsverfahren eine IS-Kurzrevision ausgewählt werden.
  4. Die IS-Kurzrevision MUSS mit positivem Votum abgeschlossen werden, bevor eine IS-Querschnittsrevision durchgeführt wird.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme fordert die Durchführung von Audits in angemessenem Umfang, was laut Erläuterung ausdrücklich Prüfmethoden wie die Dokumentensichtung und Prüfungen vor Ort/Standorten umfasst.


## PERF.4.1 — Eignungsprüfung  [4 Paare]

**Statement (normativ):** Monitoring-Evaluation MUSS Ergebnisse der Überprüfungen der Eignung, Angemessenheit und Wirksamkeit des ISMS der Institution {{ insert: param, perf.4.1-prm1 }} sowie anlassbezogen in einem Managementbericht dokumentieren.
**Klasse:** BSI-Methodik-Grundschutz-plus-plus | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Damit die Institutionsleitung fundierte Entscheidungen zur Steuerung des Informationssicherheitsprozesses treffen kann, ist ein prägnanter Managementbericht erforderlich. Darin werden die wesentlichen Eckpunkte zum Stand der Informationssicherheit übersichtlich aufbereitet. Der Bericht SOLL: kurz, klar und verständlich sein, relevante Informationen bzw. Entwicklungen enthalten, nicht überfrachtet sein d.h. den Fokus auf das Wesentliche legen. So kann die Leitung gezielt Maßnahmen priorisieren und Ressourcen effektiv einsetzen. Es muss unter anderem deutlich werden, ob der beabsichtigte Sicherheitszweck wirksam erfüllt wird.

### → ISMS.1.A12 — Management-Berichte zur Informationssicherheit (S) [Institutionsleitung]
  1. Die Institutionsleitung SOLLTE sich regelmäßig über den Stand der Informationssicherheit informieren, insbesondere über die aktuelle Gefährdungslage sowie die Wirksamkeit und Effizienz des Sicherheitsprozesses.
  2. Dazu SOLLTEN Management-Berichte geschrieben werden, welche die wesentlichen relevanten Informationen über den Sicherheitsprozess enthalten, insbesondere über Probleme, Erfolge und Verbesserungsmöglichkeiten. **◀ ZITIERT**
  3. Die Management-Berichte SOLLTEN klar priorisierte Maßnahmenvorschläge enthalten.
  4. Die Maßnahmenvorschläge SOLLTEN mit realistischen Abschätzungen zum erwarteten Umsetzungsaufwand versehen sein.
  5. Die Management-Berichte SOLLTEN revisionssicher archiviert werden.
  6. Die Management-Entscheidungen über erforderliche Aktionen, den Umgang mit Restrisiken und mit Veränderungen von sicherheitsrelevanten Prozessen SOLLTEN dokumentiert sein.
  7. Die Management-Entscheidungen SOLLTEN revisionssicher archiviert werden.
- **Satz 2** | Relation GS++→ED23: `equivalent-to` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) Satz 2 fordert die Erstellung von Management-Berichten mit den wesentlichen relevanten Informationen über den Sicherheitsprozess, was der geforderten Dokumentation der Eignungs- und Wirksamkeitsprüfung in einem Managementbericht entspricht.

### → ISMS.1.A2 — Festlegung der Sicherheitsziele und -strategie (B) [Institutionsleitung]
  1. Die Institutionsleitung MUSS den Sicherheitsprozess initiieren und etablieren.
  2. Dafür MUSS die Institutionsleitung angemessene Sicherheitsziele sowie eine Strategie für Informationssicherheit festlegen und dokumentieren.
  3. Es MÜSSEN konzeptionelle Vorgaben erarbeitet und organisatorische Rahmenbedingungen geschaffen werden, um den ordnungsgemäßen und sicheren Umgang mit Informationen innerhalb aller Geschäftsprozesse des Unternehmens oder Fachaufgaben der Behörde zu ermöglichen.
  4. Die Institutionsleitung MUSS die Sicherheitsstrategie und die Sicherheitsziele tragen und verantworten.
  5. Die Institutionsleitung MUSS die Sicherheitsziele und die Sicherheitsstrategie regelmäßig dahingehend überprüfen, ob sie noch aktuell und angemessen sind und wirksam umgesetzt werden können. **◀ ZITIERT**
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) PERF.4.1 fordert die regelmäßige Dokumentation der Überprüfungsergebnisse zur Eignung, Angemessenheit und Wirksamkeit des ISMS für das Management und deckt damit die geforderte regelmäßige Überprüfung inhaltlich ab.

### → ISMS.1.A6 — Aufbau einer geeigneten Organisationsstruktur für Informationssicherheit (B) [Institutionsleitung]
  1. Eine geeignete übergreifende Organisationsstruktur für Informationssicherheit MUSS vorhanden sein.
  2. Dafür MÜSSEN Rollen definiert sein, die konkrete Aufgaben übernehmen, um die Sicherheitsziele zu erreichen.
  3. Außerdem MÜSSEN qualifizierte Personen benannt werden, denen ausreichend Ressourcen zur Verfügung stehen, um diese Rollen zu übernehmen.
  4. Die Aufgaben, Rollen, Verantwortungen und Kompetenzen im Sicherheitsmanagement MÜSSEN nachvollziehbar definiert und zugewiesen sein.
  5. Für alle wichtigen Funktionen der Organisation für Informationssicherheit MUSS es wirksame Vertretungsregelungen geben.
  6. Kommunikationswege MÜSSEN geplant, beschrieben, eingerichtet und bekannt gemacht werden.
  7. Es MUSS für alle Aufgaben und Rollen festgelegt sein, wer wen informiert und wer bei welchen Aktionen in welchem Umfang informiert werden muss.
  8. Es MUSS regelmäßig geprüft werden, ob die Organisationsstruktur für Informationssicherheit noch angemessen ist oder ob sie an neue Rahmenbedingungen angepasst werden muss. **◀ ZITIERT**
- **Satz 8** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 8) Die regelmäßige Überprüfung der Eignung und Angemessenheit des ISMS im Rahmen der Managementbewertung umfasst als allgemeinere Anforderung auch die regelmäßige Prüfung und Anpassung der zugehörigen Sicherheitsorganisationsstruktur.

### → ISMS.1.A11 — Aufrechterhaltung der Informationssicherheit (S)
  1. Der Sicherheitsprozess, die Sicherheitskonzepte, die Leitlinie zur Informationssicherheit und die Organisationsstruktur für Informationssicherheit SOLLTEN regelmäßig auf Wirksamkeit und Angemessenheit überprüft und aktualisiert werden.
  2. Dazu SOLLTEN regelmäßig Vollständigkeits- bzw. Aktualisierungsprüfungen des Sicherheitskonzeptes durchgeführt werden.
  3. Ebenso SOLLTEN regelmäßig Sicherheitsrevisionen durchgeführt werden.
  4. Dazu SOLLTE geregelt sein, welche Bereiche und Sicherheitsmaßnahmen wann und von wem zu überprüfen sind.
  5. Überprüfungen des Sicherheitsniveaus SOLLTEN regelmäßig (mindestens jährlich) sowie anlassbezogen durchgeführt werden.
  6. Die Prüfungen SOLLTEN von qualifizierten und unabhängigen Personen durchgeführt werden.
  7. Die Ergebnisse der Überprüfungen SOLLTEN nachvollziehbar dokumentiert sein. **◀ ZITIERT**
  8. Darauf aufbauend SOLLTEN Mängel beseitigt und Korrekturmaßnahmen ergriffen werden.
- **Satz 7** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 7) Die Maßnahme PERF.4.1 fordert explizit die Dokumentation der Überprüfungsergebnisse bezüglich Eignung, Angemessenheit und Wirksamkeit des ISMS in einem Managementbericht.


## PERF.4.1.7 — Status des Realisierungsplans  [1 Paare]

**Statement (normativ):** Monitoring-Evaluation SOLLTE die erfolgreiche Umsetzung von Maßnahmen und des damit verringerten Risikos (Status des Umsetzungsplans) als Ergebnis der Überprüfung in einem Managementbericht dokumentieren.
**Klasse:** BSI-Methodik-Grundschutz-plus-plus | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Die Überprüfung von Umsetzungsdefiziten und Risiken ist im ISMS ein zentraler Bestandteil des Monitorings und der Evaluierung. Monitoring sorgt für die kontinuierliche Beobachtung des Fortschritts bei Maßnahmenumsetzung, während die Evaluierung die Wirksamkeit dieser Maßnahmen bewertet und bei Bedarf Anpassungen empfiehlt. So wird sichergestellt, dass Risiken nachhaltig reduziert und Sicherheitsziele erreicht werden. D. h. der Status des Realisierungsplans muss fortlaufend überprüft werden. Die Ergebnisse dieser Überprüfungen basieren auf den vorab erstellten Auditberichten sowie der geforderten Eignungsprüfung.

### → DER.3.1.A5 — Integration in den Informationssicherheitsprozess (S)
  1. Die Institution SOLLTE eine Richtlinie zur internen ISMS-Auditierung vorgeben.
  2. Außerdem sollte sie eine Richtlinie zur Lenkung von Korrekturmaßnahmen erstellen.
  3. Die Richtlinien SOLLTEN vorgeben, dass regelmäßige Audits und Revisionen ein Teil des Sicherheitsprozesses sind und durch diesen initiiert werden.
  4. Der oder die ISB SOLLTE sicherstellen, dass die Ergebnisse der Audits und Revisionen in das ISMS zurückfließen und dieses verbessern.
  5. Der oder die ISB SOLLTE die durchgeführten Audits und Revisionen und deren Ergebnisse in den regelmäßigen Bericht an die Institutionsleitung aufnehmen.
  6. Auch SOLLTE dort festgehalten werden, welche Mängel beseitigt wurden und wie die Qualität verbessert wurde. **◀ ZITIERT**
- **Satz 6** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 6) Satz 6 fordert, im Bericht an die Leitung festzuhalten, welche Mängel beseitigt wurden, was sich direkt mit der Dokumentation der erfolgreichen Maßnahmenumsetzung im Managementbericht nach PERF.4.1.7 überschneidet.


## PERF.3.2.1 — Einheitliches Bewertungsschema  [1 Paare]

**Statement (normativ):** Monitoring-Evaluation SOLLTE für Feststellungen in Audits ein einheitliches Bewertungsschema festlegen.
**Klasse:** BSI-Methodik-Grundschutz-plus-plus | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Das Bewertungsschema soll die einheitliche Bewertung, die Wirksamkeit der Auditprozesse und die Vergleichbarkeit von Auditergebnissen sicherstellen.

### → DER.3.1.A6 — Definition der Prüfungsgrundlage und eines einheitlichen Bewertungsschemas (S)
  1. Die Institution SOLLTE eine einheitliche Prüfungsgrundlage für Audits festlegen.
  2. Für die Bewertung der Umsetzung von Anforderungen SOLLTE ein einheitliches Bewertungsschema festgelegt und dokumentiert werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) Die G++-Maßnahme fordert explizit die Festlegung eines einheitlichen Bewertungsschemas für Feststellungen in Audits und deckt damit die Forderung des Satzes inhaltlich ab.


## PERF.4.1.9 — Maßnahmenvorschläge  [3 Paare]

**Statement (normativ):** Monitoring-Evaluation MUSS priorisierte Maßnahmenvorschläge mit realistischen Abschätzungen zum erwarteten Umsetzungsaufwand als Ergebnis der Überprüfung in einem Managementbericht dokumentieren.
**Klasse:** BSI-Methodik-Grundschutz-plus-plus | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Maßnahmenvorschläge müssen daraufhin überprüft werden, ob sie wirksam zur Risikoreduktion beitragen und mit vertretbarem Aufwand umsetzbar sind. Dabei sind Nutzen, Kosten, technischer und organisatorischer Aufwand realistisch abzuschätzen und in Relation zueinander zu bewerten, um fundierte Entscheidungen zur Umsetzung und Priorisierung treffen zu können. Die Ergebnisse dieser Überprüfungen basieren auf den vorab erstellten Auditberichten sowie der geforderten Eignungsprüfung.

### → ISMS.1.A12 — Management-Berichte zur Informationssicherheit (S) [Institutionsleitung]
  1. Die Institutionsleitung SOLLTE sich regelmäßig über den Stand der Informationssicherheit informieren, insbesondere über die aktuelle Gefährdungslage sowie die Wirksamkeit und Effizienz des Sicherheitsprozesses.
  2. Dazu SOLLTEN Management-Berichte geschrieben werden, welche die wesentlichen relevanten Informationen über den Sicherheitsprozess enthalten, insbesondere über Probleme, Erfolge und Verbesserungsmöglichkeiten.
  3. Die Management-Berichte SOLLTEN klar priorisierte Maßnahmenvorschläge enthalten. **◀ ZITIERT**
  4. Die Maßnahmenvorschläge SOLLTEN mit realistischen Abschätzungen zum erwarteten Umsetzungsaufwand versehen sein. **◀ ZITIERT**
  5. Die Management-Berichte SOLLTEN revisionssicher archiviert werden.
  6. Die Management-Entscheidungen über erforderliche Aktionen, den Umgang mit Restrisiken und mit Veränderungen von sicherheitsrelevanten Prozessen SOLLTEN dokumentiert sein.
  7. Die Management-Entscheidungen SOLLTEN revisionssicher archiviert werden.
- **Satz 3** | Relation GS++→ED23: `equal-to` | Fundrichtung: beide
  Begründung: (Teilanforderung 3) Die G++-Maßnahme PERF.4.1.9 fordert ausdrücklich, priorisierte Maßnahmenvorschläge in einem Managementbericht zu dokumentieren.
- **Satz 4** | Relation GS++→ED23: `equal-to` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die G++-Maßnahme PERF.4.1.9 fordert explizit, Maßnahmenvorschläge mit realistischen Abschätzungen zum erwarteten Umsetzungsaufwand im Managementbericht zu dokumentieren.

### → ISMS.1.A15 — Wirtschaftlicher Einsatz von Ressourcen für Informationssicherheit (S)
  1. Die Sicherheitsstrategie SOLLTE wirtschaftliche Aspekte berücksichtigen.
  2. Werden Sicherheitsmaßnahmen festgelegt, SOLLTEN die dafür erforderlichen Ressourcen beziffert werden. **◀ ZITIERT**
  3. Die für Informationssicherheit eingeplanten Ressourcen SOLLTEN termingerecht bereitgestellt werden.
  4. Bei Arbeitsspitzen oder besonderen Aufgaben SOLLTEN zusätzliche interne Mitarbeitenden eingesetzt oder externe Expertise hinzugezogen werden.
- **Satz 2** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die Maßnahme PERF.4.1.9 verlangt bei Maßnahmenvorschlägen eine realistische Abschätzung des erwarteten Umsetzungsaufwands (Kosten und Ressourcen), was die Bezifferung der erforderlichen Ressourcen inhaltlich abdeckt.

