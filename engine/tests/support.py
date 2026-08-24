# SPDX-License-Identifier: AGPL-3.0-only
"""Shared helpers for the gate and seed suites. Not a test module.

Three things live here because two or more test modules need them and a second
copy of any of them would be a second answer to the same question: the floor
reader, the wrapper-tree walk, and the beartype unwrapper.
"""

from __future__ import annotations

import ast
import json
from collections.abc import Callable
from functools import cache
from pathlib import Path
from typing import Any

ENGINE_ROOT = Path(__file__).resolve().parents[1]
WRAPPERS = ENGINE_ROOT / "src" / "econflow_engine" / "wrappers"
INVENTORY = ENGINE_ROOT.parent / ".github" / "inventory.json"


def as_shipped[F: Callable[..., Any]](function: F) -> F:
    """The callable PRODUCTION runs, whether or not the test hook is installed.

    WHY THIS EXISTS, MEASURED 2026-08-23. ``tests/conftest.py`` installs
    ``beartype.claw.beartype_package("econflow_engine")``, which rewrites every
    function in the package as it is imported. ``beartype`` is in the engine's
    ``dev`` dependency group and is ABSENT from ``[project].dependencies``, and
    the conftest comment says the hook must never move into the package -- so the
    function a deployed engine calls is the UNDECORATED one, and the test
    environment is strictly stricter than production.

    That matters for the four arguments the gates annotate concretely (``arg:
    str``, ``fn: str``, ``gate_alpha: float``, ``ordered: bool``). Under the hook
    beartype refuses a wrong type BEFORE the gate's own check can run, so the
    gate's ``GateError`` never appears -- in the test session only. Asserting the
    beartype outcome would be asserting something no deployment can produce.

    ``__wrapped__`` is set by beartype's wrapper and is ABSENT when no hook is
    installed, so this one expression yields the production callable in both
    environments. Verified in both::

        python -c "...; print(hasattr(gate_cross_section_only, '__wrapped__'))"
        # no hook  -> False   (already the production function)
        # with hook -> True   (the production function is behind it)

    ``BeartypeCallHintParamViolation`` subclasses NEITHER ``ValueError`` nor
    ``TypeError``, so the two outcomes can never be confused for one another.
    """
    unwrapped: F = getattr(function, "__wrapped__", function)
    return unwrapped


@cache
def inventory(section: str, key: str) -> int:
    """One asserted constant, from the one file that holds them.

    NO except-and-return-zero, and no default. A floor that cannot be read means
    the gate has not started, and a gate that has not started must never report
    as a gate that passed -- the failure this repository's whole anti-vacuity
    doctrine exists to refuse.
    """
    value = json.loads(INVENTORY.read_text(encoding="utf-8"))[section][key]
    return int(value)


@cache
def wrapper_modules() -> tuple[tuple[Path, ast.Module], ...]:
    """Every wrapper module, parsed ONCE per session. The set ``engine.wrappers`` counts.

    Mirrors ``.github/inventory.json`` ``commands.wrappers``::

        find src/econflow_engine/wrappers -name '*.py' -type f \\
            -not -name '__init__.py' | wc -l

    A file that does not parse is a hard failure, never a skip: a gate that
    quietly steps over the one module it cannot read is the gate that misses the
    module somebody broke.

    ``@cache`` AND A TUPLE, BOTH DELIBERATE. Six test functions across two modules
    call this, and parsing 598 files is 0.091 s (2.30 MB of source, 98,421 AST
    nodes -- it is parse-bound, not I/O-bound), so the uncached form spent 0.80 s
    of a 5.90 s suite re-parsing the same tree five times. The tuple is what keeps
    a shared cached value from being mutated by one caller under another.
    """
    if not WRAPPERS.is_dir():
        raise AssertionError(f"no wrapper tree at {WRAPPERS}; the walk cannot start.")
    parsed: list[tuple[Path, ast.Module]] = []
    for path in sorted(WRAPPERS.rglob("*.py")):
        if path.name == "__init__.py":
            continue
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"))
        except SyntaxError as exc:
            raise AssertionError(f"{path} does not parse ({exc}); refusing to guess.") from exc
        parsed.append((path, tree))
    return tuple(parsed)


def is_stub(function: ast.FunctionDef | ast.AsyncFunctionDef) -> bool:
    """A generated stub: a docstring and nothing but ``raise NotImplementedError``.

    THIS IS THE THIRD COPY OF ONE PREDICATE, AND THAT IS A KNOWN DEBT. The other
    two are ``.github/inventory.json`` ``commands.n_implemented`` and
    ``engine/scripts/gen_wrappers.py`` ``holds_only_generated_stubs`` -- same body
    filter, same ``len(body) != 1``, same ``getattr(exc, "func", exc)``, same name
    check. The drift risk is asymmetric and destructive: ``gen_wrappers.py
    --write`` REWRITES a wrapper module when its predicate says "still a stub",
    while R2 in ``test_seed_enforcement.py`` uses this one to decide which bodies
    it polices, so a divergence means ``--write`` overwriting a body R2 was
    watching. They cannot be shared today -- ``scripts/`` is deliberately not a
    package and ``tests/`` is not importable from it -- so consolidating means
    promoting the predicate into the engine package. Recorded, not done here.
    """
    body = [
        statement
        for statement in function.body
        if not (
            isinstance(statement, ast.Expr)
            and isinstance(statement.value, ast.Constant)
            and isinstance(statement.value.value, str)
        )
    ]
    if len(body) != 1 or not isinstance(body[0], ast.Raise):
        return False
    raised = body[0].exc
    name = getattr(raised, "func", raised)
    return isinstance(name, ast.Name) and name.id == "NotImplementedError"
