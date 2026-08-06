# Einzelwerkzeuge (one-page-apps)

Hier liegen Werkzeuge, die **nicht** Teil des durchgängigen Arbeitsablaufs in
[`GS++-oscal-app`](../GS++-oscal-app/) sind. Sie lösen jeweils eine abgegrenzte
Aufgabe, arbeiten nicht auf dem gemeinsamen Artefakt-Set und lassen sich
einzeln benutzen.

**Jede Datei ist für sich vollständig.** Eine einzelne HTML-Datei genügt: keine
gemeinsame Bibliothek, keine Nachbardatei, kein Build. KI-Zugang, Laufzeitwerte
und Prompts werden im Werkzeug selbst gesetzt und liegen im `localStorage`
dieses Browsers — die zentrale
[`config.html`](../GS++-oscal-app/config.html) der Sammlung gilt hier **nicht**.
Ergebnis ist jeweils eine heruntergeladene Datei; wer damit in der Sammlung
weiterarbeiten will, lädt sie dort unter „Artefakte" in ein Set.

Bei CORS-Fehlern über `file://` hilft ein lokaler Server:
`python -m http.server`.

## [SSP-Generator Edition 2023](./ssp_generator_ed23.html)

Erzeugt einen OSCAL-1.2.2-SSP gegen den **BSI IT-Grundschutz Edition 2023**
statt gegen den G++-Anwenderkatalog: Metadaten, ISMS- und Asset-Auswahl,
Tailoring über die Bausteinstruktur, Risikoanalyse und OSCAL-Export.

Der Ablauf entspricht dem [SSP-Generator](../GS++-oscal-app/ssp_generator.html)
der Hauptsammlung; wer mit Grundschutz++ arbeitet, nimmt jenen. Dieser hier ist
für Häuser gedacht, die (noch) auf der Edition 2023 aufsetzen.

## [YAML → OSCAL Konverter (C5:2026)](./c5-oscal-converter.html)

Wandelt die YAML-Kriteriendateien des BSI C5:2026 in einen
NIST-OSCAL-1.2.2-Katalog um. Das Werkzeug ist **vollständig deterministisch**:
Parsen, Gruppieren, die Joins zwischen Kriterium und Guidance, UUID-Vergabe und
der Aufbau der OSCAL-Hülle passieren komplett in JavaScript. Es gibt deshalb
kein Feld für einen API-Schlüssel, keine Modellauswahl und keine Prompts —
dieselbe Eingabe erzeugt bei jedem Lauf byteweise dasselbe Ergebnis. Die
YAML-Bibliothek ist eingebettet, das Werkzeug läuft auch offline.

Trotz des Namens ist es im Kern ein YAML-nach-OSCAL-Konverter: Wer eine andere
Kriteriensammlung in derselben YAML-Struktur vorliegen hat, kann es dafür
mitbenutzen.
