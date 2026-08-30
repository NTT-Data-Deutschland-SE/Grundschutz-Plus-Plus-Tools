# Review-Dossier Praktik KONF

Praktik KONF: 146 Controls mit Mapping, 1193 Paare gesamt. Gesampelt: 5 Controls (max/min/median Paarzahl + 2 zufällig).

## KONF.2.4 — Deaktivierung nicht benötigter Systemfunktionen  [88 Paare]

**Statement (normativ):** Konfiguration für IT-Systeme SOLLTE nicht benötigte Systemfunktionen deaktivieren.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Die Deaktivierung von Funktionen, die für Betrieb oder aus Sicherheitssicht nicht benötigt werden, hilft, die Angriffsfläche und Fehlerkomplexität zu verringern, z.B. unnötige Identitäten, ggf. nicht benötigte Schnittstellen wie Bluetooth, nicht verwendete Netzprotokolle wie NTLMv1 Authentifizierung, schwache Verschlüsselungsalgorithmen wie TLS1.1, die Anzeige von Nachrichteninhalten auf dem Sperrbildschirm oder nicht benötigte System- oder Telemetriedienste. Relevant sind dabei sowohl Betriebssystem- als auch Firmwarefunktionen.

### → APP.2.2.A5 — Absicherung des Domänencontrollers (B)
  1. Aufgrund der zentralen Rolle und der Schadensauswirkung bei Kompromittierung des AD DS für die Infrastruktur SOLLTE eine Risikobetrachtung durchgeführt werden.
  2. Der Notfallzugriff auf den Domänencontroller mit dem lokalen Restore-Konto DSRM (Directory Services Restore Mode) MUSS im Rahmen des Notfallmanagements geplant werden.
  3. Auf dem Domänencontroller MUSS eine ausreichende Größe für das Sicherheitsprotokoll auf Grundlage des in DER.1 Detektion von sicherheitsrelevanten Ereignissen festgelegten Zeitraums eingestellt sein.
  4. Aufgrund der zentralen Bedeutung des Domänencontrollers SOLLTEN auf diesem Server keine weiteren Dienste betrieben werden, sofern diese nicht zwingend auf dem gleichen Server zum Betrieb des AD DS erforderlich sind. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) KONF.2.4 fordert allgemeingültig die Deaktivierung nicht benötigter Systemfunktionen und -dienste, was die Beschränkung des Domänencontrollers auf zwingend erforderliche Dienste sachlich abdeckt.

### → APP.2.2.A9 — Schutz der Authentisierung beim Einsatz von AD DS (S)
  1. In der Gesamtstruktur SOLLTE konsequent das Authentisierungsprotokoll Kerberos eingesetzt werden.
  2. Dabei SOLLTE für die Absicherung AES128_HMAC_SHA1 oder AES256_HMAC_SHA1 verwendet werden.
  3. Wenn aus Kompatibilitätsgründen übergangsweise NTLMv2 eingesetzt wird, SOLLTE die Migration auf Kerberos geplant und terminiert werden.
  4. Die LM-Authentisierung und NTLMv1 MÜSSEN deaktiviert sein. **◀ ZITIERT**
  5. Der SMB-Datenverkehr MUSS signiert sein.
  6. SMBv1 MUSS deaktiviert sein. **◀ ZITIERT**
  7. Anonyme Zugriffe auf Domänencontroller SOLLTEN unterbunden sein.
  8. LDAP-Sitzungen SOLLTEN nur signiert und mit konfiguriertem Channel Binding Token (CBT) erfolgen.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) KONF.2.4 fordert die Deaktivierung nicht benötigter bzw. unsicherer Systemfunktionen und Protokolle und nennt NTLMv1-Authentifizierung dabei explizit als Beispiel.
- **Satz 6** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 6) Die Deaktivierung des veralteten und unsicheren Protokolls SMBv1 stellt einen konkreten Anwendungsfall der allgemeinen Vorgabe in KONF.2.4 zur Abschaltung nicht benötigter oder unsicherer Systemfunktionen und Netzprotokolle dar.

### → APP.3.1.A12 — Sichere Konfiguration (S)
  1. Webanwendungen und Webservices SOLLTEN so konfiguriert sein, dass auf ihre Ressourcen und Funktionen ausschließlich über die vorgesehenen, abgesicherten Kommunikationspfade zugegriffen werden kann.
  2. Der Zugriff auf nicht benötigte Ressourcen und Funktionen SOLLTE deaktiviert werden. **◀ ZITIERT**
  3. Falls dies nicht möglich ist, SOLLTE der Zugriff soweit wie möglich eingeschränkt werden.
  4. Folgendes SOLLTE bei der Konfiguration von Webanwendungen und Webservices umgesetzt werden: Deaktivieren nicht benötigter HTTP-Methoden, Konfigurieren der Zeichenkodierung, Vermeiden von sicherheitsrelevanten Informationen in Fehlermeldungen und Antworten, Speichern von Konfigurationsdateien außerhalb des Web-Root-Verzeichnisses sowie Festlegen von Grenzwerten für Zugriffsversuche.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 2) Satz 2 fordert explizit das Deaktivieren des Zugriffs auf nicht benötigte Ressourcen und Funktionen im Kontext von Webanwendungen, was direkt der Deaktivierung nicht benötigter Systemfunktionen aus KONF.2.4 entspricht.

### → IND.1.A9 — Restriktiver Einsatz von Wechseldatenträgern und mobilen Endgeräten in ICS-Umgebungen (S)
  1. Für die Nutzung von Wechseldatenträgern und mobilen Endgeräten SOLLTEN Regelungen aufgestellt und bekannt gegeben werden.
  2. Der Einsatz von Wechseldatenträgern und mobilen Endgeräten in ICS-Umgebungen SOLLTE beschränkt werden.
  3. Für Medien und Geräte von Dienstleistenden SOLLTEN ein Genehmigungsprozess und eine Anforderungsliste existieren.
  4. Die Vorgaben SOLLTEN allen Dienstleistenden bekannt sein und von diesen schriftlich bestätigt werden.
  5. Auf den OT-Komponenten SOLLTEN alle nicht benötigten Schnittstellen deaktiviert werden. **◀ ZITIERT**
  6. An den aktiven Schnittstellen SOLLTE die Nutzung auf bestimmte Geräte oder Medien eingeschränkt werden.
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen und deckt damit als allgemeinere Maßnahme das Deaktivieren nicht benötigter Schnittstellen auf Systemen (wie OT-Komponenten) direkt ab.

### → IND.2.1.A4 — Deaktivierung oder Deinstallation nicht genutzter Dienste, Funktionen und Schnittstellen (B) [Wartungspersonal, OT-Betrieb (Operational Technology, OT)]
  1. Alle nicht genutzten Dienste, Funktionen und Schnittstellen der ICS-Komponenten MÜSSEN deaktiviert oder deinstalliert werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen, Dienste und Schnittstellen und deckt damit die allgemeinere Fassung der im Satz geforderten Maßnahme für IT-/ICS-Systeme direkt ab.

### → IND.2.3.A3 — Drahtlose Kommunikation (H)
  1. Drahtlose Verwaltungsschnittstellen wie Bluetooth, WLAN oder NFC SOLLTEN NICHT benutzt werden.
  2. Alle nicht benutzten Kommunikationsschnittstellen SOLLTEN deaktiviert werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen und deckt damit als allgemeinere Formulierung das Deaktivieren nicht benutzter Kommunikationsschnittstellen direkt ab.

### → IND.3.2.A12 — Dedizierte Fernwartungslösung in der OT (H) [Planende]
  1. Für die Fernwartung im industriellen Umfeld SOLLTE eine dedizierte OT-Fernwartungslösung eingesetzt werden, die unabhängig von der Büro- und Gebäude-IT ist.
  2. Alle weiteren Funktionen auf den IT-Systemen zur OT-Fernwartung, insbesondere auch Funktionen zur Administration von IT-Systemen und Netzen außerhalb der OT, SOLLTEN deaktiviert bzw. unterbunden werden. **◀ ZITIERT**
  3. Falls eine maximale Unabhängigkeit realisiert werden soll, SOLLTE auch ein dedizierter Internet-Zugang für die OT-Fernwartung genutzt werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme fordert allgemein die Deaktivierung nicht benötigter Systemfunktionen auf IT-Systemen und deckt damit die Deaktivierung nicht relevanter Funktionen auf OT-Fernwartungssystemen inhaltlich ab.

### → INF.14.A11 — Absicherung von frei zugänglichen Ports und Zugängen der GA (S) [Planende]
  1. Der Anschluss von Komponenten, speziell von unautorisierten, unbekannten Komponenten und Fremdgeräten, SOLLTE insbesondere an frei zugänglichen Ethernet-Ports, USB-Ports und anderen Schnittstellen der GA kontrolliert und eingeschränkt werden.
  2. Der Anschluss einer unautorisierten oder unbekannten Komponente SOLLTE in die Ereignisprotokollierung aufgenommen werden.
  3. Eine direkte IP-basierte Kommunikation von solchen Komponenten mit Systemen der GA SOLLTE unterbunden werden (siehe INF.14.A13 Netzsegementierung in der GA).
  4. Für frei zugängliche LAN- oder WLAN-Zugänge SOLLTE eine Netzzugangskontrolle gemäß IEEE 802.1X oder vergleichbare Sicherheitsmechanismen eingesetzt werden.
  5. Hiermit SOLLTEN unzureichend authentisierte und autorisierte Komponenten in getrennten Netzsegmenten positioniert werden.
  6. Frei zugängliche Schnittstellen für temporäre Wartungszwecke, wie beispielsweise USB-Ports an GA-Komponenten, SOLLTEN nur bei Bedarf aktiviert werden. **◀ ZITIERT**
- **Satz 6** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 6) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen und Schnittstellen, was das Deaktiviert-Halten und bedarfsweise Aktivieren temporärer Wartungsschnittstellen als allgemeine Maßnahme abdeckt.

### → NET.1.2.A22 — Beschränkung der Management-Funktionen (S)
  1. Es SOLLTEN NUR die benötigten Management-Funktionen aktiviert werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen, was als allgemeinere Fassung die Beschränkung auf benötigte Management-Funktionen inhaltlich abdeckt.

### → NET.2.1.A5 — Sichere Basis-Konfiguration der Access Points (B)
  1. Access Points DÜRFEN NICHT in der Konfiguration des Auslieferungszustandes verwendet werden.
  2. Voreingestellte SSIDs (Service Set Identifiers), Zugangskennwörter oder kryptografische Schlüssel MÜSSEN vor dem produktiven Einsatz geändert werden.
  3. Außerdem MÜSSEN unsichere Administrationszugänge abgeschaltet werden. **◀ ZITIERT**
  4. Access Points DÜRFEN NUR über eine geeignet verschlüsselte Verbindung administriert werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) KONF.2.4 deckt das Abschalten unsicherer Administrationszugänge als allgemeine Deaktivierung aus Sicherheitssicht nicht benötigter bzw. unsicherer Systemfunktionen, Protokolle und Schnittstellen inhaltlich ab.

### → NET.2.2.A3 — Absicherung der WLAN-Nutzung an Hotspots (B) [IT-Betrieb]
  1. Dürfen Hotspots genutzt werden, MUSS Folgendes umgesetzt werden: Jede(r) Benutzende eines Hotspots MUSS seine oder ihre Sicherheitsanforderungen kennen und danach entscheiden, ob und unter welchen Bedingungen ihm oder ihr die Nutzung des Hotspots erlaubt ist.
  2. Werden Hotspots genutzt, dann SOLLTE sichergestellt werden, dass die Verbindung zwischen Hotspot-Access Point und IT-Systemen der Benutzenden nach dem Stand der Technik kryptografisch abgesichert wird.
  3. WLANs, die nur sporadisch genutzt werden, SOLLTEN von den Benutzenden aus der Historie gelöscht werden.
  4. Die automatische Anmeldung an WLANs SOLLTE deaktiviert werden.
  5. Wenn möglich, SOLLTEN separate Konten mit einer sicheren Grundkonfiguration und restriktiven Berechtigungen verwendet werden.
  6. Es SOLLTE sichergestellt sein, dass sich keine Benutzenden mit administrativen Berechtigungen von ihren Clients aus an externen WLANs anmelden können.
  7. Sensible Daten DÜRFEN NUR übertragen werden, wenn allen notwendigen Sicherheitsmaßnahmen auf den Clients, vor allem eine geeignete Verschlüsselung, aktiviert sind.
  8. Wird die WLAN-Schnittstelle über einen längeren Zeitraum nicht genutzt, MUSS diese deaktiviert werden. **◀ ZITIERT**
  9. Über öffentlich zugängliche WLANs DÜRFEN die Benutzenden NUR über ein Virtual Private Network (VPN) auf interne Ressourcen der Institution zugreifen.
- **Satz 8** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 8) Die Deaktivierung der zeitweise nicht genutzten WLAN-Schnittstelle stellt einen konkreten Anwendungsfall der allgemeinen Pflicht zur Deaktivierung nicht benötigter Schnittstellen und Systemfunktionen dar.

### → NET.3.1.A1 — Sichere Grundkonfiguration eines Routers oder Switches (B)
  1. Bevor ein Router oder Switch eingesetzt wird, MUSS er sicher konfiguriert werden.
  2. Alle Konfigurationsänderungen SOLLTEN nachvollziehbar dokumentiert sein.
  3. Die Integrität der Konfigurationsdateien MUSS in geeigneter Weise geschützt werden.
  4. Bevor Zugangspasswörter abgespeichert werden, MÜSSEN sie mithilfe eines zeitgemäßen kryptografischen Verfahrens abgesichert werden.
  5. Router und Switches MÜSSEN so konfiguriert sein, dass nur zwingend erforderliche Dienste, Protokolle und funktionale Erweiterungen genutzt werden. **◀ ZITIERT**
  6. Nicht benötigte Dienste, Protokolle und funktionale Erweiterungen MÜSSEN deaktiviert oder ganz deinstalliert werden. **◀ ZITIERT**
  7. Ebenfalls MÜSSEN nicht benutzte Schnittstellen auf Routern und Switches deaktiviert werden.
  8. Unbenutzte Netzports MÜSSEN nach Möglichkeit deaktiviert oder zumindest einem dafür eingerichteten Unassigned-VLAN zugeordnet werden.
  9. Wenn funktionale Erweiterungen benutzt werden, MÜSSEN die Sicherheitsrichtlinien der Institution weiterhin erfüllt sein.
  10. Auch SOLLTE begründet und dokumentiert werden, warum solche Erweiterungen eingesetzt werden.
  11. Informationen über den internen Konfigurations- und Betriebszustand MÜSSEN nach außen verborgen werden.
  12. Unnötige Auskunftsdienste MÜSSEN deaktiviert werden. **◀ ZITIERT**
- **Satz 12** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 12) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen und -dienste, was die Abschaltung unnötiger Auskunftsdienste als allgemeinere Maßnahme direkt abdeckt.
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen (inklusive Protokollen und Diensten) für IT-Systeme und deckt damit die Beschränkung auf zwingend erforderliche Dienste und Protokolle allgemein ab.
- **Satz 6** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 6) KONF.2.4 fordert allgemein die Deaktivierung nicht benötigter Systemfunktionen inklusive Dienste und Protokolle und deckt damit die Forderung von Satz 6 direkt ab.

### → NET.3.1.A13 — Administration über ein gesondertes Managementnetz (S)
  1. Router und Switches SOLLTEN ausschließlich über ein separates Managementnetz (Out-of-Band-Management) administriert werden.
  2. Eine eventuell vorhandene Administrationsschnittstelle über das eigentliche Datennetz (In-Band) SOLLTE deaktiviert werden. **◀ ZITIERT**
  3. Die verfügbaren Sicherheitsmechanismen der eingesetzten Managementprotokolle zur Authentisierung, Integritätssicherung und Verschlüsselung SOLLTEN aktiviert werden.
  4. Alle unsicheren Managementprotokolle SOLLTEN deaktiviert werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die Deaktivierung der In-Band-Administrationsschnittstelle stellt einen konkreten Anwendungsfall der allgemeinen Deaktivierung nicht benötigter Schnittstellen und Systemfunktionen gemäß KONF.2.4 dar.

### → NET.3.1.A4 — Schutz der Administrationsschnittstellen (B)
  1. Alle Administrations- und Managementzugänge der Router und Switches MÜSSEN auf einzelne Quell-IP-Adressen bzw. -Adressbereiche eingeschränkt werden.
  2. Es MUSS sichergestellt sein, dass aus nicht vertrauenswürdigen Netzen heraus nicht direkt auf die Administrationsschnittstellen zugegriffen werden kann.
  3. Um Router und Switches zu administrieren bzw. zu überwachen, SOLLTEN geeignet verschlüsselte Protokolle eingesetzt werden.
  4. Sollte dennoch auf unverschlüsselte Protokolle zurückgegriffen werden, MUSS für die Administration ein eigenes Administrationsnetz (Out-of-Band-Management) genutzt werden.
  5. Die Managementschnittstellen und die Administrationsverbindungen MÜSSEN durch eine separate Firewall geschützt werden.
  6. Für die Schnittstellen MÜSSEN geeignete Zeitbeschränkungen für z. B. Timeouts vorgegeben werden.
  7. Alle für das Management-Interface nicht benötigten Dienste MÜSSEN deaktiviert werden. **◀ ZITIERT**
  8. Verfügt eine Netzkomponente über eine dedizierte Hardwareschnittstelle, MUSS der unberechtigte Zugriff darauf in geeigneter Weise unterbunden werden.
- **Satz 7** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 7) KONF.2.4 fordert allgemein die Deaktivierung nicht benötigter Systemfunktionen und Dienste, was das Deaktivieren nicht benötigter Dienste für Management-Schnittstellen direkt umfasst.

### → NET.3.2.A17 — Deaktivierung von IPv4 oder IPv6 (S)
  1. Wenn das IPv4- oder IPv6-Protokoll in einem Netzsegment nicht benötigt wird, SOLLTE es am jeweiligen Firewall-Netzzugangspunkt (z. B. am entsprechenden Firewall-Interface) deaktiviert werden. **◀ ZITIERT**
  2. Falls das IPv4- oder IPv6-Protokoll nicht benötigt bzw. eingesetzt wird, SOLLTE es auf der Firewall komplett deaktiviert werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) KONF.2.4 fordert allgemein die Deaktivierung nicht benötigter Systemfunktionen und Netzwerkprotokolle auf IT-Systemen, was das selektive Deaktivieren von IPv4 bzw. IPv6 an Schnittstellen umfasst.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) KONF.2.4 fordert allgemein die Deaktivierung nicht benoetigter Systemfunktionen und Netzwerkprotokolle auf IT-Systemen, was die vollstaendige Deaktivierung ungenutzter Protokolle wie IPv4/IPv6 auf einer Firewall abdeckt.

### → NET.3.2.A4 — Sichere Konfiguration der Firewall (B)
  1. Bevor eine Firewall eingesetzt wird, MUSS sie sicher konfiguriert werden.
  2. Alle Konfigurationsänderungen MÜSSEN nachvollziehbar dokumentiert sein.
  3. Die Integrität der Konfigurationsdateien MUSS geeignet geschützt werden.
  4. Bevor Zugangspasswörter abgespeichert werden, MÜSSEN sie mithilfe eines zeitgemäßen kryptografischen Verfahrens abgesichert werden (siehe CON.1 Kryptokonzept).
  5. Eine Firewall MUSS so konfiguriert sein, dass ausschließlich zwingend erforderliche Dienste verfügbar sind. **◀ ZITIERT**
  6. Wenn funktionale Erweiterungen benutzt werden, MÜSSEN die Sicherheitsrichtlinien der Institution weiterhin erfüllt sein.
  7. Auch MUSS begründet und dokumentiert werden, warum solche Erweiterungen eingesetzt werden.
  8. Nicht benötigte (Auskunfts-)Dienste sowie nicht benötigte funktionale Erweiterungen MÜSSEN deaktiviert oder ganz deinstalliert werden.
  9. Informationen über den internen Konfigurations- und Betriebszustand MÜSSEN nach außen bestmöglich verborgen werden.
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen und -dienste auf IT-Systemen und deckt damit die Beschränkung auf ausschließlich erforderliche Dienste auf einer Firewall inhaltlich ab.

### → NET.3.2.A8 — Unterbindung von dynamischem Routing (B)
  1. In den Einstellungen der Firewall MUSS das dynamische Routing deaktiviert sein, es sei denn, der Paketfilter wird entsprechend dem Baustein NET.3.1 Router und Switches als Perimeter-Router eingesetzt. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) KONF.2.4 fordert allgemein die Deaktivierung nicht benötigter Systemfunktionen und Netzwerkprotokolle, was die Deaktivierung von dynamischem Routing auf Firewalls als Spezialfall einschließt.

### → NET.4.1.A16 — Sicherung von Endgeräten in frei zugänglichen Räumen (S)
  1. Der Funktionsumfang der Endgeräte, die in frei zugänglichen Räumen aufgestellt werden sollen, SOLLTE eingeschränkt werden. **◀ ZITIERT**
  2. Ist dies nicht möglich, SOLLTE das Endgerät in geeigneter Weise vor unbefugtem Zugriff geschützt werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) KONF.2.4 deckt die Forderung als allgemeinere Maßnahme zur Deaktivierung und Einschränkung nicht benötigter Systemfunktionen auf IT-Systemen inhaltlich ab.

### → NET.4.1.A8 — Einschränkung und Sperrung nicht benötigter oder sicherheitskritischer Leistungsmerkmale (S)
  1. Der Umfang der verfügbaren Leistungsmerkmale SOLLTE auf das notwendige Minimum beschränkt werden. **◀ ZITIERT**
  2. Nur die benötigten Leistungsmerkmale SOLLTEN freigeschaltet werden. **◀ ZITIERT**
  3. Die nicht benötigten oder wegen ihres Missbrauchspotenzials als kritisch eingestuften Leistungsmerkmale SOLLTEN so weit wie möglich an der zentralen Anlage abgeschaltet werden. **◀ ZITIERT**
  4. Zusätzliche Schutzmaßnahmen SOLLTEN für die auf den Endgeräten gespeicherten und abrufbaren vertraulichen Daten ergriffen werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Das Deaktivieren nicht benötigter Systemfunktionen nach KONF.2.4 setzt die Beschränkung der verfügbaren Leistungsmerkmale auf das notwendige Minimum direkt um.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die Beschränkung der Freischaltung auf benötigte Leistungsmerkmale entspricht inhaltlich der allgemeinen Forderung von KONF.2.4, nicht benötigte Systemfunktionen zu deaktivieren.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) KONF.2.4 deckt das Abschalten nicht benötigter bzw. kritischer Leistungsmerkmale und Funktionen auf Systemebene als allgemeinere Grundanforderung vollständig ab.

### → NET.4.2.A3 — Sichere Administration und Konfiguration von VoIP-Endgeräten (B)
  1. Nicht benötigte Funktionen der Endgeräte MÜSSEN deaktiviert werden. **◀ ZITIERT**
  2. Die Konfigurationseinstellungen DÜRFEN NICHT unberechtigt geändert werden.
  3. Alle Sicherheitsfunktionen der Endgeräte SOLLTEN vor dem produktiven Einsatz getestet werden.
  4. Die eingesetzten Sicherheitsmechanismen und die verwendeten Parameter SOLLTEN dokumentiert werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) KONF.2.4 fordert allgemein die Deaktivierung nicht benötigter Systemfunktionen bei IT-Systemen und deckt damit die Deaktivierung nicht benötigter Funktionen auf Endgeräten direkt ab.

### → OPS.1.1.7.A12 — Auslösung von Aktionen durch die zentralen Komponenten der Systemmanagement-Lösung (S)
  1. Aktionen, die durch das Systemmanagement auf den verwalteten Systemen ausgeführt werden, SOLLTEN ausschließlich von der Systemmanagement-Lösung ausgelöst werden.
  2. Dafür SOLLTEN nur diejenigen Management-Funktionen auf der Systemmanagement-Lösung und den zu verwaltenden Systemen aktiviert werden, die tatsächlich benötigt werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) KONF.2.4 fordert allgemein die Deaktivierung nicht benötigter Systemfunktionen auf IT-Systemen und deckt damit die Beschränkung auf tatsächlich benötigte Management-Funktionen inhaltlich ab.

### → OPS.1.2.5.A14 — Dedizierte Clients und Konten bei der Fernwartung (H)
  1. Zur Fernwartung SOLLTEN IT-Systeme eingesetzt werden, die ausschließlich zur Administration von anderen IT-Systemen dienen.
  2. Alle weiteren Funktionen auf diesen IT-Systemen SOLLTEN deaktiviert werden. **◀ ZITIERT**
  3. Die Netzkommunikation der Administrationssysteme SOLLTE so eingeschränkt werden, dass nur Verbindungen zu IT-Systemen möglich sind, die administriert werden sollen.
  4. Für Fernwartungszugänge SOLLTEN dedizierte Konten verwendet werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) KONF.2.4 fordert allgemein die Deaktivierung nicht benötigter Systemfunktionen auf IT-Systemen und deckt damit die Deaktivierung aller weiteren Funktionen auf dedizierten Administrationsclients vollständig ab.

### → OPS.1.2.5.A24 — Absicherung integrierter Fernwartungssysteme (S)
  1. Bei der Beschaffung von neuen IT-Systemen SOLLTE geprüft werden, ob diese IT-Systeme oder einzelne Komponenten der IT-Systeme über Funktionen zur Fernwartung verfügen.
  2. Werden diese Funktionen nicht verwendet, SOLLTEN sie deaktiviert werden. **◀ ZITIERT**
  3. Die Funktionen SOLLTEN ebenfalls deaktiviert werden, wenn sie durch bekannte Sicherheitslücken gefährdet sind.
  4. Werden Fernwartungsfunktionen verwendet, die in die Firmware einzelner Komponenten integriert sind, SOLLTEN deren Funktionen und der Zugriff darauf so weit wie möglich eingeschränkt werden.
  5. Die Fernwartungsfunktionen SOLLTEN nur aus einem getrennten Managementnetz erreichbar sein.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) KONF.2.4 fordert die Deaktivierung nicht benötigter System- und Firmwarefunktionen, was die Deaktivierung ungenutzter Fernwartungsfunktionen als allgemeine Vorgabe materiell abdeckt.

### → SYS.1.1.A5 — Schutz von Schnittstellen (B)
  1. Es MUSS gewährleistet werden, dass nur dafür vorgesehene Wechselspeicher und sonstige Geräte an die Server angeschlossen werden können.
  2. Alle Schnittstellen, die nicht verwendet werden, MÜSSEN deaktiviert werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen auf IT-Systemen, was das Deaktivieren nicht genutzter Schnittstellen als allgemeinere Maßnahme und laut Erläuterung explizit umfasst.

### → SYS.1.1.A6 — Deaktivierung nicht benötigter Dienste (B)
  1. Alle nicht benötigten Serverrollen, Features und Funktionen, sonstige Software und Dienste MÜSSEN deaktiviert oder deinstalliert werden, vor allem Netzdienste. **◀ ZITIERT**
  2. Auch alle nicht benötigten Funktionen in der Firmware MÜSSEN deaktiviert werden. **◀ ZITIERT**
  3. Die Empfehlungen des Betriebssystemherstellers SOLLTEN hierbei als Orientierung berücksichtigt werden.
  4. Auf Servern SOLLTE der Speicherplatz für die einzelnen Benutzenden, aber auch für Anwendungen, geeignet beschränkt werden.
  5. Die getroffenen Entscheidungen SOLLTEN so dokumentiert werden, dass nachvollzogen werden kann, welche Konfiguration und Softwareausstattung für die Server gewählt wurden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) KONF.2.4 fordert allgemein die Deaktivierung nicht benötigter Systemfunktionen und deckt damit die Deaktivierung bzw. Deinstallation nicht benötigter Rollen, Software und Dienste inhaltlich ab.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen und schließt laut Erläuterung explizit auch Firmwarefunktionen mit ein.

### → SYS.1.2.2.A1 — Planung von Windows Server 2012 (B)
  1. Der Einsatz von Windows Server 2012 MUSS vor der Installation sorgfältig geplant werden.
  2. Die Anforderungen an die Hardware MÜSSEN vor der Beschaffung geprüft werden.
  3. Es MUSS eine begründete und dokumentierte Entscheidung für eine geeignete Edition des Windows Server 2012 getroffen werden.
  4. Der Einsatzzweck des Servers sowie die Einbindung ins Active Directory MÜSSEN dabei spezifiziert werden.
  5. Die Nutzung von ins Betriebssystem integrierten Cloud-Diensten MUSS grundsätzlich abgewogen und geplant werden.
  6. Wenn nicht benötigt, MUSS die Einrichtung von Microsoft-Konten auf dem Server blockiert werden. **◀ ZITIERT**
- **Satz 6** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 6) Die Deaktivierung bzw. Blockierung nicht benötigter Microsoft-Konten stellt das Abschalten einer nicht benötigten Systemfunktion bzw. Identitätsart dar und wird durch KONF.2.4 allgemein abgedeckt.

### → SYS.1.2.2.A2 — Sichere Installation von Windows Server 2012 (B)
  1. Es DÜRFEN KEINE anderen als die benötigten Serverrollen und Features bzw. Funktionen installiert werden. **◀ ZITIERT**
  2. Wenn es vom Funktionsumfang her ausreichend ist, MUSS die Server-Core-Variante installiert werden.
  3. Andernfalls MUSS begründet werden, warum die Server-Core-Variante nicht genügt.
  4. Der Server MUSS bereits während der Installation auf einen aktuellen Patch-Stand gebracht werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) KONF.2.4 fordert die allgemeine Deaktivierung bzw. Minimierung nicht benötigter Systemfunktionen, was das Verbot der Installation nicht benötigter Serverrollen und Features inhaltlich abdeckt.

### → SYS.1.2.3.A1 — Planung von Windows Server (B)
  1. Es MUSS eine begründete und dokumentierte Entscheidung für eine geeignete Edition von Windows Server getroffen werden.
  2. Der Einsatzzweck des Servers sowie die Einbindung ins Active Directory MÜSSEN dabei spezifiziert werden.
  3. Die Nutzung von mitgelieferten Cloud-Diensten im Betriebssystem MUSS grundsätzlich abgewogen und gründlich geplant werden.
  4. Wenn nicht benötigt, MUSS die Einrichtung von Microsoft-Konten auf dem Server blockiert werden. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen und Identitäten, was das Blockieren der Einrichtung nicht benötigter Microsoft-Konten auf dem Server als allgemeine Anforderung abdeckt.

### → SYS.1.2.3.A2 — Sichere Installation von Windows Server (B)
  1. Wenn vom Funktionsumfang her ausreichend, MUSS die Server-Core-Variante installiert werden. **◀ ZITIERT**
  2. Andernfalls MUSS begründet werden, warum die Server-Core-Variante nicht genügt.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die Wahl der minimalen Server-Core-Variante ist eine systemspezifische Umsetzung der allgemeinen Forderung aus KONF.2.4, nicht benötigte Systemfunktionen zur Reduzierung der Angriffsfläche zu deaktivieren bzw. nicht zu installieren.

### → SYS.1.2.3.A3 — Telemetrie- und Nutzungsdaten unter Windows Server (B)
  1. Um die Übertragung von Diagnose- und Nutzungsdaten an Microsoft stark zu reduzieren, MUSS das Telemetrie-Level 0 (Security) auf dem Windows Server konfiguriert werden. **◀ ZITIERT**
  2. Wenn diese Einstellung nicht wirksam umgesetzt wird, dann MUSS durch geeignete Maßnahmen, etwa auf Netzebene, sichergestellt werden, dass die Daten nicht an den Hersteller übertragen werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen und benennt in der Erläuterung explizit Telemetriedienste, womit die Reduzierung der Telemetriedatenübertragung (z. B. Telemetrie-Level 0) als allgemeine Anforderung abgedeckt ist.

### → SYS.1.2.3.A6 — Sicherheit beim Fernzugriff über RDP (S)
  1. Die Auswirkungen auf die Konfiguration der lokalen Firewall SOLLTEN bei der Planung des Fernzugriffs berücksichtigt werden.
  2. Die Gruppe der Berechtigten und IT-Systeme für den Remote-Desktopzugriff (RDP) SOLLTE durch die Zuweisung entsprechender Berechtigungen festgelegt werden.
  3. Es SOLLTEN Mechanismen des Betriebssystems berücksichtigt werden, um die übertragenen Anmeldeinformationen zu schützen (z. B. Remote Credential Guard oder RestrictedAdmin).
  4. In komplexen Infrastrukturen SOLLTE das RDP-Zielsystem nur durch ein dazwischengeschaltetes RDP-Gateway erreicht werden können.
  5. Für die Verwendung von RDP SOLLTE eine Prüfung und deren Umsetzung sicherstellen, dass die nachfolgend aufgeführten Komfortfunktionen im Einklang mit dem Schutzbedarf des Zielsystems stehen: die Verwendung der Zwischenablage, die Einbindung von Wechselmedien und Netzlaufwerken sowie die Nutzung der Dateiablagen, von weiteren Geräten und Ressourcen, wie z. B. Smartcard-Lesegeräten.
  6. Die eingesetzten kryptografischen Protokolle und Algorithmen SOLLTEN den internen Vorgaben der Institution entsprechen.
  7. Sofern der Einsatz von Remote-Desktopzugriffen nicht vorgesehen ist, SOLLTEN diese vollständig deaktiviert werden. **◀ ZITIERT**
- **Satz 7** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 7) KONF.2.4 fordert allgemein die Deaktivierung nicht benötigter Systemfunktionen und -dienste, was die vollständige Deaktivierung nicht vorgesehener Remote-Desktopzugriffe direkt umfasst.

### → SYS.1.2.3.A7 — Verwendung der Windows PowerShell (H)
  1. Die PowerShell-Ausführung SOLLTE zentral protokolliert werden.
  2. Die erzeugten Protokolle SOLLTEN geeignet überwacht werden.
  3. Die Ausführung von PowerShell-Skripten SOLLTE mit dem Befehl Set-ExecutionPolicy AllSigned eingeschränkt werden, um zu verhindern, dass unsignierte Skripte (versehentlich) ausgeführt werden.
  4. Ältere Windows PowerShell-Versionen SOLLTEN deaktiviert werden. **◀ ZITIERT**
  5. Der Einsatz des PowerShell Constrained Language Mode SOLLTE geprüft werden.
  6. Zur Einschränkung der Windows PowerShell SOLLTE bei Windows Server mithilfe von Just Enough Administration (JEA) eine rollenbasierte Administration implementiert werden.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) KONF.2.4 fordert allgemein die Deaktivierung nicht benötigter bzw. veralteter Systemfunktionen zur Reduktion der Angriffsfläche, was das Abschalten älterer PowerShell-Versionen inhaltlich abdeckt.

### → SYS.1.3.A8 — Verschlüsselter Zugriff über Secure Shell (S)
  1. Um eine verschlüsselte und authentisierte, interaktive Verbindung zwischen zwei IT-Systemen aufzubauen, SOLLTE ausschließlich Secure Shell (SSH) verwendet werden.
  2. Alle anderen Protokolle, deren Funktionalität durch Secure Shell abgedeckt wird, SOLLTEN vollständig abgeschaltet werden. **◀ ZITIERT**
  3. Für die Authentifizierung SOLLTEN vorrangig Zertifikate anstatt eines Passworts verwendet werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen und Netzprotokolle, was das Abschalten durch SSH ersetzter, überflüssiger Protokolle als allgemeinere Forderung abdeckt.

### → SYS.1.6.A16 — Administrativer Fernzugriff auf Container (S)
  1. Administrative Zugriffe von einem Container auf den Container-Host und umgekehrt SOLLTEN prinzipiell wie administrative Fernzugriffe betrachtet werden.
  2. Aus einem Container SOLLTEN KEINE administrativen Fernzugriffe auf den Container-Host erfolgen.
  3. Applikations-Container SOLLTEN keine Fernwartungszugänge enthalten. **◀ ZITIERT**
  4. Administrative Zugriffe auf Applikations-Container SOLLTEN immer über die Container-Runtime erfolgen.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme fordert allgemein die Deaktivierung nicht benötigter Systemfunktionen und Dienste, was das Weglassen bzw. Deaktivieren von Fernwartungszugängen in Applikations-Containern als Spezialfall abdeckt.

### → SYS.1.7.A23 — Absicherung von z/VM (S)
  1. Falls z/VM eingesetzt wird, SOLLTE das Produkt in das Patch-Management integriert werden.
  2. Alle voreingestellten Passwörter SOLLTEN geändert werden.
  3. Die Rolle des z/VM-Systemadministrierenden SOLLTE nur an Personen vergeben werden, die diese Berechtigungen benötigen.
  4. Die Sicherheitsadministration von z/VM SOLLTE über RACF für z/VM erfolgen.
  5. Passwörter von realen Usern und Guest-Usern SOLLTEN mittels RACF für z/VM verschlüsselt werden.
  6. Die sicherheitskritischen Systemkommandos von z/VM SOLLTEN über RACF geschützt werden.
  7. Unter z/VM definierte virtuelle Maschinen SOLLTEN nur die für die jeweiligen Aufgaben notwendigen Ressourcen erhalten und strikt voneinander getrennt sein.
  8. Unter z/VM SOLLTEN nur die benötigten Dienste gestartet werden. **◀ ZITIERT**
  9. Wenn Überprüfungen durchgeführt werden, SOLLTEN die Journaling-Funktion von z/VM und die Audit-Funktionen von RACF eingesetzt werden.
- **Satz 8** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 8) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen und Systemdienste, was die Beschränkung auf benötigte Dienste unter z/VM als systemspezifischen Anwendungsfall vollständig abdeckt.

### → SYS.1.7.A30 — Absicherung der z/OS-Trace-Funktionen (S)
  1. Die Trace-Funktionen von z/OS wie GTF (Generalized Trace Facility), NetView oder ACF/TAP (Advanced Communication Function/Trace Analysis Program) und die entsprechenden Dateien SOLLTEN so geschützt werden, dass nur die zuständigen und autorisierten Mitarbeitenden darauf Zugriff haben.
  2. Die Trace-Funktion von NetView SOLLTE deaktiviert sein und nur im Bedarfsfall aktiviert werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) KONF.2.4 fordert allgemein die Deaktivierung nicht benötigter Systemfunktionen, was das standardmäßige Deaktivieren der NetView-Trace-Funktion und Aktivieren nur bei Bedarf als Spezialfall abdeckt.

### → SYS.1.7.A5 — Einsatz und Sicherung systemnaher z/OS-Terminals (B)
  1. Systemnahe z/OS-Terminals MÜSSEN physisch gegen unbefugten Zutritt und logisch gegen unbefugten Zugang geschützt werden.
  2. Insbesondere die Support-Elemente sowie die HMC-, MCS-, SMCS-, Extended MCS- und Monitor-Konsolen MÜSSEN dabei berücksichtigt werden.
  3. Voreingestellte Passwörter MÜSSEN geändert werden.
  4. Zugänge über Webserver und andere Fernzugänge MÜSSEN durch Verschlüsselung geschützt werden.
  5. Nicht benötigte Webserver und Fernzugänge MÜSSEN deaktiviert werden, wenn sie nicht benötigt werden. **◀ ZITIERT**
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) Die G++-Maßnahme KONF.2.4 fordert allgemein die Deaktivierung nicht benötigter Systemfunktionen und -dienste, was das Deaktivieren nicht benötigter Webserver und Fernzugänge inhaltlich abdeckt.

### → SYS.1.8.A2 — Sichere Grundkonfiguration von Speicherlösungen (B)
  1. Bevor eine Speicherlösung produktiv eingesetzt wird, MUSS sichergestellt sein, dass alle eingesetzten Softwarekomponenten und die Firmware aktuell sind.
  2. Danach MUSS eine sichere Grundkonfiguration hergestellt werden.
  3. Nicht genutzte Schnittstellen des Speichersystems MÜSSEN deaktiviert werden. **◀ ZITIERT**
  4. Die Dateien zur Default-Konfiguration, zur vorgenommenen Grundkonfiguration und zur aktuellen Konfiguration SOLLTEN redundant und geschützt aufbewahrt werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) KONF.2.4 fordert allgemein die Deaktivierung nicht benötigter Systemfunktionen und Schnittstellen auf IT-Systemen, was die Deaktivierung ungenutzter Schnittstellen von Speichersystemen inhaltlich abdeckt.

### → SYS.2.1.A16 — Deaktivierung und Deinstallation nicht benötigter Komponenten und Kennungen (S)
  1. Nach der Installation SOLLTE überprüft werden, welche Komponenten der Firmware sowie des Betriebssystems und welche Anwendungen und weiteren Tools auf den Clients installiert und aktiviert sind.
  2. Nicht benötigte Module, Programme, Dienste, Aufgaben und Firmwarefunktionen (wie Fernwartung) SOLLTEN deaktiviert oder ganz deinstalliert werden. **◀ ZITIERT**
  3. Nicht benötigte Laufzeitumgebungen, Interpretersprachen und Compiler SOLLTEN deinstalliert werden.
  4. Nicht benötigte Kennungen SOLLTEN deaktiviert oder gelöscht werden.
  5. Nicht benötigte Schnittstellen und Hardware des IT-Systems (wie z. B. Webcams) SOLLTEN deaktiviert werden.
  6. Es SOLLTE verhindert werden, dass diese Komponenten wieder reaktiviert werden können.
  7. Die getroffenen Entscheidungen SOLLTEN nachvollziehbar dokumentiert werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen und deckt damit die Deaktivierung von nicht benötigten Modulen, Diensten und Firmwarefunktionen aus Satz 2 inhaltlich ab.

### → SYS.2.1.A21 — Verhinderung der unautorisierten Nutzung von Rechnermikrofonen und Kameras (S)
  1. Der Zugriff auf Mikrofon und Kamera eines Clients SOLLTE nur durch Benutzende selbst möglich sein, solange sie lokal am IT-System arbeiten.
  2. Wenn vorhandene Mikrofone oder Kameras nicht genutzt und deren Missbrauch verhindert werden soll, SOLLTEN diese, wenn möglich, ausgeschaltet, abgedeckt (nur Kamera), deaktiviert oder physisch vom Gerät getrennt werden. **◀ ZITIERT**
  3. Es SOLLTE geregelt werden, wie Kameras und Mikrofone in Clients genutzt und wie die Rechte vergeben werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) KONF.2.4 fordert als übergeordnete Maßnahme die Deaktivierung nicht benötigter Systemfunktionen und Schnittstellen, was das Deaktivieren bzw. Ausschalten nicht genutzter Mikrofone und Kameras inhaltlich abdeckt.

### → SYS.2.1.A23 — Bevorzugung von Client-Server-Diensten (S)
  1. Wenn möglich, SOLLTEN zum Informationsaustausch dedizierte Serverdienste genutzt und direkte Verbindungen zwischen Clients vermieden werden.
  2. Falls dies nicht möglich ist, SOLLTE festgelegt werden, welche Client-zu-Client-Dienste (oft auch als „Peer-to-Peer“ bezeichnet) genutzt und welche Informationen darüber ausgetauscht werden dürfen.
  3. Falls erforderlich, SOLLTEN Benutzende für die Nutzung solcher Dienste geschult werden.
  4. Direkte Verbindungen zwischen Clients SOLLTEN sich nur auf das LAN beschränken.
  5. Auto-Discovery-Protokolle SOLLTEN auf das notwendige Maß beschränkt werden. **◀ ZITIERT**
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) Die Deaktivierung bzw. Beschränkung von Auto-Discovery-Protokollen auf das notwendige Maß wird als allgemeine Deaktivierung nicht benötigter Systemfunktionen und Netzprotokolle durch KONF.2.4 abgedeckt.

### → SYS.2.1.A36 — Selbstverwalteter Einsatz von SecureBoot und TPM (H)
  1. Auf UEFI-kompatiblen Systemen SOLLTEN Bootloader, Kernel sowie alle benötigten Firmware-Komponenten durch selbstkontrolliertes Schlüsselmaterial signiert werden.
  2. Nicht benötigtes Schlüsselmaterial SOLLTE entfernt werden.
  3. Sofern das Trusted Platform Module (TPM) nicht benötigt wird, SOLLTE es deaktiviert werden. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die allgemeine Deaktivierung nicht benötigter System- und Firmwarefunktionen gemäß KONF.2.4 schließt die Deaktivierung eines nicht benötigten Trusted Platform Modules (TPM) inhaltlich ein.

### → SYS.2.1.A8 — Absicherung des Bootvorgangs (B)
  1. Der Startvorgang des IT-Systems („Booten“) MUSS gegen Manipulation abgesichert werden.
  2. Es MUSS festgelegt werden, von welchen Medien gebootet werden darf.
  3. Es SOLLTE entschieden werden, ob und wie der Bootvorgang kryptografisch geschützt werden soll.
  4. Es MUSS sichergestellt werden, dass nur Administrierende die Clients von einem anderen als den voreingestellten Laufwerken oder externen Speichermedien booten können.
  5. NUR Administrierende DÜRFEN von wechselbaren oder externen Speichermedien booten können.
  6. Die Konfigurationseinstellungen des Bootvorgangs DÜRFEN NUR durch Administrierende verändert werden können.
  7. Alle nicht benötigten Funktionen in der Firmware des Client-Systems MÜSSEN deaktiviert werden. **◀ ZITIERT**
- **Satz 7** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 7) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen, was ausweislich der Erläuterung explizit auch nicht benötigte Firmwarefunktionen umfasst.

### → SYS.2.2.3.A13 — Einsatz der SmartScreen-Funktion (S)
  1. Die SmartScreen-Funktion, die aus dem Internet heruntergeladene Dateien und Webinhalte auf mögliche Schadsoftware untersucht und dazu unter Umständen personenbezogene Daten an Microsoft überträgt, SOLLTE deaktiviert werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die Deaktivierung der SmartScreen-Funktion stellt einen konkreten Anwendungsfall der allgemeinen Deaktivierung nicht benötigter System- bzw. Telemetriefunktionen gemäß KONF.2.4 dar.

### → SYS.2.2.3.A14 — Einsatz des Sprachassistenten Cortana (S) [Benutzende]
  1. Cortana SOLLTE deaktiviert werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen und -dienste, was das Abschalten des Sprachassistenten Cortana als konkreten Spezialfall sachgerecht abdeckt.

### → SYS.2.2.3.A18 — Einsatz der Windows-Remoteunterstützung (S)
  1. Die Auswirkungen auf die Konfiguration der lokalen Firewall SOLLTEN bei der Planung der Windows-Remoteunterstützung (hiermit ist nicht RDP gemeint) berücksichtigt werden.
  2. Eine Remoteunterstützung SOLLTE nur nach einer expliziten Einladung erfolgen.
  3. Bei der Speicherung einer Einladung in einer Datei SOLLTE diese ein Kennwort besitzen.
  4. Dem Aufbau einer Sitzung SOLLTE immer explizit zugestimmt werden.
  5. Die maximale Gültigkeit der Einladung für eine Unterstützung aus der Ferne SOLLTE in der Dauer angemessen sein.
  6. Sofern die Windows-Remoteunterstützung nicht verwendet wird, SOLLTE sie vollständig deaktiviert werden. **◀ ZITIERT**
- **Satz 6** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 6) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen und -dienste, was die Deaktivierung der nicht verwendeten Windows-Remoteunterstützung als Spezialfall direkt abdeckt.

### → SYS.2.2.3.A19 — Sicherheit beim Fernzugriff über RDP (S) [Benutzende]
  1. Die Auswirkungen auf die Konfiguration der lokalen Firewall SOLLTEN bei der Planung des Fernzugriffs berücksichtigt werden.
  2. Die Gruppe der berechtigten Benutzenden für den Remote-Desktopzugriff (RDP) SOLLTE durch die Zuweisung entsprechender Berechtigungen festgelegt werden.
  3. In komplexen Infrastrukturen SOLLTE das RDP-Zielsystem nur durch ein dazwischengeschaltetes RDP-Gateway erreicht werden können.
  4. Für die Verwendung von RDP SOLLTE eine Prüfung und deren Umsetzung sicherstellen, dass die nachfolgend aufgeführten Komfortfunktionen im Einklang mit dem Schutzbedarf des Zielsystems stehen: die Verwendung der Zwischenablage, die Einbindung von Druckern, die Einbindung von Wechselmedien und Netzlaufwerken sowie die Nutzung der Dateiablagen und von Smartcard-Anschlüssen. **◀ ZITIERT**
  5. Sofern der Einsatz von Remote-Desktopzugriffen nicht vorgesehen ist, SOLLTEN diese vollständig deaktiviert werden. **◀ ZITIERT**
  6. Die eingesetzten kryptografischen Protokolle und Algorithmen SOLLTEN sicher sein und den internen Vorgaben der Institution entsprechen.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) KONF.2.4 deckt die bedarfsgerechte Deaktivierung bzw. Einschränkung nicht benötigter System- und Komfortfunktionen wie RDP-Umleitungen als allgemeingültige Anforderung ab.
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) KONF.2.4 fordert allgemein die Deaktivierung nicht benötigter Systemfunktionen und -dienste, was die vollständige Deaktivierung nicht vorgesehener Remote-Desktopzugriffe inhaltlich abdeckt.

### → SYS.2.2.3.A4 — Telemetrie und Datenschutzeinstellungen unter Windows (B)
  1. Um die Übertragung von Diagnose- und Nutzungsdaten an Microsoft stark zu reduzieren, MUSS das Telemetrie-Level 0 (Security) in der Enterprise-Edition von Windows konfiguriert werden. **◀ ZITIERT**
  2. Wenn diese Einstellung nicht wirksam umgesetzt wird oder bei anderen Windows-Edition umgesetzt werden kann, dann MUSS durch geeignete Maßnahmen, etwa auf Netzebene, sichergestellt werden, dass die Daten nicht an den Hersteller übertragen werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen einschließlich Telemetriediensten und deckt damit die Windows-spezifische Reduzierung der Telemetriedatenübertragung als allgemeinere Maßnahme ab.

### → SYS.2.2.3.A9 — Sichere zentrale Authentisierung in Windows-Netzen (S)
  1. Für die zentrale Authentisierung SOLLTE ausschließlich Kerberos eingesetzt werden.
  2. Eine Gruppenrichtlinie SOLLTE die Verwendung älterer Protokolle verhindern. **◀ ZITIERT**
  3. Ist dies nicht möglich, MUSS alternativ NTLMv2 eingesetzt werden.
  4. Die Authentisierung mittels LAN-Manager und NTLMv1 DARF NICHT innerhalb der Institution und in einer produktiven Betriebsumgebung erlaubt werden. **◀ ZITIERT**
  5. Die eingesetzten kryptografischen Mechanismen SOLLTEN entsprechend dem ermittelten Schutzbedarf und basierend auf den internen Richtlinien konfiguriert und dokumentiert werden.
  6. Abweichende Einstellungen SOLLTEN begründet und mit dem Sicherheitsmanagement abgestimmt sein.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) KONF.2.4 verlangt allgemein die Deaktivierung nicht benötigter bzw. veralteter Systemfunktionen und Protokolle, was die Verhinderung älterer Authentisierungsprotokolle inhaltlich abdeckt.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die Maßnahme KONF.2.4 fordert allgemein die Deaktivierung nicht benötigter bzw. unsicherer Systemfunktionen und Protokolle, was das Verbot und die Deaktivierung von veralteten Authentifizierungsverfahren wie LAN-Manager und NTLMv1 direkt abdeckt.

### → SYS.2.3.A20 — Abschaltung kritischer SysRq-Funktionen (H)
  1. Es SOLLTE festgelegt werden, welche SysRq-Funktionen von den Benutzenden ausgeführt werden dürfen.
  2. Generell SOLLTEN keine kritischen SysRq-Funktionen von den Benutzenden ausgelöst werden können. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die Deaktivierung bzw. Unterbindung kritischer SysRq-Funktionen ist ein konkreter Anwendungsfall der allgemeinen Pflicht zur Deaktivierung nicht benötigter bzw. risikobehafteter Systemfunktionen nach KONF.2.4.

### → SYS.2.4.A3 — Verwendung geeigneter Konten (B) [Benutzende]
  1. Das bei der Erstkonfiguration von macOS angelegte Konto hat Administrationsrechte und DARF NUR zu administrativen Zwecken verwendet werden.
  2. Für die normale Verwendung des Macs MUSS ein Konto mit Standard-Berechtigungen angelegt werden.
  3. Sollte der Mac von mehreren Benutzenden verwendet werden, MUSS für jeden Benutzenden ein eigenes Konto angelegt werden.
  4. Das Gast-Konto MUSS deaktiviert werden. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die Deaktivierung des Gast-Kontos ist ein konkreter Spezialfall der allgemeinen Forderung in KONF.2.4, nicht benötigte Systemfunktionen und Identitäten zu deaktivieren.

### → SYS.2.4.A5 — Deaktivierung sicherheitskritischer Funktionen von macOS (S)
  1. Die in macOS integrierten Ortungsdienste SOLLTEN deaktiviert werden. **◀ ZITIERT**
  2. Heruntergeladene Daten SOLLTEN NICHT automatisch geöffnet werden.
  3. Inhalte von optischen und anderen Medien SOLLTEN NICHT automatisch ausgeführt werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) KONF.2.4 fordert allgemein die Deaktivierung nicht benoetigter System- und Telemetriefunktionen, was das Deaktivieren von Ortungsdiensten als spezifische Systemfunktion abdeckt.

### → SYS.3.2.1.A16 — Deaktivierung nicht benutzter Kommunikationsschnittstellen (S) [Benutzende]
  1. Kommunikationsschnittstellen SOLLTEN nur bei Bedarf und nur in geeigneten Umgebungen aktiviert werden. **◀ ZITIERT**
  2. Wird ein MDM verwendet, SOLLTEN die Schnittstellen zentral über das MDM verwaltet werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) KONF.2.4 fordert allgemein die Deaktivierung nicht benötigter Systemfunktionen und Schnittstellen, was die bedarfsweise Aktivierung von Kommunikationsschnittstellen materiell abdeckt.

### → SYS.3.2.1.A19 — Verwendung von Sprachassistenten (S)
  1. Sprachassistenten SOLLTEN nur eingesetzt werden, wenn sie zwingend notwendig sind. **◀ ZITIERT**
  2. Andernfalls SOLLTEN sie deaktiviert werden. **◀ ZITIERT**
  3. Generell SOLLTE ein Sprachassistent nicht genutzt werden können, wenn das Gerät gesperrt ist.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) KONF.2.4 fordert allgemein die Deaktivierung nicht benötigter Systemfunktionen und deckt damit die Beschränkung des Einsatzes von Sprachassistenten auf das zwingend notwendige Maß ab.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) KONF.2.4 fordert allgemein die Deaktivierung nicht benötigter Systemfunktionen und -dienste, was die Deaktivierung nicht zwingend erforderlicher Sprachassistenten als konkreten Anwendungsfall umfasst.

### → SYS.3.2.1.A3 — Sichere Grundkonfiguration für mobile Geräte (B)
  1. Alle mobilen Endgeräte MÜSSEN so konfiguriert sein, dass sie das erforderliche Schutzniveau angemessen erfüllen.
  2. Dafür MUSS eine passende Grundkonfiguration der Sicherheitsmechanismen und -einstellungen zusammengestellt und dokumentiert werden.
  3. Nicht benötigte Funktionen SOLLTEN deaktiviert werden. **◀ ZITIERT**
  4. Die Freischaltung von Kommunikationsschnittstellen MUSS geregelt und auf das dienstlich notwendige Maß reduziert werden.
  5. Nicht benutzte Schnittstellen SOLLTEN deaktiviert werden. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen auf IT-Systemen und deckt damit die Forderung von Satz 3 direkt ab.
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen und deckt damit als allgemeinere Maßnahme auch das Deaktivieren nicht benutzter Schnittstellen ab, was in den Erläuterungen zudem explizit erwähnt wird.

### → SYS.3.2.1.A34 — Konfiguration des verwendeten DNS-Servers (S)
  1. Standard-Gateway-Einträge, wie beispielsweise DNS-Server der herstellenden oder entwickelnden Institutionen, SOLLTEN durch die des Providers oder durch eigene ersetzt werden.
  2. Sollte der Provider sogenanntes DNS-over-HTTPS (DoH) anbieten, SOLLTE dieses verwendet werden.
  3. Bietet er es noch nicht an, SOLLTE es deaktiviert werden. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen und Netzwerkprotokolle, was das Deaktivieren von DoH bei fehlender Unterstützung durch den Provider als konkreten Spezialfall abdeckt.

### → SYS.3.2.3.A13 — Verwendung der Konfigurationsoption „Einschränkungen unter iOS“ (S)
  1. Alle nicht benötigten oder erlaubten Funktionen bzw. Dienste von iOS SOLLTEN deaktiviert werden. **◀ ZITIERT**
  2. Basierend auf dem Einsatzzweck und dem zugrundeliegenden Schutzbedarf SOLLTE geprüft werden, welche der Funktionen „Sperrbildschirm“, „Unified Communication“, „Siri“, „Hintergrundbild“, „Verbindung mit Host-Systemen“ und „Diagnose- und Nutzungsdaten“ einzusetzen sind. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) KONF.2.4 deckt die allgemeine Deaktivierung nicht benötigter Systemfunktionen und -dienste ab, was die Deaktivierung nicht benötigter iOS-Funktionen und -Dienste direkt umfasst.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen und deckt damit die Prüfung und bedarfsgerechte Einschränkung spezifischer Funktionen wie Sperrbildschirm oder Telemetriedienste als allgemeine Anforderung ab.

### → SYS.3.2.4.A2 — Deaktivieren des Entwicklermodus (S)
  1. In allen Android-basierten Geräten SOLLTE der Entwicklermodus deaktiviert sein. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die Deaktivierung des Entwicklermodus auf Android-Geräten stellt die systemspezifische Umsetzung der allgemeinen Forderung aus KONF.2.4 dar, nicht benötigte Systemfunktionen zu deaktivieren.

### → SYS.3.3.A13 — Schutz vor der Erstellung von Bewegungsprofilen bei der Nutzung von Mobilfunk (H) [Benutzende]
  1. Es SOLLTE geklärt werden, ob sich die Erstellung von Bewegungsprofilen durch Dritte negativ auswirken kann oder als Problem angesehen wird.
  2. Um eine Ortung über GPS zu verhindern, SOLLTE diese Funktion abgeschaltet werden. **◀ ZITIERT**
  3. Falls eine Ortung über das Mobilfunknetz verhindert werden soll, SOLLTE das Mobiltelefon abgeschaltet und der Akku entfernt werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Das Deaktivieren der GPS-Funktion zur Vermeidung von Ortungen stellt einen konkreten Anwendungsfall der allgemeinen Deaktivierung nicht benötigter bzw. sicherheitsrelevanter Systemfunktionen nach KONF.2.4 dar.

### → SYS.3.3.A8 — Nutzung drahtloser Schnittstellen von Mobiltelefonen (S) [Benutzende]
  1. Drahtlose Schnittstellen von Mobiltelefonen wie IrDA, WLAN oder Bluetooth SOLLTEN deaktiviert werden, solange sie nicht benötigt werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen und deckt damit die Deaktivierung ungenutzter drahtloser Schnittstellen allgemeingültig ab.

### → SYS.4.1.A17 — Schutz von Nutz- und Metadaten (S)
  1. Nutz- und Metadaten wie Druckaufträge und Scandateien SOLLTEN nur so kurz wie möglich auf den Geräten gespeichert werden.
  2. Die Daten SOLLTEN nach einer vordefinierten Zeit automatisch gelöscht werden.
  3. Dateiserver in den Geräten und Funktionen wie „Scan in den Gerätespeicher" SOLLTEN vom IT-Betrieb abgeschaltet werden. **◀ ZITIERT**
  4. Die dafür benötigten Protokolle und Funktionen SOLLTEN, soweit möglich, gesperrt werden. **◀ ZITIERT**
  5. Generell SOLLTE vom IT-Betrieb sichergestellt werden, dass alle Metadaten nicht für Unberechtigte sichtbar sind.
  6. Es SOLLTE von der Institution geregelt werden, wie mit Metadaten versehene Ausdrucke an Dritte weitergegeben werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen und deckt damit das Abschalten interner Dateiserver und lokaler Speicherfunktionen auf IT-Systemen als allgemeinere Regelung inhaltlich ab.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) KONF.2.4 deckt das Sperren bzw. Deaktivieren nicht benötigter Protokolle und Funktionen als allgemeine Härtungsmaßnahme für IT-Systeme inhaltlich ab.

### → SYS.4.1.A18 — Konfiguration von Druckern, Kopierern und Multifunktionsgeräten (S)
  1. Alle Drucker und Multifunktionsgeräte SOLLTEN nur vom IT-Betrieb konfiguriert werden können.
  2. Nicht benötigte Gerätefunktionen SOLLTEN abgeschaltet werden. **◀ ZITIERT**
  3. Insbesondere SOLLTEN alle nicht benötigten Daten- und Netzschnittstellen von Druckern, Kopierern und Multifunktionsgeräten deaktiviert werden.
  4. Die Geräte SOLLTEN ausschließlich über verschlüsselte Protokolle wie HTTPS und SNMPv3 verwaltet werden.
  5. Sämtliche Protokolle, mit denen unverschlüsselt auf Drucker und Multifunktionsgeräte zugegriffen werden kann, SOLLTEN vom IT-Betrieb durch verschlüsselte ersetzt oder abgeschaltet werden.
  6. Das SOLLTE insbesondere für Protokolle umgesetzt werden, mit denen sich die Gerätekonfiguration verändern lässt, z. B. SNMP, Telnet und PJL.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen auf IT-Systemen und deckt damit das Abschalten nicht benötigter Gerätefunktionen bei Druckern und Multifunktionsgeräten direkt ab.

### → SYS.4.3.A2 — Deaktivieren nicht benutzter Schnittstellen und Dienste bei eingebetteten Systemen (B)
  1. Es MUSS sichergestellt werden, dass nur auf benötigte Schnittstellen zugegriffen werden kann.
  2. Alle anderen Schnittstellen MÜSSEN deaktiviert werden. **◀ ZITIERT**
  3. Zudem DÜRFEN NUR benötigte Dienste aktiviert sein. **◀ ZITIERT**
  4. Der Zugang zu Anwendungsschnittstellen MUSS durch sichere Authentisierung geschützt sein.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen und schließt dabei laut Erläuterung explizit nicht benötigte Schnittstellen mit ein.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 3) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen und deckt damit die Beschränkung auf ausschließlich benötigte aktive Dienste direkt ab.

### → SYS.4.3.A6 — Verhindern von Debugging-Möglichkeiten bei eingebetteten Systemen (S) [Entwickelnde]
  1. Eventuelle Debugging-Möglichkeiten SOLLTEN möglichst vollständig aus eingebetteten Systemen entfernt werden. **◀ ZITIERT**
  2. Wird On-Chip-Debugging genutzt, MUSS sichergestellt werden, dass Debugging-Funktionen nicht unberechtigt genutzt oder aktiviert werden können.
  3. Weiterhin SOLLTE sichergestellt werden, dass keine Eingabeschnittstellen für Testsignale und Messpunkte zum Anschluss von Analysatoren aktiviert und für Unberechtigte nutzbar sind.
  4. Zudem SOLLTEN alle Hardware-Debugging-Schnittstellen deaktiviert sein. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die allgemeine Anforderung zur Deaktivierung nicht benötigter System- und Firmwarefunktionen in KONF.2.4 deckt das Entfernen bzw. Deaktivieren nicht benötigter Debugging-Möglichkeiten in eingebetteten Systemen inhaltlich ab.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) KONF.2.4 fordert als allgemeinere Maßnahme die Deaktivierung nicht benötigter Systemfunktionen und Schnittstellen auf System- und Firmware-Ebene, was die Deaktivierung von Hardware-Debugging-Schnittstellen umfasst.

### → SYS.4.4.A13 — Deaktivierung und Deinstallation nicht benötigter Komponenten (S)
  1. Nach der Installation SOLLTE überprüft werden, welche Protokolle, Anwendungen und weiteren Tools auf den IoT-Geräten installiert und aktiviert sind.
  2. Nicht benötigte Protokolle, Dienste, Anmeldekennungen und Schnittstellen SOLLTEN deaktiviert oder ganz deinstalliert werden. **◀ ZITIERT**
  3. Die Verwendung von nicht benötigten Funkschnittstellen SOLLTE unterbunden werden. **◀ ZITIERT**
  4. Wenn dies nicht am Gerät selber möglich ist, SOLLTEN nicht benötigte Dienste über die Firewall eingeschränkt werden.
  5. Die getroffenen Entscheidungen SOLLTEN so dokumentiert werden, dass nachvollzogen werden kann, welche Konfiguration für die IoT-Geräte gewählt wurden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) KONF.2.4 fordert allgemein die Deaktivierung nicht benötigter Systemfunktionen und deckt damit das Deaktivieren/Deinstallieren nicht benötigter Protokolle, Dienste, Schnittstellen und Kennungen direkt ab.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen und deckt damit das Unterbinden bzw. Deaktivieren nicht benötigter (Funk-)Schnittstellen als allgemeinere Forderung ab.

### → SYS.4.4.A5 — Einschränkung des Netzzugriffs (B)
  1. Der Netzzugriff von IoT-Geräten MUSS auf das erforderliche Minimum eingeschränkt werden.
  2. Dies SOLLTE regelmäßig kontrolliert werden.
  3. Dazu SOLLTEN folgende Punkte beachtet werden: Bei Verkehrskontrollen an Netzübergängen, z. B. durch Regelwerke auf Firewalls und Access Control Lists (ACLs) auf Routern, DÜRFEN NUR zuvor definierte ein- und ausgehende Verbindungen erlaubt werden.
  4. Die Routings auf IoT-Geräten und Sensoren, insbesondere die Unterdrückung von Default-Routen, SOLLTE restriktiv konfiguriert werden.
  5. Die IoT-Geräte und Sensoren SOLLTEN in einem eigenen Netzsegment betrieben werden, das ausschließlich mit dem Netzsegment für das Management kommunizieren darf.
  6. Virtual Private Networks (VPNs) zwischen den Netzen mit IoT-Geräten und Sensor-Netzen und den Management-Netzen SOLLTEN restriktiv konfiguriert werden.
  7. Die UPnP-Funktion MUSS an allen Routern deaktiviert sein. **◀ ZITIERT**
- **Satz 7** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 7) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen und Netzwerkprotokolle, was die Deaktivierung der UPnP-Funktion auf Routern als konkreten Anwendungsfall umfasst.

### → INF.13.A11 — Angemessene Härtung von Systemen im TGM (S)
  1. Alle Systeme des TGM sowie die Systeme, die durch das TGM betrieben werden, SOLLTEN angemessen gehärtet werden. **◀ ZITIERT**
  2. Die Härtungsmaßnahmen SOLLTEN dokumentiert, regelmäßig und zusätzlich bei Bedarf überprüft und, falls erforderlich, angepasst werden.
  3. Für alle Systeme des TGM sowie die Systeme, die durch das TGM betrieben werden, SOLLTE bei der Beschaffung sichergestellt werden, dass diese angemessen gehärtet werden können und insbesondere sicherheitsrelevante Updates für die geplante Nutzungsdauer bereitgestellt werden.
  4. Systeme, für die keine sicherheitsrelevanten Updates verfügbar sind, SOLLTEN nach Bekanntwerden von Schwachstellen nicht mehr genutzt werden.
  5. Wenn dies nicht möglich ist, SOLLTEN die betroffenen Systeme mit den Mitteln der Netzsegmentierung separiert und die Kommunikation kontrolliert und reglementiert werden.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die Deaktivierung nicht benötigter Systemfunktionen gemäß KONF.2.4 stellt eine zentrale technische Härtungsmaßnahme zur Reduktion der Angriffsfläche dar und deckt damit die allgemeine Forderung nach angemessener Härtung der Systeme inhaltlich ab.

### → SYS.1.5.A22 — Härtung des Virtualisierungsservers (H)
  1. Der Virtualisierungsserver SOLLTE gehärtet werden. **◀ ZITIERT**
  2. Um virtuelle IT-Systeme voreinander und gegenüber dem Virtualisierungsserver zusätzlich zu isolieren und zu kapseln, SOLLTEN Mandatory Access Controls (MACs) eingesetzt werden.
  3. Ebenso SOLLTE das IT-System, auf dem die Management-Software installiert ist, gehärtet werden.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die Deaktivierung nicht benötigter Systemfunktionen gemäß KONF.2.4 stellt eine zentrale Härtungsmaßnahme für IT-Systeme und somit auch für Virtualisierungsserver dar.

### → CON.7.A17 — Verwendung vorkonfigurierter Reise-Hardware (H) [IT-Betrieb]
  1. Damit schützenswerte Informationen der Institution auf Auslandsreisen nicht von Dritten abgegriffen werden können, SOLLTE der IT-Betrieb den Mitarbeitenden vorkonfigurierte Reise-Hardware zur Verfügung stellen.
  2. Diese Reise-Hardware SOLLTE auf Basis des Minimalprinzips nur die Funktionen und Informationen bereitstellen, die zur Durchführung der Geschäftstätigkeit unbedingt erforderlich sind. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die Maßnahme KONF.2.4 deckt die allgemeine Deaktivierung nicht benötigter Systemfunktionen nach dem Minimalprinzip für IT-Systeme ab, was die spezifische Reduktion von Systemfunktionen auf Reise-Hardware umfasst.

### → INF.10.A7 — Sichere Konfiguration von Schulungs- und Präsentationsrechnern (S) [IT-Betrieb]
  1. Dedizierte Schulungs- und Präsentationsrechner SOLLTEN mit einer Minimalkonfiguration versehen werden. **◀ ZITIERT**
  2. Es SOLLTE festgelegt sein, welche Anwendungen auf Schulungs- und Präsentationsrechnern in der jeweiligen Veranstaltung genutzt werden können.
  3. Die Schulungs- und Präsentationsrechner SOLLTEN nur an ein separates, vom LAN der Institution getrenntes Datennetz angeschlossen werden.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die Forderung nach einer Minimalkonfiguration wird durch die allgemeinere Vorgabe von KONF.2.4, alle nicht benötigten Systemfunktionen auf IT-Systemen zu deaktivieren, inhaltlich abgedeckt.

### → SYS.2.6.A2 — Sichere Installation und Konfiguration der VDI-Komponenten (B)
  1. Wenn die VDI-Komponenten installiert und konfiguriert werden, MUSS mindestens berücksichtigt werden, wie: auf betrieblich und technisch notwendige Funktionen beschränkt wird, die Kommunikation zwischen VDI-Komponenten abgesichert wird sowie virtuelle Clients sicher den Benutzenden oder Gruppen hiervon zugewiesen werden. **◀ ZITIERT**
  2. Empfehlungen von dem herstellenden Unternehmen der VDI-Lösung für die sichere Konfiguration MÜSSEN berücksichtigt werden.
  3. Die Konfigurationen der VDI-Komponenten MÜSSEN geeignet dokumentiert werden.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) KONF.2.4 fordert die Deaktivierung nicht benötigter Systemfunktionen und deckt damit die allgemeinere Fassung der im Satz verlangten Beschränkung auf betrieblich und technisch notwendige Funktionen bei der Konfiguration ab.

### → SYS.3.2.2.A12 — Absicherung der MDM-Betriebsumgebung (S)
  1. Das MDM selbst SOLLTE durch technische Maßnahmen abgesichert werden, um dem Schutzbedarf der hinterlegten oder verarbeiteten Informationen zu genügen.
  2. Das zugrundeliegende Betriebssystem SOLLTE gehärtet werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die Deaktivierung nicht benötigter Systemfunktionen stellt eine wesentliche Kernmaßnahme zur Härtung des zugrundeliegenden Betriebssystems dar.


## KONF.6.8 — Berechtigungen des Webserver-Prozesses  [4 Paare]

**Statement (normativ):** Konfiguration für Webserver SOLLTE die Berechtigungen des Webserver-Prozesses einschränken.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Wird der laufende Prozess über das Web kompromittiert, so verhindert eine Einschränkung der Rechte eine weitere Ausbreitung des Angriffs. Relevant sind dabei Zugriffsrechte für Dateisystem und Systemfunktionen. Zweckmäßig ist es hierzu, die Berechtigungen so einzuschränken, dass der Serverdienst a) keinen Zugriff auf Dateien außerhalb des WWW-Wurzelverzeichnisses hat, b) Schreibzugriffe innerhalb des WWW‑Wurzelverzeichnisses nur in explizit autorisierten Unter­verzeichnissen hat, c) keine Programme oder Shell‑Befehle außerhalb der vorgesehenen Interpreter ausführen kann, d) keine privilegierten Berechtigungen besitzt. Unterverzeichnisse die Schreibrechte benötigen könnten sind etwa /uploads, /cache, /tmp.

### → APP.3.2.A1 — Sichere Konfiguration eines Webservers (B)
  1. Nachdem der IT-Betrieb einen Webserver installiert hat, MUSS er eine sichere Grundkonfiguration vornehmen.
  2. Dazu MUSS er insbesondere den Webserver-Prozess einem Konto mit minimalen Rechten zuweisen. **◀ ZITIERT**
  3. Der Webserver MUSS in einer gekapselten Umgebung ausgeführt werden, sofern dies vom Betriebssystem unterstützt wird.
  4. Ist dies nicht möglich, SOLLTE jeder Webserver auf einem eigenen physischen oder virtuellen Server ausgeführt werden.
  5. Dem Webserver-Dienst MÜSSEN alle nicht notwendige Schreibberechtigungen entzogen werden. **◀ ZITIERT**
  6. Nicht benötigte Module und Funktionen des Webservers MÜSSEN deaktiviert werden.
- **Satz 2** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) KONF.6.8 fordert spezifisch die Einschränkung der Berechtigungen des Webserver-Prozesses und deckt damit die Zuweisung des Prozesses an ein Konto mit minimalen Rechten direkt ab.
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) Die Maßnahme KONF.6.8 fordert die Einschränkung der Berechtigungen des Webserver-Prozesses und adressiert in ihren Vorgaben explizit den Entzug nicht benötigter Schreibzugriffe.

### → APP.3.2.A2 — Schutz der Webserver-Dateien (B)
  1. Der IT-Betrieb MUSS alle Dateien auf dem Webserver, insbesondere Skripte und Konfigurationsdateien, so schützen, dass sie nicht unbefugt gelesen und geändert werden können.
  2. Es MUSS sichergestellt werden, dass Webanwendungen nur auf einen definierten Verzeichnisbaum zugreifen können (WWW-Wurzelverzeichnis). **◀ ZITIERT**
  3. Der Webserver MUSS so konfiguriert sein, dass er nur Dateien ausliefert, die sich innerhalb des WWW-Wurzelverzeichnisses befinden.
  4. Der IT-Betrieb MUSS alle nicht benötigten Funktionen, die Verzeichnisse auflisten, deaktivieren.
  5. Vertrauliche Daten MÜSSEN vor unberechtigtem Zugriff geschützt werden.
  6. Insbesondere MUSS der IT-Betrieb sicherstellen, dass vertrauliche Dateien nicht in öffentlichen Verzeichnissen des Webservers liegen.
  7. Der IT-Betrieb MUSS regelmäßig überprüfen, ob vertrauliche Dateien in öffentlichen Verzeichnissen gespeichert wurden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) KONF.6.8 fordert die Einschränkung der Berechtigungen des Webserver-Prozesses und nennt explizit die Begrenzung des Dateisystemzugriffs auf das WWW-Wurzelverzeichnis.

### → SYS.4.4.A24 — Sichere Konfiguration und Nutzung eines eingebetteten Webservers (H)
  1. In IoT-Geräten integrierte Webserver SOLLTEN möglichst restriktiv konfiguriert sein.
  2. Der Webserver SOLLTE, soweit möglich, NICHT unter einem privilegierten Konto betrieben werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) Die G++-Maßnahme KONF.6.8 verlangt die Einschränkung der Berechtigungen des Webserver-Prozesses und schließt dabei den Verzicht auf privilegierte Berechtigungen bzw. Konten explizit ein.


## KONF.7.4 — Angriffserkennung anhand von Netzverkehr  [1 Paare]

**Statement (normativ):** Konfiguration für IT-Systeme KANN Angriffserkennung anhand von Netzverkehr aktivieren.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** erhöht
**Guidance (nicht normativ):** Hierbei wird eine netzwerkbasierte Bedrohungsanalyse direkt auf dem IT-System durchgeführt. Dieser Ansatz, oft als Host-based Network Intrusion Detection System (H-NIDS) oder Endpoint Detection and Response (EDR) bezeichnet, ermöglicht eine tiefere Sicht in das Systemverhalten. Statt nur den Datenstrom am Perimeter zu überwachen, kann so die Institution verdächtige Aktivitäten wie das Scannen von Netzwerk-Ports, den Aufbau ungewöhnlicher Verbindungen zu Command-and-Control-Servern oder den Versuch der Datenexfiltration erkennen. Ohne diese Erkennung könnte sich ein Angreifer, der bereits in das Netzwerk eingedrungen ist, unentdeckt von System zu System bewegen oder sensible Daten unbemerkt nach außen senden. Die dezentrale Erkennung auf den Clients kann zudem dabei helfen, interne Lateral-Movement-Versuche zu identifizieren, da der Datenverkehr zwischen den Systemen überwacht wird, selbst wenn er das interne Netzwerk nicht verlässt. Um diese Anforderung umzusetzen, kann die Institution spezialisierte EDR- oder Endpoint-Security-Lösungen nutzen, die eine integrierte Funktion zur Netzwerküberwachung bieten. Es kann ebenfalls eine regelbasierte Erkennung über lokale Host-Firewalls oder Sicherheitsagenten aktiviert werden, die bestimmte Muster im Netzwerkverkehr blockieren oder protokollieren. Bei der Einführung solcher Maßnahmen ist es entscheidend, die Performance des Clients zu berücksichtigen. Daher kann die Konfiguration so optimiert werden, dass sie nur kritische Protokolle oder Ports überwacht, um die Systemressourcen zu schonen.

### → SYS.2.5.A14 — Erweiterte Sicherheitsfunktionen für den Einsatz von virtuellen Clients (H)
  1. Die virtuellen Clients SOLLTEN mit zusätzlichen Sicherheitsfunktionen geschützt werden.
  2. Dabei SOLLTEN mindestens die folgenden Techniken berücksichtigt werden: Mikrosegmentierung für die virtuellen Clients Intrusion-Detection- oder Intrusion-Prevention-Systeme, die entweder zentralisiert auf der Virtualisierungsinfrastruktur oder dezentral auf den virtuellen Clients bereitgestellt werden **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme KONF.7.4 deckt den im Satz geforderten Einsatz von netzwerkbasierten Intrusion-Detection-Systemen (Angriffserkennung anhand von Netzverkehr) auf den Clients ab.


## KONF.10.2 — Kryptographische Verfahren in Anwendungen  [30 Paare]

**Statement (normativ):** Konfiguration für Anwendungen SOLLTE kryptographische Verfahren nach {{ insert: param, konf.10.2-prm1 }} im Einklang mit den zugehörigen Anforderungen zum Identitäts- und Berechtigungsmanagement aktivieren.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Kryptographie wird für die Authentifizierung, Verschlüsselung und Integritätprüfung in Anwendungen verwendet, z.B. bei der Anmeldung an der Anwendung oder digitalen Signierung von Nachrichten. Die Formulierung "im Einklang mit den zugehörigen Anforderungen zum Identitäts- und Berechtigungsmanagement" bedeutet, dass die Authentifizierung so erfolgt, wie in der Praktik Berechtigung (BER) festgelegt. Hierzu gehört insbesondere die Verwendung aktueller kryptographischer Verfahren, wie sie im Thema Schlüsselmanagement zu finden ist. Anerkannte kryptographische Verfahren sind in der BSI TR-02102 zu finden.

### → APP.1.1.A12 — Verzicht auf Cloud-Speicherung (S) [Benutzende]
  1. Die in einigen Office-Produkten integrierten Funktionen für Cloud-Speicher SOLLTEN grundsätzlich deaktiviert werden.
  2. Alle Cloud-Laufwerke SOLLTEN deaktiviert werden.
  3. Alle Dokumente SOLLTEN durch die Benutzenden auf zentral verwalteten Fileservern der Institution gespeichert werden.
  4. Um Dokumente für Dritte freizugeben, SOLLTEN spezialisierte Anwendungen eingesetzt werden.
  5. Diese Anwendungen SOLLTEN mindestens über eine verschlüsselte Datenablage und -versendung sowie ein geeignetes System zur Konten- und Rechteverwaltung verfügen. **◀ ZITIERT**
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) KONF.10.2 fordert die Aktivierung kryptographischer Verfahren (wie Verschlüsselung bei Übertragung und Speicherung) in Anwendungen im Einklang mit dem Identitäts- und Berechtigungsmanagement, was die Anforderungen aus Satz 5 abdeckt.

### → APP.1.1.A16 — Integritätsprüfung von Dokumenten (H)
  1. Wenn Daten mit erhöhtem Schutzbedarf gespeichert oder übertragen werden, SOLLTEN geeignete Verfahren zur Integritätsprüfung eingesetzt werden.
  2. Falls Daten vor Manipulation geschützt werden sollen, SOLLTEN darüber hinaus kryptografische Verfahren eingesetzt werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme fordert die Aktivierung anerkannter kryptografischer Verfahren in Anwendungen, was den Einsatz kryptografischer Mechanismen zum Manipulations- und Integritätsschutz abdeckt.

### → APP.1.2.A2 — Unterstützung sicherer Verschlüsselung der Kommunikation (B)
  1. Der Webbrowser MUSS Transport Layer Security (TLS) in einer sicheren Version unterstützen. **◀ ZITIERT**
  2. Verbindungen zu Webservern MÜSSEN mit TLS verschlüsselt werden, falls dies vom Webserver unterstützt wird.
  3. Unsichere Versionen von TLS SOLLTEN deaktiviert werden.
  4. Der Webbrowser MUSS den Sicherheitsmechanismus HTTP Strict Transport Security (HSTS) gemäß RFC 6797 unterstützen und einsetzen.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) KONF.10.2 fordert allgemein die Aktivierung anerkannter kryptographischer Verfahren in Anwendungen, was die Unterstützung und den Einsatz sicherer TLS-Versionen im Webbrowser umfasst.

### → APP.2.2.A8 — Absicherung des „Sicheren Kanals“ (S)
  1. Der „Sichere Kanal“ SOLLTE so konfiguriert sein, dass alle übertragenen Daten immer verschlüsselt und signiert werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) KONF.10.2 fordert die anwendungsseitige Aktivierung kryptographischer Verfahren (wie Verschlüsselung und Integritätsprüfung/Signierung) und deckt damit die Konfiguration des sicheren Kanals zur Verschlüsselung und Signierung übertragener Daten ab.

### → APP.2.2.A9 — Schutz der Authentisierung beim Einsatz von AD DS (S)
  1. In der Gesamtstruktur SOLLTE konsequent das Authentisierungsprotokoll Kerberos eingesetzt werden. **◀ ZITIERT**
  2. Dabei SOLLTE für die Absicherung AES128_HMAC_SHA1 oder AES256_HMAC_SHA1 verwendet werden.
  3. Wenn aus Kompatibilitätsgründen übergangsweise NTLMv2 eingesetzt wird, SOLLTE die Migration auf Kerberos geplant und terminiert werden.
  4. Die LM-Authentisierung und NTLMv1 MÜSSEN deaktiviert sein.
  5. Der SMB-Datenverkehr MUSS signiert sein.
  6. SMBv1 MUSS deaktiviert sein.
  7. Anonyme Zugriffe auf Domänencontroller SOLLTEN unterbunden sein.
  8. LDAP-Sitzungen SOLLTEN nur signiert und mit konfiguriertem Channel Binding Token (CBT) erfolgen.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) KONF.10.2 verlangt die Aktivierung anerkannter kryptographischer Verfahren für die Authentifizierung in Anwendungen, was den Einsatz des Standardprotokolls Kerberos im AD DS abstrahiert abdeckt.

### → APP.2.3.A6 — Sichere Authentisierung gegenüber OpenLDAP (B)
  1. Wenn der Verzeichnisdienst zwischen verschiedenen Benutzenden unterscheiden soll, MÜSSEN sich diese geeignet authentisieren.
  2. Die Authentisierung zwischen dem slapd-Server und den Kommunikationsbeteiligten MUSS verschlüsselt werden.
  3. Es SOLLTEN NUR die Hashwerte von Passwörtern auf den Clients und Servern abgespeichert werden.
  4. Es MUSS ein geeigneter Hashing-Algorithmus verwendet werden. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) KONF.10.2 deckt die Forderung ab, indem es die Aktivierung kryptographischer Verfahren nach anerkannten Standards (wie BSI TR-02102) u. a. für die Authentifizierung in Anwendungen verlangt.

### → APP.3.4.A15 — Verschlüsselung der Datenpakete unter Samba (H)
  1. Um die Sicherheit der Datenpakete auf dem Transportweg zu gewährleisten, SOLLTEN die Datenpakete mit den ab SMB Version 3 integrierten Verschlüsselungsverfahren verschlüsselt werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) KONF.10.2 fordert allgemein die Aktivierung anerkannter kryptographischer Verfahren in Anwendungen, was die anwendungsbezogene Konfiguration der SMBv3-Transportverschlüsselung abdeckt.

### → APP.3.4.A3 — Sichere Konfiguration eines Samba-Servers (S)
  1. Datenbanken im Trivial-Database-(TDB)-Format SOLLTEN NICHT auf einer Partition gespeichert werden, die ReiserFS als Dateisystem benutzt.
  2. Wird eine netlogon-Freigabe konfiguriert, SOLLTEN unberechtigte Benutzende KEINE Dateien in dieser Freigabe modifizieren können.
  3. Das Betriebssystem eines Samba-Servers SOLLTE Access Control Lists (ACLs) in Verbindung mit dem eingesetzten Dateisystem unterstützen.
  4. Zusätzlich SOLLTE sichergestellt werden, dass das Dateisystem mit den passenden Parametern eingebunden wird.
  5. Die Voreinstellungen von SMB Message Signing SOLLTEN beibehalten werden, sofern sie nicht im Widerspruch zu den existierenden Sicherheitsrichtlinien im Informationsverbund stehen. **◀ ZITIERT**
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) KONF.10.2 fordert die Aktivierung anerkannter kryptographischer Verfahren wie dem Signieren von Nachrichten in Anwendungen, was das Beibehalten bzw. Konfigurieren von SMB Message Signing gemäß Sicherheitsrichtlinien direkt abdeckt.

### → APP.3.4.A9 — Sichere Konfiguration von Kerberos unter Samba (S)
  1. Zur Authentisierung SOLLTE das von Samba implementierte Heimdal Kerberos Key Distribution Center (KDC) verwendet werden.
  2. Es SOLLTE darauf geachtet werden, dass die von Samba vorgegebene Kerberos-Konfigurationsdatei verwendet wird.
  3. Es SOLLTEN nur sichere Verschlüsselungsverfahren für Kerberos-Tickets benutzt werden. **◀ ZITIERT**
  4. Wird mit Kerberos authentisiert, SOLLTE der zentrale Zeitserver lokal auf dem Samba-Server installiert werden.
  5. Der NTP-Dienst SOLLTE so konfiguriert werden, dass nur autorisierte Clients die Zeit abfragen können.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) KONF.10.2 fordert die anwendungsspezifische Aktivierung sicherer kryptographischer Verfahren nach Standards, was den Einsatz sicherer Verschlüsselungsverfahren für Kerberos-Tickets abdeckt.

### → APP.3.6.A17 — Einsatz von DNSSEC (S)
  1. Die DNS-Protokollerweiterung DNSSEC SOLLTE sowohl auf Resolving DNS-Servern als auch auf Advertising DNS-Servern aktiviert werden. **◀ ZITIERT**
  2. Die dabei verwendeten Schlüssel Key-Signing-Keys (KSK) und Zone-Signing-Keys (ZSK) SOLLTEN regelmäßig gewechselt werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die Aktivierung von DNSSEC auf DNS-Servern ist eine spezifische Ausprägung der allgemeinen Forderung in KONF.10.2, kryptographische Verfahren zur Integritätsprüfung und Signierung in Anwendungen zu aktivieren.

### → APP.3.6.A18 — Erweiterte Absicherung von Zonentransfers (S)
  1. Um Zonentransfers stärker abzusichern, SOLLTEN zusätzlich Transaction Signatures (TSIG) eingesetzt werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) KONF.10.2 fordert die Aktivierung kryptographischer Verfahren in Anwendungen, was den Einsatz von Transaction Signatures (TSIG) zur kryptographischen Absicherung von DNS-Zonentransfers als konkreten Anwendungsfall umfasst.

### → APP.4.2.A18 — Abschaltung von unsicherer Kommunikation (S)
  1. Die Kommunikation mit und zwischen SAP-ERP-Systemen SOLLTE mit SNC abgesichert werden. **◀ ZITIERT**
  2. Sofern Datenbank und SAP-Applikationsserver auf verschiedenen Systemen betrieben werden, SOLLTE die Datenbankverbindung in geeigneter Weise verschlüsselt werden. **◀ ZITIERT**
  3. Die internen Dienste des SAP-Applikationsservers SOLLTEN NUR mittels TLS miteinander kommunizieren. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) KONF.10.2 fordert allgemein die Aktivierung kryptographischer Verfahren in Anwendungen, was die spezifische Absicherung der SAP-Kommunikation mittels SNC als kryptographischem Standardverfahren umfasst.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) KONF.10.2 fordert allgemein die Aktivierung kryptographischer Verfahren (wie Verschlüsselung) in Anwendungskonfigurationen und deckt damit die Verschlüsselung der Datenbankverbindung des Applikationsservers ab.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) KONF.10.2 fordert allgemein die Aktivierung anerkannter kryptographischer Verfahren (wie TLS nach BSI TR-02102) in Anwendungskonfigurationen und deckt damit die TLS-Verschlüsselung interner SAP-Dienste ab.

### → APP.4.3.A16 — Verschlüsselung der Datenbankanbindung (S)
  1. Das Datenbankmanagementsystem SOLLTE so konfiguriert werden, dass Datenbankverbindungen immer verschlüsselt werden.
  2. Die dazu eingesetzten kryptografischen Verfahren und Protokolle SOLLTEN den internen Vorgaben der Institution entsprechen (siehe CON.1 Kryptokonzept). **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) KONF.10.2 fordert die Aktivierung kryptografischer Verfahren nach anerkannten Standards für Anwendungen und deckt damit die Verwendung richtlinienkonformer Verfahren bei der Datenbankanbindung inhaltlich ab.

### → APP.5.3.A10 — Ende-zu-Ende-Verschlüsselung und Signatur (H)
  1. Die Institution SOLLTE eine Ende-zu-Ende-Verschlüsselung sowie digitale Signaturen für E-Mails einsetzen.
  2. Es SOLLTEN nur Protokolle zur Verschlüsselung und Signatur genutzt werden, die dem aktuellen Stand der Technik entsprechen. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) KONF.10.2 fordert die Aktivierung kryptographischer Verfahren nach anerkannten Standards in Anwendungen und deckt damit den Einsatz dem Stand der Technik entsprechender Verschlüsselungs- und Signaturprotokolle ab.

### → APP.5.4.A16 — Einsatz eines SBC an weiteren Netzübergängen (H)
  1. Ergänzend zu einem SBC am Netzübergang zum Provider, SOLLTEN weitere SBC an internen Netzübergängen eingesetzt werden.
  2. Hierbei SOLLTEN insbesondere Netzübergänge zwischen Netzsegmenten mit unterschiedlichem Schutzbedarf berücksichtigt werden.
  3. Der SBC SOLLTE sicherstellen, dass die Verschlüsselungsmechanismen an den SBC-gesicherten Netzsegmentübergängen anforderungskonform realisiert werden. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) KONF.10.2 verlangt allgemein die anforderungs- und standardkonforme Aktivierung kryptographischer Verfahren in Anwendungen, was die Durchsetzung von Verschlüsselungsmechanismen durch den SBC abdeckt.

### → CON.10.A18 — Kryptografische Absicherung vertraulicher Daten (H)
  1. Vertrauliche Daten einer Webanwendung SOLLTEN durch sichere, kryptografische Algorithmen abgesichert werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) KONF.10.2 fordert die Aktivierung kryptographischer Verfahren nach anerkannten Standards in Anwendungen, was die Absicherung vertraulicher Daten von Webanwendungen mit sicheren kryptografischen Algorithmen abdeckt.

### → INF.14.A12 — Nutzung sicherer Übertragungsprotokolle für die GA (S)
  1. Für Konfiguration, Wartung und Steuerung von GA-relevanten Komponenten, die auf Ethernet und IP basieren, SOLLTEN sichere Protokolle eingesetzt werden, falls nicht über vertrauenswürdige Netzsegmente kommuniziert wird.
  2. Außerhalb vertrauenswürdiger Netzsegmente SOLLTE die Kommunikation über Ethernet und IP zwischen GA-Systemen verschlüsselt erfolgen.
  3. Die Verschlüsselung SOLLTE mit den jeweils aktuellen Verschlüsselungsmechanismen durchgeführt werden. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) KONF.10.2 verlangt die Aktivierung kryptographischer Verfahren nach anerkannten Standards, was den Einsatz jeweils aktueller Verschlüsselungsmechanismen inhaltlich abdeckt.

### → NET.3.4.A24 — Nutzung sicherer Protokolle zwischen NAC-Komponenten (H)
  1. Für die Kommunikation zwischen den zentralen NAC-Komponenten SOLLTEN grundsätzlich Protokolle verwendet werden, die nach dem Stand der Technik als sicher gelten.
  2. Für die Kommunikation zwischen dem RADIUS-Server und einem gegebenenfalls genutzten Verzeichnisdienst SOLLTEN nur sichere Protokolle eingesetzt werden. **◀ ZITIERT**
  3. Darüber hinaus SOLLTE auch geprüft werden, ob für die Kommunikation zwischen dem RADIUS-Server und Access-Switches sichere Protokolle eingesetzt werden sollen.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) KONF.10.2 fordert die Aktivierung anerkannter kryptographischer Verfahren in Anwendungen im Einklang mit IAM-Anforderungen, was den Einsatz sicherer Protokolle zwischen RADIUS-Server und Verzeichnisdienst umfasst.

### → NET.4.2.A15 — Sicherer Medientransport mit SRTP (H)
  1. Mediendaten und Informationen zur Steuerung dieser Daten, die über das Real-Time Transport Protocol (RTP) übertragen werden, SOLLTEN in geeigneter Weise geschützt werden.
  2. Die Nutzdaten SOLLTEN durch den Einsatz von Secure Real-Time Transport Protocol (SRTP) beziehungsweise Secure Real-Time Control Protocol (SRTCP) geschützt werden. **◀ ZITIERT**
  3. Die sicherheitsrelevanten Optionen der Implementierung des Protokolls SOLLTEN dokumentiert werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) KONF.10.2 fordert die allgemeine Aktivierung anerkannter kryptographischer Verfahren in Anwendungen, was den Einsatz von SRTP und SRTCP zur kryptographischen Absicherung von Nutzdaten als konkreten Anwendungsfall umfasst.

### → OPS.1.1.7.A5 — Gegenseitige Authentisierung von Systemmanagement-Lösung und zu verwaltenden Systemen (B)
  1. Die Authentisierung zwischen Systemmanagement-Lösung und zu verwaltenden Systemen MUSS in beide Richtungen erfolgen.
  2. Die Authentisierung MUSS in das übergreifende Authentisierungskonzept eingebunden sein.
  3. Die Authentisierung MUSS mittels sicherer Protokolle erfolgen. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) KONF.10.2 fordert die Aktivierung kryptographischer Verfahren nach anerkannten Standards für Authentifizierung und Identitätsmanagement in Anwendungen und deckt damit die Nutzung sicherer Protokolle zur Authentisierung ab.

### → OPS.1.2.5.A8 — Sichere Protokolle bei der Fernwartung (S)
  1. Nur als sicher eingestufte Kommunikationsprotokolle SOLLTEN eingesetzt werden.
  2. Dafür SOLLTEN sichere kryptografische Verfahren verwendet werden. **◀ ZITIERT**
  3. Die Stärke der verwendeten kryptografischen Verfahren und Schlüssel SOLLTE regelmäßig überprüft und bei Bedarf angepasst werden.
  4. Wird auf die Fernwartungszugänge von IT-Systemen im internen Netz über ein öffentliches Datennetz zugegriffen, SOLLTE ein abgesichertes Virtuelles Privates Netz (VPN) genutzt werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme KONF.10.2 verlangt die Aktivierung kryptographischer Verfahren nach anerkannten Standards in Anwendungen und deckt damit die allgemeinere bzw. anwendungsbezogene Forderung nach dem Einsatz sicherer kryptografischer Verfahren in Protokollen ab.

### → OPS.1.2.6.A12 — NTP-Server mit authentifizierten Auskünften (H)
  1. NTP-Server SOLLTEN sich bei der Kommunikation gegenüber Clients authentisieren. **◀ ZITIERT**
  2. Dies SOLLTE auch für die Server gelten, von denen der NTP-Server seinerseits Zeitinformationen erhält.
  3. Die NTP-Clients SOLLTEN nur authentifizierte NTP-Daten akzeptieren.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) KONF.10.2 deckt die Forderung als allgemeinere Maßnahme ab, indem sie die Aktivierung kryptographischer Verfahren zur Authentifizierung in der Konfiguration von Anwendungen vorschreibt.

### → SYS.1.5.A5 — Schutz der Administrationsschnittstellen (B)
  1. Alle Administrations- und Management-Zugänge zum Managementsystem und zu den Host-Systemen MÜSSEN eingeschränkt werden.
  2. Es MUSS sichergestellt sein, dass aus nicht-vertrauenswürdigen Netzen heraus nicht auf die Administrationsschnittstellen zugegriffen werden kann.
  3. Um die Virtualisierungsserver oder die Managementsysteme zu administrieren bzw. zu überwachen, SOLLTEN als sicher geltende Protokolle eingesetzt werden. **◀ ZITIERT**
  4. Sollte dennoch auf unsichere Protokolle zurückgegriffen werden, MUSS für die Administration ein eigenes Administrationsnetz genutzt werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) KONF.10.2 deckt den Einsatz sicherer Protokolle für Managementsysteme als allgemeine Pflicht zur Aktivierung anerkannter kryptographischer Verfahren in Anwendungskonfigurationen ab.

### → SYS.1.9.A17 — Verschlüsselung der Übertragung (H)
  1. Jegliche Kommunikation zwischen Client und Terminalserver SOLLTE geeignet verschlüsselt werden.
  2. Dabei SOLLTEN sichere Protokolle gemäß BSI TR-02102 verwendet werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) KONF.10.2 fordert die Aktivierung kryptographischer Verfahren nach anerkannten Standards (explizit BSI TR-02102) in Anwendungen und deckt damit die Verwendung sicherer kryptographischer Protokolle ab.

### → SYS.1.9.A7 — Sicherer Zugriff auf den Terminalserver (B)
  1. Es MUSS festgelegt werden, über welche Netze zwischen zugreifendem Client und Terminalserver kommuniziert werden darf.
  2. Zusätzlich MUSS festgelegt werden, wie die Kommunikation abgesichert werden soll.
  3. Es MUSS festgelegt werden, ob und wie mit dem Terminalserver-Protokoll verschlüsselt werden soll. **◀ ZITIERT**
  4. Falls das Terminalserver-Protokoll in diesem Fall keine ausreichende Verschlüsselung bietet, MUSS die Kommunikation zusätzlich abgesichert werden.
  5. Falls die Clients und der Terminalserver über unzureichend vertrauenswürdige Netze kommunizieren, MÜSSEN sich sowohl die Benutzenden als auch der Terminalserver beim Kommunikationsaufbau authentisieren.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) KONF.10.2 deckt die Festlegung und Aktivierung kryptographischer Verfahren (wie der Protokollverschlüsselung) auf Anwendungsebene als allgemeinere Anforderung inhaltlich ab.

### → CON.1.A1 — Auswahl geeigneter kryptografischer Verfahren (B) [Fachverantwortliche]
  1. Es MÜSSEN geeignete kryptografische Verfahren ausgewählt werden. **◀ ZITIERT**
  2. Dabei MUSS sichergestellt sein, dass etablierte Algorithmen verwendet werden, die von der Fachwelt intensiv untersucht wurden und von denen keine Sicherheitslücken bekannt sind.
  3. Ebenso MÜSSEN aktuell empfohlene Schlüssellängen verwendet werden.
  4. Um eine geeignete Schlüssellänge auszuwählen, SOLLTE berücksichtigt werden, wie lange das kryptografische Verfahren eingesetzt werden soll.
  5. Bei einer längeren Einsatzdauer SOLLTEN entsprechend längere Schlüssellängen eingesetzt werden.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) KONF.10.2 fordert die Aktivierung kryptographischer Verfahren nach anerkannten Standards für Anwendungen und deckt damit die Auswahl geeigneter kryptografischer Verfahren in diesem Kontext ab.

### → APP.4.2.A31 — Konfiguration von SAP Single-Sign-On (S)
  1. Sind mehrere SAP-ERP-Systeme vorhanden, SOLLTEN die Benutzenden auf die Systeme mit SAP Single-Sign-On (SAP SSO) zugreifen.
  2. Es SOLLTE in der Planungsphase entschieden werden, zwischen welchen SAP-ERP-Systemen der SSO-Mechanismus benutzt wird.
  3. Das SSO SOLLTE sicher konfiguriert und betrieben werden. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) KONF.10.2 fordert die sichere Konfiguration kryptographischer Verfahren bei der Authentifizierung und beim Identitätsmanagement und deckt damit die sichere Konfiguration des SSO ab.

### → CON.9.A8 — Verschlüsselung und digitale Signatur (S)
  1. Die Institution SOLLTE prüfen, ob Informationen während des Austausches kryptografisch gesichert werden können.
  2. Falls die Informationen kryptografisch gesichert werden, SOLLTEN dafür ausreichend sichere Verfahren eingesetzt werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) KONF.10.2 fordert den Einsatz kryptographischer Verfahren nach anerkannten Standards in Anwendungen und deckt damit die Forderung nach ausreichend sicheren kryptographischen Verfahren für den Informationsaustausch ab.


## KONF.1.4 — Einschränkung des Zugriffs auf Dokumentation  [12 Paare]

**Statement (normativ):** Konfiguration SOLLTE den Zugriff auf dokumentierte Konfigurationen einschränken.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** „Dokumentierte Konfigurationen“ sind hierbei festgehaltene Einstellungen von IT-Systemen, Anwendungen, Netzwerken oder Sicherheitskomponenten, die in schriftlicher oder elektronischer Form vorliegen und den Sollzustand einer IT-Umgebung definieren. Der Zweck der Vorschrift liegt darin, die Integrität und Vertraulichkeit solcher Konfigurationsinformationen zu schützen. Ein unkontrollierter Zugriff könnte beispielsweise dazu führen, dass ein Unbefugter Passworteinstellungen oder Firewall-Regeln manipuliert. Aus der Konfiguration von IT-Systemen könnte ein Angreifer zudem wichtige Informationen zu möglichen Schwachstellen ablesen (z.B. bei technisch notwendiger Verwendung schwacher Verschlüsselungsalgorithmen oder unsicherer Authentisierungsprotokolle wie NTLM). Ein strikter Zugriffsschutz (z.B. durch restriktive Berechtigungen oder Verschlüsselung) verhindert den unberechtigten Zugriff zu diesen sensiblen Informationen. Praktisch hilfreich kann auch sein, Konfigurationen verschlüsselt abzulegen und bei elektronischen Repositories sogenannte „Branch Protection“-Mechanismen einzusetzen, sodass Änderungen nur über geprüfte Freigabeprozesse übernommen werden können. Auf Papier vorliegende Konfigurationen kann die Institution in verschlossenen Schränken oder Archiven mit eingeschränktem Personenkreis verwahren.

### → APP.4.4.A8 — Absicherung von Konfigurationsdateien bei Kubernetes (S)
  1. Die Konfigurationsdateien des Kubernetes-Clusters, inklusive aller Erweiterungen und Anwendungen, SOLLTEN versioniert und annotiert werden.
  2. Zugangsrechte auf die Verwaltungssoftware der Konfigurationsdateien SOLLTEN minimal vergeben werden.
  3. Zugriffsrechte für lesenden und schreibenden Zugriff auf die Konfigurationsdateien der Control Plane SOLLTEN besonders sorgfältig vergeben und eingeschränkt sein. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) KONF.1.4 fordert allgemein die Einschränkung des Zugriffs auf dokumentierte Konfigurationen, was die spezifische restriktive Vergabe von Lese- und Schreibrechten auf Kubernetes-Control-Plane-Konfigurationsdateien inhaltlich abdeckt.

### → NET.3.1.A1 — Sichere Grundkonfiguration eines Routers oder Switches (B)
  1. Bevor ein Router oder Switch eingesetzt wird, MUSS er sicher konfiguriert werden.
  2. Alle Konfigurationsänderungen SOLLTEN nachvollziehbar dokumentiert sein.
  3. Die Integrität der Konfigurationsdateien MUSS in geeigneter Weise geschützt werden. **◀ ZITIERT**
  4. Bevor Zugangspasswörter abgespeichert werden, MÜSSEN sie mithilfe eines zeitgemäßen kryptografischen Verfahrens abgesichert werden.
  5. Router und Switches MÜSSEN so konfiguriert sein, dass nur zwingend erforderliche Dienste, Protokolle und funktionale Erweiterungen genutzt werden.
  6. Nicht benötigte Dienste, Protokolle und funktionale Erweiterungen MÜSSEN deaktiviert oder ganz deinstalliert werden.
  7. Ebenfalls MÜSSEN nicht benutzte Schnittstellen auf Routern und Switches deaktiviert werden.
  8. Unbenutzte Netzports MÜSSEN nach Möglichkeit deaktiviert oder zumindest einem dafür eingerichteten Unassigned-VLAN zugeordnet werden.
  9. Wenn funktionale Erweiterungen benutzt werden, MÜSSEN die Sicherheitsrichtlinien der Institution weiterhin erfüllt sein.
  10. Auch SOLLTE begründet und dokumentiert werden, warum solche Erweiterungen eingesetzt werden.
  11. Informationen über den internen Konfigurations- und Betriebszustand MÜSSEN nach außen verborgen werden.
  12. Unnötige Auskunftsdienste MÜSSEN deaktiviert werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) KONF.1.4 fordert die Zugriffsbeschränkung auf dokumentierte Konfigurationen mit dem expliziten Zweck, deren Integrität vor unbefugten Manipulationen zu schützen.

### → NET.3.1.A9 — Betriebsdokumentationen (B)
  1. Die wichtigsten betrieblichen Aufgaben eines Routers oder Switches MÜSSEN geeignet dokumentiert werden.
  2. Es SOLLTEN alle Konfigurationsänderungen sowie sicherheitsrelevante Aufgaben dokumentiert werden.
  3. Die Dokumentation SOLLTEN vor unbefugten Zugriffen geschützt werden. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 3) G++ KONF.1.4 fordert explizit die Einschränkung des Zugriffs auf dokumentierte Konfigurationen und deckt damit den Schutz der Dokumentation vor unbefugtem Zugriff inhaltlich ab.

### → NET.3.2.A14 — Betriebsdokumentationen (B)
  1. Die betrieblichen Aufgaben einer Firewall MÜSSEN nachvollziehbar dokumentiert werden.
  2. Es MÜSSEN alle Konfigurationsänderungen sowie sicherheitsrelevante Aufgaben dokumentiert werden, insbesondere Änderungen an den Systemdiensten und dem Regelwerk der Firewall.
  3. Die Dokumentation MUSS vor unbefugten Zugriffen geschützt werden. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 3) Die G++-Maßnahme KONF.1.4 fordert explizit die Einschränkung des Zugriffs auf Konfigurationsdokumentationen und deckt damit den Schutz der Dokumentation vor unbefugtem Zugriff inhaltlich ab.

### → NET.3.2.A4 — Sichere Konfiguration der Firewall (B)
  1. Bevor eine Firewall eingesetzt wird, MUSS sie sicher konfiguriert werden.
  2. Alle Konfigurationsänderungen MÜSSEN nachvollziehbar dokumentiert sein.
  3. Die Integrität der Konfigurationsdateien MUSS geeignet geschützt werden. **◀ ZITIERT**
  4. Bevor Zugangspasswörter abgespeichert werden, MÜSSEN sie mithilfe eines zeitgemäßen kryptografischen Verfahrens abgesichert werden (siehe CON.1 Kryptokonzept).
  5. Eine Firewall MUSS so konfiguriert sein, dass ausschließlich zwingend erforderliche Dienste verfügbar sind.
  6. Wenn funktionale Erweiterungen benutzt werden, MÜSSEN die Sicherheitsrichtlinien der Institution weiterhin erfüllt sein.
  7. Auch MUSS begründet und dokumentiert werden, warum solche Erweiterungen eingesetzt werden.
  8. Nicht benötigte (Auskunfts-)Dienste sowie nicht benötigte funktionale Erweiterungen MÜSSEN deaktiviert oder ganz deinstalliert werden.
  9. Informationen über den internen Konfigurations- und Betriebszustand MÜSSEN nach außen bestmöglich verborgen werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) KONF.1.4 fordert die Zugriffsbeschränkung auf elektronisch oder schriftlich festgehaltene Konfigurationen, um deren Integrität und Vertraulichkeit vor unbefugten Manipulationen zu schützen.

### → SYS.1.8.A17 — Dokumentation der Systemeinstellungen von Speichersystemen (S)
  1. Alle Systemeinstellungen von Speichersystemen SOLLTEN dokumentiert werden.
  2. Die Dokumentation SOLLTE die technischen und organisatorischen Vorgaben sowie alle spezifischen Konfigurationen der Speichersysteme der Institution enthalten.
  3. Sofern die Dokumentation der Systemeinstellungen vertrauliche Informationen beinhaltet, SOLLTEN diese vor unberechtigtem Zugriff geschützt werden. **◀ ZITIERT**
  4. Die Dokumentation SOLLTE regelmäßig überprüft werden.
  5. Sie SOLLTE immer aktuell sein.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 3) Die Maßnahme KONF.1.4 verlangt allgemein die Einschränkung des Zugriffs auf dokumentierte Konfigurationen zum Schutz vor unberechtigtem Zugriff und deckt damit den geforderten Schutz vertraulicher Systemeinstellungsdokumentationen inhaltlich ab.

### → OPS.1.1.1.A13 — Absicherung der Betriebsmittel und der Dokumentation (S)
  1. Auf die Betriebsmittel, die Dokumentation und die Betriebshandbücher SOLLTEN nur berechtigte Personen des IT-Betriebs zugreifen können. **◀ ZITIERT**
  2. Der IT-Betrieb SOLLTE sicherstellen, dass die Betriebsmittel und die Dokumentation zu jeder Zeit verfügbar sind.
  3. Falls die IT-Systeme und -Anwendungen der Betriebsmittel über die produktive Infrastruktur kommunizieren, SOLLTEN sichere Protokolle verwendet werden.
  4. Vertrauliche Daten SOLLTEN ausschließlich über sichere Protokolle übertragen werden.
  5. Die Betriebsmittel SOLLTEN in das Schwachstellenmanagement und das IT-Monitoring eingebunden werden.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) KONF.1.4 deckt die Forderung nach beschränktem Zugriff auf Dokumentation als speziellen Anwendungsfall für dokumentierte Konfigurationen ab.

### → INF.13.A3 — Dokumentation von Gebäudeeinrichtungen (B)
  1. Alle Gebäudeeinrichtungen der TGA inklusive GA MÜSSEN dokumentiert werden.
  2. Hierbei MUSS sämtliche, auch schon vorhandene, Dokumentation zusammengeführt, aus dem Blickwinkel des TGM organisiert und um TGM-spezifische Angaben ergänzt werden.
  3. Der Zugriff auf die Dokumentation MUSS geregelt werden. **◀ ZITIERT**
  4. Die gesamte Dokumentation inklusive der zugehörigen Kontaktinformationen MUSS immer aktuell und verfügbar sein.
- **Satz 3** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 3) Satz 3 fordert die Regelung des Zugriffs auf die Dokumentation der Gebäudeeinrichtungen und deckt damit die geforderte Zugriffsbeschränkung auf dokumentierte Konfigurationen für diesen Bereich ab.

### → ORP.4.A3 — Dokumentation der Benutzendenkennungen und Rechteprofile (B) [IT-Betrieb]
  1. Es MUSS dokumentiert werden, welche Benutzendenkennungen, angelegte Benutzendengruppen und Rechteprofile zugelassen und angelegt wurden.
  2. Die Dokumentation der zugelassenen Benutzendenkennungen, angelegten Benutzendengruppen und Rechteprofile MUSS regelmäßig daraufhin überprüft werden, ob sie den tatsächlichen Stand der Rechtevergabe widerspiegelt.
  3. Dabei MUSS auch geprüft werden, ob die Rechtevergabe noch den Sicherheitsanforderungen und den aktuellen Aufgaben der Benutzenden entspricht.
  4. Die Dokumentation MUSS vor unberechtigtem Zugriff geschützt werden. **◀ ZITIERT**
  5. Sofern sie in elektronischer Form erfolgt, SOLLTE sie in das Datensicherungsverfahren einbezogen werden.
- **Satz 4** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 4) Satz 4 fordert explizit, die Dokumentation vor unberechtigtem Zugriff zu schützen, was sich direkt mit der geforderten Zugriffsbeschränkung auf dokumentierte Konfigurationen aus KONF.1.4 deckt.

### → SYS.1.1.A21 — Betriebsdokumentation für Server (S)
  1. Betriebliche Aufgaben, die an einem Server durchgeführt werden, SOLLTEN nachvollziehbar dokumentiert werden (Wer?, Wann?, Was?).
  2. Aus der Dokumentation SOLLTEN insbesondere Konfigurationsänderungen nachvollziehbar sein.
  3. Sicherheitsrelevante Aufgaben, z. B. wer befugt ist, neue Festplatten einzubauen, SOLLTEN dokumentiert werden.
  4. Alles, was automatisch dokumentiert werden kann, SOLLTE auch automatisch dokumentiert werden.
  5. Die Dokumentation SOLLTE gegen unbefugten Zugriff und Verlust geschützt werden. **◀ ZITIERT**
- **Satz 5** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 5) Satz 5 fordert explizit, die Dokumentation vor unbefugtem Zugriff zu schützen, was der Zielsetzung der Zugriffseinschränkung auf dokumentierte Konfigurationen entspricht.

### → SYS.1.1.A35 — Erstellung und Pflege eines Betriebshandbuchs (S)
  1. Es SOLLTE ein Betriebshandbuch erstellt werden.
  2. Darin SOLLTEN alle erforderlichen Regelungen, Anforderungen und Einstellungen dokumentiert werden, die erforderlich sind, um Server zu betreiben.
  3. Für jede Art von Server SOLLTE es ein spezifisches Betriebshandbuch geben.
  4. Das Betriebshandbuch SOLLTE regelmäßig aktualisiert werden.
  5. Das Betriebshandbuch SOLLTE vor unberechtigtem Zugriff geschützt werden. **◀ ZITIERT**
  6. Das Betriebshandbuch SOLLTE in Notfällen zur Verfügung stehen.
- **Satz 5** | Relation GS++→ED23: `intersects-with` | Fundrichtung: beide
  Begründung: (Teilanforderung 5) Die Maßnahme KONF.1.4 fordert die Zugriffsbeschränkung auf dokumentierte Konfigurationen und deckt damit den geforderten Schutz des Betriebshandbuchs vor unberechtigtem Zugriff inhaltlich ab.

### → SYS.1.8.A2 — Sichere Grundkonfiguration von Speicherlösungen (B)
  1. Bevor eine Speicherlösung produktiv eingesetzt wird, MUSS sichergestellt sein, dass alle eingesetzten Softwarekomponenten und die Firmware aktuell sind.
  2. Danach MUSS eine sichere Grundkonfiguration hergestellt werden.
  3. Nicht genutzte Schnittstellen des Speichersystems MÜSSEN deaktiviert werden.
  4. Die Dateien zur Default-Konfiguration, zur vorgenommenen Grundkonfiguration und zur aktuellen Konfiguration SOLLTEN redundant und geschützt aufbewahrt werden. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) KONF.1.4 fordert den geschützten Umgang bzw. die Zugriffsbeschränkung auf dokumentierte Konfigurationen und deckt damit die geschützte Aufbewahrung von Konfigurationsdateien inhaltlich ab.

