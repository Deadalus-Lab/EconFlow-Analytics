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

Modes:
    --init   create what is missing; NEVER overwrite an existing file.
    --check  assert every expected module exists and that every stub
             signature still matches node-specs; exit 1 on drift.
    --write  rewrite every generated file; refuses any module holding a written
             body, so a hand-filled implementation cannot be overwritten.
"""

from __future__ import annotations

import argparse
import ast
import json
import keyword
import sys
from pathlib import Path
from typing import Any

ENGINE_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ENGINE_ROOT / "src"))

from econflow_engine.naming import (  # noqa: E402  (after sys.path)
    category_package,
    python_arg_name,
    wrapper_module_name,
)

ARTIFACTS = ENGINE_ROOT / "artifacts"
OUT_ROOT = ENGINE_ROOT / "src" / "econflow_engine" / "wrappers"
METHOD_SOURCES = ENGINE_ROOT / "METHOD-SOURCES.json"

_SOURCES: dict[str, Any] | None = None


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
    """One line naming the library or the paper this module is built from.

    The register's contract is enforced HERE rather than trusted: a row naming
    both a library and a paper, or missing entirely, stops the generation. A row
    that names neither is not an error -- it is the honest 'planned' state, and
    saying so is better than a docstring that points the reader at nothing.
    """
    row = method_sources().get(f"{package}/{module}")
    if row is None:
        raise SystemExit(f"gen_wrappers: {package}/{module} has no row in METHOD-SOURCES.json")
    library, paper = row.get("library"), row.get("paper")
    if library and paper:
        raise SystemExit(
            f"gen_wrappers: {package}/{module} names both a library and a paper; "
            "the register admits exactly one."
        )
    if library:
        return str(library)
    if paper:
        return str(paper)
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

    head = [
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
    head += ["]", "", ""]

    body: list[str] = []
    for fn in fns:
        body += stub_source(nodes_by_fn[fn], card_of[fn], forecastfn_names)
        body += ["", ""]
    return "\n".join(head + body).rstrip("\n") + "\n"

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
        plan[package / "__init__.py"] = (
            f"{SPDX}\n"
            f'"""Wrappers for category {category}."""\n'
        )
    for wrapper_file, group in by_wrapper.items():
        package = OUT_ROOT / category_package(group[0]["category"])
        module = wrapper_module_name(wrapper_file)
        plan[package / f"{module}.py"] = module_source(
            wrapper_file, group, nodes_by_fn, forecastfn_names
        )
    return plan, {"nodes_by_fn": nodes_by_fn, "forecastfn_names": forecastfn_names}


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

    THIS IS THE GUARD ON --write. Regenerating a wrapper module rewrites the whole
    file, which is free while every body raises NotImplementedError and destructive
    the moment one does not. The check is structural rather than textual: a stub is
    a docstring followed by a single `raise NotImplementedError(...)`, and anything
    else is somebody's work.
    """
    for fn in fns:
        node = next(
            (n for n in ast.walk(tree)
             if isinstance(n, ast.FunctionDef | ast.AsyncFunctionDef) and n.name == fn),
            None,
        )
        if node is None:
            continue
        body = [s for s in node.body
                if not (isinstance(s, ast.Expr) and isinstance(s.value, ast.Constant)
                        and isinstance(s.value.value, str))]
        if len(body) != 1 or not isinstance(body[0], ast.Raise):
            return fn
        exc = body[0].exc
        name = exc.func if isinstance(exc, ast.Call) else exc
        if not (isinstance(name, ast.Name) and name.id == "NotImplementedError"):
            return fn
    return None


def run_write(plan: dict[Path, str], context: dict[str, Any]) -> int:
    """Rewrite every generated file, refusing any module that holds a real body."""
    cards = read_artifact("method-cards.json")["cards"]
    fns_by_module: dict[Path, list[str]] = {}
    for card in cards:
        module = OUT_ROOT / category_package(card["category"]) / (
            f"{wrapper_module_name(card['wrapper_file'])}.py")
        fns_by_module.setdefault(module, []).extend(card["tool_fns"])

    refused: list[str] = []
    for module, fns in sorted(fns_by_module.items()):
        if not module.exists():
            continue
        tree = ast.parse(module.read_text(encoding="utf-8"))
        held = holds_only_generated_stubs(tree, fns)
        if held is not None:
            refused.append(f"{module.relative_to(ENGINE_ROOT)}: '{held}' has a written body")
    if refused:
        print("gen_wrappers --write: REFUSED, these modules are no longer stubs")
        for line in refused:
            print(f"  {line}")
        return 1

    written = 0
    for path, body in sorted(plan.items()):
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists() or path.read_text(encoding="utf-8") != body:
            path.write_text(body, encoding="utf-8")
            written += 1
    modules = len([p for p in plan if p.suffix == ".py" and p.name != "__init__.py"])
    print(f"gen_wrappers --write: {written} file(s) rewritten; "
          f"{modules} modules regenerated from the artifacts.")
    return 0


def run_check(plan: dict[Path, str], context: dict[str, Any]) -> int:
    problems: list[str] = [
        f"missing: {path.relative_to(ENGINE_ROOT)}"
        for path in sorted(plan)
        if not path.exists()
    ]
    expected = expected_signatures(context)
    cards = read_artifact("method-cards.json")["cards"]
    fns_by_module: dict[Path, list[str]] = {}
    for card in cards:
        package = OUT_ROOT / category_package(card["category"])
        module = package / f"{wrapper_module_name(card['wrapper_file'])}.py"
        fns_by_module.setdefault(module, []).extend(card["tool_fns"])

    for module, fns in sorted(fns_by_module.items()):
        if not module.exists():
            continue
        try:
            tree = ast.parse(module.read_text(encoding="utf-8"))
        except SyntaxError as exc:
            problems.append(f"unparsable: {module.relative_to(ENGINE_ROOT)}: {exc}")
            continue
        for fn in fns:
            actual = actual_signature(tree, fn)
            if actual is None:
                problems.append(f"{module.relative_to(ENGINE_ROOT)}: stub '{fn}' is absent")
                continue
            if actual != expected[fn]:
                problems.append(
                    f"{module.relative_to(ENGINE_ROOT)}: signature drift in '{fn}'\n"
                    f"      expected: {expected[fn]}\n"
                    f"      actual:   {actual}"
                )
    if problems:
        print("gen_wrappers --check: DRIFT")
        for line in problems:
            print(f"  {line}")
        return 1
    modules = len([p for p in plan if p.suffix == ".py" and p.name != "__init__.py"])
    print(
        f"gen_wrappers --check: OK -- {modules} modules, "
        f"{len(expected)} stub signatures match node-specs."
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--init", action="store_true", help="create missing files only")
    group.add_argument("--check", action="store_true", help="fail on any drift")
    group.add_argument(
        "--write", action="store_true",
        help="rewrite every generated file; refuses any module that holds a written body")
    args = parser.parse_args()

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
