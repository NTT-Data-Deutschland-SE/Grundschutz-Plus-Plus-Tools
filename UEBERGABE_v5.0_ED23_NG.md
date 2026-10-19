# Übergabe: ED23-Baustein-Profile nach Mindeststandard-Muster, NG-Kennzeichnung, Argon-Migration

Stand: 2026-10-18, Branch `main`, Commits `b6e3d15` … `87c6192` (8 Commits auf `d359435`, Merge von Release 4.3).
Plan: `~/.claude/plans/mir-ist-aufgefallen-dass-zesty-fiddle.md` (Teil 0–3). Release Notes: `RELEASE_NOTES_v5.0.md`.
Diese Datei ist die Übergabe an die nächste Sitzung; sie wird mit dem Abschluss von Schritt 7 unten gelöscht.

## 1. Was fertig und verifiziert ist

| Bereich | Stand | Verifiziert durch |
|---|---|---|
| Gpp-ai-tool auf Gemini 4 Argon (Teil 0) | `GEMINI_MODEL=gemini-4-argon`, Thinking-Levels statt Modell-Rollen, kein explizites Caching, Timeout, transiente Retries (Kappe 5), pydantic-Settings, `.env.example`, uv/pyproject/justfile, Dockerfile 3.12, `--version`/`--fresh`, `LOG_LEVEL` | `just test` 94 grün, `ruff` sauber, `check_gemini_usage_py.py`: 0 ERR / 0 WARN |
| ED23-Pin und NG-Erkennung (1.1/1.2) | `ED23_CATALOG_PIN_COMMIT=62f0803`, SHA-256 beider Dateien in `constants.py`; NG = Baustein-IDs bd − plain (`utils/ed23_baustein.detect_ng`); `ALLOWED_PROCESS_BAUSTEINE` um 3 NG- und 7 BSI-Prozess-Bausteine erweitert | `tests/test_ed23_baustein.py`; Lauf gegen echte Daten: 12 NG-Bausteine, 185 NG-Anforderungen, 2.310 Records |
| Matching inkrementell (1.3) | nur fehlende Bausteine werden angefragt, Stale-Einträge entfernt | `tests/test_stage_match_bausteine.py` |
| Abgleich-Stage (1.4) | `stage_ed23_baustein_abgleich`: deterministische Quellen (invertiertes Mapping, Satzabdeckung, GSMap, 1:1), Gate (1:1 allein zählt nicht), Maker-Checker, Post-Checks, Checkpoint/Resume, Ausgabe `hilfsdateien/ed23_baustein_abgleich.json` | `tests/test_stage_ed23_baustein_abgleich.py` (inkl. Lauf mit Fake-Client und Resume ohne Calls) |
| NG-Katalog-Stage (1.5) | `stage_ng_katalog`: ein Katalog, Schicht → Baustein, `NG-<AnforderungsID>`, schreibt nur bei Änderung | `tests/test_stage_ng_katalog.py` |
| Profil-Stage (1.6/1.7) | `stage_ED23_profiles_enhanced`: merge.custom je Anforderung, zwei Importe, use-first, Herkunfts-Props, Reifegrad-Block zuerst, `NG_`-Präfix, Reifegrad-Cache `hilfsdateien/ed23_maturity_cache.json` (6.958 Blöcke aus 78 ED23- und 17 Prozess-Profilen geerntet) | `tests/test_stage_ED23_profiles_enhanced.py`; Offline-Trockenlauf mit Stub-Modell in Temp-Verzeichnis: 156 Profile, Prüfskript 0 Befunde |
| Prüfskript, Pins, Doku (1.8/1.9) | `ED23-Baustein-profile/pruefe_export.py`, `check_pins.py` (ED23/GSMap-Quellen, `.venv` übersprungen, Fragmente), `Dokumentation/namespaces/ed23_baustein_props.md`, Tool-README, `docs/profile-maturity-contract.md`, `scripts/prozess_luecken.py`, `scripts/harvest_maturity_alters.py` | `check_pins.py` mit Fetch: alle Pins aktuell, 9/9 SHA-256 passen |
| Generatoren (Teil 2) | `one-page-apps/ssp_generator_ed23.html` V1.7 (NG-Badges, Konstante, Props, Opt-in-Prüfung), `GS++-oscal-app/ssp_generator.html` V5.18.1 (NG-Profile, NG-Katalog relativ + SHA-256 fail closed, Importreihenfolge, SSP-Props), `GSpp-Viewer.html` v9.9 (NG aus Drift-Check) | nur `node --check` der Skripte; **kein Browser-Test** |
| Doku (2.4) | Repo-README, Handbuch 3.16 (Kapitel 3 v0.15), beide Readmes, `RELEASE_NOTES_v5.0.md` | gelesen, nicht gerendert |

## 2. Was NICHT gemacht ist (und warum)

- **Die Profile sind nicht neu erzeugt.** `ED23-Baustein-profile/DE/` enthält noch die 156 alten Dateien (Pool-Form), `hilfsdateien/baustein_zielobjekt.json` hat 78 Einträge, `hilfsdateien/ed23_baustein_abgleich.json` und `ED23-Baustein-profile/DE/NG-ergaenzungskatalog.json` existieren nicht. Grund: In der Arbeitsumgebung gab es weder `Gpp-ai-tool/.env` (GEMINI_API_KEY) noch gcloud-ADC; die drei KI-Stages konnten nicht laufen.
- **Kein Self-Pin-Bump, kein neues ZIP.** `GPP_TOOLS_PIN_COMMIT` zeigt in allen Apps noch auf `2d17c83`; die Werkzeuge sehen die neuen Profile erst nach Schritt 6.
- **Kein Browser-Test** der drei geänderten HTML-Werkzeuge (Teil 3 des Plans).
- `RELEASE_NOTES_v5.0.md` ist geschrieben, aber die Pin-Zeile im Abschnitt „Hinweise zum Umstieg“ nennt noch keinen Commit.

## 3. TODO für die nächste Sitzung (in dieser Reihenfolge)

Voraussetzung: `Gpp-ai-tool/.env` mit `GEMINI_API_KEY=…` (Developer API) oder `GCP_PROJECT_ID=…` plus `gcloud auth application-default login`. Alle Befehle aus `Gpp-ai-tool/`.

1. `uv sync && uv run pytest -q && uv run python scripts/check_pins.py` — Ausgangslage grün.
2. `./scripts/run_local.sh --stage stage_match_bausteine` — erwartet 19 neue Einträge (12 NG: APP.4.5, APP.4.7, APP.4.8, APP.4.9, APP.4.10, SYS.1.10, SYS.1.11, SYS.1.2.4, SYS.5.1, ORP.6, OPS.1.1.8, DER.7; 7 Prozess: DER.3.1, DER.3.2, DER.2.2, DER.2.3, DER.4, OPS.1.2.2, CON.11.1), Map 78 → 97. Zuordnungen der Prozess-Bausteine per Augenschein prüfen; `baustein_zielobjekt.json` darf von Hand korrigiert werden (bei Prozess-Bausteinen ist die Kategorie nur informativ).
3. `./scripts/run_local.sh --stage stage_ed23_baustein_abgleich` — ca. 70 Maker- und 300 Checker-Calls, resumierbar (`.partial`). Am Ende im Log: Zahl neuer Controls, `ohne_control`, Checker-Histogramm. Erwartung aus dem Trockenlauf: ca. 147 BSI-Lücken + 185 NG-Anforderungen + Lücken der 7 Prozess-Bausteine gehen ans Modell. Lehnt der Checker sehr viele neue Controls ab, erst ansehen, dann über eine Nachfass-Runde entscheiden, nicht blind wiederholen. Nachfass für Anforderungen ohne Control nach Checker-Ablehnung: `uv run python scripts/nachfass_abgleich.py --write`, dann die Stage erneut starten (Resume). Stand 2026-10-19: Der erste Echtlauf (Checker high, Pool 5, 353 Anforderungen ans Modell) lief noch ohne die Rückfalloption für neue Controls; die Nachfass-Runde für die davon betroffenen Anforderungen steht vor Schritt 4 an.
4. `./scripts/run_local.sh --stage stage_ng_katalog` — schreibt `ED23-Baustein-profile/DE/NG-ergaenzungskatalog.json`, loggt den SHA-256.
5. `git rm -q ../ED23-Baustein-profile/DE/*.json` (die Reifegrade der alten Dateien sind im Cache gesichert), dann `./scripts/run_local.sh --stage stage_ED23_profiles_enhanced` — erwartet 97 × 2 Dateien, ca. 79 Reifegrad-Chunk-Calls (alles andere aus `ed23_maturity_cache.json`), Log-Zeile mit `maturity_cached`/`maturity_generated`.
6. Verifikation: `python -I ../ED23-Baustein-profile/pruefe_export.py ../ED23-Baustein-profile/DE` (Exit 0), `uv run python scripts/check_pins.py`, dann Schritt 4 und 5 ohne `git rm` erneut: `git status --porcelain` muss leer sein (Idempotenz). Commit 1: Profile, NG-Katalog, `hilfsdateien/baustein_zielobjekt.json`, `ed23_baustein_abgleich.json`, `ed23_maturity_cache.json`.
7. Self-Pin-Bump (Commit 2, Muster `fbcf2be`): `2d17c83071c067b3acdb9a13f851d4a0104a83ab` durch den SHA von Commit 1 ersetzen in `GS++-oscal-app/ssp_generator.html` (`GPP_TOOLS_PIN_COMMIT`, Methodik-Defaults, Presets, `MST_PIN_COMMIT`), `Baustein_2_Profile.html`, `GSpp-Viewer.html`, `pruefung_ap_ar.html`, `ssp_ausfuellen.html`, `one-page-apps/ssp_generator_ed23.html`; `GS++-oscal-app.zip` neu bauen (dieselben zwölf Dateien wie `unzip -l` zeigt); Pin-Zeile in `RELEASE_NOTES_v5.0.md`; `check_pins.py` grün; diese Übergabedatei löschen.
8. Browser-Test nach Plan Teil 3 (`python3 -m http.server 8000` im Repo-Root): ED23-Generator Pill „123 Bausteine (davon 12 NG)“, Badges, „NG-Liste prüfen“ leerer Diff, Props im Export; GS++-Generator NG-Profil laden (Katalogeintrag, NG-Badges, Log „SHA-256 geprüft“), manipulierte Katalogkopie wird verweigert, Export-Reihenfolge MST → G++ → NG → weitere, SSP `catalog-role: ng-ergaenzung`; Viewer ohne Drift-Warnung für NG-IDs. Befunde an den Stellen fixen, die in `RELEASE_NOTES_v5.0.md` je Werkzeug genannt sind.
9. Push aller Remotes erst nach Freigabe.

## 4. Entscheidungen und Annahmen, die man kennen muss

- NG = Nutzergenerierte Inhalte: ID-Präfix `NG-`, Titel `NG: …`/`NG …`, Datei `NG_…`, Prop `herkunft` (ns `…/ns/ed23-baustein`). Vollständig in `Dokumentation/namespaces/ed23_baustein_props.md`, inklusive `Herkunft:`-Remark-Grammatik und Relationsrichtung (OSCAL: Control relativ zur Anforderung; Maker-Antworten werden gedreht).
- Die 7 Prozess-Bausteine tragen `herkunft=BSI` und `ed23-schicht=prozess`; nur ihre neuen Controls sind NG (Annahme, vom Nutzer nicht widersprochen).
- Ein gemeinsamer NG-Katalog für alle Bausteine; jede Änderung eines NG-Controls ändert den Hash und damit die Back-Matter aller NG-Profile (gewollt, fail closed).
- Reifegrad-Block steht in `_enhanced` vor dem Herkunfts-Block (`Baustein_2_Profile.html` liest `adds[0].parts[0]`).
- Wortlaut: amtliches XML für BSI-Anforderungen, bd-Katalog (m3-Statement) für NG; eine BSI-Anforderung (OPS.2.3.A22) fehlt im XML und fällt auf bd-m3 zurück (Log-Warnung).
- `sec_level` neuer Controls: Stufe 1/3 → `normal-SdT`, 5 → `erhöht` (Token aus der gepinnten `security_level.csv`).
- Im GS++-Generator heißt das Dropdown „Nutzergeneriert“ jetzt „ED23-Bausteine (Baustein-Profile)“, damit NG nur Nicht-BSI-Inhalt meint.
- `ALLOWED_PROCESS_BAUSTEINE`-Kriterium: Satzabdeckung < 45 % oder ≥ 5 trägerlose Anforderungen und keine eigene Praktik; Kandidaten zweiter Runde (OPS.1.2.6, OPS.1.1.5, CON.3, OPS.1.1.4, OPS.1.1.7) nach dem ersten Echtlauf entscheiden; Tabelle mit `uv run python scripts/prozess_luecken.py`.
