# Review-Dossier Praktik SENS

Praktik SENS: 74 Controls mit Mapping, 260 Paare gesamt. Gesampelt: 5 Controls (max/min/median Paarzahl + 2 zufällig).

## SENS.2.4 — Nutzung unautorisierter Assets  [2 Paare]

**Statement (normativ):** Sensibilisierung für Nutzende SOLLTE die Nutzung unautorisierter Assets untersagen.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Die Nutzung unautorisierter Assets bezeichnet hier den Einsatz von IT-Systemen, Datenträgern, Anwendungen oder Cloud-Diensten, die nicht durch die Institution freigegeben und inventarisiert sind. Hierzu gehört auch der Anschluss privater Peripheriegeräte wie Tastaturen oder das Telefonieren mit nicht autorisierten Telefonen. Der Sinn und Zweck der Anforderung liegt darin, unkontrollierte Schatten-IT und damit verbundene Risiken zu reduzieren. So könnte etwa ein unautorisiertes USB-Gerät Schadsoftware einschleusen, oder eine nicht genehmigte Cloud-Anwendung könnte zu unbemerkten Datenabflüssen führen. Besteht ein Bedarf an Assets, dann können die festgelegten Meldewege genutzt werden. Bei der Beschaffung von Assets sind die Verfahren und Regelungen des Assetmanagements zu beachten.

### → SYS.3.2.1.A8 — Installation von Apps (B)
  1. Die Institution MUSS regeln, ob, wie und welche Apps Benutzende selbst auf ihren Geräten installieren dürfen.
  2. Sie SOLLTEN nur freigegebene Apps installieren dürfen. **◀ ZITIERT**
  3. Die Institution MUSS festlegen, aus welchen Quellen Apps installiert werden dürfen.
  4. Es MUSS unterbunden werden, dass sich Apps aus nicht zugelassenen Quellen installieren lassen.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 2) Satz 2 untersagt Benutzenden die Installation nicht freigegebener Apps, was der Untersagung der Nutzung unautorisierter Software-Assets entspricht.

### → SYS.4.5.A4 — Erstellung einer Richtlinie zum sicheren Umgang mit Wechseldatenträgern (S)
  1. Es SOLLTE eine Richtlinie für den richtigen Umgang mit Wechseldatenträgern erstellt werden.
  2. Folgende grundlegenden Aspekte SOLLTEN dabei berücksichtigt werden: welche Wechseldatenträger genutzt werden und wer diese einsetzen darf, welche Daten auf Wechseldatenträgern gespeichert werden dürfen und welche nicht, wie die auf Wechseldatenträgern gespeicherten Daten vor unbefugtem Zugriff, Manipulation und Verlust geschützt werden, wie die Daten auf den Wechseldatenträgern gelöscht werden sollen, mit welchen externen Institutionen Wechseldatenträger ausgetauscht werden dürfen und welche Sicherheitsregelungen dabei zu beachten sind, ob Wechseldatenträger an fremde IT-Systeme angeschlossen werden dürfen und was dabei zu beachten ist, wie Wechseldatenträger zu versenden sind sowie wie der Verbreitung von Schadsoftware über Wechseldatenträger vorgebeugt wird.
  3. Die Institution SOLLTE in der Sicherheitsrichtlinie festlegen, unter welchen Bedingungen Wechseldatenträger gelagert werden sollen.
  4. Insbesondere SOLLTE die Institution vorgeben, dass nur berechtigte Benutzende Zugang zu beschriebenen Wechseldatenträgern haben.
  5. Die Institution SOLLTE festlegen, dass Angaben des herstellenden Unternehmens zum Umgang mit Datenträgern berücksichtigt werden müssen.
  6. Die Institution SOLLTE die Verwendung von privaten Wechseldatenträgern untersagen. **◀ ZITIERT**
  7. Es SOLLTE regelmäßig überprüft werden, ob die Sicherheitsvorgaben für den Umgang mit Wechseldatenträgern aktuell sind.
- **Satz 6** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 6) SENS.2.4 untersagt als allgemeinere Regelung die Nutzung unautorisierter Assets (inklusive privater Datenträger) und deckt damit das Verbot privater Wechseldatenträger inhaltlich ab.


## SENS.7.1 — Spezifische Sensibilisierung  [28 Paare]

**Statement (normativ):** Sensibilisierung für Nutzende SOLLTE zu zielobjektspezifischen Schutzmaßnahmen zielgruppengerecht sensibilisieren.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Kann dazu beitragen, dass Personen Risiken, die mit ihrer konkreten Tätigkeit, ihrem Arbeitsumfeld oder den von ihnen genutzten Systemen verbunden sind, frühzeitig erkennen und angemessen reagieren können. Ziel ist es auf die spezifischen Schutzbedarfe der jeweiligen Zielobjekte – wie z. B. bestimmte IT-Systeme, Produktionsanlagen, Forschungsdaten oder vertrauliche Kundeninformationen – aufmerksam zu machen. Dazu können sowohl technische als auch organisatorischen Schutzmaßnahmen gehören. Der Begriff „zielgruppengerecht“ meint dabei, dass Inhalte in einer Form, Tiefe und Sprache bereitgestellt werden, die für die jeweiligen Nutzenden verständlich, relevant und handlungsnah sind. Für die Zielgruppengerechtigkeit ist eine Zielgruppenanalyse zweckmäßig. Die Schutzmaßnahmen ergeben sich aus der konkreten Implementierung der Anforderungen durch die Institution.

### → APP.1.1.A17 — Sensibilisierung zu spezifischen Office-Eigenschaften (B)
  1. Alle Benutzenden MÜSSEN geeignet bezüglich der Gefährdungen durch Aktive Inhalte in Office-Dateien sensibilisiert werden.
  2. Die Benutzenden MÜSSEN zum Umgang mit Dokumenten aus externen Quellen geeignet sensibilisiert werden.
  3. Die Benutzenden SOLLTEN über die Möglichkeiten und Grenzen von Sicherheitsfunktionen der eingesetzten Software und der genutzten Speicherformate informiert werden. **◀ ZITIERT**
  4. Den Benutzenden SOLLTE vermittelt werden, mit welchen Funktionen sie Dokumente vor nachträglicher Veränderung und Bearbeitung schützen können. **◀ ZITIERT**
  5. Benutzende SOLLTEN im Umgang mit den Verschlüsselungsfunktionen in Office-Produkten sensibilisiert werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 3) Die G++-Maßnahme SENS.7.1 deckt als übergeordnete Anforderung zur zielobjektspezifischen Sensibilisierung über Schutzmaßnahmen die Aufklärung über Sicherheitsfunktionen und -grenzen der eingesetzten Software und Formate ab.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) G++-Maßnahme SENS.7.1 deckt als übergeordnete Anforderung die Vermittlung zielobjektspezifischer Schutzmaßnahmen (hier Funktionen zum Schutz vor nachträglicher Bearbeitung von Dokumenten) inhaltlich ab.

### → APP.5.3.A7 — Schulung zu Sicherheitsmechanismen von E-Mail-Clients für Benutzende (S)
  1. Die Institution SOLLTE das Personal darüber aufklären, welche Risiken entstehen, wenn E-Mail-Anwendungen benutzt werden und wie sicher mit E-Mails umgegangen werden kann.
  2. Dies SOLLTE zusätzlich zur allgemeinen Schulung und Sensibilisierung geschehen. **◀ ZITIERT**
  3. Die Institution SOLLTE zu den Gefahren sensibilisieren, die entstehen können, wenn E-Mail-Anhänge geöffnet werden.
  4. Die Schulungen SOLLTEN ebenfalls darauf eingehen, wie E-Mails von gefälschten Absendeadressen erkannt werden können.
  5. Die Institution SOLLTE davor warnen, an E-Mail-Kettenbriefen teilzunehmen oder zu viele Mailinglisten zu abonnieren.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) SENS.7.1 fordert die Durchführung zielobjektspezifischer Sensibilisierungsmaßnahmen, was die Forderung nach einer über die allgemeine Sensibilisierung hinausgehenden, spezifischen Aufklärung inhaltlich abdeckt.

### → APP.5.4.A7 — Regelungen für eine sichere Benutzung der UCC-Dienste (B)
  1. Konversationen, die mit Hilfe von UCC durchgeführt werden, MÜSSEN abgesichert werden.
  2. Hierbei MÜSSEN folgende Aspekte berücksichtigt werden: Auswahl der Teilnehmenden entsprechend dem Inhalt der Konversation zusätzliche Absicherung von geplanten Konversationen über Mechanismen wie PIN oder ein Passwort Zuweisung von Moderationsrechten an ausgewählte Benutzende der einladenden Institution Regelungen zum Umgang mit Aufzeichnungen von Konversationen Regelungen für Endgeräte, die von mehreren Benutzenden verwendet werden Die Benutzenden MÜSSEN über Funktionen informiert werden, über die Konversationen abgesichert werden können.
  3. Ebenso MÜSSEN die Benutzenden dafür sensibilisiert werden, wie die UCC-Dienste sicher benutzt werden, insbesondere für externe Chats oder Videokonferenzen. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) SENS.7.1 deckt als übergeordnete Maßnahme die zielobjektspezifische Sensibilisierung von Benutzenden für die sichere Nutzung konkreter Systeme wie UCC-Dienste inhaltlich ab.

### → INF.9.A2 — Regelungen für mobile Arbeitsplätze (B) [Personalabteilung]
  1. Für alle Arbeiten unterwegs MUSS geregelt werden, welche Informationen außerhalb der Institution transportiert und bearbeitet werden dürfen.
  2. Es MUSS zudem geregelt werden, welche Schutzvorkehrungen dabei zu treffen sind.
  3. Dabei MUSS auch geklärt werden, unter welchen Rahmenbedingungen Mitarbeitende mit mobilen IT-Systemen auf interne Informationen ihrer Institution zugreifen dürfen.
  4. Die Mitnahme von IT-Komponenten und Datenträgern MUSS klar geregelt werden.
  5. So MUSS festgelegt werden, welche IT-Systeme und Datenträger mitgenommen werden dürfen, wer diese mitnehmen darf und welche grundlegenden Sicherheitsanforderungen dabei beachtet werden müssen.
  6. Es MUSS zudem protokolliert werden, wann und von wem welche mobilen Endgeräte außer Haus eingesetzt wurden.
  7. Die Benutzenden von mobilen Endgeräten MÜSSEN für den Wert mobiler IT-Systeme und den Wert der darauf gespeicherten Informationen sensibilisiert werden.
  8. Sie MÜSSEN über die spezifischen Gefährdungen und Maßnahmen der von ihnen benutzten IT-Systeme aufgeklärt werden. **◀ ZITIERT**
  9. Außerdem MÜSSEN sie darüber informiert werden, welche Art von Informationen auf mobilen IT-Systemen verarbeitet werden darf.
  10. Alle Benutzenden MÜSSEN auf die geltenden Regelungen hingewiesen werden, die von ihnen einzuhalten sind.
  11. Sie MÜSSEN entsprechend geschult werden
- **Satz 8** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 8) G++-Maßnahme SENS.7.1 fordert ausdrücklich die zielgruppengerechte Sensibilisierung der Nutzenden zu den spezifischen Risiken und Schutzmaßnahmen der von ihnen eingesetzten Systeme.

### → NET.2.2.A2 — Sensibilisierung und Schulung der WLAN-Benutzenden (B) [Vorgesetzte, IT-Betrieb]
  1. Die Benutzenden von WLAN-Komponenten, vornehmlich von WLAN-Clients, MÜSSEN sensibilisiert und zu den in der Nutzungsrichtlinie aufgeführten Maßnahmen geschult werden. **◀ ZITIERT**
  2. Hierfür MÜSSEN geeignete Schulungsinhalte identifiziert und festgelegt werden.
  3. Den Benutzenden MUSS genau erläutert werden, was die WLAN-spezifischen Sicherheitseinstellungen bedeuten und warum sie wichtig sind. **◀ ZITIERT**
  4. Außerdem MÜSSEN die Benutzenden auf die Gefahren hingewiesen werden, die drohen, wenn diese Sicherheitseinstellungen umgangen oder deaktiviert werden.
  5. Die Schulungsinhalte MÜSSEN immer entsprechend den jeweiligen Einsatzszenarien angepasst werden. **◀ ZITIERT**
  6. Neben der reinen Schulung zu WLAN-Sicherheitsmechanismen MÜSSEN den Benutzenden jedoch auch die WLAN-Sicherheitsrichtlinie ihrer Institution und die darin enthaltenen Maßnahmen vorgestellt werden.
  7. Ebenso MÜSSEN die Benutzenden für die möglichen Gefahren sensibilisiert werden, die von fremden WLANs ausgehen.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) SENS.7.1 fordert als übergeordnete Maßnahme die zielgruppengerechte Sensibilisierung von Nutzenden zu zielobjektspezifischen Schutzmaßnahmen und deckt damit die Schulung und Sensibilisierung von WLAN-Nutzenden inhaltlich ab.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) SENS.7.1 fordert die zielgruppengerechte Sensibilisierung zu zielobjektspezifischen Schutzmaßnahmen, was als allgemeine Fassung das Erläutern systemspezifischer Sicherheitseinstellungen und deren Bedeutung abdeckt.
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) SENS.7.1 fordert eine zielgruppengerechte Sensibilisierung zu zielobjektspezifischen Schutzmaßnahmen, was die Anpassung der Inhalte an konkrete Arbeitsumgebungen, Tätigkeiten und Einsatzszenarien inhaltlich abdeckt.

### → NET.3.3.A8 — Erstellung einer Sicherheitsrichtlinie zur VPN-Nutzung (S)
  1. Eine Sicherheitsrichtlinie zur VPN-Nutzung SOLLTE erstellt werden.
  2. Diese SOLLTE allen Mitarbeitenden bekannt gegeben werden.
  3. Die in der Sicherheitsrichtlinie beschriebenen Sicherheitsmaßnahmen SOLLTEN im Rahmen von Schulungen erläutert werden.
  4. Wird für Mitarbeitende ein VPN-Zugang eingerichtet, SOLLTE diesen ein Merkblatt mit den wichtigsten VPN-Sicherheitsmechanismen ausgehändigt werden. **◀ ZITIERT**
  5. Alle VPN-Benutzende SOLLTEN verpflichtet werden, die Sicherheitsrichtlinien einzuhalten.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) SENS.7.1 deckt die Bereitstellung eines VPN-Merkblatts als allgemeinere Anforderung zur zielgruppengerechten Sensibilisierung über zielobjektspezifische Schutzmaßnahmen ab.

### → NET.4.1.A9 — Schulung zur sicheren Nutzung von TK-Anlagen (S) [Vorgesetzte]
  1. Die Benutzenden der TK-Anlage SOLLTEN in die korrekte Verwendung von Diensten und Geräten eingewiesen werden. **◀ ZITIERT**
  2. Den Benutzenden der TK-Anlage SOLLTEN alle notwendigen Unterlagen zur Bedienung der entsprechenden Endgeräte zur Verfügung gestellt werden.
  3. Sämtliche Auffälligkeiten und Unregelmäßigkeiten der TK-Anlage SOLLTEN den entsprechenden Verantwortlichen gemeldet werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) SENS.7.1 fordert als übergeordnete Maßnahme die zielobjektspezifische Sensibilisierung und Einweisung von Nutzenden zu Schutzmaßnahmen für die von ihnen genutzten Systeme.

### → NET.4.2.A11 — Sicherer Umgang mit VoIP-Endgeräten (S) [Benutzende]
  1. Benutzende, die VoIP-Endgeräte einsetzen, SOLLTEN über die grundlegenden VoIP-Gefährdungen und Sicherheitsmaßnahmen informiert sein. **◀ ZITIERT**
  2. Außerdem SOLLTEN sie geeignete Passwörter zur Absicherung von Voicemails auswählen.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) SENS.7.1 deckt als übergeordnete Maßnahme für zielobjektspezifische Sensibilisierung die Information von Nutzenden über Gefährdungen und Schutzmaßnahmen spezifischer Zielobjekte wie VoIP-Endgeräte inhaltlich ab.

### → NET.4.2.A8 — Verschlüsselung von VoIP (S)
  1. Es SOLLTE entschieden werden, ob und welche Sprach- und Signalisierungsinformationen verschlüsselt werden sollen.
  2. Generell SOLLTEN alle VoIP-Datenpakete, die das gesicherte LAN verlassen, durch geeignete Sicherheitsmechanismen geschützt werden.
  3. Die Benutzenden SOLLTEN über die Nutzung der VoIP-Verschlüsselung informiert werden. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme fordert als allgemeine Vorgabe die zielgruppengerechte Sensibilisierung von Nutzenden zu zielobjektspezifischen Schutzmaßnahmen, was die Information über die Nutzung der VoIP-Verschlüsselung inhaltlich umfasst.

### → NET.4.3.A13 — Festlegung berechtigter Faxbedienenden (H) [Benutzende]
  1. Es SOLLTEN nur wenige Mitarbeitende ausgewählt werden, die auf das Faxgerät zugreifen dürfen.
  2. Diese Mitarbeitenden SOLLTEN ankommende Faxsendungen an die Empfangenden verteilen.
  3. Den Mitarbeitenden SOLLTE vermittelt werden, wie sie mit dem Gerät umgehen und wie sie die erforderlichen Sicherheitsmaßnahmen umsetzen können. **◀ ZITIERT**
  4. Jeder berechtigte Benutzende SOLLTE darüber unterrichtet werden, wer das Faxgerät bedienen darf und wer für das Gerät zuständig ist.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) G++ SENS.7.1 fordert die zielgruppengerechte Sensibilisierung zu zielobjektspezifischen Schutzmaßnahmen und deckt damit die Vermittlung des sicheren Umgangs und der erforderlichen Schutzmaßnahmen für die Mitarbeitenden ab.

### → ORP.3.A9 — Spezielle Schulung von exponierten Personen und Institutionen (H)
  1. Besonders exponierte Personen SOLLTEN vertiefende Schulungen in Hinblick auf mögliche Gefährdungen sowie geeignete Verhaltensweisen und Vorsichtsmaßnahmen erhalten. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) G++ SENS.7.1 fordert eine zielgruppengerechte Sensibilisierung bezüglich spezifischer Risiken und Schutzmaßnahmen im jeweiligen Arbeitsumfeld, was die vertiefende Schulung exponierter Personen inhaltlich abdeckt.

### → SYS.1.9.A9 — Sensibilisierung der Benutzenden (B)
  1. Alle Benutzenden von Terminalservern MÜSSEN über den sicheren Umgang mit Terminalservern sensibilisiert werden. **◀ ZITIERT**
  2. Den Benutzenden MÜSSEN mindestens die folgenden Inhalte vermittelt werden: grundsätzliche Funktionsweise und die Auswirkungen von Latenz und verfügbarer Bandbreite auf die Bedienbarkeit mögliche und erlaubte Speicherorte von Daten zugelassene Austauschmöglichkeiten von Informationen zwischen dem Betriebssystem des Clients und dem Terminalserver (z. B. Zwischenablage) Auswirkung des eigenen Ressourcenverbrauchs auf die zur Verfügung stehenden Ressourcen für andere Benutzende eingerichtete Rollen und Berechtigungen für Terminalserver-Zugriffe genutzte Authentisierung und Autorisierung der Benutzenden für die zur Verfügung gestellten Anwendungen maximale Sitzungsdauer und automatische Abmeldevorgänge
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) SENS.7.1 fordert die zielobjektspezifische Sensibilisierung von Nutzenden für bestimmte IT-Systeme und deckt damit die geforderte Sensibilisierung für den sicheren Umgang mit Terminalservern ab.

### → SYS.2.5.A12 — Sensibilisierung der Benutzenden (S)
  1. Alle Benutzenden von virtuellen Clients SOLLTEN über den sicheren Umgang mit virtuellen Clients sensibilisiert werden. **◀ ZITIERT**
  2. Falls die Ressourcen dynamisch anhand der abgerufenen Leistung zwischen mehreren virtuellen Clients aufgeteilt werden, SOLLTEN die Benutzenden darüber aufgeklärt werden, dass ihr Verhalten potenziell andere Benutzende beeinflussen kann.
  3. Falls die Sicherheitsanforderungen der auf virtuellen Clients ausgeführten Anwendungen besonders sind, SOLLTE kommuniziert werden, wie diese gegenüber physischen Clients abweichen. **◀ ZITIERT**
  4. Es SOLLTE auch kommuniziert werden, welche spezifischen Sicherheitsaspekte zu beachten sind. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) SENS.7.1 fordert als übergeordnete Maßnahme die zielgruppengerechte Sensibilisierung von Nutzenden zu zielobjektspezifischen Schutzmaßnahmen und deckt damit die allgemeine Sensibilisierung für den sicheren Umgang mit virtuellen Clients ab.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) SENS.7.1 deckt als allgemeine Anforderung zur zielobjektspezifischen Sensibilisierung auch die Aufklärung über abweichende Sicherheitsanforderungen spezifischer Systeme und Anwendungen materiell ab.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 4) Die Maßnahme SENS.7.1 deckt die Forderung nach der Vermittlung spezifischer Sicherheitsaspekte und Schutzmaßnahmen an die Nutzenden allgemein und zielobjektspezifisch ab.

### → SYS.3.1.A11 — Sicherstellung der Energieversorgung von Laptops (S) [Benutzende]
  1. Alle Benutzenden SOLLTEN darüber informiert werden, wie sie die Energieversorgung von Laptops im mobilen Einsatz optimal sicherstellen können. **◀ ZITIERT**
  2. Vorhandene Ersatzakkus SOLLTEN in geeigneten Hüllen gelagert und transportiert werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme SENS.7.1 deckt als allgemeine Anforderung zur zielobjektspezifischen Sensibilisierung von Nutzenden die zielgerichtete Unterweisung zur Energieversorgung von Laptops im mobilen Einsatz ab.

### → SYS.3.1.A6 — Sicherheitsrichtlinien für Laptops (S)
  1. Für Laptops SOLLTE eine Sicherheitsrichtlinie erstellt werden, die regelt, wie die Geräte benutzt werden dürfen.
  2. Die Benutzenden SOLLTEN hinsichtlich des Schutzbedarfs von Laptops und der dort gespeicherten Daten sensibilisiert werden.
  3. Auch SOLLTEN sie auf die spezifischen Gefährdungen bzw. die entsprechenden Anforderungen für die Nutzung aufmerksam gemacht werden. **◀ ZITIERT**
  4. Sie SOLLTEN außerdem darüber informiert werden, welche Art von Informationen sie auf Laptops verarbeiten dürfen.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) G++ SENS.7.1 deckt als allgemeine Maßnahme die zielobjektspezifische Sensibilisierung bezüglich Risiken und Nutzungsanforderungen für Systeme wie Laptops inhaltlich ab.

### → SYS.3.3.A3 — Sensibilisierung und Schulung der Mitarbeitenden im Umgang mit Mobiltelefonen (B)
  1. Mitarbeitende MÜSSEN für die besonderen Gefährdungen der Informationssicherheit durch Mobiltelefone sensibilisiert werden.
  2. Sie MÜSSEN in die Sicherheitsfunktion der Mobiltelefone eingewiesen sein. **◀ ZITIERT**
  3. Den Benutzenden MUSS der Prozess bekannt sein, durch den die Mobiltelefone gesperrt werden können.
  4. Die Benutzenden MÜSSEN darauf hingewiesen werden, wie die Mobiltelefone sicher und korrekt aufbewahrt werden sollten.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme SENS.7.1 deckt die Einweisung in die Sicherheitsfunktionen von Mobiltelefonen als zielobjektspezifische technische Schutzmaßnahme inhaltlich ab.

### → SYS.4.4.A9 — Regelung des Einsatzes von IoT-Geräten (S)
  1. Für jedes IoT-Gerät SOLLTE eine zuständige Person für dessen Betrieb benannt werden.
  2. Die Zuständigen SOLLTEN ausreichend über den Umgang mit dem IoT-Gerät informiert werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) SENS.7.1 deckt die zielobjektspezifische Information und Sensibilisierung der Zuständigen über den sicheren Umgang mit spezifischen Systemen wie IoT-Geräten inhaltlich ab.

### → SYS.4.5.A1 — Sensibilisierung zum sicheren Umgang mit Wechseldatenträgern (B)
  1. Alle Benutzenden MÜSSEN für den sicheren Umgang mit Wechseldatenträgern sensibilisiert werden. **◀ ZITIERT**
  2. Die Institution MUSS insbesondere darauf hinweisen, wie die Benutzenden mit Wechseldatenträgern umgehen sollten, um einem Verlust oder Diebstahl vorzubeugen und eine lange Lebensdauer zu gewährleisten.
  3. Die Institution MUSS die Benutzenden darüber informieren, dass sie keine Wechseldatenträger, die aus unbekannten Quellen stammen, an ihre IT-Systeme anschließen dürfen.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) SENS.7.1 fordert als allgemeine Maßnahme die zielobjektspezifische Sensibilisierung der Nutzenden, was den sicheren Umgang mit Wechseldatenträgern als Zielobjekt abdeckt.

### → ISMS.1.A8 — Integration der Mitarbeitenden in den Sicherheitsprozess (B) [Vorgesetzte]
  1. Alle Mitarbeitenden MÜSSEN in den Sicherheitsprozess integriert sein.
  2. Hierfür MÜSSEN sie über Hintergründe und die für sie relevanten Gefährdungen informiert sein.
  3. Sie MÜSSEN Sicherheitsmaßnahmen kennen und umsetzen, die ihren Arbeitsplatz betreffen. **◀ ZITIERT**
  4. Alle Mitarbeitenden MÜSSEN in die Lage versetzt werden, Sicherheit aktiv mitzugestalten.
  5. Daher SOLLTEN die Mitarbeitenden frühzeitig beteiligt werden, wenn Sicherheitsmaßnahmen zu planen oder organisatorische Regelungen zu gestalten sind.
  6. Bei der Einführung von Sicherheitsrichtlinien und Sicherheitswerkzeugen MÜSSEN die Mitarbeitenden ausreichend informiert sein, wie diese anzuwenden sind.
  7. Die Mitarbeitenden MÜSSEN darüber aufgeklärt werden, welche Konsequenzen eine Verletzung der Sicherheitsvorgaben haben kann.
- **Satz 3** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) SENS.7.1 fordert die zielgruppengerechte Sensibilisierung von Nutzenden zu zielobjekt- und arbeitsplatzspezifischen Schutzmaßnahmen, wodurch das Kennen und Umsetzen der den eigenen Arbeitsplatz betreffenden Maßnahmen direkt adressiert wird.

### → ORP.3.A3 — Einweisung des Personals in den sicheren Umgang mit IT (B) [Vorgesetzte, Personalabteilung, IT-Betrieb]
  1. Alle Mitarbeitenden und externen Benutzenden MÜSSEN in den sicheren Umgang mit IT-, ICS- und IoT-Komponenten eingewiesen und sensibilisiert werden, soweit dies für ihre Arbeitszusammenhänge relevant ist. **◀ ZITIERT**
  2. Dafür MÜSSEN verbindliche, verständliche und aktuelle Richtlinien zur Nutzung der jeweiligen Komponenten zur Verfügung stehen.
  3. Werden IT-, ICS- oder IoT-Systeme oder -Dienste in einer Weise benutzt, die den Interessen der Institution widersprechen, MUSS dies kommuniziert werden.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) SENS.7.1 deckt die zielgruppengerechte Sensibilisierung der Nutzenden zum sicheren Umgang mit spezifischen IT- und Produktionssystemen entsprechend ihres Arbeitskontexts inhaltlich ab.

### → ORP.3.A4 — Konzeption und Planung eines Sensibilisierungs- und Schulungsprogramms zur Informationssicherheit (S)
  1. Sensibilisierungs- und Schulungsprogramme zur Informationssicherheit SOLLTEN sich an den jeweiligen Zielgruppen orientieren. **◀ ZITIERT**
  2. Dazu SOLLTE eine Zielgruppenanalyse durchgeführt werden.
  3. Hierbei SOLLTEN Schulungsmaßnahmen auf die speziellen Anforderungen und unterschiedlichen Hintergründe fokussiert werden können. **◀ ZITIERT**
  4. Es SOLLTE ein zielgruppenorientiertes Sensibilisierungs- und Schulungsprogramm zur Informationssicherheit erstellt werden.
  5. Dieses Schulungsprogramm SOLLTE den Mitarbeitenden alle Informationen und Fähigkeiten vermitteln, die erforderlich sind, um in der Institution geltende Sicherheitsregelungen und -maßnahmen umsetzen zu können.
  6. Es SOLLTE regelmäßig überprüft und aktualisiert werden.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) Die G++-Maßnahme SENS.7.1 fordert explizit eine zielgruppengerechte Sensibilisierung und deckt damit die geforderte Zielgruppenorientierung der Sensibilisierungsmaßnahmen inhaltlich ab.
- **Satz 3** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) SENS.7.1 fordert eine zielgruppengerechte und zielobjektspezifische Sensibilisierung, was das Fokussieren der Maßnahmen auf spezielle Anforderungen und Zielgruppenhintergründe inhaltlich abdeckt.

### → ORP.3.A6 — Durchführung von Sensibilisierungen und Schulungen zur Informationssicherheit (S)
  1. Alle Mitarbeitenden SOLLTEN entsprechend ihren Aufgaben und Verantwortlichkeiten zu Informationssicherheitsthemen geschult werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 1) Satz 1 fordert die aufgaben- und verantwortungsbezogene Schulung aller Mitarbeitenden zu Informationssicherheitsthemen, was sich direkt mit der zielgruppengerechten und spezifischen Sensibilisierung deckt.


## SENS.9.6 — Mitnahme ins Ausland  [1 Paare]

**Statement (normativ):** Sensibilisierung für Nutzende KANN die Mitnahme nicht erforderlicher IT-Systeme und Datenträger bei Auslandsreisen untersagen.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** erhöht
**Guidance (nicht normativ):** Auf Auslandsreisen ist das Risiko für Spionage erhöht und der Rechtsschutz für Betroffene typischerweise geringer, insbesondere im EU-Ausland. Es ist daher ratsam, die mitgenommenen Geräte und sensiblen Informationen auf das für das Geschäft erforderliche Mindestmaß zu beschränken und stattdessen nach der Rückkehr an einem besser geschützten Standort weiter daran zu arbeiten. Welche IT-Systeme und Datenträger erforderlich sind, ergibt sich aus der Festlegung erlaubter Datenlokationen sowie den Aufgaben der Nutzenden. Ist die Nutzung von Informationen oder Assets der Institution im Ausland nicht vorgesehen (vgl. Anforderung Datenlokationen), dann ist die Anforderung entbehrlich.

### → CON.7.A13 — Mitnahme notwendiger Daten und Datenträger (S) [Benutzende]
  1. Vor Reiseantritt SOLLTEN Benutzende prüfen, welche Daten während der Reise nicht unbedingt auf den IT-Systemen gebraucht werden.
  2. Ist es nicht notwendig, diese Daten auf den Geräten zu lassen, SOLLTEN diese sicher gelöscht werden.
  3. Ist es nötig, schützenswerte Daten mit auf Reisen zu nehmen, SOLLTE dies nur in verschlüsselter Form erfolgen.
  4. Darüber hinaus SOLLTE schriftlich geregelt sein, welche mobilen Datenträger auf Auslandsreisen mitgenommen werden dürfen und welche Sicherheitsmaßnahmen dabei zu berücksichtigen sind (z. B. Schutz vor Schadsoftware, Verschlüsselung geschäftskritischer Daten, Aufbewahrung mobiler Datenträger). **◀ ZITIERT**
  5. Die Mitarbeitenden SOLLTEN diese Regelungen vor Reiseantritt kennen und beachten.
  6. Diese sicherheitstechnischen Anforderungen SOLLTEN sich nach dem Schutzbedarf der zu bearbeitenden Daten im Ausland und der Daten, auf die zugegriffen werden soll, richten.
- **Satz 4** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 4) Satz 4 fordert eine schriftliche Regelung darüber, welche mobilen Datenträger auf Auslandsreisen mitgenommen werden dürfen, was sich direkt mit der Einschränkung der Mitnahme von Datenträgern bei Auslandsreisen in SENS.9.6 überschneidet.


## SENS.4.1 — Personengebundene Authentisierungsmittel  [6 Paare]

**Statement (normativ):** Sensibilisierung für Nutzende SOLLTE zum Umgang mit Authentisierungsmitteln im Einklang mit den zugehörigen Anforderungen des Identitäts- und Berechtigungsmanagements sensibilisieren.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Zur Definition von Authentisierungsmitteln siehe Glossar/Namensräume. Um Missbrauch zu vermeiden ist es wichtig, diese (1) geschützt aufzubewahren und niemals weiterzugeben, (2) den Verdacht, dass ein Passwort oder Token kompromittiert sein könnte, sofort zu melden und (3) aufmerksam gegenüber ungewöhnlichen Login-Masken oder Aufforderungen zu sein, die Zugangsdaten außerhalb der gewohnten Systeme einzugeben.

### → ORP.4.A5 — Vergabe von Zutrittsberechtigungen (B) [IT-Betrieb]
  1. Es MUSS festgelegt werden, welche Zutrittsberechtigungen an welche Personen im Rahmen ihrer Funktion vergeben bzw. ihnen entzogen werden.
  2. Die Ausgabe bzw. der Entzug von verwendeten Zutrittsmittel wie Chipkarten MUSS dokumentiert werden.
  3. Wenn Zutrittsmittel kompromittiert wurden, MÜSSEN sie ausgewechselt werden.
  4. Die Zutrittsberechtigten SOLLTEN für den korrekten Umgang mit den Zutrittsmitteln geschult werden. **◀ ZITIERT**
  5. Bei längeren Abwesenheiten SOLLTEN berechtigte Personen vorübergehend gesperrt werden.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die Maßnahme SENS.4.1 deckt die Schulung bzw. Sensibilisierung von Nutzenden zum korrekten Umgang mit Authentisierungs- und Zutrittsmitteln als allgemeinere Formulierung inhaltlich ab.

### → ORP.4.A7 — Vergabe von Zugriffsrechten (B) [IT-Betrieb]
  1. Es MUSS festgelegt werden, welche Zugriffsrechte an welche Personen im Rahmen ihrer Funktion vergeben bzw. ihnen entzogen werden.
  2. Werden im Rahmen der Zugriffskontrolle Chipkarten oder Token verwendet, so MUSS die Ausgabe bzw. der Entzug dokumentiert werden.
  3. Die Anwendenden SOLLTEN für den korrekten Umgang mit Chipkarten oder Token geschult werden. **◀ ZITIERT**
  4. Bei längeren Abwesenheiten SOLLTEN berechtigte Personen vorübergehend gesperrt werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die Sensibilisierung der Nutzenden zum Umgang mit personengebundenen Authentisierungsmitteln deckt die Schulung der Anwendenden für den korrekten Umgang mit Chipkarten oder Token inhaltlich als übergeordnete Anforderung ab.

### → SYS.2.1.A28 — Verschlüsselung der Clients (H)
  1. Wenn vertrauliche Informationen auf den Clients gespeichert werden, SOLLTEN mindestens die schutzbedürftigen Dateien sowie ausgewählte Dateisystembereiche oder besser die gesamten Datenträger verschlüsselt werden.
  2. Hierfür SOLLTE ein eigenes Konzept erstellt und die Details der Konfiguration besonders sorgfältig dokumentiert werden.
  3. In diesem Zusammenhang SOLLTEN die Authentisierung (z. B. Passwort, PIN, Token), die Ablage der Wiederherstellungsinformationen, die zu verschlüsselnden Laufwerke und die Schreibrechte auf unverschlüsselte Datenträger geregelt werden.
  4. Der Zugriff auf das genutzte Schlüsselmaterial MUSS angemessen geschützt sein.
  5. Benutzende SOLLTEN darüber aufgeklärt werden, wie sie sich bei Verlust eines Authentisierungsmittels zu verhalten haben. **◀ ZITIERT**
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 5) Die Maßnahme SENS.4.1 deckt die Sensibilisierung von Nutzenden zum ordnungsgemäßen Umgang mit Authentisierungsmitteln einschließlich der Meldung und des Verhaltens bei Verlust oder Kompromittierung inhaltlich ab.

### → ORP.4.A19 — Einweisung aller Mitarbeitenden in den Umgang mit Authentisierungsverfahren und -mechanismen (S) [Benutzende, IT-Betrieb]
  1. Alle Mitarbeitende SOLLTEN in den korrekten Umgang mit dem Authentisierungsverfahren eingewiesen werden. **◀ ZITIERT**
  2. Es SOLLTE verständliche Richtlinien für den Umgang mit Authentisierungsverfahren geben.
  3. Die Mitarbeitenden SOLLTEN über relevante Regelungen informiert werden.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) SENS.4.1 fordert die Sensibilisierung bzw. Einweisung der Nutzenden zum ordnungsgemäßen Umgang mit Authentisierungsmitteln und deckt damit die Einweisung in Authentisierungsverfahren aus Satz 1 direkt ab.

### → ORP.4.A6 — Vergabe von Zugangsberechtigungen (B) [IT-Betrieb]
  1. Es MUSS festgelegt werden, welche Zugangsberechtigungen an welche Personen im Rahmen ihrer Funktion vergeben bzw. ihnen entzogen werden.
  2. Werden Zugangsmittel wie Chipkarten verwendet, so MUSS die Ausgabe bzw. der Entzug dokumentiert werden.
  3. Wenn Zugangsmittel kompromittiert wurden, MÜSSEN sie ausgewechselt werden.
  4. Die Zugangsberechtigten SOLLTEN für den korrekten Umgang mit den Zugangsmitteln geschult werden. **◀ ZITIERT**
  5. Bei längeren Abwesenheiten SOLLTEN berechtigte Personen vorübergehend gesperrt werden.
- **Satz 4** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die G++-Maßnahme fordert explizit die Sensibilisierung von Nutzenden zum korrekten Umgang mit Authentisierungs- bzw. Zugangsmitteln im Rahmen des Berechtigungsmanagements.

### → ORP.4.A8 — Regelung des Passwortgebrauchs (B) [Benutzende, IT-Betrieb]
  1. Die Institution MUSS den Passwortgebrauch verbindlich regeln (siehe auch ORP.4.A22 Regelung zur Passwortqualität und ORP.4.A23 Regelung für passwortverarbeitende Anwendungen und IT-Systeme).
  2. Dabei MUSS geprüft werden, ob Passwörter als alleiniges Authentisierungsverfahren eingesetzt werden sollen, oder ob andere Authentisierungsmerkmale bzw. -verfahren zusätzlich zu oder anstelle von Passwörtern verwendet werden können.
  3. Passwörter DÜRFEN NICHT mehrfach verwendet werden.
  4. Für jedes IT-System bzw. jede Anwendung MUSS ein eigenständiges Passwort verwendet werden.
  5. Passwörter, die leicht zu erraten sind oder in gängigen Passwortlisten geführt werden, DÜRFEN NICHT verwendet werden.
  6. Passwörter MÜSSEN geheim gehalten werden.
  7. Sie DÜRFEN NUR den Benutzenden persönlich bekannt sein.
  8. Passwörter DÜRFEN NUR unbeobachtet eingegeben werden.
  9. Passwörter DÜRFEN NICHT auf programmierbaren Funktionstasten von Tastaturen oder Mäusen gespeichert werden.
  10. Ein Passwort DARF NUR für eine Hinterlegung für einen Notfall schriftlich fixiert werden.
  11. Es MUSS dann sicher aufbewahrt werden.
  12. Die Nutzung eines Passwort-Managers SOLLTE geprüft werden.
  13. Bei Passwort-Managern mit Funktionen oder Plug-ins, mit denen Passwörter über Onlinedienste Dritter synchronisiert oder anderweitig an Dritte übertragen werden, MÜSSEN diese Funktionen und Plug-ins deaktiviert werden.
  14. Ein Passwort MUSS gewechselt werden, wenn es unautorisierten Personen bekannt geworden ist oder der Verdacht dazu besteht. **◀ ZITIERT**
- **Satz 14** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 14) Satz 14 regelt das Vorgehen beim Verdacht auf Kompromittierung eines Passworts, was inhaltlich direkt dem in SENS.4.1 genannten Sensibilisierungsaspekt zum Umgang bei Kompromittierungsverdacht entspricht.


## SENS.4.1.1 — Verdeckte Eingabe  [3 Paare]

**Statement (normativ):** Sensibilisierung für Nutzende SOLLTE zur verdeckten Eingabe von Zugangsdaten sensibilisieren.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Werden Zugangsdaten unverdeckt eingegeben, so könnten diese durch Shoulder Surfing kompromittiert werden, etwa in überfüllten Bereichen, Aufzügen oder während Videokonferenzen. Die verdeckte Eingabe umfasst dabei alle Tätigkeiten, die verhindern, dass Unbefugte die Eingabe von Passwörtern, PINs oder anderen Authentifizierungsdaten visuell erfassen können, sei es durch direkte Sichtbarkeit oder durch das Verfolgen von Handbewegungen und Tastaturanschlägen. Beispiele sind die bewusste Positionierung des Körpers oder der Hand als natürlicher Sichtschutz bei der Eingabe, sowie die Nutzung von Sichtschutzfolien auf Bildschirmen in öffentlichen Bereichen oder beim mobilen Arbeiten.

### → CON.7.A4 — Verwendung von Sichtschutz-Folien (B) [Benutzende]
  1. Benutzende MÜSSEN insbesondere im Ausland darauf achten, dass bei der Arbeit mit mobilen IT-Geräten keine schützenswerten Informationen ausgespäht werden können.
  2. Dazu MUSS ein angemessener Sichtschutz verwendet werden, der den gesamten Bildschirm des jeweiligen Gerätes umfasst und ein Ausspähen von Informationen erschwert. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 2) Satz 2 fordert den Einsatz eines angemessenen Sichtschutzes zur Verhinderung von visuellem Ausspähen, was sich mit den Maßnahmen gegen Shoulder Surfing aus SENS.4.1.1 überschneidet.

### → INF.9.A12 — Nutzung eines Bildschirmschutzes (S) [Mitarbeitende]
  1. Wenn IT-Systeme an mobilen Arbeitsplätzen genutzt werden, SOLLTEN die Mitarbeitenden einen Sichtschutz für die Bildschirme der IT-Systeme verwenden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 1) Satz 1 fordert den Einsatz eines Sichtschutzes bei mobiler Nutzung zum Schutz vor unbefugtem Einblick (Shoulder Surfing), was sich mit den Inhalten der verdeckten Eingabe deckt.

### → ORP.4.A8 — Regelung des Passwortgebrauchs (B) [Benutzende, IT-Betrieb]
  1. Die Institution MUSS den Passwortgebrauch verbindlich regeln (siehe auch ORP.4.A22 Regelung zur Passwortqualität und ORP.4.A23 Regelung für passwortverarbeitende Anwendungen und IT-Systeme).
  2. Dabei MUSS geprüft werden, ob Passwörter als alleiniges Authentisierungsverfahren eingesetzt werden sollen, oder ob andere Authentisierungsmerkmale bzw. -verfahren zusätzlich zu oder anstelle von Passwörtern verwendet werden können.
  3. Passwörter DÜRFEN NICHT mehrfach verwendet werden.
  4. Für jedes IT-System bzw. jede Anwendung MUSS ein eigenständiges Passwort verwendet werden.
  5. Passwörter, die leicht zu erraten sind oder in gängigen Passwortlisten geführt werden, DÜRFEN NICHT verwendet werden.
  6. Passwörter MÜSSEN geheim gehalten werden.
  7. Sie DÜRFEN NUR den Benutzenden persönlich bekannt sein.
  8. Passwörter DÜRFEN NUR unbeobachtet eingegeben werden. **◀ ZITIERT**
  9. Passwörter DÜRFEN NICHT auf programmierbaren Funktionstasten von Tastaturen oder Mäusen gespeichert werden.
  10. Ein Passwort DARF NUR für eine Hinterlegung für einen Notfall schriftlich fixiert werden.
  11. Es MUSS dann sicher aufbewahrt werden.
  12. Die Nutzung eines Passwort-Managers SOLLTE geprüft werden.
  13. Bei Passwort-Managern mit Funktionen oder Plug-ins, mit denen Passwörter über Onlinedienste Dritter synchronisiert oder anderweitig an Dritte übertragen werden, MÜSSEN diese Funktionen und Plug-ins deaktiviert werden.
  14. Ein Passwort MUSS gewechselt werden, wenn es unautorisierten Personen bekannt geworden ist oder der Verdacht dazu besteht.
- **Satz 8** | Relation GS++→ED23: `intersects-with` | Fundrichtung: beide
  Begründung: (Teilanforderung 8) Die G++-Maßnahme fordert explizit die Sensibilisierung zur verdeckten Eingabe von Zugangsdaten, was inhaltlich genau der Forderung entspricht, dass Passwörter nur unbeobachtet eingegeben werden dürfen.

