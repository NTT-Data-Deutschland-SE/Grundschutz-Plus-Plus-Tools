"""
OSCAL Validation Utilities

This module provides helper functions for working with OSCAL files, primarily
for validating them against their corresponding JSON schemas.
"""

import copy
import hashlib
import logging
import re
import uuid
from urllib.parse import unquote

from jsonschema import validate, ValidationError

from constants import (
    GPP_KOMPENDIUM_JSON_PATH,
    GPP_CATALOG_PIN_COMMIT,
    GPP_CATALOG_PIN_SHA256,
    BSI_2023_JSON_PATH,
    BSI_2023_PLAIN_JSON_PATH,
    ED23_CATALOG_PIN_COMMIT,
    ED23_BD_CATALOG_PIN_SHA256,
    ED23_PLAIN_CATALOG_PIN_SHA256,
    ED23_BAUSTEIN_NS,
    NG_KATALOG_FILENAME,
)
from utils.file_utils import read_json_file

logger = logging.getLogger(__name__)


def pinned_catalog_resource() -> dict:
    """Back-matter resource for the pinned G++ catalog (Handbuch 3.14, Grundregel 8).

    Field-for-field identical to what scripts/pin_profile_imports.py emits — same
    uuid5-of-the-pinned-URL derivation, same title convention — so profiles generated
    by the pipeline and profiles migrated by the script are indistinguishable and
    re-runs don't churn in git.
    """
    return {
        "uuid": pinned_catalog_resource_uuid(),
        "title": (
            f"{unquote(GPP_KOMPENDIUM_JSON_PATH.rsplit('/', 1)[-1])}"
            f" @ {GPP_CATALOG_PIN_COMMIT[:12]}"
        ),
        "rlinks": [
            {
                "href": GPP_KOMPENDIUM_JSON_PATH,
                "hashes": [
                    {"algorithm": "SHA-256", "value": GPP_CATALOG_PIN_SHA256}
                ],
            }
        ],
    }


def pinned_catalog_resource_uuid() -> str:
    """Deterministic UUID of the pinned-catalog back-matter resource."""
    return str(uuid.uuid5(uuid.NAMESPACE_URL, GPP_KOMPENDIUM_JSON_PATH))


def pinned_catalog_import_href() -> str:
    """Fragment href ("#<uuid>") a profile import uses to reference the pinned catalog."""
    return f"#{pinned_catalog_resource_uuid()}"


def _pinned_resource(url: str, commit: str, sha256: str, description: str) -> dict:
    return {
        "uuid": str(uuid.uuid5(uuid.NAMESPACE_URL, url)),
        "title": f"{unquote(url.rsplit('/', 1)[-1])} @ {commit[:12]}",
        "description": description,
        "rlinks": [
            {
                "href": url,
                "media-type": "application/json",
                "hashes": [{"algorithm": "SHA-256", "value": sha256}],
            }
        ],
    }


def pinned_ed23_catalog_resource_uuid() -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_URL, BSI_2023_JSON_PATH))


def pinned_ed23_catalog_resource() -> dict:
    """Back-matter resource of the pinned benutzerdefinierte ED23 catalog (123 Bausteine)."""
    return _pinned_resource(
        BSI_2023_JSON_PATH, ED23_CATALOG_PIN_COMMIT, ED23_BD_CATALOG_PIN_SHA256,
        "BSI IT-Grundschutz-Kompendium Edition 2023 als OSCAL (benutzerdefinierte Ausgabe NTT DATA DACH: "
        "111 BSI-Bausteine und 12 nutzergenerierte NG-Bausteine)",
    )


def pinned_ed23_plain_catalog_resource() -> dict:
    """Back-matter resource of the pinned plain BSI ED23 catalog (111 Bausteine)."""
    return _pinned_resource(
        BSI_2023_PLAIN_JSON_PATH, ED23_CATALOG_PIN_COMMIT, ED23_PLAIN_CATALOG_PIN_SHA256,
        "BSI IT-Grundschutz-Kompendium Edition 2023 als OSCAL (nur die 111 BSI-Bausteine; "
        "Referenz für die NG-Erkennung)",
    )


def ng_katalog_resource_uuid(sha256: str) -> str:
    """Deterministic UUID of the NG Ergänzungskatalog resource — changes with its content."""
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"ng-ergaenzungskatalog:{sha256}"))


def ng_katalog_resource(sha256: str, n_controls: int, title: str) -> dict:
    """Back-matter resource with a RELATIVE rlink: the catalog sits next to the profile.

    Resolved relative to the profile's URI by the consumers; the hash makes it fail closed.
    """
    return {
        "uuid": ng_katalog_resource_uuid(sha256),
        "title": title,
        "description": (
            f"NG Ergänzungskatalog mit {n_controls} nutzergenerierten Controls, Datei "
            f"{NG_KATALOG_FILENAME} neben diesem Profil"
        ),
        "rlinks": [
            {
                "href": NG_KATALOG_FILENAME,
                "media-type": "application/json",
                "hashes": [{"algorithm": "SHA-256", "value": sha256}],
            }
        ],
    }


def sha256_of_file(path: str) -> str:
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def json_equal_ignoring(a, b, ignore=("last-modified",)) -> bool:
    """Deep equality after stripping the given keys at any depth (for no-op write detection)."""
    def strip(x):
        if isinstance(x, dict):
            return {k: strip(v) for k, v in x.items() if k not in ignore}
        if isinstance(x, list):
            return [strip(v) for v in x]
        return x
    return strip(copy.deepcopy(a)) == strip(copy.deepcopy(b))


_TOKEN_RE = re.compile(r"^[^\W\d_][\w.\-]*$", re.UNICODE)


def _prop(obj: dict, name: str, ns: str = None):
    for p in obj.get("props", []) or []:
        if p.get("name") == name and (ns is None or p.get("ns") == ns):
            return p.get("value")
    return None


def validate_ed23_profile_structure(profile: dict, ng_ids: set = None, filename: str = None) -> list:
    """Structural invariants of an ED23-Baustein profile (merge.custom + two imports + alters).

    Returns human-readable problems (empty list == valid). Complements the JSON-schema check of
    ED23-Baustein-profile/pruefe_export.py with the rules only this pipeline knows.
    """
    problems = []
    prof = (profile or {}).get("profile")
    if not isinstance(prof, dict):
        return ["missing top-level 'profile' object"]
    if not prof.get("uuid"):
        problems.append("profile.uuid is missing")
    meta = prof.get("metadata") or {}
    if not meta.get("oscal-version"):
        problems.append("profile.metadata.oscal-version is missing")
    herkunft = _prop(meta, "herkunft", ED23_BAUSTEIN_NS)
    if herkunft not in ("BSI", "NG"):
        problems.append(f"metadata prop herkunft missing or invalid: {herkunft!r}")
    if not _prop(meta, "ed23-baustein", ED23_BAUSTEIN_NS):
        problems.append("metadata prop ed23-baustein is missing")
    if filename is not None:
        is_ng_file = filename.startswith("NG_")
        if is_ng_file != (herkunft == "NG"):
            problems.append(f"filename prefix NG_ ({is_ng_file}) does not match herkunft={herkunft}")
        if is_ng_file != str(meta.get("title", "")).startswith("NG "):
            problems.append("title prefix 'NG ' does not match the filename prefix")

    imports = prof.get("imports") or []
    if not imports:
        problems.append("profile.imports is missing or empty")
    imported = set()
    resources = {r.get("uuid"): r for r in (prof.get("back-matter") or {}).get("resources", []) or []}
    for i, imp in enumerate(imports):
        href = imp.get("href", "")
        if not href.startswith("#") or href[1:] not in resources:
            problems.append(f"imports[{i}] href {href!r} does not resolve to a back-matter resource")
        ids = [cid for ic in imp.get("include-controls", []) or [] for cid in ic.get("with-ids", []) or []]
        if not ids:
            problems.append(f"imports[{i}] has no with-ids")
        if i == 1:
            bad = [cid for cid in ids if not cid.startswith("NG-")]
            if bad:
                problems.append(f"imports[1] must hold only NG- ids, found {bad[:3]}")
            if ng_ids is not None:
                unknown = [cid for cid in ids if cid not in ng_ids]
                if unknown:
                    problems.append(f"imports[1] references unknown NG ids {unknown[:3]}")
            res = resources.get(href[1:], {})
            rl = (res.get("rlinks") or [{}])[0]
            if rl.get("href") != NG_KATALOG_FILENAME:
                problems.append(f"NG resource rlink must be the relative {NG_KATALOG_FILENAME}")
            if not any(h.get("algorithm") == "SHA-256" and h.get("value") for h in rl.get("hashes", []) or []):
                problems.append("NG resource rlink has no SHA-256 hash")
        elif i == 0:
            bad = [cid for cid in ids if cid.startswith("NG-")]
            if bad:
                problems.append(f"imports[0] must not hold NG- ids, found {bad[:3]}")
        imported.update(ids)
    if len(imports) > 2:
        problems.append(f"expected at most 2 imports, found {len(imports)}")

    merge = prof.get("merge") or {}
    if ((merge.get("combine") or {}).get("method")) != "use-first":
        problems.append("merge.combine.method must be 'use-first'")
    inserted = {}
    group_ids = set()
    link_targets = []

    def walk(groups, path):
        for g in groups or []:
            gid = g.get("id")
            if not gid or not _TOKEN_RE.match(gid):
                problems.append(f"group at {path} has missing/invalid id {gid!r}")
            elif gid in group_ids:
                problems.append(f"duplicate group id {gid}")
            else:
                group_ids.add(gid)
            if g.get("class") == "ed23-anforderung":
                has_insert = False
                for ins in g.get("insert-controls", []) or []:
                    for ic in ins.get("include-controls", []) or []:
                        for cid in ic.get("with-ids", []) or []:
                            has_insert = True
                            if cid in inserted:
                                problems.append(f"control {cid} inserted twice ({inserted[cid]} and {gid})")
                            inserted[cid] = gid
                            if cid not in imported:
                                problems.append(f"group {gid} inserts {cid} which is not imported")
                has_link = any(l.get("rel") == "related" for l in g.get("links", []) or [])
                if not (has_insert or has_link or _prop(g, "ohne-control", ED23_BAUSTEIN_NS)
                        or _prop(g, "entfallen", ED23_BAUSTEIN_NS)):
                    problems.append(f"group {gid} has neither controls, a related link, ohne-control nor entfallen")
                for l in g.get("links", []) or []:
                    if str(l.get("href", "")).startswith("#"):
                        link_targets.append((gid, l["href"][1:]))
            walk(g.get("groups"), f"{path}/{gid}")

    walk((merge.get("custom") or {}).get("groups"), "")
    for gid, target in link_targets:
        if target not in inserted:
            problems.append(f"group {gid} links to #{target} which is not inserted anywhere")
    missing = imported - set(inserted)
    if missing:
        problems.append(f"imported but never inserted: {sorted(missing)[:5]}")

    allowed_positions = {"before", "after", "starting", "ending"}
    seen_part_ids = set()
    for ai, alter in enumerate(((prof.get("modify") or {}).get("alters") or [])):
        cid = alter.get("control-id")
        if not cid:
            problems.append(f"alters[{ai}] has no control-id")
        elif cid not in imported:
            problems.append(f"alters[{ai}] targets {cid} which is not imported")
        adds = alter.get("adds") or []
        if not adds:
            problems.append(f"alters[{ai}] ({cid}) has no adds")
        for di, add in enumerate(adds):
            if add.get("position") not in allowed_positions:
                problems.append(f"alters[{ai}].adds[{di}] has invalid position {add.get('position')!r}")
            parts = add.get("parts") or []
            if parts:
                if not add.get("by-id"):
                    problems.append(f"alters[{ai}].adds[{di}] has parts but no by-id anchor")
                for pi, part in enumerate(parts):
                    loc = f"alters[{ai}].adds[{di}].parts[{pi}]"
                    if part.get("name") != "statement":
                        problems.append(f"{loc} name is {part.get('name')!r}, expected 'statement'")
                    pid = part.get("id")
                    if not pid:
                        problems.append(f"{loc} has no id")
                    elif pid in seen_part_ids:
                        problems.append(f"{loc} duplicate part id {pid!r}")
                    else:
                        seen_part_ids.add(pid)
                    if not part.get("prose"):
                        problems.append(f"{loc} ({pid}) has empty prose")
            elif not add.get("props"):
                problems.append(f"alters[{ai}].adds[{di}] has neither parts nor props")
    return problems

def validate_oscal(json_path: str, schema_path: str) -> bool:
    """
    Validates a JSON file against a given JSON schema.

    Args:
        json_path (str): The path to the JSON file to validate.
        schema_path (str): The path to the JSON schema file.

    Returns:
        bool: True if validation is successful, False otherwise.
    """
    schema = read_json_file(schema_path)
    if not schema:
        logger.error(f"Could not load schema from {schema_path}")
        return False

    # Workaround for https://github.com/python-jsonschema/jsonschema/issues/1213
    # The OSCAL schema uses a Unicode-aware regex that is not supported by the 'regex'
    # format checker in jsonschema. We remove the pattern to allow for structural validation.
    if 'definitions' in schema and 'TokenDatatype' in schema['definitions']:
        if 'pattern' in schema['definitions']['TokenDatatype']:
            del schema['definitions']['TokenDatatype']['pattern']

    instance = read_json_file(json_path)
    if not instance:
        logger.error(f"Could not load JSON instance from {json_path}")
        return False

    try:
        validate(instance=instance, schema=schema)
        logger.info(f"Successfully validated {json_path} against {schema_path}")
        return True
    except ValidationError as e:
        logger.error(f"Validation failed for {json_path}: {e.message}")
        return False
    except Exception as e:
        logger.error(f"An unexpected error occurred during validation of {json_path}: {e}")
        return False


def validate_enhanced_profile_structure(profile: dict) -> list:
    """Structurally validates a generated enhanced OSCAL profile.

    The repo has no bundled OSCAL profile JSON schema (the only schema path in the code is a
    component schema that is not present), so rather than validate against a full schema we
    check the invariants the pipeline must uphold for the `modify.alters[].adds[]` mechanism
    to resolve and for downstream apps to read the maturity parts (issue 3.3):

    * required top-level fields (profile / uuid / metadata.oscal-version / imports);
    * each alter has a `control-id` and at least one `adds`;
    * each `adds` has a `by-id` and `position` in the OSCAL-allowed set;
    * each added part is a `statement` with an id and prose;
    * all added part ids are unique within the profile.

    Returns a list of human-readable problem strings (empty list == valid).
    """
    problems = []
    prof = (profile or {}).get("profile")
    if not isinstance(prof, dict):
        return ["missing top-level 'profile' object"]

    if not prof.get("uuid"):
        problems.append("profile.uuid is missing")
    meta = prof.get("metadata") or {}
    if not meta.get("oscal-version"):
        problems.append("profile.metadata.oscal-version is missing")
    if not prof.get("imports"):
        problems.append("profile.imports is missing or empty")

    allowed_positions = {"before", "after", "starting", "ending"}
    seen_part_ids = set()

    for ai, alter in enumerate(((prof.get("modify") or {}).get("alters") or [])):
        if not alter.get("control-id"):
            problems.append(f"alters[{ai}] has no control-id")
        adds = alter.get("adds") or []
        if not adds:
            problems.append(f"alters[{ai}] ({alter.get('control-id')}) has no adds")
        for di, add in enumerate(adds):
            if not add.get("by-id"):
                problems.append(f"alters[{ai}].adds[{di}] has no by-id anchor")
            if add.get("position") not in allowed_positions:
                problems.append(
                    f"alters[{ai}].adds[{di}] has invalid position {add.get('position')!r}"
                )
            for pi, part in enumerate(add.get("parts") or []):
                loc = f"alters[{ai}].adds[{di}].parts[{pi}]"
                if part.get("name") != "statement":
                    problems.append(f"{loc} name is {part.get('name')!r}, expected 'statement'")
                pid = part.get("id")
                if not pid:
                    problems.append(f"{loc} has no id")
                elif pid in seen_part_ids:
                    problems.append(f"{loc} duplicate part id {pid!r}")
                else:
                    seen_part_ids.add(pid)
                if not part.get("prose"):
                    problems.append(f"{loc} ({pid}) has empty prose")

    return problems

def _find_statement_part_id(control: dict) -> str:
    """Returns the id of the control's 'statement' part, or None if it has none.

    OSCAL profile `adds` blocks anchor new sub-statements to an existing part via
    `by-id`. The G++ catalog names statement parts `{control_id}_stm`, but rather than
    assume that convention we read the actual id of the part whose name is "statement".
    """
    for part in control.get("parts", []) or []:
        if part.get("name") == "statement" and part.get("id"):
            return part["id"]
    return None


def extract_all_gpp_controls(catalog: dict) -> dict:
    """Recursively extracts all controls from a G++ catalog for quick lookup."""
    controls = {}

    def traverse_controls(control_list):
        for control in control_list:
            control_id = control.get("id")
            if control_id:
                stmt_part_id = _find_statement_part_id(control)
                # Prefer the statement part's prose for the Level 3 baseline; fall
                # back to the first part's prose for controls without a statement part.
                prose = ""
                if control.get("parts"):
                    prose = control["parts"][0].get("prose", "")
                    for part in control["parts"]:
                        if part.get("id") == stmt_part_id:
                            prose = part.get("prose", prose)
                            break
                controls[control_id] = {
                    "title": control.get("title", ""),
                    "prose": prose,
                    "statement_part_id": stmt_part_id,
                }
            # Controls can nest sub-controls (e.g. TEST.2.2.1 under TEST.2.2); these
            # are referenced directly in profiles, so they must be in the lookup too.
            if control.get("controls"):
                traverse_controls(control["controls"])

    def traverse_groups(groups):
        for group in groups:
            traverse_controls(group.get("controls", []))
            if "groups" in group:
                traverse_groups(group["groups"])

    traverse_groups(catalog.get("catalog", {}).get("groups", []))
    return controls

def get_component_type(baustein_id: str) -> str:
    """Returns the component type based on the Baustein ID format."""
    return "process" if "prozesse" in baustein_id.lower() or "methodik" in baustein_id.lower() else "software"

def normalize_id(id_str: str) -> str:
    """Normalizes an ID string for comparison (lowercase, stripped)."""
    return str(id_str).strip().lower()
