/* ==GPP-CORE-START== v1  ————————————————————————————————————————————————
   Gemeinsamer Kern aller GS++-oscal-app: Konfiguration, Prompt-Registrierung,
   Quellen-Pins und der Artefaktspeicher.

   WICHTIG — alle Apps binden diese Datei per <script src="gpp-core.js"> ein;
   sie muss neben den HTML-Dateien liegen (Weitergabe nur als kompletter
   Ordner bzw. GS++-oscal-app.zip). Fehlt sie, zeigt jede App beim Start eine
   deutliche Fehlermeldung statt still zu scheitern. Einzeldatei-Portabilität
   ist ab Version 3 bewusst aufgegeben.

   Ablage:
     localStorage  gpp:cfg:*   Konfiguration (klein, synchron beim Start lesbar)
     IndexedDB     gpp-artefacts/artefacts   Artefakte (OSCAL-Dokumente, oft > 500 kB;
                   localStorage wäre nach wenigen SSPs voll)
   ———————————————————————————————————————————————————————————————————— */
const GPP_CORE_VERSION = "1";
const GPP_CFG_PREFIX = "gpp:cfg:";

/* ---------- Konfiguration ---------- */
const GPP_CFG_DEFAULTS = {
  "ai:backend": "gemini",
  "ai:model:gemini": "gemini-3.6-flash",
  "ai:model:openrouter": "",
  // Dritter Weg: ein selbst betriebener OpenAI-kompatibler Endpoint
  // (vLLM, LM Studio, Ollama, LiteLLM, Azure-Proxy …).
  "ai:model:openai": "",
  "ai:base:openai": "",
  "ai:thinking": "medium",
  "ai:effort": "medium",
  "ai:grounding": "0",
  "ai:checker:backend": "same",
  "ai:checker:model": "",
  "ai:or:structuredonly": "1",
  // Beschreibt die Institution (KRITIS, NIS2, Branche …) und geht als
  // Hintergrund in die KI-Aufrufe aller Werkzeuge ein.
  "ai:context": "",
  // Optionaler GitHub-Token nur fürs Auflisten von Verzeichnissen (read-only
  // genügt). Ohne ihn gelten 60 Anfragen/Stunde; die Browser-Anmeldung an
  // github.com zählt dabei nicht, api.github.com wertet keine Cookies aus.
  "gh:token": "",
  "run:concurrency": "4",
  // Zwei Chunk-Begriffe, bewusst getrennt: der Validator zerlegt nach ANZAHL
  // (Befunde je Aufruf), die Generatoren nach ZEICHEN (Dokumenttext je Aufruf).
  // Ein gemeinsamer Schlüssel hätte in der jeweils anderen Einheit unsinnige
  // Werte erzeugt — 6 Zeichen bzw. 28000 Befunde.
  "run:chunk": "6",
  "run:chunkchars": "28000",
  "run:retries": "2",
};

const gppCfg = {
  get(key, fallback) {
    const v = localStorage.getItem(GPP_CFG_PREFIX + key);
    if (v !== null) return v;
    return fallback !== undefined ? fallback : (GPP_CFG_DEFAULTS[key] ?? "");
  },
  getNum(key, fallback) {
    const n = parseInt(this.get(key), 10);
    return Number.isFinite(n) ? n : fallback;
  },
  getBool(key) { return this.get(key) === "1"; },
  set(key, value) { localStorage.setItem(GPP_CFG_PREFIX + key, String(value)); },
  remove(key) { localStorage.removeItem(GPP_CFG_PREFIX + key); },
  /* Backend + Key + Modell in einem Rutsch — was jeder AI-Aufruf braucht.
     Beim eigenen OpenAI-kompatiblen Endpoint kommt die Basis-URL dazu. */
  target(backend) {
    const be = backend || this.get("ai:backend");
    const t = { backend: be, key: this.get("ai:key:" + be), model: this.get("ai:model:" + be) };
    if (be === "openai") t.baseUrl = (this.get("ai:base:openai") || "").replace(/\/+$/, "");
    return t;
  },
  /* true, wenn das Backend die OpenAI-Chat-Completions-Form spricht */
  isOpenAiStyle(backend) {
    const be = backend || this.get("ai:backend");
    return be === "openrouter" || be === "openai";
  },
  /* Endpunkt für Chat-Completions je Backend */
  chatUrl(backend) {
    const be = backend || this.get("ai:backend");
    if (be === "openrouter") return "https://openrouter.ai/api/v1/chat/completions";
    if (be === "openai") {
      const base = (this.get("ai:base:openai") || "").replace(/\/+$/, "");
      return base ? base + "/chat/completions" : "";
    }
    return "";
  },
  /* true, wenn für das aktive Backend ein Key hinterlegt ist */
  ready(backend) { return !!this.target(backend).key; },
  all() {
    const out = {};
    for (const k of Object.keys(localStorage)) {
      if (k.startsWith(GPP_CFG_PREFIX)) out[k.slice(GPP_CFG_PREFIX.length)] = localStorage.getItem(k);
    }
    return out;
  },
};

/* ---------- Prompts: Selbstregistrierung ----------
   Die Default-Texte bleiben als Konstanten im jeweiligen Tool — nur so läuft
   es allein lauffähig. Beim Start meldet das Tool sie an; config.html
   bearbeitet ausschließlich, was angemeldet ist, und kennt die Defaults
   dadurch immer im aktuellen Stand statt sie zu duplizieren. */
function gppRegisterPrompts(toolId, prompts) {
  const reg = {
    tool: toolId,
    prompts: prompts.map(p => ({
      id: p.id,
      label: p.label,
      placeholders: p.placeholders || [],
      default: p.default,
    })),
  };
  gppWriteIfChanged("promptdefaults:" + toolId, reg);
}
/* Nur bei tatsächlicher Änderung schreiben — jeder localStorage-Write feuert
   storage-Events in allen offenen Tabs und ließe sie grundlos neu rendern. */
function gppWriteIfChanged(subKey, obj) {
  const key = GPP_CFG_PREFIX + subKey;
  const json = JSON.stringify(obj);
  if (localStorage.getItem(key) !== json) localStorage.setItem(key, json);
}
/* aktiver Prompttext: Nutzerfassung, sonst der registrierte Default */
function gppPrompt(toolId, promptId, fallbackDefault) {
  const stored = localStorage.getItem(GPP_CFG_PREFIX + "prompt:" + toolId + ":" + promptId);
  if (stored !== null && stored.trim()) return stored;
  return fallbackDefault;
}

/* ---------- Quellen-Pins ----------
   Gepinnt ist der Normalfall (Handbuch 3.13/3.14, Grundregel 8). config.html
   kann pro Quelle den aktuellen Upstream-Stand auflösen und den Pin bewusst
   umsetzen — Aktualität ist ein sichtbarer Klick, kein stilles Nachziehen. */
function gppSource(sourceId, pinnedDefaultUrl) {
  const override = localStorage.getItem(GPP_CFG_PREFIX + "src:" + sourceId);
  return override || pinnedDefaultUrl;
}
/* meldet eine Quelle für die Übersicht in config.html an */
function gppRegisterSources(toolId, sources) {
  gppWriteIfChanged("srcdefaults:" + toolId, {
    tool: toolId,
    /* fixed: Quelle ist zusätzlich inhaltsgepinnt (SHA-256 im Tool) —
       config.html zeigt sie an, bietet aber kein Umpinnen an. */
    sources: sources.map(s => ({ id: s.id, label: s.label, repo: s.repo, path: s.path, default: s.default, fixed: !!s.fixed })),
  });
}
function gppIsUnpinned(url) { return /\/(refs\/heads\/[^/]+|main|master)\//.test(String(url || "")); }

/* raw.githubusercontent.com/<owner>/<repo>/<ref>/<pfad> zerlegen.
   <ref> ist entweder ein Commit/Tag-Segment ODER die dreiteilige Form
   refs/heads/<branch> — wer das übersieht und stumpf ersetzt, baut aus
   .../refs/heads/main/a.json ein kaputtes .../<sha>/heads/main/a.json. */
function gppParseRawUrl(url) {
  const m = String(url || "").match(
    /^https:\/\/raw\.githubusercontent\.com\/([^/]+)\/([^/]+)\/(refs\/(?:heads|tags)\/[^/]+|[^/]+)\/(.+)$/
  );
  return m ? { owner: m[1], repo: m[2], ref: m[3], path: m[4] } : null;
}
/* Commit-SHA der URL, oder null wenn sie auf einen beweglichen Ref zeigt */
function gppCommitOf(url) {
  const p = gppParseRawUrl(url);
  if (!p || /^refs\//.test(p.ref)) return null;
  return /^(main|master)$/.test(p.ref) ? null : p.ref;
}
/* URL auf einen Commit umschreiben — baut den Pfad neu auf statt zu ersetzen */
function gppRepinUrl(url, sha) {
  const p = gppParseRawUrl(url);
  if (!p || !sha) return url;
  return `https://raw.githubusercontent.com/${p.owner}/${p.repo}/${sha}/${p.path}`;
}

/* ---------- Verzeichnisse aus GitHub auflisten ----------
   Die contents-API braucht eine Anfrage JE Verzeichnis. Mehrere Werkzeuge
   listeten damit beim Start vier bis fünf Verzeichnisse — bei 60 Anfragen pro
   Stunde ohne Anmeldung war das Limit nach wenigen Seitenaufrufen erschöpft
   (HTTP 403). Ein trees-Aufruf mit ?recursive=1 liefert stattdessen den ganzen
   Baum eines Repos auf einmal; er wird 24 h gehalten und bei erschöpftem Limit
   auch abgelaufen weiterverwendet. Gelistet wird gegen einen festen Commit,
   die erzeugten Roh-URLs sind damit gepinnt (Grundregel 8). */
const GPP_TREE_TTL = 24 * 60 * 60 * 1000;

async function gppRepoTree(owner, repo, ref) {
  const key = GPP_CFG_PREFIX + `tree:${owner}/${repo}@${ref}`;
  let cached = null;
  try { cached = JSON.parse(localStorage.getItem(key) || "null"); } catch (e) { /* kaputt */ }
  if (cached && Array.isArray(cached.paths) && Date.now() - cached.ts < GPP_TREE_TTL) {
    return { paths: cached.paths, from: "Cache" };
  }
  try {
    /* Die Anmeldung im Browser hilft hier NICHT: api.github.com wertet keine
       Session-Cookies aus. Nur ein Token im Authorization-Header hebt das
       Limit (60 → 5000 Anfragen/Stunde); optional in config.html hinterlegbar. */
    const token = gppCfg.get("gh:token");
    const r = await fetch(`https://api.github.com/repos/${owner}/${repo}/git/trees/${ref}?recursive=1`,
      token ? { headers: { Authorization: "Bearer " + token } } : undefined);
    if (!r.ok) {
      throw new Error(r.status === 403
        ? (token ? "GitHub lehnt den hinterlegten Token ab oder das Limit ist erschöpft"
                 : "GitHub-Limit erreicht (60 Anfragen/Stunde ohne Anmeldung) — in config.html lässt sich ein Token hinterlegen")
        : `HTTP ${r.status}`);
    }
    const json = await r.json();
    const paths = (json.tree || []).filter(e => e.type === "blob").map(e => e.path);
    try { localStorage.setItem(key, JSON.stringify({ ts: Date.now(), paths })); } catch (e) { /* Quota */ }
    return { paths, from: "GitHub" };
  } catch (e) {
    if (cached && Array.isArray(cached.paths)) {
      return { paths: cached.paths, from: `abgelaufener Cache — ${e.message}`, stale: true };
    }
    throw e;
  }
}

/* Listet Dateien eines Verzeichnisses. `dir` ohne führenden Schrägstrich,
   `ext` optional (z. B. ".json"). Liefert [{name, path, url}] mit gepinnter URL. */
async function gppRepoList({ owner, repo, ref, dir, ext = "", recursive = false }) {
  const { paths, from, stale } = await gppRepoTree(owner, repo, ref);
  const prefix = dir.replace(/^\/+|\/+$/g, "") + "/";
  const files = paths.filter(p => {
    if (!p.startsWith(prefix)) return false;
    if (ext && !p.endsWith(ext)) return false;
    return recursive || !p.slice(prefix.length).includes("/");
  }).map(p => ({
    name: p.slice(p.lastIndexOf("/") + 1),
    path: p,
    url: `https://raw.githubusercontent.com/${owner}/${repo}/${ref}/${p}`,
  }));
  return { files, from, stale };
}

/* ---------- Artefaktspeicher (IndexedDB) ---------- */
const GPP_DB_NAME = "gpp-artefacts";
const GPP_DB_STORE = "artefacts";
const GPP_DB_VERSION = 1;
/* Reihenfolge = Workflow-Stufen aus index.html */
const GPP_STAGES = ["explore", "author", "model", "implement", "assess", "remediate", "validate"];
const GPP_KINDS = ["catalog", "profile", "ssp", "ap", "ar", "poam", "analysis", "workspace", "report"];

function gppDb() {
  return new Promise((resolve, reject) => {
    const req = indexedDB.open(GPP_DB_NAME, GPP_DB_VERSION);
    req.onupgradeneeded = () => {
      const db = req.result;
      if (!db.objectStoreNames.contains(GPP_DB_STORE)) {
        const os = db.createObjectStore(GPP_DB_STORE, { keyPath: "id" });
        os.createIndex("stage", "stage", { unique: false });
        os.createIndex("kind", "kind", { unique: false });
        os.createIndex("updatedAt", "updatedAt", { unique: false });
      }
    };
    req.onsuccess = () => resolve(req.result);
    req.onerror = () => reject(req.error);
  });
}
/* Eine Operation je Transaktion. Bewusst ohne await INNERHALB der Transaktion:
   eine IDB-Transaktion schließt sich selbst, sobald der Microtask-Queue leer
   läuft — ein dazwischengeschobenes await lässt sie stillschweigend abbrechen. */
async function gppTx(mode, fn) {
  const db = await gppDb();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(GPP_DB_STORE, mode);
    const store = tx.objectStore(GPP_DB_STORE);
    let result;
    let req;
    try { req = fn(store); } catch (e) { db.close(); reject(e); return; }
    if (req && typeof req === "object" && "onsuccess" in req) {
      req.onsuccess = () => { result = req.result; };
    }
    tx.oncomplete = () => { db.close(); resolve(result); };
    tx.onerror = () => { db.close(); reject(tx.error); };
    tx.onabort = () => { db.close(); reject(tx.error); };
  });
}
async function gppSha256(text) {
  const buf = new TextEncoder().encode(text);
  const d = await crypto.subtle.digest("SHA-256", buf);
  return Array.from(new Uint8Array(d)).map(b => b.toString(16).padStart(2, "0")).join("");
}

/* Ein "Set" ist ein zusammengehöriger Arbeitsstand (Profil + SSP + AP/AR + POA&M …).
   Alle Tools arbeiten immer auf dem AKTIVEN Set; index.html verwaltet die Sets
   (anlegen, wechseln, hoch-/herunterladen). Alt-Datensätze ohne set-Feld
   gehören zum Set "standard". */
const GPP_DEFAULT_SET = "standard";
function gppSetOf(rec) { return (rec && rec.set) || GPP_DEFAULT_SET; }

/* Von diesen Sorten trägt ein Set genau EIN Exemplar: ein Arbeitsstand hat
   einen SSP, eine Prüfung und eine Maßnahmenliste. Wird ein neues abgelegt,
   ersetzt es das vorherige — sonst wüsste kein Werkzeug, welches gilt.
   Kataloge, Profile und Berichte dürfen dagegen mehrfach vorkommen. */
const GPP_SINGLETON_KINDS = new Set(["ssp", "ap", "ar", "poam"]);

const gppArtefacts = {
  activeSet() {
    return (localStorage.getItem(GPP_CFG_PREFIX + "artefacts:set") || GPP_DEFAULT_SET).trim() || GPP_DEFAULT_SET;
  },
  setActiveSet(name) {
    const n = String(name || GPP_DEFAULT_SET).trim() || GPP_DEFAULT_SET;
    localStorage.setItem(GPP_CFG_PREFIX + "artefacts:set", n);
    window.dispatchEvent(new CustomEvent("gpp:artefacts-changed", { detail: { setChanged: n } }));
    try { localStorage.setItem(GPP_CFG_PREFIX + "artefacts:touch", new Date().toISOString()); } catch (e) { /* Quota egal */ }
    return n;
  },
  /* Legt ein Artefakt ab. `data` ist das fertige OSCAL-Objekt (oder ein
     beliebiges JSON-fähiges Objekt bei kind "workspace"/"analysis").
     Gleiche id ⇒ Update statt Dublette; ohne id wird über set+tool+filename
     zusammengeführt, damit wiederholte Exporte nicht den Speicher fluten. */
  async save({ id, stage, kind, title, filename, tool, data, meta, set }) {
    /* Dieselbe Serialisierung wie beim Export (index.html: stringify(…, null, 2)) —
       sonst passen sha256/size im Manifest nicht zu den ausgelieferten Dateien. */
    const json = JSON.stringify(data, null, 2);
    const now = new Date().toISOString();
    const st = (set || this.activeSet()).trim() || GPP_DEFAULT_SET;
    let key = id || `${st}:${tool}:${filename}`;
    let existing = await this.get(key);
    if (!existing && !id) {
      // Datensätze aus der Zeit vor den Sets tragen die id tool:filename
      const legacy = await this.get(`${tool}:${filename}`);
      if (legacy && gppSetOf(legacy) === st) { key = legacy.id; existing = legacy; }
    }
    const rec = {
      id: key,
      set: st,
      stage: stage || "model",
      kind: kind || "ssp",
      title: title || filename || key,
      filename: filename || `${key}.json`,
      tool: tool || "unknown",
      createdAt: existing ? existing.createdAt : now,
      updatedAt: now,
      size: json.length,
      sha256: await gppSha256(json),
      meta: meta || {},
      data,
    };
    await gppTx("readwrite", store => store.put(rec));
    /* Einzelstück-Sorten: ältere Exemplare derselben Sorte im Set weichen. */
    if (GPP_SINGLETON_KINDS.has(rec.kind)) {
      const stale = (await this.all(st)).filter(r => r.kind === rec.kind && r.id !== rec.id);
      for (const r of stale) await gppTx("readwrite", store => store.delete(r.id));
    }
    window.dispatchEvent(new CustomEvent("gpp:artefacts-changed", { detail: { id: rec.id, set: st } }));
    try { localStorage.setItem(GPP_CFG_PREFIX + "artefacts:touch", now); } catch (e) { /* Quota egal */ }
    return rec;
  },
  async get(id) {
    return (await gppTx("readonly", store => store.get(id))) || null;
  },
  /* Liste ohne die schweren data-Felder — für Dashboards.
     Ohne Argument: nur das aktive Set; "*" = alle Sets. */
  async list(set) {
    const want = set === undefined ? this.activeSet() : set;
    const all = (await gppTx("readonly", store => store.getAll())) || [];
    return all
      .filter(r => want === "*" || gppSetOf(r) === want)
      .map(({ data, ...rest }) => ({ ...rest, set: gppSetOf(rest) }))
      .sort((a, b) => (b.updatedAt || "").localeCompare(a.updatedAt || ""));
  },
  async all(set) {
    const want = set === undefined ? this.activeSet() : set;
    const all = (await gppTx("readonly", store => store.getAll())) || [];
    return all.filter(r => want === "*" || gppSetOf(r) === want);
  },
  /* Neuestes Artefakt einer Sorte im aktiven Set — für die Tool-Übergabe
     (Generator erzeugt SSP, der Editor bietet ihn automatisch an). */
  async latest(kind, set) {
    const rows = await this.list(set);
    const hit = rows.find(r => r.kind === kind);
    return hit ? await this.get(hit.id) : null;
  },
  /* Übersicht aller Sets mit Bestand */
  async sets() {
    const all = (await gppTx("readonly", store => store.getAll())) || [];
    const by = new Map();
    for (const r of all) {
      const s = gppSetOf(r);
      const e = by.get(s) || { name: s, count: 0, bytes: 0, updatedAt: "" };
      e.count++; e.bytes += r.size || 0;
      if ((r.updatedAt || "") > e.updatedAt) e.updatedAt = r.updatedAt;
      by.set(s, e);
    }
    return [...by.values()].sort((a, b) => a.name.localeCompare(b.name));
  },
  async remove(id) {
    await gppTx("readwrite", store => store.delete(id));
    window.dispatchEvent(new CustomEvent("gpp:artefacts-changed", { detail: { id, removed: true } }));
  },
  async removeSet(name) {
    const doomed = (await this.all("*")).filter(r => gppSetOf(r) === name);
    for (const r of doomed) await gppTx("readwrite", store => store.delete(r.id));
    window.dispatchEvent(new CustomEvent("gpp:artefacts-changed", { detail: { setRemoved: name } }));
    try { localStorage.setItem(GPP_CFG_PREFIX + "artefacts:touch", new Date().toISOString()); } catch (e) { /* Quota egal */ }
    return doomed.length;
  },
  async clear() {
    await gppTx("readwrite", store => store.clear());
    window.dispatchEvent(new CustomEvent("gpp:artefacts-changed", { detail: { cleared: true } }));
  },
};

/* ---------- ZIP-Writer (store, ohne Kompression) ----------
   Bewusst selbst gebaut: die Sammlung bindet keine externen Bibliotheken ein,
   und "store" reicht — OSCAL-JSON wandert ohnehin meist komprimiert über die
   Leitung. Erzeugt ein reguläres, von jedem Entpacker lesbares Archiv. */
const GPP_CRC_TABLE = (() => {
  const t = new Uint32Array(256);
  for (let i = 0; i < 256; i++) {
    let c = i;
    for (let k = 0; k < 8; k++) c = (c & 1) ? (0xEDB88320 ^ (c >>> 1)) : (c >>> 1);
    t[i] = c >>> 0;
  }
  return t;
})();
function gppCrc32(bytes) {
  let c = 0xFFFFFFFF;
  for (let i = 0; i < bytes.length; i++) c = GPP_CRC_TABLE[(c ^ bytes[i]) & 0xFF] ^ (c >>> 8);
  return (c ^ 0xFFFFFFFF) >>> 0;
}
function gppDosDateTime(d) {
  const dt = d instanceof Date ? d : new Date(d || Date.now());
  const year = Math.max(1980, dt.getFullYear());
  return {
    time: (dt.getHours() << 11) | (dt.getMinutes() << 5) | (dt.getSeconds() >> 1),
    date: ((year - 1980) << 9) | ((dt.getMonth() + 1) << 5) | dt.getDate(),
  };
}
/* files: [{ name, text, date? }] → Blob (application/zip) */
function gppZip(files) {
  const enc = new TextEncoder();
  const chunks = [], central = [];
  let offset = 0;

  const u16 = v => [v & 0xFF, (v >>> 8) & 0xFF];
  const u32 = v => [v & 0xFF, (v >>> 8) & 0xFF, (v >>> 16) & 0xFF, (v >>> 24) & 0xFF];

  for (const f of files) {
    const nameBytes = enc.encode(f.name);
    const data = enc.encode(f.text);
    const crc = gppCrc32(data);
    const { time, date } = gppDosDateTime(f.date);
    // 0x0800 = Dateiname ist UTF-8 (Umlaute in Titeln überleben das)
    const local = [
      ...u32(0x04034b50), ...u16(20), ...u16(0x0800), ...u16(0), ...u16(time), ...u16(date),
      ...u32(crc), ...u32(data.length), ...u32(data.length), ...u16(nameBytes.length), ...u16(0),
    ];
    chunks.push(new Uint8Array(local), nameBytes, data);
    central.push({ nameBytes, crc, size: data.length, time, date, offset });
    offset += local.length + nameBytes.length + data.length;
  }

  const cdStart = offset;
  for (const e of central) {
    const rec = [
      ...u32(0x02014b50), ...u16(20), ...u16(20), ...u16(0x0800), ...u16(0), ...u16(e.time), ...u16(e.date),
      ...u32(e.crc), ...u32(e.size), ...u32(e.size), ...u16(e.nameBytes.length),
      ...u16(0), ...u16(0), ...u16(0), ...u16(0), ...u32(0), ...u32(e.offset),
    ];
    chunks.push(new Uint8Array(rec), e.nameBytes);
    offset += rec.length + e.nameBytes.length;
  }
  const eocd = [
    ...u32(0x06054b50), ...u16(0), ...u16(0), ...u16(central.length), ...u16(central.length),
    ...u32(offset - cdStart), ...u32(cdStart), ...u16(0),
  ];
  chunks.push(new Uint8Array(eocd));
  return new Blob(chunks, { type: "application/zip" });
}
/* ZIP-Reader fürs Hochladen von Sets: versteht "store" (eigene Exporte) und
   "deflate" (fremde Zipper) über DecompressionStream — keine externe Bibliothek.
   Liefert [{ name, text }] für alle Nicht-Verzeichnis-Einträge. */
async function gppUnzip(blobOrBuffer) {
  const buf = blobOrBuffer instanceof Blob
    ? new Uint8Array(await blobOrBuffer.arrayBuffer())
    : new Uint8Array(blobOrBuffer);
  const dv = new DataView(buf.buffer, buf.byteOffset, buf.byteLength);
  let eocd = -1;
  for (let i = buf.length - 22; i >= Math.max(0, buf.length - 22 - 65535); i--) {
    if (dv.getUint32(i, true) === 0x06054b50) { eocd = i; break; }
  }
  if (eocd < 0) throw new Error("Kein ZIP-Endverzeichnis gefunden — ist das ein ZIP?");
  const count = dv.getUint16(eocd + 10, true);
  let off = dv.getUint32(eocd + 16, true);
  const dec = new TextDecoder();
  const out = [];
  for (let n = 0; n < count; n++) {
    if (dv.getUint32(off, true) !== 0x02014b50) throw new Error("ZIP-Zentralverzeichnis beschädigt");
    const method = dv.getUint16(off + 10, true);
    const csize = dv.getUint32(off + 20, true);
    const nameLen = dv.getUint16(off + 28, true);
    const extraLen = dv.getUint16(off + 30, true);
    const commentLen = dv.getUint16(off + 32, true);
    const lho = dv.getUint32(off + 42, true);
    const name = dec.decode(buf.subarray(off + 46, off + 46 + nameLen));
    const lnl = dv.getUint16(lho + 26, true), lel = dv.getUint16(lho + 28, true);
    const dataStart = lho + 30 + lnl + lel;
    const raw = buf.slice(dataStart, dataStart + csize);
    let bytes;
    if (method === 0) bytes = raw;
    else if (method === 8) {
      const ds = new DecompressionStream("deflate-raw");
      bytes = new Uint8Array(await new Response(new Blob([raw]).stream().pipeThrough(ds)).arrayBuffer());
    } else throw new Error(`Nicht unterstützte Kompressionsmethode ${method} in ${name}`);
    if (!name.endsWith("/")) out.push({ name, text: dec.decode(bytes) });
    off += 46 + nameLen + extraLen + commentLen;
  }
  return out;
}
function gppDownloadBlob(name, blob) {
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = name;
  document.body.appendChild(a);
  a.click();
  a.remove();
  setTimeout(() => URL.revokeObjectURL(a.href), 4000);
}

/* ---------- Log-Konsole ein- und ausklappen ----------
   Jedes Werkzeug hat eine Log-Konsole; sie soll überall gleich bedienbar sein.
   Erwartet den Konsolen-Container und ein Element in dessen Kopfzeile, an das
   der Schalter gehängt wird. Der Zustand überlebt den Reload je Werkzeug. */
function gppCollapsibleLog({ consoleEl, headEl, toolId, label = "Log" }) {
  if (!consoleEl || !headEl) return null;
  const key = GPP_CFG_PREFIX + "log:collapsed:" + (toolId || "tool");
  const btn = document.createElement("button");
  btn.type = "button";
  btn.title = `${label} ein-/ausklappen`;
  btn.style.cssText = "background:transparent;border:1px solid currentColor;border-radius:5px;" +
    "color:inherit;font:inherit;font-size:10px;line-height:1;padding:2px 7px;cursor:pointer;opacity:.75";
  /* Alles außer der Kopfzeile ausblenden — so braucht kein Werkzeug eigenes CSS.
     Die vorherige Flex-Vorgabe wird gemerkt und beim Aufklappen zurückgesetzt. */
  const prevFlex = consoleEl.style.flex;
  const others = () => [...consoleEl.children].filter(el => el !== headEl && !headEl.contains(el));
  const apply = collapsed => {
    others().forEach(el => { el.style.display = collapsed ? "none" : ""; });
    consoleEl.style.flex = collapsed ? "0 0 auto" : prevFlex;
    consoleEl.classList.toggle("collapsed", collapsed);
    btn.textContent = collapsed ? "▲ " + label : "▼ " + label;
    btn.setAttribute("aria-expanded", String(!collapsed));
  };
  apply(localStorage.getItem(key) === "1");
  btn.addEventListener("click", () => {
    const next = !consoleEl.classList.contains("collapsed");
    apply(next);
    try { localStorage.setItem(key, next ? "1" : "0"); } catch (e) { /* Quota egal */ }
  });
  headEl.appendChild(btn);
  return btn;
}

/* ---------- Hinweisbanner, wenn die Konfiguration fehlt ----------
   Die Tools halten keine eigenen AI-Felder mehr; fehlt der Key, muss der Weg
   zur config.html unmissverständlich sein. */
function gppConfigBanner(targetEl, opts = {}) {
  if (!targetEl) return null;
  const backend = gppCfg.get("ai:backend");
  const t = gppCfg.target(backend);
  const missing = [];
  if (!t.key) missing.push("API-Key");
  if (!t.model) missing.push("Modell");
  const el = document.createElement("div");
  el.id = "gpp-config-banner";
  el.style.cssText = "margin:10px 0;padding:10px 12px;border-radius:8px;font-size:12.5px;line-height:1.5;" +
    "border:1px solid rgba(255,180,80,.45);background:rgba(255,180,80,.10);color:inherit";
  if (missing.length) {
    el.innerHTML = `<b>AI-Konfiguration unvollständig</b> — es fehlt: ${missing.join(" und ")} für Backend „${backend}". ` +
      `Die Einstellungen liegen zentral in <a href="config.html" target="_blank" rel="noopener" style="color:inherit;font-weight:600">config.html</a>; ` +
      `deterministische Funktionen dieses Tools laufen auch ohne.`;
  } else if (opts.showWhenReady) {
    el.style.cssText = el.style.cssText.replace(/255,180,80/g, "120,220,160");
    el.innerHTML = `AI-Konfiguration aktiv: <b>${backend}</b> · <code>${t.model}</code> — ändern in ` +
      `<a href="config.html" target="_blank" rel="noopener" style="color:inherit;font-weight:600">config.html</a>.`;
  } else {
    return null;
  }
  const old = document.getElementById("gpp-config-banner");
  if (old) old.remove();
  targetEl.prepend(el);
  return el;
}
/* ==GPP-CORE-END== */
