"""Prüft die ED23-Baustein-Profile und den NG-Ergänzungskatalog in einem Ordner (Gpp-ai-tool-Ausgabe).

Je Profil (plain und _enhanced): OSCAL-1.2.2-Schema (merge/combine/@method ausgeblendet, siehe
Handbuch Anhang D37), Importe zeigen auf Back-Matter-Resources, der NG-Import hat einen relativen
rlink auf NG-ergaenzungskatalog.json mit dem SHA-256 der Datei (fail closed), NG-with-ids liegen
im Katalog, G++-with-ids im gepinnten Anwenderkatalog (Hash geprüft), jedes Control genau einmal
eingefügt, Fragment-Links treffen, alters zeigen auf importierte Controls, Reifegrad-Part-IDs
eindeutig, herkunft ⇔ NG_-Dateiname ⇔ „NG “-Titel, jede Anforderungsgruppe hat Controls, einen
Link, ohne-control oder entfallen, plain und enhanced haben identische merge/imports.
Der NG-Katalog: Schema, IDs eindeutig und NG-, class ng-ergaenzung, Titel NG:, herkunft=NG, genau
ein Modalverb je Statement, related-Links auflösbar.

Aufruf:
  PYTHONUTF8=1 uv run --no-project --with jsonschema --with regex python -I ED23-Baustein-profile/pruefe_export.py ED23-Baustein-profile/DE [--gpp-catalog <datei>] [--offline]
Ohne jsonschema/regex läuft die Prüfung ohne Schemateil weiter und sagt das. --offline überspringt
den Download des Anwenderkatalogs (dann keine Prüfung der G++-IDs). Exit 0 = alles ok, 1 = Befunde,
2 = Aufruffehler.
"""
import copy
import hashlib
import json
import pathlib
import re
import sys
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'mindeststandards'))
from pruefe_export import load_validator, schema_errors, walk_controls  # noqa: E402

NS_ED23 = 'https://github.com/NTT-Data-Deutschland-SE/Grundschutz-Plus-Plus-Tools/ns/ed23-baustein'
NG_FILE = 'NG-ergaenzungskatalog.json'
ANF_RE = re.compile(r'^[A-Z]{2,7}(?:\.\d+)+\.A\d+$')
MODAL_RE = re.compile(r'\b(DARF NICHT|DÜRFEN NICHT|DARF NUR|DÜRFEN NUR|MUSS|MÜSSEN|SOLLTE|SOLLTEN|KANN|KÖNNEN)\b')
CACHE = HERE.parent / 'Gpp-ai-tool' / '.cache' / 'pruefe_export'


def prop(obj, name, ns=None):
    for p in obj.get('props', []) or []:
        if p.get('name') == name and (ns is None or p.get('ns') == ns):
            return p.get('value')
    return None


def fetch_catalog(resource, local, offline):
    """Returns the set of G++ control ids of the pinned Anwenderkatalog (or None)."""
    rl = (resource.get('rlinks') or [{}])[0]
    want = next((h.get('value') for h in rl.get('hashes', []) if h.get('algorithm') == 'SHA-256'), '')
    data = None
    if local:
        data = pathlib.Path(local).read_bytes()
    elif not offline:
        CACHE.mkdir(parents=True, exist_ok=True)
        cached = CACHE / f'{want[:16]}.json'
        if cached.exists():
            data = cached.read_bytes()
        else:
            with urllib.request.urlopen(rl['href'], timeout=60) as r:
                data = r.read()
            cached.write_bytes(data)
    if data is None:
        return None, 'übersprungen (--offline)'
    have = hashlib.sha256(data).hexdigest()
    if want and have != want:
        return None, f'Hash des Anwenderkatalogs weicht ab (Resource {want[:12]}…, Datei {have[:12]}…)'
    ids = {c['id'] for c in walk_controls(json.loads(data)['catalog'].get('groups', []), [])}
    return ids, None


def check_ng_catalog(path, js):
    findings = []
    doc = json.loads(path.read_text(encoding='utf-8'))
    cat = doc.get('catalog') or {}
    for e in schema_errors(js, 'catalog', doc)[:10]:
        findings.append(f'{NG_FILE}: Schema catalog: {e}')
    if not str(cat.get('metadata', {}).get('title', '')).startswith('NG Ergänzungskatalog'):
        findings.append(f'{NG_FILE}: Titel beginnt nicht mit „NG Ergänzungskatalog“')
    if prop(cat.get('metadata', {}), 'herkunft', NS_ED23) != 'NG':
        findings.append(f'{NG_FILE}: Metadata-Prop herkunft=NG fehlt')
    controls = walk_controls(cat.get('groups', []), [])
    ids = [c['id'] for c in controls]
    dups = sorted({i for i in ids if ids.count(i) > 1})
    if dups:
        findings.append(f'{NG_FILE}: Controls mehrfach: {", ".join(dups[:8])}')
    idset = set(ids)
    gids = []

    def walk_groups(groups):
        for g in groups:
            gids.append(g.get('id'))
            walk_groups(g.get('groups', []))
    walk_groups(cat.get('groups', []))
    if len(gids) != len(set(gids)):
        findings.append(f'{NG_FILE}: Gruppen-IDs nicht eindeutig')
    for c in controls:
        cid = c['id']
        if not cid.startswith('NG-'):
            findings.append(f'{NG_FILE}: {cid} ohne Präfix NG-')
        if c.get('class') != 'ng-ergaenzung':
            findings.append(f'{NG_FILE}: {cid} class ist {c.get("class")!r}, erwartet ng-ergaenzung')
        if not str(c.get('title', '')).startswith('NG: '):
            findings.append(f'{NG_FILE}: {cid} Titel beginnt nicht mit „NG: “')
        if prop(c, 'herkunft', NS_ED23) != 'NG':
            findings.append(f'{NG_FILE}: {cid} ohne Prop herkunft=NG')
        anf = prop(c, 'ed23-anforderung', NS_ED23) or ''
        if not ANF_RE.match(anf):
            findings.append(f'{NG_FILE}: {cid} ed23-anforderung {anf!r} ist keine Anforderungs-ID')
        elif cid != f'NG-{anf}':
            findings.append(f'{NG_FILE}: {cid} passt nicht zur Anforderung {anf}')
        stm = next((p for p in c.get('parts', []) if p.get('name') == 'statement'), None)
        if not stm or not stm.get('prose'):
            findings.append(f'{NG_FILE}: {cid} ohne Statement')
        else:
            verbs = {m.group(1) for m in MODAL_RE.finditer(stm['prose'])}
            if len(verbs) != 1:
                findings.append(f'{NG_FILE}: {cid} Statement hat {len(verbs)} Modalverben statt genau eines')
        for lnk in c.get('links', []):
            href = lnk.get('href', '')
            if href.startswith('#') and href[1:] not in idset:
                findings.append(f'{NG_FILE}: Link {href} an {cid} zeigt auf kein Control des Katalogs')
            elif not href.startswith('#') and '#' not in href:
                findings.append(f'{NG_FILE}: Link {href} an {cid} ohne Fragment')
    print(f'  {NG_FILE}: {len(ids)} NG-Controls, {len(findings)} Befunde')
    return findings, idset


def check_profile(path, js, ng_ids, ng_sha, gpp_ids):
    name = path.name
    findings = []
    doc = json.loads(path.read_text(encoding='utf-8'))
    p = doc.get('profile')
    if not p:
        return [f'{name}: kein Profil'], None
    prof_v = copy.deepcopy(doc)
    comb = prof_v.get('profile', {}).get('merge', {}).get('combine')
    if isinstance(comb, dict) and comb.get('method') in ('use-first', 'keep'):
        del comb['method']
    for e in schema_errors(js, 'profile', prof_v)[:10]:
        findings.append(f'{name}: Schema profile: {e}')
    meta = p.get('metadata', {})
    herkunft = prop(meta, 'herkunft', NS_ED23)
    if herkunft not in ('BSI', 'NG'):
        findings.append(f'{name}: Metadata-Prop herkunft fehlt oder ungültig ({herkunft!r})')
    if not prop(meta, 'ed23-baustein', NS_ED23):
        findings.append(f'{name}: Metadata-Prop ed23-baustein fehlt')
    is_ng_file = name.startswith('NG_')
    if is_ng_file != (herkunft == 'NG'):
        findings.append(f'{name}: Dateipräfix NG_ passt nicht zu herkunft={herkunft}')
    if is_ng_file != str(meta.get('title', '')).startswith('NG '):
        findings.append(f'{name}: Titelpräfix „NG “ passt nicht zum Dateinamen')
    if (p.get('merge', {}).get('combine') or {}).get('method') != 'use-first':
        findings.append(f'{name}: merge.combine.method ist nicht use-first')

    resources = {r['uuid']: r for r in p.get('back-matter', {}).get('resources', [])}
    imported = set()
    for i, imp in enumerate(p.get('imports', [])):
        href = imp.get('href', '')
        res = resources.get(href[1:]) if href.startswith('#') else None
        if res is None:
            findings.append(f'{name}: Import {href} zeigt auf keine Back-Matter-Resource')
        ids = [x for ic in imp.get('include-controls', []) for x in ic.get('with-ids', [])]
        if not ids:
            findings.append(f'{name}: Import {i} ohne with-ids')
        imported.update(ids)
        if i == 0:
            bad = [x for x in ids if x.startswith('NG-')]
            if bad:
                findings.append(f'{name}: NG-IDs im Anwenderkatalog-Import: {bad[:5]}')
            if gpp_ids is not None:
                unknown = sorted(set(ids) - gpp_ids)
                if unknown:
                    findings.append(f'{name}: nicht im gepinnten Anwenderkatalog: {unknown[:8]}')
        elif i == 1:
            rl = ((res or {}).get('rlinks') or [{}])[0]
            if rl.get('href') != NG_FILE:
                findings.append(f'{name}: NG-Resource rlink ist {rl.get("href")!r}, erwartet relativ {NG_FILE}')
            want = next((h.get('value') for h in rl.get('hashes', []) if h.get('algorithm') == 'SHA-256'), '')
            if ng_sha is None:
                findings.append(f'{name}: NG-Import, aber {NG_FILE} fehlt im Ordner')
            elif want != ng_sha:
                findings.append(f'{name}: Hash des NG-Katalogs weicht ab (Profil {want[:12]}…, Datei {ng_sha[:12]}…)')
            bad = [x for x in ids if not x.startswith('NG-')]
            if bad:
                findings.append(f'{name}: Nicht-NG-IDs im NG-Import: {bad[:5]}')
            unknown = sorted(set(ids) - (ng_ids or set()))
            if unknown:
                findings.append(f'{name}: NG-IDs nicht im Katalog: {unknown[:5]}')
        else:
            findings.append(f'{name}: mehr als zwei Importe')

    inserted = {}
    links = []
    gids = []

    def walk(groups):
        for g in groups:
            gids.append(g.get('id'))
            if g.get('class') == 'ed23-anforderung':
                own = [x for ins in g.get('insert-controls', []) for ic in ins.get('include-controls', []) for x in ic.get('with-ids', [])]
                for x in own:
                    if x in inserted:
                        findings.append(f'{name}: {x} doppelt eingefügt ({inserted[x]} und {g["id"]})')
                    inserted[x] = g['id']
                    if x not in imported:
                        findings.append(f'{name}: {g["id"]} fügt {x} ein, das nicht importiert ist')
                related = [l for l in g.get('links', []) if l.get('rel') == 'related']
                links.extend((g['id'], l.get('href', '')) for l in related)
                if not (own or related or prop(g, 'ohne-control', NS_ED23) or prop(g, 'entfallen', NS_ED23)):
                    findings.append(f'{name}: Gruppe {g["id"]} hat weder Controls noch Link, ohne-control oder entfallen')
                if not prop(g, 'entfallen', NS_ED23) and not any(pt.get('name') == 'overview' and pt.get('prose') for pt in g.get('parts', [])):
                    findings.append(f'{name}: Gruppe {g["id"]} ohne overview-Text')
            walk(g.get('groups', []))
    walk(p.get('merge', {}).get('custom', {}).get('groups', []))
    if len(gids) != len(set(gids)):
        findings.append(f'{name}: Gruppen-IDs nicht eindeutig')
    for gid, href in links:
        if not href.startswith('#') or href[1:] not in inserted:
            findings.append(f'{name}: Link {href} in {gid} trifft kein eingefügtes Control')
    never = sorted(imported - set(inserted))
    if never:
        findings.append(f'{name}: importiert, aber nirgends eingefügt: {never[:8]}')

    part_ids = set()
    for a in p.get('modify', {}).get('alters', []):
        cid = a.get('control-id')
        if cid not in imported:
            findings.append(f'{name}: alter für nicht importiertes Control {cid}')
        for add in a.get('adds', []):
            for pt in add.get('parts', []):
                if pt.get('id') in part_ids:
                    findings.append(f'{name}: Reifegrad-Part-ID doppelt: {pt.get("id")}')
                part_ids.add(pt.get('id'))
            if add.get('parts') and not add.get('by-id'):
                findings.append(f'{name}: adds mit parts ohne by-id an {cid}')
    n_ng = sum(1 for x in imported if x.startswith('NG-'))
    print(f'  {name}: {len(imported) - n_ng} G++ + {n_ng} NG Controls, {len(gids)} Gruppen, {len(findings)} Befunde')
    return findings, {'imports': p.get('imports'), 'merge': p.get('merge')}


def main(argv):
    args = [a for a in argv[1:] if not a.startswith('--')]
    offline = '--offline' in argv
    local = None
    if '--gpp-catalog' in argv:
        local = argv[argv.index('--gpp-catalog') + 1]
        args = [a for a in args if a != local]
    if len(args) != 1:
        print(__doc__)
        return 2
    folder = pathlib.Path(args[0])
    profiles = sorted(f for f in folder.glob('*.json') if f.name != NG_FILE)
    if not profiles:
        print(f'keine Profile in {folder}')
        return 2
    js = load_validator()
    findings = []
    ng_path = folder / NG_FILE
    ng_ids, ng_sha = set(), None
    if ng_path.exists():
        f, ng_ids = check_ng_catalog(ng_path, js)
        findings += f
        ng_sha = hashlib.sha256(ng_path.read_bytes()).hexdigest()
    gpp_ids = None
    first = json.loads(profiles[0].read_text(encoding='utf-8'))
    res0 = first.get('profile', {}).get('back-matter', {}).get('resources', [{}])
    try:
        gpp_ids, note = fetch_catalog(res0[0], local, offline)
        if note:
            print(f'  Anwenderkatalog: {note}')
    except Exception as e:  # noqa: BLE001 — nur die G++-ID-Prüfung entfällt, mit Grund
        print(f'  Anwenderkatalog nicht ladbar ({e}); G++-IDs werden nicht geprüft')
    shapes = {}
    for path in profiles:
        f, shape = check_profile(path, js, ng_ids, ng_sha, gpp_ids)
        findings += f
        stem = path.name[:-len('_enhanced.json')] if path.name.endswith('_enhanced.json') else path.name[:-len('.json')]
        if shape is not None:
            shapes.setdefault(stem, []).append(shape)
    for stem, pair in shapes.items():
        if len(pair) != 2:
            findings.append(f'{stem}: plain und _enhanced nicht beide vorhanden')
        elif pair[0] != pair[1]:
            findings.append(f'{stem}: plain und _enhanced unterscheiden sich in imports/merge')
    print()
    for f in findings:
        print('BEFUND', f)
    print(f'{len(profiles)} Profile, {len(ng_ids)} NG-Controls, {len(findings)} Befunde')
    return 1 if findings else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
