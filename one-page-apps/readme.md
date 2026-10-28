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

**NG-Bausteine (ab ED23 V1.7).** Der gepinnte Katalog enthält neben den 111
Bausteinen des BSI 12 nutzergenerierte Bausteine von NTT DATA (APP.4.5, APP.4.7,
APP.4.8, APP.4.9, APP.4.10, SYS.1.10, SYS.1.11, SYS.1.2.4, SYS.5.1, ORP.6,
OPS.1.1.8, DER.7), die der Katalog selbst nicht markiert. Das Werkzeug führt
sie als Konstante `ED23_NG_BAUSTEINE` (Differenz der Baustein-IDs zur reinen
BSI-Datei am selben Commit), zeigt an Bausteinen, Assets und Anforderungen ein
NG-Badge, nennt sie der KI-Zuordnung als `[NG]`, schreibt in Profil und SSP die
Props `herkunft=NG` bzw. `ed23-baustein` (Namespace
[`ed23-baustein`](../Dokumentation/namespaces/ed23_baustein_props.md)) und
prüft die Liste beim Laden gegen den Katalogstand; „NG-Liste prüfen“ in der
Rail lädt auf Wunsch die BSI-Datei (15 MB) und vergleicht.

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

## [Mindeststandard → OSCAL](./mindeststandard-oscal.html)

Veröffentlicht einen **Mindeststandard des BSI** (§ 44 Abs. 1 Satz 1 BSIG) als
OSCAL-Profil und als daraus aufgelösten Katalog, beides auf dem
**Anwenderkatalog Grundschutz++** der Stand-der-Technik-Bibliothek. Jede
Anforderung des Mindeststandards wird eine Gruppe mit dem Originaltext als Part
`overview`, darunter stehen die zugeordneten Controls des Anwenderkatalogs, und
alle Anpassungen laufen über `modify` des Profils (`set-parameters` für
Parameterwerte, `alters` mit `removes`/`adds` für Statement-Ersetzungen,
Modalverb-Anhebung, Ergänzungen, entfernte Guidance und Props). Wo der
Anwenderkatalog kein passendes Control hat, entsteht ein **neues Control in
einem Ergänzungskatalog** (ein Profil kann selbst keine Controls definieren):
mit Praktik des Anwenderkatalogs als Gruppe, Zielobjektkategorien am Statement
(damit der SSP-Generator sie in Anforderungspakete aufnimmt), Querverweisen
`rel="related"` auf verwandte bestehende Controls und `alt-identifier`; das
Profil importiert ihn als zweiten Import mit SHA-256 und
`merge.combine.method = use-first`. Der aufgelöste Katalog ist die deterministische
Auflösung des Profils und trägt `rel="source-profile"` und `resolution-tool`.

Ablauf:

1. **Mindeststandard wählen.** Die Liste entspricht der Übersichtsseite des BSI
   (PD 2.1, TLS 2.4, Webbrowser 3.0, externe Cloud-Dienste 2.1, MDM 2.0,
   Videokonferenzdienste 1.0, ISMS ITKB 1.0a, HV-Benchmark kompakt 2.0,
   Nutzerpflichten NdB 3.0 als VS-NfD ohne öffentliche Dateien) mit Links auf
   PDF und IT-Grundschutz-Referenztabelle; eigene Stände sind frei eingebbar.
2. **Referenztabelle ablegen.** Das BSI liefert zu fast jedem Mindeststandard
   eine Excel-Tabelle mit Nr., Bezeichnung, Absatz, Anforderungstext und der
   Referenz auf Anforderungen des IT-Grundschutz-Kompendiums. Das Werkzeug liest
   die xlsx ohne Bibliothek (ZIP, `DecompressionStream`, `DOMParser`), erkennt
   das Modalverb und bildet aus den Nummern die Abschnitte. Die BSI-Downloads
   erlauben keinen Browserabruf, deshalb per Datei; ihr SHA-256 steht in der
   Back-Matter. **Gibt es keine Tabelle** (HV-Benchmark kompakt in keiner Version,
   Nutzerpflichten NdB nur im geschützten Bereich), nimmt das Werkzeug das
   **PDF des Mindeststandards**: pdf.js kommt bei Bedarf vom CDN, Fußnoten
   fallen über die Schriftgröße weg, und ein deterministischer Parser liest
   Nummer, Titel und Absätze (a), b), i)) aus der Dokumentstruktur; die Texte
   sind dann wortgleich mit dem Dokument. Mit Schlüssel prüft das Modell diese
   Lesung anschließend je Seitenabschnitt gegen den PDF-Text (Maker ist der
   Parser, Checker das Modell): fehlende Absätze werden ergänzt und als KI-Fund
   markiert, verstümmelte oder falsch zugeordnete Texte werden als Befund
   gemeldet, nichts wird umformuliert. Reicht die Struktur nicht, etwa bei
   Vorgaben in Tabellen wie den Mindestreifegraden des HV-Benchmark, extrahiert
   das Modell die Absätze selbst in Abschnitten zu sechs Seiten (eigener,
   editierbarer Prompt); „PDF mit KI neu auslesen“ erzwingt diesen Weg. Kompendium-Referenzen gibt es auf dem PDF-Weg nicht, die Brücke
   entfällt dann. Deterministisch vorab: Die Kompendium-Referenzen werden über das
   amtliche **BSI-GSMap ITGS 2023 → Grundschutz++** (gleicher Pin wie der
   Katalog, Auflösung über die `alt-identifier`-UUID) zu Brücken-Kandidaten.
3. **KI: prüfen, zuordnen, anpassen.** „KI: alle Anforderungen“ schickt jede
   Nummer des Mindeststandards mit allen ihren Absätzen in einem Aufruf an das
   Modell (Gemini oder OpenRouter, Schlüssel nur im Speicher). Als Kandidaten
   bekommt es wahlweise den **ganzen Anwenderkatalog** (1000 Zeilen: ID, Titel,
   Modalverb, Statement, Parameter, rund 180 k Zeichen als stabiler Präfix,
   damit das implizite Caching ab dem zweiten Aufruf greift) oder eine
   Vorauswahl aus Brücke und Stichwort-Treffern. Das Modell liefert per
   JSON-Schema je Absatz: die **Prüfung** (Art, Modalverb, ob überhaupt ein
   Control nötig ist), **Zuordnungen** mit Relation, Konfidenz und Begründung,
   je Zuordnung die **Anpassungen** (Parameterwerte, Modalverb-Anhebung, neuer
   Statement-Wortlaut, Ergänzung, Guidance entfernen); und je Nummer bei Bedarf
   **neue Controls** mit Praktik, Zielobjektkategorien aus dem Vokabular des
   Anwenderkatalogs (39 Werte an 636 Statements, leer nur für den
   Sicherheitsprozess), verwandten Controls und den Absätzen, die sie decken. Die Regeln sind bewusst eng: eine Ergänzung an einem zugeordneten
   Control geht vor einem neuen Control, kein neues Control für KANN-Absätze
   ohne eigenen Gegenstand, mehrere Absätze derselben Nummer zum selben
   Gegenstand ergeben ein Control, ein Statement trägt genau ein Modalverb.
   IDs außerhalb der gesendeten Kandidaten, fremde Parameter-IDs, unbekannte
   Absatz-Labels und Praktiken werden verworfen; neue Statements, die einen
   Parameter-Platzhalter verlieren oder mehrere Modalverben tragen, werden
   markiert; Abschwächungen von MUSS werden verworfen. Absätze ohne
   Buchstaben bekommen je Nummer eindeutige Labels: die Kennung aus dem
   Titel (etwa `I.1` beim HV-Benchmark), sonst `#1`, `#2`; das Modell
   antwortet mit genau diesen Labels. Optional urteilt ein
   **Checker** (zweites Modell, Argon empfohlen) je Zuordnung und je neuem
   Control mit bestätigt, fraglich, abgelehnt oder unsicher; er ändert nichts,
   sein Urteil steht neben dem Vorschlag und wandert als Remark in die Herkunft.
4. **Review und Übernahme.** Je Anforderung zeigt die Detailansicht Prüfung,
   Vorschläge mit Anpassungen und Checker-Urteil, Brücken-Kandidaten und das
   vorgeschlagene neue Control. „Vorschläge übernehmen“ nimmt alles ab der
   eingestellten Konfidenz, vom Checker Abgelehntes ausgenommen (auch bei neuen
   Controls); Absätze, die laut Prüfung kein Control brauchen, bekommen einen
   begründeten Vermerk. Ein neues Control, das mehrere Absätze einer Nummer
   deckt, hängt am ersten davon und trägt die Nummer in der ID; die anderen
   Absätze verweisen per `rel="related"` darauf.
   Alles bleibt von Hand änderbar: Suche im Katalog, Control-Karte mit
   Parametern, Statement, Ergänzung, Props; neues Control mit Praktik und
   Querverweisen. Jede Zuordnung trägt ihre Herkunft als Prop
   `mindeststandard-anforderung` mit Remark (Brücke, KI mit Konfidenz und
   Checker-Urteil, oder manuell).
5. **Export-Paket.** Ergänzungskatalog (falls neue Controls), OSCAL-Profil und
   aufgelöster Katalog mit gleichen Hashes; dazu der Arbeitsstand als JSON.

Ein Control darf im aufgelösten Katalog nur einmal vorkommen: Es steht unter
der ersten Anforderung, die es zuordnet; weitere Anforderungen verweisen mit
`rel="related"` darauf. Kind-Controls werden nur aufgenommen, wenn sie selbst
zugeordnet sind, und dann flach eingefügt. Der Export prüft offene
Anforderungen, Parameter ohne Wert, SOLLTE-Controls unter MUSS-Anforderungen
ohne Anhebung, fragliche Checker-Urteile, neue Controls ohne Praktik und
zielobjektbezogene neue Controls ohne Zielobjektkategorie.
Quellen: Anwenderkatalog und GSMap sind auf den Commit `160c177d` gepinnt und
werden per SHA-256 geprüft; ein anderer Katalogstand geht nur per Datei und
wird in der Back-Matter als solcher ausgewiesen. Arbeitsstände liegen als
Autosave im `localStorage` und als JSON-Datei. Bei CORS-Fehlern über `file://`
hilft `python -m http.server`.

Die Exporte gehören nach [`mindeststandards/`](../mindeststandards/);
das Prüfskript dort validiert Profil, Ergänzungskatalog und Katalog gegen die
OSCAL-Schemas und prüft Imports, Hashes, Eindeutigkeit und Links.

Fachlich ist das Ergebnis eine **Auslegung**: Das GSMap hat Status draft, die
Referenztabellen zu Cloud, MDM und Videokonferenzen verweisen auf die
Editionen 2022 und 2021, die meisten Anforderungen tragen keine
Kompendium-Referenz (bei PD 2.1 sind es 23 von 57), und was das Modell
zuordnet oder neu formuliert, ist erst nach der Review Teil des Profils.
