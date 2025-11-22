from dataclasses import dataclass


@dataclass
class Token:
    type: str
    value: str
    position: int


# トークン種類
TOKEN_TYPES = {
    "LET": "LET",
    "IDENTIFIER": "IDENTIFIER",
    "NUMBER": "NUMBER",
    "PLUS": "+",
    "MINUS": "-",
    "STAR": "*",
    "SLASH": "/",
    "EQUAL": "=",
    "LPAREN": "(",
    "RPAREN": ")",
    "COMMA": ",",
    "EOF": "EOF",
}
