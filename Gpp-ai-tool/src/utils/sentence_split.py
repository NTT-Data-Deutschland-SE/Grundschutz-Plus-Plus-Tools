"""
German sentence splitting for BSI/G++ prose — the single source of truth.

Moved verbatim from pipeline/stage_ed23_anforderungen.py so that stdlib-only
consumers (scripts/analyze_ed23_coverage.py) can import it without pulling the
AI client chain. The numbering produced by `split_sentences` defines the
`satz_nr` / `statement-sentence` semantics of hilfsdateien/gpp_ed23_anforderungen.json,
so any change here changes what a "Teilanforderung" refers to.
"""

import re
from typing import List

# German abbreviations that end in a period but do not end a sentence. Kept conservative:
# only forms that actually occur in BSI/G++ prose and are unambiguous.
ABBREVIATIONS = (
    "z. B.", "z.B.", "d. h.", "d.h.", "u. a.", "u.a.", "u. U.", "o. Ä.", "o.Ä.",
    "i. d. R.", "bzw.", "ggf.", "etc.", "evtl.", "inkl.", "vgl.", "bspw.",
    "sog.", "ca.", "max.", "min.", "Nr.", "Abs.",
    # Issue #37 (Mapping-QS): "(engl. Predictive Maintenance)" wurde mitten im Satz
    # getrennt und erzeugte Fragment-Doppelpaare (OPS.1.1.1.A26, INF.13.A18). Der
    # Korpus-Scan fand keine weiteren fehlenden Abkuerzungen (alle anderen
    # Kandidaten sind legitime satzfinale Verben).
    "engl.",
)
# Sentence boundary: terminal punctuation, whitespace, then an uppercase/quote/paren opener.
SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-ZÄÖÜ„\"(])")


def split_sentences(text: str) -> List[str]:
    """Splits German prose into sentences without breaking at known abbreviations.

    Used to number the sentences of every ED2023 Anforderung so the model can reference the
    exact sentence (`satz_nr`) that carries a match. The same function validates the returned
    numbers, so numbering is always self-consistent. Abbreviation periods are masked with a
    sentinel before splitting (multi-word forms like "z. B." would otherwise split
    internally) and restored afterwards.
    """
    normalized = " ".join((text or "").split())
    if not normalized:
        return []
    sentinel = "\x00"
    for abbr in sorted(ABBREVIATIONS, key=len, reverse=True):
        normalized = normalized.replace(abbr, abbr.replace(".", sentinel))
    pieces = SENTENCE_SPLIT.split(normalized)
    return [p.replace(sentinel, ".").strip() for p in pieces if p.strip()]
