"""
Text Utilities

This module provides utility functions for text manipulation, such as sanitizing strings for use in filenames.
"""

import regex as re

def replace_umlauts(text: str) -> str:
    r"""
    Replaces German umlauts and 'ß' with their equivalents.
    """
    mapping = {
        'ä': 'ae', 'ö': 'oe', 'ü': 'ue',
        'Ä': 'Ae', 'Ö': 'Oe', 'Ü': 'Ue',
        'ß': 'ss'
    }
    for char, replacement in mapping.items():
        text = text.replace(char, replacement)
    return text

def sanitize_filename(filename):
    """
    Sanitizes a string to be used as a filename.

    Args:
        filename (str): The string to sanitize.

    Returns:
        str: The sanitized filename.
    """
    # Replace umlauts
    filename = replace_umlauts(filename)
    # Replace spaces with underscores
    filename = filename.replace(' ', '_')
    # Remove special characters
    filename = re.sub(r'[^a-zA-Z0-9_-]', '', filename)
    # Convert to lowercase
    filename = filename.lower()
    return filename

def sanitize_oscal_prop_name(name: str) -> str:
    r"""
    Sanitizes a string to conform to the OSCAL property name format.
    The name must match the regex: ^(\p{L}|_)(\p{L}|\p{N}|[.\-_])*$
    """
    if not name:
        return "_"

    # Replace invalid characters (anything not a Unicode letter, number, dot, hyphen, or underscore) with an underscore.
    sanitized_name = re.sub(r'[^\w.-]', '_', name)

    # Ensure the name starts with a Unicode letter or underscore.
    if not re.match(r'^[\p{L}_]', sanitized_name):
        sanitized_name = '_' + sanitized_name

    return sanitized_name
