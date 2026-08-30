# Review-Dossier Praktik REA

Praktik REA: 21 Controls mit Mapping, 121 Paare gesamt. Gesampelt: 5 Controls (max/min/median Paarzahl + 2 zufällig).

## REA.2.1 — Triage und Erstreaktion  [6 Paare]

**Statement (normativ):** Sicherheitsvorfallsbehandlung SOLLTE Meldungen einer Priorität zuweisen.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Triage ist ein strukturiertes Vorgehen zur Priorisierung und Ersteinschätzung von Sicherheitsvorfällen, mit dem Ziel, rasch und effizient auf Bedrohungen zu reagieren, Ressourcen gezielt einzusetzen und weitere Schäden zu minimieren. Dabei wird festgestellt, welche Vorfälle sofortige Aufmerksamkeit benötigen, welche weiter analysiert oder beobachtet werden oder irrelevante Fehlalarme sind. Kritische Vorfälle können z.B. ein Virenfund auf einem Server, Ransomwarevorfälle oder Spionage durch professionelle Täter sein. Die Umsetzung kann auch automatisiert durch EDR/SOAR geschehen. Eine Erstreaktion ist eine schnelle Handlung, die dazu dient, weitere Schäden wie eine Ausbreitung von Angriffen oder Störungen in Geschäftsprozessen zu vermeiden. Sie kann z.B. in der Abschaltung betroffener Systeme, der Deaktivierung eines Zugangskonto, der Information Nutzender über eine Störung oder der Aktivierung eines Ausweichrechenzentrums bestehen.

### → OPS.1.2.2.A8 — Protokollierung der Archivzugriffe (B) [IT-Betrieb]
  1. Alle Zugriffe auf elektronische Archive MÜSSEN protokolliert werden.
  2. Dafür SOLLTEN Datum, Uhrzeit, Benutzender, Client und die ausgeführten Aktionen sowie Fehlermeldungen aufgezeichnet werden.
  3. Im Archivierungskonzept SOLLTE festgelegt werden, wie lange die Protokolldaten aufbewahrt werden.
  4. Die Protokolldaten der Archivzugriffe SOLLTEN regelmäßig ausgewertet werden.
  5. Dabei SOLLTEN die institutionsinternen Vorgaben beachtet werden.
  6. Auch SOLLTE definiert sein, welche Ereignisse welchen Mitarbeitenden angezeigt werden, wie z. B. Systemfehler, Timeouts oder wenn Datensätze kopiert werden.
  7. Kritische Ereignisse SOLLTEN sofort nach der Erkennung geprüft und, falls nötig, weiter eskaliert werden. **◀ ZITIERT**
- **Satz 7** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 7) Die Triage und Priorisierung von Meldungen nach REA.2.1 umfasst die sofortige Ersteinschätzung und Prüfung kritischer Ereignisse nach deren Erkennung.

### → IND.1.A10 — Monitoring, Protokollierung und Detektion (S) [OT-Betrieb (Operational Technology, OT)]
  1. Betriebs- und sicherheitsrelevante Ereignisse SOLLTEN zeitnah identifiziert werden.
  2. Hierzu SOLLTE ein geeignetes Log- und Event-Management entwickelt und umgesetzt werden.
  3. Das Log- und Event-Management SOLLTE angemessene Maßnahmen umfassen, um sicherheitsrelevante Ereignisse zu erkennen und zu erheben.
  4. Es SOLLTE zudem einen Reaktionsplan (Security Incident Response) enthalten.
  5. Der Reaktionsplan SOLLTE Verfahren zur Behandlung von Sicherheitsvorfällen festlegen.
  6. Darin abgedeckt sein SOLLTEN die Klassifizierung von Ereignissen, Meldewege und Festlegung der einzubeziehenden Organisationseinheiten, Reaktionspläne zur Schadensbegrenzung, Analyse und Wiederherstellung von Systemen und Diensten sowie die Dokumentation und Nachbereitung von Vorfällen. **◀ ZITIERT**
- **Satz 6** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 6) REA.2.1 deckt mit der Priorisierung und Triage von Meldungen die in Satz 6 geforderte Klassifizierung von Ereignissen im Rahmen der Vorfallsbehandlung ab.

### → DER.1.A15 — Zentrale Detektion und Echtzeitüberprüfung von Ereignismeldungen (H)
  1. Zentrale Komponenten SOLLTEN eingesetzt werden, um sicherheitsrelevante Ereignisse zu erkennen und auszuwerten.
  2. Zentrale, automatisierte Analysen mit Softwaremitteln SOLLTEN eingesetzt werden.
  3. Mit diesen zentralen, automatisierten Analysen mit Softwaremitteln SOLLTEN alle in der Systemumgebung anfallenden Ereignisse aufgezeichnet und in Bezug zueinander gesetzt werden.
  4. Die sicherheitsrelevanten Vorgänge SOLLTEN sichtbar gemacht werden.
  5. Alle eingelieferten Daten SOLLTEN lückenlos in der Protokollverwaltung einsehbar und auswertbar sein.
  6. Die Daten SOLLTEN möglichst permanent ausgewertet werden.
  7. Werden definierte Schwellwerte überschritten, SOLLTE automatisch alarmiert werden.
  8. Das Personal SOLLTE sicherstellen, dass bei einem Alarm unverzüglich eine qualifizierte und dem Bedarf entsprechende Reaktion eingeleitet wird. **◀ ZITIERT**
  9. In diesem Zusammenhang SOLLTEN auch die betroffenen Mitarbeitenden sofort informiert werden.
  10. Die Systemverantwortlichen SOLLTEN regelmäßig die Analyseparameter auditieren und anpassen, falls dies erforderlich ist.
  11. Zusätzlich SOLLTEN bereits überprüfte Daten regelmäßig hinsichtlich sicherheitsrelevanter Ereignisse automatisch untersucht werden.
- **Satz 8** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 8) REA.2.1 fordert die Triage und Erstreaktion auf Meldungen, womit die unverzuegliche und bedarfsgerechte Reaktion auf Alarme inhaltlich abgedeckt wird.

### → DER.2.1.A10 — Eindämmen der Auswirkung von Sicherheitsvorfällen (S) [Notfallbeauftragte, IT-Betrieb]
  1. Parallel zur Ursachenanalyse eines Sicherheitsvorfalls SOLLTE entschieden werden, ob es wichtiger ist, den entstandenen Schaden einzudämmen oder den Vorfall aufzuklären. **◀ ZITIERT**
  2. Um die Auswirkung eines Sicherheitsvorfalls abschätzen zu können, SOLLTEN ausreichend Informationen vorliegen.
  3. Für ausgewählte Sicherheitsvorfallszenarien SOLLTEN bereits im Vorfeld Worst-Case-Betrachtungen durchgeführt werden.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 1) Satz 1 fordert eine prioritäre Richtungsentscheidung zwischen schneller Schadenseindämmung (Erstreaktion) und Aufklärung, was eine wesentliche Triage- und Priorisierungsentscheidung im Sinne von REA.2.1 darstellt.

### → DER.2.1.A11 — Einstufung von Sicherheitsvorfällen (S) [IT-Betrieb]
  1. Ein einheitliches Verfahren SOLLTE festgelegt werden, um Sicherheitsvorfälle und Störungen einzustufen. **◀ ZITIERT**
  2. Das Einstufungsverfahren für Sicherheitsvorfälle SOLLTE zwischen Sicherheitsmanagement und der Störungs- und Fehlerbehebung (Incident Management) abgestimmt sein.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) Die Zuweisung von Prioritäten im Rahmen der Triage gemäß REA.2.1 deckt die geforderte Einstufung von Sicherheitsvorfällen inhaltlich ab.

### → DER.2.1.A19 — Festlegung von Prioritäten für die Behandlung von Sicherheitsvorfällen (H) [Institutionsleitung]
  1. Es SOLLTEN Prioritäten für die Behandlung von Sicherheitsvorfällen vorab festgelegt und regelmäßig aktualisiert werden. **◀ ZITIERT**
  2. Dabei SOLLTE auch die vorgenommene Einstufung von Sicherheitsvorfällen berücksichtigt werden.
  3. Die Prioritäten SOLLTEN von der Institutionsleitung genehmigt und in Kraft gesetzt werden.
  4. Sie SOLLTEN allen Verantwortlichen bekannt sein, die mit der Behandlung von Sicherheitsvorfällen zu tun haben.
  5. Die festgelegten Prioritätsklassen SOLLTEN außerdem im Incident Management hinterlegt sein.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 1) Satz 1 fordert die Festlegung von Prioritäten für die Vorfallsbehandlung, was die organisatorische Grundlage für die in REA.2.1 geforderte Priorisierung und Triage von Vorfällen bildet.


## REA.2.6 — Ursachenanalyse und Behandlung  [15 Paare]

**Statement (normativ):** Sicherheitsvorfallsbehandlung SOLLTE eine Vorgehensweise zur Ursachenanalyse und Behandlung verankern.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Um einen Vorfall vollständig beheben zu können, ist es zweckmäßig, zunächst zu analysieren, wie der Vorfall zustande kam (Root Cause Analysis): Welche Personen und Systeme sind betroffen? Welche systematischen Schwachstellen haben zu dem Vorfall geführt? Die Behebung des Vorfalls orientiert sich dann an diesen Erkenntnissen, z.B. durch Schließen der Sicherheitslücken und Wiederherstellung von Daten und Anwendungen. Je nach Vorfall kann die Behandlung durch das Schließen ausgenutzter Sicherheitslücken, einem Test anderer IT-Systeme auf vergleichbare Schwachstellen oder dem Austausch betroffener IT-Systeme, Anwendungen oder Datenbestände umgesetzt werden. Sind die Originaldaten oder -Systeme nicht mehr zu retten, so kann die Neuinstallation betroffener Systeme und die Wiederherstellung von Daten aus Backups eine Möglichkeit der Behandlung sein.

### → CON.7.A6 — Zeitnahe Verlustmeldung (B) [Benutzende]
  1. Mitarbeitende MÜSSEN ihrer Institution umgehend melden, wenn Informationen, IT-Systeme oder Datenträger verloren gegangen sind oder gestohlen wurden.
  2. Hierfür MUSS es klare Meldewege und Kontaktpersonen innerhalb der Institution geben.
  3. Die Institution MUSS die möglichen Auswirkungen des Verlustes bewerten und geeignete Gegenmaßnahmen ergreifen. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme REA.2.6 deckt die Analyse der Betroffenheit sowie die Ergreifung von Behandlungs- und Gegenmaßnahmen bei Vorfällen wie Verlusten vollumfänglich ab.

### → DER.1.A5 — Einsatz von mitgelieferten Systemfunktionen zur Detektion (B) [Fachverantwortliche]
  1. Falls eingesetzte IT-Systeme oder Anwendungen über Funktionen verfügen, mit denen sich sicherheitsrelevante Ereignisse detektieren lassen, dann MÜSSEN diese aktiviert und benutzt werden.
  2. Falls ein sicherheitsrelevanter Vorfall vorliegt, dann MÜSSEN die Meldungen der betroffenen IT-Systeme ausgewertet werden. **◀ ZITIERT**
  3. Zusätzlich MÜSSEN die protokollierten Ereignisse anderer IT-Systeme überprüft werden.
  4. Auch SOLLTEN die gesammelten Meldungen in verbindlich festgelegten Zeiträumen stichpunktartig kontrolliert werden.
  5. Es MUSS geprüft werden, ob zusätzliche Schadcodescanner auf zentralen IT-Systemen installiert werden sollen.
  6. Falls zusätzliche Schadcodescanner eingesetzt werden, dann MÜSSEN diese es über einen zentralen Zugriff ermöglichen, ihre Meldungen und Protokolle auszuwerten.
  7. Es MUSS sichergestellt sein, dass die Schadcodescanner sicherheitsrelevante Ereignisse automatisch an die Zuständigen melden.
  8. Die Zuständigen MÜSSEN die Meldungen auswerten und untersuchen.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die Forderung nach Ursachenanalyse bei Vorfällen in REA.2.6 umfasst als allgemeinere Fassung die Auswertung von Meldungen der betroffenen IT-Systeme im Vorfallsfall.

### → DER.2.1.A5 — Behebung von Sicherheitsvorfällen (B) [IT-Betrieb]
  1. Damit ein Sicherheitsvorfall erfolgreich behoben werden kann, MÜSSEN die Zuständigen zunächst das Problem eingrenzen und die Ursache finden. **◀ ZITIERT**
  2. Danach MÜSSEN die erforderlichen Maßnahmen auswählt werden, um das Problem zu beheben. **◀ ZITIERT**
  3. Die Leitung des IT-Betriebs MUSS eine Freigabe erteilen, bevor die Maßnahmen umgesetzt werden.
  4. Anschließend MUSS die Ursache beseitigt und ein sicherer Zustand hergestellt werden. **◀ ZITIERT**
  5. Eine aktuelle Liste von internen und externen Sicherheitsfachleuten MUSS vorhanden sein, die bei Sicherheitsvorfällen für Fragen aus den erforderlichen Themenbereichen hinzugezogen werden können.
  6. Es MÜSSEN sichere Kommunikationsverfahren mit diesen internen und externen Stellen etabliert werden.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) Die G++-Maßnahme REA.2.6 fordert explizit eine Vorgehensweise zur Ursachenanalyse (Root Cause Analysis) und Eingrenzung betroffener Systeme, was die Forderung von Satz 1 inhaltlich abdeckt.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) REA.2.6 fordert eine Vorgehensweise zur Vorfallsbehandlung, welche die Auswahl und Bestimmung geeigneter Maßnahmen zur Problembehebung auf Basis der Ursachenanalyse inhaltlich abdeckt.
- **Satz 4** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die G++-Maßnahme REA.2.6 verlangt die Verankerung einer Vorgehensweise zur Behandlung von Vorfällen, welche laut Erläuterung die Beseitigung der Ursachen sowie die Wiederherstellung eines sicheren Betriebszustands umfasst.

### → DER.2.3.A2 — Entscheidung für eine Bereinigungsstrategie (B)
  1. Bevor ein APT-Vorfall tatsächlich bereinigt wird, MUSS das Leitungsgremium eine Bereinigungsstrategie festlegen.
  2. Dabei MUSS insbesondere entschieden werden, ob die Schadsoftware von kompromittierten IT-Systemen entfernt werden kann, ob IT-Systeme neu installiert werden müssen oder ob IT-Systeme inklusive der Hardware komplett ausgetauscht werden sollen. **◀ ZITIERT**
  3. Weiterhin MUSS festgelegt werden, welche IT-Systeme bereinigt werden. **◀ ZITIERT**
  4. Grundlage für diese Entscheidungen MÜSSEN die Ergebnisse einer zuvor durchgeführten forensischen Untersuchung sein.
  5. Es SOLLTEN alle betroffenen IT-Systeme neu installiert werden.
  6. Danach MÜSSEN die Wiederanlaufpläne der Institution benutzt werden.
  7. Bevor jedoch Backups wieder eingespielt werden, MUSS durch forensische Untersuchungen sichergestellt sein, dass dadurch keine manipulierten Daten oder Programme auf das neu installierte IT-System übertragen werden.
  8. Entscheidet sich eine Institution dagegen, alle IT-Systeme neu zu installieren, MUSS eine gezielte APT-Bereinigung umgesetzt werden. **◀ ZITIERT**
  9. Um das Risiko übersehener Hintertüren zu minimieren, MÜSSEN nach der Bereinigung die IT-Systeme gezielt daraufhin überwacht werden, ob sie noch mit den Angreifenden kommunizieren.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) Satz 2 fordert konkrete Entscheidungen zur Vorfallsbehandlung (Entfernung von Schadsoftware, Neuinstallation oder Austausch von IT-Systemen), was sich direkt mit den Behandlungsmethoden der Maßnahme REA.2.6 deckt.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die Maßnahme REA.2.6 deckt die Festlegung der zu bereinigenden IT-Systeme ab, indem sie im Rahmen der Ursachenanalyse und Behandlung die Identifikation der betroffenen Systeme und deren Behebung verlangt.
- **Satz 8** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 8) Die G++-Maßnahme REA.2.6 deckt die gezielte Vorfallsbehandlung und Bereinigung betroffener IT-Systeme als allgemeine Anforderung zur Behebung von Sicherheitsvorfällen ab.

### → DER.2.3.A5 — Schließen des initialen Einbruchswegs (B)
  1. Wurde durch eine forensische Untersuchung herausgefunden, dass die Angreifenden durch eine technische Schwachstelle in das Netz der Institution eingedrungen sind, MUSS diese Schwachstelle geschlossen werden. **◀ ZITIERT**
  2. Konnten die Angreifenden die IT-Systeme durch menschliche Fehlhandlungen kompromittieren, MÜSSEN organisatorische, personelle und technische Maßnahmen ergriffen werden, um ähnliche Vorfälle künftig zu verhindern.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) REA.2.6 fordert die Ursachenanalyse und anschließende Behandlung von Sicherheitsvorfällen, was explizit das Schließen ausgenutzter Sicherheitslücken und Schwachstellen umfasst.

### → DER.2.3.A9 — Hardwaretausch betroffener IT-Systeme (H)
  1. Es SOLLTE erwogen werden, nach einem APT-Vorfall die Hardware komplett auszutauschen. **◀ ZITIERT**
  2. Auch wenn nach einer Bereinigung bei einzelnen IT-Systemen noch verdächtiges Verhalten beobachtet wird, SOLLTEN die betroffenen IT-Systeme ausgetauscht werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) REA.2.6 verlangt die Verankerung einer Vorgehensweise zur Vorfallsbehandlung, welche als allgemeinere Fassung ausdrücklich auch den Austausch betroffener Systeme zur Bereinigung umfasst.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) REA.2.6 fordert die Etablierung von Behandlungsmaßnahmen bei Sicherheitsvorfällen, was den Austausch betroffener IT-Systeme als Abhilfemaßnahme im Rahmen der Vorfallbehandlung allgemein umfasst.

### → OPS.1.1.4.A9 — Meldung von Infektionen mit Schadprogrammen (S) [Benutzende]
  1. Das eingesetzte Virenschutzprogramm SOLLTE eine Infektion mit einem Schadprogramm automatisch blockieren und melden.
  2. Die automatische Meldung SOLLTE an einer zentralen Stelle angenommen werden.
  3. Dabei SOLLTEN die zuständigen Mitarbeitenden je nach Sachlage über das weitere Vorgehen entscheiden.
  4. Das Vorgehen bei Meldungen und Alarmen der Virenschutzprogramme SOLLTE geplant, dokumentiert und getestet werden.
  5. Es SOLLTE insbesondere geregelt sein, was im Falle einer bestätigten Infektion geschehen soll. **◀ ZITIERT**
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) Die Forderung nach einer verankerten Vorgehensweise zur Behandlung von Sicherheitsvorfällen deckt die Regelung der Maßnahmen im Falle einer bestätigten Schadprogramminfektion als allgemeinerer Fall inhaltlich ab.

### → SYS.4.4.A16 — Beseitigung von Schadprogrammen auf IoT-Geräten (S)
  1. Der IT-Betrieb SOLLTE sich regelmäßig informieren, ob sich die eingesetzten IoT-Geräte mit Schadprogrammen infizieren könnten und wie Infektionen beseitigt werden können.
  2. Schadprogramme SOLLTEN unverzüglich beseitigt werden. **◀ ZITIERT**
  3. Kann die Ursache für die Infektion nicht behoben bzw. eine Neuinfektion nicht wirksam verhindert werden, SOLLTEN die betroffenen IoT-Geräte nicht mehr verwendet werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme REA.2.6 deckt die Behebung von Sicherheitsvorfällen und damit die Beseitigung von Schadprogrammen als allgemeinen Behandlungs- und Wiederherstellungsprozess ab.

### → DER.2.1.A7 — Etablierung einer Vorgehensweise zur Behandlung von Sicherheitsvorfällen (S) [Institutionsleitung]
  1. Es SOLLTE eine geeignete Vorgehensweise zur Behandlung von Sicherheitsvorfällen definiert werden. **◀ ZITIERT**
  2. Die Abläufe, Prozesse und Vorgaben für die verschiedenen Sicherheitsvorfälle SOLLTEN dabei eindeutig geregelt und geeignet dokumentiert werden.
  3. Die Institutionsleitung SOLLTE die festgelegte Vorgehensweise in Kraft setzen und allen Beteiligten zugänglich machen.
  4. Es SOLLTE regelmäßig überprüft werden, ob die Vorgehensweise noch aktuell und wirksam ist.
  5. Bei Bedarf SOLLTE die Vorgehensweise angepasst werden.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme REA.2.6 verlangt explizit die Verankerung einer Vorgehensweise zur Ursachenanalyse und Behandlung von Sicherheitsvorfällen und deckt damit die geforderte Definition der Vorgehensweise inhaltlich ab.

### → IND.1.A10 — Monitoring, Protokollierung und Detektion (S) [OT-Betrieb (Operational Technology, OT)]
  1. Betriebs- und sicherheitsrelevante Ereignisse SOLLTEN zeitnah identifiziert werden.
  2. Hierzu SOLLTE ein geeignetes Log- und Event-Management entwickelt und umgesetzt werden.
  3. Das Log- und Event-Management SOLLTE angemessene Maßnahmen umfassen, um sicherheitsrelevante Ereignisse zu erkennen und zu erheben.
  4. Es SOLLTE zudem einen Reaktionsplan (Security Incident Response) enthalten.
  5. Der Reaktionsplan SOLLTE Verfahren zur Behandlung von Sicherheitsvorfällen festlegen. **◀ ZITIERT**
  6. Darin abgedeckt sein SOLLTEN die Klassifizierung von Ereignissen, Meldewege und Festlegung der einzubeziehenden Organisationseinheiten, Reaktionspläne zur Schadensbegrenzung, Analyse und Wiederherstellung von Systemen und Diensten sowie die Dokumentation und Nachbereitung von Vorfällen.
- **Satz 5** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) Die Maßnahme REA.2.6 fordert explizit die Verankerung einer Vorgehensweise zur Behandlung von Sicherheitsvorfällen und deckt damit die Forderung nach entsprechenden Verfahren im Reaktionsplan direkt ab.


## REA.2.6.2.1 — Information zuständiger Behörden  [1 Paare]

**Statement (normativ):** Sicherheitsvorfallsbehandlung SOLLTE bei Vorfällen die zuständigen Behörden im Einklang mit den Compliance-Verpflichtungen informieren.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT

### → DER.2.1.A4 — Benachrichtigung betroffener Stellen bei Sicherheitsvorfällen (B) [Institutionsleitung, IT-Betrieb, Datenschutzbeauftragte, Notfallbeauftragte]
  1. Von einem Sicherheitsvorfall MÜSSEN alle betroffenen internen und externen Stellen zeitnah informiert werden.
  2. Dabei MUSS geprüft werden, ob der oder die Datenschutzbeauftragte, der Betriebs- und Personalrat sowie Mitarbeitende aus der Rechtsabteilung einbezogen werden müssen.
  3. Ebenso MÜSSEN die Meldepflichten für Behörden und regulierte Branchen berücksichtigt werden. **◀ ZITIERT**
  4. Außerdem MUSS gewährleistet sein, dass betroffene Stellen über die erforderlichen Maßnahmen informiert werden.
- **Satz 3** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 3) Die G++-Maßnahme fordert explizit die Information zuständiger Behörden gemäß Compliance-Verpflichtungen, was die Berücksichtigung von Meldepflichten für Behörden und regulierte Branchen inhaltlich abdeckt.


## REA.2.2 — Automatische Erstreaktion  [2 Paare]

**Statement (normativ):** Sicherheitsvorfallsbehandlung KANN eine automatische Erstreaktion aktivieren.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** erhöht
**Guidance (nicht normativ):** Die automatische Erstreaktion kann je nach Risikoprofil durch institutionseigene Host- oder Network Intrusion Prevention Systeme (HIPS / NIPS) oder eine vergleichbare Cloud-Lösung umgesetzt werden.

### → DER.1.A17 — Automatische Reaktion auf sicherheitsrelevante Ereignisse (H)
  1. Bei einem sicherheitsrelevanten Ereignis SOLLTEN die eingesetzten Detektionssysteme das Ereignis automatisch melden und mit geeigneten Schutzmaßnahmen reagieren. **◀ ZITIERT**
  2. Hierbei SOLLTEN Verfahren eingesetzt werden, die automatisch mögliche Angriffe, Missbrauchsversuche oder Sicherheitsverletzungen erkennen.
  3. Es SOLLTE möglich sein, automatisch in den Datenstrom einzugreifen, um einen möglichen Sicherheitsvorfall zu unterbinden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) Die G++-Maßnahme REA.2.2 fordert mit der automatischen Erstreaktion (z. B. via IPS) die Umsetzung geeigneter automatisierter Schutzmaßnahmen bei Sicherheitsereignissen.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme REA.2.2 adressiert über die automatische Erstreaktion mittels HIPS/NIPS genau die Möglichkeit, automatisch in den Datenstrom einzugreifen und Sicherheitsvorfälle zu unterbinden.


## REA.2.6.1 — Dokumentation des Vorgehens  [3 Paare]

**Statement (normativ):** Sicherheitsvorfallsbehandlung SOLLTE die zur Behandlung durchgeführten Tätigkeiten dokumentieren.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT

### → INF.11.A6 — Festlegung von Handlungsanweisungen (S) [Fachverantwortliche, Benutzende]
  1. Für alle wesentlichen Situationen, die die Informationssicherheit von Fahrzeugen betreffen, SOLLTEN Handlungsanweisungen in Form von Checklisten vorliegen.
  2. Die Handlungsanweisungen SOLLTEN dabei in die Sicherheitsrichtlinie integriert werden und in geeigneter Form als Checklisten verfügbar sein, während das Fahrzeug benutzt wird.
  3. Hierbei SOLLTE auch der Fall berücksichtigt werden, dass das Fahrzeug selbst gestohlen wird.
  4. Die Handlungsanweisungen SOLLTEN insbesondere nachfolgende Szenarien behandeln: Ausfall von IT-Komponenten der Fahrzeuge, Notfallsituationen wie Unfälle, unerlaubtes Betreten der Fahrzeuge sowie Diebstahl der Fahrzeuge oder darin abgelegter Gegenstände mit Relevanz für die Informationssicherheit.
  5. Die Zuständigkeiten für die einzelnen Aufgaben SOLLTEN in der Checkliste dokumentiert sein.
  6. Die Anweisungen SOLLTEN von den Fahrzeugbenutzenden in den entsprechenden Situationen angewendet werden.
  7. Anhand der Checkliste SOLLTE dokumentiert werden, wie sie in diesen Situationen vorgegangen sind. **◀ ZITIERT**
- **Satz 7** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 7) REA.2.6.1 deckt die Forderung nach der Dokumentation des Vorgehens bzw. der durchgeführten Tätigkeiten in Vorfall- und Ausnahmesituationen allgemeingültig ab.

### → DER.2.1.A16 — Dokumentation der Behebung von Sicherheitsvorfällen (S)
  1. Die Behebung von Sicherheitsvorfällen SOLLTE nach einem standardisierten Verfahren dokumentiert werden. **◀ ZITIERT**
  2. Es SOLLTEN alle durchgeführten Aktionen inklusive der Zeitpunkte sowie die Protokolldaten der betroffenen Komponenten dokumentiert werden. **◀ ZITIERT**
  3. Dabei SOLLTE die Vertraulichkeit bei der Dokumentation und Archivierung der Berichte gewährleistet sein.
  4. Die benötigten Informationen SOLLTEN in die jeweiligen Dokumentationssysteme eingepflegt werden, bevor die Störung als beendet und als abgeschlossen markiert wird.
  5. Im Vorfeld SOLLTEN mit dem oder der ISB die dafür erforderlichen Anforderungen an die Qualitätssicherung definiert werden.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) REA.2.6.1 deckt die Anforderung materiell ab, da sie explizit die Dokumentation der zur Vorfallsbehandlung durchgeführten Tätigkeiten verlangt.
- **Satz 2** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die Maßnahme REA.2.6.1 fordert die Dokumentation der zur Behandlung durchgeführten Tätigkeiten und deckt damit die Dokumentation der durchgeführten Aktionen aus Satz 2 inhaltlich ab.

