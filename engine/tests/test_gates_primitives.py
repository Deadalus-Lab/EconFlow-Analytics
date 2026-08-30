# SPDX-License-Identifier: AGPL-3.0-only
"""The eight gate primitives: one PASS test and one BLOCK test for each.

WHY A PAIR PER PRIMITIVE. A gate with only a block test can be a function that
refuses everything, and a gate with only a pass test can be a function that
refuses nothing; neither failure shows up in a suite that carries one half. The
block half asserts the EXACT ``detail_code``, not merely that something was
raised -- a refusal that reaches the caller under the wrong code is a refusal the
caller cannot branch on, which is the entire reason the code exists.

WHY THE REASON CODE IS ALWAYS ``other``. ``artifacts/parity-fixtures.json``
carries the 18-name ``reason_codes`` list as the wire contract and
``tests/parity/test_parity.py`` asserts membership against it. That artifact is a
frozen input, so a nineteenth reason code cannot be added without re-sealing a
corpus that records verdicts this box does not touch. ``detail_code`` is the
extensible half and carries the diagnosis instead.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from econflow_engine.errors import ENGINE_REASON_CODES, GateError
from econflow_engine.gates import (
    GATE_DETAIL_CODES,
    require_balanced_panel,
    require_cross_section,
    require_full_rank,
    require_in_range,
    require_min_length,
    require_no_missing,
    require_regular_frequency,
    require_variance,
)
from econflow_engine.gates.registry import PRIMITIVES
from tests.support import as_shipped


def test_the_detail_codes_do_not_collide_with_the_wire_reason_codes() -> None:
    """The two vocabularies must stay disjoint, or a detail code reads as a reason.

    ``GateError`` defaults ``detail_code`` to ``reason_code``, so a name present in
    both sets would be indistinguishable from an ordinary wire refusal by anything
    that reads the finer field.
    """
    assert set(GATE_DETAIL_CODES).isdisjoint(ENGINE_REASON_CODES), (
        "a gate detail code collides with a wire reason code: "
        f"{sorted(set(GATE_DETAIL_CODES) & set(ENGINE_REASON_CODES))}"
    )


def test_the_detail_code_set_is_not_empty_and_has_no_duplicates() -> None:
    """A closed set that is empty, or that repeats itself, is not a closed set."""
    assert len(GATE_DETAIL_CODES) >= 8
    assert len(set(GATE_DETAIL_CODES)) == len(GATE_DETAIL_CODES)


def test_every_registered_primitive_declares_a_code_from_the_set() -> None:
    """The registry keys ARE detail codes; an unlisted key is an unreachable rule."""
    unlisted = sorted(set(PRIMITIVES) - set(GATE_DETAIL_CODES))
    assert not unlisted, f"registry keys absent from GATE_DETAIL_CODES: {unlisted}"


# --------------------------------------------------------------------------
# require_min_length -- precondition-sample-size
# --------------------------------------------------------------------------


def test_min_length_passes_at_the_boundary() -> None:
    """Exactly the minimum is enough; the bound is inclusive and stated as such."""
    require_min_length([1.0, 2.0, 3.0], minimum=3, fn="f", arg="x")  # must not raise


def test_min_length_blocks_below_the_minimum() -> None:
    with pytest.raises(GateError) as caught:
        require_min_length([1.0, 2.0], minimum=3, fn="f", arg="x")
    assert caught.value.detail_code == "precondition-sample-size"
    assert caught.value.reason_code == "other"
    assert "f:" in str(caught.value)
    assert '"x"' in str(caught.value)


# --------------------------------------------------------------------------
# require_no_missing -- precondition-missing
# --------------------------------------------------------------------------


def test_no_missing_passes_on_finite_numbers() -> None:
    require_no_missing([1.0, 2.0, 3.0], fn="f", arg="x")  # must not raise


def test_no_missing_blocks_a_nan() -> None:
    with pytest.raises(GateError) as caught:
        require_no_missing([1.0, np.nan, 3.0], fn="f", arg="x")
    assert caught.value.detail_code == "precondition-missing"


@pytest.mark.parametrize(
    ("label", "value"),
    [
        ("numeric strings", ["1.0", "2.0", "3.0"]),
        ("a boolean list", [True, False, True]),
        ("a boolean Series", pd.Series([True, False, True])),
    ],
)
def test_the_numeric_primitives_refuse_what_merely_looks_numeric(
    label: str, value: object
) -> None:
    """REGRESSION. ``np.asarray(v, dtype=float)`` SUCCEEDS on both of these.

    The first version of ``_numeric_vector`` cast before checking the dtype, so
    ``require_no_missing(["1.0", "2.0", "3.0"])`` PASSED while
    ``gate_cross_section_only`` refused the same data -- two verdicts on one
    argument from one framework, and a string or indicator column reaching an
    estimator through whichever gate the wrapper happened to call first.

    Reproduce the old behaviour::

        python -c "import numpy as np; print(np.asarray(['1.0','2.0'], dtype=float))"
        # [1. 2.]   <- the cast that used to happen before any dtype check
    """
    with pytest.raises(GateError) as caught:
        require_no_missing(value, fn="f", arg="x")
    assert caught.value.detail_code == "precondition-shape", label


def test_no_missing_blocks_an_infinity() -> None:
    """Non-finite is the same class of defect as missing: not a usable number."""
    with pytest.raises(GateError) as caught:
        require_no_missing([1.0, np.inf, 3.0], fn="f", arg="x")
    assert caught.value.detail_code == "precondition-missing"


# --------------------------------------------------------------------------
# require_variance -- precondition-degenerate
# --------------------------------------------------------------------------


def test_variance_passes_on_a_varying_series() -> None:
    require_variance([1.0, 2.0, 3.0], fn="f", arg="x")  # must not raise


def test_variance_blocks_a_constant_series() -> None:
    with pytest.raises(GateError) as caught:
        require_variance([2.0, 2.0, 2.0], fn="f", arg="x")
    assert caught.value.detail_code == "precondition-degenerate"


def test_variance_blocks_a_constant_series_whose_value_is_not_a_dyadic_rational() -> None:
    """THE HOLE THE VARIANCE ARM ALONE LEFT, and it is a floating-point one.

    MEASURED: ``np.var(np.full(38, 0.3), ddof=1)`` is 1.2659085472296641e-32
    rather than zero, because the mean it subtracts was reached by summation and
    0.3 is not exactly representable. The same 38 rows at 0.5 give exactly 0.0.
    Before the exact arm was added beside it this rule refused the second and
    admitted the first -- one constant vector refused and another admitted, on
    nothing but whether the value is a power of two.
    """
    constant = np.full(38, 0.3)
    assert float(np.var(constant, ddof=1)) > 0.0
    with pytest.raises(GateError) as caught:
        require_variance(constant, fn="f", arg="x")
    assert caught.value.detail_code == "precondition-degenerate"
    assert "constant (zero variance)" in str(caught.value)


def test_variance_still_blocks_a_spread_that_underflows_without_the_values_being_equal(
) -> None:
    """WHY THE VARIANCE ARM STAYS, on the witness that actually exercises it.

    ``min != max`` here and the spread is still zero to double precision, so the
    exact arm admits it and only the variance arm refuses it. THE WITNESS HAD TO BE
    CORRECTED: this test was first written with ``[1.0, 1.0 + 1e-300]``, and
    ``1e-300`` is far below the spacing of 1.0 -- that literal IS ``[1.0, 1.0]``,
    so the test passed through the NEW arm while claiming to defend the old one.
    Measured, which is why the premise is asserted here rather than described.

    THE ERROR STATE IS RELAXED FOR THE CALL, and that is the finding rather than a
    convenience. Under ``np.seterr(all='raise')`` -- the state ``tests/conftest.py``
    installs for this whole suite -- ``np.var`` on this witness raises
    ``FloatingPointError: underflow encountered in square`` before the gate can
    answer, so the arm has no reachable witness there at all. That is a
    pre-existing property of ``require_variance`` computing an unguarded variance,
    not something either arm introduced, and it is pinned here rather than hidden.
    """
    witness = [1e-162, 1.5e-162]
    array = np.asarray(witness)
    assert float(np.min(array)) != float(np.max(array))
    with np.errstate(under="ignore"):
        assert float(np.var(array, ddof=1)) == 0.0
        with pytest.raises(GateError) as caught:
            require_variance(witness, fn="f", arg="x")
    assert caught.value.detail_code == "precondition-degenerate"

    with pytest.raises(FloatingPointError, match="underflow"), np.errstate(under="raise"):
        require_variance(witness, fn="f", arg="x")


# --------------------------------------------------------------------------
# require_regular_frequency -- precondition-frequency
# --------------------------------------------------------------------------


def test_regular_frequency_passes_on_an_evenly_spaced_index() -> None:
    series = pd.Series(
        [1.0, 2.0, 3.0], index=pd.date_range("2020-01-31", periods=3, freq="ME")
    )
    require_regular_frequency(series, fn="f", arg="x")  # must not raise


def test_regular_frequency_blocks_a_gap() -> None:
    index = pd.DatetimeIndex(["2020-01-01", "2020-01-02", "2020-01-09"])
    with pytest.raises(GateError) as caught:
        require_regular_frequency(pd.Series([1.0, 2.0, 3.0], index=index), fn="f", arg="x")
    assert caught.value.detail_code == "precondition-frequency"


# --------------------------------------------------------------------------
# require_in_range -- precondition-domain
# --------------------------------------------------------------------------


def test_in_range_passes_inside_the_interval() -> None:
    require_in_range(0.05, low=0.0, high=1.0, fn="f", arg="alpha")  # must not raise


def test_in_range_blocks_outside_the_interval() -> None:
    with pytest.raises(GateError) as caught:
        require_in_range(1.5, low=0.0, high=1.0, fn="f", arg="alpha")
    assert caught.value.detail_code == "precondition-domain"


def test_in_range_blocks_a_non_number_in_the_shipped_function() -> None:
    """``value: float`` is the one primitive annotation beartype shadows.

    Called through ``as_shipped`` for the reason set out in ``tests.support``:
    beartype is a dev-only dependency, so in a deployment this branch is the
    check, and asserting the hook's outcome would assert something no deployment
    produces.
    """
    with pytest.raises(GateError) as caught:
        as_shipped(require_in_range)(
            "a",  # type: ignore[arg-type]  # the wrong type IS the case under test
            low=0.0,
            high=1.0,
            fn="f",
            arg="alpha",
        )
    assert caught.value.detail_code == "precondition-shape"


def test_in_range_refuses_an_inverted_interval_as_author_error() -> None:
    """A bound the author got backwards is never reported as the user's data."""
    with pytest.raises(GateError) as caught:
        require_in_range(0.5, low=1.0, high=0.0, fn="f", arg="alpha")
    assert caught.value.detail_code == "gate-argument"


# --------------------------------------------------------------------------
# require_full_rank -- precondition-rank
# --------------------------------------------------------------------------


def test_full_rank_passes_on_independent_columns() -> None:
    design = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
    require_full_rank(design, fn="f", arg="X")  # must not raise


def test_full_rank_blocks_a_collinear_column() -> None:
    design = np.array([[1.0, 2.0], [2.0, 4.0], [3.0, 6.0]])
    with pytest.raises(GateError) as caught:
        require_full_rank(design, fn="f", arg="X")
    assert caught.value.detail_code == "precondition-rank"


# --------------------------------------------------------------------------
# require_balanced_panel -- precondition-panel
# --------------------------------------------------------------------------


def test_balanced_panel_passes_when_every_unit_has_every_period() -> None:
    frame = pd.DataFrame(
        {"id": ["a", "a", "b", "b"], "t": [1, 2, 1, 2], "y": [1.0, 2.0, 3.0, 4.0]}
    )
    require_balanced_panel(frame, unit="id", period="t", fn="f", arg="data")  # must not raise


def test_balanced_panel_blocks_a_missing_cell() -> None:
    frame = pd.DataFrame({"id": ["a", "a", "b"], "t": [1, 2, 1], "y": [1.0, 2.0, 3.0]})
    with pytest.raises(GateError) as caught:
        require_balanced_panel(frame, unit="id", period="t", fn="f", arg="data")
    assert caught.value.detail_code == "precondition-panel"


# --------------------------------------------------------------------------
# require_cross_section -- precondition-cross-section
# --------------------------------------------------------------------------


def test_cross_section_passes_on_unordered_numbers() -> None:
    rng = np.random.default_rng(0)
    require_cross_section(rng.normal(size=200), fn="f", arg="x")  # must not raise


def test_cross_section_blocks_a_dated_object() -> None:
    """A pandas object stamped with time is never a cross-section, whatever else holds."""
    series = pd.Series(
        [1.0, 2.0, 3.0], index=pd.date_range("2020-01-01", periods=3, freq="D")
    )
    with pytest.raises(GateError) as caught:
        require_cross_section(series, fn="f", arg="x")
    assert caught.value.detail_code == "precondition-cross-section"
