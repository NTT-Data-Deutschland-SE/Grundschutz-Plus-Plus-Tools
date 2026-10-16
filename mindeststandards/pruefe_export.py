"""Prüft die OSCAL-Exporte des Werkzeugs mindeststandard-oscal.html in einem Ordner.

Je Stamm (mindeststandard-<kurz>-<version>) werden profile.json, ergaenzungskatalog.json
(optional) und catalog.json geprüft: OSCAL-1.2.2-Schema, Import-Verweise, Hash des
Ergänzungskatalogs, Eindeutigkeit der Control-IDs, Fragment-Links.

Aufruf:
  PYTHONUTF8=1 uv run --no-project --with jsonschema --with regex python -I mindeststandards/pruefe_export.py mindeststandards
Ohne jsonschema/regex läuft die Prüfung ohne Schemateil weiter und sagt das.
Exit 0 = alles ok, 1 = Befunde, 2 = Aufruffehler.
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
SCHEMAS = HERE.parent / 'hilfsdateien' / 'OSCAL_Schemas'


def load_validator():
    try:
        import jsonschema  # noqa: F401
        import regex
        import jsonschema._keywords as kw
        kw.re = regex  # OSCAL-Schemas nutzen \p{L}-Klassen
        return jsonschema
    except ImportError as e:  # Schema-Prüfung ist optional, der Rest läuft
        print(f'  Hinweis: Schemaprüfung übersprungen ({e.name} fehlt)')
        return None


def schema_errors(js, kind, doc):
    if js is None:
        return []
    schema = json.loads((SCHEMAS / f'oscal_{kind}_schema.json').read_text(encoding='utf-8'))
    return [f"{'/'.join(map(str, e.path))}: {e.message[:160]}" for e in js.Draft7Validator(schema).iter_errors(doc)]


def walk_controls(groups, acc):
    for g in groups:
        for c in g.get('controls', []):
            acc.append(c)
            walk_controls([{'controls': c.get('controls', [])}], acc)
        walk_controls(g.get('groups', []), acc)
    return acc


def walk_links(node, acc):
    if isinstance(node, dict):
        for lnk in node.get('links', []) or []:
            acc.append(lnk.get('href', ''))
        for v in node.values():
            walk_links(v, acc)
    elif isinstance(node, list):
        for v in node:
            walk_links(v, acc)
    return acc


def check_stem(folder, stem, js):
    findings = []
    prof_p, erg_p, cat_p = (folder / f'{stem}.{k}.json' for k in ('profile', 'ergaenzungskatalog', 'catalog'))
    if not prof_p.exists() or not cat_p.exists():
        return [f'{stem}: profile.json oder catalog.json fehlt']
    prof = json.loads(prof_p.read_text(encoding='utf-8'))
    cat = json.loads(cat_p.read_text(encoding='utf-8'))
    erg = json.loads(erg_p.read_text(encoding='utf-8')) if erg_p.exists() else None

    for kind, doc in (('profile', prof), ('catalog', cat)) + ((('catalog', erg),) if erg else ()):
        for e in schema_errors(js, kind, doc)[:10]:
            findings.append(f'{stem}: Schema {kind}: {e}')

    p = prof['profile']
    resources = {r['uuid']: r for r in p.get('back-matter', {}).get('resources', [])}
    for imp in p.get('imports', []):
        href = imp.get('href', '')
        if not href.startswith('#') or href[1:] not in resources:
            findings.append(f'{stem}: Import {href} zeigt auf keine Back-Matter-Resource')
    erg_res = [r for r in resources.values() if any(rl.get('href', '').endswith('.ergaenzungskatalog.json') for rl in r.get('rlinks', []))]
    if erg_p.exists():
        if not erg_res:
            findings.append(f'{stem}: Ergänzungskatalog liegt vor, aber das Profil referenziert ihn nicht')
        else:
            want = erg_res[0]['rlinks'][0].get('hashes', [{}])[0].get('value', '')
            have = hashlib.sha256(erg_p.read_bytes()).hexdigest()
            if want != have:
                findings.append(f'{stem}: Hash des Ergänzungskatalogs weicht ab (Profil {want[:12]}…, Datei {have[:12]}…)')
    elif erg_res:
        findings.append(f'{stem}: Profil referenziert einen Ergänzungskatalog, die Datei fehlt')

    controls = walk_controls(cat['catalog'].get('groups', []), [])
    ids = [c['id'] for c in controls]
    dups = sorted({i for i in ids if ids.count(i) > 1})
    if dups:
        findings.append(f'{stem}: Controls mehrfach im Katalog: {", ".join(dups[:8])}')
    idset = set(ids)
    for href in walk_links(cat['catalog'], []):
        if href.startswith('#') and href[1:] not in idset:
            findings.append(f'{stem}: Link {href} zeigt auf kein Control des Katalogs')
    imported = {i for imp in p.get('imports', []) for ic in imp.get('include-controls', []) for i in ic.get('with-ids', [])}
    missing = sorted(imported - idset)
    if missing:
        findings.append(f'{stem}: im Profil importiert, im Katalog nicht vorhanden: {", ".join(missing[:8])}')
    print(f'  {stem}: {len(ids)} Controls, {len(p.get("imports", []))} Imports, Ergänzungskatalog {"ja" if erg else "nein"}, {len(findings)} Befunde')
    return findings


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    folder = pathlib.Path(argv[1])
    stems = sorted({f.name[:-len('.profile.json')] for f in folder.glob('*.profile.json')})
    if not stems:
        print(f'keine *.profile.json in {folder}')
        return 2
    js = load_validator()
    print(f'{len(stems)} Mindeststandard(e) in {folder}:')
    findings = []
    for stem in stems:
        findings += check_stem(folder, stem, js)
    for f in findings:
        print(' -', f)
    print('OK' if not findings else f'{len(findings)} Befunde')
    return 0 if not findings else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv))
