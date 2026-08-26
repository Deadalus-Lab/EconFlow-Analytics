# SPDX-License-Identifier: AGPL-3.0-only
"""What counts as an implemented body, and where the manifest lives.

ONE implementation of each, used by the generators, the harnesses and the
runtime alike. That is the siting ``naming.py`` already established, for the
same reason: two copies of one definition are two answers to one question, and
they are free to drift in silence.

WHY THE STUB PREDICATE HAD TO MOVE HERE. It had six homes -- ``tests/support.py``,
``scripts/gen_wrappers.py``, ``tests/controls/double_run.py``,
``tests/conformance/test_conformance.py``, the shell heredoc in
``.github/actions/assert-inventory/assert.sh`` and the published one-liner at
``README.md``. ``tests/support.py`` recorded the debt in its own words and named
the obstacle: ``scripts/`` is deliberately not a package and ``tests/`` is not
importable from it, so the only directory all three can reach is this one. The
drift risk is asymmetric and destructive -- ``gen_wrappers.py --write`` rewrites
a module whole when its predicate says "still a stub", while the seed rules use
theirs to decide which bodies they police, so a divergence means ``--write``
overwriting a body somebody was watching.

THE TWO SPELLINGS THAT CANNOT IMPORT PYTHON STAY AS TEXT, and that is the point
rather than a gap. ``assert.sh`` runs before the engine's environment exists and
``README.md`` is read by people, so neither can call ``is_stub``. What replaces
their deleted copies is a test that extracts each one, runs it, and compares its
answer with this module's -- so a divergence is a red test rather than a quiet
one. It has been quiet before: the README's spelling disagreed with the
manifest's in both directions for the whole time the two sat side by side, and
the agreement they appeared to have was an accident of an unrelated setting.
"""

from __future__ import annotations

import ast
from pathlib import Path

__all__ = ["find_manifest", "is_stub"]

MANIFEST_RELATIVE_PATH = Path(".github") / "inventory.json"

# The upward walk stops at the directory holding BOTH the manifest and
# ``engine/``, which is what makes the answer the repository root rather than
# the first ``.github`` on the way up. This cap is the second bound, and its
# only job is to refuse an unbounded climb to ``/`` when that pair is nowhere:
# it is a round number chosen as a bound, not a measurement, on the precedent
# of ``image.ceiling_bytes``. The deepest caller in the tree today needs six
# candidates -- ``engine/mutants/tests/controls/double_run.py`` under mutmut's
# sandbox, which reaches the root at its fifth parent.
_MAX_LEVELS_SEARCHED = 8


def is_stub(function: ast.FunctionDef | ast.AsyncFunctionDef) -> bool:
    """A generated stub: a docstring and nothing but ``raise NotImplementedError``.

    Docstrings are stripped before the body is measured because
    ``[tool.interrogate] fail-under = 100`` puts one on every function in the
    tree, so a rule counting raw statements would answer a question about
    documentation policy rather than about implementation.
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


def find_manifest(start: Path) -> Path:
    """The one ``.github/inventory.json``, found by walking up from ``start``.

    ``start`` is any path inside the tree; a module's ``__file__`` is the usual
    argument, and the file itself is simply the first candidate that cannot
    match.

    WHY A WALK AND NOT ``ENGINE_ROOT.parent``. mutmut runs the suite from
    ``engine/mutants/``, which inserts one directory level, so every harness
    that spelled the manifest as a fixed number of ``..`` resolved to
    ``engine/.github/inventory.json`` -- a path one level ABOVE the sandbox,
    which nothing in ``also_copy`` can fill and which a single-homed manifest
    forbids anyone to create. Twelve modules carried that spelling and six of
    them could not be deselected, including the gate the mutation job itself
    runs from inside the sandbox.

    BOUNDED TWICE. The walk accepts only a directory holding both the manifest
    and an ``engine/`` directory, so it cannot stop at some other ``.github`` on
    the way up, and it examines at most ``_MAX_LEVELS_SEARCHED`` candidates, so
    it cannot climb to ``/``. Measured: there is no ``.github`` directory
    anywhere above this repository's root, and the image lays the same pair out
    as ``/app/.github/inventory.json`` beside ``/app/engine``, which the suite
    at ``/app/engine`` reaches in three levels.

    A MANIFEST THAT CANNOT BE FOUND IS A HARD FAILURE, never a default and never
    a zero. A gate whose floor silently read 0 is a gate that has not started,
    and one that has not started must never report as one that passed.
    """
    origin = start.resolve()
    for candidate in [origin, *origin.parents][:_MAX_LEVELS_SEARCHED]:
        manifest = candidate / MANIFEST_RELATIVE_PATH
        if manifest.is_file() and (candidate / "engine").is_dir():
            return manifest
    raise FileNotFoundError(
        f"no {MANIFEST_RELATIVE_PATH} beside an engine/ directory within "
        f"{_MAX_LEVELS_SEARCHED} levels of {start}. Every asserted floor in this "
        "repository is read from that one file, so a gate that cannot find it "
        "has not started and must not report as one that passed."
    )
