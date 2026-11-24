"""Minimal parser for Valve's text KeyValues3 format (the game's .vdata files).

Only what the cross-check needs: objects, arrays, strings, numbers, booleans,
null, and "flagged" values such as ``resource_name:"..."`` or ``subclass: {...}``
(the flag is dropped, the value is kept).
"""
from __future__ import annotations

import re

_TOKEN = re.compile(
    r"""
    (?P<ws>\s+|//[^\n]*|/\*.*?\*/|<!--.*?-->)
  | (?P<mstr>\"\"\".*?\"\"\")
  | (?P<str>"(?:\\.|[^"\\])*")
  | (?P<punct>[{}\[\]=,])
  | (?P<flag>[A-Za-z_][A-Za-z0-9_]*:)(?=\s*["{\[])
  | (?P<word>[^\s{}\[\]=,"]+)
    """,
    re.S | re.X,
)
_NUMBER = re.compile(r"-?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?$")
_ESCAPES = {"n": "\n", "t": "\t", '"': '"', "\\": "\\"}


class KV3Error(ValueError):
    pass


def _tokens(text: str):
    pos = 0
    n = len(text)
    while pos < n:
        m = _TOKEN.match(text, pos)
        if not m:
            raise KV3Error(f"unexpected character {text[pos]!r} at offset {pos}")
        pos = m.end()
        kind = m.lastgroup
        if kind in ("ws", "flag"):
            continue
        yield kind, m.group()
    yield "end", ""


def _unquote(raw: str) -> str:
    return re.sub(r"\\(.)", lambda m: _ESCAPES.get(m.group(1), m.group(1)), raw[1:-1])


def _word(raw: str):
    if raw == "true":
        return True
    if raw == "false":
        return False
    if raw == "null":
        return None
    if _NUMBER.match(raw):
        return float(raw) if re.search(r"[.eE]", raw) else int(raw)
    return raw


class _Parser:
    def __init__(self, text: str):
        self._it = _tokens(text)
        self._tok = next(self._it)

    def _next(self):
        tok = self._tok
        if tok[0] == "end":
            raise KV3Error("unexpected end of input")
        self._tok = next(self._it)
        return tok

    def value(self):
        kind, raw = self._next()
        if kind == "str":
            return _unquote(raw)
        if kind == "mstr":
            return raw[3:-3].strip("\n")
        if kind == "word":
            return _word(raw)
        if raw == "{":
            return self._object()
        if raw == "[":
            return self._array()
        raise KV3Error(f"unexpected token {raw!r}")

    def _object(self) -> dict:
        out = {}
        while True:
            kind, raw = self._next()
            if raw == "}" and kind == "punct":
                return out
            if kind == "str":
                key = _unquote(raw)
            elif kind == "word":
                key = raw
            else:
                raise KV3Error(f"expected a key, got {raw!r}")
            kind, raw = self._next()
            if raw != "=":
                raise KV3Error(f"expected '=' after key {key!r}, got {raw!r}")
            out[key] = self.value()

    def _array(self) -> list:
        out = []
        while True:
            kind, raw = self._tok
            if kind == "punct" and raw == "]":
                self._next()
                return out
            if kind == "punct" and raw == ",":
                self._next()
                continue
            if kind == "end":
                raise KV3Error("unterminated array")
            out.append(self.value())


def loads(text: str):
    parser = _Parser(text)
    value = parser.value()
    if parser._tok[0] != "end":
        raise KV3Error(f"trailing content: {parser._tok[1]!r}")
    return value


def load(path):
    with open(path, encoding="utf-8") as fh:
        return loads(fh.read())
