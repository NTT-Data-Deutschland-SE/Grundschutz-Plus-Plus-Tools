# Namespace `ed23-baustein`: Props und Klassen der ED23-Baustein-Profile und des NG-Ergänzungskatalogs

Dieser Namespace ist der OSCAL-**naming-system identifier** (`ns`) für alle Eigenschaften, die
`Gpp-ai-tool` an die Profile in `ED23-Baustein-profile/DE/` und an den gemeinsamen
`NG-ergaenzungskatalog.json` schreibt (Stages `stage_ed23_baustein_abgleich`, `stage_ng_katalog`,
`stage_ED23_profiles_enhanced`). Er ist ein Bezeichner, keine abrufbare Datei – dieselbe Konvention
wie `…/ns/mindeststandard` des Mindeststandard-Konverters.

**Namespace-URI** (wörtlich als Prop-`ns`):

```
https://github.com/NTT-Data-Deutschland-SE/Grundschutz-Plus-Plus-Tools/ns/ed23-baustein
```

## Was BSI ist und was NG ist

**NG** steht für **Nutzergenerierte Inhalte**: alles, was nicht vom BSI stammt. Der benutzerdefinierte
ED23-Katalog (NTT DATA DACH) enthält 111 Bausteine des BSI und 12 nutzergenerierte Bausteine
(APP.4.5, APP.4.7, APP.4.8, APP.4.9, APP.4.10, SYS.1.10, SYS.1.11, SYS.1.2.4, SYS.5.1, ORP.6,
OPS.1.1.8, DER.7), ohne Marker im Katalog; die Menge ergibt sich als Differenz der Baustein-IDs zur
reinen BSI-Datei `BSI_GS_OSCAL_current_2023.json` am selben Commit. Die Kennzeichnung ist dreifach:

| Ebene | BSI | NG |
|---|---|---|
| Control-ID | ID des Anwenderkatalogs (`KONF.1.1`) | `NG-<AnforderungsID>` (`NG-SYS.1.1.A5`), nur im NG-Ergänzungskatalog |
| Titel | unverändert | Control `NG: …`, Katalog `NG Ergänzungskatalog …`, Profil eines NG-Bausteins `NG APP.4.10 – …` |
| Datei | `<kategorie>_<ID>_<titel>[_enhanced].json` | `NG_<kategorie>_<ID>_<titel>[_enhanced].json`, `NG-ergaenzungskatalog.json` |
| Prop `herkunft` | `BSI` | `NG` |

Die 7 Prozess-Bausteine ohne eigene Praktik in Grundschutz++ (DER.3.1, DER.3.2, DER.2.2, DER.2.3,
DER.4, OPS.1.2.2, CON.11.1) sind BSI-Bausteine (`herkunft=BSI`, `ed23-schicht=prozess`); nur ihre
neuen Controls sind NG.

## Properties

| prop `name` | wo | Bedeutung | Werte |
|---|---|---|---|
| `herkunft` | Profil-Metadata, NG-Katalog-Metadata, NG-Katalog-Gruppe, Anforderungsgruppe, NG-Control, SSP-Komponente, implemented-requirement | Herkunft des Inhalts | `BSI` \| `NG` |
| `ed23-baustein` | Profil-Metadata | Baustein-ID der Edition 2023 | z. B. `APP.3.6`, `APP.4.10` |
| `ed23-baustein-titel` | Profil-Metadata | Titel des Bausteins | frei |
| `zielobjektkategorie` | Profil-Metadata | per KI gematchte Zielobjektkategorie des Anwenderkatalogs (bei Prozess-Bausteinen nur informativ) | Name aus `target_object_categories.csv` |
| `ed23-katalog-pin` | Profil-Metadata, NG-Katalog-Metadata | Commit des gepinnten ED23-Katalogs | 40-stelliger SHA |
| `ed23-schicht` | Profil-Metadata | Schicht des Bausteins | `system` \| `prozess` |
| `rolle` | Anforderungsgruppe | Zuständigkeit aus dem Anforderungstitel (`[ISB]`) | frei |
| `anforderungsart` | Anforderungsgruppe | Einordnung durch das Modell (nur bei KI-geprüften Anforderungen) | `umsetzungsanforderung` \| `verweis` \| `hinweis` \| `ausnahme` |
| `ohne-control` | Anforderungsgruppe | die Anforderung hat weder ein Control des Anwenderkatalogs noch ein NG-Control; Remark = Begründung | `hinweis` \| `verweis` \| `ausnahme` \| `abgelehnt-durch-checker` \| `unbeantwortet` \| `unbestimmt` |
| `entfallen` | Anforderungsgruppe | die Anforderung ist im Kompendium entfallen (Gruppe ohne Text und Controls) | `true` |
| `ed23-anforderung` | `modify.alters[].adds[].props` am Control des Anwenderkatalogs; Prop am NG-Control | die Anforderung, der das Control zugeordnet ist; Remark beginnt mit `Herkunft:` (siehe unten) | Anforderungs-ID |
| `praktik` | NG-Control | Praktik des Anwenderkatalogs, in die das Control gehört; Remark = Klartext | Praktik-Kürzel (`KONF`, `DET`, …) |

Fremde Namespaces an denselben Stellen: `level` (ns `https://www.bsi.bund.de/ns/grundschutz`,
`1`/`3`/`5` = Basis/Standard/erhöht), `modal_verb`, `target_object_categories`, `sec_level`
(Vokabulare der Stand-der-Technik-Bibliothek), `label` (ohne ns) und `alt-identifier` (ohne ns).

## Die `Herkunft:`-Remark

Jede Zuordnung eines Controls zu einer Anforderung trägt ihre Herkunft im Remark der Prop
`ed23-anforderung`. Die Formen sind fest, die Werkzeuge parsen sie:

| Form | Quelle |
|---|---|
| `Herkunft: gpp_ed23_anforderungen (<relation>, Teilanforderung <n[,n]>): <Begründung>` | `hilfsdateien/gpp_ed23_anforderungen.json` (Maker-Checker G++ → ED23) |
| `Herkunft: satz_abdeckung (<relation>, Satz <n[,n]>): <Begründung>` | `hilfsdateien/ed23_satz_abdeckung.json` (satzgenaue Beurteilung) |
| `Herkunft: BSI-GSMap ITGS→GS++ (<relation>)` | amtliches GSMap-Mapping des BSI |
| `Herkunft: prozessbausteine_mapping (1:1-Zuordnung)` | `hilfsdateien/prozessbausteine_mapping.json` (vollständigkeitsgetrieben, allein kein Deckungsnachweis) |
| `Herkunft: KI-Vorschlag (<relation>, Konfidenz <hoch\|mittel\|niedrig>, Checker <bestaetigt\|fraglich\|unsicher\|nicht geprüft>): <Begründung>` | Maker-Checker der Stage `stage_ed23_baustein_abgleich` |
| `Herkunft: vom Modell formuliert (Konfidenz …, Checker …); kein passendes Control im Anwenderkatalog Grundschutz++ (Pin …)` | NG-Control im Ergänzungskatalog |

Ein Zusatz `[auch: <quelle>, …]` nennt weitere Quellen, die dieselbe Zuordnung tragen.
`<relation>` ist immer in OSCAL-Richtung zu lesen: **das Control relativ zur Anforderung**
(`superset-of` = das Control verlangt mehr als die Anforderung). Der Konverter-Prompt fragt die
Gegenrichtung ab; die Pipeline dreht `subset-of`/`superset-of` beim Speichern.

## Klassen

| class | Objekt | Bedeutung |
|---|---|---|
| `ed23-stufe` | Gruppe in `merge.custom` | Stufe B/S/H (Basis, Standard, erhöhter Schutzbedarf), Titel aus dem Kompendium, `label` = Stufe |
| `ed23-anforderung` | Gruppe in `merge.custom` | eine Anforderung des Bausteins: Originaltext als Part `overview`, Controls per `insert-controls` (nur beim ersten Vorkommen, sonst Link `rel="related"` „`<cid>` steht unter `<Anforderung>`“) |
| `ng-baustein` | Gruppe im NG-Katalog | Baustein, der selbst nutzergeneriert ist (12 NTT-Bausteine) |
| `baustein` | Gruppe im NG-Katalog | BSI-Baustein, für dessen Anforderungen NG-Controls entstanden sind |
| `ng-ergaenzung` | Control im NG-Katalog | nutzergeneriertes Control |

## Profilstruktur (Kurzfassung)

`imports[0]` = gepinnter Anwenderkatalog Grundschutz++ (Fragment auf Back-Matter-Resource mit
Commit-URL und SHA-256), `with-ids` = genau die zugeordneten Controls. `imports[1]` (nur bei
NG-Controls) = `NG-ergaenzungskatalog.json` über eine Resource mit **relativem** rlink und dem
SHA-256 der Datei; die Konsumenten laden sie relativ zur Profil-URI und verweigern bei
abweichendem Hash. `merge.combine.method = use-first` immer (zwei Quellen; das generierte
JSON-Schema 1.2.2 kennt das Attribut nicht, das Metaschema schon, Handbuch Anhang D37).
`modify.alters`: je Control des Anwenderkatalogs in `_enhanced` zuerst der Reifegrad-Block
(`by-id` auf die Statement-Part, Parts m1–m5, `docs/profile-maturity-contract.md`), danach ein
`adds` nur mit Props `ed23-anforderung`; `Baustein_2_Profile.html` liest `adds[0].parts[0]`, die
Reihenfolge ist Vertrag. Prüfskript: `ED23-Baustein-profile/pruefe_export.py`.

## NG-Liste neu ableiten (bei Pin-Wechsel des ED23-Katalogs)

```bash
python3 -I -c "import json;f=lambda p:{g['id'] for l in json.load(open(p))['catalog']['groups'] for g in l.get('groups',[])};print(sorted(f('BSI_GS_OSCAL_current_2023_benutzerdefinierte.json')-f('BSI_GS_OSCAL_current_2023.json')))"
```

Die Pipeline berechnet die Menge bei jedem Lauf (`utils/ed23_baustein.detect_ng`); die
Konstante `ED23_NG_BAUSTEINE` in `one-page-apps/ssp_generator_ed23.html` ist davon abgeleitet
und wird bei einem Pin-Wechsel nachgezogen.
