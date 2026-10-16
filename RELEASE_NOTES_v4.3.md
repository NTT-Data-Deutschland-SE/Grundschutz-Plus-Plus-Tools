# Grundschutz++ OSCAL Tools – Version 4.3

Version 4.3 bringt die **Mindeststandards des BSI** nach § 44 Abs. 1 Satz 1 BSIG in die Sammlung: als OSCAL-Profile auf dem Anwenderkatalog Grundschutz++ samt Ergänzungskatalogen und aufgelösten Katalogen unter `mindeststandards/`, ein Einzelwerkzeug, das sie aus den IT-Grundschutz-Referenztabellen des BSI erzeugt, und den **SSP-Generator / Editor V5.17.0**, der aktivierte Mindeststandards als Overlay vor der Modellierung über den Katalog legt.

## Neues Einzelwerkzeug: Mindeststandard → OSCAL

`one-page-apps/mindeststandard-oscal.html` (build 1.4.1) veröffentlicht einen Mindeststandard des BSI (§ 44 Abs. 1 Satz 1 BSIG) als OSCAL-Profil auf dem Anwenderkatalog Grundschutz++ (Pin `a128311`) und löst dieses Profil deterministisch zu einem Katalog auf. Grundlage ist die IT-Grundschutz-Referenztabelle, die das BSI zu den meisten Mindeststandards als Excel liefert (Nr., Bezeichnung, Absatz, Anforderungstext, Kompendium-Referenz); das Werkzeug liest sie ohne Bibliothek. Wo es keine Tabelle gibt (HV-Benchmark kompakt, Nutzerpflichten NdB), liest es das PDF des Mindeststandards: Fußnoten fallen über die Schriftgröße weg, ein deterministischer Parser nimmt Nummer, Titel und Absätze wortgleich aus der Dokumentstruktur, das Modell prüft diese Lesung je Seitenabschnitt gegen den Text (fehlende Absätze ergänzt es als KI-Fund, verstümmelte meldet es als Befund), und erst wenn die Struktur nicht reicht (Vorgaben in Tabellen), extrahiert das Modell die Absätze selbst abschnittsweise mit eigenem Prompt. Ein Wechsel des Mindeststandards in der Auswahl räumt die alte Tabelle samt Zuordnungen nach Rückfrage weg; Lauf und Export sind gesperrt, solange Tabelle und gewählter Standard nicht zusammenpassen. Jeder Absatz wird eine Gruppe mit dem Originaltext, die zugeordneten Controls stammen unverändert aus dem Anwenderkatalog, und alle Anpassungen laufen über `modify`: `set-parameters` für Parameterwerte, `alters` für Statement-Ersetzungen (etwa SOLLTE → MUSS, wenn der Mindeststandard es verlangt), Ergänzungen als Part `mindeststandard`, entfernte Guidance und zusätzliche Props.

Prüfen, Zuordnen und Anpassen macht das Modell (Gemini oder OpenRouter), ein Aufruf je Nummer des Mindeststandards mit allen ihren Absätzen: Es sieht wahlweise den ganzen Anwenderkatalog auf ID, Titel, Modalverb, Statement und Parameter gestutzt (stabiler Präfix für das implizite Caching) oder eine Vorauswahl aus der Brücke Referenztabelle × BSI-GSMap und Stichwort-Treffern, und liefert per JSON-Schema je Absatz die Einordnung, Zuordnungen mit Relation und Konfidenz und die Anpassungen je Control; je Nummer, wo nichts passt, neue Controls mit Praktik, Zielobjektkategorien aus dem Katalogvokabular und verwandten Controls. Die Regeln dafür sind nach vier Probeläufen (TLS 2.4, PD 2.1, Cloud 2.1, MDM 2.0 mit gemini-4-argon) eng gefasst: Ergänzung vor neuem Control, keines für KANN-Absätze ohne eigenen Gegenstand, mehrere Absätze derselben Nummer zum selben Gegenstand ergeben ein Control, ein Statement trägt ein Modalverb; Verstöße und verlorene Parameter-Platzhalter werden deterministisch markiert, Abschwächungen von MUSS verworfen. Neue Controls landen in einem Ergänzungskatalog (nach Praktik gruppiert, `target_object_categories` am Statement, `alt-identifier`, Querverweise `rel="related"`), den das Profil als zweiten Import mit SHA-256 und `merge.combine.method = use-first` zieht, denn ein Profil kann keine Controls definieren. Ein zuschaltbarer Checker (zweites Modell) urteilt je Zuordnung und je neuem Control und ändert nichts; die Sammelübernahme nimmt ab einer wählbaren Konfidenz und überspringt Abgelehntes. Fremde Control-IDs, Parameter-IDs, Absatz-Labels, Praktiken und Kategorien werden verworfen und im Log genannt. Profil, Ergänzungskatalog und Katalog validieren gegen die OSCAL-1.2.2-Schemas; Back-Matter mit Hashes von Katalog, GSMap, Referenztabelle und Ergänzungskatalog; Katalog mit `rel="source-profile"` und `resolution-tool`. Die neun Mindeststandards der BSI-Übersicht sind mit PDF- und Tabellen-Links hinterlegt. Die Exporte je Mindeststandard liegen unter `mindeststandards/` mit Prüfskript (`pruefe_export.py`); was das Modell vorschlägt, wird erst nach der Review Teil des Profils.


## SSP-Generator / Editor V5.17.1: Mindeststandards als Overlay

Im Abschnitt „Methodik & Assets“ gibt es den Block **2b. Mindeststandards des BSI**: ein Dropdown mit den gepinnten Profilen aus `mindeststandards/` (Commit `22ed7b6` plus SHA-256 je Datei in `MST_PINNED`; weicht die geladene Datei vom Hash ab, wird nichts übernommen), dazu ein Feld für eine beliebige Profil-URL. Aktive Mindeststandards stehen als Chips mit Controlzahl, Herkunft (gepinnt oder URL) und Entfernen-Knopf darunter. Ein aktivierter Mindeststandard legt sich **vor der Modellierung** über den Control-Pool: `set-parameters` setzen die Parameterwerte, `alters` ersetzen Statements, heben Modalverben an (ein so entstandenes MUSS lässt sich im Tailoring nicht mehr entfernen) und hängen die Ergänzungen des Mindeststandards an; die Controls seines Ergänzungskatalogs kommen in den Pool. Danach läuft die Modellierung wie bisher, und alle Controls des Mindeststandards landen im Profil und im SSP, gebündelt in einer Komponente „Mindeststandard: PD 2.1“ mit Link auf die gepinnte Profil-Resource und den Absätzen je Control.

Im erzeugten Profil stehen die Mindeststandard-Profile **vor** dem Anwenderkatalog, mit `merge.combine.method = use-first`: In der Auflösung bleibt jedes Control genau einmal übrig, in der Fassung des Mindeststandards. Die eigenen Anpassungen des Generators (Tailoring) kommen wie bisher als `alters` obendrauf. Mehrere Mindeststandards gelten in der Reihenfolge ihrer Aktivierung; ändern zwei denselben Parameter oder dasselbe Statement unterschiedlich, gewinnt der erste, und der Generator meldet den Konflikt im Block und im Log. Ergänzungen sind additiv. Geltungsbereich ist der ganze Informationsverbund; Varianten je Zielobjekt lassen sich in einem OSCAL-Profil nicht ausdrücken, weil `alters` je Control-ID gelten.

Der Ladeweg prüft die Importkette des Mindeststandard-Profils: Der Anwenderkatalog muss dem Pin der Sammlung entsprechen (sonst Warnung „anderer Katalogstand“), der Ergänzungskatalog wird relativ zur Profil-URL geholt und muss den im Profil hinterlegten SHA-256 tragen, sonst wird nichts übernommen. Beim Wiederherstellen eines Arbeitsstands erkennt der Generator Mindeststandard-Profile an ihren Import-Resourcen und baut das Overlay neu auf; Deaktivieren stellt den Katalogstand wieder her.

## Handbuch und Skill: Profilauflösung

Was die Mindeststandard-Arbeit über OSCAL-Profilauflösung gelehrt hat, steht jetzt im **Handbuch, Kapitel 3.15** („Profile übereinanderlegen: Auflösung in der Praxis“, Kapitel 3 damit v0.14): Ein Profil definiert keine Controls, deshalb der Ergänzungskatalog als zweiter Import; ohne `merge/combine` gilt laut Spezifikation `keep`, deshalb immer `combine.method = use-first` und die Import-Reihenfolge Mindeststandard vor Anwenderkatalog; `insert-controls` in `merge/custom` platziert, ein Control steht nur einmal, weitere Zuordnungen verlinken; Kinder kommen nur mit `with-child-controls`; Statements werden per `removes/by-id` und `adds/position: starting` unter gleicher ID ersetzt; Links auf nicht ausgewählte Controls bleiben nach der Auflösung stehen; ein Pin-Wechsel ist eine Neuauflösung (`mindeststandards/repin.py`). **Anhang D** bekommt D37: Das generierte JSON-Schema 1.2.2 kennt `merge/combine/@method` nicht, das Metaschema schon (Fund gegen usnistgov/OSCAL).

Der Skill **gs-plusplus-katalogarbeit** (`skills/gs-plusplus-katalogarbeit.skill`) hat dazu die neue **Grundregel 9** („Profile auflösen nach Spezifikation, nicht nach Gefühl“) und die Referenz `references/profilaufloesung.md` mit Checkliste für eigene Profile, Overlays und Pin-Wechsel. Wer den Skill installiert hat, importiert die neue Datei einmal neu.

## Versionen der Anwendungen

| Anwendung | Version |
|---|---|
| gemeinsamer Kern (gpp-core.js) | 4 · Cache-Buster v4.1 |
| gemeinsames Stylesheet (gpp-core.css) | 2 · Cache-Buster v4.1 |
| Übersicht (index.html) | 1.8 |
| OSCAL Schema Validator | 1.11.2 |
| SSP-Generator / Editor (ssp_generator) | V5.17.1 |
| GS++ Explorer (GSpp-Viewer) | v9.8 |
| BSI → G++ Profil (Baustein_2_Profile) | 0.12.0 |
| SSP ausfüllen / Grundschutzcheck (ssp_ausfuellen) | v1.7.2 |
| Prüfung AP/AR (pruefung_ap_ar) | build 9.7.0 |
| POA&M-Generator | v2.5 |

Einzelwerkzeuge in `one-page-apps/` — eigenständig, ohne `gpp-core.js`, von der Datenbank unberührt:

| Anwendung | Version |
|---|---|
| SSP-Generator Edition 2023 | ED23 V1.6 |
| C5 → OSCAL Konverter | v1.1 |
| Mindeststandard → OSCAL | build 1.4.1 |

## Hinweise zum Umstieg

- **Einmal mit Strg+F5 laden.** Kern und Stylesheet sind unverändert.
- Die Mindeststandard-Profile lädt der Generator vom Pin `MST_PIN_COMMIT` (22ed7b6) mit SHA-256 je Datei. Neue Exporte heißen: Commit und Hashes im Generator nachziehen, sonst weist er die Datei ab.
- Sieben der acht Stände wurden mit build 1.2.1 gegen den Anwenderkatalog 4e117794 erarbeitet und mit `mindeststandards/repin.py` mechanisch auf a128311 umgestellt (Import, Back-Matter, Querverweise, Kategorienwerte; Katalog neu aufgelöst). Das Skript prüft vorher, dass sich die verwendeten Controls nur in den drei umbenannten Zielobjektkategorien unterscheiden; siehe `mindeststandards/README.md`, Abschnitt Stand.
- Die Auslieferung bleibt `GS++-oscal-app.zip` (zwölf Dateien); eine einzelne HTML-Datei allein läuft nicht.
