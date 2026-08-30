# Review-Dossier Praktik PERS

Praktik PERS: 29 Controls mit Mapping, 172 Paare gesamt. Gesampelt: 5 Controls (max/min/median Paarzahl + 2 zufällig).

## PERS.2.3.2 — Rollentrennung - Virtualisierung  [3 Paare]

**Statement (normativ):** Personal SOLLTE zwischen Administration von virtuellen Systemen und Virtualisierungslösungen eine Rollentrennung verankern.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Die Administration von virtuellen Systemen bezeichnet im hier relevanten Kontext die operative Verwaltung einzelner virtueller Gastsysteme (VMs, Container, etc.), einschließlich ihrer Bereitstellung, Konfiguration, Wartung und Zugriffskontrolle. Die Virtualisierungslösung hingegen ist hier die übergeordnete Plattform oder Hypervisor-Ebene, welche physische Ressourcen virtualisiert und mehreren virtuellen Gastsystemen bereitstellt. Diese Differenzierung entspricht dem Prinzip der Rollen- bzw. Funktionstrennung (separation of duties bzw. role separation), bei dem Aufgabenbereiche so abgegrenzt werden, dass keine Person gleichzeitig über kritische Systemebenen hinweg vollumfängliche Kontrolle besitzt. Damit wird ein wesentliches Sicherheitsprinzip technischer Infrastruktur auf die Virtualisierungsschichten übertragen. Der Zweck dieser Trennung liegt in der Begrenzung von Fehlerrisiken und der Prävention von Missbrauch – sowohl vorsätzlich als auch unbeabsichtigt. Eine Person, die zugleich die Virtualisierungsebene und virtuelle Systeme verwaltet, könnte durch Fehlkonfiguration, Nachlässigkeit oder Manipulation unbeabsichtigt erhebliche Auswirkungen auf eine Vielzahl von Systemen haben oder deren Nachvollziehbarkeit beeinträchtigen. Eine klare Rollentrennung kann dem vorbeugen, indem sie Kontrollmechanismen stärkt, die Integrität der Umgebung wahrt und Fehler früher erkennen lässt.

### → OPS.1.1.2.A21 — Regelung der IT-Administrationsrollen (B)
  1. Es MÜSSEN Rollen definiert werden, die ausschließlich zur IT-Administration vergeben werden.
  2. Administrationsrollen MÜSSEN aufgrund des tatsächlichen Bedarfs im Aufgabenbereich der IT-Administration nachvollziehbar vergeben werden.
  3. Alle notwendigen IT-Administrationstätigkeiten MÜSSEN durch Berechtigungen in den Administrationsrollen nach dem Minimalprinzip abgedeckt sein.
  4. Die IT-Administration unterschiedlicher Ebenen der IT-Komponenten, z. B. die Trennung von Betriebssystem- und Anwendungsadministration, MUSS bei der Konzeption der Administrationsrollen berücksichtigt werden. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die G++-Maßnahme PERS.2.3.2 stellt einen spezifischen Anwendungsfall der geforderten Rollentrennung über verschiedene Ebenen von IT-Komponenten dar, konkret zwischen der Hypervisor- und der Gastsystemebene.

### → SYS.1.5.A12 — Rechte- und Rollenkonzept für die Administration einer virtuellen Infrastruktur (S)
  1. Anhand der in der Planung definierten Aufgaben und Rollen (siehe SYS.1.5.A8 Planung einer virtuellen Infrastruktur) SOLLTE für die Administration der virtuellen IT-Systeme und Netze sowie der Virtualisierungsserver und der Managementumgebung ein Rechte- und Rollenkonzept erstellt und umgesetzt werden.
  2. Alle Komponenten der virtuellen Infrastruktur SOLLTEN in ein zentrales Identitäts- und Berechtigungsmanagement eingebunden werden.
  3. Administrierende von virtuellen Maschinen und Administrierende der Virtualisierungsumgebung SOLLTEN unterschieden werden. **◀ ZITIERT**
  4. Sie SOLLTEN mit unterschiedlichen Zugriffsrechten ausgestattet werden.
  5. Weiterhin SOLLTE die Managementumgebung virtuelle Maschinen zur geeigneten Strukturierung gruppieren können.
  6. Die Rollen der Administrierenden SOLLTEN entsprechend zugeteilt werden.
- **Satz 3** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 3) Die G++-Maßnahme PERS.2.3.2 fordert explizit eine Rollentrennung zwischen der Administration virtueller Systeme und Virtualisierungslösungen und deckt damit die geforderte Unterscheidung der Administrierenden vollständig ab.

### → SYS.1.5.A8 — Planung einer virtuellen Infrastruktur (S) [Planende]
  1. Der Aufbau der virtuellen Infrastruktur SOLLTE detailliert geplant werden.
  2. Dabei SOLLTEN die geltenden Regelungen und Richtlinien für den Betrieb von IT-Systemen, Anwendungen und Netzen (inklusive Speichernetzen) berücksichtigt werden.
  3. Wenn mehrere virtuelle IT-Systeme auf einem Virtualisierungsserver betrieben werden, SOLLTEN KEINE Konflikte hinsichtlich des Schutzbedarfs der IT-Systeme auftreten.
  4. Weiterhin SOLLTEN die Aufgaben der einzelnen Gruppen, die für die Administration zuständig sind, festgelegt und klar voneinander abgegrenzt werden. **◀ ZITIERT**
  5. Es SOLLTE auch geregelt werden, wer für den Betrieb welcher Komponente verantwortlich ist.
- **Satz 4** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 4) PERS.2.3.2 konkretisiert die Festlegung und Abgrenzung administrativer Aufgaben im Virtualisierungsumfeld durch die geforderte Rollentrennung zwischen virtuellen Systemen und Virtualisierungslösungen.


## PERS.4.2 — Rollenspezifische Schulungen und Sensibilisierungen  [39 Paare]

**Statement (normativ):** Personal für Nutzende SOLLTE rollenspezifische Schulungen und Sensibilisierungen im Einklang mit den Anforderungen der Praktik Sensibilisierung bei Neuzugang und {{ insert: param, pers.4.2-prm1 }} ausführen.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Neue Mitarbeitende könnten ohne gezielte Einführung unbewusst vertrauliche Informationen preisgeben, unsichere Passwörter wählen oder Phishing-Mails öffnen, da ihnen relevante Schutzprinzipien oder Gefährdungen im Kontext ihrer Tätigkeit nicht bekannt sind. Ebenso könnte es bei länger Beschäftigten zu einer „Routineblindheit“ kommen, sodass beispielsweise ungewöhnliche Systemmeldungen nicht mehr ernst genommen oder sensible Daten versehentlich an unberechtigte Personen weitergegeben werden. „Rollenspezifisch“ bedeutet in diesem Zusammenhang, dass die Inhalte der Schulung auf die jeweilige Tätigkeit zugeschnitten werden – eine Person im IT-Bereich benötigt z. B. andere Sicherheitskenntnisse als jemand im Vertrieb oder in der Verwaltung. Beispiele für rollenspezifische Schulungen sind Kurse zum sicheren IT-Betrieb für Administrierende, OWASP® Top 10 Training für Webentwickler und Social Engineering Abwehrtraining für die Institutionsleitung. Eine Institution kann diese Anforderung etwa umsetzen, indem sie standardisierte E-Learning-Module bereitstellt, die durch kurze Praxisszenarien ergänzt werden. Hilfreich ist, die Dauer der Formate überschaubar zu halten, um die Akzeptanz hoch zu halten, und die Wirksamkeit regelmäßig durch Feedback oder kleine Tests zu prüfen. Ebenso kann es sinnvoll sein, Fachbereiche in die Ausgestaltung einzubinden, damit Beispiele und Szenarien aus dem tatsächlichen Arbeitsalltag stammen. Mitarbeitende, die bereits eine passende Qualifikation erworben haben, können von der Schulung ausgenommen werden.

### → ORP.3.A6 — Durchführung von Sensibilisierungen und Schulungen zur Informationssicherheit (S)
  1. Alle Mitarbeitenden SOLLTEN entsprechend ihren Aufgaben und Verantwortlichkeiten zu Informationssicherheitsthemen geschult werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `equivalent-to` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) PERS.4.2 fordert explizit die Durchführung rollenspezifischer Schulungen und Sensibilisierungen für das Personal entsprechend ihren jeweiligen Aufgaben und Tätigkeiten.

### → CON.8.A14 — Schulung des Entwicklungsteams zur Informationssicherheit (S)
  1. Die Entwickelnden und die übrigen Mitglieder des Entwicklungsteams SOLLTEN zu generellen Informationssicherheitsaspekten und zu den jeweils speziell für sie relevanten Aspekten geschult sein: Anforderungsanalyse, Projektmanagement allgemein sowie speziell bei der Software-Entwicklung, Risikomanagement bzw. Bedrohungsmodellierung in der Software-Entwicklung, Qualitätsmanagement und Qualitätssicherung, Modelle und Methoden für die Software-Entwicklung, Software-Architektur, Software-Tests, Änderungsmanagement sowie Informationssicherheit, Sicherheitsvorgaben in der Institution und Sicherheitsaspekte in speziellen Bereichen. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) PERS.4.2 verlangt rollenspezifische Sicherheits- und Sensibilisierungsschulungen für Mitarbeitende und deckt damit als allgemeinere Maßnahme auch die gezielte Schulung von Mitgliedern des Entwicklungsteams zu für sie relevanten Sicherheitsaspekten ab.

### → DER.1.A14 — Auswertung der Protokollierungsdaten durch spezialisiertes Personal (H)
  1. Es SOLLTEN Mitarbeitende speziell damit beauftragt werden, alle Protokollierungsdaten zu überwachen.
  2. Die Überwachung der Protokollierungsdaten SOLLTE die überwiegende Aufgabe der beauftragten Mitarbeitenden sein.
  3. Die beauftragten Mitarbeitenden SOLLTEN spezialisierte weiterführende Schulungen und Qualifikationen erhalten. **◀ ZITIERT**
  4. Ein Personenkreis SOLLTE benannt werden, der ausschließlich für das Thema Auswertung von Protokollierungsdaten verantwortlich ist.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme PERS.4.2 fordert rollenspezifische Schulungen und deckt damit als allgemeinere Anforderung die spezialisierten Schulungen und Qualifikationen für das mit der Protokollauswertung beauftragte Personal ab.

### → DER.1.A7 — Schulung von Zuständigen (S) [Vorgesetzte]
  1. Alle Zuständigen, die Ereignismeldungen kontrollieren, SOLLTEN weiterführende Schulungen und Qualifikationen erhalten. **◀ ZITIERT**
  2. Wenn neue IT-Komponenten beschafft werden, SOLLTE ein Budget für Schulungen eingeplant werden.
  3. Bevor die Zuständigen Schulungen für neue IT-Komponenten bekommen, SOLLTE ein Schulungskonzept erstellt werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme PERS.4.2 deckt als übergeordnete Anforderung rollenspezifische Schulungen und Qualifikationen für Fachrollen ab, wozu auch die Zuständigen für die Kontrolle von Ereignismeldungen gehören.

### → DER.2.1.A12 — Festlegung der Schnittstellen der Sicherheitsvorfallbehandlung zur Störungs- und Fehlerbehebung (S) [Notfallbeauftragte]
  1. Die Schnittstellen zwischen Störungs- und Fehlerbehebung, Notfallmanagement und Sicherheitsmanagement SOLLTEN analysiert werden.
  2. Dabei SOLLTEN auch eventuell gemeinsam benutzbare Ressourcen identifiziert werden.
  3. Die bei der Störungs- und Fehlerbehebung beteiligten Mitarbeitenden SOLLTEN für die Behandlung von Sicherheitsvorfällen sowie für das Notfallmanagement sensibilisiert werden. **◀ ZITIERT**
  4. Das Sicherheitsmanagement SOLLTE lesenden Zugriff auf eingesetzte Incident-Management-Werkzeuge haben.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) PERS.4.2 fordert allgemeine rollenspezifische Schulungen und Sensibilisierungen für Mitarbeitende, was die aufgabenbezogene Sensibilisierung des Störungsbehebungspersonals für Sicherheitsvorfälle und Notfälle umfasst.

### → DER.2.1.A15 — Schulung der Mitarbeitenden des Service Desks (S) [IT-Betrieb]
  1. Dem Personal des Service Desk SOLLTEN geeignete Hilfsmittel zur Verfügung stehen, damit sie Sicherheitsvorfälle erkennen können.
  2. Sie SOLLTEN ausreichend geschult sein, um die Hilfsmittel selbst anwenden zu können. **◀ ZITIERT**
  3. Die Mitarbeitenden des Service Desk SOLLTEN den Schutzbedarf der betroffenen IT-Systeme kennen.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) PERS.4.2 fordert rollenspezifische Schulungen für das Personal, was die aufgabenbezogene Schulung des Service-Desk-Personals zur Anwendung ihrer Hilfsmittel abdeckt.

### → DER.2.1.A21 — Einrichtung eines Teams von Fachleuten für die Behandlung von Sicherheitsvorfällen (H)
  1. Es SOLLTE ein Team mit erfahrenen und vertrauenswürdigen Fachleuten zusammengestellt werden.
  2. Neben dem technischen Verständnis SOLLTEN die Teammitglieder auch über Kompetenzen im Bereich Kommunikation verfügen.
  3. Die Vertrauenswürdigkeit der Mitglieder des Teams SOLLTE überprüft werden.
  4. Die Zusammensetzung des Teams SOLLTE regelmäßig überprüft und, wenn nötig, geändert werden.
  5. Die Mitglieder des Teams SOLLTEN in die Eskalations- und Meldewege eingebunden sein.
  6. Das Experten- und Expertinnenteam SOLLTE für die Analyse von Sicherheitsvorfällen an den in der Institution eingesetzten Systemen ausgebildet werden.
  7. Die Mitglieder des Experten- und Expertinnenteams SOLLTEN sich regelmäßig weiterbilden, sowohl zu den eingesetzten Systemen als auch zur Detektion und Reaktion auf Sicherheitsvorfälle. **◀ ZITIERT**
  8. Dem Experten- und Expertinnenteam SOLLTEN alle vorhandenen Dokumentationen sowie finanzielle und technische Ressourcen zur Verfügung stehen, um Sicherheitsvorfälle schnell und diskret zu behandeln.
  9. Das Experten- und Expertinnenteams SOLLTE in geeigneter Weise in den Organisationsstrukturen berücksichtigt und in diese integriert werden.
  10. Die Zuständigkeiten des Teams SOLLTEN vorher mit denen des Sicherheitsvorfall-Teams abgestimmt werden.
- **Satz 7** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 7) Die G++-Maßnahme fordert allgemeingültig regelmäßige rollenspezifische Schulungen für das Personal, was die fachspezifische Weiterbildung von Incident-Response-Expertenteams inhaltlich mit abdeckt.

### → DER.2.2.A6 — Schulung des Personals für die Umsetzung der forensischen Sicherung (S)
  1. Alle verantwortlichen Mitarbeitenden SOLLTEN wissen, wie sie Spuren korrekt sichern und die Werkzeuge zur Forensik richtig einsetzen.
  2. Dafür SOLLTEN geeignete Schulungen durchgeführt werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) PERS.4.2 fordert die Durchführung rollenspezifischer Schulungen und deckt damit als übergeordnete Maßnahme die Durchführung geeigneter Schulungen für die mit der Forensik betrauten Personen inhaltlich ab.

### → DER.4.A8 — Integration der Mitarbeitenden in den Notfallmanagement-Prozess (H) [Vorgesetzte, Personalabteilung]
  1. Alle Mitarbeitenden SOLLTEN regelmäßig für das Thema Notfallmanagement sensibilisiert werden.
  2. Zum Notfallmanagement SOLLTE es ein Schulungs- und Sensibilisierungskonzept geben.
  3. Die Mitarbeitenden im Notfallmanagement-Team SOLLTEN regelmäßig geschult werden, um die benötigten Kompetenzen aufzubauen. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) PERS.4.2 fordert die regelmäßige Durchführung rollenspezifischer Schulungen, was die spezifische Schulung von Mitgliedern des Notfallmanagement-Teams zur Kompetenzentwicklung als Rolleninhaber inhaltlich abdeckt.

### → IND.1.A7 — Etablieren einer übergreifenden Berechtigungsverwaltung zwischen der OT und in der Office-IT (S)
  1. Die Institution SOLLTE einen Prozess zur Verwaltung von Zugängen und zugeordneten Berechtigungen für den Zugriff auf die OT etablieren.
  2. Die Berechtigungsverwaltung SOLLTE den Prozess, die Durchführung und die Dokumentation für die Beantragung, Einrichtung und den Entzug von Berechtigungen umfassen.
  3. Die Berechtigungsverwaltung SOLLTE gewährleisten, dass Berechtigungen nach dem Minimalprinzip vergeben und regelmäßig überprüft werden.
  4. In der Berechtigungsverwaltung SOLLTEN die Zugriffe auf IT-Systeme für Mitarbeitende, Administrierende und Dritte geregelt sein.
  5. Jeder oder jede Beteiligte SOLLTE regelmäßig zu den einzuhaltenden Regelungen sensibilisiert werden. **◀ ZITIERT**
  6. Die Einhaltung SOLLTE überprüft werden.
  7. Fehlverhalten SOLLTE sanktioniert werden.
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) PERS.4.2 fordert explizit die regelmäßige Durchführung rollenspezifischer Schulungen und Sensibilisierungen für das Personal und deckt damit die geforderte regelmäßige Sensibilisierung der Beteiligten ab.

### → INF.11.A7 — Sachgerechter Umgang mit Fahrzeugen und schützenswerten Informationen (S) [Fachverantwortliche, Benutzende]
  1. Die Institution SOLLTE die Handlungsanweisungen zur Fahrzeugbenutzung um Aspekte ergänzen, wann, wie und wo Fahrzeuge sachgerecht abgestellt bzw. angedockt werden dürfen.
  2. Hierbei SOLLTE primär die Frage beantwortet werden, welche Umgebungen die Fahrzeuge angemessenen vor unerlaubten Zutritt oder Sachbeschädigung schützen.
  3. Des Weiteren SOLLTE hierbei berücksichtigt werden, welche Informationen und IT-Systeme in den Fahrzeugen aufbewahrt werden dürfen.
  4. Ausreichende Maßnahmen zum Zutrittsschutz SOLLTEN ergriffen werden.
  5. Die Ladung der Fahrzeuge SOLLTE sicher verstaut werden.
  6. Es SOLLTE sichergestellt werden, dass schützenswerte Informationen nicht von außerhalb der Fahrzeuge von Unbefugten eingesehen, mitgehört oder entwendet werden können.
  7. Die Mitarbeitenden SOLLTEN mit der grundlegenden Funktionsweise der Fahrzeuge und den betreffenden IT-Komponenten vertraut gemacht werden. **◀ ZITIERT**
  8. Die Mitarbeitenden SOLLTEN auch über die bestehenden Sicherheitsrisiken informiert werden.
- **Satz 7** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 7) Die G++-Maßnahme PERS.4.2 verlangt rollenspezifische Schulungen für Nutzende, was die tätigkeitsbezogene Einweisung der Mitarbeitenden in die Funktionsweise der Fahrzeuge und IT-Komponenten als allgemeinere Anforderung abdeckt.

### → INF.9.A2 — Regelungen für mobile Arbeitsplätze (B) [Personalabteilung]
  1. Für alle Arbeiten unterwegs MUSS geregelt werden, welche Informationen außerhalb der Institution transportiert und bearbeitet werden dürfen.
  2. Es MUSS zudem geregelt werden, welche Schutzvorkehrungen dabei zu treffen sind.
  3. Dabei MUSS auch geklärt werden, unter welchen Rahmenbedingungen Mitarbeitende mit mobilen IT-Systemen auf interne Informationen ihrer Institution zugreifen dürfen.
  4. Die Mitnahme von IT-Komponenten und Datenträgern MUSS klar geregelt werden.
  5. So MUSS festgelegt werden, welche IT-Systeme und Datenträger mitgenommen werden dürfen, wer diese mitnehmen darf und welche grundlegenden Sicherheitsanforderungen dabei beachtet werden müssen.
  6. Es MUSS zudem protokolliert werden, wann und von wem welche mobilen Endgeräte außer Haus eingesetzt wurden.
  7. Die Benutzenden von mobilen Endgeräten MÜSSEN für den Wert mobiler IT-Systeme und den Wert der darauf gespeicherten Informationen sensibilisiert werden.
  8. Sie MÜSSEN über die spezifischen Gefährdungen und Maßnahmen der von ihnen benutzten IT-Systeme aufgeklärt werden.
  9. Außerdem MÜSSEN sie darüber informiert werden, welche Art von Informationen auf mobilen IT-Systemen verarbeitet werden darf.
  10. Alle Benutzenden MÜSSEN auf die geltenden Regelungen hingewiesen werden, die von ihnen einzuhalten sind.
  11. Sie MÜSSEN entsprechend geschult werden **◀ ZITIERT**
- **Satz 11** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 11) Die G++-Maßnahme PERS.4.2 fordert allgemeine und rollenspezifische Schulungen für Nutzende, was die geforderte Schulung der Benutzenden mobiler Endgeräte inhaltlich abdeckt.

### → INF.9.A8 — Sicherheitsrichtlinie für mobile Arbeitsplätze (S) [IT-Betrieb]
  1. Alle relevanten Sicherheitsanforderungen für mobile Arbeitsplätze SOLLTEN in einer für die mobilen Mitarbeitenden verpflichtenden Sicherheitsrichtlinie dokumentiert werden.
  2. Sie SOLLTE zudem mit den bereits vorhandenen Sicherheitsrichtlinien der Institution sowie mit allen relevanten Fachabteilungen abgestimmt werden.
  3. Die Sicherheitsrichtlinie für mobile Arbeitsplätze SOLLTE regelmäßig aktualisiert werden.
  4. Die Mitarbeitenden der Institution SOLLTEN hinsichtlich der aktuellen Sicherheitsrichtlinie sensibilisiert und geschult sein. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) PERS.4.2 fordert die regelmäßige und anlassbezogene Schulung und Sensibilisierung von Nutzenden, was die Schulung der Mitarbeitenden bezüglich relevanter Sicherheitsrichtlinien inhaltlich abdeckt.

### → NET.2.2.A2 — Sensibilisierung und Schulung der WLAN-Benutzenden (B) [Vorgesetzte, IT-Betrieb]
  1. Die Benutzenden von WLAN-Komponenten, vornehmlich von WLAN-Clients, MÜSSEN sensibilisiert und zu den in der Nutzungsrichtlinie aufgeführten Maßnahmen geschult werden. **◀ ZITIERT**
  2. Hierfür MÜSSEN geeignete Schulungsinhalte identifiziert und festgelegt werden.
  3. Den Benutzenden MUSS genau erläutert werden, was die WLAN-spezifischen Sicherheitseinstellungen bedeuten und warum sie wichtig sind.
  4. Außerdem MÜSSEN die Benutzenden auf die Gefahren hingewiesen werden, die drohen, wenn diese Sicherheitseinstellungen umgangen oder deaktiviert werden.
  5. Die Schulungsinhalte MÜSSEN immer entsprechend den jeweiligen Einsatzszenarien angepasst werden.
  6. Neben der reinen Schulung zu WLAN-Sicherheitsmechanismen MÜSSEN den Benutzenden jedoch auch die WLAN-Sicherheitsrichtlinie ihrer Institution und die darin enthaltenen Maßnahmen vorgestellt werden.
  7. Ebenso MÜSSEN die Benutzenden für die möglichen Gefahren sensibilisiert werden, die von fremden WLANs ausgehen.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) PERS.4.2 verlangt die rollenspezifische Schulung und Sensibilisierung von Nutzenden, was die allgemeine Entsprechung zur Schulung und Sensibilisierung von WLAN-Nutzenden darstellt.

### → NET.3.3.A8 — Erstellung einer Sicherheitsrichtlinie zur VPN-Nutzung (S)
  1. Eine Sicherheitsrichtlinie zur VPN-Nutzung SOLLTE erstellt werden.
  2. Diese SOLLTE allen Mitarbeitenden bekannt gegeben werden.
  3. Die in der Sicherheitsrichtlinie beschriebenen Sicherheitsmaßnahmen SOLLTEN im Rahmen von Schulungen erläutert werden. **◀ ZITIERT**
  4. Wird für Mitarbeitende ein VPN-Zugang eingerichtet, SOLLTE diesen ein Merkblatt mit den wichtigsten VPN-Sicherheitsmechanismen ausgehändigt werden.
  5. Alle VPN-Benutzende SOLLTEN verpflichtet werden, die Sicherheitsrichtlinien einzuhalten.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) PERS.4.2 fordert die Durchführung rollenspezifischer Schulungen und Sensibilisierungen für Nutzende, was die Vermittlung relevanter Sicherheitsmaßnahmen aus Richtlinien (wie der VPN-Nutzungsrichtlinie) im Rahmen von Schulungen als allgemeinere Anforderung abdeckt.

### → NET.4.1.A9 — Schulung zur sicheren Nutzung von TK-Anlagen (S) [Vorgesetzte]
  1. Die Benutzenden der TK-Anlage SOLLTEN in die korrekte Verwendung von Diensten und Geräten eingewiesen werden. **◀ ZITIERT**
  2. Den Benutzenden der TK-Anlage SOLLTEN alle notwendigen Unterlagen zur Bedienung der entsprechenden Endgeräte zur Verfügung gestellt werden.
  3. Sämtliche Auffälligkeiten und Unregelmäßigkeiten der TK-Anlage SOLLTEN den entsprechenden Verantwortlichen gemeldet werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) PERS.4.2 deckt als übergeordnete Anforderung für rollenspezifische Schulungen und Sensibilisierungen von Nutzenden die Einweisung in die Nutzung von TK-Diensten und -Geräten ab.

### → NET.4.2.A11 — Sicherer Umgang mit VoIP-Endgeräten (S) [Benutzende]
  1. Benutzende, die VoIP-Endgeräte einsetzen, SOLLTEN über die grundlegenden VoIP-Gefährdungen und Sicherheitsmaßnahmen informiert sein. **◀ ZITIERT**
  2. Außerdem SOLLTEN sie geeignete Passwörter zur Absicherung von Voicemails auswählen.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) PERS.4.2 deckt als übergeordnete Maßnahme für rollenspezifische Schulungen und Sensibilisierungen von Nutzenden die Unterrichtung von VoIP-Endgeräte-Nutzenden über relevante Gefährdungen und Sicherheitsmaßnahmen inhaltlich ab.

### → NET.4.3.A13 — Festlegung berechtigter Faxbedienenden (H) [Benutzende]
  1. Es SOLLTEN nur wenige Mitarbeitende ausgewählt werden, die auf das Faxgerät zugreifen dürfen.
  2. Diese Mitarbeitenden SOLLTEN ankommende Faxsendungen an die Empfangenden verteilen.
  3. Den Mitarbeitenden SOLLTE vermittelt werden, wie sie mit dem Gerät umgehen und wie sie die erforderlichen Sicherheitsmaßnahmen umsetzen können. **◀ ZITIERT**
  4. Jeder berechtigte Benutzende SOLLTE darüber unterrichtet werden, wer das Faxgerät bedienen darf und wer für das Gerät zuständig ist.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) PERS.4.2 deckt die Vermittlung des sicheren Umgangs und relevanter Sicherheitsmaßnahmen als allgemeinere rollenspezifische Schulung und Sensibilisierung für Nutzende inhaltlich ab.

### → OPS.1.1.1.A16 — Schulung des Betriebspersonals (S)
  1. Für den IT-Betrieb SOLLTE durch einen Schulungsplan sichergestellt werden, dass für alle IT-Komponenten und Betriebsmittel jeweils mehrere Personen die erforderlichen Fähigkeiten und Qualifikationen besitzen.
  2. In den Schulungsmaßnahmen SOLLTEN insbesondere die folgenden Themen adressiert werden: Härtung und Standard-Konfigurationen spezifische Sicherheitseinstellungen für die betriebenen IT-Komponenten und eingesetzten Betriebsmittel mögliche Interferenzen zwischen den genutzten Betriebsmitteln Abhängigkeiten und Schnittstellen der Prozesse des IT-Betriebs Wenn neue IT-Komponenten beschafft werden, SOLLTE ein Budget für entsprechende Schulungsmaßnahmen des IT-Betriebs eingeplant werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 2) Satz 2 konkretisiert rollenspezifische Schulungsinhalte für das IT-Betriebspersonal zur Gewährleistung des sicheren IT-Betriebs.

### → OPS.1.1.4.A7 — Sensibilisierung und Verpflichtung der Benutzenden (B) [Benutzende]
  1. Benutzende MÜSSEN regelmäßig über die Bedrohung durch Schadprogramme aufgeklärt werden. **◀ ZITIERT**
  2. Sie MÜSSEN die grundlegenden Verhaltensregeln einhalten, um die Gefahr eines Befalls durch Schadprogramme zu reduzieren.
  3. Dateien, E-Mails, Webseiten usw. aus nicht vertrauenswürdigen Quellen SOLLTEN NICHT geöffnet werden.
  4. Sie MÜSSEN entsprechenden Kontaktpersonen für den Fall eines Verdacht auf eine Infektion mit einem Schadprogramm bekannt sein.
  5. Sie MÜSSEN sich an die ihnen benannten Kontaktpersonen wenden, wenn der Verdacht auf eine Infektion mit einem Schadprogramm besteht.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme PERS.4.2 deckt die regelmäßige Aufklärung der Nutzenden über Sicherheitsrisiken wie Schadprogramme als allgemeinere Pflicht zur rollenspezifischen und regelmäßigen Sensibilisierung von Nutzenden ab.

### → OPS.1.2.2.A11 — Einweisung in die Administration und Bedienung des Archivsystems (S) [IT-Betrieb, Benutzende]
  1. Die zuständigen Mitarbeitende des IT-Betriebs und die Benutzenden SOLLTEN für ihren Aufgabenbereich geschult werden. **◀ ZITIERT**
  2. Die Schulung der Mitarbeitenden des IT-Betriebs SOLLTE folgende Themen umfassen: Systemarchitektur und Sicherheitsmechanismen des verwendeten Archivsystems und des darunterliegenden Betriebssystems, Installation und Bedienung des Archivsystems und Umgang mit Archivmedien, Dokumentation der Administrationstätigkeiten sowie Eskalationsprozeduren.
  3. Die Schulung der Benutzende SOLLTE folgende Themen umfassen: Umgang mit dem Archivsystem, Bedienung des Archivsystems sowie rechtliche Rahmenbedingungen der Archivierung. **◀ ZITIERT**
  4. Die Durchführung der Schulungen sowie die Teilnahme SOLLTEN dokumentiert werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) PERS.4.2 fordert rollenspezifische Schulungen für das Personal entsprechend ihren jeweiligen Aufgaben, was die allgemeine Schulungspflicht für IT-Betrieb und Benutzende aus Satz 1 abdeckt.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme PERS.4.2 deckt als allgemeinere Anforderung rollenspezifische Schulungen für Nutzende ab, worunter auch die konkreten Schulungsinhalte für Benutzende des Archivsystems fallen.

### → OPS.1.2.4.A5 — Sensibilisierung und Schulung der Mitarbeitenden (B)
  1. Anhand eines Leitfadens MÜSSEN die Mitarbeitenden für die Gefahren sensibilisiert werden, die mit der Telearbeit verbunden sind. **◀ ZITIERT**
  2. Außerdem MÜSSEN sie in die entsprechenden Sicherheitsmaßnahmen der Institution eingewiesen und im Umgang mit diesen geschult werden. **◀ ZITIERT**
  3. Die Schulungs- und Sensibilisierungsmaßnahmen für Mitarbeitenden SOLLTEN regelmäßig wiederholt werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) PERS.4.2 fordert als allgemeinere Maßnahme rollen- und tätigkeitsspezifische Sensibilisierungen und Schulungen von Nutzenden und deckt damit die Gefahrensensibilisierung für Telearbeitende inhaltlich ab.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme PERS.4.2 verlangt rollenspezifische Schulungen und Sensibilisierungen für Nutzende bei Neuzugang und regelmäßig, was die Einweisung und Schulung in die relevanten Sicherheitsmaßnahmen der Institution als allgemeine Fassung materiell abdeckt.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme PERS.4.2 verlangt explizit, rollenspezifische Schulungen und Sensibilisierungen regelmäßig auszuführen, was die regelmäßige Wiederholung der Schulungsmaßnahmen abdeckt.

### → OPS.2.3.A10 — Etablierung einer zuständigen Person für das Auslagerungsmanagement (S) [Personalabteilung]
  1. Die verschiedenen Outsourcing-Vorhaben SOLLTEN durch eine zuständige Person für das Auslagerungsmanagement verwaltet werden.
  2. Die zuständige Person SOLLTE ernannt und die Befugnisse festgelegt und dokumentiert werden.
  3. Die zuständige Person SOLLTE als Schnittstelle in der Kommunikation zwischen den Nutzenden und Anbietenden von Outsourcing eingesetzt werden.
  4. Darüber hinaus SOLLTE die zuständige Person Berichte über das Outsourcing in regelmäßigen Abständen und anlassbezogen anfertigen und der Institutionsleitung übergeben.
  5. In der Vertragsgestaltung SOLLTE die zuständige Person einbezogen werden.
  6. Die zuständige Person SOLLTE ein angemessenes Kontingent von Arbeitstagen für die Aufgaben des Auslagerungsmanagements eingeräumt bekommen.
  7. Darüber hinaus SOLLTE die zuständige Person hinsichtlich Informationssicherheit geschult und sensibilisiert sein. **◀ ZITIERT**
- **Satz 7** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 7) Die G++-Maßnahme PERS.4.2 verlangt rollenspezifische Schulungen und Sensibilisierungen zur Informationssicherheit und deckt damit die gezielte Schulung der zuständigen Person für das Auslagerungsmanagement ab.

### → ORP.3.A9 — Spezielle Schulung von exponierten Personen und Institutionen (H)
  1. Besonders exponierte Personen SOLLTEN vertiefende Schulungen in Hinblick auf mögliche Gefährdungen sowie geeignete Verhaltensweisen und Vorsichtsmaßnahmen erhalten. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) PERS.4.2 verlangt rollenspezifische Schulungen und Sensibilisierungen für Nutzende, was die vertiefenden Schulungen für besonders exponierte Personen (wie z. B. die Institutionsleitung) direkt abdeckt.

### → ORP.4.A11 — Zurücksetzen von Passwörtern (S) [IT-Betrieb]
  1. Für das Zurücksetzen von Passwörtern SOLLTE ein angemessenes sicheres Verfahren definiert und umgesetzt werden.
  2. Die Mitarbeitenden des IT-Betriebs, die Passwörter zurücksetzen können, SOLLTEN entsprechend geschult werden. **◀ ZITIERT**
  3. Bei höherem Schutzbedarf des Passwortes SOLLTE eine Strategie definiert werden, falls Mitarbeitende des IT-Betriebs aufgrund fehlender sicherer Möglichkeiten der Übermittlung des Passwortes die Verantwortung nicht übernehmen können.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) PERS.4.2 verlangt die regelmäßige Durchführung rollenspezifischer Schulungen, was die zielgerichtete Schulung von IT-Betriebsmitarbeitenden für das Zurücksetzen von Passwörtern als allgemeinere Maßnahme abdeckt.

### → ORP.4.A19 — Einweisung aller Mitarbeitenden in den Umgang mit Authentisierungsverfahren und -mechanismen (S) [Benutzende, IT-Betrieb]
  1. Alle Mitarbeitende SOLLTEN in den korrekten Umgang mit dem Authentisierungsverfahren eingewiesen werden. **◀ ZITIERT**
  2. Es SOLLTE verständliche Richtlinien für den Umgang mit Authentisierungsverfahren geben.
  3. Die Mitarbeitenden SOLLTEN über relevante Regelungen informiert werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme PERS.4.2 fordert Schulungen und Sensibilisierungen für Nutzende bei Neuzugang und regelmäßig, was die Einweisung aller Mitarbeitenden in den korrekten Umgang mit Authentisierungsverfahren als allgemeine Schulungspflicht abdeckt.

### → SYS.1.7.A4 — Schulung des z/OS-Bedienungspersonals (B) [Vorgesetzte]
  1. Administrierende, Bedienende und Prüfende im z/OS-Bereich MÜSSEN entsprechend ihren Aufgaben ausgebildet sein. **◀ ZITIERT**
  2. Insbesondere MÜSSEN RACF-Administrierende mit dem Sicherheitssystem selbst sowie gegebenenfalls mit den weiteren für sie relevanten Funktionen vertraut sein.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) PERS.4.2 fordert rollenspezifische Schulungen für Personal entsprechend ihrer jeweiligen Tätigkeit, was die aufgabenbezogene Ausbildung von Administrierenden, Bedienenden und Prüfenden abdeckt.

### → SYS.1.9.A9 — Sensibilisierung der Benutzenden (B)
  1. Alle Benutzenden von Terminalservern MÜSSEN über den sicheren Umgang mit Terminalservern sensibilisiert werden. **◀ ZITIERT**
  2. Den Benutzenden MÜSSEN mindestens die folgenden Inhalte vermittelt werden: grundsätzliche Funktionsweise und die Auswirkungen von Latenz und verfügbarer Bandbreite auf die Bedienbarkeit mögliche und erlaubte Speicherorte von Daten zugelassene Austauschmöglichkeiten von Informationen zwischen dem Betriebssystem des Clients und dem Terminalserver (z. B. Zwischenablage) Auswirkung des eigenen Ressourcenverbrauchs auf die zur Verfügung stehenden Ressourcen für andere Benutzende eingerichtete Rollen und Berechtigungen für Terminalserver-Zugriffe genutzte Authentisierung und Autorisierung der Benutzenden für die zur Verfügung gestellten Anwendungen maximale Sitzungsdauer und automatische Abmeldevorgänge
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) PERS.4.2 fordert rollenspezifische Sensibilisierungen und Schulungen für Nutzende, was die allgemeinere Fassung der geforderten Sensibilisierung von Terminalserver-Benutzenden darstellt.

### → SYS.2.1.A23 — Bevorzugung von Client-Server-Diensten (S)
  1. Wenn möglich, SOLLTEN zum Informationsaustausch dedizierte Serverdienste genutzt und direkte Verbindungen zwischen Clients vermieden werden.
  2. Falls dies nicht möglich ist, SOLLTE festgelegt werden, welche Client-zu-Client-Dienste (oft auch als „Peer-to-Peer“ bezeichnet) genutzt und welche Informationen darüber ausgetauscht werden dürfen.
  3. Falls erforderlich, SOLLTEN Benutzende für die Nutzung solcher Dienste geschult werden. **◀ ZITIERT**
  4. Direkte Verbindungen zwischen Clients SOLLTEN sich nur auf das LAN beschränken.
  5. Auto-Discovery-Protokolle SOLLTEN auf das notwendige Maß beschränkt werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) PERS.4.2 deckt als allgemeinere Maßnahme zur rollenspezifischen Schulung von Nutzenden die bedarfsgerechte Schulung von Anwendern für spezifische Dienste inhaltlich ab.

### → SYS.2.5.A12 — Sensibilisierung der Benutzenden (S)
  1. Alle Benutzenden von virtuellen Clients SOLLTEN über den sicheren Umgang mit virtuellen Clients sensibilisiert werden. **◀ ZITIERT**
  2. Falls die Ressourcen dynamisch anhand der abgerufenen Leistung zwischen mehreren virtuellen Clients aufgeteilt werden, SOLLTEN die Benutzenden darüber aufgeklärt werden, dass ihr Verhalten potenziell andere Benutzende beeinflussen kann.
  3. Falls die Sicherheitsanforderungen der auf virtuellen Clients ausgeführten Anwendungen besonders sind, SOLLTE kommuniziert werden, wie diese gegenüber physischen Clients abweichen.
  4. Es SOLLTE auch kommuniziert werden, welche spezifischen Sicherheitsaspekte zu beachten sind.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) PERS.4.2 deckt als übergeordnete Maßnahme für rollenspezifische Schulungen und Sensibilisierungen von Nutzenden die zielgruppenspezifische Sensibilisierung zum sicheren Umgang mit virtuellen Clients ab.

### → SYS.3.2.1.A2 — Festlegung einer Strategie für die Cloud-Nutzung (B)
  1. Die Institution MUSS im Zusammenhang mit Smartphones und Tablets eine generelle Strategie für die Cloud-Nutzung sowie für den Schutz und die Kontrolle der Informationen festlegen.
  2. Die erlaubte Nutzung von Cloud-Diensten für Informationen der Institution MUSS geklärt und festgelegt werden.
  3. Es MUSS festgelegt werden, ob und in welchem Umfang Cloud-Dienste bei privater Nutzung der Geräte erlaubt sind.
  4. Die Benutzenden MÜSSEN regelmäßig bezüglich der Nutzung solcher Cloud-Dienste sensibilisiert werden. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) PERS.4.2 deckt als allgemeine Anforderung die regelmäßige rollenspezifische Sensibilisierung und Schulung von Nutzenden bezüglich sicherheitsrelevanter Themen wie der Cloud-Nutzung ab.

### → SYS.3.3.A1 — Sicherheitsrichtlinien und Regelungen für die Nutzung von Mobiltelefonen (B)
  1. Im Hinblick auf die Nutzung und Kontrolle der Geräte MUSS eine Sicherheitsrichtlinie erstellt werden.
  2. Jeder benutzenden Person eines Mobiltelefons MUSS ein Exemplar der Sicherheitsrichtlinie ausgehändigt werden.
  3. Es MUSS regelmäßig überprüft werden, ob die Sicherheitsrichtlinie eingehalten wird.
  4. Die Sicherheitsrichtlinie zur dienstlichen Nutzung von Mobiltelefonen SOLLTE Bestandteil der Schulung zu Sicherheitsmaßnahmen sein. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) PERS.4.2 verlangt rollenspezifische Schulungen und Sensibilisierungen für Nutzende, was die Vermittlung relevanter Sicherheitsrichtlinien wie der zur Mobiltelefonnutzung im Rahmen von Sicherheitsschulungen allgemein abdeckt.

### → ORP.2.A15 — Qualifikation des Personals (B) [Vorgesetzte]
  1. Mitarbeitende MÜSSEN regelmäßig geschult bzw. weitergebildet werden. **◀ ZITIERT**
  2. In allen Bereichen MUSS sichergestellt werden, dass kein Mitarbeitende mit veralteten Wissensstand arbeitet.
  3. Weiterhin SOLLTE den Mitarbeitenden während ihrer Beschäftigung die Möglichkeit gegeben werden, sich im Rahmen ihres Tätigkeitsfeldes weiterzubilden. **◀ ZITIERT**
  4. Werden Stellen besetzt, MÜSSEN die erforderlichen Qualifikationen und Fähigkeiten genau formuliert sein.
  5. Anschließend SOLLTE geprüft werden, ob diese bei den Bewerbenden für die Stelle tatsächlich vorhanden sind.
  6. Es MUSS sichergestellt sein, dass Stellen nur von Mitarbeitenden besetzt werden, für die sie qualifiziert sind.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) PERS.4.2 fordert explizit die regelmäßige Durchführung von rollenspezifischen Schulungen für Nutzende und deckt damit die geforderte regelmäßige Schulung und Weiterbildung der Mitarbeitenden ab.
- **Satz 3** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme PERS.4.2 fordert regelmäßige, auf die jeweilige Rolle bzw. Tätigkeit zugeschnittene Schulungen und deckt damit die kontinuierliche tätigkeitsbezogene Weiterbildungsmöglichkeit für Mitarbeitende direkt ab.

### → ORP.3.A3 — Einweisung des Personals in den sicheren Umgang mit IT (B) [Vorgesetzte, Personalabteilung, IT-Betrieb]
  1. Alle Mitarbeitenden und externen Benutzenden MÜSSEN in den sicheren Umgang mit IT-, ICS- und IoT-Komponenten eingewiesen und sensibilisiert werden, soweit dies für ihre Arbeitszusammenhänge relevant ist. **◀ ZITIERT**
  2. Dafür MÜSSEN verbindliche, verständliche und aktuelle Richtlinien zur Nutzung der jeweiligen Komponenten zur Verfügung stehen.
  3. Werden IT-, ICS- oder IoT-Systeme oder -Dienste in einer Weise benutzt, die den Interessen der Institution widersprechen, MUSS dies kommuniziert werden.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die G++-Maßnahme PERS.4.2 fordert rollenspezifische Schulungen und Sensibilisierungen für Nutzende und deckt damit die geforderte Einweisung und Sensibilisierung im jeweiligen Arbeitszusammenhang inhaltlich ab.

### → ORP.3.A4 — Konzeption und Planung eines Sensibilisierungs- und Schulungsprogramms zur Informationssicherheit (S)
  1. Sensibilisierungs- und Schulungsprogramme zur Informationssicherheit SOLLTEN sich an den jeweiligen Zielgruppen orientieren. **◀ ZITIERT**
  2. Dazu SOLLTE eine Zielgruppenanalyse durchgeführt werden.
  3. Hierbei SOLLTEN Schulungsmaßnahmen auf die speziellen Anforderungen und unterschiedlichen Hintergründe fokussiert werden können.
  4. Es SOLLTE ein zielgruppenorientiertes Sensibilisierungs- und Schulungsprogramm zur Informationssicherheit erstellt werden.
  5. Dieses Schulungsprogramm SOLLTE den Mitarbeitenden alle Informationen und Fähigkeiten vermitteln, die erforderlich sind, um in der Institution geltende Sicherheitsregelungen und -maßnahmen umsetzen zu können.
  6. Es SOLLTE regelmäßig überprüft und aktualisiert werden.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 1) Satz 1 fordert die Ausrichtung von Sensibilisierungs- und Schulungsprogrammen an Zielgruppen, was sich direkt mit der Durchführung rollenspezifischer Schulungen in PERS.4.2 überschneidet.


## PERS.6.1.2 — Neubesetzung  [1 Paare]

**Statement (normativ):** Personal für Mitarbeitende SOLLTE bei Weggang frei gewordene Zuständigkeiten zuweisen.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Stellen Sie sicher, dass durch den Weggang von Mitarbeitenden keine Aufgaben des ISMS verwaisen – auch nicht bis zu einer geplanten Neueinstellung. Ordnen Sie stattdessen die Zuständigkeit für die Aufgaben/Rollenunverzüglich bestehendem Personal zu. Achten Sie dabei auch darauf, dass die festgelegten Rollentrennungen dabei nicht aufgehoben, bzw. durchbrochen werden. Um eine kontinuierliche Bearbeitung von Aufgaben sicherzustellen, ist eine Übergabe sinnvoll.

### → ORP.2.A2 — Geregelte Verfahrensweise beim Weggang von Mitarbeitenden (B) [Vorgesetzte, IT-Betrieb]
  1. Verlassen Mitarbeitende die Institution, MUSS der oder die Nachfolgende rechtzeitig eingewiesen werden. **◀ ZITIERT**
  2. Dies SOLLTE idealerweise durch den oder die ausscheidenden Mitarbeitenden erfolgen.
  3. Ist eine direkte Übergabe nicht möglich, MUSS von den ausscheidenden Mitarbeitenden eine ausführliche Dokumentation angefertigt werden.
  4. Außerdem MÜSSEN von ausscheidenden Mitarbeitenden alle im Rahmen ihrer Tätigkeit erhaltenen Unterlagen, Schlüssel und Geräte sowie Ausweise und Zutrittsberechtigungen eingezogen werden.
  5. Vor der Verabschiedung MUSS noch einmal auf Verschwiegenheitsverpflichtungen hingewiesen werden.
  6. Es SOLLTE besonders darauf geachtet werden, dass keine Interessenkonflikte auftreten.
  7. Um nach einem Stellenwechsel Interessenkonflikte zu vermeiden, SOLLTEN Konkurrenzverbote und Karenzzeiten vereinbart werden.
  8. Weiterhin MÜSSEN Notfall- und andere Ablaufpläne aktualisiert werden.
  9. Alle betroffenen Stellen innerhalb der Institution, wie z. B. das Sicherheitspersonal oder die IT-Abteilung, MÜSSEN über das Ausscheiden des oder der Mitarbeitenden informiert werden.
  10. Damit alle verbundenen Aufgaben, die beim Ausscheiden des oder der Mitarbeitenden anfallen, erledigt werden, SOLLTE hier ebenfalls eine Checkliste angelegt werden.
  11. Zudem SOLLTE es einen festen Ansprechpartner oder Ansprechpartnerin der Personalabteilung geben, der den Weggang von Mitarbeitenden begleitet.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 1) Satz 1 fordert die rechtzeitige Einweisung von Nachfolgenden beim Weggang von Mitarbeitenden und deckt damit die geregelte Übergabe frei gewordener Zuständigkeiten ab.


## PERS.2.2 — Rollen  [14 Paare]

**Statement (normativ):** Personal SOLLTE für alle Tätigkeiten im Geltungsbereich Rollen mit Zielen, Aufgaben, erforderlichen Kompetenzen und Qualifikationen verankern.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Eine Rolle beschreibt eine Stelle oder Personalposition innerhalb des ISMS. Sie benennt die Aufgaben der Position und die dazu erforderlichen Qualifikationsvoraussetzungen. Beispiele: Teamleiter, Entwickler, Admin, Sicherheitsanalyst, Fachaufgabenverantwortlicher.

### → APP.7.A5 — Geeignete Steuerung der Anwendungsentwicklung (S)
  1. Bei der Entwicklung von Individualsoftware SOLLTE ein geeignetes Steuerungs- und Projektmanagementmodell verwendet werden.
  2. Hierbei SOLLTE das ausgewählte Modell mit dem Auftragnehmenden abgestimmt werden.
  3. Bei der Steuerung SOLLTE es berücksichtigt werden.
  4. Es SOLLTE insbesondere berücksichtigt werden, dass das benötigte Personal ausreichend qualifiziert ist. **◀ ZITIERT**
  5. Alle relevanten Phasen SOLLTEN während des Lebenszyklus der Software abgedeckt werden.
  6. Außerdem SOLLTE es ein geeignetes Entwicklungsmodell, ein Risikomanagement sowie Qualitätsziele enthalten.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die G++-Maßnahme PERS.2.2 fordert als allgemeine Regelung die Verankerung von Rollen mit erforderlichen Kompetenzen und Qualifikationen für alle Tätigkeiten, was die Berücksichtigung ausreichend qualifizierten Personals bei der Entwicklung inhaltlich abdeckt.

### → CON.8.A1 — Definition von Rollen und Zuständigkeiten (S) [Zentrale Verwaltung]
  1. Für den Software-Entwicklungsprozess SOLLTE eine gesamtzuständige Person ein benannt werden.
  2. Außerdem SOLLTEN die Rollen und Zuständigkeiten für alle Aktivitäten im Rahmen der Software-Entwicklung festgelegt werden. **◀ ZITIERT**
  3. Die Rollen SOLLTEN dabei fachlich die nachfolgenden Themen abdecken: Requirements-Engineering (Anforderungsmanagement) und Änderungsmanagement, Software-Entwurf und -Architektur, Informationssicherheit in der Software-Entwicklung, Software-Implementierung in dem für das Entwicklungsvorhaben relevanten Bereichen, sowie Software-Tests.
  4. Für jedes Entwicklungsvorhaben SOLLTE eine zuständige Person für die Informationssicherheit benannt werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) PERS.2.2 fordert allgemein die Festlegung von Rollen für alle Tätigkeiten im Geltungsbereich und deckt damit die Definition von Rollen für Aktivitäten der Software-Entwicklung ab.

### → DER.4.A5 — Aufbau einer geeigneten Organisationsstruktur für das Notfallmanagement (H) [Institutionsleitung]
  1. Die Rollen für das Notfallmanagement SOLLTEN für die Gegebenheiten der Institution angemessen festgelegt werden.
  2. Dies SOLLTE mit den Aufgaben, Pflichten und Kompetenzen der Rollen schriftlich dokumentiert werden. **◀ ZITIERT**
  3. Es SOLLTEN für alle Rollen im Notfallmanagement qualifizierte Mitarbeitende benannt werden.
  4. Die Organisationsstruktur im Notfallmanagement SOLLTE regelmäßig darauf überprüft werden, ob sie praxistauglich, effektiv und effizient ist.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) Satz 2 fordert die Dokumentation von Rollen mit deren Aufgaben, Pflichten und Kompetenzen für das Notfallmanagement, was ein fachspezifischer Anwendungsfall von PERS.2.2 ist.

### → INF.1.A26 — Pforten- oder Sicherheitsdienst (H)
  1. Die Aufgaben des Pforten- oder Sicherheitsdienstes SOLLTEN klar dokumentiert sein. **◀ ZITIERT**
  2. Der Pfortendienst SOLLTE alle Personenbewegungen an der Pforte und an allen anderen Eingängen beobachten und, je nach Sicherheitskonzept, kontrollieren.
  3. Alle Mitarbeitenden und Besuchenden SOLLTEN sich bei dem Pfortendienst ausweisen können.
  4. Besuchende SOLLTEN zu den Besuchten begleitet oder an der Pforte abgeholt werden.
  5. Der Pfortendienst SOLLTE rechtzeitig darüber informiert werden, wenn sich Zutrittsberechtigungen ändern.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) PERS.2.2 fordert die Verankerung von Rollen einschließlich ihrer Aufgaben und Qualifikationen, was die Dokumentation der Aufgaben des Pforten- bzw. Sicherheitsdienstes als Rolle umfasst.

### → ISMS.1.A6 — Aufbau einer geeigneten Organisationsstruktur für Informationssicherheit (B) [Institutionsleitung]
  1. Eine geeignete übergreifende Organisationsstruktur für Informationssicherheit MUSS vorhanden sein.
  2. Dafür MÜSSEN Rollen definiert sein, die konkrete Aufgaben übernehmen, um die Sicherheitsziele zu erreichen. **◀ ZITIERT**
  3. Außerdem MÜSSEN qualifizierte Personen benannt werden, denen ausreichend Ressourcen zur Verfügung stehen, um diese Rollen zu übernehmen.
  4. Die Aufgaben, Rollen, Verantwortungen und Kompetenzen im Sicherheitsmanagement MÜSSEN nachvollziehbar definiert und zugewiesen sein. **◀ ZITIERT**
  5. Für alle wichtigen Funktionen der Organisation für Informationssicherheit MUSS es wirksame Vertretungsregelungen geben.
  6. Kommunikationswege MÜSSEN geplant, beschrieben, eingerichtet und bekannt gemacht werden.
  7. Es MUSS für alle Aufgaben und Rollen festgelegt sein, wer wen informiert und wer bei welchen Aktionen in welchem Umfang informiert werden muss.
  8. Es MUSS regelmäßig geprüft werden, ob die Organisationsstruktur für Informationssicherheit noch angemessen ist oder ob sie an neue Rahmenbedingungen angepasst werden muss.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) Die G++-Maßnahme PERS.2.2 fordert explizit die Verankerung von Rollen mit Zielen und Aufgaben, was die Forderung nach Definition von Rollen zur Übernahme konkreter Aufgaben direkt abdeckt.
- **Satz 4** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) PERS.2.2 fordert explizit die Verankerung von Rollen mit deren Aufgaben und erforderlichen Kompetenzen für Tätigkeiten im Geltungsbereich.

### → OPS.1.1.1.A2 — Festlegung von Rollen und Berechtigungen für den IT-Betrieb (B)
  1. Für alle betriebenen IT-Komponenten MUSS das jeweilige Rollen- und Berechtigungskonzept auch Rollen und zugehörige Berechtigungen für den IT-Betrieb festlegen.
  2. Für die Betriebsmittel MUSS ebenfalls ein Rollen- und Berechtigungskonzept erstellt werden.
  3. Das Rollen- und Berechtigungskonzept für den IT-Betrieb MUSS die IT-Nutzung von IT-Betriebsaufgaben trennen.
  4. Administrationsaufgaben und sonstige Betriebsaufgaben MÜSSEN durch unterschiedliche Rollen getrennt werden.
  5. Grundsätzlich SOLLTE der IT-Betrieb für unterschiedliche Betriebstätigkeiten unterschiedliche Rollen festlegen, die für die jeweiligen Tätigkeiten die erforderlichen Berechtigungen besitzen. **◀ ZITIERT**
  6. Sammel-Accounts DÜRFEN NUR in begründeten Ausnahmefällen eingerichtet werden.
  7. Die Rollen und Berechtigungen MÜSSEN regelmäßig geprüft und auf die aktuellen Gegebenheiten angepasst werden.
  8. Insbesondere MÜSSEN die Berechtigungen von ausgeschiedenem Personal auf den IT-Komponenten entfernt werden.
  9. Ebenso MÜSSEN die Rollen und Berechtigungen gelöscht werden, wenn IT-Komponenten außer Betrieb genommenen werden.
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 5) Satz 5 fordert die Festlegung spezifischer Rollen für unterschiedliche Tätigkeiten im IT-Betrieb, was eine fachspezifische Ausprägung der allgemeinen Rollendefinition für Tätigkeiten gemäß PERS.2.2 darstellt.

### → OPS.1.1.2.A21 — Regelung der IT-Administrationsrollen (B)
  1. Es MÜSSEN Rollen definiert werden, die ausschließlich zur IT-Administration vergeben werden. **◀ ZITIERT**
  2. Administrationsrollen MÜSSEN aufgrund des tatsächlichen Bedarfs im Aufgabenbereich der IT-Administration nachvollziehbar vergeben werden.
  3. Alle notwendigen IT-Administrationstätigkeiten MÜSSEN durch Berechtigungen in den Administrationsrollen nach dem Minimalprinzip abgedeckt sein.
  4. Die IT-Administration unterschiedlicher Ebenen der IT-Komponenten, z. B. die Trennung von Betriebssystem- und Anwendungsadministration, MUSS bei der Konzeption der Administrationsrollen berücksichtigt werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) PERS.2.2 deckt als übergeordnete Anforderung die allgemeine Definition und Verankerung von Rollen (einschließlich Administrationsrollen) für alle Tätigkeiten im Geltungsbereich ab.

### → OPS.1.1.2.A8 — Administration von Fachanwendungen (S)
  1. Es SOLLTE geregelt und dokumentiert werden, welche Administrationsaufgaben für Fachanwendungen vom IT-Betrieb und welche durch die Fachadministration durchgeführt werden. **◀ ZITIERT**
  2. Für Fachanwendungen SOLLTE identifiziert werden, welche Zugriffe der IT-Betrieb auf Systemebene benötigt.
  3. Alle Schnittstellen und Abhängigkeiten zwischen der Fachadministration und der Administration durch den IT-Betrieb SOLLTEN identifiziert werden.
  4. Immer wenn Administrationsprozesse erstellt und gepflegt werden, SOLLTEN die Zuständigkeiten und Abhängigkeiten dieser Schnittstellen berücksichtigt werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) PERS.2.2 deckt die Forderung ab, da das Verankern von Rollen mitsamt ihren Aufgaben die Zuteilung und Dokumentation von Administrationsaufgaben an IT-Betrieb und Fachadministration allgemein umfasst.

### → OPS.1.1.6.A7 — Personalauswahl der Software-Testenden (S) [Personalabteilung, Fachverantwortliche]
  1. Bei der Auswahl der Software-Testenden SOLLTEN gesonderte Auswahlkriterien berücksichtigt werden.
  2. Die Software-Testenden SOLLTEN die erforderliche berufliche Qualifikation haben. **◀ ZITIERT**
  3. Wird Individualsoftware auf Quellcode-Ebene überprüft, dann SOLLTEN die Testenden über ausreichendes Fachwissen über die zu testenden Programmiersprache und der Entwicklungsumgebung verfügen.
  4. Der Quellcode SOLLTE NICHT ausschließlich von Testenden überprüft werden, die auch an der Erstellung des Quellcodes beteiligt waren.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme PERS.2.2 fordert als allgemeine Regelung für alle Rollen und Tätigkeiten die Verankerung der erforderlichen Kompetenzen und Qualifikationen, was die geforderte berufliche Qualifikation von Software-Testenden abdeckt.

### → SYS.1.7.A18 — Rollenkonzept für z/OS-Systeme (S)
  1. Mindestens für die Systemverwaltung von z/OS-Systemen SOLLTE ein Rollenkonzept eingeführt werden. **◀ ZITIERT**
  2. Für alle wichtigen Rollen der Systemverwaltung SOLLTEN außerdem Stellvertretungsregelungen vorhanden sein.
  3. Die RACF-Attribute SPECIAL, OPERATIONS und AUDITOR SOLLTEN verschiedenen Personen zugeordnet werden (Rollentrennung).
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) PERS.2.2 fordert die allgemeine Verankerung von Rollen für alle Tätigkeiten im Geltungsbereich, was das geforderte Rollenkonzept für die Systemverwaltung abdeckt.

### → ORP.1.A1 — Festlegung von Verantwortlichkeiten und Regelungen (B) [Institutionsleitung]
  1. Innerhalb einer Institution MÜSSEN alle relevanten Aufgaben und Funktionen klar definiert und voneinander abgegrenzt sein. **◀ ZITIERT**
  2. Es MÜSSEN verbindliche Regelungen für die Informationssicherheit für die verschiedenen betrieblichen Aspekte übergreifend festgelegt werden.
  3. Die Organisationsstrukturen sowie verbindliche Regelungen MÜSSEN anlassbezogen überarbeitet werden.
  4. Die Änderungen MÜSSEN allen Mitarbeitenden bekannt gegeben werden.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 1) Satz 1 fordert die klare Definition aller relevanten Funktionen (Rollen) innerhalb der Institution, was sich direkt mit der Festlegung von Rollen in PERS.2.2 deckt.

### → OPS.1.1.1.A1 — Festlegung der Aufgaben und Zuständigkeiten des IT-Betriebs (B)
  1. Für alle betriebenen IT-Komponenten MUSS festgelegt werden, welche Aufgaben für den IT-Betrieb anfallen und wer dafür zuständig ist.
  2. Hierfür MÜSSEN die entsprechenden Rechte, Pflichten, Aufgaben mit den hierfür erforderlichen Tätigkeiten, Befugnisse und zugehörigen Prozesse geregelt werden. **◀ ZITIERT**
  3. Weiterhin MÜSSEN die Schnittstellen und Meldewege sowie das Eskalationsmanagement zwischen verschiedenen Betriebseinheiten und gegenüber anderen organisatorischen Einheiten der Institution festgelegt werden.
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme PERS.2.2 deckt die Regelung von Rollen, Aufgaben und Pflichten für Tätigkeiten im Geltungsbereich inhaltlich ab.

### → ORP.2.A15 — Qualifikation des Personals (B) [Vorgesetzte]
  1. Mitarbeitende MÜSSEN regelmäßig geschult bzw. weitergebildet werden.
  2. In allen Bereichen MUSS sichergestellt werden, dass kein Mitarbeitende mit veralteten Wissensstand arbeitet.
  3. Weiterhin SOLLTE den Mitarbeitenden während ihrer Beschäftigung die Möglichkeit gegeben werden, sich im Rahmen ihres Tätigkeitsfeldes weiterzubilden.
  4. Werden Stellen besetzt, MÜSSEN die erforderlichen Qualifikationen und Fähigkeiten genau formuliert sein. **◀ ZITIERT**
  5. Anschließend SOLLTE geprüft werden, ob diese bei den Bewerbenden für die Stelle tatsächlich vorhanden sind.
  6. Es MUSS sichergestellt sein, dass Stellen nur von Mitarbeitenden besetzt werden, für die sie qualifiziert sind.
- **Satz 4** | Relation GS++→ED23: `intersects-with` | Fundrichtung: beide
  Begründung: (Teilanforderung 4) PERS.2.2 fordert explizit die Festlegung erforderlicher Kompetenzen und Qualifikationen für Rollen bzw. Stellen, was die geforderte genaue Formulierung abdeckt.


## PERS.1.1.2 — Zuweisung der Aufgaben  [2 Paare]

**Statement (normativ):** Personal MUSS die mit den Verfahren und Regelungen verbundenen Aufgaben {{ insert: param, pers.1.1.2-prm1 }} zuweisen.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Die Zuweisung von Aufgaben bezeichnet die eindeutige und verbindliche Übertragung von konkreten Tätigkeiten und Verantwortlichkeiten des Änderungsprozesses, wie etwa die Risikobewertung, die technische Umsetzung oder die finale Freigabe, an definierte Stellen in der Institution. Der Sinn dieser Vorschrift ist es, die Verantwortlichkeit ("Accountability") für jeden einzelnen Schritt im Prozess klarzustellen. Ohne eine solche Zuweisung könnten kritische Prüfungen unterbleiben, weil sich niemand explizit zuständig fühlt, was wiederum die Wahrscheinlichkeit fehlgeschlagener Änderungen erhöht. Eine klare Regelung kann sicherstellen, dass keine Aufgaben übersehen werden und jede Tätigkeit von einer dafür qualifizierten und befugten Stelle ausgeführt wird, was die Prozesssicherheit signifikant erhöht. Eine bewährte Methode zur Umsetzung ist die Erstellung einer RACI-Matrix (Responsible, Accountable, Consulted, Informed), die tabellarisch für jeden Prozessschritt darstellt, wer für die Durchführung verantwortlich ist, wer die Gesamtverantwortung trägt, wer zu konsultieren und wer zu informieren ist. Diese Zuständigkeiten können auch direkt in einem Workflow- oder Ticketsystem abgebildet werden, sodass Aufgaben, wie beispielsweise Genehmigungsschritte, automatisch an die richtige Gruppe oder Person weitergeleitet werden. Sinnvoll ist es die Zuweisung anhand von Rollen (z.B. "Anwendungsverantwortlicher", "Netzwerkadministrator", "Change Manager") vorzunehmen, statt an konkrete Personen. Dieser Ansatz stellt sicher, dass die Prozesse auch bei Personalwechseln stabil weiterlaufen, da die Zuständigkeit an die Funktion und nicht an das Individuum gebunden ist.

### → ORP.1.A2 — Zuweisung der Zuständigkeiten (B) [Institutionsleitung]
  1. Für alle Geschäftsprozesse, Anwendungen, IT-Systeme, Räume und Gebäude sowie Kommunikationsverbindungen MUSS festgelegt werden, wer für diese und deren Sicherheit zuständig ist. **◀ ZITIERT**
  2. Alle Mitarbeitenden MÜSSEN darüber informiert sein, insbesondere wofür sie zuständig sind und welche damit verbundenen Aufgaben sie wahrnehmen.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 1) Satz 1 fordert die Festlegung von Zuständigkeiten für Geschäftsprozesse und IT-Ressourcen, was der Zuweisung von Aufgaben und Verantwortlichkeiten an Rollen oder Personen entspricht.

### → ISMS.1.A1 — Übernahme der Gesamtverantwortung für Informationssicherheit durch die Leitung (B) [Institutionsleitung]
  1. Die Institutionsleitung MUSS die Gesamtverantwortung für Informationssicherheit in der Institution übernehmen.
  2. Dies MUSS für alle Beteiligten deutlich erkennbar sein.
  3. Die Institutionsleitung MUSS den Sicherheitsprozess initiieren, steuern und kontrollieren.
  4. Die Institutionsleitung MUSS Informationssicherheit vorleben.
  5. Die Institutionsleitung MUSS die Zuständigkeiten für Informationssicherheit festlegen. **◀ ZITIERT**
  6. Die zuständigen Mitarbeitenden MÜSSEN mit den erforderlichen Kompetenzen und Ressourcen ausgestattet werden.
  7. Die Institutionsleitung MUSS sich regelmäßig über den Status der Informationssicherheit informieren lassen.
  8. Insbesondere MUSS sich die Institutionsleitung über mögliche Risiken und Konsequenzen aufgrund fehlender Sicherheitsmaßnahmen informieren lassen.
- **Satz 5** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 5) Satz 5 fordert das Festlegen von Zuständigkeiten für die Informationssicherheit, was sich direkt mit der Zuweisung von Aufgaben und Verantwortlichkeiten an zuständige Personen oder Rollen deckt.

