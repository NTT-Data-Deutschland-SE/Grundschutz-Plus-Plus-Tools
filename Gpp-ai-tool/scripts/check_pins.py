#!/usr/bin/env python3
"""check_pins.py -- v1.0.0

Prueft die Quellen-Pins der Werkzeugsammlung gegen Upstream
(Handbuch Kapitel 3.13/3.14, Repin-Verfahren):

1. Inventar: alle gepinnten raw.githubusercontent.com-URLs mit 40er-SHA
   und alle nackten SHA-Konstanten (GPP_CATALOG_PIN_COMMIT, STDT_PIN, ...)
   im Repo, je Datei gezaehlt. Meldet uneinheitliche Pins je Quelle.
2. Upstream: je gepinntem (Repo, Pfad) der juengste Commit auf main, der
   den Pfad beruehrt (`commits?path=...&per_page=1`, Konvention aus
   config.html). Pin == juengster Commit -> aktuell.
3. Inhalt: weicht der Commit ab, werden gepinnter und aktueller Stand
   geladen und verglichen -- erst byteweise, dann als OSCAL-Struktur
   (Controls: id, title, params, parts, props). Rotierende
   alt-identifier, UUIDs und last-modified zaehlen NICHT als Aenderung;
   nur Wortlaut-/Struktur-Abweichungen ergeben "DRIFT".
4. Selbst-Pins (eigenes Repo) laufen lokal ueber `git diff --quiet
   <pin> HEAD -- <pfad>` statt ueber die API (HEAD, damit der Lauf auch
   vor dem Push stimmt: Pin muss den aktuellen Inhalt zeigen).
5. SHA-256-Pin-Konstanten (*PIN*SHA256*, z. B. GPP_CATALOG_PIN_SHA256) werden gegen den Hash des
   gepinnten Inhalts geprueft.

Aufruf (Repo-Wurzel oder beliebig, --root zeigt aufs Repo):
  python3 check_pins.py [--root PFAD] [--json] [--no-fetch] [--cache DIR]

Exit-Code: 0 = alle Pins aktuell oder nur kosmetische Abweichung,
           1 = DRIFT (inhaltliche Aenderung upstream) oder Hash-Fehler,
           2 = Inventar inkonsistent (uneinheitliche Pins je Quelle).

Nur stdlib. Ein GitHub-Token wird aus GH_TOKEN/GITHUB_TOKEN oder
`gh auth token` genommen, sonst laeuft die Abfrage unauthentifiziert
(60 Requests/h reichen fuer die ~15 Quellen).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

VERSION = "1.0.0"
UA = f"check-pins/{VERSION}"

SELF_REPO = "NTT-Data-Deutschland-SE/Grundschutz-Plus-Plus-Tools"

# Verzeichnisse/Dateien, die keine Live-Pins tragen:
# hilfsdateien/ = Provenienz der Generierung (bewusst alte SHAs),
# .claude/ = Worktrees paralleler Sessions, ZIP = Auslieferungsarchiv
# (wird aus dem Ordner gebaut, traegt dieselben Pins).
SKIP_DIRS = {".git", ".claude", "hilfsdateien", "node_modules", "__pycache__"}
SKIP_SUFFIXES = {".zip", ".png", ".jpg", ".pdf", ".pyc", ".docx", ".xlsx"}
SKIP_NAMES = {"RELEASE_NOTES_v3.0.md", "RELEASE_NOTES_v4.0.md"}

RAW_URL = re.compile(
    r"https://raw\.githubusercontent\.com/"
    r"(?P<repo>[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)/"
    r"(?P<sha>[0-9a-f]{40})/"
    r"(?P<path>[^\"'\s)<>\\]+)"
)
BARE_CONST = re.compile(
    r"(?P<name>[A-Z][A-Z0-9_]*(?:PIN|COMMIT)[A-Z0-9_]*)\s*[:=]\s*[\"']?(?P<sha>[0-9a-f]{40})\b"
)
SHA256_CONST = re.compile(
    r"(?P<name>[A-Z][A-Z0-9_]*PIN[A-Z0-9_]*SHA256[A-Z0-9_]*)\s*[:=]\s*[\"']?(?P<hash>[0-9a-f]{64})\b"
)

# Props/Felder, deren Aenderung kosmetisch ist (Rotation je Publikation).
COSMETIC_PROP_NAMES = {"alt-identifier"}
COSMETIC_KEYS = {"uuid", "last-modified", "published", "version"}


# --------------------------------------------------------------------------
# Inventar
# --------------------------------------------------------------------------

@dataclass
class Source:
    repo: str
    path: str                       # URL-dekodiert
    pins: dict[str, set[str]] = field(default_factory=lambda: defaultdict(set))  # sha -> files
    count: int = 0

    @property
    def key(self) -> tuple[str, str]:
        return (self.repo, self.path)

    @property
    def consistent(self) -> bool:
        return len(self.pins) == 1

    @property
    def sha(self) -> str:
        return max(self.pins, key=lambda s: len(self.pins[s]))


@dataclass
class BareConst:
    name: str
    sha: str
    file: str


@dataclass
class HashConst:
    name: str
    hash: str
    file: str


def iter_files(root: Path):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            p = Path(dirpath) / fn
            if p.suffix.lower() in SKIP_SUFFIXES or fn in SKIP_NAMES:
                continue
            if p.name == Path(__file__).name:
                continue
            yield p


def scan(root: Path) -> tuple[dict, list[BareConst], list[HashConst]]:
    sources: dict[tuple[str, str], Source] = {}
    bare: list[BareConst] = []
    hashes: list[HashConst] = []
    for p in iter_files(root):
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        rel = p.relative_to(root).as_posix()
        for m in RAW_URL.finditer(text):
            path = urllib.parse.unquote(m["path"])
            src = sources.setdefault((m["repo"], path), Source(m["repo"], path))
            src.pins[m["sha"]].add(rel)
            src.count += 1
        for m in BARE_CONST.finditer(text):
            bare.append(BareConst(m["name"], m["sha"], rel))
        for m in SHA256_CONST.finditer(text):
            hashes.append(HashConst(m["name"], m["hash"], rel))
    return sources, bare, hashes


# --------------------------------------------------------------------------
# Netz
# --------------------------------------------------------------------------

def github_token() -> str | None:
    tok = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if tok:
        return tok
    try:
        out = subprocess.run(["gh", "auth", "token"], capture_output=True,
                             text=True, timeout=10)
        if out.returncode == 0 and out.stdout.strip():
            return out.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        pass
    return None


class Fetcher:
    def __init__(self, cache: Path | None, token: str | None):
        self.cache = cache
        self.token = token
        if cache:
            cache.mkdir(parents=True, exist_ok=True)

    def _get(self, url: str, api: bool = False) -> bytes:
        headers = {"User-Agent": UA}
        if api:
            headers["Accept"] = "application/vnd.github+json"
            if self.token:
                headers["Authorization"] = f"Bearer {self.token}"
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=120) as r:
            return r.read()

    def api(self, endpoint: str):
        return json.loads(self._get("https://api.github.com/" + endpoint, api=True))

    def raw(self, repo: str, sha: str, path: str) -> bytes:
        if self.cache:
            cp = self.cache / f"{sha}__{hashlib.sha1(path.encode()).hexdigest()[:10]}.bin"
            if cp.exists():
                return cp.read_bytes()
        url = f"https://raw.githubusercontent.com/{repo}/{sha}/{urllib.parse.quote(path, safe='/')}"
        data = self._get(url)
        if self.cache:
            cp.write_bytes(data)
        return data

    def latest_commit(self, repo: str, path: str) -> tuple[str, str, str] | None:
        q = urllib.parse.urlencode({"path": path, "per_page": 1})
        items = self.api(f"repos/{repo}/commits?{q}")
        if not items:
            return None
        c = items[0]
        return c["sha"], c["commit"]["committer"]["date"], c["commit"]["message"].split("\n")[0]


# --------------------------------------------------------------------------
# OSCAL-Strukturvergleich
# --------------------------------------------------------------------------

def _strip(obj):
    """Entfernt kosmetische Felder rekursiv (UUIDs, Zeitstempel, alt-identifier)."""
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            if k in COSMETIC_KEYS:
                continue
            if k == "props" and isinstance(v, list):
                v = [p for p in v if p.get("name") not in COSMETIC_PROP_NAMES]
                if not v:
                    continue
            out[k] = _strip(v)
        return out
    if isinstance(obj, list):
        return [_strip(x) for x in obj]
    return obj


def _controls(node, acc: dict):
    for c in node.get("controls", []) or []:
        acc[c["id"]] = c
        _controls(c, acc)
    for g in node.get("groups", []) or []:
        _controls(g, acc)


def oscal_controls(doc) -> dict | None:
    """Liefert id -> control fuer catalog/profile-resolved; None wenn kein Katalog."""
    if not isinstance(doc, dict):
        return None
    cat = doc.get("catalog")
    if not isinstance(cat, dict):
        return None
    acc: dict = {}
    _controls(cat, acc)
    return acc


def _control_fingerprint(c: dict) -> str:
    return json.dumps(_strip(c), sort_keys=True, ensure_ascii=False)


def _diff_fields(a: dict, b: dict) -> list[str]:
    fields = []
    for k in ("title", "params", "parts", "props", "links", "class"):
        if json.dumps(_strip(a.get(k)), sort_keys=True) != json.dumps(_strip(b.get(k)), sort_keys=True):
            fields.append(k)
    return fields


@dataclass
class ContentDiff:
    bytes_equal: bool
    is_catalog: bool
    added: list[str] = field(default_factory=list)
    removed: list[str] = field(default_factory=list)
    changed: dict[str, list[str]] = field(default_factory=dict)   # id -> geaenderte Felder
    n_old: int = 0
    n_new: int = 0
    cosmetic_only: bool = False
    note: str = ""

    @property
    def substantive(self) -> bool:
        if self.bytes_equal:
            return False
        if self.is_catalog:
            return bool(self.added or self.removed or self.changed)
        return not self.cosmetic_only


def compare_content(old: bytes, new: bytes) -> ContentDiff:
    if old == new:
        return ContentDiff(True, False)
    try:
        jo, jn = json.loads(old), json.loads(new)
    except json.JSONDecodeError:
        return ContentDiff(False, False, note="kein JSON, nur Byte-Vergleich")
    co, cn = oscal_controls(jo), oscal_controls(jn)
    if co is None or cn is None:
        same = json.dumps(_strip(jo), sort_keys=True) == json.dumps(_strip(jn), sort_keys=True)
        return ContentDiff(False, False, cosmetic_only=same,
                           note="kein OSCAL-Katalog; Vergleich ohne UUID/Zeitstempel")
    d = ContentDiff(False, True, n_old=len(co), n_new=len(cn))
    d.added = sorted(set(cn) - set(co))
    d.removed = sorted(set(co) - set(cn))
    for cid in sorted(set(co) & set(cn)):
        if _control_fingerprint(co[cid]) != _control_fingerprint(cn[cid]):
            d.changed[cid] = _diff_fields(co[cid], cn[cid])
    d.cosmetic_only = not (d.added or d.removed or d.changed)
    return d


# --------------------------------------------------------------------------
# Selbst-Pins lokal
# --------------------------------------------------------------------------

def git_path_changed(root: Path, pin: str, path: str, ref: str = "HEAD") -> bool | None:
    try:
        r = subprocess.run(["git", "-C", str(root), "diff", "--quiet", pin, ref, "--", path],
                           capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.SubprocessError):
        return None
    if r.returncode in (0, 1):
        return r.returncode == 1
    return None


# --------------------------------------------------------------------------
# Hauptlauf
# --------------------------------------------------------------------------

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[1])
    ap.add_argument("--root", type=Path, default=None,
                    help="Repo-Wurzel (Default: zwei Ebenen ueber diesem Skript)")
    ap.add_argument("--json", action="store_true", help="Ergebnis als JSON")
    ap.add_argument("--no-fetch", action="store_true",
                    help="nur Inventar + Selbst-Pins, keine Upstream-Abfrage")
    ap.add_argument("--cache", type=Path, default=None,
                    help="Download-Cache (Default: <TEMP>/check_pins)")
    ap.add_argument("--max-list", type=int, default=15,
                    help="max. gelistete Control-IDs je Kategorie")
    args = ap.parse_args(argv)

    root = args.root or Path(__file__).resolve().parents[2]
    cache = args.cache or Path(os.environ.get("TEMP") or "/tmp") / "check_pins"
    sources, bare, hashes = scan(root)

    report = {"version": VERSION, "root": str(root), "sources": [], "bare": [],
              "sha256": [], "exit": 0}
    exit_code = 0

    # 1. Inventar-Konsistenz: nackte Konstanten muessen zu einer URL-Quelle passen.
    url_shas = {sha for s in sources.values() for sha in s.pins}
    sha_to_repos = defaultdict(set)
    for s in sources.values():
        for sha in s.pins:
            sha_to_repos[sha].add(s.repo)
    for b in bare:
        repos = sorted(sha_to_repos.get(b.sha, []))
        report["bare"].append({"name": b.name, "sha": b.sha, "file": b.file,
                               "repo": repos[0] if repos else None})
    orphan_bare = [b for b in bare if b.sha not in url_shas]

    for s in sources.values():
        if not s.consistent:
            exit_code = max(exit_code, 2)

    # 2./3. Upstream und Inhalt
    fetcher = None if args.no_fetch else Fetcher(cache, github_token())
    sha256_by_content: dict[str, str] = {}

    for s in sorted(sources.values(), key=lambda x: (x.repo, x.path)):
        entry = {"repo": s.repo, "path": s.path, "pin": s.sha, "count": s.count,
                 "files": sorted({f for fs in s.pins.values() for f in fs}),
                 "consistent": s.consistent,
                 "pins": {sha: sorted(fs) for sha, fs in s.pins.items()},
                 "status": "?", "upstream": None, "diff": None}
        if s.repo == SELF_REPO:
            changed = git_path_changed(root, s.sha, s.path)
            entry["status"] = ("AKTUELL" if changed is False else
                               "DRIFT" if changed else "UNBEKANNT (git)")
            entry["upstream"] = "HEAD (lokal)"
            if changed:
                exit_code = max(exit_code, 1)
        elif fetcher is None:
            entry["status"] = "UEBERSPRUNGEN (--no-fetch)"
        else:
            try:
                latest = fetcher.latest_commit(s.repo, s.path)
            except urllib.error.HTTPError as e:
                entry["status"] = f"FEHLER API {e.code}"
                latest = None
            if latest:
                lsha, ldate, lmsg = latest
                entry["upstream"] = {"sha": lsha, "date": ldate, "message": lmsg}
                if lsha == s.sha:
                    entry["status"] = "AKTUELL"
                else:
                    try:
                        old = fetcher.raw(s.repo, s.sha, s.path)
                        new = fetcher.raw(s.repo, lsha, s.path)
                    except urllib.error.HTTPError as e:
                        entry["status"] = f"FEHLER RAW {e.code}"
                        old = new = None
                    if old is not None:
                        sha256_by_content[s.sha + s.path] = hashlib.sha256(old).hexdigest()
                        d = compare_content(old, new)
                        entry["diff"] = {
                            "bytes_equal": d.bytes_equal, "is_catalog": d.is_catalog,
                            "n_old": d.n_old, "n_new": d.n_new,
                            "added": d.added, "removed": d.removed,
                            "changed": d.changed, "cosmetic_only": d.cosmetic_only,
                            "note": d.note,
                        }
                        if d.bytes_equal:
                            entry["status"] = "AKTUELL (Commit neuer, Bytes identisch)"
                        elif d.substantive:
                            entry["status"] = "DRIFT"
                            exit_code = max(exit_code, 1)
                        else:
                            entry["status"] = "KOSMETISCH (nur UUID/alt-identifier/Zeitstempel)"
            elif entry["status"] == "?":
                entry["status"] = "FEHLER: Pfad upstream unbekannt"
        if entry["status"] == "AKTUELL" and fetcher and s.repo != SELF_REPO and hashes:
            # Hash fuer SHA-256-Pruefung auch bei aktuellem Pin einmal laden.
            try:
                sha256_by_content[s.sha + s.path] = hashlib.sha256(
                    fetcher.raw(s.repo, s.sha, s.path)).hexdigest()
            except urllib.error.HTTPError:
                pass
        report["sources"].append(entry)

    # 5. SHA-256-Konstanten gegen gepinnte Inhalte
    known_hashes = set(sha256_by_content.values())
    for h in hashes:
        ok = None if fetcher is None else (h.hash in known_hashes)
        report["sha256"].append({"name": h.name, "hash": h.hash, "file": h.file, "ok": ok})
        if ok is False:
            exit_code = max(exit_code, 1)

    report["orphan_bare"] = [{"name": b.name, "sha": b.sha, "file": b.file} for b in orphan_bare]
    report["exit"] = exit_code

    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return exit_code

    print(f"check_pins v{VERSION}  --  Repo: {root}")
    print(f"Quellen: {len(sources)}  |  nackte Pin-Konstanten: {len(bare)}  |  "
          f"SHA-256-Konstanten: {len(hashes)}\n")
    for e in report["sources"]:
        print(f"[{e['status']}] {e['repo']}")
        print(f"    Pfad : {e['path']}")
        print(f"    Pin  : {e['pin']}  ({e['count']}x in {len(e['files'])} Dateien)")
        if not e["consistent"]:
            print("    !!! UNEINHEITLICH:")
            for sha, fs in e["pins"].items():
                print(f"        {sha}: {', '.join(fs)}")
        up = e["upstream"]
        if isinstance(up, dict):
            print(f"    Neu  : {up['sha']}  {up['date']}  {up['message']}")
        d = e["diff"]
        if d and not d["bytes_equal"]:
            if d["is_catalog"]:
                print(f"    Controls: {d['n_old']} -> {d['n_new']}  "
                      f"(+{len(d['added'])} / -{len(d['removed'])} / ~{len(d['changed'])})")
                for label, ids in (("neu", d["added"]), ("entfernt", d["removed"])):
                    if ids:
                        more = f" ... (+{len(ids) - args.max_list})" if len(ids) > args.max_list else ""
                        print(f"      {label:9}: {', '.join(ids[:args.max_list])}{more}")
                if d["changed"]:
                    items = list(d["changed"].items())
                    for cid, flds in items[:args.max_list]:
                        print(f"      geaendert: {cid}  [{', '.join(flds)}]")
                    if len(items) > args.max_list:
                        print(f"      ... (+{len(items) - args.max_list} weitere)")
            elif d["note"]:
                print(f"    Hinweis: {d['note']}")
        print()

    if report["orphan_bare"]:
        print("Nackte Pin-Konstanten ohne passende URL-Quelle (pruefen!):")
        for b in report["orphan_bare"]:
            print(f"    {b['file']}: {b['name']} = {b['sha']}")
        print()
    if hashes and fetcher:
        bad = [h for h in report["sha256"] if h["ok"] is False]
        print(f"SHA-256-Konstanten: {len(hashes) - len(bad)}/{len(hashes)} passen zu einem gepinnten Inhalt")
        for h in bad:
            print(f"    FALSCH: {h['file']}: {h['name']} = {h['hash']}")
        print()

    verdict = {0: "OK - alle Pins aktuell (oder nur kosmetische Abweichung)",
               1: "DRIFT - Repin pruefen (Repin-Verfahren, Handbuch 3.14)",
               2: "INKONSISTENT - uneinheitliche Pins je Quelle"}[exit_code]
    print(f"Ergebnis: {verdict}")
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
