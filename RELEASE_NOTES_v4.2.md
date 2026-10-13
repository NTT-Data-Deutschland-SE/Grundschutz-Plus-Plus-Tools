# Grundschutz++ OSCAL Tools – Version 4.2

Das BSI hat am 01.10.2026 in der Stand-der-Technik-Bibliothek (PR #112) drei Zielobjektkategorien umbenannt und den Namespace `target_object_categories.csv` neu geschrieben. An den Controls ändert das nichts — 1000 Controls vorher wie nachher, Statement-IDs, Props, Modalverben und Parameter gleich —, wohl aber an allem, was Kategorien beim **Namen** nennt: Filter, Profildateien, die Typzuordnung im SSP und die KI-Zuordnung von Assets. Version 4.2 zieht die Sammlung auf diesen Stand nach. Dazu bekommen die beiden SSP-Werkzeuge Namen, die sagen, was sie tun.

| bisher | neu | UUID (unverändert) |
|---|---|---|
| Endgeräte | Mobile Endgeräte | `837781a4…` |
| Faxe | Faxanwendungen | `05df1662…` |
| Datenträgerarchiv | Archiv | `dfd8e05b…` |

Außerdem im Namespace: eine neue Spalte **Beispiel** (Spalte 3), umgeschriebene, meist kürzere Definitionen — die Beispiele stehen jetzt in der neuen Spalte —, und Institutionsleitung hat den Typ `Mitarbeitende` statt `Nutzende`; die Elternkette über `ChildOfUUID` ist gleich geblieben.

## Neue Namen für die SSP-Werkzeuge

Im SSP-Generator entsteht der SSP und dort wird er auch geändert — er heißt jetzt **SSP-Generator / Editor**. Der bisherige „SSP-Editor“ dokumentiert die Umsetzung je Control, also den Grundschutzcheck, und heißt **SSP ausfüllen / Grundschutzcheck**. Umbenannt sind Reiter, Titel, Kopfzeilen, Hilfe-Readme und Handbuch. Dateinamen, Tool-IDs und Speicher-Schlüssel bleiben, damit vorhandene Sets und Arbeitsstände unverändert laden. Die Übersicht zeigt NTT DATA in der Kopfzeile.

## Quellen-Pin auf a128311

Anwenderkatalog, Kernel-, Methodik- und Risiko-Katalog sowie die Namespaces kommen jetzt vom Commit `a12831136f41` (SHA-256 des Anwenderkatalogs `27a9d500…`, Resource-UUID `afe1c75e-8725-5df2-a57b-235d7d5236f4`). Pin, Hash, Resource-UUID und Kurzform sind synchron in allen Werkzeugen, in `constants.py` und in allen 229 Profilen ersetzt; `hilfsdateien/` bleibt als Provenienz unberührt. `check_pins.py` meldet alle Pins aktuell.

Der Nachweis, dass die Umbenennung keine Controls verschiebt: `stage_gpp` gegen den neuen Stand neu gerechnet, alle 56 Control-Pools sind identisch mit `hilfsdateien/zielobjekt_controls.json`.

## Profile mit neuem Namen

Die Profile der drei Kategorien heißen jetzt `mobile_endgeraete_*`, `faxanwendungen_*` und `archiv_*` — drei Kategorie-Profile und 22 Profile je ED2023-Baustein. Die Titel tragen den neuen Namen. Die Kategorie-Profile behalten ihre UUID (sie hängt an der Kategorie-UUID); die Baustein-Profile bekommen die UUID, die die Pipeline für den neuen Namen deterministisch vergibt. Wer ein Baustein-Profil per UUID referenziert, muss nachziehen; SSPs mit gepinnter Profil-URL laden weiter den alten Stand.

Bewusst nicht nachgezogen sind die KI-erzeugten Reifegrad-Texte der `_enhanced`-Profile; dort steht stellenweise noch der alte Wortlaut („Konfiguration für Faxe …“).

## SSP-Generator / Editor V5.16.0

* **Alte Namen bleiben lesbar.** Gespeicherte Arbeitsstände, Analysen und Profil-URLs mit `endgeraete`, `faxe` oder `datentraegerarchiv` werden auf die neuen Kategorien abgebildet.
* **OSCAL-Komponententyp.** Faxanwendungen ist jetzt `software` (BSI-Typ „Anwendungen“). Institutionsleitung ist `service` — bisher kam fälschlich `network` heraus, weil das Schlüsselwort „leitung“ für Standleitungen griff. Die Kategorie im Namen eines ED2023-Profils wird über den längsten passenden Präfix erkannt statt über das erste Wortsegment.
* **KI-Zuordnung von Assets.** Das Modell sieht je Kategorie zusätzlich die **Beispiele** aus der neuen Spalte; ohne sie fehlten nach dem Kürzen der Definitionen Signalwörter wie Server, Router oder Firewall. Für Mobile Endgeräte kommt der Hinweis dazu, dass auch stationäre Clients dorthin gehören: Die BSI-Definition nennt nur noch mobile Geräte, die ED2023-Client-Bausteine SYS.2.1 bis SYS.2.4 hängen über die unveränderte UUID aber weiter an dieser Kategorie. Beispiele und Hinweis stehen in den Kategoriezeilen, nicht im Prompt-Text — wer den Zuordnungs-Prompt in `config.html` angepasst hat, bekommt sie trotzdem.

## Weitere Werkzeuge und Pipeline

* **BSI → G++ Profil 0.12.0** gibt dem Modell bei der Klassifikation ebenfalls die Beispiele und löst alte Kategorienamen in Modellantworten auf.
* **SSP-Generator Edition 2023 (ED23 V1.6)** hat denselben Block für die Typzuordnung.
* **Pipeline (`Gpp-ai-tool`).** Die Namespace-CSV kommt jetzt vom Katalog-Commit statt von `main`. Vorher hätte ein Lauf die neue CSV gegen den gepinnten Katalog gelesen und die drei umbenannten Pools still geleert. `stage_match_bausteine` übergibt die Beispiele, `zielobjekte_stats.sh` liest die UUID aus der letzten Spalte statt fest aus Spalte 7.
* **`check_pins.py` v1.0.1** lässt `QS/fixtures/` wie `hilfsdateien/` aus: Die Analyse-Payloads der Messläufe vom 13.09. halten fest, gegen welchen Stand sie entstanden sind, und werden nicht umgepinnt.

## Nicht im Umfang von 4.2

* Ein QS-Lauf gegen die RECPLAST-Baseline (`QS/score_ssp.py`) für V5.16.0 steht aus. Er zeigt, ob die Beispiele die Zuordnung verbessern.
* Die Reifegrad-Texte der `_enhanced`-Profile (siehe oben).
* Die offenen Punkte aus 4.1 gelten weiter.

## Versionen der Anwendungen

| Anwendung | Version |
|---|---|
| gemeinsamer Kern (gpp-core.js) | 4 · Cache-Buster v4.1 |
| gemeinsames Stylesheet (gpp-core.css) | 2 · Cache-Buster v4.1 |
| Übersicht (index.html) | 1.8 |
| OSCAL Schema Validator | 1.11.2 |
| SSP-Generator / Editor (ssp_generator) | V5.16.0 |
| GS++ Explorer (GSpp-Viewer) | v9.8 · nur Pins |
| BSI → G++ Profil (Baustein_2_Profile) | 0.12.0 |
| SSP ausfüllen / Grundschutzcheck (ssp_ausfuellen) | v1.7.2 |
| Prüfung AP/AR (pruefung_ap_ar) | build 9.7.0 · nur Pins |
| POA&M-Generator | v2.5 · nur Pins |

Einzelwerkzeuge in `one-page-apps/` — eigenständig, ohne `gpp-core.js`, von der Datenbank unberührt:

| Anwendung | Version |
|---|---|
| SSP-Generator Edition 2023 | ED23 V1.6 |
| C5 → OSCAL Konverter | v1.1 |

## Hinweise zum Umstieg

- **Einmal mit Strg+F5 laden**, damit die Seiten mit den neuen Pins aus dem Cache kommen. Kern und Stylesheet sind unverändert.
- **Eigene Filter, Profile oder Auswertungen, die Kategorien beim Namen nennen** — „Endgeräte“, „Faxe“, „Datenträgerarchiv“ —, treffen gegen den neuen Katalog nichts mehr. Auf die neuen Namen umstellen oder über die UUID aus der Namespace-CSV gehen.
- **Wer die Namespace-CSV selbst liest:** über den Spaltennamen, nicht über die Position; die neue Spalte Beispiel verschiebt alles ab Spalte 3.
- Die Auslieferung bleibt `GS++-oscal-app.zip` (zwölf Dateien); eine einzelne HTML-Datei allein läuft nicht.
