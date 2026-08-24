# SPDX-License-Identifier: AGPL-3.0-only
"""A wrapper refuses through the gate framework, never with a ``raise`` of its own.

WHAT IT ENFORCES. Inside ``wrappers/**`` the only permitted ``raise`` is
``NotImplementedError`` -- the generated stub -- or a bare re-``raise`` inside an
``except``, which re-emits an exception the body did not invent. A refusal is a
CALL into :mod:`econflow_engine.gates.primitives`. ``assert`` is refused outright:
it carries no reason code, its message is not the wire message, and ``python -O``
removes it, so a body's last input check would vanish from an optimised
deployment without a diff.

WHY A RULE AND NOT A CONVENTION. 1456 bodies land across phase 2. A convention
holds for the first fifty and then somebody writes ``raise ValueError("n too
small")``, which ``make_tool`` does not catch, so a documented precondition
reaches the user as a stack trace instead of the rule that blocked them. An
inline ``GateError(...)`` is refused for the softer reason: it works, but it
puts the message and the code at the call site, which is the drift the registry
exists to prevent.

IT PARSES, IT DOES NOT GREP -- modelled on ``.github/scripts/check-no-network.sh``,
this tree's reference for a rule that cannot decay. A wrapper docstring
legitimately says "raises GateError" when it documents its refusals, and a regular
expression cannot tell that from code.

THREE ANTI-VACUITY GUARDS, the same three that script carries:
  1. an EXACT denominator from ``.github/inventory.json`` with no default -- a walk
     that found zero files must fail, not print "0 violations";
  2. three POSITIVE controls that must be flagged on every run;
  3. three NEGATIVE controls that must not be, so the rule cannot decay into one
     that fires on prose or on the stub it exists to permit.
"""

from __future__ import annotations

import ast

import pytest

from tests.support import inventory, wrapper_modules

# --- the three positive controls: each MUST be flagged --------------------
POSITIVE_CONTROLS: dict[str, str] = {
    "a bare ValueError": (
        "def f(*, n):\n"
        '    """Node ``f``."""\n'
        '    raise ValueError("x")\n'
    ),
    "an inline GateError": (
        "from econflow_engine.errors import GateError\n"
        "def f(*, n):\n"
        '    """Node ``f``."""\n'
        '    raise GateError("other", "x")\n'
    ),
    "an assert": (
        "def f(*, n):\n"
        '    """Node ``f``."""\n'
        "    assert n > 0\n"
    ),
}

# --- the three negative controls: each MUST NOT be flagged ----------------
NEGATIVE_CONTROLS: dict[str, str] = {
    "a docstring naming GateError": (
        "def f(*, n):\n"
        '    """Node ``f``.\n'
        "\n"
        "    Raises GateError when ``n`` is below the documented minimum, and\n"
        '    raises GateError again for a constant input. See ./README.md.\n'
        '    """\n'
        "    return {}\n"
    ),
    "the generated stub": (
        "def f(*, n):\n"
        '    """Node ``f``."""\n'
        '    raise NotImplementedError("f: not implemented. The method card is in '
        './README.md.")\n'
    ),
    "a primitive call": (
        "from econflow_engine.gates.primitives import require_variance\n"
        "def f(*, x):\n"
        '    """Node ``f``."""\n'
        '    require_variance(x, fn="f", arg="x")\n'
        "    return {}\n"
    ),
}


def violations(tree: ast.Module) -> list[str]:
    """Every ``raise`` a wrapper may not make, and every ``assert``.

    A BARE ``raise`` IS PERMITTED and only inside an ``except`` handler: it
    re-emits an exception the body did not invent, which is how a wrapper wraps a
    library error it has already caught. ``ast.Raise`` with ``exc is None``
    outside a handler is a syntax error, so the parser has already refused it.
    """
    found: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assert):
            found.append(
                f"line {node.lineno}: assert -- carries no reason code and is removed "
                "by python -O; call a gate primitive instead"
            )
        elif isinstance(node, ast.Raise):
            if node.exc is None:
                continue  # a bare re-raise
            raised = node.exc
            name = raised.func if isinstance(raised, ast.Call) else raised
            called = (
                name.id
                if isinstance(name, ast.Name)
                else name.attr
                if isinstance(name, ast.Attribute)
                else "<computed>"
            )
            if called == "NotImplementedError":
                continue  # the generated stub
            found.append(
                f"line {node.lineno}: raise {called}(...) -- a wrapper refuses by "
                "CALLING a gate primitive, never by raising"
            )
    return found


def test_the_positive_controls_are_all_flagged() -> None:
    """A rule that stopped catching its own planted defects has a hole."""
    for label, source in POSITIVE_CONTROLS.items():
        assert violations(ast.parse(source)), f"positive control {label!r} was NOT flagged"


def test_the_negative_controls_are_all_clean() -> None:
    """A rule that fires on prose, on the stub, or on a primitive call is decayed."""
    for label, source in NEGATIVE_CONTROLS.items():
        flagged = violations(ast.parse(source))
        assert not flagged, f"negative control {label!r} was flagged on {flagged}"


def test_the_walk_parsed_every_wrapper_module_the_manifest_declares() -> None:
    """ANTI-VACUITY, and it is EXACT rather than a floor.

    The walk is the same set ``commands.wrappers`` counts, so equality is
    available and is strictly stronger: a floor would admit a walk that grew a
    duplicate, and equality catches a module that appeared as well as one that
    vanished.
    """
    parsed = len(wrapper_modules())
    declared = inventory("engine", "wrappers")
    assert declared > 0, "engine.wrappers is not a floor at zero"
    assert parsed == declared, (
        f"parsed {parsed} wrapper module(s) against engine.wrappers = {declared}; "
        "the walk is wrong, not the tree"
    )


def test_no_wrapper_raises_outside_the_gate_framework() -> None:
    """The rule itself, over the whole wrapper tier."""
    offenders = [
        (path, hits) for path, tree in wrapper_modules() if (hits := violations(tree))
    ]
    assert not offenders, "\n".join(
        f"{path}\n" + "\n".join(f"    {hit}" for hit in hits[:5])
        for path, hits in offenders[:10]
    )


@pytest.mark.parametrize("label", sorted(POSITIVE_CONTROLS))
def test_each_positive_control_names_the_rule_it_broke(label: str) -> None:
    """The message a contributor reads must say what to do instead, not just 'no'."""
    (message,) = violations(ast.parse(POSITIVE_CONTROLS[label]))
    assert "gate primitive" in message
