# Review-Dossier Praktik ARCH

Praktik ARCH: 58 Controls mit Mapping, 435 Paare gesamt. Gesampelt: 5 Controls (max/min/median Paarzahl + 2 zufällig).

## ARCH.2.2.8 — Segmentierung von Test und Betrieb  [4 Paare]

**Statement (normativ):** Architektur für Netze SOLLTE Verbindungen zwischen Testumgebungen und Betrieb einschränken.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Entwicklungs-, Staging- und Testumgebungen haben oft geringere Sicherheitsvorkehrungen als Produktivsysteme. Eine saubere Trennung zwischen Test- und Produktivumgebung verhindert Übergriffe auf das Produktivsystem und vermeidet Ressourcenkonflikte.

### → NET.1.1.A22 — Spezifikation des Segmentierungskonzepts (S)
  1. Auf Basis der Spezifikationen von Netzarchitektur und Netzdesign SOLLTE ein umfassendes Segmentierungskonzept für das interne Netz erstellt werden.
  2. Dieses Segmentierungskonzept SOLLTE eventuell vorhandene virtualisierte Netze in Virtualisierungs-Hosts beinhalten.
  3. Das Segmentierunskonzept SOLLTE geplant, umgesetzt, betrieben und nachhaltig gepflegt werden.
  4. Das Konzept SOLLTE mindestens die folgenden Punkte umfassen, soweit diese in der Zielumgebung vorgesehen sind: Initial anzulegende Netzsegmente und Vorgaben dazu, wie neue Netzsegmente zu schaffen sind und wie Endgeräte in den Netzsegmenten zu positionieren sind, Festlegung für die Segmentierung von Entwicklungs- und Testsystemen (Staging), Netzzugangskontrolle für Netzsegmente mit Clients, Anbindung von Netzbereichen, die über Funktechniken oder Standleitung an die Netzsegmente angebunden sind, Anbindung der Virtualisierungs-Hosts und von virtuellen Maschinen auf den Hosts an die Netzsegmente, Rechenzentrumsautomatisierung sowie Festlegungen dazu, wie Endgeräte einzubinden sind, die mehrere Netzsegmente versorgen, z. B. Load Balancer, und Speicher- sowie Datensicherungslösungen. **◀ ZITIERT**
  5. Abhängig von der Sicherheitsrichtlinie und der Anforderungsspezifikation SOLLTE für jedes Netzsegment konzipiert werden, wie es netztechnisch realisiert werden soll.
  6. Darüber hinaus SOLLTE festgelegt werden, welche Sicherheitsfunktionen die Koppelelemente zwischen den Netzsegmenten bereitstellen müssen (z. B. Firewall als zustandsbehafteter Paketfilter oder IDS/IPS).
- **Satz 4** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die G++-Maßnahme deckt als Spezialfall den in Satz 4 explizit geforderten Punkt der Segmentierung von Test- und Entwicklungsumgebungen (Staging) vom Produktivbetrieb ab.

### → OPS.1.1.6.A13 — Trennung der Testumgebung von der Produktivumgebung (S)
  1. Software SOLLTE nur in einer hierfür vorgesehenen Testumgebung getestet werden.
  2. Die Testumgebung SOLLTE von der Produktivumgebung getrennt betrieben werden. **◀ ZITIERT**
  3. Die in der Testumgebung verwendeten Architekturen und Mechanismen SOLLTEN dokumentiert werden.
  4. Es SOLLTEN Verfahren dokumentiert werden, wie mit der Testumgebung nach Abschluss des Software-Tests zu verfahren ist.
- **Satz 2** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) ARCH.2.2.8 fordert die Einschränkung von Verbindungen zwischen Testumgebungen und dem Produktivbetrieb und deckt damit die geforderte Trennung der beiden Umgebungen netzwerkseitig ab.

### → CON.8.A7 — Durchführung von entwicklungsbegleitenden Software-Tests (B) [Testende, Entwickelnde]
  1. Schon bevor die Software im Freigabeprozess getestet und freigegeben wird, MÜSSEN entwicklungsbegleitende Software-Tests durchgeführt und der Quellcode auf Fehler gesichtet werden.
  2. Hierbei SOLLTEN bereits die Fachverantwortlichen des Auftraggebenden oder der beauftragenden Fachabteilung beteiligt werden.
  3. Die entwicklungsbegleitenden Tests MÜSSEN die funktionalen und nichtfunktionalen Anforderungen der Software umfassen.
  4. Die Software-Tests MÜSSEN dabei auch Negativtests abdecken.
  5. Zusätzlich MÜSSEN auch alle kritischen Grenzwerte der Eingabe sowie der Datentypen überprüft werden.
  6. Testdaten SOLLTEN dafür sorgfältig ausgewählt und geschützt werden.
  7. Darüber hinaus SOLLTE eine automatische statische Code-Analyse durchgeführt werden.
  8. Die Software MUSS in einer Test- und Entwicklungsumgebung getestet werden, die getrennt von der Produktionsumgebung ist. **◀ ZITIERT**
  9. Außerdem MUSS getestet werden, ob die Systemvoraussetzungen für die vorgesehene Software ausreichend dimensioniert sind.
- **Satz 8** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 8) ARCH.2.2.8 fordert die netzwerkseitige Trennung und Einschränkung von Verbindungen zwischen Testumgebungen und dem Produktivbetrieb, was die im Satz geforderte Trennung der Umgebungen abdeckt.

### → SYS.1.7.A33 — Trennung von Test- und Produktionssystemen unter z/OS (H)
  1. Es SOLLTEN technische Maßnahmen ergriffen werden, um Entwicklungs- und Testsysteme von Produktionssystemen unter z/OS zu trennen. **◀ ZITIERT**
  2. Dabei SOLLTEN eventuelle Zugriffsmöglichkeiten über gemeinsame Festplatten und den Parallel Sysplex beachtet werden.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) ARCH.2.2.8 fordert allgemein die netztechnische Trennung und Einschränkung von Verbindungen zwischen Test- und Produktionsumgebungen, was die technische Trennung von Entwicklungs- und Testsystemen unter z/OS abdeckt.


## ARCH.5.1 — Einschränkung und Inspektion von Verbindungen  [54 Paare]

**Statement (normativ):** Architektur für Netze SOLLTE Verbindungen zwischen IT-Systemen einschränken.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Über Netverbindungen können unbeabsichtigte Verbindungen aufgebaut werden oder netzbasierte Angriffe über das Internet gegen die Institution erfolgen. Unerwünschter Datenverkehr nach außen können z.B. private IP-Adressen (RFC 1918 leakage), Multicasting, TCP/UDP Ports für veraltete, angreifbare Protokolle oder ICMP-Verkehr sein. Die Beschränkung der Verbindung zwischen IT-Systemen kann sowohl durch zustandsbehaftete Paketfilter, als auch mit Application Layer Gateways umgesetzt werden. Empfehlenswert ist eine Kombination aus Allowlisting, IP-Reputationslisten, Deep Packet Inspection und Durchsatzratenbegrenzung. Hierbei können Verbindungen auch nach Kategorien autorisiert werden (z.B. anhand von IP-Subnetzen oder Voraussetzungen wie per Zertifikat authentifzierten IT-Systemen). Damit dabei keine unnötigen Verbindungen zugelassen werden, ist es wichtig, die Kategorisierung möglich genau zu wählen (z.B. möglichst einzelne Subnetze statt des ganzen Netzes oder nur bestimmte Ports oder Anwendungen zuzulassen).

### → APP.2.1.A11 — Einrichtung des Zugriffs auf Verzeichnisdienste (S)
  1. Der Zugriff auf den Verzeichnisdienst SOLLTE entsprechend der Sicherheitsrichtlinie konfiguriert werden.
  2. Wird der Verzeichnisdienst als Server im Internet eingesetzt, SOLLTE er entsprechend durch ein Sicherheitsgateway geschützt werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) ARCH.5.1 fordert allgemein die Einschränkung und Filterung von Netzwerkverbindungen (u. a. über Paketfilter und Application Layer Gateways), was den Schutz öffentlich erreichbarer Server durch Sicherheitsgateways umfasst.

### → APP.3.1.A11 — Sichere Anbindung von Hintergrundsystemen (S)
  1. Der Zugriff auf Hintergrundsysteme, auf denen Funktionen und Daten ausgelagert werden, SOLLTE ausschließlich über definierte Schnittstellen und von definierten IT-Systemen aus möglich sein. **◀ ZITIERT**
  2. Bei der Kommunikation über Netz- und Standortgrenzen hinweg SOLLTE der Datenverkehr authentisiert und verschlüsselt werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme fordert als allgemeine Regel die Einschränkung von Verbindungen zwischen IT-Systemen auf autorisierte Systeme und Schnittstellen (Allowlisting), was die Beschränkung des Zugriffs auf Hintergrundsysteme inhaltlich abdeckt.

### → APP.4.2.A15 — Sichere Konfiguration des SAP-Routers (S)
  1. Der SAP-Router SOLLTE den Zugang zum Netz regeln und die bestehende Firewall-Architektur zweckmäßig ergänzen. **◀ ZITIERT**
  2. Auch SOLLTE er den Zugang zum SAP-ERP-System kontrollieren. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die allgemeine G++-Maßnahme ARCH.5.1 fordert die netzwerkarchitektonische Einschränkung von Verbindungen zwischen IT-Systemen (u. a. über Application Layer Gateways), was die Funktion des SAP-Routers zur Zugangsregelung und Ergänzung der Firewall abdeckt.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die allgemeine G++-Forderung nach der netzseitigen Einschränkung von Verbindungen zwischen IT-Systemen deckt die Kontrolle des Netzzugangs zum SAP-ERP-System über entsprechende Gateways/Router ab.

### → APP.4.2.A3 — Netzsicherheit (B)
  1. Um die Netzsicherheit zu gewährleisten, MÜSSEN entsprechende Konzepte unter Berücksichtigung des SAP-ERP-Systems erstellt und Einstellungen am System durchgeführt werden.
  2. Weiterhin SOLLTEN der SAP-Router und SAP Web Dispatcher eingesetzt werden, um ein sicheres SAP-Netz zu implementieren und aufrechtzuerhalten. **◀ ZITIERT**
  3. Um Sicherheitslücken aufgrund von Fehlinterpretationen oder Missverständnissen zu vermeiden, MÜSSEN sich die Bereiche IT-Betrieb, Firewall-Betrieb, Portalbetrieb und SAP-Betrieb miteinander abstimmen.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die allgemeine G++-Forderung zur Einschränkung von Verbindungen zwischen IT-Systemen (u. a. mittels Application Layer Gateways) deckt den Einsatz von SAP-Router und SAP Web Dispatcher als technologiespezifische Ausprägung zur Netz- und Verbindungssicherheit inhaltlich ab.

### → APP.4.4.A18 — Verwendung von Mikro-Segmentierung (H)
  1. Die Pods SOLLTEN auch innerhalb eines Kubernetes-Namespace nur über die notwendigen Netzports miteinander kommunizieren können. **◀ ZITIERT**
  2. Es SOLLTEN Regeln innerhalb des CNI existieren, die alle bis auf die für den Betrieb notwendigen Netzverbindungen innerhalb des Kubernetes-Namespace unterbinden.
  3. Diese Regeln SOLLTEN Quelle und Ziel der Verbindungen genau definieren und dafür mindestens eines der folgenden Kriterien nutzen: Service-Name, Metadaten („Labels"), die Kubernetes Service Accounts oder zertifikatsbasierte Authentifizierung.
  4. Alle Kriterien, die als Bezeichnung für diese Verbindung dienen, SOLLTEN so abgesichert sein, dass sie nur von berechtigten Personen und Verwaltungs-Diensten verändert werden können.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) ARCH.5.1 fordert die allgemeine netzwerkseitige Einschränkung von Verbindungen zwischen IT-Systemen auf notwendige Ports und Dienste, was die Port-Einschränkung der Kommunikation zwischen Pods abdeckt.

### → APP.4.4.A7 — Separierung der Netze bei Kubernetes (S)
  1. Die Netze für die Administration der Nodes, der Control Plane sowie die einzelnen Netze der Anwendungsdienste SOLLTEN separiert werden.
  2. Es SOLLTEN NUR die für den Betrieb notwendigen Netzports der Pods in die dafür vorgesehenen Netze freigegeben werden. **◀ ZITIERT**
  3. Bei mehreren Anwendungen auf einem Kubernetes-Cluster SOLLTEN zunächst alle Netzverbindungen zwischen den Kubernetes-Namespaces untersagt und nur benötigte Netzverbindungen gestattet sein (Whitelisting).
  4. Die zur Administration der Nodes, der Runtime und von Kubernetes inklusive seiner Erweiterungen notwendigen Netzports SOLLTEN NUR aus dem Administrationsnetz und von Pods, die diese benötigen, erreichbar sein.
  5. Nur ausgewählte Administrierende SOLLTEN in Kubernetes berechtigt sein, das CNI zu verwalten und Regeln für das Netz anzulegen oder zu ändern.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) ARCH.5.1 fordert die generelle Beschränkung von Netzwerkverbindungen auf das notwendige Maß (u. a. per Port- und Allowlisting), was die gezielte Freigabe nur betriebsnotwendiger Netzports für Pods abstrahierend abdeckt.

### → IND.1.A16 — Stärkere Abschottung der Zonen (H)
  1. Bei hoch schutzbedürftigen oder schlecht absicherbaren ICS-Umgebungen SOLLTEN vorbeugend Schnittstellensysteme mit Sicherheitsprüffunktionen eingesetzt werden. **◀ ZITIERT**
  2. Durch Realisierung einer oder mehrerer Anbindungszonen (DMZ) in P-A-P-Struktur SOLLTEN durchgängige Außenverbindungen terminiert werden.
  3. Erforderliche Sicherheitsprüfungen SOLLTEN so erfolgen, dass die ICS-Anlage nicht angepasst werden muss.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) ARCH.5.1 deckt den Einsatz von Schnittstellensystemen mit Sicherheitsprüffunktionen ab, indem es die allgemeine Beschränkung und Inspektion von Verbindungen zwischen Systemen (u. a. via Application Layer Gateways und DPI) fordert.

### → IND.2.1.A6 — Netzsegmentierung (B) [OT-Betrieb (Operational Technology, OT), Planende]
  1. ICS-Komponenten MÜSSEN von der Office-IT getrennt werden.
  2. Hängen ICS-Komponenten von anderen Diensten im Netz ab, SOLLTE das ausreichend dokumentiert werden.
  3. ICS-Komponenten SOLLTEN so wenig wie möglich mit anderen ICS-Komponenten kommunizieren. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) ARCH.5.1 fordert allgemein die Einschränkung von Verbindungen zwischen IT-Systemen, was das Prinzip der Minimierung der Kommunikation zwischen ICS-Komponenten inhaltlich abdeckt.

### → INF.11.A17 — Netztrennung des In-Vehicle-Network mit einem Sonderfahrzeugnetz über Gateways (H)
  1. Generell SOLLTE die Institution sicherstellen, dass keine Informationen unerlaubt und undefiniert zwischen dem In-Vehicle-Network (IVN), das wiederum an die Netze der fahrzeugherstellenden Unternehmen angebunden ist und den einsatzspezifischen IT-Komponenten ausgetauscht werden. **◀ ZITIERT**
  2. Hierzu SOLLTEN Gateways mit standardisierten Protokollen (z. B. nach Standard CiA 447) eingesetzt werden.
  3. Die Gateways SOLLTEN dabei vom fahrzeugherstellenden Unternehmen freigegeben sein.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme ARCH.5.1 deckt die Forderung als allgemeines Prinzip ab, indem sie verlangt, Verbindungen zwischen IT-Systemen einzuschränken, um unerwünschten oder unautorisierten Datenverkehr zu unterbinden.

### → INF.13.A13 — Sichere Anbindung von eingeschränkt vertrauenswürdigen Systemen im TGM (S) [Planende]
  1. Eingeschränkt vertrauenswürdige Systeme, die aus wichtigen betrieblichen Gründen im TGM eingebunden werden müssen, SOLLTEN über ein System angebunden werden, das die Kommunikation mit Hilfe von Firewall-Funktionen kontrolliert und reglementiert. **◀ ZITIERT**
  2. Dieses System SOLLTE in der Verantwortlichkeit des TGM liegen.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die Maßnahme ARCH.5.1 fordert die generelle Einschränkung und Kontrolle von Verbindungen zwischen IT-Systemen mittels Firewall- und Filterfunktionen, was die kontrollierte Anbindung von Systemen im TGM abdeckt.

### → INF.14.A11 — Absicherung von frei zugänglichen Ports und Zugängen der GA (S) [Planende]
  1. Der Anschluss von Komponenten, speziell von unautorisierten, unbekannten Komponenten und Fremdgeräten, SOLLTE insbesondere an frei zugänglichen Ethernet-Ports, USB-Ports und anderen Schnittstellen der GA kontrolliert und eingeschränkt werden.
  2. Der Anschluss einer unautorisierten oder unbekannten Komponente SOLLTE in die Ereignisprotokollierung aufgenommen werden.
  3. Eine direkte IP-basierte Kommunikation von solchen Komponenten mit Systemen der GA SOLLTE unterbunden werden (siehe INF.14.A13 Netzsegementierung in der GA). **◀ ZITIERT**
  4. Für frei zugängliche LAN- oder WLAN-Zugänge SOLLTE eine Netzzugangskontrolle gemäß IEEE 802.1X oder vergleichbare Sicherheitsmechanismen eingesetzt werden.
  5. Hiermit SOLLTEN unzureichend authentisierte und autorisierte Komponenten in getrennten Netzsegmenten positioniert werden.
  6. Frei zugängliche Schnittstellen für temporäre Wartungszwecke, wie beispielsweise USB-Ports an GA-Komponenten, SOLLTEN nur bei Bedarf aktiviert werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die Maßnahme ARCH.5.1 fordert die generelle netzwerkbasierte Einschränkung von Verbindungen zwischen IT-Systemen (z. B. mittels Paketfiltern oder Allowlisting), was das Unterbinden direkter IP-basierter Kommunikation mit GA-Systemen abdeckt.

### → INF.14.A13 — Netzsegmentierung in der GA (S) [Planende]
  1. Innerhalb des GA-Netzes SOLLTE eine Netzsegmentierung umgesetzt werden, die bedarfsgerecht einzelne GA-Systeme, einzelne TGA-Anlagen oder einzelne Gruppen von TGA-Anlagen innerhalb eines GA-Systems voneinander trennt.
  2. Für die Übergänge zwischen den Segmenten SOLLTEN entsprechende Regeln definiert und zur Umsetzung Komponenten mit Sicherheitsfunktionen, mindestens zustandsbehaftete Paketfilter, genutzt werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) G++ ARCH.5.1 fordert die Einschränkung von Verbindungen zwischen Systemen, was laut Erläuterung die regelbasierte Filterung von Übergängen mittels zustandsbehafteter Paketfilter einschließt.

### → INF.14.A15 — Absicherung von GA-spezifischen Netzen (S)
  1. Sind in GA-spezifischen Netzen wie z. B. BACnet Sicherheitsmechanismen der Kommunikation verfügbar, SOLLTEN diese genutzt werden.
  2. Mindestens SOLLTEN Mechanismen zur Authentisierung und Verschlüsselung genutzt werden.
  3. Für GA-spezifische Netze, die keine angemessenen Sicherheitsmechanismen realisieren können, SOLLTE erwogen werden, diese auf ein GA-spezifisches Netz mit angemessenen Sicherheitsmechanismen umzustellen.
  4. Grundsätzlich SOLLTE die Kommunikation mit GA-spezifischen Netzen durch Koppelelemente mit Sicherheitsfunktionen kontrolliert und gegebenenfalls reglementiert werden. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die Maßnahme ARCH.5.1 fordert die allgemeine Einschränkung und Reglementierung von Verbindungen zwischen Netzen und IT-Systemen mittels zustandsbehafteter Paketfilter oder Gateways, was die geforderte Kontrolle durch Koppelelemente inhaltlich abdeckt.

### → INF.14.A16 — Absicherung von drahtloser Kommunikation in GA-Netzen (S) [Planende]
  1. In GA-Netzen, die auf einer drahtlosen Kommunikation wie z. B. EnOcean basieren, SOLLTEN die Sicherheitsmechanismen der jeweiligen Funktechnik zur Absicherung der Kommunikation genutzt werden.
  2. Insbesondere SOLLTEN eine angemessene Authentisierung und eine Verschlüsselung auf der Luftschnittstelle umgesetzt werden.
  3. Ist dies für die entsprechenden Endgeräte nicht möglich, SOLLTE für diese Endgeräte die Kommunikation am Übergang in kabelgebundene Netze kontrolliert werden, z. B. durch eine Komponente mit Firewall-Funktion. **◀ ZITIERT**
  4. Darüber hinaus SOLLTEN mögliche Störungen für die Ausbreitung der Funkwellen, beispielsweise durch Abschattungen, bei der Planung der GA-Netze berücksichtigt werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die allgemeine Anforderung in ARCH.5.1 zur Einschränkung und Filterung von Verbindungen zwischen Systemen mittels Paketfiltern oder Firewalls deckt die geforderte Kontrolle des Datenverkehrs am Netzübergang inhaltlich ab.

### → INF.14.A17 — Absicherung von Mobilfunkkommunikation in GA-Netzen (S) [Planende]
  1. Wird im Rahmen der GA Mobilfunk eingesetzt, SOLLTEN für solche GA-Netze die Sicherheitsmechanismen der jeweiligen Mobilfunknetze genutzt werden.
  2. Werden öffentliche Mobilfunknetze wie 5G oder Sigfox in der GA verwendet, SOLLTE eine unkontrollierte direkte IP-basierte Kommunikation mit GA-relevanten Komponenten unterbunden werden.
  3. GA-Komponenten SOLLTEN nur dann mit einem dedizierten Anschluss an ein öffentliches Mobilfunknetz ausgestattet werden, falls dieser für deren Betrieb essenziell ist.
  4. Hierfür SOLLTE geprüft und festgelegt werden, für welche GA-Komponenten ein Anschluss an öffentliche Mobilfunknetze notwendig ist.
  5. Sofern im öffentlichen Mobilfunknetz keine Trennung der GA-Netze möglich ist, wie z. B. bei 5G mit Slicing, SOLLTE im Kommunikationspfad eine Entkopplung der IP-Kommunikation durch ein Application Layer Gateway (ALG) stattfinden.
  6. Falls Mobilfunktechniken in der GA als Bestandteil der öffentlichen Mobilfunkinfrastruktur eines Mobilfunkunternehmens eingesetzt werden, SOLLTEN mit den Mitteln der entsprechenden Mobilfunktechnik ein oder mehrere virtuelle Mobilfunknetze realisiert werden, die ausschließlich der GA zur Verfügung stehen.
  7. Falls in der GA mit Hilfe von Mobilfunktechniken wie LTE und 5G autarke private Mobilfunknetze lokal auf dem Campus eingerichtet werden, SOLLTE der Übergang zwischen diesen Mobilfunknetzen und den sonstigen Netzen durch ein Koppelelement mit Firewall-Funktion abgesichert werden. **◀ ZITIERT**
  8. Auch für private Mobilfunknetze SOLLTE eine Segmentierung in mehrere virtuelle Mobilfunknetze umgesetzt werden.
- **Satz 7** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 7) Die G++-Maßnahme ARCH.5.1 deckt die Forderung als übergeordnete Anforderung zur Einschränkung von Netzverbindungen mittels Paketfiltern und Firewalls an Netzübergängen ab.

### → INF.14.A18 — Sichere Anbindung von GA-externen Systemen (S)
  1. Die Kommunikation von GA-Systemen mit GA-externen Systemen SOLLTE ausschließlich über definierte Schnittstellen und mit definierten IT-Systemen möglich sein.
  2. Die Kommunikation SOLLTE authentisiert und verschlüsselt werden.
  3. Die möglichen Schnittstellen zu GA-externen Systemen SOLLTEN auf das notwendige Maß beschränkt werden. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme ARCH.5.1 fordert allgemein die Einschränkung von Verbindungen zwischen IT-Systemen auf das notwendige Maß, was die Beschränkung möglicher Schnittstellen zu externen Systemen inhaltlich abdeckt.

### → INF.14.A19 — Nutzung dedizierter Adressbereiche für GA-Netze (S) [Planende]
  1. Für die GA SOLLTEN dedizierte Adressbereiche genutzt werden, die sich insbesondere von den Adressbereichen der Büro-IT und der OT unterscheiden.
  2. Für diese Adressbereiche SOLLTE festgelegt werden, aus welchen Bereichen statische Adressen vergeben werden und welche GA-relevanten Komponenten statische Adressen erhalten.
  3. Falls an die GA angebundene Netzbereiche wie TGA-Anlagen identische Adressbereiche nutzen (Replizieren von Anlagenkonfigurationen), MÜSSEN diese in getrennten Segmenten positioniert werden, um Adresskonflikte zu unterbinden.
  4. In diesem Fall MUSS die segmentübergreifende Kommunikation durch entsprechende Mechanismen abgesichert werden, beispielsweise durch den Einsatz eines ALG oder von Network Address Translation (NAT). **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) ARCH.5.1 fordert die allgemeine Einschränkung und Absicherung von Netzwerkverbindungen zwischen Systemen und benennt dazu unter anderem Application Layer Gateways (ALG) als geeigneten Kontrollmechanismus.

### → INF.14.A28 — Physische Trennung der GA (H) [Planende]
  1. Bei erhöhtem Schutzbedarf SOLLTEN GA-Netze als physisch getrennte Zonen gemäß Baustein NET.1.1 Netzarchitektur und -design realisiert werden.
  2. Abhängig vom Schutzbedarf SOLLTE für die Anbindung beispielsweise an externe Clouds ein dedizierter, restriktiv reglementierter Internet-Zugang bereitgestellt werden.
  3. Ebenfalls SOLLTEN, abhängig vom Schutzbedarf der GA-Systeme, Anbindungen an nicht vertrauenswürdige Netze, gegebenenfalls auch Anbindungen an institutionseigene Büro- oder OT-Netze, unterbunden werden. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) ARCH.5.1 verlangt als allgemeines Prinzip die netzseitige Einschränkung und das Unterbinden von Verbindungen zwischen IT-Systemen und deckt damit das Unterbinden von Anbindungen an nicht vertrauenswürdige oder andere interne Netze ab.

### → INF.14.A29 — Trennung einzelner TGA-Anlagen (H)
  1. Um einzelne TGA-Anlagen mit erhöhtem Schutzbedarf innerhalb eines GA-Systems abzusichern, SOLLTEN solche TGA-Anlagen in separaten Netzsegmenten positioniert werden.
  2. Zur Kontrolle der Kommunikation SOLLTEN Firewall-Funktionen unmittelbar vor dem Anlagennetz positioniert werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) ARCH.5.1 verlangt allgemein die Einschränkung und Kontrolle von Verbindungen zwischen Netzen und IT-Systemen mittels Paketfiltern und Firewalls.

### → INF.14.A6 — Separierung von Netzen der GA (B) [Planende, IT-Betrieb]
  1. GA-Netze MÜSSEN von Büro-Netzen und sonstigen Netzen der Institution mindestens logisch getrennt werden.
  2. Jegliche Kommunikation zwischen GA-Systemen und sonstigen IT-Systemen MUSS kontrolliert und reglementiert werden. **◀ ZITIERT**
  3. Hierfür MÜSSEN an allen Übergängen einer solchen Segmentierung entsprechende Komponenten mit Sicherheitsfunktionen, mindestens mit Firewall-Funktion, vorgesehen werden. **◀ ZITIERT**
  4. Wird die GA für einen Gebäudekomplex oder eine Liegenschaft zentral eingerichtet, so MUSS die gebäudeübergreifende GA-Kommunikation über LAN-, WLAN-, WAN-, Funknetz- oder Internet-Verbindungen auch auf Ebene des Netzes separiert werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) ARCH.5.1 fordert die allgemeine Einschränkung und Reglementierung von Verbindungen zwischen IT-Systemen mittels Paketfiltern und Gateways, was die Kontrolle des Kommunikationsverkehrs zwischen GA- und sonstigen Systemen abdeckt.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) ARCH.5.1 fordert die netzwerkseitige Einschränkung von Verbindungen zwischen IT-Systemen mittels Filter- und Firewall-Komponenten und deckt damit die Bereitstellung entsprechender Sicherheitsfunktionen an Netzübergängen ab.

### → NET.1.1.A19 — Separierung der Infrastrukturdienste (S)
  1. Server, die grundlegende Dienste für die IT-Infrastruktur bereitstellen, SOLLTEN in einem dedizierten Netzsegment positioniert werden.
  2. Die Kommunikation mit ihnen SOLLTE durch einen zustandsbehafteten Paketfilter (Firewall) kontrolliert werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) G++ ARCH.5.1 fordert die generelle Einschränkung von Verbindungen zwischen IT-Systemen, was die geforderte Kontrolle der Kommunikation mittels zustandsbehafteter Paketfilterung inhaltlich umfasst.

### → NET.1.1.A4 — Netztrennung in Zonen (B)
  1. Das Gesamtnetz MUSS mindestens in folgende drei Zonen physisch separiert sein: internes Netz, demilitarisierte Zone (DMZ) und Außenanbindungen (inklusive Internetanbindung sowie Anbindung an andere nicht vertrauenswürdige Netze).
  2. Die Zonenübergänge MÜSSEN durch eine Firewall abgesichert werden. **◀ ZITIERT**
  3. Diese Kontrolle MUSS dem Prinzip der lokalen Kommunikation folgen, sodass von Firewalls ausschließlich erlaubte Kommunikation weitergeleitet wird (Allowlist). **◀ ZITIERT**
  4. Nicht vertrauenswürdige Netze (z. B. Internet) und vertrauenswürdige Netze (z. B. Intranet) MÜSSEN mindestens durch eine zweistufige Firewall-Struktur, bestehend aus zustandsbehafteten Paketfiltern (Firewall), getrennt werden.
  5. Um Internet und externe DMZ netztechnisch zu trennen, MUSS mindestens ein zustandsbehafteter Paketfilter eingesetzt werden. **◀ ZITIERT**
  6. In der zweistufigen Firewall-Architektur MUSS jeder ein- und ausgehende Datenverkehr durch den äußeren Paketfilter bzw. den internen Paketfilter kontrolliert und gefiltert werden.
  7. Eine P-A-P-Struktur, die aus Paketfilter, Application-Layer-Gateway bzw. Sicherheits-Proxies und Paketfilter besteht, MUSS immer realisiert werden, wenn die Sicherheitsrichtlinie oder die Anforderungsspezifikation dies fordern.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) ARCH.5.1 verlangt als allgemeine Grundforderung die Einschränkung von Netzverbindungen (u. a. mittels Firewall- und Paketfiltertechnologie), was die Absicherung von Zonenübergängen durch Firewalls inhaltlich abdeckt.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 3) Satz 3 fordert die Beschränkung des Datenverkehrs durch Firewalls auf ausschließlich erlaubte Kommunikation (Allowlist), was der geforderten Einschränkung von Verbindungen in ARCH.5.1 entspricht.
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) ARCH.5.1 fordert als übergeordnete Anforderung die Einschränkung von Netzverbindungen, was den Einsatz von zustandsbehafteten Paketfiltern zur Trennung von externem Datenverkehr (Internet/DMZ) materiell abdeckt.

### → NET.1.1.A5 — Client-Server-Segmentierung (B)
  1. Clients und Server MÜSSEN in unterschiedlichen Netzsegmenten platziert werden.
  2. Die Kommunikation zwischen diesen Netzsegmenten MUSS mindestens durch einen zustandsbehafteten Paketfilter kontrolliert werden. **◀ ZITIERT**
  3. Es SOLLTE beachtet werden, dass mögliche Ausnahmen, die es erlauben, Clients und Server in einem gemeinsamen Netzsegment zu positionieren, in den entsprechenden anwendungs- und systemspezifischen Bausteinen geregelt werden.
  4. Für Gastzugänge und für Netzbereiche, in denen keine ausreichende interne Kontrolle über die Endgeräte gegeben ist, MÜSSEN dedizierte Netzsegmente eingerichtet werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) ARCH.5.1 fordert allgemein die Einschränkung von Verbindungen zwischen IT-Systemen in Netzarchitekturen, was explizit die Kontrolle des Datenverkehrs mittels zustandsbehafteter Paketfilter umfasst.

### → NET.1.1.A8 — Grundlegende Absicherung des Internetzugangs (B)
  1. Der Internetverkehr MUSS über die Firewall-Struktur geführt werden (siehe NET.1.1.A4 Netztrennung in Zonen).
  2. Die Datenflüsse MÜSSEN durch die Firewall-Struktur auf die benötigten Protokolle und Kommunikationsbeziehungen eingeschränkt werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) ARCH.5.1 fordert die generelle Einschränkung von Verbindungen zwischen IT-Systemen (u. a. per Paketfilter auf benötigte Ports, Protokolle und Kommunikationsbeziehungen) und deckt den Satz damit direkt ab.

### → NET.2.1.A16 — Zusätzliche Absicherung bei der Anbindung von WLANs an ein LAN (H)
  1. Wird eine WLAN-Infrastruktur an ein LAN angebunden, SOLLTE der Übergang zwischen WLANs und LAN entsprechend des höheren Schutzbedarfs zusätzlich abgesichert werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) ARCH.5.1 fordert die generelle Einschränkung von Verbindungen zwischen Netzen bzw. IT-Systemen (z. B. mittels Paketfiltern oder Gateways), was die zusätzliche Absicherung von Netzübergängen wie zwischen WLAN und LAN abdeckt.

### → NET.2.1.A9 — Sichere Anbindung von WLANs an ein LAN (S) [Planende]
  1. Werden WLANs an ein LAN angebunden, SOLLTE der Übergang zwischen WLANs und LAN abgesichert werden, beispielsweise durch einen Paketfilter. **◀ ZITIERT**
  2. Der Access Point SOLLTE unter Berücksichtigung der Anforderung NET.2.1.A7 Aufbau eines Distribution Systems eingebunden sein.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) ARCH.5.1 fordert allgemein die Einschränkung und Filterung von Netzverbindungen (z. B. durch Paketfilter), was die Absicherung des Netzübergangs zwischen WLAN und LAN inhaltlich abdeckt.

### → NET.3.1.A14 — Schutz vor Missbrauch von ICMP-Nachrichten (S)
  1. Die Protokolle ICMP und ICMPv6 SOLLTEN restriktiv gefiltert werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) ARCH.5.1 fordert die allgemeine Einschränkung und Filterung von Netzverbindungen zwischen IT-Systemen, was laut Erläuterung explizit die Filterung von ICMP-Verkehr umfasst.

### → NET.3.1.A15 — Bogon- und Spoofing-Filterung (S)
  1. Es SOLLTE verhindert werden, dass Angreifende mithilfe gefälschter, reservierter oder noch nicht zugewiesener IP-Adressen in die Router und Switches eindringen können. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) ARCH.5.1 fordert als übergeordnete Maßnahme die Einschränkung von Netzverbindungen mittels Paketfilterung und Adressbeschränkungen, was die Filterung von gefälschten und reservierten IP-Adressen umfasst.

### → NET.3.2.A18 — Administration über ein gesondertes Managementnetz (S)
  1. Firewalls SOLLTEN ausschließlich über ein separates Managementnetz (Out-of-Band-Management) administriert werden.
  2. Eine eventuell vorhandene Administrationsschnittstelle über das eigentliche Datennetz (In-Band) SOLLTE deaktiviert werden.
  3. Die Kommunikation im Managementnetz SOLLTE über Management-Firewalls (siehe NET.1.1 Netz-Architektur und -design) auf wenige Managementprotokolle mit genau festgelegten Ursprüngen und Zielen beschränkt werden. **◀ ZITIERT**
  4. Die verfügbaren Sicherheitsmechanismen der eingesetzten Managementprotokolle zur Authentisierung, Integritätssicherung und Verschlüsselung SOLLTEN aktiviert sein.
  5. Alle unsicheren Managementprotokolle SOLLTEN deaktiviert werden (siehe NET.1.2 Netzmanagement).
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) ARCH.5.1 fordert allgemein die Einschränkung von Verbindungen zwischen IT-Systemen mittels Filterung nach Ursprung, Ziel und Protokollen, was die Beschränkung der Kommunikation im Managementnetz abdeckt.

### → NET.3.2.A2 — Festlegen der Firewall-Regeln (B)
  1. Die gesamte Kommunikation zwischen den beteiligten Netzen MUSS über die Firewall geleitet werden.
  2. Es MUSS sichergestellt sein, dass von außen keine unerlaubten Verbindungen in das geschützte Netz aufgebaut werden können. **◀ ZITIERT**
  3. Ebenso DÜRFEN KEINE unerlaubten Verbindungen aus dem geschützten Netz heraus aufgebaut werden. **◀ ZITIERT**
  4. Für die Firewall MÜSSEN eindeutige Regeln definiert werden, die festlegen, welche Kommunikationsverbindungen und Datenströme zugelassen werden.
  5. Alle anderen Verbindungen MÜSSEN durch die Firewall unterbunden werden (Allowlist-Ansatz). **◀ ZITIERT**
  6. Die Kommunikationsbeziehungen mit angeschlossenen Dienst-Servern, die über die Firewall geführt werden, MÜSSEN in den Regeln berücksichtigt sein.
  7. Es MÜSSEN Zuständige benannt werden, die Filterregeln entwerfen, umsetzen und testen.
  8. Zudem MUSS geklärt werden, wer Filterregeln verändern darf.
  9. Die getroffenen Entscheidungen sowie die relevanten Informationen und Entscheidungsgründe MÜSSEN dokumentiert werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) ARCH.5.1 fordert die Einschränkung von Verbindungen zwischen IT-Systemen, was das Verhindern unerlaubter Verbindungen von außen in das interne Netz (z. B. mittels Paketfiltern und Allowlisting) abdeckt.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) ARCH.5.1 fordert die generelle Einschränkung von Verbindungen zwischen IT-Systemen und thematisiert explizit die Unterbindung unerwünschten Datenverkehrs nach außen.
- **Satz 5** | Relation GS++→ED23: `intersects-with` | Fundrichtung: beide
  Begründung: (Teilanforderung 5) Satz 5 fordert das Unterbinden aller nicht explizit erlaubten Verbindungen mittels Allowlist-Ansatz an der Firewall, was der Einschränkung von Verbindungen aus ARCH.5.1 entspricht.

### → NET.3.2.A3 — Einrichten geeigneter Filterregeln am Paketfilter (B)
  1. Basierend auf den Firewall-Regeln aus NET.3.2.A2 Festlegen der Firewall-Regeln MÜSSEN geeignete Filterregeln für den Paketfilter definiert und eingerichtet werden. **◀ ZITIERT**
  2. Ein Paketfilter MUSS so eingestellt sein, dass er alle ungültigen TCP-Flag-Kombinationen verwirft.
  3. Grundsätzlich MUSS immer zustandsbehaftet gefiltert werden.
  4. Auch für die verbindungslosen Protokolle UDP und ICMP MÜSSEN zustandsbehaftete Filterregeln konfiguriert werden.
  5. Die Firewall MUSS die Protokolle ICMP und ICMPv6 restriktiv filtern.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) Satz 1 fordert die Definition und Einrichtung von Filterregeln am Paketfilter zur Beschränkung des Netzverkehrs, was direkt der Kernforderung von ARCH.5.1 entspricht.

### → NET.3.3.A11 — Sichere Anbindung eines externen Netzes (S)
  1. Es SOLLTE sichergestellt werden, dass VPN-Verbindungen NUR zwischen den dafür vorgesehenen IT-Systemen und Diensten aufgebaut werden. **◀ ZITIERT**
  2. Die dabei eingesetzten Tunnel-Protokolle SOLLTEN für den Einsatz geeignet sein.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) ARCH.5.1 fordert die Einschränkung von Verbindungen zwischen IT-Systemen auf autorisierte Systeme und Dienste mittels Filterung und Allowlisting, was die Beschränkung von VPN-Verbindungen auf vorgesehene Endpunkte und Dienste abdeckt.

### → NET.3.4.A14 — Umsetzung weiterer Maßnahmen bei Verwendung von MAC-Adress-Authentisierung (S)
  1. Endgeräte, die nicht über eine sichere EAP-Methode authentisiert werden können und anhand ihrer MAC-Adresse identifiziert werden, SOLLTEN NICHT als vertrauenswürdige Endgeräte eingestuft werden.
  2. Der Netzzugang SOLLTE auf das notwendige Minimum beschränkt werden. **◀ ZITIERT**
  3. Hierfür SOLLTEN weitere Maßnahmen wie Nutzung von Kommunikationsbeschränkungen oder nachgelagertes Endgeräte-Profiling der Endgeräte-Aktivitäten umgesetzt werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) ARCH.5.1 fordert als allgemeinere Maßnahme die verbindliche Einschränkung von Verbindungen zwischen IT-Systemen im Netz auf das notwendige Maß.
- **Satz 3** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme ARCH.5.1 fordert allgemein die Einschränkung von Verbindungen zwischen IT-Systemen und deckt damit die im Satz geforderten Kommunikationsbeschränkungen ab.

### → NET.3.4.A17 — Positionierung des RADIUS-Servers im Management-Bereich (S)
  1. Der RADIUS-Server SOLLTE in einem geschützten Netzsegment innerhalb des Management-Bereichs (siehe NET.1.1 Netzarchitektur und -design) positioniert werden.
  2. Kommunikationsanfragen an den RADIUS-Server SOLLTEN nur von vertrauenswürdigen Quellen zugelassen werden. **◀ ZITIERT**
  3. Diese SOLLTEN auf ein Minimum eingeschränkt werden. **◀ ZITIERT**
  4. Der RADIUS-Server SOLLTE NICHT direkt mit Endgeräten kommunizieren, sondern ausschließlich über den Authenticator auf den Access-Switches.
  5. Anfragen der Access-Switches SOLLTEN nur aus dem gemeinsamen Management-Netzsegment akzeptiert werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme ARCH.5.1 fordert allgemein die Einschränkung von Verbindungen zwischen IT-Systemen (u. a. per Allowlisting und Subnetzbeschränkung), was die Beschränkung von Anfragen an den RADIUS-Server auf vertrauenswürdige Quellen als Spezialfall abdeckt.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) ARCH.5.1 fordert die allgemeine Einschränkung von Verbindungen zwischen IT-Systemen, was das geforderte Minimieren von Kommunikationsanfragen netzwerkseitig abdeckt.
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) ARCH.5.1 fordert die generelle netzbasierte Einschränkung von Verbindungen zwischen IT-Systemen (z. B. anhand von Subnetzen), was die segmentbasierte Einschränkung von Anfragen der Access-Switches an den RADIUS-Server abdeckt.

### → NET.4.2.A16 — Trennung des Daten- und VoIP-Netzes (H)
  1. Das VoIP-Netz SOLLTE in geeigneter Weise vom Datennetz getrennt werden.
  2. Es SOLLTE geregelt werden, wie mit Geräten umzugehen ist, die auf das VoIP- und Datennetz zugreifen müssen.
  3. VoIP-Endgeräte in einem VoIP-Netz SOLLTEN NUR die vorgesehenen VoIP-Verbindungen zu anderen IT-Systemen aufbauen können. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme ARCH.5.1 fordert allgemeingültig die Einschränkung von Netzwerkverbindungen zwischen IT-Systemen (z. B. per Allowlisting), was die Beschränkung von VoIP-Endgeräten auf vorgesehene Verbindungen inhaltlich abdeckt.

### → OPS.1.1.7.A17 — Kontrolle der Systemmanagement-Kommunikation (S)
  1. Die Kommunikation zwischen den Benutzenden und der Systemmanagement-Lösung sowie zwischen der Systemmanagement-Lösung und den zu verwaltenden IT-Systemen SOLLTE über geeignete Filtertechniken auf unbedingt notwendige Verbindungen eingeschränkt werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) ARCH.5.1 fordert die generelle netzwerkbasierte Einschränkung von Verbindungen zwischen IT-Systemen mittels Filtertechniken und deckt damit die anforderungsspezifische Filterung der Systemmanagement-Kommunikation ab.

### → OPS.1.2.5.A14 — Dedizierte Clients und Konten bei der Fernwartung (H)
  1. Zur Fernwartung SOLLTEN IT-Systeme eingesetzt werden, die ausschließlich zur Administration von anderen IT-Systemen dienen.
  2. Alle weiteren Funktionen auf diesen IT-Systemen SOLLTEN deaktiviert werden.
  3. Die Netzkommunikation der Administrationssysteme SOLLTE so eingeschränkt werden, dass nur Verbindungen zu IT-Systemen möglich sind, die administriert werden sollen. **◀ ZITIERT**
  4. Für Fernwartungszugänge SOLLTEN dedizierte Konten verwendet werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) ARCH.5.1 fordert als allgemeinere Maßnahme die netzseitige Einschränkung von Verbindungen zwischen IT-Systemen mittels Filterung und Allowlisting, was die Beschränkung der Netzkommunikation von Administrationssystemen auf die zu verwaltenden Zielsysteme abdeckt.

### → SYS.1.5.A4 — Sichere Konfiguration eines Netzes für virtuelle Infrastrukturen (B)
  1. Es MUSS sichergestellt werden, dass bestehende Sicherheitsmechanismen (z. B. Firewalls) und Monitoring-Systeme nicht über virtuelle Netze umgangen werden können.
  2. Auch MUSS ausgeschlossen sein, dass über virtuelle IT-Systeme, die mit mehreren Netzen verbunden sind, unerwünschte Netzverbindungen aufgebaut werden können.
  3. Netzverbindungen zwischen virtuellen IT-Systemen und physischen IT-Systemen sowie für virtuelle Firewalls SOLLTEN gemäß den Sicherheitsrichtlinien der Institution konfiguriert werden. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) ARCH.5.1 fordert die generelle Einschränkung von Verbindungen zwischen IT-Systemen in der Netzarchitektur und deckt damit die richtlinienkonforme Konfiguration von Verbindungen zwischen virtuellen und physischen Systemen sowie Firewalls ab.

### → SYS.1.6.A5 — Separierung der Administrations- und Zugangsnetze bei Containern (B)
  1. Die Netze für die Administration des Hosts, die Administration der Container und deren Zugangsnetze MÜSSEN dem Schutzbedarf angemessen separiert werden.
  2. Grundsätzlich SOLLTE mindestens die Administration des Hosts nur aus dem Administrationsnetz möglich sein.
  3. Es SOLLTEN nur die für den Betrieb notwendigen Kommunikationsbeziehungen erlaubt werden. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) ARCH.5.1 fordert die generelle Einschränkung von Netzverbindungen zwischen IT-Systemen (insbesondere über Allowlisting), was die Erlaubnis ausschließlich betriebsnotwendiger Kommunikationsbeziehungen direkt abdeckt.

### → SYS.1.9.A7 — Sicherer Zugriff auf den Terminalserver (B)
  1. Es MUSS festgelegt werden, über welche Netze zwischen zugreifendem Client und Terminalserver kommuniziert werden darf. **◀ ZITIERT**
  2. Zusätzlich MUSS festgelegt werden, wie die Kommunikation abgesichert werden soll.
  3. Es MUSS festgelegt werden, ob und wie mit dem Terminalserver-Protokoll verschlüsselt werden soll.
  4. Falls das Terminalserver-Protokoll in diesem Fall keine ausreichende Verschlüsselung bietet, MUSS die Kommunikation zusätzlich abgesichert werden.
  5. Falls die Clients und der Terminalserver über unzureichend vertrauenswürdige Netze kommunizieren, MÜSSEN sich sowohl die Benutzenden als auch der Terminalserver beim Kommunikationsaufbau authentisieren.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) ARCH.5.1 deckt die Forderung als allgemeine Netzwerkanforderung ab, indem Verbindungen zwischen IT-Systemen (z. B. auf Basis von IP-Subnetzen/Netzen) eingeschränkt und autorisiert werden müssen.

### → SYS.4.4.A13 — Deaktivierung und Deinstallation nicht benötigter Komponenten (S)
  1. Nach der Installation SOLLTE überprüft werden, welche Protokolle, Anwendungen und weiteren Tools auf den IoT-Geräten installiert und aktiviert sind.
  2. Nicht benötigte Protokolle, Dienste, Anmeldekennungen und Schnittstellen SOLLTEN deaktiviert oder ganz deinstalliert werden.
  3. Die Verwendung von nicht benötigten Funkschnittstellen SOLLTE unterbunden werden.
  4. Wenn dies nicht am Gerät selber möglich ist, SOLLTEN nicht benötigte Dienste über die Firewall eingeschränkt werden. **◀ ZITIERT**
  5. Die getroffenen Entscheidungen SOLLTEN so dokumentiert werden, dass nachvollzogen werden kann, welche Konfiguration für die IoT-Geräte gewählt wurden.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) ARCH.5.1 verlangt allgemein die netzbasierte Einschränkung von Verbindungen zwischen IT-Systemen (u. a. mittels Paketfiltern/Firewalls auf Port- und Anwendungsebene), was die Einschränkung nicht benötigter Dienste per Firewall direkt abdeckt.

### → SYS.4.4.A15 — Restriktive Rechtevergabe (S)
  1. Die Zugriffsberechtigungen auf IoT-Geräte SOLLTEN möglichst restriktiv vergeben werden.
  2. Wenn dies über die IoT-Geräte selber nicht möglich ist, SOLLTE überlegt werden, dies netzseitig zu regeln. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) ARCH.5.1 fordert die netzseitige Einschränkung von Verbindungen zwischen IT-Systemen, was die geforderte netzseitige Regelung von Zugriffsberechtigungen auf IoT-Geräte abbildet.

### → SYS.4.4.A5 — Einschränkung des Netzzugriffs (B)
  1. Der Netzzugriff von IoT-Geräten MUSS auf das erforderliche Minimum eingeschränkt werden. **◀ ZITIERT**
  2. Dies SOLLTE regelmäßig kontrolliert werden.
  3. Dazu SOLLTEN folgende Punkte beachtet werden: Bei Verkehrskontrollen an Netzübergängen, z. B. durch Regelwerke auf Firewalls und Access Control Lists (ACLs) auf Routern, DÜRFEN NUR zuvor definierte ein- und ausgehende Verbindungen erlaubt werden. **◀ ZITIERT**
  4. Die Routings auf IoT-Geräten und Sensoren, insbesondere die Unterdrückung von Default-Routen, SOLLTE restriktiv konfiguriert werden.
  5. Die IoT-Geräte und Sensoren SOLLTEN in einem eigenen Netzsegment betrieben werden, das ausschließlich mit dem Netzsegment für das Management kommunizieren darf.
  6. Virtual Private Networks (VPNs) zwischen den Netzen mit IoT-Geräten und Sensor-Netzen und den Management-Netzen SOLLTEN restriktiv konfiguriert werden.
  7. Die UPnP-Funktion MUSS an allen Routern deaktiviert sein.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme ARCH.5.1 fordert die generelle Einschränkung von Verbindungen zwischen IT-Systemen auf das Notwendige und deckt damit die Beschränkung des Netzzugriffs von IoT-Geräten auf das erforderliche Minimum inhaltlich ab.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) ARCH.5.1 fordert allgemein die Einschränkung von Verbindungen zwischen IT-Systemen mittels Paketfiltern und Allowlisting, was die Beschränkung auf vordefinierte Verbindungen an Netzübergängen abdeckt.

### → CON.11.1.A16 — Zusammenschaltung von VS-IT nach § 58 VSA (B)
  1. Bevor VS-IT mit anderer VS-IT zusammengeschaltet werden darf, MUSS geprüft werden, ob und inwieweit Informationen zwischen der zusammengeschalteten VS-IT ausgetauscht werden dürfen.
  2. Bei der Prüfung MUSS das jeweilige Schutzniveau und der Grundsatz „Kenntnis nur, wenn nötig“ berücksichtigt werden.
  3. Abhängig vom Ergebnis der Prüfung MÜSSEN IT-Sicherheitsfunktionen zum Schutz der Systemübergänge implementiert werden (siehe CON.11.1.A3 Einsatz von IT-Sicherheitsprodukten nach §§ 51, 52 VSA). **◀ ZITIERT**
  4. Vor der Zusammenschaltung der VS-IT MUSS bewertet und dokumentiert werden, ob diese für das angestrebte Szenario zwingend erforderlich ist und ob durch die Zusammenschaltung eine besondere Gefährdung der einzelnen Teilsysteme entsteht.
  5. Es MUSS geprüft werden, ob der durch die Zusammenschaltung von VS-IT entstandene Gesamtbestand der Daten höher einzustufen ist und weitere Geheimschutzmaßnahmen notwendig werden.
  6. Wird VS-IT für die Verarbeitung von VS des Geheimhaltungsgrads VS-NfD direkt oder kaskadiert mit VS-IT für die Verarbeitung von VS des Geheimhaltungsgrades STRENG GEHEIM gekoppelt, dann MUSS sichergestellt werden, dass keine Verbindungen zu ungeschützten oder öffentlichen Netzen hergestellt werden.
- **Satz 3** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) ARCH.5.1 fordert die technische Einschränkung und Absicherung von Verbindungen zwischen IT-Systemen, was die Implementierung von IT-Sicherheitsfunktionen an Systemübergängen inhaltlich abdeckt.


## ARCH.5.1.4 — UDP-basierte Angriffe  [1 Paare]

**Statement (normativ):** Architektur für Netze SOLLTE bekannte UDP-basierte Angriffsmethoden blockieren.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** UDP-basierte Angriffsmethoden (englisch: known UDP-based attack vectors) sind hierbei Techniken zu verstehen, die das User Datagram Protocol (UDP) ausnutzen. UDP ist das am meisten verwendete Protokoll für die Übertragung von Datenstreams. Aufgrund seiner verbindungslosen Eigenschaft ermöglicht UDP eine sehr schnelle Datenübertragung und wird daher oft für zeitkritische Anwendungen wie Videostreaming, VoIP oder DNS-Anfragen verwendet. Genau diese Eigenschaft macht es jedoch anfällig für Missbrauch, da die Absenderadresse leicht gefälscht werden kann (IP-Spoofing). Beispiele für Angriffe sind Sequence Number Guessing, DHCP Starvation und UDP Hole-Punching Abuse. Die Anforderung kann durch Blockieren solcher Verbindungen oder nur bestimmter Mechanismen umgesetzt werden.

### → NET.3.2.A19 — Schutz vor TCP SYN Flooding, UDP Paket Storm und Sequence Number Guessing am Paketfilter (S)
  1. Am Paketfilter, der Server-Dienste schützt, die aus nicht vertrauenswürdigen Netzen erreichbar sind, SOLLTE ein geeignetes Limit für halboffene und offene Verbindungen gesetzt werden.
  2. Am Paketfilter, der Server-Dienste schützt, die aus weniger oder nicht vertrauenswürdigen Netzen erreichbar sind, SOLLTEN die sogenannten Rate Limits für UDP-Datenströme gesetzt werden. **◀ ZITIERT**
  3. Am äußeren Paketfilter SOLLTE bei ausgehenden Verbindungen für TCP eine zufällige Generierung von Initial Sequence Numbers (ISN) aktiviert werden, sofern dieses nicht bereits durch Sicherheitsproxies realisiert wird.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) Die G++-Maßnahme ARCH.5.1.4 fordert das Blockieren bekannter UDP-basierter Angriffsmethoden auf Netzebene, was die Durchsetzung von Rate Limits für UDP-Datenströme zur Abwehr von UDP-basierten Angriffen als allgemeinere Anforderung abdeckt.


## ARCH.2.2.9 — Segmentierung von IPv4 und IPv6  [1 Paare]

**Statement (normativ):** Architektur für Netze SOLLTE Verbindungen zwischen IPv4 und IPv6 einschränken.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** IPv4 und IPv6 sind grundlegende Netzprotokolle, die unterschiedliche Protokollstacks und Sicherheitseigenschaften haben. Eine Trennung von IT-Systemen mit IPv4 und IPv6 erschwert es Angreifern, Schwachstellen der Protokolle auszunutzen oder zu kombinieren und verringert die Wahrscheinlichkeit von Fehlern durch Wechselwirkungen.

### → NET.1.1.A20 — Zuweisung dedizierter Subnetze für IPv4/IPv6-Endgerätegruppen (S)
  1. Unterschiedliche IPv4-/IPv6- Endgeräte SOLLTEN je nach verwendetem Protokoll (IPv4-/IPv6- oder IPv4/IPv6-DualStack) dedizierten Subnetzen zugeordnet werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme ARCH.2.2.9 fordert die Segmentierung und Einschränkung von Verbindungen zwischen IPv4 und IPv6, was die Zuordnung der Endgeräte zu dedizierten Subnetzen je nach Protokoll inhaltlich abdeckt.


## ARCH.8.1 — Redundanz im Kernnetz  [7 Paare]

**Statement (normativ):** Architektur für Netze SOLLTE für das Kernnetz redundante Netzkomponenten installieren.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Ziel hierbei ist es, dass beim Ausfall eines Systems oder einer Systemkomponente die Netzanbindung stets weiterhin funktionsfähig bleibt (Single-Point-of-Failure).

### → NET.1.1.A13 — Netzplanung (B)
  1. Jede Netzimplementierung MUSS geeignet, vollständig und nachvollziehbar geplant werden.
  2. Dabei MÜSSEN die Sicherheitsrichtlinie sowie die Anforderungsspezifikation beachtet werden.
  3. Darüber hinaus MÜSSEN in der Planung mindestens die folgenden Punkte bedarfsgerecht berücksichtigt werden: Anbindung von Internet und, sofern vorhanden, Standortnetz und Extranet, Topologie des Gesamtnetzes und der Netzbereiche, d. h. Zonen und Netzsegmente, Dimensionierung und Redundanz der Netz- und Sicherheitskomponenten, Übertragungsstrecken und Außenanbindungen, zu nutzende Protokolle und deren grundsätzliche Konfiguration und Adressierung, insbesondere IPv4/IPv6-Subnetze von Endgerätegruppen sowie Administration und Überwachung (siehe NET.1.2 Netzmanagement). **◀ ZITIERT**
  4. Die Netzplanung MUSS regelmäßig überprüft werden.
- **Satz 3** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 3) ARCH.8.1 fordert die redundante Auslegung von Netzkomponenten im Kernnetz und deckt damit die im Satz geforderte Berücksichtigung der Redundanz von Netzkomponenten als konkreten Spezialfall ab.

### → NET.1.1.A16 — Spezifikation der Netzarchitektur (S)
  1. Auf Basis der Sicherheitsrichtlinie und der Anforderungsspezifikation SOLLTE eine Architektur für die Zonen inklusive internem Netz, DMZ-Bereich und Außenanbindungen entwickelt und nachhaltig gepflegt werden.
  2. Dabei SOLLTEN je nach spezifischer Situation der Institution alle relevanten Architekturelemente betrachtet werden, mindestens jedoch: Netzarchitektur des internen Netzes mit Festlegungen dazu, wie Netzvirtualisierungstechniken, Layer-2- und Layer-3-Kommunikation sowie Redundanzverfahren einzusetzen sind, Netzarchitektur für Außenanbindungen, inklusive Firewall-Architekturen, sowie DMZ- und Extranet-Design und Vorgaben an die Standortkopplung, Festlegung, an welchen Stellen des Netzes welche Sicherheitskomponenten wie Firewalls oder IDS/IPS zu platzieren sind und welche Sicherheitsfunktionen diese realisieren müssen, Vorgaben für die Netzanbindung der verschiedenen IT-Systeme, Netzarchitektur in Virtualisierungs-Hosts, wobei insbesondere Network Virtualization Overlay (NVO) und die Architektur in Vertikal integrierten Systemen (ViS) zu berücksichtigen sind, Festlegungen der grundsätzlichen Architektur-Elemente für eine Private Cloud sowie Absicherung der Anbindungen zu Virtual Private Clouds, Hybrid Clouds und Public Clouds sowie Architektur zur sicheren Administration und Überwachung der IT-Infrastruktur. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme ARCH.8.1 deckt als architektonische Vorgabe zur Redundanz im Kernnetz einen spezifischen Teilaspekt der in Satz 2 geforderten Festlegungen zu Redundanzverfahren im internen Netz ab.

### → NET.1.1.A28 — Hochverfügbare Netz- und Sicherheitskomponenten (H)
  1. Zentrale Bereiche des internen Netzes sowie die Sicherheitskomponenten SOLLTEN hochverfügbar ausgelegt sein. **◀ ZITIERT**
  2. Dazu SOLLTEN die Komponenten redundant ausgelegt und auch intern hochverfügbar realisiert werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) ARCH.8.1 fordert die redundante Installation von Netzkomponenten im Kernnetz, was die geforderte hochverfügbare Auslegung zentraler Netzbereiche inhaltlich abdeckt.
- **Satz 2** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die Maßnahme ARCH.8.1 fordert explizit die redundante Installation von Netzkomponenten im Kernnetz, was die geforderte redundante Auslegung der Komponenten abdeckt.

### → NET.3.2.A29 — Einsatz von Hochverfügbarkeitslösungen (H)
  1. Paketfilter und Application-Level-Gateway SOLLTEN hochverfügbar ausgelegt werden.
  2. Zudem SOLLTEN zwei voneinander unabhängige Zugangsmöglichkeiten zum externen Netz bestehen, z. B. zwei Internetzugänge von unterschiedlichen Providern.
  3. Interne und externe Router sowie alle weiteren beteiligten aktiven Komponenten (z. B. Switches) SOLLTEN ebenfalls hochverfügbar ausgelegt sein. **◀ ZITIERT**
  4. Auch nach einem automatischen Failover SOLLTE die Firewall-Struktur die Anforderungen der Sicherheitsrichtlinie erfüllen (Fail safe bzw. Fail secure).
  5. Die Funktion SOLLTE anhand von zahlreichen Parametern überwacht werden.
  6. Die Funktionsüberwachung SOLLTE sich nicht auf ein einzelnes Kriterium stützen.
  7. Protokolldateien und Warnmeldungen der Hochverfügbarkeitslösung SOLLTEN regelmäßig kontrolliert werden.
- **Satz 3** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 3) Die G++-Maßnahme fordert die Installation redundanter Netzkomponenten im Kernnetz, was die geforderte hochverfügbare Auslegung von Routern und Switches inhaltlich abdeckt.

### → NET.3.1.A26 — Hochverfügbarkeit (H)
  1. Die Realisierung einer Hochverfügbarkeitslösung SOLLTE den Betrieb der Router und Switches bzw. deren Sicherheitsfunktionen NICHT behindern oder das Sicherheitsniveau senken.
  2. Router und Switches SOLLTEN redundant ausgelegt werden. **◀ ZITIERT**
  3. Dabei SOLLTE darauf geachtet werden, dass die Sicherheitsrichtlinie der Institution eingehalten wird.
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) Die Maßnahme ARCH.8.1 deckt die Forderung direkt ab, indem sie die Installation redundanter Netzkomponenten zur Vermeidung von Ausfällen vorschreibt.

### → SYS.1.5.A9 — Netzplanung für virtuelle Infrastrukturen (S) [Planende]
  1. Der Aufbau des Netzes für virtuelle Infrastrukturen SOLLTE detailliert geplant werden.
  2. Auch SOLLTE geprüft werden, ob für bestimmte Virtualisierungsfunktionen (wie z. B. die Live-Migration) ein eigenes Netz aufgebaut und genutzt werden muss.
  3. Es SOLLTE geplant werden, welche Netzsegmente aufgebaut werden müssen (z. B. Managementnetz, Speichernetz).
  4. Es SOLLTE festgelegt werden, wie die Netzsegmente sich sicher voneinander trennen und schützen lassen.
  5. Dabei SOLLTE sichergestellt werden, dass das produktive Netz vom Managementnetz getrennt ist (siehe SYS.1.5.A11 Administration der Virtualisierungsinfrastruktur über ein gesondertes Managementnetz).
  6. Auch die Verfügbarkeitsanforderungen an das Netz SOLLTEN erfüllt werden. **◀ ZITIERT**
- **Satz 6** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 6) Die Installation redundanter Netzkomponenten zur Vermeidung von Single Points of Failure deckt die Erfüllung der Verfügbarkeitsanforderungen an das Netz direkt ab.

