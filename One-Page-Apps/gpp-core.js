/* ==GPP-CORE-START== v1  ————————————————————————————————————————————————
   Gemeinsamer Kern aller One-Page-Apps: Konfiguration, Prompt-Registrierung,
   Quellen-Pins und der Artefaktspeicher.

   WICHTIG — dieser Block wird in JEDE Tool-Datei hineinkopiert, nicht per
   <script src> eingebunden. Die Tools sollen einzeln per Doppelklick und
   offline laufen; eine externe Datei würde genau das brechen. Diese Datei
   (_gpp-core.js) ist die Quelle der Wahrheit, `node _gpp-core-check.js`
   vergleicht die eingebetteten Kopien damit.

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
  "ai:thinking": "medium",
  "ai:effort": "medium",
  "ai:grounding": "0",
  "ai:checker:backend": "same",
  "ai:checker:model": "",
  "ai:or:structuredonly": "1",
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
  /* Backend + Key + Modell in einem Rutsch — was jeder AI-Aufruf braucht */
  target(backend) {
    const be = backend || this.get("ai:backend");
    return { backend: be, key: this.get("ai:key:" + be), model: this.get("ai:model:" + be) };
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
    registeredAt: new Date().toISOString(),
    prompts: prompts.map(p => ({
      id: p.id,
      label: p.label,
      placeholders: p.placeholders || [],
      default: p.default,
    })),
  };
  localStorage.setItem(GPP_CFG_PREFIX + "promptdefaults:" + toolId, JSON.stringify(reg));
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
  localStorage.setItem(GPP_CFG_PREFIX + "srcdefaults:" + toolId, JSON.stringify({
    tool: toolId,
    registeredAt: new Date().toISOString(),
    sources: sources.map(s => ({ id: s.id, label: s.label, repo: s.repo, path: s.path, default: s.default })),
  }));
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

const gppArtefacts = {
  /* Legt ein Artefakt ab. `data` ist das fertige OSCAL-Objekt (oder ein
     beliebiges JSON-fähiges Objekt bei kind "workspace"/"analysis").
     Gleiche id ⇒ Update statt Dublette; ohne id wird über tool+filename
     zusammengeführt, damit wiederholte Exporte nicht den Speicher fluten. */
  async save({ id, stage, kind, title, filename, tool, data, meta }) {
    const json = JSON.stringify(data);
    const now = new Date().toISOString();
    const key = id || `${tool}:${filename}`;
    const existing = await this.get(key);
    const rec = {
      id: key,
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
    window.dispatchEvent(new CustomEvent("gpp:artefacts-changed", { detail: { id: rec.id } }));
    try { localStorage.setItem(GPP_CFG_PREFIX + "artefacts:touch", now); } catch (e) { /* Quota egal */ }
    return rec;
  },
  async get(id) {
    return (await gppTx("readonly", store => store.get(id))) || null;
  },
  /* Liste ohne die schweren data-Felder — für Dashboards */
  async list() {
    const all = (await gppTx("readonly", store => store.getAll())) || [];
    return all
      .map(({ data, ...rest }) => rest)
      .sort((a, b) => (b.updatedAt || "").localeCompare(a.updatedAt || ""));
  },
  async all() {
    return (await gppTx("readonly", store => store.getAll())) || [];
  },
  async remove(id) {
    await gppTx("readwrite", store => store.delete(id));
    window.dispatchEvent(new CustomEvent("gpp:artefacts-changed", { detail: { id, removed: true } }));
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
function gppDownloadBlob(name, blob) {
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = name;
  document.body.appendChild(a);
  a.click();
  a.remove();
  setTimeout(() => URL.revokeObjectURL(a.href), 4000);
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
