# Review-Dossier Praktik GEB

Praktik GEB: 65 Controls mit Mapping, 288 Paare gesamt. Gesampelt: 5 Controls (max/min/median Paarzahl + 2 zufällig).

## GEB.10.2.7 — Brandschutzprüfung  [12 Paare]

**Statement (normativ):** Gebäudemanagement für Standorte SOLLTE die Wirksamkeit der Brandschutzmaßnahmen {{ insert: param, geb.10.2.7-prm1 }} überprüfen.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Eine regelmäßige Überprüfung von Brandmeldeanlagen, Rauchmeldern und organisatorische Maßnahmen stellt sicher, dass diese weiterhin funktionieren. Hier besteht ein enger Zusammenhang zu Compliance-Verpflichtungen, die Brandschutzprüfungen fordern.

### → INF.1.A17 — Baulicher Rauchschutz (S) [Planende]
  1. Der bauliche Rauchschutz SOLLTE nach Installations- und Umbauarbeiten überprüft werden.
  2. Es SOLLTE regelmäßig überprüft werden, ob die Rauchschutz-Komponenten noch funktionieren. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) GEB.10.2.7 fordert die regelmäßige Überprüfung der Wirksamkeit von Brandschutz- und Rauchschutzmaßnahmen und deckt damit die geforderte Funktionsprüfung der Rauchschutz-Komponenten ab.

### → INF.1.A18 — Brandschutzbegehungen (S)
  1. Brandschutzbegehungen SOLLTEN regelmäßig, d. h. mindestens ein- bis zweimal im Jahr, stattfinden. **◀ ZITIERT**
  2. Bei Brandschutzbegehungen festgestellte Mängel SOLLTEN unverzüglich behoben werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) Die regelmäßige Überprüfung der Wirksamkeit von Brandschutzmaßnahmen (Brandschutzprüfung) deckt die Forderung nach regelmäßigen Brandschutzbegehungen inhaltlich ab.

### → INF.1.A3 — Einhaltung von Brandschutzvorschriften (B)
  1. Die bestehenden Brandschutzvorschriften sowie die Auflagen der Bauaufsicht MÜSSEN eingehalten werden.
  2. Die Fluchtwege MÜSSEN vorschriftsmäßig ausgeschildert und freigehalten werden.
  3. Es MUSS regelmäßig kontrolliert werden, dass die Fluchtwege benutzbar und frei von Hindernissen sind, damit das Gebäude in einer Gefahrensituation schnell geräumt werden kann. **◀ ZITIERT**
  4. Bei der Brandschutzplanung SOLLTE die örtliche Feuerwehr hinzugezogen werden.
  5. Unnötige Brandlasten MÜSSEN vermieden werden.
  6. Es MUSS eine Brandschutzbeauftragte oder einen Brandschutzbeauftragten oder eine mit dem Aufgabengebiet betraute Person geben.
  7. Diese Person MUSS geeignet geschult sein.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die allgemeine Forderung nach regelmaessiger Ueberpruefung der Brandschutzmassnahmen in GEB.10.2.7 deckt die wiederkehrende Kontrolle von Fluchtwegen als organisatorische Brandschutzmassnahme inhaltlich ab.

### → INF.1.A4 — Branderkennung in Gebäuden (B) [Planende]
  1. Gebäude MÜSSEN entsprechend der Auflagen in der Baugenehmigung und dem Brandschutzkonzept folgend mit einer ausreichenden Anzahl von Rauchmeldern ausgestattet sein.
  2. Ist eine lokale Alarmierung am Ort des Melders nicht ausreichend, MÜSSEN alle Melder auf eine Brandmeldezentrale (BMZ) aufgeschaltet werden.
  3. Bei Rauchdetektion MUSS eine Alarmierung im Gebäude ausgelöst werden.
  4. Es MUSS sichergestellt sein, dass alle im Gebäude anwesenden Personen diese wahrnehmen können.
  5. Die Funktionsfähigkeit aller Rauchmelder sowie aller sonstigen Komponenten einer Brandmeldeanlage (BMA) MUSS regelmäßig überprüft werden. **◀ ZITIERT**
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) Die G++-Maßnahme fordert die regelmäßige Prüfung von Brandschutzmaßnahmen, was die Überprüfung der Funktionsfähigkeit von Brandmeldeanlagen und Rauchmeldern direkt umfasst.

### → INF.1.A5 — Handfeuerlöscher (B)
  1. Zur Sofortbekämpfung von Bränden MÜSSEN Handfeuerlöscher in der jeweils geeigneten Brandklasse (DIN EN 3 Tragbare Feuerlöscher) in ausreichender Zahl und Größe im Gebäude zur Verfügung stehen.
  2. Die Handfeuerlöscher MÜSSEN regelmäßig geprüft und gewartet werden. **◀ ZITIERT**
  3. Die Mitarbeitenden SOLLTEN in die Benutzung der Handfeuerlöscher eingewiesen werden.
  4. Die Einweisungen SOLLTEN in zweckmäßigen Zeitabständen wiederholt werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) GEB.10.2.7 deckt als übergeordnete Anforderung zur regelmäßigen Überprüfung von Brandschutzmaßnahmen die wiederkehrende Prüfung und Instandhaltung von Handfeuerlöschern inhaltlich ab.

### → INF.2.A10 — Inspektion und Wartung der Infrastruktur (B) [Wartungspersonal, Haustechnik]
  1. Für alle Komponenten der baulich-technischen Infrastruktur MÜSSEN mindestens die vom herstellenden Unternehmen empfohlenen oder durch Normen festgelegten Intervalle und Vorschriften für Inspektion und Wartung eingehalten werden.
  2. Inspektionen und Wartungsarbeiten MÜSSEN protokolliert werden.
  3. Brandschotten MÜSSEN daraufhin geprüft werden, ob sie unversehrt sind. **◀ ZITIERT**
  4. Die Ergebnisse MÜSSEN dokumentiert werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 3) Die regelmäßige Überprüfung der Wirksamkeit von Brandschutzmaßnahmen umfasst als allgemeinere Forderung auch die Integritätsprüfung von baulichen Brandschotten.

### → INF.2.A8 — Einsatz einer Brandmeldeanlage (B) [Planende]
  1. In einem Rechenzentrum MUSS eine Brandmeldeanlage installiert sein.
  2. Diese MUSS alle Flächen überwachen.
  3. Alle Meldungen der Brandmeldeanlage MÜSSEN geeignet weitergeleitet werden (siehe dazu auch INF.2.A13 Planung und Installation von Gefahrenmeldeanlagen).
  4. Die Brandmeldeanlage MUSS regelmäßig gewartet werden. **◀ ZITIERT**
  5. Es MUSS sichergestellt werden, dass in Räumen des Rechenzentrums keine besonderen Brandlasten vorhanden sind.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) GEB.10.2.7 fordert die regelmaessige Ueberpruefung der Brandschutzmassnahmen, was laut Erlaeuterung explizit die Funktionspruefung und Wartung von Brandmeldeanlagen umfasst.

### → INF.2.A9 — Einsatz einer Lösch- oder Brandvermeidungsanlage (B) [Haustechnik]
  1. In einem Rechenzentrum MUSS entweder eine Lösch- oder Brandvermeidungsanlage nach aktuellem Stand der Technik installiert sein oder durch technische (insbesondere durch eine flächendeckende Brandfrüherkennung, siehe INF.2.A17 Brandfrüherkennung) und organisatorische Maßnahmen (geschultes Personal und Reaktionspläne für Meldungen der Brandfrüherkennung) sichergestellt sein, dass unmittelbar (innerhalb von maximal 3 Minuten) auf Meldungen der Brandfrüherkennung mit schadensminimierenden Maßnahmen reagiert wird.
  2. In Serverräumen ohne Lösch- oder Brandvermeidungsanlage MÜSSEN Handfeuerlöscher mit geeigneten Löschmitteln in ausreichender Zahl und Größe vorhanden sein.
  3. Es MUSS beachtet werden, dass darüber hinausgehende baurechtliche Anforderungen hinsichtlich der Ausstattung mit Handfeuerlöschern davon unberührt bleiben.
  4. Die Feuerlöscher MÜSSEN so angebracht werden, dass sie im Brandfall leicht zu erreichen sind.
  5. Jeder Feuerlöscher MUSS regelmäßig geprüft und gewartet werden. **◀ ZITIERT**
  6. Alle Mitarbeitenden, die ein Rechenzentrum oder einen Serverraum betreten dürfen, MÜSSEN in die Benutzung der Handfeuerlöscher eingewiesen werden.
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) Die G++-Maßnahme fordert als allgemeinere Brandschutzprüfung die regelmäßige Überprüfung von Brandschutzmaßnahmen, was die wiederkehrende Prüfung und Wartung von Feuerlöschern einschließt.

### → INF.5.A17 — Inspektion und Wartung der Infrastruktur (S) [Haustechnik, IT-Betrieb, Wartungspersonal]
  1. Für alle Komponenten der baulich-technischen Infrastruktur SOLLTEN mindestens die vom herstellenden Unternehmen empfohlenen oder durch Normen festgelegten Intervalle und Vorschriften für Inspektion und Wartung eingehalten werden.
  2. Kabel- und Rohrdurchführungen durch brand- und rauchabschnittbegrenzende Wände SOLLTEN daraufhin geprüft werden, ob die Schotten die für den jeweiligen Einsatzzweck erforderliche Zulassung haben und unversehrt sind. **◀ ZITIERT**
  3. Inspektionen und Wartungsarbeiten MÜSSEN geeignet protokolliert werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die regelmäßige Prüfung der Wirksamkeit von Brandschutzmaßnahmen in GEB.10.2.7 umfasst als allgemeinere Prüfpflicht auch die Überprüfung von Brandschotten und Durchführungen auf Zulassung und Unversehrtheit.

### → INF.6.A1 — Handfeuerlöscher (B) [Brandschutzbeauftragte]
  1. Im Brandfall MÜSSEN im Datenträgerarchiv geeignete Handfeuerlöscher leicht erreichbar sein.
  2. Diese Handfeuerlöscher MÜSSEN regelmäßig inspiziert und gewartet werden. **◀ ZITIERT**
  3. Mitarbeitende, die in der Nähe eines Datenträgerarchivs tätig sind, MÜSSEN in die Benutzung der Handfeuerlöscher eingewiesen werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die regelmaessige Ueberpruefung der Wirksamkeit von Brandschutzmassnahmen gemaess GEB.10.2.7 stellt die allgemeinere Taetigkeit zur regelmaessigen Inspektion und Wartung von Brandschutzeinrichtungen wie Handfeuerloeschern dar.

### → INF.1.A19 — Information des oder der Brandschutzbeauftragten (S)
  1. Der oder die Brandschutzbeauftragte SOLLTE über Arbeiten an Leitungstrassen, Fluren, Flucht- und Rettungswegen informiert werden.
  2. Diese Person SOLLTE die ordnungsgemäße Ausführung von Brandschutzmaßnahmen kontrollieren. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) Die regelmäßige Überprüfung der Brandschutzmaßnahmen in GEB.10.2.7 deckt die Kontrolle der ordnungsgemäßen Ausführung von Brandschutzmaßnahmen inhaltlich als allgemeinere Fassung ab.

### → INF.1.A34 — Gefahrenmeldeanlage (H)
  1. Es SOLLTE eine den Räumlichkeiten und den Risiken angemessene Gefahrenmeldeanlage geben.
  2. Die Gefahrenmeldeanlage SOLLTE regelmäßig geprüft und gewartet werden. **◀ ZITIERT**
  3. Es MUSS sichergestellt werden, dass diejenigen, die Gefahrenmeldungen empfangen in der Lage sind, technisch und personell angemessen auf den Alarm zu reagieren.
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme fordert die regelmäßige Wirksamkeitsprüfung von Brandschutzmaßnahmen (einschließlich Brandmeldeanlagen), was die geforderte regelmäßige Prüfung von Gefahrenmeldeanlagen für den Brandschutzbereich abdeckt.


## GEB.5.3 — Physische Mikrosegmentierung  [4 Paare]

**Statement (normativ):** Gebäudemanagement für IT-Systeme KANN eine physische Mikrosegmentierung installieren.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** erhöht
**Guidance (nicht normativ):** Bei der physischen Mikrosegmentierung in der Sicherheitsarchitektur geht es darum, unterschiedliche physische Grenzen innerhalb gemeinsam genutzter Einrichtungen zu schaffen, um verschiedene Sicherheitsbereiche zu isolieren und zu schützen. Dies ist besonders wichtig für Umgebungen, in denen Assets mit verschiedenen Sicherheitseigenschaften nebeneinander existieren. Bei dieser Strategie werden bauliche Maßnahmen eingesetzt, wie z. B. getrennte Eingänge, dedizierte Versorgungssysteme, Fallen, abgeschottete HLK-Anlagen, physisch getrennte Netzwerkinfrastrukturen und zugangskontrollierte Zonen, um die seitliche Bewegung von Bedrohungen zu verhindern und gleichzeitig die Einhaltung von Vorschriften zu gewährleisten. Zu den üblichen Anwendungen gehören Bürogebäude mit mehreren Mietparteien, in denen verschiedene Institutionen eine Trennung benötigen, Colocation-Rechenzentren mit kundenspezifischer Geräteisolierung, gemeinsam genutzte Regierungseinrichtungen mit unterschiedlichen Klassifizierungsanforderungen und Campus-Umgebungen, in denen miteinander verbundene Gebäude unterschiedliche Sicherheitsperimeter aufrechterhalten müssen - all dies unterstützt ein umfassendes Risikomanagement und die Eindämmung von Vorfällen. Maßnahmen können z.B. intelligenten Schlössern an Käfigtüren und Sensoren an den Seitenwänden von Serverracks sein.

### → INF.2.A1 — Festlegung von Anforderungen (B) [Haustechnik, Planende]
  1. Für ein Rechenzentrum MÜSSEN angemessene technische und organisatorische Vorgaben definiert und umgesetzt werden.
  2. Wenn ein Rechenzentrum geplant wird oder geeignete Räumlichkeiten ausgewählt werden, MÜSSEN auch geeignete Sicherheitsmaßnahmen unter Berücksichtigung des Schutzbedarfs der IT-Komponenten (insbesondere der Verfügbarkeit) mit geplant werden.
  3. Ein Rechenzentrum MUSS insgesamt als geschlossener Sicherheitsbereich konzipiert werden.
  4. Es MUSS zudem unterschiedliche Sicherheitszonen aufweisen. **◀ ZITIERT**
  5. Dafür MÜSSEN z. B. Verwaltungs-, Logistik-, IT-Betriebs- und Support-Bereiche klar voneinander getrennt werden.
  6. Im Falle eines Serverraums SOLLTE geprüft werden, ob unterschiedliche Sicherheitszonen eingerichtet werden können. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `intersects-with` | Fundrichtung: beide
  Begründung: (Teilanforderung 4) Die Maßnahme GEB.5.3 fordert mit der physischen Mikrosegmentierung genau die Schaffung physischer Grenzen und zugangskontrollierter Zonen zur Trennung unterschiedlicher Sicherheitsbereiche für IT-Systeme.
- **Satz 6** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 6) Die Maßnahme GEB.5.3 fordert die physische Mikrosegmentierung zur Schaffung getrennter Sicherheitsbereiche für IT-Systeme, was der Einrichtung unterschiedlicher Sicherheitszonen in einem Serverraum entspricht.

### → INF.1.A23 — Bildung von Sicherheitszonen (H) [Planende]
  1. Räume ähnlichen Schutzbedarfs SOLLTEN in Zonen zusammengefasst werden, um vergleichbare Risiken einheitlich behandeln und Kosten für erforderliche Sicherheitsmaßnahmen reduzieren zu können. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 1) Satz 1 fordert die Bildung und physische Trennung von Sicherheitszonen nach Schutzbedarf, was der allgemeinen Fassung der physischen Mikrosegmentierung entspricht.

### → INF.2.A6 — Zutrittskontrolle (B) [Haustechnik]
  1. Der Zutritt zum Rechenzentrum MUSS kontrolliert werden.
  2. Zutrittsrechte MÜSSEN gemäß der Vorgaben des Bausteins ORP.4 Identitäts- und Berechtigungsmanagement vergeben werden.
  3. Für im Rechenzentrum tätige Personen MUSS sichergestellt werden, dass diese keinen Zutritt zu IT-Systemen außerhalb ihres Tätigkeitsbereiches erhalten. **◀ ZITIERT**
  4. Alle Zutrittsmöglichkeiten zum Rechenzentrum MÜSSEN mit Zutrittskontrolleinrichtungen ausgestattet sein.
  5. Jeder Zutritt zum Rechenzentrum MUSS von der Zutrittskontrolle individuell erfasst werden.
  6. Im Falle eines Serverraums SOLLTE geprüft werden, ob eine Überwachung aller Zutrittsmöglichkeiten sinnvoll ist.
  7. Es MUSS regelmäßig kontrolliert werden, ob die Regelungen zum Einsatz einer Zutrittskontrolle eingehalten werden.
  8. Die Anforderungen der Institution an ein Zutrittskontrollsystem MÜSSEN in einem Konzept ausreichend detailliert dokumentiert werden.
- **Satz 3** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die physische Mikrosegmentierung (z. B. durch Rack- und Käfigtrennung in Rechenzentren) dient genau dazu, den physischen Zugriff auf IT-Systeme innerhalb einer Einrichtung auf den jeweiligen Zuständigkeitsbereich zu beschränken.


## GEB.9.1.1 — Vorausschauende Lastanalyse  [1 Paare]

**Statement (normativ):** Gebäudemanagement für Standorte KANN die bedarfsgerechte Stromversorgung {{ insert: param, geb.9.1.1-prm1 }} vorausschauend überprüfen.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** erhöht
**Guidance (nicht normativ):** Die prädiktive Lastanalyse in Stromversorgungssystemen bezieht sich auf die ausgefeilte Analyse von elektrischen Lastmustern, einschließlich Oberschwingungen der Stromqualität, um den zukünftigen Stromverbrauch und Qualitätsprobleme vorherzusagen, bevor sie auftreten. Sie kann in Bereichen, in denen die Stromversorgung von höchster Bedeutung ist, helfen, die kontinuierliche Verfügbarkeit der IT-Infrastruktur durch Überwachung und Vorhersage potenzieller Stromanomalien sicherzustellen, die die Systemintegrität gefährden könnten. Im Gegensatz zu reaktiven Ansätzen, die Probleme erst nach ihrem Auftreten angehen, werden bei der vorausschauenden Lastanalyse fortschrittliche Algorithmen zur Analyse historischer Stromverbrauchsdaten, harmonischer Verzerrungen und Spannungsschwankungen eingesetzt, um Muster zu erkennen, die auf bevorstehende Stromversorgungsprobleme hinweisen. Die Implementierung kann mit Netzqualitätsanalysatoren an kritischen Infrastrukturpunkten, Integration mit SCADA-Systemen und durch Analyse mit Algorithmen des maschinellen Lernens, die Netzanomalien mit bestimmten Betriebsbedingungen korrelieren, geschehen. Eine regelmäßige Validierung der Vorhersagemodelle anhand tatsächlicher Vorfälle hilft die Analyse zu verbessern, während die Integration mit automatisierten Energieverwaltungssystemen einen dynamischen Lastausgleich während vorhergesagter Stressperioden ermöglichen kann, wodurch sowohl die Stromqualität, als auch die Systemverfügbarkeit ohne menschliches Eingreifen aufrechterhalten werden.

### → INF.1.A2 — Angepasste Aufteilung der Stromkreise (B)
  1. Es MUSS regelmäßig überprüft werden, ob die Absicherung und Auslegung der Stromkreise noch den tatsächlichen Bedürfnissen genügen. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) Die G++-Maßnahme fordert die regelmäßige vorausschauende Überprüfung einer bedarfsgerechten Stromversorgung und deckt damit die regelmäßige Prüfung der bedarfsgerechten Auslegung und Absicherung inhaltlich ab.


## GEB.9.3 — Notaus  [3 Paare]

**Statement (normativ):** Gebäudemanagement für Standorte KANN eine Notausschaltung für die Versorgungseinrichtungen installieren.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** erhöht
**Guidance (nicht normativ):** Eine Notausschaltung bezeichnet in diesem Kontext eine zentral verfügbare, technisch implementierte Vorrichtung, mit der im Gefahrenfall die Energieversorgung kritischer Versorgungseinrichtungen wie Strom, Gas oder Klimaanlagen unmittelbar und vollständig unterbrochen werden kann. Der Sinn und Zweck einer solchen Einrichtung liegt darin, Gefahren für Menschen, Technik und Informationen schnell eingrenzen zu können: Ein unkontrollierter Brand könnte sich durch weiterlaufende Klimageräte verstärken, ein Stromschlag durch beschädigte Leitungen könnte Menschen gefährden, oder ein Wasserschaden durch defekte Kühlung könnte weitere Systeme zerstören. Gleichzeitig kann eine sofortige Unterbrechung der Energiezufuhr Folgeschäden eindämmen, indem Brandlast reduziert oder die Ausbreitung toxischer Gase verhindert werden kann. Zur Umsetzung kann eine Institution beispielsweise (1) physische Notausschalter an klar gekennzeichneten, jederzeit zugänglichen Stellen nahe den Ausgängen oder im Leitstand installieren, (2) die Schalter so konzipieren, dass sie nur für definierte Versorgungskreise wie IT-Serverräume oder Technikzonen wirken und nicht die gesamte Einrichtung unkontrolliert lahmlegen, und (3) ergänzende visuelle Hinweise oder Leitsymbole anbringen, die die Bedienung im Ernstfall erleichtern.

### → INF.2.A4 — Notabschaltung der Stromversorgung (B) [Haustechnik]
  1. Es MUSS geeignete Möglichkeiten geben, elektrische Verbraucher im Rechenzentrum spannungsfrei zu schalten. **◀ ZITIERT**
  2. Dabei MUSS darauf geachtet werden, ob und wie eine vorhandene USV räumlich und funktional in die Stromversorgung eingebunden ist.
  3. Werden klassische Not-Aus-Schalter eingesetzt, MUSS darauf geachtet werden, dass darüber nicht das komplette Rechenzentrum abgeschaltet wird. **◀ ZITIERT**
  4. Die Notabschaltung MUSS sinnvoll parzelliert und zielgerichtet erfolgen. **◀ ZITIERT**
  5. Alle Not-Aus-Schalter MÜSSEN so geschützt sein, dass sie nicht unbeabsichtigt oder unbefugt betätigt werden können.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) Die Installation einer Notausschaltung für die Energie- und Stromversorgungseinrichtungen gemäß GEB.9.3 deckt die Bereitstellung von Möglichkeiten zum Spannungsfreischalten elektrischer Verbraucher inhaltlich ab.
- **Satz 3** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die Maßnahme GEB.9.3 umfasst die Installation und Konzeption von Notausschaltungen, die gezielt auf definierte Versorgungskreise wirken und ein unkontrolliertes Abschalten der gesamten Einrichtung verhindern.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) GEB.9.3 beschreibt die zielgerichtete Konzeption von Notausschaltungen für definierte Versorgungskreise, um eine unkontrollierte Gesamtabschaltung zu vermeiden, was die geforderte sinnvolle Parzellierung abdeckt.


## GEB.10.1.3 — Redundante Klimatisierung  [4 Paare]

**Statement (normativ):** Gebäudemanagement für Standorte KANN redundante Klimasysteme installieren.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** erhöht
**Guidance (nicht normativ):** Redundant ist eine Klimatisierung, wenn alle zu ihrer Funktionsfähigkeit erforderlichen Komponenten und Anbindungen redundant sind, d.h. kein einzelner Fehlerpunkt zu einem Ausfall führen würde (Single Point of Failure).

### → INF.2.A16 — Klimatisierung im Rechenzentrum (S) [Planende]
  1. Es SOLLTE sichergestellt werden, dass im Rechenzentrum geeignete klimatische Bedingungen geschaffen und aufrechterhalten werden.
  2. Die Klimatisierung SOLLTE für das Rechenzentrum ausreichend dimensioniert sein.
  3. Alle relevanten Werte SOLLTEN ständig überwacht werden.
  4. Weicht ein Wert von der Norm ab, SOLLTE automatisch alarmiert werden.
  5. Die Klimaanlagen SOLLTEN in IT-Betriebsbereichen möglichst ausfallsicher sein. **◀ ZITIERT**
- **Satz 5** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) Die G++-Maßnahme GEB.10.1.3 adressiert die geforderte Ausfallsicherheit der Klimaanlagen direkt durch die Installation redundanter Klimasysteme ohne Single Point of Failure.

### → INF.5.A19 — Redundanz des Raumes für technische Infrastruktur (H) [Planende]
  1. Der Raum SOLLTE redundant ausgelegt werden.
  2. Beide Räume SOLLTEN eine eigene Elektrounterverteilung erhalten, die direkt von der Niederspannungshauptverteilung (NSHV) versorgt wird.
  3. Beide Räume SOLLTEN unterschiedlichen Brandabschnitten zugeordnet sein und, sofern erforderlich, jeweils über eine eigene raumlufttechnische Anlage verfügen. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die Installation redundanter Klimasysteme nach GEB.10.1.3 deckt die Forderung nach einer jeweils eigenen raumlufttechnischen Anlage für die redundanten Räume inhaltlich ab.

### → INF.5.A24 — Lüftung und Kühlung (H) [Planende, Haustechnik, Wartungspersonal]
  1. Die Lüftungs- und Kühltechnik SOLLTE betriebsredundant ausgelegt werden. **◀ ZITIERT**
  2. Es SOLLTE sichergestellt werden, dass diese Anlagen regelmäßig gewartet werden.
  3. Bei sehr hohem Schutzbedarf SOLLTE auch eine Wartungsredundanz vorhanden sein. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme GEB.10.1.3 fordert die Installation redundanter Klimasysteme zur Vermeidung von Single Points of Failure, was die geforderte betriebsredundante Auslegung der Kühltechnik direkt abdeckt.
- **Satz 3** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die Maßnahme GEB.10.1.3 deckt mit der Installation redundanter Klimasysteme ohne Single Point of Failure die geforderte Redundanz (inklusive Wartungsredundanz) für Klimatechnik ab.

