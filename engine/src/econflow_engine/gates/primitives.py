# SPDX-License-Identifier: AGPL-3.0-only
"""The eight refusal primitives every wrapper body calls instead of raising.

WHY A PRIMITIVE RATHER THAN A ``raise`` IN THE BODY. A method precondition --
"this needs at least 30 observations", "this needs a regular frequency" -- is the
same rule in dozens of wrappers across different categories. Written out at each
site it is dozens of independent points of drift in a CORRECTNESS rule, dozens of
message phrasings a client cannot branch on, and dozens of places where somebody
raises the one exception type the pipeline turns into a crash. Written once it is
one rule, one message shape and one code.
``tests/test_gate_discipline.py`` is what keeps it that way: inside
``wrappers/**`` the only permitted ``raise`` is ``NotImplementedError``.

THE VOCABULARY AND THE REFUSAL CONSTRUCTOR LIVE IN
:mod:`~econflow_engine.gates.codes`, one level below this module, because
``require_cross_section`` delegates to
:mod:`~econflow_engine.gates.cross_section` and a shared constant in either of
those two would be a cycle. ``GATE_DETAIL_CODES`` is re-exported here, where the
gate framework's readers look for it.

Every message says WHAT was violated, WHY it matters and WHERE to go. That shape
is the project's rule for a refusal: the user must be shown which rule blocked
the node and what the rule requires, never a stack trace.
"""

from __future__ import annotations

from collections.abc import Sized

import numpy as np
import pandas as pd

from econflow_engine.errors import GateError
from econflow_engine.gates.codes import GATE_DETAIL_CODES, GateDetailCode, refusal
from econflow_engine.gates.cross_section import (
    TIME_INDEX_TYPES,
    gate_cross_section_only,
)

__all__ = [
    "GATE_DETAIL_CODES",
    "require_balanced_panel",
    "require_cross_section",
    "require_full_rank",
    "require_in_range",
    "require_min_length",
    "require_no_missing",
    "require_regular_frequency",
    "require_variance",
]



def _refuse(fn: str, message: str, code: GateDetailCode) -> GateError:
    """Build the one refusal shape. ``fn`` names the node the rule blocked.

    ``code`` is a ``Literal``, so ``mypy --strict`` refuses an undeclared code
    here rather than a test noticing it later.
    """
    return refusal(f"{fn}: {message}", code)


def _numeric_vector(value: object, *, fn: str, arg: str) -> np.ndarray:
    """Reduce an accepted container to ONE numeric vector, or refuse.

    Shared by the numeric primitives so that "what counts as a vector here" is
    answered once. A pandas object is taken by its values; anything that does not
    reduce to a 1-D numeric array is a shape refusal, never a silent coercion.

    THE DTYPE IS CHECKED BEFORE THE CAST, AND THAT ORDER IS THE WHOLE POINT.
    ``np.asarray(value, dtype=float)`` SUCCEEDS on ``["1.0", "2.0"]`` and on a
    boolean column, so casting first would silently admit both -- and this module
    would then disagree with
    :func:`~econflow_engine.gates.cross_section.gate_cross_section_only`, which
    requires a numeric dtype and excludes bool, about the same argument. Measured
    before the fix: ``require_no_missing(["1.0", "2.0", "3.0"])`` passed while the
    cross-section gate refused the same data.

    Booleans are excluded for the reason the cross-section gate excludes them: an
    indicator column has a mean and a variance that are arithmetically valid and
    statistically meaningless to a method expecting a measurement.
    """
    if isinstance(value, pd.Series):
        value = value.to_numpy()
    if isinstance(value, pd.DataFrame):
        raise _refuse(
            fn,
            f'"{arg}" is a DataFrame where a single numeric vector is required. '
            "Select the column the rule applies to and pass that.",
            "precondition-shape",
        )
    array = np.asarray(value)
    if not np.issubdtype(array.dtype, np.number) or np.issubdtype(array.dtype, np.bool_):
        raise _refuse(
            fn,
            f'"{arg}" is not numeric (class: {type(value).__name__}, dtype: '
            f"{array.dtype}); the rule needs numbers to evaluate, and a value that "
            "merely looks like one is not silently converted.",
            "precondition-shape",
        )
    if array.ndim != 1:
        raise _refuse(
            fn,
            f'"{arg}" has {array.ndim} dimension(s) where a single numeric vector is '
            "required.",
            "precondition-shape",
        )
    return array.astype(float)


def require_min_length(value: object, *, minimum: int, fn: str, arg: str) -> None:
    """Refuse an input shorter than the method's documented minimum.

    THE BOUND IS INCLUSIVE: exactly ``minimum`` observations pass. Estimators do
    not fail loudly on a short sample -- they return a number with a standard
    error nobody can trust -- so the length has to be a gate rather than a note.
    """
    if minimum < 1:
        raise _refuse(
            fn,
            f'the gate was given minimum = {minimum} for "{arg}"; a minimum length '
            "is a positive integer.",
            "gate-argument",
        )
    observed = (
        len(value)
        if isinstance(value, Sized)
        else int(_numeric_vector(value, fn=fn, arg=arg).size)
    )
    if observed < minimum:
        raise _refuse(
            fn,
            f'"{arg}" carries {observed} observation(s); this method requires at least '
            f"{minimum}. Below that the estimate is reported with a standard error that "
            "does not describe it. Supply a longer sample, or choose a method the card "
            "lists as admissible at this length.",
            "precondition-sample-size",
        )


def require_no_missing(value: object, *, fn: str, arg: str) -> None:
    """Refuse a missing or non-finite value where the method needs a number.

    ``inf`` is refused alongside ``nan`` deliberately: both are "not a usable
    number", and a library handed an infinity typically returns a plausible
    finite answer computed from a degenerate intermediate rather than raising.
    """
    array = _numeric_vector(value, fn=fn, arg=arg)
    # ONE pass over the data on the passing path. `isnan` then `isinf` is two
    # passes and two boolean temporaries; the split into the two counts only
    # happens on the branch that is about to raise anyway. Measured at n = 1e6:
    # 477 us for the two-pass form against 234 us for this one.
    if not np.all(np.isfinite(array)):
        n_missing = int(np.count_nonzero(np.isnan(array)))
        n_infinite = int(np.count_nonzero(np.isinf(array)))
        raise _refuse(
            fn,
            f'"{arg}" contains {n_missing} missing and {n_infinite} non-finite '
            "value(s). This method has no missing-value rule of its own, so it would "
            "either propagate them into the result or drop them silently and report a "
            "sample size it did not use. Impute or remove them explicitly first.",
            "precondition-missing",
        )


def require_variance(value: object, *, fn: str, arg: str) -> None:
    """Refuse a constant input to a method whose statistic divides by its spread."""
    array = _numeric_vector(value, fn=fn, arg=arg)
    if array.size < 2:
        raise _refuse(
            fn,
            f'"{arg}" carries {array.size} observation(s); variance is undefined below 2.',
            "precondition-sample-size",
        )
    if float(np.var(array, ddof=1)) <= 0.0:
        raise _refuse(
            fn,
            f'"{arg}" is constant (zero variance). Every statistic this method reports '
            "is scaled by the spread of the input, so a constant column yields a "
            "division by zero or a silently meaningless number. Remove the column, or "
            "check that the right variable was passed.",
            "precondition-degenerate",
        )


def require_regular_frequency(value: object, *, fn: str, arg: str) -> None:
    """Refuse an irregularly spaced time index to a method that assumes even steps.

    Lag operators, differencing and every spectral method are defined on a FIXED
    step. Handed a gapped index they compute over positions rather than over
    time, and the result reads as ordinary output.

    REGULARITY IS A CALENDAR QUESTION, NOT AN ARITHMETIC ONE -- measured against
    pandas 3.0.5 before this rule was written. A month-end index has steps of 28,
    29, 30 and 31 days, and a business-day index has steps of 1 and 3; both are
    perfectly regular, and a gate that compared raw nanosecond differences would
    refuse most of macroeconomics. So the answer comes from
    :func:`pandas.infer_freq`, which is calendar-aware.

    A ``PeriodIndex`` takes the other branch, and the reason is a trap:
    ``infer_freq`` REFUSES one outright (``TypeError: PeriodIndex given``), while
    its ``.freq`` attribute is the period UNIT and stays set even on a gapped
    index -- ``PeriodIndex(['2020-01', '2020-02', '2020-05'])`` reports
    ``<MonthEnd>``. Its ordinals already count in calendar units, so there the
    arithmetic difference IS the right test: ``[1, 1, 1]`` against ``[1, 3]``.
    """
    index = value if isinstance(value, pd.Index) else getattr(value, "index", None)
    # TIME_INDEX_TYPES rather than a second inline isinstance tuple: the
    # cross-section gate already owns the answer to "does this object carry
    # time", and two copies is how a Timedelta index ends up refused by one gate
    # and unseen by the other.
    if not isinstance(index, TIME_INDEX_TYPES):
        raise _refuse(
            fn,
            f'"{arg}" carries no time index (found: {type(index).__name__}); this '
            "method is defined on a dated series with a fixed step.",
            "precondition-shape",
        )
    if len(index) < 3:
        raise _refuse(
            fn,
            f'"{arg}" carries {len(index)} observation(s); a frequency is not '
            "determined below 3.",
            "precondition-sample-size",
        )
    if isinstance(index, pd.PeriodIndex):
        # `.astype("int64")` rather than the equivalent `.asi8`: pandas-stubs does
        # not declare `asi8` on PeriodIndex, so mypy --strict rejects it while it
        # works perfectly at run time. Both were probed on pandas 3.0.5 and return
        # the same ordinals -- [1, 1, 1] regular against [1, 3] gapped.
        steps = np.unique(np.diff(np.asarray(index.astype("int64"))))
        regular = steps.size == 1
        found = f"{steps.size} distinct steps between consecutive periods"
    else:
        regular = pd.infer_freq(index) is not None
        found = "pandas can infer no frequency from the dates"
    if not regular:
        raise _refuse(
            fn,
            f'"{arg}" is not regularly spaced ({found}). Lags, differences and every '
            "spectral quantity this method computes are defined on a FIXED step, so on "
            "a gapped index they would be taken over positions and reported as if taken "
            "over time. Resample to a regular frequency first.",
            "precondition-frequency",
        )


def require_in_range(value: float, *, low: float, high: float, fn: str, arg: str) -> None:
    """Refuse a parameter outside its admissible interval. BOTH BOUNDS INCLUSIVE."""
    if low > high:
        raise _refuse(
            fn,
            f'the gate was given low = {low} above high = {high} for "{arg}".',
            "gate-argument",
        )
    if isinstance(value, bool) or not isinstance(value, float | int):
        raise _refuse(
            fn,
            f'"{arg}" is not a number (class: {type(value).__name__}).',
            "precondition-shape",
        )
    if not low <= float(value) <= high:
        raise _refuse(
            fn,
            f'"{arg}" = {value} lies outside [{low}, {high}], the interval on which '
            "this method is defined. Outside it the quantity either does not exist or "
            "is computed from an expression the method never validates.",
            "precondition-domain",
        )


def require_full_rank(value: object, *, fn: str, arg: str) -> None:
    """Refuse a rank-deficient design to a method that inverts a cross-product.

    A collinear column makes the normal equations singular. Numerical linear
    algebra rarely says so: it returns coefficients from a pseudo-inverse, and
    those coefficients are not identified.
    """
    frame = value.to_numpy() if isinstance(value, pd.DataFrame) else value
    array = np.asarray(frame, dtype=float)
    if array.ndim != 2:
        raise _refuse(
            fn,
            f'"{arg}" has {array.ndim} dimension(s) where a 2-D design matrix is '
            "required.",
            "precondition-shape",
        )
    n_rows, n_columns = array.shape
    if n_columns < 1:
        raise _refuse(fn, f'"{arg}" has no columns.', "precondition-shape")
    rank = int(np.linalg.matrix_rank(array))
    if rank < n_columns:
        raise _refuse(
            fn,
            f'"{arg}" has rank {rank} over {n_columns} column(s) '
            f"({n_rows} row(s)): at least one column is a linear combination of the "
            "others. The cross-product this method inverts is singular, and the "
            "coefficients a pseudo-inverse returns are not identified. Drop the "
            "redundant column, or add the observations that would separate them.",
            "precondition-rank",
        )


def require_balanced_panel(
    value: object, *, unit: str, period: str, fn: str, arg: str
) -> None:
    """Refuse an unbalanced panel to a method whose estimator assumes a full grid.

    Refuses a duplicated (unit, period) pair for the same reason: it is the other
    way the grid fails to be a grid, and it silently doubles a unit's weight.
    """
    if not isinstance(value, pd.DataFrame):
        raise _refuse(
            fn,
            f'"{arg}" is a {type(value).__name__} where a panel DataFrame is required.',
            "precondition-shape",
        )
    missing_columns = [c for c in (unit, period) if c not in value.columns]
    if missing_columns:
        raise _refuse(
            fn,
            f'"{arg}" has no column(s) {missing_columns}; the panel gate was told to '
            f'index it by unit "{unit}" and period "{period}".',
            "gate-argument",
        )
    units = value[unit].unique()
    periods = value[period].unique()
    expected = len(units) * len(periods)
    if len(value) != expected:
        raise _refuse(
            fn,
            f'"{arg}" is not a balanced panel: {len(units)} unit(s) x '
            f"{len(periods)} period(s) = {expected} expected rows, {len(value)} present. "
            "This method's estimator is defined on the full grid, so a hole or a "
            "duplicate shifts the weight each unit carries without reporting it. "
            "Balance the panel, or choose a method the card lists as admissible on an "
            "unbalanced one.",
            "precondition-panel",
        )


def require_cross_section(
    value: object, *, fn: str, arg: str, gate_alpha: float = 0.05, ordered: bool = True
) -> None:
    """Refuse time-ordered data to a cross-section-only method.

    The framework face of :func:`econflow_engine.gates.cross_section.gate_cross_section_only`,
    which does the work and already raises ``GateError`` under the codes of this
    set. Call that one directly when the body needs the diagnostics report; call
    this one when the body only needs the refusal.
    """
    gate_cross_section_only(value, arg=arg, fn=fn, gate_alpha=gate_alpha, ordered=ordered)
