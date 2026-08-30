# ED23↔GS++ Mapping-QS — Stichprobenprüfung 30.08.2026

Qualitätsprüfung des v2-Union-Mappings `hilfsdateien/gpp_ed23_anforderungen.json` (v2026-08-29, 5.145 Zuordnungen): 96 stratifiziert gezogene Controls (5 je Praktik, Seed 23), alle 943 zugehörigen Paare, vier Prüfachsen (Inhalt / Relationstyp / Satzwahl / Begründungsehrlichkeit), 18 unabhängige Reviewer-Agenten plus adversariale Nachprüfung der Extremurteile.

**Ergebnisbericht: [`bericht.md`](bericht.md)**

## Inhalt

| Datei/Ordner | Inhalt |
|---|---|
| `bericht.md` | Vollständiger QS-Bericht mit Master-Tabelle, Befunden, Streichliste (76 Paare) und Empfehlungen |
| `results/` | 18 Reviewer-Protokolle: je Paar eine `PAIR\|…`-Zeile (4 Achsen-Urteile + Flags), je Control eine `CTRL\|…`-Zeile (hilfreich/drop/Lücken) + Kommentar, je Praktik SUMMARY + Top-Probleme |
| `tally.json` | Alle 943 Einzelurteile maschinenlesbar (aggregiert aus `results/`) |
| `dossiers/` | 20 Praktik-Dossiers: die Prüfgrundlage — je gesampeltes Control das GS++-Statement + Guidance (Katalog @ 36a0fac4) und alle Ziel-Anforderungen mit amtlichen, nummerierten Satztexten, zitierte Sätze markiert |
| `gen_dossiers.py` | Generator der Dossiers (deterministisch, Seed 23). Achtung: absolute Pfade der Erstellungsmaschine; benötigt den gecachten resolved Catalog `gpp-resolved_catalog@36a0fac473c6.json` (liegt unter `Gpp-ai-tool/.cache/ed23_gap/`) |
| `tally.py` | Aggregation der `results/*.txt` zu Master-Statistik und `tally.json` |
| `review_instructions.md` | Die identische Prüfanweisung aller 18 Reviewer (Achsen-Definitionen, Relations-Semantik, Kalibrierung, Ausgabeformat) |

## Provenienz

- Mapping: `gpp_ed23_anforderungen.json` v2026-08-29 (Union, 5.145 Paare)
- GS++-Quelle: resolved Catalog @ Commit `36a0fac473c630dd76c83fdfb13a201770b4e1bd`
- ED23-Ziel: amtliches XML_Kompendium_2023 (v4), Satztexte aus `hilfsdateien/ed23_anforderungen_stripped.json`
- Satznummern 1-basiert, identisch zur `statement-sentence`-Prop des Mappings
- Prüfdatum: 2026-08-30; Reviewer: Claude (Fable 5), 18 unabhängige Instanzen
