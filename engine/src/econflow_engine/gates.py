# SPDX-License-Identifier: AGPL-3.0-only
"""Cross-cutting L1 gates: the checks every wrapper body may assume have run.

WHAT THIS IS: the shared, pure, hard input-validity rules that MANY wrappers
across DIFFERENT categories need. Exactly as :mod:`econflow_engine.serialize` is
the ONE serialisation, this is the once-written validity rule. Copying it into
each caller would mean three independent points of drift in a CORRECTNESS rule.

EXACTLY TWO PUBLIC FUNCTIONS -- the same two the contract exports:

``gate_cross_section_only``
    normative gate 4. Refuses data that carries time order to a method that
    assumes a cross-section.
``gate_sliding_window_step``
    normative gate 1 (Keogh). A DETECTOR, NOT a blocker: it returns the step
    ``k`` (0 = clean) and the caller raises.

PRINCIPLES:

* pure   -- no mutation, no printing, no plotting, no transport.
* total  -- every unsupported type raises. NEVER a silent pass-through.
* hard   -- failure raises with an EDUCATIONAL message: what, why, where to go.
* numeric-out -- returns purely numeric diagnostics, ready to serialise.

THE COST OF THE LJUNG-BOX BRANCH, STATED EXPLICITLY: it is a test of size
``gate_alpha``, so BY CONSTRUCTION it blocks about ``gate_alpha`` of genuinely
i.i.d. input. Live-measured on the engine 4.6.1 over 5000 replications of ``rnorm``:
n = 200 -> 1.6% (0.01), 5.7% (0.05), 10.1% (0.10); n = 60 -> 2.3%, 6.7%, 10.8%.
That is why the level is the GATE'S OWN and does not inherit the caller's alpha,
and why ``ordered=False`` exists as an explicit escape for genuinely unordered
data.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any

import numpy as np
import pandas as pd
from scipy import stats

__all__ = [
    "CrossSectionReport",
    "GroupDiagnostics",
    "gate_cross_section_only",
    "gate_sliding_window_step",
]

_HAC_POINTER = (
    'For time-dependent data use the existing HAC path '
    "(category 07-causality-policy -- wrap_vcov_hac / wrap_vcov_cl / wrap_vcov_panel)."
)
_WHY_CROSS_SECTION = (
    "The node is CROSS-SECTION ONLY. Autocorrelation INFLATES the Type I error "
    "(it shrinks the variance estimator), so the test's p-values come out falsely "
    f"significant. {_HAC_POINTER}"
)


@dataclass(frozen=True, slots=True)
class GroupDiagnostics:
    """Per-group Ljung-Box diagnostics. ``NaN`` statistics mean 'not tested'."""

    name: str
    statistic: float
    p_value: float
    lag: int
    n: int
    n_na: int
    tested: bool


@dataclass(frozen=True, slots=True)
class CrossSectionReport:
    groups: tuple[GroupDiagnostics, ...]
    gate_alpha: float
    ordered: bool
    branch: str
    decision: str


def _prefix(fn: str) -> str:
    return f"{fn}: " if fn else ""


def _one_string(value: object, name: str) -> str:
    if not isinstance(value, str):
        raise ValueError(f'gate_cross_section_only: "{name}" must be ONE string.')
    return value


def _has_time_index(obj: object) -> str | None:
    """Return the offending index type when a pandas object carries TIME order.

    A dated object can announce itself in many ways, and a check that enumerates
    them is a check that goes stale. pandas has ONE mechanism -- a temporal
    index -- so the check collapses to it, and it remains a CLASS
    check: an object explicitly stamped with time is never a cross-section,
    regardless of ``ordered``.
    """
    index = getattr(obj, "index", None)
    if isinstance(index, pd.DatetimeIndex | pd.PeriodIndex | pd.TimedeltaIndex):
        return type(index).__name__
    return None


def _reject_time_series(obj: object, what: str, label: str) -> None:
    hit = _has_time_index(obj)
    if hit is not None:
        raise ValueError(
            f'{label}cross-section-only gate -- "{what}" is a TIME SERIES object '
            f"(index: {hit}; branch: class-rejected). This applies REGARDLESS of "
            f'"ordered": an object explicitly stamped with time is never a '
            f"cross-section. {_WHY_CROSS_SECTION}"
        )


def _fill_names(
    names: Sequence[object] | None, k: int, arg: str, open_: str, close: str
) -> list[str]:
    out: list[str] = []
    for i in range(k):
        raw = None if names is None else names[i]
        text = "" if raw is None else str(raw)
        out.append(text if text else f"{arg}{open_}{i + 1}{close}")
    return out


def _groups_of(x: object, arg: str, label: str) -> dict[str, np.ndarray]:  # noqa: C901
    """Reduce any accepted container to named numeric vectors. Total by design."""
    _reject_time_series(x, arg, label)

    if isinstance(x, pd.DataFrame):
        names = _fill_names(list(x.columns), x.shape[1], arg, "[[", "]]")
        for name, column in zip(names, (x[c] for c in x.columns), strict=True):
            _reject_time_series(column, f"{arg}${name}", label)
        numeric = [
            (name, x[col]) for name, col in zip(names, x.columns, strict=True)
            if pd.api.types.is_numeric_dtype(x[col]) and not pd.api.types.is_bool_dtype(x[col])
        ]
        if not numeric:
            raise ValueError(
                f'{label}cross-section-only gate -- "{arg}" (DataFrame) has no numeric '
                "column to check."
            )
        return {name: np.asarray(col, dtype=float) for name, col in numeric}

    if isinstance(x, pd.Series):
        if not pd.api.types.is_numeric_dtype(x):
            raise ValueError(
                f'{label}cross-section-only gate -- the Series "{arg}" is not numeric '
                f"(dtype: {x.dtype})."
            )
        return {arg: np.asarray(x, dtype=float)}

    if isinstance(x, np.ndarray) and x.ndim == 2:
        if not np.issubdtype(x.dtype, np.number):
            raise ValueError(
                f'{label}cross-section-only gate -- the matrix "{arg}" is not numeric '
                f"(dtype: {x.dtype})."
            )
        if x.shape[1] < 1:
            raise ValueError(
                f'{label}cross-section-only gate -- the matrix "{arg}" has no columns.'
            )
        names = _fill_names(None, x.shape[1], arg, "[,", "]")
        return {names[j]: np.asarray(x[:, j], dtype=float) for j in range(x.shape[1])}

    if isinstance(x, Mapping):
        if not x:
            raise ValueError(f'{label}cross-section-only gate -- the mapping "{arg}" is empty.')
        return {
            str(k): _one_numeric_vector(v, str(k), arg, label) for k, v in x.items()
        }

    if isinstance(x, list | tuple):
        if not x:
            raise ValueError(f'{label}cross-section-only gate -- the list "{arg}" is empty.')
        if all(isinstance(v, int | float | np.floating | np.integer) for v in x):
            return {arg: np.asarray(x, dtype=float)}
        names = _fill_names(None, len(x), arg, "[[", "]]")
        return {
            names[j]: _one_numeric_vector(v, names[j], arg, label) for j, v in enumerate(x)
        }

    if isinstance(x, np.ndarray) and x.ndim == 1 and np.issubdtype(x.dtype, np.number):
        return {arg: np.asarray(x, dtype=float)}

    raise ValueError(
        f'{label}cross-section-only gate -- unsupported type for "{arg}" '
        f"(class: {type(x).__name__}). Accepted: a numeric vector, a numeric 2-D array, "
        "a sequence or mapping of numeric vectors, or a DataFrame with numeric columns."
    )


def _one_numeric_vector(value: object, name: str, arg: str, label: str) -> np.ndarray:
    _reject_time_series(value, name, label)
    array = np.asarray(value)
    if array.ndim != 1 or not np.issubdtype(array.dtype, np.number):
        raise ValueError(
            f'{label}cross-section-only gate -- the element "{name}" of "{arg}" is not a '
            f"numeric vector (class: {type(value).__name__})."
        )
    return array.astype(float)


def _ljung_box(values: np.ndarray, lag: int) -> tuple[float, float]:
    """The Ljung-Box portmanteau test with ``fitdf = 0``.

    Written out rather than delegated, so the autocorrelation estimator is the
    SAME one the reference uses: ``acf`` divides every lag by the FULL sum of
    squares, which is what makes Q comparable across lags.
    """
    n = values.size
    centred = values - values.mean()
    denominator = float(np.dot(centred, centred))
    numerators = np.array(
        [float(np.dot(centred[: n - k], centred[k:])) for k in range(1, lag + 1)]
    )
    rho = numerators / denominator
    weights = 1.0 / np.arange(n - 1, n - lag - 1, -1, dtype=float)
    statistic = float(n * (n + 2) * np.sum(weights * rho**2))
    # fitdf = 0: the input is DATA, not model residuals.
    p_value = float(stats.chi2.sf(statistic, lag))
    return statistic, p_value


def _diagnose(
    values: np.ndarray, name: str, lb_lag: int | None, label: str, arg: str, run_lb: bool
) -> GroupDiagnostics:
    n_bad = int(np.count_nonzero(np.isinf(values)))
    if n_bad:
        raise ValueError(
            f'{label}cross-section-only gate -- group "{name}" of "{arg}" contains {n_bad} '
            "non-finite values (inf). The Ljung-Box statistic does not handle them and "
            "would return a silently wrong p-value."
        )
    n_na = int(np.count_nonzero(np.isnan(values)))
    clean = values[~np.isnan(values)]
    n = clean.size
    if n < 3:
        raise ValueError(
            f'{label}cross-section-only gate -- group "{name}" of "{arg}" has n = {n} valid '
            f"observations (after removing {n_na} missing); the minimum is 3."
        )
    if float(np.var(clean, ddof=1)) <= 0:
        raise ValueError(
            f'{label}cross-section-only gate -- group "{name}" of "{arg}" is constant (zero '
            "variance). The Ljung-Box statistic is undefined on such input."
        )
    untested = GroupDiagnostics(name, float("nan"), float("nan"), 0, n, n_na, False)
    if not run_lb:
        return untested
    if n < 5 and lb_lag is None:
        # min(10, n // 5) would give lag < 1: an EXPLICIT "not tested", never a
        # silent pass -- the caller may surface it.
        return untested
    lag = min(10, n // 5) if lb_lag is None else lb_lag
    if lag >= n:
        raise ValueError(
            f'{label}cross-section-only gate -- lb_lag = {lag} >= n = {n} in group "{name}" '
            f'of "{arg}"; Ljung-Box requires lag < n.'
        )
    statistic, p_value = _ljung_box(clean, lag)
    return GroupDiagnostics(name, statistic, p_value, lag, n, n_na, True)


def gate_cross_section_only(
    x: object,
    arg: str = "x",
    fn: str = "",
    lb_lag: int | None = None,
    gate_alpha: float = 0.05,
    ordered: bool = True,
) -> CrossSectionReport:
    """Refuse time-ordered data to a cross-section-only method.

    Twelve hard stops, in the order the engine original applies them:

    1. ``arg`` / ``fn`` not a single string.
    2. ``gate_alpha`` outside (0, 1), or not a single number.
    3. ``ordered`` not a single boolean.
    4. ``lb_lag`` neither ``None`` nor a positive integer.
    5. ``lb_lag`` given TOGETHER with ``ordered=False`` -- contradictory, and it
       would be a silent no-op.
    6. the input (or a column / element) carries a TIME index, REGARDLESS of
       ``ordered``.
    7. a DataFrame with no numeric column, a non-numeric matrix, a matrix with no
       columns, an empty sequence, a non-numeric element, an unsupported type.
    8. an infinite value in a group (the statistic would be silently wrong).
    9. fewer than 3 valid observations after dropping missing values.
    10. zero variance.
    11. ``lb_lag >= n``.
    12. a Ljung-Box p-value below ``gate_alpha`` -- REJECTION, reported with the
        statistic, the lag, n, the HAC pointer and the ``ordered=False`` escape.

    Checks 8-10 run EVEN WITH ``ordered=False``: declaring "no order" skips ONLY
    the Ljung-Box, nothing else. Missing values are removed, COUNTED and
    reported (``n_na``) -- never dropped silently.
    """
    arg = _one_string(arg, "arg")
    fn = _one_string(fn, "fn")
    label = _prefix(fn)
    if not isinstance(gate_alpha, float | int) or isinstance(gate_alpha, bool):
        raise ValueError('gate_cross_section_only: "gate_alpha" must be ONE number in (0, 1).')
    if not 0 < float(gate_alpha) < 1:
        raise ValueError('gate_cross_section_only: "gate_alpha" must be ONE number in (0, 1).')
    if not isinstance(ordered, bool):
        raise ValueError(
            'gate_cross_section_only: "ordered" must be ONE True/False (an EXPLICIT '
            "declaration: do the rows carry ORDER meaning?)."
        )
    if lb_lag is not None:
        if isinstance(lb_lag, bool) or not isinstance(lb_lag, int) or lb_lag < 1:
            raise ValueError(
                'gate_cross_section_only: "lb_lag" must be None or ONE positive integer.'
            )
        if not ordered:
            raise ValueError(
                'gate_cross_section_only: "lb_lag" was given TOGETHER with ordered=False -- '
                "CONTRADICTORY: with ordered=False the Ljung-Box precheck does not run, so "
                '"lb_lag" would be a silent no-op. Declare ordered=True or omit "lb_lag".'
            )

    groups = _groups_of(x, arg, label)
    diagnostics = tuple(
        _diagnose(values, name, lb_lag, label, arg, run_lb=ordered)
        for name, values in groups.items()
    )

    rejected = [g for g in diagnostics if g.tested and not np.isnan(g.p_value)
                and g.p_value < gate_alpha]
    if rejected:
        worst = min(rejected, key=lambda g: g.p_value)
        raise ValueError(
            f'{label}cross-section-only gate -- "{arg}" WAS REJECTED by the Ljung-Box '
            f'whiteness precheck: group "{worst.name}" shows statistically significant '
            f"autocorrelation (X-squared = {worst.statistic:.6g}, lag = {worst.lag}, "
            f"p-value = {worst.p_value:.6g} < gate_alpha = {gate_alpha}, n = {worst.n}). "
            "IF the rows do NOT carry order (a genuine cross-section), declare it "
            f"EXPLICITLY with ordered=False. {_WHY_CROSS_SECTION}"
        )

    return CrossSectionReport(
        groups=diagnostics,
        gate_alpha=float(gate_alpha),
        ordered=ordered,
        branch="ljung-box-tested" if ordered else "skipped-by-declaration",
        decision=(
            "pass-unordered"
            if not ordered
            else ("pass" if all(g.tested for g in diagnostics) else "pass-untested")
        ),
    )


def _shift_matches(matrix: np.ndarray, a_cols: slice, b_cols: slice, tol: float) -> bool:
    """PER-ELEMENT tolerance, NEVER mean-relative: ``|a-b| <= tol*max(|a|,|b|,1)``.

    A mean-relative test passes on a panel whose average magnitude is large while
    individual cells disagree wildly, which is exactly the case this gate exists
    to catch.
    """
    a = matrix[:-1, a_cols]
    b = matrix[1:, b_cols]
    diff = np.abs(a - b)
    if not np.all(np.isfinite(diff)):
        return False
    bound = tol * np.maximum(np.maximum(np.abs(a), np.abs(b)), 1.0)
    return bool(np.all(diff <= bound))


def gate_sliding_window_step(
    matrix: Any, max_step: int | None = None, tol: float = 1e-12
) -> int:
    """Detect sliding-window construction. Returns the step ``k``; 0 means clean.

    A DETECTOR, not a blocker -- the caller decides. Generalised beyond k = 1:
    the step is a free parameter of how the subsequences were built, so a step-2
    window is covered by the Keogh, Lin & Truppel result just as much as a step-1
    one. Every fixed step in ``[1, min(floor(m/2), m-2)]`` is checked.
    """
    array = np.asarray(matrix)
    if array.ndim != 2 or not np.issubdtype(array.dtype, np.number):
        raise ValueError(
            'gate_sliding_window_step: "matrix" must be a NUMERIC 2-D array '
            "(objects in rows, features in columns)."
        )
    if isinstance(tol, bool) or not isinstance(tol, float | int) or tol < 0:
        raise ValueError('gate_sliding_window_step: "tol" must be ONE non-negative number.')
    n, m = array.shape
    if n < 3 or m < 3:
        return 0
    if max_step is None:
        k_max = m // 2
    else:
        if isinstance(max_step, bool) or not isinstance(max_step, int) or max_step < 1:
            raise ValueError(
                'gate_sliding_window_step: "max_step" must be None or ONE positive integer.'
            )
        k_max = max_step
    k_max = min(k_max, m - 2)
    values = array.astype(float)
    for k in range(1, k_max + 1):
        tail = slice(k, m)
        head = slice(0, m - k)
        if _shift_matches(values, tail, head, float(tol)) or _shift_matches(
            values, head, tail, float(tol)
        ):
            return k
    return 0
