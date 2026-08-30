# Review-Dossier Praktik BES

Praktik BES: 93 Controls mit Mapping, 421 Paare gesamt. Gesampelt: 5 Controls (max/min/median Paarzahl + 2 zufällig).

## BES.4.2 — Dokumentation der Beschaffungskriterien  [43 Paare]

**Statement (normativ):** Beschaffungsmanagement für Einkäufe SOLLTE {{ insert: param, bes.4.2-prm1 }} für die Beschaffung dokumentieren.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Beschaffungskriterien sind nachvollziehbare Bewertungsmaßstäbe, die bei der Anschaffung von IT-Produkten und Dienstleistungen berücksichtigt werden, um sicherzustellen, dass diese den Sicherheitsanforderungen der Institution entsprechen. Sie ergeben sich aus dem erfassten Bedarf (z.B. einer Beschreibung der Funktionen von IT-Produkten oder zu leistenden Diensten), sowie den Sicherheitsanforderungen an das zu beschaffende Produkt oder die Dienstleistung, die über das jeweilige Zielobjekt im Katalog gefiltert werden können. Beispiele für Beschaffungskriterien sind die Erfüllung definierter Sicherheitsstandards, Verschlüsselungsfähigkeiten, Authentifizierungsmechanismen, Autorisierungskonzepte, die Stärke der geforderten Mechanismen (z.B. Mehr-Faktor-Authentifizierung), Verfügbarkeitsgarantien (SLAs), Umfang und Qualität der Dokumentation, Regelungen zur Prüfung oder Überwachung der Sicherheitskontrollen, sowie Einsatzbedingungen wie Temperatur oder mobile Konnektivität. Relevant ist dabei der gesamte Lebenszyklus von Vertragsschluss über Entwicklung von Lösungen bis hin zu Regelungen für Kündigungen. Zu den Kriterien können auch Negativkriterien gehören, die eine Beschaffung verhindern würden (z.B. "Keine Komponenten von der unmittelbaren Konkurrenz oder aus Staaten von denen bekannt ist, dass sie Spionage gegen den Sektor der Institution betreiben"). Je nach Beschaffung kann dafür eine Beschreibung von Informationen und Methoden zur Bereitstellung oder zum Abruf der Informationen relevant sein, sowie eine Beschreibung bestimmter technischer Eigenschaften eines Systems oder einer Anwendung. Zur Umsetzung bietet es sich an, standardisierte Vertragsvorlagen für neue Verträge zu verwenden. Bei individuellen Verträgen, die einzelne Sicherheitskontrollmechanismen festlegen, bietet sich ein Austausch von Beschreibungen der Mechanismen über strukturierte Datenformate wie OSCAL an. Weitere Informationen zur Festlegung möglicher Kriterien, inklusive einer Risikobeurteilung, können der ISO/IEC 27036-3 entnommen werden.

### → APP.2.1.A9 — Geeignete Auswahl von Komponenten für Verzeichnisdienste (S) [Fachverantwortliche]
  1. Für den Einsatz eines Verzeichnisdienstes SOLLTEN geeignete Komponenten identifiziert werden.
  2. Es SOLLTE unter Berücksichtigung von APP.6 Allgemeine Software ein Anforderungskatalog erstellt werden, nach dem die Komponenten für den Verzeichnisdienst ausgewählt und beschafft werden. **◀ ZITIERT**
  3. Im Rahmen der Planung und Konzeption des Verzeichnisdienstes SOLLTEN passend zum Einsatzzweck Anforderungen an dessen Sicherheit formuliert werden.
  4. Insbesondere SOLLTE bereits bei der Produktauswahl berücksichtigt werden, wie weitere Sicherheitsanforderungen unter Einsatz der jeweiligen Komponente umgesetzt werden können.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) BES.4.2 fordert die Dokumentation von Beschaffungskriterien, was der Erstellung eines Anforderungskatalogs für die Auswahl und Beschaffung von Komponenten entspricht.

### → APP.3.1.A9 — Beschaffung von Webanwendungen und Webservices (S)
  1. Zusätzlich zu den allgemeinen Aspekten der Beschaffung von Software SOLLTE die Institution mindestens folgendes bei der Beschaffung von Webanwendungen und Webservices berücksichtigen: sichere Eingabevalidierung und Ausgabekodierung, sicheres Session-Management, sichere kryptografische Verfahren, sichere Authentisierungsverfahren, sichere Verfahren zum serverseitigen Speichern von Zugangsdaten, geeignetes Berechtigungsmanagement, ausreichende Protokollierungsmöglichkeiten, regelmäßige Sicherheitsupdates durch den Entwickelnden der Software, Schutzmechanismen vor verbreiteten Angriffen auf Webanwendungen und Webservices sowie Zugriff auf den Quelltext der Webanwendung oder des Webservices. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) BES.4.2 deckt als allgemeinere Anforderung zur Dokumentation und Festlegung von Sicherheitskriterien für Beschaffungsvorhaben die Berücksichtigung spezifischer technischer Sicherheitsanforderungen bei der Softwarebeschaffung inhaltlich ab.

### → APP.3.3.A7 — Auswahl eines Dateisystems (S)
  1. Der IT-Betrieb SOLLTE eine Anforderungsliste erstellen, nach der die Dateisysteme des Fileservers bewertet werden. **◀ ZITIERT**
  2. Das Dateisystem SOLLTE den Anforderungen der Institution entsprechen.
  3. Das Dateisystem SOLLTE eine Journaling-Funktion bieten.
  4. Auch SOLLTE es über einen Schutzmechanismus verfügen, der verhindert, dass mehrere Benutzende oder Anwendungen gleichzeitig schreibend auf eine Datei zugreifen.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme BES.4.2 deckt das Erstellen einer Bewertungs- bzw. Anforderungsliste für IT-Produkte wie Dateisysteme durch die Dokumentation von Beschaffungskriterien allgemeingültig ab.

### → APP.6.A1 — Planung des Software-Einsatzes (B) [Fachverantwortliche]
  1. Bevor eine Institution eine (neue) Software einführt, MUSS sie entscheiden, wofür die Software genutzt und welche Informationen damit verarbeitet werden sollen, wie die Benutzenden bei der Anforderungserhebung beteiligt und bei der Einführung unterstützt werden sollen, wie die Software an weitere Anwendungen und IT-Systeme über welche Schnittstellen angebunden wird, auf welchen IT-Systemen die Software ausgeführt werden soll und welche Ressourcen zur Ausführung der Software erforderlich sind, sowie ob sich die Institution in Abhängigkeit zu einem Hersteller oder einer Herstellerin begibt, wenn sie diese Software einsetzt.
  2. Hierbei MÜSSEN bereits Sicherheitsaspekte berücksichtigt werden. **◀ ZITIERT**
  3. Zusätzlich MUSS die Institution die Zuständigkeiten für fachliche Betreuung, Freigabe und betriebliche Administration schon im Vorfeld klären und festlegen.
  4. Die Zuständigkeiten MÜSSEN dokumentiert und bei Bedarf aktualisiert werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die Maßnahme BES.4.2 verlangt die Dokumentation von Beschaffungskriterien basierend auf Sicherheitsanforderungen und deckt damit die frühzeitige Berücksichtigung von Sicherheitsaspekten bei der Softwareauswahl ab.

### → APP.6.A2 — Erstellung eines Anforderungskatalogs für Software (B) [Fachverantwortliche]
  1. Auf Basis der Ergebnisse der Planung MÜSSEN die Anforderungen an die Software in einem Anforderungskatalog erhoben werden. **◀ ZITIERT**
  2. Der Anforderungskatalog MUSS dabei die grundlegenden funktionalen Anforderungen umfassen.
  3. Darüber hinaus MÜSSEN die nichtfunktionalen Anforderungen und hier insbesondere die Sicherheitsanforderungen in den Anforderungskatalog integriert werden. **◀ ZITIERT**
  4. Hierbei MÜSSEN sowohl die Anforderungen von den Fachverantwortlichen als auch vom IT-Betrieb berücksichtigt werden.
  5. Insbesondere MÜSSEN auch die rechtlichen Anforderungen, die sich aus dem Kontext der zu verarbeitenden Daten ergeben, berücksichtigt werden.
  6. Der fertige Anforderungskatalog SOLLTE mit allen betroffenen Fachabteilungen abgestimmt werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 1) Das Erheben und Dokumentieren von Anforderungen an Software in einem Anforderungskatalog stellt eine konkrete Umsetzung der Dokumentation von Beschaffungskriterien für Softwareprodukte dar.
- **Satz 3** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) BES.4.2 fordert die Dokumentation von Beschaffungskriterien, welche explizit Sicherheitsanforderungen und nichtfunktionale Kriterien wie SLAs und Sicherheitsstandards für zu beschaffende IT-Produkte umfassen.

### → CON.1.A9 — Festlegung von Kriterien für die Auswahl von Hard- oder Software mit kryptografischen Funktionen (S) [Fachverantwortliche]
  1. Im Kryptokonzept SOLLTE festgelegt werden, anhand welcher Kriterien und Anforderungen Hard- oder Software mit kryptografischen Funktionen ausgesucht wird. **◀ ZITIERT**
  2. Hierbei SOLLTEN Aspekte wie Funktionsumfang, Interoperabilität, Wirtschaftlichkeit, Fehlbedienungs- und Fehlfunktionssicherheit, technische Aspekte, personelle und organisatorische Aspekte, Lebensdauer von kryptografischen Verfahren und der eingesetzten Schlüssellängen sowie gesetzliche Rahmenbedingungen internationale rechtliche Aspekte wie Export- und Importbeschränkungen für Hard- oder Software mit kryptografischen Funktionen, wenn die kryptografischen Verfahren auch im Ausland eingesetzt werden Datenschutz berücksichtigt und im Kryptokonzept dokumentiert werden.
  3. Dabei SOLLTE grundsätzlich zertifizierte Hard- oder Software mit kryptografischen Funktionen, deren Zertifizierung die jeweils relevanten Aspekte der Kryptografie umfasst, bevorzugt ausgewählt werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) BES.4.2 deckt die Forderung als übergeordnete, allgemeine Maßnahme zur Dokumentation von Beschaffungskriterien für IT-Produkte und -Dienstleistungen inhaltlich ab.

### → CON.11.1.A4 — Beschaffung von VS-IT nach § 49 VSA (B)
  1. Bevor VS-IT beschafft wird, MUSS sichergestellt werden, dass deren Sicherheit während des gesamten Lebenszyklus ab dem Zeitpunkt, zu dem fest steht, dass die IT zur VS-Verarbeitung eingesetzt werden soll, bis zur Aussonderung kontinuierlich gewährleistet wird.
  2. Um einen durchgehenden Geheimschutz sicherzustellen, MÜSSEN die Vergabeunterlagen so formuliert werden, dass die Anforderungen der VSA vollständig erfüllt werden können.
  3. Bei Beschaffungsaufträgen für VS-IT MÜSSEN die notwendigen IT-Sicherheitsfunktionen der jeweiligen IT-Produkte vorab festgelegt werden. **◀ ZITIERT**
  4. Bei der Formulierung der Vergabeunterlagen MÜSSEN insbesondere die Aufbewahrung, Archivierung und Löschung von elektronischer VS sowie Aussonderung, Wartung und Instandsetzung von VS-IT berücksichtigt werden.
  5. Sofern einem zu beschaffenden IT-Produkt eine IT-Sicherheitsfunktion zugeordnet ist, SOLLTE ein IT-Produkt aus der Liste der zugelassenen IT-Sicherheitsprodukte beschafft werden.
  6. Wird stattdessen ein Produkt ohne Zulassungsaussage ausgewählt, dann SOLLTE im Vorhinein mit dem BSI abgeklärt werden, ob es zugelassen werden kann.
  7. Zusätzlich SOLLTE in der Ausschreibung aufgenommen werden, dass der Hersteller an einem Zulassungsverfahren mitwirken muss (siehe BSI TL - IT 01).
  8. Verträge MÜSSEN derart gestaltet werden, dass bei einer Rückgabe von defekten oder geleasten IT-Produkten deren Datenträger oder sonstige Komponenten, auf denen VS gespeichert sein könnten, im Besitz der Dienststelle verbleiben.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 3) Die Maßnahme BES.4.2 verlangt die vorherige Festlegung und Dokumentation von Beschaffungskriterien, wozu explizit die Sicherheitsanforderungen und IT-Sicherheitsfunktionen der zu beschaffenden Produkte gehören.

### → CON.3.A7 — Beschaffung eines geeigneten Datensicherungssystems (S) [IT-Betrieb]
  1. Bevor ein Datensicherungssystem beschafft wird, SOLLTE der IT-Betrieb eine Anforderungsliste erstellen, nach der die am Markt erhältlichen Produkte bewertet werden. **◀ ZITIERT**
  2. Die angeschafften Datensicherungssysteme SOLLTEN die Anforderungen des Datensicherungskonzepts der Institution erfüllen.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) BES.4.2 verlangt allgemein die Dokumentation von Beschaffungskriterien als Bewertungsmaßstäbe für einzukaufende IT-Produkte und deckt damit die Erstellung einer Anforderungsliste zur Produktbewertung vor der Beschaffung ab.

### → CON.8.A17 — Auswahl vertrauenswürdiger Entwicklungswerkzeuge (H)
  1. Zur Entwicklung der Software SOLLTEN nur Werkzeuge mit nachgewiesenen Sicherheitseigenschaften verwendet werden.
  2. An die herstellenden Unternehmen von Hardware oder Software SOLLTEN hinreichende Anforderungen zur Sicherheit ihrer Werkzeuge gestellt werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) BES.4.2 fordert die Dokumentation von Beschaffungs- und Sicherheitskriterien für IT-Einkäufe, was das Stellen von Sicherheitsanforderungen an herstellende Unternehmen von Werkzeugen als allgemeine Beschaffungstätigkeit abdeckt.

### → CON.8.A3 — Auswahl einer Entwicklungsumgebung (B)
  1. Eine Liste der erforderlichen und optionalen Auswahlkriterien für eine Entwicklungsumgebung MUSS von Fachverantwortlichen für die Software-Entwicklung erstellt werden. **◀ ZITIERT**
  2. Die Entwicklungsumgebung MUSS anhand der vorgegebenen Kriterien ausgewählt werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) BES.4.2 verlangt die allgemeine Dokumentation von Kriterien für die Beschaffung und Auswahl von IT-Produkten, was die Erstellung von Auswahlkriterien für Entwicklungsumgebungen aus Satz 1 abdeckt.

### → IND.1.A11 — Sichere Beschaffung und Systementwicklung (S)
  1. Sollen OT-Systeme beschafft, geplant oder entwickelt werden, SOLLTEN Regelungen zur Informationssicherheit getroffen und dokumentiert werden.
  2. Die Unterlagen SOLLTEN Teil der Ausschreibung sein.
  3. Bei Beschaffungen, Planungen oder Entwicklungen SOLLTE die Informationssicherheit in dem gesamten Lebenszyklus berücksichtigt werden.
  4. Voraussetzungen und Umsetzungshinweise für einen sicheren Betrieb von ICS-Komponenten von den herstellenden Unternehmen SOLLTEN frühzeitig eingeplant und umgesetzt werden.
  5. Für ICS-Komponenten SOLLTEN einheitliche und dem Schutzbedarf angemessene Anforderungen an die Informationssicherheit definiert werden. **◀ ZITIERT**
  6. Diese SOLLTEN berücksichtigt werden, wenn neue ICS-Komponenten beschafft werden.
  7. Die Einhaltung und Umsetzung SOLLTE dokumentiert werden.
  8. Die Institution SOLLTE dokumentieren, wie sich das System in die Konzepte für die Zoneneinteilung, das Berechtigungs- und Schwachstellen-Management sowie für den Virenschutz einfügt und diese gegebenenfalls anpassen.
  9. Es SOLLTE geregelt sein, wie der Betrieb aufrechterhalten werden kann, falls einer der Kooperationspartner keine Dienstleistungen mehr anbietet.
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 5) BES.4.2 fordert die Dokumentation von Beschaffungs- und Sicherheitskriterien für Einkäufe und deckt damit die Definition angemessener Sicherheitsanforderungen für Komponenten ab.

### → INF.11.A1 — Planung und Beschaffung (B) [Fachverantwortliche, Beschaffungsstelle, Datenschutzbeauftragte]
  1. Bevor Fahrzeuge beschafft werden, MUSS der Einsatzzweck geplant werden.
  2. Die funktionalen Anforderungen an die Fahrzeuge und insbesondere die Anforderungen an die Informationssicherheit, sowie den Datenschutz der verbauten IT-Komponenten MÜSSEN erhoben werden. **◀ ZITIERT**
  3. Hierbei MÜSSEN folgende Aspekte berücksichtigt werden: Einsatzszenarien der Fahrzeuge, nähere Einsatzumgebung der Fahrzeuge sowie der gesamte Lebenszyklus der Fahrzeuge.
  4. Die Fahrzeuge MÜSSEN außerdem über angemessene Schließsysteme verfügen, sofern die Fahrzeuge nicht durchgehend durch andere Maßnahmen oder Regelungen gesichert werden können.
  5. Während der Planung SOLLTE berücksichtigt werden, dass viele Fahrzeuge Daten an die fahrzeugherstellenden Unternehmen und weitere Dritte übermitteln können.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) BES.4.2 fordert die Erfassung und Dokumentation von Beschaffungskriterien, was die funktionale Bedarfsermittlung sowie Sicherheits- und Datenschutzanforderungen für Beschaffungsvorhaben allgemein abdeckt.

### → INF.13.A5 — Planung des TGM (S) [Planende]
  1. Das TGM, die zugrundeliegende Infrastruktur und die zugehörigen Prozesse SOLLTEN geeignet geplant werden.
  2. Die Planung SOLLTE dabei mindestens eine detaillierte Anforderungsanalyse, eine ausreichende Grobkonzeptionierung und eine Fein- und Umsetzungsplanung umfassen.
  3. Im Rahmen der Anforderungsanalyse SOLLTEN Anforderungen an TGM-Infrastruktur und TGM-Prozesse spezifiziert werden.
  4. Dabei SOLLTEN alle wesentlichen Elemente für das TGM berücksichtigt werden.
  5. Auch SOLLTE die Sicherheitsrichtlinie für das TGM beachtet werden.
  6. Steht die Nachfrageorganisation zum Zeitpunkt der Planung noch nicht fest, SOLLTEN im Rahmen einer universellen Planung zumindest grundlegende Anforderungen erfasst werden, die dem Stand der Technik entsprechen.
  7. Für die Anforderungsspezifikation SOLLTEN auch die Schnittstellen der zu verwaltenden Systeme dokumentiert werden, z. B. um die Kompatibilität von TGM-Lösung und zu verwaltenden Systemen zu gewährleisten.
  8. Außerdem SOLLTEN vor der Beauftragung von Dienstleistenden oder vor der Anschaffung von Hard- oder Software der durch das TGM zu verwaltenden Systeme die Anforderungen des TGM in einem Lastenheft des TGM spezifiziert werden. **◀ ZITIERT**
  9. In diesem Lastenheft SOLLTE auch die Durchführung von Tests berücksichtigt werden (siehe auch INF.13.A22 Durchführung von Systemtests im TGM).
  10. Wenn im TGM Funktionen der Künstlichen Intelligenz (KI) eingesetzt werden, SOLLTE bei dem zuständigen herstellenden Unternehmen angefragt werden, ob und wie die Informationssicherheit hier angemessen berücksichtigt wird.
  11. Die Grobkonzeptionierung SOLLTE gemäß INF.13.A6 Erstellung eines TGM-Konzepts erfolgen.
  12. In der Fein- und Umsetzungsplanung für das TGM SOLLTEN alle in der Sicherheitsrichtlinie und im TGM-Konzept adressierten Punkte berücksichtigt werden.
- **Satz 8** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 8) BES.4.2 fordert allgemein die Dokumentation von Kriterien und Anforderungen für anstehende Beschaffungen von Produkten und Dienstleistungen und deckt damit die Spezifikation im Lastenheft vor dem Einkauf ab.

### → NET.1.2.A36 — Einbindung der Protokollierung des Netzmanagements in eine SIEM-Lösung (H)
  1. Die Protokollierung des Netzmanagements SOLLTE in eine Security-Information-and-Event-Management (SIEM)-Lösung eingebunden werden.
  2. Dazu SOLLTEN die Anforderungskataloge zur Auswahl von Netzmanagement-Lösungen hinsichtlich der erforderlichen Unterstützung von Schnittstellen und Übergabeformaten angepasst werden (siehe NET.1.2.A2 Anforderungsspezifikation für das Netzmanagement). **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme BES.4.2 verlangt allgemein die Dokumentation von Beschaffungskriterien, was die fachspezifische Anpassung von Anforderungskatalogen für Netzmanagement-Lösungen um Schnittstellen- und Formatkriterien abdeckt.

### → NET.2.1.A11 — Geeignete Auswahl von WLAN-Komponenten (S)
  1. Anhand der Ergebnisse der Planungsphase SOLLTE eine Anforderungsliste erstellt werden, mithilfe derer die am Markt erhältlichen Produkte bewertet werden können. **◀ ZITIERT**
  2. Werden WLAN-Komponenten beschafft, SOLLTE neben Sicherheit auch auf Datenschutz und Kompatibilität der WLAN-Komponenten untereinander geachtet werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) BES.4.2 fordert die Dokumentation von Beschaffungskriterien als Bewertungsmaßstäbe bei der Anschaffung von IT-Produkten, was die allgemeinere Fassung der geforderten Anforderungsliste zur Produktbewertung darstellt.

### → NET.3.1.A11 — Beschaffung eines Routers oder Switches (S)
  1. Bevor Router oder Switches beschafft werden, SOLLTE basierend auf der Sicherheitsrichtlinie eine Anforderungsliste erstellt werden, anhand derer die am Markt erhältlichen Produkte bewertet werden. **◀ ZITIERT**
  2. Es SOLLTE darauf geachtet werden, dass das von der Institution angestrebte Sicherheitsniveau mit den zu beschaffenden Geräten erreicht werden kann.
  3. Grundlage für die Beschaffung SOLLTEN daher die Anforderungen aus der Sicherheitsrichtlinie sein.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) BES.4.2 verlangt die Dokumentation von Beschaffungskriterien basierend auf den Sicherheitsanforderungen, was der Erstellung einer Anforderungsliste zur Produktbewertung vor der Beschaffung entspricht.

### → NET.3.2.A15 — Beschaffung einer Firewall (B)
  1. Bevor eine Firewall beschafft wird, MUSS eine Anforderungsliste erstellt werden, anhand derer die am Markt erhältlichen Produkte bewertet werden. **◀ ZITIERT**
  2. Es MUSS darauf geachtet werden, dass das von der Institution angestrebte Sicherheitsniveau mit der Firewall erreichbar ist.
  3. Grundlage für die Beschaffung MÜSSEN daher die Anforderungen aus der Sicherheitsrichtlinie sein.
  4. Wird IPv6 eingesetzt, MUSS der Paketfilter die IPv6-Erweiterungsheader (Extension Header) überprüfen.
  5. Zudem MUSS sich IPv6 adäquat zu IPv4 konfigurieren lassen.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) BES.4.2 fordert die Dokumentation von Beschaffungskriterien als Bewertungsmaßstäbe für IT-Produkte, was der Erstellung einer Anforderungsliste zur Produktbewertung vor der Beschaffung entspricht.

### → NET.3.3.A9 — Geeignete Auswahl von VPN-Produkten (S)
  1. Bei der Auswahl von VPN-Produkten SOLLTEN die Anforderungen der Institutionen an die Vernetzung unterschiedlicher Standorte und die Anbindung von mobilen Mitarbeitenden oder Telearbeitsplätzen berücksichtigt werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) BES.4.2 deckt als allgemeine Maßnahme die Definition und Dokumentation von anforderungsbasierten Beschaffungskriterien für IT-Produkte ab, worunter auch VPN-Szenarien zur Standortvernetzung und mobilen Anbindung fallen.

### → NET.4.1.A1 — Anforderungsanalyse und Planung für TK-Anlagen (B) [IT-Betrieb]
  1. Vor der Beschaffung oder Erweiterung einer TK-Anlage MUSS eine Anforderungsanalyse durchgeführt werden.
  2. Im Rahmen dieser Analyse MUSS festgelegt werden, welche Funktionen die TK-Anlage bieten soll.
  3. Hierbei MÜSSEN neben der Ausprägung der TK-Anlage auch die Anzahl der benötigten Verbindungen und Anschlüsse festgelegt werden.
  4. Auch eine mögliche Erweiterbarkeit und grundlegenden Sicherheitsfunktionen MÜSSEN bei der Planung betrachtet werden. **◀ ZITIERT**
  5. Darüber hinaus MÜSSEN je nach Bedarf Support- und Wartungsverträge für die TK-Anlage berücksichtigt werden.
  6. Basierend auf den ermittelten Anforderungen MUSS anschließend der Einsatz der TK-Anlage geplant und dokumentiert werden.
  7. Die zuvor ermittelten Anforderungen und die Planung MÜSSEN mit den entsprechenden IT-Zuständigen abgestimmt werden.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) BES.4.2 fordert die Dokumentation von Beschaffungskriterien basierend auf dem erfassten Bedarf und Sicherheitsanforderungen, was die planerische Berücksichtigung von Sicherheitsfunktionen und Produkteigenschaften vor der Beschaffung abdeckt.

### → NET.4.1.A13 — Beschaffung von TK-Anlagen (S)
  1. Bei der Beschaffung von TK-Anlagen SOLLTEN die Ergebnisse der Anforderungsanalyse und der Planung miteinbezogen werden. **◀ ZITIERT**
  2. Bei der Beschaffung einer TK-Anlage SOLLTE beachtet werden, dass sie neben digitalen auch analoge Teilnehmeranschlüsse anbieten sollte.
  3. Darüber hinaus SOLLTEN vorhandene Kommunikationssysteme und -komponenten bei der Beschaffung berücksichtigt werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) BES.4.2 fordert die Dokumentation von Beschaffungskriterien basierend auf dem erfassten Bedarf und Sicherheitsanforderungen und deckt damit die Einbeziehung von Anforderungsanalyse und Planung in die Beschaffung ab.

### → NET.4.2.A9 — Geeignete Auswahl von VoIP-Komponenten (S)
  1. Bevor VoIP-Komponenten beschafft werden, SOLLTE eine Anforderungsliste erstellt werden.
  2. Anhand der Anforderungsliste SOLLTEN die am Markt erhältlichen Produkte bewertet werden.
  3. Diese Anforderungsliste SOLLTE alle Merkmale zur Erreichung des angestrebten Sicherheitsniveaus umfassen. **◀ ZITIERT**
  4. Es SOLLTE geregelt werden, wie die am Markt erhältlichen Produkte gemäß der Anforderungsliste bewertet werden können.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) BES.4.2 fordert die Dokumentation von Beschaffungskriterien, welche laut Erläuterung explizit die Sicherheitsanforderungen und Merkmale zur Erreichung des angestrebten Sicherheitsniveaus umfassen.

### → NET.4.3.A6 — Beschaffung geeigneter Faxgeräte und Faxserver (S) [Beschaffungsstelle]
  1. Bevor Faxgeräte oder Faxserver beschafft werden, SOLLTE eine Anforderungsliste erstellt werden. **◀ ZITIERT**
  2. Anhand dieser Liste SOLLTEN die infrage kommenden Systeme oder Komponenten bewertet werden.
  3. Die Anforderungsliste für Faxgeräte SOLLTE auch sicherheitsrelevante Aspekte umfassen, wie den Austausch einer Teilnehmererkennung, die Ausgabe von Sendeberichten sowie eine Fehlerprotokollierung und Journalführung. **◀ ZITIERT**
  4. Zudem SOLLTEN angemessene zusätzliche Sicherheitsfunktionen anhand des Schutzbedarfs berücksichtigt werden. **◀ ZITIERT**
  5. Bei einem Faxserver SOLLTEN alle Anforderungen an das IT-System einschließlich Betriebssystem, Kommunikationskomponenten und Applikationssoftware erhoben und berücksichtigt werden.
  6. Die Möglichkeit, dass ein Faxserver in ein bestehendes Datennetz und in ein Groupware-System integriert werden kann, SOLLTE bei Bedarf berücksichtigt werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Das Dokumentieren von Beschaffungskriterien nach BES.4.2 deckt die allgemeine Erstellung einer Anforderungsliste vor der Beschaffung inhaltlich ab.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) BES.4.2 deckt die Dokumentation von Sicherheitskriterien für Beschaffungen allgemein ab, worunter auch die sicherheitsrelevanten Anforderungen an Faxgeräte fallen.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) BES.4.2 fordert die Dokumentation von Beschaffungskriterien, welche sich explizit aus den schutzbedarfsbezogenen Sicherheitsanforderungen und benötigten Sicherheitsfunktionen von IT-Produkten ableiten.

### → OPS.1.1.3.A8 — Sicherer Einsatz von Werkzeugen für das Patch- und Änderungsmanagement (S)
  1. Anforderungen und Rahmenbedingungen SOLLTEN definiert werden, nach denen Werkzeuge für das Patch- und Änderungsmanagement ausgewählt werden. **◀ ZITIERT**
  2. Außerdem SOLLTE eine spezifische Sicherheitsrichtlinie für die eingesetzten Werkzeuge erstellt werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme BES.4.2 deckt als übergeordnete Anforderung zur Dokumentation von Beschaffungskriterien die Definition von Auswahlkriterien und Rahmenbedingungen für spezifische Werkzeuge inhaltlich ab.

### → OPS.1.2.5.A9 — Auswahl und Beschaffung geeigneter Fernwartungswerkzeuge (S)
  1. Die Auswahl geeigneter Fernwartungswerkzeuge SOLLTE sich aus den betrieblichen, sicherheitstechnischen und datenschutzrechtlichen Anforderungen der Institution ergeben. **◀ ZITIERT**
  2. Alle Beschaffungsentscheidungen SOLLTEN mit den System- und Anwendungsverantwortlichen sowie dem oder der Informationssicherheitsbeauftragten abgestimmt werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) BES.4.2 fordert die Dokumentation von Beschaffungskriterien, die sich aus den betrieblichen und sicherheitstechnischen Anforderungen an zu beschaffende Produkte ergeben, was die Auswahlkriterien für Fernwartungswerkzeuge abdeckt.

### → OPS.2.2.A8 — Sorgfältige Auswahl von Cloud-Diensteanbietenden (S) [Institutionsleitung]
  1. Basierend auf der Service-Definition für den Cloud-Dienst SOLLTE ein detailliertes Anforderungsprofil für Cloud-Diensteanbietende erstellt werden. **◀ ZITIERT**
  2. Eine Leistungsbeschreibung und ein Lastenheft SOLLTEN erstellt werden.
  3. Für die Bewertung von Cloud-Diensteanbietenden SOLLTEN auch ergänzende Informationsquellen herangezogen werden.
  4. Ebenso SOLLTEN verfügbare Service-Beschreibungen der Cloud-Diensteanbietenden sorgfältig geprüft und hinterfragt werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) Das Erstellen eines detaillierten Anforderungsprofils für Cloud-Diensteanbietende entspricht der Dokumentation spezifischer Beschaffungskriterien für diesen Kontext.

### → OPS.2.3.A3 — Festlegung von Eignungsanforderungen an Anbietende von Outsourcing (B) [Fachverantwortliche, Institutionsleitung]
  1. Interne Eignungsanforderungen an potenzielle Anbietende von Outsourcing MÜSSEN festgelegt werden. **◀ ZITIERT**
  2. Diese Eignungsanforderungen MÜSSEN die erforderlichen Kompetenzen, um den Prozess aus Sicht der Informationssicherheit abzusichern, sowie die Reputation hinsichtlich der Vertrauenswürdigkeit und Zuverlässigkeit berücksichtigen.
  3. Diese Eignungsanforderungen SOLLTEN auf Basis der Unternehmensstrategie (siehe OPS.2.3.A8 Erstellung einer Strategie für Outsourcing-Vorhaben) erstellt werden.
  4. Es MUSS geprüft werden, ob potenzielle Interessenkonflikte vorliegen.
  5. Ferner SOLLTEN die Anbietenden von Outsourcing regelmäßig gegen die Eignungsanforderungen geprüft werden.
  6. Wenn die Anbietenden von Outsourcing nicht die Eignungsanforderungen erfüllen, SOLLTEN Handlungsmaßnahmen getroffen und in einem Maßnahmenkatalog festgehalten werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) BES.4.2 fordert die Festlegung und Dokumentation von Beschaffungskriterien für Produkte und Dienstleistungen, was das Aufstellen interner Eignungsanforderungen an potenzielle Anbieter abdeckt.

### → ORP.4.A18 — Einsatz eines zentralen Authentisierungsdienstes (S) [IT-Betrieb]
  1. Um ein zentrales Identitäts- und Berechtigungsmanagement aufzubauen, SOLLTE ein zentraler netzbasierter Authentisierungsdienst eingesetzt werden.
  2. Der Einsatz eines zentralen netzbasierten Authentisierungsdienstes SOLLTE sorgfältig geplant werden.
  3. Dazu SOLLTEN die Sicherheitsanforderungen dokumentiert werden, die für die Auswahl eines solchen Dienstes relevant sind. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die Maßnahme fordert generell die Dokumentation von sicherheitsrelevanten Beschaffungs- und Auswahlkriterien für Produkte und Dienstleistungen und deckt damit die Dokumentation der Anforderungen für die Auswahl des Dienstes ab.

### → SYS.1.1.A13 — Beschaffung von Servern (S)
  1. Bevor ein oder mehrere Server beschafft werden, SOLLTE eine Anforderungsliste erstellt werden, anhand derer die am Markt erhältlichen Produkte bewertet werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die Maßnahme BES.4.2 fordert die Dokumentation von Beschaffungskriterien als nachvollziehbare Bewertungsmaßstäbe für Einkäufe und deckt damit die Erstellung einer Anforderungsliste zur Produktbewertung vor der Beschaffung ab.

### → SYS.1.8.A8 — Auswahl einer geeigneten Speicherlösung (S)
  1. Die technischen Grundlagen unterschiedlicher Speicherlösungen SOLLTEN detailliert beleuchtet werden.
  2. Die Auswirkungen dieser technischen Grundlagen auf den möglichen Einsatz in der Institution SOLLTEN geprüft werden.
  3. Die Möglichkeiten und Grenzen der verschiedenen Speichersystemarten SOLLTEN für die Verantwortlichen der Institution transparent dargestellt werden.
  4. Die Entscheidungskriterien für eine Speicherlösung SOLLTEN nachvollziehbar dokumentiert werden. **◀ ZITIERT**
  5. Ebenso SOLLTE die Entscheidung für die Auswahl einer Speicherlösung nachvollziehbar dokumentiert werden.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) BES.4.2 fordert die allgemeine Dokumentation von Kriterien für die Beschaffung und Auswahl von IT-Produkten, was die Dokumentation von Entscheidungskriterien für eine Speicherlösung direkt abdeckt.

### → SYS.2.1.A11 — Beschaffung von Clients (S)
  1. Bevor Clients beschafft werden, SOLLTE eine Anforderungsliste erstellt werden, anhand derer die am Markt erhältlichen Produkte bewertet werden. **◀ ZITIERT**
  2. Die jeweiligen herstellenden Unternehmen von IT- und Betriebssystem SOLLTEN für den gesamten geplanten Nutzungszeitraum Patches für Schwachstellen zeitnah zur Verfügung stellen.
  3. Auf Betriebssysteme, die über ein Rolling-Release-Modell aktualisiert werden, SOLLTE verzichtet werden.
  4. Die zu beschaffenden Systeme SOLLTEN über eine Firmware-Konfigurationsoberfläche für UEFI SecureBoot und, sofern vorhanden, für das TPM verfügen, die eine Kontrolle durch die Institution gewährleistet und so den selbstverwalteten Betrieb von SecureBoot und des TPM ermöglicht.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die Maßnahme BES.4.2 fordert die Dokumentation von Beschaffungskriterien als Bewertungsmaßstäbe, was der Erstellung einer Anforderungsliste zur Bewertung von Produkten vor der Beschaffung entspricht.

### → SYS.2.2.3.A2 — Auswahl und Beschaffung einer geeigneten Windows-Version (B)
  1. Der Funktionsumfang und die Versorgung mit funktionalen Änderungen einer Windows-Version MÜSSEN unter Berücksichtigung des ermittelten Schutzbedarfs und des Einsatzzwecks ausgewählt werden.
  2. Die Umsetzbarkeit der erforderlichen Absicherungsmaßnahmen MUSS bei der Auswahl berücksichtigt werden. **◀ ZITIERT**
  3. Basierend auf dem Ergebnis der Überprüfung MUSS der etablierte Beschaffungsprozess um die Auswahl des entsprechenden Lizenzmodells und „Service Branches“ (CB, CBB oder LTSC) erweitert werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) BES.4.2 fordert die Dokumentation von Beschaffungskriterien zur Erfüllung von Sicherheitsanforderungen, was die Berücksichtigung der Umsetzbarkeit von Absicherungsmaßnahmen bei der Produktauswahl abstrahierend abdeckt.

### → SYS.3.3.A7 — Beschaffung von Mobiltelefonen (S)
  1. Bevor Mobiltelefone beschafft werden, SOLLTE eine Anforderungsliste erstellt werden. **◀ ZITIERT**
  2. Anhand der Anforderungsliste SOLLTEN die am Markt erhältlichen Produkte bewertet werden.
  3. Das Produkt SOLLTE danach ausgewählt werden, ob die Herstellenden für den geplanten Einsatzzeitraum Updates anbieten.
  4. Es SOLLTE gewährleistet werden, dass Ersatzteile wie Akkus und Ladegeräte in ausreichender Qualität nachbeschafft werden können.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) G++ BES.4.2 deckt das Erstellen einer Anforderungsliste vor einer Beschaffung generalisiert über die Dokumentation von Beschaffungskriterien ab.

### → SYS.4.1.A1 — Planung des Einsatzes von Druckern, Kopierern und Multifunktionsgeräten (B)
  1. Bevor Drucker, Kopierer und Multifunktionsgeräte beschafft werden, MUSS der sichere Einsatz geplant werden.
  2. Dabei SOLLTEN folgende Kriterien berücksichtigt werden: Unterstützung sicherer Protokolle zur Datenübertragung und Administration, Verschlüsselung der abgespeicherten Informationen, Authentisierung der Benutzenden direkt am Gerät, Nutzung physischer Schutzmechanismen, wie Ösen zum Diebstahlschutz oder Geräteschlösser, Existenz eines zuverlässigen und leistungsfähigen automatischen Seiteneinzugs der Scaneinheit, Unterstützung geeigneter Datenformate, Bei Bedarf Unterstützung von Patch- sowie Barcodes zur Dokumententrennung und Übergabe von Metainformationen, Existenz einer Funktion zum sicheren Löschen des Speichers sowie Verfügbarkeit von regelmäßigen Updates und Wartungsverträgen. **◀ ZITIERT**
  3. Es MUSS festgelegt werden, wo die Geräte aufgestellt werden dürfen.
  4. Außerdem MUSS festgelegt sein, wer auf die Drucker, Kopierer und Multifunktionsgeräte zugreifen darf.
  5. Die Ergebnisse SOLLTEN in einem Basiskonzept dokumentiert werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) BES.4.2 fordert allgemein die Dokumentation von Beschaffungskriterien für Einkäufe ab, was die Berücksichtigung und Festlegung der in Satz 2 detaillierten Kriterien für Druck- und Multifunktionsgeräte inhaltlich umfasst.

### → SYS.4.3.A4 — Erstellung von Beschaffungskriterien für eingebettete Systeme (S) [Beschaffungsstelle]
  1. Bevor eingebettete Systeme beschafft werden, SOLLTE eine Anforderungsliste erstellt werden, anhand derer die infrage kommenden Systeme oder Komponenten bewertet werden. **◀ ZITIERT**
  2. Die Anforderungsliste SOLLTE mindestens folgende sicherheitsrelevante Aspekte umfassen: Aspekte der materiellen Sicherheit, Anforderungen an die Sicherheitseigenschaften der Hardware, Anforderungen an die Sicherheitseigenschaften der Software, Unterstützung eines Trusted Plattform Module (TPM) durch das Betriebssystem, Sicherheitsaspekte der Entwicklungsumgebung sowie organisatorische Sicherheitsaspekte. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) BES.4.2 verlangt die allgemeine Dokumentation von Kriterien/Anforderungen für die Beschaffung, was die Erstellung einer Anforderungsliste zur Bewertung von Beschaffungsobjekten vor dem Einkauf inhaltlich abdeckt.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) BES.4.2 fordert die Dokumentation von Beschaffungskriterien für IT-Produkte, was als allgemeine Maßnahme die inhaltliche Festlegung sicherheitsrelevanter Kriterien für die Beschaffung abdeckt.

### → SYS.4.4.A8 — Beschaffungskriterien für IoT-Geräte (S) [Beschaffungsstelle]
  1. Der oder die ISB SOLLTE bei allen Beschaffungen von IoT-Geräten mit einbezogen werden.
  2. Bevor IoT-Geräte beschafft werden, SOLLTE festgelegt werden, welche Sicherheitsanforderungen diese erfüllen müssen. **◀ ZITIERT**
  3. Bei der Beschaffung von IoT-Geräten SOLLTEN Aspekte der materiellen Sicherheit ebenso wie Anforderungen an die Sicherheitseigenschaften der Software ausreichend berücksichtigt werden. **◀ ZITIERT**
  4. Eine Anforderungsliste SOLLTE erstellt werden, anhand derer die am Markt erhältlichen Produkte bewertet werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) G++-Maßnahme BES.4.2 verlangt die Dokumentation von Beschaffungskriterien basierend auf Sicherheitsanforderungen und deckt damit das vorherige Festlegen von Sicherheitsanforderungen für die Beschaffung allgemein ab.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) G++ BES.4.2 fordert die Dokumentation von Beschaffungskriterien bezüglich der Sicherheitsanforderungen und technischen Eigenschaften von IT-Produkten, was sowohl materielle als auch softwareseitige Sicherheitsaspekte abdeckt.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die Dokumentation von Beschaffungskriterien als Bewertungsmaßstäbe für Produkte deckt die geforderte Erstellung einer Anforderungsliste zur Produktbewertung inhaltlich ab.

### → ORP.5.A2 — Beachtung der Rahmenbedingungen (B) [Vorgesetzte, Zentrale Verwaltung, Institutionsleitung]
  1. Die als sicherheitsrelevant identifizierten Anforderungen MÜSSEN bei der Planung und Konzeption von Geschäftsprozessen, Anwendungen und IT-Systemen oder bei der Beschaffung neuer Komponenten einfließen. **◀ ZITIERT**
  2. Führungskräfte, die eine rechtliche Verantwortung für die Institution tragen, MÜSSEN für die Einhaltung der gesetzlichen, vertraglichen und sonstigen Vorgaben sorgen.
  3. Die Verantwortlichkeiten und Zuständigkeiten für die Einhaltung dieser Vorgaben MÜSSEN festgelegt sein.
  4. Es MÜSSEN geeignete Maßnahmen identifiziert und umgesetzt werden, um Verstöße gegen relevante Anforderungen zu vermeiden.
  5. Wenn solche Verstöße erkannt werden, MÜSSEN sachgerechte Korrekturmaßnahmen ergriffen werden, um die Abweichungen zu beheben.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) BES.4.2 stellt sicher, dass Sicherheitsanforderungen als nachvollziehbare Kriterien in den Beschaffungsprozess neuer Komponenten und Dienstleistungen einfließen und dort dokumentiert werden.

### → SYS.1.8.A9 — Auswahl von Liefernden für eine Speicherlösung (S)
  1. Anhand der spezifizierten Anforderungen an eine Speicherlösung SOLLTEN geeignete Liefernde ausgewählt werden.
  2. Die Auswahlkriterien und die Entscheidung SOLLTEN nachvollziehbar dokumentiert werden. **◀ ZITIERT**
  3. Außerdem SOLLTEN Aspekte der Wartung und Instandhaltung schriftlich in sogenannten Service-Level-Agreements (SLAs) festgehalten werden.
  4. Die SLAs SOLLTEN eindeutig und quantifizierbar sein.
  5. Es SOLLTE genau geregelt werden, wann der Vertrag mit den Liefernden endet.
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) BES.4.2 fordert explizit die Dokumentation der Kriterien für die Beschaffung und deckt damit die nachvollziehbare Dokumentation der Auswahlkriterien inhaltlich ab.


## BES.5.13.1 — Datenbereitstellung  [3 Paare]

**Statement (normativ):** Beschaffungsmanagement für Outsourcing KANN die Bereitstellung der beim Dienstleister verarbeiteten Daten in einem standardisierten Format vereinbaren.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** erhöht
**Guidance (nicht normativ):** Kann das Risiko verringern, dass im Falle eines Anbieterwechsels, einer Vertragsbeendigung oder einer Notfallwiederherstellung Daten nur in proprietären oder unvollständig dokumentierten Formaten vorliegen. Ohne ein solches Format könnte eine Institution vor dem Problem stehen, dass bei einem unerwarteten Ausfall des Dienstleisters die Daten erst zeitaufwendig konvertiert werden müssen, was den Geschäftsbetrieb verzögert oder kritische Prozesse unterbricht.

### → OPS.2.2.A15 — Sicherstellung der Portabilität von Cloud-Diensten (H) [Fachverantwortliche]
  1. Die Institution SOLLTE alle Anforderungen definieren, die es ermöglichen, Cloud-Diensteanbietende zu wechseln oder den Cloud-Dienst bzw. die Daten in die eigene IT-Infrastruktur zurückzuholen.
  2. Zudem SOLLTE die Institution regelmäßig Portabilitätstests durchführen.
  3. In den Verträgen mit den Cloud-Diensteanbietenden SOLLTEN Vorgaben festgehalten werden, mit denen sich die notwendige Portabilität gewährleisten lässt. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 3) Satz 3 fordert die vertragliche Vereinbarung von Vorgaben zur Gewährleistung der Portabilität, was die Bereitstellung von Daten in standardisierten Formaten beim Outsourcing/Cloud-Dienstleister umfasst.

### → OPS.2.3.A7 — Regelungen für eine geplante oder ungeplante Beendigung eines Outsourcing-Verhältnisses (B) [Fachverantwortliche, Institutionsleitung]
  1. Für geplante sowie ungeplante Beendigungen des Outsourcing-Verhältnisses MÜSSEN Regelungen getroffen werden.
  2. Es MUSS festgelegt werden, wie alle Informationen, Daten und Hardware der Nutzenden vom Anbietenden von Outsourcing zurückgegeben werden. **◀ ZITIERT**
  3. Hierbei MÜSSEN gesetzliche Vorgaben zur Aufbewahrung von Daten beachtet werden.
  4. Ferner SOLLTE überprüft werden, ob die Zugangs-, Zutritts- und Zugriffsrechte für die Anbietenden von Outsourcing mit der Beendigung des Outsourcing-Verhältnisses aufgehoben wurden.
- **Satz 2** | Relation GS++→ED23: `subset-of` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 2) Satz 2 fordert Festlegungen zur Rückgabe von Daten und Informationen durch den Dienstleister bei Beendigung des Outsourcings, was die Bereitstellung der Daten gemäß BES.5.13.1 umfasst.

### → OPS.3.2.A6 — Regelungen für eine geplante und ungeplante Beendigung eines Outsourcing-Verhältnisses (B)
  1. Es MÜSSEN Regelungen getroffen werden, wie verfahren wird, wenn Outsourcing-Verhältnisse geplant oder ungeplant beendet werden.
  2. Es MUSS festgelegt werden, wie alle Informationen, Daten und Hardware der Nutzenden von den Anbietenden von Outsourcing zurückgegeben werden. **◀ ZITIERT**
  3. Anschließend MÜSSEN die verbleibenden Datenbestände der Nutzenden von Outsourcing nach Ablauf der gesetzlichen Vorgaben zur Datenaufbewahrung sicher gelöscht werden.
  4. Dies MUSS durch die Anbietenden von Outsourcing dokumentiert werden.
  5. Ferner SOLLTE überprüft werden, ob die Zugangs-, Zutritts- und Zugriffsrechte für die Nutzenden von Outsourcing aufgehoben wurden, nachdem das Outsourcing-Verhältnis beendet wurde.
- **Satz 2** | Relation GS++→ED23: `subset-of` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 2) Satz 2 fordert die Festlegung der Rückgabe aller Daten und Informationen bei Beendigung des Outsourcings, was die allgemeinere Pflicht zur geregelten Bereitstellung der Dienstleisterdaten darstellt.


## BES.8.3 — Ressourcensouveränität  [1 Paare]

**Statement (normativ):** Beschaffungsmanagement für Outsourcing KANN ausreichende interne Ressourcen für den Fall einer geplanten oder ungeplanten Beendigung des Vertrages zuweisen.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** erhöht
**Guidance (nicht normativ):** Die Bereithaltung ausreichender interner Ressourcen zielt hier darauf ab, für den Fall einer plötzlichen Einstellung der beschafften Dienste ausreichend ausgestattet zu sein, um einer übermäßigen Abhängigkeit gegenüber den Anbietenden von Outsourcing vorzubeugen. Zu den notwendigen Ressourcen gehört sowohl Personal, welches für die bei einem Ausfall des Dienstleisters erforderlichen Aufgaben qualifiziert ist, als auch die für diese Aufgaben erforderliche Infrastruktur (z.B. IT-Systeme, Anwendungslizenzen, Zugänge und Berechtigungen).

### → OPS.2.3.A8 — Erstellung einer Strategie für Outsourcing-Vorhaben (S) [Institutionsleitung]
  1. Eine Strategie für Outsourcing-Vorhaben SOLLTE erstellt und etabliert werden.
  2. In dieser Strategie SOLLTEN die Ziele, Chancen und Risiken der Outsourcing-Vorhaben beschrieben werden.
  3. Die Strategie SOLL der Institution einen Rahmen für die Anforderungsprofile, die Eignungsanforderung an Anbietende von Outsourcing sowie dem Auslagerungsmanagement vorgeben.
  4. Darüber hinaus SOLLTEN neben den wirtschaftlichen, technischen, organisatorischen und rechtlichen Rahmenbedingungen auch die relevanten Aspekte der Informationssicherheit berücksichtigt werden.
  5. Es SOLLTE eine Multi-Sourcing Strategie verfolgt werden, um Engpässe sowie Abhängigkeiten von Anbietenden von Outsourcing zu vermeiden.
  6. Die Nutzenden von Outsourcing SOLLTEN ausreichend Fähigkeiten, Kompetenzen sowie Ressourcen behalten, um einer Abhängigkeit gegenüber den Anbietenden von Outsourcing vorzubeugen. **◀ ZITIERT**
- **Satz 6** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 6) BES.8.3 fordert explizit die Vorhaltung und Zuweisung ausreichender interner Ressourcen und qualifizierten Personals, um Abhängigkeiten gegenüber Outsourcing-Anbietern zu vermeiden.


## BES.7.1.1 — Test der Kompatibilität  [3 Paare]

**Statement (normativ):** Beschaffungsmanagement für Outsourcing SOLLTE die Kompatibilität des Dienstes mit dem Informationsverbund im Hinblick auf die Schnittstellen, die Netzanbindung, das Administrationsmodell und das Datenmanagementmodell testen.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Die Regelung dient dazu, ungewollte Brüche oder Inkompatibilitäten zu vermeiden, die im Betrieb zu Sicherheits- oder Funktionsproblemen führen können. Ohne eine solche Überprüfung könnte z. B. eine unklare Rechtevergabe dazu führen, dass ein Dienstleister umfassendere Zugriffe erhält als notwendig, oder eine fehlerhafte Schnittstellenintegration könnte den Ausfall wichtiger Anwendungen nach sich ziehen. Umgekehrt kann eine saubere Prüfung sicherstellen, dass Outsourcing-Dienste nahtlos integriert, technisch handhabbar und im Betrieb kontrollierbar bleiben. Für die Bewertung der Kompatibilität sind dabei vier Aspekte besonders kritisch: Schnittstellen sind die technischen Übergabepunkte, an denen Systeme Daten austauschen oder Funktionen ansprechen; Netzanbindung bezeichnet die physische oder logische Verbindung zwischen dem Dienstleister und dem Informationsverbund der Institution; das Administrationsmodell beschreibt, wer welche Rechte zur Einrichtung, Änderung und Überwachung von Systemkomponenten hat; und das Datenmanagementmodell legt fest, wie Daten gespeichert, strukturiert, repliziert und gelöscht werden.

### → OPS.2.2.A6 — Planung der sicheren Einbindung von Cloud-Diensten (S)
  1. Bevor ein Cloud-Dienst genutzt wird, SOLLTE sorgfältig geplant werden, wie er in die IT der Institution eingebunden werden soll.
  2. Hierfür SOLLTE mindestens geprüft werden, ob Anpassungen der Schnittstellen, der Netzanbindung, des Administrationsmodells sowie des Datenmanagementmodells notwendig sind. **◀ ZITIERT**
  3. Die Ergebnisse SOLLTEN dokumentiert und regelmäßig aktualisiert werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) BES.7.1.1 fordert explizit die Überprüfung bzw. das Testen der Kompatibilität bezüglich der vier identischen Aspekte (Schnittstellen, Netzanbindung, Administrationsmodell und Datenmanagementmodell).

### → OPS.2.3.A15 — Anbindung an die Netze der Outsourcing-Partner (S)
  1. Bevor das Datennetz der Nutzenden an das Datennetz der Anbietenden von Outsourcing angebunden wird, SOLLTEN alle sicherheitsrelevanten Aspekte schriftlich vereinbart werden.
  2. Es SOLLTE geprüft und dokumentiert werden, dass die Vereinbarungen für die Netzanbindung eingehalten werden.
  3. Das geforderte Sicherheitsniveau SOLLTE nachweislich bei den Anbietenden von Outsourcing umgesetzt und überprüft werden, bevor die Netzanbindung zu den Nutzenden von Outsourcing aktiviert wird.
  4. Bevor die Netze angebunden werden, SOLLTE mit Testdaten die Verbindung getestet werden. **◀ ZITIERT**
  5. Gibt es Sicherheitsprobleme auf einer der beiden Seiten, SOLLTE festgelegt sein, wer informiert und wie eskaliert wird.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) BES.7.1.1 verlangt das Testen der Kompatibilität hinsichtlich der Netzanbindung und Schnittstellen und deckt damit die allgemeinere Fassung des geforderten Verbindungstests vor der Anbindung ab.

### → OPS.3.2.A13 — Anbindung an die Netze der Outsourcing-Partner (S)
  1. Bevor das Datennetz der Anbietenden an das Datennetz der Nutzenden von Outsourcing angebunden wird, SOLLTEN alle sicherheitsrelevanten Aspekte schriftlich vereinbart werden.
  2. Bevor beide Netze verbunden werden, SOLLTEN sie auf bekannte Sicherheitslücken analysiert werden.
  3. Es SOLLTE geprüft werden, ob die Vereinbarungen für die Netzanbindung eingehalten werden und das geforderte Sicherheitsniveau nachweislich erreicht wird.
  4. Bevor die Netze angebunden werden, SOLLTE mit Testdaten die Verbindung getestet werden. **◀ ZITIERT**
  5. Gibt es Sicherheitsprobleme auf einer der beiden Seiten, SOLLTE festgelegt sein, wer informiert und wie eskaliert wird.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die G++-Maßnahme fordert das Testen der Netzanbindung und Schnittstellen im Rahmen des Outsourcings und deckt damit die geforderte Testung der Verbindung inhaltlich ab.


## BES.1.3 — Lieferanten- und Dienstleisterverzeichnis  [1 Paare]

**Statement (normativ):** Beschaffungsmanagement für Einkäufe SOLLTE alle direkten Zulieferer und Dienstleister inklusive der jeweiligen Kontaktdaten und den bezogenen Lieferungen dokumentieren.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Direkte Zulieferer sind hier alle Vertragspartner, von denen IT-Produkte bezogen werden. Dienstleister sind alle Vertragspartner, die schützenswerte Informationen des Informationsverbundes verarbeiten.

### → OPS.2.3.A11 — Führung eines Auslagerungsregisters (S)
  1. Die zuständige Person für das Auslagerungsmanagement SOLLTE ein Auslagerungsregister erstellen und pflegen, dass die Dokumentation der Outsourcing-Prozesse und Vorhaben in der Institution zentralisiert.
  2. Dieses SOLLTE auf der Basis der Anforderungsprofile erstellt werden und Informationen zu den Anbietenden von Outsourcing, Leistungskennzahlen, Kritikalität des Prozesses, abgeschlossene Verträgen und Vereinbarungen sowie Änderungen enthalten. **◀ ZITIERT**
  3. Änderungen am Auslagerungsregister SOLLTEN geeignet nachgehalten werden.
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 2) Satz 2 fordert die Erfassung von Informationen über Outsourcing-Anbieter sowie deren Verträge in einem Register, was sich inhaltlich mit der Dokumentation von Dienstleistern und bezogenen Leistungen deckt.

