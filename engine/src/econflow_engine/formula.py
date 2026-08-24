# SPDX-License-Identifier: AGPL-3.0-only
"""SECURITY. The default-deny allowlist for the ``formula`` argument kind.

WHY IT EXISTS: the same formula string travels browser -> backend -> engine, and
a formula is the one argument kind that carries executable structure rather than
a value. This IS the gate -- there is no second one behind it, so a malicious or
model-generated payload rejected here is rejected for good. The canonical attack
recorded against the panel-data methods, ``y ~ system('rm -rf /')``, MUST be
rejected.

PRINCIPLE: DEFAULT-DENY. Anything not explicitly on the allowlist is rejected. No
denylist, no ``eval``, no Unicode normalisation (a homoglyph ``lοg`` is NOT
``log`` and must be rejected).

FIDELITY TO THE GRAMMAR. A formula is a documented syntax with a documented
parser, and these limits are the parser's, MEASURED on the reference
implementation at version 4.6.1 rather than recalled. They are recorded because
they are the only justification for the exact numbers below:

* the reference parser raises ``contextstack overflow`` once 50 bracket contexts are open
  SIMULTANEOUSLY (49 -> OK, 50 -> parse error). ``[[`` pushes TWO contexts (24
  nested ``[[`` -> OK, 25 -> parse error). ``~`` and a parenthesis-free ``if`` do
  not push.
* the walk's depth limit of 64 is reachable through left-associative chains that
  open no brackets: ``y ~ x + x + ...`` with 64 terms -> ACCEPT, 65 -> depth.
* a string in CALL-HEAD position is turned into a symbol by the reference parser:
  ``y ~ "log"(x)`` -> ACCEPT, ``y ~ "system"(x)`` -> denied-call.
* ``NULL`` and complex literals (``1i``) are neither numeric, logical nor
  character -> "disallowed term type" (the exporter classifies this as ``other``).

DELIBERATELY STRICTER THAN THE GRAMMAR -- raw strings, ``r"(...)"``: the tokenizer
does not support them, so ANY input containing one comes out as ``formula-parse``.
The rejection is P1-safe, raw strings are meaningless inside a formula, and no
corpus input contains one. Adding raw-string support to a parser that IS a
SECURITY BOUNDARY, merely to align one reason code, is disproportionate risk.
"""

from __future__ import annotations

import unicodedata
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal

from econflow_engine.mcp.allowlists import FORMULA_ALLOWED_CALLS, FORMULA_MAX_DEPTH

__all__ = [
    "FORMULA_MAX_PARSE_NESTING",
    "FormulaReasonCode",
    "FormulaResult",
    "validate_formula",
]

_ALLOWED_CALL_SET: frozenset[str] = frozenset(FORMULA_ALLOWED_CALLS)

#: The reference parser's simultaneous-bracket-context ceiling (49 -> OK, 50 -> error).
FORMULA_MAX_PARSE_NESTING = 49

FormulaReasonCode = Literal[
    "formula-not-string",
    "formula-parse",
    "formula-multi-expr",
    "formula-not-tilde",
    "formula-denied-call",
    "formula-bad-head",
    "formula-bad-var",
    "formula-depth",
    "other",
]


@dataclass(frozen=True, slots=True)
class FormulaResult:
    """Outcome of the allowlist walk. ``reason_code`` is set iff ``ok`` is false."""

    ok: bool
    reason_code: FormulaReasonCode | None = None
    message: str | None = None


_OK = FormulaResult(ok=True)


class _FormulaError(Exception):
    def __init__(self, reason_code: FormulaReasonCode, message: str) -> None:
        super().__init__(message)
        self.reason_code: FormulaReasonCode = reason_code
        self.message = message


def _parse_error(detail: str) -> _FormulaError:
    return _FormulaError("formula-parse", f"formula: cannot parse -- {detail}")


# ----------------------------------------------------------------------------
# AST
# ----------------------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class _Lit:
    """A numeric / logical literal -- always an allowed term."""


@dataclass(frozen=True, slots=True)
class _Bad:
    """NULL or a complex literal: not numeric, logical or character."""


@dataclass(frozen=True, slots=True)
class _Str:
    v: str


@dataclass(frozen=True, slots=True)
class _Sym:
    v: str


@dataclass(frozen=True, slots=True)
class _Call:
    head: _Node
    args: tuple[_Node, ...]
    fn_call: bool = False


_Node = _Lit | _Bad | _Str | _Sym | _Call

_LIT = _Lit()
_BAD = _Bad()


# ----------------------------------------------------------------------------
# Tokenizer
# ----------------------------------------------------------------------------


def _is_id_start(c: str) -> bool:
    """``[\\p{L}\\p{Nl}.]`` -- the identifier-start class."""
    cat = unicodedata.category(c)
    return cat[0] == "L" or cat == "Nl" or c == "."


def _is_id_cont(c: str) -> bool:
    """``[\\p{L}\\p{N}._]`` -- the identifier-continuation class."""
    cat = unicodedata.category(c)
    return cat[0] in ("L", "N") or c in "._"


_MULTI_OPS: tuple[str, ...] = (
    "<<-",
    "->>",
    ":::",
    "<-",
    "->",
    "<=",
    ">=",
    "==",
    "!=",
    "&&",
    "||",
    "::",
    "|>",
    "[[",
)
_SINGLE_OPS = "+-*/^~?!<>=:$@()[]{},;|&\\"


@dataclass(frozen=True, slots=True)
class _Tok:
    t: Literal["num", "str", "sym", "op", "eof"]
    v: str
    nl: bool
    complex: bool = False


def _tokenize(src: str) -> list[_Tok]:  # noqa: C901 - a tokenizer is one flat dispatch
    toks: list[_Tok] = []
    i = 0
    nl = False
    n = len(src)

    while i < n:
        c = src[i]
        if c == "\n":
            nl = True
            i += 1
            continue
        if c in " \t\f":
            i += 1
            continue
        if c == "#":
            while i < n and src[i] != "\n":
                i += 1
            continue
        if c in ('"', "'"):
            j = i + 1
            closed = False
            val = ""
            while j < n:
                d = src[j]
                if d == "\\":
                    val += src[j + 1] if j + 1 < n else ""
                    j += 2
                    continue
                if d == c:
                    closed = True
                    j += 1
                    break
                val += d
                j += 1
            if not closed:
                raise _parse_error("unexpected end of input (unterminated string)")
            toks.append(_Tok("str", val, nl))
            nl = False
            i = j
            continue
        if c == "`":
            j = i + 1
            closed = False
            val = ""
            while j < n:
                d = src[j]
                if d == "\\":
                    val += src[j + 1] if j + 1 < n else ""
                    j += 2
                    continue
                if d == "`":
                    closed = True
                    j += 1
                    break
                val += d
                j += 1
            if not closed:
                raise _parse_error("unexpected end of input (unterminated `name`)")
            toks.append(_Tok("sym", val, nl))
            nl = False
            i = j
            continue
        if c.isdigit() or (c == "." and i + 1 < n and src[i + 1].isdigit()):
            j, is_complex = _scan_number(src, i, n)
            toks.append(_Tok("num", src[i:j], nl, is_complex))
            nl = False
            i = j
            continue
        if _is_id_start(c):
            j = i + 1
            while j < n and _is_id_cont(src[j]):
                j += 1
            toks.append(_Tok("sym", src[i:j], nl))
            nl = False
            i = j
            continue
        if c == "%":
            close = src.find("%", i + 1)
            nl_pos = src.find("\n", i + 1)
            if close < 0 or (nl_pos >= 0 and nl_pos < close):
                raise _parse_error("unexpected '%' (unterminated %operator%)")
            toks.append(_Tok("op", src[i : close + 1], nl))
            nl = False
            i = close + 1
            continue
        multi = next((op for op in _MULTI_OPS if src.startswith(op, i)), None)
        if multi is not None:
            toks.append(_Tok("op", multi, nl))
            nl = False
            i += len(multi)
            continue
        if c in _SINGLE_OPS:
            toks.append(_Tok("op", c, nl))
            nl = False
            i += 1
            continue
        raise _parse_error(f"unexpected {c!r}")

    toks.append(_Tok("eof", "", nl))
    return toks


def _scan_number(src: str, i: int, n: int) -> tuple[int, bool]:
    """Return ``(end_index, is_complex)`` for the numeric literal starting at ``i``."""
    j = i
    is_complex = False
    if src[i] == "0" and i + 1 < n and src[i + 1] in "xX":
        j = i + 2
        while j < n and src[j] in "0123456789abcdefABCDEF":
            j += 1
    else:
        while j < n and src[j].isdigit():
            j += 1
        if j < n and src[j] == ".":
            j += 1
            while j < n and src[j].isdigit():
                j += 1
        if j < n and src[j] in "eE":
            k = j + 1
            if k < n and src[k] in "+-":
                k += 1
            if k < n and src[k].isdigit():
                j = k
                while j < n and src[j].isdigit():
                    j += 1
    if j < n and src[j] == "L":
        j += 1
    elif j < n and src[j] == "i":
        is_complex = True
        j += 1
    return j, is_complex


# ----------------------------------------------------------------------------
# Parser -- Pratt, with the grammar's binding powers
# ----------------------------------------------------------------------------

_INFIX_BP: dict[str, int] = {
    "?": 1,
    "=": 2,
    "<-": 3,
    "<<-": 3,
    "->": 4,
    "->>": 4,
    "~": 5,
    "||": 6,
    "|": 6,
    "&&": 7,
    "&": 7,
    "==": 9,
    "!=": 9,
    "<": 9,
    ">": 9,
    "<=": 9,
    ">=": 9,
    "+": 10,
    "-": 10,
    "*": 11,
    "/": 11,
    "|>": 12,
    ":": 13,
    "^": 15,
    "$": 16,
    "@": 16,
    "::": 17,
    ":::": 17,
}
_RIGHT_ASSOC = frozenset({"^", "<-", "<<-", "="})
_BP_SPECIAL_OP = 12
_NAME_RHS_OPS = frozenset({"::", ":::", "$", "@"})
_NON_ASSOC_OPS = frozenset({"==", "!=", "<", ">", "<=", ">="})
_POSTFIX_BP = 18
_BP_UNARY_NOT = 8
_BP_UNARY_SIGN = 14
_BP_UNARY_TILDE = 5
_BP_UNARY_HELP = 1
_BP_ARG = 3

_RESERVED_LITERALS = frozenset(
    {"TRUE", "FALSE", "Inf", "NaN", "NA", "NA_integer_", "NA_real_", "NA_character_"}
)
_RESERVED_WORDS = frozenset(
    {"if", "else", "repeat", "while", "function", "for", "in", "next", "break"}
)

_EOF = _Tok("eof", "", False)


def _is_reserved_word(v: str) -> bool:
    return v in _RESERVED_LITERALS or v in _RESERVED_WORDS or v in ("NULL", "NA_complex_")


class _Parser:
    __slots__ = ("_nl_sig", "_open", "_pos", "_toks")

    def __init__(self, toks: list[_Tok]) -> None:
        self._toks = toks
        self._pos = 0
        self._open = 0
        self._nl_sig = True

    # -- token access ---------------------------------------------------

    def _peek(self) -> _Tok:
        return self._toks[self._pos] if self._pos < len(self._toks) else _EOF

    def _next(self) -> _Tok:
        t = self._peek()
        if t.t != "eof":
            self._pos += 1
        return t

    def _expect_op(self, v: str) -> None:
        t = self._peek()
        if t.t != "op" or t.v != v:
            seen = "end of input" if t.t == "eof" else t.v
            raise _parse_error(f"unexpected {seen!r} (expected {v!r})")
        self._pos += 1

    def _push(self, k: int) -> None:
        self._open += k
        if self._open > FORMULA_MAX_PARSE_NESTING:
            raise _parse_error("contextstack overflow")

    def _pop(self, k: int) -> None:
        self._open -= k

    # -- grammar --------------------------------------------------------

    def parse_program(self) -> list[_Node]:
        out: list[_Node] = []
        while True:
            t = self._peek()
            if t.t == "eof":
                break
            if t.t == "op" and t.v == ";":
                raise _parse_error("unexpected ';'")
            out.append(self._parse_expr(0))
            after = self._peek()
            if after.t == "eof":
                break
            if after.t == "op" and after.v == ";":
                self._pos += 1
                continue
            if after.nl:
                continue
            raise _parse_error(f"unexpected {after.v!r}")
        return out

    def _parse_expr(self, min_bp: int, stop_at_eq: bool = False) -> _Node:  # noqa: C901
        left = self._parse_prefix()
        while True:
            t = self._peek()
            if t.t != "op":
                break
            if self._nl_sig and t.nl:
                break
            if stop_at_eq and t.v == "=":
                break
            if t.v in ("(", "[", "[["):
                if min_bp > _POSTFIX_BP:
                    break
                left = self._parse_postfix(left, t.v)
                continue
            bp = _BP_SPECIAL_OP if t.v.startswith("%") else _INFIX_BP.get(t.v)
            if bp is None or bp < min_bp:
                break
            self._pos += 1
            if t.v in _NAME_RHS_OPS:
                left = _Call(_Sym(t.v), (left, self._parse_name_rhs(t.v, left)))
                continue
            right_min = bp if t.v in _RIGHT_ASSOC else bp + 1
            right = self._parse_expr(right_min)
            if t.v == "|>":
                if not isinstance(right, _Call) or not right.fn_call:
                    raise _parse_error("the pipe operator requires a function call as RHS")
                left = _Call(right.head, (left, *right.args), True)
                continue
            left = _Call(_Sym(t.v), (left, right))
            if t.v in _NON_ASSOC_OPS:
                nxt = self._peek()
                if nxt.t == "op" and nxt.v in _NON_ASSOC_OPS:
                    raise _parse_error(f"unexpected {nxt.v!r}")
        return left

    def _is_named_arg_start(self) -> bool:
        if self._pos + 1 >= len(self._toks):
            return False
        a = self._toks[self._pos]
        b = self._toks[self._pos + 1]
        if b.t != "op" or b.v != "=":
            return False
        if a.t == "str":
            return True
        return a.t == "sym" and not _is_reserved_word(a.v)

    def _parse_name_rhs(self, op: str, left: _Node) -> _Node:
        if op in ("::", ":::") and not isinstance(left, _Sym | _Str):
            raise _parse_error(f"unexpected {op!r}")
        r = self._peek()
        if r.t == "sym" and not _is_reserved_word(r.v):
            self._pos += 1
            return _Sym(r.v)
        if r.t == "str":
            self._pos += 1
            return _Str(r.v)
        seen = "end of input" if r.t == "eof" else r.v
        raise _parse_error(f"unexpected {seen!r} after {op!r}")

    def _parse_postfix(self, head: _Node, opener: str) -> _Node:
        # A string in call-head position is turned into a symbol by the reference parser.
        h: _Node = _Sym(head.v) if opener == "(" and isinstance(head, _Str) else head
        if opener == "(":
            return _Call(h, tuple(self._parse_args(1, ")")), True)
        if opener == "[":
            return _Call(_Sym("["), (h, *self._parse_args(1, "]")))
        return _Call(_Sym("[["), (h, *self._parse_args(2, "]", 2)))

    def _parse_args(self, weight: int, closer: str, close_count: int = 1) -> list[_Node]:
        self._pos += 1  # consume the opener
        self._push(weight)
        saved_nl = self._nl_sig
        self._nl_sig = False
        args: list[_Node] = []

        def at_closer() -> bool:
            t = self._peek()
            return t.t == "op" and t.v == closer

        def at_end() -> bool:
            t = self._peek()
            return t.t == "eof" or (t.t == "op" and t.v in (",", closer))

        if not at_closer():
            while True:
                if at_end():
                    args.append(_Sym(""))  # empty argument, e.g. x[, 1]
                elif self._is_named_arg_start():
                    self._pos += 2  # name and '='
                    args.append(_Sym("") if at_end() else self._parse_expr(0, True))
                else:
                    args.append(self._parse_expr(0, True))
                    eq = self._peek()
                    if eq.t == "op" and eq.v == "=":
                        raise _parse_error("unexpected '='")
                sep = self._peek()
                if sep.t == "op" and sep.v == ",":
                    self._pos += 1
                    continue
                break

        for _ in range(close_count):
            self._expect_op(closer)
        self._pop(weight)
        self._nl_sig = saved_nl
        return args

    def _parse_braced(self) -> _Node:
        self._pos += 1  # '{'
        self._push(1)
        saved_nl = self._nl_sig
        self._nl_sig = True  # inside `{ }` a newline SEPARATES statements
        stmts: list[_Node] = []
        while True:
            t = self._peek()
            if t.t == "eof":
                raise _parse_error("unexpected end of input (expected '}')")
            if t.t == "op" and t.v == "}":
                break
            if t.t == "op" and t.v == ";":
                self._pos += 1
                continue
            stmts.append(self._parse_expr(0))
        self._expect_op("}")
        self._pop(1)
        self._nl_sig = saved_nl
        return _Call(_Sym("{"), tuple(stmts))

    def _parse_paren(self) -> _Node:
        self._pos += 1  # '('
        self._push(1)
        saved_nl = self._nl_sig
        self._nl_sig = False
        e = self._parse_expr(0)
        self._expect_op(")")
        self._pop(1)
        self._nl_sig = saved_nl
        return _Call(_Sym("("), (e,))

    def _parse_prefix(self) -> _Node:  # noqa: C901 - one flat dispatch as in the grammar
        t = self._next()
        if t.t == "eof":
            raise _parse_error("unexpected end of input")
        if t.t == "num":
            return _BAD if t.complex else _LIT
        if t.t == "str":
            return _Str(t.v)
        if t.t == "sym":
            if t.v in ("NULL", "NA_complex_"):
                return _BAD
            if t.v in _RESERVED_LITERALS:
                return _LIT
            if t.v == "if":
                return self._parse_if()
            if t.v == "for":
                return self._parse_for()
            if t.v == "while":
                return self._parse_while()
            if t.v == "repeat":
                return _Call(_Sym("repeat"), (self._parse_expr(0),))
            if t.v == "function":
                return self._parse_function()
            if t.v in ("next", "break"):
                return _Call(_Sym(t.v), ())
            if t.v in _RESERVED_WORDS:
                raise _parse_error(f"unexpected {t.v!r}")
            return _Sym(t.v)
        # t.t == "op"
        if t.v == "(":
            self._pos -= 1
            return self._parse_paren()
        if t.v == "{":
            self._pos -= 1
            return self._parse_braced()
        if t.v in ("-", "+"):
            return _Call(_Sym(t.v), (self._parse_expr(_BP_UNARY_SIGN),))
        if t.v == "!":
            return _Call(_Sym("!"), (self._parse_expr(_BP_UNARY_NOT),))
        if t.v == "~":
            return _Call(_Sym("~"), (self._parse_expr(_BP_UNARY_TILDE + 1),))
        if t.v == "?":
            return _Call(_Sym("?"), (self._parse_expr(_BP_UNARY_HELP),))
        if t.v == "\\":
            return self._parse_function()
        raise _parse_error(f"unexpected {t.v!r}")

    def _parse_control_cond(self) -> _Node:
        self._expect_op("(")
        self._push(1)
        saved_nl = self._nl_sig
        self._nl_sig = False
        cond = self._parse_expr(0)
        self._expect_op(")")
        self._pop(1)
        self._nl_sig = saved_nl
        return cond

    def _parse_if(self) -> _Node:
        cond = self._parse_control_cond()
        body = self._parse_expr(0)
        t = self._peek()
        if t.t == "sym" and t.v == "else":
            self._pos += 1
            return _Call(_Sym("if"), (cond, body, self._parse_expr(0)))
        return _Call(_Sym("if"), (cond, body))

    def _parse_for(self) -> _Node:
        self._expect_op("(")
        self._push(1)
        saved_nl = self._nl_sig
        self._nl_sig = False
        v = self._next()
        if v.t != "sym":
            raise _parse_error("unexpected token in for(...)")
        in_tok = self._next()
        if in_tok.t != "sym" or in_tok.v != "in":
            raise _parse_error("expected 'in' in for(...)")
        seq = self._parse_expr(0)
        self._expect_op(")")
        self._pop(1)
        self._nl_sig = saved_nl
        return _Call(_Sym("for"), (_Sym(v.v), seq, self._parse_expr(0)))

    def _parse_while(self) -> _Node:
        cond = self._parse_control_cond()
        return _Call(_Sym("while"), (cond, self._parse_expr(0)))

    def _parse_function(self) -> _Node:
        self._expect_op("(")
        self._push(1)
        saved_nl = self._nl_sig
        self._nl_sig = False
        defaults: list[_Node] = []
        while True:
            t = self._peek()
            if t.t == "op" and t.v == ")":
                break
            p = self._next()
            if p.t != "sym":
                raise _parse_error("invalid formal in function(...)")
            eq = self._peek()
            if eq.t == "op" and eq.v == "=":
                self._pos += 1
                defaults.append(self._parse_expr(_BP_ARG))
            sep = self._peek()
            if sep.t == "op" and sep.v == ",":
                self._pos += 1
                continue
            break
        self._expect_op(")")
        self._pop(1)
        self._nl_sig = saved_nl
        return _Call(_Sym("function"), (*defaults, self._parse_expr(0)))


# ----------------------------------------------------------------------------
# The allowlist walk
# ----------------------------------------------------------------------------


def _validate_lang(expr: _Node, allowed_vars: tuple[str, ...] | None, depth: int) -> None:
    if depth > FORMULA_MAX_DEPTH:
        raise _FormulaError(
            "formula-depth", "formula: excessive expression depth (possible malicious input)."
        )
    if isinstance(expr, _Lit | _Str):
        return
    if isinstance(expr, _Sym):
        if expr.v == ".":
            return  # '.' = every variable (formula shorthand)
        if allowed_vars is not None and expr.v and expr.v not in allowed_vars:
            raise _FormulaError(
                "formula-bad-var", f"formula: disallowed/unknown variable '{expr.v}'."
            )
        return
    if isinstance(expr, _Call):
        if not isinstance(expr.head, _Sym):
            raise _FormulaError(
                "formula-bad-head",
                "formula: disallowed call (the head is not a plain symbol -- "
                "pkg::fn and (fn)() are rejected).",
            )
        if expr.head.v not in _ALLOWED_CALL_SET:
            raise _FormulaError(
                "formula-denied-call",
                f"formula: disallowed function/operator '{expr.head.v}' (default-deny allowlist).",
            )
        for a in expr.args:
            _validate_lang(a, allowed_vars, depth + 1)
        return
    raise _FormulaError("other", "formula: disallowed term type in the expression.")


def validate_formula(s: object, allowed_vars: Sequence[str] | None = None) -> FormulaResult:
    """Validate an the grammar formula string against the default-deny allowlist.

    ``allowed_vars`` restricts the admissible symbols; ``None`` means every symbol
    that survives the call allowlist is accepted.
    """
    if not isinstance(s, str) or len(s) == 0:
        return FormulaResult(
            ok=False,
            reason_code="formula-not-string",
            message='formula: must be a formula or a non-empty string (e.g. "y ~ x1 + x2").',
        )
    vars_ = None if allowed_vars is None else tuple(str(v) for v in allowed_vars)

    try:
        exprs = _Parser(_tokenize(s)).parse_program()
    except _FormulaError as e:
        return FormulaResult(ok=False, reason_code=e.reason_code, message=e.message)

    if len(exprs) != 1:
        return FormulaResult(
            ok=False,
            reason_code="formula-multi-expr",
            message="formula: must contain EXACTLY one expression (no ';', no multiples).",
        )
    lang = exprs[0]
    if not (isinstance(lang, _Call) and isinstance(lang.head, _Sym) and lang.head.v == "~"):
        return FormulaResult(
            ok=False,
            reason_code="formula-not-tilde",
            message='formula: must be a formula with \'~\' (e.g. "y ~ x1 + x2").',
        )
    try:
        _validate_lang(lang, vars_, 0)
    except _FormulaError as e:
        return FormulaResult(ok=False, reason_code=e.reason_code, message=e.message)
    return _OK
