# Review-Dossier Praktik UMS

Praktik UMS: 10 Controls mit Mapping, 83 Paare gesamt. Gesampelt: 5 Controls (max/min/median Paarzahl + 2 zufällig).

## UMS.2.2 — Priorisierung von Maßnahmen  [1 Paare]

**Statement (normativ):** Umsetzung MUSS eine Priorisierung der festgelegten Maßnahmen auf Basis der Risikobewertung, Abhängigkeiten und Ressourcenverfügbarkeit festlegen.
**Klasse:** BSI-Methodik-Grundschutz-plus-plus | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Es ist eine geeignete Priorisierung der Anforderungen und Maßnahmenumsetzung vorzunehmen. Gesetzliche Verpflichtungen und Compliance, der Umsetzungsaufwand einer Anforderung bzw. Maßnahme oder die Risikomitigierung der Anforderungen können bei der Priorisierung helfen.

### → ISMS.1.A12 — Management-Berichte zur Informationssicherheit (S) [Institutionsleitung]
  1. Die Institutionsleitung SOLLTE sich regelmäßig über den Stand der Informationssicherheit informieren, insbesondere über die aktuelle Gefährdungslage sowie die Wirksamkeit und Effizienz des Sicherheitsprozesses.
  2. Dazu SOLLTEN Management-Berichte geschrieben werden, welche die wesentlichen relevanten Informationen über den Sicherheitsprozess enthalten, insbesondere über Probleme, Erfolge und Verbesserungsmöglichkeiten.
  3. Die Management-Berichte SOLLTEN klar priorisierte Maßnahmenvorschläge enthalten. **◀ ZITIERT**
  4. Die Maßnahmenvorschläge SOLLTEN mit realistischen Abschätzungen zum erwarteten Umsetzungsaufwand versehen sein.
  5. Die Management-Berichte SOLLTEN revisionssicher archiviert werden.
  6. Die Management-Entscheidungen über erforderliche Aktionen, den Umgang mit Restrisiken und mit Veränderungen von sicherheitsrelevanten Prozessen SOLLTEN dokumentiert sein.
  7. Die Management-Entscheidungen SOLLTEN revisionssicher archiviert werden.
- **Satz 3** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 3) Satz 3 fordert explizit, dass Berichte klar priorisierte Maßnahmenvorschläge enthalten sollen, was sich direkt mit der geforderten Priorisierung von Maßnahmen deckt.


## UMS.5.2 — Dokumentation von Ausnahmen  [27 Paare]

**Statement (normativ):** Umsetzung MUSS Ausnahmegenehmigungen mit Begründung dokumentieren.
**Klasse:** BSI-Methodik-Grundschutz-plus-plus | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Um rechtlich bedeutsame Entscheidungen zur Informationsverarbeitung später nachvollziehen und ggf. anpassen zu können, ist eine Dokumentation dieser Entscheidungen wichtig. Die Dokumentation muss nicht separat von Geschäftsprozessen vorgenommen werden. Vielmehr ist es sogar empfehlenswert, Geschäftsprozesse und Entscheidungsdokumentation zu integrieren, z. B. in CMDBs, Aktenverzeichnissen, Commit-Messages oder Ticketsystemen. Hierbei sind auch die Anforderungen zur "Aufgabenzuweisung" und "Anweisung zur Einhaltung" zu berücksichtigen.

### → APP.2.2.A3 — Planung der Gruppenrichtlinien unter Windows (B)
  1. Es MUSS ein Konzept zur Einrichtung von Gruppenrichtlinien vorliegen.
  2. Mehrfachüberdeckungen MÜSSEN beim Gruppenrichtlinienkonzept möglichst vermieden werden.
  3. In der Dokumentation des Gruppenrichtlinienkonzepts MÜSSEN Ausnahmeregelungen erkannt werden können. **◀ ZITIERT**
  4. Alle Gruppenrichtlinienobjekte MÜSSEN durch restriktive Zugriffsrechte geschützt sein.
  5. Für die Parameter in allen Gruppenrichtlinienobjekten MÜSSEN sichere Vorgaben festgelegt sein.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die allgemeine Pflicht zur Dokumentation von Ausnahmegenehmigungen in UMS.5.2 deckt die fachspezifische Forderung ab, Ausnahmeregelungen im Gruppenrichtlinienkonzept nachvollziehbar zu dokumentieren.

### → APP.4.6.A12 — Vermeidung von generischer Modulausführung (S)
  1. Transaktionen, Programme, Funktionsbausteine und Methoden SOLLTEN NICHT generisch ausführbar sein.
  2. Sollte es wichtige Gründe für eine generische Ausführung geben, SOLLTE detailliert dokumentiert werden, wo und warum dies geschieht. **◀ ZITIERT**
  3. Zusätzlich SOLLTE eine Allowlist definiert werden, die alle erlaubten Module enthält.
  4. Bevor ein Modul aufgerufen wird, SOLLTE die Eingabe von Benutzenden mit der Allowlist abgeglichen werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme UMS.5.2 fordert die allgemeine Dokumentation von Ausnahmegenehmigungen mit Begründung und deckt damit die geforderte Dokumentation von Ausnahmen und Gründen bei generischer Modulausführung ab.

### → APP.4.6.A13 — Vermeidung von generischem Zugriff auf Tabelleninhalte (S)
  1. Tabelleninhalte SOLLTEN NICHT generisch ausgelesen werden.
  2. Sollte es wichtige Gründe dafür geben, dies doch zu tun, SOLLTE detailliert dokumentiert werden, wo und warum dies geschieht. **◀ ZITIERT**
  3. Außerdem SOLLTE dann gewährleistet sein, dass sich der dynamische Tabellenname auf eine kontrollierbare Liste von Werten beschränkt.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme fordert allgemein die Dokumentation von Ausnahmegenehmigungen mit Begründung, was die geforderte Dokumentation von Abweichungen (wo und warum) inhaltlich abdeckt.

### → APP.4.6.A16 — Verzicht auf systemabhängige Funktionsausführung (S)
  1. ABAP-Programme SOLLTEN NICHT systemabhängig programmiert werden, so dass sie nur auf einem bestimmten SAP-System ausgeführt werden können.
  2. Sollte dies jedoch unbedingt erforderlich sein, SOLLTE es detailliert dokumentiert werden. **◀ ZITIERT**
  3. Außerdem SOLLTE der Code dann manuell überprüft werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme fordert die allgemeine Dokumentation von Ausnahmen und deckt damit die geforderte Dokumentation für den Ausnahmefall einer systemabhängigen ABAP-Programmierung direkt ab.

### → CON.2.A1 — Umsetzung Standard-Datenschutzmodell (B)
  1. Die gesetzlichen Bestimmungen zum Datenschutz (DSGVO, BDSG, die Datenschutzgesetze der Bundesländer und gegebenenfalls einschlägige bereichsspezifische Datenschutzregelungen) MÜSSEN eingehalten werden.
  2. Wird die SDM-Methodik nicht berücksichtigt, die Maßnahmen also nicht auf der Basis der Gewährleistungsziele systematisiert und mit dem Referenzmaßnahmen-Katalog des SDM abgeglichen, SOLLTE dies begründet und dokumentiert werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme fordert die allgemeine Dokumentation von Ausnahmen mit Begründung, was die geforderte begründete Dokumentation bei Nicht-Anwendung der SDM-Methodik als Spezialfall abdeckt.

### → NET.3.4.A20 — Einsatz von MACsec (H)
  1. Für jedes Datenpaket SOLLTE die Datenintegrität gewährleistet werden.
  2. Darüber hinaus SOLLTE erwogen werden, diese Daten zu verschlüsseln.
  3. Hierfür SOLLTE MACsec gemäß IEEE 802.1AE genutzt werden.
  4. Access-Switches und Endgeräte, die MACsec nicht unterstützen oder für die MACsec nicht eingerichtet werden soll, SOLLTEN erfasst werden. **◀ ZITIERT**
  5. Für diese SOLLTE regelmäßig überprüft werden, ob die Ausschlussgründe noch gelten.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Das Erfassen von Geräten, bei denen MACsec nicht eingerichtet werden kann oder soll, ist ein spezifischer Anwendungsfall der allgemeinen Dokumentation von Ausnahmegenehmigungen gemäß UMS.5.2.

### → NET.3.4.A27 — Prüfung der Notwendigkeit für MAC-Adress-Authentisierung (H)
  1. Eine Authentisierung über MAC-Adressen SOLLTE nur dort genutzt werden, wo dies technisch unumgänglich ist und die Sicherheitsrichtlinien dies zulassen.
  2. Es SOLLTE im Vorfeld geprüft werden, ob solche Ausnahmefälle notwendig sind.
  3. Ist dies der Fall, SOLLTEN die Ausnahmefälle auf den minimalen Einsatzbereich eingeschränkt werden.
  4. Die Begründung und das Ergebnis der Prüfung SOLLTEN dokumentiert werden. **◀ ZITIERT**
  5. Sie SOLLTEN regelmäßig und bei Bedarf nochmals verifiziert werden.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) G++ UMS.5.2 deckt die Forderung ab, da sie allgemein die Dokumentation von Ausnahmegenehmigungen samt Begründung vorschreibt.

### → NET.3.4.A7 — Nutzung sicherer Authentisierungsverfahren (S)
  1. Endgeräte SOLLTEN sichere Authentisierungsverfahren nach dem Stand der Technik verwenden.
  2. Endgeräte SOLLTEN automatisiert auf Basis von Zertifikaten oder Zugangskonten authentisiert werden.
  3. Unsichere Authentisierungsverfahren SOLLTEN nur in begründeten Ausnahmefällen genutzt und die Entscheidung dokumentiert werden. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme fordert allgemein die Dokumentation von begründeten Ausnahmegenehmigungen und deckt damit die geforderte Begründung und Dokumentation von Ausnahmen bei Authentisierungsverfahren ab.

### → OPS.1.1.3.A15 — Regelmäßige Aktualisierung von IT-Systemen und Software (B)
  1. IT-Systeme und Software SOLLTEN regelmäßig aktualisiert werden.
  2. Grundsätzlich SOLLTEN Patches zeitnah nach Veröffentlichung eingespielt werden.
  3. Basierend auf dem Konzept für das Patch- und Änderungsmanagement MÜSSEN Patches zeitnah nach Veröffentlichung bewertet und entsprechend priorisiert werden.
  4. Für die Bewertung SOLLTE geprüft werden, ob es zu diesem Patch bekannte Schwachstellen gibt.
  5. Es MUSS entschieden werden, ob der Patch eingespielt werden soll.
  6. Wenn ein Patch eingespielt wird, SOLLTE kontrolliert werden, ob dieser auf allen relevanten Systemen zeitnah erfolgreich eingespielt wurde.
  7. Wenn ein Patch nicht eingespielt wird, MÜSSEN die Entscheidung und die Gründe dafür dokumentiert werden. **◀ ZITIERT**
  8. Falls Hardware- oder Software-Produkte eingesetzt werden sollen, die nicht mehr von den Herstellenden unterstützt werden oder für die kein Support mehr vorhanden ist, MUSS geprüft werden, ob diese dennoch sicher betrieben werden können.
  9. Ist dies nicht der Fall, DÜRFEN diese Hardware- oder Software-Produkte NICHT mehr verwendet werden.
- **Satz 7** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 7) UMS.5.2 verlangt die Dokumentation von Ausnahmegenehmigungen samt Begründung und deckt damit das geforderte Dokumentieren von Entscheidungen und Gründen beim Nicht-Einspielen von Patches allgemein ab.

### → OPS.1.1.4.A2 — Nutzung systemspezifischer Schutzmechanismen (B)
  1. Es MUSS geprüft werden, welche Schutzmechanismen die verwendeten IT-Systeme sowie die darauf genutzten Betriebssysteme und Anwendungen bieten.
  2. Diese Mechanismen MÜSSEN genutzt werden, sofern es keinen mindestens gleichwertigen Ersatz gibt oder gute Gründe dagegen sprechen.
  3. Werden sie nicht genutzt, MUSS dies begründet und dokumentiert werden. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) UMS.5.2 deckt als allgemeine Regelung zur Dokumentation von Ausnahmen samt Begründung die Forderung nach begründeter und dokumentierter Nicht-Nutzung von Schutzmechanismen vollständig ab.

### → ORP.5.A5 — Ausnahmegenehmigungen (S) [Vorgesetzte]
  1. Ist es in Einzelfällen erforderlich, von getroffenen Regelungen abzuweichen, SOLLTE die Ausnahme begründet und durch eine autorisierte Stelle nach einer Risikoabschätzung genehmigt werden.
  2. Es SOLLTE ein Genehmigungsverfahren für Ausnahmegenehmigungen geben.
  3. Es SOLLTE eine Übersicht über alle erteilten Ausnahmegenehmigungen erstellt und gepflegt werden. **◀ ZITIERT**
  4. Ein entsprechendes Verfahren für die Dokumentation und ein Überprüfungsprozess SOLLTE etabliert werden. **◀ ZITIERT**
  5. Alle Ausnahmegenehmigungen SOLLTEN befristet sein.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die Pflicht zur Dokumentation von Ausnahmegenehmigungen (z. B. in Verzeichnissen oder Systemen) deckt als allgemeinere Dokumentationsanforderung die Erstellung und Pflege einer Übersicht über erteilte Ausnahmen inhaltlich ab.
- **Satz 4** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 4) Satz 4 fordert die Etablierung eines Verfahrens zur Dokumentation von Ausnahmegenehmigungen, was der Forderung von UMS.5.2 entspricht.

### → SYS.1.1.A39 — Zentrale Verwaltung der Sicherheitsrichtlinien von Servern (S)
  1. Alle Einstellungen des Servers SOLLTEN durch Nutzung eines zentralen Managementsystems (siehe auch OPS.1.1.7 Systemmanagement) verwaltet und entsprechend dem ermittelten Schutzbedarf sowie auf den internen Richtlinien basierend konfiguriert sein.
  2. Technisch nicht umsetzbare Konfigurationsparameter SOLLTEN dokumentiert, begründet und mit dem Sicherheitsmanagement abgestimmt werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) UMS.5.2 fordert die Dokumentation von Ausnahmegenehmigungen mit Begründung und deckt damit das geforderte Dokumentieren und Begründen von Konfigurationsabweichungen inhaltlich ab.

### → SYS.1.2.2.A2 — Sichere Installation von Windows Server 2012 (B)
  1. Es DÜRFEN KEINE anderen als die benötigten Serverrollen und Features bzw. Funktionen installiert werden.
  2. Wenn es vom Funktionsumfang her ausreichend ist, MUSS die Server-Core-Variante installiert werden.
  3. Andernfalls MUSS begründet werden, warum die Server-Core-Variante nicht genügt. **◀ ZITIERT**
  4. Der Server MUSS bereits während der Installation auf einen aktuellen Patch-Stand gebracht werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die Pflicht zur Begründung bei Nichteinsatz der Server-Core-Variante stellt einen Spezialfall der allgemeinen Dokumentation von begründeten Ausnahmen gemäß UMS.5.2 dar.

### → SYS.1.2.3.A2 — Sichere Installation von Windows Server (B)
  1. Wenn vom Funktionsumfang her ausreichend, MUSS die Server-Core-Variante installiert werden.
  2. Andernfalls MUSS begründet werden, warum die Server-Core-Variante nicht genügt. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die G++-Maßnahme UMS.5.2 verlangt die Dokumentation von Ausnahmegenehmigungen inklusive Begründung und deckt damit die allgemeinere Pflicht zur Begründung des Abweichens von der Server-Core-Variante inhaltlich ab.

### → SYS.1.6.A17 — Ausführung von Containern ohne Privilegien (S)
  1. Die Container-Runtime und alle instanziierten Container SOLLTEN nur von einem nicht-privilegierten System-Account ausgeführt werden, der über keine erweiterten Rechte für den Container-Dienst und das Betriebssystem des Host-Systems verfügt oder diese Rechte erlangen kann.
  2. Die Container-Runtime SOLLTE durch zusätzliche Maßnahmen gekapselt werden, etwa durch Verwendung der Virtualisierungserweiterungen von CPUs.
  3. Sofern Container ausnahmsweise Aufgaben des Host-Systems übernehmen sollen, SOLLTEN die Privilegien auf dem Host-System auf das erforderliche Minimum begrenzt werden.
  4. Ausnahmen SOLLTEN angemessen dokumentiert werden. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) UMS.5.2 fordert explizit die Dokumentation von Ausnahmen und deckt damit die Anforderung aus Satz 4 vollständig auf allgemeiner Ebene ab.

### → SYS.2.2.3.A9 — Sichere zentrale Authentisierung in Windows-Netzen (S)
  1. Für die zentrale Authentisierung SOLLTE ausschließlich Kerberos eingesetzt werden.
  2. Eine Gruppenrichtlinie SOLLTE die Verwendung älterer Protokolle verhindern.
  3. Ist dies nicht möglich, MUSS alternativ NTLMv2 eingesetzt werden.
  4. Die Authentisierung mittels LAN-Manager und NTLMv1 DARF NICHT innerhalb der Institution und in einer produktiven Betriebsumgebung erlaubt werden.
  5. Die eingesetzten kryptografischen Mechanismen SOLLTEN entsprechend dem ermittelten Schutzbedarf und basierend auf den internen Richtlinien konfiguriert und dokumentiert werden.
  6. Abweichende Einstellungen SOLLTEN begründet und mit dem Sicherheitsmanagement abgestimmt sein. **◀ ZITIERT**
- **Satz 6** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 6) UMS.5.2 fordert explizit die Dokumentation von Ausnahmegenehmigungen inklusive Begründung und deckt damit die geforderte Begründung abweichender Einstellungen inhaltlich ab.

### → APP.4.3.A1 — Erstellung einer Sicherheitsrichtlinie für Datenbanksysteme (B)
  1. Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution MUSS eine spezifische Sicherheitsrichtlinie für Datenbanksysteme erstellt werden.
  2. Darin MÜSSEN nachvollziehbar Anforderungen und Vorgaben beschrieben sein, wie Datenbanksysteme sicher betrieben werden sollen.
  3. Die Richtlinie MUSS allen im Bereich Datenbanksysteme zuständigen Mitarbeitenden bekannt sein.
  4. Sie MUSS grundlegend für ihre Arbeit sein.
  5. Wird die Richtlinie verändert oder wird von den Anforderungen abgewichen, MUSS dies mit dem oder der ISB abgestimmt und dokumentiert werden. **◀ ZITIERT**
  6. Es MUSS regelmäßig überprüft werden, ob die Richtlinie noch korrekt umgesetzt ist.
  7. Die Ergebnisse MÜSSEN sinnvoll dokumentiert werden.
- **Satz 5** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) Die G++-Maßnahme UMS.5.2 deckt die geforderte Dokumentation von Abweichungen (Ausnahmen) von den Richtlinienanforderungen inhaltlich ab.

### → APP.4.3.A12 — Einheitlicher Konfigurationsstandard von Datenbankmanagementsystemen (S)
  1. Für alle eingesetzten Datenbankmanagementsysteme SOLLTE ein einheitlicher Konfigurationsstandard definiert werden.
  2. Alle Datenbankmanagementsysteme SOLLTEN nach diesem Standard konfiguriert und einheitlich betrieben werden.
  3. Falls es bei einer Installation notwendig ist, vom Konfigurationsstandard abzuweichen, SOLLTEN alle Schritte von dem oder der ISB freigegeben und nachvollziehbar dokumentiert werden. **◀ ZITIERT**
  4. Der Konfigurationsstandard SOLLTE regelmäßig überprüft und, falls erforderlich, angepasst werden.
- **Satz 3** | Relation GS++→ED23: `intersects-with` | Fundrichtung: beide
  Begründung: (Teilanforderung 3) UMS.5.2 fordert die Dokumentation von Ausnahmegenehmigungen und deckt damit die im Satz geforderte nachvollziehbare Dokumentation von Abweichungen ab.

### → APP.6.A5 — Sichere Installation von Software (B)
  1. Software MUSS entsprechend der Regelung für die Installation auf den IT-Systemen installiert werden.
  2. Dabei MÜSSEN ausschließlich unveränderte Versionen der freigegebenen Software verwendet werden.
  3. Wird von diesen Anweisungen abgewichen, MUSS dies durch Vorgesetzte und den IT-Betrieb genehmigt werden und entsprechend dokumentiert werden. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die G++-Maßnahme UMS.5.2 deckt die in Satz 3 geforderte Dokumentation von Ausnahmegenehmigungen bei Abweichungen direkt und allgemein ab.

### → CON.1.A10 — Erstellung eines Kryptokonzepts (S)
  1. Ausgehend von dem allgemeinen Sicherheitskonzept der Institution SOLLTE ein Kryptokonzept für Hard- oder Software mit kryptografischen Funktionen erstellt werden.
  2. Im Kryptokonzept SOLLTE beschrieben werden, wie die Datensicherungen von kryptografischen Schlüsseln durchgeführt werden, wie das Schlüsselmanagement von kryptografischen Schlüsseln ausgestaltet ist sowie wie das Krypto-Kastaster erhoben wird.
  3. Weiterhin SOLLTE im Kryptokonzept beschrieben werden, wie sichergestellt wird, dass kryptografische Funktionen von Hard- oder Software sicher konfiguriert und korrekt eingesetzt werden.
  4. Im Kryptokonzept SOLLTEN alle technischen Vorgaben für Hard- und Software mit kryptografischen Funktionen beschrieben werden (z. B. Anforderungen, Konfiguration oder Parameter).
  5. Um geeignete kryptografische Verfahren auszuwählen, SOLLTE die BSI TR 02102 berücksichtigt werden.
  6. Wird das Kryptokonzept verändert oder von ihm abgewichen, SOLLTE dies mit dem oder der ISB abgestimmt und dokumentiert werden. **◀ ZITIERT**
  7. Das Kryptokonzept SOLLTE allen bekannt sein, die kryptografische Verfahren einsetzen.
  8. Außerdem SOLLTE es bindend für ihre Arbeit sein.
  9. Insbesondere der IT-Betrieb SOLLTE die kryptografischen Vorgaben des Kryptokonzepts umsetzen.
- **Satz 6** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 6) UMS.5.2 fordert die Dokumentation von Ausnahmegenehmigungen mit Begründung und deckt damit die allgemeine Pflicht zur Dokumentation von Abweichungen vom Kryptokonzept inhaltlich ab.

### → DER.1.A1 — Erstellung einer Sicherheitsrichtlinie für die Detektion von sicherheitsrelevanten Ereignissen (B)
  1. Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution MUSS eine spezifische Sicherheitsrichtlinie für die Detektion von sicherheitsrelevanten Ereignissen erstellt werden.
  2. In der spezifischen Sicherheitsrichtlinie MÜSSEN nachvollziehbar Anforderungen und Vorgaben beschrieben werden, wie die Detektion von sicherheitsrelevanten Ereignissen geplant, aufgebaut und sicher betrieben werden kann.
  3. Die spezifische Sicherheitsrichtlinie MUSS allen im Bereich Detektion zuständigen Mitarbeitenden bekannt und grundlegend für ihre Arbeit sein.
  4. Falls die spezifische Sicherheitsrichtlinie verändert wird oder von den Anforderungen abgewichen wird, dann MUSS dies mit dem oder der verantwortlichen ISB abgestimmt und dokumentiert werden. **◀ ZITIERT**
  5. Es MUSS regelmäßig überprüft werden, ob die spezifische Sicherheitsrichtlinie noch korrekt umgesetzt ist.
  6. Die Ergebnisse der Überprüfung MÜSSEN sinnvoll dokumentiert werden.
- **Satz 4** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) UMS.5.2 deckt die Forderung nach der Dokumentation von Ausnahmen und Abweichungen von den Vorgaben der Sicherheitsrichtlinie direkt ab.

### → NET.1.1.A1 — Sicherheitsrichtlinie für das Netz (B) [IT-Betrieb]
  1. Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution MUSS eine spezifische Sicherheitsrichtlinie für das Netz erstellt werden.
  2. Darin MÜSSEN nachvollziehbar Anforderungen und Vorgaben beschrieben werden, wie Netze sicher konzipiert und aufgebaut werden.
  3. In der Richtlinie MUSS unter anderem festgelegt werden, in welchen Fällen die Zonen zu segmentieren sind und in welchen Fällen Benutzendengruppen bzw. Mandanten und Mandantinnen logisch oder sogar physisch zu trennen sind, welche Kommunikationsbeziehungen und welche Netz- und Anwendungsprotokolle jeweils zugelassen werden, wie der Datenverkehr für Administration und Überwachung netztechnisch zu trennen ist, welche institutionsinterne, standortübergreifende Kommunikation (WAN, Funknetze) erlaubt und welche Verschlüsselung im WAN, LAN oder auf Funkstrecken erforderlich ist sowie welche institutionsübergreifende Kommunikation zugelassen ist.
  4. Die Richtlinie MUSS allen im Bereich Netzdesign zuständigen Mitarbeitenden bekannt sein.
  5. Sie MUSS zudem grundlegend für ihre Arbeit sein.
  6. Wird die Richtlinie verändert oder wird von den Anforderungen abgewichen, MUSS dies dokumentiert und mit dem oder der verantwortlichen ISB abgestimmt werden. **◀ ZITIERT**
  7. Es MUSS regelmäßig überprüft werden, ob die Richtlinie noch korrekt umgesetzt ist.
  8. Die Ergebnisse MÜSSEN sinnvoll dokumentiert werden.
- **Satz 6** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 6) UMS.5.2 fordert explizit die Dokumentation von Ausnahmegenehmigungen und deckt damit die geforderte Dokumentationspflicht bei Abweichungen von den Richtlinienanforderungen ab.

### → NET.3.1.A10 — Erstellung einer Sicherheitsrichtlinie (S)
  1. Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution SOLLTE eine spezifische Sicherheitsrichtlinie erstellt werden.
  2. In der Sicherheitsrichtlinie SOLLTEN nachvollziehbar Anforderungen und Vorgaben beschrieben sein, wie Router und Switches sicher betrieben werden können.
  3. Die Richtlinie SOLLTE allen Administrierenden bekannt und grundlegend für ihre Arbeit sein.
  4. Wird die Richtlinie verändert oder wird von den festgelegten Anforderungen abgewichen, SOLLTE das mit dem oder der ISB abgestimmt und dokumentiert werden. **◀ ZITIERT**
  5. Es SOLLTE regelmäßig überprüft werden, ob die Richtlinie noch korrekt umgesetzt ist.
  6. Die Ergebnisse SOLLTEN geeignet dokumentiert werden.
- **Satz 4** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) UMS.5.2 fordert die Dokumentation von Ausnahmegenehmigungen und deckt damit die im Satz geforderte Dokumentation von Abweichungen materiell ab.

### → NET.3.2.A1 — Erstellung einer Sicherheitsrichtlinie (B)
  1. Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution MUSS eine spezifische Sicherheitsrichtlinie erstellt werden.
  2. In dieser MÜSSEN nachvollziehbar Anforderungen und Vorgaben beschrieben sein, wie Firewalls sicher betrieben werden können.
  3. Die Richtlinie MUSS allen im Bereich Firewalls zuständigen Mitarbeitenden bekannt und grundlegend für ihre Arbeit sein.
  4. Wird die Richtlinie verändert oder wird von den Anforderungen abgewichen, MUSS dies mit dem oder der ISB abgestimmt und dokumentiert werden. **◀ ZITIERT**
  5. Es MUSS regelmäßig überprüft werden, ob die Richtlinie noch korrekt umgesetzt ist.
  6. Die Ergebnisse MÜSSEN sinnvoll dokumentiert werden.
- **Satz 4** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) UMS.5.2 fordert die Dokumentation von Ausnahmegenehmigungen und deckt damit die geforderte Dokumentation bei Abweichungen von Richtlinienanforderungen ab.

### → OPS.1.1.5.A1 — Erstellung einer Sicherheitsrichtlinie für die Protokollierung (B) [Fachverantwortliche]
  1. Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution MUSS eine spezifische Sicherheitsrichtlinie für die Protokollierung erstellt werden.
  2. In dieser Sicherheitsrichtlinie MÜSSEN nachvollziehbar Anforderungen und Vorgaben beschrieben sein, wie die Protokollierung zu planen, aufzubauen und sicher zu betreiben ist.
  3. In der spezifischen Sicherheitsrichtlinie MUSS geregelt werden, wie, wo und was zu protokollieren ist.
  4. Dabei SOLLTEN sich Art und Umfang der Protokollierung am Schutzbedarf der Informationen orientieren.
  5. Die spezifische Sicherheitsrichtlinie MUSS von dem oder der ISB gemeinsam mit den Fachverantwortlichen erstellt werden.
  6. Sie MUSS allen für die Protokollierung zuständigen Mitarbeitenden bekannt und grundlegend für ihre Arbeit sein.
  7. Wird die spezifische Sicherheitsrichtlinie verändert oder wird von den Anforderungen abgewichen, MUSS dies mit dem oder der ISB abgestimmt und dokumentiert werden. **◀ ZITIERT**
  8. Es MUSS regelmäßig überprüft werden, ob die spezifische Sicherheitsrichtlinie noch korrekt umgesetzt ist.
  9. Die Ergebnisse der Überprüfung MÜSSEN dokumentiert werden.
- **Satz 7** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 7) Die G++-Maßnahme fordert die Dokumentation von Ausnahmegenehmigungen und deckt damit die geforderte Dokumentation von Abweichungen aus Satz 7 allgemein ab.

### → SYS.1.8.A6 — Erstellung einer Sicherheitsrichtlinie für Speicherlösungen (S)
  1. Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution SOLLTE eine spezifische Sicherheitsrichtlinie für Speicherlösungen erstellt werden.
  2. Darin SOLLTEN nachvollziehbar Vorgaben beschrieben sein, wie Speicherlösungen sicher geplant, administriert, installiert, konfiguriert und betrieben werden können.
  3. Die Richtlinie SOLLTE allen für Speicherlösungen zuständigen Administrierenden bekannt und grundlegend für ihre Arbeit sein.
  4. Wird die Richtlinie verändert oder wird von den Vorgaben abgewichen, SOLLTE dies mit dem oder der ISB abgestimmt und dokumentiert werden. **◀ ZITIERT**
  5. Es SOLLTE regelmäßig überprüft werden, ob die Richtlinie noch korrekt umgesetzt ist.
  6. Gegebenenfalls SOLLTE sie aktualisiert werden.
  7. Die Ergebnisse SOLLTEN sinnvoll dokumentiert werden.
- **Satz 4** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die G++-Maßnahme fordert die Dokumentation von Ausnahmegenehmigungen und deckt damit die geforderte Dokumentation bei Abweichungen von den Richtlinienvorgaben inhaltlich ab.


## UMS.6.1 — Nachverfolgung des Umsetzungsfortschritts  [4 Paare]

**Statement (normativ):** Umsetzung MUSS ein Verfahren für die Nachverfolgung der Umsetzung von Maßnahmen verankern.
**Klasse:** BSI-Methodik-Grundschutz-plus-plus | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Es wird empfohlen, dass der Prozess zur Fortschrittsverfolgung der Umsetzung von Anforderungen bzw. Sicherheitsmaßnahmen folgende Aspekte umfasst: Planung und Definition (Zielsetzung, KPI-Definition und detaillierte Umsetzungsplanung), Implementierung (Start der Umsetzung mit klarer Verantwortlichkeit und initialer Bestandsaufnahme), Überwachung (Regelmäßiges Status-Reporting, Soll-Ist-Vergleiche und KPI-Messungen), Bewertung und Anpassung (Ursachenanalyse, Korrekturmaßnahmen und regelmäßige Kommunikation an Stakeholder), Dokumentation und Lessons Learned (Abschlussdokumentation und kontinuierliche Verbesserung mittels PDCA-Zyklus). Eine strukturierte Vorgehensweise gewährleistet, dass Fortschritte transparent nachvollzogen werden, Abweichungen frühzeitig erkannt und der Sicherheitsstatus stetig verbessert werden kann.

### → DER.3.1.A25 — Nachbereitung eines Audits (S)
  1. Die Institution SOLLTE die im Auditbericht oder bei einer Revision festgestellten Abweichungen oder Mängel in einer angemessenen Zeit abstellen.
  2. Die durchzuführenden Korrekturmaßnahmen inklusive Zeitpunkt und Zuständigkeiten SOLLTEN dokumentiert werden.
  3. Auch abgeschlossene Korrekturmaßnahmen SOLLTEN dokumentiert werden. **◀ ZITIERT**
  4. Die Institution SOLLTE dazu ein definiertes Verfahren etablieren und einsetzen.
  5. Gab es schwerwiegende Abweichungen oder Mängel, SOLLTE das Audit- bzw. Revisionsteam überprüfen, ob die Korrekturmaßnahmen durchgeführt wurden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) UMS.6.1 fordert ein Verfahren zur Nachverfolgung von Maßnahmenumsetzungen, welches die Dokumentation und den Abschluss (Abschlussdokumentation) von Maßnahmen explizit mit abdeckt.

### → DER.3.2.A22 — Nachbereitung einer IS-Revision (S)
  1. Die im IS-Revisionsbericht festgestellten Abweichungen SOLLTEN in einer angemessenen Zeit durch die Institution korrigiert werden.
  2. Die durchzuführenden Korrekturmaßnahmen SOLLTEN mit Zuständigkeiten, Umsetzungstermin und dem jeweiligen Status dokumentiert sein.
  3. Die Umsetzung SOLLTE kontinuierlich nachverfolgt und der Umsetzungsstatus fortgeschrieben werden. **◀ ZITIERT**
  4. Grundsätzlich SOLLTE geprüft werden, ob ergänzende IS-Revisionen notwendig sind.
  5. Die Institution SOLLTE die Grob- und Detailplanung zur IS-Revision anpassen.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 3) Die G++-Maßnahme UMS.6.1 fordert die Verankerung eines Verfahrens zur Nachverfolgung der Maßnahmenumsetzung und deckt damit die kontinuierliche Nachverfolgung der Umsetzung inhaltlich ab.

### → DER.4.A14 — Regelmäßige Überprüfung und Verbesserung der Notfallmaßnahmen (H) [Institutionsleitung]
  1. Alle Notfallmaßnahmen SOLLTEN regelmäßig oder bei größeren Änderungen daraufhin überprüft werden, ob sie noch eingehalten und korrekt umgesetzt werden.
  2. Es SOLLTE geprüft werden, ob sie sich noch dazu eignen, die definierten Ziele zu erreichen.
  3. Dabei SOLLTE untersucht werden, ob technische Maßnahmen korrekt implementiert und konfiguriert wurden und ob organisatorische Maßnahmen effektiv und effizient umgesetzt sind.
  4. Bei Abweichungen SOLLTEN die Ursachen für die Mängel ermittelt und Verbesserungsmaßnahmen veranlasst werden.
  5. Diese Ergebnisübersicht SOLLTE von der Institutionsleitung freigegeben werden.
  6. Es SOLLTE zudem ein Prozess etabliert werden, der steuert und überwacht, ob und wie die Verbesserungsmaßnahmen umgesetzt werden. **◀ ZITIERT**
  7. Verzögerungen SOLLTEN frühzeitig an die Institutionsleitung gemeldet werden.
  8. Es SOLLTE von der Institutionsleitung festgelegt sein, wie die Überprüfungen koordiniert werden.
  9. Die Überprüfungen SOLLTEN so geplant werden, dass kein relevanter Teil ausgelassen wird.
  10. Insbesondere SOLLTEN die im Bereich der Revision, der IT, des Sicherheitsmanagements, des Informationssicherheitsmanagements und des Notfallmanagements durchgeführten Überprüfungen miteinander koordiniert werden.
  11. Dazu SOLLTE geregelt werden, welche Maßnahmen wann und von wem überprüft werden.
- **Satz 6** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 6) Die G++-Maßnahme UMS.6.1 fordert die Verankerung eines Verfahrens zur Nachverfolgung der Umsetzung von Maßnahmen, was den geforderten Steuerungs- und Überwachungsprozess für Verbesserungsmaßnahmen inhaltlich abdeckt.

### → ISMS.1.A10 — Erstellung eines Sicherheitskonzepts (S)
  1. Für den festgelegten Geltungsbereich (Informationsverbund) SOLLTE ein angemessenes Sicherheitskonzept als das zentrale Dokument im Sicherheitsprozess erstellt werden.
  2. Es SOLLTE entschieden werden, ob das Sicherheitskonzept aus einem oder aus mehreren Teilkonzepten bestehen soll, die sukzessive erstellt werden, um zunächst in ausgewählten Bereichen das erforderliche Sicherheitsniveau herzustellen.
  3. Im Sicherheitskonzept MÜSSEN aus den Sicherheitszielen der Institution, dem identifizierten Schutzbedarf und der Risikobewertung konkrete Sicherheitsmaßnahmen passend zum betrachteten Informationsverbund abgeleitet werden.
  4. Sicherheitsprozess und Sicherheitskonzept MÜSSEN die individuell geltenden Vorschriften und Regelungen berücksichtigen.
  5. Die im Sicherheitskonzept vorgesehenen Maßnahmen MÜSSEN zeitnah in die Praxis umgesetzt werden.
  6. Dies MUSS geplant und die Umsetzung MUSS kontrolliert werden. **◀ ZITIERT**
- **Satz 6** | Relation GS++→ED23: `intersects-with` | Fundrichtung: beide
  Begründung: (Teilanforderung 6) UMS.6.1 deckt die Kontrolle und Nachverfolgung der Maßnahmenumsetzung durch ein entsprechendes Verfahren zur Fortschrittsverfolgung inhaltlich direkt ab.


## UMS.5.1 — Autorisierung von Ausnahmen  [16 Paare]

**Statement (normativ):** Umsetzung MUSS Ausnahmegenehmigungen für Verpflichtungen durch {{ insert: param, ums.5.1-prm1 }} autorisieren.
**Klasse:** BSI-Methodik-Grundschutz-plus-plus | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Bei Zielkonflikten zwischen Verpflichtungen müssen diese gegeneinander abgewogen und falls erforderlich Ausnahmegenehmigungen von der zuständigen Person oder Rolle eingeholt werden. Zur Entscheidungsfindung kann eine Risikobetrachtung vorgenommen werden. Es ist zu prüfen ob die Nicht-Umsetzung von Anforderungen zur Erforderlichkeit einer Risikobetrachtung führt, siehe verwandte Anforderung.

### → APP.4.3.A1 — Erstellung einer Sicherheitsrichtlinie für Datenbanksysteme (B)
  1. Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution MUSS eine spezifische Sicherheitsrichtlinie für Datenbanksysteme erstellt werden.
  2. Darin MÜSSEN nachvollziehbar Anforderungen und Vorgaben beschrieben sein, wie Datenbanksysteme sicher betrieben werden sollen.
  3. Die Richtlinie MUSS allen im Bereich Datenbanksysteme zuständigen Mitarbeitenden bekannt sein.
  4. Sie MUSS grundlegend für ihre Arbeit sein.
  5. Wird die Richtlinie verändert oder wird von den Anforderungen abgewichen, MUSS dies mit dem oder der ISB abgestimmt und dokumentiert werden. **◀ ZITIERT**
  6. Es MUSS regelmäßig überprüft werden, ob die Richtlinie noch korrekt umgesetzt ist.
  7. Die Ergebnisse MÜSSEN sinnvoll dokumentiert werden.
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) Die Maßnahme UMS.5.1 fordert die Autorisierung von Ausnahmen für Verpflichtungen durch eine zuständige Rolle, was die geforderte Abstimmung von Abweichungen mit dem ISB inhaltlich abdeckt.

### → APP.4.3.A12 — Einheitlicher Konfigurationsstandard von Datenbankmanagementsystemen (S)
  1. Für alle eingesetzten Datenbankmanagementsysteme SOLLTE ein einheitlicher Konfigurationsstandard definiert werden.
  2. Alle Datenbankmanagementsysteme SOLLTEN nach diesem Standard konfiguriert und einheitlich betrieben werden.
  3. Falls es bei einer Installation notwendig ist, vom Konfigurationsstandard abzuweichen, SOLLTEN alle Schritte von dem oder der ISB freigegeben und nachvollziehbar dokumentiert werden. **◀ ZITIERT**
  4. Der Konfigurationsstandard SOLLTE regelmäßig überprüft und, falls erforderlich, angepasst werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die Maßnahme UMS.5.1 deckt die im Satz geforderte Freigabe von Abweichungen (Ausnahmen) durch eine zuständige Rolle autorisierend ab.

### → APP.6.A5 — Sichere Installation von Software (B)
  1. Software MUSS entsprechend der Regelung für die Installation auf den IT-Systemen installiert werden.
  2. Dabei MÜSSEN ausschließlich unveränderte Versionen der freigegebenen Software verwendet werden.
  3. Wird von diesen Anweisungen abgewichen, MUSS dies durch Vorgesetzte und den IT-Betrieb genehmigt werden und entsprechend dokumentiert werden. **◀ ZITIERT**
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) UMS.5.1 fordert die Autorisierung von Ausnahmegenehmigungen durch zuständige Stellen und deckt damit die Genehmigungspflicht bei Abweichungen aus Satz 3 materiell ab.

### → CON.11.1.A1 — Einhaltung der Grundsätze zur VS-Verarbeitung mit IT nach § 3, 4 und 6 und Nr. 1 Anlage V zur VSA (B)
  1. VS des Geheimhaltungsgrades VS-NfD DÜRFEN NUR mit VS-IT verarbeitet, die hierfür freigegeben ist.
  2. Private IT DARF NICHT für die Verarbeitung von Verschlusssachen eingesetzt werden.
  3. Bei der Verarbeitung von VS mit VS-IT MUSS der Grundsatz "Kenntnis nur, wenn nötig" eingehalten werden.
  4. Es DÜRFEN NUR Personen Kenntnis von einer VS erhalten, die auf Grund ihrer Aufgabenerfüllung von ihr Kenntnis erhalten müssen.
  5. Personen DÜRFEN NICHT umfassender oder eher über eine VS unterrichtet werden, als dies aus Gründen der Aufgabenerfüllung notwendig ist.
  6. Die Einhaltung des Grundsatzes „Kenntnis nur, wenn nötig“ SOLLTE, insbesondere falls die VS-IT durch mehrere Benutzende verwendet wird, primär über technische Maßnahmen sichergestellt werden.
  7. Nach dem Grundsatz der mehrschichtigen Sicherheit MÜSSEN personelle, organisatorische, materielle und technische Maßnahmen getroffen werden, die in ihrem Zusammenwirken Risiken eines Angriffs reduzieren (Prävention), Angriffe erkennbar machen (Detektion) und im Falle eines erfolgreichen Angriffs die negativen Folgen begrenzen (Reaktion).
  8. Bei der Erfüllung der Anforderungen des vorliegenden Bausteins MÜSSEN die relevanten Technischen Leitlinien des BSI (BSI TL) beachtet werden.
  9. Falls von den BSI TL abgewichen werden soll, dann DARF dies NUR in Ausnahmefällen und im Einvernehmen mit dem BSI erfolgen. **◀ ZITIERT**
- **Satz 9** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 9) UMS.5.1 deckt als allgemeine Anforderung zur Autorisierung von Ausnahmegenehmigungen bei Verpflichtungen die spezifische Genehmigungspflicht für Abweichungen von den BSI TL im Einvernehmen mit der zuständigen Stelle inhaltlich ab.

### → IND.3.2.A3 — Regelmäßige Prüfungen sowie Ausnahmegenehmigungen bestehender OT-Fernwartungszugänge (B) [IT-Betrieb]
  1. Sämtliche Anlagen MÜSSEN regelmäßig geprüft werden, ob alle ihre Fernwartungszugänge dem Soll-Zustand, d. h. dem aktuellen Fernwartungskonzept für die OT, entsprechen.
  2. Für notwendige Abweichungen vom Konzept MUSS innerhalb der OT ein Genehmigungsprozess etabliert werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 2) Die G++-Maßnahme UMS.5.1 fordert die Autorisierung von Ausnahmegenehmigungen durch zuständige Personen/Rollen und deckt damit die Etablierung eines Genehmigungsprozesses für Abweichungen allgemein ab.

### → NET.1.1.A1 — Sicherheitsrichtlinie für das Netz (B) [IT-Betrieb]
  1. Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution MUSS eine spezifische Sicherheitsrichtlinie für das Netz erstellt werden.
  2. Darin MÜSSEN nachvollziehbar Anforderungen und Vorgaben beschrieben werden, wie Netze sicher konzipiert und aufgebaut werden.
  3. In der Richtlinie MUSS unter anderem festgelegt werden, in welchen Fällen die Zonen zu segmentieren sind und in welchen Fällen Benutzendengruppen bzw. Mandanten und Mandantinnen logisch oder sogar physisch zu trennen sind, welche Kommunikationsbeziehungen und welche Netz- und Anwendungsprotokolle jeweils zugelassen werden, wie der Datenverkehr für Administration und Überwachung netztechnisch zu trennen ist, welche institutionsinterne, standortübergreifende Kommunikation (WAN, Funknetze) erlaubt und welche Verschlüsselung im WAN, LAN oder auf Funkstrecken erforderlich ist sowie welche institutionsübergreifende Kommunikation zugelassen ist.
  4. Die Richtlinie MUSS allen im Bereich Netzdesign zuständigen Mitarbeitenden bekannt sein.
  5. Sie MUSS zudem grundlegend für ihre Arbeit sein.
  6. Wird die Richtlinie verändert oder wird von den Anforderungen abgewichen, MUSS dies dokumentiert und mit dem oder der verantwortlichen ISB abgestimmt werden. **◀ ZITIERT**
  7. Es MUSS regelmäßig überprüft werden, ob die Richtlinie noch korrekt umgesetzt ist.
  8. Die Ergebnisse MÜSSEN sinnvoll dokumentiert werden.
- **Satz 6** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 6) Die Maßnahme UMS.5.1 deckt die im Satz geforderte Autorisierung bzw. Abstimmung von Abweichungen durch eine zuständige Rolle (ISB) inhaltlich ab.

### → NET.3.1.A10 — Erstellung einer Sicherheitsrichtlinie (S)
  1. Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution SOLLTE eine spezifische Sicherheitsrichtlinie erstellt werden.
  2. In der Sicherheitsrichtlinie SOLLTEN nachvollziehbar Anforderungen und Vorgaben beschrieben sein, wie Router und Switches sicher betrieben werden können.
  3. Die Richtlinie SOLLTE allen Administrierenden bekannt und grundlegend für ihre Arbeit sein.
  4. Wird die Richtlinie verändert oder wird von den festgelegten Anforderungen abgewichen, SOLLTE das mit dem oder der ISB abgestimmt und dokumentiert werden. **◀ ZITIERT**
  5. Es SOLLTE regelmäßig überprüft werden, ob die Richtlinie noch korrekt umgesetzt ist.
  6. Die Ergebnisse SOLLTEN geeignet dokumentiert werden.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) UMS.5.1 fordert die Autorisierung von Ausnahmegenehmigungen durch zuständige Rollen und deckt damit die geforderte Abstimmung von Abweichungen mit der zuständigen Stelle (ISB) inhaltlich ab.

### → NET.3.2.A1 — Erstellung einer Sicherheitsrichtlinie (B)
  1. Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution MUSS eine spezifische Sicherheitsrichtlinie erstellt werden.
  2. In dieser MÜSSEN nachvollziehbar Anforderungen und Vorgaben beschrieben sein, wie Firewalls sicher betrieben werden können.
  3. Die Richtlinie MUSS allen im Bereich Firewalls zuständigen Mitarbeitenden bekannt und grundlegend für ihre Arbeit sein.
  4. Wird die Richtlinie verändert oder wird von den Anforderungen abgewichen, MUSS dies mit dem oder der ISB abgestimmt und dokumentiert werden. **◀ ZITIERT**
  5. Es MUSS regelmäßig überprüft werden, ob die Richtlinie noch korrekt umgesetzt ist.
  6. Die Ergebnisse MÜSSEN sinnvoll dokumentiert werden.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) UMS.5.1 fordert die Autorisierung von Ausnahmegenehmigungen durch eine zuständige Rolle und deckt damit die Abstimmung von Anforderungsabweichungen mit dem ISB ab.

### → NET.3.4.A27 — Prüfung der Notwendigkeit für MAC-Adress-Authentisierung (H)
  1. Eine Authentisierung über MAC-Adressen SOLLTE nur dort genutzt werden, wo dies technisch unumgänglich ist und die Sicherheitsrichtlinien dies zulassen.
  2. Es SOLLTE im Vorfeld geprüft werden, ob solche Ausnahmefälle notwendig sind. **◀ ZITIERT**
  3. Ist dies der Fall, SOLLTEN die Ausnahmefälle auf den minimalen Einsatzbereich eingeschränkt werden.
  4. Die Begründung und das Ergebnis der Prüfung SOLLTEN dokumentiert werden.
  5. Sie SOLLTEN regelmäßig und bei Bedarf nochmals verifiziert werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die geforderte Vorabprüfung der Notwendigkeit einer Ausnahme wird durch den allgemeinen Prozess zur Autorisierung und Abwägung von Ausnahmegenehmigungen in UMS.5.1 abgedeckt.

### → OPS.1.1.5.A1 — Erstellung einer Sicherheitsrichtlinie für die Protokollierung (B) [Fachverantwortliche]
  1. Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution MUSS eine spezifische Sicherheitsrichtlinie für die Protokollierung erstellt werden.
  2. In dieser Sicherheitsrichtlinie MÜSSEN nachvollziehbar Anforderungen und Vorgaben beschrieben sein, wie die Protokollierung zu planen, aufzubauen und sicher zu betreiben ist.
  3. In der spezifischen Sicherheitsrichtlinie MUSS geregelt werden, wie, wo und was zu protokollieren ist.
  4. Dabei SOLLTEN sich Art und Umfang der Protokollierung am Schutzbedarf der Informationen orientieren.
  5. Die spezifische Sicherheitsrichtlinie MUSS von dem oder der ISB gemeinsam mit den Fachverantwortlichen erstellt werden.
  6. Sie MUSS allen für die Protokollierung zuständigen Mitarbeitenden bekannt und grundlegend für ihre Arbeit sein.
  7. Wird die spezifische Sicherheitsrichtlinie verändert oder wird von den Anforderungen abgewichen, MUSS dies mit dem oder der ISB abgestimmt und dokumentiert werden. **◀ ZITIERT**
  8. Es MUSS regelmäßig überprüft werden, ob die spezifische Sicherheitsrichtlinie noch korrekt umgesetzt ist.
  9. Die Ergebnisse der Überprüfung MÜSSEN dokumentiert werden.
- **Satz 7** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 7) UMS.5.1 deckt die im Satz geforderte Abstimmung und Autorisierung von Abweichungen von Richtlinienvorgaben durch eine zuständige Rolle generisch ab.

### → SYS.1.1.A39 — Zentrale Verwaltung der Sicherheitsrichtlinien von Servern (S)
  1. Alle Einstellungen des Servers SOLLTEN durch Nutzung eines zentralen Managementsystems (siehe auch OPS.1.1.7 Systemmanagement) verwaltet und entsprechend dem ermittelten Schutzbedarf sowie auf den internen Richtlinien basierend konfiguriert sein.
  2. Technisch nicht umsetzbare Konfigurationsparameter SOLLTEN dokumentiert, begründet und mit dem Sicherheitsmanagement abgestimmt werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) UMS.5.1 fordert die Autorisierung von Ausnahmegenehmigungen durch zuständige Rollen, was die geforderte Abstimmung von nicht umsetzbaren Konfigurationen mit dem Sicherheitsmanagement abdeckt.

### → SYS.1.8.A6 — Erstellung einer Sicherheitsrichtlinie für Speicherlösungen (S)
  1. Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution SOLLTE eine spezifische Sicherheitsrichtlinie für Speicherlösungen erstellt werden.
  2. Darin SOLLTEN nachvollziehbar Vorgaben beschrieben sein, wie Speicherlösungen sicher geplant, administriert, installiert, konfiguriert und betrieben werden können.
  3. Die Richtlinie SOLLTE allen für Speicherlösungen zuständigen Administrierenden bekannt und grundlegend für ihre Arbeit sein.
  4. Wird die Richtlinie verändert oder wird von den Vorgaben abgewichen, SOLLTE dies mit dem oder der ISB abgestimmt und dokumentiert werden. **◀ ZITIERT**
  5. Es SOLLTE regelmäßig überprüft werden, ob die Richtlinie noch korrekt umgesetzt ist.
  6. Gegebenenfalls SOLLTE sie aktualisiert werden.
  7. Die Ergebnisse SOLLTEN sinnvoll dokumentiert werden.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die Autorisierung von Ausnahmegenehmigungen durch eine zuständige Rolle gemäß UMS.5.1 deckt die geforderte Abstimmung von Abweichungen von den Richtlinienvorgaben mit dem ISB inhaltlich ab.

### → SYS.2.2.3.A9 — Sichere zentrale Authentisierung in Windows-Netzen (S)
  1. Für die zentrale Authentisierung SOLLTE ausschließlich Kerberos eingesetzt werden.
  2. Eine Gruppenrichtlinie SOLLTE die Verwendung älterer Protokolle verhindern.
  3. Ist dies nicht möglich, MUSS alternativ NTLMv2 eingesetzt werden.
  4. Die Authentisierung mittels LAN-Manager und NTLMv1 DARF NICHT innerhalb der Institution und in einer produktiven Betriebsumgebung erlaubt werden.
  5. Die eingesetzten kryptografischen Mechanismen SOLLTEN entsprechend dem ermittelten Schutzbedarf und basierend auf den internen Richtlinien konfiguriert und dokumentiert werden.
  6. Abweichende Einstellungen SOLLTEN begründet und mit dem Sicherheitsmanagement abgestimmt sein. **◀ ZITIERT**
- **Satz 6** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 6) UMS.5.1 deckt die im Satz geforderte Abstimmung und Autorisierung von abweichenden Einstellungen (Ausnahmen) durch eine zuständige Rolle wie das Sicherheitsmanagement generisch ab.

### → ORP.5.A5 — Ausnahmegenehmigungen (S) [Vorgesetzte]
  1. Ist es in Einzelfällen erforderlich, von getroffenen Regelungen abzuweichen, SOLLTE die Ausnahme begründet und durch eine autorisierte Stelle nach einer Risikoabschätzung genehmigt werden. **◀ ZITIERT**
  2. Es SOLLTE ein Genehmigungsverfahren für Ausnahmegenehmigungen geben. **◀ ZITIERT**
  3. Es SOLLTE eine Übersicht über alle erteilten Ausnahmegenehmigungen erstellt und gepflegt werden.
  4. Ein entsprechendes Verfahren für die Dokumentation und ein Überprüfungsprozess SOLLTE etabliert werden.
  5. Alle Ausnahmegenehmigungen SOLLTEN befristet sein.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) UMS.5.1 deckt die Autorisierung von Ausnahmegenehmigungen durch eine zuständige Person oder Rolle sowie die damit verbundene Risikobetrachtung direkt ab.
- **Satz 2** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die Maßnahme UMS.5.1 fordert die Autorisierung von Ausnahmegenehmigungen durch zuständige Rollen und deckt damit das geforderte Genehmigungsverfahren inhaltlich ab.

### → DER.1.A1 — Erstellung einer Sicherheitsrichtlinie für die Detektion von sicherheitsrelevanten Ereignissen (B)
  1. Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution MUSS eine spezifische Sicherheitsrichtlinie für die Detektion von sicherheitsrelevanten Ereignissen erstellt werden.
  2. In der spezifischen Sicherheitsrichtlinie MÜSSEN nachvollziehbar Anforderungen und Vorgaben beschrieben werden, wie die Detektion von sicherheitsrelevanten Ereignissen geplant, aufgebaut und sicher betrieben werden kann.
  3. Die spezifische Sicherheitsrichtlinie MUSS allen im Bereich Detektion zuständigen Mitarbeitenden bekannt und grundlegend für ihre Arbeit sein.
  4. Falls die spezifische Sicherheitsrichtlinie verändert wird oder von den Anforderungen abgewichen wird, dann MUSS dies mit dem oder der verantwortlichen ISB abgestimmt und dokumentiert werden. **◀ ZITIERT**
  5. Es MUSS regelmäßig überprüft werden, ob die spezifische Sicherheitsrichtlinie noch korrekt umgesetzt ist.
  6. Die Ergebnisse der Überprüfung MÜSSEN sinnvoll dokumentiert werden.
- **Satz 4** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) UMS.5.1 fordert die Autorisierung von Ausnahmegenehmigungen durch eine zuständige Rolle und deckt damit die geforderte Abstimmung von Abweichungen mit der verantwortlichen Stelle inhaltlich ab.


## UMS.1.2 — Bewertung des Restrisikos  [3 Paare]

**Statement (normativ):** Umsetzung SOLLTE das bestehende Restrisiko durch die nicht umgesetzten Anforderungen festlegen.
**Klasse:** BSI-Methodik-Grundschutz-plus-plus | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Die Risiken der Nichtumsetzung von Anforderungen können auch konsolidiert werden, um diese für die Institutionsleitung nachvollziehbarer zu machen.

### → ORP.5.A5 — Ausnahmegenehmigungen (S) [Vorgesetzte]
  1. Ist es in Einzelfällen erforderlich, von getroffenen Regelungen abzuweichen, SOLLTE die Ausnahme begründet und durch eine autorisierte Stelle nach einer Risikoabschätzung genehmigt werden. **◀ ZITIERT**
  2. Es SOLLTE ein Genehmigungsverfahren für Ausnahmegenehmigungen geben.
  3. Es SOLLTE eine Übersicht über alle erteilten Ausnahmegenehmigungen erstellt und gepflegt werden.
  4. Ein entsprechendes Verfahren für die Dokumentation und ein Überprüfungsprozess SOLLTE etabliert werden.
  5. Alle Ausnahmegenehmigungen SOLLTEN befristet sein.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 1) Satz 1 fordert vor der Genehmigung von Abweichungen von Regelungen eine Risikoabschätzung, was der Bewertung des Restrisikos bei nicht umgesetzten Anforderungen entspricht.

### → DER.3.2.A19 — Überprüfung der gewählten Risikobehandlungsoptionen (S) [IS-Revisionsteam]
  1. Das IS-Revisionsteam SOLLTE prüfen, ob die verbleibenden Restrisiken für den Informationsverbund angemessen und tragbar sind und ob sie verbindlich durch die Institutionsleitung getragen werden. **◀ ZITIERT**
  2. Das IS-Revisionsteam SOLLTE stichprobenartig verifizieren, ob bzw. inwieweit die gewählten Risikobehandlungsoptionen umgesetzt sind.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 1) Satz 1 befasst sich mit der Prüfung und Beurteilung der Tragbarkeit von verbleibenden Restrisiken, was sich inhaltlich direkt mit der Bewertung des Restrisikos überschneidet.

### → ISMS.1.A12 — Management-Berichte zur Informationssicherheit (S) [Institutionsleitung]
  1. Die Institutionsleitung SOLLTE sich regelmäßig über den Stand der Informationssicherheit informieren, insbesondere über die aktuelle Gefährdungslage sowie die Wirksamkeit und Effizienz des Sicherheitsprozesses.
  2. Dazu SOLLTEN Management-Berichte geschrieben werden, welche die wesentlichen relevanten Informationen über den Sicherheitsprozess enthalten, insbesondere über Probleme, Erfolge und Verbesserungsmöglichkeiten.
  3. Die Management-Berichte SOLLTEN klar priorisierte Maßnahmenvorschläge enthalten.
  4. Die Maßnahmenvorschläge SOLLTEN mit realistischen Abschätzungen zum erwarteten Umsetzungsaufwand versehen sein.
  5. Die Management-Berichte SOLLTEN revisionssicher archiviert werden.
  6. Die Management-Entscheidungen über erforderliche Aktionen, den Umgang mit Restrisiken und mit Veränderungen von sicherheitsrelevanten Prozessen SOLLTEN dokumentiert sein. **◀ ZITIERT**
  7. Die Management-Entscheidungen SOLLTEN revisionssicher archiviert werden.
- **Satz 6** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 6) Satz 6 fordert die Dokumentation von Management-Entscheidungen über den Umgang mit Restrisiken, was sich inhaltlich mit der Festlegung und Bewertung des Restrisikos für die Institutionsleitung überschneidet.

