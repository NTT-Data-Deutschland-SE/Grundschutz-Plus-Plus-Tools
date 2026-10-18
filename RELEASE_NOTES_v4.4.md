# Grundschutz++ OSCAL Tools – Version 4.4

Version 4.4 stellt die **ED23-Baustein-Profile** auf das Muster der Mindeststandard-Profile um, nimmt die **12 nutzergenerierten Bausteine** des benutzerdefinierten ED23-Katalogs und **7 Prozess-Bausteine ohne Gegenstück in Grundschutz++** auf, und kennzeichnet alles, was nicht vom BSI stammt, als **NG (Nutzergenerierte Inhalte)** – in Daten und Werkzeugen. Die Pipeline `Gpp-ai-tool` läuft dazu auf **Gemini 4 Argon** mit einem Modell und Thinking-Levels.

## ED23-Baustein-Profile: Anforderungen als Struktur, NG-Ergänzungskatalog, Herkunft je Zuordnung

Bisher enthielt ein Profil in `ED23-Baustein-profile/DE/` den kompletten Control-Pool der per KI gematchten Zielobjektkategorie, keine einzige Anforderung des Bausteins. Jetzt ist der Baustein selbst die Struktur (Handbuch 3.15/3.16): `imports[0]` ist der gepinnte Anwenderkatalog mit genau den zugeordneten Controls; `merge.custom` bildet die Stufen Basis/Standard/erhöht und darunter je Anforderung eine Gruppe mit dem amtlichen Wortlaut (Part `overview`) und ihren Controls (`insert-controls`, jedes Control nur einmal, sonst `rel="related"`); `modify.alters` nennt je Control die Anforderungen mit `Herkunft:`-Remark (Mapping der Pipeline, satzgenaue Beurteilung, GSMap des BSI, 1:1-Prozessmapping oder KI-Vorschlag mit Konfidenz und Checker-Urteil). Anforderungen, für die der Anwenderkatalog nichts bietet, bekommen ein neues Control im gemeinsamen `DE/NG-ergaenzungskatalog.json` (`NG-<AnforderungsID>`, Titel `NG: …`, class `ng-ergaenzung`, Praktik, Zielobjektkategorien, `alt-identifier`, Querverweise), den das Profil als `imports[1]` mit relativem rlink und SHA-256 zieht (fail closed), `merge.combine.method = use-first`. Die `_enhanced`-Profile tragen weiter die Reifegrad-Blöcke, jetzt vor den Herkunfts-Props (`adds[0]` bleibt der Reifegrad-Block; Vertrag in `Gpp-ai-tool/docs/profile-maturity-contract.md`).

Die Liste der Bausteine: die 78 System-Bausteine wie bisher, dazu die 12 NG-Bausteine von NTT DATA (APP.4.5, APP.4.7, APP.4.8, APP.4.9, APP.4.10, SYS.1.10, SYS.1.11, SYS.1.2.4, SYS.5.1, ORP.6, OPS.1.1.8, DER.7; sie standen im Katalog, fielen aber am Schichtfilter oder an der nie neu erzeugten Zuordnungsdatei heraus) und 7 BSI-Prozess-Bausteine, deren Thema in Grundschutz++ keine eigene Praktik hat (DER.3.1, DER.3.2, DER.2.2, DER.2.3, DER.4, OPS.1.2.2, CON.11.1; Kriterium: Satzabdeckung unter 45 % oder mindestens fünf Anforderungen ohne jeden Träger, Tabelle mit `Gpp-ai-tool/scripts/prozess_luecken.py`). Die übrigen Prozess-Bausteine bleiben bei den Praktiken-Profilen.

**NG = Nutzergenerierte Inhalte.** Profile der NG-Bausteine heißen `NG_<kategorie>_<ID>_<titel>.json` mit Titel `NG …`; jedes Profil und der Katalog tragen die Metadata-Prop `herkunft` (`BSI` | `NG`) im neuen Namespace `…/ns/ed23-baustein` (`Dokumentation/namespaces/ed23_baustein_props.md`: Props, Klassen, ID-Schema, Herkunft-Grammatik, Neuableitung der NG-Liste). Das Prüfskript `ED23-Baustein-profile/pruefe_export.py` kontrolliert Schema, Importe, NG-Hash, Control-nur-einmal, Dateiname ⇔ Titel ⇔ `herkunft`.

## Gpp-ai-tool 5.0.1: Gemini 4 Argon, Abgleich-Stage, NG-Katalog, Reifegrad-Cache

- **Ein Modell.** `GEMINI_MODEL=gemini-4-argon`; die früheren Rollen (Maker, Verifier, Pro) sind Thinking-Levels (`MAKER_THINKING_LEVEL` medium, `CHECKER_THINKING_LEVEL` high). Kein explizites Context-Caching mehr (auf Argon HTTP 400): der Korpus ist der stabile Prompt-Prefix, implizit gecacht. Keine Sampling-Parameter, 20-Minuten-Timeout, Retries nur bei transienten Fehlern und Schema-Verstößen (Kappe 5), Nutzungs-Log je Call. Typed Settings (`pydantic-settings`, `.env.example`, README-Tabelle), `uv`/`pyproject.toml`/`justfile`, Dockerfile auf Python 3.12, `LOG_LEVEL`-Hebel, `--version`, `--fresh`.
- **Pins.** Der ED23-Katalog (NTT DATA DACH, Commit `62f0803`) ist jetzt auch in der Pipeline gepinnt, mit SHA-256 beider Dateien; die NG-Menge ist die Differenz der Baustein-IDs. `scripts/check_pins.py` kennt die ED23- und GSMap-Quellen.
- **Review-Fixes (5.0.1).** Resume von `stage_ed23_baustein_abgleich` baut den vollständigen KI-Block aus der veröffentlichten Ausgabe zurück (vorher gingen neue Controls beim zweiten Lauf ohne `--fresh` verloren) und prüft nur noch offene Kandidaten des Checkpoints nach; `stage_match_bausteine` schreibt die bereinigte Map auch, wenn nichts nachzufragen ist; ein `MAX_TOKENS`-Abbruch wird nicht mehr fünfmal identisch wiederholt (`OutputTruncatedError`); `LOG_LEVEL` aus `.env` wirkt; Pins sind in `.env.example` als Prozessumgebung-only dokumentiert.
- **Neue Stages.** `stage_ed23_baustein_abgleich` (deterministische Quellen zuerst, Maker-Checker nur für Anforderungen ohne Träger, resumierbar) und `stage_ng_katalog` (deterministisch, schreibt nur bei Änderung). `stage_match_bausteine` fragt nur fehlende Bausteine nach. `stage_ED23_profiles_enhanced` baut die Profile neu und holt Reifegrad-Texte aus `hilfsdateien/ed23_maturity_cache.json` (aus den bisherigen Profilen geerntet, 6.958 Blöcke); das Modell wird nur für Controls ohne Eintrag gerufen.

## SSP-Generator / Editor V5.18.1: NG-Bausteine und NG-Ergänzungskatalog

Das Dropdown der ED23-Baustein-Profile (bisher „Nutzergeneriert“, jetzt „ED23-Bausteine (Baustein-Profile)“) markiert NG-Profile mit `NG ·`. Ein Profil mit NG-Controls lädt den NG-Ergänzungskatalog relativ zur Profil-URL und prüft seinen SHA-256 aus der Back-Matter; weicht er ab, entsteht kein Zielobjekt. Die NG-Controls hängen am Zielobjekt (Badge „NG“ im Tailoring, Hinweis „NG-Ergänzung zu <Anforderung>“), der Katalog erscheint einmal in der Katalogliste und verschwindet erst, wenn keine NG-ID mehr referenziert ist (weder an einem Zielobjekt noch global noch in einer Anpassung). Im erzeugten Profil folgt der NG-Katalog auf den Anwenderkatalog (Mindeststandard-Profile davor, `use-first`), NG-IDs stehen nie im Basis-Import; Profil-Metadaten, SSP-Komponenten und implemented-requirements tragen `herkunft=NG`, die Back-Matter-Resource `catalog-role: ng-ergaenzung`. Props-only-`adds` der neuen Profile sind keine Tailoring-Anpassungen; das `NG_`-Präfix gehört nicht zur Zielobjektkategorie.

## SSP-Generator Edition 2023 V1.7: NG-Bausteine markiert

Konstante `ED23_NG_BAUSTEINE` neben dem Katalog-Pin, Plausibilitätsprüfung beim Laden, Status „123 Bausteine (davon 12 NG)“, NG-Badges in Prozessliste, Asset-Picker, Asset-Liste und Tailoring (je Anforderung), `[NG]`-Hinweis für die KI-Zuordnung (ein gespeicherter eigener Mapping-Prompt wird nicht automatisch ergänzt), Props `ed23-baustein`/`herkunft=NG` in Profil und SSP, Beschreibung der Basiskatalog-Resource nennt die NG-Bausteine. „NG-Liste prüfen“ in der Rail lädt auf Wunsch die reine BSI-Datei (15 MB) und vergleicht.

## Weitere Werkzeuge

GS++ Explorer v9.9 nimmt NG-Controls aus dem Drift-Check und loggt ihre Quelle. `ssp_ausfuellen`, `pruefung_ap_ar` und `Baustein_2_Profile` lesen die neuen Profile unverändert (alle Importe mit Hash-Prüfung bzw. nur `imports[0]`) und erhalten nur den Selbst-Pin.

## Handbuch 3.16 und Namespace ed23-baustein

Kapitel 3 (v0.15) bekommt **3.16 „Nutzergenerierte Inhalte kennzeichnen: die ED23-Baustein-Profile“**: warum der Katalog die NG-Bausteine nicht verrät, die dreifache Kennzeichnung, die Struktur nach 3.15 mit asset-bezogenem Geltungsbereich, was das Modell entscheidet und was nicht, Pin-Disziplin in Pipeline und Selbst-Pin.

## Versionen der Anwendungen

| Anwendung | Version |
|---|---|
| gemeinsamer Kern (gpp-core.js) | 4 · Cache-Buster v4.1 |
| gemeinsames Stylesheet (gpp-core.css) | 2 · Cache-Buster v4.1 |
| Übersicht (index.html) | 1.8 |
| OSCAL Schema Validator | 1.11.2 |
| SSP-Generator / Editor (ssp_generator) | V5.18.1 |
| GS++ Explorer (GSpp-Viewer) | v9.9 |
| BSI → G++ Profil (Baustein_2_Profile) | 0.12.0 · nur Selbst-Pin |
| SSP ausfüllen / Grundschutzcheck (ssp_ausfuellen) | v1.7.2 · nur Selbst-Pin |
| Prüfung AP/AR (pruefung_ap_ar) | build 9.7.0 · nur Selbst-Pin |
| POA&M-Generator | v2.5 |
| Pipeline (Gpp-ai-tool) | 5.0.0 |

Einzelwerkzeuge in `one-page-apps/`: eigenständig, ohne `gpp-core.js`, von der Datenbank unberührt:

| Anwendung | Version |
|---|---|
| SSP-Generator Edition 2023 | ED23 V1.7 |
| C5 → OSCAL Konverter | v1.1 · nur Selbst-Pin |
| Mindeststandard → OSCAL | build 1.4.1 · nur Selbst-Pin |

## Hinweise zum Umstieg

- **Einmal mit Strg+F5 laden.** Kern und Stylesheet sind unverändert.
- Die neuen Profile werden in den Werkzeugen erst nach dem Selbst-Pin-Bump sichtbar (`GPP_TOOLS_PIN_COMMIT` zeigt auf den Commit mit den regenerierten Profilen; zweiter Commit „Selbst-Pin auf …“).
- Ein NG-Ergänzungskatalog, dessen SHA-256 nicht zur Profil-Back-Matter passt, wird abgewiesen; nach jeder Regeneration der Profile ist der Katalog-Hash in allen betroffenen Profilen neu (die Pipeline schreibt das selbst).
- Wer im Generator Edition 2023 einen eigenen Mapping-Prompt gespeichert hat, ergänzt den `[NG]`-Satz selbst (Prompt-Vorlage im Werkzeug).
- Die Auslieferung bleibt `GS++-oscal-app.zip` (zwölf Dateien); eine einzelne HTML-Datei allein läuft nicht.
- `Gpp-ai-tool`: `uv sync`, `.env` nach `.env.example`; `GROUND_TRUTH_MODEL*`, `ED23_MAKER_MODEL`, `AI_ENDPOINT_ID` und `CONTEXT_CACHE_TTL_SECONDS` entfallen.
