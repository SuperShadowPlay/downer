# downer
## A CommonMark to HTML Python 3 module.

Provides a CommonMark-flavored Markdown-to-HTML function that will take a string formatted with Markdown text and return a string with the equivalent HTML.
Uses the syntax as described in [CommonMark 0.31.2](https://spec.commonmark.org/0.31.2). Support for other Markdown flavors has been considered but is not a current goal of this project.

This module attempts to parse CommonMark text into an AST, which is done with a handwritten lexer and parser.
It will attempt to feature an HTML generator that takes the AST and reconstructs valid HTML for the provided text.
# Feature To-Do
- [ ] Lexer
- [ ] Parser
- [ ] HTML Generator