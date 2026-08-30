# Review-Dossier Praktik DLS

Praktik DLS: 16 Controls mit Mapping, 62 Paare gesamt. Gesampelt: 5 Controls (max/min/median Paarzahl + 2 zufällig).

## DLS.1.1 — Verfahren und Regelungen  [11 Paare]

**Statement (normativ):** Dienstleistersteuerung für Dienstleistungen MUSS ein Verfahren zur Steuerung und geordneten Beendigung von Dienstleistungsverträgen verankern.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** Hierzu gehört die Kontrolle der Einhaltung von Vereinbarungen zur Sicherheit mit Dienstleistern und (falls erforderlich) einen geeigneten Weg für die Beendigung von Verträgen vorzubereiten. Die bei der Festlegung des Verfahrens im Einzelnen zu berücksichtigenden Inhalte ergeben sich aus den Anforderungen dieser Praktik.

### → IND.1.A11 — Sichere Beschaffung und Systementwicklung (S)
  1. Sollen OT-Systeme beschafft, geplant oder entwickelt werden, SOLLTEN Regelungen zur Informationssicherheit getroffen und dokumentiert werden.
  2. Die Unterlagen SOLLTEN Teil der Ausschreibung sein.
  3. Bei Beschaffungen, Planungen oder Entwicklungen SOLLTE die Informationssicherheit in dem gesamten Lebenszyklus berücksichtigt werden.
  4. Voraussetzungen und Umsetzungshinweise für einen sicheren Betrieb von ICS-Komponenten von den herstellenden Unternehmen SOLLTEN frühzeitig eingeplant und umgesetzt werden.
  5. Für ICS-Komponenten SOLLTEN einheitliche und dem Schutzbedarf angemessene Anforderungen an die Informationssicherheit definiert werden.
  6. Diese SOLLTEN berücksichtigt werden, wenn neue ICS-Komponenten beschafft werden.
  7. Die Einhaltung und Umsetzung SOLLTE dokumentiert werden.
  8. Die Institution SOLLTE dokumentieren, wie sich das System in die Konzepte für die Zoneneinteilung, das Berechtigungs- und Schwachstellen-Management sowie für den Virenschutz einfügt und diese gegebenenfalls anpassen.
  9. Es SOLLTE geregelt sein, wie der Betrieb aufrechterhalten werden kann, falls einer der Kooperationspartner keine Dienstleistungen mehr anbietet. **◀ ZITIERT**
- **Satz 9** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 9) Die Maßnahme fordert ein Verfahren zur geordneten Beendigung von Dienstleistungsverträgen, was die Regelung zur Betriebsaufrechterhaltung beim Wegfall von Dienstleistern inhaltlich abdeckt.

### → ISMS.1.A5 — Vertragsgestaltung bei Bestellung eines oder einer externen Informationssicherheitsbeauftragten (B) [Institutionsleitung]
  1. Die Institutionsleitung MUSS einen externen oder eine externe ISB bestellen, wenn die Rolle des oder der ISB nicht durch einen internen Mitarbeitenden besetzt werden kann.
  2. Der Vertrag mit einem oder einer externen ISB MUSS alle Aufgaben des oder der ISB sowie die damit verbundenen Rechte und Pflichten umfassen.
  3. Der Vertrag MUSS eine geeignete Vertraulichkeitsvereinbarung umfassen.
  4. Der Vertrag MUSS eine kontrollierte Beendigung des Vertragsverhältnisses, einschließlich der Übergabe der Aufgaben an die Auftraggebenden, gewährleisten. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 4) DLS.1.1 fordert die Verankerung eines Verfahrens zur geordneten Beendigung von Dienstleistungsverträgen, was die kontrollierte Beendigung des Vertragsverhältnisses für externe Dienstleister wie einen externen ISB allgemein abdeckt.

### → OPS.2.2.A14 — Geordnete Beendigung eines Cloud-Nutzungs-Verhältnisses (S) [Fachverantwortliche, Institutionsleitung]
  1. Wenn das Dienstleistungsverhältnis mit den Cloud-Diensteanbietenden beendet wird, SOLLTE sichergestellt sein, dass dadurch die Geschäftstätigkeit oder die Fachaufgaben der Institution nicht beeinträchtigt wird. **◀ ZITIERT**
  2. Die Verträge mit den Cloud-Diensteanbietenden SOLLTEN regeln, wie das jeweilige Dienstleistungsverhältnis geordnet aufgelöst werden kann. **◀ ZITIERT**
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) DLS.1.1 verlangt die Verankerung eines Verfahrens zur geordneten Beendigung von Dienstleistungsverträgen, was das Sicherstellen einer unterbrechungsfreien Geschäftstätigkeit bei Vertragsende allgemein abdeckt.
- **Satz 2** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 2) DLS.1.1 fordert die Verankerung eines Verfahrens zur geordneten Beendigung von Dienstleistungsverträgen und deckt damit die vertragliche Regelung zur geordneten Auflösung des Dienstleistungsverhältnisses inhaltlich ab.

### → OPS.2.2.A9 — Vertragsgestaltung mit den Cloud-Diensteanbietenden (S) [Institutionsleitung]
  1. Die vertraglichen Regelungen zwischen der auftraggebenden Institution und den Cloud-Diensteanbietenden SOLLTEN in Art, Umfang und Detaillierungsgrad dem Schutzbedarf der Informationen angepasst sein, die im Zusammenhang mit der Cloud-Nutzung stehen.
  2. Es SOLLTE geregelt werden, an welchem Standort die Cloud-Diensteanbietenden ihre Leistung erbringen.
  3. Zusätzlich SOLLTEN Eskalationsstufen und Kommunikationswege zwischen der Institution und den Cloud-Diensteanbietenden definiert werden.
  4. Auch SOLLTE vereinbart werden, wie die Daten der Institution sicher zu löschen sind.
  5. Ebenso SOLLTEN Kündigungsregelungen schriftlich fixiert werden. **◀ ZITIERT**
  6. Die Cloud-Diensteanbietenden SOLLTEN alle Subunternehmen offenlegen, die sie für den Cloud-Dienst benötigen.
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) DLS.1.1 verankert ein Verfahren zur geordneten Beendigung von Dienstleistungsverträgen und deckt damit die Festlegung von Kündigungsregelungen auf übergeordneter Ebene ab.

### → OPS.2.3.A19 — Überprüfung der Handlungsalternativen hinsichtlich einer geplanten oder ungeplanten Beendigung eines Outsourcing-Verhältnisses (S) [Beschaffungsstelle]
  1. Handlungsalternativen SOLLTEN entwickelt werden für den Fall einer geplanten oder ungeplanten Beendigung des Outsourcing-Verhältnisses. **◀ ZITIERT**
  2. Das Resultat SOLLTE in einem Maßnahmenkatalog für geplante und ungeplante Beendigung des Outsourcing-Verhältnisses dokumentiert werden.
  3. Dabei SOLLTEN auch alternative Anbietende von Outsourcing ermittelt werden, die über das notwendige Niveau an Informationssicherheit verfügen, um den Prozess sicher umzusetzen.
  4. Dies SOLLTE in regelmäßigen Abständen und anlassbezogen geprüft werden.
- **Satz 1** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) DLS.1.1 fordert die Verankerung eines Verfahrens zur geordneten Beendigung von Dienstleistungsverträgen einschließlich der Vorbereitung geeigneter Wege zur Beendigung, was die Entwicklung von Handlungsalternativen für den Ausstieg inhaltlich abdeckt.

### → SYS.1.8.A9 — Auswahl von Liefernden für eine Speicherlösung (S)
  1. Anhand der spezifizierten Anforderungen an eine Speicherlösung SOLLTEN geeignete Liefernde ausgewählt werden.
  2. Die Auswahlkriterien und die Entscheidung SOLLTEN nachvollziehbar dokumentiert werden.
  3. Außerdem SOLLTEN Aspekte der Wartung und Instandhaltung schriftlich in sogenannten Service-Level-Agreements (SLAs) festgehalten werden.
  4. Die SLAs SOLLTEN eindeutig und quantifizierbar sein.
  5. Es SOLLTE genau geregelt werden, wann der Vertrag mit den Liefernden endet. **◀ ZITIERT**
- **Satz 5** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) Die G++-Maßnahme DLS.1.1 fordert die Verankerung von Verfahren und Regelungen zur geordneten Beendigung von Dienstleistungsverträgen und deckt die Forderung nach Regelung des Vertragsendes inhaltlich ab.

### → OPS.1.1.1.A18 — Planung des Einsatzes von Dienstleistenden (S)
  1. Der IT-Betrieb SOLLTE den Einsatz von Dienstleistenden koordinieren und diese unter anderem über SLAs so steuern, dass die Dienstleistung in ausreichendem Maße erbracht wird. **◀ ZITIERT**
  2. Der Einsatz von verschiedenen Dienstleistenden SOLLTE aufeinander abgestimmt werden, insbesondere falls diese für den gleichen Tätigkeitsbereich vorgesehen sind.
  3. Für solche Situationen SOLLTE jeweils eine eindeutige Kommunikationsschnittstelle festgelegt werden.
  4. Der IT-Betrieb SOLLTE die Festlegungen zum Dienstleistendenmanagement sowie die für die Dienstleistenden vorgesehenen Tätigkeiten festhalten, regelmäßig prüfen und anpassen.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) Die G++-Maßnahme DLS.1.1 fordert die Etablierung eines Verfahrens zur Steuerung von Dienstleistungsverträgen und deckt damit die geforderte Steuerung und Koordination von Dienstleistenden ab.

### → OPS.2.3.A14 — Erweiterte Anforderungen an Verträge mit Anbietenden von Outsourcing (S)
  1. Mit Anbietenden von Outsourcing SOLLTE vereinbart werden, auf welche Bereiche und Dienste die Anbietenden im Netz der Nutzenden von Outsourcing zugreifen dürfen.
  2. Der Umgang mit anfallenden Metadaten SOLLTE geregelt werden.
  3. Die Nutzenden SOLLTEN Leistungskennzahlen für die Anbietenden von Outsourcing definieren und im Vertrag festlegen.
  4. Für den Fall, dass die vereinbarten Leistungskennzahlen unzureichend erfüllt werden, SOLLTEN mit den Anbietenden von Outsourcing Konsequenzen, wie z. B. Vertragsstrafen, festgelegt werden.
  5. Die Verträge SOLLTEN Kündigungsoptionen, um das Outsourcing-Verhältnisses aufzulösen, enthalten. **◀ ZITIERT**
  6. Hierbei SOLLTE auch geregelt sein, wie das Eigentum der Nutzenden von Outsourcing zurückgegeben wird.
  7. Im Vertrag SOLLTEN Verantwortlichkeiten hinsichtlich des Notfall- und Krisenmanagements definiert und benannt werden.
- **Satz 5** | Relation GS++→ED23: `intersects-with` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 5) Die Maßnahme verlangt ein Verfahren zur geordneten Beendigung von Dienstleistungsverträgen, was Kündigungsoptionen und Beendigungsregelungen in Verträgen einschließt.

### → OPS.2.3.A7 — Regelungen für eine geplante oder ungeplante Beendigung eines Outsourcing-Verhältnisses (B) [Fachverantwortliche, Institutionsleitung]
  1. Für geplante sowie ungeplante Beendigungen des Outsourcing-Verhältnisses MÜSSEN Regelungen getroffen werden. **◀ ZITIERT**
  2. Es MUSS festgelegt werden, wie alle Informationen, Daten und Hardware der Nutzenden vom Anbietenden von Outsourcing zurückgegeben werden.
  3. Hierbei MÜSSEN gesetzliche Vorgaben zur Aufbewahrung von Daten beachtet werden.
  4. Ferner SOLLTE überprüft werden, ob die Zugangs-, Zutritts- und Zugriffsrechte für die Anbietenden von Outsourcing mit der Beendigung des Outsourcing-Verhältnisses aufgehoben wurden.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) Die Maßnahme DLS.1.1 fordert explizit die Verankerung von Verfahren und Regelungen zur geordneten Beendigung von Dienstleistungsverhältnissen und deckt damit die Kernforderung von Satz 1 direkt ab.

### → OPS.3.2.A6 — Regelungen für eine geplante und ungeplante Beendigung eines Outsourcing-Verhältnisses (B)
  1. Es MÜSSEN Regelungen getroffen werden, wie verfahren wird, wenn Outsourcing-Verhältnisse geplant oder ungeplant beendet werden. **◀ ZITIERT**
  2. Es MUSS festgelegt werden, wie alle Informationen, Daten und Hardware der Nutzenden von den Anbietenden von Outsourcing zurückgegeben werden.
  3. Anschließend MÜSSEN die verbleibenden Datenbestände der Nutzenden von Outsourcing nach Ablauf der gesetzlichen Vorgaben zur Datenaufbewahrung sicher gelöscht werden.
  4. Dies MUSS durch die Anbietenden von Outsourcing dokumentiert werden.
  5. Ferner SOLLTE überprüft werden, ob die Zugangs-, Zutritts- und Zugriffsrechte für die Nutzenden von Outsourcing aufgehoben wurden, nachdem das Outsourcing-Verhältnis beendet wurde.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) DLS.1.1 fordert explizit die Verankerung eines Verfahrens zur geordneten Beendigung von Dienstleistungsverträgen und deckt damit die Forderung nach Regelungen für die Beendigung von Outsourcing-Verhältnissen direkt ab.


## DLS.2.3 — Vollverschlüsselung  [3 Paare]

**Statement (normativ):** Dienstleistersteuerung für Daten KANN diese, wenn der Anbieter deren Inhalt zur Vertragserbringung nicht kennen muss, für diesen nicht entschlüsselbar vor der Übertragung zum Dienstleister verschlüsseln.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** erhöht
**Guidance (nicht normativ):** Hierbei handelt es sich um eine Verschlüsselung at-rest, bei welcher der Dienstleister keinen Zugang zum Schlüssel erhält. Die Umsetzung kann z.B. auf Dateiebene oder durch Container erfolgen.

### → OPS.2.3.A23 — Einsatz von Verschlüsselungen (H)
  1. Sensible Daten SOLLTEN angemessen verschlüsselt werden, wenn sie zum Anbietenden von Outsourcing übertragen werden.
  2. Die abgelegten Daten SOLLTEN durch eine Datenverschlüsselung oder eine Verschlüsselung des Speichermediums geschützt werden. **◀ ZITIERT**
  3. Nach Möglichkeit SOLLTE eine vom BSI geprüfte und freigegebene Verschlüsselungssoftware genutzt werden.
- **Satz 2** | Relation GS++→ED23: `subset-of` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 2) Satz 2 fordert den Schutz abgelegter Daten beim Outsourcing-Dienstleister durch Daten- oder Speichermedienverschlüsselung, was der in DLS.2.3 thematisierten Verschlüsselung at-rest entspricht.

### → OPS.3.2.A20 — Verschlüsselte Datenübertragung und -speicherung (H)
  1. Für die Übertragung von Daten von und zu den Nutzenden von Outsourcing sowie die Speicherung SOLLTE mit den Nutzenden von Outsourcing eine sicheres Verschlüsselungsverfahren festgelegt werden. **◀ ZITIERT**
  2. Dabei SOLLTE sich die eingesetzte Verschlüsselungsmethode am Schutzbedarf der Daten orientieren.
  3. Die Verschlüsselungsmethode SOLLTE regelmäßig und anlassbezogen auf ihre Funktionsfähigkeit hin überprüft werden.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 1) Satz 1 fordert die Festlegung eines sicheren Verschlüsselungsverfahrens für die Speicherung und Übertragung von Daten im Outsourcing-Kontext, was sich mit der geforderten Speicherverschlüsselung für Dienstleister überschneidet.

### → OPS.2.2.A17 — Einsatz von Verschlüsselung bei Cloud-Nutzung (H)
  1. Wenn Daten durch Cloud-Diensteanbietende verschlüsselt werden, SOLLTE vertraglich geregelt werden, welche Verschlüsselungsmechanismen und welche Schlüssellängen eingesetzt werden dürfen.
  2. Wenn eigene Verschlüsselungsmechanismen genutzt werden, SOLLTE ein geeignetes Schlüsselmanagement sichergestellt sein. **◀ ZITIERT**
  3. Bei der Verschlüsselung SOLLTEN die eventuellen Besonderheiten des gewählten Cloud-Service-Modells berücksichtigt werden.
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 2) Satz 2 adressiert den Einsatz eigener Verschlüsselungsmechanismen bei Cloud-Diensten, was die vom Dienstleister unabhängige Verschlüsselung vor der Datenübertragung gemäß DLS.2.3 abdeckt.


## DLS.4.1.1 — Unabhängigkeit  [1 Paare]

**Statement (normativ):** Dienstleistersteuerung für Outsourcing SOLLTE die Unabhängigkeit der Verarbeitung schützenswerter Informationen vor der Außerbetriebnahme testen.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** „Unabhängigkeit der Verarbeitung“ meint hier die Fähigkeit, dass die Nutzung von Informationen in Geschäftsprozessen der Institution nicht von den Systemen, Verfahren oder Interessen des externen Dienstleisters abhängig ist, sodass ihre Integrität, Verfügbarkeit und Vertraulichkeit auch nach einer Außerbetriebnahme des Outsourcings gewährleistet bleibt. Die Vorschrift dient dem Zweck, die Risiken zu minimieren, die entstehen können, wenn ein Dienstleister seine Leistung einstellt, Verträge beendet werden oder ein abruptes Ende der Zusammenarbeit erfolgt. Ohne Vorkehrungen könnte dies dazu führen, dass kritische Daten unzugänglich bleiben, unkontrolliert gelöscht werden oder in Abhängigkeit von proprietären Formaten verloren gehen. Zur Umsetzung kann die Institution verschiedene Maßnahmen prüfen: (1) Ein systematischer Test, ob Daten in standardisierten, portablen Formaten exportierbar sind und in eigenen oder alternativen Systemen fehlerfrei weiterverarbeitet werden können. (2) Ein Probelauf, bei dem die Verbindung zum Dienstleister gezielt getrennt wird, um zu überprüfen, ob die Institution ihre Geschäftsprozesse auch ohne aktive Anbindung fortführen kann. (3) Ein kontrolliertes Abschalten einzelner vom Dienstleister erbrachter Dienste, um zu verifizieren, ob vorbereitete Ersatzprozesse oder interne Systeme die Funktion übernehmen. (4) Eine Teststellung für die Rückgabe von Datenbeständen am Ende der Vertragslaufzeit, bei der die Vollständigkeit, Konsistenz und Nutzbarkeit der gelieferten Daten geprüft wird. Mit solchen Maßnahmen kann die Institution sicherstellen, dass die Verarbeitung schützenswerter Informationen eigenständig aufrechterhalten werden kann.

### → OPS.2.2.A15 — Sicherstellung der Portabilität von Cloud-Diensten (H) [Fachverantwortliche]
  1. Die Institution SOLLTE alle Anforderungen definieren, die es ermöglichen, Cloud-Diensteanbietende zu wechseln oder den Cloud-Dienst bzw. die Daten in die eigene IT-Infrastruktur zurückzuholen.
  2. Zudem SOLLTE die Institution regelmäßig Portabilitätstests durchführen. **◀ ZITIERT**
  3. In den Verträgen mit den Cloud-Diensteanbietenden SOLLTEN Vorgaben festgehalten werden, mit denen sich die notwendige Portabilität gewährleisten lässt.
- **Satz 2** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 2) Satz 2 fordert die regelmäßige Durchführung von Portabilitätstests, was ein direkter Anwendungsfall für das Testen der Unabhängigkeit der Verarbeitung von einem externen Dienstleister darstellt.


## DLS.2.2 — Transportverschlüsselung  [4 Paare]

**Statement (normativ):** Dienstleistersteuerung für Daten SOLLTE den Transport bei der Übertragung zum Anbieter nach {{ insert: param, dls.2.2-prm1 }} verschlüsseln.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** normal-SdT
**Guidance (nicht normativ):** „Transport“ bedeutet hier der technische Vorgang der Datenübertragung zwischen der Institution und dem Dienstleister, also etwa über das Internet oder dedizierte Leitungen. Der Sinn dieser Vorschrift liegt darin, die Vertraulichkeit und Integrität von Informationen zu schützen, wenn sie in fremde Infrastrukturen überführt werden. Ohne eine solche Maßnahme könnte ein Angreifer Daten während der Übertragung abfangen oder manipulieren, beispielsweise über „Man-in-the-Middle“-Angriffe oder durch Abhören unsicherer Netze. Da beschaffte Dienstleistungen typischerweise außerhalb der direkten Kontrolle der Institution liegen, gibt es hier eine eigene Vorgabe, um die besondere Risikosituation beim Übergang von interner zu externer Infrastruktur gezielt abzusichern. Eine Institution kann die Anforderung praktisch umsetzen, indem sie (1) den Einsatz von Protokollen wie TLS in allen Web- und API-basierten Schnittstellen zum Anbieter sicherstellt, (2) für administrative Zugänge oder besonders sensible Datenübertragungen zusätzlich VPN-Verbindungen nutzen kann, und (3) Zertifikatsprüfungen so konfiguriert, dass unsichere oder abgelaufene Zertifikate nicht akzeptiert werden.

### → CON.9.A8 — Verschlüsselung und digitale Signatur (S)
  1. Die Institution SOLLTE prüfen, ob Informationen während des Austausches kryptografisch gesichert werden können. **◀ ZITIERT**
  2. Falls die Informationen kryptografisch gesichert werden, SOLLTEN dafür ausreichend sichere Verfahren eingesetzt werden.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) DLS.2.2 verlangt die Transportverschlüsselung bei der Datenübertragung zu Dienstleistern und deckt damit als konkreter Anwendungsfall die kryptografische Sicherung von Informationen während des Austausches ab.

### → OPS.2.3.A23 — Einsatz von Verschlüsselungen (H)
  1. Sensible Daten SOLLTEN angemessen verschlüsselt werden, wenn sie zum Anbietenden von Outsourcing übertragen werden. **◀ ZITIERT**
  2. Die abgelegten Daten SOLLTEN durch eine Datenverschlüsselung oder eine Verschlüsselung des Speichermediums geschützt werden.
  3. Nach Möglichkeit SOLLTE eine vom BSI geprüfte und freigegebene Verschlüsselungssoftware genutzt werden.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) Die G++-Maßnahme DLS.2.2 fordert explizit die Transportverschlüsselung bei der Übertragung von Daten an den Dienstleister und deckt damit die Forderung von Satz 1 inhaltlich direkt ab.

### → OPS.3.2.A10 — Etablierung eines sicheren Kommunikationskanals und Festlegung der Kommunikationspartner (S)
  1. Die Anbietenden von Outsourcing SOLLTEN einen sicheren Kommunikationskanal zu den Nutzenden von Outsourcing einrichten. **◀ ZITIERT**
  2. Es SOLLTE dokumentiert sein, welche Informationen über diesen Kommunikationskanal an den Outsourcing-Partner übermittelt werden.
  3. Dabei SOLLTE sichergestellt werden, dass an den jeweiligen Enden des Kommunikationskanals entsprechend Zuständige benannt sind.
  4. Dabei SOLLTE regelmäßig und anlassbezogen überprüft werden, ob diese Personen noch in ihrer Funktion als dedizierte Kommunikationspartner beschäftigt sind.
  5. Zwischen den Outsourcing-Partnern SOLLTE geregelt sein, nach welchen Kriterien welcher Kommunikationspartner welche Informationen erhalten darf.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 1) Die geforderte Transportverschluesselung bei der Uebertragung zum Dienstleister setzt die Einrichtung eines sicheren Kommunikationskanals technisch direkt um.

### → OPS.3.2.A20 — Verschlüsselte Datenübertragung und -speicherung (H)
  1. Für die Übertragung von Daten von und zu den Nutzenden von Outsourcing sowie die Speicherung SOLLTE mit den Nutzenden von Outsourcing eine sicheres Verschlüsselungsverfahren festgelegt werden. **◀ ZITIERT**
  2. Dabei SOLLTE sich die eingesetzte Verschlüsselungsmethode am Schutzbedarf der Daten orientieren.
  3. Die Verschlüsselungsmethode SOLLTE regelmäßig und anlassbezogen auf ihre Funktionsfähigkeit hin überprüft werden.
- **Satz 1** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 1) DLS.2.2 deckt die geforderte sichere Verschlüsselung für die Datenübertragung im Rahmen von Dienstleistungen bzw. Outsourcing inhaltlich ab.


## DLS.3.2 — Checkup  [3 Paare]

**Statement (normativ):** Dienstleistersteuerung für Outsourcing KANN die risikoorientierte Entscheidung über Outsourcing auf Grundlage der Geschäftsprozessprofile auf Änderungen der Gefährdungslage oder Prozessinhalte {{ insert: param, dls.3.2-prm1 }} überprüfen.
**Klasse:** BSI-Stand-der-Technik-Kernel-G0 | **sec_level:** erhöht
**Guidance (nicht normativ):** Die risikoorientierte Entscheidung über Outsourcing kann in diesem Kontext als wiederkehrende Bewertung der Abhängigkeiten und Gefahren verstanden werden, die durch externe Dienstleister in den Geschäftsprozessen einer Institution entstehen. Der Parameter regelmäßig kann je nach Kritikalität der ausgelagerten Prozesse sinnvoll mit Werten wie halbjährlich, jährlich oder nach definierten Ereignissen (z. B. Einführung neuer regulatorischer Vorgaben oder Sicherheitsvorfälle) ausgefüllt werden. Änderungen der Gefährdungslage beziehen sich auf die dynamische Entwicklung von Bedrohungen wie Cyberangriffe, Lieferkettenstörungen oder neue regulatorische Anforderungen, während Änderungen der Prozessinhalte vor allem die Anpassung oder Erweiterung der durch Dienstleister erbrachten Leistungen umfassen. Der Zweck dieser Vorschrift liegt darin, frühzeitig sicherzustellen, dass die bisherigen Risikoeinschätzungen und Dienstleistervereinbarungen weiterhin tragfähig sind und nicht durch externe Veränderungen entwertet werden. Ohne eine solche Überprüfung könnte beispielsweise ein Dienstleister aufgrund verschärfter Bedrohungen unzureichenden Schutz bieten oder durch eine stillschweigende Ausweitung von Leistungen in Bereiche gelangen, die ursprünglich nicht risikobewertet wurden. Eine regelmäßige Kontrolle kann dagegen dafür sorgen, dass Risiken durch Outsourcing transparent bleiben und rechtzeitig nachjustiert werden. Zur praktischen Umsetzung kann eine Institution beispielsweise (1) eine Checkliste führen, die bei jeder Neubewertung konkrete Aspekte wie Datenlokation, technische Sicherheitsmaßnahmen oder Zertifikatsgültigkeiten abfragt und (2) ein automatisiertes Monitoring nutzen, das öffentliche Sicherheitsnachweise wie Testate nach BSI C5 oder SOC-Reports erfasst und in die Bewertung einbindet. Auch die Nutzung von Incident-Datenbanken oder branchenspezifischen Threat-Feeds kann helfen, Gefährdungslagen aktuell einzuschätzen. Ein bewährter Tipp ist es, nicht nur formale Unterlagen zu prüfen, sondern auch technische Stichproben durchzuführen, etwa in Form von Konfigurationsprüfungen oder Penetrationstests, sofern dies durch den Dienstleister gestattet wird. Damit kann die Institution sicherstellen, dass die theoretische Risikoabwägung durch reale Prüfungen gestützt wird und sich an tatsächlichen Veränderungen orientiert.

### → OPS.2.2.A1 — Erstellung einer Strategie für die Cloud-Nutzung (B) [Fachverantwortliche, Institutionsleitung, Datenschutzbeauftragte]
  1. Eine Strategie für die Cloud-Nutzung MUSS erstellt werden.
  2. Darin MÜSSEN Ziele, Chancen und Risiken definiert werden, die die Institution mit der Cloud-Nutzung verbindet.
  3. Zudem MÜSSEN die rechtlichen und organisatorischen Rahmenbedingungen sowie die technischen Anforderungen untersucht werden, die sich aus der Nutzung von Cloud-Diensten ergeben.
  4. Die Ergebnisse dieser Untersuchung MÜSSEN in einer Machbarkeitsstudie dokumentiert werden.
  5. Es MUSS festgelegt werden, welche Dienste in welchem Bereitstellungsmodell zukünftig von Cloud-Diensteanbietenden bezogen werden sollen.
  6. Zudem MUSS sichergestellt werden, dass bereits in der Planungsphase zur Cloud-Nutzung alle grundlegenden technischen und organisatorischen Sicherheitsaspekte ausreichend berücksichtigt werden.
  7. Für den geplanten Cloud-Dienst SOLLTE eine grobe individuelle Sicherheitsanalyse durchgeführt werden.
  8. Diese SOLLTE wiederholt werden, wenn sich technische und organisatorische Rahmenbedingungen wesentlich verändern. **◀ ZITIERT**
  9. Für größere Cloud-Projekte SOLLTE zudem eine Roadmap erarbeitet werden, die festlegt, wann und wie ein Cloud-Dienst eingeführt wird.
- **Satz 8** | Relation GS++→ED23: `superset-of` | Fundrichtung: ed23-seitig
  Begründung: (Teilanforderung 8) DLS.3.2 deckt die Wiederholung der Sicherheits- bzw. Risikobewertung bei veränderten Rahmenbedingungen (Gefährdungslage oder Prozessinhalte) im Rahmen des Outsourcings inhaltlich ab.

### → OPS.2.3.A2 — Verfolgung eines risikoorientierten Ansatzes im Auslagerungsmanagement (B)
  1. Für Prozesse, die potenziell ausgelagert werden sollen, MUSS risikoorientiert betrachtet und entschieden werden, ob diese ausgelagert werden können.
  2. Für diese Bewertung SOLLTEN die Anforderungsprofile als Grundlage genutzt werden.
  3. Wenn der Prozess ausgelagert wird, SOLLTE das Resultat im Auslagerungsregister abgelegt werden.
  4. Um Änderungen an Prozessen oder der Gefährdungslage zu berücksichtigen, MÜSSEN in regelmäßigen Abständen sowie anlassbezogen die ausgelagerten Prozesse erneut risikoorientiert betrachtet werden. **◀ ZITIERT**
- **Satz 4** | Relation GS++→ED23: `subset-of` | Fundrichtung: beide
  Begründung: (Teilanforderung 4) Die G++-Maßnahme DLS.3.2 deckt die regelmäßige und anlassbezogene risikoorientierte Überprüfung der ausgelagerten Prozesse bei Änderungen der Gefährdungslage oder Prozessinhalte inhaltlich direkt ab.

### → OPS.2.3.A18 — Überprüfung der Vereinbarungen mit Anbietenden von Outsourcing (S)
  1. Vereinbarungen mit Anbietenden von Outsourcing hinsichtlich der Angemessenheit der festgelegten Sicherheitsanforderungen sowie sonstigen Sicherheitsanforderungen SOLLTEN in regelmäßigen Abständen und anlassbezogen überprüft werden. **◀ ZITIERT**
  2. Vereinbarungen mit Anbietenden von Outsourcing mit unzureichend festgelegten Sicherheitsanforderungen SOLLTEN nachgebessert werden.
  3. Die Anbietenden von Outsourcing SOLLTEN dazu verpflichtet werden, bei veränderter Gefährdungs- oder Gesetzeslage, die festgelegten Sicherheitsanforderungen nachzubessern.
- **Satz 1** | Relation GS++→ED23: `intersects-with` | Fundrichtung: gpp-seitig
  Begründung: (Teilanforderung 1) Satz 1 fordert die regelmäßige und anlassbezogene Überprüfung von Outsourcing-Vereinbarungen auf Angemessenheit der Sicherheitsanforderungen, was sich direkt mit der wiederkehrenden Überprüfung der Outsourcing-Entscheidung bei veränderter Gefährdungs- oder Prozesslage in DLS.3.2 überschneidet.

