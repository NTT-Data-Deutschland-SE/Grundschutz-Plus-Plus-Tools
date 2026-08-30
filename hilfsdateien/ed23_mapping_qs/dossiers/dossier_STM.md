# Review-Dossier Praktik STM

Praktik STM: 7 Controls mit Mapping, 23 Paare gesamt. Gesampelt: 5 Controls (max/min/median Paarzahl + 2 zufällig).

## STM.2.1.2 — Erfassung relevanter Assets  [7 Paare]

**Statement (normativ):** Strukturmodellierung MUSS alle relevanten Assets für die betrachteten Geschäftsprozesse festlegen.
**Klasse:** BSI-Methodik-Grundschutz-plus-plus | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Die Asset-Modellierung ist der zentrale Schritt, um den zuvor festgelegten Informationsverbund strukturiert und nachvollziehbar in sicherheitsrelevante Bestandteile zu zerlegen. Im ersten Durchgang des PDCA-Zyklus ist es ausreichend, die Assets zu erfassen, die für den wichtigsten Geschäftsprozess erforderlich sind. Weitere Geschäftsprozesse und zugehörige Assets können iterativ in nachfolgenden Zyklen oder parallel ergänzt werden. Relevante Assets können insbesondere Informationen, Systeme und Anwendungen (System Assets), Netz- und Kommunikationskomponenten, Infrastrukturelle und physische Assets, Personelle und organisatorische Assets. Für jedes Asset wird eine eindeutige Bezeichnung/ID, eine kurze Beschreibung und ihr Zweck sowie eine Zuordnung zu Geschäftsprozess(en) festgehalten. Zuletzt wird jedem Asset eine verantwortliche Rolle bzw. ein Asset-Owner zugewiesen. Ggfs. ist ebenfalls der Standort bzw. die logische Einordnung (Netz, Anwendungskontext etc.) des Assets festzuhalten. Abhängigkeiten zwischen Assets werden ebenfalls notiert.

### → APP.6.A9 — Inventarisierung von Software (S)
  1. Software SOLLTE inventarisiert werden. **◀ ZITIERT**
  2. In einem Bestandsverzeichnis SOLLTE dokumentiert werden, auf welchen Systemen die Software unter welcher Lizenz eingesetzt wird.
  3. Bei Bedarf SOLLTEN zusätzlich die sicherheitsrelevanten Einstellungen miterfasst werden.
  4. Software SOLLTE nur mit Lizenzen eingesetzt werden, die dem Einsatzzweck und den vertraglichen Bestimmungen entsprechen.
  5. Die Lizenz SOLLTE den gesamten vorgesehenen Benutzungszeitraum der Software abdecken.
  6. Wird von einer Standardkonfiguration abgewichen, SOLLTE dies dokumentiert werden.
  7. Das Bestandsverzeichnis SOLLTE anlassbezogen durch den IT-Betrieb aktualisiert werden, insbesondere wenn Software installiert wird.
  8. Das Bestandsverzeichnis SOLLTE so aufgebaut sein, dass bei Sicherheitsvorfällen eine schnelle Gesamtübersicht mit den notwendigen Details ermöglicht wird.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) STM.2.1.2 fordert die Erfassung aller relevanten Assets, wozu explizit auch Anwendungen und Software im Informationsverbund gehören.

### → IND.1.A4 — Dokumentation der OT-Infrastruktur (S)
  1. Alle sicherheitsrelevanten Parameter der OT-Infrastruktur SOLLTEN dokumentiert sein.
  2. In einem Bestandsverzeichnis SOLLTEN alle Software- und Systemkomponenten geführt werden. **◀ ZITIERT**
  3. Hieraus SOLLTEN die eingesetzten Produkt- und Protokollversionen sowie die Zuständigkeiten hervorgehen.
  4. Zu den eingesetzten Komponenten SOLLTEN eventuelle Restriktionen der herstellenden Unternehmen oder regulatorische Auflagen bestimmt sein.
  5. Diese Dokumentation und ein Systeminventar SOLLTEN beispielsweise in einem Leitsystem geführt werden.
  6. Zusätzlich SOLLTE ein aktueller Netzplan Zonen, Zonenübergänge (Conduits), eingesetzte Kommunikationsprotokolle und -verfahren sowie Außenschnittstellen dokumentieren.
  7. Bei den Schnittstellen SOLLTEN aktive Netzkomponenten und manuelle Datentransferverfahren, z. B. durch Wechseldatenträger, berücksichtigt werden.
  8. Zonen und Conduits schützen die OT-Infrastrukur, indem die Automatisierungslösung in Zellen und Kommunikationskanälen strukturiert werden SOLLTE.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 2) Satz 2 fordert die Führung aller Software- und Systemkomponenten in einem Bestandsverzeichnis, was eine direkte Ausprägung der Erfassung relevanter System-Assets darstellt.

### → IND.2.7.A1 — Erfassung und Dokumentation (B) [Planende, Wartungspersonal]
  1. Alle zum SIS gehörenden Hardware- und Softwarekomponenten, relevante Informationen, Verbindungen sowie Rollen und Zuständigkeiten MÜSSEN gesondert erfasst und dokumentiert werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) STM.2.1.2 deckt die Erfassung und Dokumentation aller relevanten Assets (Hard-/Software, Informationen, Verbindungen und verantwortliche Rollen) als allgemeine Anforderung vollständig ab.

### → INF.13.A8 — Erstellung und Pflege eines Inventars für das TGM (S) [Planende]
  1. Für die Dokumentation von Systemen, die durch das TGM verwaltet werden, SOLLTE ein Inventar erstellt und gepflegt werden. **◀ ZITIERT**
  2. Das Inventar SOLLTE vollständig und aktuell gehalten werden.
  3. Aus dem Inventar SOLLTEN für alle Systeme Verantwortlichkeiten und Zuständigkeiten ersichtlich sein.
  4. Auch die Elemente der TGM-Infrastruktur selbst SOLLTEN dokumentiert werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 1) Satz 1 fordert die Erstellung und Pflege eines Inventars für durch das TGM verwaltete Systeme, was eine konkrete fachspezifische Ausprägung der Erfassung relevanter Assets darstellt.

### → SYS.4.3.A1 — Regelungen zum Umgang mit eingebetteten Systemen (B)
  1. Alle Benutzenden und Administrierende MÜSSEN über Verhaltensregeln und Meldewege bei Ausfällen, Fehlfunktionen oder bei Verdacht auf einen Sicherheitsvorfall informiert sein.
  2. Alle eingebetteten Systeme inklusive Schnittstellen MÜSSEN erfasst werden. **◀ ZITIERT**
  3. Die eingebetteten Systeme MÜSSEN sicher vorkonfiguriert werden.
  4. Die vorgenommene Konfiguration SOLLTE dokumentiert sein.
  5. Weiterhin SOLLTEN Regelungen festgelegt werden, um die Integrität und Funktionsfähigkeit der eingebetteten Systeme zu testen.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) STM.2.1.2 fordert die Erfassung aller relevanten Assets (einschliesslich Systeme und ihrer logischen Einordnung bzw. Schnittstellen) und deckt damit die Erfassung eingebetteter Systeme als allgemeinere Basispflicht ab.

### → OPS.1.1.1.A6 — Durchführung des IT-Asset-Managements (S)
  1. Der IT-Betrieb SOLLTE eine Übersicht aller vorhandenen IT-Assets erstellen, regelmäßig prüfen und aktuell halten. **◀ ZITIERT**
  2. Im IT-Asset-Management (ITAM) SOLLTEN alle produktiven IT-Komponenten, Test-Instanzen und IT-Komponenten der Reservevorhaltung erfasst werden.
  3. Auch vorhandene, aber nicht mehr genutzte IT-Assets SOLLTEN erfasst werden.
  4. Es SOLLTEN ITAM-Tools eingesetzt werden, die eine zentrale Verwaltung der IT-Assets ermöglichen.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 1) Satz 1 fordert die Erstellung und Pflege einer Übersicht aller IT-Assets, was sich mit der Erfassung sicherheitsrelevanter Assets überschneidet.

### → ORP.1.A8 — Betriebsmittel- und Geräteverwaltung (S) [IT-Betrieb]
  1. Alle Geräte und Betriebsmittel, die Einfluss auf die Informationssicherheit haben und die zur Aufgabenerfüllung und zur Einhaltung der Sicherheitsanforderungen erforderlich sind, SOLLTEN in ausreichender Menge vorhanden sein.
  2. Es SOLLTE geeignete Prüf- und Genehmigungsverfahren vor Einsatz der Geräte und Betriebsmittel geben.
  3. Geräte und Betriebsmittel SOLLTEN in geeigneten Bestandsverzeichnissen aufgelistet werden. **◀ ZITIERT**
  4. Um den Missbrauch von Daten zu verhindern, SOLLTE die zuverlässige Löschung oder Vernichtung von Geräten und Betriebsmitteln geregelt sein (siehe hierzu CON.6 Löschen und Vernichten).
- **Satz 3** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 3) Satz 3 fordert die Auflistung von Geräten und Betriebsmitteln in Bestandsverzeichnissen, was sich mit der Erfassung und Dokumentation relevanter Assets in STM.2.1.2 überschneidet.


## STM.3.1 — Überprüfung des gesetzten Sicherheitsniveaus  [1 Paare]

**Statement (normativ):** Strukturmodellierung SOLLTE die initiale Einstufung der Sicherheitsniveaus der Anforderungen im Anforderungspaket bei Abweichungen des Kontextes der Institution überprüfen.
**Klasse:** BSI-Methodik-Grundschutz-plus-plus | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Diese Anforderung ist besonders dann erforderlich, wenn Geschäftsprozesse oder die darin verarbeiteten Informationen einen hohen Schutzbedarf aufweisen. In diesem Teilschritt der Anforderungsanalyse´wird die initiale Einstellung des Sicherheitsniveaus überprüft und bei Bedarf, auch bei einzelnen Assets, geändert.

### → ISMS.1.A11 — Aufrechterhaltung der Informationssicherheit (S)
  1. Der Sicherheitsprozess, die Sicherheitskonzepte, die Leitlinie zur Informationssicherheit und die Organisationsstruktur für Informationssicherheit SOLLTEN regelmäßig auf Wirksamkeit und Angemessenheit überprüft und aktualisiert werden.
  2. Dazu SOLLTEN regelmäßig Vollständigkeits- bzw. Aktualisierungsprüfungen des Sicherheitskonzeptes durchgeführt werden.
  3. Ebenso SOLLTEN regelmäßig Sicherheitsrevisionen durchgeführt werden.
  4. Dazu SOLLTE geregelt sein, welche Bereiche und Sicherheitsmaßnahmen wann und von wem zu überprüfen sind.
  5. Überprüfungen des Sicherheitsniveaus SOLLTEN regelmäßig (mindestens jährlich) sowie anlassbezogen durchgeführt werden. **◀ ZITIERT**
  6. Die Prüfungen SOLLTEN von qualifizierten und unabhängigen Personen durchgeführt werden.
  7. Die Ergebnisse der Überprüfungen SOLLTEN nachvollziehbar dokumentiert sein.
  8. Darauf aufbauend SOLLTEN Mängel beseitigt und Korrekturmaßnahmen ergriffen werden.
- **Satz 5** | Relation GS++→ED23: `subset-of` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 5) Satz 5 fordert explizit anlassbezogene sowie regelmäßige Überprüfungen des Sicherheitsniveaus, was sich inhaltlich mit der Überprüfung des Sicherheitsniveaus bei Kontextabweichungen überschneidet.


## STM.4.1 — Durchführung der Risikobetrachtung  [4 Paare]

**Statement (normativ):** Strukturmodellierung MUSS eine Risikobetrachtung bei durch die GS++-Methodik festgeleger Notwendigkeit ausführen.
**Klasse:** BSI-Methodik-Grundschutz-plus-plus | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Diese Anforderung beschreibt Szenarien, die einen Aussprung in eine separate Risikobetrachtung erfordern. Eine Risikobetrachtung ist insbesondere notwendig bei Geschäftsprozessen oder Assets mit hohem Schutzbedarf, bei Herabstufung des Sicherheitsniveaus (von erhöht auf normal- SdT) oder bei Nicht-Umsetzung von Anforderungen. Zuletzt ist eine Risikobetrachtung zur Ergänzung des Anforderungspakets z.B. bei Assets ohne passende Anforderungen im GS++ erforderlich.

### → APP.2.2.A5 — Absicherung des Domänencontrollers (B)
  1. Aufgrund der zentralen Rolle und der Schadensauswirkung bei Kompromittierung des AD DS für die Infrastruktur SOLLTE eine Risikobetrachtung durchgeführt werden. **◀ ZITIERT**
  2. Der Notfallzugriff auf den Domänencontroller mit dem lokalen Restore-Konto DSRM (Directory Services Restore Mode) MUSS im Rahmen des Notfallmanagements geplant werden.
  3. Auf dem Domänencontroller MUSS eine ausreichende Größe für das Sicherheitsprotokoll auf Grundlage des in DER.1 Detektion von sicherheitsrelevanten Ereignissen festgelegten Zeitraums eingestellt sein.
  4. Aufgrund der zentralen Bedeutung des Domänencontrollers SOLLTEN auf diesem Server keine weiteren Dienste betrieben werden, sofern diese nicht zwingend auf dem gleichen Server zum Betrieb des AD DS erforderlich sind.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) G++ STM.4.1 verlangt als übergeordnete Anforderung die Durchführung einer Risikobetrachtung bei hohem Schutzbedarf bzw. Schadensauswirkung, was die geforderte Risikobetrachtung für den AD DS inhaltlich abdeckt.

### → OPS.3.2.A12 — Durchführung einer risikoorientierten Betrachtung von Prozessen, Anwendungen und IT-Systemen (S)
  1. Werden Prozesse, Anwendungen oder IT-Systeme neu aufgebaut und Kunden bereitgestellt, SOLLTEN diese regelmäßig und anlassbezogen risikoorientiert betrachtet und dokumentiert werden. **◀ ZITIERT**
  2. Aus den sich daraus ergebenen Ergebnissen SOLLTEN geeignete Maßnahmen festgelegt werden.
  3. Darüber hinaus SOLLTEN die Resultate dazu verwendet werden, um das Informationssicherheitsmanagement weiter zu verbessern.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme STM.4.1 deckt als allgemeinere methodische Vorgabe zur Durchführung von Risikobetrachtungen für Prozesse und Assets die in Satz 1 geforderte risikoorientierte Betrachtung ab.

### → DER.4.A7 — Erstellung eines Notfallkonzepts (H) [Institutionsleitung]
  1. Alle kritischen Geschäftsprozesse und Ressourcen SOLLTEN identifiziert werden, beispielsweise mit einer Business-Impact-Analyse (BIA).
  2. Es SOLLTEN die wichtigsten relevanten Risiken für die kritischen Geschäftsprozesse und Fachaufgaben sowie deren Ressourcen identifiziert werden. **◀ ZITIERT**
  3. Für jedes identifizierte Risiko SOLLTE entschieden werden, welche Risikostrategien zur Risikobehandlung eingesetzt werden sollen.
  4. Es SOLLTEN Kontinuitätsstrategien entwickelt werden, die einen Wiederanlauf und eine Wiederherstellung der kritischen Geschäftsprozesse in der geforderten Zeit ermöglichen.
  5. Es SOLLTE ein Notfallkonzept erstellt werden.
  6. Es SOLLTEN solche Notfallpläne und Maßnahmen entwickelt und implementiert werden, die eine effektive Notfallbewältigung und eine schnelle Wiederaufnahme der kritischen Geschäftsprozesse ermöglichen.
  7. Im Notfallkonzept SOLLTE die Informationssicherheit berücksichtigt und entsprechende Sicherheitskonzepte für die Notfalllösungen entwickelt werden.
- **Satz 2** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die Durchführung einer Risikobetrachtung für Geschäftsprozesse und Assets mit hohem Schutzbedarf nach STM.4.1 deckt die geforderte Identifikation relevanter Risiken für kritische Geschäftsprozesse und Ressourcen ab.

### → ORP.5.A5 — Ausnahmegenehmigungen (S) [Vorgesetzte]
  1. Ist es in Einzelfällen erforderlich, von getroffenen Regelungen abzuweichen, SOLLTE die Ausnahme begründet und durch eine autorisierte Stelle nach einer Risikoabschätzung genehmigt werden. **◀ ZITIERT**
  2. Es SOLLTE ein Genehmigungsverfahren für Ausnahmegenehmigungen geben.
  3. Es SOLLTE eine Übersicht über alle erteilten Ausnahmegenehmigungen erstellt und gepflegt werden.
  4. Ein entsprechendes Verfahren für die Dokumentation und ein Überprüfungsprozess SOLLTE etabliert werden.
  5. Alle Ausnahmegenehmigungen SOLLTEN befristet sein.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 1) Satz 1 fordert explizit eine Risikoabschätzung bei Abweichungen von getroffenen Regelungen, was einem der konkreten Anlässe zur Durchführung einer Risikobetrachtung gemäß STM.4.1 entspricht.


## STM.1.2 — Dokumentation der externen Schnittstellen  [4 Paare]

**Statement (normativ):** Strukturmodellierung MUSS Schnittstellen des Informationsverbunds zu externen Prozessen festlegen.
**Klasse:** BSI-Methodik-Grundschutz-plus-plus | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Zum Informationsverbund werden die organisatorischen, technischen und infrastrukturellen Schnittstellen dargestellt. Wie bei der Beschreibung des Informationsverbunds selbst, werden auch hier organisatorische, technische sowie infrastrukturelle Schnittstellen berücksichtigt.

### → IND.1.A4 — Dokumentation der OT-Infrastruktur (S)
  1. Alle sicherheitsrelevanten Parameter der OT-Infrastruktur SOLLTEN dokumentiert sein.
  2. In einem Bestandsverzeichnis SOLLTEN alle Software- und Systemkomponenten geführt werden.
  3. Hieraus SOLLTEN die eingesetzten Produkt- und Protokollversionen sowie die Zuständigkeiten hervorgehen.
  4. Zu den eingesetzten Komponenten SOLLTEN eventuelle Restriktionen der herstellenden Unternehmen oder regulatorische Auflagen bestimmt sein.
  5. Diese Dokumentation und ein Systeminventar SOLLTEN beispielsweise in einem Leitsystem geführt werden.
  6. Zusätzlich SOLLTE ein aktueller Netzplan Zonen, Zonenübergänge (Conduits), eingesetzte Kommunikationsprotokolle und -verfahren sowie Außenschnittstellen dokumentieren.
  7. Bei den Schnittstellen SOLLTEN aktive Netzkomponenten und manuelle Datentransferverfahren, z. B. durch Wechseldatenträger, berücksichtigt werden. **◀ ZITIERT**
  8. Zonen und Conduits schützen die OT-Infrastrukur, indem die Automatisierungslösung in Zellen und Kommunikationskanälen strukturiert werden SOLLTE.
- **Satz 7** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 7) STM.1.2 fordert die Festlegung und Dokumentation der technischen sowie organisatorischen Schnittstellen des Informationsverbunds, was die Berücksichtigung von Netzkomponenten und manuellen Transferverfahren einschließt.

### → INF.14.A2 — Festlegung eines Inbetriebnahme- und Schnittstellenmanagements für die GA (B)
  1. Aufgrund der Vielzahl von TGA-Anlagen und Komponenten in Gebäuden, die in GA-Systemen angebunden werden, MUSS der Ablauf zur Inbetriebnahme der involvierten TGA-Anlagen und GA-relevanten Komponenten aufeinander abgestimmt und übergreifend festgelegt werden.
  2. Dieser Ablauf MUSS koordiniert umgesetzt werden, um ein voll funktionsfähiges Gebäude zu gewährleisten.
  3. Ebenso MÜSSEN klare Schnittstellen zwischen den betreibenden Organisationen der GA und der GA-relevanten Komponenten sowie den betreibenden Organisationen der TGA-Anlagen definiert werden. **◀ ZITIERT**
  4. Inbetriebnahme- und Schnittstellenmanagement MÜSSEN dokumentiert werden.
  5. Sowohl regelmäßig als auch zusätzlich bei Bedarf MÜSSEN die Festlegungen geprüft und gegebenenfalls nachjustiert werden.
  6. Insbesondere bei Änderungen innerhalb der GA-Systeme MÜSSEN die Festlegungen angepasst werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) STM.1.2 fordert allgemein die Festlegung organisatorischer Schnittstellen des Verbunds zu externen Prozessen und Organisationen, was die Definition klarer Schnittstellen zwischen den betreibenden Organisationen der GA und TGA abdeckt.

### → OPS.2.2.A4 — Festlegung von Verantwortungsbereichen und Schnittstellen (B) [Fachverantwortliche]
  1. Basierend auf der Service-Definition für Cloud-Dienste MÜSSEN alle relevanten Schnittstellen und Verantwortlichkeiten für die Cloud-Nutzung identifiziert und dokumentiert werden. **◀ ZITIERT**
  2. Es MUSS klar erkennbar sein, wie die Verantwortungsbereiche zwischen Cloud-Diensteanbietenden und der auftraggebenden Institution voneinander abgegrenzt sind.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 1) Satz 1 fordert die Identifikation und Dokumentation relevanter Schnittstellen bei der Cloud-Nutzung, was ein fachspezifischer Anwendungsfall der Dokumentation externer Schnittstellen ist.

### → OPS.2.3.A1 — Erstellung von Anforderungsprofilen für Prozesse (B) [Fachverantwortliche]
  1. Falls keine Business-Impact-Analyse (BIA) vorhanden ist, MÜSSEN Anforderungsprofile in Form von Steckbriefen für die Prozesse angefertigt werden, die potenziell ausgelagert werden sollen.
  2. Diese Anforderungsprofile MÜSSEN die Funktion, verarbeite Daten, Schnittstellen sowie eine Bewertung der Informationssicherheit enthalten. **◀ ZITIERT**
  3. Insbesondere MÜSSEN die Abhängigkeiten zwischen den Prozessen sowie zu untergeordneten Teilprozessen berücksichtigt werden.
  4. Die Anforderungsprofile MÜSSEN die Kritikalität des jeweiligen Prozesses für den ordentlichen Geschäftsbetrieb abbilden.
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 2) Satz 2 fordert für potenziell auszulagernde Prozesse die Erfassung von Schnittstellen in Anforderungsprofilen, was einen konkreten Anwendungsfall der Festlegung und Dokumentation von Schnittstellen zu externen Prozessen darstellt.


## STM.2.1 — Erstellung eines Anforderungspakets  [2 Paare]

**Statement (normativ):** Strukturmodellierung MUSS ein Anforderungspaket für den betrachteten Informationsverbund modellieren.
**Klasse:** BSI-Methodik-Grundschutz-plus-plus | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Das Anforderungspaket enthält alle Anforderungen, die für den betrachteten Informationsverbund und den priorisierten Geschäftsprozess relevant sind. Diese stammen zum Großteil aus dem GS++, können jedoch bei Bedarf durch individuelle Anforderungen ergänzt werden. Diese Anforderung dient der grundsätzlichen Vorgabe ein Anforderungspaket zu erstellen. Weitere Details sind den folgenden Anforderungen dieser Praktik zu entnehmen.

### → ISMS.1.A10 — Erstellung eines Sicherheitskonzepts (S)
  1. Für den festgelegten Geltungsbereich (Informationsverbund) SOLLTE ein angemessenes Sicherheitskonzept als das zentrale Dokument im Sicherheitsprozess erstellt werden. **◀ ZITIERT**
  2. Es SOLLTE entschieden werden, ob das Sicherheitskonzept aus einem oder aus mehreren Teilkonzepten bestehen soll, die sukzessive erstellt werden, um zunächst in ausgewählten Bereichen das erforderliche Sicherheitsniveau herzustellen.
  3. Im Sicherheitskonzept MÜSSEN aus den Sicherheitszielen der Institution, dem identifizierten Schutzbedarf und der Risikobewertung konkrete Sicherheitsmaßnahmen passend zum betrachteten Informationsverbund abgeleitet werden.
  4. Sicherheitsprozess und Sicherheitskonzept MÜSSEN die individuell geltenden Vorschriften und Regelungen berücksichtigen.
  5. Die im Sicherheitskonzept vorgesehenen Maßnahmen MÜSSEN zeitnah in die Praxis umgesetzt werden.
  6. Dies MUSS geplant und die Umsetzung MUSS kontrolliert werden.
- **Satz 1** | Relation GS++→ED23: `equivalent-to` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) Satz 1 fordert die grundlegende Erstellung eines angemessenen Sicherheitskonzepts für den festgelegten Informationsverbund, was der Modellierung des Anforderungspakets entspricht.

### → ISMS.1.A7 — Festlegung von Sicherheitsmaßnahmen (B)
  1. Im Rahmen des Sicherheitsprozesses MÜSSEN für die gesamte Informationsverarbeitung ausführliche und angemessene Sicherheitsmaßnahmen festgelegt werden. **◀ ZITIERT**
  2. Alle Sicherheitsmaßnahmen SOLLTEN systematisch in Sicherheitskonzepten dokumentiert werden.
  3. Die Sicherheitsmaßnahmen SOLLTEN regelmäßig aktualisiert werden.
- **Satz 1** | Relation GS++→ED23: `equivalent-to` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) STM.2.1 fordert die übergeordnete Modellierung eines Anforderungspakets für den gesamten Informationsverbund, was der Festlegung von Sicherheitsmaßnahmen für die Informationsverarbeitung entspricht.

