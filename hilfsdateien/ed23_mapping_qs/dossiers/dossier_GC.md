# Review-Dossier Praktik GC

Praktik GC: 29 Controls mit Mapping, 102 Paare gesamt. Gesampelt: 5 Controls (max/min/median Paarzahl + 2 zufällig).

## GC.11.1 — Dokumentenlenkung  [10 Paare]

**Statement (normativ):** Governance und Compliance MUSS ein Verfahren zur Lenkung der Dokumente im Rahmen des ISMS über ihren kompletten Lebenszyklus hinweg verankern.
**Klasse:** BSI-Methodik-Grundschutz-plus-plus | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Ziel eines Verfahrens zur Dokumentenlenkung ist die Sicherstellung der Nachvollziehbarkeit von Dokumenten. Das Verfahren stellt hierbei die Nachvollziehbarkeit über den gesamten Lebenszyklus des Dokuments sicher. Dies beinhaltet die Erstellung bzw. Übernahme (z. B. aus "Alt-Dokumenten" oder externen Dokumenten) der Dokumente mit Titel, Autor, Dokumenteneigentümer, Sicherheitsklassifikation, Erstelldatum sowie einheitlicher Formate. Des Weiteren beinhaltet dies die Steuerung mit einem Änderungsmanagement (Versionierung), einer einheitlichen Veröffentlichung, einer angemessen geschützten Ablage und ggf. auch Archivierung sowie einer Rücknahme.

### → ISMS.1.A13 — Dokumentation des Sicherheitsprozesses (S)
  1. Der Ablauf des Sicherheitsprozesses SOLLTE dokumentiert werden.
  2. Wichtige Entscheidungen und die Arbeitsergebnisse der einzelnen Phasen wie Sicherheitskonzept, Richtlinien oder Untersuchungsergebnisse von Sicherheitsvorfällen SOLLTEN ausreichend dokumentiert werden.
  3. Es SOLLTE eine geregelte Vorgehensweise für die Erstellung und Archivierung von Dokumentationen im Rahmen des Sicherheitsprozesses geben. **◀ ZITIERT**
  4. Regelungen SOLLTEN existieren, um die Aktualität und Vertraulichkeit der Dokumentationen zu wahren. **◀ ZITIERT**
  5. Von den vorhandenen Dokumenten SOLLTE die jeweils aktuelle Version kurzfristig zugänglich sein. **◀ ZITIERT**
  6. Außerdem SOLLTEN alle Vorgängerversionen zentral archiviert werden. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `equivalent-to` | Fundrichtung: beide
  Begründung: (Teilanforderung 3) Satz 3 fordert explizit eine geregelte Vorgehensweise für die Erstellung und Archivierung von Dokumentationen im Sicherheitsprozess, was der geforderten Dokumentenlenkung über den Lebenszyklus entspricht.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Das geforderte Verfahren zur Dokumentenlenkung über den gesamten Lebenszyklus umfasst explizit das Änderungsmanagement für die Aktualität sowie Klassifikation und geschützte Ablage für die Vertraulichkeit.
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) Das geforderte Verfahren zur Dokumentenlenkung über den gesamten Lebenszyklus umfasst die Versionierung, Veröffentlichung und Bereitstellung der jeweils aktuellen Dokumentenversionen.
- **Satz 6** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 6) GC.11.1 fordert ein Verfahren zur Dokumentenlenkung über den gesamten Lebenszyklus, welches explizit die Versionierung und Archivierung von ISMS-Dokumenten umfasst.

### → DER.3.1.A27 — Aufbewahrung und Archivierung von Unterlagen zu Audits und Revisionen (S)
  1. Die Institution SOLLTE Auditprogramme sowie Unterlagen zu Audits und Revisionen entsprechend den regulatorischen Anforderungen nachvollziehbar und revisionssicher ablegen und aufbewahren. **◀ ZITIERT**
  2. Dabei SOLLTE sichergestellt werden, dass lediglich berechtigte Personen auf Auditprogramme und Unterlagen zugreifen können.
  3. Die Institution SOLLTE die Auditprogramme und Unterlagen nach Ablauf der Aufbewahrungsfrist sicher vernichten.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) GC.11.1 fordert als allgemeinere Maßnahme die nachvollziehbare und geschützte Ablage sowie Archivierung von ISMS-Dokumenten über deren gesamten Lebenszyklus.

### → DER.4.A12 — Dokumentation im Notfallmanagement-Prozess (H)
  1. Der Ablauf des Notfallmanagement-Prozesses, die Arbeitsergebnisse der einzelnen Phasen und wichtige Entscheidungen SOLLTEN dokumentiert werden.
  2. Ein festgelegtes Verfahren SOLLTE sicherstellen, dass diese Dokumente regelmäßig aktualisiert werden. **◀ ZITIERT**
  3. Darüber hinaus SOLLTE der Zugriff auf die Dokumentation auf autorisierte Personen beschränkt werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) GC.11.1 verankert ein allgemeines Verfahren zur Dokumentenlenkung über den gesamten Lebenszyklus inklusive Änderungsmanagement, was das geforderte Verfahren zur Aktualisierung von Dokumenten abdeckt.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme GC.11.1 deckt die Beschränkung des Zugriffs auf autorisierte Personen als allgemeinere Fassung über die Vorgabe einer angemessen geschützten Ablage und Sicherheitsklassifikation im Rahmen der Dokumentenlenkung ab.

### → INF.12.A10 — Dokumentation und Kennzeichnung der Verkabelung (S) [IT-Betrieb, Haustechnik]
  1. Eine Institution SOLLTE sicherstellen, dass sie für ihre Verkabelung sowohl über eine interne als auch eine externe Dokumentation verfügt.
  2. Die interne Dokumentation MUSS alle Aufzeichnungen zur Installation und zum Betrieb der Verkabelung enthalten.
  3. Die interne Dokumentation SOLLTE so umfangreich angefertigt und gepflegt werden, dass der Betrieb und dessen Weiterentwicklung bestmöglich unterstützt werden.
  4. Die externe Dokumentation (Beschriftung von Anschlüssen zur Unterstützung des Betriebs) der Verkabelung SOLLTE möglichst neutral gehalten werden.
  5. Jede Veränderung im Netz SOLLTE dokumentiert werden.
  6. Eine Interims- oder Arbeitsversion der Dokumentation SOLLTE unmittelbar, d. h. am Tag selbst angepasst werden.
  7. Die Stamm-Dokumentation MUSS spätestens 4 Wochen nach Abschluss der jeweiligen Arbeiten aktualisiert sein.
  8. Es SOLLTE geprüft werden, ob ein Dokumentenmanagement für die Dokumentation eingesetzt werden kann. **◀ ZITIERT**
  9. Die Dokumentation SOLLTE regelmäßig überprüft und aktualisiert werden.
  10. Sämtliche technischen Einrichtungen, die im Rahmen der Verkabelung dokumentiert sind, MÜSSEN hinsichtlich der Dokumentationstreue spätestens nach 4 Jahren geprüft werden.
- **Satz 8** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 8) GC.11.1 fordert die übergeordnete Verankerung eines Verfahrens zur Dokumentenlenkung im ISMS, was den Einsatz bzw. die Prüfung eines Dokumentenmanagements für Dokumentationen allgemein abdeckt.

### → ISMS.1.A12 — Management-Berichte zur Informationssicherheit (S) [Institutionsleitung]
  1. Die Institutionsleitung SOLLTE sich regelmäßig über den Stand der Informationssicherheit informieren, insbesondere über die aktuelle Gefährdungslage sowie die Wirksamkeit und Effizienz des Sicherheitsprozesses.
  2. Dazu SOLLTEN Management-Berichte geschrieben werden, welche die wesentlichen relevanten Informationen über den Sicherheitsprozess enthalten, insbesondere über Probleme, Erfolge und Verbesserungsmöglichkeiten.
  3. Die Management-Berichte SOLLTEN klar priorisierte Maßnahmenvorschläge enthalten.
  4. Die Maßnahmenvorschläge SOLLTEN mit realistischen Abschätzungen zum erwarteten Umsetzungsaufwand versehen sein.
  5. Die Management-Berichte SOLLTEN revisionssicher archiviert werden. **◀ ZITIERT**
  6. Die Management-Entscheidungen über erforderliche Aktionen, den Umgang mit Restrisiken und mit Veränderungen von sicherheitsrelevanten Prozessen SOLLTEN dokumentiert sein.
  7. Die Management-Entscheidungen SOLLTEN revisionssicher archiviert werden. **◀ ZITIERT**
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) GC.11.1 fordert die übergeordnete Lenkung und revisionssichere Nachvollziehbarkeit bzw. Archivierung aller ISMS-Dokumente über deren gesamten Lebenszyklus hinweg und deckt damit auch Management-Berichte ab.
- **Satz 7** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 7) GC.11.1 deckt als übergeordnete Anforderung die nachvollziehbare Lenkung und revisionssichere Archivierung aller ISMS-Dokumente über deren gesamten Lebenszyklus hinweg ab.


## GC.9.1.1.1 — Informationssicherheitsbeauftragter  [3 Paare]

**Statement (normativ):** Governance und Compliance MUSS die Zuständigkeit für Informationssicherheit {{ insert: param, gc.9.1.1.1-prm1 }} , welche unmittelbar der Institutionsleitung unterstellt ist, zuweisen.
**Klasse:** BSI-Methodik-Grundschutz-plus-plus | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Informationssicherheit liegt in der Verantwortung der Institutionsleitung. Die operative Aufgabe „Informationssicherheit“ wird an einen Informationssicherheitsbeauftragten (ISB) delegiert, der diese Aufgabe innerhalb der Institution koordiniert und vorantreibt. Daher ist diese Rolle in jeder Institution (unabhängig von Art und Größe) zu besetzen. Je nach Art und Ausrichtung der Institution wird der ISB anders genannt. Häufige Titel sind neben dem Informationssicherheitsbeauftragten, Chief Information Security Officer (CISO) oder Informationssicherheitsmanager (ISM). Die Hauptaufgabe des ISB besteht darin, die Institutionsleitung bei deren Aufgabenwahrnehmung bezüglich der Informationssicherheit zu beraten und diese bei der Umsetzung zu unterstützen. Zu den ISB-Aufgaben gehört es u.a., den Sicherheitsprozess operativ zu steuern und zu koordinieren, die Institutionsleitung bei der Erstellung der Sicherheitsleitlinie zu unterstützen, die Erstellung des Sicherheitskonzepts und zugehöriger Teilkonzepte und Richtlinien zu koordinieren, den Umsetzungsplan für Sicherheitsmaßnahmen anzufertigen, sowie ihre Umsetzung zu initiieren und zu überprüfen, der Institutionsleitung und anderen Sicherheitsverantwortlichen über den Status der Informationssicherheit zu berichten, sicherheitsrelevante Projekte zu koordinieren, sicherheitsrelevante Vorfälle zu untersuchen, sowie Sensibilisierungen und Schulungen zur Informationssicherheit zu initiieren und zu koordinieren.

### → IND.1.A1 — Einbindung in die Sicherheitsorganisation (B)
  1. Ein Managementsystem für Informationssicherheit (ISMS) für den Betrieb der OT-Infrastruktur MUSS entweder als selbständiges ISMS oder als Teil eines Gesamt-ISMS existieren.
  2. Eine gesamtverantwortliche Person für die Informationssicherheit im OT-Bereich MUSS benannt werden. **◀ ZITIERT**
  3. Er oder sie MUSS innerhalb der Institution bekannt gegeben werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) Die G++-Maßnahme GC.9.1.1.1 fordert als allgemeine Entsprechung die Benennung bzw. Zuweisung der Zuständigkeit für Informationssicherheit an eine verantwortliche Person (ISB).

### → ISMS.1.A4 — Benennung eines oder einer Informationssicherheitsbeauftragten (B) [Institutionsleitung]
  1. Die Institutionsleitung MUSS einen oder eine ISB benennen. **◀ ZITIERT**
  2. Der oder die ISB MUSS die Informationssicherheit in der Institution fördern und den Sicherheitsprozess mitsteuern und koordinieren. **◀ ZITIERT**
  3. Die Institutionsleitung MUSS den oder die ISB mit angemessenen Ressourcen ausstatten.
  4. Die Institutionsleitung MUSS dem oder der ISB die Möglichkeit einräumen, bei Bedarf direkt an sie selbst zu berichten.
  5. Der oder die ISB MUSS bei allen größeren Projekten sowie bei der Einführung neuer Anwendungen und IT-Systeme frühzeitig beteiligt werden.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) GC.9.1.1.1 verlangt explizit die Zuweisung der Zuständigkeit für Informationssicherheit an eine Person, was der Benennung eines ISB entspricht.
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) GC.9.1.1.1 weist die Zuständigkeit für Informationssicherheit dem ISB zu, zu dessen Kernaufgaben laut Erläuterung genau die Steuerung, Koordinierung und Förderung des Sicherheitsprozesses gehört.


## GC.9.1.1.1.2 — Vorspracherecht  [1 Paare]

**Statement (normativ):** Governance und Compliance MUSS das direkte Vorspracherecht des Informationssicherheitsbeauftragten bei der Institutionsleitung verankern.
**Klasse:** BSI-Methodik-Grundschutz-plus-plus | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Das Vorspracherecht trägt dazu bei, dass die Institutionsleitung ein vollständiges und unverfälschtes Bild über den Stand der Informationssicherheit erhält. Ohne dieses direkte Vorsprachrecht kann es passieren, dass andere Organisationseinheiten sicherheitsrelevante Informationen in der Weitergabe beeinflussen. Zum Beispiel könnte ein ISB dem Leitungsstab zugeordnet sein.

### → ISMS.1.A4 — Benennung eines oder einer Informationssicherheitsbeauftragten (B) [Institutionsleitung]
  1. Die Institutionsleitung MUSS einen oder eine ISB benennen.
  2. Der oder die ISB MUSS die Informationssicherheit in der Institution fördern und den Sicherheitsprozess mitsteuern und koordinieren.
  3. Die Institutionsleitung MUSS den oder die ISB mit angemessenen Ressourcen ausstatten.
  4. Die Institutionsleitung MUSS dem oder der ISB die Möglichkeit einräumen, bei Bedarf direkt an sie selbst zu berichten. **◀ ZITIERT**
  5. Der oder die ISB MUSS bei allen größeren Projekten sowie bei der Einführung neuer Anwendungen und IT-Systeme frühzeitig beteiligt werden.
- **Satz 4** | Relation GS++→ED23: `equivalent-to` | Fundrichtung: beide
  Begründung: (Teilanforderung 4) Die G++-Maßnahme fordert explizit das direkte Vorspracherecht des ISB bei der Institutionsleitung, was der geforderten Möglichkeit zur direkten Berichterstattung inhaltlich genau entspricht.


## GC.3.1.1 — Gesetzliche Verpflichtungen  [10 Paare]

**Statement (normativ):** Governance und Compliance MUSS gesetzliche Verpflichtungen, welche die Verarbeitung von Informationen durch die Institution betreffen, analysieren.
**Klasse:** BSI-Methodik-Grundschutz-plus-plus | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Gesetzliche Verpflichtungen, welche die Verarbeitung von Informationen durch die Institution betreffen, sind dokumentiert. Gesetzliche Verpflichtungen meint alle Pflichten, die sich unmittelbar aus dem Recht ergeben, inklusive des Verfassungsrechts, Europarechts und Verordnungen. Relevante gesetzliche Verpflichtungen können sich je nach Institution z. B. aus Grundrechten, Cyber Resilience Act, Data Act, Digital Markets Act, NIS, DSGVO, BDSG, TKG, TDDDG oder GeschGehG ergeben. Hierbei werden Verpflichtungen, die sich mittelbar auswirken wie die Arbeitsstättenverordnung oder allgemeine Regelungen zur Fürsorgepflicht, auch beachtet.

### → APP.3.2.A7 — Rechtliche Rahmenbedingungen für Webangebote (B) [Fachverantwortliche, Zentrale Verwaltung, Compliance-Beauftragte]
  1. Werden über den Webserver Inhalte für Dritte publiziert oder Dienste angeboten, MÜSSEN dabei die relevanten rechtlichen Rahmenbedingungen beachtet werden. **◀ ZITIERT**
  2. Die Institution MUSS die jeweiligen Telemedien- und Datenschutzgesetze sowie das Urheberrecht einhalten. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) GC.3.1.1 fordert die allgemeine Analyse aller gesetzlichen Verpflichtungen bei der Informationsverarbeitung und deckt damit die Beachtung relevanter rechtlicher Rahmenbedingungen für Webangebote auf einer übergeordneten Ebene ab.
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) GC.3.1.1 fordert die Analyse gesetzlicher Verpflichtungen der Informationsverarbeitung (darunter Telemedien- und Datenschutzrecht) und deckt damit die allgemeine Pflicht zur Erfassung und Beachtung dieser rechtlichen Vorgaben ab.

### → APP.6.A2 — Erstellung eines Anforderungskatalogs für Software (B) [Fachverantwortliche]
  1. Auf Basis der Ergebnisse der Planung MÜSSEN die Anforderungen an die Software in einem Anforderungskatalog erhoben werden.
  2. Der Anforderungskatalog MUSS dabei die grundlegenden funktionalen Anforderungen umfassen.
  3. Darüber hinaus MÜSSEN die nichtfunktionalen Anforderungen und hier insbesondere die Sicherheitsanforderungen in den Anforderungskatalog integriert werden.
  4. Hierbei MÜSSEN sowohl die Anforderungen von den Fachverantwortlichen als auch vom IT-Betrieb berücksichtigt werden.
  5. Insbesondere MÜSSEN auch die rechtlichen Anforderungen, die sich aus dem Kontext der zu verarbeitenden Daten ergeben, berücksichtigt werden. **◀ ZITIERT**
  6. Der fertige Anforderungskatalog SOLLTE mit allen betroffenen Fachabteilungen abgestimmt werden.
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) GC.3.1.1 deckt die Forderung als allgemeinere Maßnahme ab, da sie die systematische Analyse aller gesetzlichen Verpflichtungen bezüglich der Informationsverarbeitung in der Institution verlangt.

### → DER.1.A2 — Einhaltung rechtlicher Bedingungen bei der Auswertung von Protokollierungsdaten (B)
  1. Wenn Protokollierungsdaten ausgewertet werden, dann MÜSSEN dabei die Bestimmungen aus den aktuellen Gesetzen zum Bundes- und Landesdatenschutz eingehalten werden.
  2. Wenn Detektionssysteme eingesetzt werden, dann MÜSSEN die Persönlichkeitsrechte bzw. Mitbestimmungsrechte der Mitarbeitendenvertretungen gewahrt werden.
  3. Ebenso MUSS sichergestellt sein, dass alle weiteren relevanten gesetzlichen Bestimmungen beachtet werden, z. B. das Telemediengesetz (TMG), das Betriebsverfassungsgesetz und das Telekommunikationsgesetz. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) GC.3.1.1 fordert die allgemeine Analyse und Erfassung gesetzlicher Verpflichtungen bei der Informationsverarbeitung (wie TKG und TDDDG), was die Beachtung dieser rechtlichen Bestimmungen aus Satz 3 grundlegend abdeckt.

### → NET.3.2.A21 — Temporäre Entschlüsselung des Datenverkehrs (S)
  1. Verschlüsselte Verbindungen in nicht vertrauenswürdige Netze SOLLTEN temporär entschlüsselt werden, um das Protokoll zu verifizieren und die Daten auf Schadsoftware zu prüfen.
  2. Hierbei SOLLTEN die rechtlichen Rahmenbedingungen beachtet werden. **◀ ZITIERT**
  3. Die Komponente, die den Datenverkehr temporär entschlüsselt, SOLLTE unterbinden, dass veraltete Verschlüsselungsoptionen und kryptografische Algorithmen benutzt werden.
  4. Der eingesetzte TLS-Proxy SOLLTE prüfen können, ob Zertifikate vertrauenswürdig sind.
  5. Ist ein Zertifikat nicht vertrauenswürdig, SOLLTE es möglich sein, die Verbindung abzuweisen.
  6. Eigene Zertifikate SOLLTEN nachrüstbar sein, um auch „interne“ Root-Zertifikate konfigurieren und prüfen zu können.
  7. Vorkonfigurierte Zertifikate SOLLTEN überprüft und entfernt werden, wenn sie nicht benötigt werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme GC.3.1.1 deckt als allgemeine Anforderung zur Analyse gesetzlicher Verpflichtungen bei der Informationsverarbeitung die Beachtung rechtlicher Rahmenbedingungen bei der Entschlüsselung inhaltlich ab.

### → OPS.1.1.5.A8 — Archivierung von Protokollierungsdaten (S)
  1. Protokollierungsdaten SOLLTEN archiviert werden.
  2. Dabei SOLLTEN die gesetzlich vorgeschriebenen Regelungen berücksichtigt werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme GC.3.1.1 fordert die Analyse gesetzlicher Verpflichtungen bei der Informationsverarbeitung und deckt damit die allgemeinere Pflicht zur Berücksichtigung gesetzlicher Regelungen bei der Archivierung von Daten ab.

### → OPS.2.2.A2 — Erstellung einer Sicherheitsrichtlinie für die Cloud-Nutzung (B) [Fachverantwortliche]
  1. Auf Basis der Strategie für die Cloud-Nutzung MUSS eine Sicherheitsrichtlinie für die Cloud-Nutzung erstellt werden.
  2. Sie MUSS konkrete Sicherheitsvorgaben beinhalten, mit denen sich Cloud-Dienste innerhalb der Institution umsetzen lassen.
  3. Außerdem MÜSSEN darin spezielle Sicherheitsanforderungen an die Cloud-Diensteanbietenden sowie das festgelegte Schutzniveau für Cloud-Dienste hinsichtlich Vertraulichkeit, Integrität und Verfügbarkeit dokumentiert werden.
  4. Wenn Cloud-Dienste von internationalen Anbietenden genutzt werden, MÜSSEN die speziellen länderspezifischen Anforderungen und gesetzlichen Bestimmungen berücksichtigt werden. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) GC.3.1.1 fordert die allgemeine Analyse aller gesetzlichen Verpflichtungen der Informationsverarbeitung, was die Berücksichtigung länderspezifischer gesetzlicher Bestimmungen bei internationalen Anbietern umfasst.

### → ORP.5.A1 — Identifikation der Rahmenbedingungen (B) [Zentrale Verwaltung, Institutionsleitung]
  1. Alle gesetzlichen, vertraglichen und sonstigen Vorgaben mit Auswirkungen auf das Informationssicherheitsmanagement MÜSSEN identifiziert und dokumentiert werden. **◀ ZITIERT**
  2. Die für die einzelnen Bereiche der Institution relevanten gesetzlichen, vertraglichen und sonstigen Vorgaben SOLLTEN in einer strukturierten Übersicht herausgearbeitet werden.
  3. Die Dokumentation MUSS auf dem aktuellen Stand gehalten werden.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) Die Maßnahme GC.3.1.1 deckt die im Satz geforderte Identifikation und Dokumentation bezüglich der gesetzlichen Vorgaben als wesentlichen Teilbereich inhaltlich ab.

### → ORP.5.A4 — Konzeption und Organisation des Compliance Managements (S) [Institutionsleitung]
  1. In der Institution SOLLTE ein Prozess aufgebaut werden, um alle relevanten gesetzlichen, vertraglichen und sonstigen Vorgaben mit Auswirkungen auf das Informationssicherheitsmanagement zu identifizieren. **◀ ZITIERT**
  2. Es SOLLTEN geeignete Prozesse und Organisationsstrukturen aufgebaut werden, um basierend auf der Identifikation und Beachtung der rechtlichen Rahmenbedingungen, den Überblick über die verschiedenen rechtlichen Anforderungen an die einzelnen Bereiche der Institution zu gewährleisten.
  3. Dafür SOLLTEN Zuständige für das Compliance Management festgelegt werden.
  4. Compliance-Beauftragte und Informationssicherheitsbeauftragte SOLLTEN sich regelmäßig austauschen.
  5. Sie SOLLTEN gemeinsam Sicherheitsanforderungen ins Compliance Management integrieren, sicherheitsrelevante Anforderungen in Sicherheitsmaßnahmen überführen und deren Umsetzung kontrollieren.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 1) Satz 1 fordert die Etablierung eines Prozesses zur Identifikation relevanter gesetzlicher Vorgaben für die Informationssicherheit, was sich direkt mit der Analyse gesetzlicher Verpflichtungen aus GC.3.1.1 deckt.

### → APP.4.2.A6 — Erstellung und Umsetzung eines Konten- und Berechtigungskonzeptes (B) [Fachabteilung, Entwickelnde]
  1. Für SAP-ERP-Systeme MUSS ein Konten- und Berechtigungskonzept ausgearbeitet und umgesetzt werden.
  2. Dabei MÜSSEN folgende Punkte berücksichtigt werden: Identitätsprinzip, Minimalprinzip, Stellenprinzip, Belegprinzip der Buchhaltung, Belegprinzip der Berechtigungsverwaltung, Funktionstrennungsprinzip (Segregation of Duties, SoD), Genehmigungsprinzip, Standardprinzip, Schriftformprinzip und Kontrollprinzip MÜSSEN berücksichtigt werden.
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
  13. Gesetzliche und interne Rahmenbedingungen wie die Grundsätze ordnungsgemäßer Buchführung (GoB), das Handelsgesetzbuch (HGB) oder interne Vorgaben der Institution MÜSSEN berücksichtigt werden. **◀ ZITIERT**
  14. Das Konten- und Berechtigungskonzept SOLLTE auch den Betrieb technischer Konten abdecken, also auch die Berechtigung von Hintergrund- und Schnittstellenkonten.
  15. Es SOLLTEN geeignete Kontrollmechanismen angewandt werden, um SoD-Konfliktfreiheit von Rollen und die Vergabe von kritischen Berechtigungen an Konten zu überwachen.
  16. Werden neben dem ABAP-Backend weitere Komponenten wie SAP HANA und SAP NetWeaver Gateway (für Fiori-Anwendungen) verwendet, MUSS das Design der Berechtigungen zwischen den Komponenten abgestimmt und synchronisiert werden.
- **Satz 13** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 13) Die allgemeine G++-Anforderung zur Analyse gesetzlicher Verpflichtungen für die Informationsverarbeitung deckt die Berücksichtigung gesetzlicher Rahmenbedingungen (wie GoB und HGB) inhaltlich ab.


## GC.1.2 — Freigabe des ISMS  [4 Paare]

**Statement (normativ):** Governance und Compliance MUSS alle festgelegten Verfahren für das ISMS durch die Institutionsleitung autorisieren.
**Klasse:** BSI-Methodik-Grundschutz-plus-plus | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Die Freigabe des Prozesses der ISMS-Verfahren erfolgt durch die Institutionsleitung. Diese Freigabe sollte dokumentiert werden, um Verbindlichkeit und Nachvollziehbarkeit sicherzustellen. Beispielsweise kann diese Freigabe durch die Vorlage eines Managementberichts eingeholt werden.

### → DER.2.1.A7 — Etablierung einer Vorgehensweise zur Behandlung von Sicherheitsvorfällen (S) [Institutionsleitung]
  1. Es SOLLTE eine geeignete Vorgehensweise zur Behandlung von Sicherheitsvorfällen definiert werden.
  2. Die Abläufe, Prozesse und Vorgaben für die verschiedenen Sicherheitsvorfälle SOLLTEN dabei eindeutig geregelt und geeignet dokumentiert werden.
  3. Die Institutionsleitung SOLLTE die festgelegte Vorgehensweise in Kraft setzen und allen Beteiligten zugänglich machen. **◀ ZITIERT**
  4. Es SOLLTE regelmäßig überprüft werden, ob die Vorgehensweise noch aktuell und wirksam ist.
  5. Bei Bedarf SOLLTE die Vorgehensweise angepasst werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) GC.1.2 verlangt die Autorisierung aller ISMS-Verfahren durch die Institutionsleitung, was das Inkraftsetzen der festgelegten Vorgehensweisen durch die Leitung als allgemeinere Pflicht abdeckt.

### → DER.3.2.A2 — Erstellung eines IS-Revisionshandbuches (B)
  1. Für die IS-Revision MUSS ein IS-Revisionshandbuch erstellt werden, das die angestrebten Ziele, einzuhaltende gesetzliche Vorgaben, Informationen über die Organisation, die Ressourcen und die Rahmenbedingungen enthält.
  2. Außerdem MUSS darin die Archivierung der Dokumentation beschrieben sein.
  3. Das Handbuch MUSS von der Leitungsebene verabschiedet werden. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die Maßnahme GC.1.2 fordert die Autorisierung aller ISMS-Verfahren durch die Institutionsleitung, was die Verabschiedung des IS-Revisionshandbuchs durch die Leitungsebene als allgemeinere Fassung abdeckt.

### → DER.2.1.A2 — Erstellung einer Richtlinie zur Behandlung von Sicherheitsvorfällen (B)
  1. Eine Richtlinie zur Behandlung von Sicherheitsvorfällen MUSS erstellt werden.
  2. Darin MÜSSEN Zweck und Ziel der Richtlinie definiert sowie alle Aspekte der Behandlung von Sicherheitsvorfällen geregelt werden.
  3. So MÜSSEN Verhaltensregeln für die verschiedenen Arten von Sicherheitsvorfällen beschrieben sein.
  4. Zusätzlich MUSS es für alle Mitarbeitenden zielgruppenorientierte und praktisch anwendbare Handlungsanweisungen geben.
  5. Weiterhin SOLLTEN die Schnittstellen zu anderen Managementbereichen berücksichtigt werden, z. B. zum Notfallmanagement.
  6. Die Richtlinie MUSS allen Mitarbeitenden bekannt sein.
  7. Sie MUSS mit dem IT-Betrieb abgestimmt und durch die Institutionsleitung verabschiedet sein. **◀ ZITIERT**
  8. Die Richtlinie MUSS regelmäßig geprüft und aktualisiert werden.
- **Satz 7** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 7) GC.1.2 deckt als übergeordnete Regelung die Verabschiedung und Autorisierung von ISMS-Verfahren und -Richtlinien durch die Institutionsleitung ab.

### → ISMS.1.A12 — Management-Berichte zur Informationssicherheit (S) [Institutionsleitung]
  1. Die Institutionsleitung SOLLTE sich regelmäßig über den Stand der Informationssicherheit informieren, insbesondere über die aktuelle Gefährdungslage sowie die Wirksamkeit und Effizienz des Sicherheitsprozesses.
  2. Dazu SOLLTEN Management-Berichte geschrieben werden, welche die wesentlichen relevanten Informationen über den Sicherheitsprozess enthalten, insbesondere über Probleme, Erfolge und Verbesserungsmöglichkeiten.
  3. Die Management-Berichte SOLLTEN klar priorisierte Maßnahmenvorschläge enthalten.
  4. Die Maßnahmenvorschläge SOLLTEN mit realistischen Abschätzungen zum erwarteten Umsetzungsaufwand versehen sein.
  5. Die Management-Berichte SOLLTEN revisionssicher archiviert werden.
  6. Die Management-Entscheidungen über erforderliche Aktionen, den Umgang mit Restrisiken und mit Veränderungen von sicherheitsrelevanten Prozessen SOLLTEN dokumentiert sein. **◀ ZITIERT**
  7. Die Management-Entscheidungen SOLLTEN revisionssicher archiviert werden.
- **Satz 6** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 6) Satz 6 fordert die Dokumentation von Management-Entscheidungen bezüglich Veränderungen von sicherheitsrelevanten Prozessen, was die Autorisierung und Freigabe von ISMS-Verfahren durch die Leitung umfasst.

