#!/usr/bin/env python3
"""repin.py -- Mindeststandard-Exporte auf einen neuen Anwenderkatalog-Pin umstellen.

Stellt Profil und Ergänzungskatalog eines Stamms mechanisch von einem alten auf einen
neuen Commit der Stand-der-Technik-Bibliothek um und löst den Katalog gegen den neuen
Stand neu auf (gleicher Resolver wie buildCatalog() in mindeststandard-oscal.html).
Gedacht für Pin-Wechsel OHNE inhaltliche Änderung der verwendeten Controls; das Skript
prüft das selbst und bricht ab, wenn sich mehr als Kategorienamen und Control-Klasse geändert haben;
upstream umformulierte Controls nimmt --accept-changed bewusst in der neuen Fassung mit (die alters des
Profils bleiben unverändert).

Aufruf (Repo-Wurzel):
  uv run --no-project python -I -X utf8 mindeststandards/repin.py \
      --alt <alter-katalog.json> --neu <neuer-katalog.json> --neu-commit <40er-SHA> \
      [--check-only] [--stem mindeststandard-pd-2.1 ...] [--accept-changed BER.5.2,...]

Mit --check-only wird nur der Resolver gegen die vorhandenen Kataloge geprüft
(Stämme, deren Profil schon auf dem neuen Pin steht, müssen bis auf uuid und
last-modified identisch herauskommen).
"""
from __future__ import annotations

import argparse
import copy
import datetime as dt
import hashlib
import json
import re
import sys
import uuid
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOL = HERE.parent / 'one-page-apps' / 'mindeststandard-oscal.html'
SDT_RAW = 'https://raw.githubusercontent.com/BSI-Bund/Stand-der-Technik-Bibliothek/'
CATALOG_PATH = 'control_layer/Grundschutz%2B%2B/Grundschutz%2B%2B-resolved_catalog.json'
GSMAP_PATH = 'control_layer/Mappings/IT-GS2023-zu-GSpp/ITGS-to-GS%2B%2B-mapping_collection.json'
NS_MST = 'https://github.com/NTT-Data-Deutschland-SE/Grundschutz-Plus-Plus-Tools/ns/mindeststandard'
RENAMES = {'Endgeräte': 'Mobile Endgeräte', 'Faxe': 'Faxanwendungen', 'Datenträgerarchiv': 'Archiv'}
# Formulierungen in Statements, die der Umbenennung folgen (Katalogwortlaut vorher -> nachher)
PHRASES = [('Konfiguration für Endgeräte', 'Konfiguration für Mobile Endgeräte'),
           ('Nutzende von Endgeräten', 'Nutzende von Mobilen Endgeräten')]
# Umbenannte Control-Klasse (Build 2026-10-22, Kernel-Konsolidierung: alle 901 Kernel-Controls)
CLASS_RENAMES = {'BSI-Stand-der-Technik-Kernel-G0': 'BSI-Stand-der-Technik-Kernel'}


def tool_constant(name: str) -> str:
    m = re.search(rf"^const {name} = '([^']+)';", TOOL.read_text(encoding='utf-8'), re.M)
    if not m:
        sys.exit(f'Konstante {name} nicht in {TOOL.name} gefunden')
    return m.group(1)


def dumps(doc) -> str:
    """Wie JSON.stringify(doc, null, 2) im Werkzeug (kein Zeilenumbruch am Ende)."""
    return json.dumps(doc, ensure_ascii=False, indent=2)


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.') + f'{dt.datetime.now().microsecond // 1000:03d}Z'


def load_catalog(path: Path):
    cat = json.loads(path.read_text(encoding='utf-8'))['catalog']
    by_id = {}

    def walk(groups):
        for g in groups:
            for c in g.get('controls', []):
                by_id[c['id']] = c
                walk([{'controls': c.get('controls', [])}])
            walk(g.get('groups', []))
    walk(cat.get('groups', []))
    return cat, by_id


def normalize_renames(ctl):
    """Alten Katalogwortlaut auf den neuen heben, genau so eng wie der Katalog selbst umbenannt
    hat: Kategorienwerte (target_object_categories) als Liste, Statements über die festen
    Formulierungen, Control-Klassen über CLASS_RENAMES; sonstige Prosa (Guidance, „stationäre Endgeräte“) bleibt unangetastet."""
    c = copy.deepcopy(ctl)

    def walk(node):
        if isinstance(node, dict):
            if node.get('name') == 'target_object_categories' and isinstance(node.get('value'), str):
                node['value'] = rename_categories(node['value'])
            if node.get('class') in CLASS_RENAMES:
                node['class'] = CLASS_RENAMES[node['class']]
            if isinstance(node.get('prose'), str):
                for before, after in PHRASES:
                    node['prose'] = node['prose'].replace(before, after)
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)
    walk(c)
    return c


def normalize_class(ctl):
    """Nur die Klassenumbenennung (CLASS_RENAMES), rekursiv auch in verschachtelten Kind-Controls."""
    c = copy.deepcopy(ctl)

    def walk(node):
        if isinstance(node, dict):
            if node.get('class') in CLASS_RENAMES:
                node['class'] = CLASS_RENAMES[node['class']]
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)
    walk(c)
    return c


def rename_categories(value: str) -> str:
    parts = [p.strip() for p in value.split(',')]
    return ', '.join(RENAMES.get(p, p) for p in parts)


# ---------------------------------------------------------------- Resolver (= buildCatalog)
def apply_alter(ctl, alter, warn):
    def by_id(i):
        for k in ('parts', 'params', 'links'):
            lst = ctl.get(k) or []
            for idx, x in enumerate(lst):
                if x.get('id') == i:
                    return lst, idx
        return None
    for r in alter.get('removes', []):
        if r.get('by-id'):
            t = by_id(r['by-id'])
            if t:
                t[0].pop(t[1])
            else:
                warn(f"{ctl['id']}: removes by-id {r['by-id']} trifft nichts")
        if r.get('by-name'):
            ctl['parts'] = [p for p in ctl.get('parts', []) if p.get('name') != r['by-name']]
        if r.get('by-class'):
            ctl['parts'] = [p for p in ctl.get('parts', []) if p.get('class') != r['by-class']]
        if r.get('by-ns'):
            ctl['props'] = [p for p in ctl.get('props', []) if p.get('ns') != r['by-ns']]
            ctl['parts'] = [p for p in ctl.get('parts', []) if p.get('ns') != r['by-ns']]
        if r.get('by-item-name'):
            ctl['props'] = [p for p in ctl.get('props', []) if p.get('name') != r['by-item-name']]
    for a in alter.get('adds', []):
        target = next((p for p in ctl.get('parts', []) if p.get('id') == a['by-id']), None) if a.get('by-id') else ctl
        if target is None:
            warn(f"{ctl['id']}: adds by-id {a['by-id']} trifft nichts")
            continue
        pos = a.get('position', 'ending')
        for k in ('props', 'parts', 'links', 'params'):
            if not a.get(k):
                continue
            target.setdefault(k, [])
            items = copy.deepcopy(a[k])
            target[k] = items + target[k] if pos == 'starting' else target[k] + items


def resolve_control(cid, modify, base, erg_controls, warn):
    src = base.get(cid) or erg_controls.get(cid)
    if src is None:
        raise SystemExit(f'{cid} weder im Anwenderkatalog noch im Ergänzungskatalog')
    c = copy.deepcopy(src)
    c.pop('_group', None)
    c.pop('controls', None)
    for sp in modify.get('set-parameters', []):
        p = next((x for x in c.get('params', []) if x.get('id') == sp['param-id']), None)
        if p:
            p['values'] = sp['values']
            if sp.get('label'):
                p['label'] = sp['label']
    for alter in modify.get('alters', []):
        if alter['control-id'] == cid:
            apply_alter(c, alter, warn)
    return c


def build_catalog(profile_doc, erg_doc, base, metadata, warn):
    prof = profile_doc['profile']
    modify = prof.get('modify', {})
    erg_controls = {c['id']: c for g in (erg_doc or {}).get('catalog', {}).get('groups', []) for c in g.get('controls', [])}

    def walk(g):
        out = {k: g[k] for k in ('id', 'class', 'title', 'props', 'parts', 'links') if k in g}
        ids = [i for ic in g.get('insert-controls', []) for x in ic.get('include-controls', []) for i in x.get('with-ids', [])]
        if ids:
            out['controls'] = [resolve_control(i, modify, base, erg_controls, warn) for i in ids]
        if g.get('groups'):
            out['groups'] = [walk(s) for s in g['groups']]
        return out
    return {'catalog': {'uuid': str(uuid.uuid4()), 'metadata': metadata,
                        'groups': [walk(g) for g in prof['merge']['custom']['groups']],
                        'back-matter': copy.deepcopy(prof['back-matter'])}}


def strip_volatile(doc):
    d = copy.deepcopy(doc)
    d['catalog'].pop('uuid', None)
    d['catalog']['metadata'].pop('last-modified', None)
    return d


# ---------------------------------------------------------------- Hauptlauf
def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--alt', type=Path, required=True, help='Anwenderkatalog des alten Pins (resolved_catalog.json)')
    ap.add_argument('--neu', type=Path, required=True, help='Anwenderkatalog des neuen Pins')
    ap.add_argument('--neu-commit', required=True, help='40er Commit-SHA des neuen Pins')
    ap.add_argument('--stem', action='append', help='nur diese Stämme (Standard: alle mit altem Pin)')
    ap.add_argument('--check-only', action='store_true', help='nur Resolver gegen vorhandene Kataloge prüfen')
    ap.add_argument('--accept-changed', action='append', default=[],
                    help='Control-IDs (kommagetrennt), die upstream umformuliert wurden und in der neuen Fassung übernommen werden')
    args = ap.parse_args(argv)
    accept = {i.strip() for s in args.accept_changed for i in s.split(',') if i.strip()}

    warnings: list[str] = []
    warn = warnings.append
    old_cat, old = load_catalog(args.alt)
    new_cat, new = load_catalog(args.neu)
    new_sha = hashlib.sha256(args.neu.read_bytes()).hexdigest()
    old_sha = hashlib.sha256(args.alt.read_bytes()).hexdigest()
    resource_uuid = tool_constant('CATALOG_RESOURCE_UUID')
    tool_pin = tool_constant('SDT_PIN_COMMIT')
    tool_sha = tool_constant('CATALOG_SHA256')
    if args.neu_commit != tool_pin or new_sha != tool_sha:
        sys.exit(f'Neuer Pin passt nicht zum Werkzeug: Werkzeug {tool_pin[:12]}/{tool_sha[:12]}, hier {args.neu_commit[:12]}/{new_sha[:12]}')
    new_url = f'{SDT_RAW}{args.neu_commit}/{CATALOG_PATH}'
    new_gsmap = f'{SDT_RAW}{args.neu_commit}/{GSMAP_PATH}'

    stems = args.stem or sorted({p.name[:-len('.profile.json')] for p in HERE.glob('*.profile.json')})
    rc = 0
    for stem in stems:
        prof_p, erg_p, cat_p = (HERE / f'{stem}.{k}.json' for k in ('profile', 'ergaenzungskatalog', 'catalog'))
        prof_text = prof_p.read_text(encoding='utf-8')
        prof = json.loads(prof_text)
        erg = json.loads(erg_p.read_text(encoding='utf-8')) if erg_p.exists() else None
        cat = json.loads(cat_p.read_text(encoding='utf-8'))
        p = prof['profile']
        base_res = next(r for r in p['back-matter']['resources'] if CATALOG_PATH in r['rlinks'][0]['href'])
        old_commit = re.search(r'Bibliothek/([0-9a-f]{40})/', base_res['rlinks'][0]['href']).group(1)
        on_new = old_commit == args.neu_commit

        if args.check_only:
            if not on_new:
                print(f'  {stem}: steht auf {old_commit[:12]}, Resolver-Check nur für Stände auf dem neuen Pin')
                continue
            md = copy.deepcopy(cat['catalog']['metadata'])
            rebuilt = build_catalog(prof, erg, new, md, warn)
            same = strip_volatile(rebuilt) == strip_volatile(cat)
            text_same = dumps(rebuilt).replace(rebuilt['catalog']['uuid'], cat['catalog']['uuid']) == cat_p.read_text(encoding='utf-8')
            print(f'  {stem}: Resolver {"identisch" if same else "WEICHT AB"}, Textform {"identisch" if text_same else "weicht ab"}')
            if not same:
                rc = 1
            continue

        if on_new:
            print(f'  {stem}: steht schon auf {args.neu_commit[:12]}, nichts zu tun')
            continue
        # 1) Inhaltliche Prüfung: verwendete Controls dürfen sich nur in Kategorienamen unterscheiden
        ids = [i for imp in p['imports'] for ic in imp.get('include-controls', []) for i in ic.get('with-ids', []) if i in old or i in new]
        changed, accepted, n_class = [], [], 0
        for i in ids:
            if i not in new:
                sys.exit(f'{stem}: {i} fehlt im neuen Katalog')
            a, b = dumps(old[i]), dumps(new[i])
            if a == b:
                continue
            only_class = dumps(normalize_class(old[i]))
            if only_class != a:
                n_class += 1
            if only_class == b:
                continue
            if dumps(normalize_renames(old[i])) == b:
                changed.append(i)
            elif i in accept:
                accepted.append(i)
            else:
                sys.exit(f'{stem}: {i} hat sich zwischen den Pins inhaltlich geändert, kein mechanischer Pin-Wechsel möglich'
                         f' (--accept-changed {i}, wenn die neue Fassung übernommen werden soll)')
        mech = []
        if n_class:
            mech.append('Control-Klasse ' + ', '.join(f'{a} → {b}' for a, b in CLASS_RENAMES.items()) + f' ({n_class} Controls)')
        if changed:
            mech.append(f'umbenannte Zielobjektkategorien ({len(changed)}: {", ".join(changed)})')
        befund = ('nur in ' + '; '.join(mech)) if mech else 'nicht'
        uebernommen = (f' Upstream umformuliert (Titel und Statement) und in der neuen Fassung übernommen: {", ".join(accepted)};'
                       ' die Anpassungen des Profils an diesen Controls (alters) bleiben unverändert.') if accepted else ''
        # 2) Ergänzungskatalog
        erg_sha = None
        if erg is not None:
            em = erg['catalog']['metadata']
            em['last-modified'] = now_iso()
            em['remarks'] = em['remarks'].replace(f'Pin {old_commit[:12]}', f'Pin {args.neu_commit[:12]}')
            em['remarks'] += f' Pin am {dt.date.today().isoformat()} mechanisch von {old_commit[:12]} auf {args.neu_commit[:12]} umgestellt (repin.py); die verwendeten Controls des Anwenderkatalogs unterscheiden sich zwischen beiden Ständen {befund}.{uebernommen}'
            erg['catalog']['uuid'] = str(uuid.uuid4())
            n_cat = n_link = 0
            for g in erg['catalog'].get('groups', []):
                for c in g.get('controls', []):
                    for part in c.get('parts', []):
                        for pr in part.get('props', []):
                            if pr.get('name') == 'target_object_categories':
                                nv = rename_categories(pr['value'])
                                if nv != pr['value']:
                                    pr['value'] = nv
                                    n_cat += 1
                    for lnk in c.get('links', []):
                        if old_commit in lnk.get('href', ''):
                            lnk['href'] = lnk['href'].replace(old_commit, args.neu_commit)
                            n_link += 1
            erg_text = dumps(erg)
            erg_sha = sha256(erg_text)
            erg_p.write_text(erg_text, encoding='utf-8', newline='')
            print(f'  {stem}: Ergänzungskatalog: {n_link} Links umgepinnt, {n_cat} Kategorienwerte umbenannt, SHA-256 {erg_sha[:12]}')
        # 3) Profil
        old_res_uuid = base_res['uuid']
        base_res['uuid'] = resource_uuid
        base_res['title'] = f'Grundschutz++-resolved_catalog.json @ {args.neu_commit[:12]}'
        base_res['description'] = f"{new_cat['metadata'].get('title') or 'Anwenderkatalog Grundschutz++'}, Version {new_cat['metadata'].get('version', '?')}"
        base_res['rlinks'][0]['href'] = new_url
        base_res['rlinks'][0]['hashes'] = [{'algorithm': 'SHA-256', 'value': new_sha}]
        for imp in p['imports']:
            if imp['href'] == f'#{old_res_uuid}':
                imp['href'] = f'#{resource_uuid}'
        for r in p['back-matter']['resources']:
            href = r['rlinks'][0]['href']
            if GSMAP_PATH in href:
                r['rlinks'][0]['href'] = new_gsmap
                r['title'] = r['title'].replace(old_commit[:12], args.neu_commit[:12])
                old_u, r['uuid'] = r['uuid'], str(uuid.uuid5(uuid.NAMESPACE_URL, new_gsmap))
                for imp in p['imports']:
                    if imp['href'] == f'#{old_u}':
                        imp['href'] = f'#{r["uuid"]}'
            if href.endswith('.ergaenzungskatalog.json') and erg_sha:
                old_u = r['uuid']
                r['uuid'] = str(uuid.uuid5(uuid.NAMESPACE_URL, f'ergaenzungskatalog:{erg_sha}'))
                r['rlinks'][0]['hashes'] = [{'algorithm': 'SHA-256', 'value': erg_sha}]
                for imp in p['imports']:
                    if imp['href'] == f'#{old_u}':
                        imp['href'] = f'#{r["uuid"]}'
        n_phr = 0
        for alter in p.get('modify', {}).get('alters', []):
            for a in alter.get('adds', []):
                for part in a.get('parts', []):
                    if part.get('name') == 'statement':
                        for before, after in PHRASES:
                            if before in part.get('prose', ''):
                                part['prose'] = part['prose'].replace(before, after)
                                n_phr += 1
        pm = p['metadata']
        pm['last-modified'] = now_iso()
        pm['remarks'] += f' Pin am {dt.date.today().isoformat()} mechanisch von {old_commit[:12]} auf {args.neu_commit[:12]} umgestellt (repin.py, Katalog neu aufgelöst); die {len(ids)} verwendeten Controls unterscheiden sich zwischen beiden Ständen {befund}.{uebernommen}'
        p['uuid'] = str(uuid.uuid4())
        prof_text_new = dumps(prof)
        prof_p.write_text(prof_text_new, encoding='utf-8', newline='')
        # 4) Katalog neu auflösen
        cm = copy.deepcopy(cat['catalog']['metadata'])
        cm['last-modified'] = now_iso()
        for pr in cm.get('props', []):
            if pr.get('name') == 'resolution-tool' and 'repin.py' not in pr['value']:
                pr['value'] += ' · mindeststandards/repin.py (gleicher Resolver)'
        cm['remarks'] += f' Am {dt.date.today().isoformat()} gegen den Anwenderkatalog-Stand {args.neu_commit[:12]} neu aufgelöst (repin.py).'
        new_catalog = build_catalog(prof, erg, new, cm, warn)
        cat_p.write_text(dumps(new_catalog), encoding='utf-8', newline='')
        n_ctl = sum(1 for _ in iter_controls(new_catalog['catalog']['groups']))
        print(f'  {stem}: Profil auf {args.neu_commit[:12]} ({len(ids)} Controls, {n_class} mit neuer Klasse, {len(changed)} mit Kategorienamen, {len(accepted)} upstream umformuliert, {n_phr} Statement-Formulierungen nachgezogen), Katalog neu aufgelöst: {n_ctl} Controls, SHA-256 Profil {sha256(prof_text_new)[:12]}')
    for w in warnings:
        print('  Hinweis:', w)
    return rc


def iter_controls(groups):
    for g in groups:
        yield from g.get('controls', [])
        yield from iter_controls(g.get('groups', []))


if __name__ == '__main__':
    sys.exit(main())
