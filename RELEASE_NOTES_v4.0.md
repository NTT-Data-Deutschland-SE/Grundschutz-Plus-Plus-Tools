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

Die Sperre ist dabei **keine Höflichkeit, sondern Schreibvoraussetzung** — schärfer als im ursprünglichen Plan: Die RLS-Policy verlangt für jedes Schreiben die gehaltene Sperre, auch `curl` kommt daran nicht vorbei, und der Client blockiert konsistent dazu schon das lokale Speichern („Set ist nicht gesperrt"), damit der lokale Stand nicht vom Server wegläuft. Der Status-Chip zeigt den Zustand **„nur lesen"**, bevor man tippt. Deshalb darf auch `pruefer` sperren — sonst könnte er nie AP/AR schreiben.

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

## Befunde aus dem Release-Candidate-Test

Der Testlauf mit der Datenbank (Admin legt ein Set an, erzeugt ein Baustein-Profil, will es im SSP verwenden und Rechte vergeben) hat eine Kette stiller Ausfälle aufgedeckt — jeder für sich klein, zusammen ein „es geht nicht":

- **„BSI → G++ Profil" verweigerte stumm.** Ohne gehaltene Sperre lehnt der Kern das Ablegen ab — das Werkzeug schrieb das nur in seine (oft eingeklappte) Log-Konsole, und das Profil fehlte in der Übersicht. Jetzt erscheint das rote Banner des Kerns wie in den anderen Werkzeugen; der Chip neben Stufe 3 zeigt, ob die Ablage gelungen ist. Außerdem vergaß das Werkzeug den Profilnamen zwischen zwei Läufen nicht: Ein zweiter Baustein hätte das Profil des ersten im Set überschrieben.
- **Profile aus dem Arbeitsstand als Zielobjekt.** Der Generator bot Set-Profile nur unter „Zusätzliche Kataloge" an (Import in den SSP). Jetzt gibt es beides: dort als Import, unter „Zielobjekte anlegen" als Grundlage eines Zielobjekts — mit allen Controls im Tailoring und den mitgebrachten `alters` als Anpassungen, die beim Export unverändert wieder hinausgehen (Original-Parts wie `ed2023-quelle` werden nicht zu `statement` umgedeutet).
- **Der Generator hielt fremde Profile für seine.** Beim Start las er das jüngste Profil *irgendeines* Werkzeugs als Blaupausen-Profil; seit Baustein-Profile im Set liegen, kamen Titel und Zusatzkataloge aus dem falschen Dokument. Er liest jetzt nur sein eigenes. Und die Rekonstruktion aus dem Set erkannte Zielobjekte am OSCAL-Typ `service` — fast alle sind aber `hardware`, `software`, `network` oder `physical` und verschwanden beim Neuladen; der nächste Live-Sync schrieb den SSP dann ohne sie. Erkannt wird jetzt der Profil-Link, `set://`-Quellen kommen aus dem Artefaktspeicher.
- **Profil-Editor in Stufe 3.** Das erzeugte Profil lässt sich direkt bearbeiten (Titel, Controls an- und abwählen, Controls aus dem Katalog ergänzen, Ergänzungstexte je Control), mit JSON-Sicht daneben. Eine Wahrheit für Download, Set und beide Sichten — vorher konnten Textfeld-Änderungen still am Set vorbeigehen.
- **Set-Rechte für neue Sets.** Die Vorschlagsliste in `config.html` kannte nur Sets mit Artefakten — ein frisch angelegtes, noch leeres Set fehlte und schien nicht berechtigbar. Jetzt stehen aktives Set, Server-Rechte und Server-Artefakte drin, der Name darf auch frei eingetippt werden, und die Erfolgsmeldung überlebt das Neu-Rendern der Liste. Scheitert `whoami` beim Laden (Token-Refresh, Netz), blieb die Benutzerverwaltung bisher die ganze Sitzung verborgen — jetzt wird der Fehler angezeigt und beim nächsten Anlass oder per Klick erneut versucht.

## Nicht im Umfang von 4.0

* Die produktive Härtung des Backends (TLS auf dem öffentlichen Port, GoTrue-Admin-API statt direkter `auth.users`-Schreibzugriff bei der Konto-Anlage) — die Terraform-Umgebung ist eine Testinstanz.

## Versionen der Anwendungen

| Anwendung | Version |
|---|---|
| gemeinsamer Kern (gpp-core.js) | 3 · Cache-Buster v3.9 |
| Übersicht (index.html) | 1.4 |
| OSCAL Schema Validator | 1.11.2 |
| SSP-Generator (G++) | V5.11.0 |
| GS++ Explorer (GSpp-Viewer) | v9.8 |
| BSI → G++ Profil (Baustein_2_Profile) | 0.10.0 |
| SSP-Editor (ssp_ausfuellen) | v1.3.0 |
| Prüfung AP/AR (pruefung_ap_ar) | build 9.5.2 |
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
