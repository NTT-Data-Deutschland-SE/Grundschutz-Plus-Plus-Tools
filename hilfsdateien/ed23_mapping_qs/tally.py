"""Aggregiert die Reviewer-Ergebnisse (PAIR/CTRL-Zeilen) aus results/*.txt,
prüft Vollständigkeit gegen das Mapping und baut die Master-Statistik."""
import json, re, sys
from pathlib import Path
from collections import defaultdict, Counter

SCRATCH = Path(__file__).parent
REPO = Path(r"C:\Users\micro\Documents\DEV_Projects\Claude_Working\Grundschutz-Plus-Plus-Tools")

mapping = json.loads((REPO / "hilfsdateien/gpp_ed23_anforderungen.json").read_text(encoding="utf-8"))
maps = mapping["mapping-collection"]["mappings"][0]["maps"]
expected = defaultdict(set)  # ctrl -> {(ed23id, satz)}
for m in maps:
    sid = m["sources"][0]["id-ref"]
    tid = m["targets"][0]["id-ref"]
    sn = None
    for p in m["targets"][0].get("props", []):
        if p["name"] == "statement-sentence":
            sn = p["value"]
    expected[sid].add((tid, sn))

pair_rows = []   # dicts
ctrl_rows = {}
comments = {}
bad_lines = []

def norm_axis(val):
    return val.strip().lower()

for f in sorted((SCRATCH / "results").glob("*.txt")):
    for raw in f.read_text(encoding="utf-8").splitlines():
        line = raw.strip().strip("`")
        if line.startswith("PAIR|"):
            parts = [p.strip() for p in line.split("|")]
            if len(parts) < 8:
                bad_lines.append((f.name, raw)); continue
            d = {"file": f.name, "ctrl": parts[1], "ed23": parts[2], "satznr": parts[3]}
            for p in parts[4:]:
                if "=" in p:
                    k, v = p.split("=", 1)
                    d[k.strip().lower()] = v.strip()
            pair_rows.append(d)
        elif line.startswith("CTRL|"):
            parts = [p.strip() for p in line.split("|")]
            d = {"file": f.name}
            for p in parts[2:]:
                if "=" in p:
                    k, v = p.split("=", 1)
                    d[k.strip().lower()] = v.strip()
            ctrl_rows[parts[1]] = d
        elif line.upper().startswith("KOMMENTAR"):
            # attach to last CTRL
            if ctrl_rows:
                last = list(ctrl_rows)[-1]
                comments[last] = line.split(":", 1)[-1].strip()

# ---- completeness check ----
seen = defaultdict(set)
for d in pair_rows:
    sn = d["satznr"].removeprefix("S").strip()
    if sn.upper().startswith("OHNE"):
        sn = None
    seen[d["ctrl"]].add((d["ed23"], sn))
print("== Vollständigkeit (nur gesampelte Controls mit Reviews) ==")
missing_total = 0
for ctrl in sorted(seen):
    exp = expected.get(ctrl, set())
    miss = exp - seen[ctrl]
    extra = seen[ctrl] - exp
    if miss or extra:
        missing_total += len(miss)
        print(f"{ctrl}: reviewed {len(seen[ctrl])}/{len(exp)}  fehlend={sorted(miss)[:6]}{'...' if len(miss)>6 else ''}  extra={sorted(extra)[:4]}")
print(f"Controls mit Review: {len(seen)}, Paar-Zeilen: {len(pair_rows)}, fehlende Paare: {missing_total}, bad lines: {len(bad_lines)}")
for fn, l in bad_lines[:10]:
    print("BAD:", fn, l[:120])

# ---- aggregate ----
def bucket_inhalt(v):
    v = norm_axis(v)
    if v.startswith("ja"): return "ja"
    if v.startswith("grenz"): return "grenzwertig"
    if v.startswith("nein"): return "nein"
    return "unklar:" + v

agg = defaultdict(Counter)
flags_c = defaultdict(Counter)
rel_fixes = Counter()
for d in pair_rows:
    pk = d["ctrl"].split(".")[0]
    inh = bucket_inhalt(d.get("inhalt", "?"))
    agg[pk]["pairs"] += 1
    agg[pk][inh] += 1
    rel = norm_axis(d.get("relation", "ok"))
    if not rel.startswith("ok"):
        agg[pk]["relation-falsch"] += 1
        m = re.search(r"->\s*([a-z-]+)", rel)
        if m: rel_fixes[m.group(1)] += 1
    satz = norm_axis(d.get("satz", "ok"))
    if satz.startswith("falsch"):
        agg[pk]["satz-falsch"] += 1
    begr = norm_axis(d.get("begr", "ok"))
    if not begr.startswith("ok"):
        agg[pk]["begr-problem"] += 1
    fl = d.get("flags", "-")
    for x in re.split(r"[,;]\s*", fl):
        x = x.strip().lower()
        if x and x != "-":
            flags_c[pk][x] += 1

print()
print("== Master-Statistik je Praktik ==")
hdr = f"{'Praktik':8} {'Paare':>5} {'ja':>4} {'grenzw':>6} {'nein':>4} {'rel!':>4} {'satz!':>5} {'begr!':>5}  Quote-ja"
print(hdr)
tot = Counter()
for pk in sorted(agg):
    a = agg[pk]
    for k in ["pairs","ja","grenzwertig","nein","relation-falsch","satz-falsch","begr-problem"]:
        tot[k] += a[k]
    q = a["ja"] / a["pairs"] * 100 if a["pairs"] else 0
    print(f"{pk:8} {a['pairs']:>5} {a['ja']:>4} {a['grenzwertig']:>6} {a['nein']:>4} {a['relation-falsch']:>4} {a['satz-falsch']:>5} {a['begr-problem']:>5}  {q:5.1f}%")
q = tot["ja"] / tot["pairs"] * 100 if tot["pairs"] else 0
print(f"{'TOTAL':8} {tot['pairs']:>5} {tot['ja']:>4} {tot['grenzwertig']:>6} {tot['nein']:>4} {tot['relation-falsch']:>4} {tot['satz-falsch']:>5} {tot['begr-problem']:>5}  {q:5.1f}%")

print()
print("== Relations-Korrekturvorschläge (Ziel-Typ) ==", dict(rel_fixes))
print()
print("== Flags je Praktik ==")
for pk in sorted(flags_c):
    print(pk, dict(flags_c[pk]))

print()
print("== Controls: hilfreich / drop ==")
for ctrl in sorted(ctrl_rows):
    d = ctrl_rows[ctrl]
    print(f"{ctrl:12} hilfreich={d.get('hilfreich','?'):9} drop={d.get('drop','?'):7} luecken={d.get('luecken','-')[:80]}")

# save merged json for report generation
out = {"pairs": pair_rows, "ctrls": ctrl_rows, "comments": comments}
(SCRATCH / "tally.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print()
print("tally.json geschrieben.")

# nein-pairs listing
print()
print("== Alle inhalt=nein Paare ==")
for d in pair_rows:
    if bucket_inhalt(d.get("inhalt","?")) == "nein":
        print(f"{d['ctrl']} -> {d['ed23']} {d['satz']} [{d.get('relation','')}] flags={d.get('flags','-')}")
