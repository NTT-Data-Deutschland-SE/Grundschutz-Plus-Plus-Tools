"""
Utility functions for parsing the loaded data into structured formats.

This module contains the logic to transform the raw data loaded from files
into more structured and accessible formats that the pipeline can easily use.
"""

import logging
from typing import Any, Dict, List, Tuple

from constants import ALLOWED_MAIN_GROUPS, ALLOWED_PROCESS_BAUSTEINE


def find_bausteine_with_prose(bsi_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Parses the BSI 2023 JSON to extract a list of Bausteine that have prose.
    """
    bausteine_with_prose = []
    catalog = bsi_data.get("catalog", {})
    for group in catalog.get("groups", []):
        for sub_group in group.get("groups", []):
            if sub_group.get("class") == "baustein":
                # Extract the Baustein's purpose/usage prose. Older catalog revisions labelled
                # this part name "usage"; the current BSI ED2023 catalog labels it "Zielsetzung"
                # (the Baustein's objective). Part names vary across Bausteine ("Zielsetzung",
                # "1.2 Zielsetzung", "1.2. Zielsetzung", ...), so match by substring on name/title
                # and fall back to "Einleitung" (introduction) if no objective part exists.
                baustein_description = ""
                for keyword in ("usage", "zielsetzung", "einleitung"):
                    for part in sub_group.get("parts", []):
                        name = (part.get("name") or "").lower()
                        title = str(part.get("title") or "").lower()
                        if (keyword in name or keyword in title) and part.get("prose"):
                            baustein_description = part["prose"]
                            break
                    if baustein_description:
                        break

                group_id = group.get("id", "").upper()
                sub_group_id = sub_group.get("id", "").upper()
                if (
                    group_id in ALLOWED_MAIN_GROUPS
                    or sub_group_id in ALLOWED_PROCESS_BAUSTEINE
                ):
                    if baustein_description:
                        bausteine_with_prose.append(
                            {
                                "id": sub_group.get("id"),
                                "title": _ensure_string_title(sub_group.get("title")),
                                "description": baustein_description,
                                "layer": group_id,
                            }
                        )
    return bausteine_with_prose


logger = logging.getLogger(__name__)

def _ensure_string_title(title_value: Any) -> str:
    """Ensures the title value is a single string, handling lists."""
    if isinstance(title_value, list) and title_value:
        # If it's a list (common in the source JSON), take the first element.
        return str(title_value[0])
    elif isinstance(title_value, str):
        return title_value
    # Fallback for empty lists or other types.
    return ""



def _traverse_and_collect_controls(
    controls: List[Dict[str, Any]],
    zielobjekt_to_controls_map: Dict[str, List[str]],
    gpp_control_titles: Dict[str, str],
):
    """
    Recursively traverses a list of controls to populate the maps, ensuring no
    duplicate control IDs are added for any Zielobjekt.
    """
    for control in controls:
        control_id = control.get("id")
        if not control_id:
            continue

        control_title_value = control.get("title")
        final_title = _ensure_string_title(control_title_value)

        if final_title:
            gpp_control_titles[control_id] = final_title

        for part in control.get("parts", []):
            for prop in part.get("props", []):
                if prop.get("name") == "target_object_categories":
                    zielobjekte = [
                        zo.strip() for zo in prop.get("value", "").split(",")
                    ]
                    for zo_name in zielobjekte:
                        if zo_name not in zielobjekt_to_controls_map:
                            zielobjekt_to_controls_map[zo_name] = []
                        if control_id not in zielobjekt_to_controls_map[zo_name]:
                            zielobjekt_to_controls_map[zo_name].append(control_id)

        # Recursive step for nested controls
        if "controls" in control and control["controls"]:
            _traverse_and_collect_controls(
                control["controls"],
                zielobjekt_to_controls_map,
                gpp_control_titles,
            )


def parse_gpp_kompendium_controls(
    gpp_kompendium_data: Dict[str, Any]
) -> Tuple[Dict[str, List[str]], Dict[str, str]]:
    """
    Parses the G++ Kompendium to create two maps:
    1. A map of Zielobjekt names to their associated G++ control IDs.
    2. A map of all G++ control IDs to their titles for semantic matching.

    Args:
        gpp_kompendium_data: The loaded G++ Kompendium JSON data.

    Returns:
        A tuple containing:
        - A dictionary mapping Zielobjekt names to a list of G++ control IDs.
        - A dictionary mapping G++ control IDs to their titles.
    """
    logger.debug("Parsing G++ Kompendium for Zielobjekt-control and control-title maps...")
    zielobjekt_to_controls_map = {}
    gpp_control_titles = {}

    try:
        groups = gpp_kompendium_data.get("catalog", {}).get("groups", [])
        for group in groups:
            for sub_group in group.get("groups", []):
                if sub_group.get("controls"):
                    _traverse_and_collect_controls(
                        sub_group["controls"],
                        zielobjekt_to_controls_map,
                        gpp_control_titles,
                    )
    except Exception as e:
        logger.error(f"Failed to parse G++ Kompendium controls due to an error: {e}")
        raise

    logger.debug(f"Successfully mapped {len(zielobjekt_to_controls_map)} Zielobjekte to controls.")
    logger.debug(f"Successfully parsed {len(gpp_control_titles)} G++ control titles.")
    return zielobjekt_to_controls_map, gpp_control_titles


def filter_markdown(control_ids: List[str], markdown_content: str) -> str:
    """
    Filters a markdown table to include only rows with specified IDs.

    This function is more robust than a regex search as it processes the table
    line by line.

    Args:
        control_ids: A list of IDs (e.g., "GPP.1.1", "SYS.1.1.A1") to retain.
        markdown_content: The full markdown table as a string.

    Returns:
        A string of the filtered markdown table, or an empty string if filtering fails.
    """

    if not control_ids:
        return ""

    lines = markdown_content.strip().splitlines()

    if len(lines) < 2:
        logger.warning("Markdown content is too short to contain a header and separator.")
        return ""

    header = lines[0]
    separator = lines[1]

    # Validate that the separator line looks correct
    if not separator.strip().startswith('|'):
        logger.warning("Markdown separator line is malformed.")
        return ""

    # Efficiently find all relevant rows in a single pass
    rows = []
    control_id_set = set(control_ids)
    for line in lines[2:]:
        line_trimmed = line.strip()
        if line_trimmed.startswith('|'):
            parts = [p.strip() for p in line_trimmed.split('|')]
            if len(parts) > 2 and parts[1] in control_id_set:
                rows.append(line)

    if not rows:
        logger.warning(f"No rows found for control IDs: {control_ids}")
        return ""

    return "\n".join([header, separator] + rows)