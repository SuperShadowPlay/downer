"""Defines Tokens for the parser."""

from enum import Enum


class TokenType(Enum):
    UNSPECIFIED = 0  # An uninitialized type. No actual token should ever have this type.

    # Leaf Container tokens
    HEADING_1 = 1  # <h1>
    HEADING_2 = 2  # |
    HEADING_3 = 3  # |
    HEADING_4 = 4  # |
    HEADING_5 = 5  # |
    HEADING_6 = 6  # <h6>
    THEMATIC_BREAK = 7  # <hr/>
    CODE_BLOCK = 8  # <code> signified by an indent
    FENCED_CODE_BLOCK = 9  # <code> signified by ``` or ~~~
    HTML_BLOCK = 10  # Block of raw HTML tags
    LINK_REF_DEF = 11  # Link reference definition
    PARAGRAPH = 12  # <p>
    BLANK_LINE = 13

    # Block Container tokens
    BLOCK_QUOTE = 14  # <blockquote>
    BULLET_LIST_MARKER = 15
    ORDERED_LIST_MARKER = 16
    LIST = 17

    # Inline tokens
    CODE_SPAN = 18  # <code> signified by one backtick
    LEFT_DELIMITER = 19  # Left-flanking delimiter run
    RIGHT_DELIMITER = 20  # Right-flanking delimiter run
    LINK = 21  # <a href=example.com> Link with []() syntax
    IMAGE = 22  # <img>
    AUTOLINK = 23  # Link enclosed by < and >
    HTML_TAG = 24  # Inline HTML tag
    HARD_BREAK = 25  # A line end that is preceded by two spaces. A <br/> tag.
    SOFT_BREAK = 26  # A normal line break.
    TEXT = 27  # Anything else!


class Token:
    token_type = TokenType.UNSPECIFIED
    value = None
    parent = None
    children = None

    def __init__(self, token_type: TokenType, value="", parent=None):
        self.token_type = token_type
        self.value = value
        self.parent = parent
        self.children = []

    def __str__(self):
        parent_name = "None"
        if self.parent is not None:
            parent_name = self.parent.token_type

        return f'{self.token_type} "{self.value}", parent: "{parent_name}", children: {len(self.children)}'
