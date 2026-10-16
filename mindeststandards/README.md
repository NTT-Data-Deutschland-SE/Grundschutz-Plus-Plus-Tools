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
| `….arbeitsstand.json` | der Arbeitsstand des Werkzeugs (Anforderungen, Zuordnungen, Anpassungen, Modellvorschläge mit Checker-Urteilen) zum Wiederaufnehmen und Nachvollziehen |

## Herkunft und Verbindlichkeit

Die Anforderungstexte stammen aus den IT-Grundschutz-Referenztabellen des BSI
(Excel je Mindeststandard), die Controls unverändert aus dem Anwenderkatalog
(Commit `a128311`, SHA-256 in der Back-Matter). Die Zuordnung ist zweistufig:
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
Control im Katalog nur einmal vorkommt und dass Fragment-Links auf vorhandene
Controls zeigen. Exit 0 heißt: alles stimmt.

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

| Mindeststandard | Version | Dateien | Stand |
|---|---|---|---|
| (noch keine abgelegt) | | | |
