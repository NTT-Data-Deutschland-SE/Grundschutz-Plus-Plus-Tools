# Anhang C: Glossar der Methodik-Begriffe

**Handbuch zur Grundschutz++ Methodik · Version 0.4 (Entwurf)** · Stand: 2026-10-26 · Quellen: Katalog-Build 2026-10-22 (Statements und Guidance), Namespace-CSVs (Klon vom 2026-10-23), BSI-Standard 300-1 (Version 1.0, 20.10.2026) · Änderung 0.4: Begriffe des Standards 300-1 aufgenommen (Anwendungsbereich, Blaupause, Korrektur- und Verbesserungsplan, Mindestkriterien, nicht anwendbar, Prozessschritt, temporäre und dauerhafte Nichterfüllung), bestehende Einträge auf Build 2026-10-22 und Standard nachgezogen.

Aufgenommen sind nur katalog-, namespace- oder standardbelegte Begriffe; die Fundstelle steht bei jedem Eintrag, Begriffe, die nur der Standard 300-1 kennt, sind so gekennzeichnet. Begriffe, deren Definition in den Quellen fehlt oder strittig ist, tragen einen Verweis auf Anhang D. Kursiv gesetzte Alt-Begriffe der 200-2-Welt sind in Kapitel 10.2 übersetzt.

**Action Word** – Das Erfüllungsverb eines Statements mit definierter Erfüllungssemantik im Namespace `action_words.csv` (27 Verben, 13 davon in der Methodik verwendet). Das Action Word liefert das Prüfkriterium einer Anforderung. (Kapitel 3.2)

**alt-identifier** – Stabile UUID jedes Controls; versionsfeste Referenz, im Gegensatz zur sprechenden ID, die sich zwischen Builds ändern kann. (Kapitel 3.1, 10.3)

**Anforderungspaket** – Menge aller Anforderungen, die für den betrachteten Informationsverbund und den priorisierten Geschäftsprozess gelten; zentrales Arbeitsdokument der Methodik, erzeugt durch STM.2, abgearbeitet durch UMS, evaluiert durch PERF.1.2/1.3. (Kapitel 5.2)

**Anwendungsbereich** – Begriff des Standards 300-1 für den Geltungsbereich des Katalogs (GC.6.1): der von der Institutionsleitung festgelegte Umfang des ISMS aus Geschäftsprozessen, Institutionseinheiten, Standorten, Anwendungen und IT-Systemen; kann einen oder mehrere Informationsverbünde enthalten (Standard 300-1, Kap. 2.3, 3.1). (Kapitel 4.6)

**Ausnahmegenehmigung** – Autorisierte, begründete und dokumentierte Abweichung von einer Verpflichtung (UMS.5.1, UMS.5.2); Nachweisdokument „Freigegebene Ausnahmegenehmigung". Nach Standard 300-1 für MUSS-Anforderungen ausgeschlossen (Kap. 4.1.2); dort außerdem die Autorisierung eines Risikos außerhalb der Akzeptanzkriterien durch die Institutionsleitung (Mindestkriterium 27). Begriffsumfang siehe Anhang D. (Kapitel 6.5)

**Blaupause** – Nach Standard 300-1 „ein vorgefertigter Katalog von Anforderungen" für ein Anwendungsszenario mit vorgegebenen Parametern; Auswahl mit Version, Zuordnung und Anpassung zu dokumentieren, für bestimmte Institutionen verpflichtend möglich (Kap. 3.3). Technisch ein OSCAL-Profil über dem Anwenderkatalog; im Katalog nur in der Praktik-Beschreibung von STM erwähnt. (Kapitel 3.8, 5.2)

**Control** – Einzelne Anforderung im OSCAL-Katalog, mit Statement, meist Guidance, Properties und gegebenenfalls Kind-Controls bis Ebene 4. (Kapitel 3.1)

**documentation-Prop** – Property am Statement, die das Nachweisdokument der Anforderung benennt; 59 der 95 Methodik-Controls tragen sie, 20 Dokumente insgesamt (Build 2026-10-22). (Kapitel 3.2, Anhang B)

**effort_level** – Aufwandsstufe 0 bis 5 je Control; 0 heißt „wird nicht bewertet, da zwingend erforderlich", 5 steht für komplexe Großmaßnahmen. Definitionen im Namespace `effort_level.csv`. (Kapitel 3.4)

**Geltungsbereich** – Formal und organisatorisch abgegrenzter Anwendungsbereich des ISMS, festgelegt nach Freigabe der Institutionsleitung (GC.6.1); Grundlage des Informationsverbunds; im Standard 300-1 „Anwendungsbereich". (Kapitel 4.6)

**Guidance** – Erläuternder Part eines Controls; nicht normativ, aber auslegungsleitend und teils mit faktisch bindenden Festlegungen. (Kapitel 3.10)

**Informationssicherheitseinstufung** – Verfahren zur Festlegung der Geschäftsprozesse und zur zweistufigen Einstufung ihres Schutzbedarfs in „normal" oder „hoch" (GC.7). (Kapitel 4.7)

**Informationsverbund** – Technisch-organisatorische Ausgestaltung des Geltungsbereichs: Systeme, Prozesse, Personen, Komponenten samt Grenzen und Schnittstellen (STM.1.1, STM.1.2); zugleich Name des Nachweisdokuments. (Kapitel 5.1)

**Institutionsleitung** – Oberste Führungsebene; trägt die Gesamtverantwortung, autorisiert ISMS, Leitlinie und Geltungsbereich, entscheidet über den wichtigsten Geschäftsprozess und empfängt den Managementbericht (GC.1.2, GC.5.1.2, GC.6.1, GC.7.1.2, PERF.4.2). (Kapitel 4, 8.4)

**ISB (Informationssicherheitsbeauftragter)** – Unabhängige, unmittelbar der Institutionsleitung unterstellte Person mit der Zuständigkeit für Informationssicherheit; mit Ressourcen und direktem Vorspracherecht auszustatten (GC.9.1.1.1 mit Sub-Controls). Titelvarianten laut Guidance: CISO, ISM. (Kapitel 4.9)

**ISMS-Regelwerk** – Nachweisdokument der Verfahren und Regelungen zur Errichtung und Aufrechterhaltung des ISMS (GC.1.1); die Klammer über der Dokumentenlandschaft. (Kapitel 4.1)

**Katalog-Build** – Versionsstand des maschinenlesbaren Katalogs (hier durchgängig: 2026-10-22; das vom BSI angekündigte Update an den Standard 300-1 steht aus); Grundschutz++ erscheint in Builds statt Editionen. (Kapitel 1.1, 10.3)

**Kernel** – Die technischen und organisatorischen Sicherheitspraktiken ASST bis TEST (14 Praktiken, 901 Controls im Anwenderkatalog); nicht Gegenstand dieses Handbuchs. (Kapitel 1.2)

**Korrektur- und Verbesserungsplan** – Begriff des Standards 300-1 für die priorisierten Korrektur- und Verbesserungsvorschläge; „wird in den Umsetzungsplan aufgenommen" (Kap. 6.3), also kein zweites Dokument. (Kapitel 7.5)

**Managementbericht** – Verdichtetes Berichtsdokument der Managementbewertung an die Institutionsleitung; Rahmen und Maßnahmenvorschläge MUSS, acht Inhaltsbausteine SOLLTE (PERF.4.1 mit Sub-Controls, PERF.4.2); zugleich Vehikel der ISMS-Freigabe (GC.1.2). (Kapitel 8.4)

**Mindestkriterien** – 35 verbindliche Kriterien für die Risikobetrachtung in Anhang 3 des Standards 300-1 (Initiierung 1 bis 10, Identifikation 11 bis 17, Bewertung 18 bis 22, Behandlung 23 bis 31, phasenübergreifend 32 bis 35); im Anwenderkatalog nur zum Teil durch Controls gedeckt, gebunden über das nicht importierte RISK.1.2. (Kapitel 4.12)

**Modalverb** – Verbindlichkeitsstufe eines Statements nach RFC 2119 / DIN 820-2: MUSS (uneingeschränkt), SOLLTE (Abweichung nur begründet und dokumentiert), KANN (definiert, in der Methodik unbenutzt; im Kernel 224-mal, durchgängig auf „erhöht"). Bestand der Methodik: 76 MUSS, 19 SOLLTE. Der Standard 300-1 regelt den Umgang mit nicht erfüllten Anforderungen nach dem Modalverb (Kap. 4.1.2). (Kapitel 3.2, 6.1)

**Nicht anwendbar** – Dritter Statuswert des Standards 300-1 neben erfüllt und nicht erfüllt, wenn eine Anforderung „funktional nicht erfüllt werden kann oder die zugrunde liegende Komponente nicht im Informationsverbund existiert", mit Begründungspflicht (Kap. 4.1.1); in der Guidance zu UMS.1.1 nicht vorgesehen, in OSCAL „not-applicable". (Kapitel 6.1)

**Nicht-Konformität** – Abweichung von Anforderungen des ISMS, unabhängig von der Entdeckungsquelle; systematisch zu erfassen, ursachenanalytisch zu bearbeiten (VRB.2). Verhältnis zum Begriff „Fehler" in VRB.4.1: Anhang D. (Kapitel 7.2)

**Parameter** – Belegbare Platzhalter in Statements (`{{…}}`), von der Institution mit konkreten Werten zu füllen (STM.5.1); 15 in der Methodik (Build 2026-10-22), davon neun `{{regelmäßig}}`-Varianten; nach Standard 300-1 „variabel gestaltbare Elemente innerhalb einer Anforderung", die Blaupausen vorgeben dürfen (Kap. 3.5). (Kapitel 3.3)

**Praktik** – Oberste Gliederungseinheit des Katalogs und zugleich Adressat der Anforderungen („Governance und Compliance MUSS …"); fünf Methodik-Praktiken, definiert im Namespace `practices.csv`. (Kapitel 2.1, 2.3)

**Prozessschritt** – Gliederungseinheit des Standards 300-1: Erhebung und Planung, Anforderungsanalyse, Realisierung, Überwachung, kontinuierliche Verbesserung; der Standard nennt keine Control-IDs, die Zuordnung zu den Praktiken ist Auslegung. (Kapitel 2.7)

**Profil (OSCAL Profile)** – Dokumenttyp für Auswahl, Parametrisierung und Anpassung über Katalogen; der Anwenderkatalog entsteht durch Auflösung des Grundschutz++-Profils, Blaupausen sind technisch weitere Profile. (Kapitel 3.8)

**Restrisiko** – Risiko aus nicht umgesetzten Anforderungen; Bewertung im Katalog SOLLTE (UMS.1.2), nach Standard 300-1 Pflicht mit Freigabe durch die Institutionsleitung (Kap. 2.11, 4.1.1, Mindestkriterium 30). (Kapitel 6.1, 9.3)

**Risikoeigentümer** – Rolle aus der Risikomethodik (GC.12.1, Guidance; RISK.1.3 als MUSS); zeichnet laut Guidance zu VRB.5.1 die Freigabe im Umsetzungsplan; nach Standard 300-1 ist es der Geschäftsprozesseigentümer, sofern nichts anderes festgelegt ist (Kap. 4.2.1, Mindestkriterium 16). (Kapitel 4.12, 5.4, 7.5)

**Schutzbedarf** – Zweistufige Einstufung („normal" / „hoch") von Geschäftsprozessen oder Informationen nach Bedeutung für Geschäftsziele oder gesetzlichen Auftrag (GC.7.1.2); „hoch" löst die dedizierte Risikobetrachtung aus (GC.7.2). Eigene Kategorien sind nach Standard 300-1 erlaubt, aber auf die zwei Stufen abzubilden (Kap. 2.6). (Kapitel 4.7)

**sec_level** – Sicherheitsstufe eines Controls: „normal-SdT" oder „erhöht" (Namespace `security_level.csv`); in der Methodik durchgängig „normal-SdT", gesteuert über STM.3.1; „erhöht" bedeutet nach Standard 300-1 das Modalverb KANN und optionale Erfüllung (Kap. 3.4.2). (Kapitel 3.4, 5.3)

**Statement** – Normativer Anforderungssatz eines Controls nach der Satzschablone Praktik + Modalverb + Result + Result-Spezifikation + Action Word. (Kapitel 3.2)

**Temporäre und dauerhafte Nichterfüllung** – Einordnung einer nicht erfüllten SOLLTE-Anforderung nach Standard 300-1: temporär, wenn die Erfüllung zu einem absehbaren Zeitpunkt vorgesehen ist (Begründung, keine Risikobetrachtung); dauerhaft, wenn sie auf absehbare Zeit oder endgültig unterbleibt (Risikobetrachtung nach Anhang 3, Freigabe der Restrisiken durch die Leitung) (Kap. 4.1.2). Im Katalog nicht vorgesehen. (Kapitel 6.1)

**Umsetzungsplan** – Gemeinsames Steuerungsdokument von UMS und VRB für alle Maßnahmen samt Zuständigen, Fristen, Prioritäten und Risiken; Gegenstück zum alten *Realisierungsplan*; Mindestangaben je Maßnahme nach Standard 300-1, Kap. 4.3. (Kapitel 6.2, 7.5)

**Umsetzungsstatus** – Im Katalog binäre Feststellung je Anforderung: umgesetzt oder nicht umgesetzt, umgesetzt nur, wenn auch alle abhängigen Anforderungen umgesetzt sind (UMS.1.1, Guidance); im Standard 300-1 dreiwertig: erfüllt, nicht erfüllt, nicht anwendbar (Kap. 4.1.1). (Kapitel 6.1)

**Vererbung** – Deterministische Erweiterung der Zielobjektkategorie-Zuordnung eines Assets um alle Elternknoten der Zielobjekthierarchie (STM.2.1.4.1); automatisierbar und zur Automatisierung empfohlen. (Kapitel 5.2)

**Verbundweite Anforderungen** – Die Anforderungen der ISMS-Praktiken, die ohne Selektion einmalig auf den gesamten Informationsverbund modelliert werden (STM.2.1.1, Guidance). (Kapitel 5.2)

**Wirksamkeitsprüfung** – Test, ob umgesetzte Korrektur- und Verbesserungsmaßnahmen ihre Wirkung erreichen (VRB.6.1 MUSS), samt bewertendem Verfahren darüber (VRB.6.2 SOLLTE). (Kapitel 7.6)

**Zielobjektkategorie** – Standardisierte Klasse, über die Kernel-Anforderungen an Assets modelliert werden; 39 Kategorien mit Hierarchie im Namespace `target_object_categories.csv`, im Standard 300-1 in Anhang 1 definiert (drei Namen weichen ab); funktionaler Nachfolger der Bausteine; in der Methodik selbst nicht belegt. (Kapitel 3.7, 5.2)

---

*Ende Anhang C (v0.4). Fehlende Begriffe bitte mit Fundstelle nachmelden.*
