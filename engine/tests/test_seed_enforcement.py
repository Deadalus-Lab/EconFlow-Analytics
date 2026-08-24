# SPDX-License-Identifier: AGPL-3.0-only
"""Box 2.1.13 -- randomness is pinned, and the three rules that enforce it.

THE UNSEEDED SET IS READ FROM THE ARTIFACT VOCABULARY, NEVER COPIED. It is
authored in ``engine/corpus/_vocabulary.json`` under ``stochastic_unseeded_fns``
and propagated to ``artifacts/node-specs.json``, the generated manifest and
``mcp/allowlists.py``. A list re-typed here would be a second source of truth
that goes stale the day a method is added.

WHY THREE RULES AND NOT ONE. Measured 2026-08-23, and the numbers are what split
it::

    len(STOCHASTIC_UNSEEDED_FNS)                              -> 27
    those with NO `seed` argument at all                      -> 21
    nodes carrying a `seed` argument                          -> 246
    of those, NOT in the unseeded set                         -> 240

So the catalogue holds three distinct populations, and one rule cannot cover
them: 21 functions whose randomness cannot be pinned by an argument (R3 -- their
results must never be cached), 246 that expose a seed knob and must honour it
(R2), and 598 modules that must not reach a process-global generator at all (R1).

R1 and R3 bite TODAY over the real tree. R2's floor is ``engine.n_implemented``,
which is 0, so it examines a planted control under ``tests/controls/`` until the
first real body lands -- named here rather than left as a silent zero.
"""

from __future__ import annotations

import ast
import json
from functools import cache
from typing import Any

import pytest

from econflow_engine.mcp.allowlists import STOCHASTIC_UNSEEDED_FNS
from econflow_engine.mcp.gateway import run_method
from tests.support import ENGINE_ROOT, inventory, is_stub, wrapper_modules

# The modern numpy API. Everything ELSE under ``np.random`` is the legacy
# RandomState surface, which reads and writes a process-global stream: two calls
# in one process are not independent of each other, and no argument pins them.
_MODERN_NUMPY_RANDOM = frozenset(
    {
        "default_rng",
        "Generator",
        "SeedSequence",
        "BitGenerator",
        "PCG64",
        "PCG64DXSM",
        "Philox",
        "SFC64",
        "MT19937",
    }
)
_NUMPY_ALIASES = frozenset({"np", "numpy"})
# The standard library's module-level functions, which share one global stream.
_STDLIB_GLOBAL = frozenset({"seed", "random"})


# ==========================================================================
# R1 -- no wrapper touches a process-global generator
# ==========================================================================


def global_random_violations(tree: ast.Module) -> list[str]:
    """Names and calls that reach a generator no argument can pin."""
    found: list[str] = []
    # ONE walk. The `default_rng()` hits are collected separately and appended at
    # the end so the reported order is unchanged from the two-walk form; a second
    # full ast.walk of every module cost 26 ms per run and grows with body size.
    unseeded_rng: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            function = node.func
            if (
                isinstance(function, ast.Attribute)
                and function.attr == "default_rng"
                and not node.args
                and not node.keywords
            ):
                unseeded_rng.append(
                    f"line {node.lineno}: default_rng() with no argument -- a generator "
                    "seeded from the operating system is not reproducible"
                )
            continue
        if isinstance(node, ast.ImportFrom) and (node.module or "").startswith(
            ("numpy.random", "random")
        ):
            names = ", ".join(alias.name for alias in node.names)
            found.append(f"line {node.lineno}: from {node.module} import {names}")
            continue
        if not isinstance(node, ast.Attribute):
            continue
        parent = node.value
        # np.random.<attr>
        if (
            isinstance(parent, ast.Attribute)
            and parent.attr == "random"
            and isinstance(parent.value, ast.Name)
            and parent.value.id in _NUMPY_ALIASES
            and node.attr not in _MODERN_NUMPY_RANDOM
        ):
            found.append(
                f"line {node.lineno}: {parent.value.id}.random.{node.attr} -- the legacy "
                "global generator; use np.random.default_rng(seed)"
            )
        # random.<attr> from the standard library
        elif (
            isinstance(parent, ast.Name)
            and parent.id == "random"
            and node.attr in _STDLIB_GLOBAL
        ):
            found.append(
                f"line {node.lineno}: random.{node.attr} -- the standard library's "
                "global stream; use np.random.default_rng(seed)"
            )
    found.extend(unseeded_rng)
    return found


R1_POSITIVE: dict[str, str] = {
    "np.random.seed": "import numpy as np\ndef f():\n    np.random.seed(0)\n",
    "a legacy global draw": "import numpy as np\ndef f():\n    return np.random.normal(size=3)\n",
    "stdlib random.seed": "import random\ndef f():\n    random.seed(0)\n",
    "stdlib random.random": "import random\ndef f():\n    return random.random()\n",
    "an unseeded default_rng": (
        "import numpy as np\ndef f():\n    return np.random.default_rng().normal()\n"
    ),
    "a from-import": "from numpy.random import seed\n",
}

R1_NEGATIVE: dict[str, str] = {
    "a seeded generator": (
        "import numpy as np\n"
        "def f(*, seed=None):\n"
        "    return np.random.default_rng(seed).normal(size=3)\n"
    ),
    "prose about seeding": (
        "def f(*, x):\n"
        '    """This method is deterministic; it calls np.random.seed nowhere."""\n'
        "    note = 'random.seed is not used here'\n"
        "    return {'note': note}\n"
    ),
    "an unrelated .random attribute": (
        "def f(*, model):\n    return model.random.state\n"
    ),
}


def test_r1_positive_controls_are_all_flagged() -> None:
    for label, source in R1_POSITIVE.items():
        assert global_random_violations(ast.parse(source)), (
            f"R1 positive control {label!r} was NOT flagged; the rule has a hole"
        )


def test_r1_negative_controls_are_all_clean() -> None:
    for label, source in R1_NEGATIVE.items():
        flagged = global_random_violations(ast.parse(source))
        assert not flagged, f"R1 negative control {label!r} was flagged on {flagged}"


def test_r1_walk_parsed_every_wrapper_module_the_manifest_declares() -> None:
    """ANTI-VACUITY. A walk that found nothing must fail, not report zero findings."""
    parsed = len(wrapper_modules())
    declared = inventory("engine", "wrappers")
    assert declared > 0, "engine.wrappers is not a floor at zero"
    assert parsed == declared, f"parsed {parsed} module(s) against {declared} declared"


def test_r1_no_wrapper_reaches_a_process_global_generator() -> None:
    offenders = [
        (path, hits) for path, tree in wrapper_modules() if (hits := global_random_violations(tree))
    ]
    assert not offenders, "\n".join(
        f"{path}\n" + "\n".join(f"    {hit}" for hit in hits[:5]) for path, hits in offenders[:10]
    )


# ==========================================================================
# R2 -- a declared seed must reach the body
# ==========================================================================


def seed_ignored(tree: ast.Module) -> list[str]:
    """Implemented functions that declare ``seed`` and never reference it.

    THE SILENT DEFECT NOTHING ELSE CATCHES. The signature is right, the type
    checkers are happy, the result is plausible -- and it is a different number on
    every call while the argument promises it will not be. Stubs are skipped by
    the same predicate ``engine.n_implemented`` uses, so the rule applies to
    exactly the functions that figure counts.
    """
    found: list[str] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef):
            continue
        if node.name.startswith("_") or is_stub(node):
            continue
        arguments = node.args
        declared = [
            argument.arg
            for argument in (*arguments.args, *arguments.kwonlyargs, *arguments.posonlyargs)
        ]
        if "seed" not in declared:
            continue
        referenced = any(
            isinstance(inner, ast.Name) and inner.id == "seed"
            for statement in node.body
            for inner in ast.walk(statement)
        )
        if not referenced:
            found.append(
                f"line {node.lineno}: {node.name} declares a `seed` argument and never "
                "references it -- the call is not reproducible and says it is"
            )
    return found


CONTROL_MODULE = ENGINE_ROOT / "tests" / "controls" / "ignores_seed.py"


def test_r2_catches_the_planted_control_on_disk() -> None:
    """The control is a FILE, so this exercises the read and the parse, not only the rule.

    ``engine.n_implemented`` is 0, so without this the rule would examine nothing.
    """
    assert CONTROL_MODULE.is_file(), f"the planted control is missing at {CONTROL_MODULE}"
    findings = seed_ignored(ast.parse(CONTROL_MODULE.read_text(encoding="utf-8")))
    assert len(findings) == 1, f"expected exactly the planted defect, got {findings}"
    assert "run_planted_ignores_seed" in findings[0]


def test_r2_clears_the_paired_negative_control() -> None:
    """The same file holds a correct function; flagging it would mean the rule decayed."""
    findings = seed_ignored(ast.parse(CONTROL_MODULE.read_text(encoding="utf-8")))
    assert not any("run_planted_uses_seed" in finding for finding in findings)


def test_r2_no_implemented_wrapper_ignores_its_declared_seed() -> None:
    """The real tier. Vacuous while every body is a stub -- hence the control above."""
    offenders = [
        (path, hits) for path, tree in wrapper_modules() if (hits := seed_ignored(tree))
    ]
    assert not offenders, "\n".join(
        f"{path}\n" + "\n".join(f"    {hit}" for hit in hits) for path, hits in offenders[:10]
    )


def test_r2_declares_how_many_bodies_it_actually_examined() -> None:
    """Names the floor rather than leaving a silent zero, and it rises with 2.2."""
    examined = sum(
        1
        for _, tree in wrapper_modules()
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef)
        and not node.name.startswith("_")
        and not is_stub(node)
    )
    assert examined == inventory("engine", "n_implemented"), (
        f"R2 examined {examined} implemented body/bodies; engine.n_implemented says "
        f"{inventory('engine', 'n_implemented')}. Move the manifest constant in the "
        "same change as the bodies."
    )


# ==========================================================================
# R3 -- a stochastic node with no seed argument is never cached
# ==========================================================================


@cache
def _node_specs() -> dict[str, Any]:
    """``node-specs.json``, parsed ONCE.

    Not the session-scoped ``node_specs`` fixture in ``conftest.py``, and that is
    forced: ``_seedless_stochastic`` below runs at COLLECTION time inside
    ``@pytest.mark.parametrize``, where no fixture exists yet. The two test bodies
    that are not collection-bound take the fixture instead, so the 3.67 MB
    artifact is read once rather than five times.
    """
    loaded: dict[str, Any] = json.loads(
        (ENGINE_ROOT / "artifacts" / "node-specs.json").read_bytes().decode("utf-8")
    )
    return loaded


@cache
def _seedless_stochastic() -> tuple[str, ...]:
    """The unseeded-set members that expose no ``seed`` argument at all.

    Both halves come from the artifact: the set from the vocabulary, the argument
    lists from ``node-specs.json``.
    """
    by_fn = {node["fn"]: node for node in _node_specs()["nodes"]}
    return tuple(
        sorted(
            fn
            for fn in STOCHASTIC_UNSEEDED_FNS
            if not any(argument["name"] == "seed" for argument in by_fn[fn]["arguments"])
        )
    )


def test_r3_the_seedless_population_is_the_measured_twenty_one() -> None:
    """ASSERT THE COUNT ITSELF. A vocabulary that shrank to zero must fail, not pass.

    Without this the parametrised test below would run over an empty set and
    report success -- a gate that examined nothing reading as a gate that passed.
    """
    assert len(STOCHASTIC_UNSEEDED_FNS) == 27
    assert len(_seedless_stochastic()) == 21


@pytest.mark.parametrize("fn", _seedless_stochastic())
def test_r3_a_seedless_stochastic_node_is_never_cached(fn: str) -> None:
    """``run_method`` computes the cache verdict BEFORE dispatch.

    That is why this bites today, with every body still a stub: the verdict is
    spread into the not-implemented and refused responses alike
    (``mcp/gateway.py``), so the caching decision is testable long before the
    method computes anything.
    """
    assert run_method(fn, {}).cache == "bypass"


def test_r3_bypass_is_not_the_answer_for_everything(node_specs: dict[str, Any]) -> None:
    """THE CONTRAST THAT MAKES THE RULE ABOVE MEAN SOMETHING.

    Every node would satisfy ``cache == "bypass"`` if the gateway simply never
    cached anything. A deterministic node carrying no seed argument must come
    back ``miss``, or the 21 assertions above are satisfied by a constant.
    """
    deterministic = [
        node["fn"]
        for node in node_specs["nodes"]
        if node["fn"] not in STOCHASTIC_UNSEEDED_FNS
        and not any(argument["name"] == "seed" for argument in node["arguments"])
    ]
    assert len(deterministic) > 1000, f"only {len(deterministic)} deterministic nodes"
    for fn in deterministic[:25]:
        assert run_method(fn, {}).cache == "miss", f"{fn} bypassed the cache unexpectedly"


def test_r3_a_node_exposing_an_unpinned_seed_also_bypasses(
    node_specs: dict[str, Any],
) -> None:
    """The third population: 246 nodes expose a seed knob this call did not pin."""
    with_seed = [
        node["fn"]
        for node in node_specs["nodes"]
        if any(argument["name"] == "seed" for argument in node["arguments"])
    ]
    assert len(with_seed) == 246
    assert len([fn for fn in with_seed if fn not in STOCHASTIC_UNSEEDED_FNS]) == 240
    for fn in with_seed[:15]:
        assert run_method(fn, {}).cache == "bypass"
