# Grundschutz++ OSCAL Tools – Version 4.0

Version 3 hat die neun Werkzeuge auf eine gemeinsame Basis gestellt und einen geteilten Artefaktbestand im Browser eingeführt. Version 4 öffnet diesen Bestand über den einzelnen Rechner hinaus: eine **optionale gemeinsame Datenbank**, in der ein Team an denselben Sets arbeitet, mit serverseitig durchgesetzten Rechten und einer beratenden Sperre gegen gleichzeitiges Schreiben. Der entscheidende Satz bleibt gültig und bleibt richtig: **ohne hinterlegten Server verhält sich alles exakt wie bisher — offline, ohne Backend, nur der Browser.**

Damit sind alle Phasen des Datenbank-Plans umgesetzt (der Plan selbst, `PLAN_Datenbank-Backend.md`, ist mit diesem Release abgearbeitet und aus dem Repository entfernt — die getroffenen Entscheidungen samt bewusster Abweichungen stehen hier und in `infra/terraform/README.md`, Abschnitt 4).

## Neu: Zusammenarbeit über eine gemeinsame Datenbank

Wer in `config.html` eine Server-URL hinterlegt und sich anmeldet, dessen Speichervorgänge gehen **zusätzlich** in eine gemeinsame PostgreSQL-Datenbank (PostgREST + GoTrue, als Supabase-Stack — self-hosted oder gehostet, derselbe Client-Code). Alles andere bleibt, wie es war.

**Lokal zuerst — die Datenbank ist ein Ziel, kein Nadelöhr.** Jedes Werkzeug speichert wie bisher in die IndexedDB und liefert zurück; der Push an den Server hängt daran, nicht davor. Ein Netzausfall verliert nichts und blockiert nichts: fehlgeschlagene Übertragungen warten in einer Outbox und gehen bei nächster Verbindung raus. Das automatische Dauerspeichern des POA&M-Generators wird dabei entprellt, damit aus Dutzenden Änderungen pro Minute nicht Dutzende Anfragen werden.

**Konflikte werden benannt, nicht überschrieben.** Der ohnehin berechnete `sha256` dient als Version. Trägt der Server inzwischen eine fremde Änderung, gewinnt niemand automatisch — das Werkzeug meldet den Konflikt und bietet Übernehmen oder Erzwingen an. Bei gehaltener Sperre tritt das praktisch nie auf; tritt es doch auf, ist es ein echter Befund.

**Ein Status-Chip** unten in jedem Werkzeug zeigt den Zustand: lokal, ausstehend, synchron oder Konflikt. Er hängt sich selbst ein — kein Eingriff in die einzelnen Werkzeuge.

**Zwei Anmeldewege, ein Token.** E-Mail und Passwort für kleine Teams und Einzelinstallationen; alternativ der Unternehmens-IdP über OIDC (der Browser wird umgeleitet, GoTrue führt den Code-Austausch serverseitig — der fehleranfälligste Teil wird bewusst nicht selbst gebaut). Für die Werkzeuge dahinter ist beides dasselbe Token.

**Was den Browser nie verlässt:** API-Schlüssel, GitHub-Token und Prompts. Die sind persönlich und gehören nicht in einen geteilten Bestand. Vom Sitzungszustand liegt nur das kurzlebige Refresh-Token im Browser; das Passwort wird nirgends gespeichert.

## Neu: Rollen und Rechte — in der Datenbank durchgesetzt

Vier Rollen, angelehnt an die tatsächliche Arbeitsteilung (Plan §4):

| Rolle | Darf |
|---|---|
| `leser` | Alle Sets der Organisation lesen. Kein Schreiben, keine Sperre. |
| `bearbeiter` | Sets sperren und darin schreiben — Kataloge, Profile, SSP, Workspaces. **Nicht** `ap`/`ar`. |
| `pruefer` | Wie `leser`, zusätzlich `ap`, `ar`, `poam` schreiben. Trennt Prüfung von Erstellung. |
| `admin` | Alles, plus Benutzerverwaltung, plus fremde Sperren brechen. |

Der springende Punkt: **Durchgesetzt wird in der Datenbank, nicht im Client.** Jedes Werkzeug ließe sich manipulieren oder durch `curl` ersetzen — wer was darf, entscheidet PostgreSQL über Row-Level-Security und geprüfte Funktionen. Die Rechte liegen in Tabellen (`memberships`, `set_permissions`), nicht in den Token-Claims: Eine Änderung des Admins greift mit der nächsten Anfrage, nicht erst nach Ablauf des Tokens. Ein **Set-Recht** kann die globale Rolle für ein einzelnes Set feiner setzen.

**Benutzerverwaltung für den Admin** direkt in `config.html` → „Zusammenarbeit" (nur sichtbar, wenn die Datenbank die Rolle `admin` meldet): Konten anlegen und löschen, globale Rollen ändern, Set-Rechte vergeben und entziehen. Jede Aktion prüft serverseitig auf `admin`, bevor sie irgendetwas tut.

**Nachvollziehbarkeit:** Jede Schreiboperation und jeder Sperrvorgang erzeugt eine Audit-Zeile (Wer, Was, Wann — ohne Dokumentinhalt), die nur der Admin liest.

Was ein Unauthentifizierter kann: **nichts Datenrelevantes.** Ohne Anmeldung gibt es kein Lesen und kein Schreiben; der öffentliche Anon-Key ist kein Vertrauensmerkmal. Das Berechtigungsmodell ist in der Betriebsanleitung (`infra/terraform/README.md`, Abschnitt 4) vollständig beschrieben, samt curl-Abnahme der Grenzen.

## Sperren gegen gleichzeitiges Schreiben — sichtbar und bedienbar

Wer ein Set bearbeitet, sperrt es für andere: In der Übersicht steht neben der Set-Auswahl **„Bearbeiten (sperren)"** bzw. **„Freigeben"**; eine fremde Sperre wird mit Halter und Uhrzeit angezeigt, und der Status-Chip warnt in jedem Werkzeug (🔒), solange sie steht. Der Admin kann eine fremde Sperre **übernehmen** — mit Rückfrage, und der Vorgang steht im Audit-Log.

Die Sperre ist dabei **keine Höflichkeit, sondern Schreibvoraussetzung** — schärfer als im ursprünglichen Plan: Die RLS-Policy verlangt für jedes Schreiben die gehaltene Sperre, auch `curl` kommt daran nicht vorbei, und der Client blockiert konsistent dazu schon das lokale Speichern („Set ist nicht gesperrt"), damit der lokale Stand nicht vom Server wegläuft. Der Status-Chip zeigt den Zustand **„nur lesen"**, bevor man tippt. Deshalb darf auch `pruefer` sperren — sonst könnte er nie AP/AR schreiben. Zusätzlich hängt oben in jedem Werkzeug eine **Sperr-Pill**, sobald das aktive Set nicht von einem selbst gesperrt ist: „🔓 nicht gesperrt — Änderungen werden NICHT gespeichert" mit **„Jetzt sperren"** direkt daneben (kein Umweg über die Übersicht), bzw. „🔒 von *Name* gesperrt — nur lesen" bei fremder Sperre. Übernehmen bleibt bewusst in der Übersicht (Rückfrage, Audit).

Drei weitere Regeln aus derselben Logik: **Neue Sets legt nur der Admin an** (Nicht-Admins schreiben und sperren nur Sets, die existieren — Artefakte vorhanden oder Set-Recht vergeben). **Ganze Sets löscht oder leert ebenfalls nur der Admin** — das Wholesale-Löschen eines geteilten Standes ist eine Verwaltungsentscheidung, keine Bearbeitung; einzelne Artefakte entfernen bleibt normales Arbeiten mit Sperre. Die Knöpfe „+ Neues Set", „Set löschen" und „Set leeren" erscheinen entsprechend nur für Admins; im reinen Lokalbetrieb ohne Datenbank bleiben sie für alle frei. Und **gelöscht heißt überall gelöscht**: Löscht der Admin ein Set (oder jemand einzelne Artefakte), spiegelt der nächste Abgleich die Löschung auf alle anderen Browser — dort aber in einen lokalen **Papierkorb** (`config.html` → Speicher) statt ins Nichts, denn die Spiegelung könnte den letzten existierenden Stand eines Dokuments treffen. Eigene, noch nicht übertragene Arbeit bleibt geschützt, und rein lokale Sets, die nie auf dem Server waren, rührt der Abgleich nicht an.

Technisch: atomarer Erwerb, Heartbeat alle 60 Sekunden solange ein Tab sichtbar ist, Zeitüberschreitung von fünf Minuten, damit ein abgestürzter Tab kein Set dauerhaft blockiert. Der Sperrerwerb zieht zugleich den Serverstand des Sets in den Browser. Beim Schließen eines Tabs wird bewusst **nicht** automatisch freigegeben — die Sperre gehört dem Benutzer, nicht dem Tab, und ein zweites offenes Werkzeug arbeitet womöglich weiter; verwaiste Sperren räumt die Zeitüberschreitung ab.

**Geteilte Sets werden gefunden.** Nach der Anmeldung (und beim Laden jeder Seite) holt der Client alle Sets, auf die der Benutzer Zugriff hat — auch solche, die nur per Set-Recht zugewiesen und noch leer sind — und zeigt sie in der Set-Auswahl der Übersicht. Ein neu berechtigtes Teammitglied sieht ein geteiltes Set damit sofort, ohne den Namen kennen zu müssen.

## Betrieb: Testumgebung als Terraform

Neu im Repository unter `infra/terraform/`: die Referenzinstallation als Infrastruktur-als-Code — eine einzelne Compute-Engine-VM mit dem Supabase-Compose-Stack, wahlweise mit Caddy als TLS-Endpunkt und statischem Host, sodass Werkzeuge und API unter demselben Ursprung liegen und die CORS-Frage entfällt. Das Startskript spielt das Datenbankschema beim ersten Boot ein und legt das Admin-Konto an (Passwort im Secret Manager). Bewusst kein Cloud SQL und kein Cloud Run: Der Aufbau soll dem entsprechen, was Anwender später selbst betreiben.

Das `schema.sql` liegt als eigene Datei bei — Tabellen, RLS-Policies, die Rollen-Auflösung, die Sperr- und Admin-Funktionen und die Audit-Trigger. Es ist idempotent und gegen die Testinstanz verifiziert.

## Bestehende Arbeit in die Datenbank bringen

Wer schon vor der Zusammenarbeit lokal gearbeitet hat, überträgt den Bestand mit einem Klick: In der Übersicht erscheint **„⤒ In DB übertragen"**, sobald man die Sperre des aktiven Sets hält. Jedes lokale Artefakt wird angestoßen; was auf dem Server bereits identisch liegt, geht still durch, echte Kollisionen laufen als Konflikt auf und werden bewusst entschieden. Der Lösch-Spiegel des Abgleichs weiß dabei, was er anfassen darf: Nur Stände, die der Server nachweislich kennt (einmal übertragen oder von dort geholt), gelten bei ihm als „drüben gelöscht" — nie synchronisierter Altbestand bleibt liegen und wartet auf die Übertragung.

## Die Werkzeugkette speichert sich selbst (Live-Set)

Mit der gemeinsamen Datenbank fällt der letzte manuelle Handgriff: **die Abspeichern-Knöpfe sind weg.** SSP-Generator, SSP-Editor, Prüfung und POA&M schreiben ihr Dokument (Profil, SSP, AP, AR, POA&M) bei jeder Änderung entprellt als Einzelstück ins aktive Set — kurz nach der Eingabe, spätestens alle 30 Sekunden, und sofort beim Verlassen der Seite. Heruntergeladen wird in der Übersicht; dort hängen die Export-Knöpfe an jedem Artefakt.

Die Werkzeuge lesen einander damit direkt zu: Ein im Generator ergänztes Control steht beim nächsten Öffnen im Editor und in der Prüfung; ein „nicht erfüllt" aus der Prüfung erscheint als Maßnahme im POA&M. Die Übernahmen **mergen statt überschreiben** — der Generator bestimmt die Struktur, der Editor behält seine Texte je Control und Komponente, die Prüfung ihre Bewertungen, das POA&M seine Abarbeitung (Status, Fristen, Meilensteine); Einträge zu Controls, die es nicht mehr gibt, entfallen benannt. Übernommen wird nur bei **inhaltlich** geändertem Artefakt (sha256-Vergleich), und jeder Arbeitsstand gehört seinem Werkzeug — ein Wechsel zwischen den Seiten verwechselt keine Stände mehr. Verliert eine Prüfungs-Session doch einmal ihre Bewertungen, holt sie sie aus dem AR-Artefakt zurück.

Ein Set trägt dabei **genau ein** SSP, AP, AR und POA&M — Neues ersetzt Altes, auch serverseitig; die Übersicht räumt Duplikate aus Altbeständen beim Laden weg. Die Zähler an den Reitern zeigen nicht mehr „wie viele Dateien", sondern **wie viele Controls** im jeweiligen Dokument stecken.

Scheitert ein Live-Speichern — typisch: die Sperre fehlt —, erscheint ein **rotes Banner** am oberen Rand statt einer stillen Logzeile, und es verschwindet mit dem nächsten erfolgreichen Speichern. Wer ohne Sperre arbeitet, sieht das sofort, nicht erst beim Datenverlust.

## Leistung und Bedienung

- **Prüfung bei großen Beständen:** Die Controls einer Komponente werden erst beim Aufklappen aufgebaut. Ein Bestand mit ~8.800 Controls belegte zuvor rund 3 GB Browser-Speicher und brauchte Minuten — jetzt ~33 MB und unter 100 ms fürs Rendern. Die Filter arbeiten deshalb über das Modell und klappen Treffer-Komponenten selbst auf.
- **Delta-Abgleich mit der Datenbank:** Gezogen werden nur geänderte Artefakte (id+sha256-Vorabfrage, gebündelte Volltext-Abfragen) — der Seitenaufruf zieht nicht mehr den kompletten Bestand durchs Netz. Gepusht wird beim Freigeben der Sperre, alle fünf Minuten und beim Verstecken des Tabs; lokal ist ohnehin jede Änderung sofort gesichert.
- **Schwebende Filterleiste links** (`gppFilterDock`) für Seiten ohne Filter in der Navigation — zuerst im SSP-Generator für die Tailoring-Suche.
- **Log-Konsolen** klappen jetzt überall wirklich zusammen (auch bei fester CSS-Höhe), und der DB-Status-Chip weicht der eingeklappten Konsole aus, statt ihre Bedienung zu überdecken.

## Präziseres G++ ↔ ED23-Mapping — mit Teilanforderungen

Die vorberechnete Zuordnung jeder Grundschutz++-Maßnahme zu den Anforderungen der Edition 2023 (`hilfsdateien/gpp_ed23_anforderungen.json`, im Explorer das Panel „Zeige BSI ED23 Anforderungen") war unpräzise: oft zu viele Treffer, nicht spezifisch für die Maßnahme innerhalb ihrer Praktik (Issue #28). Die Ursache lag im Kontext — die KI sah nur Titel und einen einzelnen Statement-Satz; die Erläuterung wurde verworfen, bei einem Fünftel der Maßnahmen standen rohe Parameter-Platzhalter im Text, und von den Nachbar-Maßnahmen derselben Praktik wusste sie nichts.

Die Zuordnung wurde vollständig neu erzeugt, mit drei Änderungen:

- **Voller Kontext, klare Abgrenzung.** Jede Anfrage trägt jetzt Statement (Parameter aufgelöst), Erläuterung und Praktik — und die Nachbar-Maßnahmen als ausdrückliche Negativ-Liste: Was primär zu einer Nachbar-Maßnahme gehört, wird nicht dieser zugeordnet.
- **Zwei Stufen statt einer.** Ein großzügiger Suchlauf sammelt Kandidaten (gegen den vollständigen, gecachten ED23-Korpus), danach prüft ein strengeres Modell jeden Kandidaten einzeln. Nur was die Prüfung besteht, erreicht die Datei. Im handgeprüften Sample blockiert das alle bekannten Fehlzuordnungs-Muster — thematische Nähe ohne inhaltliche Deckung überlebt die Einzelprüfung nicht.
- **Jede Zuordnung nennt ihre Teilanforderung.** Die Beschreibungen der ED23-Anforderungen sind satzweise nummeriert; jede Zuordnung benennt den tragenden Satz — wir nennen ihn **Teilanforderung** — als Präfix `(Teilanforderung n)` in der Begründung und maschinenlesbar als `statement-sentence`-Prop. Damit ist jeder Treffer in Sekunden nachprüfbar: Man liest genau den Satz, auf dem er ruht. (Der Begriff „Teilanforderung" stammt aus keinem BSI-Standard; er wird lediglich in einem Absatz des BSI-Auditierungsschemas verwendet — wir übernehmen ihn, weil er das Gemeinte präzise trifft.)

Das Ergebnis: **3.046 verifizierte Zuordnungen für 820 Maßnahmen** statt zuvor 5.521 für 1.000 — im Median 3 statt 5 pro Maßnahme. Dass 180 Maßnahmen jetzt ohne Treffer dastehen, ist beabsichtigt: G++-spezifische Konzepte (etwa die Strukturmodellierungs-Methodik) haben in der Edition 2023 schlicht kein Gegenstück, und eine leere Liste ist ehrlicher als eine ungefähre. Der Explorer zeigt die neuen Begründungen ohne eigene Änderung an; die Erzeugung ist im Gpp-ai-tool dokumentiert (Maker-Checker-Verfahren, `ED23_MAKER_MODEL`).

## Befunde aus dem Release-Candidate-Test

Der Testlauf mit der Datenbank (Admin legt ein Set an, erzeugt ein Baustein-Profil, will es im SSP verwenden und Rechte vergeben) hat eine Kette stiller Ausfälle aufgedeckt — jeder für sich klein, zusammen ein „es geht nicht":

- **„BSI → G++ Profil" verweigerte stumm.** Ohne gehaltene Sperre lehnt der Kern das Ablegen ab — das Werkzeug schrieb das nur in seine (oft eingeklappte) Log-Konsole, und das Profil fehlte in der Übersicht. Jetzt erscheint das rote Banner des Kerns wie in den anderen Werkzeugen; der Chip neben Stufe 3 zeigt, ob die Ablage gelungen ist. Außerdem vergaß das Werkzeug den Profilnamen zwischen zwei Läufen nicht: Ein zweiter Baustein hätte das Profil des ersten im Set überschrieben.
- **Profile aus dem Arbeitsstand als Zielobjekt.** Der Generator bot Set-Profile nur unter „Zusätzliche Kataloge" an (Import in den SSP). Jetzt gibt es beides: dort als Import, unter „Zielobjekte anlegen" als Grundlage eines Zielobjekts — mit allen Controls im Tailoring und den mitgebrachten `alters` als Anpassungen, die beim Export unverändert wieder hinausgehen (Original-Parts wie `ed2023-quelle` werden nicht zu `statement` umgedeutet).
- **Der Generator hielt fremde Profile für seine.** Beim Start las er das jüngste Profil *irgendeines* Werkzeugs als Blaupausen-Profil; seit Baustein-Profile im Set liegen, kamen Titel und Zusatzkataloge aus dem falschen Dokument. Er liest jetzt nur sein eigenes. Und die Rekonstruktion aus dem Set erkannte Zielobjekte am OSCAL-Typ `service` — fast alle sind aber `hardware`, `software`, `network` oder `physical` und verschwanden beim Neuladen; der nächste Live-Sync schrieb den SSP dann ohne sie. Erkannt wird jetzt der Profil-Link, `set://`-Quellen kommen aus dem Artefaktspeicher.
- **BSI-Komponenten überlebten keinen Seitenstart.** Dieselbe Lücke für die Component-Definitions aus dem SdT-`implementation_layer` (Abschnitt 3b): Die Rekonstruktion aus dem Set kannte sie nicht, nach einem Reload fehlten sie im Arbeitsstand, ihre gemappten Controls rutschten als „manuell" durch, und der nächste Live-Sync schrieb den SSP ohne Komponenten, Resource und Umsetzungsbeschreibungen zurück. Jetzt werden sie am Link `component-definition` erkannt, die Quell-CDef über die gepinnte back-matter-Resource (URL + SHA-256) erneut geladen und auf G++-Controls gemappt; die Komponenten-UUIDs aus dem SSP bleiben erhalten, damit die Umsetzungsbeschreibungen je Control weiter passen. Ist die Quelle nicht erreichbar, bleiben Bauteile und Zuordnungen aus dem SSP bestehen — mit Warnung im Log und Hinweis in der Liste („Quelle nicht nachgeladen"), damit nichts still verschwindet.
- **Profil-Editor in Stufe 3.** Das erzeugte Profil lässt sich direkt bearbeiten (Titel, Controls an- und abwählen, Controls aus dem Katalog ergänzen, Ergänzungstexte je Control), mit JSON-Sicht daneben. Eine Wahrheit für Download, Set und beide Sichten — vorher konnten Textfeld-Änderungen still am Set vorbeigehen. Und: **Vorhandene Profile aus dem Arbeitsstand lassen sich ohne Pipeline-Lauf öffnen und weiterbearbeiten** — gespeichert wird in denselben Set-Eintrag (gleiche ID, Ursprungs-Tool bleibt), bloßes Öffnen fasst nichts an. Nur die Blaupausen-Profile des SSP-Generators sind ausgenommen: die schreibt dessen Live-Sync ohnehin bei jeder Änderung neu.
- **Zielobjekt-Profile waren Lückentext.** Ins Profil kamen nur Controls, für die das KI-Satz-Mapping Treffer fand — die übrigen Controls der Zielobjektkategorie fehlten. Jetzt gilt: Gibt es eine Zielobjektkategorie, stehen **alle Controls ihres Pools** im Profil (Prozess-Bausteine und C.2 bleiben wie bisher); der Ed2023-Wortlaut hängt als `alters`-Ergänzung an den Controls, für die es ihn gibt. Dazu nutzt das Werkzeug jetzt auch das **vorberechnete G++↔ED23-Matching** (`hilfsdateien/gpp_ed23_anforderungen.json`, gepinnte Quelle wie im Generator): Nennt es für eine Anforderung dieses Bausteins ein Control, das das Satz-Mapping nicht traf, wird der volle Anforderungstext aus dem geparsten PDF deterministisch dort ergänzt — erkennbar am Präfix „vorberechnetes G++-Matching"; Treffer außerhalb des Kategorie-Pools werden gezählt und im Log genannt, nicht ins Profil gemischt.
- **Quellen-Pins: Umstellen wischte die übrigen Prüfergebnisse weg.** Nach „Alle Quellen prüfen" zeigte jede Quelle ihren Stand — aber der erste Klick auf „Auf diesen Commit umstellen" baute die ganze Liste neu und leerte alle anderen Ergebnisboxen; es wirkte, als höre die Prüfung nach der ersten Quelle auf. Jetzt aktualisiert sich nur die betroffene Zeile (Pill, URL, Ergebnis), der Rest bleibt stehen. Dazu neu: **„⤒ Alle updaten"** stellt alle prüfbaren Quellen in einem Rutsch auf den jeweils neuesten Commit um — mit Rückfrage, Ergebnis je Quelle und Zusammenfassung; inhaltsgepinnte Quellen (SHA-256) bleiben unberührt.
- **„Control anpassen": Parameter nur, wenn es welche gibt — und zwar die echten.** Der Reiter „Parameter setzen" erschien für jedes Control und ließ eine frei geratene ID (`<Control>_prm_1`) eintragen — solche IDs existieren im Katalog nicht, der set-parameter lief bei der Profil-Auflösung ins Leere. Jetzt erscheint der Reiter nur bei Controls mit Katalog-Parametern und bietet genau diese an (z. B. `gc.1.1-prm1`), mit dem Katalogwert als Hinweis und dem bereits gesetzten Wert vorbefüllt; der Re-Import löst Parameter-IDs über den Katalog-Index auf. Und **„Text ergänzen" zeigt die vorhandenen Ergänzungen** direkt editierbar (Text und Position), auch die aus einem Set-Profil mitgebrachten — deren Original-Part bleibt beim Export erhalten.
- **Risiken der Dokumentanalyse erschienen nirgends.** Die KI-Analyse extrahierte Risiken samt Bedrohung (G 0.x) und mitigierenden Controls — sie flossen aber nur unsichtbar in den SSP-Export; die Risikoanalyse-Sektion blieb leer, nichts war prüf-, änder- oder löschbar. Jetzt landen sie in der Risiko-Tabelle (Ziel-Zuordnung über die Quell-ID des Dokuments, z. B. „S007"), mitigierende Controls werden gegen den Katalog aufgelöst — nirgends definierte KI-Maßnahmen als gekennzeichnete Custom-Controls geführt — und der Export zählt nichts doppelt.
- **Neuer Umsetzungsstatus `not-implemented` — vom SSP bis ins POA&M.** Bewusste Erweiterung des NIST-Vokabulars (eingereicht als Issue #2272/PR #2273 an usnistgov/OSCAL): „nicht umgesetzt" ist eine Feststellung, kein Plan. Der SSP-Editor bietet den Status je Control an (eigene Farbe, Filter), der Generator normalisiert ihn aus der Dokumentanalyse, und die Prüfung belegt Befunde vor: Deklarieren ALLE Komponenten eines Controls `not-implemented`, steht das Finding als „nicht erfüllt" mit Begründung bereit (gemischte Stände bleiben offen, ein echtes Prüfurteil gewinnt immer, ein alter Befund ohne Urteil löscht die Vorbelegung nicht). Über das AR (Finding + Risiko) macht das POA&M daraus wie gewohnt eine Maßnahme.
- **Sperr-Pill in jedem Werkzeug.** Der Status-Chip unten rechts („nur lesen") war zu leise, das rote Banner kam erst nach dem ersten verweigerten Speichern. Jetzt hängt oben eine deutliche Pill, solange das aktive Set nicht von einem selbst gesperrt ist — mit „Jetzt sperren" direkt an Ort und Stelle (Kern, Cache-Buster v4.0; die Übersicht unterdrückt sie, dort steht die Sperr-Verwaltung selbst).
- **Set-Rechte für neue Sets.** Die Vorschlagsliste in `config.html` kannte nur Sets mit Artefakten — ein frisch angelegtes, noch leeres Set fehlte und schien nicht berechtigbar. Jetzt stehen aktives Set, Server-Rechte und Server-Artefakte drin, der Name darf auch frei eingetippt werden, und die Erfolgsmeldung überlebt das Neu-Rendern der Liste. Scheitert `whoami` beim Laden (Token-Refresh, Netz), blieb die Benutzerverwaltung bisher die ganze Sitzung verborgen — jetzt wird der Fehler angezeigt und beim nächsten Anlass oder per Klick erneut versucht.

## Nachtrag 26.08.2026 — Terraform-Testumgebung

Beim Neuaufbau der Testumgebung nach dem Release fiel auf, dass das Admin-Konto beim ersten Boot **keine `admin`-Mitgliedschaft** bekam: psql ersetzt seine `:'variablen'` nicht innerhalb von `DO $$ … $$`-Blöcken, der Schritt brach mit einem Syntaxfehler ab, und der Admin sah nichts. `startup.sh` legt die Mitgliedschaft jetzt mit einem gewöhnlichen `INSERT … ON CONFLICT` an — für den Admin und, bei `seed_test_users = true`, für die Testkonten.

Dazu die Betriebsanleitung (`infra/terraform/README.md`) überarbeitet: keine Zugangsdaten und keine feste IP mehr im Text; stattdessen, wie `ANON_KEY` und `SERVICE_ROLE_KEY` von der VM zu holen sind (sie entstehen dort, nicht in Terraform), und ein Abschnitt „Zugriffsweg wählen" — ohne `allow_public_api` oder `domain` läuft die Datenbank nur durch den IAP-Tunnel, was die Werkzeuge im Browser nicht erreichen. Beide Schalter stehen jetzt kommentiert in `terraform.tfvars.example`.

## Nachtrag 29.08.2026 — Quellen-Pins auf den aktuellen Stand

Turnusmäßige Pin-Prüfung über alle Quellen der Werkzeuge (Grundregel 8: gepinnt ist der Normalfall, Aktualisieren ist eine bewusste Entscheidung):

- **Stand-der-Technik-Bibliothek neu gepinnt (`36a0fac4`, Rolling-Publication vom 27.08.).** Gegenüber dem bisherigen Pin `47de2824` enthält der Stand echte Korrekturen: GC.4.2 „externen"→„internen", KONF.7.14 neu formuliert (Signaturprüfung für nachladbaren Code im Kernelmodus), überarbeitete Guidance zu BER.3.24, KONF.4.1.1 und KONF.6.1.2, dazu Tippfehler- und Tag-Korrekturen. Der Control-Bestand ist unverändert (1000 IDs). Der Wechsel erfolgte koordiniert an allen Stellen zugleich: Katalog-Pin, SHA-256-Inhaltspin und Resource-UUID in den sechs Werkzeugen und der Pipeline, dazu alle 229 Repo-Profile (Zielobjektkategorien + ED23-Baustein-profile) auf das neue Pin-Ziel migriert. Auch Kernel-, Methodik- und Risikomanagement-Katalog (Viewer-Schnellauswahl, BSI-Komponenten im Generator) zeigen auf diesen Stand.
- **Selbst-Pins vereinheitlicht.** Die Repo-eigenen Quellen (Hilfsdateien, C3A-/C5-/Beispiel-Kataloge, Methodik-Profile) pinnten noch drei verschiedene Commits; sie zeigen jetzt einheitlich auf den Stand mit den migrierten Profilen.
- **Unverändert gelassen:** Der ED23-Katalog-Pin (`62f08039`, NTTDATA-DACH) ist weiterhin der neueste Stand; die Zielobjektkategorien-CSV ist am neuen Pin byteidentisch; `hilfsdateien/gpp_ed23_anforderungen.json` und die Gap-Analyse behalten ihre Provenienz-Referenzen auf den Erzeugungsstand. Bekannte, bewusst akzeptierte Drift: die Maturity-Statements zu KONF.7.14 entstanden gegen den alten Wortlaut.

Außerdem seit dem letzten Tag-Stand hinzugekommen: die ED23-Lücken-Kreuzanalyse (Script, Report, Handbuch-Zahlen) und der deterministische Zerlegungsvergleich samt vorbereiteter (nicht ausgeführter) Satz-Abdeckungs-Stage.

## Nachtrag 29.08.2026 — Relationstypen im G++↔ED23-Mapping, BSI-GSMap in der Anzeige

- **Jede Zuordnung trägt jetzt einen differenzierten OSCAL-Relationstyp.** Die neue Stage `stage_ed23_relationen` hat alle 3.046 verifizierten (G++-Maßnahme, ED23-Anforderung)-Paare einzeln klassifiziert (3.042 explizit, 4 Default nach Fehlversuchen); Paare, Satz-Referenzen und Begründungen blieben unverändert, der Diff betrifft ausschließlich das `relationship`-Feld. Verteilung: 1.337 superset-of, 1.062 intersects-with, 551 subset-of, 94 equivalent-to, 2 equal-to (OSCAL-Leserichtung: die G++-Maßnahme relativ zur ED23-Anforderung). Der Report deutet das in Abschnitt 5: Wo G++ abdeckt, deckt es überwiegend als die allgemeinere Fassung ab — das BSI-eigene GSMap zeigt gespiegelt dasselbe Muster.
- **BSI-GSMap als zweite Quelle in den ED23-Panels.** Viewer, SSP-Generator, SSP-Ausfüllen und Prüfung AP/AR zeigen neben unserem Mapping das amtliche ITGS-Mapping (Pin `8f0bcd1f`), jede Zeile als „wir"/„BSI" gekennzeichnet: UA-genaue Quell-IDs, elementare Gefährdungen als Kurzliste, Relation für die Anzeige auf die einheitliche Leserichtung G++→ED23 gespiegelt (Tooltip). Neue Relation-Spalte in allen vier Panels; `Baustein_2_Profile` trägt die Relation in den Matching-Blöcken, hält die BSI-Quelle aber bewusst aus der Profil-Erzeugung heraus.
- **Developer-API-Modus für die Pipeline.** Der AiClient läuft alternativ zu Vertex/ADC mit `GEMINI_API_KEY` (aus `.env` in `Gpp-ai-tool/` oder Repo-Root, gitignored, BOM-tolerant gelesen); der Klassifikationslauf lief vollständig darüber. Checkpoints beider neuer Stages gegen transiente Windows-Datei-Locks gehärtet.
- **Rückmeldung ans BSI:** Issue [Stand-der-Technik-Bibliothek#98](https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek/issues/98) dokumentiert die Unvollständigkeit des ITGS-Mappings (510 von 1.834 aktiven Anforderungen, 17 veraltete Ziel-IDs) mit Reproduktionsweg.
- Quellen-Pins der fünf Werkzeuge auf den klassifizierten Mapping-Stand (`1971460`) gehoben.

## Nachtrag 29.08.2026 — Amtliche Basis: v2-Union des ED23-Mappings, Kostenplan, Werkzeug-Politur

Die Mapping-Erstellung baut jetzt vollständig auf dem **amtlichen BSI-XML-Kompendium** auf; die NTT-Maturity-Paraphrase ist aus der gesamten Auswertungs-Kette entfernt (die Reifegrad-Profile und `ssp_generator_ed23` bleiben als eigenes Produkt unberührt).

- **`gpp_ed23_anforderungen.json` als beidrichtige Union (PR #36): 5.145 Zuordnungen** — GS++-seitiger Batch-Maker-Checker plus satzweise ED23-seitige Prüfung aller 6.611 normativen Sätze, 1.209 Paare beidseitig bestätigt, Provenienz-Prop `matching-direction` je Eintrag, durchgängig amtliche Satz-Nummerierung, OSCAL-Relationstyp je Zuordnung (3.103 superset-of, 1.093 intersects-with, 809 subset-of, 125 equivalent-to, 15 equal-to). Neue Kernzahlen: 227 von 1.834 aktiven Anforderungen ohne dieses Mapping (12,4 %), 139 ohne jede der drei Quellen (7,6 %), 3.615 von 6.611 normativen Teilanforderungen abgedeckt (54,7 %, jede einzeln beurteilt), Gegenrichtung 133 von 1.000 Maßnahmen. Neue Stages `stage_ed23_satz_abdeckung` und `stage_ed23_relationen`, Merge deterministisch via `scripts/merge_ed23_mappings.py`.
- **Analyse ohne Näherungen:** Die Alignment-Stufe des Reports entfiel ersatzlos (Mapping- und amtliche Satz-Nummern sind dieselbe Welt); `ed23_gap_report.md` trägt die Autoren-Einordnung (Migrationsfolgen, Bürokratiekosten, WIE-Verlust) jetzt generiert am Reportanfang. Handbuch 10.5 Punkt 3 auf die Union-Zahlen gezogen; BSI-Issue [Stand-der-Technik-Bibliothek#98](https://github.com/BSI-Bund/Stand-der-Technik-Bibliothek/issues/98) per Body-Vermerk und Nachtrag aktualisiert (inkl. Korrektur des Zerlegungsbefunds: amtlich nummeriert nur 11,8 % disjunkt).
- **Token-Kostenplan** (`Gpp-ai-tool/docs/token-kostenplan.md`): Ist-Analyse des 150-€-Neuaufbau-Tages, acht priorisierte Sparmaßnahmen, Unix-Runbook. Umgesetzt: Maker-Batching (cached Korpus je Call ÷ Batchgröße), Verify-Skip über die Satz-Abdeckung (1.138 gesparte Prüfungen), Sibling-Diät, Kandidaten-Checkpoints mit Lock-Härtung in allen Stages, Token-Bilanz je Lauf, Developer-API-Modus via `GEMINI_API_KEY` (.env). Realkosten des kompletten v2-Zyklus: **22 € statt ~150 €**.
- **Werkzeuge:** ED23-Panels kennzeichnen die Quelle jetzt als `Tool`/`BSI`; Selbst-Pins aller sechs Werkzeuge einheitlich auf den Report-Endstand; `config.html` vergleicht beim Update-Check den Datei-Inhalt (Blob-SHA) statt nur Commit-SHAs und bietet keine inhaltsgleichen Downgrades mehr an. Fremd-Pins geprüft und unverändert korrekt (SdT-Kataloge `36a0fac4`, ITGS `8f0bcd1f`, NTT-ED23 `62f08039`).

## Nachtrag 30.08.2026 — Qualitätsgesicherte Relationstypen: QS-Stichprobe, Streichliste, Familien-Klassifikation

Das G++↔ED23-Mapping wurde erstmals systematisch qualitätsgeprüft und auf Basis der Befunde bereinigt und neu klassifiziert (Issue [#37](https://github.com/NTT-Data-Deutschland-SE/Grundschutz-Plus-Plus-Tools/issues/37), PR [#38](https://github.com/NTT-Data-Deutschland-SE/Grundschutz-Plus-Plus-Tools/pull/38)).

- **QS-Stichprobe** (`hilfsdateien/ed23_mapping_qs/`): 943 der 5.145 Zuordnungen (96 Controls, alle 20 Praktiken) auf vier Achsen geprüft — Inhalt, Relationstyp, Satzwahl, Begründungsehrlichkeit. Ergebnis: Substanz gut (86,9 % inhaltlich sauber, nur 4 echte Fehltreffer), aber 15,9 % der Relationstypen nicht haltbar (fast immer zu großzügiges `superset-of`) und jede zehnte Begründung geschönt. Vollständiger Bericht, 18 Reviewer-Protokolle, Dossiers und Prüfanweisung liegen versioniert im Repo.
- **Bereinigung:** 76 beanstandete Zuordnungen entfernt (Audit: `dropped_pairs.json`), Satz-Splitter-Fix (`engl.` zerriss zwei amtliche Sätze in Fragment-Doppelpaare) mit validierter Satznummern-Migration in Mapping und Satz-Abdeckung.
- **Relationstypen als Familie neu klassifiziert:** `stage_ed23_relationen` urteilt jetzt je Maßnahme über alle ihre Zuordnungen gemeinsam (volle amtliche Satzlisten, Statement + Guidance, explizite Subsumtionsregel und Begründungs-Stilregel) statt Paar für Paar isoliert. Lauf über alle 5.069 Paare: **1.233 Typ-Wechsel, davon 835 superset-of → intersects-with; die superset-Quote fällt von 60,3 % auf 45,1 %** — die frühere Verteilung hatte die Volldeckung systematisch überzeichnet. 2.533 Begründungen ersetzt („deckt … ab" nur noch, wo es stimmt; KANN/SOLLTE wird nicht mehr als „fordert" ausgegeben). Pilot-Gate gegen die QS-Urteile bestanden; Kosten des kompletten Nachlaufs unter 2 € — die Control-Gruppierung macht den kontextreicheren Lauf zugleich billiger (856 statt ~5.100 Calls).
- **Gerichteter Lücken-Nachfass:** 27 QS-Verdachte geprüft, 17 neue Zuordnungen aufgenommen (u. a. KONF.7.4→SYS.1.1.A27 Hostbasierte Angriffserkennung, KONF.10.2→APP.3.2.A11/APP.4.3.A24), 10 Verdachte ehrlich ohne Treffer protokolliert (`nachfass_ergebnis.json`). Neue Einträge tragen `matching-direction: qs-nachfass`. **Endstand: 5.086 Zuordnungen.**
- **Neue Kernzahlen** (Analyzer `--strict` grün, Anker nachgezogen): 231 von 1.834 aktiven Anforderungen ohne dieses Mapping (12,6 %), 141 ohne jede der drei Quellen (7,7 %), 3.573 von 6.611 normativen Teilanforderungen abgedeckt (54,0 %), Gegenrichtung 135 von 1.000 Maßnahmen. `ed23_gap_report.md` weist jetzt den Qualitätsstand der Relationstypen und die **strukturelle Korpus-Lücke RISK** aus (Risikomethodik liegt in 200-3, nicht im Kompendium — dünne Scheintreffer werden nicht mehr geführt); Handbuch 10.5-3 entsprechend aktualisiert.
- **Doku:** `matching-direction` ist jetzt im Namespace-Dokument definiert — einschließlich der Klarstellung, dass „beide" ein Konfidenz- und kein Qualitätssiegel ist (die QS fand einen erfundenen Begründungsinhalt auf einem beidseitig bestätigten Paar).

## Nicht im Umfang von 4.0

* Die produktive Härtung des Backends (TLS auf dem öffentlichen Port, GoTrue-Admin-API statt direkter `auth.users`-Schreibzugriff bei der Konto-Anlage) — die Terraform-Umgebung ist eine Testinstanz.

## Versionen der Anwendungen

| Anwendung | Version |
|---|---|
| gemeinsamer Kern (gpp-core.js) | 3 · Cache-Buster v4.0 |
| Übersicht (index.html) | 1.4 |
| OSCAL Schema Validator | 1.11.2 |
| SSP-Generator (G++) | V5.12.0 |
| GS++ Explorer (GSpp-Viewer) | v9.8 |
| BSI → G++ Profil (Baustein_2_Profile) | 0.11.0 |
| SSP-Editor (ssp_ausfuellen) | v1.4.0 |
| Prüfung AP/AR (pruefung_ap_ar) | build 9.6.0 |
| POA&M-Generator | v2.4 |

Einzelwerkzeuge in `one-page-apps/` — eigenständig, ohne `gpp-core.js`, von der Datenbank unberührt:

| Anwendung | Version |
|---|---|
| SSP-Generator Edition 2023 | ED23 V1.5 |
| C5 → OSCAL Konverter | v1.1 |

## Hinweise zum Umstieg

- **Die Datenbank ist optional und aus.** Ohne Server-URL in `config.html` ändert sich für bestehende Nutzung nichts; der Artefaktbestand bleibt lokal im Browser.
- Wer die gemeinsame Datenbank nutzt, braucht die Sammlung über HTTP ausgeliefert (nicht per Doppelklick über `file://`) — die Terraform-Umgebung liefert dafür den statischen Host gleich mit.
- **Für Betreiber:** Nach dem Einspielen des Schemas müssen Konten eine Mitgliedschaft erhalten (`seed_users.sh` bzw. die Benutzerverwaltung), sonst sehen sie nichts — das ist die Durchsetzung, kein Fehler. Signup am Identity-Provider gehört auf der Testinstanz abgeschaltet; Konten legt der Admin an.
