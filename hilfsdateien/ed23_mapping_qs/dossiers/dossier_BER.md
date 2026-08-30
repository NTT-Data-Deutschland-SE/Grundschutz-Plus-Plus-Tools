# Review-Dossier Praktik BER

Praktik BER: 74 Controls mit Mapping, 406 Paare gesamt. Gesampelt: 5 Controls (max/min/median Paarzahl + 2 zufällig).

## BER.3.21 — Dienstekonten  [3 Paare]

**Statement (normativ):** Berechtigung für Hostsysteme SOLLTE eine automatische Verwaltung der Zugangsdaten von Dienste-Konten aktivieren.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Eine automatische Verwaltung der Zugangsdaten von Dienste-Konten bezeichnet in diesem Kontext die technische Fähigkeit, Passwörter, Schlüssel oder Tokens solcher Konten – im Englischen häufig als service accounts oder machine identities bezeichnet – durch spezialisierte Systeme ohne manuelles Eingreifen zu erzeugen, zu speichern, regelmäßig zu erneuern und kontrolliert zu verteilen. Zugangsdaten sind hierbei sämtliche Authentifizierungsinformationen, die einem Dienst ermöglichen, auf Ressourcen anderer Systeme zuzugreifen, beispielsweise API-Schlüssel, SSH-Keys oder Anmeldedaten für Datenbanken. Dienste-Konten werden meist von Applikationen, Hintergrunddiensten oder Automatisierungsprozessen genutzt und unterscheiden sich von personenbezogenen Benutzerkonten dadurch, dass sie keinem Individuum zugeordnet sind, sondern einem technischen Zweck dienen. Erfolgt bei Zugangskonten für automatisierte Dienste eine automatische Rotation von Passwörtern oder Anmeldezertifikaten, so werden statische Passwörter, die Ablage von Zugangsdaten auf Netzlaufwerken oder plötzliche Fehlfunktionen durch Zertifikatsablauf vermieden. Ihre automatische Verwaltung kann durch zentrale Passworttresore (password vaults), Identitätsmanagementsysteme (Identity and Access Management, IAM) oder Secret-Management-Lösungen realisiert werden.

### → APP.2.2.A16 — Härtung der AD-DS-Konten (B)
  1. Built-in-AD-DS-Konten MÜSSEN mit komplexen Passwörtern versehen werden.
  2. Sie DÜRFEN NUR als Notfallkonten dienen.
  3. Das Built-in „Guest“- / „Gast“-Konto MUSS deaktiviert werden.
  4. Die Berechtigungen für die Gruppe „Everyone“ / „Jeder“ MUSS beschränkt werden.
  5. Privilegierte Konten MÜSSEN Mitglied der Gruppe „Protected Users“ / „Geschütze Benutzer“ sein.
  6. Für Dienstkonten MÜSSEN (Group) Managed Service Accounts verwendet werden. **◀ ZITIERT**
  7. Vor dem Löschen nicht mehr verwendeter Konten MUSS geprüft werden, nach welcher Aufbewahrungsfrist diese gelöscht werden können.
  8. Dabei MÜSSEN die Auswirkungen auf die Detektion und gesetzliche Aufbewahrungs- und Löschfristen berücksichtigt werden.
  9. Der Zugriff auf das AdminSDHolder-Objekt SOLLTE zum Schutz der Berechtigungen besonders geschützt sein.
- **Satz 6** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 6) BER.3.21 fordert die automatische Verwaltung der Zugangsdaten von Dienstekonten, was die technologieunabhängige Entsprechung zum Einsatz von (Group) Managed Service Accounts in AD DS darstellt.

### → SYS.1.2.2.A6 — Sichere Authentisierung und Autorisierung in Windows Server 2012 (S)
  1. In Windows Server 2012 R2 SOLLTEN alle Konten von Benutzenden Mitglied der Sicherheitsgruppe „Geschützte Nutzer“ sein.
  2. Konten für Dienste und Computer SOLLTEN NICHT Mitglied von „Geschützte Nutzer“ sein.
  3. Dienste-Konten in Windows Server 2012 SOLLTEN Mitglied der Gruppe „Managed Service Account“ sein. **◀ ZITIERT**
  4. Der PPL-Schutz des Local Credential Store LSA SOLLTE aktiviert werden.
  5. Der Einsatz dynamischer Zugriffsregeln auf Ressourcen SOLLTE bevorzugt werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) BER.3.21 fordert die automatische Verwaltung von Zugangsdaten für Dienstekonten, was das allgemeine Schutzziel hinter dem Einsatz von Managed Service Accounts in Windows darstellt.

### → SYS.1.2.3.A5 — Sichere Authentisierung und Autorisierung in Windows Server (S)
  1. In Windows Server SOLLTEN alle Konten von Benutzenden Mitglied der Sicherheitsgruppe „Protected Users“ sein.
  2. Konten für Dienste und Computer SOLLTEN NICHT Mitglied von „Protected Users“ sein.
  3. Dienste-Konten in Windows Server SOLLTEN Mitglied der Gruppe „Managed Service Account“ sein. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 3) G++ BER.3.21 fordert die allgemeine automatische Verwaltung der Zugangsdaten von Dienstekonten, was der Windows-spezifischen Umsetzung mittels Managed Service Accounts (MSA/gMSA) entspricht.


## BER.4.1 — Prinzip der geringsten Berechtigungen  [83 Paare]

**Statement (normativ):** Berechtigung SOLLTE die Vergabe von Berechtigungen nach dem Prinzip der geringsten Berechtigungen einschränken.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Das Prinzip der geringsten Berechtigungen, im Englischen als Principle of Least Privilege (PoLP) bekannt, besagt, dass Nutzende, Prozesse oder Systeme nur die minimal notwendigen Zugriffsrechte erhalten dürfen, um die ihnen jeweils zugewiesenen Aufgaben zu erfüllen. Dies dient primär der Minimierung der Angriffsfläche und der Begrenzung potenzieller Schäden. Sollte beispielsweise ein Zugangskonto durch Phishing kompromittiert werden, könnte ein Angreifer ohne dieses Prinzip weitreichenden Zugriff auf kritische Daten oder Systeme erlangen und diese manipulieren, exfiltrieren oder verschlüsseln. Die konsequente Anwendung dieses Grundsatzes kann die Ausbreitung von Schadsoftware nach einem ersten Eindringen erheblich erschweren und sicherstellen, dass Mitarbeitende nur jene Informationen einsehen, die für ihre Tätigkeit unmittelbar relevant sind. Hierdurch wird auch das Risiko von Datendiebstahl durch Innentäter reduziert. Es empfiehlt sich als Ergänzung hier auch das "Need to know"-Prinzip zu betrachten, da sich beide Prinzipien ergänzen. Während das "Least Privilege"-Prinzip auf Systremrechte, Rollen und Berechtigungen fokussiert, liegt der Fokus des "Need to know"-Prinzips mehr auf Informationen und Datenzugriff. Zur sinnvollen Umsetzung kann die Institution ein rollenbasiertes Berechtigungskonzept (Role-Based Access Control, RBAC) etablieren, bei dem Berechtigungen nicht an einzelne Personen, sondern an vordefinierte Rollen (z.B. "Finanzbuchhaltung" oder "Netzwerkadministrator") gebunden werden. Für die Einführung in eine bestehende Umgebung kann ein gestuftes Vorgehen gewählt werden: (1) Zunächst wird ein Überwachungsmodus ("Audit-Only") aktiviert, der protokolliert, welche Zugriffe durch eine strengere Richtlinie verweigert würden, ohne sie tatsächlich zu blockieren. (2) Anschließend werden diese Protokolle analysiert, um legitime, für den Geschäftsbetrieb notwendige Zugriffe zu identifizieren und diese gezielt in die jeweiligen Rollen und Berechtigungsgruppen aufzunehmen. (3) Erst wenn keine legitimen Zugriffe mehr in den Protokollen als "verweigert" auftauchen, wird die Richtlinie scharf geschaltet und blockiert aktiv alle nicht explizit erlaubten Zugriffe. Alle relevanten Anforderungen zur Vergabe von Berechtigungen können mit den Handlungsworten "authentifizieren", "autorisieren" und "einschränken" gefunden werden.

### → APP.1.4.A5 — Minimierung und Kontrolle von App-Berechtigungen (B) [Fachverantwortliche]
  1. Sicherheitsrelevante Berechtigungseinstellungen MÜSSEN so fixiert werden, dass sie nicht durch Personen oder Apps geändert werden können.
  2. Wo dies technisch nicht möglich ist, MÜSSEN die Berechtigungseinstellungen regelmäßig geprüft und erneut gesetzt werden.
  3. Bevor eine App in einer Institution eingeführt wird, MUSS sichergestellt werden, dass sie nur die minimal benötigten App-Berechtigungen für ihre Funktion erhält. **◀ ZITIERT**
  4. Nicht unbedingt notwendige Berechtigungen MÜSSEN hinterfragt und gegebenenfalls unterbunden werden. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 3) Satz 3 fordert explizit die Umsetzung des Prinzips der minimal benötigten Berechtigungen (Least Privilege) bei der Einführung von Apps.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Das in BER.4.1 geforderte Prinzip der geringsten Berechtigungen verlangt die Einschränkung von Berechtigungen auf das Notwendigste und deckt damit das Hinterfragen und Unterbinden nicht benötigter Berechtigungen direkt ab.

### → APP.2.1.A13 — Absicherung der Kommunikation mit Verzeichnisdiensten (S)
  1. Werden vertrauliche Informationen übertragen, SOLLTE die gesamte Kommunikation mit dem Verzeichnisdienst über ein sicheres Protokoll entsprechend der Technischen Richtlinie TR-02102 des BSI (z. B. TLS) verschlüsselt werden.
  2. Der Datenaustausch zwischen Client und Verzeichnisdienst-Server SOLLTE abgesichert werden.
  3. Es SOLLTE definiert werden, auf welche Daten zugegriffen werden darf. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) BER.4.1 fordert die Beschränkung von Zugriffsrechten nach dem Minimalprinzip (Need-to-know / Least Privilege), was die Definition der zulässigen Datenzugriffe grundlegend abdeckt.

### → APP.2.1.A19 — Umgang mit anonymen Zugriffen auf Verzeichnisdienste (S)
  1. Sollen anonymen Benutzenden auf einzelne Teilbereiche des Verzeichnisbaums Zugriffe eingeräumt werden, so SOLLTE hierfür ein Proxy-Dienst vorgelagert werden.
  2. Dieser Proxy-Dienst SOLLTE über ein gesondertes Konto, einen sogenannten Proxy-User, auf den eigentlichen Verzeichnisdienst zugreifen.
  3. Die Zugriffsrechte für diesen Proxy-User SOLLTEN hinreichend restriktiv vergeben werden. **◀ ZITIERT**
  4. Sie SOLLTEN zudem wieder komplett entzogen werden, wenn der Account nicht mehr gebraucht wird.
  5. Damit nicht versehentlich schutzbedürftige Informationen herausgegeben werden, SOLLTE die Suchfunktion des Verzeichnisdienstes dem Einsatzzweck angemessen eingeschränkt werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die restriktive Vergabe von Zugriffsrechten für den Proxy-User ist ein konkreter Anwendungsfall des in BER.4.1 geforderten Prinzips der geringsten Berechtigungen.

### → APP.2.1.A6 — Sicherer Betrieb von Verzeichnisdiensten (B)
  1. Die Sicherheit des Verzeichnisdienstes MUSS im Betrieb permanent aufrechterhalten werden.
  2. Alle den Betrieb eines Verzeichnisdienst-Systems betreffenden Richtlinien, Regelungen und Prozesse SOLLTEN nachvollziehbar dokumentiert und aktuell gehalten werden.
  3. Sofern der Verzeichnisdienst zur Verwaltung von Anmeldedaten verwendet wird, MÜSSEN dedizierte Clients bei der Fernwartung eingesetzt werden.
  4. Der Zugriff auf alle Administrationswerkzeuge MUSS für normale Benutzende unterbunden werden. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Das Unterbinden des Zugriffs auf Administrationswerkzeuge für normale Benutzende ist eine direkte Anwendung des in BER.4.1 geforderten Prinzips der geringsten Berechtigungen.

### → APP.2.2.A1 — Planung von Active Directory Domain Services (B) [Fachverantwortliche]
  1. Es MUSS eine Funktionsebene für die Domäne(n) und die Gesamtstruktur von mindestens Windows Server 2016 gewählt werden.
  2. Ein bedarfsgerechtes Berechtigungskonzept für die Domäne(n) und die Gesamtstruktur MUSS entworfen werden.
  3. Dabei MUSS berücksichtigt werden, dass zwischen den einzelnen Domänen einer Gesamtstruktur produktbedingt keine Sicherheitsgrenzen bestehen und daher keine sichere Begrenzung der administrativen Bereiche innerhalb einer Gesamtstruktur möglich ist.
  4. Administrative Delegationen MÜSSEN mit restriktiven und bedarfsgerechten Berechtigungen ausgestattet sein. **◀ ZITIERT**
  5. Die geplante Struktur einschließlich etwaiger Schema-Änderungen MUSS nachvollziehbar dokumentiert sein.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) BER.4.1 fordert die Vergabe von Berechtigungen nach dem Least-Privilege-Prinzip und deckt damit die geforderte restriktive und bedarfsgerechte Rechtevergabe bei administrativen Delegationen ab.

### → APP.2.2.A16 — Härtung der AD-DS-Konten (B)
  1. Built-in-AD-DS-Konten MÜSSEN mit komplexen Passwörtern versehen werden.
  2. Sie DÜRFEN NUR als Notfallkonten dienen.
  3. Das Built-in „Guest“- / „Gast“-Konto MUSS deaktiviert werden.
  4. Die Berechtigungen für die Gruppe „Everyone“ / „Jeder“ MUSS beschränkt werden. **◀ ZITIERT**
  5. Privilegierte Konten MÜSSEN Mitglied der Gruppe „Protected Users“ / „Geschütze Benutzer“ sein.
  6. Für Dienstkonten MÜSSEN (Group) Managed Service Accounts verwendet werden.
  7. Vor dem Löschen nicht mehr verwendeter Konten MUSS geprüft werden, nach welcher Aufbewahrungsfrist diese gelöscht werden können.
  8. Dabei MÜSSEN die Auswirkungen auf die Detektion und gesetzliche Aufbewahrungs- und Löschfristen berücksichtigt werden.
  9. Der Zugriff auf das AdminSDHolder-Objekt SOLLTE zum Schutz der Berechtigungen besonders geschützt sein.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die G++-Maßnahme fordert die allgemeine Einschränkung von Berechtigungen nach dem Least-Privilege-Prinzip, was die spezifische Beschränkung der Rechte für die Gruppe 'Everyone/Jeder' als Anwendungsfall abdeckt.

### → APP.2.2.A17 — Anmelderestriktionen für hochprivilegierte Konten der Gesamtstruktur auf Clients und Servern (B)
  1. Die Anmeldung von hochpriviligierten Domänen- und Gesamtstruktur-Konten und Gruppen MUSS technisch auf die minimal notwendigen IT-Systeme einschränkt werden. **◀ ZITIERT**
  2. Insbesondere die Anmeldung von Mitgliedern der Gruppen „Schema Admins“ / „Schema-Administratoren“, „Enterprise Admins“ / „Enterprise-Administratoren“ und „Domain Admins“ / „Domänen-Administratoren“ SOLLTE technisch auf den Domänencontroller beschränkt werden, eine Anmeldung an anderen IT-Systemen ist für diese Gruppen also zu unterbinden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme BER.4.1 fordert als übergeordnetes Prinzip die Vergabe von Rechten nach dem Least-Privilege-Prinzip, was die Beschränkung von Anmeldebefugnissen hochprivilegierter Konten auf das minimale Maß als Spezialfall abdeckt.

### → APP.2.2.A18 — Einschränken des Hinzufügens neuer Computer-Objekte zur Domäne (B)
  1. Die Berechtigung, in der Domäne neue Computer-Objekte hinzuzufügen, MUSS auf die notwendigen administrativen Konten beschränkt werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) BER.4.1 fordert die allgemeine Beschränkung von Berechtigungen nach dem Principle of Least Privilege, was die domänenspezifische Einschränkung der Berechtigung zum Hinzufügen von Computer-Objekten auf administrative Konten maßgeblich abdeckt.

### → APP.2.2.A23 — Regelmäßige Analyse von Berechtigungen und resultierenden Angriffspfaden (H)
  1. Aufgrund der Komplexität von Berechtigungen, die nicht immer unmittelbar ersichtlich sind, SOLLTE eine regelmäßige Analyse der Berechtigungsstrukturen im AD DS vorgenommen werden.
  2. Insbesondere Berechtigungen, die durch die Integration von Anwendungen in AD DS entstehen (beispielsweise Microsoft Exchange) SOLLTEN kritisch auf ihre Notwendigkeit hin geprüft und auf die minimal notwendigen Berechtigungen reduziert werden.
  3. Aktualisierungen können ebenfalls auch Berechtigungsstrukturen im AD DS ändern, daher SOLLTE die Analyse auch nach entsprechenden Aktualisierungen durchgeführt werden.
  4. Mögliche Angriffspfade über die Berechtigungen der AD-DS-Konten, die beispielsweise bei Kompromittierung von Konten zur Kompromittierung der Domäne bzw. der vollständigen Gesamtstruktur führen, SOLLTEN möglichst gering sein. **◀ ZITIERT**
  5. Die Aktivitäten der verbleibenden, als kritisch identifizierten Konten SOLLTEN besonders überwacht werden.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Das Prinzip der geringsten Berechtigungen (BER.4.1) fordert die minimale Rechtevergabe, um Angriffsflächen und potenzielle Angriffspfade bei Kompromittierungen wirksam zu reduzieren.

### → APP.2.2.A3 — Planung der Gruppenrichtlinien unter Windows (B)
  1. Es MUSS ein Konzept zur Einrichtung von Gruppenrichtlinien vorliegen.
  2. Mehrfachüberdeckungen MÜSSEN beim Gruppenrichtlinienkonzept möglichst vermieden werden.
  3. In der Dokumentation des Gruppenrichtlinienkonzepts MÜSSEN Ausnahmeregelungen erkannt werden können.
  4. Alle Gruppenrichtlinienobjekte MÜSSEN durch restriktive Zugriffsrechte geschützt sein. **◀ ZITIERT**
  5. Für die Parameter in allen Gruppenrichtlinienobjekten MÜSSEN sichere Vorgaben festgelegt sein.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die G++-Maßnahme BER.4.1 fordert die allgemeine Vergabe von Berechtigungen nach dem Principle of Least Privilege, was den Schutz von Gruppenrichtlinienobjekten durch restriktive Zugriffsrechte als spezifischen Anwendungsfall abdeckt.

### → APP.2.2.A7 — Umsetzung sicherer Verwaltungsmethoden für Active Directory (B) [Fachverantwortliche]
  1. Es MUSS sichergestellt sein, dass die Konten von Dienste-Administrierenden ausschließlich von Mitgliedern der Gruppe der Dienste-Administrierenden verwaltet werden.
  2. Bevor Konten vordefinierten AD-DS-Gruppen hinzugefügt werden, SOLLTE geprüft werden, ob alle der Gruppe zugehörigen Rechte für die mit den Konten verbundenen Tätigkeiten erforderlich sind. **◀ ZITIERT**
  3. Den Gruppen „Schema-Admins“ / „Schema-Administratoren“ sowie der Gruppe „Enterprise Admins“ / „Organisations-Administratoren“ und „Domain Admins“ / „Domänen-Administratoren“ SOLLTEN neben dem AD-DS-Built-In-Konto für Administrierende weitere administrative Konten nur temporär für den Zeitraum zugewiesen werden, in dem sie diese Berechtigungen benötigen.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die Forderung, vor der Zuweisung zu prüfen, ob alle Gruppenrechte für die Tätigkeit erforderlich sind, stellt eine konkrete AD-spezifische Anwendung des Prinzips der geringsten Berechtigungen (Least Privilege) dar, welches durch BER.4.1 allgemein verlangt wird.

### → APP.3.1.A4 — Kontrolliertes Einbinden von Dateien und Inhalten (B)
  1. Falls eine Webanwendung oder ein Webservice eine Upload-Funktion für Dateien anbietet, MUSS diese Funktion durch den IT-Betrieb so weit wie möglich eingeschränkt werden.
  2. Insbesondere MÜSSEN die erlaubte Dateigröße, erlaubte Dateitypen und erlaubte Speicherorte festgelegt werden.
  3. Es MUSS festgelegt werden, welche Clients die Funktion verwenden dürfen. **◀ ZITIERT**
  4. Auch MÜSSEN Zugriffs- und Ausführungsrechte restriktiv gesetzt werden. **◀ ZITIERT**
  5. Zudem MUSS sichergestellt werden, dass Clients Dateien nur im vorgegebenen erlaubten Speicherort speichern können.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme BER.4.1 fordert die Vergabe von Berechtigungen nach dem Minimalprinzip einzuschränken, was als allgemeine Fassung die Festlegung und Beschränkung berechtigter Clients für Anwendungsfunktionen umfasst.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die G++-Maßnahme BER.4.1 fordert die generelle Vergabe von Berechtigungen nach dem Least-Privilege-Prinzip und deckt damit das restriktive Setzen von Zugriffs- und Ausführungsrechten als allgemeinen Fall ab.

### → APP.3.6.A6 — Absicherung von dynamischen DNS-Updates (B)
  1. Es MUSS sichergestellt werden, dass nur legitimierte IT-Systeme Domain-Informationen ändern dürfen.
  2. Es MUSS festgelegt werden, welche Domain-Informationen die IT-Systeme ändern dürfen. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Das Prinzip der geringsten Berechtigungen (BER.4.1) fordert allgemein die minimale und zweckgebundene Zuweisung von Zugriffs- und Änderungsrechten, was die Festlegung des zulässigen Umfangs an änderbaren Domain-Informationen umfasst.

### → APP.4.2.A12 — SAP-Berechtigungsentwicklung (S) [Fachabteilung, Entwickelnde]
  1. Die technischen Berechtigungen SOLLTEN aufgrund fachlicher Vorgaben entwickelt werden.
  2. Des Weiteren SOLLTEN SAP-Berechtigungen auf dem Entwicklungssystem der SAP-Landschaft angepasst oder neu erstellt werden.
  3. Das SOLLTE auch bei S/4HANA die Berechtigungsentwicklung auf HANA-Datenbanken mit einschließen.
  4. Hier SOLLTEN Repository-Rollen aufgebaut und transportiert werden.
  5. Datenbankprivilegien SOLLTEN NICHT direkt an Konten vergeben werden.
  6. Bei Eigenentwicklungen für z. B. Transaktionen oder Berechtigungsobjekte SOLLTE die Transaktion SU24 gepflegt werden (Zuordnungen von Berechtigungsobjekten zu Transaktionen).
  7. Die Gesamtberechtigung * oder Intervalle in Objektausprägungen SOLLTEN vermieden werden. **◀ ZITIERT**
  8. Die Berechtigungsentwicklung SOLLTE im Rahmen eines Änderungsmanagements durchgeführt werden.
  9. Es SOLLTE sichergestellt sein, dass das Produktivsystem ausreichend vor Berechtigungsänderungen geschützt ist und keine Entwicklerschlüssel vergeben werden.
  10. Das Qualitätssicherungssystem SOLLTE bei der Berechtigungsvergabe und ergänzenden Einstellungen analog zum Produktivsystem betrieben werden.
- **Satz 7** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 7) Die Vermeidung von Gesamtberechtigungen (*) und Intervallen in Berechtigungsobjekten ist eine spezifische technische Ausprägung des Prinzips der geringsten Berechtigungen (Least Privilege) gemäß BER.4.1.

### → APP.4.2.A13 — SAP-Passwortsicherheit (S)
  1. Um eine sichere Anmeldung am SAP-ERP-System zu gewährleisten, SOLLTEN Profilparameter, Customizing-Schalter oder Sicherheitsrichtlinien geeignet eingestellt werden.
  2. Die eingesetzten Hash-Algorithmen für die gespeicherten Hashwerte der Passwörter in einem SAP-ERP-System SOLLTEN den aktuellen Sicherheitsstandards entsprechen.
  3. Zugriffe auf Tabellen mit Hashwerten SOLLTEN eingeschränkt werden. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die allgemeine Begrenzung von Zugriffsrechten nach dem Principle of Least Privilege in BER.4.1 schließt das restriktive Einschränken von Zugriffen auf spezifische, sensible Tabellen wie solche mit Hashwerten mit ein.

### → APP.4.2.A14 — Identifizierung kritischer SAP-Berechtigungen (S) [Fachabteilung]
  1. Der Umgang mit kritischen Berechtigungen SOLLTE streng kontrolliert werden.
  2. Es SOLLTE darauf geachtet werden, dass diese Berechtigungen, Rollen und Profile nur restriktiv vergeben werden. **◀ ZITIERT**
  3. Dies SOLLTE auch für kritische Rollenkombinationen und additive Effekte wie z. B. Kreuzberechtigungen sichergestellt sein.
  4. Kritische Berechtigungen SOLLTEN regelmäßig identifiziert, überprüft und bewertet werden.
  5. Die SAP-Profile SAP_ALL und SAP_NEW* sowie das SAP-Berechtigungsobjekt S_DEVELOP (mit Änderungsberechtigungen ACTVT 01 und 02) SOLLTEN im Produktivsystem nicht vergeben werden. **◀ ZITIERT**
  6. Notfall-Konten SOLLTEN von dieser Vorgabe ausgeschlossen sein.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Das Prinzip der geringsten Berechtigungen in BER.4.1 fordert direkt die restriktive Vergabe und Einschränkung von Berechtigungen.
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) Das Verbot weitgehender Berechtigungen und Entwicklerrechte im Produktivsystem (SAP_ALL, SAP_NEW*, S_DEVELOP) stellt einen konkreten technologiespezifischen Anwendungsfall des allgemeinen Prinzips der geringsten Berechtigungen dar.

### → APP.4.2.A16 — Umsetzung von Sicherheitsanforderungen für das Betriebssystem Windows (S)
  1. Das SAP-ERP-System SOLLTE NICHT auf einem Windows-Domaincontroller installiert werden.
  2. Die SAP-spezifischen Konten wie <sid>adm oder SAPService <sid> SOLLTEN abgesichert werden.
  3. Nach der Installation SOLLTE das Konto <db><sid> gesperrt werden.
  4. Das Konto SAPService <sid> SOLLTE KEINE Rechte zur interaktiven Anmeldung besitzen. **◀ ZITIERT**
  5. In Bezug auf diese Berechtigungen SOLLTEN die zum SAP-ERP-System dazugehörigen Systemressourcen wie Dateien, Prozesse und gemeinsam genutzte Speicher geschützt werden.
  6. Die spezifischen Berechtigungen der vom SAP-ERP-System angelegten Konten Guest, System, SAP system users = <sapsid>adm, SAPService<SAPSID> und Database users = <database-specific users> und Benutzendengruppen SOLLTEN mithilfe geeigneter Einstellungen abgesichert werden. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Das Entziehen interaktiver Anmelderechte fuer Dienstkonten stellt eine konkrete Umsetzung des allgemeinen Prinzips der geringsten Berechtigungen (Least Privilege) gemaess BER.4.1 dar.
- **Satz 6** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 6) Die allgemeine Begrenzung von Berechtigungen nach dem Least-Privilege-Prinzip gemäß BER.4.1 deckt die gezielte Absicherung und Einschränkung der spezifischen Berechtigungen für SAP-spezifische Systemkonten und Gruppen ab.

### → APP.4.2.A17 — Umsetzung von Sicherheitsanforderungen für das Betriebssystem Unix (S)
  1. Für die SAP-ERP-Systemverzeichnisse unter Unix SOLLTEN Zugriffsberechtigungen festgelegt werden. **◀ ZITIERT**
  2. Auch SOLLTEN die Passwörter der systemspezifischen Konten <sid>adm und <db><sid> geändert werden.
  3. Nach der Installation SOLLTE das Konto <db><sid> gesperrt werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme BER.4.1 fordert die Vergabe und Einschränkung von Berechtigungen nach dem Least-Privilege-Prinzip, was die allgemeine Vorgabe für das Festlegen von Zugriffsberechtigungen auf Verzeichnisebene darstellt.

### → APP.4.2.A22 — Schutz des Spools im SAP-ERP-System (S) [Entwickelnde]
  1. Es SOLLTE sichergestellt sein, dass auf Daten der sequenziellen Datenverarbeitung wie Spool oder Druck nur eingeschränkt zugegriffen werden kann. **◀ ZITIERT**
  2. Auch SOLLTE verhindert werden, dass unberechtigte Konten auf die vom SAP-Spoolsystem benutzte Datenablage TemSe zugreifen können. **◀ ZITIERT**
  3. Die hierfür vergebenen Berechtigungen SOLLTEN regelmäßig überprüft werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) BER.4.1 fordert die allgemeine Einschränkung von Berechtigungen nach dem Least-Privilege-Prinzip und deckt damit den geforderten eingeschränkten Zugriff auf Spool- und Druckdaten ab.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) BER.4.1 fordert die allgemeine Beschränkung von Zugriffsrechten nach dem Minimalprinzip, was den Ausschluss unberechtigter Konten vom Zugriff auf spezifische Datenablagen wie TemSe umfasst.

### → APP.4.2.A24 — Aktivierung und Absicherung des Internet Communication Frameworks (S)
  1. Es SOLLTE darauf geachtet werden, dass nur notwendige ICF-Dienste aktiviert werden.
  2. Alle ICF-Dienste, die unter einem ICF-Objekt sind, SOLLTEN nur einzeln aktiviert werden.
  3. ICF-Berechtigungen SOLLTEN restriktiv vergeben werden. **◀ ZITIERT**
  4. Die Kommunikation SOLLTE verschlüsselt erfolgen.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) BER.4.1 deckt die geforderte restriktive Vergabe von ICF-Berechtigungen durch die allgemeine Pflicht zur Vergabe von Berechtigungen nach dem Prinzip der geringsten Berechtigungen (Least Privilege) ab.

### → APP.4.3.A13 — Restriktive Handhabung von Datenbank-Links (S)
  1. Es SOLLTE sichergestellt sein, dass nur Zuständige dazu berechtigt sind, Datenbank-Links (DB-Links) anzulegen. **◀ ZITIERT**
  2. Werden solche Links angelegt, MÜSSEN so genannte Private DB-Links vor Public DB-Links bevorzugt angelegt werden.
  3. Alle von den Zuständigen angelegten DB-Links SOLLTEN dokumentiert und regelmäßig überprüft werden.
  4. Zudem SOLLTEN DB-Links mitberücksichtigt werden, wenn das Datenbanksystem gesichert wird (siehe APP.4.3.A9 Datensicherung eines Datenbanksystems).
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Das in BER.4.1 geforderte Prinzip der geringsten Berechtigung deckt als allgemeiner Grundsatz die Anforderung ab, die Berechtigung zum Anlegen von DB-Links ausschließlich auf zuständige Personen zu beschränken.

### → APP.4.4.A10 — Absicherung von Prozessen der Automatisierung (S)
  1. Alle Prozesse der Automatisierungssoftware, wie CI/CD und deren Pipelines, SOLLTEN nur mit unbedingt notwendigen Rechten arbeiten. **◀ ZITIERT**
  2. Wenn unterschiedliche Gruppen von Benutzenden die Konfiguration über die Automatisierungssoftware verändern oder Pods starten können, SOLLTE dies für jede Gruppe durch eigene Prozesse durchgeführt werden, die nur die für die jeweilige Gruppe notwendigen Rechte besitzen.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) BER.4.1 fordert allgemeingültig die Vergabe von Berechtigungen nach dem Prinzip der geringsten Berechtigungen (Least Privilege), was die Beschränkung von Rechten für Automatisierungsprozesse und CI/CD-Pipelines direkt umfasst.

### → APP.4.4.A3 — Identitäts- und Berechtigungsmanagement bei Kubernetes (B)
  1. Kubernetes und alle anderen Anwendungen der Control Plane MÜSSEN jede Aktion eines Benutzenden oder, im automatisierten Betrieb, einer entsprechenden Software authentifizieren und autorisieren, unabhängig davon, ob die Aktionen über einen Client, eine Weboberfläche oder über eine entsprechende Schnittstelle (API) erfolgt.
  2. Administrative Handlungen DÜRFEN NICHT anonym erfolgen.
  3. Benutzende DÜRFEN NUR die unbedingt notwendigen Rechte erhalten. **◀ ZITIERT**
  4. Berechtigungen ohne Einschränkungen MÜSSEN sehr restriktiv vergeben werden.
  5. Nur ein kleiner Kreis von Personen SOLLTE berechtigt sein, Prozesse der Automatisierung zu definieren. **◀ ZITIERT**
  6. Nur ausgewählte Administrierende SOLLTEN in Kubernetes das Recht erhalten, Freigaben für Festspeicher (Persistent Volumes) anzulegen oder zu ändern.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 3) Die G++-Maßnahme BER.4.1 fordert die Vergabe von Rechten nach dem Principle of Least Privilege, was der Anforderung entspricht, dass Benutzende nur die unbedingt notwendigen Rechte erhalten dürfen.
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) Die G++-Maßnahme BER.4.1 fordert die allgemeine Anwendung des Prinzips der geringsten Berechtigung, wodurch die restriktive Vergabe von Rechten zur Definition von Automatisierungsprozessen inhaltlich abgedeckt wird.

### → APP.4.4.A7 — Separierung der Netze bei Kubernetes (S)
  1. Die Netze für die Administration der Nodes, der Control Plane sowie die einzelnen Netze der Anwendungsdienste SOLLTEN separiert werden.
  2. Es SOLLTEN NUR die für den Betrieb notwendigen Netzports der Pods in die dafür vorgesehenen Netze freigegeben werden.
  3. Bei mehreren Anwendungen auf einem Kubernetes-Cluster SOLLTEN zunächst alle Netzverbindungen zwischen den Kubernetes-Namespaces untersagt und nur benötigte Netzverbindungen gestattet sein (Whitelisting).
  4. Die zur Administration der Nodes, der Runtime und von Kubernetes inklusive seiner Erweiterungen notwendigen Netzports SOLLTEN NUR aus dem Administrationsnetz und von Pods, die diese benötigen, erreichbar sein.
  5. Nur ausgewählte Administrierende SOLLTEN in Kubernetes berechtigt sein, das CNI zu verwalten und Regeln für das Netz anzulegen oder zu ändern. **◀ ZITIERT**
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) Die G++-Maßnahme BER.4.1 fordert die Einschränkung von Rechten nach dem Prinzip der geringsten Berechtigungen (Least Privilege), was die spezifische Beschränkung von CNI- und Netzwerk-Administrationsrechten auf ausgewählte Administrierende abstrahierend abdeckt.

### → APP.4.4.A8 — Absicherung von Konfigurationsdateien bei Kubernetes (S)
  1. Die Konfigurationsdateien des Kubernetes-Clusters, inklusive aller Erweiterungen und Anwendungen, SOLLTEN versioniert und annotiert werden.
  2. Zugangsrechte auf die Verwaltungssoftware der Konfigurationsdateien SOLLTEN minimal vergeben werden. **◀ ZITIERT**
  3. Zugriffsrechte für lesenden und schreibenden Zugriff auf die Konfigurationsdateien der Control Plane SOLLTEN besonders sorgfältig vergeben und eingeschränkt sein. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme BER.4.1 fordert die allgemeine Anwendung des Prinzips der geringsten Berechtigungen (Least Privilege), was die minimale Vergabe von Rechten für die Verwaltungssoftware in Satz 2 abstrahierend abdeckt.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) BER.4.1 fordert allgemein die Vergabe und Einschränkung von Zugriffsrechten nach dem Prinzip der geringsten Berechtigungen, was die spezifische Begrenzung von Lese- und Schreibrechten auf Konfigurationsdateien inhaltlich abdeckt.

### → APP.4.4.A9 — Nutzung von Kubernetes Service-Accounts (S)
  1. Pods SOLLTEN NICHT den "default"-Service-Account nutzen.
  2. Dem "default"-Service-Account SOLLTEN keine Rechte eingeräumt werden. **◀ ZITIERT**
  3. Pods für unterschiedliche Anwendungen SOLLTEN jeweils unter eigenen Service-Accounts laufen.
  4. Berechtigungen für die Service-Accounts der Pods der Anwendungen SOLLTEN auf die unbedingt notwendigen Rechte beschränkt werden. **◀ ZITIERT**
  5. Pods, die keinen Service-Account benötigen, SOLLTEN diesen nicht einsehen können und keinen Zugriff auf entsprechende Token haben.
  6. Nur Pods der Control Plane und Pods, die diese unbedingt benötigen, SOLLTEN privilegierte Service-Accounts nutzen.
  7. Programme der Automatisierung SOLLTEN jeweils eigene Token erhalten, auch wenn sie aufgrund ähnlicher Aufgaben einen gemeinsamen Service-Account nutzen.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Das Einräumen von keinen Berechtigungen für den ungenutzten default-Service-Account stellt eine konkrete technologiespezifische Ausprägung des Prinzips der geringsten Berechtigungen (Least Privilege) nach BER.4.1 dar.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die G++-Maßnahme fordert die generelle Vergabe von Berechtigungen nach dem Prinzip der geringsten Berechtigungen (Least Privilege), was die Beschränkung der Rechte von Service-Accounts auf das Notwendige unmittelbar abdeckt.

### → APP.5.2.A12 — Einsatz von Outlook Anywhere, MAPI over HTTP und Outlook im Web (S)
  1. Der IT-Betrieb SOLLTE Outlook Anywhere, MAPI over HTTP und Outlook im Web entsprechend den Sicherheitsanforderungen der Institution konfigurieren.
  2. Der Zugriff auf Exchange über das Internet SOLLTE auf die notwendigen Benutzenden beschränkt werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die Beschränkung des Exchange-Internetzugriffs auf notwendige Benutzende ist eine konkrete Anwendung des in BER.4.1 allgemein geforderten Prinzips der geringsten Berechtigungen.

### → APP.5.2.A3 — Berechtigungsmanagement und Zugriffsrechte (B)
  1. Zusätzlich zum allgemeinen Berechtigungskonzept MUSS die Institution ein Berichtigungskonzept für die Systeme der Exchange-Infrastruktur erstellen, geeignet dokumentieren und anwenden.
  2. Der IT-Betrieb MUSS serverseitige Benutzendenprofile für einen rechnerunabhängigen Zugriff der Benutzenden auf Exchange-Daten verwenden.
  3. Er MUSS die Standard-NTFS-Berechtigungen für das Exchange-Verzeichnis so anpassen, dass nur autorisierte Administrierende und Systemkonten auf die Daten in diesem Verzeichnis zugreifen können. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die Maßnahme BER.4.1 fordert die allgemeine Beschränkung von Berechtigungen nach dem Prinzip der geringsten Rechte, was das einschränkende Anpassen von Standard-NTFS-Berechtigungen auf autorisierte Konten als Spezialfall umfasst.

### → CON.11.1.A1 — Einhaltung der Grundsätze zur VS-Verarbeitung mit IT nach § 3, 4 und 6 und Nr. 1 Anlage V zur VSA (B)
  1. VS des Geheimhaltungsgrades VS-NfD DÜRFEN NUR mit VS-IT verarbeitet, die hierfür freigegeben ist.
  2. Private IT DARF NICHT für die Verarbeitung von Verschlusssachen eingesetzt werden.
  3. Bei der Verarbeitung von VS mit VS-IT MUSS der Grundsatz "Kenntnis nur, wenn nötig" eingehalten werden. **◀ ZITIERT**
  4. Es DÜRFEN NUR Personen Kenntnis von einer VS erhalten, die auf Grund ihrer Aufgabenerfüllung von ihr Kenntnis erhalten müssen.
  5. Personen DÜRFEN NICHT umfassender oder eher über eine VS unterrichtet werden, als dies aus Gründen der Aufgabenerfüllung notwendig ist.
  6. Die Einhaltung des Grundsatzes „Kenntnis nur, wenn nötig“ SOLLTE, insbesondere falls die VS-IT durch mehrere Benutzende verwendet wird, primär über technische Maßnahmen sichergestellt werden.
  7. Nach dem Grundsatz der mehrschichtigen Sicherheit MÜSSEN personelle, organisatorische, materielle und technische Maßnahmen getroffen werden, die in ihrem Zusammenwirken Risiken eines Angriffs reduzieren (Prävention), Angriffe erkennbar machen (Detektion) und im Falle eines erfolgreichen Angriffs die negativen Folgen begrenzen (Reaktion).
  8. Bei der Erfüllung der Anforderungen des vorliegenden Bausteins MÜSSEN die relevanten Technischen Leitlinien des BSI (BSI TL) beachtet werden.
  9. Falls von den BSI TL abgewichen werden soll, dann DARF dies NUR in Ausnahmefällen und im Einvernehmen mit dem BSI erfolgen.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme BER.4.1 deckt die Forderung nach dem Grundsatz 'Kenntnis nur, wenn nötig' (Need-to-Know) über die allgemeine Einschränkung von Zugriffsrechten nach dem Prinzip der geringsten Berechtigungen materiell ab.

### → CON.11.1.A8 — Verwaltung und Nachweis von elektronischen VS nach § 21 VSA (B)
  1. Für die Verwaltung von elektronischen VS MÜSSEN die Grundsätze ordnungsgemäßer Aktenführung (gemäß Registraturrichtlinie für das Bearbeiten und Verwalten von Schriftgut in Bundesministerien) und die Vorgaben der VSA zur Verwaltung und Nachweisführung von VS eingehalten werden (keine Nachweisführung für VS des Geheimhaltungsgrades VS-NfD erforderlich).
  2. Elektronische VS, die als VS-NfD eingestuft sind, DÜRFEN NUR unter Einhaltung des Grundsatzes „Kenntnis nur, wenn nötig“ in offenen (elektronischen) Registraturen verwaltet werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme BER.4.1 fordert die allgemeine Beschränkung von Berechtigungen nach dem Least-Privilege- bzw. Need-to-know-Prinzip und deckt damit die Einhaltung dieses Grundsatzes beim Zugriff auf Daten und Registraturen ab.

### → DER.3.1.A27 — Aufbewahrung und Archivierung von Unterlagen zu Audits und Revisionen (S)
  1. Die Institution SOLLTE Auditprogramme sowie Unterlagen zu Audits und Revisionen entsprechend den regulatorischen Anforderungen nachvollziehbar und revisionssicher ablegen und aufbewahren.
  2. Dabei SOLLTE sichergestellt werden, dass lediglich berechtigte Personen auf Auditprogramme und Unterlagen zugreifen können. **◀ ZITIERT**
  3. Die Institution SOLLTE die Auditprogramme und Unterlagen nach Ablauf der Aufbewahrungsfrist sicher vernichten.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die allgemeine G++-Maßnahme BER.4.1 fordert die Einschränkung von Berechtigungen nach dem Least-Privilege-Prinzip und deckt damit die Beschränkung des Zugriffs auf Auditunterlagen für ausschließlich berechtigte Personen inhaltlich ab.

### → DER.3.2.A8 — Aufbewahrung von IS-Revisionsberichten (B)
  1. Die Institution MUSS den IS-Revisionsbericht und die diesem zugrundeliegenden Referenzdokumente mindestens für zehn Jahre ab Zustellung des Berichts sicher aufbewahren, sofern keine anders lautenden Gesetze oder Verordnungen gelten.
  2. Die Institution MUSS sicherstellen, dass lediglich berechtigte Personen auf die IS-Revisionsberichte und die Referenzdokumente zugreifen können. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme BER.4.1 fordert die Einschränkung von Berechtigungen nach dem Prinzip der geringsten Berechtigungen (Least Privilege / Need-to-know), was den Zugriffsschutz sensibler Dokumente wie IS-Revisionsberichte auf ausschließlich berechtigte Personen als allgemeine Regelung abdeckt.

### → IND.1.A8 — Sichere Administration (S) [IT-Betrieb]
  1. Für die Erstkonfiguration, Verwaltung und Fernwartung in der OT SOLLTEN entweder sichere Protokolle oder abgetrennte Administrationsnetze mit entsprechendem Schutzbedarf genutzt werden.
  2. Der Zugang zu diesen Schnittstellen SOLLTE auf die Berechtigten eingeschränkt sein.
  3. Es SOLLTE nur der Zugriff auf die Systeme und Funktionen gewährt sein, die für die jeweilige Administrationsaufgabe benötigt werden. **◀ ZITIERT**
  4. Die Systeme und Kommunikationskanäle, mit denen die Administration oder Fernwartung durchgeführt wird, SOLLTEN das gleiche Schutzniveau aufweisen wie die verwaltete OT-Komponente.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) BER.4.1 fordert die Vergabe von Berechtigungen nach dem Principle of Least Privilege, was die aufgabenbezogene Beschränkung von Zugriffen auf Systeme und Funktionen direkt abdeckt.

### → INF.5.A3 — Zutrittsregelung und -kontrolle (B) [Haustechnik, IT-Betrieb]
  1. Der Raum für technische Infrastruktur MUSS gegen unberechtigten Zutritt geschützt werden.
  2. Es MUSS geregelt werden, welche Personen für welchen Zeitraum, für welche Bereiche und zu welchem Zweck den Raum betreten dürfen.
  3. Dabei MUSS sichergestellt sein, dass keine unnötigen oder zu weitreichenden Zutrittsrechte vergeben werden. **◀ ZITIERT**
  4. Alle Zutritte zum Raum für technische Infrastruktur SOLLTEN von der Zutrittskontrolle individuell erfasst werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme BER.4.1 formuliert das allgemeine Prinzip der geringsten Berechtigungen und deckt damit die Forderung ab, keine unnötigen oder zu weitreichenden Rechte zu vergeben.

### → NET.1.2.A10 — Beschränkung der SNMP-Kommunikation (B)
  1. Grundsätzlich DÜRFEN im Netzmanagement KEINE unsicheren Versionen des Simple Network Management Protocol (SNMP) eingesetzt werden.
  2. Werden dennoch unsichere Protokolle verwendet und nicht über andere sichere Netzprotokolle (z. B. VPN oder TLS) abgesichert, MUSS ein separates Managementnetz genutzt werden.
  3. Grundsätzlich SOLLTE über SNMP nur mit den minimal erforderlichen Zugriffsrechten zugegriffen werden. **◀ ZITIERT**
  4. Die Zugangsberechtigung SOLLTE auf dedizierte Management-Server eingeschränkt werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme BER.4.1 fordert allgemeingültig das Prinzip der geringsten Berechtigungen (Least Privilege), welches die Beschränkung von SNMP-Zugriffen auf minimal erforderliche Rechte direkt abdeckt.

### → NET.4.3.A13 — Festlegung berechtigter Faxbedienenden (H) [Benutzende]
  1. Es SOLLTEN nur wenige Mitarbeitende ausgewählt werden, die auf das Faxgerät zugreifen dürfen. **◀ ZITIERT**
  2. Diese Mitarbeitenden SOLLTEN ankommende Faxsendungen an die Empfangenden verteilen.
  3. Den Mitarbeitenden SOLLTE vermittelt werden, wie sie mit dem Gerät umgehen und wie sie die erforderlichen Sicherheitsmaßnahmen umsetzen können.
  4. Jeder berechtigte Benutzende SOLLTE darüber unterrichtet werden, wer das Faxgerät bedienen darf und wer für das Gerät zuständig ist.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme BER.4.1 fordert die Einschränkung von Berechtigungen nach dem Least-Privilege-Prinzip und deckt damit die Beschränkung des Zugriffs auf das Faxgerät auf wenige Berechtigte als allgemeiner Grundsatz ab.

### → OPS.1.1.1.A13 — Absicherung der Betriebsmittel und der Dokumentation (S)
  1. Auf die Betriebsmittel, die Dokumentation und die Betriebshandbücher SOLLTEN nur berechtigte Personen des IT-Betriebs zugreifen können. **◀ ZITIERT**
  2. Der IT-Betrieb SOLLTE sicherstellen, dass die Betriebsmittel und die Dokumentation zu jeder Zeit verfügbar sind.
  3. Falls die IT-Systeme und -Anwendungen der Betriebsmittel über die produktive Infrastruktur kommunizieren, SOLLTEN sichere Protokolle verwendet werden.
  4. Vertrauliche Daten SOLLTEN ausschließlich über sichere Protokolle übertragen werden.
  5. Die Betriebsmittel SOLLTEN in das Schwachstellenmanagement und das IT-Monitoring eingebunden werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die Beschränkung des Zugriffs auf Betriebsmittel und Dokumentation auf berechtigte Personen des IT-Betriebs ist eine direkte Ausprägung des Prinzips der geringsten Berechtigungen (Least Privilege / Need-to-know).

### → OPS.1.1.2.A21 — Regelung der IT-Administrationsrollen (B)
  1. Es MÜSSEN Rollen definiert werden, die ausschließlich zur IT-Administration vergeben werden.
  2. Administrationsrollen MÜSSEN aufgrund des tatsächlichen Bedarfs im Aufgabenbereich der IT-Administration nachvollziehbar vergeben werden.
  3. Alle notwendigen IT-Administrationstätigkeiten MÜSSEN durch Berechtigungen in den Administrationsrollen nach dem Minimalprinzip abgedeckt sein. **◀ ZITIERT**
  4. Die IT-Administration unterschiedlicher Ebenen der IT-Komponenten, z. B. die Trennung von Betriebssystem- und Anwendungsadministration, MUSS bei der Konzeption der Administrationsrollen berücksichtigt werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) BER.4.1 fordert allgemein die Einschränkung von Berechtigungen nach dem Prinzip der geringsten Berechtigungen (Least Privilege / Minimalprinzip) und deckt damit die geforderte bedarfsgerechte Minimalvergabe für Administrationsrollen inhaltlich ab.

### → OPS.1.1.2.A7 — Regelung der IT-Administrationstätigkeit (S)
  1. Jede IT-Administrationstätigkeit SOLLTE einer klar definierten Aufgabe zugeordnet sein.
  2. Für diese Aufgaben SOLLTE geregelt werden, durch wen diese Aufgabe ausgeführt werden darf und durch wen diese Aufgabe beauftragt werden darf.
  3. Es SOLLTE nachvollziehbar sein, in welchen Prozessen sich Administrationsaufgaben einfügen.
  4. IT-Administrationstätigkeiten SOLLTEN nur mit denjenigen Berechtigungen durchgeführt werden, die zur Erfüllung der entsprechenden Aufgabe notwendig sind. **◀ ZITIERT**
  5. Es SOLLTE festgelegt werden, wie IT-Administrationstätigkeiten auszuführen sind.
  6. Die Regelungen für IT-Administrationstätigkeiten SOLLTEN regelmäßig und anlassbezogen überprüft und aktualisiert werden.
  7. Für jede IT-Administrationstätigkeit SOLLTE sichergestellt werden, dass diese bei Bedarf auch im Notfall ausgeführt werden kann.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die G++-Maßnahme BER.4.1 fordert die allgemeine Umsetzung des Prinzips der geringsten Berechtigungen (Least Privilege), was die Beschränkung von Administrationsrechten auf das aufgabenbezogen notwendige Maß aus Satz 4 vollständig abdeckt.

### → OPS.1.2.5.A19 — Fernwartung durch Dritte (S)
  1. Wird die Fernwartung von Externen durchgeführt, SOLLTEN alle Fernwartungsaktivitäten von internen Mitarbeitenden beobachtet werden.
  2. Alle Fernwartungsvorgänge durch Dritte SOLLTEN aufgezeichnet werden.
  3. Mit externem Wartungspersonal MÜSSEN vertragliche Regelungen über die Sicherheit der betroffenen IT-Systeme und Informationen geschlossen werden.
  4. Die Pflichten und Kompetenzen des externen Wartungspersonals SOLLTEN in den vertraglichen Regelungen festgehalten werden.
  5. Sollten Dienstleistende mehrere Kunden und Kundinnen fernwarten, MUSS gewährleistet sein, dass die Netze der Kunden und Kundinnen nicht miteinander verbunden werden.
  6. Die Fernwartungsschnittstellen SOLLTEN so konfiguriert sein, dass es Dienstleistenden nur möglich ist, auf die IT-Systeme und Netzsegmente zuzugreifen, die für seine Arbeit benötigt werden. **◀ ZITIERT**
- **Satz 6** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 6) Die G++-Maßnahme BER.4.1 fordert die allgemeine Umsetzung des Prinzips der geringsten Berechtigungen (Least Privilege), womit die spezifische Beschränkung der Zugriffe von Fernwartungsdienstleistern auf nur zwingend benötigte Systeme und Segmente abgedeckt ist.

### → OPS.3.2.A17 — Zutritts-, Zugangs- und Zugriffskontrolle (S)
  1. Zutritts-, Zugangs- und Zugriffsberechtigungen SOLLTEN sowohl für das Personal der Anbietenden von Outsourcing als auch für das Personal der Nutzenden von Outsourcing geregelt sein.
  2. Ebenfalls SOLLTEN Zutritts-, Zugangs- und Zugriffsberechtigungen für Auditoren und andere Prüfer festgelegt werden.
  3. Dabei SOLLTEN nur so viele Rechte vergeben werden, wie für die Tätigkeit notwendig ist. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) BER.4.1 fordert die Einschränkung der Rechtevergabe nach dem Prinzip der geringsten Berechtigungen (Least Privilege) und deckt damit die Beschränkung der Rechte auf das für die Tätigkeit notwendige Maß direkt ab.

### → SYS.1.1.A1 — Zugriffsschutz und Nutzung (B)
  1. Physische Server MÜSSEN an Orten betrieben werden, zu denen nur berechtigte Personen Zutritt haben.
  2. Physische Server MÜSSEN daher in Rechenzentren, Serverräumen oder abschließbaren Serverschränken aufgestellt beziehungsweise eingebaut werden (siehe hierzu die entsprechenden Bausteine der Schicht INF Infrastruktur).
  3. Bei virtualisierten Servern MUSS der Zugriff auf die Ressourcen der Instanz und deren Konfiguration ebenfalls auf die berechtigten Personen begrenzt werden. **◀ ZITIERT**
  4. Server DÜRFEN NICHT als Arbeitsplatzrechner genutzt werden.
  5. Server DÜRFEN NICHT zur Erledigung von Aufgaben und Tätigkeiten verwendet werden, die grundsätzlich auf einem Client-System aus- und durchgeführt werden können.
  6. Insbesondere DÜRFEN vorhandene Anwendungen, wie Webbrowser, auf dem Server NICHT für das Abrufen von Informationen aus dem Internet oder das Herunterladen von Software, Treibern und Updates verwendet werden.
  7. Als Arbeitsplatz genutzte IT-Systeme DÜRFEN NICHT als Server genutzt werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Das allgemeine Prinzip der geringsten Berechtigungen nach BER.4.1 umfasst die geforderte Begrenzung des Zugriffs auf Instanzressourcen und Konfigurationen auf berechtigte Personen.

### → SYS.1.2.3.A6 — Sicherheit beim Fernzugriff über RDP (S)
  1. Die Auswirkungen auf die Konfiguration der lokalen Firewall SOLLTEN bei der Planung des Fernzugriffs berücksichtigt werden.
  2. Die Gruppe der Berechtigten und IT-Systeme für den Remote-Desktopzugriff (RDP) SOLLTE durch die Zuweisung entsprechender Berechtigungen festgelegt werden. **◀ ZITIERT**
  3. Es SOLLTEN Mechanismen des Betriebssystems berücksichtigt werden, um die übertragenen Anmeldeinformationen zu schützen (z. B. Remote Credential Guard oder RestrictedAdmin).
  4. In komplexen Infrastrukturen SOLLTE das RDP-Zielsystem nur durch ein dazwischengeschaltetes RDP-Gateway erreicht werden können.
  5. Für die Verwendung von RDP SOLLTE eine Prüfung und deren Umsetzung sicherstellen, dass die nachfolgend aufgeführten Komfortfunktionen im Einklang mit dem Schutzbedarf des Zielsystems stehen: die Verwendung der Zwischenablage, die Einbindung von Wechselmedien und Netzlaufwerken sowie die Nutzung der Dateiablagen, von weiteren Geräten und Ressourcen, wie z. B. Smartcard-Lesegeräten.
  6. Die eingesetzten kryptografischen Protokolle und Algorithmen SOLLTEN den internen Vorgaben der Institution entsprechen.
  7. Sofern der Einsatz von Remote-Desktopzugriffen nicht vorgesehen ist, SOLLTEN diese vollständig deaktiviert werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) G++ BER.4.1 fordert die generelle Vergabe und Einschränkung von Rechten nach dem Least-Privilege-Prinzip und deckt damit die Festlegung berechtigter Benutzer und IT-Systeme über gezielte Berechtigungszuweisung ab.

### → SYS.1.3.A2 — Sorgfältige Vergabe von IDs (B)
  1. Jeder Login-Name, jede User-ID (UID) und jede Gruppen-ID (GID) DARF NUR einmal vorkommen.
  2. Jedes Konto von Benutzenden MUSS Mitglied mindestens einer Gruppe sein.
  3. Jede in der Datei /etc/passwd vorkommende GID MUSS in der Datei /etc/group definiert sein.
  4. Jede Gruppe SOLLTE nur die Konten enthalten, die unbedingt notwendig sind. **◀ ZITIERT**
  5. Bei vernetzten Systemen MUSS außerdem darauf geachtet werden, dass die Vergabe von Benutzenden- und Gruppennamen, UID und GID im Systemverbund konsistent erfolgt, wenn beim systemübergreifenden Zugriff die Möglichkeit besteht, dass gleiche UIDs bzw. GIDs auf den Systemen unterschiedlichen Benutzenden- bzw. Gruppennamen zugeordnet werden könnten.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Das Prinzip der geringsten Berechtigungen (Least Privilege) in BER.4.1 bildet das übergeordnete Prinzip ab, dem die Beschränkung von Gruppenmitgliedschaften auf das unbedingt notwendige Maß direkt entspricht.

### → SYS.1.5.A12 — Rechte- und Rollenkonzept für die Administration einer virtuellen Infrastruktur (S)
  1. Anhand der in der Planung definierten Aufgaben und Rollen (siehe SYS.1.5.A8 Planung einer virtuellen Infrastruktur) SOLLTE für die Administration der virtuellen IT-Systeme und Netze sowie der Virtualisierungsserver und der Managementumgebung ein Rechte- und Rollenkonzept erstellt und umgesetzt werden.
  2. Alle Komponenten der virtuellen Infrastruktur SOLLTEN in ein zentrales Identitäts- und Berechtigungsmanagement eingebunden werden.
  3. Administrierende von virtuellen Maschinen und Administrierende der Virtualisierungsumgebung SOLLTEN unterschieden werden.
  4. Sie SOLLTEN mit unterschiedlichen Zugriffsrechten ausgestattet werden. **◀ ZITIERT**
  5. Weiterhin SOLLTE die Managementumgebung virtuelle Maschinen zur geeigneten Strukturierung gruppieren können.
  6. Die Rollen der Administrierenden SOLLTEN entsprechend zugeteilt werden.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Das Prinzip der geringsten Berechtigungen (Least Privilege) in BER.4.1 fordert allgemein, Berechtigungen auf das jeweils erforderliche Maß zu beschränken, was die Vergabe differenzierter Zugriffsrechte für unterschiedliche Administrationsaufgaben abdeckt.

### → SYS.1.5.A2 — Sicherer Einsatz virtueller IT-Systeme (B)
  1. Jede Person, die virtuelle IT-Systeme administriert, MUSS wissen, wie sich eine Virtualisierung auf die betriebenen IT-Systeme und Anwendungen auswirkt.
  2. Die Zugriffsrechte für Administrierende auf virtuelle IT-Systeme MÜSSEN auf das tatsächlich notwendige Maß reduziert sein. **◀ ZITIERT**
  3. Es MUSS gewährleistet sein, dass die für die virtuellen IT-Systeme notwendigen Netzverbindungen in der virtuellen Infrastruktur verfügbar sind.
  4. Auch MUSS geprüft werden, ob die Anforderungen an die Isolation und Kapselung der virtuellen IT-Systeme sowie der darauf betriebenen Anwendungen hinreichend erfüllt sind.
  5. Weiterhin MÜSSEN die eingesetzten virtuellen IT-Systeme den Anforderungen an die Verfügbarkeit und den Datendurchsatz genügen.
  6. Im laufenden Betrieb MUSS die Performance der virtuellen IT-Systeme überwacht werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme BER.4.1 fordert die Vergabe von Berechtigungen nach dem Prinzip der geringsten Berechtigungen und deckt damit die Reduzierung von Administrationsrechten auf das notwendige Maß allgemeingültig ab.

### → SYS.1.6.A17 — Ausführung von Containern ohne Privilegien (S)
  1. Die Container-Runtime und alle instanziierten Container SOLLTEN nur von einem nicht-privilegierten System-Account ausgeführt werden, der über keine erweiterten Rechte für den Container-Dienst und das Betriebssystem des Host-Systems verfügt oder diese Rechte erlangen kann. **◀ ZITIERT**
  2. Die Container-Runtime SOLLTE durch zusätzliche Maßnahmen gekapselt werden, etwa durch Verwendung der Virtualisierungserweiterungen von CPUs.
  3. Sofern Container ausnahmsweise Aufgaben des Host-Systems übernehmen sollen, SOLLTEN die Privilegien auf dem Host-System auf das erforderliche Minimum begrenzt werden. **◀ ZITIERT**
  4. Ausnahmen SOLLTEN angemessen dokumentiert werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme BER.4.1 fordert die allgemeine Anwendung des Prinzips der geringsten Berechtigung auf Prozesse und Konten, was die Ausführung von Container-Runtimes und Containern über nicht-privilegierte Systemkonten als Spezialfall abdeckt.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme BER.4.1 fordert allgemeingültig die Vergabe von Berechtigungen nach dem Prinzip der geringsten Rechte, was die Beschränkung von Container-Host-Privilegien auf das erforderliche Minimum direkt einschließt.

### → SYS.1.6.A18 — Accounts der Anwendungsdienste (S)
  1. Die System-Accounts innerhalb eines Containers SOLLTEN keine Berechtigungen auf dem Host-System haben.
  2. Wo aus betrieblichen Gründen diese Berechtigung notwendig ist, SOLLTE diese nur für unbedingt notwendige Daten und Systemzugriffe gelten. **◀ ZITIERT**
  3. Der Account im Container, der für diesen Datenaustausch notwendig ist, SOLLTE im Host-System bekannt sein.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) BER.4.1 fordert die allgemeine Beschränkung von Berechtigungen nach dem Prinzip der geringsten Rechte (Least Privilege), was die Beschränkung auf unbedingt notwendige Daten und Systemzugriffe bei Ausnahmeberechtigungen direkt abdeckt.

### → SYS.1.6.A19 — Einbinden von Datenspeichern in Container (S)
  1. Die Container SOLLTEN NUR auf die für den Betrieb notwendigen Massenspeicher und Verzeichnisse zugreifen können. **◀ ZITIERT**
  2. Nur wenn Berechtigungen benötigt werden, SOLLTEN diese explizit vergeben werden. **◀ ZITIERT**
  3. Sofern die Container-Runtime für einen Container lokalen Speicher einbindet, SOLLTEN die Zugriffsrechte im Dateisystem auf den Service-Account des Containers eingeschränkt sein. **◀ ZITIERT**
  4. Werden Netzspeicher verwendet, so SOLLTEN die Berechtigungen auf dem Netzspeicher selbst gesetzt werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme fordert die allgemeine Umsetzung des Principle of Least Privilege für Systeme und Prozesse, was die spezifische Einschränkung des Containerzugriffs auf nur betriebsnotwendige Speicher und Verzeichnisse direkt umfasst.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme BER.4.1 fordert die Umsetzung des Prinzips der geringsten Berechtigungen (Least Privilege), was die bedarfsgerechte und explizite Vergabe von Berechtigungen aus Satz 2 direkt allgemein abdeckt.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme BER.4.1 fordert allgemein die Vergabe von Berechtigungen nach dem Least-Privilege-Prinzip und deckt damit die Einschränkung der Dateisystem-Zugriffsrechte auf den Service-Account des Containers als konkreten Anwendungsfall ab.

### → SYS.1.7.A1 — Einsatz restriktiver z/OS-Kennungen (B)
  1. Berechtigungen mit hoher Autorisierung DÜRFEN NUR an Benutzende vergeben werden, die diese Rechte für ihre Tätigkeiten benötigen. **◀ ZITIERT**
  2. Insbesondere die RACF-Attribute SPECIAL, OPERATIONS, AUDITOR und die entsprechenden GROUP-Attribute sowie die User-ID 0 unter den Unix System Services (USS) MÜSSEN restriktiv gehandhabt werden.
  3. Die Vergabe und der Einsatz dieser Berechtigungen MÜSSEN nachvollziehbar sein.
  4. Die besondere Kennung IBMUSER DARF NUR bei der Neuinstallation zur Erzeugung von Kennungen mit Attribut SPECIAL benutzt werden.
  5. Diese Kennung MUSS danach dauerhaft gesperrt werden.
  6. Um zu vermeiden, dass Administrierende sich dauerhaft aussperren, MUSS ein Notfall-User-Verfahren eingerichtet werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme BER.4.1 fordert die Vergabe von Berechtigungen nach dem Prinzip der geringsten Berechtigungen (Least Privilege), was die Beschränkung von Berechtigungen mit hoher Autorisierung auf zwingend für die Tätigkeit benötigte Rechte inhaltlich allgemein abdeckt.

### → SYS.1.7.A17 — Synchronisierung von z/OS-Passwörtern und RACF-Kommandos (S)
  1. Falls z/OS-Passwörter oder RACF-Kommandos über mehrere z/OS-Systeme automatisch synchronisiert werden sollen, SOLLTEN die jeweiligen Systeme möglichst weitgehend standardisiert sein.
  2. Die Sperrung von Kennungen durch Fehleingaben von Passwörtern SOLLTE NICHT synchronisiert werden.
  3. Das Risiko durch Synchronisation sicherheitskritischer RACF-Kommandos SOLLTE berücksichtigt werden.
  4. Die Verwaltungsfunktion des Synchronisationsprogramms SOLLTE nur autorisierten Mitarbeitenden im Rahmen ihrer Tätigkeit zur Verfügung stehen. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) BER.4.1 fordert die Vergabe von Rechten nach dem Prinzip der geringsten Berechtigungen bezogen auf die Aufgabenerfüllung, was die Einschränkung der Verwaltungsfunktionen auf dafür autorisierte Mitarbeitende abdeckt.

### → SYS.1.7.A19 — Absicherung von z/OS-Transaktionsmonitoren (S)
  1. Falls Transaktionsmonitore oder Datenbanken unter z/OS eingesetzt werden, wie beispielsweise IMS, CICS oder Db2, SOLLTEN diese mittels RACF abgesichert werden.
  2. Dies gilt auch für die zugehörigen System-Kommandos und -Dateien.
  3. Interne Sicherheitsmechanismen der Transaktionsmonitore und Datenbanken SOLLTEN hingegen nur dort angewandt werden, wo es keine entsprechenden RACF-Funktionen gibt.
  4. Benutzende und Administrierende SOLLTEN nur die Zugriffsrechte erhalten, die sie für ihre jeweilige Tätigkeit benötigen. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die G++-Maßnahme BER.4.1 fordert die Umsetzung des Prinzips der geringsten Berechtigungen, was der Forderung entspricht, Benutzenden und Administrierenden nur die für ihre Tätigkeit benötigten Rechte einzuräumen.

### → SYS.1.7.A2 — Absicherung sicherheitskritischer z/OS-Dienstprogramme (B)
  1. Sicherheitskritische (Dienst-)Programme und Kommandos sowie deren Alias-Namen MÜSSEN mit Rechten auf entsprechende RACF-Profile so geschützt werden, dass sie nur von den dafür vorgesehenen und autorisierten Personen benutzt werden können. **◀ ZITIERT**
  2. Es MUSS sichergestellt sein, dass (Fremd-)Programme nicht unerlaubt installiert werden können.
  3. Außerdem DÜRFEN Programme NUR von gesicherten Quellen und über nachvollziehbare Methoden (z. B. SMP/E) installiert werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) BER.4.1 deckt die z/OS-spezifische Forderung als übergeordnetes Prinzip ab, da die Beschränkung des Zugriffs auf sicherheitskritische Dienstprogramme auf autorisierte Personen eine konkrete Anwendung des Least-Privilege-Prinzips darstellt.

### → SYS.1.7.A23 — Absicherung von z/VM (S)
  1. Falls z/VM eingesetzt wird, SOLLTE das Produkt in das Patch-Management integriert werden.
  2. Alle voreingestellten Passwörter SOLLTEN geändert werden.
  3. Die Rolle des z/VM-Systemadministrierenden SOLLTE nur an Personen vergeben werden, die diese Berechtigungen benötigen. **◀ ZITIERT**
  4. Die Sicherheitsadministration von z/VM SOLLTE über RACF für z/VM erfolgen.
  5. Passwörter von realen Usern und Guest-Usern SOLLTEN mittels RACF für z/VM verschlüsselt werden.
  6. Die sicherheitskritischen Systemkommandos von z/VM SOLLTEN über RACF geschützt werden.
  7. Unter z/VM definierte virtuelle Maschinen SOLLTEN nur die für die jeweiligen Aufgaben notwendigen Ressourcen erhalten und strikt voneinander getrennt sein.
  8. Unter z/VM SOLLTEN nur die benötigten Dienste gestartet werden.
  9. Wenn Überprüfungen durchgeführt werden, SOLLTEN die Journaling-Funktion von z/VM und die Audit-Funktionen von RACF eingesetzt werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme BER.4.1 fordert die Vergabe von Berechtigungen nach dem Prinzip der geringsten Berechtigung, was die bedarfsgerechte Beschränkung administrativer Rollen wie der des z/VM-Systemadministrierenden materiell abdeckt.

### → SYS.1.7.A30 — Absicherung der z/OS-Trace-Funktionen (S)
  1. Die Trace-Funktionen von z/OS wie GTF (Generalized Trace Facility), NetView oder ACF/TAP (Advanced Communication Function/Trace Analysis Program) und die entsprechenden Dateien SOLLTEN so geschützt werden, dass nur die zuständigen und autorisierten Mitarbeitenden darauf Zugriff haben. **◀ ZITIERT**
  2. Die Trace-Funktion von NetView SOLLTE deaktiviert sein und nur im Bedarfsfall aktiviert werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme BER.4.1 fordert die generelle Vergabe von Berechtigungen nach dem Prinzip der geringsten Berechtigungen und deckt damit die spezifische Beschränkung des Zugriffs auf z/OS-Trace-Funktionen und -Dateien auf autorisierte Mitarbeitende ab.

### → SYS.1.7.A7 — Restriktive Autorisierung unter z/OS (B)
  1. Im Rahmen der Grundkonfiguration MÜSSEN die Autorisierungsmechanismen so konfiguriert werden, dass alle Personen (definierte User-IDs in Gruppen gemäß Rolle) nur die Zugriffsmöglichkeiten erhalten, die sie für ihre jeweiligen Tätigkeiten benötigen. **◀ ZITIERT**
  2. Hierfür MÜSSEN insbesondere APF-Autorisierungen (Authorized Program Facility), SVCs (SuperVisor Calls), Ressourcen des z/OS-Betriebssystems, IPL-Parameter, Parmlib-Definitionen, Started Tasks und JES2/3-Definitionen berücksichtigt werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme fordert die Einschränkung von Berechtigungen nach dem Prinzip der geringsten Berechtigungen (Least Privilege), was der Kernforderung des Satzes nach einer Vergabe nur der benötigten Zugriffsrechte entspricht.

### → SYS.1.7.A8 — Einsatz des z/OS-Sicherheitssystems RACF (B)
  1. Der Einsatz von RACF für z/OS MUSS sorgfältig geplant werden, dazu gehören auch die Auswahl des Zeichensatzes, die Festlegung von Regeln für User-ID und Passwort sowie die Aktivierung der KDFAES-Verschlüsselung.
  2. Falls RACF PassTickets verwendet werden, MUSS der Enhanced PassTicket Algorithmus aktiviert werden.
  3. Voreingestellte Passwörter für das RVARY-Kommando und für neu angelegte User-IDs MÜSSEN geändert werden.
  4. Falls RACF-Exits eingesetzt werden sollen, MUSS deren Einsatz begründet, dokumentiert und regelmäßig überwacht werden.
  5. Für das Anlegen, Sperren, Freischalten und Löschen von RACF-Kennungen MÜSSEN geeignete Vorgehensweisen festgelegt sein.
  6. Nach einer festgelegten Anzahl fehlgeschlagener Anmeldeversuche MUSS eine RACF-Kennung gesperrt werden (Ausnahme: Notfall-User-Verfahren).
  7. Kennungen von Benutzenden MÜSSEN außerdem nach längerer Inaktivität gesperrt werden, Kennungen von Verfahren hingegen nicht.
  8. Dateien, Started Tasks und sicherheitskritische Programme MÜSSEN mittels RACF-Profilen geschützt werden.
  9. Benutzende DÜRFEN darüber NUR die Zugriffsmöglichkeiten erhalten, die sie gemäß ihrer Rolle benötigen. **◀ ZITIERT**
  10. Es MUSS außerdem sichergestellt sein, dass Benutzende ihre Zugriffsmöglichkeiten nicht unerlaubt erweitern können.
- **Satz 9** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 9) G++ BER.4.1 fordert die Beschränkung von Berechtigungen nach dem Prinzip der geringsten Berechtigung (Least Privilege), was die Beschränkung von Benutzerrechten auf die rollenbezogen erforderlichen Zugriffe inhaltlich vollständig abdeckt.

### → SYS.1.7.A9 — Mandantenfähigkeit unter z/OS (B)
  1. Falls ein z/OS-System von Mandanten genutzt werden soll, MUSS ein RACF-Konzept zur Mandantentrennung erstellt werden.
  2. Die Daten und Anwendungen der Mandanten MÜSSEN durch RACF-Profile getrennt werden.
  3. Hohe Berechtigungen im RACF (SPECIAL, OPERATIONS, AUDITOR) und ändernden Zugriff auf Dateien des z/OS-Betriebssystems DÜRFEN NUR Mitarbeitende der Betreibenden haben. **◀ ZITIERT**
  4. Die Wartungsfenster, in denen das z/OS-System nicht zur Verfügung steht, MÜSSEN mit allen Mandanten, die auf dem betroffenen System arbeiten, abgestimmt werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme BER.4.1 fordert die allgemeine Einschränkung von Berechtigungen nach dem Least-Privilege-Prinzip, was die Beschränkung administrativer Rechte und Systemzugriffe auf das z/OS-Betriebspersonal als konkreten Spezialfall abdeckt.

### → SYS.1.9.A11 — Sichere Konfiguration von Profilen (S)
  1. Benutzende SOLLTEN ihre spezifischen Einstellungen (Benutzendenprofile) NICHT derart ändern dürfen, dass die Informationssicherheit oder die Nutzung des Terminalservers eingeschränkt wird. **◀ ZITIERT**
  2. Für die Benutzendenprofile SOLLTE eine geeignete maximale Größe festgelegt werden.
  3. Wenn Verbünde aus Terminalservern eingesetzt werden, SOLLTEN die Benutzendenprofile zentral abgelegt werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme fordert als allgemeine Regel das Prinzip der geringsten Berechtigung (Least Privilege), was die Einschränkung von Änderungsrechten an Benutzendenprofilen zur Vermeidung von Sicherheitsrisiken inhaltlich abdeckt.

### → SYS.2.2.3.A12 — Datei- und Freigabeberechtigungen unter Windows (S)
  1. Der Zugriff auf Dateien und Ordner auf dem lokalen System sowie auf Netzfreigaben SOLLTE gemäß einem Berechtigungs- und Zugriffskonzept konfiguriert werden.
  2. Auch die standardmäßig vorhandenen administrativen Freigaben auf dem System SOLLTEN hierbei berücksichtigt werden.
  3. Die Schreibrechte für Benutzende SOLLTEN auf einen definierten Bereich im Dateisystem beschränkt werden. **◀ ZITIERT**
  4. Insbesondere SOLLTEN Benutzende keine Schreibrechte für Ordner des Betriebssystems oder installierter Anwendungen erhalten.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die Beschränkung der Schreibrechte von Benutzenden auf definierte Dateisystembereiche stellt eine direkte Ausprägung des in BER.4.1 allgemein geforderten Prinzips der geringsten Berechtigungen (Least Privilege) dar.

### → SYS.2.2.3.A19 — Sicherheit beim Fernzugriff über RDP (S) [Benutzende]
  1. Die Auswirkungen auf die Konfiguration der lokalen Firewall SOLLTEN bei der Planung des Fernzugriffs berücksichtigt werden.
  2. Die Gruppe der berechtigten Benutzenden für den Remote-Desktopzugriff (RDP) SOLLTE durch die Zuweisung entsprechender Berechtigungen festgelegt werden. **◀ ZITIERT**
  3. In komplexen Infrastrukturen SOLLTE das RDP-Zielsystem nur durch ein dazwischengeschaltetes RDP-Gateway erreicht werden können.
  4. Für die Verwendung von RDP SOLLTE eine Prüfung und deren Umsetzung sicherstellen, dass die nachfolgend aufgeführten Komfortfunktionen im Einklang mit dem Schutzbedarf des Zielsystems stehen: die Verwendung der Zwischenablage, die Einbindung von Druckern, die Einbindung von Wechselmedien und Netzlaufwerken sowie die Nutzung der Dateiablagen und von Smartcard-Anschlüssen.
  5. Sofern der Einsatz von Remote-Desktopzugriffen nicht vorgesehen ist, SOLLTEN diese vollständig deaktiviert werden.
  6. Die eingesetzten kryptografischen Protokolle und Algorithmen SOLLTEN sicher sein und den internen Vorgaben der Institution entsprechen.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme BER.4.1 fordert die Vergabe von Berechtigungen nach dem Minimalprinzip einzuschränken, was die Festlegung und Begrenzung des berechtigten Benutzerkreises für RDP über entsprechende Berechtigungszuweisungen als allgemeinen Grundsatz abdeckt.

### → SYS.2.2.3.A21 — Einsatz des Encrypting File Systems (H)
  1. Da das Encrypting File System (EFS) die verwendeten Schlüssel mit dem Passwort des jeweiligen Kontos schützt, SOLLTE ein sicheres Passwort verwendet werden.
  2. Zusätzlich SOLLTEN restriktive Zugriffsrechte die mit EFS verschlüsselten Dateien schützen. **◀ ZITIERT**
  3. Der Wiederherstellungsagent SOLLTE ein dediziertes Konto und kein Administrationskonto sein.
  4. In diesem Zusammenhang SOLLTE der private Schlüssel des Agenten gesichert und aus dem System entfernt werden.
  5. Es SOLLTEN von allen privaten Schlüsseln Datensicherungen erstellt werden.
  6. Beim Einsatz von EFS mit lokalen Konten SOLLTEN die lokalen Passwortspeicher mittels Syskey verschlüsselt werden.
  7. Alternativ kann der Windows Defender Credential Guard genutzt werden.
  8. Benutzende SOLLTEN im korrekten Umgang mit EFS geschult werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die Forderung nach restriktiven Zugriffsrechten entspricht dem Prinzip der geringsten Berechtigungen (Least Privilege), welches durch BER.4.1 allgemeingültig gefordert wird.

### → SYS.2.3.A8 — Einsatz von Techniken zur Rechtebeschränkung von Anwendungen (S)
  1. Zur Beschränkung der Zugriffsrechte von Anwendungen auf Dateien, Geräte und Netze SOLLTE App-Armor oder SELinux eingesetzt werden.
  2. Es SOLLTEN die von dem jeweiligen Unix-Derivat bzw. der Linux-Distribution am besten unterstützten Lösungen eingesetzt werden.
  3. Rechte SOLLTEN grundsätzlich entzogen sein und wo nötig über Positivlisten explizit erteilt werden. **◀ ZITIERT**
  4. Erweiterungen zur Rechtebeschränkung SOLLTEN im Zwangsmodus (Enforcing Mode) oder mit geeigneten Alternativen verwendet werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) BER.4.1 fordert als allgemeines Prinzip der geringsten Berechtigung (Least Privilege) genau den grundlegenden Ausschluss bzw. Entzug nicht benötigter Rechte und deren explizite Vergabe nach Erforderlichkeit.

### → SYS.2.4.A3 — Verwendung geeigneter Konten (B) [Benutzende]
  1. Das bei der Erstkonfiguration von macOS angelegte Konto hat Administrationsrechte und DARF NUR zu administrativen Zwecken verwendet werden.
  2. Für die normale Verwendung des Macs MUSS ein Konto mit Standard-Berechtigungen angelegt werden. **◀ ZITIERT**
  3. Sollte der Mac von mehreren Benutzenden verwendet werden, MUSS für jeden Benutzenden ein eigenes Konto angelegt werden.
  4. Das Gast-Konto MUSS deaktiviert werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Das Anlegen und Verwenden eines Kontos mit Standard-Berechtigungen für normale Aufgaben ist eine direkte Umsetzung des in BER.4.1 geforderten Prinzips der geringsten Berechtigungen (Least Privilege).

### → SYS.4.1.A14 — Authentisierung und Autorisierung bei Druckern, Kopierern und Multifunktionsgeräten (H)
  1. Nur berechtigte Personen SOLLTEN auf die ausgedruckten oder kopierten Dokumente zugreifen können.
  2. Es SOLLTEN möglichst nur zentrale Drucker, Kopierer und Multifunktionsgeräte eingesetzt werden, bei denen sich die Benutzenden am Gerät authentisieren, bevor der Druckauftrag startet („Secure-Print“).
  3. Nachdem sich die Benutzenden authentisiert haben, SOLLTEN ausschließlich nur die eigenen Druckaufträge sichtbar sein.
  4. Nur die für die jeweiligen Benutzenden notwendigen Funktionen SOLLTEN freigeschaltet werden. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Das in BER.4.1 geforderte Prinzip der geringsten Berechtigungen deckt die Beschränkung auf die für Benutzende zwingend notwendigen Funktionen (Least Privilege) als allgemeine Regelung direkt ab.

### → SYS.4.4.A15 — Restriktive Rechtevergabe (S)
  1. Die Zugriffsberechtigungen auf IoT-Geräte SOLLTEN möglichst restriktiv vergeben werden. **◀ ZITIERT**
  2. Wenn dies über die IoT-Geräte selber nicht möglich ist, SOLLTE überlegt werden, dies netzseitig zu regeln.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die Maßnahme BER.4.1 fordert die allgemeine Anwendung des Prinzips der geringsten Berechtigung und deckt damit die geforderte restriktive Vergabe von Zugriffsberechtigungen inhaltlich ab.

### → APP.4.2.A6 — Erstellung und Umsetzung eines Konten- und Berechtigungskonzeptes (B) [Fachabteilung, Entwickelnde]
  1. Für SAP-ERP-Systeme MUSS ein Konten- und Berechtigungskonzept ausgearbeitet und umgesetzt werden.
  2. Dabei MÜSSEN folgende Punkte berücksichtigt werden: Identitätsprinzip, Minimalprinzip, Stellenprinzip, Belegprinzip der Buchhaltung, Belegprinzip der Berechtigungsverwaltung, Funktionstrennungsprinzip (Segregation of Duties, SoD), Genehmigungsprinzip, Standardprinzip, Schriftformprinzip und Kontrollprinzip MÜSSEN berücksichtigt werden. **◀ ZITIERT**
  3. Konto-, Berechtigungs- und gegebenenfalls Profiladministrierender MÜSSEN getrennte Verantwortlichkeiten und damit Berechtigungen haben.
  4. Vorgehensweisen im Rahmen der Berechtigungsadministration für Rollen anlegen, ändern, löschen, transportieren und SU24 Vorschlagswerte transportieren MÜSSEN definiert werden.
  5. Dabei SOLLTEN Berechtigungsrollen nur im Entwicklungssystem angelegt und gepflegt werden.
  6. Sie SOLLTEN mit Hilfe des Transport-Management-Systems (TMS) transportiert werden.
  7. Berechtigungen SOLLTEN in Berechtigungsrollen (PFCG-Rollen) angelegt, gespeichert und den Konten zugeordnet werden (rollenbasiertes Berechtigungskonzept).
  8. Da sich einzelne kritische Aktionen in den Rollen nicht immer vermeiden lassen, SOLLTEN sie von kompensierenden Kontrollen (mitigation controls) abgedeckt werden.
  9. Vorgehensweisen im Rahmen der Berechtigungsvergabe für Konten und Berechtigungen beantragen, genehmigen, ändern und löschen MÜSSEN definiert werden.
  10. Namenskonventionen für Konten-Kennungen und technische Rollennamen MÜSSEN definiert werden.
  11. Vorschlagswerte und Prüfkennzeichen SOLLTEN in der Transaktion SU24 gepflegt werden.
  12. Die Vorgehensweise dazu SOLLTE im Konten- und Berechtigungskonzept beschrieben sein.
  13. Gesetzliche und interne Rahmenbedingungen wie die Grundsätze ordnungsgemäßer Buchführung (GoB), das Handelsgesetzbuch (HGB) oder interne Vorgaben der Institution MÜSSEN berücksichtigt werden.
  14. Das Konten- und Berechtigungskonzept SOLLTE auch den Betrieb technischer Konten abdecken, also auch die Berechtigung von Hintergrund- und Schnittstellenkonten.
  15. Es SOLLTEN geeignete Kontrollmechanismen angewandt werden, um SoD-Konfliktfreiheit von Rollen und die Vergabe von kritischen Berechtigungen an Konten zu überwachen.
  16. Werden neben dem ABAP-Backend weitere Komponenten wie SAP HANA und SAP NetWeaver Gateway (für Fiori-Anwendungen) verwendet, MUSS das Design der Berechtigungen zwischen den Komponenten abgestimmt und synchronisiert werden.
- **Satz 2** | Relation GS++→ED23: `subset-of` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 2) Satz 2 fordert bei der Ausarbeitung des Konten- und Berechtigungskonzepts explizit die Berücksichtigung des Minimalprinzips (Principle of Least Privilege).

### → IND.1.A7 — Etablieren einer übergreifenden Berechtigungsverwaltung zwischen der OT und in der Office-IT (S)
  1. Die Institution SOLLTE einen Prozess zur Verwaltung von Zugängen und zugeordneten Berechtigungen für den Zugriff auf die OT etablieren.
  2. Die Berechtigungsverwaltung SOLLTE den Prozess, die Durchführung und die Dokumentation für die Beantragung, Einrichtung und den Entzug von Berechtigungen umfassen.
  3. Die Berechtigungsverwaltung SOLLTE gewährleisten, dass Berechtigungen nach dem Minimalprinzip vergeben und regelmäßig überprüft werden. **◀ ZITIERT**
  4. In der Berechtigungsverwaltung SOLLTEN die Zugriffe auf IT-Systeme für Mitarbeitende, Administrierende und Dritte geregelt sein.
  5. Jeder oder jede Beteiligte SOLLTE regelmäßig zu den einzuhaltenden Regelungen sensibilisiert werden.
  6. Die Einhaltung SOLLTE überprüft werden.
  7. Fehlverhalten SOLLTE sanktioniert werden.
- **Satz 3** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 3) BER.4.1 deckt die Forderung nach der Vergabe von Berechtigungen nach dem Minimalprinzip (Prinzip der geringsten Berechtigungen) direkt ab.

### → ORP.4.A2 — Einrichtung, Änderung und Entzug von Berechtigungen (B) [IT-Betrieb]
  1. Benutzendenkennungen und Berechtigungen DÜRFEN NUR aufgrund des tatsächlichen Bedarfs und der Notwendigkeit zur Aufgabenerfüllung vergeben werden (Prinzip der geringsten Berechtigungen, englisch Least Privileges und Erforderlichkeitsprinzip, englisch Need-to-know). **◀ ZITIERT**
  2. Bei personellen Veränderungen MÜSSEN die nicht mehr benötigten Benutzendenkennungen und Berechtigungen entfernt werden.
  3. Beantragen Mitarbeitende Berechtigungen, die über den Standard hinausgehen, DÜRFEN diese NUR nach zusätzlicher Begründung und Prüfung vergeben werden.
  4. Zugriffsberechtigungen auf Systemverzeichnisse und -dateien SOLLTEN restriktiv eingeschränkt werden.
  5. Alle Berechtigungen MÜSSEN über separate administrative Rollen eingerichtet werden.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) Die Maßnahme BER.4.1 fordert explizit die Vergabe von Berechtigungen nach dem Prinzip der geringsten Berechtigungen und deckt damit die Forderung von Satz 1 inhaltlich direkt ab.

### → APP.5.4.A5 — Rollen- und Berechtigungskonzept für UCC (B)
  1. Das Rollen- und Berechtigungskonzept MUSS um UCC-spezifische Definitionen von Rollen und Berechtigungen ergänzt werden.
  2. Solche Definitionen MÜSSEN sowohl für alle internen Benutzenden als auch für die externen Benutzenden getroffen werden.
  3. Es MÜSSEN folgende Aspekte berücksichtigt werden: Berechtigungen zur zielgerichteten Benutzung von UCC-Diensten gemäß festgelegter Einsatzzwecke Berechtigungen zur Anpassung der Konfiguration von Konversationen Berechtigungen für spezielle Funktionen von UCC-Diensten wie Aufzeichnung von Konversationen und Zugriff auf Dateiablagen eines UCC-Dienstes Darüber hinaus MÜSSEN die Berechtigungen der Konten ebenfalls auf das notwendige Minimum reduziert werden. **◀ ZITIERT**
  4. Dienste, die nur für einen Teil der Benutzenden zur Verfügung stehen, DÜRFEN NICHT für die restlichen Benutzenden zugänglich sein.
  5. Zudem SOLLTEN nur Benutzende mit einer entsprechenden Berechtigung auf Daten wie Aufzeichnungen oder Dateiablagen zugreifen können.
  6. Die Festlegungen MÜSSEN festgehalten, regelmäßig und anlassbezogen geprüft und aktualisiert werden.
- **Satz 3** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme BER.4.1 deckt die Forderung nach der Beschränkung von Berechtigungen auf das notwendige Minimum als allgemeine Ausprägung des Least-Privilege-Prinzips inhaltlich ab.

### → APP.6.A4 — Regelung für die Installation und Konfiguration von Software (B) [Fachverantwortliche]
  1. Die Installation und Konfiguration der Software MUSS durch den IT-Betrieb so geregelt werden, dass die Software nur mit dem geringsten notwendigen Funktionsumfang installiert und ausgeführt wird, die Software mit den geringsten möglichen Berechtigungen ausgeführt wird, die datensparsamsten Einstellungen (in Bezug auf die Verarbeitung von personenbezogenen Daten) konfiguriert werden sowie alle relevanten Sicherheitsupdates und -patches installiert sind, bevor die Software produktiv eingesetzt wird. **◀ ZITIERT**
  2. Hierbei MÜSSEN auch abhängige Komponenten (unter anderem Laufzeitumgebungen, Bibliotheken, Schnittstellen sowie weitere Programme) mitbetrachtet werden.
  3. Der IT-Betrieb MUSS in Abstimmung mit den Fachverantwortlichen festlegen, wer die Software wie installieren darf.
  4. Idealerweise SOLLTE Software immer zentral durch den IT-Betrieb installiert werden.
  5. Ist es erforderlich, dass die Software (teilweise) manuell installiert wird, dann MUSS der IT-Betrieb eine Installationsanweisung erstellen, in der klar geregelt wird, welche Zwischenschritte zur Installation durchzuführen und welche Konfigurationen vorzunehmen sind.
  6. Darüber hinaus MUSS der IT-Betrieb regeln, wie die Integrität der Installationsdateien überprüft wird.
  7. Falls zu einem Installationspaket digitale Signaturen oder Prüfsummen verfügbar sind, MÜSSEN mit diesen die Integrität überprüft werden.
  8. Sofern erforderlich, SOLLTE der IT-Betrieb eine sichere Standardkonfiguration der Software festlegen, mit der die Software konfiguriert wird.
  9. Die Standardkonfiguration SOLLTE dokumentiert werden.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 1) Satz 1 fordert ausdrücklich, dass Software so geregelt und konfiguriert werden muss, dass sie mit den geringsten möglichen Berechtigungen ausgeführt wird, was eine direkte Umsetzung des Least-Privilege-Prinzips darstellt.

### → SYS.1.3.A14 — Verhinderung des Ausspähens von Informationen über das System und über Benutzende (H)
  1. Die Ausgabe von Informationen über das Betriebssystem und der Zugriff auf Protokoll- und Konfigurationsdateien SOLLTE für Benutzende auf das notwendige Maß beschränkt werden. **◀ ZITIERT**
  2. Außerdem SOLLTEN bei Befehlsaufrufen keine vertraulichen Informationen als Parameter übergeben werden.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) BER.4.1 fordert als übergeordnetes Prinzip der geringsten Berechtigungen die Beschränkung von Zugriffsrechten und Informationen auf das notwendige Maß, was die Einschränkung des Zugriffs auf System-, Protokoll- und Konfigurationsdateien materiell abdeckt.


## BER.7.6 — Etablierte Algorithmen beim Transport  [1 Paare]

**Statement (normativ):** Berechtigung SOLLTE die ausschließliche Verwendung etablierter kryptografischer Algorithmen beim Transport geheimer Schlüssel verankern.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Aktuelle etablierte Algorithmen sind in BSI TR-02102 zu finden. Der Transport kann mit Public Key Cryptography Standards (PKCS), z.B. PKCS#12 Dateiformat erfolgen. Für weitere Details zur Implementierung siehe Detailspezifikation kryptografischer Abläufe und Mechanismen des BSI.

### → CON.1.A4 — Geeignetes Schlüsselmanagement (B)
  1. In einem geeigneten Schlüsselmanagement für kryptografische Hard oder Software MUSS festgelegt werden, wie Schlüssel und Zertifikate erzeugt, gespeichert, ausgetauscht und wieder gelöscht oder vernichtet werden.
  2. Es MUSS ferner festgelegt werden, wie die Integrität und Authentizität der Schlüssel sichergestellt wird.
  3. Kryptografische Schlüssel SOLLTEN immer mit geeigneten Schlüsselgeneratoren und in einer sicheren Umgebung erzeugt werden.
  4. In Hard- oder Software mit kryptografischen Funktionen SOLLTEN voreingestellte Schlüssel (ausgenommen öffentliche Zertifikate) ersetzt werden.
  5. Ein Schlüssel SOLLTE möglichst nur einem Einsatzzweck dienen.
  6. Insbesondere SOLLTEN für die Verschlüsselung und Signaturbildung unterschiedliche Schlüssel benutzt werden.
  7. Kryptografische Schlüssel SOLLTEN mit sicher geltenden Verfahren ausgetauscht werden. **◀ ZITIERT**
  8. Wenn öffentliche Schlüssel von Dritten verwendet werden, MUSS sichergestellt sein, dass die Schlüssel authentisch sind und die Integrität der Schlüsseldaten gewährleistet ist.
  9. Geheime Schlüssel MÜSSEN sicher gespeichert und vor unbefugtem Zugriff geschützt werden.
  10. Alle kryptografischen Schlüssel SOLLTEN hinreichend häufig gewechselt werden.
  11. Grundsätzlich SOLLTE geregelt werden, wie mit abgelaufenen Schlüsseln und damit verbundenen Signaturen verfahren wird.
  12. Falls die Gültigkeit von Schlüsseln oder Zertifikaten zeitlich eingeschränkt wird, dann MUSS durch die Institution sichergestellt werden, dass die zeitlich eingeschränkten Zertifikate oder Schlüssel rechtzeitig erneuert werden.
  13. Eine Vorgehensweise SOLLTE für den Fall festgelegt werden, dass ein privater Schlüssel offengelegt wird.
  14. Alle erzeugten kryptografischen Schlüssel SOLLTEN sicher aufbewahrt und verwaltet werden.
- **Satz 7** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 7) BER.7.6 fordert die ausschließliche Nutzung etablierter kryptografischer Algorithmen beim Transport geheimer Schlüssel und deckt damit den sicheren Schlüsselaustausch direkt ab.


## BER.7.12 — Authentizität  [3 Paare]

**Statement (normativ):** Berechtigung SOLLTE die Verifikation der Authentizität öffentlicher Schlüssel vor jeder Nutzung verankern.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Für die Implementierung genügt es, wenn die eingesetzten IT-Produkte bereits so entwickelt oder beschafft worden sind, dass sie die Prüfung automatisiert durchführen.

### → SYS.2.1.A18 — Nutzung von verschlüsselten Kommunikationsverbindungen (S)
  1. Kommunikationsverbindungen SOLLTEN, soweit möglich, durch Verschlüsselung geschützt werden.
  2. Die Clients SOLLTEN kryptografische Algorithmen und Schlüssellängen verwenden, die dem Stand der Technik und den Sicherheitsanforderungen der Institution entsprechen.
  3. Neue Zertifikate von Zertifikatsausstellern SOLLTEN erst nach Überprüfung des Fingerprints aktiviert werden. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die Überprüfung des Fingerprints neuer CA-Zertifikate vor der Aktivierung ist eine konkrete Ausprägung der Verifikation der Authentizität öffentlicher Schlüssel.

### → CON.1.A4 — Geeignetes Schlüsselmanagement (B)
  1. In einem geeigneten Schlüsselmanagement für kryptografische Hard oder Software MUSS festgelegt werden, wie Schlüssel und Zertifikate erzeugt, gespeichert, ausgetauscht und wieder gelöscht oder vernichtet werden.
  2. Es MUSS ferner festgelegt werden, wie die Integrität und Authentizität der Schlüssel sichergestellt wird. **◀ ZITIERT**
  3. Kryptografische Schlüssel SOLLTEN immer mit geeigneten Schlüsselgeneratoren und in einer sicheren Umgebung erzeugt werden.
  4. In Hard- oder Software mit kryptografischen Funktionen SOLLTEN voreingestellte Schlüssel (ausgenommen öffentliche Zertifikate) ersetzt werden.
  5. Ein Schlüssel SOLLTE möglichst nur einem Einsatzzweck dienen.
  6. Insbesondere SOLLTEN für die Verschlüsselung und Signaturbildung unterschiedliche Schlüssel benutzt werden.
  7. Kryptografische Schlüssel SOLLTEN mit sicher geltenden Verfahren ausgetauscht werden.
  8. Wenn öffentliche Schlüssel von Dritten verwendet werden, MUSS sichergestellt sein, dass die Schlüssel authentisch sind und die Integrität der Schlüsseldaten gewährleistet ist. **◀ ZITIERT**
  9. Geheime Schlüssel MÜSSEN sicher gespeichert und vor unbefugtem Zugriff geschützt werden.
  10. Alle kryptografischen Schlüssel SOLLTEN hinreichend häufig gewechselt werden.
  11. Grundsätzlich SOLLTE geregelt werden, wie mit abgelaufenen Schlüsseln und damit verbundenen Signaturen verfahren wird.
  12. Falls die Gültigkeit von Schlüsseln oder Zertifikaten zeitlich eingeschränkt wird, dann MUSS durch die Institution sichergestellt werden, dass die zeitlich eingeschränkten Zertifikate oder Schlüssel rechtzeitig erneuert werden.
  13. Eine Vorgehensweise SOLLTE für den Fall festgelegt werden, dass ein privater Schlüssel offengelegt wird.
  14. Alle erzeugten kryptografischen Schlüssel SOLLTEN sicher aufbewahrt und verwaltet werden.
- **Satz 2** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die Maßnahme verankert die Prüfung der Authentizität öffentlicher Schlüssel vor jeder Nutzung und deckt damit als konkrete Umsetzungsvorgabe einen wesentlichen Teilaspekt der Sicherstellung von Schlüsselauthentizität ab.
- **Satz 8** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 8) BER.7.12 fordert die Verifikation der Authentizität öffentlicher Schlüssel vor deren Nutzung und deckt damit die geforderte Prüfung bei der Verwendung öffentlicher Schlüssel inhaltlich ab.


## BER.2.4 — Protokollierung von Stammdatenänderungen  [1 Paare]

**Statement (normativ):** Berechtigung SOLLTE Änderungen von Identitäts-Stammdaten protokollieren.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Zu einem Ereignisprotokoll gehört der Zeitpunkt, das Zugangskonto, sowie welche Änderungen vorgenommen wurden.

### → APP.2.1.A12 — Überwachung von Verzeichnisdiensten (S)
  1. Verzeichnisdienste SOLLTEN gemeinsam mit dem Server beobachtet und protokolliert werden, auf dem sie betrieben werden.
  2. Insbesondere Änderungen innerhalb des Verzeichnisdienstes sowie Konfigurationsänderungen des Verzeichnisdienstes SOLLTEN vorrangig protokolliert werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) BER.2.4 fordert die Protokollierung von Änderungen an Identitäts-Stammdaten, was die Protokollierung von Änderungen innerhalb des Verzeichnisdienstes inhaltlich abdeckt.

