"""Erzeugt pro GS++-Praktik ein Review-Dossier (Markdown) mit 5 stratifiziert
gesampelten Controls und allen ihren ED23-Zuordnungen samt amtlichen Satztexten.
Stratifizierung: max. Paare, min. Paare, Median, + 2 seeded-random (seed=23)."""
import json, random, re, sys
from pathlib import Path
from collections import defaultdict

REPO = Path(r"C:\Users\micro\Documents\DEV_Projects\Claude_Working\Grundschutz-Plus-Plus-Tools")
OUT = Path(__file__).parent / "dossiers"
OUT.mkdir(exist_ok=True)

mapping = json.loads((REPO / "hilfsdateien/gpp_ed23_anforderungen.json").read_text(encoding="utf-8"))
maps = mapping["mapping-collection"]["mappings"][0]["maps"]

ed = json.loads((REPO / "hilfsdateien/ed23_anforderungen_stripped.json").read_text(encoding="utf-8"))
ed_by_id = {a["id"]: a for a in ed["ed23_anforderungen"]}

cat = json.loads((REPO / "Gpp-ai-tool/.cache/ed23_gap/gpp-resolved_catalog@36a0fac473c6.json").read_text(encoding="utf-8"))

# ---- flatten catalog controls ----
controls = {}
def walk_controls(ctls):
    for c in ctls or []:
        controls[c["id"]] = c
        walk_controls(c.get("controls"))
def walk_groups(groups):
    for g in groups or []:
        walk_controls(g.get("controls"))
        walk_groups(g.get("groups"))
walk_groups(cat["catalog"].get("groups"))
print(f"catalog controls: {len(controls)}")

def part_prose(ctl, name):
    for p in ctl.get("parts", []):
        if p.get("name") == name:
            return p.get("prose", "")
    return ""

def prop(obj, name):
    for p in obj.get("props", []):
        if p.get("name") == name:
            return p.get("value")
    return None

# ---- group maps by source control ----
by_source = defaultdict(list)
for m in maps:
    by_source[m["sources"][0]["id-ref"]].append(m)

by_praktik = defaultdict(list)  # praktik -> [(ctrl_id, n_pairs)]
for cid, ms in by_source.items():
    by_praktik[cid.split(".")[0]].append((cid, len(ms)))

# ---- sanity check sentence indexing ----
app = ed_by_id["APP.3.6.A1"]
print("APP.3.6.A1 Satz 4 (1-basiert):", app["saetze"][3][:120])

# ---- stratified sampling ----
rng = random.Random(23)
samples = {}
for pk, lst in sorted(by_praktik.items()):
    lst = sorted(lst, key=lambda t: (-t[1], t[0]))
    n = len(lst)
    if n <= 5:
        chosen = [c for c, _ in lst]
    else:
        fixed = {lst[0][0], lst[-1][0], lst[n // 2][0]}
        rest = [c for c, _ in lst if c not in fixed]
        chosen = sorted(fixed) + rng.sample(rest, 5 - len(fixed))
    samples[pk] = chosen

# ---- emit dossiers ----
REL_ORDER = {"equal-to": 0, "equivalent-to": 1, "superset-of": 2, "subset-of": 3, "intersects-with": 4}
total_pairs = 0
for pk, chosen in samples.items():
    lines = []
    praktik_pairs = sum(n for _, n in by_praktik[pk])
    lines.append(f"# Review-Dossier Praktik {pk}")
    lines.append("")
    lines.append(f"Praktik {pk}: {len(by_praktik[pk])} Controls mit Mapping, {praktik_pairs} Paare gesamt. "
                 f"Gesampelt: {len(chosen)} Controls (max/min/median Paarzahl + 2 zufällig).")
    lines.append("")
    for cid in chosen:
        ctl = controls.get(cid)
        ms = by_source[cid]
        total_pairs += len(ms)
        lines.append(f"## {cid} — {ctl['title'] if ctl else '?? NICHT IM KATALOG ??'}  [{len(ms)} Paare]")
        if not ctl:
            lines.append("**FEHLER: Control nicht im gepinnten Katalog 36a0fac4!**")
            lines.append("")
            continue
        stm = part_prose(ctl, "statement")
        gdn = part_prose(ctl, "guidance")
        lines.append("")
        lines.append(f"**Statement (normativ):** {stm}")
        sec = prop(ctl, "sec_level")
        lines.append(f"**Klasse:** {ctl.get('class','')} | **sec_level:** {sec}")
        if gdn:
            g = gdn if len(gdn) <= 3000 else gdn[:3000] + " […Guidance gekürzt…]"
            lines.append(f"**Guidance (nicht normativ):** {g}")
        lines.append("")
        # group pairs by target requirement
        by_target = defaultdict(list)
        for m in ms:
            by_target[m["targets"][0]["id-ref"]].append(m)
        for tid in sorted(by_target, key=lambda t: (min(REL_ORDER.get(x.get("relationship"), 9) for x in by_target[t]), t)):
            tms = by_target[tid]
            edreq = ed_by_id.get(tid)
            lines.append(f"### → {tid} — {edreq['name'] if edreq else '?? NICHT IN ED23-STRIPPED ??'}")
            cited = {}
            for m in tms:
                sn = prop(m["targets"][0], "statement-sentence")
                cited[sn] = m
            if edreq:
                for i, s in enumerate(edreq["saetze"], 1):
                    mark = " **◀ ZITIERT**" if str(i) in cited else ""
                    lines.append(f"  {i}. {s}{mark}")
            for sn, m in sorted(cited.items(), key=lambda kv: (kv[0] is None, kv[0])):
                rel = m.get("relationship")
                direction = prop(m, "matching-direction")
                sn_str = sn if sn is not None else "OHNE SATZ"
                lines.append(f"- **Satz {sn_str}** | Relation GS++→ED23: `{rel}` | Fundrichtung: {direction}")
                lines.append(f"  Begründung: {m.get('remarks','(keine)')}")
            lines.append("")
        lines.append("")
    (OUT / f"dossier_{pk}.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"{pk}: {len(chosen)} Controls, {sum(len(by_source[c]) for c in chosen)} Paare -> dossier_{pk}.md "
          f"({(OUT / f'dossier_{pk}.md').stat().st_size // 1024} KB)")
print("TOTAL sampled pairs:", total_pairs)
