#!/usr/bin/env python3
"""Bewertet SSP-Exporte des Generators (Plan Abschnitt 4), ohne Modellaufruf.

Liest je Export das OSCAL-SSP und den Analyse-Payload ("KI-Dokumentanalyse"
in der Back-Matter) und gibt die Kennzahlen als Markdown-Tabelle aus.

Dokumentunabhaengige Kennzahlen laufen immer; die RECPLAST-Kennzahlen nur mit
--gold QS/recplast (Ground Truth aus build_gold.py).

Aufruf:  python score_ssp.py [--gold QS/recplast] export1.json [export2.json ...]
"""
import argparse, base64, collections, csv, json, pathlib, re, sys

OSCAL_COMPONENT_TYPES = {"this-system", "system", "interconnection", "software", "hardware", "service",
                         "policy", "physical", "process-procedure", "plan", "guidance", "standard", "validation", "network"}
STATUS_VALUES = {"implemented", "partial", "planned", "alternative", "not-applicable", "not-implemented", ""}
LEVEL_VALUES = {"low", "medium", "high", "very-high", "", "unbewertet"}
HAEUFIGKEIT = {"selten": "low", "mittel": "medium", "häufig": "high", "sehr häufig": "very-high"}
AUSWIRKUNG = {"vernachlässigbar": "low", "begrenzt": "medium", "beträchtlich": "high", "existenzbedrohend": "very-high"}
ENGLISH = re.compile(r"\b(the|and|with|for|extracted|security plan|system security|measures|assets from)\b", re.I)
AEOEUE = re.compile(r"[a-z](ae|oe|ue)[a-z]", re.I)
GENERATOR_COMPONENTS = {"Risikoanalyse Controls", "Basis Methodik (standard)"}


def props(o):
    return {p.get("name"): p.get("value") for p in (o.get("props") or [])}


def load_export(path):
    d = json.load(open(path, encoding="utf-8"))
    ssp = d["system-security-plan"]
    analysis = None
    for r in ssp.get("back-matter", {}).get("resources", []):
        if r.get("title") == "KI-Dokumentanalyse" and r.get("base64"):
            analysis = json.loads(base64.b64decode(r["base64"]["value"]).decode("utf-8"))
    return ssp, analysis


def load_gold(folder):
    g = {}
    for name in ("zielobjekte", "schutzbedarf", "grundschutz_check", "risiken", "rollen"):
        p = pathlib.Path(folder) / f"{name}.csv"
        g[name] = list(csv.DictReader(open(p, encoding="utf-8"), delimiter=";")) if p.exists() else []
    return g


def norm_id(s):
    return re.sub(r"\s+", "", str(s or "")).upper()


def score(path, gold):
    ssp, ana = load_export(path)
    comps = ssp["system-implementation"]["components"]
    real = [c for c in comps if c.get("type") != "this-system" and c.get("title") not in GENERATOR_COMPONENTS
            and not str(c.get("title", "")).startswith("Prozess: ")]
    irs = ssp["control-implementation"]["implemented-requirements"]
    out = collections.OrderedDict()
    out["Modell"] = f'{ana["model"].get("provider", "?")}/{ana["model"].get("model", "?")}' if ana else "?"
    out["Komponenten (ohne Generator-Eigene)"] = len(real)

    # --- dokumentunabhaengig ---------------------------------------------
    assets = ana.get("assets", []) if ana else []
    procs = ana.get("processes", []) if ana else []
    ctrls = ana.get("controls", []) if ana else []
    risks = ana.get("risks", []) if ana else []
    impls = [i for c in ctrls for i in c.get("implementations", [])]
    comp_ids = {norm_id(props(c).get("source-id")) for c in comps if props(c).get("source-id")}
    verworfen = [a for a in assets if a.get("sourceId") and norm_id(a["sourceId"]) not in comp_ids]
    out["Verworfene Analyse-Assets (nicht als Komponente)"] = len(verworfen)
    unbest_sb = sum(1 for a in assets if (a.get("schutzbedarf") or "") in ("", "unbestimmt"))
    unbest_st = sum(1 for i in impls if (i.get("status") or "") in ("", "unbestimmt"))
    unbest_rk = sum(1 for r in risks if (r.get("likelihood") or "") in ("", "unbewertet"))
    out["Unbestimmt: Schutzbedarf / Status / Risikoskala"] = f"{unbest_sb}/{len(assets)} · {unbest_st}/{len(impls)} · {unbest_rk}/{len(risks)}"
    types_ok = sum(1 for a in assets if (a.get("componentType") or "") in OSCAL_COMPONENT_TYPES)
    types_distinct = len({a.get("componentType") for a in assets})
    st_ok = sum(1 for i in impls if (i.get("status") or "") in STATUS_VALUES)
    lv_ok = sum(1 for r in risks if (r.get("likelihood") or "") in LEVEL_VALUES and (r.get("impact") or "") in LEVEL_VALUES)
    out["Vokabular: Typ konform / Typen verschieden"] = f"{types_ok}/{len(assets)} · {types_distinct}"
    out["Vokabular: Status konform, Skala konform"] = f"{st_ok}/{len(impls)} · {lv_ok}/{len(risks)}"
    all_medium = sum(1 for r in risks if r.get("likelihood") == "medium" and r.get("impact") == "medium")
    out["Risiken medium/medium"] = f"{all_medium}/{len(risks)}"
    belegt = sum(1 for e in assets + procs + ctrls + risks if e.get("quote") and e.get("quoteVerified"))
    out["Belegquote (verifiziertes Zitat)"] = f"{belegt}/{len(assets) + len(procs) + len(ctrls) + len(risks)}"
    texts = [str(v) for e in assets + procs + ctrls + risks for v in e.values() if isinstance(v, str)]
    out["Sprache: Felder englisch / ae-oe-ue"] = f"{sum(1 for t in texts if ENGLISH.search(t))} · {sum(1 for t in texts if AEOEUE.search(t))}"
    ai_ids = [c["controlId"] for c in ctrls if str(c.get("controlId", "")).upper().startswith("AI-")]
    out["AI-IDs (Muster)"] = f"{len(ai_ids)} · {len({re.sub(r'[0-9]+', '#', x) for x in ai_ids})} Muster"
    out["Zuordnung deterministisch (ED23-Mapping)"] = sum(1 for c in ctrls if c.get("coverageSource") == "ed23-mapping")
    out["Schutzbedarf-Herkunft vererbt"] = sum(1 for c in comps if props(c).get("sicherheitsniveau-herkunft", "").startswith("vererbt"))

    # --- RECPLAST-Ground-Truth ------------------------------------------------
    if gold and gold["zielobjekte"]:
        gold_ids = {norm_id(r["id"]) for r in gold["zielobjekte"] if r["typ"] != "teilprozess"}
        ana_ids = {norm_id(x.get("sourceId")) for x in assets + procs}
        found_ana = gold_ids & ana_ids
        found_ssp = gold_ids & comp_ids
        out["Zielobjekt-Recall: Analyse / SSP"] = f"{len(found_ana)}/{len(gold_ids)} · {len(found_ssp)}/{len(gold_ids)}"
        out["Dublettenverhältnis (Komponenten je gefundener Kennung)"] = f"{len(real) / max(1, len(found_ssp)):.2f}"
        comp_by_id = {}
        for c in comps:
            sid = norm_id(props(c).get("source-id"))
            if sid:
                comp_by_id.setdefault(sid, c)
        expl = [r for r in gold["schutzbedarf"] if r["gspp_sicherheitsniveau"] == "erhöht" and not r["id"].startswith("GP")]
        hit = falsch = fehlt = 0
        for r in expl:
            c = comp_by_id.get(norm_id(r["id"]))
            if not c:
                fehlt += 1
            elif props(c).get("sicherheitsniveau") == "erhöht":
                hit += 1
            else:
                falsch += 1
        out[f"Schutzbedarf explizit ({len(expl)} Objekte): Treffer / falsch / fehlt"] = f"{hit} / {falsch} / {fehlt}"
        out["Objekte auf erhöht gesamt"] = sum(1 for c in comps if props(c).get("sicherheitsniveau") == "erhöht")
        gp = [r for r in gold["schutzbedarf"] if r["id"].startswith("GP") and r["gspp_sicherheitsniveau"] == "erhöht"]
        gp_hit = sum(1 for r in gp if props(comp_by_id.get(norm_id(r["id"]), {})).get("sicherheitsniveau") == "erhöht")
        out[f"Schutzbedarf Geschäftsprozesse ({len(gp)}): Treffer"] = gp_hit
        # Status: Analyse-Controls mit Kompendiums-ID
        ctrl_by_id = {norm_id(c.get("controlId")): c for c in ctrls}
        ok = erfasst = 0
        for r in gold["grundschutz_check"]:
            c = ctrl_by_id.get(norm_id(r["anforderung"]))
            if not c:
                continue
            erfasst += 1
            statuses = {i.get("status") for i in c.get("implementations", [])}
            if r["status_oscal"] in statuses:
                ok += 1
        out["Umsetzungsstatus (49): korrekt / erfasst"] = f"{ok} / {erfasst}"
        # Risikoskalen Tabelle 28 (S007) und 29
        gold_r = {(r["gefaehrdung"], r["zielobjekt"]): r for r in gold["risiken"]}
        r_ok = r_found = 0
        for rk in risks:
            m = re.search(r"G\s*0\.(\d+)", f'{rk.get("title", "")} {rk.get("threat", "")}')
            if not m:
                continue
            key = f"G 0.{m.group(1)}"
            refs = [norm_id(x) for x in rk.get("targetRefs", [])]
            target = "S007" if "S007" in refs else ("GP001" if "GP001" in refs else None)
            cand = gold_r.get((key, target)) or gold_r.get((key, "S007")) or gold_r.get((key, "GP001"))
            if not cand:
                continue
            r_found += 1
            if HAEUFIGKEIT.get(cand["haeufigkeit"]) == rk.get("likelihood") and AUSWIRKUNG.get(cand["auswirkung"]) == rk.get("impact"):
                r_ok += 1
        out["Risikoskalen laut PDF: korrekt / erkannte Gefährdungen"] = f"{r_ok} / {r_found}"
        rollen = [r["rolle"].lower() for r in gold["rollen"]]
        parties = [i.get("responsibleParty", "") for i in impls if i.get("responsibleParty")]
        fremd = [p for p in parties if not any(r in p.lower() for r in rollen) and not re.match(r"^nicht (angegeben|spezifiziert|dokumentiert)", p, re.I)]
        out["Verantwortliche außerhalb der PDF-Rollen"] = f"{len(fremd)}/{len(parties)}"
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gold", default=None)
    ap.add_argument("exports", nargs="+")
    a = ap.parse_args()
    gold = load_gold(a.gold) if a.gold else None
    results = [(pathlib.Path(p).name, score(p, gold)) for p in a.exports]
    keys = list(results[0][1].keys())
    print("| Kennzahl | " + " | ".join(n for n, _ in results) + " |")
    print("|---|" + "---|" * len(results))
    for k in keys:
        print(f"| {k} | " + " | ".join(str(r.get(k, "")) for _, r in results) + " |")


if __name__ == "__main__":
    main()
