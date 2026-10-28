# Mindeststandards des BSI als OSCAL

Hier liegen die Mindeststandards des BSI nach § 44 Abs. 1 Satz 1 BSIG als
OSCAL-Artefakte auf dem **Anwenderkatalog Grundschutz++** der
Stand-der-Technik-Bibliothek, erzeugt mit dem Einzelwerkzeug
[`one-page-apps/mindeststandard-oscal.html`](../one-page-apps/mindeststandard-oscal.html).

Je Mindeststandard gibt es bis zu vier Dateien mit gemeinsamem Stamm
`mindeststandard-<kurz>-<version>`:

| Datei | Inhalt |
|---|---|
| `….profile.json` | OSCAL-Profil: importiert den gepinnten Anwenderkatalog (und, falls vorhanden, den Ergänzungskatalog), bildet mit `merge.custom` je Abschnitt und Absatz des Mindeststandards eine Gruppe mit dem Originaltext und passt die Controls über `modify` an (`set-parameters`, `alters`) |
| `….ergaenzungskatalog.json` | nur wenn der Anwenderkatalog für einen Absatz kein Control hat: neue Controls, nach Praktik gruppiert, mit `alt-identifier`, Querverweisen `rel="related"` und dem Absatz, den sie decken; das Profil importiert ihn mit SHA-256 |
| `….catalog.json` | der aus dem Profil deterministisch aufgelöste Katalog (`rel="source-profile"`, `resolution-tool`), zum direkten Lesen und Weiterverarbeiten |
| `….arbeitsstand.json` | der Arbeitsstand des Werkzeugs (Anforderungen, Zuordnungen, Anpassungen, Modellvorschläge mit Checker-Urteilen) zum Wiederaufnehmen und Nachvollziehen; für die bisher abgelegten Stände nicht mitgeliefert |

## Herkunft und Verbindlichkeit

Die Anforderungstexte stammen aus den IT-Grundschutz-Referenztabellen des BSI
(Excel je Mindeststandard) oder, wo es keine Tabelle gibt (HV-Benchmark), aus
dem PDF des Mindeststandards; die Controls unverändert aus dem Anwenderkatalog
(Commit und SHA-256 stehen in der Back-Matter des jeweiligen Profils, siehe
Abschnitt Stand). Die Zuordnung ist zweistufig:
Kompendium-Referenzen der Tabelle gehen deterministisch über das amtliche
BSI-GSMap ITGS 2023 → Grundschutz++ (Status draft); alles Übrige, die
Anpassungen und die neuen Controls hat ein Sprachmodell vorgeschlagen und ein
Bearbeiter übernommen. Jede Zuordnung trägt ihre Herkunft als Prop
`mindeststandard-anforderung` mit Remark (Brücke mit Mapping-ID, Modell mit
Konfidenz und Checker-Urteil, oder manuell). Die Statements neuer Controls sind
Formulierungen auf Grundlage des Mindeststandards, keine amtlichen Texte des
BSI. Das Ergebnis ist damit **Auslegung**, kein Dokument des BSI.

## Prüfen

```bash
PYTHONUTF8=1 uv run --no-project --with jsonschema --with regex python -I mindeststandards/pruefe_export.py mindeststandards
```

Das Skript prüft je Stamm: Profil, Ergänzungskatalog und Katalog gegen die
OSCAL-1.2.2-Schemas aus `hilfsdateien/OSCAL_Schemas`, dass jeder Import des
Profils auf eine Back-Matter-Resource zeigt, dass der Hash des
Ergänzungskatalogs in der Back-Matter mit der Datei übereinstimmt, dass jedes
Control im Katalog nur einmal vorkommt und dass Fragment-Links an Controls des
Ergänzungskatalogs auf vorhandene Controls zeigen. Links, die Controls aus dem
Anwenderkatalog mitbringen und die auf nicht ausgewählte Controls zeigen, zählt
es nur als Hinweis. Eine Lücke des generierten JSON-Schemas 1.2.2 nimmt es aus:
dort fehlt `merge/combine/@method`, das Metaschema 1.2.2 kennt das Attribut
(`use-first`, `keep`). Exit 0 heißt: alles stimmt.

## Pin wechseln

```bash
uv run --no-project python -I -X utf8 mindeststandards/repin.py --alt <alter-katalog.json> --neu <neuer-katalog.json> --neu-commit <40er-SHA> [--accept-changed <Control-IDs>]
```

`repin.py` stellt alle Stände, die noch auf dem alten Commit stehen, auf den
neuen um (siehe oben) und verlangt, dass der neue Commit und der SHA-256 zu den
Konstanten in `mindeststandard-oscal.html` passen. Mit `--check-only` prüft es
nur, ob sein Resolver die vorhandenen Kataloge byteidentisch reproduziert.
Umbenannte Zielobjektkategorien und die Control-Klasse gelten als mechanisch;
Controls, die upstream umformuliert wurden, übernimmt es nur mit
`--accept-changed <IDs>` in der neuen Fassung (die `alters` des Profils
bleiben), sonst bricht es ab.
Nach einem Pin-Wechsel die Hashes in `MST_PINNED` des SSP-Generators
nachziehen.

## Lizenz

Profil, Ergänzungskatalog und Katalog stehen unter CC BY-SA 4.0, wie die
Stand-der-Technik-Bibliothek des BSI, deren Controls sie enthalten. Quellen:
Anwenderkatalog Grundschutz++ und BSI-GSMap (BSI-Bund/Stand-der-Technik-Bibliothek,
CC BY-SA 4.0) sowie die Mindeststandards des BSI nach § 44 Abs. 1 Satz 1 BSIG
(wörtlich und mit Quellenangabe wiedergegeben; amtliche Werke im Sinne von
§ 5 Abs. 2 UrhG, Änderungsverbot und Quellenangabe nach §§ 62, 63 UrhG beachtet).
Die Statements neuer Controls sind eigene Formulierungen. Das Ergebnis ist
Auslegung, kein Dokument des BSI.

## Stand

Erstmals abgelegt am 16.10.2026 (Commit `22ed7b6`, builds 1.2.1 und 1.4.1), mit Release 4.3 auf `a128311` und mit Release 5.1 am 28.10.2026 auf `160c177d` umgepinnt; Werkzeug „Mindeststandard → OSCAL“.

Alle Stände importieren den Anwenderkatalog am Commit `160c177d` (Build
2026-10-22; SHA-256 `7c3acebd…`, Resource-UUID
`c45ef8e9-7d97-5035-b3df-6af73bf31126`).

| Mindeststandard | Version | Stand BSI | Build | Controls | Ergänzungskatalog |
|---|---|---|---|---|---|
| HV-Benchmark kompakt (HV) | 2.0 | 11/2023 | 1.4.1 | 58 | nein |
| ISMS ITKB | 1.0a | 07/2025 | 1.2.1, umgepinnt | 43 | ja |
| Mobile Device Management (MDM) | 2.0 | 09/2022 | 1.2.1, umgepinnt | 98 | ja |
| Nutzung externer Cloud-Dienste (NCD) | 2.1 | 12/2022 | 1.2.1, umgepinnt | 64 | ja |
| Protokollierung und Detektion (PD) | 2.1 | 11/2024 | 1.2.1, umgepinnt | 54 | ja |
| Transport Layer Security (TLS) | 2.4 | 05/2023 | 1.2.1, umgepinnt | 17 | nein |
| Videokonferenzdienste (VK) | 1.0 | 10/2021 | 1.2.1, umgepinnt | 60 | ja |
| Webbrowser (WB) | 3.0 | 02/2024 | 1.2.1, umgepinnt | 49 | ja |

„Umgepinnt“ heißt: Der Stand wurde mit build 1.2.1 gegen den Anwenderkatalog
`4e117794` erarbeitet und am 16.10.2026 mit `repin.py` mechanisch auf `a128311`
umgestellt. Zwischen beiden Katalogständen unterscheiden sich die verwendeten
Controls nur in den drei umbenannten Zielobjektkategorien (Release 4.2);
`repin.py` prüft das Control für Control und bricht sonst ab. Beim Umpinnen
werden Import, Back-Matter-Resource (URL, SHA-256, UUID) und die Querverweise
des Ergänzungskatalogs umgestellt, Kategorienwerte und die Katalogformulierung
„Konfiguration für Mobile Endgeräte“ nachgezogen, und der Katalog wird mit dem
Resolver des Werkzeugs neu aufgelöst; die Remarks der Dateien halten das fest.

Am 28.10.2026 (Release 5.1) wurden alle acht Stände mit `repin.py` von
`a128311` auf `160c177d` umgestellt. Zwischen diesen Katalogständen
unterscheiden sich die verwendeten Controls nur in der Control-Klasse
(`BSI-Stand-der-Technik-Kernel-G0` → `BSI-Stand-der-Technik-Kernel`,
Kernel-Konsolidierung des Builds 2026-10-22; `repin.py` kennt die
Umbenennung als mechanisch), mit einer Ausnahme: BER.5.2 (MDM) hat das BSI
in Titel und Statement umformuliert („Zurücksetzung und Ersetzung von
Authentifizierungsmitteln“); der Stand übernimmt das Control mit
`--accept-changed BER.5.2` in der neuen Fassung, das ersetzende
MUSS-Statement des MDM-Profils (`BER.5.2_stm`) bleibt unverändert. Die
Remarks von Profil und Ergänzungskatalog nennen beides.
Der Mindeststandard NdB 3.0 (VS-NfD) liegt nicht öffentlich vor und fehlt
deshalb.
