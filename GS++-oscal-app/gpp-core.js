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
     IndexedDB     gpp-remote/outbox   noch nicht übertragene Datenbank-Pushes
                   (eigene DB, damit alte Kern-Stände im Cache nie an einer
                   hochgezählten gpp-artefacts-Version scheitern)
   ———————————————————————————————————————————————————————————————————— */
/* Wird erhöht, sobald der Kern etwas anbietet, ohne das die Werkzeuge nicht mehr
   starten (v2: gppFloatingSave, gppAttrArg; v3: gppRemote — Sync mit der
   gemeinsamen Datenbank). Jede Seite prüft beim Start gegen
   ihren Mindeststand — nur so fällt ein alter, aus dem Browser-Cache geladener
   Kern auf, statt beim ersten Aufruf einer neuen Funktion das ganze Skript
   abzubrechen. Die Prüfung auf ein beliebiges Symbol reicht dafür nicht. */
const GPP_CORE_VERSION = "3";
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
  // Gemeinsame Datenbank (optional, Abschnitt "Zusammenarbeit" in config.html).
  // Ohne db:url verhält sich die Sammlung exakt wie ohne diese Schlüssel.
  "db:url": "",
  "db:anonkey": "",
  "db:auth:mode": "passwort",
  "db:auth:provider": "keycloak",
  "db:email": "",
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

/* Wert für ein inline-onclick sicher machen: encodeURIComponent lässt
   ! ' ( ) * ~ unkodiert stehen — das Apostroph beendet den JS-String im
   Attribut, ein Name wie "Klaus' Laptop" bricht den Handler, ein präparierter
   Wert führt eigenen Code aus. Nach der zusätzlichen Kodierung des Apostrophs
   besteht das Ergebnis nur noch aus [A-Za-z0-9-_.!~*()%] und ist damit sowohl
   im einfach gequoteten JS-String als auch im doppelt gequoteten HTML-Attribut
   unkritisch. Gegenstück im Handler ist decodeURIComponent(). */
function gppAttrArg(value) {
  return encodeURIComponent(String(value == null ? "" : value)).replace(/'/g, "%27");
}

/* Hängt den zentral gesetzten Unternehmenskontext an eine System-Instruktion
   oder — wo ein Werkzeug keine hat — an den Prompt selbst. config.html sagt zu,
   dass dieser Text in die KI-Aufrufe eingeht; eingelöst wird die Zusage hier,
   an der einen Backend-Weiche jedes Werkzeugs. Ohne gesetzten Kontext bleibt
   der Text unverändert — kein leerer Absatz, keine Änderung am Prompt-Hash. */
function gppWithContext(systemOrPrompt) {
  const ctx = (gppCfg.get("ai:context") || "").trim();
  const base = systemOrPrompt == null ? "" : String(systemOrPrompt);
  if (!ctx) return base;
  return (base ? base + "\n\n" : "") +
    "Berücksichtige zwingend folgenden Unternehmenskontext für deine Antwort:\n" + ctx;
}

/* ---------- Prompts: Selbstregistrierung ----------
   Die Default-Texte bleiben als Konstanten im jeweiligen Tool: dort stehen sie
   neben dem Code, der sie benutzt, und ändern sich mit ihm. Beim Start meldet
   das Tool sie an; config.html bearbeitet ausschließlich, was angemeldet ist,
   und kennt die Defaults dadurch immer im aktuellen Stand, statt eine zweite
   Kopie zu pflegen, die beim nächsten Prompt-Umbau still veraltet. */
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
/* Ein Pin ist genau ein 40-stelliger Commit-SHA — sonst nichts. Branchnamen
   (main, develop, feature/x) sind offensichtlich beweglich, Tags aber ebenso:
   ein Tag lässt sich verschieben, ohne dass die URL sich ändert. Wer hier
   großzügig ist, meldet "gepinnt" für Quellen, die sich morgen still ändern —
   das ist schlimmer als gar keine Anzeige (Handbuch 3.13/3.14, Grundregel 8). */
const GPP_COMMIT_RE = /^[0-9a-f]{40}$/i;

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
/* github.com/<owner>/<repo>/(blob|raw)/<ref>/<pfad> — die Browser-Form derselben Datei */
function gppParseBlobUrl(url) {
  const m = String(url || "").match(
    /^https?:\/\/(?:www\.)?github\.com\/([^/]+)\/([^/]+)\/(?:blob|raw)\/(refs\/(?:heads|tags)\/[^/]+|[^/]+)\/(.+)$/
  );
  return m ? { owner: m[1], repo: m[2], ref: m[3], path: m[4] } : null;
}
/* Meldet true, wenn die URL nachweislich auf einen beweglichen Ref zeigt.
   Bei GitHub-URLs ist das entscheidbar: alles außer einem Commit-SHA ist
   beweglich. Bei fremden Hosts ist es das nicht — dort werden nur die
   eindeutigen Ref-Namen im Pfad gemeldet, damit die Regel keine Fehlalarme
   über Quellen produziert, deren Versionierung wir nicht kennen. */
function gppIsUnpinned(url) {
  const p = gppParseRawUrl(url) || gppParseBlobUrl(url);
  if (p) return !GPP_COMMIT_RE.test(p.ref);
  return /\/(refs\/(?:heads|tags)\/[^/]+|main|master|develop|latest|HEAD)\//.test(String(url || ""));
}
/* Commit-SHA der URL, oder null wenn sie auf einen beweglichen Ref zeigt */
function gppCommitOf(url) {
  const p = gppParseRawUrl(url) || gppParseBlobUrl(url);
  return p && GPP_COMMIT_RE.test(p.ref) ? p.ref : null;
}
/* URL auf einen Commit umschreiben — baut den Pfad neu auf statt zu ersetzen.
   Die Host-Form bleibt erhalten: raw bleibt raw, blob bleibt blob. */
function gppRepinUrl(url, sha) {
  if (!sha) return url;
  const raw = gppParseRawUrl(url);
  if (raw) return `https://raw.githubusercontent.com/${raw.owner}/${raw.repo}/${sha}/${raw.path}`;
  const blob = gppParseBlobUrl(url);
  if (blob) return `https://github.com/${blob.owner}/${blob.repo}/blob/${sha}/${blob.path}`;
  return url;
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
/* Nimmt Text oder fertige Bytes. Text wird als UTF-8 kodiert — dieselbe
   Kodierung, mit der die Datei später ausgeliefert wird. */
async function gppSha256(textOrBytes) {
  const buf = typeof textOrBytes === "string" ? new TextEncoder().encode(textOrBytes) : textOrBytes;
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
    try { gppRemote.onSetChanged(n); } catch (e) { /* Sync bricht Lokales nie */ }
    return n;
  },
  /* Legt ein Artefakt ab. `data` ist das fertige OSCAL-Objekt (oder ein
     beliebiges JSON-fähiges Objekt bei kind "workspace"/"analysis").
     Gleiche id ⇒ Update statt Dublette; ohne id wird über set+tool+filename
     zusammengeführt, damit wiederholte Exporte nicht den Speicher fluten. */
  async save({ id, stage, kind, title, filename, tool, data, meta, set }) {
    /* Dieselbe Serialisierung wie beim Export (index.html: stringify(…, null, 2)) —
       sonst passen sha256/size im Manifest nicht zu den ausgelieferten Dateien.
       Gezählt und gehasht wird über die UTF-8-Bytes, nicht über JS-Zeichen:
       jedes ä, ö, ü und — zählt sonst als eins statt als zwei bzw. drei Bytes,
       und die Größe im Manifest passt nicht zur Datei auf der Platte. */
    const json = JSON.stringify(data, null, 2);
    const bytes = new TextEncoder().encode(json);
    const now = new Date().toISOString();
    const st = (set || this.activeSet()).trim() || GPP_DEFAULT_SET;
    /* In der Zusammenarbeit ist die Sperre Schreibvoraussetzung — wirft, wenn
       sie fehlt. Ohne DB/Anmeldung und bei Netzausfall kein Eingriff. */
    if (typeof gppRemote !== "undefined") await gppRemote.requireLock(st);
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
      size: bytes.length,
      sha256: await gppSha256(bytes),
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
    /* DB-Push NACH dem lokalen Erfolg anstoßen, nie davor (Leitprinzip:
       IndexedDB ist die Wahrheit, die Datenbank ein Ziel, kein Nadelöhr).
       existing.sha256 ist der Stand, den der Server zuletzt gesehen haben
       kann — er dient drüben als Konfliktprüfung. */
    try { gppRemote.onLocalSave(rec, existing ? existing.sha256 : null); } catch (e) { /* Sync bricht Lokales nie */ }
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
    const rec = await this.get(id);
    if (rec && typeof gppRemote !== "undefined") await gppRemote.requireLock(gppSetOf(rec));
    await gppTx("readwrite", store => store.delete(id));
    window.dispatchEvent(new CustomEvent("gpp:artefacts-changed", { detail: { id, removed: true } }));
    try { gppRemote.onLocalRemove(id); } catch (e) { /* Sync bricht Lokales nie */ }
  },
  async removeSet(name) {
    if (typeof gppRemote !== "undefined") await gppRemote.requireSetDeletion(name);
    const doomed = (await this.all("*")).filter(r => gppSetOf(r) === name);
    for (const r of doomed) await gppTx("readwrite", store => store.delete(r.id));
    window.dispatchEvent(new CustomEvent("gpp:artefacts-changed", { detail: { setRemoved: name } }));
    try { localStorage.setItem(GPP_CFG_PREFIX + "artefacts:touch", new Date().toISOString()); } catch (e) { /* Quota egal */ }
    try { gppRemote.onLocalRemoveSet(name); } catch (e) { /* Sync bricht Lokales nie */ }
    return doomed.length;
  },
  async clear() {
    await gppTx("readwrite", store => store.clear());
    window.dispatchEvent(new CustomEvent("gpp:artefacts-changed", { detail: { cleared: true } }));
  },
};

/* ---------- Gemeinsame Datenbank: gppRemote (Phase 2 des DB-Plans) ----------
   Optionale Synchronisierung mit einer PostgREST+GoTrue-Instanz (Supabase-Stack,
   self-hosted oder gehostet — derselbe Code). Ohne gesetzte db:url ist dieses
   Modul vollständig inert; die Sammlung verhält sich wie bisher.

   Leitprinzip: IndexedDB bleibt die Wahrheit für den laufenden Vorgang, die
   Datenbank ist ein Ziel, kein Nadelöhr. save() liefert lokal zurück, der Push
   hängt daran; scheitert er, wandert er in die Outbox (IndexedDB gpp-remote)
   und wird bei nächster Gelegenheit erneut versucht.

   SERVER-KONTRAKT (gegen die Testinstanz vom 2026-08-09 verifiziert):
     POST {url}/auth/v1/token?grant_type=password       {email, password}
     POST {url}/auth/v1/token?grant_type=refresh_token  {refresh_token}
     POST {url}/auth/v1/logout
     GET  {url}/auth/v1/authorize?provider=…&redirect_to=…   (Pfad B, OIDC)
       → Token-Claims: sub, email, exp (≤ 1 h); org und gpp_role als eigene
         Claims ODER in app_metadata — user() liest beide Stellen.
     Tabelle {url}/rest/v1/artefacts — Spalten: id (PK), set_name, stage,
       kind, title, filename, tool, created_at, updated_at, size, sha256,
       meta, data; org und updated_by setzt der Server aus dem JWT.
       RBAC macht die RLS-Policy, nicht der Client.
       Schreiben ist Compare-and-Swap über den Zeilenfilter:
         PATCH ?id=eq.…&sha256=eq.{prev}  + Prefer: return=representation
           → []  heißt: Zeile fehlt ODER trägt einen anderen sha256.
         Dann GET ?id=eq.…: Zeile da → Konflikt (fremde Änderung);
         Zeile fehlt → POST (neue Zeile); 409/23505 dabei = Einfüge-Rennen,
         wird beim nächsten flush als Konflikt gemeldet.
       Einzelstück-Sorten (GPP_SINGLETON_KINDS) räumt der Client nach
       erfolgreichem Push per DELETE …&kind=eq.…&id=neq.… nach — eine
       serverseitige artefact_save()-Funktion, die Schreiben und Räumen in
       einer Transaktion erledigt, bleibt das Phase-1-Soll; sobald sie
       existiert, wandert _push() dorthin.
     POST {url}/rest/v1/rpc/acquire_set_lock {p_set_name, p_holder_name}
       → [Zeile] | [] (leer: jemand anderes hält die Sperre);
       erneuter Aufruf = Heartbeat.
     DELETE {url}/rest/v1/set_locks?set_name=eq.…   (Freigabe; RLS: nur
       Halter oder admin)
     POST {url}/rest/v1/rpc/whoami {} → {user_id, email, org, gpp_role,
       set_roles} — wirksame Rechte aus der DB (memberships/set_permissions),
       NICHT aus den Token-Claims: Admin-Änderungen greifen sofort, Claims
       hängen bis zu 1 h nach. Die UI richtet sich danach; durchgesetzt wird
       ohnehin serverseitig (RLS).
     Benutzerverwaltung (nur Rolle admin, config.html):
       POST rpc/admin_list_users {} · rpc/admin_create_user {p_email,
       p_password, p_gpp_role} · rpc/admin_delete_user {p_user_id} ·
       rpc/admin_set_role {p_user_id, p_gpp_role} · rpc/admin_set_set_role
       {p_user_id, p_set_name, p_gpp_role} · rpc/admin_clear_set_role
       {p_user_id, p_set_name}
   Alle REST-Aufrufe mit apikey: {anon-key} und Authorization: Bearer {jwt}.

   NICHT synchronisiert: gpp:cfg:* — insbesondere ai:key:* und gh:token
   verlassen den Browser nicht. Vom Sitzungszustand liegt nur das Refresh-Token
   im localStorage; das kurzlebige Access-Token lebt im Speicher des Tabs. */
const GPP_REMOTE_DB = "gpp-remote";
const GPP_REMOTE_STORE = "outbox";
/* Papierkorb für spiegel-gelöschte Artefakte: Wenn der Abgleich eine fremde
   Löschung nachvollzieht, kann er den LETZTEN existierenden Stand eines
   Dokuments treffen — der Browser, der ihn hält, wurde nie gefragt. Deshalb
   wird nicht vernichtet, sondern verschoben; gppRemoteTrash.list()/restore()
   holen es zurück. Der eigene, bewusste Löschvorgang (removeSet mit
   Rückfrage) läuft NICHT über den Papierkorb. */
const GPP_REMOTE_TRASH = "trash";

function gppRemoteDbOpen() {
  return new Promise((resolve, reject) => {
    const req = indexedDB.open(GPP_REMOTE_DB, 2);
    req.onupgradeneeded = () => {
      if (!req.result.objectStoreNames.contains(GPP_REMOTE_STORE)) {
        req.result.createObjectStore(GPP_REMOTE_STORE, { keyPath: "key" });
      }
      if (!req.result.objectStoreNames.contains(GPP_REMOTE_TRASH)) {
        req.result.createObjectStore(GPP_REMOTE_TRASH, { keyPath: "id" });
      }
    };
    req.onsuccess = () => resolve(req.result);
    req.onerror = () => reject(req.error);
  });
}
/* Gleiches Muster wie gppTx: eine Operation je Transaktion, kein await darin. */
async function gppRemoteTx(mode, fn, storeName = GPP_REMOTE_STORE) {
  const db = await gppRemoteDbOpen();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(storeName, mode);
    let result;
    let req;
    try { req = fn(tx.objectStore(storeName)); } catch (e) { db.close(); reject(e); return; }
    if (req && typeof req === "object" && "onsuccess" in req) {
      req.onsuccess = () => { result = req.result; };
    }
    tx.oncomplete = () => { db.close(); resolve(result); };
    tx.onerror = () => { db.close(); reject(tx.error); };
    tx.onabort = () => { db.close(); reject(tx.error); };
  });
}

/* Zugriff auf den Papierkorb — bewusst klein: auflisten, wiederherstellen
   (zurück in den Artefaktbestand UND als Push in die Datenbank, sofern
   angemeldet), leeren. */
const gppRemoteTrash = {
  async list() { return (await gppRemoteTx("readonly", s => s.getAll(), GPP_REMOTE_TRASH)) || []; },
  async restore(id) {
    const entry = await gppRemoteTx("readonly", s => s.get(id), GPP_REMOTE_TRASH);
    if (!entry) return null;
    const { trashedAt, ...rec } = entry;
    await gppTx("readwrite", store => store.put(rec));
    await gppRemoteTx("readwrite", s => s.delete(id), GPP_REMOTE_TRASH);
    window.dispatchEvent(new CustomEvent("gpp:artefacts-changed", { detail: { id: rec.id, restored: true } }));
    try { gppRemote.onLocalSave(rec, null); } catch (e) { /* Push folgt beim nächsten Anlass */ }
    return rec;
  },
  async clear() { await gppRemoteTx("readwrite", s => s.clear(), GPP_REMOTE_TRASH); },
};

const gppRemote = {
  _access: null,          // Access-Token: nur im Speicher dieses Tabs
  _exp: 0,
  _flushing: false,
  _debounceTimer: null,
  _lastSync: "",
  _lastError: "",
  _refreshKey: GPP_CFG_PREFIX + "db:refresh",

  url() { return (gppCfg.get("db:url") || "").trim().replace(/\/+$/, ""); },
  anonKey() { return (gppCfg.get("db:anonkey") || "").trim(); },
  enabled() { return !!this.url(); },
  refreshToken() { return localStorage.getItem(this._refreshKey) || ""; },
  loggedIn() { return !!this._access || !!this.refreshToken(); },

  claims() {
    if (!this._access) return null;
    try {
      const b64 = this._access.split(".")[1].replace(/-/g, "+").replace(/_/g, "/");
      return JSON.parse(new TextDecoder().decode(Uint8Array.from(atob(b64), c => c.charCodeAt(0))));
    } catch (e) { return null; }
  },
  /* org und gpp_role stehen bei Pfad B als eigene Claims im Token, bei
     GoTrue-Konten (Pfad A) je nach Hook-Konfiguration in app_metadata —
     beide Stellen lesen, damit der Rest des Codes es nie wissen muss. */
  user() {
    const c = this.claims();
    if (!c) return null;
    const app = c.app_metadata || {};
    return { email: c.email || "", org: c.org || app.org || "", role: c.gpp_role || app.gpp_role || "", exp: c.exp || 0 };
  },

  _setSession(json) {
    this._access = json.access_token || null;
    const c = this.claims();
    this._exp = c && c.exp ? c.exp * 1000 : Date.now() + (json.expires_in || 3600) * 1000;
    if (json.refresh_token) {
      try { localStorage.setItem(this._refreshKey, json.refresh_token); } catch (e) { /* Quota */ }
    }
    this._emit();
  },
  _clearSession() {
    this._access = null;
    this._exp = 0;
    localStorage.removeItem(this._refreshKey);
    this._emit();
  },

  async _auth(pathAndQuery, body) {
    const r = await fetch(this.url() + "/auth/v1/" + pathAndQuery, {
      method: "POST",
      headers: { "Content-Type": "application/json", apikey: this.anonKey() },
      body: JSON.stringify(body),
    });
    const json = await r.json().catch(() => ({}));
    if (!r.ok) throw new Error(json.error_description || json.msg || json.message || "HTTP " + r.status);
    return json;
  },
  async login(email, password) {
    const json = await this._auth("token?grant_type=password", { email, password });
    this._setSession(json);
    gppCfg.set("db:email", email);
    this.flushSoon(500);
    /* Frisch angemeldet: alle zugänglichen Sets holen, damit geteilte Stände
       sofort auftauchen und nicht erst nach manuellem Setwechsel. */
    this.pullAll().catch(() => {});
    return this.user();
  },
  async refresh() {
    /* Immer frisch aus dem localStorage lesen: GoTrue ROTIERT Refresh-Tokens,
       und ein anderer Tab kann inzwischen rotiert haben. Gleichzeitige
       Refreshes zweier Tabs deckt die Reuse-Toleranz von GoTrue ab. */
    const rt = this.refreshToken();
    if (!rt) throw new Error("keine Sitzung");
    try {
      this._setSession(await this._auth("token?grant_type=refresh_token", { refresh_token: rt }));
    } catch (e) {
      /* Abgelehnter Refresh = Sitzung beendet (abgelaufen, widerrufen).
         Aufräumen statt endlos mit demselben Token wiederholen. */
      this._clearSession();
      throw e;
    }
  },
  async token() {
    if (this._access && Date.now() < this._exp - 60000) return this._access;
    await this.refresh();
    return this._access;
  },
  async logout() {
    try {
      if (this._access) {
        await fetch(this.url() + "/auth/v1/logout", {
          method: "POST",
          headers: { Authorization: "Bearer " + this._access, apikey: this.anonKey() },
        });
      }
    } catch (e) { /* lokal ist die Sitzung gleich ohnehin weg */ }
    this._clearSession();
  },
  /* Pfad B: GoTrue führt den OIDC-Tanz serverseitig; der Browser wird nur
     umgeleitet. Genau deshalb bauen wir Authorization Code + PKCE nicht selbst
     (fehleranfälligste Stelle des Vorhabens, siehe Plan Abschnitt 3). */
  oidcStart() {
    const provider = gppCfg.get("db:auth:provider") || "keycloak";
    const back = location.origin + location.pathname;
    location.href = this.url() + "/auth/v1/authorize?provider=" + encodeURIComponent(provider) +
      "&redirect_to=" + encodeURIComponent(back);
  },
  /* Rückkehr aus Pfad B: Tokens stehen im URL-Fragment. Das Fragment verlässt
     den Browser nie — aber es gehört auch nicht in Verlauf oder Lesezeichen,
     deshalb sofort aus der Adresszeile entfernen. */
  oidcComplete() {
    if (!location.hash.includes("access_token=")) return false;
    const p = new URLSearchParams(location.hash.slice(1));
    if (!p.get("access_token")) return false;
    this._setSession({
      access_token: p.get("access_token"),
      refresh_token: p.get("refresh_token") || "",
      expires_in: parseInt(p.get("expires_in") || "3600", 10),
    });
    history.replaceState(null, "", location.pathname + location.search);
    this.flushSoon(500);
    this.pullAll().catch(() => {});
    return true;
  },

  /* REST-Aufruf mit Auth, Timeout und einmaligem Retry nach 401 (Token kann
     zwischen Prüfung und Ankunft am Server ablaufen — die Claims sagen ≤ 1 h). */
  async api(path, { method = "GET", body, headers = {}, retried = false } = {}) {
    const tok = await this.token();
    const ctrl = new AbortController();
    const timer = setTimeout(() => ctrl.abort(), 20000);
    let r;
    try {
      r = await fetch(this.url() + "/rest/v1/" + path, {
        method,
        headers: { apikey: this.anonKey(), Authorization: "Bearer " + tok, "Content-Type": "application/json", ...headers },
        body: body === undefined ? undefined : JSON.stringify(body),
        signal: ctrl.signal,
      });
    } finally { clearTimeout(timer); }
    if (r.status === 401 && !retried) {
      await this.refresh();
      return this.api(path, { method, body, headers, retried: true });
    }
    if (!r.ok) {
      const json = await r.json().catch(() => ({}));
      const err = new Error(json.message || json.hint || "HTTP " + r.status);
      err.status = r.status;   // 401/403 = Rechte (bleibt am Eintrag), sonst Transport
      throw err;
    }
    if (r.status === 204) return null;
    const text = await r.text();
    return text ? JSON.parse(text) : null;
  },

  /* ---- Outbox ---- */
  async _outboxAll() { return (await gppRemoteTx("readonly", s => s.getAll())) || []; },
  async _outboxGet(key) { return (await gppRemoteTx("readonly", s => s.get(key))) || null; },
  async _outboxPut(e) { await gppRemoteTx("readwrite", s => s.put(e)); },
  async _outboxDel(key) { await gppRemoteTx("readwrite", s => s.delete(key)); },

  /* ---- Einhängepunkte der vier Schreibfunktionen ---- */
  onLocalSave(rec, prevSha) {
    if (!this.enabled()) return;
    (async () => {
      const key = "save:" + rec.id;
      const alt = await this._outboxGet(key);
      /* Baseline bewahren: prevSha ist der letzte Stand, den der Server kennt.
         Hängt bereits ein unerledigter Push, hat der Server auch alle
         zwischenzeitlichen lokalen Stände nie gesehen — der ÄLTESTE prevSha
         bleibt der richtige Vergleichswert, sonst meldet der Server nie einen
         Konflikt, obwohl er längst etwas anderes trägt. */
      if (!alt) {
        await this._outboxPut({ key, op: "save", id: rec.id, set: rec.set, prevSha: prevSha || null,
          queuedAt: new Date().toISOString(), tries: 0 });
      }
      this._emit();
      this._debounce();
    })().catch(() => { /* Outbox nicht schreibbar → nächster save versucht es erneut */ });
  },
  onLocalRemove(id) {
    if (!this.enabled()) return;
    (async () => {
      await this._outboxDel("save:" + id);   // ein Push für Gelöschtes wäre Unsinn
      await this._outboxPut({ key: "remove:" + id, op: "remove", id, queuedAt: new Date().toISOString(), tries: 0 });
      this._emit();
      this._debounce();
    })().catch(() => {});
  },
  onLocalRemoveSet(name) {
    if (!this.enabled()) return;
    (async () => {
      for (const e of await this._outboxAll()) {
        if (e.set === name || (e.op === "remove" && String(e.id).startsWith(name + ":"))) await this._outboxDel(e.key);
      }
      await this._outboxPut({ key: "removeset:" + name, op: "removeset", set: name, queuedAt: new Date().toISOString(), tries: 0 });
      this._emit();
      this._debounce();
    })().catch(() => {});
  },
  onSetChanged(name) {
    /* Beim Setwechsel den Serverstand nachziehen (Plan Phase 2) — verzögert,
       damit der Wechsel selbst nicht auf das Netz wartet. Danach den
       Sperrzustand des neuen Sets holen. */
    if (!this.enabled() || !this.loggedIn()) return;
    setTimeout(() => {
      this.pullSet(name).catch(() => {});
      this._refreshLock(name).catch(() => {});
    }, 300);
  },

  /* Entprellung: abarbeiten_POAM_generator speichert bei jeder Änderung —
     ungebremst wären das Dutzende Anfragen pro Minute. Ein Sammel-Timer über
     alle Einträge genügt, die Outbox selbst ist bereits je Artefakt dedupliziert. */
  _debounce() {
    clearTimeout(this._debounceTimer);
    this._debounceTimer = setTimeout(() => this.flush(), 2000);
  },
  flushSoon(ms) {
    clearTimeout(this._debounceTimer);
    this._debounceTimer = setTimeout(() => this.flush(), ms || 0);
  },

  async flush() {
    if (this._flushing || !this.enabled() || !this.loggedIn()) return;
    this._flushing = true;
    try {
      const entries = (await this._outboxAll())
        .filter(e => !e.conflict)
        .sort((a, b) => (a.queuedAt || "").localeCompare(b.queuedAt || ""));
      for (const e of entries) {
        try {
          const pushedSha = await this._push(e);
          /* Kam während des Pushes ein neuer Speichervorgang für dasselbe
             Artefakt herein, hat onLocalSave den bestehenden Eintrag NICHT neu
             angelegt — der neue Stand stünde dann weder auf dem Server noch als
             eigener Eintrag. Den Eintrag mit dem gepushten sha als neuer
             Baseline behalten statt löschen, damit der nächste Lauf ihn nachholt. */
          if (e.op === "save" && pushedSha) {
            const now = await gppArtefacts.get(e.id);
            if (now && now.sha256 !== pushedSha) {
              e.prevSha = pushedSha; e.tries = 0; delete e.lastError;
              await this._outboxPut(e);
              this._lastError = "";
              continue;
            }
          }
          await this._outboxDel(e.key);
          if (e.op === "save") await this._markSeen(e.id);
          this._lastError = "";
        } catch (err) {
          if (err && err.conflict) {
            /* Fremde Änderung: niemand gewinnt automatisch (Plan Phase 2).
               Der Eintrag bleibt markiert liegen, bis jemand entscheidet. */
            e.conflict = err.conflict;
            await this._outboxPut(e);
            continue;
          }
          e.tries = (e.tries || 0) + 1;
          e.lastError = String((err && err.message) || err);
          await this._outboxPut(e);
          this._lastError = e.lastError;
          /* Rechteproblem (401/403) klebt am Eintrag — die übrigen können
             trotzdem durchgehen. Transportfehler heißt: Server gerade nicht
             erreichbar, der Rest scheitert genauso — abbrechen, Outbox hält. */
          if (err && err.status) continue;
          break;
        }
      }
      this._lastSync = new Date().toISOString();
    } finally {
      this._flushing = false;
      this._emit();
    }
  },
  async _push(e) {
    if (e.op === "save") {
      const rec = await gppArtefacts.get(e.id);
      if (!rec) return;   // inzwischen lokal gelöscht — der remove-Eintrag folgt
      /* Erst die Sitzung sicherstellen: direkt nach einem Seiten-Reload gibt es
         nur das Refresh-Token, und _toRow() läse leere Claims — updated_by
         wäre null, obwohl der Urheber bekannt ist. */
      await this.token();
      const row = this._toRow(rec);
      const id = encodeURIComponent(rec.id);
      let geschrieben = false;
      if (e.prevSha) {
        /* Compare-and-Swap: der Filter trifft nur, wenn der Server noch den
           Stand trägt, den dieser Client zuletzt gesehen hat. */
        const hits = await this.api("artefacts?id=eq." + id + "&sha256=eq." + encodeURIComponent(e.prevSha),
          { method: "PATCH", body: row, headers: { Prefer: "return=representation" } });
        geschrieben = !!(hits && hits.length);
      }
      if (!geschrieben) {
        const cur = await this.api("artefacts?id=eq." + id + "&select=sha256,updated_by,updated_at");
        if (cur && cur.length) {
          if (cur[0].sha256 === rec.sha256) return;   // identischer Inhalt liegt schon drüben (zweiter Tab)
          if (e.prevSha && cur[0].sha256 === e.prevSha) {
            /* Der Server trägt noch GENAU unseren Ausgangsstand — die CAS-PATCH
               hat also nicht wegen einer fremden Änderung 0 Zeilen getroffen,
               sondern weil die RLS-Policy (Rolle × kind) das Schreiben verwehrt.
               Kein Konflikt, sondern ein Rechteproblem: so melden (bleibt am
               Eintrag, keine Konfliktschleife, kein Datenverlust über „Übernehmen"). */
            const err = new Error(`keine Schreibberechtigung für Sorte „${rec.kind}" im Set „${rec.set}"`);
            err.status = 403;
            throw err;
          }
          const err = new Error("Konflikt");
          err.conflict = { serverSha: cur[0].sha256 || "", updatedBy: cur[0].updated_by || "", updatedAt: cur[0].updated_at || "" };
          throw err;
        }
        await this.api("artefacts", { method: "POST", body: row });
      }
      /* Einzelstück-Sorten serverseitig nachziehen: das lokale save() hat
         ältere Exemplare bereits ohne eigenen Push-Eintrag verdrängt. */
      if (GPP_SINGLETON_KINDS.has(rec.kind)) {
        await this.api("artefacts?set_name=eq." + encodeURIComponent(rec.set) +
          "&kind=eq." + encodeURIComponent(rec.kind) + "&id=neq." + id, { method: "DELETE" });
      }
      return rec.sha256;   // gepushter Stand — flush erkennt daran ein Resave während des Pushes
    } else if (e.op === "remove") {
      /* return=representation, um 0 gelöschte Zeilen zu erkennen: entweder schon
         fort (idempotent, ok) oder die RLS-Policy (Rolle × kind) verwehrt das
         Löschen. Steht die Zeile danach noch, war es eine Verweigerung — als
         Rechteproblem melden, sonst käme das Artefakt beim nächsten pullSet
         stumm zurück. */
      const del = await this.api("artefacts?id=eq." + encodeURIComponent(e.id),
        { method: "DELETE", headers: { Prefer: "return=representation" } });
      if (!(del && del.length)) {
        const still = await this.api("artefacts?id=eq." + encodeURIComponent(e.id) + "&select=id");
        if (still && still.length) {
          const err = new Error("keine Berechtigung, dieses Artefakt zu löschen");
          err.status = 403;
          throw err;
        }
      }
    } else if (e.op === "removeset") {
      /* Über die admin-RPC, nicht über Zeilen-DELETEs: sie räumt Artefakte,
         Sperre und Set-Rechte in einer Transaktion und prüft selbst auf
         admin. Andere Clients spiegeln die Löschung beim nächsten pullAll —
         in ihren Papierkorb, nicht ins Nichts. */
      await this.api("rpc/admin_delete_set", { method: "POST", body: { p_set_name: e.set } });
      this._held.delete(e.set);
    }
  },

  /* Serverstand eines Sets in die lokale IndexedDB ziehen. Upsert, kein
     Spiegel: lokale Artefakte, die der Server nicht kennt, bleiben stehen —
     "Lokal zuerst" heißt auch, dass ein Pull nie Arbeit löscht. Artefakte mit
     offenem Outbox-Eintrag werden übersprungen (die lokale, noch nicht
     gepushte Fassung gewinnt bis zur Klärung). Geschrieben wird direkt per
     gppTx, NICHT über save(): kein erneuter Push, keine Singleton-Räumung. */
  async pullSet(setName) {
    if (!this.enabled() || !this.loggedIn()) return { pulled: 0, total: 0 };
    const name = setName || gppArtefacts.activeSet();
    const outbox = await this._outboxAll();
    /* Eigene, noch nicht ausgeführte Set-Löschung: die Zeilen stehen serverseitig
       bis zum Push noch — nicht wieder einlesen, sonst kehrt das gerade gelöschte
       Set zurück und landet nach dem Push als Phantom im Papierkorb. Der
       removeset-Eintrag trägt keine id, greift also nicht über `pending`. */
    if (outbox.some(e => e.op === "removeset" && e.set === name)) return { pulled: 0, removed: 0, total: 0 };
    const rows = await this.api("artefacts?set_name=eq." + encodeURIComponent(name) +
      "&select=id,set_name,stage,kind,title,filename,tool,created_at,updated_at,size,sha256,meta,data") || [];
    const pending = new Set(outbox.map(e => e.id).filter(Boolean));
    let pulled = 0;
    for (const row of rows) {
      if (pending.has(row.id)) continue;
      const local = await gppArtefacts.get(row.id);
      if (local && local.sha256 === row.sha256) continue;
      await gppTx("readwrite", store => store.put(this._toLocal(row)));
      pulled++;
    }
    /* Gelöschtes spiegeln: führt der Server das Set (Zeilen vorhanden oder als
       zugängliches Set bekannt), verschwinden lokale Zeilen, die er nicht mehr
       hat — außer eigener, noch nicht gepushter Arbeit (Outbox). Rein lokale
       Sets, die der Server nie kannte, bleiben vollständig unberührt. */
    let removed = 0;
    if (rows.length > 0 || this.remoteSets().includes(name)) {
      const serverIds = new Set(rows.map(r => r.id));
      for (const rec of await gppArtefacts.all(name)) {
        if (serverIds.has(rec.id) || pending.has(rec.id)) continue;
        if (!rec.remoteSeen) continue;   // nie synchronisiert → wartet auf Übertragung, keine fremde Löschung
        await this._trash(rec);
        removed++;
      }
    }
    if (pulled || removed) {
      window.dispatchEvent(new CustomEvent("gpp:artefacts-changed", { detail: { set: name, pulled, removed } }));
      try { localStorage.setItem(GPP_CFG_PREFIX + "artefacts:touch", new Date().toISOString()); } catch (e) { /* Quota */ }
    }
    this._lastSync = new Date().toISOString();
    this._emit();
    return { pulled, removed, total: rows.length };
  },
  /* Alle für den Benutzer zugänglichen Sets vom Server holen — nicht nur das
     aktive. Ohne das entdeckt ein neu Hinzugekommener geteilte Sets nie: der
     Setwechsel-Pull greift erst, wenn man den Namen schon kennt. Zwei Quellen:
     Sets MIT Artefakten (RLS filtert auf die Org) und Sets, auf die eine
     ausdrückliche Berechtigung besteht (die dürfen leer sein — der Admin hat
     Zugang vergeben, bevor Inhalt existiert). Die Namen landen in
     localStorage, damit index.html auch leere berechtigte Sets anzeigen kann. */
  async pullAll() {
    if (!this.enabled() || !this.loggedIn()) return { sets: [], pulled: 0 };
    const vorher = this.remoteSets();   // VOR dem Überschreiben: für die Löscherkennung
    const rows = await this.api("artefacts?select=set_name") || [];
    const dataSets = [...new Set(rows.map(r => r.set_name))];
    let permSets = [];
    let permOk = true;
    try { permSets = [...new Set((await this.api("set_permissions?select=set_name") || []).map(r => r.set_name))]; }
    catch (e) { permOk = false; /* Recht auf die Sicht fehlt evtl. ODER transienter Fehler — „known" ist dann lückenhaft */ }
    const known = [...new Set([...dataSets, ...permSets])].sort();
    try { localStorage.setItem(GPP_CFG_PREFIX + "remote:sets", JSON.stringify(known)); } catch (e) { /* Quota */ }
    let pulled = 0;
    /* Über ALLE bekannten Sets, nicht nur die mit Serverdaten: ein per
       Berechtigung bekanntes, drüben geleertes Set muss auch lokal leeren —
       pullSet spiegelt Löschungen für server-bekannte Sets. */
    for (const s of known) { try { pulled += (await this.pullSet(s)).pulled; } catch (e) { /* nächstes Set */ } }
    /* Gelöschtes löschen — überall: ein Set, das der Server nachweislich
       KANNTE (stand im letzten pullAll) und jetzt nicht mehr führt, wurde
       drüben gelöscht und verschwindet auch hier. Rein lokale Sets, die nie
       auf dem Server waren, bleiben unberührt; eigene noch nicht gepushte
       Arbeit (Outbox) schützt den jeweiligen Datensatz. */
    let removedSets = 0;
    /* Löschungen nur spiegeln, wenn die Set-Liste vollständig ermittelt wurde:
       schlug die set_permissions-Abfrage fehl, ist „known" lückenhaft und darf
       kein Set als „drüben gelöscht" einstufen — sonst wischt eine einzige
       fehlgeschlagene Anfrage lokalen Bestand in den Papierkorb. */
    if (permOk) {
      const pending = new Set((await this._outboxAll()).map(e => e.set).filter(Boolean));
      for (const name of vorher) {
        if (known.includes(name) || pending.has(name)) continue;
        const doomed = (await gppArtefacts.all(name)).filter(r => r.remoteSeen);
        for (const r of doomed) await this._trash(r);
        if (doomed.length) {
          removedSets++;
          if (gppArtefacts.activeSet() === name && !(await gppArtefacts.all(name)).length) {
            gppArtefacts.setActiveSet(GPP_DEFAULT_SET);
          }
        }
      }
    }
    /* Auch ohne gezogene Zeilen neu rendern: die Set-Liste selbst hat sich
       geändert (neue leere Berechtigung, entferntes Set). */
    window.dispatchEvent(new CustomEvent("gpp:artefacts-changed", { detail: { knownSets: known, removedSets } }));
    this._lastSync = new Date().toISOString();
    this._emit();
    return { sets: known, dataSets, permSets, pulled, removedSets };
  },
  /* Server-Set-Namen aus dem letzten pullAll — für die Set-Auswahl der UI,
     auch für berechtigte, noch leere Sets. */
  remoteSets() {
    try { return JSON.parse(localStorage.getItem(GPP_CFG_PREFIX + "remote:sets") || "[]"); }
    catch (e) { return []; }
  },
  /* Spiegel-Löschung: in den Papierkorb verschieben statt vernichten — die
     fremde Löschung könnte den letzten existierenden Stand treffen. */
  async _trash(rec) {
    try { await gppRemoteTx("readwrite", s => s.put({ ...rec, trashedAt: new Date().toISOString() }), GPP_REMOTE_TRASH); }
    catch (e) { /* Papierkorb voll/kaputt: lieber behalten als vernichten */ return; }
    await gppTx("readwrite", store => store.delete(rec.id));
  },
  /* remoteSeen markiert Zeilen, die der Server nachweislich kennt (gepullt
     oder erfolgreich gepusht). Nur solche darf der Lösch-Spiegel anfassen —
     lokaler Altbestand, der NIE synchronisiert wurde, ist keine „drüben
     gelöschte" Zeile, sondern wartet auf die Übertragung (Phase 5). Ein
     lokaler Neu-Save baut den Datensatz ohne Marker; bis zum nächsten
     erfolgreichen Push schützt ohnehin die Outbox. */
  _toLocal(row) {
    return { id: row.id, set: row.set_name, stage: row.stage, kind: row.kind, title: row.title,
      filename: row.filename, tool: row.tool, createdAt: row.created_at, updatedAt: row.updated_at,
      size: row.size, sha256: row.sha256, meta: row.meta || {}, data: row.data, remoteSeen: true };
  },
  async _markSeen(id) {
    const rec = await gppArtefacts.get(id);
    if (rec && !rec.remoteSeen) {
      rec.remoteSeen = true;
      await gppTx("readwrite", store => store.put(rec));
    }
  },
  /* Zeitstempel und updated_by gehen mit: die Testinstanz (schema.sql) hat
     keinen Trigger dafür, und andere Browser sollen beim Pull echte Zeiten
     und den Urheber sehen — der speist die Konfliktmeldung. */
  _toRow(rec) {
    const c = this.claims() || {};
    return { id: rec.id, set_name: rec.set, stage: rec.stage, kind: rec.kind, title: rec.title,
      filename: rec.filename, tool: rec.tool, created_at: rec.createdAt, updated_at: rec.updatedAt,
      size: rec.size, sha256: rec.sha256, meta: rec.meta || {}, data: rec.data,
      updated_by: c.sub || null };
  },

  /* Konfliktklärung — bewusst schlicht (confirm), die Werkzeuge bekommen mit
     Phase 4 eine richtige Anzeige. Übernehmen = Serverstand ersetzt den
     eigenen; Erzwingen = eigener Stand überschreibt mit der Server-Baseline. */
  async resolveConflicts() {
    const entries = (await this._outboxAll()).filter(e => e.conflict);
    for (const e of entries) {
      const rec = await gppArtefacts.get(e.id);
      const wer = (e.conflict.updatedBy || "jemand anderes") +
        (e.conflict.updatedAt ? " (" + String(e.conflict.updatedAt).slice(0, 16).replace("T", " ") + ")" : "");
      const titel = (rec && rec.title) || e.id;
      if (confirm(`„${titel}": in der Datenbank liegt eine fremde Änderung von ${wer}.\n\nOK — fremde Änderung übernehmen (der eigene Stand wird ersetzt)\nAbbrechen — weiter entscheiden`)) {
        const rows = await this.api("artefacts?id=eq." + encodeURIComponent(e.id) +
          "&select=id,set_name,stage,kind,title,filename,tool,created_at,updated_at,size,sha256,meta,data");
        if (rows && rows[0]) {
          await gppTx("readwrite", store => store.put(this._toLocal(rows[0])));
          window.dispatchEvent(new CustomEvent("gpp:artefacts-changed", { detail: { id: e.id, pulled: 1 } }));
        }
        await this._outboxDel(e.key);
      } else if (confirm(`„${titel}": stattdessen den EIGENEN Stand erzwingen und die fremde Änderung überschreiben?`)) {
        e.prevSha = e.conflict.serverSha || null;
        delete e.conflict;
        e.tries = 0;
        await this._outboxPut(e);
      }
      /* zweimal Abbrechen: Eintrag bleibt als Konflikt liegen */
    }
    this._emit();
    this.flushSoon(0);
  },

  /* ---- Sperren (Phase 4) ----
     Beratend, nicht erzwingend: gegen böswillige Umgehung schützt die
     RLS-Policy, nicht die Sperre. Erneutes Acquire = Heartbeat (60 s, solange
     der Tab sichtbar ist). BEWUSST keine automatische Freigabe beim Schließen
     des Tabs — die Sperre gehört dem Benutzer, nicht dem Tab, und ein zweites
     offenes Werkzeug arbeitet womöglich weiter; abgestürzte Sitzungen räumt
     die 5-Minuten-TTL des Servers ab. */
  _held: new Set(),        // Sets, deren Sperre dieser Benutzer hält (Tab-Sicht)
  _lockCache: null,        // letzter bekannter Sperrzustand des aktiven Sets

  async lockAcquire(setName) {
    const set = setName || gppArtefacts.activeSet();
    const u = this.user() || {};
    const rows = await this.api("rpc/acquire_set_lock", { method: "POST",
      body: { p_set_name: set, p_holder_name: u.email || "unbekannt" } });
    const lock = Array.isArray(rows) ? rows[0] : rows;
    if (lock && !this._held.has(set)) {
      /* Nur beim ERWERB den Serverstand ziehen (Plan Phase 2) — nicht bei
         jedem Heartbeat, sonst pullten wir minütlich. */
      this._held.add(set);
      this.pullSet(set).catch(() => {});
    }
    await this._refreshLock(set);
    return lock || null;
  },
  async lockRelease(setName) {
    const set = setName || gppArtefacts.activeSet();
    await this.api("set_locks?set_name=eq." + encodeURIComponent(set), { method: "DELETE" });
    this._held.delete(set);
    await this._refreshLock(set);
  },
  async lockStatus(setName) {
    const rows = await this.api("set_locks?set_name=eq." + encodeURIComponent(setName || gppArtefacts.activeSet()));
    return (rows && rows[0]) || null;
  },
  /* Fremde Sperre brechen: löschen + neu erwerben. Bei Nicht-Admins löscht
     das DELETE null Zeilen (RLS) und der Erwerb scheitert wie gehabt — die
     Rechteprüfung bleibt beim Server. Der Sperrbruch steht im audit-Log. */
  async lockTakeover(setName) {
    const set = setName || gppArtefacts.activeSet();
    await this.lockRelease(set).catch(() => {});
    return this.lockAcquire(set);
  },
  /* Sperrzustand des aktiven Sets nachladen und bei Änderung Bescheid geben.
     _held folgt dabei der Server-Wahrheit: Übernahme durch einen Admin oder
     TTL-Ablauf beendet den eigenen Heartbeat von selbst. */
  async _refreshLock(setName) {
    if (!this.enabled() || !this.loggedIn()) { this._lockCache = null; return null; }
    const set = setName || gppArtefacts.activeSet();
    try {
      let lock = await this.lockStatus(set);
      /* Abgelaufene Sperre (5 min ohne Heartbeat) zählt wie keine — genau wie
         serverseitig gpp_holds_lock/acquire_set_lock. Sonst hielte ein Halter
         nach TTL-Ablauf fälschlich weiter (der Push würde zum Scheinkonflikt),
         und eine fremde, abgestürzte Sitzung blockierte, obwohl der Server die
         Sperre sofort neu vergäbe. */
      if (lock && lock.heartbeat_at &&
          Date.now() - new Date(lock.heartbeat_at).getTime() >= 5 * 60000) lock = null;
      await this.token();
      const me = (this.claims() || {}).sub || null;
      const info = { set, lock, mine: !!(lock && me && lock.holder === me) };
      if (info.mine) this._held.add(set); else this._held.delete(set);
      /* Der Cache trägt die Anzeige (Chip, Übersicht) und meint das AKTIVE
         Set — eine Abfrage für ein anderes Set darf ihn nicht überschreiben. */
      if (set === gppArtefacts.activeSet()) {
        const changed = JSON.stringify(info) !== JSON.stringify(this._lockCache);
        this._lockCache = info;
        if (changed) this._emit();
      }
      return info;
    } catch (e) { return { set, transportError: true }; }
  },

  /* Schreib-Gate: In der Zusammenarbeit ist die Sperre Schreibvoraussetzung —
     ohne sie wird auch LOKAL nichts geändert, sonst liefe der lokale Stand
     vom Server weg und der Push scheiterte später an der RLS. Ohne DB oder
     ohne Anmeldung bleibt alles frei (Offline-Betrieb ist der Normalfall);
     bei Netzfehlern wird nicht blockiert — dann entscheidet der Server beim
     Push, das ist der Offline-Weg. */
  async requireLock(setName) {
    if (!this.enabled() || !this.loggedIn()) return;
    if (this._held.has(setName)) return;
    const info = await this._refreshLock(setName);
    /* Nur eine frische, GENAU dieses Set betreffende Antwort ohne eigene Sperre
       blockiert. Ein Netzfehler (info.transportError) oder ein aus dem Cache
       stammender Treffer für ein anderes Set blockiert NICHT — dann entscheidet
       der Server beim Push (Offline-Weg: „bei Netzfehlern wird nicht blockiert").
       Früher verschluckte _refreshLock den Netzfehler und lieferte den Cache, so
       dass der Zweig unerreichbar war und der Offline-Fall fälschlich blockierte. */
    if (info && !info.transportError && info.set === setName && !info.mine) {
      throw new Error(`Set „${setName}" ist nicht gesperrt — in der Übersicht „Bearbeiten (sperren)" wählen. Ohne Sperre wird in der Zusammenarbeit nichts geändert.`);
    }
  },

  /* Ein GANZES Set löschen ist Verwaltungssache: nur admin, und auch der nur
     mit gehaltener Sperre. Einzelne Artefakte entfernen bleibt normales
     Bearbeiten. Bei Netzfehlern kein Block — der Push landet dann an der
     admin_delete_set-RPC, die serverseitig ablehnt, und der nächste Abgleich
     stellt die lokale Kopie wieder her. */
  async requireSetDeletion(setName) {
    if (!this.enabled() || !this.loggedIn()) return;
    let rolle = "";
    try { rolle = ((await this.whoami()) || {}).gpp_role || ""; } catch (e) { return; }
    if (rolle !== "admin") {
      throw new Error("Ein geteiltes Set löscht nur die Rolle admin. Einzelne Artefakte lassen sich weiterhin entfernen (mit Sperre).");
    }
    await this.requireLock(setName);
  },

  /* Wirksame Rechte aus der Datenbank — für UI-Weichen wie die
     Benutzerverwaltung. user() liest dagegen nur die Token-Claims. */
  async whoami() {
    return this.api("rpc/whoami", { method: "POST", body: {} });
  },

  /* Phase 5: bestehenden LOKALEN Bestand eines Sets in die Datenbank bringen.
     Die Sync-Schicht kennt nur neue Speichervorgänge — was vor der Anmeldung
     entstand, hat keinen Outbox-Eintrag und würde nie gepusht. Hier bekommt
     jedes Artefakt des Sets einen, ohne Baseline: Kollisionen mit vorhandenen
     Server-Zeilen laufen als Konflikt auf und werden bewusst entschieden;
     identische Inhalte gehen still durch. Sperre vorausgesetzt. */
  async pushSet(setName) {
    if (!this.enabled() || !this.loggedIn()) throw new Error("nicht angemeldet");
    const name = setName || gppArtefacts.activeSet();
    await this.requireLock(name);
    const recs = await gppArtefacts.all(name);
    let queued = 0;
    for (const rec of recs) {
      const key = "save:" + rec.id;
      if (!(await this._outboxGet(key))) {
        await this._outboxPut({ key, op: "save", id: rec.id, set: name, prevSha: null,
          queuedAt: new Date().toISOString(), tries: 0 });
        queued++;
      }
    }
    this._emit();
    await this.flush();
    const rest = await this.status();
    return { queued, total: recs.length, pending: rest.pending, conflicts: rest.conflicts };
  },

  /* ---- Zustand für Anzeigen (config.html, Status-Chip) ---- */
  async status() {
    let entries = [];
    if (this.enabled()) { try { entries = await this._outboxAll(); } catch (e) { /* Anzeige bleibt leer */ } }
    return {
      enabled: this.enabled(),
      loggedIn: this.loggedIn(),
      user: this.user(),
      pending: entries.filter(e => !e.conflict).length,
      conflicts: entries.filter(e => e.conflict).length,
      lastSync: this._lastSync,
      lastError: this._lastError,
      lock: this._lockCache,   // Sperrzustand des aktiven Sets (letzter Stand)
    };
  },
  _emit() { window.dispatchEvent(new CustomEvent("gpp:remote-changed")); },
};

/* Status-Chip: das Phase-3-Gegenstück zu gppConfigBanner, aber selbst
   einhängend — kein Eingriff in die einzelnen Werkzeuge nötig. Erscheint nur,
   wenn eine Server-URL konfiguriert ist; config.html unterdrückt ihn über
   window.GPP_REMOTE_NO_CHIP und zeigt den Zustand selbst an. */
function gppRemoteChip() {
  if (window.GPP_REMOTE_NO_CHIP || !gppRemote.enabled()) return null;
  const old = document.getElementById("gpp-remote-chip");
  if (old) old.remove();
  const chip = document.createElement("button");
  chip.id = "gpp-remote-chip";
  chip.type = "button";
  chip.style.cssText = "position:fixed;right:14px;bottom:14px;z-index:119;cursor:pointer;" +
    "font:600 11px/1 ui-monospace,Consolas,monospace;letter-spacing:.04em;padding:7px 11px;" +
    "border-radius:999px;border:1px solid;background:rgba(15,23,42,.92);backdrop-filter:blur(10px)";
  let conflicts = 0;
  const render = async () => {
    const s = await gppRemote.status();
    conflicts = s.conflicts;
    let text, farbe, hint;
    const fremdeSperre = s.lock && s.lock.lock && !s.lock.mine;
    if (s.conflicts) {
      text = `DB · ${s.conflicts} Konflikt${s.conflicts > 1 ? "e" : ""}`;
      farbe = "#f87171";
      hint = "Fremde Änderungen in der Datenbank — klicken zum Klären.";
    } else if (fremdeSperre) {
      text = `DB · 🔒 ${s.lock.lock.holder_name || "gesperrt"}`;
      farbe = "#fbbf24";
      hint = `Set „${s.lock.set}" ist seit ${String(s.lock.lock.acquired_at || "").slice(11, 16)} von ${s.lock.lock.holder_name} gesperrt — eigene Änderungen riskieren Konflikte. Die Sperre ist beratend; verwaltet wird sie in der Übersicht.`;
    } else if (!s.loggedIn) {
      text = "DB · lokal";
      farbe = "#fbbf24";
      hint = "Nicht angemeldet — Änderungen bleiben in diesem Browser. Klicken für die Anmeldung.";
    } else if (s.pending) {
      text = `DB · ${s.pending} ausstehend`;
      farbe = "#fbbf24";
      hint = s.lastError ? "Letzter Fehler: " + s.lastError : "Wird übertragen, sobald der Server erreichbar ist.";
    } else if (s.lock && !s.lock.lock) {
      /* Angemeldet, Set frei, aber nicht gesperrt: Speichern würde am
         Schreib-Gate scheitern — das soll man sehen, BEVOR man tippt. */
      text = "DB · nur lesen";
      farbe = "#94a3b8";
      hint = `Set „${s.lock.set}" ist nicht gesperrt — zum Bearbeiten in der Übersicht „Bearbeiten (sperren)" wählen. Lesen und Export gehen immer.`;
    } else {
      const eigene = s.lock && s.lock.mine ? " ✏" : "";
      text = "DB · synchron" + eigene;
      farbe = "#34d399";
      hint = "Alle Änderungen sind in der gemeinsamen Datenbank." +
        (eigene ? ` Du hältst die Sperre für Set „${s.lock.set}".` : "") +
        (s.user && s.user.email ? " Angemeldet: " + s.user.email : "");
    }
    chip.textContent = text;
    chip.title = hint;
    chip.style.color = farbe;
    chip.style.borderColor = farbe;
  };
  chip.addEventListener("click", () => {
    if (conflicts) gppRemote.resolveConflicts();
    else window.open("config.html#sec-zusammenarbeit", "_blank", "noopener");
  });
  window.addEventListener("gpp:remote-changed", () => { render(); });
  render();
  document.body.appendChild(chip);
  return chip;
}

/* Anstöße für die Outbox: Rückkehr der Verbindung, Sichtbarwerden des Tabs,
   Sicherheitsnetz-Intervall, und einmal kurz nach dem Laden. */
if (typeof window !== "undefined") {
  window.addEventListener("online", () => gppRemote.flushSoon(1000));
  document.addEventListener("visibilitychange", () => {
    if (document.hidden) return;
    gppRemote.flushSoon(1500);
    /* Zurück im Blick: gehaltene Sperren sofort bestätigen, bevor die TTL
       während einer langen Hintergrundphase abläuft. */
    if (gppRemote.enabled() && gppRemote.loggedIn()) {
      for (const s of gppRemote._held) gppRemote.lockAcquire(s).catch(() => {});
    }
  });
  setInterval(() => { if (gppRemote.enabled() && gppRemote.loggedIn()) gppRemote.flush(); }, 45000);
  /* Sperr-Takt: Heartbeat für gehaltene Sperren, Zustands-Abgleich fürs
     aktive Set (auch Nicht-Halter sollen eine fremde Sperre sehen). Nur im
     sichtbaren Tab — ein Dutzend Hintergrund-Tabs soll den Server nicht
     minütlich zwölffach befragen. */
  setInterval(() => {
    if (document.hidden || !gppRemote.enabled() || !gppRemote.loggedIn()) return;
    for (const s of gppRemote._held) {
      if (s !== gppArtefacts.activeSet()) gppRemote.lockAcquire(s).catch(() => {});
    }
    gppRemote._refreshLock().then(info => {
      if (info && info.mine) return gppRemote.lockAcquire(info.set);
    }).catch(() => {});
  }, 60000);
  const gppRemoteBoot = () => {
    if (gppRemote.enabled() && gppRemote.loggedIn()) {
      gppRemote.flushSoon(1500);
      /* Beim Laden jeder Seite die zugänglichen Sets nachziehen — so ist die
         Set-Liste überall aktuell, nicht nur direkt nach dem Anmelden. */
      setTimeout(() => gppRemote.pullAll().catch(() => {}), 1800);
      /* Sperrzustand des aktiven Sets: hält dieser Benutzer sie (aus einem
         früheren Seitenaufruf), übernimmt dieser Tab den Heartbeat. */
      setTimeout(() => gppRemote._refreshLock().catch(() => {}), 1200);
    }
    gppRemoteChip();
  };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", gppRemoteBoot);
  else gppRemoteBoot();
}

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
function gppCollapsibleLog({ consoleEl, headEl, toolId, label = "Log", defaultCollapsed = false }) {
  if (!consoleEl || !headEl) return null;
  const key = GPP_CFG_PREFIX + "log:collapsed:" + (toolId || "tool");
  /* Einige Werkzeuge reichen die komplette Kopfzeile ein, andere nur deren
     Aktionsbereich. Fuer das Ein-/Ausblenden brauchen wir immer das direkte
     Kind des Konsolen-Containers, der Schalter selbst bleibt aber bei den
     vorhandenen Aktionen. */
  const headerEl = [...consoleEl.children].find(el => el === headEl || el.contains(headEl)) || headEl;
  const btn = document.createElement("button");
  btn.type = "button";
  btn.className = "gpp-log-toggle";
  btn.title = `${label} ein-/ausklappen`;
  btn.style.cssText = "background:transparent;border:1px solid currentColor;border-radius:5px;" +
    "color:inherit;font:inherit;font-size:10px;line-height:1;padding:2px 7px;cursor:pointer;opacity:.75";
  /* Alles außer der Kopfzeile ausblenden — so braucht kein Werkzeug eigenes CSS.
     Die vorherige Flex-Vorgabe wird gemerkt und beim Aufklappen zurückgesetzt. */
  const prevFlex = consoleEl.style.flex;
  const others = () => [...consoleEl.children].filter(el => el !== headerEl);
  const apply = (collapsed, persist = false) => {
    others().forEach(el => { el.style.display = collapsed ? "none" : ""; });
    consoleEl.style.flex = collapsed ? "0 0 auto" : prevFlex;
    consoleEl.classList.toggle("collapsed", collapsed);
    btn.textContent = collapsed ? "▲ " + label : "▼ " + label;
    btn.setAttribute("aria-expanded", String(!collapsed));
    if (persist) {
      try { localStorage.setItem(key, collapsed ? "1" : "0"); } catch (e) { /* Quota egal */ }
    }
    window.dispatchEvent(new CustomEvent("gpp:log-resize"));
  };
  const gespeichert = localStorage.getItem(key);
  apply(gespeichert === null ? Boolean(defaultCollapsed) : gespeichert === "1");
  btn.addEventListener("click", event => {
    event.stopPropagation();
    const next = !consoleEl.classList.contains("collapsed");
    apply(next, true);
  });
  /* persist=false für programmatisches Öffnen (etwa automatisch bei einer
     Warnung): Eine vom Werkzeug ausgelöste Anzeige darf nicht als bewusste
     Entscheidung des Nutzers gespeichert werden und dessen zugeklappten
     Zustand dauerhaft überschreiben. */
  btn.setCollapsed = (collapsed, persist = true) => apply(Boolean(collapsed), persist);
  btn.toggle = () => apply(!consoleEl.classList.contains("collapsed"), true);
  btn.isCollapsed = () => consoleEl.classList.contains("collapsed");
  headEl.appendChild(btn);
  return btn;
}

/* ---------- Einheitliche, schwebende Speicheraktion ----------
   Die Original-Buttons bleiben an ihrem Platz und werden visuell ausgeblendet;
   das Menue arbeitet mit Proxies. Dadurch bleiben spaeter registrierte Listener
   sowie dynamische Disabled-/Hidden-Zustaende der Werkzeuge erhalten. */
function gppFloatingSave({ buttons = [], consoleEl = null, hideContainers = [], label = "Abspeichern", toolId = "tool" } = {}) {
  const entries = buttons.map(item => {
    const cfg = typeof item === "object" && !(item instanceof Element) ? item : { el: item };
    const el = typeof cfg.el === "string" ? document.querySelector(cfg.el) : cfg.el;
    return el ? { el, label: cfg.label || el.dataset.saveLabel || el.textContent.trim() } : null;
  }).filter(Boolean);
  if (!entries.length) return null;

  const alt = document.getElementById(`gpp-save-${toolId}`);
  if (alt) { if (typeof alt.gppDispose === "function") alt.gppDispose(); alt.remove(); }
  const dock = document.createElement("div");
  dock.id = `gpp-save-${toolId}`;
  dock.style.cssText = "position:fixed;left:14px;bottom:14px;z-index:120;font:600 12px/1.2 system-ui,-apple-system,sans-serif";

  const menu = document.createElement("div");
  menu.hidden = true;
  menu.setAttribute("role", "menu");
  menu.style.cssText = "position:absolute;left:0;bottom:calc(100% + 8px);min-width:220px;max-width:min(360px,calc(100vw - 28px));" +
    "padding:6px;background:rgba(15,23,42,.97);border:1px solid rgba(148,163,184,.35);border-radius:8px;" +
    "box-shadow:0 16px 40px rgba(0,0,0,.42);backdrop-filter:blur(16px)";

  const hiddenContainers = new Set(hideContainers.map(item => typeof item === "string" ? document.querySelector(item) : item).filter(Boolean));
  const actionButtons = [];
  const sourceAvailable = el => {
    if (el.disabled || el.hidden || getComputedStyle(el).display === "none") return false;
    for (let parent = el.parentElement; parent; parent = parent.parentElement) {
      if (hiddenContainers.has(parent)) continue;
      const style = getComputedStyle(parent);
      if (style.display === "none" || style.visibility === "hidden") return false;
    }
    return true;
  };

  entries.forEach(({ el, label: actionLabel }) => {
    el.dataset.saveLabel = actionLabel;
    el.style.setProperty("position", "fixed", "important");
    el.style.setProperty("left", "-10000px", "important");
    el.style.setProperty("top", "0", "important");
    el.style.setProperty("width", "1px", "important");
    el.style.setProperty("height", "1px", "important");
    el.style.setProperty("overflow", "hidden", "important");
    el.style.setProperty("clip-path", "inset(50%)", "important");
    el.style.setProperty("pointer-events", "none", "important");
    /* Optisch weg heisst nicht weg fuer die Tastatur: ohne diese beiden Zeilen
       laeuft der Tabulator in einen unsichtbaren 1px-Knopf, der Fokusrahmen
       verschwindet mitten auf der Seite und Enter loest den Export blind aus.
       pointer-events blockt nur die Maus. */
    el.setAttribute("tabindex", "-1");
    el.setAttribute("aria-hidden", "true");

    const action = document.createElement("button");
    action.type = "button";
    action.setAttribute("role", "menuitem");
    action.textContent = actionLabel;
    action.title = actionLabel;
    action.style.cssText = "display:block;width:100%;margin:0;padding:9px 10px;border:0;border-radius:5px;" +
      "background:transparent;color:#e2e8f0;text-align:left;cursor:pointer;font:600 12px/1.25 system-ui,-apple-system,sans-serif";
    const sync = () => {
      const disabled = !sourceAvailable(el);
      if (action.disabled !== disabled) action.disabled = disabled;
      const opacity = disabled ? ".42" : "1";
      const cursor = disabled ? "not-allowed" : "pointer";
      if (action.style.opacity !== opacity) action.style.opacity = opacity;
      if (action.style.cursor !== cursor) action.style.cursor = cursor;
    };
    sync();
    action.addEventListener("mouseenter", () => { if (!action.disabled) action.style.background = "rgba(148,163,184,.16)"; });
    action.addEventListener("mouseleave", () => { action.style.background = "transparent"; });
    action.addEventListener("click", () => {
      sync();
      if (!action.disabled) el.click();
      menu.hidden = true;
      trigger.setAttribute("aria-expanded", "false");
      trigger.focus();   // Fokus zurueck an den Ausloeser statt ins Leere
    });
    actionButtons.push({ action, sync });
    menu.appendChild(action);
  });

  const trigger = document.createElement("button");
  trigger.type = "button";
  trigger.textContent = label;
  trigger.setAttribute("aria-haspopup", "menu");
  trigger.setAttribute("aria-expanded", "false");
  trigger.style.cssText = "min-width:132px;padding:10px 15px;border:1px solid rgba(52,211,153,.6);border-radius:7px;" +
    "background:#059669;color:white;box-shadow:0 10px 28px rgba(0,0,0,.38);cursor:pointer;font:700 13px/1 system-ui,-apple-system,sans-serif";
  trigger.addEventListener("click", () => {
    syncAll();
    menu.hidden = !menu.hidden;
    trigger.setAttribute("aria-expanded", String(!menu.hidden));
  });
  menu.addEventListener("click", event => event.stopPropagation());
  dock.append(menu, trigger);
  document.body.appendChild(dock);

  const closeMenu = () => {
    if (menu.hidden) return;
    menu.hidden = true;
    trigger.setAttribute("aria-expanded", "false");
  };

  /* Alle Eintraege pruefen und das Dock ganz ausblenden, wenn keine einzige
     Aktion erreichbar ist — ein dauerhaft ausgegrautes Menue (Viewer ohne
     KI-Schluessel, Uebersicht bei geschlossener Artefakt-Flaeche) ist nur ein
     Versprechen, das die Seite nicht halten kann. */
  const syncAll = () => {
    actionButtons.forEach(item => item.sync());
    const nutzbar = actionButtons.some(item => !item.action.disabled);
    dock.style.display = nutzbar ? "" : "none";
    if (!nutzbar) closeMenu();
  };
  syncAll();

  hiddenContainers.forEach(el => { el.style.display = "none"; });
  const abbruch = new AbortController();
  const signal = abbruch.signal;
  if (typeof MutationObserver !== "undefined") {
    /* Der Beobachter haengt an document.body, feuert also bei jeder Attribut-
       aenderung der Seite — bei laufender KI-Analyse pro Fortschrittsschritt.
       Deshalb werden Schuebe auf einen Lauf je Frame zusammengefasst, statt
       je Mutation die getComputedStyle-Kette jedes Knopfes hochzulaufen. */
    let geplant = false;
    /* In einem verborgenen Tab liefert requestAnimationFrame keinen Takt — dort
       muss ein Timeout einspringen, sonst bleibt der Zustand des Docks stehen,
       bis der Tab wieder sichtbar wird. */
    const gleichNachher = fn => (typeof requestAnimationFrame === "function" && !document.hidden)
      ? requestAnimationFrame(fn) : setTimeout(fn, 50);
    const observer = new MutationObserver(() => {
      if (geplant) return;
      geplant = true;
      gleichNachher(() => { geplant = false; syncAll(); });
    });
    observer.observe(document.body, { subtree: true, attributes: true, attributeFilter: ["class", "style", "hidden", "disabled"] });
    signal.addEventListener("abort", () => observer.disconnect());
  }

  const placeAboveConsole = () => {
    let bottom = 14;
    if (consoleEl) {
      const rect = consoleEl.getBoundingClientRect();
      if (rect.height > 0 && rect.bottom >= window.innerHeight - 2) bottom = Math.ceil(window.innerHeight - rect.top + 12);
    }
    /* Nach oben begrenzen: bei starkem Zoom oder kurzem Fenster ist die Konsole
       hoeher als der Rest, und ein ungebremstes bottom schoebe Knopf UND Menue
       aus dem sichtbaren Bereich. */
    const maxBottom = Math.max(14, window.innerHeight - dock.offsetHeight - 8);
    dock.style.bottom = `${Math.min(bottom, maxBottom)}px`;
  };
  placeAboveConsole();
  window.addEventListener("resize", placeAboveConsole, { signal });
  window.addEventListener("gpp:log-resize", () => requestAnimationFrame(placeAboveConsole), { signal });
  if (consoleEl && typeof ResizeObserver !== "undefined") {
    const ro = new ResizeObserver(placeAboveConsole);
    ro.observe(consoleEl);
    signal.addEventListener("abort", () => ro.disconnect());
  }
  /* Schliessen beim Klick nach draussen: der Treffer wird am Ziel geprueft statt
     darauf zu bauen, dass jeder Klick bis document durchblubbert. Sonst haelt
     ein beliebiges stopPropagation auf der Seite — etwa am Log-Schalter — das
     Menue offen, waehrend das Dock unter dem Zeiger wegspringt. */
  document.addEventListener("click", event => { if (!dock.contains(event.target)) closeMenu(); }, { signal, capture: true });
  document.addEventListener("keydown", event => { if (event.key === "Escape") closeMenu(); }, { signal });

  /* Ein zweiter Aufruf fuer dasselbe Werkzeug raeumt den alten Stand ab —
     ohne das blieben Beobachter und Listener am entfernten Dock haengen. */
  dock.gppDispose = () => abbruch.abort();
  return { dock, trigger, menu, actions: actionButtons.map(item => item.action), placeAboveConsole, dispose: dock.gppDispose };
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
