# SPDX-License-Identifier: AGPL-3.0-only
"""Normative gate 4: refuse data that carries time order to a cross-section method.

EVERY REFUSAL IS A ``GateError``. It was a bare ``ValueError`` until box 2.1.4,
which meant the one exception type ``make_tool`` turns into a clean refusal was
the one type this module did not raise: a violation reached the caller as a
crash, with no reason code to branch on. See :mod:`econflow_engine.gates.primitives`
for why ``reason_code`` stays ``"other"`` and the diagnosis lives in
``detail_code``.

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

import numpy as np
import pandas as pd
from scipy import stats

from econflow_engine.errors import GateError
from econflow_engine.gates.codes import GateDetailCode, refusal

__all__ = [
    "TIME_INDEX_TYPES",
    "CrossSectionReport",
    "GroupDiagnostics",
    "gate_cross_section_only",
]

#: The ONE answer to "does this pandas object carry time order". pandas has a
#: single mechanism -- a temporal index -- so the check collapses to these three
#: classes, and it is named here rather than re-typed at each site.
TIME_INDEX_TYPES = (pd.DatetimeIndex, pd.PeriodIndex, pd.TimedeltaIndex)

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
        raise _refuse(
            f'gate_cross_section_only: "{name}" must be ONE string.',
            "gate-argument",
        )
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
    if isinstance(index, TIME_INDEX_TYPES):
        return type(index).__name__
    return None


def _reject_time_series(obj: object, what: str, label: str) -> None:
    hit = _has_time_index(obj)
    if hit is not None:
        raise _refuse(
            f'{label}cross-section-only gate -- "{what}" is a TIME SERIES object '
            f"(index: {hit}; branch: class-rejected). This applies REGARDLESS of "
            f'"ordered": an object explicitly stamped with time is never a '
            f"cross-section. {_WHY_CROSS_SECTION}",
            "precondition-cross-section",
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


def _refuse(message: str, code: GateDetailCode) -> GateError:
    """Local alias for the shared constructor, so ``"other"`` is written once.

    ``code`` is a ``Literal``, so ``mypy --strict`` rejects an undeclared code at
    the raise site rather than a test noticing it later.
    """
    return refusal(message, code)


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
            raise _refuse(
                f'{label}cross-section-only gate -- "{arg}" (DataFrame) has no numeric '
                "column to check.",
                "precondition-shape",
            )
        return {name: np.asarray(col, dtype=float) for name, col in numeric}

    if isinstance(x, pd.Series):
        if not pd.api.types.is_numeric_dtype(x):
            raise _refuse(
                f'{label}cross-section-only gate -- the Series "{arg}" is not numeric '
                f"(dtype: {x.dtype}).",
                "precondition-shape",
            )
        return {arg: np.asarray(x, dtype=float)}

    if isinstance(x, np.ndarray) and x.ndim == 2:
        if not np.issubdtype(x.dtype, np.number):
            raise _refuse(
                f'{label}cross-section-only gate -- the matrix "{arg}" is not numeric '
                f"(dtype: {x.dtype}).",
                "precondition-shape",
            )
        if x.shape[1] < 1:
            raise _refuse(
                f'{label}cross-section-only gate -- the matrix "{arg}" has no columns.',
                "precondition-shape",
            )
        names = _fill_names(None, x.shape[1], arg, "[,", "]")
        return {names[j]: np.asarray(x[:, j], dtype=float) for j in range(x.shape[1])}

    if isinstance(x, Mapping):
        if not x:
            raise _refuse(
                f'{label}cross-section-only gate -- the mapping "{arg}" is empty.',
                "precondition-shape",
            )
        return {
            str(k): _one_numeric_vector(v, str(k), arg, label) for k, v in x.items()
        }

    if isinstance(x, list | tuple):
        if not x:
            raise _refuse(
                f'{label}cross-section-only gate -- the list "{arg}" is empty.',
                "precondition-shape",
            )
        if all(isinstance(v, int | float | np.floating | np.integer) for v in x):
            return {arg: np.asarray(x, dtype=float)}
        names = _fill_names(None, len(x), arg, "[[", "]]")
        return {
            names[j]: _one_numeric_vector(v, names[j], arg, label) for j, v in enumerate(x)
        }

    if isinstance(x, np.ndarray) and x.ndim == 1 and np.issubdtype(x.dtype, np.number):
        return {arg: np.asarray(x, dtype=float)}

    raise _refuse(
        f'{label}cross-section-only gate -- unsupported type for "{arg}" '
        f"(class: {type(x).__name__}). Accepted: a numeric vector, a numeric 2-D array, "
        "a sequence or mapping of numeric vectors, or a DataFrame with numeric columns.",
        "precondition-shape",
    )


def _one_numeric_vector(value: object, name: str, arg: str, label: str) -> np.ndarray:
    _reject_time_series(value, name, label)
    array = np.asarray(value)
    if array.ndim != 1 or not np.issubdtype(array.dtype, np.number):
        raise _refuse(
            f'{label}cross-section-only gate -- the element "{name}" of "{arg}" is not a '
            f"numeric vector (class: {type(value).__name__}).",
            "precondition-shape",
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
        raise _refuse(
            f'{label}cross-section-only gate -- group "{name}" of "{arg}" contains {n_bad} '
            "non-finite values (inf). The Ljung-Box statistic does not handle them and "
            "would return a silently wrong p-value.",
            "precondition-missing",
        )
    n_na = int(np.count_nonzero(np.isnan(values)))
    clean = values[~np.isnan(values)]
    n = clean.size
    if n < 3:
        raise _refuse(
            f'{label}cross-section-only gate -- group "{name}" of "{arg}" has n = {n} valid '
            f"observations (after removing {n_na} missing); the minimum is 3.",
            "precondition-sample-size",
        )
    if float(np.var(clean, ddof=1)) <= 0:
        raise _refuse(
            f'{label}cross-section-only gate -- group "{name}" of "{arg}" is constant (zero '
            "variance). The Ljung-Box statistic is undefined on such input.",
            "precondition-degenerate",
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
        # SAMPLE SIZE, NOT ARGUMENT MISUSE. `lb_lag=None` derives a lag that is
        # always below n, so this fires only on a caller-supplied lag -- but the
        # honest statement to the user is that the series is too short for the
        # lag this node tests at, and a longer series fixes it as surely as a
        # smaller lag does.
        raise _refuse(
            f'{label}cross-section-only gate -- lb_lag = {lag} >= n = {n} in group "{name}" '
            f'of "{arg}"; Ljung-Box requires lag < n.',
            "precondition-sample-size",
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
        raise _refuse(
            'gate_cross_section_only: "gate_alpha" must be ONE number in (0, 1).',
            "gate-argument",
        )
    if not 0 < float(gate_alpha) < 1:
        raise _refuse(
            'gate_cross_section_only: "gate_alpha" must be ONE number in (0, 1).',
            "gate-argument",
        )
    if not isinstance(ordered, bool):
        raise _refuse(
            'gate_cross_section_only: "ordered" must be ONE True/False (an EXPLICIT '
            "declaration: do the rows carry ORDER meaning?).",
            "gate-argument",
        )
    if lb_lag is not None:
        if isinstance(lb_lag, bool) or not isinstance(lb_lag, int) or lb_lag < 1:
            raise _refuse(
                'gate_cross_section_only: "lb_lag" must be None or ONE positive integer.',
                "gate-argument",
            )
        if not ordered:
            raise _refuse(
                'gate_cross_section_only: "lb_lag" was given TOGETHER with ordered=False -- '
                "CONTRADICTORY: with ordered=False the Ljung-Box precheck does not run, so "
                '"lb_lag" would be a silent no-op. Declare ordered=True or omit "lb_lag".',
                "gate-argument",
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
        raise _refuse(
            f'{label}cross-section-only gate -- "{arg}" WAS REJECTED by the Ljung-Box '
            f'whiteness precheck: group "{worst.name}" shows statistically significant '
            f"autocorrelation (X-squared = {worst.statistic:.6g}, lag = {worst.lag}, "
            f"p-value = {worst.p_value:.6g} < gate_alpha = {gate_alpha}, n = {worst.n}). "
            "IF the rows do NOT carry order (a genuine cross-section), declare it "
            f"EXPLICITLY with ordered=False. {_WHY_CROSS_SECTION}",
            "precondition-cross-section",
        )

    if not ordered:
        decision = "pass-unordered"
    elif all(g.tested for g in diagnostics):
        decision = "pass"
    else:
        decision = "pass-untested"

    return CrossSectionReport(
        groups=diagnostics,
        gate_alpha=float(gate_alpha),
        ordered=ordered,
        branch="ljung-box-tested" if ordered else "skipped-by-declaration",
        decision=decision,
    )
