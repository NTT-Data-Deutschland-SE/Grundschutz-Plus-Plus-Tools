# Review-Dossier Praktik ASST

Praktik ASST: 53 Controls mit Mapping, 476 Paare gesamt. Gesampelt: 5 Controls (max/min/median Paarzahl + 2 zufällig).

## ASST.1.1.2 — Zuweisung der Aufgaben  [6 Paare]

**Statement (normativ):** Informationen und Assets MUSS die mit den Verfahren und Regelungen verbundenen Aufgaben {{ insert: param, asst.1.1.2-prm1 }} zuweisen.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Die Zuweisung von Aufgaben bezeichnet die eindeutige und verbindliche Übertragung von konkreten Tätigkeiten und Verantwortlichkeiten des Änderungsprozesses, wie etwa die Risikobewertung, die technische Umsetzung oder die finale Freigabe, an definierte Stellen in der Institution. Der Sinn dieser Vorschrift ist es, die Verantwortlichkeit ("Accountability") für jeden einzelnen Schritt im Prozess klarzustellen. Ohne eine solche Zuweisung könnten kritische Prüfungen unterbleiben, weil sich niemand explizit zuständig fühlt, was wiederum die Wahrscheinlichkeit fehlgeschlagener Änderungen erhöht. Eine klare Regelung kann sicherstellen, dass keine Aufgaben übersehen werden und jede Tätigkeit von einer dafür qualifizierten und befugten Stelle ausgeführt wird, was die Prozesssicherheit signifikant erhöht. Eine bewährte Methode zur Umsetzung ist die Erstellung einer RACI-Matrix (Responsible, Accountable, Consulted, Informed), die tabellarisch für jeden Prozessschritt darstellt, wer für die Durchführung verantwortlich ist, wer die Gesamtverantwortung trägt, wer zu konsultieren und wer zu informieren ist. Diese Zuständigkeiten können auch direkt in einem Workflow- oder Ticketsystem abgebildet werden, sodass Aufgaben, wie beispielsweise Genehmigungsschritte, automatisch an die richtige Gruppe oder Person weitergeleitet werden. Sinnvoll ist es die Zuweisung anhand von Rollen (z.B. "Anwendungsverantwortlicher", "Netzwerkadministrator", "Change Manager") vorzunehmen, statt an konkrete Personen. Dieser Ansatz stellt sicher, dass die Prozesse auch bei Personalwechseln stabil weiterlaufen, da die Zuständigkeit an die Funktion und nicht an das Individuum gebunden ist.

### → APP.3.6.A8 — Verwaltung von Domainnamen (B) [Zentrale Verwaltung]
  1. Es MUSS sichergestellt sein, dass die Registrierungen für alle Domains, die von einer Institution benutzt werden, regelmäßig und rechtzeitig verlängert werden.
  2. Eine Person MUSS bestimmt werden, die dafür zuständig ist, die Internet-Domainnamen zu verwalten. **◀ ZITIERT**
  3. Falls Dienstleistende mit der Domainverwaltung beauftragt werden, MUSS darauf geachtet werden, dass die Institution die Kontrolle über die Domains behält.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme ASST.1.1.2 deckt als allgemeine Anforderung zur Zuweisung von Asset-bezogenen Aufgaben an zuständige Personen oder Rollen die Benennung einer zuständigen Person für das Domain-Management inhaltlich ab.

### → INF.11.A4 — Erstellung einer Sicherheitsrichtlinie (S) [Fachverantwortliche, IT-Betrieb]
  1. Alle relevanten Sicherheitsanforderungen für die IT innerhalb der Fahrzeuge SOLLTEN in einer für Mitarbeitende verpflichtenden Sicherheitsrichtlinie dokumentiert werden.
  2. Die Richtlinie SOLLTE allen relevanten Mitarbeitenden der Institution bekannt sein und die Grundlage für ihren Umgang mit Fahrzeugen darstellen.
  3. In der Richtlinie SOLLTEN die Zuständigkeiten für einzelne Aufgaben klar geregelt sein. **◀ ZITIERT**
  4. Die Sicherheitsrichtlinie SOLLTE regelmäßig überprüft und anlassbezogen aktualisiert werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme fordert explizit die Zuweisung der mit den Regelungen verbundenen Aufgaben an zuständige Personen oder Rollen und deckt damit die geforderte Regelung der Zuständigkeiten direkt ab.

### → INF.11.A6 — Festlegung von Handlungsanweisungen (S) [Fachverantwortliche, Benutzende]
  1. Für alle wesentlichen Situationen, die die Informationssicherheit von Fahrzeugen betreffen, SOLLTEN Handlungsanweisungen in Form von Checklisten vorliegen.
  2. Die Handlungsanweisungen SOLLTEN dabei in die Sicherheitsrichtlinie integriert werden und in geeigneter Form als Checklisten verfügbar sein, während das Fahrzeug benutzt wird.
  3. Hierbei SOLLTE auch der Fall berücksichtigt werden, dass das Fahrzeug selbst gestohlen wird.
  4. Die Handlungsanweisungen SOLLTEN insbesondere nachfolgende Szenarien behandeln: Ausfall von IT-Komponenten der Fahrzeuge, Notfallsituationen wie Unfälle, unerlaubtes Betreten der Fahrzeuge sowie Diebstahl der Fahrzeuge oder darin abgelegter Gegenstände mit Relevanz für die Informationssicherheit.
  5. Die Zuständigkeiten für die einzelnen Aufgaben SOLLTEN in der Checkliste dokumentiert sein. **◀ ZITIERT**
  6. Die Anweisungen SOLLTEN von den Fahrzeugbenutzenden in den entsprechenden Situationen angewendet werden.
  7. Anhand der Checkliste SOLLTE dokumentiert werden, wie sie in diesen Situationen vorgegangen sind.
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) Die G++-Maßnahme fordert allgemein die Zuweisung von Aufgaben an zuständige Rollen oder Personen, was die fahrzeugspezifische Dokumentation von Zuständigkeiten für Aufgaben in Checklisten inhaltlich abdeckt.

### → OPS.1.1.1.A19 — Regelungen für Wartungs- und Reparaturarbeiten (S)
  1. IT-Komponenten SOLLTEN regelmäßig gewartet werden.
  2. Es SOLLTE geregelt sein, welche Sicherheitsaspekte bei Wartungs- und Reparaturarbeiten zu beachten sind.
  3. Es SOLLTE festgelegt werden, wer für die Wartung oder Reparatur von IT-Komponenten zuständig ist. **◀ ZITIERT**
  4. Durchgeführte Wartungs- und Reparaturarbeiten SOLLTEN dokumentiert werden.
  5. Es SOLLTE sichergestellt werden, dass Wartungs- und Reparaturarbeiten, die durch Dritte ausgeführt werden, mit den Beteiligten abgestimmt sind.
  6. Es SOLLTEN interne Mitarbeitende des IT-Betriebs bestimmt werden, die solche Arbeiten autorisieren, gegebenenfalls beobachten oder unterstützen und abnehmen.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme fordert als allgemeine Regelung die Zuweisung von Aufgaben und Zuständigkeiten für verfahrensbezogene Tätigkeiten an Personen oder Rollen, was die Festlegung von Zuständigkeiten für Wartungs- und Reparaturarbeiten an IT-Assets abdeckt.

### → SYS.4.4.A9 — Regelung des Einsatzes von IoT-Geräten (S)
  1. Für jedes IoT-Gerät SOLLTE eine zuständige Person für dessen Betrieb benannt werden. **◀ ZITIERT**
  2. Die Zuständigen SOLLTEN ausreichend über den Umgang mit dem IoT-Gerät informiert werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme ASST.1.1.2 verlangt die allgemeine Zuweisung von Aufgaben und Verantwortlichkeiten an zuständige Rollen oder Personen für Assets, was die Benennung von Zuständigen für den Betrieb von IoT-Geräten als Spezialfall abdeckt.

### → APP.6.A1 — Planung des Software-Einsatzes (B) [Fachverantwortliche]
  1. Bevor eine Institution eine (neue) Software einführt, MUSS sie entscheiden, wofür die Software genutzt und welche Informationen damit verarbeitet werden sollen, wie die Benutzenden bei der Anforderungserhebung beteiligt und bei der Einführung unterstützt werden sollen, wie die Software an weitere Anwendungen und IT-Systeme über welche Schnittstellen angebunden wird, auf welchen IT-Systemen die Software ausgeführt werden soll und welche Ressourcen zur Ausführung der Software erforderlich sind, sowie ob sich die Institution in Abhängigkeit zu einem Hersteller oder einer Herstellerin begibt, wenn sie diese Software einsetzt.
  2. Hierbei MÜSSEN bereits Sicherheitsaspekte berücksichtigt werden.
  3. Zusätzlich MUSS die Institution die Zuständigkeiten für fachliche Betreuung, Freigabe und betriebliche Administration schon im Vorfeld klären und festlegen. **◀ ZITIERT**
  4. Die Zuständigkeiten MÜSSEN dokumentiert und bei Bedarf aktualisiert werden.
- **Satz 3** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die Maßnahme fordert als allgemeine Regelung die Zuweisung von Aufgaben und Verantwortlichkeiten an Personen oder Rollen, was die Festlegung der Zuständigkeiten für Betreuung, Freigabe und Administration abdeckt.


## ASST.4.2 — Vertraulichkeit und Integrität beim Transport  [44 Paare]

**Statement (normativ):** Informationen und Assets für Daten SOLLTE Vertraulichkeit und Integrität beim Transport verankern.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Transport meint hier sowohl die Datenübertragung per Netz als auch auf physischen Datenträgern (Sneakernet) oder den physischen Transport ganzer Systeme. Zur Umsetzung kann z.B. in Netzen die Transportverschlüsselung und -signierung von E-Mails, Ende-zu-Ende-Verschlüsselung mit PGP genutzt werden. Beim physischen Transport können die vorherige Verschlüsselung von Speichermedien, die Verwahrung von Assets an der Person, Verwahrungsprotokolle, manipulationssichere Verpackungen, Geolocation Tracking oder vertrauenswürdige Kuriere genutzt werden. Die Auswahl der Maßnahmen richtet sich nach dem Schutzbedarf der ausgetauschten Informationen und der Transportart.

### → APP.2.1.A20 — Absicherung der Replikation (H)
  1. Replikationen von vertraulichen Inhalten SOLLTEN zusätzlich zu einer Verschlüsselung auf Applikations- oder Transportebene durch z. B. IPsec gesichert werden. **◀ ZITIERT**
  2. Für die Authentisierung im Rahmen der Replikation SOLLTEN möglichst starke Authentisierungsverfahren verwendet werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) ASST.4.2 fordert allgemein die Absicherung von Vertraulichkeit und Integrität bei Datenübertragungen und deckt damit die Verschlüsselung vertraulicher Inhalte bei der Replikation ab.

### → APP.2.2.A8 — Absicherung des „Sicheren Kanals“ (S)
  1. Der „Sichere Kanal“ SOLLTE so konfiguriert sein, dass alle übertragenen Daten immer verschlüsselt und signiert werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die Maßnahme fordert die Sicherstellung von Vertraulichkeit und Integrität beim Datentransport (inkl. Transportverschlüsselung und Signierung), was die spezifische Absicherung des Übertragungskanals mittels Verschlüsselung und Signatur abdeckt.

### → APP.3.1.A11 — Sichere Anbindung von Hintergrundsystemen (S)
  1. Der Zugriff auf Hintergrundsysteme, auf denen Funktionen und Daten ausgelagert werden, SOLLTE ausschließlich über definierte Schnittstellen und von definierten IT-Systemen aus möglich sein.
  2. Bei der Kommunikation über Netz- und Standortgrenzen hinweg SOLLTE der Datenverkehr authentisiert und verschlüsselt werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die Maßnahme ASST.4.2 fordert die Sicherstellung von Vertraulichkeit und Integrität beim Datentransport (z. B. durch Transportverschlüsselung und Signaturen), was die geforderte Authentisierung und Verschlüsselung des Datenverkehrs über Netzgrenzen inhaltlich abdeckt.

### → APP.3.4.A15 — Verschlüsselung der Datenpakete unter Samba (H)
  1. Um die Sicherheit der Datenpakete auf dem Transportweg zu gewährleisten, SOLLTEN die Datenpakete mit den ab SMB Version 3 integrierten Verschlüsselungsverfahren verschlüsselt werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) ASST.4.2 fordert allgemein die Wahrung von Vertraulichkeit und Integrität bei der Datenübertragung im Netz (z. B. durch Transportverschlüsselung), was die konkrete Paketverschlüsselung via SMBv3 abdeckt.

### → CON.11.1.A10 — Elektronische Übertragung von VS nach §§ 24, 53, 55 und Nr. 6.2 Anlage V zur VSA (B)
  1. Falls VS elektronisch übertragen werden sollen, MÜSSEN die Regelungen der VSA zur Weitergabe von VS (§ 24 VSA) eingehalten werden.
  2. Für die Weitergabe an Parlamente, Landesbehörden und nicht öffentliche Stellen MÜSSEN zusätzlich die besonderen Regelungen nach §§ 25 und 26 VSA beachtet werden.
  3. Die VS-IT aller Kommunikationspartner MUSS für die Verarbeitung von VS des Geheimhaltungsgrads VS-NfD freigegeben sein.
  4. Werden VS elektronisch übertragen, MÜSSEN sie grundsätzlich durch ein IT-Sicherheitsprodukt mit Zulassungsaussage verschlüsselt werden. **◀ ZITIERT**
  5. Auf eine Verschlüsselung DARF NUR verzichtet werden, falls: VS ausschließlich leitungsgebunden übertragen werden und die Übertragungseinrichtungen, einschließlich Kabel und Verteiler, gegen unbefugten Zugriff geschützt sind, oder neben den Hausnetzen zusätzlich das Transportnetz für die Verarbeitung von VS freigegeben ist.
  6. Es DARF NUR innerhalb von Räumen und Bereichen, die gegen unkontrollierten Zutritt geschützt sind, von einem Zugriffsschutz ausgegangen werden.
  7. VS DÜRFEN NUR in Ausnahmefällen nach § 55 Abs. 2-4 VSA unter Einhaltung der dort genannten Anforderungen und Vorsichtsmaßnahmen auf anderem Wege elektronisch übertragen werden.
  8. Falls im Vorhinein zu erwarten ist, dass VS elektronisch übertragen werden könnten, DARF die Ausnahmeregelung nach § 55 VSA NICHT angewendet werden.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die G++-Maßnahme fordert allgemein die Wahrung von Vertraulichkeit beim Transport (u. a. durch Verschlüsselung), was die speziellere Vorgabe zur Verschlüsselung elektronisch übertragener VS abdeckt.

### → CON.11.1.A11 — Mitnahme elektronischer VS nach § 28 VSA und Nr. 7 Anlage V zur VSA (B)
  1. Elektronische VS DÜRFEN NUR auf Dienstreisen und zu Dienstbesprechungen mitgenommen werden, soweit dies dienstlich notwendig ist und sie angemessen gegen unbefugte Kenntnisnahme gesichert werden. **◀ ZITIERT**
  2. Werden diese persönlich mitgenommen, MÜSSEN diese folgendermaßen gespeichert werden: auf hierfür freigegebener VS-IT, auf einem Datenträger, der in einem verschlossenen Umschlag transportiert wird, auf einem Datenträger, der mit einem IT-Sicherheitsprodukt mit Zulassungsaussage verschlüsselt wurde, oder durch ein IT-Sicherheitsprodukt mit Zulassungsaussage verschlüsselt, falls der Datenträger selbst nicht durch ein IT-Sicherheitsprodukt mit Zulassungsaussage verschlüsselt wurde. **◀ ZITIERT**
  3. Falls VS des Geheimhaltungsgrades VS-NfD in Privatwohnungen verarbeitet werden sollen, dann DÜRFEN diese NUR elektronisch mit hierfür freigegebener VS-IT verarbeitet werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) ASST.4.2 fordert die Verankerung von Vertraulichkeit beim physischen Transport von Daten und deckt damit die Sicherung elektronischer VS gegen unbefugte Kenntnisnahme bei der Mitnahme auf Reisen ab.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme ASST.4.2 fordert allgemein die Wahrung von Vertraulichkeit und Integrität beim physischen Transport und deckt damit die konkreten VS-Vorgaben zur Verschlüsselung und sicheren Verwahrung von Datenträgern bei persönlicher Mitnahme ab.

### → CON.7.A10 — Verschlüsselung tragbarer IT-Systeme und Datenträger (B) [Benutzende, IT-Betrieb]
  1. Damit schützenswerte Informationen nicht durch unberechtigte Dritte eingesehen werden können, MÜSSEN Mitarbeitende vor Reiseantritt sicherstellen, dass alle schützenswerten Informationen entsprechend den internen Richtlinien abgesichert sind. **◀ ZITIERT**
  2. Mobile Datenträger und IT-Systeme SOLLTEN dabei vor Reiseantritt durch Benutzende oder den IT-Betrieb verschlüsselt werden.
  3. Die kryptografischen Schlüssel MÜSSEN getrennt vom verschlüsselten Gerät aufbewahrt werden.
  4. Bei der Verschlüsselung von Daten SOLLTEN die gesetzlichen Regelungen des Ziellandes beachtet werden.
  5. Insbesondere landesspezifische Gesetze zur Herausgabe von Passwörtern und zur Entschlüsselung von Daten SOLLTEN berücksichtigt werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) ASST.4.2 verlangt die Verankerung von Vertraulichkeit beim Transport (inklusive physischem Transport von Systemen/Datenträgern), was die Absicherung schützenswerter Informationen vor Reiseantritt materiell abdeckt.

### → CON.9.A8 — Verschlüsselung und digitale Signatur (S)
  1. Die Institution SOLLTE prüfen, ob Informationen während des Austausches kryptografisch gesichert werden können. **◀ ZITIERT**
  2. Falls die Informationen kryptografisch gesichert werden, SOLLTEN dafür ausreichend sichere Verfahren eingesetzt werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) ASST.4.2 verlangt die Verankerung von Vertraulichkeit und Integrität beim Informationstransport, was die Prüfung und Auswahl geeigneter kryptografischer Schutzmaßnahmen wie Transport- und Ende-zu-Ende-Verschlüsselung für den Datenaustausch einschließt.

### → DER.3.1.A11 — Kommunikation und Verhalten während der Prüfungen (S) [Auditteam]
  1. Das Auditteam bzw. Revisionsteam SOLLTE klare Regelungen dafür aufstellen, wie das Audit- bzw. Revisionsteam und die Mitarbeitenden der zu prüfenden Institution bzw. Abteilung miteinander Informationen austauschen.
  2. Das Auditteam SOLLTE durch geeignete Maßnahmen sicherstellen, dass die bei einem Audit ausgetauschten Informationen auch vertraulich und integer bleiben. **◀ ZITIERT**
  3. Personen, die das Audit begleiten, SOLLTEN NICHT die Prüfungen beeinflussen.
  4. Zudem SOLLTEN sie zur Vertraulichkeit verpflichtet werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) ASST.4.2 fordert die Sicherstellung von Vertraulichkeit und Integrität bei der Übertragung bzw. beim Austausch von Informationen und deckt damit die allgemeine Anforderung aus Satz 2 ab.

### → DER.3.2.A10 — Kommunikationsabsprache (S)
  1. Es SOLLTE klar geregelt werden, wie Informationen zwischen dem IS-Revisionsteam und der zu prüfenden Institution auszutauschen sind.
  2. So SOLLTE sichergestellt werden, dass diese Informationen vertraulich und integer bleiben. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die Maßnahme ASST.4.2 fordert explizit die Sicherstellung von Vertraulichkeit und Integrität bei der Informationsübertragung, was der Zielsetzung von Satz 2 entspricht.

### → IND.2.1.A17 — Nutzung sicherer Protokolle für die Übertragung von Mess- und Steuerdaten (S) [OT-Betrieb (Operational Technology, OT)]
  1. Mess- oder Steuerdaten SOLLTEN bei der Übertragung vor unberechtigten Zugriffen oder Veränderungen geschützt werden. **◀ ZITIERT**
  2. Bei Anwendungen mit Echtzeitanforderungen SOLLTE geprüft werden, ob dies umsetzbar ist.
  3. Werden Mess- oder Steuerdaten über öffentliche Netze übertragen, SOLLTEN sie angemessen geschützt werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme ASST.4.2 fordert allgemein die Wahrung von Vertraulichkeit und Integrität bei der Übertragung, was den Schutz vor unberechtigten Zugriffen und Veränderungen direkt abdeckt.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) ASST.4.2 fordert die Sicherstellung von Vertraulichkeit und Integrität bei der Übertragung von Daten über Netze und deckt damit den Schutz bei der Übertragung über öffentliche Netze ab.

### → IND.2.1.A2 — Nutzung sicherer Übertragungs-Protokolle für die Konfiguration und Wartung (B) [Wartungspersonal, OT-Betrieb (Operational Technology, OT)]
  1. Für die Konfiguration und Wartung von ICS-Komponenten MÜSSEN sichere Protokolle eingesetzt werden.
  2. Die Informationen MÜSSEN geschützt übertragen werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) ASST.4.2 fordert explizit den Schutz von Vertraulichkeit und Integrität bei der Datenübertragung und deckt damit die geschützte Übertragung von Informationen direkt ab.

### → IND.2.7.A8 — Sichere Übertragung von Engineering Daten auf SIS (S) [Planende, Wartungspersonal, ICS-Informationssicherheitsbeauftragte]
  1. Die Integrität der Engineering-Daten SOLLTE während der Übertragung auf SIS sichergestellt werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) ASST.4.2 fordert allgemein die Sicherstellung der Integrität bei der Datenübertragung und deckt damit die Übertragung von Engineering-Daten auf SIS inhaltlich ab.

### → INF.13.A21 — Protokollierung im TGM (S)
  1. Ereignisse, die im Ereignismanagement entsprechend klassifiziert wurden, SOLLTEN protokolliert werden.
  2. Außerdem SOLLTEN für die Systeme sicherheitsrelevante Ereignisse protokolliert werden.
  3. Alle Konfigurationszugriffe sowie alle manuellen und automatisierten Steuerungszugriffe SOLLTEN protokolliert werden.
  4. Abhängig vom Schutzbedarf SOLLTE eine vollumfängliche Protokollierung inklusive Metadaten und Inhalt der Änderungen erfolgen.
  5. Die Protokollierung SOLLTE auf einer zentralen Protokollierungsinstanz zusammengeführt werden.
  6. Protokollierungsdaten SOLLTEN NUR über sichere Kommunikationswege übertragen werden. **◀ ZITIERT**
  7. Bei sicherheitskritischen Ereignissen SOLLTE automatisch alarmiert werden.
- **Satz 6** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 6) ASST.4.2 fordert allgemein den Schutz von Vertraulichkeit und Integrität bei der Datenübertragung (Transport), was die Übertragung von Protokollierungsdaten über sichere Kommunikationswege inhaltlich abdeckt.

### → INF.14.A18 — Sichere Anbindung von GA-externen Systemen (S)
  1. Die Kommunikation von GA-Systemen mit GA-externen Systemen SOLLTE ausschließlich über definierte Schnittstellen und mit definierten IT-Systemen möglich sein.
  2. Die Kommunikation SOLLTE authentisiert und verschlüsselt werden. **◀ ZITIERT**
  3. Die möglichen Schnittstellen zu GA-externen Systemen SOLLTEN auf das notwendige Maß beschränkt werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) ASST.4.2 fordert die Sicherstellung von Vertraulichkeit und Integrität bei der Datenübertragung (u. a. durch Verschlüsselung und Signierung), womit die authentisierte und verschlüsselte Kommunikation materiell abgedeckt ist.

### → INF.14.A25 — Dediziertes Monitoring in der GA (S)
  1. Für alle Komponenten, die für die GA betriebsrelevant sind, SOLLTE ein geeignetes Monitoringkonzept erstellt und umgesetzt werden.
  2. Hierbei SOLLTEN die Verfügbarkeit sowie bedeutsame Parameter der GA-relevanten Komponenten laufend überwacht werden.
  3. Fehlerzustände sowie die Überschreitung definierter Grenzwerte SOLLTEN automatisch an die betreibende Organisation gemeldet werden.
  4. Es SOLLTEN durch die GA mindestens Alarme ausgelöst werden, wenn TGA-Anlagen ausfallen oder wichtige Funktionen zum automatisierten Steuern und Regeln nicht verfügbar sind.
  5. Zudem SOLLTE festgelegt werden, für welche besonders sicherheitsrelevanten Ereignisse und für welche weiteren Ereignisse automatische Alarmmeldungen generiert werden.
  6. Statusmeldungen und Monitoringdaten SOLLTEN NUR über sichere Kommunikationswege übertragen werden. **◀ ZITIERT**
- **Satz 6** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 6) ASST.4.2 fordert allgemein die Absicherung von Datenübertragungen hinsichtlich Vertraulichkeit und Integrität, was die Übertragung von Status- und Monitoringdaten über sichere Kommunikationswege abdeckt.

### → INF.14.A26 — Protokollierung in der GA (S)
  1. Ergänzend zum Baustein OPS.1.1.5 Protokollierung SOLLTEN Statusänderungen an GA-relevanten Komponenten und sicherheitsrelevante Ereignisse protokolliert werden.
  2. Zusätzlich SOLLTEN alle schreibenden Konfigurationszugriffe auf TGA-Anlagen und gegebenenfalls GA-relevante Komponenten sowie alle manuellen und automatisierten Änderungen der Zustände von diesen protokolliert werden.
  3. Es SOLLTE festgelegt werden, welche Protokollierungsdaten auf einer zentralen Protokollierungsinstanz zusammengeführt werden.
  4. Protokollierungsdaten SOLLTEN NUR über sichere Kommunikationswege übertragen werden. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) ASST.4.2 fordert allgemein die Absicherung von Vertraulichkeit und Integrität bei der Datenübertragung, was die sichere Übertragung von Protokollierungsdaten über geschützte Kommunikationswege abdeckt.

### → INF.8.A2 — Transport von Arbeitsmaterial zum häuslichen Arbeitsplatz (B)
  1. Es MUSS geregelt werden, welche Datenträger und Unterlagen am häuslichen Arbeitsplatz bearbeitet und zwischen der Institution und dem häuslichen Arbeitsplatz hin und her transportiert werden dürfen.
  2. Generell MÜSSEN Datenträger und andere Unterlagen sicher transportiert werden. **◀ ZITIERT**
  3. Diese Regelungen MÜSSEN den Mitarbeitenden in geeigneter Weise bekanntgegeben werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) ASST.4.2 verlangt die Sicherstellung von Vertraulichkeit und Integrität beim physischen und digitalen Transport von Daten und Datenträgern und deckt die Forderung nach sicherem Transport damit inhaltlich ab.

### → NET.1.1.A7 — Absicherung von schützenswerten Informationen (B)
  1. Schützenswerte Informationen MÜSSEN über nach dem derzeitigen Stand der Technik sichere Protokolle übertragen werden, falls nicht über vertrauenswürdige dedizierte Netzsegmente (z. B. innerhalb des Managementnetzes) kommuniziert wird. **◀ ZITIERT**
  2. Können solche Protokolle nicht genutzt werden, MUSS nach Stand der Technik angemessen verschlüsselt und authentisiert werden (siehe NET.3.3 VPN). **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) Die G++-Maßnahme fordert die Gewährleistung von Vertraulichkeit und Integrität beim Datentransport (einschließlich Netzübertragung) und deckt damit die sichere Übertragung schützenswerter Daten als allgemeinere Pflicht inhaltlich ab.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) ASST.4.2 verlangt die Gewährleistung von Vertraulichkeit und Integrität bei der Übertragung, was die geforderte Verschlüsselung und Authentisierung schützenswerter Daten beim Transport abdeckt.

### → NET.2.2.A3 — Absicherung der WLAN-Nutzung an Hotspots (B) [IT-Betrieb]
  1. Dürfen Hotspots genutzt werden, MUSS Folgendes umgesetzt werden: Jede(r) Benutzende eines Hotspots MUSS seine oder ihre Sicherheitsanforderungen kennen und danach entscheiden, ob und unter welchen Bedingungen ihm oder ihr die Nutzung des Hotspots erlaubt ist.
  2. Werden Hotspots genutzt, dann SOLLTE sichergestellt werden, dass die Verbindung zwischen Hotspot-Access Point und IT-Systemen der Benutzenden nach dem Stand der Technik kryptografisch abgesichert wird.
  3. WLANs, die nur sporadisch genutzt werden, SOLLTEN von den Benutzenden aus der Historie gelöscht werden.
  4. Die automatische Anmeldung an WLANs SOLLTE deaktiviert werden.
  5. Wenn möglich, SOLLTEN separate Konten mit einer sicheren Grundkonfiguration und restriktiven Berechtigungen verwendet werden.
  6. Es SOLLTE sichergestellt sein, dass sich keine Benutzenden mit administrativen Berechtigungen von ihren Clients aus an externen WLANs anmelden können.
  7. Sensible Daten DÜRFEN NUR übertragen werden, wenn allen notwendigen Sicherheitsmaßnahmen auf den Clients, vor allem eine geeignete Verschlüsselung, aktiviert sind. **◀ ZITIERT**
  8. Wird die WLAN-Schnittstelle über einen längeren Zeitraum nicht genutzt, MUSS diese deaktiviert werden.
  9. Über öffentlich zugängliche WLANs DÜRFEN die Benutzenden NUR über ein Virtual Private Network (VPN) auf interne Ressourcen der Institution zugreifen.
- **Satz 7** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 7) ASST.4.2 fordert allgemein die Absicherung von Vertraulichkeit und Integrität bei der Datenübertragung (insbesondere durch Verschlüsselung), was die Bedingung in Satz 7 zur geschützten Übertragung sensibler Daten inhaltlich abdeckt.

### → NET.3.2.A23 — Systemüberwachung und -Auswertung (S)
  1. Firewalls SOLLTEN in ein geeignetes Systemüberwachungs- bzw. Monitoringkonzept eingebunden werden.
  2. Es SOLLTE ständig überwacht werden, ob die Firewall selbst sowie die darauf betriebenen Dienste korrekt funktionieren.
  3. Bei Fehlern oder wenn Grenzwerte überschritten werden, SOLLTE das Betriebspersonal alarmiert werden.
  4. Zudem SOLLTEN automatische Alarmmeldungen generiert werden, die bei festgelegten Ereignissen ausgelöst werden.
  5. Protokolldaten oder Statusmeldungen SOLLTEN NUR über sichere Kommunikationswege übertragen werden. **◀ ZITIERT**
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) ASST.4.2 verlangt den Schutz von Daten (Vertraulichkeit und Integrität) bei der Übertragung über Netze, was die sichere Übertragung von Protokoll- und Statusdaten als allgemeinen Fall vollständig abdeckt.

### → NET.3.4.A16 — Protokollierung der Ereignisse (S)
  1. Ergänzend zu OPS.1.1.5 Protokollierung SOLLTEN Statusänderungen an NAC-Komponenten sowie alle relevanten NAC-spezifischen, gegebenenfalls sicherheitskritischen Ereignisse protokolliert werden.
  2. Zusätzlich SOLLTEN alle schreibenden Konfigurationszugriffe auf die zentralen NAC-Komponenten protokolliert werden.
  3. Es SOLLTE festgelegt werden, welche Protokollierungsdaten mit welchen Details erfasst und welche Daten auf einer zentralen Protokollierungsinstanz zusammengeführt werden.
  4. Protokollierungsdaten SOLLTEN NUR über sichere Kommunikationswege übertragen werden. **◀ ZITIERT**
  5. Sicherheitskritische Ereignisse wie RADIUS-down oder eine ungewöhnliche Anzahl von RADIUS-Anfragen SOLLTEN zu einem automatischen Alarm führen.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die G++-Maßnahme fordert allgemein die Wahrung von Vertraulichkeit und Integrität beim Datentransport (z. B. via Transportverschlüsselung), was die Übertragung von Protokolldaten über sichere Kommunikationswege inhaltlich abdeckt.

### → NET.3.4.A20 — Einsatz von MACsec (H)
  1. Für jedes Datenpaket SOLLTE die Datenintegrität gewährleistet werden. **◀ ZITIERT**
  2. Darüber hinaus SOLLTE erwogen werden, diese Daten zu verschlüsseln. **◀ ZITIERT**
  3. Hierfür SOLLTE MACsec gemäß IEEE 802.1AE genutzt werden.
  4. Access-Switches und Endgeräte, die MACsec nicht unterstützen oder für die MACsec nicht eingerichtet werden soll, SOLLTEN erfasst werden.
  5. Für diese SOLLTE regelmäßig überprüft werden, ob die Ausschlussgründe noch gelten.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) ASST.4.2 fordert allgemein die Gewährleistung von Vertraulichkeit und Integrität beim Datentransport (inklusive Datenübertragung per Netz), was den Schutz der Datenintegrität von Datenpaketen abdeckt.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme fordert allgemein die Gewährleistung der Vertraulichkeit beim Datentransport, was das Erwägen und Einsetzen von Verschlüsselung für übertragene Daten umfasst.

### → NET.4.2.A8 — Verschlüsselung von VoIP (S)
  1. Es SOLLTE entschieden werden, ob und welche Sprach- und Signalisierungsinformationen verschlüsselt werden sollen.
  2. Generell SOLLTEN alle VoIP-Datenpakete, die das gesicherte LAN verlassen, durch geeignete Sicherheitsmechanismen geschützt werden. **◀ ZITIERT**
  3. Die Benutzenden SOLLTEN über die Nutzung der VoIP-Verschlüsselung informiert werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) ASST.4.2 deckt als übergeordnete Anforderung den Schutz von Daten (Vertraulichkeit und Integrität) bei der Übertragung über Netze ab, worunter auch VoIP-Datenpakete beim Verlassen des gesicherten LANs fallen.

### → OPS.1.1.1.A9 — Durchführung von IT-Monitoring (S)
  1. Alle IT-Komponenten SOLLTEN in ein einheitliches IT-Monitoring eingebunden werden, das alle relevanten Parameter der IT-Komponenten beinhaltet.
  2. Das IT-Monitoring SOLLTE mit dem übergeordneten Service-Management abgestimmt werden.
  3. Der IT-Betrieb SOLLTE das IT-Monitoring entsprechend eines vorher festgelegten Monitoring-Plans durchführen.
  4. Je IT-Komponente SOLLTEN angemessene Schwellwerte ermittelt werden, die eine Meldung oder einen Alarm auslösen.
  5. Der IT-Betrieb SOLLTE für das IT-Monitoring spezifizieren, welche Meldewege genutzt werden und welche Konsequenzen aus den Meldungen oder Alarmen gezogen werden.
  6. Auf Basis von Monitoring-Ergebnissen SOLLTE überprüft werden, ob die Infrastruktur erweitert oder angepasst wird.
  7. Über die gewonnenen Erkenntnisse SOLLTEN regelmäßig Reports erstellt werden, die das aktuelle Lagebild der betriebenen IT und die zeitliche Entwicklung sowie Trends darstellen.
  8. Die Konzeption des IT-Monitorings SOLLTE regelmäßig und anlassbezogen geprüft und aktualisiert werden, um dem aktuellen Stand der Technik und der betriebenen Infrastruktur zu entsprechen.
  9. Die Monitoring-Daten SOLLTEN nur über sichere Kommunikationswege übertragen werden. **◀ ZITIERT**
- **Satz 9** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 9) Die G++-Maßnahme ASST.4.2 fordert allgemein die Absicherung von Vertraulichkeit und Integrität bei der Datenübertragung, was die sichere Übertragung von Monitoring-Daten inhaltlich abdeckt.

### → OPS.1.1.7.A19 — Absicherung der Systemmanagement-Kommunikation zwischen der Systemmanagement-Lösung und den zu verwaltenden Systemen (S)
  1. Die Systemmanagement-Kommunikation zwischen der Systemmanagement-Lösung und den zu verwaltenden Systemen SOLLTE grundsätzlich verschlüsselt sein. **◀ ZITIERT**
  2. Die Stärke der verwendeten kryptografischen Verfahren und Schlüssel SOLLTE regelmäßig überprüft und bei Bedarf angepasst werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) ASST.4.2 fordert allgemein die Wahrung der Vertraulichkeit und Integrität bei der Datenübertragung (u. a. durch Transportverschlüsselung) und deckt damit die Verschlüsselung der Systemmanagement-Kommunikation als Spezialfall ab.

### → SYS.1.8.A23 — Einsatz von Verschlüsselung für Speicherlösungen (H)
  1. Alle in Speicherlösungen abgelegten Daten SOLLTEN verschlüsselt werden.
  2. Es SOLLTE festgelegt werden, auf welchen Ebenen (Data-in-Motion und Data-at-Rest) verschlüsselt wird.
  3. Dabei SOLLTE beachtet werden, dass die Verschlüsselung auf dem Transportweg auch bei Replikationen und Backup-Traffic relevant ist. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die Maßnahme ASST.4.2 fordert allgemein den Schutz von Vertraulichkeit und Integrität beim Transport (u. a. durch Transportverschlüsselung im Netz), was die Absicherung von Replikations- und Backup-Verkehr auf dem Transportweg abdeckt.

### → SYS.1.8.A24 — Sicherstellung der Integrität der SAN-Fabric (H)
  1. Um die Integrität der SAN-Fabric sicherzustellen, SOLLTEN Protokolle mit zusätzlichen Sicherheitsmerkmalen eingesetzt werden. **◀ ZITIERT**
  2. Bei den folgenden Protokollen SOLLTEN deren Sicherheitseigenschaften berücksichtigt und entsprechende Konfigurationen verwendet werden: Diffie Hellman Challenge Handshake Authentication Protocol (DH-CHAP), Fibre Channel Authentication Protocol (FCAP) und Fibre Channel Password Authentication Protocol (FCPAP).
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme ASST.4.2 fordert die Sicherstellung der Integrität bei der Datenübertragung über Netze, was den Einsatz von Protokollen mit Sicherheitsmerkmalen in der SAN-Fabric als technischem Spezialfall abstrahierend abdeckt.

### → SYS.3.3.A10 — Sichere Datenübertragung über Mobiltelefone (S) [Benutzende]
  1. Es SOLLTE geregelt sein, welche Daten über Mobiltelefone übertragen werden dürfen.
  2. Die dafür erlaubten Schnittstellen SOLLTEN festgelegt werden.
  3. Außerdem SOLLTE beschlossen werden, wie die Daten bei Bedarf zu verschlüsseln sind. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) ASST.4.2 verlangt Maßnahmen zur Sicherstellung von Vertraulichkeit beim Datentransport, was die Festlegung von Verschlüsselungsverfahren für die Datenübertragung einschließt.

### → SYS.4.1.A15 — Verschlüsselung von Informationen bei Druckern, Kopierern und Multifunktionsgeräten (S)
  1. Wenn möglich, SOLLTEN alle auf geräteinternen, nichtflüchtigen Speichermedien abgelegten Informationen verschlüsselt werden.
  2. Auch Druckaufträge SOLLTEN möglichst verschlüsselt übertragen werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) ASST.4.2 fordert allgemein die Wahrung der Vertraulichkeit bei der Datenübertragung (Transportverschlüsselung), was die verschlüsselte Übertragung von Druckaufträgen als Spezialfall umfasst.

### → SYS.4.4.A11 — Verwendung von verschlüsselter Datenübertragung (S)
  1. IoT-Geräte SOLLTEN Daten nur verschlüsselt übertragen. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme ASST.4.2 fordert allgemein den Schutz der Vertraulichkeit bei der Datenübertragung durch Transportverschlüsselung und deckt die Pflicht zur verschlüsselten Übertragung durch IoT-Geräte damit inhaltlich ab.

### → SYS.4.5.A10 — Datenträgerverschlüsselung (B)
  1. Wenn Wechseldatenträger außerhalb eines sicheren Bereiches verwendet oder transportiert werden und dabei schutzbedürftige Daten enthalten, MÜSSEN die Daten mit einem sicheren Verfahren verschlüsselt werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) ASST.4.2 verlangt den Schutz von Vertraulichkeit beim physischen Transport von Daten und Speichermedien entsprechend deren Schutzbedarf, was die Verschlüsselung schutzbedürftiger Wechseldatenträger abdeckt.

### → SYS.4.5.A14 — Sichere Versandart und Verpackung (H)
  1. Die Institution SOLLTE überprüfen, wie vertrauliche Informationen bei einem Versand angemessen geschützt werden können. **◀ ZITIERT**
  2. Es SOLLTE eine sichere Versandverpackung für Wechseldatenträger verwendet werden, bei der Manipulationen sofort zu erkennen sind. **◀ ZITIERT**
  3. Die Institution SOLLTE alle Beteiligten auf notwendige Versand- und Verpackungsarten hinweisen.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) ASST.4.2 fordert die Verankerung von Vertraulichkeit und Integrität beim Datentransport (inklusive physischer Datenträger) anhand des Schutzbedarfs, was die Überprüfung angemessener Schutzmaßnahmen für den Versand vertraulicher Informationen umfasst.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) ASST.4.2 fordert die Sicherung von Vertraulichkeit und Integrität beim physischen Datentransport und umfasst explizit manipulationssichere Verpackungen für Speichermedien.

### → SYS.4.5.A5 — Regelung zur Mitnahme von Wechseldatenträgern (S)
  1. Es SOLLTE klare schriftliche Regeln dazu geben, ob, wie und zu welchen Anlässen Wechseldatenträger mitgenommen werden dürfen.
  2. Insbesondere SOLLTE festgelegt sein, welche Wechseldatenträger von wem außer Haus transportiert werden dürfen und welche Sicherheitsmaßnahmen dabei zu beachten sind. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) ASST.4.2 fordert Maßnahmen zur Wahrung von Vertraulichkeit und Integrität beim Transport, was den physischen Transport von Datenträgern und die dabei zu beachtenden Sicherheitsmaßnahmen direkt umfasst.

### → CON.9.A2 — Regelung des Informationsaustausches (B)
  1. Bevor Informationen ausgetauscht werden, MUSS die Institution festlegen, wie schutzbedürftig die Informationen sind.
  2. Sie MUSS festlegen, wie die Informationen bei der Übertragung zu schützen sind. **◀ ZITIERT**
  3. Falls schutzbedürftige Daten übermittelt werden, MUSS die Institution die Empfangenden darüber informieren, wie schutzbedürftig die Informationen sind.
  4. Falls die Informationen schutzbedürftig sind, MUSS die Institution die Empfangenden darauf hingewiesen werden, dass diese die Daten ausschließlich zu dem Zweck nutzen dürfen, zu dem sie übermittelt wurden.
- **Satz 2** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) ASST.4.2 verlangt ausdrücklich, Vertraulichkeit und Integrität bei der Datenübertragung bzw. beim Transport schutzbedarfsadäquat zu verankern, was die Festlegung von Schutzmaßnahmen bei der Übertragung abdeckt.

### → APP.1.1.A15 — Einsatz von Verschlüsselung und Digitalen Signaturen (H)
  1. Daten mit erhöhtem Schutzbedarf SOLLTEN nur verschlüsselt gespeichert bzw. übertragen werden. **◀ ZITIERT**
  2. Bevor ein in ein Office-Produkt integriertes Verschlüsselungsverfahren genutzt wird, SOLLTE geprüft werden, ob es einen ausreichenden Schutz bietet.
  3. Zusätzlich SOLLTE ein Verfahren eingesetzt werden, mit dem Makros und Dokumente digital signiert werden können.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) ASST.4.2 fordert den Schutz der Vertraulichkeit beim Transport von Daten gemäß deren Schutzbedarf, was den Aspekt der verschlüsselten Datenübertragung aus Satz 1 materiell abdeckt.

### → CON.7.A16 — Integritätsschutz durch Check-Summen oder digitale Signaturen (H) [Benutzende]
  1. Benutzende SOLLTEN Check-Summen im Rahmen der Datenübertragung und Datensicherung verwenden, um die Integrität der Daten überprüfen zu können. **◀ ZITIERT**
  2. Besser noch SOLLTEN digitale Signaturen verwendet werden, um die Integrität von schützenswerten Informationen zu bewahren.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) ASST.4.2 fordert allgemein die Sicherstellung der Integrität bei der Datenübertragung, was die Verwendung von Integritätsprüfmechanismen wie Prüfsummen beim Transport abdeckt.

### → INF.10.A6 — Einrichtung sicherer Netzzugänge (S) [IT-Betrieb]
  1. Es SOLLTE sichergestellt werden, dass mitgebrachte IT-Systeme nicht über das Datennetz mit internen IT-Systemen der Institution verbunden werden können.
  2. Auf das LAN der Institution SOLLTEN ausschließlich dafür vorgesehene IT-Systeme zugreifen können.
  3. Ein Datennetz für externe Personen SOLLTE vom LAN der Institution getrennt werden.
  4. Netzzugänge SOLLTEN so eingerichtet sein, dass verhindert wird, dass Dritte den internen Datenaustausch mitlesen können. **◀ ZITIERT**
  5. Netzanschlüsse in Besprechungs-, Veranstaltungs- oder Schulungsräumen SOLLTEN abgesichert werden.
  6. Es SOLLTE verhindert werden, dass IT-Systeme in Besprechungs-, Veranstaltungs- und Schulungsräumen gleichzeitig eine Verbindung zum Intranet und zum Internet aufbauen können.
  7. Außerdem SOLLTE die Stromversorgung aus einer Unterverteilung heraus getrennt von anderen Räumen aufgebaut werden.
- **Satz 4** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die G++-Maßnahme ASST.4.2 fordert die Wahrung der Vertraulichkeit bei der Datenübertragung im Netz und deckt damit als allgemeinere Regelung das Verhindern des Mitlesens interner Datenverkehre durch Dritte ab.

### → SYS.4.5.A11 — Integritätsschutz durch Checksummen oder digitale Signaturen (H)
  1. Es SOLLTE ein Verfahren zum Schutz gegen zufällige oder vorsätzliche Veränderungen eingesetzt werden, mit dem die Integrität von vertraulichen Informationen sichergestellt wird. **◀ ZITIERT**
  2. Die Verfahren zum Schutz vor Veränderungen SOLLTEN dem aktuellen Stand der Technik entsprechen.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme fordert die Verankerung von Integritätsschutz beim Informationstransport (z. B. durch digitale Signaturen) und deckt damit die Forderung nach einem Verfahren zur Sicherstellung der Integrität vertraulicher Daten inhaltlich ab.


## ASST.7.7 — Beschriftungen entfernen  [1 Paare]

**Statement (normativ):** Informationen und Assets SOLLTE alle der Institution zuzuordnenden Beschriftungen vor der Veräußerung von Assets löschen.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Die „Beschriftung“ eines Assets ist jede physische oder digitale Kennzeichnung, die eine eindeutige Zuordnung des Gegenstands oder Datenträgers zu Werten der Institution ermöglicht. Darunter fallen unter anderem Eigentumskennzeichnungen (engl. asset tags), Seriennummern, Barcodes, Gravuren, Aufkleber mit Logo, aber auch digitale Metadaten wie Gerätebezeichnungen, E-Mail-Konten, Hostnamen oder eingebettete Wasserzeichen. Das Löschen dieser Beschriftungen vor der Veräußerung stellt sicher, dass Dritte nicht unmittelbar auf den ursprünglichen Eigentümer schließen oder unautorisierte Rückschlüsse auf interne Strukturen, Sicherheitsarchitekturen oder Verantwortlichkeiten ziehen. Ohne diese Bereinigung könnte ein weiterveräußertes Gerät durch verbleibende Markierungen auf die Institution hinweisen und so gezielt für Social-Engineering-Angriffe oder Reputationsschäden genutzt werden. Eine solche Zuordnung könnte zudem dazu führen, dass vertrauliche Informationen über Inventar, Sicherheitsstandards oder IT-Bestände unbeabsichtigt offengelegt werden. Zudem könnte eine verbleibende Beschriftung zu Missverständnissen über Eigentumsverhältnisse oder Haftung führen, falls das Asset in einen Vorfall verwickelt wird. Konkret können unter den zu entfernenden Beschriftungen beispielsweise Eigentumsaufkleber mit der Inventarnummer, Etiketten mit Standort- oder Abteilungsbezeichnungen, Markierungen für interne Verwendungszwecke (z.B. "Testgerät", "intern"), aber auch digital eingebettete Informationen wie institutionelle Metadaten in Office-Dokumenten oder gespeicherte WLAN-Profile auf mobilen Geräten verstanden werden. Auch optische Hinweise wie eingravierte Logos auf Gehäusen oder institutionelle Startbildschirme bei Laptops können darunterfallen. Zur Umsetzung kann es hilfreich sein, vor der Veräußerung eine Sichtprüfung durchzuführen und standardisierte Checklisten zu nutzen, um typische Beschriftungen systematisch zu identifizieren. Je nach Beschaffenheit des Assets kann der Einsatz von Reinigungsmitteln, Etikettenentfernern oder speziellen Werkzeugen in Betracht gezogen werden. Auch softwaregestützte Verfahren, etwa das Zurücksetzen auf Werkseinstellungen und das Prüfen auf verbleibende Metadaten, sind relevant. Nicht zuletzt kann die Einbindung von ISB oder des Datenschutzbeauftragten in Zweifelsfällen Klarheit darüber schaffen, ob eine bestimmte Kennzeichnung potenziell sicherheitsrelevant ist.

### → NET.4.2.A12 — Sichere Außerbetriebnahme von VoIP-Komponenten (S)
  1. Wenn VoIP-Komponenten außer Betrieb genommen oder ersetzt werden, SOLLTEN alle sicherheitsrelevanten Informationen von den Geräten gelöscht werden.
  2. Nach dem Löschvorgang SOLLTE überprüft werden, ob die Daten auch tatsächlich erfolgreich entfernt wurden.
  3. Vertrauliche Informationen SOLLTEN auch von Backup-Medien gelöscht werden.
  4. Alle Beschriftungen, insbesondere der Endgeräte, SOLLTEN vor der Entsorgung entfernt werden. **◀ ZITIERT**
  5. Es SOLLTE frühzeitig mit Herstellenden, Vertreibenden beziehungsweise Service-Unternehmen geklärt werden, welche Maßnahmen zur Löschung sicherheitsrelevanter Informationen mit den Vertrags- und Garantiebedingungen vereinbar sind.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 4) Die G++-Maßnahme ASST.7.7 fordert explizit das Entfernen aller der Institution zuzuordnenden Beschriftungen und Kennzeichnungen von Assets vor deren Veräußerung oder Entsorgung.


## ASST.3.12 — Autorisierung von Personen oder Institutionen  [16 Paare]

**Statement (normativ):** Informationen und Assets für Daten SOLLTE den Zugriff von Personen oder Institutionen im Einklang mit den zugehörigen Anforderungen zum Identitäts- und Berechtigungsmanagement autorisieren.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Ziel dieser Regelung ist es, sicherzustellen, dass nur berechtigte Stellen auf sensible Werte zugreifen, wodurch unautorisierte Einsichtnahme, Manipulation oder Missbrauch verhindert werden kann. Ohne eine klare Kopplung an Identitäts- und Berechtigungsmanagement könnte es zu unkontrollierten Datenabflüssen, Einsicht durch Dritte oder langfristigen Abhängigkeiten von bestimmten Dienstleistern kommen, die den Zugriff einseitig steuern könnten. Eine korrekte Umsetzung kann hingegen Transparenz schaffen und den Zugriff auf Informationen nachvollziehbar, reversibel und sicher gestalten. Umfasst sowohl die Autorisierung eigenen Personals, als auch die Autorisierung externer Dienstleister oder Partner. Die Formulierung "im Einklang mit den zugehörigen Anforderungen zum Identitäts- und Berechtigungsmanagement" bedeutet, dass die Autorisierung so erfolgt, wie in der Praktik Berechtigung (BER) festgelegt.

### → APP.2.1.A13 — Absicherung der Kommunikation mit Verzeichnisdiensten (S)
  1. Werden vertrauliche Informationen übertragen, SOLLTE die gesamte Kommunikation mit dem Verzeichnisdienst über ein sicheres Protokoll entsprechend der Technischen Richtlinie TR-02102 des BSI (z. B. TLS) verschlüsselt werden.
  2. Der Datenaustausch zwischen Client und Verzeichnisdienst-Server SOLLTE abgesichert werden.
  3. Es SOLLTE definiert werden, auf welche Daten zugegriffen werden darf. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme ASST.3.12 verlangt die Autorisierung des Zugriffs von Personen oder Institutionen auf Daten und deckt damit die Definition zulässiger Datenzugriffe allgemein ab.

### → APP.4.2.A22 — Schutz des Spools im SAP-ERP-System (S) [Entwickelnde]
  1. Es SOLLTE sichergestellt sein, dass auf Daten der sequenziellen Datenverarbeitung wie Spool oder Druck nur eingeschränkt zugegriffen werden kann.
  2. Auch SOLLTE verhindert werden, dass unberechtigte Konten auf die vom SAP-Spoolsystem benutzte Datenablage TemSe zugreifen können. **◀ ZITIERT**
  3. Die hierfür vergebenen Berechtigungen SOLLTEN regelmäßig überprüft werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme ASST.3.12 fordert die Autorisierung des Zugriffs auf Daten im Rahmen des Berechtigungsmanagements und deckt damit die Verhinderung unberechtigter Zugriffe auf Datenablagen wie TemSe als allgemeingültige Pflicht ab.

### → CON.11.1.A14 — Zugangs- und Zugriffsschutz nach § 3 VSA (B)
  1. VS-IT, die für VS-NfD eingestufte VS eingesetzt wird, MUSS so geschützt werden, dass ein Zugang zur VS-IT und ein Zugriff auf VS nur für verpflichtete Personen (siehe CON.11.1.A5 Verpflichtung bei Zugang zu VS nach § 4 und Anlage V zur VSA) möglich ist. **◀ ZITIERT**
  2. Der Schutz der VS MUSS sichergestellt werden über: IT-Sicherheitsprodukte mit Zulassungsaussage, materielle, organisatorische oder personelle Maßnahmen.
  3. Für den Zugangs- und Zugriffsschutz SOLLTE eine Mehr-Faktor-Authentisierung genutzt werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme ASST.3.12 deckt die Forderung ab, da sie allgemein die Autorisierung des Zugriffs von Personen auf Daten und Assets im Rahmen des Berechtigungsmanagements verlangt.

### → DER.3.1.A27 — Aufbewahrung und Archivierung von Unterlagen zu Audits und Revisionen (S)
  1. Die Institution SOLLTE Auditprogramme sowie Unterlagen zu Audits und Revisionen entsprechend den regulatorischen Anforderungen nachvollziehbar und revisionssicher ablegen und aufbewahren.
  2. Dabei SOLLTE sichergestellt werden, dass lediglich berechtigte Personen auf Auditprogramme und Unterlagen zugreifen können. **◀ ZITIERT**
  3. Die Institution SOLLTE die Auditprogramme und Unterlagen nach Ablauf der Aufbewahrungsfrist sicher vernichten.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) ASST.3.12 verlangt die Autorisierung des Zugriffs von Personen auf Daten im Rahmen des Berechtigungsmanagements, was die Beschränkung des Zugriffs auf Auditunterlagen auf berechtigte Personen allgemeingültig abdeckt.

### → DER.3.2.A8 — Aufbewahrung von IS-Revisionsberichten (B)
  1. Die Institution MUSS den IS-Revisionsbericht und die diesem zugrundeliegenden Referenzdokumente mindestens für zehn Jahre ab Zustellung des Berichts sicher aufbewahren, sofern keine anders lautenden Gesetze oder Verordnungen gelten.
  2. Die Institution MUSS sicherstellen, dass lediglich berechtigte Personen auf die IS-Revisionsberichte und die Referenzdokumente zugreifen können. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme fordert allgemein die Autorisierung des Zugriffs von Personen auf Daten und deckt damit die gezielte Zugriffsbeschränkung auf Revisionsberichte und Dokumente inhaltlich ab.

### → INF.13.A2 — Regelung und Dokumentation von Verantwortlichkeiten und Zuständigkeiten im Gebäude (B) [Institutionsleitung, Planende]
  1. Da es in einem Gebäude meist unterschiedliche Verantwortlichkeiten und Zuständigkeiten für verschiedene Bereiche gibt, MÜSSEN die entsprechenden Rechte, Pflichten, Aufgaben, Kompetenzen und zugehörigen Prozesse geregelt und dokumentiert werden.
  2. Hierbei MÜSSEN auch die organisatorischen Strukturen im Gebäude berücksichtigt und dokumentiert werden.
  3. Insbesondere MÜSSEN alle Nachfrage- und betreibenden Organisationen erfasst werden.
  4. Wird das TGM durch eine externe Organisation betrieben, MÜSSEN die zugehörigen Rechte, Pflichten, Aufgaben und Kompetenzen gemäß Baustein OPS.2.3 Nutzung von Outsourcing vertraglich festgehalten werden.
  5. Weiterhin MÜSSEN die Schnittstellen und Meldewege inklusive Eskalation zwischen allen Beteiligten festgelegt und dokumentiert werden.
  6. Auch die Koordination verschiedener betreibender Organisationen MUSS geregelt und dokumentiert werden.
  7. Der Zugriff auf die Dokumentation MUSS geregelt werden. **◀ ZITIERT**
  8. Die gesamte Dokumentation inklusive der zugehörigen Kontaktinformationen MUSS immer aktuell und verfügbar sein.
- **Satz 7** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 7) Die Maßnahme ASST.3.12 fordert die Autorisierung des Zugriffs von Personen auf Daten und deckt damit die Regelung des Zugriffs auf die Dokumentation inhaltlich ab.

### → SYS.1.7.A26 — WorkLoad Management für z/OS-Systeme (S)
  1. Die Programme, Dateien und Kommandos des WorkLoad Managers (WLM) sowie die dafür notwendigen Couple Data Sets SOLLTEN mittels RACF geschützt werden. **◀ ZITIERT**
  2. Dabei SOLLTE sichergestellt sein, dass die Berechtigungen zum Ändern des WLM über z/OS-Kommandos und über die SDSF-Schnittstelle gleich sind.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme ASST.3.12 fordert allgemein die Autorisierung des Zugriffs auf Daten und Assets über das Berechtigungsmanagement, was den spezifischen Schutz von WLM-Ressourcen mittels RACF umfasst.

### → SYS.1.7.A30 — Absicherung der z/OS-Trace-Funktionen (S)
  1. Die Trace-Funktionen von z/OS wie GTF (Generalized Trace Facility), NetView oder ACF/TAP (Advanced Communication Function/Trace Analysis Program) und die entsprechenden Dateien SOLLTEN so geschützt werden, dass nur die zuständigen und autorisierten Mitarbeitenden darauf Zugriff haben. **◀ ZITIERT**
  2. Die Trace-Funktion von NetView SOLLTE deaktiviert sein und nur im Bedarfsfall aktiviert werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme ASST.3.12 deckt als allgemeine Vorgabe zur Zugriffsberechtigung auf Daten und Assets die im Satz geforderte Zugriffsbeschränkung auf Trace-Dateien und -Funktionen für ausschließlich autorisierte Personen inhaltlich ab.

### → SYS.3.2.1.A1 — Festlegung einer Richtlinie für den Einsatz von Smartphones und Tablets (B)
  1. Bevor eine Institution Smartphones oder Tablets bereitstellt, betreibt oder einsetzt, MUSS eine generelle Richtlinie für die Nutzung und Kontrolle der Geräte festgelegt werden.
  2. Hierbei MUSS unter anderem festgelegt werden, wer mit Smartphones auf welche Informationen der Institution zugreifen darf. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) ASST.3.12 fordert die Autorisierung des Zugriffs von Personen auf Daten und deckt damit die allgemeine Pflicht ab, festzulegen, wer auf welche Informationen zugreifen darf.

### → SYS.4.5.A4 — Erstellung einer Richtlinie zum sicheren Umgang mit Wechseldatenträgern (S)
  1. Es SOLLTE eine Richtlinie für den richtigen Umgang mit Wechseldatenträgern erstellt werden.
  2. Folgende grundlegenden Aspekte SOLLTEN dabei berücksichtigt werden: welche Wechseldatenträger genutzt werden und wer diese einsetzen darf, welche Daten auf Wechseldatenträgern gespeichert werden dürfen und welche nicht, wie die auf Wechseldatenträgern gespeicherten Daten vor unbefugtem Zugriff, Manipulation und Verlust geschützt werden, wie die Daten auf den Wechseldatenträgern gelöscht werden sollen, mit welchen externen Institutionen Wechseldatenträger ausgetauscht werden dürfen und welche Sicherheitsregelungen dabei zu beachten sind, ob Wechseldatenträger an fremde IT-Systeme angeschlossen werden dürfen und was dabei zu beachten ist, wie Wechseldatenträger zu versenden sind sowie wie der Verbreitung von Schadsoftware über Wechseldatenträger vorgebeugt wird.
  3. Die Institution SOLLTE in der Sicherheitsrichtlinie festlegen, unter welchen Bedingungen Wechseldatenträger gelagert werden sollen.
  4. Insbesondere SOLLTE die Institution vorgeben, dass nur berechtigte Benutzende Zugang zu beschriebenen Wechseldatenträgern haben. **◀ ZITIERT**
  5. Die Institution SOLLTE festlegen, dass Angaben des herstellenden Unternehmens zum Umgang mit Datenträgern berücksichtigt werden müssen.
  6. Die Institution SOLLTE die Verwendung von privaten Wechseldatenträgern untersagen.
  7. Es SOLLTE regelmäßig überprüft werden, ob die Sicherheitsvorgaben für den Umgang mit Wechseldatenträgern aktuell sind.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) ASST.3.12 fordert die Autorisierung des Zugriffs von Personen auf Daten-Assets und deckt damit die Vorgabe ab, dass nur Berechtigte Zugang zu beschriebenen Wechseldatenträgern haben dürfen.

### → APP.4.6.A15 — Vermeidung von Datenlecks (S)
  1. Es SOLLTE eine ausreichend sichere Berechtigungsprüfung durchgeführt werden, bevor geschäftskritische Daten angezeigt, übermittelt oder exportiert werden. **◀ ZITIERT**
  2. Vorgesehene (gewollte) Möglichkeiten des Exports SOLLTEN dokumentiert werden.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die Maßnahme ASST.3.12 fordert die Autorisierung des Zugriffs auf Daten gemäß dem Berechtigungsmanagement, was die im Satz geforderte Berechtigungsprüfung vor Anzeige, Übermittlung oder Export inhaltlich abdeckt.

### → CON.9.A1 — Festlegung zulässiger Empfangender (B) [Zentrale Verwaltung]
  1. Die zentrale Verwaltungsstelle MUSS sicherstellen, dass durch die Weitergabe von Informationen nicht gegen rechtliche Rahmenbedingungen verstoßen wird.
  2. Die zentrale Verwaltungsstelle MUSS festlegen, wer welche Informationen erhalten und weitergeben darf. **◀ ZITIERT**
  3. Es MUSS festgelegt werden, auf welchen Wegen die jeweiligen Informationen ausgetauscht werden dürfen.
  4. Alle Beteiligten MÜSSEN vor dem Austausch von Informationen sicherstellen, dass die empfangende Stelle die notwendigen Berechtigungen für den Erhalt und die Weiterverarbeitung der Informationen besitzt.
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) ASST.3.12 fordert die Autorisierung des Zugriffs von Personen oder Institutionen auf Daten und deckt damit die Festlegung ab, wer welche Informationen erhalten darf.

### → DER.4.A12 — Dokumentation im Notfallmanagement-Prozess (H)
  1. Der Ablauf des Notfallmanagement-Prozesses, die Arbeitsergebnisse der einzelnen Phasen und wichtige Entscheidungen SOLLTEN dokumentiert werden.
  2. Ein festgelegtes Verfahren SOLLTE sicherstellen, dass diese Dokumente regelmäßig aktualisiert werden.
  3. Darüber hinaus SOLLTE der Zugriff auf die Dokumentation auf autorisierte Personen beschränkt werden. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die Maßnahme ASST.3.12 verlangt die Autorisierung des Zugriffs von Personen auf Daten und deckt damit die allgemeine Pflicht ab, den Zugriff auf Dokumentationen auf autorisierte Personen zu beschränken.

### → ORP.4.A16 — Richtlinien für die Zugriffs- und Zugangskontrolle (S) [IT-Betrieb]
  1. Es SOLLTE eine Richtlinie für die Zugriffs- und Zugangskontrolle von IT-Systemen, IT-Komponenten und Datennetzen erstellt werden.
  2. Es SOLLTEN Standard-Rechteprofile benutzt werden, die den Funktionen und Aufgaben der Mitarbeitenden entsprechen. **◀ ZITIERT**
  3. Für jedes IT-System und jede IT-Anwendung SOLLTE eine schriftliche Zugriffsregelung existieren.
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 2) Satz 2 fordert die Verwendung von Standard-Rechteprofilen entsprechend den Aufgaben der Mitarbeitenden, was der rollenbasierten Autorisierung von Personen für den Zugriff auf Assets entspricht.

### → ORP.4.A2 — Einrichtung, Änderung und Entzug von Berechtigungen (B) [IT-Betrieb]
  1. Benutzendenkennungen und Berechtigungen DÜRFEN NUR aufgrund des tatsächlichen Bedarfs und der Notwendigkeit zur Aufgabenerfüllung vergeben werden (Prinzip der geringsten Berechtigungen, englisch Least Privileges und Erforderlichkeitsprinzip, englisch Need-to-know). **◀ ZITIERT**
  2. Bei personellen Veränderungen MÜSSEN die nicht mehr benötigten Benutzendenkennungen und Berechtigungen entfernt werden.
  3. Beantragen Mitarbeitende Berechtigungen, die über den Standard hinausgehen, DÜRFEN diese NUR nach zusätzlicher Begründung und Prüfung vergeben werden.
  4. Zugriffsberechtigungen auf Systemverzeichnisse und -dateien SOLLTEN restriktiv eingeschränkt werden.
  5. Alle Berechtigungen MÜSSEN über separate administrative Rollen eingerichtet werden.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 1) Satz 1 fordert die bedarfsgerechte Vergabe von Berechtigungen an Personen nach dem Erforderlichkeitsprinzip, was sich direkt mit der geforderten Autorisierung von Personen für den Zugriff auf Daten und Assets deckt.

### → ORP.4.A7 — Vergabe von Zugriffsrechten (B) [IT-Betrieb]
  1. Es MUSS festgelegt werden, welche Zugriffsrechte an welche Personen im Rahmen ihrer Funktion vergeben bzw. ihnen entzogen werden. **◀ ZITIERT**
  2. Werden im Rahmen der Zugriffskontrolle Chipkarten oder Token verwendet, so MUSS die Ausgabe bzw. der Entzug dokumentiert werden.
  3. Die Anwendenden SOLLTEN für den korrekten Umgang mit Chipkarten oder Token geschult werden.
  4. Bei längeren Abwesenheiten SOLLTEN berechtigte Personen vorübergehend gesperrt werden.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 1) Satz 1 fordert die Festlegung und Vergabe von Zugriffsrechten an Personen, was sich direkt mit der geforderten Autorisierung von Personen für den Zugriff auf Informationen und Assets überschneidet.


## ASST.5.2 — Geregelte Wartungen  [30 Paare]

**Statement (normativ):** Informationen und Assets für IT-Systeme SOLLTE die Wartung {{ insert: param, asst.5.2-prm1 }} ausführen.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** „Wartung“ bezeichnet hier sämtliche planmäßigen oder zustandsabhängigen Maßnahmen zur Erhaltung der Funktionsfähigkeit, Sicherheit und Integrität von IT-Systemen, Anwendungen und den zugehörigen physischen wie logischen Assets („maintenance“). Verschleißende Systeme und Infrastrukturen könnten zu Fehlerzuständen und hierdurch zu Ausfallzeiten und Sicherheitsrisiken führen. Das betrifft auch die für das IT-System verwendete Stromversorgung, USV, Klimatechnik, sowie Brandabschottungen für Kabel- und Rohrdurchführungen. Beispiele hierfür können vielfältig sein: Ein Server kann turnusmäßig mit Firmware‑Updates versorgt oder nach einer bestimmten Betriebsdauer auf Staubablagerungen überprüft werden; Netzwerkkomponenten können per Lifecycle‑Plan aktualisiert oder lüfterseitig gereinigt werden; USV‑Batterien können nach Herstellerempfehlung getauscht werden; Software‑Module können per Patch‑Management in ein Wartungsfenster eingeplant werden. Eine „regelmäßige Wartung“ bedeutet hierbei ein turnusmäßiges Vorgehen nach festen Zeitintervallen (Vorausbestimmte Instandhaltungsstrategie), während prädiktive Wartung den tatsächlichen Abnutzungs- oder Belastungszustand auswertet, um Eingriffe bedarfsgerecht zu planen (Prädiktive Instandhaltungsstrategie). Beide Ansätze verfolgen das Ziel, Sicherheits- und Betriebsrisiken zu minimieren, die aus dem Ausfall oder der Fehlfunktion technischer Komponenten resultieren könnten.

### → OPS.1.1.1.A26 — Proaktive Instandhaltung im IT-Betrieb (H)
  1. Für die IT-Systeme SOLLTE eine proaktive Instandhaltung durchgeführt werden, in der in festgelegten Intervallen vorbeugende Instandhaltungsmaßnahmen durchgeführt werden. **◀ ZITIERT**
  2. Ergänzend zu der regelmäßigen Wartung und der proaktiven Instandhaltung SOLLTE je IT-Komponente abgewogen werden, ob eine vorausschauende Instandhaltung (engl. **◀ ZITIERT**
  3. Predictive Maintenance) genutzt wird. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `equivalent-to` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die Maßnahme ASST.5.2 fordert explizit die regelmäßige Ausführung von Wartungs- und Instandhaltungsmaßnahmen in festen Intervallen für IT-Systeme.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) Die G++-Maßnahme ASST.5.2 fordert explizit die regelmäßige oder prädiktive Durchführung von Wartungen und deckt damit die geforderte Nutzung vorausschauender Instandhaltung ab.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) ASST.5.2 fordert explizit die regelmäßige oder prädiktive Ausführung von Wartungen und deckt damit die Nutzung von Predictive Maintenance ab.

### → APP.3.3.A9 — Sicheres Speichermanagement (S)
  1. Der IT-Betrieb SOLLTE regelmäßig überprüfen, ob die Massenspeicher des Fileservers noch wie vorgesehen funktionieren. **◀ ZITIERT**
  2. Es SOLLTEN geeignete Ersatzspeicher vorgehalten werden.
  3. Wurde eine Speicherhierarchie (Primär-, Sekundär- bzw. Tertiärspeicher) aufgebaut, SOLLTE ein (teil-)automatisiertes Speichermanagement verwendet werden.
  4. Werden Daten automatisiert verteilt, SOLLTE regelmäßig manuell überprüft werden, ob dies korrekt funktioniert.
  5. Es SOLLTEN mindestens nicht-autorisierte Zugriffsversuche auf Dateien und Änderungen von Zugriffsrechten protokolliert werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die regelmäßige Funktionsprüfung von Massenspeichern stellt eine Form der regelmäßigen bzw. prädiktiven Wartung zur Erhaltung der Funktionsfähigkeit von IT-Assets gemäß ASST.5.2 dar.

### → INF.1.A34 — Gefahrenmeldeanlage (H)
  1. Es SOLLTE eine den Räumlichkeiten und den Risiken angemessene Gefahrenmeldeanlage geben.
  2. Die Gefahrenmeldeanlage SOLLTE regelmäßig geprüft und gewartet werden. **◀ ZITIERT**
  3. Es MUSS sichergestellt werden, dass diejenigen, die Gefahrenmeldungen empfangen in der Lage sind, technisch und personell angemessen auf den Alarm zu reagieren.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) ASST.5.2 fordert die regelmäßige Durchführung von Wartungs- und Instandhaltungsmaßnahmen an Systemen und physischer Infrastruktur, was die geforderte regelmäßige Prüfung und Wartung der Gefahrenmeldeanlage abdeckt.

### → INF.11.A2 — Wartung, Inspektion und Updates (B) [Fachverantwortliche, IT-Betrieb]
  1. Die Fahrzeuge und die dazugehörenden IT-Komponenten MÜSSEN nach den Vorgaben des herstellenden Unternehmens gewartet werden. **◀ ZITIERT**
  2. Hierbei MUSS beachtet werden, dass die Intervalle der herkömmlichen Wartung und von Updates der integrierten IT-Komponenten voneinander abweichen können.
  3. Es MUSS klar geregelt werden, wer in welcher Umgebung die Updates installieren darf.
  4. Auch „Over-the-Air“ (OTA) Updates MÜSSEN geregelt eingespielt werden.
  5. Wartungs- und Reparaturarbeiten MÜSSEN von befugtem und qualifiziertem Personal in einer sicheren Umgebung durchgeführt werden.
  6. Dabei SOLLTE schon vor der Wartung geklärt werden, wie mit Fremdfirmen umgegangen wird.
  7. Werden Fahrzeuge in fremden Institutionen gewartet, SOLLTE geprüft werden, ob alle nicht benötigten, zum Fahrzeug dazugehörigen portablen IT-Systeme entfernt werden.
  8. Werden die Fahrzeuge wieder in den Einsatzbetrieb integriert, MUSS mittels Checkliste geprüft werden, ob alle Beanstandungen und Mängel auch behoben wurden.
  9. Es MUSS auch geprüft werden, ob die vorhandenen IT-Komponenten einsatzfähig sind.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) ASST.5.2 fordert die Durchführung regelmäßiger oder prädiktiver Wartungen an Assets und Systemkomponenten, was die Wartung der IT-Komponenten nach Herstellervorgaben inhaltlich abdeckt.

### → INF.12.A12 — Kontrolle elektrotechnischer Anlagen und bestehender Verbindungen (S) [IT-Betrieb, Haustechnik]
  1. Alle elektrischen Anlagen und Betriebsmittel SOLLTEN gemäß DGUV Vorschrift 3, entsprechend den in § 5 Prüfung genannten Durchführungsanweisungen, regelmäßig geprüft werden. **◀ ZITIERT**
  2. Alle Unregelmäßigkeiten, die festgestellt werden, MÜSSEN unverzüglich dokumentiert werden.
  3. Festgestellte Unregelmäßigkeiten MÜSSEN unverzüglich den zuständigen Organisationseinheiten gemeldet werden.
  4. Die zuständigen Organisationseinheiten MÜSSEN die festgestellten Unregelmäßigkeiten so zeitnah beheben, dass eine Gefährdung von Personen ausgeschlossen werden kann.
  5. Die Verfügbarkeit der elektrischen Anlagen und Betriebsmittel MUSS hierbei im erforderlichen Maß sichergestellt sein.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme fordert die regelmäßige Wartung und Prüfung von IT- und Infrastruktur-Assets (inklusive Stromversorgung), was die regelmäßige elektrotechnische Prüfung nach DGUV V3 auf allgemeinerer Ebene abdeckt.

### → INF.12.A17 — Redundanzen für die IT-Verkabelung (H) [IT-Betrieb]
  1. Es SOLLTE geprüft werden, ob eine redundante primäre IT-Verkabelung geschaffen werden soll, die über unabhängige Trassen geführt wird.
  2. Ebenso SOLLTE geprüft werden, ob die Anschlüsse an IT- oder TK-Provider redundant ausgelegt werden sollen.
  3. Bei hohen oder sehr hohen Verfügbarkeitsanforderungen SOLLTE überlegt werden, in den relevanten Gebäuden die Sekundär- und Tertiärverkabelung redundant auszulegen.
  4. Dabei SOLLTEN redundant ausgelegte Teile der Sekundärverkabelung in unterschiedlichen Brandabschnitten geführt werden.
  5. Wird eine redundante Verkabelung verwendet, SOLLTE deren Funktionsfähigkeit regelmäßig geprüft werden. **◀ ZITIERT**
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) Die G++-Maßnahme ASST.5.2 fordert die regelmäßige Ausführung von Wartungsmaßnahmen zur Erhaltung der Funktionsfähigkeit von IT- und Infrastruktur-Assets, was die regelmäßige Funktionsprüfung redundanter Verkabelungen als allgemeinerer Rahmen abdeckt.

### → INF.13.A17 — Regelung von Wartungs- und Reparaturarbeiten im TGM (S)
  1. Gebäudeeinrichtungen SOLLTEN regelmäßig gewartet werden. **◀ ZITIERT**
  2. Hierfür SOLLTE ein Wartungsplan erstellt werden.
  3. Es SOLLTE geregelt sein, welche Sicherheitsaspekte bei Wartungs- und Reparaturarbeiten zu beachten sind.
  4. Dabei SOLLTEN auch die Abhängigkeiten der verschiedenen Gewerke berücksichtigt werden.
  5. Darüber hinaus SOLLTE festgelegt werden, wer für die Wartung oder Reparatur von Einrichtungen zuständig ist.
  6. Durchgeführte Wartungsarbeiten SOLLTEN dokumentiert werden.
  7. Es SOLLTE zu jedem Zeitpunkt gewährleistet werden, dass Wartungs- und Reparaturarbeiten, die durch Dritte ausgeführt werden, kontrolliert, ausschließlich abgestimmt durchgeführt und abgenommen werden.
  8. Hierfür SOLLTEN interne Mitarbeitende der Haustechnik bestimmt werden, die solche Wartungs- und Reparaturarbeiten autorisieren, beobachten, gegebenenfalls unterstützen und abnehmen.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) Die G++-Maßnahme ASST.5.2 fordert explizit die regelmäßige Durchführung von Wartungen für Assets und die zugehörige Infrastruktur (inklusive Klimatechnik und Stromversorgung).

### → INF.13.A18 — Proaktive Instandhaltung im TGM (S) [Planende]
  1. Für Systeme, die durch das TGM verwaltet werden, SOLLTE eine angemessene proaktive Instandhaltung durchgeführt werden. **◀ ZITIERT**
  2. Hierfür SOLLTEN die regelmäßigen Wartungsintervalle je System festgelegt werden.
  3. Zusätzlich SOLLTE je System abgewogen werden, ob ergänzend zur regelmäßigen Instandhaltung eine vorausschauende Instandhaltung (engl. **◀ ZITIERT**
  4. Predictive Maintenance) genutzt werden kann und in welchem Umfang hierdurch die regelmäßigen Wartungsintervalle verlängert werden können. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) ASST.5.2 deckt die geforderte Durchführung einer proaktiven Instandhaltung durch die Pflicht zur regelmäßigen oder prädiktiven Ausführung von Wartungsmaßnahmen inhaltlich ab.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 3) Die G++-Maßnahme ASST.5.2 fordert explizit die regelmäßige oder prädiktive Durchführung von Wartungen und deckt damit die Prüfung und Nutzung vorausschauender Instandhaltung inhaltlich ab.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die Maßnahme ASST.5.2 fordert explizit die regelmäßige oder prädiktive Durchführung von Wartungen und deckt damit die Nutzung von Predictive Maintenance zur bedarfsgerechten Anpassung von Wartungsstrategien inhaltlich ab.

### → INF.2.A10 — Inspektion und Wartung der Infrastruktur (B) [Wartungspersonal, Haustechnik]
  1. Für alle Komponenten der baulich-technischen Infrastruktur MÜSSEN mindestens die vom herstellenden Unternehmen empfohlenen oder durch Normen festgelegten Intervalle und Vorschriften für Inspektion und Wartung eingehalten werden. **◀ ZITIERT**
  2. Inspektionen und Wartungsarbeiten MÜSSEN protokolliert werden.
  3. Brandschotten MÜSSEN daraufhin geprüft werden, ob sie unversehrt sind.
  4. Die Ergebnisse MÜSSEN dokumentiert werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) ASST.5.2 fordert die regelmäßige Durchführung von Wartungen u. a. für Infrastrukturkomponenten nach festen Intervallen bzw. Herstellerempfehlungen und deckt damit die Einhaltung der Wartungsvorgaben aus Satz 1 ab.

### → INF.2.A14 — Einsatz einer Netzersatzanlage (S) [Planende, Haustechnik]
  1. Die Energieversorgung eines Rechenzentrums aus dem Netz eines Energieversorgungsunternehmens SOLLTE um eine Netzersatzanlage (NEA) ergänzt werden.
  2. Wird eine NEA verwendet, MUSS sie regelmäßig gewartet werden. **◀ ZITIERT**
  3. Bei diesen Wartungen MÜSSEN auch Belastungs- und Funktionstests sowie Testläufe unter Last durchgeführt werden.
  4. Der Betriebsmittelvorrat einer NEA MUSS regelmäßig daraufhin überprüft werden, ob er ausreichend ist.
  5. Außerdem MUSS regelmäßig kontrolliert werden, ob die Vorräte noch verwendbar sind, vor allem um die sogenannte Dieselpest zu vermeiden.
  6. Nach Möglichkeit SOLLTE statt Diesel-Kraftstoff schwefelarmes Heizöl verwendet werden.
  7. Die Tankvorgänge von Brennstoffen MÜSSEN protokolliert werden.
  8. Aus dem Protokoll MUSS die Art des Brennstoffs, die genutzten Additive, das Tankdatum und die getankte Menge hervorgehen.
  9. Wenn für einen Serverraum auf den Einsatz einer NEA verzichtet wird, SOLLTE alternativ zur NEA eine USV mit einer dem Schutzbedarf angemessenen Autonomiezeit realisiert werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) ASST.5.2 verlangt die regelmäßige Durchführung von Wartungen für Assets und Infrastrukturen, was die regelmäßige Wartung einer Netzersatzanlage (NEA) als allgemeine Anforderung vollständig abdeckt.

### → INF.2.A26 — Redundante Auslegung von Netzersatzanlagen (H) [Planende]
  1. Netzersatzanlagen SOLLTEN redundant ausgelegt werden.
  2. Hinsichtlich der Wartung MÜSSEN auch redundante NEAs entsprechend INF.2.A14 Einsatz einer Netzersatzanlage behandelt werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) ASST.5.2 fordert die regelmäßige Durchführung von Wartungsmaßnahmen an Systemen und Infrastrukturkomponenten, was die geforderte Wartung redundanter Netzersatzanlagen inhaltlich abdeckt.

### → INF.2.A3 — Einsatz einer unterbrechungsfreien Stromversorgung (B) [Haustechnik]
  1. Für alle betriebsrelevanten Komponenten des Rechenzentrums MUSS eine unterbrechungsfreie Stromversorgung (USV) installiert werden.
  2. Da der Leistungsbedarf von Klimaanlagen oft zu hoch für eine USV ist, MUSS mindestens die Steuerung der Anlagen an die unterbrechungsfreie Stromversorgung angeschlossen werden.
  3. Im Falle eines Serverraums SOLLTE je nach Verfügbarkeitsanforderungen der IT-Systeme geprüft werden, ob der Betrieb einer USV notwendig ist.
  4. Die USV MUSS ausreichend dimensioniert sein.
  5. Bei relevanten Änderungen an den Verbrauchern MUSS überprüft werden, ob die vorhandenen USV-Systeme noch ausreichend dimensioniert sind.
  6. Bei USV-Systemen mit Batterie als Energiespeicher MUSS die Batterie im erforderlichen Temperaturbereich gehalten werden.
  7. Sie SOLLTE dazu vorzugsweise räumlich getrennt von der Leistungselektronik der USV platziert werden.
  8. Die USV MUSS regelmäßig gewartet und auf Funktionsfähigkeit getestet werden. **◀ ZITIERT**
  9. Dafür MÜSSEN die vom herstellenden Unternehmen vorgesehenen Wartungsintervalle eingehalten werden.
- **Satz 8** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 8) ASST.5.2 fordert die regelmäßige Durchführung von Wartungen zur Erhaltung der Funktionsfähigkeit von IT-Systemen und Infrastrukturkomponenten wie der USV.

### → INF.2.A5 — Einhaltung der Lufttemperatur und -feuchtigkeit (B) [Haustechnik]
  1. Es MUSS sichergestellt werden, dass die Lufttemperatur und Luftfeuchtigkeit im IT-Betriebsbereich innerhalb der vorgeschriebenen Grenzwerte liegen.
  2. Die tatsächliche Wärmelast in den gekühlten Bereichen MUSS in regelmäßigen Abständen und nach größeren Umbauten überprüft werden.
  3. Eine vorhandene Klimatisierung MUSS regelmäßig gewartet werden. **◀ ZITIERT**
  4. Die Parameter Temperatur und Feuchtigkeit MÜSSEN mindestens so aufgezeichnet werden, dass sich rückwirkend erkennen lässt, ob Grenzwerte überschritten wurden, und dass sie bei der Lokalisierung der Ursache der Abweichung sowie bei der Beseitigung der Ursache unterstützend genutzt werden können.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) ASST.5.2 fordert die regelmäßige Durchführung von Wartungsarbeiten an IT-Assets und Infrastrukturen, was laut Erläuterung explizit auch die Klimatechnik einschließt.

### → INF.2.A9 — Einsatz einer Lösch- oder Brandvermeidungsanlage (B) [Haustechnik]
  1. In einem Rechenzentrum MUSS entweder eine Lösch- oder Brandvermeidungsanlage nach aktuellem Stand der Technik installiert sein oder durch technische (insbesondere durch eine flächendeckende Brandfrüherkennung, siehe INF.2.A17 Brandfrüherkennung) und organisatorische Maßnahmen (geschultes Personal und Reaktionspläne für Meldungen der Brandfrüherkennung) sichergestellt sein, dass unmittelbar (innerhalb von maximal 3 Minuten) auf Meldungen der Brandfrüherkennung mit schadensminimierenden Maßnahmen reagiert wird.
  2. In Serverräumen ohne Lösch- oder Brandvermeidungsanlage MÜSSEN Handfeuerlöscher mit geeigneten Löschmitteln in ausreichender Zahl und Größe vorhanden sein.
  3. Es MUSS beachtet werden, dass darüber hinausgehende baurechtliche Anforderungen hinsichtlich der Ausstattung mit Handfeuerlöschern davon unberührt bleiben.
  4. Die Feuerlöscher MÜSSEN so angebracht werden, dass sie im Brandfall leicht zu erreichen sind.
  5. Jeder Feuerlöscher MUSS regelmäßig geprüft und gewartet werden. **◀ ZITIERT**
  6. Alle Mitarbeitenden, die ein Rechenzentrum oder einen Serverraum betreten dürfen, MÜSSEN in die Benutzung der Handfeuerlöscher eingewiesen werden.
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) ASST.5.2 fordert allgemein die regelmäßige oder prädiktive Durchführung von Wartungen für IT-Systeme und deren physische Infrastruktur, was die regelmäßige Prüfung und Wartung von Feuerlöschern als Spezialfall abdeckt.

### → INF.5.A16 — Einsatz einer unterbrechungsfreien Stromversorgung (S) [Haustechnik]
  1. Es SOLLTE geprüft werden, welche Geräte an eine USV angeschlossen werden sollen.
  2. Falls eine USV erforderlich ist, SOLLTE die Stützzeit der USV so ausgelegt sein, dass alle versorgten Komponenten sicher herunterfahren können.
  3. Es SOLLTE berücksichtigt werden, dass die Batterien von USV-Anlagen altern.
  4. Bei relevanten Änderungen SOLLTE überprüft werden, ob die vorhandenen USV-Anlagen noch ausreichend dimensioniert sind.
  5. Die Batterie der USV SOLLTE im erforderlichen Temperaturbereich gehalten werden.
  6. Die USV SOLLTE regelmäßig gewartet und auf Funktionsfähigkeit getestet werden. **◀ ZITIERT**
  7. Dafür SOLLTEN die vom herstellenden Unternehmen vorgesehenen Wartungsintervalle eingehalten werden. **◀ ZITIERT**
- **Satz 6** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 6) ASST.5.2 fordert die regelmäßige Durchführung von Wartungsmaßnahmen zur Erhaltung der Funktionsfähigkeit von Assets inklusive USV-Anlagen.
- **Satz 7** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 7) ASST.5.2 verlangt die regelmäßige oder prädiktive Durchführung von Wartungen (u. a. nach festen Zeitintervallen und Herstellerempfehlungen auch für USV-Systeme), was das Einhalten der Wartungsintervalle abdeckt.

### → INF.5.A17 — Inspektion und Wartung der Infrastruktur (S) [Haustechnik, IT-Betrieb, Wartungspersonal]
  1. Für alle Komponenten der baulich-technischen Infrastruktur SOLLTEN mindestens die vom herstellenden Unternehmen empfohlenen oder durch Normen festgelegten Intervalle und Vorschriften für Inspektion und Wartung eingehalten werden. **◀ ZITIERT**
  2. Kabel- und Rohrdurchführungen durch brand- und rauchabschnittbegrenzende Wände SOLLTEN daraufhin geprüft werden, ob die Schotten die für den jeweiligen Einsatzzweck erforderliche Zulassung haben und unversehrt sind.
  3. Inspektionen und Wartungsarbeiten MÜSSEN geeignet protokolliert werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme ASST.5.2 fordert die regelmäßige bzw. prädiktive Durchführung von Wartungen und deckt damit die Einhaltung von Wartungsintervallen für Infrastrukturkomponenten inhaltlich ab.

### → INF.5.A23 — Netzersatzanlage (H) [Planende, Haustechnik, Wartungspersonal]
  1. Die Energieversorgung der Institution SOLLTE um eine Netzersatzanlage (NEA) ergänzt werden.
  2. Der Betriebsmittelvorrat einer NEA SOLLTE regelmäßig kontrolliert werden.
  3. Die NEA SOLLTE außerdem regelmäßig gewartet werden. **◀ ZITIERT**
  4. Bei diesen Wartungen SOLLTEN auch Belastungs- und Funktionstests sowie Testläufe unter Last durchgeführt werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) ASST.5.2 fordert die regelmäßige Durchführung von Wartungen für Assets und Infrastrukturkomponenten, was die regelmäßige Wartung der Netzersatzanlage (NEA) umfasst.

### → INF.5.A24 — Lüftung und Kühlung (H) [Planende, Haustechnik, Wartungspersonal]
  1. Die Lüftungs- und Kühltechnik SOLLTE betriebsredundant ausgelegt werden.
  2. Es SOLLTE sichergestellt werden, dass diese Anlagen regelmäßig gewartet werden. **◀ ZITIERT**
  3. Bei sehr hohem Schutzbedarf SOLLTE auch eine Wartungsredundanz vorhanden sein.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme ASST.5.2 fordert explizit die regelmäßige oder prädiktive Durchführung von Wartungen für IT-Systeme und deren Infrastruktur (inklusive Klimatechnik) und deckt damit die regelmäßige Wartung der Lüftungs- und Kühltechnik direkt ab.

### → INF.6.A7 — Einhaltung von klimatischen Bedingungen (S) [Haustechnik]
  1. Es SOLLTE sichergestellt werden, dass die zulässigen Höchst- und Tiefstwerte für Temperatur und Luftfeuchtigkeit sowie der Schwebstoffanteil in der Raumluft im Datenträgerarchiv eingehalten werden.
  2. Die Werte von Lufttemperatur und -feuchte SOLLTEN mehrmals im Jahr für die Dauer von einer Woche aufgezeichnet und dokumentiert werden.
  3. Dabei festgestellte Abweichungen vom Sollwert SOLLTEN zeitnah behoben werden.
  4. Die eingesetzten Klimageräte SOLLTEN regelmäßig gewartet werden. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) ASST.5.2 fordert die regelmäßige Durchführung von Wartungen für Infrastrukturen inklusive Klimatechnik und deckt damit die regelmäßige Wartung der eingesetzten Klimageräte inhaltlich ab.

### → INF.6.A9 — Gefahrenmeldeanlage (H) [Haustechnik]
  1. Es SOLLTE in Datenträgerarchiven eine angemessene Gefahrenmeldeanlage eingerichtet werden.
  2. Diese Gefahrenmeldeanlage SOLLTE regelmäßig geprüft und gewartet werden. **◀ ZITIERT**
  3. Es SOLLTE sichergestellt sein, dass diejenigen Personen, die Gefahrenmeldungen empfangen in der Lage sind, auf Alarmmeldungen angemessen zu reagieren.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) ASST.5.2 fordert die regelmäßige Durchführung von Wartungen zur Erhaltung der Funktionsfähigkeit und Sicherheit von Systemen sowie zugehöriger physischer Infrastruktur, was die geforderte regelmäßige Prüfung und Wartung der Gefahrenmeldeanlage abdeckt.

### → OPS.1.2.2.A19 — Regelmäßige Funktions- und Recoverytests bei der Archivierung (S) [IT-Betrieb]
  1. Für die Archivierung SOLLTEN regelmäßige Funktions- und Recoverytests durchgeführt werden.
  2. Die Archivierungsdatenträger SOLLTEN mindestens einmal jährlich daraufhin überprüft werden, ob sie noch lesbar und integer sind.
  3. Für die Fehlerbehebung SOLLTEN geeignete Prozesse definiert werden.
  4. Weiterhin SOLLTEN die Hardwarekomponenten des Archivsystems regelmäßig auf ihre einwandfreie Funktion hin geprüft werden. **◀ ZITIERT**
  5. Es SOLLTE regelmäßig geprüft werden, ob alle Archivierungsprozesse fehlerfrei funktionieren.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) ASST.5.2 fordert die regelmäßige Durchführung von Wartungsmaßnahmen zur Erhaltung der Funktionsfähigkeit von IT- und Hardware-Assets, was die regelmäßige Funktionsprüfung der Archiv-Hardwarekomponenten als allgemeine Anforderung abdeckt.

### → SYS.1.7.A3 — Wartung von Z-Systemen (B)
  1. Die Z-Hardware und -Firmware, das Betriebssystem sowie die verschiedenen Programme MÜSSEN regelmäßig und bei Bedarf gepflegt werden. **◀ ZITIERT**
  2. Die hierfür notwendigen Wartungsaktivitäten MÜSSEN geplant und in das Änderungsmanagement (siehe OPS.1.1.3 Patch- und Änderungsmanagement) integriert werden.
  3. Insbesondere DÜRFEN Updates durch das herstellende Unternehmen NUR unter Kontrolle der Betreibenden durchgeführt werden, lokal über SE (Support Elements) bzw. HMC (Hardware Management Console) oder remote über die RSF (Remote Support Facility).
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) ASST.5.2 fordert die regelmäßige bzw. prädiktive Durchführung von Wartungsmaßnahmen für IT-Systeme und deckt damit die regelmäßige und bedarfsgerechte Pflege von Hardware, Firmware und Software inhaltlich ab.

### → SYS.4.4.A21 — Einsatzumgebung und Stromversorgung (H) [Haustechnik]
  1. Es SOLLTE geklärt werden, ob IoT-Geräte in der angedachten Einsatzumgebung betrieben werden dürfen (Schutzbedarf anderer IT-Systeme, Datenschutz).
  2. IoT-Geräte SOLLTEN in der Einsatzumgebung vor Diebstahl, Zerstörung und Manipulation geschützt werden.
  3. Es SOLLTE geklärt sein, ob ein IoT-Gerät bestimmte Anforderungen an die physische Einsatzumgebung hat, wie z. B. Luftfeuchtigkeit, Temperatur oder Energieversorgung.
  4. Falls erforderlich, SOLLTEN dafür ergänzende Maßnahmen bei der Infrastruktur umgesetzt werden.
  5. Wenn IoT-Geräte mit Batterien betrieben werden, SOLLTE der regelmäßige Funktionstest und Austausch der Batterien geregelt werden. **◀ ZITIERT**
  6. IoT-Geräte SOLLTEN entsprechend ihrer vorgesehenen Einsatzart und dem vorgesehenen Einsatzort vor Staub und Verschmutzungen geschützt werden.
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) Die G++-Maßnahme fordert die regelmäßige Ausführung von Wartungsmaßnahmen, was das turnusmäßige Prüfen und Tauschen von Verschleißteilen wie Batterien zur Erhaltung der Betriebsbereitschaft direkt abdeckt.

### → OPS.1.1.1.A19 — Regelungen für Wartungs- und Reparaturarbeiten (S)
  1. IT-Komponenten SOLLTEN regelmäßig gewartet werden. **◀ ZITIERT**
  2. Es SOLLTE geregelt sein, welche Sicherheitsaspekte bei Wartungs- und Reparaturarbeiten zu beachten sind.
  3. Es SOLLTE festgelegt werden, wer für die Wartung oder Reparatur von IT-Komponenten zuständig ist.
  4. Durchgeführte Wartungs- und Reparaturarbeiten SOLLTEN dokumentiert werden.
  5. Es SOLLTE sichergestellt werden, dass Wartungs- und Reparaturarbeiten, die durch Dritte ausgeführt werden, mit den Beteiligten abgestimmt sind.
  6. Es SOLLTEN interne Mitarbeitende des IT-Betriebs bestimmt werden, die solche Arbeiten autorisieren, gegebenenfalls beobachten oder unterstützen und abnehmen.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) Die Maßnahme ASST.5.2 fordert explizit die regelmäßige oder prädiktive Durchführung von Wartungen an IT-Systemen und deckt damit Satz 1 direkt ab.

### → IND.2.3.A2 — Kalibrierung von Sensoren (S) [Wartungspersonal]
  1. Wenn notwendig, SOLLTEN Sensoren regelmäßig kalibriert werden. **◀ ZITIERT**
  2. Die Kalibrierungen SOLLTEN geeignet dokumentiert werden.
  3. Der Zugang zur Kalibrierung eines Sensors MUSS geschützt sein.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) ASST.5.2 deckt die regelmäßige Kalibrierung von Sensoren als allgemeinen Oberbegriff der regelmäßigen Wartung und Instandhaltung von IT- und Infrastruktur-Assets ab.

