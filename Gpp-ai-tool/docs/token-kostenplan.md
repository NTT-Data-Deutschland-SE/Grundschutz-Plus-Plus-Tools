# Token-Kostenanalyse und Sparplan für die ED23-Mapping-Läufe

Stand 2026-08-29. Anlass: Der Neuaufbau-Tag (Relationen-Klassifikation, Satz-Abdeckung,
v2-Anlauf) hat rund 150 € an Gemini-Kosten verursacht. Dieses Dokument hält fest, wo das
Geld hinging und mit welchen Maßnahmen künftige Läufe um eine Größenordnung billiger werden.

## 1. Ist-Analyse (gemessen aus den Lauf-Logs)

| Posten | Volumen | Befund |
|---|---|---|
| v2-Maker (Lauf gecrasht) | 1.000 Calls × ~264k cached Tokens = **265 Mio.** | Der amtliche Volltext-Korpus (1 Mio. Zeichen) wird je Call abgerechnet. Cached heißt ~75 % Rabatt, nicht gratis. Durch den Crash (Windows-Datei-Lock beim Checkpoint) vollständig verloren. |
| Satz-Abdeckungs-Maker (2 Anläufe) | ~2.900 Calls × 39k cached ≈ **115 Mio.** | Gleicher Mechanismus, kleinerer Korpus; Anlauf 1 (~43 Mio.) durch den ersten Lock-Crash verloren. |
| ~15.300 Verify-/Relationen-Calls | je 2–8k Tokens **uncached** ≈ 50–100 Mio. | Kein Cache möglich (jeder Prompt individuell). Haupttreiber je Call: die Praktik-Nachbarn als Negativkontext mit vollen Statements (bei BER: 92 Controls). |
| Output gesamt | ~3 Mio. Tokens | Je Token ~8× teurer als Input, aber nicht der Treiber. |
| Weggeworfene Arbeit | 2 Lock-Crashes, 2 bewusste Neustarts | **25–35 % des Tagesbudgets.** |

Kernerkenntnis: Drei Posten dominieren — cached Maker-Input (Korpusgröße × Callzahl),
uncached Verify-Prompts (Callzahl × Sibling-Ballast) und Verluste durch Abbrüche.

## 2. Maßnahmen, priorisiert nach Hebel

1. **Inkrementelle Läufe** (−90 % und mehr bei Katalog-/Kompendium-Updates): SHA-256 je
   GS++-Maßnahme und je ED23-Anforderung im Artefakt ablegen; die Stages mappen nur noch
   das Delta, unveränderte Einträge werden übernommen. Vollneuläufe bleiben die Ausnahme
   (Korpus-Semantikwechsel wie am 29.08.).
2. **Gemini Batch API** (−50 % auf alles): Die Läufe sind nicht interaktiv — als
   Batch-Jobs kosten sie die Hälfte. Einmaliger Umbau im AiClient (Submit/Poll statt
   synchroner Calls).
3. **Maker-Batching** (Cache-Kosten ÷ Batchgröße): 5–10 Maßnahmen bzw. Anforderungen je
   Maker-Call. Der 265-Mio.-Posten des v2-Laufs würde auf 26–53 Mio. fallen.
   Recall-Risiko klein; per Stichprobe (23-Control-Sample-Methode) absichern.
4. **Verify-Prompt-Diät** (−40–70 % auf den Verify-Block): Nachbar-Maßnahmen nur als
   `ID | Titel` statt mit vollem Statement — der Negativkontext bleibt benennbar.
5. **Korpus-Diät** (−30–40 % auf die Cache-Basis): Nur normative Sätze in den
   Maker-Korpus; Kontextprosa trägt zur Kandidatensuche wenig bei.
6. **Richtungs-Ökonomie**: Eine Richtung voll rechnen, die Gegenrichtung nur als
   gezielte Lückenprüfung über unabgedeckte Sätze bzw. Maßnahmen — halbiert die zweite
   Verify-Masse.
7. **Crash-Ökonomie**: os.replace-Retry und Kandidaten-Zwischencheckpoints in allen
   Stages (Stand heute: Satz-Abdeckung und Relationen ja, stage_ed23_anforderungen noch
   nicht — nachrüsten vor dem nächsten Lauf). Betrieblich: Virenscanner-Ausnahme für
   `hilfsdateien/` prüfen — die transienten Datei-Locks sind die Wurzel beider Crashes.
8. **Token-Buchhaltung als Pflicht**: usage_metadata je Stage aggregieren und am Ende
   mit €-Schätzung loggen (`scripts/analyze_token_log.py` als Grundlage). Kein Lauf mehr
   ohne Kostenzeile im Log.

**Zielbild:** Update-Zyklus unter 10 €, kompletter Neuaufbau 20–40 €.

## 3. Offener Zustand (für den nächsten Arbeitstag)

Die Kette „alles amtlich" ist halb durch:

- **Fertig und committet:** Satz-Abdeckung (`hilfsdateien/ed23_satz_abdeckung.json`,
  4.600 verifizierte Paare, amtliche Nummerierung); XML-Umbau der Mapping-Stages;
  Merge-Skript; Analyzer ohne Alignment-Stufe.
- **Ausstehend (bewusst gestoppt, Kostenentscheidung):** v2-Lauf von
  `stage_ed23_anforderungen` (vorher Maßnahmen 3, 4, 7 einbauen), danach
  `scripts/merge_ed23_mappings.py`, danach `stage_ed23_relationen` über die Union,
  danach `scripts/analyze_ed23_coverage.py` mit neuen Anker-Werten.
- **Übergangs-Inkonsistenz, bekannt:** `gpp_ed23_anforderungen.json` (3.046er) trägt
  noch Paraphrase-Satznummern, `ed23_anforderungen_stripped.json` ist bereits die
  amtliche Projektion. Bis zum v2-Lauf keine Analyse-Reports regenerieren; die
  Werkzeug-Anzeige ist nicht betroffen (sie liest satz_nr nicht).
