# Review-Dossier Praktik NOT

Praktik NOT: 31 Controls mit Mapping, 189 Paare gesamt. Gesampelt: 5 Controls (max/min/median Paarzahl + 2 zufällig).

## NOT.3.1 — Wiederanlaufplan  [28 Paare]

**Statement (normativ):** Notfallplanung SOLLTE einen Wiederanlaufplan für zeitkritische Systeme und Anwendungen dokumentieren.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Ein Wiederanlaufplan legt fest, wie eine ausgefallene (IT)-Ressource auf ein vorgesehenes Notbetriebsniveau innerhalb einer Wiederanlaufzeit durch Notfallteams zur Verfügung gestellt wird. Besteht ein BCMS, dann werden die kritischen Ressourcen innerhalb der Business Impact Analyse identifiziert und in dieser entsprechende Wiederanlaufzeiten festgelegt. Die ausgewählten BC-Strategien des BCMS bieten ferner den Rahmen für die Wiederanlaufplanung. Besteht kein BCMS, dann können die zeitkritischen IT-Ressourcen anhand der Schutzbedarfsfeststellung (erhöhter Schutzbedarf in der Verfügbarkeit) identifiziert werden. Die Wiederanlaufzeit kann dann nur grob anhand der Ergebnisse der Informationssicherheitseinstufung geschätzt werden. Zeitkritisch sind IT-Systeme und Anwendungen genau dann, wenn ihre fortlaufende Verfügbarkeit für die Aufrechterhaltug des Geschäftsbetriebes auch im Notfall zwingend erforderlich ist. Nähere Informationen können dem BSI-Standard 200-4 Kapitel 12 Wiederanlauf- und Wiederherstellungsplanung (AS) entnommen werden.

### → APP.2.1.A16 — Erstellung eines Notfallplans für den Ausfall eines Verzeichnisdienstes (H)
  1. Im Rahmen der Notfallvorsorge SOLLTE es eine bedarfsgerechte Notfallplanung für Verzeichnisdienste geben. **◀ ZITIERT**
  2. Für den Ausfall wichtiger Verzeichnisdienst-Systeme SOLLTEN Notfallpläne vorliegen. **◀ ZITIERT**
  3. Alle Notfall-Prozeduren für die gesamte Systemkonfiguration der Verzeichnisdienst-Komponenten SOLLTEN dokumentiert werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) NOT.3.1 deckt die Forderung nach einer Notfallplanung für Verzeichnisdienste als zeitkritische Systeme/Anwendungen auf übergeordneter Ebene durch die Dokumentation eines Wiederanlaufplans ab.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) NOT.3.1 verlangt die Dokumentation von Wiederanlaufplänen für zeitkritische Systeme und deckt damit als allgemeingültige Anforderung das Vorliegen von Notfallplänen für den Ausfall wichtiger Verzeichnisdienst-Systeme inhaltlich ab.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die Forderung nach Dokumentation von Notfall-Prozeduren für Systemkomponenten wird durch die allgemeine Pflicht zur Dokumentation eines Wiederanlaufplans für zeitkritische Systeme und Anwendungen in NOT.3.1 abgedeckt.

### → APP.3.6.A9 — Erstellen eines Notfallplans für DNS-Server (B)
  1. Ein Notfallplan für DNS-Server MUSS erstellt werden.
  2. Der Notfallplan für DNS-Server MUSS in die bereits vorhandenen Notfallpläne der Institution integriert werden.
  3. Im Notfallplan für DNS-Server MUSS ein Datensicherungskonzept für die Zonen- und Konfigurationsdateien beschrieben sein.
  4. Das Datensicherungskonzept für die Zonen- und Konfigurationsdateien MUSS in das existierende Datensicherungskonzept der Institution integriert werden.
  5. Der Notfallplan für DNS-Server MUSS einen Wiederanlaufplan für alle DNS-Server im Informationsverbund enthalten. **◀ ZITIERT**
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) NOT.3.1 fordert die Dokumentation von Wiederanlaufplaenen fuer zeitkritische Systeme und Anwendungen, was den Wiederanlaufplan fuer DNS-Server als allgemeine Anforderung abdeckt.

### → APP.4.3.A22 — Notfallvorsorge (H)
  1. Für das Datenbankmanagementsystem SOLLTE ein Notfallplan erstellt werden, der festlegt, wie ein Notbetrieb realisiert werden kann. **◀ ZITIERT**
  2. Die für den Notfallplan notwendigen Ressourcen SOLLTEN ermittelt werden.
  3. Zusätzlich SOLLTE der Notfallplan definieren, wie aus dem Notbetrieb der Regelbetrieb wiederhergestellt werden kann.
  4. Der Notfallplan SOLLTE die nötigen Meldewege, Reaktionswege, Ressourcen und Reaktionszeiten der Fachverantwortlichen festlegen.
  5. Auf Basis eines Koordinationsplans zum Wiederanlauf SOLLTEN alle von der Datenbank abhängigen IT-Systeme vorab ermittelt und berücksichtigt werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) NOT.3.1 fordert die Dokumentation eines Wiederanlaufplans für Systeme und Anwendungen zur Erreichung des Notbetriebs, was die Erstellung eines Notfallplans zur Realisierung des Notbetriebs für das DBMS abdeckt.
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) Die Maßnahme NOT.3.1 fordert die Dokumentation eines Wiederanlaufplans für zeitkritische Systeme, was die Ermittlung und koordinierte Berücksichtigung abhängiger Systeme beim Wiederanlauf abdeckt.

### → APP.5.4.A12 — Einbindung von UCC in die Notfallplanung (H)
  1. Ausgehend von einer Business Impact Analyse SOLLTE geprüft werden, welche UCC-Dienste in der Notfallplanung berücksichtigt werden sollen.
  2. Hierbei SOLLTEN in Notfallsituationen für einzelne UCC-Dienste alternative Anwendungen bereitgestellt werden.
  3. Insbesondere SOLLTE für die Benutzenden die Erreichbarkeit von wichtigen Diensten wie der Notruf gewährleistet werden.
  4. Zudem SOLLTE ein Notfallplan für die UCC-Dienste erstellt werden, in dem notwendige Konfigurationen sowie Routing-Anpassungen, die über den Telefonie-Provider realisiert werden, behandelt werden. **◀ ZITIERT**
  5. Ebenso SOLLTE der Wiederanlauf der UCC-Komponenten und -Dienste unter Berücksichtigung der Wechselwirkungen innerhalb der UCC-Dienste festgelegt werden. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die G++-Maßnahme NOT.3.1 fordert allgemein die Dokumentation von Wiederanlaufplänen für zeitkritische Systeme und Anwendungen, was die Erstellung eines Notfallplans für UCC-Dienste inklusive technischer Konfigurationen und Anpassungen abdeckt.
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) NOT.3.1 fordert die Dokumentation eines Wiederanlaufplans für zeitkritische Systeme und Anwendungen, was die Festlegung des Wiederanlaufs von UCC-Komponenten und -Diensten als allgemeinere Maßnahme inhaltlich abdeckt.

### → INF.14.A27 — Berücksichtigung von Wechselwirkungen zwischen Komponenten der GA in der Notfallplanung (S)
  1. Es SOLLTE initial und in regelmäßigen Abständen nachvollziehbar analysiert werden, wie sich die GA und die abgeleiteten Planungen und Konzepte auf die Notfallplanung auswirken.
  2. Insbesondere SOLLTE festgelegt werden, wie bei einem Ausfall von TGA-Anlagen oder GA-relevanten Komponenten durch technischen Defekt oder Angriff die Wechselwirkungen auf andere TGA-Anlagen, GA-relevante Systeme und TGM minimiert werden können.
  3. Im Rahmen der Notfallplanung SOLLTE auch festgelegt werden, welches Wartungspersonal für die betroffenen TGA-Anlagen und GA-relevanten Systeme zuständig ist und über welche Meldewege dieses erreicht werden kann.
  4. Außerdem SOLLTE festgelegt werden, welche Berechtigungen das Wartungspersonal zur Behebung von Notfällen hat.
  5. Es SOLLTE in der Notfallplanung auch spezifiziert werden, wie bei Ausfall der GA-Systeme ein gegebenenfalls erforderlicher Notbetrieb von TGA-Anlagen sichergestellt wird.
  6. Dabei SOLLTE für alle TGA-Anlagen und GA-Systeme inklusive aller GA-relevanten Komponenten eine Wiederanlaufreihenfolge festgelegt und in den entsprechenden Wiederanlaufplänen dokumentiert werden. **◀ ZITIERT**
- **Satz 6** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 6) NOT.3.1 fordert allgemein die Dokumentation von Wiederanlaufplänen für zeitkritische Systeme, was die Festlegung und Dokumentation der Wiederanlaufreihenfolge für GA- und TGA-Systeme inhaltlich abdeckt.

### → NET.1.2.A27 — Einbindung des Netzmanagements in die Notfallplanung (S)
  1. Die Netzmanagement-Lösungen SOLLTEN in die Notfallplanung der Institution eingebunden werden. **◀ ZITIERT**
  2. Dazu SOLLTEN die Netzmanagement-Werkzeuge und die Konfigurationen der Netzkomponenten gesichert und in die Wiederanlaufpläne integriert sein. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme NOT.3.1 fordert die allgemeine Wiederanlaufplanung für zeitkritische Systeme und Anwendungen, was die Einbindung von Netzmanagement-Lösungen in die Notfallplanung als Spezialfall inhaltlich abdeckt.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) G++ NOT.3.1 fordert die allgemeine Erstellung von Wiederanlaufplänen für zeitkritische Systeme und Anwendungen, was die Integration von Netzmanagement-Lösungen und deren Konfigurationen in Wiederanlaufpläne inhaltlich abdeckt.

### → NET.1.2.A38 — Festlegung von Notbetriebsformen für die Netzmanagement-Infrastruktur (H)
  1. Für eine schnelle Wiederherstellung der Sollzustände von Software bzw. Firmware sowie der Konfiguration der Komponenten in der Netzmanagement-Infrastruktur SOLLTEN hinreichend gute Ersatzlösungen festgelegt werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) NOT.3.1 fordert die Dokumentation eines Wiederanlaufplans zur Überführung zeitkritischer Systeme auf ein Notbetriebsniveau bzw. zur Wiederherstellung, was die Festlegung entsprechender Ersatzlösungen für Systemkomponenten und deren Konfigurationen allgemein abdeckt.

### → NET.3.1.A22 — Notfallvorsorge bei Routern und Switches (S)
  1. Es SOLLTE geplant und vorbereitet werden, welche Fehler bei Routern oder Switches in einem Notfall diagnostiziert werden könnten.
  2. Außerdem SOLLTE geplant und vorbereitet werden, wie die identifizierten Fehler behoben werden können.
  3. Für typische Ausfallszenarien SOLLTEN entsprechende Handlungsanweisungen definiert und in regelmäßigen Abständen aktualisiert werden. **◀ ZITIERT**
  4. Die Notfallplanungen für Router und Switches SOLLTEN mit der übergreifenden Störungs- und Notfallvorsorge abgestimmt sein.
  5. Die Notfallplanungen SOLLTEN sich am allgemeinen Notfallvorsorgekonzept orientieren.
  6. Es SOLLTE sichergestellt sein, dass die Dokumentationen zur Notfallvorsorge und die darin enthaltenen Handlungsanweisungen in Papierform vorliegen.
  7. Das im Rahmen der Notfallvorsorge beschriebene Vorgehen SOLLTE regelmäßig geprobt werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die Dokumentation eines Wiederanlaufplans in NOT.3.1 umfasst die Definition konkreter Handlungsanweisungen zur Bewältigung und Behebung von Ausfallszenarien zeitkritischer Systeme.

### → NET.3.2.A32 — Notfallvorsorge für die Firewall (S)
  1. Diagnose und Fehlerbehebungen SOLLTEN bereits im Vorfeld geplant und vorbereitet werden.
  2. Für typische Ausfallszenarien SOLLTEN entsprechende Handlungsanweisungen definiert und in regelmäßigen Abständen aktualisiert werden. **◀ ZITIERT**
  3. Die Notfallplanungen für die Firewall SOLLTEN mit der übergreifenden Störungs- und Notfallvorsorge abgestimmt sein.
  4. Sie SOLLTEN sich am allgemeinen Notfallvorsorgekonzept orientieren (siehe DER.4 Notfallmanagement).
  5. Es SOLLTE sichergestellt sein, dass die Dokumentationen zur Notfallvorsorge und die darin enthaltenen Handlungsanweisungen in Papierform vorliegen.
  6. Das im Rahmen der Notfallvorsorge beschriebene Vorgehen SOLLTE regelmäßig geprobt werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die Dokumentation eines Wiederanlaufplans in NOT.3.1 umfasst inhaltlich die Definition von Handlungsanweisungen zur Bewältigung von Ausfallszenarien zeitkritischer Systeme.

### → NET.4.1.A14 — Notfallvorsorge für TK-Anlagen (S)
  1. Es SOLLTE ein Notfallplan für die TK-Anlage erstellt werden. **◀ ZITIERT**
  2. Dieser SOLLTE in das Notfallkonzept der Institution integriert werden.
  3. Es SOLLTEN regelmäßig Notfallübungen bezüglich der TK-Anlagen durchgeführt werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) NOT.3.1 fordert die Dokumentation von Wiederanlaufplänen für zeitkritische Systeme und deckt damit als allgemeinere Maßnahme die Erstellung eines Notfallplans für TK-Anlagen inhaltlich ab.

### → OPS.1.1.7.A16 — Einbindung des Systemmanagements in die Notfallplanung (S)
  1. Die Systemmanagement-Lösung SOLLTE in die Notfallplanung der Institution eingebunden werden. **◀ ZITIERT**
  2. Dazu SOLLTEN sowohl die Systemmanagement-Lösung als auch die Konfigurationen der zu verwaltenden Systeme gesichert und in die Wiederanlaufpläne integriert sein. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) G++ NOT.3.1 fordert die allgemeine Erstellung von Wiederanlaufplänen für zeitkritische Systeme und Anwendungen, was die Einbindung der Systemmanagement-Lösung in die Notfallplanung als generelle Fassung abdeckt.
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) NOT.3.1 verlangt die Erstellung von Wiederanlaufplänen für zeitkritische Systeme und deckt damit als allgemeinere Anforderung die Integration der Systemmanagement-Lösung in die Wiederanlaufplanung inhaltlich ab.

### → OPS.1.2.5.A21 — Erstellung eines Notfallplans für den Ausfall der Fernwartung (S)
  1. Es SOLLTE ein Konzept entwickelt werden, wie die Folgen eines Ausfalls von Fernwartungskomponenten minimiert werden können.
  2. Dieses SOLLTE festhalten, wie im Falle eines Ausfalls zu reagieren ist.
  3. Durch den Notfallplan SOLLTE sichergestellt sein, dass Störungen, Schäden und Folgeschäden minimiert werden.
  4. Außerdem SOLLTE festgelegt werden, wie eine zeitnahe Wiederherstellung des Normalbetriebs erfolgen kann. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die geforderte Festlegung zur zeitnahen Wiederherstellung des Normalbetriebs wird durch die Pflicht zur Dokumentation eines Wiederanlaufplans in NOT.3.1 abgedeckt.

### → SYS.1.8.A20 — Notfallvorsorge und Notfallreaktion für Speicherlösungen (S)
  1. Es SOLLTE ein Notfallplan für die eingesetzte Speicherlösung erstellt werden. **◀ ZITIERT**
  2. Der Notfallplan SOLLTE genau beschreiben, wie in bestimmten Notfallsituationen vorzugehen ist.
  3. Auch SOLLTEN Handlungsanweisungen in Form von Maßnahmen und Kommandos enthalten sein, die die Fehleranalyse und Fehlerkorrektur unterstützen.
  4. Um Fehler zu beheben, SOLLTEN geeignete Werkzeuge eingesetzt werden.
  5. Regelmäßige Übungen und Tests SOLLTEN anhand des Notfallplans durchgeführt werden.
  6. Nach den Übungen und Tests sowie nach einem tatsächlichen Notfall SOLLTEN die dabei erzeugten Daten sicher gelöscht werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die Forderung nach Dokumentation eines Wiederanlaufplans für zeitkritische Systeme und Anwendungen in NOT.3.1 deckt die allgemeinere Pflicht zur Erstellung eines Notfallplans für Speicherlösungen materiell ab.

### → SYS.2.1.A38 — Einbindung in die Notfallplanung (H)
  1. Die Clients SOLLTEN im Notfallmanagementprozess berücksichtigt werden.
  2. Die Clients SOLLTEN hinsichtlich der Geschäftsprozesse oder Fachaufgaben, für die sie benötigt werden, für den Wiederanlauf priorisiert werden. **◀ ZITIERT**
  3. Es SOLLTEN geeignete Notfallmaßnahmen vorgesehen werden, indem mindestens Wiederanlaufpläne erstellt, Bootmedien zur Systemwiederherstellung generiert sowie Passwörter und kryptografische Schlüssel sicher hinterlegt werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) NOT.3.1 fordert die Erstellung von Wiederanlaufplänen für zeitkritische IT-Systeme basierend auf deren Kritikalität für den Geschäftsbetrieb, was die Priorisierung von Clients für den Wiederanlauf inhaltlich abdeckt.
- **Satz 3** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) NOT.3.1 fordert die Dokumentation von Wiederanlaufplänen für zeitkritische Systeme und deckt damit die allgemeine Pflicht zur Erstellung von Wiederanlaufplänen aus Satz 3 inhaltlich ab.

### → DER.4.A7 — Erstellung eines Notfallkonzepts (H) [Institutionsleitung]
  1. Alle kritischen Geschäftsprozesse und Ressourcen SOLLTEN identifiziert werden, beispielsweise mit einer Business-Impact-Analyse (BIA).
  2. Es SOLLTEN die wichtigsten relevanten Risiken für die kritischen Geschäftsprozesse und Fachaufgaben sowie deren Ressourcen identifiziert werden.
  3. Für jedes identifizierte Risiko SOLLTE entschieden werden, welche Risikostrategien zur Risikobehandlung eingesetzt werden sollen.
  4. Es SOLLTEN Kontinuitätsstrategien entwickelt werden, die einen Wiederanlauf und eine Wiederherstellung der kritischen Geschäftsprozesse in der geforderten Zeit ermöglichen.
  5. Es SOLLTE ein Notfallkonzept erstellt werden.
  6. Es SOLLTEN solche Notfallpläne und Maßnahmen entwickelt und implementiert werden, die eine effektive Notfallbewältigung und eine schnelle Wiederaufnahme der kritischen Geschäftsprozesse ermöglichen. **◀ ZITIERT**
  7. Im Notfallkonzept SOLLTE die Informationssicherheit berücksichtigt und entsprechende Sicherheitskonzepte für die Notfalllösungen entwickelt werden.
- **Satz 6** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 6) NOT.3.1 verlangt mit der Dokumentation eines Wiederanlaufplans für zeitkritische Systeme die Erstellung eines zentralen Notfallplans zur schnellen Wiederaufnahme des Betriebs.

### → IND.1.A13 — Notfallplanung für OT (H)
  1. Notfallpläne für den Ausfall und für die Kompromittierung jeder Zone SOLLTEN definiert, dokumentiert, nach jeder größeren Änderung getestet und regelmäßig geübt sein. **◀ ZITIERT**
  2. Zudem SOLLTE ein wirksames Ersatzverfahren für den Ausfall der (Fern-) Administrationsmöglichkeit definiert, dokumentiert und getestet sein.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) NOT.3.1 deckt die Erstellung und Dokumentation von Notfall- und Wiederanlaufplänen für zeitkritische Systeme als allgemeinere Fassung der geforderten zonenbezogenen Ausfallplanung ab.

### → OPS.1.1.1.A17 — Planung des IT-Betriebs unter besonderer Berücksichtigung von Mangel- und Notsituationen (S)
  1. Der IT-Betrieb SOLLTE für die betriebenen IT-Komponenten definieren, wann eine Mangel- oder eine Notsituation vorliegt.
  2. Für diese Situationen SOLLTE nach den Vorgaben des allgemeinen Notfallmanagements festgelegt werden, welche IT-Komponenten vorrangig betrieben werden oder für einen Mindestbetrieb benötigt werden. **◀ ZITIERT**
  3. Die Notfallplanung SOLLTE die folgenden Punkte beinhalten: Disaster-Recovery-Plan Notfallhandbuch für die IT-Komponenten unter Einbeziehung der gesamten Infrastruktur Umgang mit kritischen und längerfristigen betriebsbehindernden Störungen **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) NOT.3.1 fordert einen Wiederanlaufplan für zeitkritische Systeme und deckt damit die Festlegung vorrangig zu betreibender bzw. für den Mindestbetrieb erforderlicher IT-Komponenten im Notfall inhaltlich ab.
- **Satz 3** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme NOT.3.1 deckt die Forderung nach einem Disaster-Recovery-Plan bzw. Wiederanlaufplan für IT-Systeme im Rahmen der Notfallplanung direkt ab.

### → OPS.2.2.A12 — Aufrechterhaltung der Informationssicherheit im laufenden Cloud-Nutzungs-Betrieb (S)
  1. Alle für die eingesetzten Cloud-Dienste erstellten Dokumentationen und Richtlinien SOLLTEN regelmäßig aktualisiert werden.
  2. Es SOLLTE außerdem periodisch kontrolliert werden, ob die vertraglich zugesicherten Leistungen erbracht werden.
  3. Auch SOLLTEN sich die Cloud-Diensteanbietenden und die Institution nach Möglichkeit regelmäßig abstimmen.
  4. Ebenso SOLLTE geplant und geübt werden, wie auf Systemausfälle zu reagieren ist. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) NOT.3.1 fordert die Dokumentation eines Wiederanlaufplans für zeitkritische Systeme und deckt damit die geforderte Planung der Reaktion auf Systemausfälle inhaltlich ab.

### → SYS.1.1.A22 — Einbindung in die Notfallplanung (S)
  1. Der Server SOLLTE im Notfallmanagementprozess berücksichtigt werden. **◀ ZITIERT**
  2. Dazu SOLLTEN die Notfallanforderungen an den Server ermittelt und geeignete Notfallmaßnahmen umgesetzt werden, z. B. indem Wiederanlaufpläne erstellt oder Passwörter und kryptografische Schlüssel sicher hinterlegt werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die Erstellung von Wiederanlaufplänen für zeitkritische Systeme gemäß NOT.3.1 konkretisiert und deckt die Berücksichtigung des Servers im Notfallmanagementprozess inhaltlich ab.
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) NOT.3.1 fordert die Dokumentation von Wiederanlaufplänen für zeitkritische Systeme und Anwendungen und deckt damit die Erstellung von Wiederanlaufplänen als Notfallmaßnahme für Server ab.


## NOT.3.3 — Sensibilisierung zum Vorgehen im Notfall  [3 Paare]

**Statement (normativ):** Notfallplanung für Nutzende SOLLTE zur Vorgehensweise in Notfällen und Krisen sensibilisieren.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Eine Sensibilisierung für die Vorgehensweise in Notfällen und Krisen (Contingency Training) stellt sicher, dass alle zuständigen Stellen ihre Aufgaben bei einem Schadensereignis kennen. Zweckmäßig ist es, die Detailtiefe der Sensibilisierung auf die unterschiedlichen Aufgaben bei einem Schadensereignis zuzuschneiden. Beispielsweise genügt es für manche Mitarbeitenden zu wissen, welche Erreichbarkeit bei einem Schadensereignis von ihnen erwartet wird.

### → DER.4.A1 — Erstellung eines Notfallhandbuchs (S)
  1. Es SOLLTE ein Notfallhandbuch erstellt werden, in dem die wichtigsten Informationen zu Rollen, Sofortmaßnahmen, Alarmierung und Eskalation sowie Kommunikations-, grundsätzlichen Geschäftsfortführungs-, Wiederanlauf- und Wiederherstellungsplänen enthalten sind.
  2. Zuständigkeiten und Befugnisse SOLLTEN zugewiesen, kommuniziert und im Notfallhandbuch festgehalten werden.
  3. Es SOLLTE sichergestellt sein, dass im Notfall entsprechend geschultes Personal zur Verfügung steht. **◀ ZITIERT**
  4. Es SOLLTE regelmäßig durch Tests und Übungen überprüft werden, ob die im Notfallhandbuch beschriebenen Maßnahmen auch wie vorgesehen funktionieren.
  5. Es SOLLTE regelmäßig geprüft werden, ob das Notfallhandbuch noch aktuell ist.
  6. Gegebenenfalls SOLLTE es aktualisiert werden.
  7. Es SOLLTE auch im Notfall zugänglich sein.
  8. Das Notfallhandbuch SOLLTE um Verhaltensregeln für spezielle Fälle ergänzt werden, z. B. Brand.
  9. Die Regeln SOLLTEN allen Mitarbeitenden bekanntgegeben werden. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme NOT.3.3 fordert Notfallschulungen bzw. -sensibilisierungen (Contingency Training), damit Personal im Notfall seine Aufgaben kennt und entsprechend geschult zur Verfügung steht.
- **Satz 9** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 9) Die Sensibilisierung der Nutzenden zum Vorgehen in Notfällen deckt die Bekanntgabe der Notfall- und Verhaltensregeln an alle Mitarbeitenden inhaltlich ab.

### → DER.4.A8 — Integration der Mitarbeitenden in den Notfallmanagement-Prozess (H) [Vorgesetzte, Personalabteilung]
  1. Alle Mitarbeitenden SOLLTEN regelmäßig für das Thema Notfallmanagement sensibilisiert werden. **◀ ZITIERT**
  2. Zum Notfallmanagement SOLLTE es ein Schulungs- und Sensibilisierungskonzept geben.
  3. Die Mitarbeitenden im Notfallmanagement-Team SOLLTEN regelmäßig geschult werden, um die benötigten Kompetenzen aufzubauen.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) NOT.3.3 fordert explizit die Sensibilisierung von Nutzenden bezüglich des Vorgehens in Notfällen und deckt damit die regelmäßige Sensibilisierung der Mitarbeitenden für das Notfallmanagement inhaltlich ab.


## NOT.4.8 — Verschlüsselte Datensicherung  [1 Paare]

**Statement (normativ):** Notfallplanung SOLLTE die Datensicherung durch {{ insert: param, not.4.8-prm1 }} verschlüsseln.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Die Datensicherung enthält typischerweise eine große Menge schützenswerter Daten. Durch Verschlüsselung wird die Vertraulichkeit und Integrität geschützter Informationen auch nach einem schwerwiegenden Vorfall gewährleistet. Dies kann besonders bei einem Datenleck (engl. Data Breach) oder Diebstahl von Speichermedien helfen, da die Offenlegung sensibler Daten selbst bei unbefugtem Zugriff verhindert werden kann. Für anerkannte Algorithmen siehe BSI TR-02102. Technisch kann die Festplattenverschlüsselung auf dem Sicherungsspeicher (Disk Encryption) genutzt werden, aber auch die dateibasierte Verschlüsselung jedes einzelnen Sicherungs-Archives. Wichtig ist es, dabei auch auf die Verwaltung der kryptographischen Schlüssel (Key Management) zu achten, damit diese weder einem unbeugten Zugriff ausgesetzt sind, noch der Zugriff auf die Datensicherung im Ernstfall durch fehlende Zugangsdaten unmöglich wird.

### → CON.3.A13 — Einsatz kryptografischer Verfahren bei der Datensicherung (H) [IT-Betrieb]
  1. Um die Vertraulichkeit der gesicherten Daten zu gewährleisten, SOLLTE der IT-Betrieb alle Datensicherungen verschlüsseln. **◀ ZITIERT**
  2. Es SOLLTE sichergestellt werden, dass sich die verschlüsselten Daten auch nach längerer Zeit wieder einspielen lassen.
  3. Verwendete kryptografische Schlüssel SOLLTEN mit einer getrennten Datensicherung geschützt werden.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme NOT.4.8 fordert explizit die Verschlüsselung der Datensicherung mit einem anerkannten kryptografischen Algorithmus und deckt damit die Forderung von Satz 1 inhaltlich vollständig ab.


## NOT.4.2 — Sicherung des Systems  [15 Paare]

**Statement (normativ):** Notfallplanung für IT-Systeme SOLLTE deren Datensicherung {{ insert: param, not.4.2-prm1 }} ausführen.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Zu den erforderlichen Daten können z.B. Konfigurationsdateien des Betriebssystems, Firmware, Lizenzen, Treiber und die Systemdokumentation gehören. Bei gleichartigen Systemen kann die Anforderung auch durch die Sicherung einer Kopie erfolgen, wenn mit dieser alle IT-Systeme dieser Art funktionsfähig wiederhergestellt werden können. Die Anforderung kann auch durch die Wiederherstellung aus einem Versionskontrollsystem erfolgen.

### → APP.3.4.A13 — Regelmäßige Sicherung wichtiger Systemkomponenten eines Samba-Servers (S)
  1. Es SOLLTEN alle Systemkomponenten in das institutionsweite Datensicherungskonzept eingebunden werden, die erforderlich sind, um einen Samba-Server wiederherzustellen. **◀ ZITIERT**
  2. Auch die Kontoinformationen aus allen eingesetzten Backends SOLLTEN berücksichtigt werden.
  3. Ebenso SOLLTEN alle TDB-Dateien gesichert werden.
  4. Des Weiteren SOLLTE die Samba-Registry mit gesichert werden, falls sie für Freigaben eingesetzt wurde.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) NOT.4.2 fordert die regelmäßige Datensicherung von IT-Systemen zur Gewährleistung ihrer Wiederherstellbarkeit und deckt damit die Einbindung aller zur Wiederherstellung nötigen Systemkomponenten in die Datensicherung ab.

### → APP.4.4.A5 — Datensicherung im Cluster (B)
  1. Es MUSS eine Datensicherung des Clusters erfolgen. **◀ ZITIERT**
  2. Die Datensicherung MUSS umfassen: Festspeicher (Persistent Volumes), Konfigurationsdateien von Kubernetes und den weiteren Programmen der Control Plane, den aktuellen Zustand des Kubernetes-Clusters inklusive der Erweiterungen, Datenbanken der Konfiguration, namentlich hier etcd, alle Infrastrukturanwendungen, die zum Betrieb des Clusters und der darin befindlichen Dienste notwendig sind und die Datenhaltung der Code und Image Registries.
  3. Es SOLLTEN auch Snapshots für den Betrieb der Anwendungen betrachtet werden.
  4. Snapshots DÜRFEN die Datensicherung NICHT ersetzen.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) NOT.4.2 fordert die regelmaessige Datensicherung von IT-Systemen und deckt damit die allgemeine Pflicht zur Datensicherung der Cluster-Systeme ab.

### → APP.5.2.A5 — Datensicherung von Exchange (B)
  1. Exchange-Server MÜSSEN vor Installationen und Konfigurationsänderungen sowie in zyklischen Abständen gesichert werden. **◀ ZITIERT**
  2. Dabei MÜSSEN insbesondere die Exchange-Server-Datenbanken gesichert werden.
  3. Gelöschte Exchange-Objekte SOLLTEN erst nach einiger Zeit aus der Datenbank entfernt werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) NOT.4.2 deckt die geforderte regelmäßige Datensicherung von Exchange-Servern als IT-Systeme auf allgemeiner Ebene ab.

### → NET.1.2.A6 — Regelmäßige Datensicherung (B)
  1. Bei der Datensicherung des Netzmanagements MÜSSEN mindestens die Systemdaten für die Einbindung der zu verwaltenden Komponenten bzw. Objekte, Ereignismeldungen, Statistikdaten sowie vorgehaltene Daten für das Konfigurationsmanagement gesichert werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme NOT.4.2 fordert die regelmäßige Datensicherung von IT-Systemen und deckt die Sicherung der system- und konfigurationsrelevanten Daten des Netzmanagements als allgemeine Anforderung inhaltlich ab.

### → NET.3.1.A8 — Regelmäßige Datensicherung (B)
  1. Die Konfigurationsdateien von Routern und Switches MÜSSEN regelmäßig gesichert werden. **◀ ZITIERT**
  2. Die Sicherungskopien MÜSSEN so abgelegt werden, dass im Notfall darauf zugegriffen werden kann.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) NOT.4.2 fordert die regelmäßige Datensicherung von IT-Systemen, was die regelmäßige Sicherung von Konfigurationsdateien für Systeme wie Router und Switches direkt umfasst.

### → NET.4.1.A12 — Datensicherung der Konfigurationsdateien (S)
  1. Die Konfigurations- und Anwendungsdaten der eingesetzten TK-Anlage SOLLTEN bei der Ersteinrichtung und anschließend regelmäßig gesichert werden, insbesondere nachdem sich diese geändert haben. **◀ ZITIERT**
  2. Es SOLLTE regelmäßig geprüft und dokumentiert werden, ob die Sicherungen der TK-Anlagen auch tatsächlich als Basis für eine Systemwiederherstellung genutzt werden können.
  3. Es SOLLTE ein Datensicherungskonzept für TK-Anlagen erstellt und mit den allgemeinen Konzepten der Datensicherung für Server und Netzkomponenten abgestimmt werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) G++ NOT.4.2 deckt als allgemeine Anforderung zur regelmäßigen Datensicherung von IT-Systemen inklusive deren Konfigurationsdateien die geforderte Datensicherung der TK-Anlage inhaltlich ab.

### → SYS.1.7.A24 — Datenträgerverwaltung unter z/OS-Systemen (S)
  1. Dateien, Programme und Funktionen zur Verwaltung von Datenträgern sowie die Datenträger selbst (Festplatten und Bänder) einschließlich Master-Katalog SOLLTEN mittels RACF-Profilen geschützt werden.
  2. Es SOLLTEN Sicherungskopien aller wichtigen Dateien zur Verfügung stehen, die in einer Notfallsituation zurückgespielt werden können. **◀ ZITIERT**
  3. Die Zuordnung von Datenträgern zu den Z-Systemen SOLLTE nachvollziehbar sein.
  4. Es SOLLTE gewährleistet werden, dass je nach Volumen und Zeitfenster genügend Bandstationen zur Verfügung stehen.
  5. Beim Einsatz des HSM (Hierarchical Storage Manager) SOLLTE festgelegt werden, welche Festplatten gesichert werden sollen und wie die Sicherung erfolgen soll.
  6. Bänder, die vom HSM verwaltet werden, SOLLTEN NICHT anderweitig bearbeitet werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme NOT.4.2 fordert die regelmäßige Durchführung der Datensicherung für IT-Systeme zur Notfallwiederherstellung und deckt damit die Bereitstellung von wiederherstellbaren Sicherungskopien wichtiger Systemdateien ab.

### → SYS.3.3.A11 — Ausfallvorsorge bei Mobiltelefonen (S) [Benutzende]
  1. Die auf einem Mobiltelefon gespeicherten Daten SOLLTEN in regelmäßigen Abständen auf einem externen Medium gesichert werden. **◀ ZITIERT**
  2. Muss ein defektes Mobiltelefon repariert werden, SOLLTEN zuvor alle Daten gelöscht und das Gerät auf den Werkszustand zurückgesetzt werden.
  3. Es SOLLTEN immer Ersatzgeräte vorhanden sein, um ein ausgefallenes Mobiltelefon kurzfristig ersetzen zu können.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) NOT.4.2 fordert allgemein die regelmäßige Datensicherung von IT-Systemen, was die regelmäßige Sicherung der Daten von Mobiltelefonen als IT-Systeme umfasst.

### → CON.3.A5 — Regelmäßige Datensicherung (B) [IT-Betrieb, Mitarbeitende]
  1. Regelmäßige Datensicherungen MÜSSEN gemäß den Datensicherungsplänen erstellt werden. **◀ ZITIERT**
  2. Alle Mitarbeitenden MÜSSEN über die Regelungen zur Datensicherung informiert sein.
  3. Auch MÜSSEN sie darüber informiert werden, welche Aufgaben sie bei der Erstellung von Datensicherungen haben.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) NOT.4.2 fordert die regelmäßige Ausführung der Datensicherung für IT-Systeme und deckt damit die Durchführung regelmäßiger Datensicherungen als Spezialfall inhaltlich ab.

### → CON.3.A6 — Entwicklung eines Datensicherungskonzepts (S) [Fachverantwortliche, IT-Betrieb]
  1. Die Institution SOLLTE ein Datensicherungskonzept erstellen, dass mindestens die nachfolgenden Punkte umfasst: Definitionen zu wesentlichen Aspekten der Datensicherung (z. B. unterschiedliche Verfahrensweisen zur Datensicherung), Gefährdungslage, Einflussfaktoren je IT-System oder Gruppe von IT-Systemen, Datensicherungspläne je IT-System oder Gruppe von IT-Systemen sowie relevante Ergebnisse des Notfallmanagements/BCM, insbesondere die Recovery Point Objective (RPO) je IT-System oder Gruppe von IT-Systemen.
  2. Der IT-Betrieb SOLLTE das Datensicherungskonzept mit den jeweiligen Fachverantwortlichen der betreffenden Anwendungen abstimmen.
  3. Wird ein zentrales Datensicherungssystem für die Sicherung der Daten eingesetzt, SOLLTE beachtet werden, dass sich aufgrund der Konzentration der Daten ein höherer Schutzbedarf ergeben kann.
  4. Datensicherungen SOLLTEN regelmäßig gemäß dem Datensicherungskonzept durchgeführt werden. **◀ ZITIERT**
  5. Das Datensicherungskonzept selbst SOLLTE auch in einer Datensicherung enthalten sein.
  6. Die im Datensicherungskonzept enthaltenen technischen Informationen, um Systeme und Datensicherungen wiederherzustellen (Datensicherungspläne), SOLLTEN in der Art gesichert werden, dass sie auch verfügbar sind, wenn die Datensicherungssysteme selbst ausfallen.
  7. Die Mitarbeitenden SOLLTEN über den Teil des Datensicherungskonzepts unterrichtet werden, der sie betrifft.
  8. Regelmäßig SOLLTE kontrolliert werden, ob das Datensicherungskonzept korrekt umgesetzt wird.
- **Satz 4** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die G++-Maßnahme NOT.4.2 fordert mit der regelmäßigen Ausführung der Datensicherung für IT-Systeme einen wesentlichen Teil bzw. Spezialfall der in Satz 4 geforderten regelmäßigen Durchführung von Datensicherungen.

### → OPS.1.2.2.A7 — Regelmäßige Datensicherung der System- und Archivdaten (B) [IT-Betrieb]
  1. Alle Archivdaten, die zugehörigen Indexdatenbanken sowie die Systemdaten MÜSSEN regelmäßig gesichert werden (siehe CON.3 Datensicherungskonzept). **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) NOT.4.2 fordert explizit die regelmäßige Datensicherung von IT-Systemen und deckt damit die im Satz geforderte regelmäßige Sicherung der Systemdaten inhaltlich ab.

### → IND.1.A19 — Erstellung von Datensicherungen (B) [Mitarbeitende, OT-Betrieb (Operational Technology, OT)]
  1. Programme und Daten MÜSSEN regelmäßig gesichert werden. **◀ ZITIERT**
  2. Auch nach jeder Systemänderung an OT-Komponenten MUSS eine Sicherung erstellt werden.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) NOT.4.2 fordert explizit die regelmäßige Durchführung der Datensicherung für IT-Systeme und deckt damit die regelmäßige Sicherung von Programmen und Systemdaten ab.

### → NET.1.2.A27 — Einbindung des Netzmanagements in die Notfallplanung (S)
  1. Die Netzmanagement-Lösungen SOLLTEN in die Notfallplanung der Institution eingebunden werden.
  2. Dazu SOLLTEN die Netzmanagement-Werkzeuge und die Konfigurationen der Netzkomponenten gesichert und in die Wiederanlaufpläne integriert sein. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) NOT.4.2 deckt die regelmaessige Sicherung von IT-Systemen und deren Konfigurationsdateien ab, was die geforderte Sicherung der Konfigurationen von Netzkomponenten inhaltlich umfasst.

### → OPS.1.1.2.A26 — Backup der Konfiguration (S)
  1. Alle Konfigurationen SOLLTEN durch regelmäßige Backups auf Anwendungsebene und auf IT-Systemebene gesichert werden. **◀ ZITIERT**
  2. Vor IT-Administrationstätigkeiten mit potenziell weitreichenden Folgen SOLLTE ein zusätzliches Backup gemacht werden.
  3. Für Backups SOLLTE gewährleistet sein, dass sie im Fehlerfall wieder eingespielt werden können.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) NOT.4.2 fordert die regelmäßige Datensicherung von IT-Systemen und deckt damit den Teil des Satzes zur Sicherung von Konfigurationen auf IT-Systemebene ab.

### → OPS.1.1.7.A14 — Zentrale Konfigurationsverwaltung für zu verwaltende Systeme (S)
  1. Software und Konfigurationsdaten für die zu verwaltenden Systeme SOLLTEN konsequent in einem Konfigurationsmanagement verwaltet werden, das eine Versionierung und Änderungsverfolgung ermöglicht.
  2. Die zugehörige Dokumentation zur Konfigurationsverwaltung SOLLTE vollständig und immer aktuell sein.
  3. Die benötigten Dokumentationen SOLLTEN an zentraler Stelle sicher verfügbar sein sowie in die Datensicherung eingebunden werden. **◀ ZITIERT**
  4. Die zentrale Konfigurationsverwaltung SOLLTE nachhaltig gepflegt und regelmäßig auditiert werden.
  5. Sämtliche Schnittstellen zwischen Systemmanagement-Lösung und anderen Anwendungen und Diensten SOLLTEN dokumentiert und vollständig in einem Konfigurationsmanagement verwaltet werden.
  6. Zwischen relevanten Betriebsbereichen SOLLTEN funktionale Änderungen an den Schnittstellen frühzeitig abgestimmt und dokumentiert werden.
  7. Die Konfigurationsdaten für die zu verwaltenden Systeme SOLLTEN automatisch über das Netz verteilt und ohne Betriebsunterbrechung installiert und aktiviert werden können.
- **Satz 3** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) NOT.4.2 fordert die regelmäßige Datensicherung von IT-Systemen und schließt laut Erläuterung explizit die Sicherung der Systemdokumentation ein.


## NOT.4.14 — Offline-Kopie  [2 Paare]

**Statement (normativ):** Notfallplanung für Daten SOLLTE eine Offline-Kopie {{ insert: param, not.4.14-prm1 }} ausführen.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Eine Offline-Kopie ist eine Datensicherung, die physisch oder logisch von produktiven Systemen und dem laufenden Netzwerk getrennt ist („offline backup“ oder „air-gapped backup“). „Regelmäßig“ bedeutet, dass die Institution in Abhängigkeit von Verfügbarkeit und Kritikalität ihrer Daten feste Intervalle definiert, beispielsweise täglich, wöchentlich oder monatlich. Der Sinn und Zweck dieser Vorgabe liegt darin, sicherzustellen, dass im Falle von Schadsoftwarebefall oder gezielten Angriffen keine gleichzeitige Kompromittierung aller Sicherungskopien stattfinden kann; ein Angriff könnte sonst auch Backups verschlüsseln oder löschen. Eine Offline-Kopie kann dagegen die Wiederherstellung kritischer Systeme nach einem Ransomware-Angriff oder auch nach einem physischen Ausfall, etwa durch Stromschaden oder Brand, unterstützen. Eine Institution kann dies umsetzen, indem sie (1) Kopien in Papierform oder auf wechselbaren Medien wie externen Festplatten, RDX-Kassetten oder Bändern erstellt, die nach dem Backup-Vorgang vom Netzwerk getrennt und geschützt aufbewahrt werden, (2) Cloud-Backups so konfiguriert, dass sie durch Write-Once-Read-Many-(WORM)-Speicher geschützt und logisch von aktiven Systemen isoliert sind, oder (3) eine Rotation von Datenträgern einführt, bei der Kopien an einem separaten, physischen Standort verwahrt werden.

### → CON.3.A14 — Schutz von Datensicherungen (B) [IT-Betrieb]
  1. Die erstellten Datensicherungen MÜSSEN in geeigneter Weise vor unbefugtem Zugriff geschützt werden.
  2. Hierbei MUSS insbesondere sichergestellt werden, dass Datensicherungen nicht absichtlich oder unbeabsichtigt überschrieben werden können.
  3. IT-Systeme, die für die Datensicherung eingesetzt werden, SOLLTEN einen schreibenden Zugriff auf die Speichermedien für die Datensicherung nur für autorisierte Datensicherungen oder autorisierte Administrationstätigkeiten gestatten.
  4. Alternativ SOLLTEN die Speichermedien für die Datensicherung nur für autorisierte Datensicherungen oder autorisierte Administrationstätigkeiten mit den entsprechenden IT-Systemen verbunden werden. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `equivalent-to` | Fundrichtung: beide
  Begründung: (Teilanforderung 4) Das Erstellen einer Offline-Kopie nach NOT.4.14 verlangt die physische oder logische Trennung der Speichermedien außerhalb des Sicherungsvorgangs, was der gezielten Anbindung der Medien nur für autorisierte Datensicherungen entspricht.

### → CON.3.A2 — Festlegung der Verfahrensweisen für die Datensicherung (B) [Fachverantwortliche, IT-Betrieb]
  1. Der IT-Betrieb MUSS Verfahren festlegen, wie die Daten gesichert werden.
  2. Für die Datensicherungsverfahren MÜSSEN Art, Häufigkeit und Zeitpunkte der Datensicherungen bestimmt werden.
  3. Dies MUSS wiederum auf Basis der erhobenen Einflussfaktoren und in Abstimmung mit den jeweiligen Fachverantwortlichen geschehen.
  4. Auch MUSS definiert sein, welche Speichermedien benutzt werden und wie die Transport- und Aufbewahrungsmodalitäten ausgestaltet sein müssen.
  5. Datensicherungen MÜSSEN immer auf separaten Speichermedien für die Datensicherung gespeichert werden.
  6. Besonders schützenswerte Speichermedien für die Datensicherung SOLLTEN nur während der Datensicherung und Datenwiederherstellung mit dem Netz der Institution oder dem Ursprungssystem verbunden werden. **◀ ZITIERT**
  7. In virtuellen Umgebungen sowie für Storage-Systeme SOLLTE geprüft werden, ob das IT-System ergänzend durch Snapshot-Mechanismen gesichert werden kann, um hierdurch mehrere schnell wiederherstellbare Zwischenversionen zwischen den vollständigen Datensicherungen zu erstellen.
- **Satz 6** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 6) Die G++-Maßnahme NOT.4.14 fordert die Erstellung von Offline-Kopien bzw. Air-Gapped Backups, was inhaltlich der geforderten Netztrennung der Backup-Medien außerhalb von Sicherungs- und Wiederherstellungsvorgängen entspricht.

