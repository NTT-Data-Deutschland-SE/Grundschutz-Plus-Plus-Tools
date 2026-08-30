# Review-Dossier Praktik DET

Praktik DET: 65 Controls mit Mapping, 380 Paare gesamt. Gesampelt: 5 Controls (max/min/median Paarzahl + 2 zufällig).

## DET.3.1.6 — Systemspezifische Ereignisse  [3 Paare]

**Statement (normativ):** Detektion für IT-Systeme KANN {{ insert: param, det.3.1.6-prm1 }} protokollieren.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** erhöht
**Guidance (nicht normativ):** Bestimmte systemspezifische Ereignisse meint hier, dass von der Instiution konkret festgehalten wurde, welche für das System relevanten Ereignisse im Einzelnen protokolliert werden. Beispiele sind Aktionen mit spezifisch konfigurierten privilegierten Berechtigungen, Prozessaktivitäten des Betriebssystems, wie das Starten eines Systemprozesses, Dateierzeugung oder das Laden eines Treibers, die Modifikation von Systemkonfigurationsdateien oder die Installation oder Deinstallation von Systemdiensten und Anwendungen, sowie das Herunterfahren oder Neustarten des Systems. Die Festlegung, welche dieser oder weiterer systemspezifischer Ereignisse protokolliert werden, obliegt der Institution und hängt von der jeweiligen Systemumgebung und dem Schutzbedarf ab.

### → NET.3.4.A16 — Protokollierung der Ereignisse (S)
  1. Ergänzend zu OPS.1.1.5 Protokollierung SOLLTEN Statusänderungen an NAC-Komponenten sowie alle relevanten NAC-spezifischen, gegebenenfalls sicherheitskritischen Ereignisse protokolliert werden. **◀ ZITIERT**
  2. Zusätzlich SOLLTEN alle schreibenden Konfigurationszugriffe auf die zentralen NAC-Komponenten protokolliert werden.
  3. Es SOLLTE festgelegt werden, welche Protokollierungsdaten mit welchen Details erfasst und welche Daten auf einer zentralen Protokollierungsinstanz zusammengeführt werden.
  4. Protokollierungsdaten SOLLTEN NUR über sichere Kommunikationswege übertragen werden.
  5. Sicherheitskritische Ereignisse wie RADIUS-down oder eine ungewöhnliche Anzahl von RADIUS-Anfragen SOLLTEN zu einem automatischen Alarm führen.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) DET.3.1.6 deckt die Protokollierung systemspezifischer Ereignisse und Statusänderungen auf IT-Systemen wie NAC-Komponenten als allgemeinere Anforderung ab.

### → OPS.1.1.5.A11 — Steigerung des Protokollierungsumfangs (H)
  1. Bei erhöhtem Schutzbedarf von Anwendungen oder IT-Systemen SOLLTEN grundsätzlich mehr Ereignisse protokolliert werden, sodass sicherheitsrelevante Vorfälle möglichst lückenlos nachvollziehbar sind. **◀ ZITIERT**
  2. Um die Protokollierungsdaten in Echtzeit auswerten zu können, SOLLTEN sie in verkürzten Zeitabständen von den protokollierenden IT-Systemen und Anwendungen zentral gespeichert werden.
  3. Die Protokollierung SOLLTE eine Auswertung über den gesamten Informationsverbund ermöglichen.
  4. Anwendungen und IT-Systeme, mit denen eine zentrale Protokollierung nicht möglich ist, SOLLTEN bei einem erhöhten Schutzbedarf NICHT eingesetzt werden.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) DET.3.1.6 deckt die Forderung nach einer Steigerung des Protokollierungsumfangs für IT-Systeme ab, indem abhängig vom Schutzbedarf die Protokollierung zusätzlicher systemspezifischer Ereignisse ermöglicht wird.

### → NET.3.1.A7 — Protokollierung bei Routern und Switches (B)
  1. Ein Router oder Switch MUSS so konfiguriert werden, dass er unter anderem folgende Ereignisse protokolliert: Konfigurationsänderungen (möglichst automatisch), Reboot, Systemfehler, Statusänderungen pro Interface, System und Netzsegment sowie Login-Fehler **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) DET.3.1.6 deckt die im Satz geforderte Protokollierung systemspezifischer Ereignisse wie Konfigurationsänderungen und Reboots auf IT-Systemebene inhaltlich ab.


## DET.4.8 — Ausstellung neuer HTTPS-Zertifikate  [1 Paare]

**Statement (normativ):** Detektion für Webserver KANN die rechtzeitige Ausstellung neuer HTTPS-Zertifikate für Hostsysteme, die im Internet erreichbar sind, überwachen.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** erhöht
**Guidance (nicht normativ):** „Rechtzeitige Ausstellung neuer HTTPS-Zertifikate“ meint hier, dass überwacht wird, ob vor Ablauf eines bestehenden TLS-/HTTPS-Zertifikats ein neues, gültiges und zur jeweiligen Webserver-Identität passendes Zertifikat aktiviert wird (certificate expiry monitoring, certificate renewal). „HTTPS-Zertifikate“ sind hier X.509-Zertifikate für TLS-gesicherte Webverbindungen, die insbesondere Servernamen, Gültigkeitszeitraum, ausstellende Zertifizierungsstelle und kryptografische Bindung an einen Schlüssel enthalten. „Server, die im Internet erreichbar sind“ bezeichnet Webserver mit öffentlich erreichbarer Adresse oder öffentlich auflösbarem Namen, etwa Webportale, APIs, Kundenportale oder Administrationsoberflächen, sofern sie aus dem Internet angesprochen werden können. Die Vorschrift zielt darauf ab, ablaufende oder nicht rechtzeitig erneuerte Zertifikate frühzeitig sichtbar zu machen: Ein versäumter Austausch könnte zu Browserwarnungen, Dienstunterbrechungen, fehlgeschlagenen API-Verbindungen, Vertrauensverlust bei Nutzenden oder improvisierten Notfallmaßnahmen führen. Eine entsprechende Detektion kann die Verfügbarkeit und Vertrauenswürdigkeit öffentlich erreichbarer Webdienste unterstützen und kann zugleich Hinweise auf Fehlkonfigurationen, unvollständige Automatisierung oder unerwartete Änderungen im Zertifikatsbestand liefern. Hierbei ist es sinnvoll nicht nur die Restlaufzeit mit Schwellwerten zu überwachen, sondern auch die tatsächliche Bereitstellung des neuen Zertifikates. Dazu können ein Monitoring der Zertifikatsdaten direkt am Webendpunkt, sowie Auswertungen aus Load-Balancern oder Reverse-Proxys gehören.

### → CON.1.A4 — Geeignetes Schlüsselmanagement (B)
  1. In einem geeigneten Schlüsselmanagement für kryptografische Hard oder Software MUSS festgelegt werden, wie Schlüssel und Zertifikate erzeugt, gespeichert, ausgetauscht und wieder gelöscht oder vernichtet werden.
  2. Es MUSS ferner festgelegt werden, wie die Integrität und Authentizität der Schlüssel sichergestellt wird.
  3. Kryptografische Schlüssel SOLLTEN immer mit geeigneten Schlüsselgeneratoren und in einer sicheren Umgebung erzeugt werden.
  4. In Hard- oder Software mit kryptografischen Funktionen SOLLTEN voreingestellte Schlüssel (ausgenommen öffentliche Zertifikate) ersetzt werden.
  5. Ein Schlüssel SOLLTE möglichst nur einem Einsatzzweck dienen.
  6. Insbesondere SOLLTEN für die Verschlüsselung und Signaturbildung unterschiedliche Schlüssel benutzt werden.
  7. Kryptografische Schlüssel SOLLTEN mit sicher geltenden Verfahren ausgetauscht werden.
  8. Wenn öffentliche Schlüssel von Dritten verwendet werden, MUSS sichergestellt sein, dass die Schlüssel authentisch sind und die Integrität der Schlüsseldaten gewährleistet ist.
  9. Geheime Schlüssel MÜSSEN sicher gespeichert und vor unbefugtem Zugriff geschützt werden.
  10. Alle kryptografischen Schlüssel SOLLTEN hinreichend häufig gewechselt werden.
  11. Grundsätzlich SOLLTE geregelt werden, wie mit abgelaufenen Schlüsseln und damit verbundenen Signaturen verfahren wird.
  12. Falls die Gültigkeit von Schlüsseln oder Zertifikaten zeitlich eingeschränkt wird, dann MUSS durch die Institution sichergestellt werden, dass die zeitlich eingeschränkten Zertifikate oder Schlüssel rechtzeitig erneuert werden. **◀ ZITIERT**
  13. Eine Vorgehensweise SOLLTE für den Fall festgelegt werden, dass ein privater Schlüssel offengelegt wird.
  14. Alle erzeugten kryptografischen Schlüssel SOLLTEN sicher aufbewahrt und verwaltet werden.
- **Satz 12** | Relation GS++→ED23: `subset-of` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 12) Satz 12 fordert das Sicherstellen der rechtzeitigen Erneuerung zeitlich beschränkter Zertifikate, was die allgemeine Vorgabe für die in DET.4.8 beschriebene Überwachung der rechtzeitigen HTTPS-Zertifikatsausstellung darstellt.


## DET.6.1.2 — Automatische Alarmierung  [31 Paare]

**Statement (normativ):** Detektion SOLLTE bei sicherheitskritischen Ereignissen eine Alarmierung von {{ insert: param, det.6.1.2-prm1 }} durch {{ insert: param, det.6.1.2-prm2 }} ausführen.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Für die Definition eines sicherheitskritischen Ereignisses, siehe Glossar (Namensräume des Grundschutz++). Bewährt hat sich hierzu der Einsatz eines Security Information and Event Management Systems (SIEM), das die Audit Logs verschiedener Hersteller auf Ereignisse überprüfen und diese korrelieren kann. Passen Sie Schwellwerte und Kriterien so an, dass keine Alarmmüdigkeit (alert fatigue) beim Personal aufkommt.

### → DER.1.A15 — Zentrale Detektion und Echtzeitüberprüfung von Ereignismeldungen (H)
  1. Zentrale Komponenten SOLLTEN eingesetzt werden, um sicherheitsrelevante Ereignisse zu erkennen und auszuwerten.
  2. Zentrale, automatisierte Analysen mit Softwaremitteln SOLLTEN eingesetzt werden.
  3. Mit diesen zentralen, automatisierten Analysen mit Softwaremitteln SOLLTEN alle in der Systemumgebung anfallenden Ereignisse aufgezeichnet und in Bezug zueinander gesetzt werden.
  4. Die sicherheitsrelevanten Vorgänge SOLLTEN sichtbar gemacht werden.
  5. Alle eingelieferten Daten SOLLTEN lückenlos in der Protokollverwaltung einsehbar und auswertbar sein.
  6. Die Daten SOLLTEN möglichst permanent ausgewertet werden.
  7. Werden definierte Schwellwerte überschritten, SOLLTE automatisch alarmiert werden. **◀ ZITIERT**
  8. Das Personal SOLLTE sicherstellen, dass bei einem Alarm unverzüglich eine qualifizierte und dem Bedarf entsprechende Reaktion eingeleitet wird.
  9. In diesem Zusammenhang SOLLTEN auch die betroffenen Mitarbeitenden sofort informiert werden.
  10. Die Systemverantwortlichen SOLLTEN regelmäßig die Analyseparameter auditieren und anpassen, falls dies erforderlich ist.
  11. Zusätzlich SOLLTEN bereits überprüfte Daten regelmäßig hinsichtlich sicherheitsrelevanter Ereignisse automatisch untersucht werden.
- **Satz 7** | Relation GS++→ED23: `equivalent-to` | Fundrichtung: beide
  Begründung: (Teilanforderung 7) Die G++-Maßnahme fordert explizit die automatisierte Alarmierung zuständiger Personen bei sicherheitskritischen Ereignissen und deckt damit die Forderung nach automatischer Alarmierung bei Schwellwertüberschreitung direkt ab.

### → APP.4.2.A32 — Echtzeiterfassung und Alarmierung von irregulären Vorgängen (H)
  1. Die wichtigsten Sicherheitsaufzeichnungsfunktionen der SAP-ERP-Systeme wie Security Audit Log oder System Log SOLLTEN kontinuierlich überwacht werden.
  2. Bei verdächtigen Vorgängen SOLLTEN automatisch die zuständigen Mitarbeitenden alarmiert werden. **◀ ZITIERT**
  3. Um SAP-spezifische Sicherheitsvorfälle analysieren und Falschmeldungen von echten Sicherheitsvorfällen abgrenzen zu können, SOLLTEN entweder Mitarbeitende geschult oder entsprechende Serviceleistungen von Drittanbietenden genutzt werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) Die G++-Maßnahme DET.6.1.2 deckt die Forderung nach einer automatisierten Alarmierung zuständiger Personen bei sicherheitskritischen bzw. verdächtigen Ereignissen direkt und vollständig ab.

### → APP.4.3.A18 — Überwachung des Datenbankmanagementsystems (S)
  1. Die für den sicheren Betrieb kritischen Parameter, Ereignisse und Betriebszustände des Datenbankmanagementsystems SOLLTEN definiert werden.
  2. Diese SOLLTEN mithilfe eines Monitoring-Systems überwacht werden.
  3. Für alle kritischen Parameter, Ereignisse und Betriebszustände SOLLTEN Schwellwerte festgelegt werden.
  4. Wenn diese Werte überschritten werden, MUSS geeignet reagiert werden.
  5. Hierbei SOLLTEN die zuständigen Mitarbeitenden alarmiert werden. **◀ ZITIERT**
  6. Anwendungsspezifische Parameter, Ereignisse, Betriebszustände und deren Schwellwerte SOLLTEN mit den Zuständigen für die Fachanwendungen abgestimmt werden.
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) G++ DET.6.1.2 deckt die Forderung nach Alarmierung zuständiger Personen bei sicherheitskritischen Ereignissen bzw. Schwellwertüberschreitungen direkt ab.

### → DER.1.A18 — Durchführung regelmäßiger Integritätskontrollen (H)
  1. Alle Detektionssysteme SOLLTEN regelmäßig daraufhin überprüft werden, ob sie noch integer sind.
  2. Auch SOLLTEN die Berechtigungen der Benutzenden kontrolliert werden.
  3. Zusätzlich SOLLTEN die Sensoren eine Integritätskontrolle von Dateien durchführen.
  4. Bei sich ändernden Werten SOLLTE eine automatische Alarmierung ausgelöst werden. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) DET.6.1.2 fordert die automatisierte Auslösung von Alarmen bei sicherheitskritischen Ereignissen und deckt damit die geforderte automatische Alarmierung bei Integritätsabweichungen als allgemeine Form ab.

### → DER.1.A5 — Einsatz von mitgelieferten Systemfunktionen zur Detektion (B) [Fachverantwortliche]
  1. Falls eingesetzte IT-Systeme oder Anwendungen über Funktionen verfügen, mit denen sich sicherheitsrelevante Ereignisse detektieren lassen, dann MÜSSEN diese aktiviert und benutzt werden.
  2. Falls ein sicherheitsrelevanter Vorfall vorliegt, dann MÜSSEN die Meldungen der betroffenen IT-Systeme ausgewertet werden.
  3. Zusätzlich MÜSSEN die protokollierten Ereignisse anderer IT-Systeme überprüft werden.
  4. Auch SOLLTEN die gesammelten Meldungen in verbindlich festgelegten Zeiträumen stichpunktartig kontrolliert werden.
  5. Es MUSS geprüft werden, ob zusätzliche Schadcodescanner auf zentralen IT-Systemen installiert werden sollen.
  6. Falls zusätzliche Schadcodescanner eingesetzt werden, dann MÜSSEN diese es über einen zentralen Zugriff ermöglichen, ihre Meldungen und Protokolle auszuwerten.
  7. Es MUSS sichergestellt sein, dass die Schadcodescanner sicherheitsrelevante Ereignisse automatisch an die Zuständigen melden. **◀ ZITIERT**
  8. Die Zuständigen MÜSSEN die Meldungen auswerten und untersuchen.
- **Satz 7** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 7) DET.6.1.2 fordert die automatisierte Alarmierung der zuständigen Personen bei sicherheitskritischen Ereignissen und deckt damit die automatische Meldepflicht von Erkennungssystemen wie Schadcodescannern inhaltlich ab.

### → IND.1.A22 — Zentrale Systemprotokollierung und -überwachung (S) [OT-Betrieb (Operational Technology, OT)]
  1. Die Protokollierungsdaten von ICS-Komponenten SOLLTEN zentral gespeichert werden.
  2. Bei sicherheitskritischen Ereignissen SOLLTE automatisch alarmiert werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) DET.6.1.2 fordert explizit die automatische Alarmierung zuständiger Personen bei sicherheitskritischen Ereignissen und deckt die Anforderung damit passgenau ab.

### → IND.2.7.A10 — Anzeige und Alarmierung von simulierten oder gebrückten Variablen (S) [Planende]
  1. Variablen der SIS, die durch Ersatzwerte besetzt (simuliert) oder von außen gebrückt werden, SOLLTEN in geeigneter Weise überwacht werden.
  2. Die Werte SOLLTEN den Benutzenden fortlaufend angezeigt werden.
  3. Grenzwerte SOLLTEN definiert werden.
  4. Wenn diese Grenzwerte erreicht werden, SOLLTEN die zuständigen Personen in geeigneter Weise alarmiert werden. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) DET.6.1.2 deckt die geforderte Alarmierung zuständiger Personen bei Überschreitung definierter Grenzwerte bzw. sicherheitskritischer Ereignisse als allgemeine Anforderung ab.

### → INF.13.A21 — Protokollierung im TGM (S)
  1. Ereignisse, die im Ereignismanagement entsprechend klassifiziert wurden, SOLLTEN protokolliert werden.
  2. Außerdem SOLLTEN für die Systeme sicherheitsrelevante Ereignisse protokolliert werden.
  3. Alle Konfigurationszugriffe sowie alle manuellen und automatisierten Steuerungszugriffe SOLLTEN protokolliert werden.
  4. Abhängig vom Schutzbedarf SOLLTE eine vollumfängliche Protokollierung inklusive Metadaten und Inhalt der Änderungen erfolgen.
  5. Die Protokollierung SOLLTE auf einer zentralen Protokollierungsinstanz zusammengeführt werden.
  6. Protokollierungsdaten SOLLTEN NUR über sichere Kommunikationswege übertragen werden.
  7. Bei sicherheitskritischen Ereignissen SOLLTE automatisch alarmiert werden. **◀ ZITIERT**
- **Satz 7** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 7) DET.6.1.2 fordert explizit die automatische Alarmierung bei sicherheitskritischen Ereignissen und deckt Satz 7 damit vollständig ab.

### → NET.1.2.A26 — Alarming und Logging (S)
  1. Wichtige Ereignisse auf Netzkomponenten und auf den Netzmanagement-Werkzeugen SOLLTEN automatisch an ein zentrales Management-System übermittelt und dort protokolliert werden (siehe OPS.1.1.5 Protokollierung).
  2. Das zuständige Personal SOLLTE zusätzlich automatisch benachrichtigt werden. **◀ ZITIERT**
  3. Das Alarming und Logging SOLLTE mindestens folgende Punkte beinhalten: Ausfall bzw. Nichterreichbarkeit von Netz- oder Management-Komponenten, Hardware-Fehlfunktionen, fehlerhafte Anmeldeversuche sowie kritische Zustände oder Überlastung von IT-Systemen.
  4. Ereignismeldungen bzw. Logging-Daten SOLLTEN einem zentralen Management-System entweder kontinuierlich oder gebündelt übermittelt werden.
  5. Alarmmeldungen SOLLTEN sofort wenn sie auftreten übermittelt werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) G++-Maßnahme DET.6.1.2 fordert explizit die automatisierte Alarmierung zuständiger Personen bei sicherheitskritischen Ereignissen und deckt damit die automatische Benachrichtigung des zuständigen Personals vollständig ab.
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) DET.6.1.2 fordert eine automatisierte Alarmierung bei sicherheitskritischen Ereignissen, was die sofortige Übermittlung von Alarmmeldungen beim Auftreten der Ereignisse inhaltlich abdeckt.

### → NET.3.2.A23 — Systemüberwachung und -Auswertung (S)
  1. Firewalls SOLLTEN in ein geeignetes Systemüberwachungs- bzw. Monitoringkonzept eingebunden werden.
  2. Es SOLLTE ständig überwacht werden, ob die Firewall selbst sowie die darauf betriebenen Dienste korrekt funktionieren.
  3. Bei Fehlern oder wenn Grenzwerte überschritten werden, SOLLTE das Betriebspersonal alarmiert werden.
  4. Zudem SOLLTEN automatische Alarmmeldungen generiert werden, die bei festgelegten Ereignissen ausgelöst werden. **◀ ZITIERT**
  5. Protokolldaten oder Statusmeldungen SOLLTEN NUR über sichere Kommunikationswege übertragen werden.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die G++-Maßnahme DET.6.1.2 fordert explizit eine automatische Alarmierung bei sicherheitskritischen Ereignissen und deckt damit die Anforderung zur Generierung ereignisbasierter automatischer Alarmmeldungen vollständig ab.

### → NET.3.4.A12 — Monitoring der NAC-Lösung (S)
  1. Die zentralen RADIUS-Server und alle Access-Switches mit Authenticator sowie alle weiteren zentralen Dienste, die für die NAC-Lösung essentiell sind, SOLLTEN in ein möglichst umfassendes und einheitliches Monitoring eingebunden werden.
  2. Ergänzend zum allgemeinen Monitoring gemäß OPS.1.1.1 Allgemeiner IT-Betrieb SOLLTEN alle NAC-spezifischen Parameter überwacht werden, die die Funktionalität der NAC-Lösung oder der entsprechenden Dienste sicherstellen.
  3. Insbesondere SOLLTE die Verfügbarkeit des RADIUS-Protokolls überprüft werden.
  4. Hierfür SOLLTEN RADIUS-Anfragen an aktive Konten erzeugt werden, um die gesamte NAC-Wirkkette inklusive der externen Verzeichnisdienste zu prüfen.
  5. Für die Access-Switches SOLLTE der Status von NAC in das Monitoring einbezogen werden, um ein Deaktivieren von NAC zu erkennen.
  6. Abweichungen von definierten Zuständen und Grenzwerten SOLLTEN dem IT-Betrieb gemeldet werden. **◀ ZITIERT**
- **Satz 6** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 6) DET.6.1.2 fordert die automatisierte Alarmierung der zuständigen Stellen bei sicherheitskritischen Ereignissen bzw. Schwellwertüberschreitungen und deckt damit die Meldung von Zustands- und Grenzwertabweichungen ab.

### → NET.3.4.A16 — Protokollierung der Ereignisse (S)
  1. Ergänzend zu OPS.1.1.5 Protokollierung SOLLTEN Statusänderungen an NAC-Komponenten sowie alle relevanten NAC-spezifischen, gegebenenfalls sicherheitskritischen Ereignisse protokolliert werden.
  2. Zusätzlich SOLLTEN alle schreibenden Konfigurationszugriffe auf die zentralen NAC-Komponenten protokolliert werden.
  3. Es SOLLTE festgelegt werden, welche Protokollierungsdaten mit welchen Details erfasst und welche Daten auf einer zentralen Protokollierungsinstanz zusammengeführt werden.
  4. Protokollierungsdaten SOLLTEN NUR über sichere Kommunikationswege übertragen werden.
  5. Sicherheitskritische Ereignisse wie RADIUS-down oder eine ungewöhnliche Anzahl von RADIUS-Anfragen SOLLTEN zu einem automatischen Alarm führen. **◀ ZITIERT**
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) DET.6.1.2 fordert die automatische Alarmierung bei sicherheitskritischen Ereignissen und deckt damit die im Satz geforderte automatisierte Alarmierung für sicherheitskritische Ereignisse allgemeingültig ab.

### → NET.3.4.A25 — Einbindung der NAC-Lösung in ein Sicherheitsmonitoring (H)
  1. Die NAC-Lösung SOLLTE in ein Sicherheitsmonitoring eingebunden werden.
  2. Dies SOLLTE zumindest für die zentralen NAC-Komponenten und für die weiteren zentralen Dienste, die von der NAC-Lösung genutzt werden, umgesetzt werden.
  3. NAC-spezifische Sicherheitsereignisse (z. B. häufige Zurückweisung von Anfragen oder die Mehrfachverwendung von Identitäten) SOLLTEN in eine Alarmierung übernommen werden. **◀ ZITIERT**
  4. Wird für die IT der Institution ein System zur zentralen Detektion und automatisierten Echtzeitüberprüfung von Ereignismeldungen eingesetzt, SOLLTEN die zentralen NAC-Komponenten sowie gegebenenfalls die weiteren zentralen Dienste hierin eingebunden werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) DET.6.1.2 deckt als allgemeine Regelung zur automatischen Alarmierung bei sicherheitskritischen Ereignissen die Übernahme von NAC-spezifischen Sicherheitsereignissen in ein Alarmierungssystem inhaltlich ab.

### → OPS.1.1.1.A22 — Automatisierte Tests auf Schwachstellen (H)
  1. Alle IT-Komponenten SOLLTEN regelmäßig und automatisiert auf Schwachstellen getestet werden.
  2. Die Ergebnisse der Tests SOLLTEN automatisiert protokolliert und anderen Werkzeugen im Sicherheitsmonitoring bereitgestellt werden.
  3. Bei kritischen Schwachstellen SOLLTE eine automatisierte Alarmierung erfolgen. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) DET.6.1.2 fordert eine automatisierte Alarmierung bei sicherheitskritischen Ereignissen, was die geforderte automatisierte Alarmierung bei kritischen Schwachstellen als allgemeinere Maßnahme inhaltlich abdeckt.

### → OPS.1.1.7.A15 — Statusüberwachung, Protokollierung und Alarmierung bei relevanten Ereignissen im Systemmanagement-Lösung und den zu verwaltenden Systemen (S)
  1. Die grundlegenden Performance- und Verfügbarkeitsparameter der Systemmanagement-Lösung und der zu verwaltenden Systeme SOLLTEN kontinuierlich überwacht werden.
  2. Dafür SOLLTEN vorab die jeweiligen Schwellwerte ermittelt werden (Baselining).
  3. Werden definierte Schwellwerte überschritten, SOLLTE das zuständige Personal automatisch benachrichtigt werden. **◀ ZITIERT**
  4. Zur besseren Fehleranalyse SOLLTEN Informationen aus der Statusüberwachung anderer Bereiche, z. B. aus einem eigenen Bereich „Netze“, ebenfalls betrachtet werden, um die genaue Ursache für eine Störung zu finden.
  5. Wichtige Ereignisse auf zu verwaltenden Systemen und auf der Systemmanagement-Lösung SOLLTEN automatisch an eine zentrale Protokollierungsinfrastruktur übermittelt und dort protokolliert werden (siehe OPS.1.1.5 Protokollierung).
  6. Wichtige Ereignisse SOLLTEN mindestens für folgende Aspekte definiert werden: Ausfall sowie Nichterreichbarkeit von zu verwaltenden Systemen, Ausfall sowie Nichterreichbarkeit von Systemmanagement-Komponenten, Hardware-Fehlfunktionen, Anmeldeversuche an der Systemmanagement-Lösung, Anmeldeversuche an zu verwaltenden Systemen, kritische Zustände oder Überlastung der Systemmanagement-Lösung sowie kritische Zustände oder Überlastung von zu verwaltenden Systemen.
  7. Ereignismeldungen sowie Protokollierungs-Daten SOLLTEN an ein zentrales Logging-System übermittelt werden.
  8. Alarmmeldungen SOLLTEN sofort, wenn sie auftreten, übermittelt werden. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) DET.6.1.2 fordert die automatisierte Benachrichtigung bzw. Alarmierung des zuständigen Personals bei kritischen Ereignissen und Schwellwertüberschreitungen und deckt damit die Forderung von Satz 3 inhaltlich ab.
- **Satz 8** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 8) Die G++-Maßnahme DET.6.1.2 fordert eine automatisierte Alarmierung der zuständigen Rollen bei kritischen Ereignissen und deckt damit die unverzügliche Übermittlung von Alarmmeldungen inhaltlich ab.

### → OPS.1.1.7.A25 — Protokollierung und Reglementierung von Systemmanagement-Sitzungen (H)
  1. Die Sitzungsinhalte, insbesondere die Aktivitäten von Benutzenden auf der Systemmanagement-Lösung sowie sämtliche direkte Zugriffe auf zu verwaltende Systeme, SOLLTEN kontinuierlich durch eine technische Lösung protokolliert und reglementiert werden.
  2. Dabei SOLLTEN die Aktivitäten auf Befehlsebene, d. h. manuelle und automatisierte Befehle, kontrolliert und gegebenenfalls unterbunden werden.
  3. Während der Überwachung SOLLTE nicht nur bei konkreten Regelverstößen, sondern auch bei Anomalien im Benutzendenverhalten eine Alarmierung erfolgen. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) DET.6.1.2 fordert die automatisierte Alarmierung bei sicherheitskritischen Ereignissen und deckt damit die allgemeine Pflicht zur Alarmierung bei Regelverstößen und Verhaltensanomalien ab.

### → SYS.1.1.A27 — Hostbasierte Angriffserkennung (H)
  1. Hostbasierte Angriffserkennungssysteme (Host-based Intrusion Detection Systems, IDS und Intrusion Prevention Systems, IPS) SOLLTEN eingesetzt werden, um das Systemverhalten auf Anomalien und Missbrauch hin zu überwachen.
  2. Die eingesetzten IDS/IPS-Mechanismen SOLLTEN geeignet ausgewählt, konfiguriert und ausführlich getestet werden.
  3. Bei einer Angriffserkennung SOLLTE das Betriebspersonal in geeigneter Weise alarmiert werden. **◀ ZITIERT**
  4. Über Betriebssystem-Mechanismen oder geeignete Zusatzprodukte SOLLTEN Veränderungen an Systemdateien und Konfigurationseinstellungen überprüft, eingeschränkt und gemeldet werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) DET.6.1.2 fordert explizit die Alarmierung zuständiger Personen bei sicherheitskritischen Ereignissen und deckt damit die geforderte Alarmierung des Personals bei einer Angriffserkennung direkt ab.

### → SYS.3.2.2.A23 — Durchsetzung von Compliance-Anforderungen (H)
  1. Verstöße gegen die Regelungen der Institution oder sogar eine Manipulation des Betriebssystems SOLLTEN mit einer geeigneten Lösung erkannt werden.
  2. Die folgenden Aktionen SOLLTEN bei Verdacht auf Verstoß gegen Regelungen oder Manipulation des Betriebssystems ausgeführt werden.
  3. Hierzu SOLLTEN entsprechende Funktionen bereitgestellt werden: selbstständiges Versenden von Warnhinweisen, selbstständiges Sperren des Geräts, Löschen der vertraulichen Informationen der Institution, Löschen des kompletten Geräts, Verhindern des Zugangs zu Unternehmens-Apps sowie Verhindern des Zugangs zu den Systemen und Informationen der Institution.
  4. Bei Verdacht auf einen Verstoß oder eine Manipulation SOLLTE ein Alarm an die zuständigen Administrierenden und das Sicherheitsmanagement in der Institution gesandt werden. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) DET.6.1.2 deckt die geforderte Benachrichtigung bei Verdachtsfällen durch die allgemeine Pflicht zur Alarmierung zuständiger Rollen bei sicherheitskritischen Ereignissen ab.

### → DER.1.A17 — Automatische Reaktion auf sicherheitsrelevante Ereignisse (H)
  1. Bei einem sicherheitsrelevanten Ereignis SOLLTEN die eingesetzten Detektionssysteme das Ereignis automatisch melden und mit geeigneten Schutzmaßnahmen reagieren. **◀ ZITIERT**
  2. Hierbei SOLLTEN Verfahren eingesetzt werden, die automatisch mögliche Angriffe, Missbrauchsversuche oder Sicherheitsverletzungen erkennen.
  3. Es SOLLTE möglich sein, automatisch in den Datenstrom einzugreifen, um einen möglichen Sicherheitsvorfall zu unterbinden.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) DET.6.1.2 deckt den Teil der Forderung bezüglich der automatischen Meldung/Alarmierung bei sicherheitsrelevanten Ereignissen direkt ab.

### → INF.13.A20 — Regelung des Ereignismanagements im TGM (S) [Planende]
  1. Im TGM auftretende Ereignisse SOLLTEN hinsichtlich ihrer Bedeutung und ihres Einflusses kategorisiert, gefiltert und klassifiziert werden (englisch Event Management).
  2. Für die Ereignisse SOLLTEN Schwellwerte definiert werden, die eine automatisierte Einstufung von Ereignissen ermöglichen.
  3. Je nach Klassifizierung der Ereignisse SOLLTEN entsprechende Maßnahmen für Monitoring, Alarmierung und Meldewege (Eskalation) sowie Maßnahmen zur Protokollierung bestimmt werden. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) DET.6.1.2 setzt die geforderten Maßnahmen zur Alarmierung und Eskalation in Abhängigkeit von der Kritikalität eines Ereignisses konkret als automatisierten Alarmierungsmechanismus um.

### → IND.2.7.A12 — Sicherstellen der Integrität und Authentizität von Anwendungsprogrammen und Konfigurationsdaten (H) [Planende]
  1. Es SOLLTE darauf geachtet werden, dass die herstellenden Unternehmen geeignete Mechanismen entwickeln und integrieren, die die Integrität und Authentizität von Konfigurationsdaten und Anwendungsprogrammen auf dem Logiksystem oder auf den damit verbundenen Sensoren und Aktoren gewährleisten.
  2. Jegliche Software, die als Download angeboten wird, SOLLTE vor Manipulation geschützt werden.
  3. Verletzungen der Integrität SOLLTEN automatisch erkannt und gemeldet werden. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) DET.6.1.2 deckt die automatische Meldung bzw. Alarmierung bei sicherheitskritischen Ereignissen wie Integritätsverletzungen allgemein ab.

### → INF.14.A25 — Dediziertes Monitoring in der GA (S)
  1. Für alle Komponenten, die für die GA betriebsrelevant sind, SOLLTE ein geeignetes Monitoringkonzept erstellt und umgesetzt werden.
  2. Hierbei SOLLTEN die Verfügbarkeit sowie bedeutsame Parameter der GA-relevanten Komponenten laufend überwacht werden.
  3. Fehlerzustände sowie die Überschreitung definierter Grenzwerte SOLLTEN automatisch an die betreibende Organisation gemeldet werden. **◀ ZITIERT**
  4. Es SOLLTEN durch die GA mindestens Alarme ausgelöst werden, wenn TGA-Anlagen ausfallen oder wichtige Funktionen zum automatisierten Steuern und Regeln nicht verfügbar sind.
  5. Zudem SOLLTE festgelegt werden, für welche besonders sicherheitsrelevanten Ereignisse und für welche weiteren Ereignisse automatische Alarmmeldungen generiert werden.
  6. Statusmeldungen und Monitoringdaten SOLLTEN NUR über sichere Kommunikationswege übertragen werden.
- **Satz 3** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) DET.6.1.2 verlangt die automatisierte Alarmierung zuständiger Stellen bei sicherheitskritischen Ereignissen und deckt damit die geforderte automatische Meldung von Fehlerzuständen und Grenzwertüberschreitungen materiell ab.

### → INF.2.A11 — Automatische Überwachung der Infrastruktur (B) [Haustechnik]
  1. Alle Einrichtungen der Infrastruktur, wie z. B. Leckageüberwachung, Klima-, Strom- und USV-Anlagen, MÜSSEN automatisch überwacht werden.
  2. Erkannte Störungen MÜSSEN schnellstmöglich in geeigneter Weise weitergeleitet und bearbeitet werden.
  3. Im Falle eines Serverraums SOLLTEN IT- und Supportgeräte, die nicht oder nur selten von einer Person bedient werden müssen, mit einer Fernanzeige für Störungen ausgestattet werden.
  4. Die verantwortlichen Mitarbeitenden MÜSSEN zeitnah alarmiert werden. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) DET.6.1.2 fordert die Alarmierung der zuständigen Personen bei sicherheitskritischen Ereignissen und deckt damit die zeitnahe Alarmierung der verantwortlichen Mitarbeitenden inhaltlich ab.

### → NET.3.4.A26 — Hochverfügbarkeit der zentralen NAC-Komponenten (H)
  1. Die zentralen NAC-Komponenten SOLLTEN redundant ausgelegt werden.
  2. Alle weiteren zentralen Dienste, die für die Funktionsfähigkeit der NAC-Lösung essentiell sind, SOLLTEN auch hochverfügbar ausgelegt sein.
  3. Die für die Hochverfügbarkeit relevanten Parameter SOLLTEN in Monitoring und Protokollierung integriert werden.
  4. Statusänderungen und Warnmeldungen SOLLTEN regelmäßig kontrolliert und gegebenenfalls in eine Alarmierung einbezogen werden. **◀ ZITIERT**
  5. Die RADIUS-down-Policies, mit denen eine Kommunikation auch bei ausgefallenem RADIUS-Dienst gewährleistet wird, SOLLTEN das Sicherheitsniveau des Netzes NICHT senken.
- **Satz 4** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) DET.6.1.2 fordert die automatisierte Alarmierung bei sicherheitsrelevanten bzw. kritischen Ereignissen und deckt damit die Einbeziehung relevanter Statusänderungen und Warnmeldungen in eine Alarmierung ab.

### → OPS.1.2.2.A8 — Protokollierung der Archivzugriffe (B) [IT-Betrieb]
  1. Alle Zugriffe auf elektronische Archive MÜSSEN protokolliert werden.
  2. Dafür SOLLTEN Datum, Uhrzeit, Benutzender, Client und die ausgeführten Aktionen sowie Fehlermeldungen aufgezeichnet werden.
  3. Im Archivierungskonzept SOLLTE festgelegt werden, wie lange die Protokolldaten aufbewahrt werden.
  4. Die Protokolldaten der Archivzugriffe SOLLTEN regelmäßig ausgewertet werden.
  5. Dabei SOLLTEN die institutionsinternen Vorgaben beachtet werden.
  6. Auch SOLLTE definiert sein, welche Ereignisse welchen Mitarbeitenden angezeigt werden, wie z. B. Systemfehler, Timeouts oder wenn Datensätze kopiert werden. **◀ ZITIERT**
  7. Kritische Ereignisse SOLLTEN sofort nach der Erkennung geprüft und, falls nötig, weiter eskaliert werden. **◀ ZITIERT**
- **Satz 6** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 6) DET.6.1.2 deckt die gezielte Weiterleitung und Anzeige von Ereignissen an zuständige Personen oder Rollen durch automatisierte Alarmierungsmechanismen inhaltlich ab.
- **Satz 7** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 7) Die Maßnahme DET.6.1.2 deckt die Eskalation bzw. Alarmierung zuständiger Rollen bei sicherheitskritischen Ereignissen unmittelbar nach deren Erkennung ab.

### → SYS.1.6.A24 — Hostbasierte Angriffserkennung (H)
  1. Das Verhalten der Container und der darin betriebenen Anwendungen und Dienste SOLLTE überwacht werden.
  2. Abweichungen von einem normalen Verhalten SOLLTEN bemerkt und gemeldet werden. **◀ ZITIERT**
  3. Die Meldungen SOLLTEN im zentralen Prozess zur Behandlung von Sicherheitsvorfällen angemessen behandelt werden.
  4. Das zu überwachende Verhalten SOLLTE mindestens umfassen: Netzverbindungen, erstellte Prozesse, Dateisystem-Zugriffe und Kernel-Anfragen (Syscalls).
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) DET.6.1.2 fordert die automatisierte Alarmierung bzw. Meldung bei sicherheitskritischen Ereignissen an zuständige Stellen und deckt damit den Meldungsaspekt von festgestellten Verhaltensabweichungen ab.

### → SYS.1.7.A16 — Überwachung von z/OS-Systemen (S)
  1. Während des Betriebs SOLLTE das z/OS-System auf wichtige Meldungen, Ereignisse und die Einhaltung von Grenzwerten überwacht werden.
  2. Insbesondere Fehlermeldungen auf der HMC-Konsole, WTOR- und wichtige WTO-Nachrichten (Write To Operator/with Reply), System Tasks, Sicherheitsverletzungen, Kapazitätsgrenzen sowie die Systemauslastung SOLLTEN berücksichtigt werden.
  3. Für die Überwachung SOLLTEN außerdem mindestens die MCS-Konsole, die System Management Facility, das SYSLOG und die relevanten Protokolldaten der Anwendungen herangezogen werden.
  4. Es SOLLTE gewährleistet sein, dass alle wichtigen Meldungen zeitnah erkannt werden und, falls notwendig, in geeigneter Weise darauf reagiert wird. **◀ ZITIERT**
  5. Systemnachrichten SOLLTEN dabei so gefiltert werden, dass nur die wichtigen Nachrichten dargestellt werden.
- **Satz 4** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) DET.6.1.2 fordert die automatisierte Alarmierung zuständiger Rollen bei sicherheitskritischen Ereignissen, was das zeitnahe Erkennen und Einleiten einer Reaktion auf wichtige Meldungen materiell abdeckt.

### → SYS.4.4.A22 — Systemüberwachung (H)
  1. Die IoT-Geräte SOLLTEN in ein geeignetes Systemüberwachungs- bzw. Monitoringkonzept eingebunden werden.
  2. Der Systemzustand und die Funktionsfähigkeit der IoT-Geräte SOLLTEN laufend überwacht werden.
  3. Fehlerzustände sowie die Überschreitung definierter Grenzwerte SOLLTEN an das Betriebspersonal gemeldet werden. **◀ ZITIERT**
  4. Es SOLLTE geprüft werden, ob die verwendeten Geräte die Anforderung an die Verfügbarkeit erfüllen.
  5. Alternativ SOLLTE geprüft werden, ob weitere Maßnahmen, wie das Einrichten eines Clusters oder die Beschaffung von Standby-Geräten, erforderlich sind.
- **Satz 3** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme DET.6.1.2 verlangt die automatisierte Alarmierung zuständiger Personen bei sicherheitskritischen Ereignissen bzw. Schwellwertüberschreitungen und deckt damit die geforderte Meldung von Fehlerzuständen und Grenzwertüberschreitungen an das Personal ab.


## DET.1.1.1 — Dokumentation  [4 Paare]

**Statement (normativ):** Detektion MUSS die Verfahren und Regelungen dokumentieren.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Ohne eine Dokumentation könnte die Einhaltung der Verfahren und Regelungen von der Tagesform oder dem individuellen Wissen einzelner Mitarbeiter abhängen, was zu inkonsistenten Entscheidungen und Fehlern führen könnte; insbesondere beim Ausscheiden eines langjährigen Administrators könnte wertvolles prozessuales Wissen verloren gehen. Eine klare Dokumentation sichert die Verbindlichkeit und Wiederholbarkeit und dient als unverzichtbare Grundlage für die Einarbeitung neuer Kollegen, für die Durchführung von Audits und zur einheitlichen Anwendung der Regeln in der gesamten Institution. Die Dokumentation kann in einem eigenständigen Dokument als Richtlinie erfolgen, aber auch als Abschnitt in einem bereits bestehenden Dokument oder über die digital strukturiere Erfassung von Maßnahmen zur Umsetzung der Anforderungen, etwa über eine Software zum Management der Informationssicherheit. Sinnvoll ist es Ort und Struktur der Dokumentation an der jeweiligen Zielgruppe, d.h. den für das Management und die Umsetzung verantwortlichen Personen oder Rollen, auszurichten.

### → DER.1.A3 — Festlegung von Meldewegen für sicherheitsrelevante Ereignisse (B)
  1. Für sicherheitsrelevante Ereignisse MÜSSEN geeignete Melde- und Alarmierungswege festgelegt und dokumentiert werden.
  2. Es MUSS bestimmt werden, welche Stellen wann zu informieren sind.
  3. Es MUSS aufgeführt sein, wie die jeweiligen Personen erreicht werden können.
  4. Je nach Dringlichkeit MUSS ein sicherheitsrelevantes Ereignis über verschiedene Kommunikationswege gemeldet werden.
  5. Alle Personen, die für die Meldung bzw. Alarmierung relevant sind, MÜSSEN über ihre Aufgaben informiert sein.
  6. Alle Schritte des Melde- und Alarmierungsprozesses MÜSSEN ausführlich beschrieben sein. **◀ ZITIERT**
  7. Die eingerichteten Melde- und Alarmierungswege SOLLTEN regelmäßig geprüft, erprobt und aktualisiert werden, falls erforderlich.
- **Satz 6** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 6) Die Pflicht zur Dokumentation der Verfahren und Regelungen in DET.1.1.1 deckt die ausführliche Beschreibung aller Schritte des Melde- und Alarmierungsprozesses inhaltlich ab.

### → DER.1.A1 — Erstellung einer Sicherheitsrichtlinie für die Detektion von sicherheitsrelevanten Ereignissen (B)
  1. Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution MUSS eine spezifische Sicherheitsrichtlinie für die Detektion von sicherheitsrelevanten Ereignissen erstellt werden.
  2. In der spezifischen Sicherheitsrichtlinie MÜSSEN nachvollziehbar Anforderungen und Vorgaben beschrieben werden, wie die Detektion von sicherheitsrelevanten Ereignissen geplant, aufgebaut und sicher betrieben werden kann. **◀ ZITIERT**
  3. Die spezifische Sicherheitsrichtlinie MUSS allen im Bereich Detektion zuständigen Mitarbeitenden bekannt und grundlegend für ihre Arbeit sein.
  4. Falls die spezifische Sicherheitsrichtlinie verändert wird oder von den Anforderungen abgewichen wird, dann MUSS dies mit dem oder der verantwortlichen ISB abgestimmt und dokumentiert werden.
  5. Es MUSS regelmäßig überprüft werden, ob die spezifische Sicherheitsrichtlinie noch korrekt umgesetzt ist.
  6. Die Ergebnisse der Überprüfung MÜSSEN sinnvoll dokumentiert werden.
- **Satz 2** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) Satz 2 fordert die nachvollziehbare schriftliche Beschreibung (Dokumentation) der Anforderungen und Vorgaben zur Detektion in der Sicherheitsrichtlinie.

### → OPS.1.1.5.A1 — Erstellung einer Sicherheitsrichtlinie für die Protokollierung (B) [Fachverantwortliche]
  1. Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution MUSS eine spezifische Sicherheitsrichtlinie für die Protokollierung erstellt werden. **◀ ZITIERT**
  2. In dieser Sicherheitsrichtlinie MÜSSEN nachvollziehbar Anforderungen und Vorgaben beschrieben sein, wie die Protokollierung zu planen, aufzubauen und sicher zu betreiben ist. **◀ ZITIERT**
  3. In der spezifischen Sicherheitsrichtlinie MUSS geregelt werden, wie, wo und was zu protokollieren ist.
  4. Dabei SOLLTEN sich Art und Umfang der Protokollierung am Schutzbedarf der Informationen orientieren.
  5. Die spezifische Sicherheitsrichtlinie MUSS von dem oder der ISB gemeinsam mit den Fachverantwortlichen erstellt werden.
  6. Sie MUSS allen für die Protokollierung zuständigen Mitarbeitenden bekannt und grundlegend für ihre Arbeit sein.
  7. Wird die spezifische Sicherheitsrichtlinie verändert oder wird von den Anforderungen abgewichen, MUSS dies mit dem oder der ISB abgestimmt und dokumentiert werden.
  8. Es MUSS regelmäßig überprüft werden, ob die spezifische Sicherheitsrichtlinie noch korrekt umgesetzt ist.
  9. Die Ergebnisse der Überprüfung MÜSSEN dokumentiert werden.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) DET.1.1.1 verlangt die Dokumentation der Regelungen und Verfahren (u. a. in Form einer Richtlinie), was der geforderten Erstellung einer spezifischen Richtlinie entspricht.
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) DET.1.1.1 fordert die Dokumentation von Verfahren und Regelungen (u. a. in Form einer Richtlinie), was der inhaltlichen Ausgestaltung und Verschriftlichung der Vorgaben für Planung, Aufbau und Betrieb aus Satz 2 entspricht.


## DET.3.1.8 — Privilegierte Ereignisse  [12 Paare]

**Statement (normativ):** Detektion für Anwendungen SOLLTE privilegierte Ereignisse einschließlich der Aktivierung, Deaktivierung oder Blockierung privilegierter Funktionen protokollieren.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Privilegierte Ereignisse sind Vorgänge, bei denen besonders weitreichende Rechte genutzt werden – beispielsweise die Vergabe oder Entziehung von Administratorrechten, das Deaktivieren von Virenscannern oder Änderungen an Firewallregeln. Gerade solche Eingriffe könnten einen erheblichen Einfluss auf die Verfügbarkeit und Integrität von Daten haben. Ohne eine gezielte Aufzeichnung könnten sicherheitsrelevante Änderungen unentdeckt bleiben – etwa, wenn ein Angreifer unbefugt einen privilegierten Account übernimmt und Spuren verwischt, oder wenn ein interner Benutzer kritische Funktionen deaktiviert, wodurch Schutzmaßnahmen umgangen werden.

### → APP.2.1.A12 — Überwachung von Verzeichnisdiensten (S)
  1. Verzeichnisdienste SOLLTEN gemeinsam mit dem Server beobachtet und protokolliert werden, auf dem sie betrieben werden.
  2. Insbesondere Änderungen innerhalb des Verzeichnisdienstes sowie Konfigurationsänderungen des Verzeichnisdienstes SOLLTEN vorrangig protokolliert werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) DET.3.1.8 deckt Konfigurationsänderungen und Änderungen an Verzeichnisdienstobjekten (wie Rechtevergaben) als privilegierte Anwendungsereignisse direkt ab.

### → APP.4.2.A29 — Einrichten von Notfall-Konten (S)
  1. Es SOLLTEN Notfall-Konten angelegt werden.
  2. Die eingerichteten Konten und Berechtigungen SOLLTEN stark kontrolliert und genau dokumentiert werden.
  3. Außerdem SOLLTEN alle von Notfall-Konten durchgeführten Aktivitäten protokolliert werden. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) DET.3.1.8 deckt die Protokollierung von Aktivitäten durch Notfall-Konten als allgemeine Anforderung zur Aufzeichnung privilegierter Ereignisse und Funktionen in Anwendungen inhaltlich ab.

### → NET.3.4.A16 — Protokollierung der Ereignisse (S)
  1. Ergänzend zu OPS.1.1.5 Protokollierung SOLLTEN Statusänderungen an NAC-Komponenten sowie alle relevanten NAC-spezifischen, gegebenenfalls sicherheitskritischen Ereignisse protokolliert werden.
  2. Zusätzlich SOLLTEN alle schreibenden Konfigurationszugriffe auf die zentralen NAC-Komponenten protokolliert werden. **◀ ZITIERT**
  3. Es SOLLTE festgelegt werden, welche Protokollierungsdaten mit welchen Details erfasst und welche Daten auf einer zentralen Protokollierungsinstanz zusammengeführt werden.
  4. Protokollierungsdaten SOLLTEN NUR über sichere Kommunikationswege übertragen werden.
  5. Sicherheitskritische Ereignisse wie RADIUS-down oder eine ungewöhnliche Anzahl von RADIUS-Anfragen SOLLTEN zu einem automatischen Alarm führen.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Schreibende Konfigurationszugriffe auf zentrale NAC-Komponenten stellen privilegierte Ereignisse dar, deren Protokollierung durch DET.3.1.8 allgemein gefordert wird.

### → OPS.1.1.2.A18 — Durchgängige Protokollierung administrativer Tätigkeiten (H)
  1. Bei IT-Komponenten mit hohem Schutzbedarf SOLLTEN alle administrativen Tätigkeiten in sämtlichen Bereichen protokolliert werden. **◀ ZITIERT**
  2. Dabei SOLLTE jede administrative Aktion vollständig nachvollzogen werden.
  3. Die ausführenden Administrierenden SOLLTEN keinen Einfluss auf Art und Umfang der Protokollierung nehmen können.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) DET.3.1.8 deckt die geforderte Protokollierung administrativer Tätigkeiten als anwendungsspezifischen Spezialfall für privilegierte Ereignisse und Funktionen inhaltlich ab.

### → OPS.1.1.2.A28 — Protokollierung administrativer Tätigkeiten (S)
  1. Administrative Tätigkeiten SOLLTEN protokolliert werden. **◀ ZITIERT**
  2. Die Protokolldateien SOLLTEN für eine angemessene Zeitdauer geschützt aufbewahrt werden.
  3. Die ausführenden Administrierenden SOLLTEN keine Möglichkeiten haben, die aufgezeichneten Protokolldateien zu verändern oder zu löschen.
  4. Protokolldaten SOLLTEN regelmäßig geprüft werden.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) DET.3.1.8 deckt die Anforderung als anwendungsbezogene Konkretisierung ab, indem sie explizit die Protokollierung privilegierter Ereignisse und administrativer Funktionen fordert.

### → OPS.1.1.2.A5 — Nachweisbarkeit von administrativen Tätigkeiten (B)
  1. Administrative Tätigkeiten MÜSSEN nachweisbar sein. **◀ ZITIERT**
  2. Dafür MUSS mindestens festgehalten werden, welche Änderung bei einer Tätigkeit durchgeführt wurde, wer eine Tätigkeit durchgeführt hat und wann eine Tätigkeit durchgeführt wurde.
  3. Die Institution MUSS jederzeit nachweisen können, welche Person welche administrativen Tätigkeiten durchgeführt hat.
  4. Dazu SOLLTEN alle Administrierenden über eine eigene Zugangskennung verfügen.
  5. Auch Vertretungen von Administrierenden SOLLTEN eigene Zugangskennungen erhalten.
  6. Jeder Anmeldevorgang (Login) über eine Administrationskennung MUSS protokolliert werden.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) DET.3.1.8 setzt die Nachweisbarkeit administrativer Tätigkeiten für den Anwendungskontext durch die Protokollierung privilegierter Ereignisse und Funktionen konkret um.

### → SYS.1.1.A10 — Protokollierung (B)
  1. Generell MÜSSEN alle sicherheitsrelevanten Systemereignisse protokolliert werden, dazu gehören mindestens: Systemstarts und Reboots, erfolgreiche und erfolglose Anmeldungen am IT-System (Betriebssystem und Anwendungssoftware), fehlgeschlagene Berechtigungsprüfungen, blockierte Datenströme (Verstöße gegen ACLs oder Firewallregeln), Einrichtung oder Änderungen von Benutzenden, Gruppen und Berechtigungen, sicherheitsrelevante Fehlermeldungen (z. B. Hardwaredefekte, Überschreitung von Kapazitätsgrenzen) sowie Warnmeldungen von Sicherheitssystemen (z. B. Virenschutz). **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die Maßnahme DET.3.1.8 deckt einen konkreten Teilaspekt von Satz 1 ab, indem sie die Protokollierung privilegierter Ereignisse (wie Rechtevergaben und Änderungen an Sicherheitsfunktionen) bei Anwendungen fordert.

### → IND.1.A15 — Überwachung von weitreichenden Berechtigungen (H)
  1. Die Institution SOLLTE ein Bestandsverzeichnis führen, das alle vergebenen Zutritts-, Zugangs und Zugriffsrechte auf kritische Systeme enthält.
  2. Das Verzeichnis SOLLTE beinhalten, welche Rechte ein bestimmter Benutzender oder eine bestimme Benutzende effektiv hat und wer an einem bestimmten System über welche Rechte verfügt.
  3. Alle kritischen administrativen Tätigkeiten SOLLTEN protokolliert werden. **◀ ZITIERT**
  4. Der IT-Betrieb SOLLTE NICHT die Protokolle löschen oder manipulieren können.
- **Satz 3** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die Maßnahme DET.3.1.8 fordert explizit die Protokollierung privilegierter Ereignisse, was die geforderte Protokollierung kritischer administrativer Tätigkeiten inhaltlich abdeckt.

### → INF.13.A21 — Protokollierung im TGM (S)
  1. Ereignisse, die im Ereignismanagement entsprechend klassifiziert wurden, SOLLTEN protokolliert werden.
  2. Außerdem SOLLTEN für die Systeme sicherheitsrelevante Ereignisse protokolliert werden.
  3. Alle Konfigurationszugriffe sowie alle manuellen und automatisierten Steuerungszugriffe SOLLTEN protokolliert werden. **◀ ZITIERT**
  4. Abhängig vom Schutzbedarf SOLLTE eine vollumfängliche Protokollierung inklusive Metadaten und Inhalt der Änderungen erfolgen.
  5. Die Protokollierung SOLLTE auf einer zentralen Protokollierungsinstanz zusammengeführt werden.
  6. Protokollierungsdaten SOLLTEN NUR über sichere Kommunikationswege übertragen werden.
  7. Bei sicherheitskritischen Ereignissen SOLLTE automatisch alarmiert werden.
- **Satz 3** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) DET.3.1.8 verlangt die Protokollierung privilegierter Ereignisse und Eingriffe, was Konfigurations- und Steuerungszugriffe inhaltlich abdeckt.

### → NET.4.1.A5 — Protokollierung bei TK-Anlagen (B)
  1. Bei TK-Anlagen MÜSSEN geeignete Daten erfasst und bei Bedarf ausgewertet werden.
  2. Protokolliert werden MÜSSEN zusätzlich alle systemtechnischen Eingriffe, die Programmveränderungen beinhalten, sowie Auswertungsläufe, Datenübermittlungen und Datenzugriffe.
  3. Alle Administrationsarbeiten an der TK-Anlage MÜSSEN ebenfalls protokolliert werden. **◀ ZITIERT**
  4. Die protokollierten Informationen SOLLTEN regelmäßig kontrolliert werden.
- **Satz 3** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die Protokollierung privilegierter Ereignisse nach DET.3.1.8 deckt die geforderte Protokollierung von Administrationsarbeiten an der TK-Anlage inhaltlich ab.

### → SYS.1.7.A1 — Einsatz restriktiver z/OS-Kennungen (B)
  1. Berechtigungen mit hoher Autorisierung DÜRFEN NUR an Benutzende vergeben werden, die diese Rechte für ihre Tätigkeiten benötigen.
  2. Insbesondere die RACF-Attribute SPECIAL, OPERATIONS, AUDITOR und die entsprechenden GROUP-Attribute sowie die User-ID 0 unter den Unix System Services (USS) MÜSSEN restriktiv gehandhabt werden.
  3. Die Vergabe und der Einsatz dieser Berechtigungen MÜSSEN nachvollziehbar sein. **◀ ZITIERT**
  4. Die besondere Kennung IBMUSER DARF NUR bei der Neuinstallation zur Erzeugung von Kennungen mit Attribut SPECIAL benutzt werden.
  5. Diese Kennung MUSS danach dauerhaft gesperrt werden.
  6. Um zu vermeiden, dass Administrierende sich dauerhaft aussperren, MUSS ein Notfall-User-Verfahren eingerichtet werden.
- **Satz 3** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) DET.3.1.8 fordert die Protokollierung privilegierter Ereignisse wie der Vergabe und Nutzung von Administrationsrechten, wodurch die geforderte Nachvollziehbarkeit gewährleistet wird.

### → SYS.1.9.A13 — Protokollierung bei Terminalservern (S)
  1. Für die Terminalserver SOLLTE entschieden werden, welche Ereignisse an eine zentrale Protokollierungsinfrastruktur (siehe OPS.1.1.5 Protokollierung) übermittelt werden sollen.
  2. Hierbei SOLLTEN mindestens die folgenden spezifischen Ereignisse an Terminalservern protokolliert werden: Anbindung von Peripheriegeräten der zugreifenden Clients über das Terminalserver-Protokoll, Aktionen auf dem Terminalserver durch zugreifende Clients, die erweiterte Rechte benötigen sowie Konfigurationsänderungen mit Auswirkungen auf den Terminalserver-Dienst. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) DET.3.1.8 deckt die geforderte Protokollierung von Aktionen ab, die erweiterte bzw. privilegierte Rechte auf dem System erfordern.

