"""Main file of the package. Holds the convert function."""

import re

md_tags = {
    "**": ("<strong>", "</strong>"),
    "*":  ("<em>", "</em>"),
}


def convert(md_string) -> str:
    """Converts a given string of markdown text into an HTML equivalent"""

    md_string = _find_bold(md_string)
    md_string = _find_italics(md_string)

    return md_string


def _find_generic(tag, regex, md_string) -> str:
    """Find a generic open/close tag pairs like bold, italics, etc.
    Private method to be used with convert().
    Args:
        tag (str): The tag in plaintext. This should have an entry in the md_tags dict
        regex (str): The regex string that will be used to identify the tag
        md_string (str): The string containing markdown"""

    result = ""
    tag_split = re.split(regex, md_string)
    if len(tag_split) > 0:
        closing_tag = False
        for idx in range(len(tag_split)):
            # Don't open an unclosed tag and also don't leave one hanging
            if (idx == len(tag_split) - 1) and ((len(tag_split) % 2) == 1):
                result += tag_split[idx]

            # Otherwise, just operate as normal
            else:
                result += tag_split[idx] + md_tags[tag][closing_tag]
                closing_tag = not closing_tag

        return result

    else:
        return md_string


def _find_bold(md_string) -> str:
    """Find bold tags and return a string with them inserted.
    Args:
        md_string (str): String containing markdown"""

    tag = '**'
    regex = r"(?<!\\)[*]{2}|[_]{2}"
    return _find_generic(tag, regex, md_string)


def _find_italics(md_string) -> str:
    """Find italics tags and return a string with them inserted.
    Should be used only after _find_bold() has been applied previously.
    Args:
        md_string (str): String containing markdown"""

    tag = '*'
    regex = r"(?<![*\\])[*]|[_]"  # Potentially buggy behavior because _word* will italicize
    return _find_generic(tag, regex, md_string)
