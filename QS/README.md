# QS: Qualitätssicherung der KI-Dokumentanalyse

Nur für die Entwicklung (Plan `Dokumentation/plan-ssp-generator-genauigkeit.md`, E5).
Nicht Teil der Auslieferung (ZIP). Ziel ist die Qualität der Extraktion insgesamt;
die Fixtures hier sind Regressionsmaterial, kein Optimierungsziel.

- `score_ssp.py`: Kennzahlen aus einem SSP-Export des Generators, ohne Modellaufruf.
  Dokumentunabhängige Zeilen laufen über jeden Export, die RECPLAST-Zeilen mit `--gold`.
- `recplast/`: Ground Truth zum BSI-Beispiel RECPLAST (`build_gold.py` erzeugt die CSVs
  aus dem PDF, das nicht im Repo liegt; SHA-256 steht im Skript). `baseline_2026-09-13.md`
  ist der Stand der vier Modell-Läufe vor Stufe 1.
- `fixtures/`: exportierte Chunk-Caches je Modell für Replay-Läufe (kommen mit Stufe 1).

```bash
PYTHONUTF8=1 uv run --no-project --with pdfplumber python QS/recplast/build_gold.py <Beschreibung_Recplast.pdf>
PYTHONUTF8=1 uv run --no-project python QS/score_ssp.py --gold QS/recplast <export.json> [...]
```
