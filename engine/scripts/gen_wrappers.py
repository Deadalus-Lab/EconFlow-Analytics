#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
"""node-specs + method-cards -> src/econflow_engine/wrappers/**.

Emits, from BOTH committed artifacts:

    wrappers/<category-package>/<module>.py   598 modules, one per wrapper file

Unlike the generated schema tier these files ARE committed: the stubs are filled
in by hand, one method at a time.

NAMING (verified over all 598 wrapper files: zero collisions, every name a valid
identifier):

    category "00-data-utilities"                        -> package c00_data_utilities
THE N:1 CASES: two wrapper files are each governed by TWO cards --
``c08_panel_data/static_panel_estimators.py`` (#46 static estimators, #47
dynamic GMM) and ``c07_causality_policy/staggered_did.py``. Each yields ONE
module carrying the tool functions of both, never two.

TWO GENERATED REGIONS PER MODULE; EVERYTHING ELSE BELONGS TO THE AUTHOR.

    # --- gen_wrappers: header begin ---   SPDX, docstring, imports, __all__
    # --- gen_wrappers: header end ---

    def fn(*, ...) -> dict[str, Any]:
        \"\"\"Node ``fn`` -- method card #N.
        ... Args: / Returns: / Gates: / Validation: <- generated
        .. gen_wrappers: end of generated docstring
        Examples:                                    <- the author's
        Note:                                        <- the author's
        \"\"\"
        <body>                                       <- the author's

THE PER-FUNCTION BOUNDARY IS A SENTINEL INSIDE THE DOCSTRING, because a
docstring cannot be split into two docstrings. ``.. `` opens a reStructuredText
comment, so the line renders as a comment rather than as text, and doctest never
matches it -- it looks only for a line whose first non-space characters are
``>>>``. Both were measured rather than recalled: docutils 0.23 renders the line
as an HTML comment, and ``doctest.DocTestParser`` finds zero examples in a stub
docstring against one in a control.

Keeping the sentinel INSIDE the docstring is also what preserves interrogate's
count. ``run_verifications.sh`` step 7 asserts that nothing under wrappers/ is
undocumented and that the number of documentable objects stays at or above
``engine.methods``; closing the docstring early would leave 1456 objects
undocumented while interrogate went on printing 100.0 %, because that percentage
is rounded to one decimal before it is compared with the floor.

Modes:
    --init   create what is missing; NEVER overwrite an existing file.
    --check  assert every expected module exists, that every stub signature
             still matches node-specs, and that the TEXT of every generated
             region is the text this generator emits; exit 1 on drift. The
             region comparison is textual because a marker is a comment, and
             comments do not survive into an abstract syntax tree.
    --write  re-derive every generated region in place, never touching a byte
             after a sentinel or after a docstring's closing quotes. A module
             carrying no marker region can only be rewritten whole, and that
             path is still refused for any module holding a written body.
    --scaffold-tests MODULE [--out PATH]
             emit the four mandatory test classes for one wrapper module, on
             stdout or to PATH. A FOURTH MODE rather than a fifth generator:
             ``engine.generators`` is an exact-equality constant and ci.yml
             runs a hand-named loop over four generators, every one of which
             answers ``--check`` against committed bytes. A test scaffolder has
             no committed output to re-derive.
"""

from __future__ import annotations

import argparse
import ast
import functools
import json
import keyword
import sys
from pathlib import Path
from typing import Any

ENGINE_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ENGINE_ROOT / "src"))

from econflow_engine.metrics import find_manifest, is_stub  # noqa: E402  (after sys.path)
from econflow_engine.naming import (  # noqa: E402  (after sys.path)
    category_package,
    python_arg_name,
    wrapper_module_name,
)

ARTIFACTS = ENGINE_ROOT / "artifacts"
OUT_ROOT = ENGINE_ROOT / "src" / "econflow_engine" / "wrappers"
METHOD_SOURCES = ENGINE_ROOT / "METHOD-SOURCES.json"
INVENTORY = find_manifest(Path(__file__))

# THE THREE MARKERS. Changing any of these strings is a tree-wide migration and
# not an edit: every committed module carries them, and tests/test_gen_wrappers.py
# keeps an independent copy so a marker changed on one side is caught by
# disagreement between two homes rather than believed on the word of one.
HEADER_BEGIN = "# --- gen_wrappers: header begin ---"
HEADER_END = "# --- gen_wrappers: header end ---"
DOCSTRING_END = ".. gen_wrappers: end of generated docstring"

# The scaffold plants this in every test it emits, and a committed test still
# carrying it is refused: 598 unfilled scaffolds would raise suite.min_tests by
# several thousand while asserting nothing about any method.
SCAFFOLD_MARKER = "TODO(2.2)"

_SOURCES: dict[str, Any] | None = None


def inventory_constant(section: str, key: str) -> int:
    """One asserted constant, from the one file that holds them all.

    NO DEFAULT and no except-and-return-zero. A denominator that cannot be read
    means this gate has not started, and a gate that has not started must never
    be reported as a gate that passed.
    """
    try:
        return int(json.loads(INVENTORY.read_text(encoding="utf-8"))[section][key])
    except (OSError, KeyError, ValueError, TypeError) as exc:
        raise SystemExit(
            f"gen_wrappers: cannot read {section}.{key} from {INVENTORY}: {exc}"
        ) from exc


def emitted(source: str, label: str) -> str:
    """Every byte this generator writes or prints, parsed before it leaves.

    THE BOUNDARY THIS ENFORCES: prose goes through ``_wrap``, emitted Python
    never does. Applied to a call, ``_wrap`` splits the string literal across
    lines and produces source Python cannot read -- which is what it did here,
    and what this refuses. A generator able to emit invalid Python and not
    notice is the same failure shape as a gate that examines nothing.
    """
    try:
        ast.parse(source)
    except SyntaxError as exc:
        raise SystemExit(f"gen_wrappers: emitted invalid Python for {label}: {exc}") from exc
    return source


def method_sources() -> dict[str, Any]:
    """The implementation-source register, read once.

    Prose about WHICH library implements a module comes from here and never from
    the sealed cards. The cards record how the catalogue was SELECTED; this file
    records how it is being BUILT, and only the second changes as work proceeds.
    """
    global _SOURCES
    if _SOURCES is None:
        if not METHOD_SOURCES.is_file():
            raise SystemExit(f"gen_wrappers: {METHOD_SOURCES} is absent; it is the register.")
        _SOURCES = json.loads(METHOD_SOURCES.read_text(encoding="utf-8"))["modules"]
    return _SOURCES


def reference_implementation(package: str, module: str) -> str:
    """One line naming the library, the paper or the dataset a module is built from.

    The register's contract is enforced HERE rather than trusted: a row naming
    more than one of the three, or missing entirely, stops the generation. A row
    that names none of them is not an error -- it is the honest 'planned' state,
    and saying so is better than a docstring that points the reader at nothing.

    A DATASET IS CREDITED TO ITS PUBLISHER AND NOT TO ITS DIGEST. The row carries
    the SHA-256 of the committed snapshot, which is what identifies the bytes;
    what a reader of the docstring needs is who published the table, and the
    register is one line away for the rest.
    """
    row = method_sources().get(f"{package}/{module}")
    if row is None:
        raise SystemExit(f"gen_wrappers: {package}/{module} has no row in METHOD-SOURCES.json")
    library, paper, dataset = row.get("library"), row.get("paper"), row.get("dataset")
    if sum(bool(x) for x in (library, paper, dataset)) > 1:
        raise SystemExit(
            f"gen_wrappers: {package}/{module} names more than one of a library, a "
            "paper and a dataset; the register admits exactly one."
        )
    if library:
        return str(library)
    if paper:
        return str(paper)
    if dataset:
        return (f"a committed dataset snapshot published by {dataset['publisher']}; "
                "see engine/METHOD-SOURCES.json")
    return "not yet selected; see engine/METHOD-SOURCES.json"
LINE_LIMIT = 100

# REUSE-IgnoreStart -- the line below is EMITTED INTO GENERATED OUTPUT, not a
# declaration about this file. reuse reads the tag wherever it appears, sees the
# surrounding quotes and escapes as part of the expression, and reports it as an
# invalid SPDX expression. This file's own licence is declared at the top.
SPDX = "# SPDX-License-Identifier: AGPL-3.0-only"
# REUSE-IgnoreEnd

# kind -> the Python type a wrapper actually receives.
#
# The handle kinds are where the contract's time-series representations collapse:
# pandas has ONE. `resolve_handle` in `econflow_engine.mcp.adapters` is the single
# place that materialises a pointer into these types, and this table is its
# contract as seen from the wrapper side.
_SCALAR_TYPES: dict[str, str] = {
    "integer": "int",
    "number": "float",
    "boolean": "bool",
    "string": "str",
    "formula": "str",
    "path": "str",
    "raw": "Any",
    "raw_handle": "Any",
    "series_codes": "Sequence[str]",
    "int_array": "Sequence[int]",
    "num_array": "Sequence[float]",
    "raw_handle_array": "Sequence[Any]",
    "series_handle": "pd.Series",
    "irregular_series_handle": "pd.Series",
    "multiseries_handle": "pd.DataFrame",
    "df_handle": "pd.DataFrame",
    "matrix_handle": "np.ndarray",
    "exog_handle": "np.ndarray",
}


# Cached because --scaffold-tests reads the 3 MB card artifact once per module,
# and the line-limit sweep over all 598 asks for it 598 times. Nothing here
# mutates what an artifact returns.
@functools.cache
def read_artifact(name: str) -> Any:
    return json.loads((ARTIFACTS / name).read_bytes().decode("utf-8"))


# ---------------------------------------------------------------------------
# Signature derivation
# ---------------------------------------------------------------------------


def annotation_for(arg: dict[str, Any], forecastfn_names: tuple[str, ...]) -> str:
    kind = arg["kind"]
    if kind == "enum":
        return "Literal[" + ", ".join(json.dumps(v) for v in arg["enum"]) + "]"
    if kind == "forecastfn_enum":
        return "Literal[" + ", ".join(json.dumps(v) for v in forecastfn_names) + "]"
    try:
        return _SCALAR_TYPES[kind]
    except KeyError as exc:  # pragma: no cover - the vocabulary is closed
        raise SystemExit(f"gen_wrappers: no Python type for kind {kind!r}.") from exc


def render_param(arg: dict[str, Any], forecastfn_names: tuple[str, ...]) -> list[str]:
    """One parameter, wrapped across lines only when it would exceed the limit."""
    name = python_arg_name(arg["name"])
    ann = annotation_for(arg, forecastfn_names)
    optional = not arg["required"]
    tail = " | None = None," if optional else ","
    single = f"    {name}: {ann}{tail}"
    if len(single) <= LINE_LIMIT:
        return [single]
    if not ann.startswith("Literal["):  # pragma: no cover - only enums are long
        raise SystemExit(f"gen_wrappers: cannot wrap the annotation of {arg['name']!r}.")
    values = ann[len("Literal[") : -1].split(", ")
    lines = [f"    {name}: ("]
    lines.append("        Literal[")
    lines += [f"            {v}," for v in values]
    lines.append("        ]")
    if optional:
        lines.append("        | None")
    lines.append("    ) = None," if optional else "    ),")
    return lines


def gates_section(card: dict[str, Any]) -> list[str]:
    """The Gates section, rendered from the card's ``precondition_gates`` field.

    DATA, NOT CODE. Nothing here imports or consults the gate registry: the two
    are built independently, and a code dependency would couple two changes that
    each have to be green on their own. The field is empty on nearly every card,
    and the section says so in words rather than being omitted -- an absent
    section reads as "this method needs no precondition", which is a claim
    nobody has made.
    """
    lines = ["", "    Gates:"]
    declared = card.get("precondition_gates") or []
    if not declared:
        return lines + _wrap(
            "None declared. The ``precondition_gates`` field of this method card is empty; "
            "the checks a body must run are named here once the field carries them.",
            "        ",
        )
    lines += _wrap("Declared on the method card:", "        ")
    lines.append("")
    for entry in declared:
        lines += _wrap(f"- {docsafe(str(entry))}", "        ", subsequent="          ")
    return lines


def validation_section(card: dict[str, Any]) -> list[str]:
    """The Validation section, rendered from the card's ``validation_notes``.

    EMITTED ONLY WHERE THE CARD HAS SOMETHING TO SAY, which is the opposite of
    the Gates section above and is deliberate. "No gate is declared" is a claim
    about a closed vocabulary and is worth writing down; "nobody wrote a note" is
    not a claim about anything, and a section saying so on 595 modules would say
    less each time it appeared.

    WHY THESE SENTENCES ARE NOT GATE NAMES AND CANNOT BECOME ONE. They describe
    filesystem state, argument grammar, membership against a list only the
    runtime knows, an ordering that is a security property, a post-condition and
    a default. Every gate primitive takes a numeric vector, a panel or one scalar
    parameter, so a vocabulary of them can name none of it -- and a refusal a
    user would otherwise meet undocumented is the thing this section carries.
    """
    notes = card.get("validation_notes") or []
    if not notes:
        return []
    lines = ["", "    Validation:"]
    lines += _wrap("Documented on the method card:", "        ")
    lines.append("")
    for note in notes:
        lines += _wrap(f"- {docsafe(str(note))}", "        ", subsequent="          ")
    return lines


def author_sections() -> list[str]:
    """Examples and Note: emitted once, then owned by whoever writes the body.

    NO ``>>>`` LINE IS EVER EMITTED FOR A STUB. Box 2.1.18 runs the suite under
    ``--doctest-modules``; an example against a body that raises
    NotImplementedError is a failure, and 1456 of them would arrive on the day
    that box lands. An example is written with the body, which is the only point
    at which one can be true.
    """
    return [
        "",
        "    Examples:",
        *_wrap(
            "None yet. This node raises ``NotImplementedError``; its example is written "
            "with its body and belongs to whoever writes it.",
            "        ",
        ),
        "",
        "    Note:",
        *_wrap(
            "The implementation note is written with the body: the library functions it "
            "calls and their versions, what the method leaves out, and every gate added "
            "with the source that requires it.",
            "        ",
        ),
    ]


def stub_source(
    node: dict[str, Any], card: dict[str, Any], forecastfn_names: tuple[str, ...]
) -> list[str]:
    fn = node["fn"]
    lines = [f"def {fn}("]
    if node["arguments"]:
        lines.append("    *,")
        for arg in node["arguments"]:
            lines += render_param(arg, forecastfn_names)
    lines.append(") -> dict[str, Any]:")

    lines.append(f'    """Node ``{fn}`` -- method card #{card["id"]}.')
    lines.append("")
    lines += _wrap(docsafe(card["method"]) + ".", "    ")
    lines.append("")
    lines += _wrap(
        f"Category {node['category']}; memory class ``{node['memory_class']}``.",
        "    ",
    )
    register = (node.get("register") or {}).get("field")
    if register is not None:
        lines.append("")
        lines += _wrap(
            f"Registers its result under ``{register}``, so a later node can consume it "
            "as a handle.",
            "    ",
        )
    status = node["executability"]["status"]
    if status != "executable":
        lines.append("")
        lines += _wrap(f"[{status}] {docsafe(node['executability']['reason'] or '')}", "    ")
    lines.append("")
    lines.append("    Args:")
    for arg in node["arguments"]:
        py = python_arg_name(arg["name"])
        wire = "" if py == arg["name"] else f" (wire name ``{arg['name']}``)"
        desc = docsafe((arg.get("description") or "").strip()) or "(no description in the spec)"
        req = "required" if arg["required"] else "optional"
        default = f" Default ``{arg['default']!r}``." if arg.get("has_default") else ""
        lines += _wrap(
            f"{py}{wire}: [{arg['kind']}, {req}] {desc}{default}",
            "        ",
            subsequent="            ",
        )
    lines.append("")
    lines.append("    Returns:")
    lines.append("        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.")
    lines += gates_section(card)
    lines += validation_section(card)
    lines.append("")
    lines.append(f"    {DOCSTRING_END}")
    lines += author_sections()
    lines.append('    """')
    # The message names no document: the card lives in engine/corpus/, which is a
    # source tree, not something a user of this package has on disk.
    lines.append("    raise NotImplementedError(")
    lines.append(f'        "{fn}: not implemented."')
    lines.append("    )")
    return lines


def _break_long_word(word: str, width: int) -> list[str]:
    """Split a token that cannot fit, preferring a natural separator.

    The artifact carries slash-separated option lists up to 97 characters long
    (``ols/str/csstr/...``). Breaking those at a ``/`` reads naturally; a hard cut
    is the last resort, so that NO emitted line can exceed the limit.
    """
    seps = "/|,;"
    chunks: list[str] = []
    rest = word
    while len(rest) > width:
        cut = max(rest.rfind(c, 0, width) for c in seps)
        cut = cut + 1 if cut > 0 else width
        chunks.append(rest[:cut])
        rest = rest[cut:]
    if rest:
        chunks.append(rest)
    return chunks


def _wrap(text: str, indent: str, subsequent: str | None = None) -> list[str]:
    """Greedy wrap; every emitted line is guaranteed to fit inside the limit."""
    cont = subsequent if subsequent is not None else indent
    width = LINE_LIMIT - len(cont)
    words: list[str] = []
    for raw in text.split():
        words += _break_long_word(raw, width) if len(raw) > width else [raw]
    if not words:
        return []
    out: list[str] = []
    current = indent + words[0]
    for word in words[1:]:
        candidate = f"{current} {word}"
        if len(candidate) > LINE_LIMIT:
            out.append(current)
            current = cont + word
        else:
            current = candidate
    out.append(current)
    return out


def docsafe(text: str) -> str:
    """Make artifact text safe to embed verbatim in a docstring.

    Three argument descriptions contain a literal backslash (an escaped newline,
    an escaped tab, a set-difference sign). Left alone they become invalid escape
    sequences and Python warns at import time; doubling them preserves exactly
    what the reader sees.
    """
    return text.replace(chr(92), chr(92) * 2).replace('"""', "'''")


def module_source(
    wrapper_file: str,
    cards: list[dict[str, Any]],
    nodes_by_fn: dict[str, dict[str, Any]],
    forecastfn_names: tuple[str, ...],
) -> str:
    category = cards[0]["category"]
    package = category_package(category)
    module = wrapper_module_name(wrapper_file)
    plural = "s" if len(cards) > 1 else ""
    ids = ", ".join(f"#{c['id']}" for c in cards)

    fns = [fn for card in cards for fn in card["tool_fns"]]
    card_of = {fn: card for card in cards for fn in card["tool_fns"]}

    kinds = {a["kind"] for fn in fns for a in nodes_by_fn[fn]["arguments"]}
    typing_names = ["Any"]
    if any(k in kinds for k in ("enum", "forecastfn_enum")):
        typing_names.append("Literal")
    needs_pandas = any(_SCALAR_TYPES.get(k, "").startswith("pd.") for k in kinds)
    needs_numpy = any(_SCALAR_TYPES.get(k, "").startswith("np.") for k in kinds)
    needs_sequence = any(_SCALAR_TYPES.get(k, "").startswith("Sequence") for k in kinds)
    if needs_pandas or needs_numpy:
        typing_names.append("TYPE_CHECKING")

    # The SPDX line sits INSIDE the region, so a header that lost it is re-derived
    # by --write rather than only reported by the spdx gate. Both SPDX gates read
    # the identifier wherever it appears in the file -- `grep -m1` in the
    # pre-commit hook, `grep -qm1` in ci.yml -- so nothing depends on it being the
    # first line, and REUSE.toml declares the whole tree with aggregate precedence.
    head = [
        HEADER_BEGIN,
        SPDX,
        f'"""Method wrapper ``{module}`` -- method card{plural} {ids}.',
        "",
    ]
    for card in cards:
        head += _wrap(f"#{card['id']} {docsafe(card['method'])}", "", subsequent="    ")
    head.append("")
    head += _wrap(f"Category {category}; module ``{module}``.", "")
    head.append("")
    head += _wrap(
        f"Reference implementation: {docsafe(reference_implementation(package, module))}.", ""
    )
    head.append("")
    head += _wrap(
        "See ``engine/corpus/`` for when this method applies, what to reach for "
        "instead, and the interpretation traps recorded against it.",
        "",
    )
    head += ['"""', "", "from __future__ import annotations", ""]
    if needs_sequence:
        head.append("from collections.abc import Sequence")
    # isort puts CONSTANT_CASE names first, so TYPE_CHECKING leads.
    ordered = sorted(typing_names, key=lambda n: (not n.isupper(), n))
    head.append(f"from typing import {', '.join(ordered)}")
    head += [
        "",
        f"from econflow_engine.generated.args.{package} import NODE_META, wire_model",
    ]
    if needs_pandas or needs_numpy:
        head += ["", "if TYPE_CHECKING:"]
        if needs_numpy:
            head.append("    import numpy as np")
        if needs_pandas:
            head.append("    import pandas as pd")
    head += [
        "",
        "# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and",
        "# read kinds and defaults from ``NODE_META[fn]`` without another import.",
        "__all__ = [",
    ]
    head += [f'    "{name}",' for name in [*sorted(fns), "NODE_META", "wire_model"]]
    head += ["]", "", HEADER_END, "", ""]

    body: list[str] = []
    for fn in fns:
        body += stub_source(nodes_by_fn[fn], card_of[fn], forecastfn_names)
        body += ["", ""]
    return "\n".join(head + body).rstrip("\n") + "\n"


# ---------------------------------------------------------------------------
# The generated regions
# ---------------------------------------------------------------------------


class SpliceError(Exception):
    """A file whose generated regions cannot be located.

    Never swallowed and never guessed past: the alternative to raising is
    editing the wrong span of somebody's file.
    """


def _header_span(lines: list[str], label: str) -> tuple[int, int]:
    begins = [i for i, line in enumerate(lines) if line.strip() == HEADER_BEGIN]
    ends = [i for i, line in enumerate(lines) if line.strip() == HEADER_END]
    if len(begins) != 1 or len(ends) != 1:
        raise SpliceError(
            f"{label}: expected exactly one header region, found "
            f"{len(begins)} begin and {len(ends)} end marker(s)"
        )
    if begins[0] >= ends[0]:
        raise SpliceError(f"{label}: the header end marker precedes its begin marker")
    return begins[0], ends[0]


def _function_span(lines: list[str], fn: str, label: str) -> tuple[int, int]:
    """The ``def`` line through the sentinel that closes the generated docstring.

    The search stops at the next module-level ``def``, so a function whose
    sentinel was deleted is reported rather than silently swallowing the
    function below it.
    """
    opening = f"def {fn}("
    start = next((i for i, line in enumerate(lines) if line.startswith(opening)), None)
    if start is None:
        raise SpliceError(f"{label}: '{fn}' has no module-level def")
    for i in range(start + 1, len(lines)):
        if lines[i].strip() == DOCSTRING_END:
            return start, i
        if lines[i].startswith("def "):
            break
    raise SpliceError(f"{label}: '{fn}' carries no '{DOCSTRING_END}' sentinel")


def generated_regions(
    text: str, fns: list[str], label: str
) -> tuple[list[str], list[tuple[str, tuple[int, int]]]]:
    """The lines of ``text`` and every span this generator owns, each named.

    ONE LOCATOR, run over both the file on disk and the freshly planned source,
    so the two can never be found by rules that differ. The names travel with the
    spans because a drift report has to say WHICH region moved.
    """
    lines = text.split("\n")
    named = [("the header", _header_span(lines, label))]
    named += [
        (f"the generated docstring of '{fn}'", _function_span(lines, fn, label)) for fn in fns
    ]
    ordered = sorted(span for _, span in named)
    for (_, end), (start, _) in zip(ordered, ordered[1:], strict=False):
        if start <= end:
            raise SpliceError(f"{label}: two generated regions overlap")
    return lines, named


def splice(current: str, planned: str, fns: list[str], label: str) -> str:
    """Re-derive every generated region of ``current`` from ``planned``.

    Nothing outside those spans is read or written, so a body, an example and an
    implementation note come through byte for byte -- including every byte after
    a sentinel and after a docstring's closing quotes.
    """
    old_lines, old_named = generated_regions(current, fns, label)
    new_lines, new_named = generated_regions(planned, fns, label)
    out = list(old_lines)
    # Bottom up, so an earlier span's indices are still valid after a later one
    # has changed length.
    pairs = [(old, new) for (_, old), (_, new) in zip(old_named, new_named, strict=True)]
    for (old_start, old_end), (new_start, new_end) in sorted(pairs, reverse=True):
        out[old_start : old_end + 1] = new_lines[new_start : new_end + 1]
    return "\n".join(out)

# ---------------------------------------------------------------------------
# Planning, writing, checking
# ---------------------------------------------------------------------------


def build_plan() -> tuple[dict[Path, str], dict[str, Any]]:
    specs = read_artifact("node-specs.json")
    cards = read_artifact("method-cards.json")["cards"]
    nodes_by_fn = {n["fn"]: n for n in specs["nodes"]}
    forecastfn_names = tuple(specs["vocabulary"]["forecastfn_names"])

    by_wrapper: dict[str, list[dict[str, Any]]] = {}
    for card in cards:
        by_wrapper.setdefault(card["wrapper_file"], []).append(card)
    for group in by_wrapper.values():
        group.sort(key=lambda c: c["id"])
        categories = {c["category"] for c in group}
        if len(categories) != 1:
            raise SystemExit(f"gen_wrappers: {group[0]['wrapper_file']} spans {categories}.")

    by_category: dict[str, list[dict[str, Any]]] = {}
    for card in cards:
        by_category.setdefault(card["category"], []).append(card)
    for group in by_category.values():
        group.sort(key=lambda c: c["id"])

    plan: dict[Path, str] = {}
    for category in by_category:
        package = OUT_ROOT / category_package(category)
        plan[package / "__init__.py"] = emitted(
            f"{SPDX}\n" f'"""Wrappers for category {category}."""\n',
            f"{category_package(category)}/__init__.py",
        )
    # ONE DERIVATION OF WHICH FUNCTIONS A MODULE HOLDS, AND IN WHICH ORDER. The
    # splice pairs the spans it finds on disk with the spans it finds in the
    # planned text by position, so two derivations that ordered the functions
    # differently would pair a docstring with the wrong function.
    fns_by_module: dict[Path, list[str]] = {}
    for wrapper_file, group in by_wrapper.items():
        package = OUT_ROOT / category_package(group[0]["category"])
        module = wrapper_module_name(wrapper_file)
        path = package / f"{module}.py"
        fns_by_module[path] = [fn for card in group for fn in card["tool_fns"]]
        plan[path] = emitted(
            module_source(wrapper_file, group, nodes_by_fn, forecastfn_names),
            str(path.relative_to(OUT_ROOT)),
        )
    return plan, {
        "nodes_by_fn": nodes_by_fn,
        "forecastfn_names": forecastfn_names,
        "fns_by_module": fns_by_module,
    }


def expected_signatures(context: dict[str, Any]) -> dict[str, list[str]]:
    """fn -> the canonical parameter spelling, as ``ast.unparse`` would render it."""
    nodes_by_fn: dict[str, dict[str, Any]] = context["nodes_by_fn"]
    forecastfn_names: tuple[str, ...] = context["forecastfn_names"]
    out: dict[str, list[str]] = {}
    for fn, node in nodes_by_fn.items():
        params = []
        for arg in node["arguments"]:
            ann = ast.unparse(ast.parse(annotation_for(arg, forecastfn_names), mode="eval").body)
            if not arg["required"]:
                ann = f"{ann} | None"
            params.append(f"{python_arg_name(arg['name'])}: {ann}")
        out[fn] = params
    return out


def actual_signature(tree: ast.AST, fn: str) -> list[str] | None:
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef) and node.name == fn:
            args = node.args
            if args.args or args.posonlyargs or args.vararg:
                return ["<not keyword-only>"]
            return [
                f"{a.arg}: {ast.unparse(a.annotation) if a.annotation else '<untyped>'}"
                for a in args.kwonlyargs
            ]
    return None


def run_init(plan: dict[Path, str]) -> int:
    created = 0
    for path, body in sorted(plan.items()):
        if path.exists():
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")
        created += 1
    modules = len([p for p in plan if p.suffix == ".py" and p.name != "__init__.py"])
    print(
        f"gen_wrappers --init: {created} file(s) created; "
        f"{modules} modules expected. Existing files were left untouched."
    )
    return 0


def holds_only_generated_stubs(tree: ast.Module, fns: list[str]) -> str | None:
    """None if every named function is still the emitted stub, else the first that is not.

    THE GUARD ON THE ONE WRITE THAT CANNOT BE SURGICAL. A module carrying the
    marker region is spliced, and a splice cannot reach a body; a module without
    one can only be rewritten whole, which is free while every body raises
    NotImplementedError and destructive the moment one does not. So this was
    demoted from the gate on every write to the gate on that path alone. The
    check is structural rather than textual, and it is `econflow_engine.metrics`
    that decides what the structure is: this generator's answer and the figure
    the manifest publishes have to be the same answer, because `--write` rewrites
    a module whole on the strength of it.
    """
    for fn in fns:
        node = next(
            (n for n in ast.walk(tree)
             if isinstance(n, ast.FunctionDef | ast.AsyncFunctionDef) and n.name == fn),
            None,
        )
        if node is None:
            continue
        if not is_stub(node):
            return fn
    return None


def _plan_route(path: Path, planned: str, fns: list[str]) -> tuple[str, bool]:
    """The text to write for one existing module, and whether it was spliced.

    THE ROUTE A FILE TAKES IS DECIDED BY ITS MARKERS, NOT BY ITS BODY. A module
    carrying the marker region is SPLICED, so a body and its author-owned
    Examples and Note survive byte for byte -- which is what lets this generator
    keep running once implementations land. A module with no marker region can
    only be rewritten WHOLE, and a whole rewrite over somebody's work is
    destruction; ``holds_only_generated_stubs`` guards that path and only that
    path, demoted from the gate on every write to the gate on the one write that
    cannot be surgical. Anything that can be neither raises the refusal.
    """
    label = str(path.relative_to(ENGINE_ROOT))
    current = path.read_text(encoding="utf-8")
    try:
        return emitted(splice(current, planned, fns, label), label), True
    except SpliceError as exc:
        unspliceable = exc
    try:
        tree = ast.parse(current)
    except SyntaxError as syntax:
        raise SpliceError(f"{label}: does not parse ({syntax})") from syntax
    held = holds_only_generated_stubs(tree, fns)
    if held is not None:
        raise SpliceError(
            f"{label}: '{held}' has a written body, and it cannot be spliced -- {unspliceable}"
        )
    return planned, False


def _refuse(reasons: list[str]) -> int:
    print("gen_wrappers --write: REFUSED, nothing was written")
    for line in reasons:
        print(f"  {line}")
    return 1


def run_write(plan: dict[Path, str], context: dict[str, Any]) -> int:
    """Re-derive every generated region in place, preserving everything else.

    Nothing is written until every module has been routed, so a refusal leaves
    the tree exactly as it found it.
    """
    fns_by_module: dict[Path, list[str]] = context["fns_by_module"]

    # A MODULE WHOSE FUNCTIONS THE PLAN DID NOT NAME IS REFUSED BEFORE ANYTHING
    # IS ROUTED, and this is the one hole the demotion of
    # holds_only_generated_stubs opened. That predicate loops over the names it
    # is handed, so an EMPTY list makes it answer "still a stub" about any file
    # whatsoever -- true for a package __init__.py, which holds no functions, and
    # false for everything else. generated_regions has the matching blind spot:
    # with no names it locates the header and not one docstring, so the splice
    # succeeds having re-derived a fraction of what it reports. Both are silent,
    # and the write path now visits files the old card-derived loop never did.
    unnamed = [
        f"{path.name}: the plan names no tool function for this module"
        for path in sorted(plan)
        if path.suffix == ".py" and path.name != "__init__.py" and not fns_by_module.get(path)
    ]
    if unnamed:
        return _refuse(unnamed)

    targets: dict[Path, str] = {}
    refused: list[str] = []
    spliced = 0

    for path, planned in sorted(plan.items()):
        if not path.exists():
            targets[path] = planned
            continue
        try:
            text, was_spliced = _plan_route(path, planned, fns_by_module.get(path, []))
        except SpliceError as exc:
            refused.append(str(exc))
            continue
        targets[path] = text
        if was_spliced:
            spliced += 1

    if refused:
        return _refuse(refused)

    written = 0
    for path, target in sorted(targets.items()):
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists() or path.read_text(encoding="utf-8") != target:
            path.write_text(target, encoding="utf-8")
            written += 1
    modules = len([p for p in plan if p.suffix == ".py" and p.name != "__init__.py"])
    print(
        f"gen_wrappers --write: {written} file(s) rewritten; {spliced} spliced in place; "
        f"{modules} modules re-derived from the artifacts."
    )
    return 0


def _signature_problems(
    tree: ast.Module, fns: list[str], expected: dict[str, list[str]], label: str
) -> list[str]:
    """The keyword-only signature of each stub, against node-specs.

    Kept beside the textual region comparison because this is the check that can
    name WHICH argument moved and to what; a diff of two blocks of text cannot.
    """
    problems: list[str] = []
    for fn in fns:
        actual = actual_signature(tree, fn)
        if actual is None:
            problems.append(f"{label}: stub '{fn}' is absent")
        elif actual != expected[fn]:
            problems.append(
                f"{label}: signature drift in '{fn}'\n"
                f"      expected: {expected[fn]}\n"
                f"      actual:   {actual}"
            )
    return problems


def _region_problems(
    current: str, planned: str, fns: list[str], label: str
) -> tuple[list[str], bool]:
    """(what differs, whether the regions were located at all).

    The second half is what the denominators count. A module whose markers could
    not be found has been reported, not compared, and must not be counted as
    compared -- that is the difference between a gate that failed and a gate that
    quietly examined less than it claims.
    """
    try:
        old_lines, old_named = generated_regions(current, fns, label)
        new_lines, new_named = generated_regions(planned, fns, label)
    except SpliceError as exc:
        return [str(exc)], False
    return [
        f"{label}: {name} differs from the text this generator emits"
        for (name, (a, b)), (_, (c, d)) in zip(old_named, new_named, strict=True)
        if old_lines[a : b + 1] != new_lines[c : d + 1]
    ], True


# WHAT --check MUST HAVE REACHED, and where each figure comes from. A
# marker-parsing bug that located no region would otherwise compare nothing and
# report success, which is the failure this repository has met most often.
_DENOMINATORS = {
    "package header(s)": ("engine", "categories"),
    "module header region(s)": ("engine", "wrappers"),
    "generated docstring region(s)": ("engine", "methods"),
}


def _check_counts(counted: dict[str, int], problems: list[str]) -> None:
    """Every denominator this run reached, against the manifest. EXACT EQUALITY."""
    for name, (section, key) in _DENOMINATORS.items():
        declared = inventory_constant(section, key)
        if counted[name] != declared:
            problems.append(
                f"compared {counted[name]} {name}; {section}.{key} declares {declared}"
            )


def run_check(plan: dict[Path, str], context: dict[str, Any]) -> int:
    """Every generated region on disk is the text this generator emits.

    THE COMPARISON IS TEXTUAL, and it has to be: the region markers are comments,
    and comments do not survive into an abstract syntax tree. The signature
    comparison stays alongside it because it is the one that can say WHICH
    argument moved.
    """
    problems: list[str] = [
        f"missing: {path.relative_to(ENGINE_ROOT)}"
        for path in sorted(plan)
        if not path.exists()
    ]
    expected = expected_signatures(context)
    fns_by_module: dict[Path, list[str]] = context["fns_by_module"]
    counted = dict.fromkeys(_DENOMINATORS, 0)

    for path, planned in sorted(plan.items()):
        if not path.exists():
            continue
        label = str(path.relative_to(ENGINE_ROOT))
        current = path.read_text(encoding="utf-8")
        if path.name == "__init__.py":
            counted["package header(s)"] += 1
            if current != planned:
                problems.append(f"{label}: the package header differs from the generated text")
            continue
        fns = fns_by_module.get(path, [])
        try:
            problems += _signature_problems(ast.parse(current), fns, expected, label)
        except SyntaxError as exc:
            problems.append(f"unparsable: {label}: {exc}")
            continue
        found, located = _region_problems(current, planned, fns, label)
        problems += found
        if located:
            counted["module header region(s)"] += 1
            counted["generated docstring region(s)"] += len(fns)

    _check_counts(counted, problems)
    if problems:
        print("gen_wrappers --check: DRIFT")
        for line in problems:
            print(f"  {line}")
        return 1
    reached = ", ".join(f"{counted[name]} {name}" for name in _DENOMINATORS)
    print(
        f"gen_wrappers --check: OK -- {reached} reproduce the generated text exactly; "
        f"{len(expected)} stub signatures match node-specs."
    )
    return 0


# ---------------------------------------------------------------------------
# The per-wrapper test scaffold
# ---------------------------------------------------------------------------


def _resolve_module(module: str) -> tuple[str, str, list[dict[str, Any]]]:
    """``bry_boschan`` or ``c19_.../bry_boschan`` -> (package, module, its cards).

    All 598 module names are distinct, so the bare form is unambiguous; the
    qualified form is accepted because that is how the tree spells a path.
    """
    wanted = module.removesuffix(".py").split("/")[-1]
    hint = module.split("/")[0] if "/" in module else None
    cards = [
        card
        for card in read_artifact("method-cards.json")["cards"]
        if wrapper_module_name(card["wrapper_file"]) == wanted
        and (hint is None or category_package(card["category"]) == hint)
    ]
    if not cards:
        raise SystemExit(
            f"gen_wrappers: no wrapper module named {module!r}. "
            "Name it as it appears under src/econflow_engine/wrappers/."
        )
    cards.sort(key=lambda card: card["id"])
    return category_package(cards[0]["category"]), wanted, cards


# EVERY LINE BELOW IS EMITTED VERBATIM. Nothing here goes through ``_wrap``:
# that wraps PROSE, and applied to a call it splits the string literal across
# lines and emits source Python cannot read. If a line is long, ruff decides
# that, not a wrapper -- and ``emitted`` parses the result either way.
_SCAFFOLD_CLASSES: tuple[tuple[str, str, tuple[tuple[str, tuple[str, ...]], ...]], ...] = (
    (
        "TestGatesBlock",
        "Class A -- one passing and one refused input for every declared gate.",
        (
            (
                "test_every_declared_gate_has_a_passing_and_a_refused_input",
                (
                    "for each gate the research sheet lists, assert one input that",
                    "passes and one refused with its reason_code, its detail_code and",
                    "a message naming the rule.",
                ),
            ),
            (
                "test_an_undeclared_argument_is_refused_before_the_body_runs",
                (
                    "call through wire_model(fn) with an argument the node does not",
                    "declare, and assert the refusal.",
                ),
            ),
        ),
    ),
    (
        "TestStructure",
        "Class B -- the shape of the result, and that the wire can carry it.",
        (
            (
                "test_the_result_carries_exactly_the_declared_output_keys",
                (
                    "assert set(payload) == set(output_keys.keys) for this fn in",
                    "node-specs.json -- EXACT, because that field is the whole key",
                    "set rather than the card's partial prose. Where the status is",
                    "`undeclared`, declare it in corpus/ in this same change and",
                    "lower engine.undeclared_output_keys. Then a to_mcp walk with no",
                    "serialisation stub in the payload, and a to_json round-trip.",
                ),
            ),
            (
                "test_the_registered_object_is_what_a_consumer_needs",
                (
                    "if the node registers, assert register_field in NODE_META and",
                    "exercise one consumer; if it does not, delete this test.",
                ),
            ),
        ),
    ),
    (
        "TestOracleCase",
        "Class C -- a published number, its citation and its tolerance class.",
        (
            (
                "test_the_published_number_is_reproduced_within_its_tolerance",
                (
                    "load the oracle case and compare. The number is published, never",
                    "one this body produced, and a case with no tolerance_class is an",
                    "error rather than a fallback.",
                ),
            ),
        ),
    ),
    (
        "TestDeterminism",
        "Class D -- identical inputs, identical bytes.",
        (
            (
                "test_two_identical_calls_serialise_to_identical_bytes",
                (
                    "call twice and compare to_json(to_mcp(result)); if the fn is in",
                    "stochastic_unseeded_fns, pin the seed and read that set from the",
                    "artifact rather than from a copied list.",
                ),
            ),
        ),
    ),
)


def _scaffold_test(name: str, message: tuple[str, ...]) -> list[str]:
    """One emitted test: a signature, then a ``pytest.fail`` nobody can miss.

    The message is a tuple of ALREADY-SHORT lines rendered as adjacent string
    literals, which Python concatenates. That is the whole reason the prose
    wrapper is not used here.
    """
    return [
        "",
        f"    def {name}(self) -> None:",
        "        pytest.fail(",
        f'            "{SCAFFOLD_MARKER}: {message[0]} "',
        *[f'            "{part} "' for part in message[1:-1]],
        *([f'            "{message[-1]}"'] if len(message) > 1 else []),
        "        )",
    ]


def scaffold_tests(module: str) -> str:
    """The four mandatory test classes for one wrapper module, as source text.

    NOT COMMITTED IN BULK. This is a command box 2.2 runs for the module it is
    about to implement, and every test it emits fails until it is written.
    """
    package, name, cards = _resolve_module(module)
    fns = [fn for card in cards for fn in card["tool_fns"]]
    ids = ", ".join(f"#{card['id']}" for card in cards)
    plural = "s" if len(cards) > 1 else ""

    lines = [
        SPDX,
        f'"""Tests for the wrapper module ``{name}`` -- method card{plural} {ids}.',
        "",
        *_wrap(
            f"Scaffolded by ``python scripts/gen_wrappers.py --scaffold-tests {name}``; "
            f"its home is ``tests/wrappers/{package}/test_{name}.py``.",
            "",
        ),
        "",
        *_wrap(
            "FOUR CLASSES, IN THIS ORDER. A is the gates block, B the shape of the result, "
            "C the oracle case and D determinism. Every test below fails until it is "
            f"written, and each carries a ``{SCAFFOLD_MARKER}`` marker: remove one only by "
            "writing the test it stands in for, because a committed file under "
            "tests/wrappers/ that still carries a marker is refused.",
            "",
        ),
        '"""',
        "",
        "from __future__ import annotations",
        "",
        "import pytest",
        "",
        # Parenthesised with a trailing comma, which is what keeps the longest
        # package and module names inside the line limit -- measured over all 598,
        # where the one-line form overruns for 30-odd of them. The magic trailing
        # comma also stops a formatter collapsing it back.
        f"from econflow_engine.wrappers.{package} import (",
        f"    {name} as wrapper,",
        ")",
        "",
        "MODULE_FNS = (",
        *[f'    "{fn}",' for fn in fns],
        ")",
    ]
    for cls, summary, tests in _SCAFFOLD_CLASSES:
        lines += ["", "", f"class {cls}:", f'    """{summary}"""']
        for test_name, message in tests:
            lines += _scaffold_test(test_name, message)
    lines += [
        "",
        "",
        "def test_the_module_exports_every_function_its_cards_name() -> None:",
        '    """The one assertion a scaffold can make truthfully before a body exists."""',
        "    missing = [fn for fn in MODULE_FNS if not hasattr(wrapper, fn)]",
        "    assert not missing, missing",
    ]
    return emitted("\n".join(lines).rstrip("\n") + "\n", f"the scaffold for {name}")


def run_scaffold(module: str, out: str | None) -> int:
    source = scaffold_tests(module)
    if out is None:
        print(source, end="")
        return 0
    path = Path(out)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(source, encoding="utf-8")
    print(f"gen_wrappers --scaffold-tests: wrote {path}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--init", action="store_true", help="create missing files only")
    group.add_argument("--check", action="store_true", help="fail on any drift")
    group.add_argument(
        "--write", action="store_true",
        help="re-derive every generated region in place, preserving every written body")
    group.add_argument(
        "--scaffold-tests", metavar="MODULE",
        help="emit the four mandatory test classes for one wrapper module")
    parser.add_argument(
        "--out", metavar="PATH", help="write the scaffold to PATH instead of stdout")
    args = parser.parse_args()

    if args.out is not None and args.scaffold_tests is None:
        parser.error("--out belongs to --scaffold-tests")
    if args.scaffold_tests is not None:
        return run_scaffold(args.scaffold_tests, args.out)

    plan, context = build_plan()
    for path in plan:
        stem = path.stem
        if path.suffix == ".py" and (not stem.isidentifier() or keyword.iskeyword(stem)):
            raise SystemExit(f"gen_wrappers: {stem!r} is not a usable module name.")
    if args.init:
        return run_init(plan)
    if args.write:
        return run_write(plan, context)
    return run_check(plan, context)


if __name__ == "__main__":
    raise SystemExit(main())
