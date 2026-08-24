# SPDX-License-Identifier: AGPL-3.0-only
"""Every refusal in the two normative gates is a ``GateError`` with a detail code.

WHAT THIS FILE EXISTS TO STOP COMING BACK. Until box 2.1.4 both gates raised a
bare ``ValueError`` at all 23 of their raise sites. ``mcp/make_tool.py`` catches
``GateError`` and nothing else, so a body that called one of these gates turned a
documented refusal into a CRASH -- ``run_method`` never reached its ``refused``
branch, and the caller got a stack trace instead of the rule that blocked it.
``GateError`` subclasses ``ValueError``, so the change is additive at the call
site and total at the boundary.

THE PARAMETRISED CASES BELOW COVER ALL 23 SITES. Each names the site, the input
that reaches it and the ``detail_code`` it must carry. Reproduce the count::

    python3 -c "import ast,pathlib as P; print(sum(isinstance(n, ast.Raise)
    for f in ('cross_section.py','sliding_window.py')
    for n in ast.walk(ast.parse((P.Path('src/econflow_engine/gates')/f).read_text()))))"
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

import numpy as np
import pandas as pd
import pytest
from beartype.roar import BeartypeCallHintParamViolation

from econflow_engine.errors import GateError
from econflow_engine.gates import (
    GATE_DETAIL_CODES,
    gate_cross_section_only,
    gate_sliding_window_step,
)
from tests.support import as_shipped

# THE SUBJECT IS THE SHIPPED FUNCTION, NOT THE TEST-DECORATED ONE. See
# `tests.support.as_shipped`: conftest installs beartype's import hook over the
# whole package, beartype is a dev-only dependency, and for the four concretely
# annotated arguments it refuses a wrong type before the gate's own check runs.
# Asserting that outcome would assert something no deployment can produce.
# `test_beartype_shadows_...` below asserts the test-session behaviour separately,
# so both truths are pinned to a specific exception type.
_cross_gate = as_shipped(gate_cross_section_only)
_window_gate = as_shipped(gate_sliding_window_step)

_ORDERED = np.arange(200, dtype=float)  # a perfect ramp: maximal autocorrelation
_DATED = pd.Series([1.0, 2.0, 3.0], index=pd.date_range("2020-01-01", periods=3, freq="D"))


def _cross(**kwargs: Any) -> Callable[[], object]:
    def call() -> object:
        return _cross_gate(**kwargs)

    return call


def _window(**kwargs: Any) -> Callable[[], object]:
    def call() -> object:
        return _window_gate(**kwargs)

    return call


# site (source line of the raise at the time of the conversion), the call, the code
CASES: list[tuple[str, Callable[[], object], str]] = [
    ("arg not a string", _cross(x=[1.0, 2.0, 3.0], arg=1), "gate-argument"),
    ("fn not a string", _cross(x=[1.0, 2.0, 3.0], fn=1), "gate-argument"),
    ("gate_alpha not a number", _cross(x=[1.0, 2.0, 3.0], gate_alpha="a"), "gate-argument"),
    ("gate_alpha out of (0,1)", _cross(x=[1.0, 2.0, 3.0], gate_alpha=2.0), "gate-argument"),
    ("ordered not a bool", _cross(x=[1.0, 2.0, 3.0], ordered=1), "gate-argument"),
    ("lb_lag not a positive int", _cross(x=[1.0, 2.0, 3.0], lb_lag=0), "gate-argument"),
    (
        "lb_lag with ordered=False",
        _cross(x=[1.0, 2.0, 3.0], lb_lag=1, ordered=False),
        "gate-argument",
    ),
    ("a dated Series", _cross(x=_DATED), "precondition-cross-section"),
    (
        "a DataFrame with a dated column",
        _cross(x=pd.DataFrame({"a": _DATED})),
        "precondition-cross-section",
    ),
    ("the Ljung-Box rejection", _cross(x=_ORDERED), "precondition-cross-section"),
    (
        "a DataFrame with no numeric column",
        _cross(x=pd.DataFrame({"a": ["x", "y", "z"]})),
        "precondition-shape",
    ),
    ("a non-numeric Series", _cross(x=pd.Series(["x", "y", "z"])), "precondition-shape"),
    (
        "a non-numeric matrix",
        _cross(x=np.array([["a", "b"], ["c", "d"], ["e", "f"]], dtype=object)),
        "precondition-shape",
    ),
    ("a matrix with no columns", _cross(x=np.zeros((3, 0))), "precondition-shape"),
    ("an empty mapping", _cross(x={}), "precondition-shape"),
    ("an empty list", _cross(x=[]), "precondition-shape"),
    ("an unsupported type", _cross(x=object()), "precondition-shape"),
    (
        "a non-numeric element of a list",
        _cross(x=[[1.0, 2.0, 3.0], "not a vector"]),
        "precondition-shape",
    ),
    ("an infinity in a group", _cross(x=[1.0, np.inf, 3.0, 4.0]), "precondition-missing"),
    ("fewer than three valid values", _cross(x=[1.0, 2.0]), "precondition-sample-size"),
    ("a constant group", _cross(x=[2.0, 2.0, 2.0, 2.0]), "precondition-degenerate"),
    (
        "lb_lag at or above n",
        _cross(x=[1.0, 2.0, 3.0, 4.0, 5.0], lb_lag=5),
        "precondition-sample-size",
    ),
    ("the window matrix is not 2-D", _window(matrix=[1.0, 2.0, 3.0]), "precondition-shape"),
    ("a negative tolerance", _window(matrix=np.zeros((4, 4)), tol=-1.0), "gate-argument"),
    (
        "max_step not a positive integer",
        _window(matrix=np.zeros((4, 4)), max_step=0),
        "gate-argument",
    ),
]


@pytest.mark.parametrize(("site", "call", "code"), CASES, ids=[c[0] for c in CASES])
def test_every_refusal_carries_a_reason_code_and_a_detail_code(
    site: str, call: Callable[[], object], code: str
) -> None:
    """A bare ``ValueError`` here would escape ``make_tool`` as a crash."""
    with pytest.raises(GateError) as caught:
        call()
    assert caught.value.reason_code == "other", site
    assert caught.value.detail_code == code, site
    assert caught.value.detail_code in GATE_DETAIL_CODES, site


def test_the_cases_reach_every_raise_site_in_the_two_gate_modules() -> None:
    """ANTI-VACUITY. Fewer cases than raise sites means a site nothing exercises.

    The parametrisation is written by hand, so nothing but this makes it move when
    a raise is added. Reading the count out of the source is what turns "25 cases
    pass" into "every refusal in these two modules is covered".
    """
    import ast
    from pathlib import Path

    gates = Path(__file__).resolve().parents[1] / "src" / "econflow_engine" / "gates"
    sites = sum(
        isinstance(node, ast.Raise)
        for name in ("cross_section.py", "sliding_window.py")
        for node in ast.walk(ast.parse((gates / name).read_text(encoding="utf-8")))
    )
    assert sites == 23, f"the two gate modules now hold {sites} raise sites, not 23"
    assert len(CASES) >= sites, f"{len(CASES)} cases against {sites} raise sites"


# The four arguments the gate annotates concretely. beartype refuses a wrong type
# for these BEFORE the gate's own check runs -- under the test hook and nowhere
# else. `lb_lag` is deliberately NOT here: it is annotated `int | None`, so the
# invalid value `0` satisfies the annotation, beartype passes it through and the
# gate's own check fires in BOTH environments. Measured, not assumed.
SHADOWED: list[tuple[str, dict[str, Any]]] = [
    ("arg", {"x": [1.0, 2.0, 3.0], "arg": 1}),
    ("fn", {"x": [1.0, 2.0, 3.0], "fn": 1}),
    ("gate_alpha", {"x": [1.0, 2.0, 3.0], "gate_alpha": "a"}),
    ("ordered", {"x": [1.0, 2.0, 3.0], "ordered": 1}),
]


def test_the_beartype_hook_is_installed_over_the_package() -> None:
    """The premise of the two tests below. If this fails, they prove nothing.

    ``__wrapped__`` is present only because ``conftest.py`` installed the claw
    hook. Its absence would mean the suite is running unhooked, and
    ``test_beartype_shadows_...`` would be asserting a behaviour nothing produces.
    """
    assert hasattr(gate_cross_section_only, "__wrapped__"), (
        "beartype's import hook is not installed over econflow_engine; "
        "tests/conftest.py:36 is what installs it"
    )
    assert _cross_gate is not gate_cross_section_only


@pytest.mark.parametrize(("argument", "kwargs"), SHADOWED, ids=[c[0] for c in SHADOWED])
def test_the_shipped_gate_refuses_a_wrong_type_with_its_own_code(
    argument: str, kwargs: dict[str, Any]
) -> None:
    """PRODUCTION BEHAVIOUR: no beartype, so the gate's own check is the check.

    Deleting these four checks because "beartype already covers it" would remove
    them from every deployment, since beartype is not a runtime dependency.
    """
    with pytest.raises(GateError) as caught:
        _cross_gate(**kwargs)
    assert caught.value.reason_code == "other", argument
    assert caught.value.detail_code == "gate-argument", argument


@pytest.mark.parametrize(("argument", "kwargs"), SHADOWED, ids=[c[0] for c in SHADOWED])
def test_beartype_shadows_those_four_checks_under_the_test_hook(
    argument: str, kwargs: dict[str, Any]
) -> None:
    """TEST-SESSION BEHAVIOUR, asserted so the difference is documented and pinned.

    ``BeartypeCallHintParamViolation`` subclasses neither ``ValueError`` nor
    ``TypeError``, so it can never be mistaken for a ``GateError``; the
    ``pytest.raises`` below would not catch one.
    """
    assert not issubclass(BeartypeCallHintParamViolation, ValueError)
    with pytest.raises(BeartypeCallHintParamViolation) as caught:
        gate_cross_section_only(**kwargs)
    assert argument in str(caught.value), (
        f"beartype's message must name the offending parameter {argument!r}"
    )


def test_a_clean_cross_section_still_passes_and_reports() -> None:
    """The gate must still ADMIT, or the block cases above prove only that it refuses."""
    rng = np.random.default_rng(0)
    report = gate_cross_section_only(rng.normal(size=200), arg="x", fn="f")
    assert report.decision == "pass"
    assert report.branch == "ljung-box-tested"
    assert len(report.groups) == 1
    assert report.groups[0].tested is True


def test_the_window_detector_still_finds_a_step_and_still_clears_clean_data() -> None:
    """Paired: a built sliding window is detected, an unrelated matrix is not."""
    base = np.arange(30, dtype=float)
    windowed = np.stack([base[i : i + 6] for i in range(10)])
    assert gate_sliding_window_step(windowed) == 1
    rng = np.random.default_rng(1)
    assert gate_sliding_window_step(rng.normal(size=(10, 6))) == 0
