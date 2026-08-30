# Review-Dossier Praktik TEST

Praktik TEST: 34 Controls mit Mapping, 220 Paare gesamt. Gesampelt: 5 Controls (max/min/median Paarzahl + 2 zufällig).

## TEST.1.1.2 — Zuweisung der Aufgaben  [4 Paare]

**Statement (normativ):** Änderungen und Tests MUSS die mit den Verfahren und Regelungen verbundenen Aufgaben {{ insert: param, test.1.1.2-prm1 }} zuweisen.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Die Zuweisung von Aufgaben bezeichnet die eindeutige und verbindliche Übertragung von konkreten Tätigkeiten und Verantwortlichkeiten des Änderungsprozesses, wie etwa die Risikobewertung, die technische Umsetzung oder die finale Freigabe, an definierte Stellen in der Institution. Der Sinn dieser Vorschrift ist es, die Verantwortlichkeit ("Accountability") für jeden einzelnen Schritt im Prozess klarzustellen. Ohne eine solche Zuweisung könnten kritische Prüfungen unterbleiben, weil sich niemand explizit zuständig fühlt, was wiederum die Wahrscheinlichkeit fehlgeschlagener Änderungen erhöht. Eine klare Regelung kann sicherstellen, dass keine Aufgaben übersehen werden und jede Tätigkeit von einer dafür qualifizierten und befugten Stelle ausgeführt wird, was die Prozesssicherheit signifikant erhöht. Eine bewährte Methode zur Umsetzung ist die Erstellung einer RACI-Matrix (Responsible, Accountable, Consulted, Informed), die tabellarisch für jeden Prozessschritt darstellt, wer für die Durchführung verantwortlich ist, wer die Gesamtverantwortung trägt, wer zu konsultieren und wer zu informieren ist. Diese Zuständigkeiten können auch direkt in einem Workflow- oder Ticketsystem abgebildet werden, sodass Aufgaben, wie beispielsweise Genehmigungsschritte, automatisch an die richtige Gruppe oder Person weitergeleitet werden. Sinnvoll ist es die Zuweisung anhand von Rollen (z.B. "Anwendungsverantwortlicher", "Netzwerkadministrator", "Change Manager") vorzunehmen, statt an konkrete Personen. Dieser Ansatz stellt sicher, dass die Prozesse auch bei Personalwechseln stabil weiterlaufen, da die Zuständigkeit an die Funktion und nicht an das Individuum gebunden ist.

### → INF.11.A2 — Wartung, Inspektion und Updates (B) [Fachverantwortliche, IT-Betrieb]
  1. Die Fahrzeuge und die dazugehörenden IT-Komponenten MÜSSEN nach den Vorgaben des herstellenden Unternehmens gewartet werden.
  2. Hierbei MUSS beachtet werden, dass die Intervalle der herkömmlichen Wartung und von Updates der integrierten IT-Komponenten voneinander abweichen können.
  3. Es MUSS klar geregelt werden, wer in welcher Umgebung die Updates installieren darf. **◀ ZITIERT**
  4. Auch „Over-the-Air“ (OTA) Updates MÜSSEN geregelt eingespielt werden.
  5. Wartungs- und Reparaturarbeiten MÜSSEN von befugtem und qualifiziertem Personal in einer sicheren Umgebung durchgeführt werden.
  6. Dabei SOLLTE schon vor der Wartung geklärt werden, wie mit Fremdfirmen umgegangen wird.
  7. Werden Fahrzeuge in fremden Institutionen gewartet, SOLLTE geprüft werden, ob alle nicht benötigten, zum Fahrzeug dazugehörigen portablen IT-Systeme entfernt werden.
  8. Werden die Fahrzeuge wieder in den Einsatzbetrieb integriert, MUSS mittels Checkliste geprüft werden, ob alle Beanstandungen und Mängel auch behoben wurden.
  9. Es MUSS auch geprüft werden, ob die vorhandenen IT-Komponenten einsatzfähig sind.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die Maßnahme TEST.1.1.2 fordert die Zuweisung von Aufgaben und Verantwortlichkeiten bei Änderungen an zuständige Rollen und deckt damit die Regelung ab, wer Updates durchführen darf.

### → SYS.3.3.A6 — Updates von Mobiltelefonen (S) [Benutzende]
  1. Es SOLLTE regelmäßig geprüft werden, ob es Softwareupdates für die Mobiltelefone gibt.
  2. Der Umgang mit Updates SOLLTE geregelt werden.
  3. Wenn es neue Softwareupdates gibt, SOLLTE festgelegt werden, wie die Benutzenden darüber informiert werden.
  4. Es SOLLTE festgelegt werden, ob die Benutzenden die Updates selber installieren dürfen, oder ob die Mobiltelefone an einer zentralen Stelle hierfür abgegeben werden sollen. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die Zuweisung von Aufgaben und Durchführungsverantwortlichkeiten an bestimmte Rollen (z. B. Benutzende vs. zentrale Stelle) deckt die geforderte Festlegung zur Update-Installation ab.

### → OPS.1.1.3.A2 — Festlegung der Zuständigkeiten (B)
  1. Für alle Organisationsbereiche MÜSSEN Zuständige für das Patch- und Änderungsmanagement festgelegt werden. **◀ ZITIERT**
  2. Die definierten Zuständigkeiten MÜSSEN sich auch im Berechtigungskonzept widerspiegeln.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) Die Maßnahme fordert explizit die Zuweisung der Aufgaben und Verantwortlichkeiten im Änderungsmanagement an zuständige Personen oder Rollen und deckt damit die Forderung des Satzes inhaltlich ab.

### → APP.6.A4 — Regelung für die Installation und Konfiguration von Software (B) [Fachverantwortliche]
  1. Die Installation und Konfiguration der Software MUSS durch den IT-Betrieb so geregelt werden, dass die Software nur mit dem geringsten notwendigen Funktionsumfang installiert und ausgeführt wird, die Software mit den geringsten möglichen Berechtigungen ausgeführt wird, die datensparsamsten Einstellungen (in Bezug auf die Verarbeitung von personenbezogenen Daten) konfiguriert werden sowie alle relevanten Sicherheitsupdates und -patches installiert sind, bevor die Software produktiv eingesetzt wird.
  2. Hierbei MÜSSEN auch abhängige Komponenten (unter anderem Laufzeitumgebungen, Bibliotheken, Schnittstellen sowie weitere Programme) mitbetrachtet werden.
  3. Der IT-Betrieb MUSS in Abstimmung mit den Fachverantwortlichen festlegen, wer die Software wie installieren darf. **◀ ZITIERT**
  4. Idealerweise SOLLTE Software immer zentral durch den IT-Betrieb installiert werden.
  5. Ist es erforderlich, dass die Software (teilweise) manuell installiert wird, dann MUSS der IT-Betrieb eine Installationsanweisung erstellen, in der klar geregelt wird, welche Zwischenschritte zur Installation durchzuführen und welche Konfigurationen vorzunehmen sind.
  6. Darüber hinaus MUSS der IT-Betrieb regeln, wie die Integrität der Installationsdateien überprüft wird.
  7. Falls zu einem Installationspaket digitale Signaturen oder Prüfsummen verfügbar sind, MÜSSEN mit diesen die Integrität überprüft werden.
  8. Sofern erforderlich, SOLLTE der IT-Betrieb eine sichere Standardkonfiguration der Software festlegen, mit der die Software konfiguriert wird.
  9. Die Standardkonfiguration SOLLTE dokumentiert werden.
- **Satz 3** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die Zuweisung von Aufgaben und Verantwortlichkeiten an zuständige Rollen oder Personen in TEST.1.1.2 deckt die Festlegung, wer die Software installieren darf, auf allgemeiner Ebene ab.


## TEST.3.1 — Sicherheitstest  [29 Paare]

**Statement (normativ):** Änderungen und Tests SOLLTE vor wesentlichen Änderungen die Einhaltung der Sicherheitsanforderungen testen.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Änderungen sind wesentlich, wenn sie die Informationssicherheit von Produktivsystemen und -anwendungen betreffen und über eine geringe Anzahl von Nutzenden hinaus Auswirkungen haben können. Dabei sind sowohl die Sicherheitsanforderungen relevant, die direkt durch IT-Produkte umgesetzt werden (technische Anforderungen), als auch die prozessualen Anforderungen, die von der Änderung betroffen sind, etwa zur Überwachung von Ereignissen oder zur Sensibilisierung des Personals. Die Sicherheitsanforderungen ergeben sich aus den für das jeweilige Zielobjekt geltenden Vorgaben aus allen Praktiken. Sowohl die Funktionalität einzelner Module als auch das Zusammenspiel von Schnittstellen ist wichtig, um Sicherheitslücken frühzeitig zu erkennen.

### → APP.1.1.A11 — Geregelter Einsatz von Erweiterungen für Office-Produkte (S)
  1. Alle Erweiterungen von Office-Produkten, wie Add-ons und Extensions, SOLLTEN vor dem produktiven Einsatz genauso getestet werden wie neue Versionen. **◀ ZITIERT**
  2. Hierbei SOLLTE ausschließlich auf isolierten Testsystemen getestet werden.
  3. Die Tests SOLLTEN prüfen, ob Erweiterungen negative Auswirkungen auf die Office-Produkte und die laufenden IT-Systeme haben.
  4. Die Tests der eingesetzten Erweiterungen SOLLTEN einem definierten Testplan folgen.
  5. Dieser Testplan SOLLTE so gestaltet sein, dass Dritte das Vorgehen nachvollziehen können.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) TEST.3.1 deckt die Forderung ab, da sie als allgemeinere Maßnahme verlangt, Änderungen wie neue Versionen und Erweiterungen vor dem produktiven Einsatz auf Einhaltung der Sicherheitsanforderungen zu testen.

### → APP.1.4.A8 — Verhinderung von Datenabfluss (B)
  1. Um zu verhindern, dass Apps ungewollt vertrauliche Daten versenden oder aus den gesendeten Daten Profile über die Benutzenden erstellt werden, MUSS die App-Kommunikation geeignet eingeschränkt werden.
  2. Dazu SOLLTE die Kommunikation im Rahmen des Test- und Freigabeverfahrens analysiert werden. **◀ ZITIERT**
  3. Weiterhin SOLLTE überprüft werden, ob eine App ungewollte Protokollierungs- oder Hilfsdateien schreibt, die möglicherweise vertrauliche Informationen enthalten.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) TEST.3.1 verlangt allgemein Sicherheitstests vor Freigaben und Änderungen zur Einhaltung von Sicherheitsanforderungen, was die Sicherheitsanalyse der Kommunikation im Test- und Freigabeverfahren als Testfall umfasst.

### → APP.2.3.A10 — Sichere Aktualisierung von OpenLDAP (S)
  1. Bei Updates SOLLTE darauf geachtet werden, ob die Änderungen eingesetzte Backends oder Overlays sowie Softwareabhängigkeiten betreffen.
  2. Beim Update auf neue Releases SOLLTE geprüft werden, ob die verwendeten Overlays und Backends in der neuen Version weiterhin zur Verfügung stehen.
  3. Ist dies nicht der Fall, SOLLTEN geeignete Migrationspfade ausgewählt werden.
  4. Setzen Administrierende eigene Skripte ein, SOLLTEN sie daraufhin überprüft werden, ob sie mit der aktualisierten Version von OpenLDAP problemlos zusammenarbeiten. **◀ ZITIERT**
  5. Die Konfiguration und die Zugriffsrechte SOLLTEN nach einer Aktualisierung sorgfältig geprüft werden.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) TEST.3.1 fordert allgemeine Sicherheitstests und das Prüfen von Schnittstellen vor Änderungen, was die Kompatibilitätsprüfung eigener Skripte nach Updates abdeckt.

### → APP.5.2.A9 — Sichere Konfiguration von Exchange-Servern (S)
  1. Der IT-Betrieb SOLLTE Exchange-Server entsprechend der Vorgaben aus der Sicherheitsrichtlinie installieren und konfigurieren.
  2. Konnektoren SOLLTEN sicher konfiguriert werden.
  3. Der IT-Betrieb SOLLTE die Protokollierung des Exchange-Systems aktivieren.
  4. Für vorhandene benutzendenspezifische Anpassungen SOLLTE ein entsprechendes Konzept erstellt werden.
  5. Bei der Verwendung von funktionalen Erweiterungen SOLLTE sichergestellt sein, dass die definierten Anforderungen an die Schutzziele Vertraulichkeit, Integrität und Verfügbarkeit weiterhin erfüllt sind. **◀ ZITIERT**
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) TEST.3.1 fordert allgemeingültig die Prüfung der Einhaltung von Sicherheitsanforderungen bei Änderungen, was die Sicherstellung der Schutzziele beim Einsatz funktionaler Erweiterungen abdeckt.

### → APP.5.4.A3 — Initiales und regelmäßiges Testen der UCC-Dienste (B)
  1. Für die UCC-Dienste MÜSSEN initial Tests durchgeführt werden, die verifizieren, dass die UCC-Komponenten untereinander und mit anderen UCC-Diensten interferenzfrei funktionieren.
  2. Ebenfalls MÜSSEN Tests mit ausgewählten Benutzenden durchgeführt werden, um insbesondere Wechselwirkungen mit anderen Anwendungen zu überprüfen.
  3. Diese Tests SOLLTEN wiederholt werden, wenn die UCC-Dienste erweitert oder verändert werden. **◀ ZITIERT**
  4. Zusätzlich SOLLTE die Konfiguration der UCC-Dienste in regelmäßigen Abständen auf Plausibilität und Konformität für die festgelegten Einsatzzwecke überprüft werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 3) Satz 3 fordert die Wiederholung von Tests bei Erweiterung oder Veränderung von UCC-Diensten, was der Forderung nach Sicherheitstests bei Änderungen entspricht.

### → CON.1.A11 — Test von Hardware mit kryptografischen Funktionen (H) [IT-Betrieb]
  1. Im Kryptokonzept SOLLTEN Testverfahren für Hardware mit kryptografischen Funktionen festgelegt werden.
  2. Bevor Hardware mit kryptografischen Funktionen eingesetzt wird, sollte getestet werden, ob die kryptografischen Funktionen korrekt funktionieren.
  3. Wenn ein IT-System geändert wird, SOLLTE getestet werden, ob die eingesetzte kryptografische Hardware noch ordnungsgemäß funktioniert. **◀ ZITIERT**
  4. Die Konfiguration der kryptografischen Hardware SOLLTE regelmäßig überprüft werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) TEST.3.1 verlangt als allgemeinere Maßnahme das Testen der Einhaltung von Sicherheitsanforderungen bei Änderungen und deckt damit funktionale Sicherheitstests bei Systemänderungen ab.

### → CON.8.A5 — Sicheres Systemdesign (B)
  1. Folgende Grundregeln des sicheren Systemdesigns MÜSSEN in der zu entwickelnden Software berücksichtigt werden: Grundsätzlich MÜSSEN alle Eingabedaten vor der Weiterverarbeitung geprüft und validiert werden.
  2. Bei Client-Server-Anwendungen MÜSSEN die Daten grundsätzlich auf dem Server validiert werden.
  3. Die Standardeinstellungen der Software MÜSSEN derart voreingestellt sein, dass ein sicherer Betrieb der Software ermöglicht wird.
  4. Bei Fehlern oder Ausfällen von Komponenten des Systems DÜRFEN NICHT schützenswerte Informationen preisgegeben werden.
  5. Die Software MUSS mit möglichst geringen Privilegien ausgeführt werden können.
  6. Schützenswerte Daten MÜSSEN entsprechend der Vorgaben des Kryptokonzepts verschlüsselt übertragen und gespeichert werden.
  7. Zur Benutzenden-Authentisierung und Authentifizierung MÜSSEN vertrauenswürdige Mechanismen verwendet werden, die den Sicherheitsanforderungen an die Anwendung entsprechen.
  8. Falls zur Authentifizierung Passwörter gespeichert werden, MÜSSEN diese mit einem sicheren Hashverfahren gespeichert werden.
  9. Sicherheitsrelevante Ereignisse MÜSSEN in der Art protokolliert werden, dass sie im Nachgang ausgewertet werden können.
  10. Informationen, die für den Produktivbetrieb nicht relevant sind (z. B. Kommentare mit Zugangsdaten für die Entwicklungsumgebung), SOLLTEN in ausgeliefertem Programmcode und ausgelieferten Konfigurationsdateien entfernt werden.
  11. Das Systemdesign MUSS dokumentiert werden.
  12. Es MUSS überprüft werden, ob alle Sicherheitsanforderungen an das Systemdesign erfüllt wurden. **◀ ZITIERT**
- **Satz 12** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 12) TEST.3.1 verlangt das Testen der Einhaltung von Sicherheitsanforderungen und deckt damit die Überprüfung der Erfüllung von Sicherheitsanforderungen inhaltlich ab.

### → INF.13.A12 — Sichere Konfiguration der TGM-Systeme (S)
  1. Alle Systeme des TGM sowie die Systeme, die durch das TGM betrieben werden, SOLLTEN sicher konfiguriert werden.
  2. Die Konfiguration SOLLTE mindestens vor Inbetriebnahme eines Systems getestet werden. **◀ ZITIERT**
  3. Konfigurationsänderungen während des Produktivbetriebs SOLLTEN vor Aktivierung auf einer Testinstanz getestet oder nur im Vier-Augen-Prinzip durchgeführt werden.
  4. Die Konfiguration von Systemen SOLLTE gesichert werden, um ein schnelles Wiedereinspielen einer fehlerfreien Version zu ermöglichen (Rollback).
  5. Rollback-Tests SOLLTEN auf einem Testsystem eingerichtet oder während Wartungsfenstern durchgeführt werden.
  6. Die Konfigurationen SOLLTEN zentral gespeichert werden.
  7. Für gleichartige Systeme, inklusive der Geräte der Automations- und Feldebene (siehe Kapitel 4.1 Genutzte TGM-spezifische Fachbegriffe), SOLLTE eine automatisierte Verteilung von Software-Updates und Konfigurationen eingerichtet werden.
  8. Konfigurationsänderungen SOLLTEN allen Beteiligten an Betriebs- und Serviceprozessen (Entstörung, Rufbereitschaft, Wartungen etc.) bekannt gemacht werden, insbesondere Änderungen der Zugangsmechanismen oder der Passwörter sowie Änderungen an Kommunikations- und Steuerparametern für die eingebundenen Systeme.
  9. Es SOLLTE sichergestellt werden, dass im Störungsfall beispielsweise eine Wartungstechnikerin oder ein Wartungstechniker das System bedienen bzw. parametrieren kann.
  10. Außerdem SOLLTE regelmäßig und zusätzlich bei Bedarf geprüft werden, ob die Systeme gemäß den Vorgaben konfiguriert sind.
  11. Die Ergebnisse SOLLTEN nachvollziehbar dokumentiert werden.
  12. Abweichungen von den Vorgaben SOLLTEN behoben werden.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) TEST.3.1 fordert Sicherheitstests vor wesentlichen Änderungen (einschließlich Inbetriebnahme), was das vorherige Testen der Konfiguration auf Einhaltung der Sicherheitsanforderungen allgemein abdeckt.

### → INF.14.A3 — Sichere Anbindung von TGA-Anlagen und GA-Systemen (B)
  1. Für alle TGA-Anlagen, GA-Systeme und GA-relevanten Komponenten MUSS festgelegt werden, ob durch andere TGA-Anlagen, GA-Systeme oder GA-relevante Komponenten Aktionen ausgelöst werden dürfen.
  2. Falls eine solche Integration zulässig ist, SOLLTE reglementiert werden, welche automatisierten Aktionen durch welche Informationen eines GA-Systems ausgelöst werden dürfen.
  3. Falls eine TGA-Anlage nicht in ein GA-System integriert werden kann oder darf, diese jedoch an ein GA-System gekoppelt werden soll, MUSS festgelegt werden, welche Informationen der TGA-Anlage an das GA-System gemeldet werden.
  4. Sowohl die Integration von TGA-Anlagen in ein GA-System als auch die rückwirkungsfreie Kopplung von TGA-Anlagen an GA-Systeme MÜSSEN angemessen abgesichert sein.
  5. Ebenfalls MUSS die Anbindung von GA-Systemen untereinander angemessen abgesichert werden.
  6. Hierzu MÜSSEN insbesondere die Ablauf- und Funktionsketten innerhalb eines GA-Systems bzw. zwischen GA-Systemen angemessen geplant werden.
  7. Hierbei MÜSSEN alle Übergänge zwischen Gewerken und Techniken berücksichtigt werden.
  8. Diese Ablauf- und Funktionsketten MÜSSEN umfassend getestet und bei Fehlverhalten nachjustiert werden. **◀ ZITIERT**
  9. Die Festlegungen MÜSSEN vollumfänglich dokumentiert werden.
  10. Sowohl regelmäßig als auch ergänzend bei Bedarf SOLLTE geprüft werden, ob die Dokumentation noch aktuell ist.
  11. Bei Abweichungen MUSS die Ursache für die Abweichungen eruiert und behoben werden.
- **Satz 8** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 8) TEST.3.1 fordert das Testen von Sicherheitsanforderungen inklusive Schnittstellen und Modulfunktionen, was das Testen und Nachjustieren von Ablauf- und Funktionsketten allgemein abdeckt.

### → NET.1.1.A14 — Umsetzung der Netzplanung (B)
  1. Das geplante Netz MUSS fachgerecht umgesetzt werden.
  2. Dies MUSS während der Abnahme geprüft werden. **◀ ZITIERT**
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) TEST.3.1 fordert das Testen der Einhaltung von Sicherheitsanforderungen vor wesentlichen Änderungen, was die Prüfung der fachgerechten Umsetzung im Rahmen einer Abnahme abdeckt.

### → NET.3.3.A3 — Sichere Installation von VPN-Endgeräten (B)
  1. Wird eine Appliance eingesetzt, die eine Wartung benötigt, MUSS es dafür einen gültigen Wartungsvertrag geben.
  2. Es MUSS sichergestellt werden, dass nur qualifiziertes Personal VPN-Komponenten installiert.
  3. Die Installation der VPN-Komponenten sowie eventuelle Abweichungen von den Planungsvorgaben SOLLTEN dokumentiert werden.
  4. Die Funktionalität und die gewählten Sicherheitsmechanismen des VPN MÜSSEN vor Inbetriebnahme geprüft werden. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) TEST.3.1 verlangt als allgemeine Maßnahme die Prüfung von Funktionalität und Sicherheitsanforderungen vor wesentlichen Änderungen bzw. Inbetriebnahmen und deckt damit die geforderte Vorabprüfung des VPNs inhaltlich ab.

### → NET.3.4.A3 — Erstellung eines Anforderungskatalogs für NAC (S)
  1. Die Anforderungen an die NAC-Lösung SOLLTEN in einem Anforderungskatalog erhoben werden.
  2. Der Anforderungskatalog SOLLTE dabei die grundlegenden funktionalen Anforderungen umfassen und alle NAC-Komponenten (z. B. Endgeräte, Access-Switches und RADIUS-Server) adressieren.
  3. Der Anforderungskatalog SOLLTE mit allen betroffenen Fachabteilungen, den zuständigen Gremien und den Richtlinien der Institution abgestimmt werden.
  4. Der Anforderungskatalog SOLLTE regelmäßig und bei Bedarf aktualisiert werden.
  5. Wenn NAC-Komponenten beschafft werden, SOLLTEN zugehörige Anforderungen berücksichtigt werden.
  6. Die NAC-Lösung SOLLTE auf Basis des Anforderungskatalogs getestet werden. **◀ ZITIERT**
- **Satz 6** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 6) TEST.3.1 fordert allgemeingültig das Testen der Einhaltung von Sicherheitsanforderungen vor wesentlichen Änderungen, was das anforderungsbasierte Testen einer NAC-Lösung inhaltlich abdeckt.

### → NET.4.2.A3 — Sichere Administration und Konfiguration von VoIP-Endgeräten (B)
  1. Nicht benötigte Funktionen der Endgeräte MÜSSEN deaktiviert werden.
  2. Die Konfigurationseinstellungen DÜRFEN NICHT unberechtigt geändert werden.
  3. Alle Sicherheitsfunktionen der Endgeräte SOLLTEN vor dem produktiven Einsatz getestet werden. **◀ ZITIERT**
  4. Die eingesetzten Sicherheitsmechanismen und die verwendeten Parameter SOLLTEN dokumentiert werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) TEST.3.1 verlangt allgemein das Testen der Einhaltung von Sicherheitsanforderungen vor wesentlichen Änderungen und Produktiveinsätzen, was das Testen der Sicherheitsfunktionen von Endgeräten vor dem produktiven Einsatz abdeckt.

### → NET.4.3.A3 — Sicherer Betrieb eines Faxservers (B) [IT-Betrieb]
  1. Bevor ein Faxserver in Betrieb genommen wird, SOLLTE eine Testphase erfolgen. **◀ ZITIERT**
  2. Konfigurationsparameter sowie alle Änderungen an der Konfiguration eines Faxservers SOLLTEN dokumentiert werden.
  3. Die Archivierung und Löschung von Faxdaten SOLLTEN geregelt sein.
  4. Außerdem MUSS regelmäßig die Verbindung vom Faxserver zur TK-Anlage beziehungsweise zum öffentlichen Telefonnetz auf ihre Funktion geprüft werden.
  5. Es MUSS außerdem sichergestellt werden, dass der Faxserver ausschließlich Fax-Dienste anbietet und nicht für weitere Dienste genutzt wird.
  6. Alle nicht benötigten Leistungsmerkmale und Zugänge der eingesetzten Kommunikationsschnittstellen MÜSSEN deaktiviert werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) TEST.3.1 fordert allgemeingültig das Durchführen von Sicherheitstests vor wesentlichen Änderungen bzw. Inbetriebnahmen und deckt damit die geforderte Testphase vor Inbetriebnahme eines Faxservers ab.

### → OPS.1.1.6.A12 — Durchführung von Regressionstests (S) [Testende]
  1. Wenn Software verändert wurde, SOLLTEN Regressionstests durchgeführt werden. **◀ ZITIERT**
  2. Hierbei SOLLTE überprüft werden, ob bisherige bestehende Sicherheitsmechanismen und -einstellungen durch das Update ungewollt verändert wurden. **◀ ZITIERT**
  3. Regressionstests SOLLTEN vollständig durchgeführt werden und hierbei auch Erweiterungen sowie Hilfsmittel umfassen.
  4. Werden Testfälle ausgelassen, SOLLTE dies begründet und dokumentiert werden.
  5. Die durchgeführten Testfälle und die Testergebnisse SOLLTEN dokumentiert werden.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) TEST.3.1 fordert das Testen der Sicherheitsanforderungen vor wesentlichen Änderungen, was das Durchführen von Regressionstests bei veränderter Software auf allgemeiner Ebene abdeckt.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Das Testen der Einhaltung von Sicherheitsanforderungen vor Änderungen nach TEST.3.1 deckt die Überprüfung ab, ob bestehende Sicherheitsmechanismen und -einstellungen durch ein Update ungewollt beeinträchtigt wurden.

### → OPS.1.1.6.A15 — Überprüfung der Installation und zugehörigen Dokumentation (S) [Testende]
  1. Die Installation der Software SOLLTE entsprechend der Regelungen zur Installation und Konfiguration von Software (siehe Baustein APP.6 Allgemeine Software) überprüft werden. **◀ ZITIERT**
  2. Falls vorhanden, SOLLTE zusätzlich die Installations- und Konfigurationsdokumentation geprüft werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) TEST.3.1 fordert allgemeingültig das Testen der Einhaltung von Sicherheitsanforderungen vor wesentlichen Änderungen, was die Überprüfung einer Softwareinstallation anhand von Konfigurations- und Installationsvorgaben einschließt.

### → OPS.1.2.2.A16 — Regelmäßige Erneuerung technischer Archivsystem-Komponenten (S) [IT-Betrieb]
  1. Archivsysteme SOLLTEN über lange Zeiträume auf dem aktuellen technischen Stand gehalten werden.
  2. Neue Hard- und Software SOLLTE vor der Installation in einem laufenden Archivsystem ausführlich getestet werden. **◀ ZITIERT**
  3. Wenn neue Komponenten in Betrieb genommen oder neue Dateiformate eingeführt werden, SOLLTE ein Migrationskonzept erstellt werden.
  4. Darin SOLLTEN alle Änderungen, Tests und erwarteten Testergebnisse beschrieben sein.
  5. Die Konvertierung der einzelnen Daten SOLLTE dokumentiert werden (Transfervermerk).
  6. Wenn Archivdaten in neue Formate konvertiert werden, SOLLTE geprüft werden, ob die Daten aufgrund rechtlicher Anforderungen zusätzlich in ihren ursprünglichen Formaten zu archivieren sind.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) G++ TEST.3.1 fordert allgemein das Testen vor wesentlichen Änderungen, was das Testen neuer Hard- und Software vor der Installation im laufenden System als allgemeineres Prinzip abdeckt.

### → OPS.2.2.A10 — Sichere Migration zu einem Cloud-Dienst (S) [Fachverantwortliche]
  1. Die Migration zu einem Cloud-Dienst SOLLTE auf Basis des erstellten Migrationskonzeptes erfolgen.
  2. Während der Migration SOLLTE überprüft werden, ob das Sicherheitskonzept für die Cloud-Nutzung an potenzielle neue Anforderungen angepasst werden muss.
  3. Auch SOLLTEN alle Notfallvorsorgemaßnahmen vollständig und aktuell sein.
  4. Die Migration zu einem Cloud-Dienst SOLLTE zunächst in einem Testlauf überprüft werden. **◀ ZITIERT**
  5. Ist der Cloud-Dienst in den produktiven Betrieb übergegangen, SOLLTE abgeglichen werden, ob die Cloud-Diensteanbietenden die definierten Anforderungen der Institution erfüllen.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) TEST.3.1 fordert allgemeingültig, vor wesentlichen Änderungen wie einer Cloud-Migration entsprechende Tests zur Einhaltung der Anforderungen durchzuführen, was den geforderten Testlauf abdeckt.

### → SYS.1.5.A17 — Überwachung des Betriebszustands und der Konfiguration der virtuellen Infrastruktur (S)
  1. Der Betriebszustand der virtuellen Infrastruktur SOLLTE überwacht werden.
  2. Dabei SOLLTE unter anderem geprüft werden, ob noch ausreichend Ressourcen verfügbar sind.
  3. Es SOLLTE auch geprüft werden, ob es eventuell Konflikte bei gemeinsam genutzten Ressourcen eines Virtualisierungsservers gibt.
  4. Weiterhin SOLLTEN die Konfigurationsdateien der virtuellen IT-Systeme regelmäßig auf unautorisierte Änderungen überprüft werden.
  5. Wird die Konfiguration der Virtualisierungsinfrastruktur geändert, SOLLTEN die Änderungen geprüft und getestet werden, bevor sie umgesetzt werden. **◀ ZITIERT**
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) G++ TEST.3.1 deckt die Forderung nach Prüfung und Tests vor Umsetzung von Änderungen als übergeordnete Anforderung an Sicherheitstests vor wesentlichen Änderungen vollständig ab.

### → SYS.3.2.2.A20 — Regelmäßige Überprüfung des MDM (B)
  1. Sicherheitseinstellungen MÜSSEN regelmäßig überprüft werden.
  2. Bei neuen Betriebssystemversionen der mobilen Endgeräte MUSS vorab geprüft werden, ob das MDM diese vollständig unterstützt und die Konfigurationsprofile und Sicherheitseinstellungen weiterhin wirksam und ausreichend sind. **◀ ZITIERT**
  3. Abweichungen MÜSSEN korrigiert werden.
  4. Die zugeteilten Berechtigungen für Benutzende und Administrierende MÜSSEN regelmäßig daraufhin überprüft werden, ob sie weiterhin angemessen sind (Minimalprinzip).
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) TEST.3.1 fordert allgemein das Testen der Einhaltung von Sicherheitsanforderungen vor wesentlichen Änderungen, was die Vorabprüfung von Sicherheitseinstellungen und Profilen bei neuen Betriebssystemversionen umfasst.

### → OPS.1.1.3.A1 — Konzept für das Patch- und Änderungsmanagement (B) [Fachverantwortliche]
  1. Wenn IT-Komponenten, Software oder Konfigurationsdaten geändert werden, MUSS es dafür Vorgaben geben, die auch Sicherheitsaspekte berücksichtigen.
  2. Diese MÜSSEN in einem Konzept für das Patch- und Änderungsmanagement festgehalten und befolgt werden.
  3. Alle Patches und Änderungen MÜSSEN geeignet geplant, genehmigt und dokumentiert werden.
  4. Patches und Änderungen SOLLTEN vorab geeignet getestet werden (siehe hierzu auch OPS.1.1.6 Software-Tests und Freigaben). **◀ ZITIERT**
  5. Wenn Patches installiert und Änderungen durchgeführt werden, MÜSSEN Rückfall-Lösungen vorhanden sein.
  6. Bei größeren Änderungen MUSS zudem der oder die ISB beteiligt sein.
  7. Insgesamt MUSS sichergestellt werden, dass das angestrebte Sicherheitsniveau während und nach den Änderungen erhalten bleibt.
  8. Insbesondere SOLLTEN auch die gewünschten Sicherheitseinstellungen erhalten bleiben.
- **Satz 4** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 4) TEST.3.1 fordert explizit, vor wesentlichen Änderungen Tests zur Einhaltung der Sicherheitsanforderungen durchzuführen, was die Forderung nach Vorab-Tests von Änderungen und Patches abdeckt.

### → APP.3.4.A7 — Sichere Konfiguration von DNS unter Samba (S)
  1. Wenn Samba als DNS-Server eingesetzt wird, SOLLTE die Einführung sorgfältig geplant und die Umsetzung vorab getestet werden. **◀ ZITIERT**
  2. Da Samba verschiedene AD-Integrationsmodi unterstützt, SOLLTE der IT-Betrieb die DNS-Einstellungen entsprechend dem Verwendungsszenario von Samba vornehmen.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) TEST.3.1 fordert allgemeingültig das vorherige Testen von wesentlichen Änderungen bzw. Systemeinführungen und deckt damit die Forderung ab, die Umsetzung der Samba-DNS-Einführung vorab zu testen.

### → INF.13.A16 — Prozess für Änderungen im TGM (S)
  1. Änderungen SOLLTEN immer angekündigt und mit allen beteiligten Gewerken (siehe Kapitel 4.1 Genutzte TGM-spezifische Fachbegriffe), Nachfrage- und betreibenden Organisationen abgestimmt werden.
  2. Außerdem SOLLTEN Regelungen für den Fall getroffen werden, dass ein Rückbau von Änderungen mit fehlerhaftem Ergebnis nicht oder nur mit hohem Aufwand möglich ist.
  3. Daher sollten im Änderungsmanagement vor Ausführung der Änderung Tests durchgeführt werden, die auch die Fähigkeit des Rückbaus beinhalten.
  4. Für die verschiedenen Typen von Änderungen SOLLTE die jeweilige Testtiefe festgelegt werden.
  5. Bei der Einführung neuer Systeme und bei großen Änderungen an bestehenden Systemen SOLLTE eine entsprechend hohe Testtiefe vorgesehen werden (siehe INF.13.A22 Durchführung von Systemtests im TGM). **◀ ZITIERT**
- **Satz 5** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) TEST.3.1 verlangt explizit Sicherheitstests vor wesentlichen Änderungen und deckt damit die geforderte hohe Testtiefe bei großen Änderungen bzw. neuen Systemen inhaltlich ab.

### → INF.13.A22 — Durchführung von Systemtests im TGM (S) [Planende]
  1. Systeme des TGM und Systeme, die durch das TGM verwaltet werden, SOLLTEN vor der Inbetriebnahme und bei großen Systemänderungen hinsichtlich ihrer funktionalen und nicht-funktionalen Anforderungen getestet werden.
  2. Dabei SOLLTE auch das Soll- und Ist-Verhalten von Funktionen und Einstellungen geprüft werden.
  3. Bei den nicht-funktionalen Anforderungen SOLLTEN auch Anforderungen der Informationssicherheit getestet sowie zusätzlich bei Bedarf auch Lasttests durchgeführt werden. **◀ ZITIERT**
  4. Für die Tests SOLLTE eine Testspezifikation erstellt werden, die eine Beschreibung der Testumgebung, der Testtiefe und der Testfälle inklusive der Kriterien für eine erfolgreiche Testdurchführung enthält.
  5. Die Testdurchführung SOLLTE in einem Testbericht dokumentiert werden.
  6. Testspezifikationen SOLLTEN regelmäßig und zusätzlich bei Bedarf geprüft und gegebenenfalls aktualisiert werden, um dem aktuellen Stand der Technik zu entsprechen und auch neueste Erkenntnisse abdecken zu können.
- **Satz 3** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) TEST.3.1 fordert explizit das Testen der Einhaltung von Sicherheitsanforderungen vor wesentlichen Änderungen und deckt damit den Kern der geforderten Informationssicherheitstests aus Satz 3 ab.

### → OPS.1.1.1.A7 — Sicherstellung eines ordnungsgemäßen IT-Betriebs (S)
  1. Der IT-Betrieb SOLLTE für alle IT-Komponenten Betriebskonzepte entwickeln.
  2. Diese Betriebskonzepte SOLLTEN regelmäßig geprüft und angepasst werden.
  3. Die sicherheitsrelevanten Vorgaben zur Konfiguration SOLLTEN umgesetzt werden.
  4. Dafür SOLLTEN die gehärteten Standard-Konfigurationen genutzt werden.
  5. Der IT-Betrieb SOLLTE für alle Tätigkeiten Prüfkriterien festlegen, die in ihrer Gesamtheit als Leitfaden für den ordnungsgemäßen IT-Betrieb dienen.
  6. Die Freigabe von installierten oder geänderten IT-Komponenten in den produktiven Betrieb SOLLTE über diese Prüfkriterien nachgewiesen werden.
  7. Bei Inbetriebnahme und nach Updates oder Umstrukturierungen SOLLTEN Systemtests für die IT-Komponenten durchgeführt werden. **◀ ZITIERT**
  8. Der IT-Betrieb SOLLTE festlegen, in welcher Umgebung die jeweiligen Systemtests mit welcher Testabdeckung und Testtiefe durchgeführt werden.
  9. Der IT-Betrieb SOLLTE Vorkehrungen für die Ersatzbeschaffung von IT-Komponenten treffen.
  10. Hierfür SOLLTEN eine Reservevorhaltung oder Lieferverträge vorgesehen werden.
  11. Alle Tätigkeiten des IT-Betriebs SOLLTEN umfassend und nachvollziehbar erfasst werden.
  12. Hierfür SOLLTE der IT-Betrieb ein geeignetes Werkzeug wie ein Ticketsystem nutzen.
  13. Der IT-Betrieb SOLLTE insbesondere die Qualität der Betriebsprozesse, die Einhaltung von SLAs und die Zufriedenheit der Benutzenden systematisch erfassen.
  14. Es SOLLTEN regelmäßig Reports erstellt werden, die dem Nachweis eines ordnungsgemäßen IT-Betriebs dienen.
- **Satz 7** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 7) TEST.3.1 deckt die Forderung nach Tests bei Änderungen wie Updates oder Umstrukturierungen ab, indem Sicherheitstests vor wesentlichen Änderungen verbindlich vorgeschrieben werden.

### → OPS.1.1.6.A1 — Planung der Software-Tests (B)
  1. Die Rahmenbedingungen für Software-Tests MÜSSEN vor den Tests innerhalb der Institution entsprechend der Schutzbedarfe, Organisationseinheiten, technischen Möglichkeiten und Test-Umgebungen festlegt sein.
  2. Die Software MUSS auf Basis der Anforderungen des Anforderungskatalogs zu der Software getestet werden. **◀ ZITIERT**
  3. Liegt auch ein Pflichtenheft vor, dann MUSS dieses zusätzlich berücksichtigt werden.
  4. Die Testfälle MÜSSEN so ausgewählt werden, sodass diese möglichst repräsentativ alle Funktionen der Software überprüfen.
  5. Zusätzlich SOLLTEN auch Negativ-Tests berücksichtigt werden, die überprüfen, ob die Software keine ungewollten Funktionen enthält.
  6. Die Testumgebung MUSS so ausgewählt werden, sodass diese möglichst repräsentativ alle in der Institution eingesetzten Gerätemodelle und Betriebssystemumgebungen abdeckt.
  7. Es SOLLTE dabei getestet werden, ob die Software mit den eingesetzten Betriebssystemen in den vorliegenden Konfigurationen kompatibel und funktionsfähig ist.
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 2) Satz 2 fordert Software-Tests auf Basis des Anforderungskatalogs, was das Überprüfen der Einhaltung definierter Sicherheitsanforderungen als wesentliche Testaktivität einschließt.

### → OPS.1.1.6.A5 — Durchführung von Software-Tests für nicht funktionale Anforderungen (B) [Testende]
  1. Es MÜSSEN Software-Tests durchgeführt werden, die überprüfen, ob alle wesentlichen nichtfunktionalen Anforderungen erfüllt werden. **◀ ZITIERT**
  2. Insbesondere MÜSSEN sicherheitsspezifische Software-Tests durchgeführt werden, wenn die Anwendung sicherheitskritische Funktionen mitbringt. **◀ ZITIERT**
  3. Die durchgeführten Testfälle, sowie die Testergebnisse, MÜSSEN dokumentiert werden.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) Das Testen von Sicherheitsanforderungen gemäß TEST.3.1 deckt als wesentlicher Teilbereich die geforderte Prüfung nichtfunktionaler Anforderungen ab.
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) TEST.3.1 fordert Sicherheitstests zur Einhaltung von Sicherheitsanforderungen vor wesentlichen Änderungen und deckt damit sicherheitsspezifische Software-Tests für sicherheitskritische Funktionen inhaltlich ab.


## TEST.5.4 — Persistenz  [1 Paare]

**Statement (normativ):** Änderungen und Tests SOLLTE die Persistenz nach wesentlichen Änderungen testen.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Persistenz bedeutet hier, dass eine wesentliche Änderung nach ihrer Einführung dauerhaft wirksam bleibt, also auch nach einem Neustart, einem System-Update oder einem Rückspielen von Konfigurations-Backups nicht unbeabsichtigt verloren geht. Dies könnte beispielsweise dazu führen, dass eine sicherheitsrelevante Konfiguration nach einem Reboot verschwindet oder eine Migration zu einem neuen Anbieter scheitert, weil Daten oder Regeln nicht portabel waren. Eine Institution kann die Anforderung praktisch umsetzen, indem Änderungen nach Abschluss nicht nur funktional, sondern auch über System- und Lebenszyklusereignisse hinweg überprüft werden. Dazu kann es hilfreich sein, Änderungen gezielt mit simulierten Neustarts, Failover-Tests oder dem erneuten Einspielen von Standard-Backups zu validieren. Um den laufenden Betrieb hierdurch nicht zu beeinträchtigen können Systeme oder Anwendungsinstanzen nacheinander oder zu unkritischen Zeiten neu gestartet werden.

### → NET.3.1.A25 — Erweiterter Integritätsschutz für die Konfigurationsdateien (H)
  1. Stürzt ein Router oder Switch ab, SOLLTE sichergestellt werden, dass bei der Wiederherstellung bzw. beim Neustart keine alten oder fehlerhaften Konfigurationen (unter anderem ACLs) benutzt werden. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) TEST.5.4 fordert das Testen und Sicherstellen der Persistenz von Konfigurationen über Neustarts und Wiederherstellungen hinweg, wodurch das unbeabsichtigte Laden alter oder fehlerhafter Konfigurationsstände verhindert wird.


## TEST.2.2 — Folgenabschätzung  [6 Paare]

**Statement (normativ):** Änderungen und Tests für Administrierende SOLLTE zu einer strukturierten Folgenabschätzung vor wesentlichen Änderungen anweisen.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Sinnvoll ist es die Ausführlichkeit der Folgenabschätzung an Umfang und Reichweite der Änderungen, sowie dem Risikoprofil betroffener Assets zu orientieren: Empfehlenswert ist es die Änderungen je nach Abschätzung der Folgen in Klassen einzusortieren (z.B. Geringe Auswirkungen, Mittlere Auswirkungen, Hohe Auswirkungen) und die weitere Prüftiefe nach dieser Einstufung auszurichten.

### → APP.2.3.A10 — Sichere Aktualisierung von OpenLDAP (S)
  1. Bei Updates SOLLTE darauf geachtet werden, ob die Änderungen eingesetzte Backends oder Overlays sowie Softwareabhängigkeiten betreffen. **◀ ZITIERT**
  2. Beim Update auf neue Releases SOLLTE geprüft werden, ob die verwendeten Overlays und Backends in der neuen Version weiterhin zur Verfügung stehen. **◀ ZITIERT**
  3. Ist dies nicht der Fall, SOLLTEN geeignete Migrationspfade ausgewählt werden.
  4. Setzen Administrierende eigene Skripte ein, SOLLTEN sie daraufhin überprüft werden, ob sie mit der aktualisierten Version von OpenLDAP problemlos zusammenarbeiten.
  5. Die Konfiguration und die Zugriffsrechte SOLLTEN nach einer Aktualisierung sorgfältig geprüft werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die allgemeine Forderung nach einer strukturierten Folgenabschätzung vor Änderungen in TEST.2.2 deckt das Prüfen der Auswirkungen von Updates auf Komponenten und Abhängigkeiten inhaltlich ab.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die geforderte Prüfung der Verfügbarkeit von Overlays und Backends in der neuen Version stellt eine Ausprägung der allgemeinen strukturierten Folgenabschätzung vor wesentlichen Änderungen gemäß TEST.2.2 dar.

### → APP.5.2.A7 — Migration von Exchange-Systemen (S)
  1. Der IT-Betrieb SOLLTE alle Migrationsschritte gründlich planen und dokumentieren.
  2. Der IT-Betrieb SOLLTE dabei Postfächer, Objekte, Sicherheitsrichtlinien, Active-Directory-Konzepte sowie die Anbindung an andere E-Mail-Systeme berücksichtigen.
  3. Außerdem SOLLTE er Funktionsunterschiede zwischen verschiedenen Versionen von Exchange beachten. **◀ ZITIERT**
  4. Das neue Exchange-System SOLLTE, bevor es installiert wird, in einem separaten Testnetz geprüft werden.
- **Satz 3** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 3) Die Beachtung von Funktionsunterschieden bei Versionswechseln ist ein zentraler Aspekt der von TEST.2.2 geforderten strukturierten Folgenabschätzung vor wesentlichen Änderungen.

### → OPS.1.1.2.A24 — Prüfen von IT-Administrationstätigkeiten (S)
  1. Bevor eine IT-Administrationstätigkeit durchgeführt wird, SOLLTE geprüft werden, ob der Anlass und die Art der Tätigkeit im Kontext der zugrundeliegenden Aufgabe plausibel sind.
  2. Nachdem eine IT-Administrationstätigkeit an einer Komponente durchgeführt wurde, SOLLTE geprüft werden, ob die Konfiguration und der Status der Komponente dem gewünschten Zielzustand entspricht.
  3. Falls eine zusätzliche Qualitätssicherung der ausgeführten Administrationsaufgabe notwendig ist, SOLLTE diese nicht durch dieselbe Person durchgeführt werden, die die entsprechenden Tätigkeiten durchgeführt hat.
  4. Für IT-Administrationstätigkeiten mit potenziell weitreichenden Folgen SOLLTE geprüft werden, ob diese Tätigkeiten die Verfügbarkeit der IT-Administration selbst einschränken könnten. **◀ ZITIERT**
  5. In diesem Fall SOLLTEN entsprechende Vorkehrungen getroffen werden, um einen Rollback der IT-Administrationstätigkeiten zu ermöglichen.
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) Die G++-Maßnahme TEST.2.2 verlangt eine strukturierte Folgenabschätzung vor wesentlichen Änderungen durch Administrierende, was die Prüfung potenziell weitreichender Auswirkungen von Administrationstätigkeiten inhaltlich abdeckt.

### → SYS.1.7.A35 — Einsatz von RACF-Exits (H)
  1. Falls RACF-Exits eingesetzt werden, SOLLTEN die sicherheitstechnischen und betrieblichen Auswirkungen analysiert werden. **◀ ZITIERT**
  2. Die RACF-Exits SOLLTEN außerdem über das SMP/E (System Modification Program/Enhanced) als USERMOD installiert und überwacht werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) TEST.2.2 fordert eine strukturierte Folgenabschätzung vor wesentlichen Änderungen, was die Analyse der sicherheitstechnischen und betrieblichen Auswirkungen beim Einsatz von RACF-Exits als allgemeinere Anforderung abdeckt.

### → OPS.1.1.3.A7 — Integration des Änderungsmanagements in die Geschäftsprozesse (S)
  1. Der Änderungsmanagementprozess SOLLTE in die Geschäftsprozesse beziehungsweise Fachaufgaben integriert werden.
  2. Bei geplanten Änderungen SOLLTE die aktuelle Situation der davon betroffenen Geschäftsprozesse berücksichtigt werden. **◀ ZITIERT**
  3. Alle relevanten Fachabteilungen SOLLTEN über anstehende Änderungen informiert werden.
  4. Auch SOLLTE es eine Eskalationsebene geben, deren Mitglieder der Leitungsebene der Institution angehören.
  5. Die Mitglieder dieser Eskalationsebene SOLLTEN in Zweifelsfällen über Priorität und Terminplanung einer Hard- oder Software-Änderung entscheiden.
- **Satz 2** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) Die geforderte strukturierte Folgenabschätzung vor wesentlichen Änderungen deckt die Berücksichtigung der Situation und Auswirkungen auf betroffene Prozesse inhaltlich ab.


## TEST.3.1.10 — Lasttest  [2 Paare]

**Statement (normativ):** Änderungen und Tests KANN die Belastbarkeit bei hoher Auslastung testen.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** erhöht
**Guidance (nicht normativ):** Ziel ist es, die Dimensionierung der Ressourcen zu verifizieren und Fehler zu entdecken, die nur bei höherer Last auftreten. Hierzu können z.B. eine hohe Zahl gleichzeitiger Verbindungen, große Datenmengen oder eine hohe Zahl paralleler Interaktionen genutzt werden. Die Höhe der Auslastung kann sich dabei z.B. nach der maximalen Anzahl erwarteter gleichzeitiger Nutzungen richten.

### → CON.8.A7 — Durchführung von entwicklungsbegleitenden Software-Tests (B) [Testende, Entwickelnde]
  1. Schon bevor die Software im Freigabeprozess getestet und freigegeben wird, MÜSSEN entwicklungsbegleitende Software-Tests durchgeführt und der Quellcode auf Fehler gesichtet werden.
  2. Hierbei SOLLTEN bereits die Fachverantwortlichen des Auftraggebenden oder der beauftragenden Fachabteilung beteiligt werden.
  3. Die entwicklungsbegleitenden Tests MÜSSEN die funktionalen und nichtfunktionalen Anforderungen der Software umfassen.
  4. Die Software-Tests MÜSSEN dabei auch Negativtests abdecken.
  5. Zusätzlich MÜSSEN auch alle kritischen Grenzwerte der Eingabe sowie der Datentypen überprüft werden.
  6. Testdaten SOLLTEN dafür sorgfältig ausgewählt und geschützt werden.
  7. Darüber hinaus SOLLTE eine automatische statische Code-Analyse durchgeführt werden.
  8. Die Software MUSS in einer Test- und Entwicklungsumgebung getestet werden, die getrennt von der Produktionsumgebung ist.
  9. Außerdem MUSS getestet werden, ob die Systemvoraussetzungen für die vorgesehene Software ausreichend dimensioniert sind. **◀ ZITIERT**
- **Satz 9** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 9) TEST.3.1.10 deckt das Testen der Dimensionierung der Systemressourcen bzw. -voraussetzungen mittels Lasttests direkt ab.

### → INF.13.A22 — Durchführung von Systemtests im TGM (S) [Planende]
  1. Systeme des TGM und Systeme, die durch das TGM verwaltet werden, SOLLTEN vor der Inbetriebnahme und bei großen Systemänderungen hinsichtlich ihrer funktionalen und nicht-funktionalen Anforderungen getestet werden.
  2. Dabei SOLLTE auch das Soll- und Ist-Verhalten von Funktionen und Einstellungen geprüft werden.
  3. Bei den nicht-funktionalen Anforderungen SOLLTEN auch Anforderungen der Informationssicherheit getestet sowie zusätzlich bei Bedarf auch Lasttests durchgeführt werden. **◀ ZITIERT**
  4. Für die Tests SOLLTE eine Testspezifikation erstellt werden, die eine Beschreibung der Testumgebung, der Testtiefe und der Testfälle inklusive der Kriterien für eine erfolgreiche Testdurchführung enthält.
  5. Die Testdurchführung SOLLTE in einem Testbericht dokumentiert werden.
  6. Testspezifikationen SOLLTEN regelmäßig und zusätzlich bei Bedarf geprüft und gegebenenfalls aktualisiert werden, um dem aktuellen Stand der Technik zu entsprechen und auch neueste Erkenntnisse abdecken zu können.
- **Satz 3** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 3) Die Maßnahme TEST.3.1.10 deckt die im Satz geforderte Durchführung von Lasttests zur Überprüfung der Belastbarkeit bei hoher Auslastung direkt ab.

