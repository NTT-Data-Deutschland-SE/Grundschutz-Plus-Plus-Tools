# Grundschutz++ OSCAL Tools – Version 5.1

Version 5.1 zieht die Sammlung auf den **Build 2026-10-22 der Stand-der-Technik-Bibliothek** (Commit `160c177d`, Merge des BSI-PR #115 vom 2026-10-23): Anwenderkatalog-Pin, SHA-256 und Resource-UUID in allen Werkzeugen, in der Pipeline und in allen 267 Profilen, die acht Mindeststandard-Stände neu aufgelöst, und der GS++ Explorer liest den Kernel-Katalog an seinem neuen Ort. Am Anwenderkatalog selbst ändert sich wenig (1000 Controls, keine ID entfallen oder hinzugekommen), aber die Control-Klasse der 901 Kernel-Controls heißt jetzt `BSI-Stand-der-Technik-Kernel`, und vier BER.5-Controls sind umformuliert.

## Was sich in der Bibliothek geändert hat (a1283113 → 160c177d)

- **Kernel konsolidiert.** Der Kernel-Quellkatalog liegt jetzt unter `control_layer/Kernel/BSI-Stand-der-Technik-Kernel-catalog.json`; die beiden Dateien unter `control_layer/Grundschutz++/sources/catalogs/Kernel/` (prop-lose Basisfassung und G0-Variante) sind entfallen, die alte URL liefert 404. Die neue Datei entspricht der früheren G0-Variante mit Schutzziel-Props (`confidentiality`, `integrity`, `availability`, `authenticity`) und `threats`. Die Control-Klasse aller 901 Kernel-Controls wurde von `BSI-Stand-der-Technik-Kernel-G0` auf `BSI-Stand-der-Technik-Kernel` umbenannt, auch im aufgelösten Anwenderkatalog.
- **Vier Controls umformuliert.** BER.5.1 („Ausgabe, Registrierung und Zuordnung“), BER.5.1.1 („Identität der vorgesehenen Empfänger“), BER.5.2 („Zurücksetzung und Ersetzung von Authentifizierungsmitteln“) und BER.5.13 („Identität vor Zurücksetzung und Ersetzung“) tragen neue Titel und Statements; in BER.5.13 ist „Berechtigungsmitteln“ zu „Authentifizierungsmitteln“ korrigiert. IDs, `alt-identifier`, Parameter-IDs und Prop-Namen sind stabil, kein Profil der Sammlung verweist auf eine entfallene ID.
- **Lieferketten-Profil.** Es importiert denselben Kernel-Katalog; sein aufgelöster Katalog trägt deshalb auf allen 146 Controls die fünf Props, die der früher referenzierten prop-losen Datei fehlten. `documentation/namespaces/result.csv` kennt zusätzlich „Authentifizierungsmittel“.
- Methodik- und Risikokatalog nur in den Metadaten geändert, die GSMap byte-identisch.

## Repin: Anwenderkatalog 160c177d in Werkzeugen, Pipeline und Profilen

- Pin `160c177db6c84d3c621fff614559943b1de8c600`, SHA-256 `7c3acebd…`, Resource-UUID `c45ef8e9-7d97-5035-b3df-6af73bf31126` (uuid5 der gepinnten URL) und die Kurzform `160c177db6c8` stehen synchron in den sechs Werkzeugen der Sammlung, in `one-page-apps/mindeststandard-oscal.html`, in `Gpp-ai-tool/src/constants.py` und in allen 267 Profilen (194 ED23-Baustein-Profile, 73 Praktiken- und Zielobjektprofile): byte-genaue Token-Ersetzung wie bei 9c2e444 und 26b9200. `hilfsdateien/` und `QS/fixtures/` bleiben als Provenienz auf ihren alten Ständen.
- **NG-Ergänzungskatalog.** Seine 186 Links auf den Anwenderkatalog zeigen auf den neuen Pin; sein SHA-256 ist dadurch neu (`d3f46881…`) und in den 76 Profilen nachgezogen, die ihn importieren (fail closed bleibt). `ED23-Baustein-profile/pruefe_export.py` gegen den neuen Anwenderkatalog: 194 Profile, 69 NG-Controls, 0 Befunde.
- **Mindeststandards.** Alle acht Stände mit `mindeststandards/repin.py` umgestellt und neu aufgelöst. Das Skript kennt die Klassenumbenennung jetzt als mechanische Änderung (vorher hätte es beim ersten Kernel-Control abgebrochen) und bekommt `--accept-changed <IDs>` für Controls, die upstream umformuliert wurden: Der MDM-Stand übernimmt BER.5.2 in der neuen Fassung, sein ersetzendes MUSS-Statement bleibt unverändert; die Remarks von Profil und Ergänzungskatalog halten beides fest. `pruefe_export.py`: 0 Befunde; `repin.py --check-only`: Resolver und Textform identisch. Die SHA-256-Werte der acht Profile in `MST_PINNED` des SSP-Generators sind nachgezogen.
- `Gpp-ai-tool/scripts/check_pins.py`: alle 14 Quellen AKTUELL (für die Katalogpfade liefert die API den Inhalts-Commit 9fb19de7 statt des Merges, Bytes identisch), 9/9 SHA-256-Konstanten passen.

## GS++ Explorer v9.10: Kernel-Katalog am neuen Ort

`STDT_PIN` für Methodik, Kernel und Risikomanagement auf `160c177d`; die Kernel-Quelle (`GPP_SOURCES`, Schnellauswahl, Pin-Übersicht in `config.html`) zeigt auf `control_layer/Kernel/…`. Da der neue Kernel-Katalog der früheren G0-Variante entspricht, zeigen alle 901 Kernel-Cards jetzt Schutzziel-Badges und `threats`-Tags; der Klassenfilter kennt nur noch `BSI-Stand-der-Technik-Kernel`.

## Handbuch 3 (v0.16)

3.13 auf die Kernel-Konsolidierung berichtigt: Ort und `rlink` des Kernel-Katalogs, Wegfall der G0-Variante, die neue Control-Klasse (die bisherige Aussage, die Klasse laute weiterhin `…-G0`, war falsch) und die Props des Lieferketten-Katalogs. Die Änderungszeile nennt 3.16 (Release 5.0) als Teil dieses Standes. `verify_kapitel.py` gegen den Anwenderkatalog 160c177d: OK (58 IDs).

## Sonstiges

- `mindeststandards/README.md` (Abschnitte „Pin wechseln“ und „Stand“) und `one-page-apps/readme.md` nennen den neuen Pin; `GS++-oscal-app/readme.md` zählt die 267 gepinnten Profile.
- Der SdT-Drift-Watcher (Cloud-Routine, täglich 07:00 Uhr), dessen Bericht vom 2026-10-24 dieses Release ausgelöst hat, greift mit seinem Prop-Check jetzt nach `GS++-oscal-app/*.html` und `one-page-apps/*.html` statt ins Leere.

## Versionen der Anwendungen

| Anwendung | Version |
|---|---|
| gemeinsamer Kern (gpp-core.js) | 4 · Cache-Buster v4.1 |
| gemeinsames Stylesheet (gpp-core.css) | 2 · Cache-Buster v4.1 |
| Übersicht (index.html) | 1.8 |
| OSCAL Schema Validator | 1.11.2 |
| SSP-Generator / Editor (ssp_generator) | V5.18.1 · Katalog-Pin, MST-Hashes, Selbst-Pin |
| GS++ Explorer (GSpp-Viewer) | v9.10 |
| BSI → G++ Profil (Baustein_2_Profile) | 0.12.0 · Katalog-Pin, Selbst-Pin |
| SSP ausfüllen / Grundschutzcheck (ssp_ausfuellen) | v1.7.2 · Katalog-Pin, Selbst-Pin |
| Prüfung AP/AR (pruefung_ap_ar) | build 9.7.0 · Katalog-Pin, Selbst-Pin |
| POA&M-Generator | v2.5 · Katalog-Pin |
| Pipeline (Gpp-ai-tool) | 5.0.1 · Katalog-Pin |

Einzelwerkzeuge in `one-page-apps/`: eigenständig, ohne `gpp-core.js`, von der Datenbank unberührt:

| Anwendung | Version |
|---|---|
| SSP-Generator Edition 2023 | ED23 V1.7 · nur Selbst-Pin |
| C5 → OSCAL Konverter | v1.1 · nur Selbst-Pin |
| Mindeststandard → OSCAL | build 1.4.1 · Katalog-Pin |

## Hinweise zum Umstieg

- **Einmal mit Strg+F5 laden.** Kern und Stylesheet sind unverändert.
- Die Selbst-Pins (`GPP_TOOLS_PIN_COMMIT`, `MST_PIN_COMMIT`, `GPPT_PIN`) zeigen auf `7fc5416`, Commit 1 dieses Releases mit den umgepinnten Profilen (zweiter Commit „Selbst-Pin auf 7fc5416“, ZIP neu gebaut).
- Neu erzeugte Profile, SSPs, Prüfpläne und POA&Ms nennen in ihrer Back-Matter die neue Katalog-Resource (URL mit `160c177d`, SHA-256 `7c3acebd…`, UUID `c45ef8e9…`). Ältere Dateien verweisen weiter auf den Stand `a1283113`, der unter seiner Commit-URL erreichbar bleibt.
- Wer den MDM-Stand nutzt: BER.5.2 heißt jetzt „Zurücksetzung und Ersetzung von Authentifizierungsmitteln“; die Zuordnungen MDM.2.2.04 a/b und MDM.2.6.18 a hängen unverändert daran.
- Die Auslieferung bleibt `GS++-oscal-app.zip` (zwölf Dateien); eine einzelne HTML-Datei allein läuft nicht.
