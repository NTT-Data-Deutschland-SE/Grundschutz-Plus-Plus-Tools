# Kapitel 6: UMS – Umsetzung

**Handbuch zur Grundschutz++ Methodik · Kapitel-Version 0.9 (Entwurf)**
Stand: 2026-10-26 · Normative Basis: `BSI-Methodik-Grundschutz++-catalog.json`, Build 2026-10-22; BSI-Standard 300-1 (Version 1.0, 20.10.2026) · Gliederungsbezug: Kapitel 6 gemäß `00_gliederung_v0.1.md`
Änderung 0.9: Standard 300-1 eingearbeitet: dreiwertiger Umsetzungsstatus und Bewertung fehlender Umsetzungen nach Modalverb in 6.1, Mindestfelder und Nachweise des Umsetzungsplans in 6.2, Leitungsfreigabe und Rollentrennung in 6.3 bis 6.6, Ausnahmemanagement in 6.5 neu gefasst (keine Ausnahme von MUSS-Anforderungen), offene Fragen aktualisiert.

## 6.0 Einordnung: wo das Anforderungspaket Arbeit wird

Die Umsetzung (UMS) ist die Do-Phase der Methodik und mit elf Controls die kompakteste der fünf Praktiken: 10 MUSS, 1 SOLLTE, und nur die Restrisiko-Bewertung (UMS.1.2) trägt einen `effort_level` über null (Stufe 2). Ihr Leitdokument ist der Umsetzungsplan, an dem sechs der elf Controls hängen; er ist das Grundschutz++-Gegenstück zum Realisierungsplan (Referenzdokument A.6) der alten Welt und zugleich das Bindeglied zu PERF (Evaluation des Umsetzungsplans, PERF.1.2) und VRB (Fortschreibung, VRB-Bezug auf denselben Plan).

Die Praktik folgt einer schlichten Logik: Status feststellen (UMS.1), Maßnahmen planen und priorisieren (UMS.2), Zuständige benennen (UMS.3), Fristen setzen (UMS.4), Ausnahmen regeln (UMS.5), Fortschritt verfolgen und den Plan fortschreiben (UMS.6), Compliance im Prozess halten (UMS.7). Das liest sich wie solides Projektmanagement, und genau das ist der Punkt: Grundschutz++ verlangt hier keine Sicherheitsmagie, sondern nachweisbare Arbeitsorganisation. Die eine wirklich harte methodische Entscheidung steckt im Statusmodell, und sie verdient die ersten Kästen des Kapitels.

Im Standard 300-1 heißt die Praktik „Prozessschritt 3 – Realisierung" (Standard 300-1, Kap. 4 (S. 18 bis 21)): Ermittlung und Bewertung des Umsetzungsstatus, Durchführung der Risikobetrachtung (im Katalog STM.4.1, Kapitel 5.4), Umsetzungsplanung und Priorisierung, Zuständigkeiten und Fristen, Fortschrittsverfolgung. Von den sieben Stellen, an denen Standard und Katalog-Build auseinanderliegen (Kapitel 2.7), treffen drei diese Praktik: der Umsetzungsstatus, die Ausnahmen und das Restrisiko.

## 6.1 UMS.1 Umsetzungsstatus: ja, nein, und nach dem Standard nicht anwendbar

**Anforderungsbezug.**

| Control | Verbindlichkeit | Kern | Dokument |
|---|---|---|---|
| UMS.1.1 Ermittlung des Umsetzungsstatus | MUSS | Umsetzungsstatus aller Anforderungen im Paket vollständig `{{regelmäßig}}` überprüfen | keines zugeordnet |
| UMS.1.2 Bewertung des Restrisikos | SOLLTE | Restrisiko durch nicht umgesetzte Anforderungen festlegen | keines zugeordnet |

> „Umsetzung MUSS den Umsetzungsstatus der Anforderungen im Anforderungspaket vollständig `{{regelmäßig}}` überprüfen." (UMS.1.1)

Die Guidance dazu ist die vielleicht folgenreichste Einzelaussage der Praktik: Der Status kann nur „umgesetzt" oder „nicht umgesetzt" sein, und eine Anforderung gilt erst dann als umgesetzt, wenn sie selbst und alle in Abhängigkeit stehenden Anforderungen umgesetzt sind.

> **Abweichung zu 200-2:** Der IT-Grundschutz-Check nach 200-2 kennt vier Umsetzungsstatus: „entbehrlich", „ja", „teilweise", „nein". Grundschutz++ kennt in der Guidance zu UMS.1.1 genau zwei: umgesetzt oder nicht umgesetzt. „Teilweise" entfällt ersatzlos, eine teilweise umgesetzte Anforderung ist nicht umgesetzt. „Entbehrlich" entfällt im Katalog als Status und wandert als Entscheidung nach vorn in die Modellierung (STM.2.1.5, Streichung mit dokumentierter Begründung); der Standard 300-1 holt es als „nicht anwendbar" in den Status zurück (Kasten unten). Wer sein altes GS-Check-Tooling weiterbenutzt, importiert ein Statusmodell, das weder Katalog noch Standard so kennen.

> **Standard 300-1 und Katalog-Build 2026-10-22: drei Statuswerte.** Der Standard legt fest: „Für jede Anforderung muss der aktuelle Umsetzungsstatus vollständig überprüft werden", und der Status hat drei Werte, „erfüllt" („ja"), „nicht erfüllt" („nein") und „nicht anwendbar": „Eine Anforderung kann als ‚nicht anwendbar' gelten, wenn die Anforderung funktional nicht erfüllt werden kann oder die zugrunde liegende Komponente nicht im Informationsverbund existiert. Für jede ‚nicht anwendbare' Anforderung ist eine Begründung zu dokumentieren." (Standard 300-1, Kap. 4.1.1 (S. 18)). Der Katalog sagt in der Guidance zu UMS.1.1 „grundsätzlich nur ‚umgesetzt' (‚ja') oder ‚nicht umgesetzt' (‚nein')". Zwei Folgen: Der dritte Wert ersetzt die Streichung aus STM.2.1.5 (Kapitel 5.2), und der Standard sagt „erfüllt", wo der Katalog „umgesetzt" sagt; beide Begriffe meinen dasselbe (Anhang D, D45). Erwartete Katalogänderung: Guidance zu UMS.1.1 mit drei Werten. Bis dahin führen Sie den dritten Wert mit Begründung, denn der Standard verlangt ihn, und der Katalog schließt ihn an keiner normativen Stelle aus (Anhang D, D38).

Die Festlegung des Katalogs reicht bis in die OSCAL-Dokumentation: Von den Statuswerten, die OSCAL für die Umsetzung vorsieht, nutzt das BSI nur „implemented" für umgesetzt; alles andere bleibt leer und bedeutet nicht umgesetzt, denn ein ausdrückliches „nein" kennt OSCAL nicht (Kapitel 3.9; die Festlegung ist in den Repository-Quellen bislang nicht dokumentiert, Anhang D, D32). Für den dritten Wert des Standards hat OSCAL „not-applicable" im Angebot, die Werkzeugsammlung führt ihn als „N/A"; dass der Standard diesen Wert deckt, ist Auslegung, denn zu OSCAL sagt er nichts.

Wie die Nichtanwendbarkeit technisch zu vollziehen ist, sagen weder Katalog noch Standard. OSCAL kennt zwei Orte: das Profil (die Anforderung wird gar nicht erst importiert) und den System-Sicherheitsplan (das Control trägt den Status „not-applicable"). Der SSP-Generator der Werkzeugsammlung arbeitet bisher nach dem Profilweg, er erzeugt ein institutionsspezifisches Profil mit Positivliste (include-controls mit with-ids) und baut den System-Sicherheitsplan darauf auf, gestrichene Anforderungen erscheinen dort also nie; das passt zur Streichung aus STM.2.1.5, und die OSCAL-FAQ des Repositories nennt das Entfernen nicht anwendbarer Anforderungen ausdrücklich als Zweck von Profilen. Der Standard verlangt die Aufnahme aller kategorielosen Anforderungen und die Begründung am Status, und das ist der SSP-Weg. Für den Ablageort der Begründung ist in beiden Fällen nichts geregelt (Anhang D, D33).

**Bewertung fehlender Umsetzungen nach Modalverb.** Was mit einer nicht erfüllten Anforderung geschieht, regelt der Standard nach ihrem Modalverb (Standard 300-1, Kap. 4.1.1 und 4.1.2 (S. 18 f.)); der Katalog hat dafür kein Control. KANN-Anforderungen „müssen nicht unbedingt berücksichtigt werden", sie sind optional. Jede nicht erfüllte SOLLTE-Anforderung ist als temporär oder dauerhaft einzuordnen: temporär, wenn die Erfüllung vorgesehen ist und „zu einem absehbaren späteren Zeitpunkt erfolgen soll", mit stichhaltiger Begründung zu dokumentieren und ohne Risikobetrachtung; dauerhaft, wenn die Anforderung „auf absehbare Zeit oder endgültig nicht erfüllt wird", dann ist eine Risikobetrachtung nach Anhang 3 auszuführen (Mindestkriterium 34) und die verbleibenden Restrisiken sind der Institutionsleitung zur Freigabe vorzulegen (Kriterium 30). Für noch nicht erfüllte, aber im Umsetzungsplan vorgesehene Anforderungen gilt zusätzlich: Das noch nicht mitigierte Risiko ist „zu identifizieren und an die Institutionsleitung mitzuteilen", und es „muss von der Institutionsleitung getragen werden" (Kap. 4.1.1); für SOLLTE-Anforderungen in diesem Zustand verlangt Kap. 2.11 (S. 11) eine „Restrisikobetrachtung" mit Freigabe durch die Leitung. MUSS-Anforderungen sind verpflichtend, für jede nicht erfüllte sind Maßnahmen festzulegen: „Die Durchführung einer Risikobetrachtung kann die Erfüllung einer MUSS-Anforderung nicht ersetzen. Eine Ausnahmegenehmigung oder Risikoakzeptanz ist nicht möglich." Häufen sich dauerhafte Nichterfüllungen von SOLLTE-Anforderungen, „könnte eine erhebliche Abweichung festgestellt werden" (Kap. 4.1.2 (S. 19)). Die Begriffe temporär und dauerhaft definiert der Standard nur über diese Sätze, und die Restrisikobetrachtung aus Kap. 2.11 ist von der Risikobetrachtung aus Kap. 4.1.2 nur dem Namen nach unterschieden (Anhang D, D46).

**Umsetzungshinweise.** Das binäre Modell des Katalogs nimmt dem Schönfärben die Grundlage, und der dritte Wert des Standards ändert daran nichts, denn „nicht anwendbar" braucht eine Begründung; der vertraute Ausweg „teilweise", mit dem sich halbfertige Maßnahmen jahrelang tragen ließen, fehlt in beiden. Das hat allerdings zwei ernste Kosten. Erstens gehen Nuancen verloren: „Teilweise" trug Information, nämlich dass begonnen wurde, wie weit die Umsetzung gediehen ist und was noch fehlt. Im binären Status ist eine zu neunzig Prozent fertige Maßnahme von einer unbegonnenen nicht zu unterscheiden; die Dokumentation wird an dieser Stelle schlechter, nicht besser. Diese Information muss anderswo überleben, realistisch im Umsetzungsplan mit Maßnahmenständen und Restarbeiten (UMS.2, UMS.6), sonst ist sie weg. Zweitens ist die leere Angabe doppeldeutig: Sie steht für „geprüft und nicht umgesetzt" ebenso wie für „noch gar nicht bearbeitet"; die Werkzeuge der Bibliothek zeigen die leere Angabe folgerichtig als „Offen" an. Aus der Statusliste selbst ist damit nicht ablesbar, ob die Erhebung vollständig war; 200-2 konnte genau das mit dem ausdrücklichen „nein" vom fehlenden Eintrag unterscheiden. Wer die Vollständigkeit der Erhebung belegen will, braucht einen Vermerk außerhalb des Status, etwa ein Erhebungsdatum je Anforderung. Nehmen Sie außerdem die Abhängigkeitsregel ernst: Sie brauchen eine gepflegte Sicht darauf, welche Anforderungen voneinander abhängen, sonst ist „umgesetzt" nicht belastbar feststellbar (wo diese Abhängigkeiten herkommen, ist eine offene Frage, siehe Abschnitt 6.9). Setzen Sie den Parameter `{{regelmäßig}}` realistisch; er ist das vereinbarte Prüfintervall, an dem Sie gemessen werden. Die Restrisiko-Bewertung nach UMS.1.2 ist im Katalog SOLLTE; der Standard macht sie zur Pflicht, samt Freigabe durch die Institutionsleitung (oben, Anhang D, D41), und die Guidance zeigt den Zweck: konsolidiert aufbereitet macht sie die Lücken für die Leitung nachvollziehbar, und genau dort gehören sie hin.

**Audit-Perspektive.** Die Statusliste übernimmt die Rolle des Referenzdokuments A.4 (Ergebnis des IT-Grundschutz-Checks). Übertragen aus dem Auditierungsschema kommt eine Verschärfung hinzu: Das Schema behandelt nicht umgesetzte Anforderungen so, dass die entstehenden Risiken bewertet, der Leitungsebene transparent dargestellt und von dieser per Unterschrift oder elektronischer Freigabe getragen werden müssen. Im Katalog ist die Restrisiko-Bewertung nur SOLLTE; der Standard 300-1 hat die Spannung aufgelöst und verlangt Restrisikobetrachtung und Leitungsfreigabe (Kap. 2.11, 4.1.1), der Katalog muss nachziehen (Abschnitt 6.9). Praktisch heißt das: Wer UMS.1.2 auslässt, mag sich auf das SOLLTE des Katalogs berufen, verstößt aber gegen den Standard und wird im Zertifizierungsverfahren die Risikoübernahme der Leitung nachweisen müssen. Ein Vor-Ort-Klassiker bleibt der Stichprobenabgleich: Status „umgesetzt" auf dem Papier gegen die Realität am System.

**Typische Fehler.** Der Status wird einmal vor dem Audit erhoben statt `{{regelmäßig}}`. Halbfertige Maßnahmen werden als umgesetzt geführt, weil das alte „teilweise" im Kopf weiterlebt. Abhängigkeiten sind nirgends erfasst, sodass Anforderungen als erledigt gelten, deren Voraussetzungen fehlen. Und das Restrisiko existiert als Excel-Liste beim ISB, die die Leitung nie gesehen hat.

## 6.2 UMS.2 Umsetzungsplanung: aus dem Paket wird ein Plan

**Anforderungsbezug.**

| Control | Verbindlichkeit | Kern | Dokument |
|---|---|---|---|
| UMS.2.1 Umsetzungsplanung | MUSS | Maßnahmen für nicht umgesetzte Anforderungen gemäß strukturierter Vorgehensweise festlegen | Umsetzungsplan |
| UMS.2.2 Priorisierung von Maßnahmen | MUSS | Priorisierung auf Basis von Risikobewertung, Abhängigkeiten und Ressourcenverfügbarkeit festlegen | Umsetzungsplan |

Das Ergebnis beschreibt die Guidance zu UMS.2.1 als Überführung „des unstrukturierten Anforderungspakets hin zu einem strukturierten Umsetzungsplans" [sic]. Der Hebel dabei: Maßnahmen und Anforderungen sind nicht eins zu eins; eine gute Maßnahme deckt mehrere Anforderungen zugleich ab, und die Guidance verlangt ausdrücklich, solche Synergien zu suchen.

Der Standard 300-1 füllt den Plan mit Mindestangaben (Standard 300-1, Kap. 4.3 (S. 20)): Jede Maßnahme ist mit den Anforderungen zu verknüpfen, die sie adressiert, bei mehreren mit allen; Abhängigkeiten zwischen Anforderungen und Maßnahmen sind kenntlich zu machen; je Maßnahme sind mindestens „die zugehörige Anforderung", „das Datum der Umsetzung oder Überprüfung" und „die dokumentierende beziehungsweise prüfende Person" festzuhalten. Nachweise sind der Maßnahme eindeutig zuzuordnen; bei automatisierter Überprüfung sind „das eingesetzte Tool, der Zeitpunkt der Prüfung und das ermittelte Prüfergebnis" zu dokumentieren und erzeugte Prüfberichte der Maßnahme und Anforderung zuzuordnen. Änderungen an Zuordnung, Umsetzungsstand oder Prüfergebnis sind nachzuziehen, eine Historie mit Zeitpunkt, verantwortlicher Person und Tool wird empfohlen. Für die Priorisierung nennt der Standard Aufwand, Synergien, Risikohöhe, strategische Bedeutung und Quick-Wins und empfiehlt, „die Anforderungen der Elternknoten im Anforderungspaket in der Umsetzung zu priorisieren". Die Guidance zu VRB.5.1 und RISK.1.10 beschreibt eine längere Feldliste (Kapitel 7.5); der Standard ist das Minimum, die Guidance das Maximum, und beides gehört in dieselbe Spaltendefinition (Anhang D, D47).

**Umsetzungshinweise.** Denken Sie in Maßnahmen, nicht in Anforderungszeilen. Ein zentrales Patch- und Härtungsprojekt, eine MFA-Einführung oder ein Berechtigungskonzept erledigen jeweils Dutzende Anforderungszeilen; der Umsetzungsplan sollte diese Bündelung abbilden, mit Rückverweis auf die abgedeckten Control-IDs. Für die Priorisierung nennt das Statement drei Kriterien (Risikobewertung, Abhängigkeiten, Ressourcenverfügbarkeit), die Guidance ergänzt gesetzliche Verpflichtungen und Umsetzungsaufwand. Aus der Beratungspraxis: Priorisieren Sie zuerst nach Risiko und gesetzlicher Pflicht, dann nach Aufwand, und dokumentieren Sie die Reihenfolge-Entscheidung; ein Plan, dessen Reihenfolge niemand begründen kann, ist im Audit nur eine Liste.

**Audit-Perspektive.** Der Umsetzungsplan ist das A.6-Gegenstück und wird auf zwei Dinge geprüft: Vollständigkeit (findet sich jede nicht umgesetzte Anforderung aus UMS.1.1 im Plan wieder?) und Begründbarkeit der Priorisierung gegen die genannten Kriterien. Eine nicht umgesetzte Anforderung, die in keinem Plan auftaucht, ist der direkte Weg zur Abweichung, denn dann fehlt der Nachweis, dass die Institution ihre Lücken überhaupt steuert.

**Typische Fehler.** Der Plan ist eine umbenannte Kopie der Statusliste, ohne Maßnahmenbündelung und ohne Prioritäten. Die Priorisierung folgt der Lautstärke der Fachbereiche statt der Risikobewertung. Quick Wins werden abgearbeitet, während die unbequemen Hochrisiko-Maßnahmen seit drei Planversionen auf „Q4" stehen.

## 6.3 UMS.3 Umsetzungszuständige: eindeutig heißt eine

**Anforderungsbezug.**

| Control | Verbindlichkeit | Kern | Dokument |
|---|---|---|---|
| UMS.3.1 Benennung von Umsetzungszuständigen | MUSS | Zuständige für die Umsetzung nicht erfüllter Anforderungen eindeutig zuweisen | Umsetzungsplan |

Die Guidance verlangt Kompetenzen und Ressourcen bei den Zugewiesenen, Abstimmung mit den betroffenen Bereichen für Akzeptanz, und erlaubt bei komplexeren Maßnahmen die Trennung in fachliche und operative Verantwortung samt Teilaufgaben. Der Standard 300-1 sagt dasselbe und ergänzt, dass Zuständigkeiten und Fristen „in geeigneter Form dokumentiert werden" sollten, etwa in einem Projektmanagement- oder Ticketsystem, und dass das Vorgehen von der Institutionsleitung freizugeben ist, „da diese die erforderlichen Ressourcen bereitstellen muss" (Standard 300-1, Kap. 4.4 (S. 21)).

**Umsetzungshinweise.** „Eindeutig" ist das Schlüsselwort: pro Maßnahme genau eine verantwortliche Rolle, keine Gremien, keine Doppelspitzen ohne Klärung, wer entscheidet. Die Trennung fachlich/operativ aus der Guidance ist in der Praxis Gold wert, etwa Fachverantwortung beim Prozesseigner, operative Umsetzung beim Systembetrieb. Und weisen Sie niemandem eine Maßnahme zu, der weder Budget noch Zugriff hat; die Guidance nennt Kompetenzen und Ressourcen nicht zur Zierde.

**Audit-Perspektive.** Schnell geprüft: Spalte „Zuständig" im Umsetzungsplan, Stichprobe im Interview („Wussten Sie, dass Sie diese Maßnahme verantworten?"). Zuständige, die von ihrer Zuständigkeit nichts wissen, sind eine der ergiebigsten Vor-Ort-Feststellungen überhaupt.

**Typische Fehler.** Zuständig ist „die IT". Zuständig ist der ISB, für alles, womit UMS.3.1 formal erfüllt und praktisch beerdigt ist. Personen statt Rollen, und nach dem nächsten Weggang zeigt der halbe Plan auf ein verwaistes Postfach.

## 6.4 UMS.4 Umsetzungsfristen: Termine, die gehalten werden müssen

**Anforderungsbezug.**

| Control | Verbindlichkeit | Kern | Dokument |
|---|---|---|---|
| UMS.4.1 Festlegung von Umsetzungsfristen | MUSS | realistisches Zieldatum für nicht umgesetzte Anforderungen festlegen | Umsetzungsplan |

Die Guidance verlangt dreierlei: Das Zieldatum berücksichtigt Umfang, Ressourcen und Abhängigkeiten; die Einhaltung wird nachgehalten; bei Überschreitung werden geeignete Maßnahmen eingeleitet.

**Umsetzungshinweise.** „Realistisch" schützt vor dem verbreiteten Reflex, alle Fristen auf das Audit-Datum zu legen. Planen Sie gegen Kapazität, nicht gegen Wunsch, und definieren Sie vorab, was bei Fristriss passiert: Eskalation an wen, Neubewertung wann, gegebenenfalls Aussprung in die Risikobetrachtung nach STM.4.1, wenn aus dem Verzug eine dauerhafte Nichtumsetzung wird. Fristen ohne Konsequenzmechanismus sind Dekoration.

**Audit-Perspektive.** Der Auditor liest die Fristenhistorie: Wie oft wurden Termine verschoben, gibt es Nachweise für die eingeleiteten Maßnahmen bei Überschreitung. Ein Plan, in dem dieselbe Maßnahme dreimal kommentarlos verschoben wurde, belegt das Gegenteil von „nachgehalten" und liefert die Abweichung gleich mit Begründung.

**Typische Fehler.** Sammeltermine („alles bis Jahresende"), die niemand ernst nimmt. Verschiebungen ohne Entscheidung und ohne Spur. Fristen, die nur der ISB kennt, während die Zuständigen aus UMS.3.1 nie eingebunden wurden.

## 6.5 UMS.5 Ausnahmemanagement: der geregelte Weg am Soll vorbei, außer bei MUSS

**Anforderungsbezug.**

| Control | Verbindlichkeit | Kern | Dokument |
|---|---|---|---|
| UMS.5.1 Autorisierung von Ausnahmen | MUSS | Ausnahmegenehmigungen durch `{{eine zuständige Person oder Rolle}}` autorisieren | keines zugeordnet |
| UMS.5.2 Dokumentation von Ausnahmen | MUSS | Ausnahmegenehmigungen mit Begründung dokumentieren | Freigegebene Ausnahmegenehmigung |

UMS.5.1 adressiert laut Guidance Zielkonflikte zwischen Verpflichtungen: Wo Anforderungen kollidieren, wird abgewogen und die Ausnahme von der parametrisierten zuständigen Stelle autorisiert, gestützt auf eine Risikobetrachtung, wo nötig; ob die Nicht-Umsetzung einer Anforderung eine Risikobetrachtung erfordert, ist laut Guidance zu prüfen. UMS.5.2 verlangt die dokumentierte Begründung, und die Guidance ist erfreulich modern: Die Dokumentation darf in die Geschäftsprozesse integriert werden, ausdrücklich genannt werden CMDBs, Aktenverzeichnisse, Commit-Messages und Ticketsysteme.

> **Standard 300-1 und Katalog-Build 2026-10-22: keine Ausnahme von MUSS.** Der Standard zieht eine Grenze, die der Katalog nicht kennt: „MUSS-Anforderungen sind verpflichtend. Für nicht erfüllte MUSS-Anforderungen sind Maßnahmen zu deren Erfüllung festzulegen. Die Durchführung einer Risikobetrachtung kann die Erfüllung einer MUSS-Anforderung nicht ersetzen. Eine Ausnahmegenehmigung oder Risikoakzeptanz ist nicht möglich." (Standard 300-1, Kap. 4.1.2 (S. 19)). Das Wort „Ausnahmegenehmigung" verwendet der Standard an genau einer weiteren Stelle, in Mindestkriterium 27 (S. 38): Ein Risiko, das die Risikoakzeptanzkriterien nicht erfüllt und trotzdem nicht weiter behandelt werden soll, „ist durch die Institutionsleitung zu autorisieren". Die Ausnahme ist damit eine Leitungsentscheidung über ein Risiko, und ihr Gegenstand ist eine SOLLTE-Anforderung in dauerhafter Nichterfüllung oder ein Restrisiko (Abschnitt 6.1). Die Guidance zu UMS.5.1 und zu STM.4.1 spricht dagegen ohne Modalverb-Bezug von Ausnahmen und von der „Nicht-Umsetzung von Anforderungen". Die Lesart früherer Fassungen dieses Handbuchs, UMS.5 decke auch MUSS-Anforderungen, ist damit überholt; die Frage, ob UMS.5.1 mit „Verpflichtungen" nur Compliance-Verpflichtungen aus GC.3 oder auch Katalog-Anforderungen meint, bleibt für SOLLTE-Anforderungen offen (Anhang D, D9, D40). Erwartete Katalogänderung: Guidance zu UMS.5.1 mit Modalverb-Bezug und Verweis auf die Risikoakzeptanz durch die Leitung.

**Umsetzungshinweise.** Definieren Sie den Ausnahmeprozess, bevor die erste Ausnahme gebraucht wird, und zwar für das, was der Standard ausnehmbar lässt: Zielkonflikte zwischen Verpflichtungen, dauerhaft nicht erfüllte SOLLTE-Anforderungen und Risiken außerhalb der Akzeptanzkriterien. Der Prozess braucht Antrag, Risikobetrachtung nach Anhang 3 des Standards (bei dauerhafter SOLLTE-Nichterfüllung Pflicht, Mindestkriterium 34), Autorisierungsinstanz (Parameter setzen, konsistent mit GC.9; für Restrisiken und Ausnahmen nach Kriterium 27 ist es die Institutionsleitung), Befristung (Kriterium 28 verlangt sie für temporär akzeptierte Risiken) und Wiedervorlage. Befristen Sie jede Ausnahme; unbefristete Ausnahmen sind keine Ausnahmen, sondern stillschweigende Regeländerungen. Eine nicht erfüllte MUSS-Anforderung bekommt eine Maßnahme im Umsetzungsplan, keinen Antrag; bis zur Umsetzung ist das Risiko der Leitung mitzuteilen, und sie trägt es (Kap. 4.1.1). Die Erlaubnis zur integrierten Dokumentation sollten technische Teams nutzen: Eine begründete Ausnahme in der Commit-Message oder im Ticket ist auffindbarer als ein Formular im Laufwerk, solange die Fundstelle im ISMS referenziert ist.

**Audit-Perspektive.** Das Dokument „Freigegebene Ausnahmegenehmigung" ist die Evidenz; geprüft wird die Kette Antrag, Begründung, Risikobetrachtung, Autorisierung durch die parametrisierte Stelle beziehungsweise die Leitung, Befristung. Ausnahmen, die faktisch gelebt, aber nie autorisiert wurden, sind keine Ausnahmen, sondern nicht umgesetzte Anforderungen ohne Steuerung, und genau so wird der Auditor sie werten. Eine „Ausnahme" von einer MUSS-Anforderung ist nach dem Standard eine nicht erfüllte MUSS-Anforderung ohne Maßnahme, also der Kandidat für die schwerwiegende Abweichung (Kapitel 9.3).

**Typische Fehler.** Die Autorisierungsinstanz ist nie parametrisiert worden, also autorisiert de facto der ISB sich selbst. Ausnahmen ohne Enddatum sammeln sich über Jahre. Die Begründung lautet „aus betrieblichen Gründen" und erklärt nichts. MUSS-Anforderungen werden per Ausnahmeformular „geregelt", und erst der Auditor erklärt, dass der Standard das ausschließt. Verstreute Dokumentation ohne zentrales Register, sodass niemand sagen kann, wie viele Ausnahmen aktuell gelten.

## 6.6 UMS.6 Umsetzungsfortschrittsverfolgung: der Plan lebt

**Anforderungsbezug.**

| Control | Verbindlichkeit | Kern | Dokument |
|---|---|---|---|
| UMS.6.1 Nachverfolgung des Umsetzungsfortschritts | MUSS | Verfahren für die Nachverfolgung der Maßnahmenumsetzung verankern | Umsetzungsplan |
| UMS.6.2 Fortschreibung des Umsetzungsplans | MUSS | Verfahren zur Fortschreibung des Umsetzungsplans verankern | Umsetzungsplan |

Die Guidance zu UMS.6.1 empfiehlt einen vollständigen Verfolgungszyklus von Planung und KPI-Definition über Status-Reporting und Soll-Ist-Vergleiche bis zu Ursachenanalyse, Korrekturmaßnahmen und Lessons Learned. UMS.6.2 hält den Plan aktuell: Zeitpläne und Ressourcen anpassen, Prioritäten neu bewerten, neue Maßnahmen ergänzen, obsolete streichen und, bemerkenswert, die Erkenntnisse aus der Wirksamkeitsprüfung integrieren, womit der Katalog die Brücke zu VRB.6 schlägt. Der Standard 300-1 verlangt die kontinuierliche Nachverfolgung und eine Rollentrennung: Ein Interessenkonflikt „zwischen der für die Umsetzung und der für die Fortschrittsverfolgung zuständigen Person ist durch eine angemessene Rollenverteilung zu verhindern"; als Elemente nennt er ein Verfahren, die Dokumentation von Stand und Abweichungen, die frühe Erkennung von Hindernissen, Eskalationspfade, regelmäßige Statusberichte bis in den Managementbericht und die Anpassung des Plans als „lebendes Dokument" (Standard 300-1, Kap. 4.5 (S. 21)).

**Umsetzungshinweise.** Beide Controls verlangen Verfahren, nicht Heldentaten: ein fester Berichtstakt, ein Soll-Ist-Vergleich gegen die Fristen aus UMS.4.1, eine definierte Eingangstür für Änderungen am Plan. Wer den Umsetzungsplan in einem Ticketsystem oder ISMS-Tool führt, bekommt Nachverfolgung und Fortschreibung fast geschenkt; wer ihn als Dokument führt, braucht Disziplin und Versionierung nach GC.11.1. Entscheidend ist die Rückkopplung: Statusergebnisse aus UMS.1.1 und Wirksamkeitsbefunde aus VRB.6 müssen den Plan tatsächlich verändern, sonst ist die Fortschreibung Fassade.

**Audit-Perspektive.** Die Versionshistorie des Umsetzungsplans erzählt dem Auditor die Wahrheit über die Praktik: Ein Plan mit lebendiger Änderungshistorie, nachvollziehbaren Neubewertungen und integrierten Prüfergebnissen belegt ein funktionierendes Verfahren; ein Plan mit Stand vom letzten Audit belegt das Gegenteil, und zwar für UMS.6.1 und UMS.6.2 gleichzeitig.

**Typische Fehler.** Das Reporting misst Aktivität („80 Prozent der Tickets bearbeitet") statt Wirkung. Der Plan wird nur vor Audits aktualisiert. Erkenntnisse aus Wirksamkeitsprüfungen und Vorfällen landen in Protokollen, aber nie im Plan.

## 6.7 UMS.7 Compliance-Management: die Pflicht bleibt im Prozess

**Anforderungsbezug.**

| Control | Verbindlichkeit | Kern | Dokument |
|---|---|---|---|
| UMS.7.1 Wahrung von Compliance in der Umsetzung | MUSS | Verfahren zur Überprüfung von Compliance im Umsetzungsprozess verankern | Compliance-Verpflichtungen |

Die Guidance verlangt die regelmäßige Überprüfung und Aktualisierung der compliance-bezogenen Prozesse und Anweisungen, damit sie bei sich ändernder Regulierung wirksam bleiben, und nennt Prüflisten oder Auditierung als geeignete Verfahren.

**Umsetzungshinweise.** Das ist das Umsetzungs-Gegenstück zu GC.3: Dort wird erfasst, was gilt; hier wird geprüft, dass die Umsetzung es einhält. Praktisch genügt eine Compliance-Spalte im Umsetzungsplan plus eine Prüfliste je einschlägiger Verpflichtung, angewendet bei Maßnahmenabschluss. Wichtig ist der Aktualisierungspfad: Ändert sich eine Verpflichtung im Kataster (GC.3.1), müssen die betroffenen Maßnahmen und Anweisungen nachgezogen werden; verankern Sie diesen Trigger explizit.

**Audit-Perspektive.** Geprüft wird am Beispiel: Der Auditor nimmt eine Verpflichtung aus dem Kataster und verfolgt sie bis in die umgesetzte Maßnahme. Reißt die Kette (Verpflichtung erfasst, aber in keiner Maßnahme berücksichtigt), steht der Verdacht im Raum, dass das Compliance-Management aus GC.3 ein Papiertiger ist; die Feststellung trifft dann beide Praktiken.

**Typische Fehler.** Compliance wird bei der Planung einmal bedacht und bei Änderungen der Rechtslage nie wieder. Die Prüfliste existiert, wird aber nur bei Neuprojekten angewendet, nicht im Bestand.

## 6.8 Dokumenten-Output der Praktik

| Dokument | Gefordert durch |
|---|---|
| Umsetzungsplan | UMS.2.1, UMS.2.2, UMS.3.1, UMS.4.1, UMS.6.1, UMS.6.2 |
| Freigegebene Ausnahmegenehmigung | UMS.5.2 |
| Compliance-Verpflichtungen | UMS.7.1 |

Drei Controls fordern kein Dokument (UMS.1.1, UMS.1.2, UMS.5.1). Gerade beim Umsetzungsstatus ist das bemerkenswert: Die Statusliste, funktional das A.4-Gegenstück und eine der wichtigsten Auditevidenzen, hat im Katalog kein zugeordnetes Dokument. In der Praxis gehört sie als Bestandteil oder Anlage zum Umsetzungsplan, gelenkt nach GC.11.1; die fehlende Zuordnung steht in Abschnitt 6.9.

## 6.9 Offene Fragen und Katalogfunde

1. **Woher kommen die Abhängigkeiten?** UMS.1.1 macht die Umsetzung einer Anforderung von „allen in Abhängigkeit stehenden Anforderungen" abhängig, aber der Methodik-Teil des Katalogs enthält kein Feld, das solche Abhängigkeiten definiert. Die Control-Verschachtelung scheidet als Quelle aus, denn sie ist rein thematische Gruppierung (Kapitel 3.1); offen bleibt, ob OSCAL-`links` im Kernel oder institutionsindividuelle Festlegungen gemeint sind. *Teilweise beantwortet:* Der Standard 300-1 verlangt, Abhängigkeiten zwischen Anforderungen und Maßnahmen im Umsetzungsplan kenntlich zu machen (Kap. 4.3 (S. 20)), und der Namespace definiert in `dependency.txt` die Abhängigkeit als zwingende Reihenfolge; welche Datenquelle die Abhängigkeiten liefert, bleibt offen (Anhang D, D3).
2. **Restrisiko nur SOLLTE.** UMS.1.2 stuft die Restrisiko-Bewertung als SOLLTE ein, während das Auditierungsschema (Abschnitt 4.5) für nicht umgesetzte Anforderungen die Risikodarstellung gegenüber der Leitungsebene und deren dokumentierte Risikoübernahme verlangt. *Durch den Standard 300-1 entschieden:* Restrisikobetrachtung und Freigabe durch die Institutionsleitung sind Pflicht (Kap. 2.11, 4.1.1, Mindestkriterium 30); UMS.1.2 (SOLLTE) und der nicht importierte RISK.1.9 (SOLLTE) hinken hinterher. Erwartete Katalogänderung (Anhang D, D4, D41).
3. **Kein Dokument für den Umsetzungsstatus.** UMS.1.1 ohne `documentation`-Prop, obwohl die Statusliste zentrale Auditevidenz ist (vgl. Abschnitt 6.8).
4. **Begriffsschärfe „Verpflichtungen" in UMS.5.1.** Das Statement autorisiert Ausnahmen „für Verpflichtungen", die Guidance behandelt Zielkonflikte zwischen Verpflichtungen und die Nicht-Umsetzung von Anforderungen. *Teilweise entschieden:* Ausnahmen von MUSS-Anforderungen schließt der Standard 300-1 aus (Abschnitt 6.5); ob UMS.5 Compliance-Verpflichtungen aus GC.3 oder auch SOLLTE-Anforderungen meint, bleibt offen (Anhang D, D9, D40).
5. **Statuswert „nicht anwendbar".** Der Standard führt ihn ein, die Guidance zu UMS.1.1 kennt nur zwei Werte, und er ersetzt die Streichung aus STM.2.1.5 (Abschnitt 6.1; Anhang D, D38, D39). Erwartete Katalogänderung.
6. **Begriffe.** „erfüllt" (Standard) und „umgesetzt" (Katalog) meinen dasselbe; „temporär" und „dauerhaft" sind im Standard nur über Beispielsätze definiert, und die „Restrisikobetrachtung" aus Kap. 2.11 ist gegen die „Risikobetrachtung" aus Kap. 4.1.2 nicht abgegrenzt (Anhang D, D45, D46).
7. **Mindestfelder und Nachweise des Umsetzungsplans** stehen nur im Standard (Kap. 4.3); der Katalog kennt in UMS.2 bis UMS.6 keine Feldliste außer der Guidance zu VRB.5.1 (Anhang D, D47).

---

*Ende Kapitel 6 (v0.9). Review-Anmerkungen bitte gegen die Control-IDs und die Kapitel des Standards 300-1.*
