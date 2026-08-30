# Review-Dossier Praktik DEV

Praktik DEV: 31 Controls mit Mapping, 117 Paare gesamt. Gesampelt: 5 Controls (max/min/median Paarzahl + 2 zufällig).

## DEV.1.1 — Verfahren und Regelungen  [13 Paare]

**Statement (normativ):** Entwicklung MUSS Verfahren und Regelungen zur Entwicklung von IT-Produkten verankern.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Für ein Verfahren zur Softwareentwicklung siehe BSI TR-03185. Entwickelt die Institution im Informationsverbund keine IT-Produkte, so sind diese und alle anderen Anforderungen der Praktik entbehrlich. Die bei der Festlegung des Verfahrens im Einzelnen zu berücksichtigenden Inhalte ergeben sich aus den Anforderungen dieser Praktik.

### → APP.1.1.A10 — Regelung der Software-Entwicklung durch Endbenutzende (S)
  1. Für die Software-Entwicklung auf Basis von Office-Anwendungen, z. B. mit Makros, SOLLTEN verbindliche Regelungen getroffen werden (siehe auch APP.1.1.A2 Einschränken von Aktiven Inhalten). **◀ ZITIERT**
  2. Zunächst SOLLTE in jeder Institution die Grundsatzentscheidung getroffen werden, ob solche Eigenentwicklungen überhaupt erwünscht sind.
  3. Die Entscheidung SOLLTE in den betroffenen Sicherheitsrichtlinien dokumentiert werden.
  4. Werden Eigenentwicklungen erlaubt, SOLLTE ein Verfahren für den Umgang mit entsprechenden Funktionen der Office-Produkte für die Endbenutzenden erstellt werden. **◀ ZITIERT**
  5. Zuständigkeiten SOLLTEN klar definiert werden.
  6. Alle notwendigen Informationen über die erstellten Anwendungen SOLLTEN angemessen dokumentiert werden.
  7. Aktuelle Versionen der Regelungen SOLLTEN allen betroffenen Benutzenden zeitnah zugänglich gemacht und von diesen beachtet werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) DEV.1.1 fordert allgemein die Verankerung von Verfahren und Regelungen zur Entwicklung, was die Erstellung verbindlicher Regelungen für Software-Entwicklungen (wie Office-Makros) abdeckt.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) DEV.1.1 fordert allgemein die Verankerung von Verfahren und Regelungen zur Softwareentwicklung, was die Erstellung eines Verfahrens für Eigenentwicklungen durch Endbenutzende aus Satz 4 abdeckt.

### → APP.4.2.A26 — Schutz von selbstentwickeltem Code im SAP-ERP-System (S)
  1. Es SOLLTE ein Custom-Code-Managementprozess definiert werden, damit selbstentwickelter Code ausgetauscht oder entfernt wird, falls er durch SAP-Standard-Code ersetzt werden kann oder er nicht mehr benutzt wird.
  2. Ferner SOLLTEN die Anforderungen aus der Richtlinie für die Entwicklung von ABAP-Programmen berücksichtigt werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) DEV.1.1 fordert allgemein die Verankerung von Verfahren und Regelungen zur Softwareentwicklung, was die Berücksichtigung und Einhaltung spezifischer Entwicklungsrichtlinien (wie für ABAP) einschließt.

### → APP.4.3.A19 — Schutz vor schädlichen Datenbank-Skripten (S) [Entwickelnde]
  1. Werden Datenbank-Skripte entwickelt, SOLLTEN dafür verpflichtende Qualitätskriterien definiert werden (siehe CON.8 Software-Entwicklung). **◀ ZITIERT**
  2. Datenbank-Skripte SOLLTEN ausführlichen Funktionstests auf gesonderten Testsystemen unterzogen werden, bevor sie produktiv eingesetzt werden.
  3. Die Ergebnisse SOLLTEN dokumentiert werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) DEV.1.1 verlangt die Verankerung von Verfahren und Regelungen für die Entwicklung, was als allgemeinere Fassung die Festlegung verpflichtender Qualitätskriterien für Skripte und Software umfasst.

### → APP.4.6.A5 — Erstellung einer Richtlinie für die ABAP-Entwicklung (S)
  1. Es SOLLTE eine Richtlinie für die Entwicklung von ABAP-Programmen erstellt werden. **◀ ZITIERT**
  2. Die Richtlinie SOLLTE neben Namenskonventionen auch Vorgaben zu ABAP-Elementen beinhalten, die verwendet bzw. nicht verwendet werden dürfen.
  3. Die Anforderungen aus diesem Baustein SOLLTEN in die Richtlinie aufgenommen werden.
  4. Die Richtlinie SOLLTE für die Entwickelnden verbindlich sein.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) DEV.1.1 verlangt das allgemeine Verankern von Verfahren und Regelungen für die Entwicklung, was die Erstellung einer spezifischen ABAP-Entwicklungsrichtlinie inhaltlich umfasst.

### → APP.7.A1 — Erweiterung der Planung des Software-Einsatzes um Aspekte von Individualsoftware (B)
  1. Die Planung des Software-Einsatzes MUSS um Aspekte von Individualsoftware ergänzt werden, indem definiert wird, wer dafür zuständig ist, die Software-Entwicklung bzw. den Auftragnehmenden zu steuern und zu koordinieren, sowie in was für einen organisatorischen Rahmen die Software zu entwickeln ist (Projektmanagementmodell). **◀ ZITIERT**
  2. Individualsoftware SOLLTE im Rahmen eines Entwicklungsprojektes entwickelt werden.
  3. Das Entwicklungsprojekt sollte anhand eines Ablaufplans zeitlich grob geplant werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) DEV.1.1 verlangt die Verankerung von Verfahren und Regelungen zur Entwicklung von IT-Produkten, was den geforderten organisatorischen Rahmen und das Vorgehensmodell für die Individualsoftware-Entwicklung grundlegend abdeckt.

### → APP.7.A2 — Festlegung von Sicherheitsanforderungen an den Prozess der Software-Entwicklung (B)
  1. Die Institution MUSS klare Anforderungen an den Prozess der Software-Entwicklung definieren. **◀ ZITIERT**
  2. Aus den Anforderungen MUSS hervorgehen, in was für einer Umgebung die Software entwickelt werden darf und welche technischen und organisatorischen Maßnahmen von Seiten der beauftragten Software-Entwickelnden umzusetzen sind.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) DEV.1.1 deckt die Forderung nach der Festlegung von Vorgaben für die Software-Entwicklung durch die Verankerung von Verfahren und Regelungen zur Entwicklung direkt ab.

### → APP.7.A5 — Geeignete Steuerung der Anwendungsentwicklung (S)
  1. Bei der Entwicklung von Individualsoftware SOLLTE ein geeignetes Steuerungs- und Projektmanagementmodell verwendet werden. **◀ ZITIERT**
  2. Hierbei SOLLTE das ausgewählte Modell mit dem Auftragnehmenden abgestimmt werden.
  3. Bei der Steuerung SOLLTE es berücksichtigt werden.
  4. Es SOLLTE insbesondere berücksichtigt werden, dass das benötigte Personal ausreichend qualifiziert ist.
  5. Alle relevanten Phasen SOLLTEN während des Lebenszyklus der Software abgedeckt werden.
  6. Außerdem SOLLTE es ein geeignetes Entwicklungsmodell, ein Risikomanagement sowie Qualitätsziele enthalten.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) DEV.1.1 deckt die Forderung nach der Verwendung eines Steuerungs- und Entwicklungsmodells als allgemeine Pflicht zur Verankerung von Verfahren und Regelungen zur Softwareentwicklung ab.

### → CON.8.A11 — Erstellung einer Richtlinie für die Software-Entwicklung (S)
  1. Es SOLLTE eine Richtlinie für die Software-Entwicklung erstellt und aktuell gehalten werden. **◀ ZITIERT**
  2. Die Richtlinie SOLLTE neben Namenskonventionen auch Vorgaben zu Elementen beinhalten, die verwendet bzw. nicht verwendet werden dürfen.
  3. Die relevanten Anforderungen aus diesem Baustein SOLLTEN in die Richtlinie aufgenommen werden.
  4. Die Richtlinie SOLLTE für die Entwickelnden verbindlich sein.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) DEV.1.1 fordert die grundlegende Verankerung von Verfahren und Regelungen für die Entwicklung, was der allgemeinen Etablierung einer Richtlinie für die Software-Entwicklung entspricht.

### → CON.8.A16 — Geeignete Steuerung der Software-Entwicklung (S)
  1. Bei einer Software-Entwicklung SOLLTE ein geeignetes Steuerungs- bzw. Projektmanagementmodell auf Basis des ausgewählten Vorgehensmodells verwendet werden. **◀ ZITIERT**
  2. Das Steuerungs- bzw. Projektmanagementmodell SOLLTE in die Richtlinie zur Software Entwicklung integriert werden.
  3. Dabei SOLLTEN insbesondere die benötigten Qualifikationen beim Personal und die Abdeckung aller relevanten Phasen während des Lebenszyklus der Software berücksichtigt werden.
  4. Für das Vorgehensmodell SOLLTE ein geeignetes Risikomanagement festgelegt werden.
  5. Außerdem SOLLTEN geeignete Qualitätsziele für das Entwicklungsprojekt definiert werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Das Verankern von Verfahren und Regelungen zur Entwicklung von IT-Produkten deckt die allgemeine Verwendung eines geeigneten Steuerungs- bzw. Vorgehensmodells für die Entwicklung ab.

### → CON.8.A2 — Auswahl eines Vorgehensmodells (B)
  1. Ein geeignetes Vorgehensmodell zur Software-Entwicklung MUSS festgelegt werden. **◀ ZITIERT**
  2. Anhand des gewählten Vorgehensmodells MUSS ein Ablaufplan für die Software-Entwicklung erstellt werden.
  3. Die Sicherheitsanforderungen der Auftraggebenden an die Vorgehensweise MÜSSEN im Vorgehensmodell integriert werden.
  4. Das ausgewählte Vorgehensmodell, einschließlich der festgelegten Sicherheitsanforderungen, MUSS eingehalten werden. **◀ ZITIERT**
  5. Das Personal SOLLTE in der Methodik des gewählten Vorgehensmodells geschult sein.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) Das Verankern von Verfahren und Regelungen zur Entwicklung von IT-Produkten umfasst inhaltlich die Festlegung eines Vorgehensmodells für die Software-Entwicklung.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Das Verankern von Verfahren und Regelungen zur Entwicklung umfasst als übergeordneter Grundsatz auch die verbindliche Einhaltung des festgelegten Vorgehensmodells und der Sicherheitsanforderungen.

### → INF.14.A7 — Festlegung einer Sicherheitsrichtlinie für die GA (S)
  1. Ausgehend von der allgemeinen Sicherheitsleitlinie der Institution und der übergreifenden Sicherheitsrichtlinie für das TGM SOLLTEN die Sicherheitsanforderungen an die GA, d. h. für alle GA-Systeme, in einer GA-Sicherheitsrichtlinie konkretisiert werden.
  2. Diese Richtlinie SOLLTE allen Personen, die an Planung, Beschaffung, Implementierung und Betrieb der GA-Systeme beteiligt sind, bekannt und Grundlage für deren Arbeit sein.
  3. Die Inhalte und die Umsetzung der geforderten Richtlinieninhalte SOLLTEN regelmäßig überprüft, gegebenenfalls angepasst und die Ergebnisse der Prüfung nachvollziehbar dokumentiert werden.
  4. In der Sicherheitsrichtlinie SOLLTEN auch die Vorgaben an Entwicklung und Test für den Einsatz von GA-Systemen spezifiziert werden. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) DEV.1.1 fordert als allgemeinere Fassung das Verankern von Verfahren und Regelungen für die Entwicklung, was die Spezifikation von Entwicklungsvorgaben inhaltlich abdeckt.


## DEV.4.4 — Integrität externer Software  [3 Paare]

**Statement (normativ):** Entwicklung für Anwendungen SOLLTE die Integrität externer Softwareartefakte und -Schnittstellen vor dem Release testen.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Gemeint ist damit sowohl die technische Unversehrtheit (z. B. durch kryptografische Prüfungen wie Hash- oder Signaturvalidierung) als auch die inhaltliche Zuverlässigkeit (z. B. keine eingeschleusten Schadfunktionen oder versteckte Abhängigkeiten). Der Sinn und Zweck dieser Anforderung liegt darin, die Risiken durch unsichere oder manipulierte Fremdkomponenten zu reduzieren. So könnte ein Angreifer Schadcode in eine weit verbreitete Bibliothek einschleusen, die dann unbemerkt in der Anwendung landet, oder eine Abhängigkeit könnte im Hintergrund auf nicht mehr gepflegte Versionen verweisen. Eine wirksame Integritätsprüfung kann verhindern, dass fehlerhafte oder kompromittierte Bausteine in produktive Anwendungen gelangen und kann damit auch die Abhängigkeit von nicht vertrauenswürdigen Quellen abmildern. Zur Umsetzung können (1) Hashwerte oder digitale Signaturen von Bibliotheken mit den Referenzwerten der Hersteller verglichen werden, (2) der Bezug externer Pakete über offizielle, verifizierte Repositories, statt über inoffizielle Quellen stattfinden, und (3) in der Build-Pipeline eine automatisierte Integritätsprüfung eingerichtet sein, die verdächtige oder unvollständige Bibliotheken blockieret. Ergänzend kann eine institutionseigene Allowlist gepflegt werden, die geprüfte Versionen von Bibliotheken enthält, sodass Entwickler nicht unkontrolliert beliebige Abhängigkeiten einbinden. Ein praktischer Tipp kann sein, die Prüfmechanismen möglichst früh im Entwicklungsprozess zu automatisieren, um spätere manuelle Nacharbeiten oder Verzögerungen vor einem Release zu vermeiden.

### → CON.8.A6 — Verwendung von externen Bibliotheken aus vertrauenswürdigen Quellen (B)
  1. Wird im Rahmen des Entwicklungs- und Implementierungsprozesses auf externe Bibliotheken zurückgegriffen, MÜSSEN diese aus vertrauenswürdigen Quellen bezogen werden.
  2. Bevor externe Bibliotheken verwendet werden, MUSS deren Integrität sichergestellt werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) DEV.4.4 fordert explizit das Testen bzw. Sicherstellen der Integrität externer Softwareartefakte und deckt damit die Prüfung der Integrität externer Bibliotheken direkt ab.

### → APP.6.A4 — Regelung für die Installation und Konfiguration von Software (B) [Fachverantwortliche]
  1. Die Installation und Konfiguration der Software MUSS durch den IT-Betrieb so geregelt werden, dass die Software nur mit dem geringsten notwendigen Funktionsumfang installiert und ausgeführt wird, die Software mit den geringsten möglichen Berechtigungen ausgeführt wird, die datensparsamsten Einstellungen (in Bezug auf die Verarbeitung von personenbezogenen Daten) konfiguriert werden sowie alle relevanten Sicherheitsupdates und -patches installiert sind, bevor die Software produktiv eingesetzt wird.
  2. Hierbei MÜSSEN auch abhängige Komponenten (unter anderem Laufzeitumgebungen, Bibliotheken, Schnittstellen sowie weitere Programme) mitbetrachtet werden.
  3. Der IT-Betrieb MUSS in Abstimmung mit den Fachverantwortlichen festlegen, wer die Software wie installieren darf.
  4. Idealerweise SOLLTE Software immer zentral durch den IT-Betrieb installiert werden.
  5. Ist es erforderlich, dass die Software (teilweise) manuell installiert wird, dann MUSS der IT-Betrieb eine Installationsanweisung erstellen, in der klar geregelt wird, welche Zwischenschritte zur Installation durchzuführen und welche Konfigurationen vorzunehmen sind.
  6. Darüber hinaus MUSS der IT-Betrieb regeln, wie die Integrität der Installationsdateien überprüft wird.
  7. Falls zu einem Installationspaket digitale Signaturen oder Prüfsummen verfügbar sind, MÜSSEN mit diesen die Integrität überprüft werden. **◀ ZITIERT**
  8. Sofern erforderlich, SOLLTE der IT-Betrieb eine sichere Standardkonfiguration der Software festlegen, mit der die Software konfiguriert wird.
  9. Die Standardkonfiguration SOLLTE dokumentiert werden.
- **Satz 7** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 7) Satz 7 fordert die Überprüfung der Integrität von Softwarepaketen anhand digitaler Signaturen oder Prüfsummen, was sich inhaltlich mit der Integritätsprüfung externer Software in DEV.4.4 überschneidet.

### → CON.8.A20 — Überprüfung von externen Komponenten (B)
  1. Unbekannte externe Komponenten (bzw. Programm-Bibliotheken), deren Sicherheit nicht durch etablierte und anerkannte Peer-Reviews oder vergleichbares sichergestellt werden kann, MÜSSEN auf Schwachstellen überprüft werden.
  2. Alle externen Komponenten MÜSSEN auf potentielle Konflikte überprüft werden.
  3. Die Integrität von externen Komponenten MUSS durch Prüfsummen oder kryptographische Zertifikate überprüft werden. **◀ ZITIERT**
  4. Darüber hinaus SOLLTEN keine veralteten Versionen von externen Komponenten in aktuellen Entwicklungsprojekten verwendet werden.
- **Satz 3** | Relation GS++→ED23: `intersects-with` | Fundrichtung: beide
  Begründung: (Teilanforderung 3) DEV.4.4 verlangt explizit die Überprüfung der Integrität externer Softwareartefakte, unter anderem durch kryptografische Validierungen wie Hashwerte oder Signaturen.


## DEV.5.2 — Information über Zeitraum für Updates  [1 Paare]

**Statement (normativ):** Entwicklung für Anwendungen SOLLTE Auftraggeber über den festgelegten Zeitraum für Sicherheitsupdates informieren.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Stellen Sie den Empfängern der Software Informationen darüber bereit, wie lange Sicherheitsaktualisierungen gewährleistet werden und wie diese bezogen werden können.

### → SYS.3.2.1.A5 — Updates von Betriebssystem und Apps (B)
  1. Bereits bei der Auswahl von zu beschaffenden mobilen Geräten MUSS die Institution darauf achten, dass die herstellende Institution angibt, über welchen geplanten Nutzungszeitraum Sicherheitsaktualisierungen für die Geräte bereitgestellt werden. **◀ ZITIERT**
  2. Ältere Geräte, für die keine Aktualisierungen mehr bereitgestellt werden, MÜSSEN ausgesondert und durch von der herstellenden Institution unterstützte Geräte ersetzt werden.
  3. Apps SOLLTEN ebenfalls NICHT mehr eingesetzt werden, wenn sie nicht mehr durch die herstellende Institution unterstützt werden.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 1) Satz 1 fordert das Vorliegen von Herstellerangaben zum Bereitstellungszeitraum von Sicherheitsaktualisierungen bei der Geräteauswahl und bildet damit das beschaffungsseitige Pendant zur Informationspflicht aus DEV.5.2.


## DEV.1.2 — Regelmäßige Überprüfung  [1 Paare]

**Statement (normativ):** Entwicklung MUSS die Verfahren und Regelungen {{ insert: param, dev.1.2-prm1 }} und anlassbezogen auf Aktualität überprüfen.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Eine geplante Überprüfung der etablierten Verfahren und Regelungen dient dazu festzustellen, ob diese noch wirksam, effizient und an die aktuellen Gegebenheiten angepasst sind. Eine anlassbezogene Überprüfung wird durch spezifische Ereignisse ausgelöst, wie etwa einen schwerwiegenden Sicherheitsvorfall, eine strategische Neuausrichtung der IT oder neue gesetzliche Anforderungen. Der Zweck dieser Anforderung ist es, die kontinuierliche Verbesserung und Anpassungsfähigkeit des Prozesses sicherzustellen, da veraltete Regelungen neuen technologischen Entwicklungen oder Bedrohungen nicht mehr gerecht werden könnten; ein vor Jahren für monolithische Anwendungen konzipierter Prozess ist beispielsweise für agile Entwicklungsmethoden oder Microservice-Architekturen ungeeignet. Die regelmäßige Überprüfung kann die Effektivität des Sicherheitsmanagements langfristig aufrechterhalten und die Resilienz der Institution stärken.

### → CON.8.A11 — Erstellung einer Richtlinie für die Software-Entwicklung (S)
  1. Es SOLLTE eine Richtlinie für die Software-Entwicklung erstellt und aktuell gehalten werden. **◀ ZITIERT**
  2. Die Richtlinie SOLLTE neben Namenskonventionen auch Vorgaben zu Elementen beinhalten, die verwendet bzw. nicht verwendet werden dürfen.
  3. Die relevanten Anforderungen aus diesem Baustein SOLLTEN in die Richtlinie aufgenommen werden.
  4. Die Richtlinie SOLLTE für die Entwickelnden verbindlich sein.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) DEV.1.2 deckt mit der regelmäßigen und anlassbezogenen Überprüfung auf Aktualität die im Satz geforderte Pflicht ab, die Richtlinie aktuell zu halten.


## DEV.4.11 — Test bei Änderungen am Quellcode  [5 Paare]

**Statement (normativ):** Entwicklung für Anwendungen SOLLTE Änderungen am Quellcode im Einklang mit den Verfahren und Regelungen für Änderungen und Tests testen.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** „Änderungen am Quellcode“ (engl. source code changes) bezeichnet im gegebenen Kontext sämtliche Modifikationen, die an den Programmbestandteilen einer Anwendung vorgenommen werden, also etwa neue Funktionen, Fehlerkorrekturen oder Anpassungen an Schnittstellen. Fehlerhafte oder ungetestete Anpassungen könnten etwa zu Sicherheitslücken, Datenverlust oder Instabilitäten im Betrieb führen, wohingegen eine strukturierte Prüfung verhindern kann, dass bekannte Schwachstellen erneut auftreten oder unbeabsichtigte Seiteneffekte entstehen. Solche Änderungen sind daher als Teil des Change Managements zu betrachten, dessen Anforderungen im Einzelnen in der Praktik Änderungen und Tests zu finden sind. Zur praktischen Umsetzung kann eine Institution jede Änderung automatisiert durch Static Application Security Testing (SAST) prüfen, wodurch potenzielle Schwachstellen direkt im Quellcode erkannt werden können. Ergänzend ist es sinnvoll Dynamic Application Security Testing (DAST) einzusetzen, um die lauffähige Anwendung in einer Testumgebung gegen typische Angriffe wie SQL-Injection oder Cross-Site-Scripting zu überprüfen. Sinnvolle Maßnahmen können dabei sein: (1) Aufbau einer Continuous-Integration-Pipeline, die automatisierte Unit-, Integrations- und Sicherheitstests einbindet und Ergebnisse konsolidiert darstellt, (2) Durchführung von manuellen explorativen Tests in einer isolierten Testumgebung, um auch unerwartete Nutzungsmuster zu prüfen, (3) Einsatz von Regressionstests, die sicherstellen können, dass neue Änderungen keine bestehenden Funktionen beeinträchtigen. Eine Institution kann damit die Qualitätssicherung stärken und gleichzeitig Angriffsflächen durch fehlerhafte Änderungen reduzieren.

### → APP.4.3.A19 — Schutz vor schädlichen Datenbank-Skripten (S) [Entwickelnde]
  1. Werden Datenbank-Skripte entwickelt, SOLLTEN dafür verpflichtende Qualitätskriterien definiert werden (siehe CON.8 Software-Entwicklung).
  2. Datenbank-Skripte SOLLTEN ausführlichen Funktionstests auf gesonderten Testsystemen unterzogen werden, bevor sie produktiv eingesetzt werden. **◀ ZITIERT**
  3. Die Ergebnisse SOLLTEN dokumentiert werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) DEV.4.11 verlangt das systematische Testen von Codeänderungen, was als allgemeinere Fassung der Pflicht zum Funktionstest von Datenbank-Skripten vor dem Produktiveinsatz dient.

### → APP.4.6.A22 — Einsatz von ABAP-Codeanalyse Werkzeugen (H)
  1. Zur automatisierten Überprüfung von ABAP-Code auf sicherheitsrelevante Programmierfehler, funktionale und technische Fehler sowie auf qualitative Schwachstellen SOLLTE ein ABAP-Codeanalyse-Werkzeug eingesetzt werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) DEV.4.11 fordert das Testen von Quellcodeänderungen (inklusive automatisierter statischer Codeanalysen wie SAST), was den Einsatz von Codeanalyse-Werkzeugen für ABAP als technologiespezifischen Anwendungsfall abdeckt.

### → CON.8.A7 — Durchführung von entwicklungsbegleitenden Software-Tests (B) [Testende, Entwickelnde]
  1. Schon bevor die Software im Freigabeprozess getestet und freigegeben wird, MÜSSEN entwicklungsbegleitende Software-Tests durchgeführt und der Quellcode auf Fehler gesichtet werden. **◀ ZITIERT**
  2. Hierbei SOLLTEN bereits die Fachverantwortlichen des Auftraggebenden oder der beauftragenden Fachabteilung beteiligt werden.
  3. Die entwicklungsbegleitenden Tests MÜSSEN die funktionalen und nichtfunktionalen Anforderungen der Software umfassen.
  4. Die Software-Tests MÜSSEN dabei auch Negativtests abdecken.
  5. Zusätzlich MÜSSEN auch alle kritischen Grenzwerte der Eingabe sowie der Datentypen überprüft werden.
  6. Testdaten SOLLTEN dafür sorgfältig ausgewählt und geschützt werden.
  7. Darüber hinaus SOLLTE eine automatische statische Code-Analyse durchgeführt werden.
  8. Die Software MUSS in einer Test- und Entwicklungsumgebung getestet werden, die getrennt von der Produktionsumgebung ist.
  9. Außerdem MUSS getestet werden, ob die Systemvoraussetzungen für die vorgesehene Software ausreichend dimensioniert sind.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) G++ DEV.4.11 verlangt das Testen von Änderungen am Quellcode und deckt damit die Durchführung entwicklungsbegleitender Software-Tests inhaltlich ab.

### → OPS.1.1.6.A12 — Durchführung von Regressionstests (S) [Testende]
  1. Wenn Software verändert wurde, SOLLTEN Regressionstests durchgeführt werden. **◀ ZITIERT**
  2. Hierbei SOLLTE überprüft werden, ob bisherige bestehende Sicherheitsmechanismen und -einstellungen durch das Update ungewollt verändert wurden.
  3. Regressionstests SOLLTEN vollständig durchgeführt werden und hierbei auch Erweiterungen sowie Hilfsmittel umfassen.
  4. Werden Testfälle ausgelassen, SOLLTE dies begründet und dokumentiert werden.
  5. Die durchgeführten Testfälle und die Testergebnisse SOLLTEN dokumentiert werden.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) DEV.4.11 fordert das Testen von Änderungen am Quellcode im Entwicklungskontext, was die Durchführung von Regressionstests bei veränderter Software inhaltlich abdeckt.

### → OPS.1.1.6.A2 — Durchführung von funktionalen Software-Tests (B) [Testende]
  1. Mit funktionalen Software-Tests MUSS die ordnungsgemäße und vollständige Funktion der Software überprüft werden. **◀ ZITIERT**
  2. Die funktionalen Software-Tests MÜSSEN so durchgeführt werden, dass sie den Produktivbetrieb nicht beeinflussen.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) DEV.4.11 fordert das Testen von Quellcodeänderungen mittels Unit-, Integrations- und Regressionstests und deckt damit die Durchführung funktionaler Software-Tests zur Überprüfung der ordnungsgemäßen Funktion im Entwicklungskontext ab.

