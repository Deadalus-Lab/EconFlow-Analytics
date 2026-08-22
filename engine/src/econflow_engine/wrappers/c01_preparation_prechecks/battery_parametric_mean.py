# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``battery_parametric_mean`` -- method card #250.

#250 Battery of PARAMETRIC MEAN tests on CROSS-SECTION data: t-test (one sample / two samples Welch
    or Student pooled / paired) · one-way ANOVA (equal variances, a full ANOVA table) · the one-way
    Welch (1951) test WITHOUT the equal-variance assumption

Category 01-preparation-prechecks; module ``battery_parametric_mean``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tp_anova",
    "tp_t_test",
    "tp_welch",
    "NODE_META",
    "wire_model",
]


def tp_t_test(
    *,
    x: Any,
    y: Any | None = None,
    mu: float | None = None,
    paired: bool | None = None,
    var_equal: bool | None = None,
    alternative: Literal["two.sided", "less", "greater"] | None = None,
    conf_level: float | None = None,
    alpha: float | None = None,
    na_action: Literal["fail", "omit"] | None = None,
    x_name: str | None = None,
    y_name: str | None = None,
    lb_lag: int | None = None,
    gate_alpha: float | None = None,
    ordered: bool | None = None,
) -> dict[str, Any]:
    """Node ``tp_t_test`` -- method card #250.

    Battery of PARAMETRIC MEAN tests on CROSS-SECTION data: t-test (one sample / two samples Welch
    or Student pooled / paired) · one-way ANOVA (equal variances, a full ANOVA table) · the one-way
    Welch (1951) test WITHOUT the equal-variance assumption.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to the 1st sample: a PLAIN numeric VECTOR of cross-section
            observations. FORBIDDEN: matrix/DataFrame (use the tp_anova/tp_welch)· series handles
            (CROSS-SECTION ONLY gate); Inf/NaN (the t-test routine does NOT error — it returns NaN);
            a constant sample («data are essentially constant»)· n < 3.
        y: [raw_handle, optional] Handle to the 2nd sample (optional). Omitted => a ONE-SAMPLE test
            vs 'mu'. Given => two-sample (or paired if paired=True, in which case EQUAL length is
            required).
        mu: [number, optional] The H0 value of the mean (one-sample) or of the DIFFERENCE of means
            (two-sample/paired); default 0. A SINGLE finite number. Default ``0``.
        paired: [boolean, optional] True => a paired t-test on the DIFFERENCES x - y (requires 'y'
            of EQUAL length). ⚠️ The Ljung-Box precheck runs ON THE DIFFERENCES — these are the true
            input of the paired test. Default ``False``.
        var_equal: [boolean, optional] False (default) => Welch/Satterthwaite (SEPARATE variances —
            the safe default). True => Student pooled variance. ONLY for two-sample unpaired: with
            one-sample/paired, stats ignores it SILENTLY => hard gate. Default ``False``.
        alternative: [enum, optional] Alternative hypothesis (default 'two.sided'). 'greater' = the
            mean of x is GREATER (one-sample: the mean > mu). One-sided tests give a HALF-INFINITE
            confidence interval.
        conf_level: [number, optional] Confidence level of the interval in the OPEN interval (0, 1);
            default 0.95. Default ``0.95``.
        alpha: [number, optional] Significance level OF THE TEST in the OPEN interval (0, 1) —
            default 0.05. Determines ONLY the 'reject'/'decision' fields of the output; it does NOT
            change the p-value and does NOT affect the cross-section gate (that has its OWN
            'gate_alpha'). Default ``0.05``.
        na_action: [enum, optional] EXPLICIT NA policy (default 'fail' = hard stop). the t-test
            routine/aov remove NA SILENTLY, so the reported n is not the input's n. With 'omit' the
            removal happens EXPLICITLY and the count is returned (n_na); in paired, PAIRS are
            removed, in anova/welch, ROWS.
        x_name: [string, optional] LABEL of the 1st sample in the output (default 'x'; <= 100
            characters). NOT data. Default ``'x'``.
        y_name: [string, optional] LABEL of the 2nd sample (default 'y'). Must differ from x_name.
            Default ``'y'``.
        lb_lag: [integer, optional] Lag of the Ljung-Box whiteness precheck (cross-section gate). If
            omitted: the documented rule min(10, n/5) (Hyndman & Athanasopoulos, FPP 3rd ed. §5.4).
            MUST be a positive integer < n.
        gate_alpha: [number, optional] Level OF THE CROSS-SECTION GATE in the OPEN interval (0, 1) —
            default 0.05. Rejection threshold ONLY of the Ljung-Box whiteness precheck. ⚠️ It IS a
            TEST OF SIZE gate_alpha: it blocks, by construction, ~gate_alpha of the proportion of
            VALID i.i.d. input (live: n=200 -> 1.6%/5.7%/10.1% at 0.01/0.05/0.10). Hence it is
            DECOUPLED from the test's 'alpha'. Default ``0.05``.
        ordered: [boolean, optional] EXPLICIT declaration: do the ROWS carry ORDER meaning? True
            (default, conservative) => the Ljung-Box precheck RUNS. False => the user declares a
            genuine cross-section (the rows are EXCHANGEABLE) and the precheck is SKIPPED EXPLICITLY
            (decision = 'pass-unordered'). ⚠️ Ljung-Box depends on ORDER: the same numbers pass
            unsorted and get BLOCKED sorted — while the t.test/aov/oneway.test are
            permutation-invariant. The rejection of series handles/series ALWAYS applies,
            regardless. Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tp_t_test: not implemented."
    )


def tp_anova(
    *,
    data: pd.DataFrame,
    response: str,
    group: str,
    alpha: float | None = None,
    na_action: Literal["fail", "omit"] | None = None,
    lb_lag: int | None = None,
    gate_alpha: float | None = None,
    ordered: bool | None = None,
) -> dict[str, Any]:
    """Node ``tp_anova`` -- method card #250.

    Battery of PARAMETRIC MEAN tests on CROSS-SECTION data: t-test (one sample / two samples Welch
    or Student pooled / paired) · one-way ANOVA (equal variances, a full ANOVA table) · the one-way
    Welch (1951) test WITHOUT the equal-variance assumption.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a CROSS-SECTION DataFrame (rows = units:
            countries/firms/households) with ONE numeric response column and ONE grouping column
            (categorical/string). ⚠️ CROSS-SECTION ONLY: each group passes a Ljung-Box whiteness
            precheck; time series ARE REJECTED (see the HAC path, the HAC path, category
            07-causality-policy).
        response: [string, required] NAME of the NUMERIC response-variable column in 'data' (NOT
            data). Must exist in the DataFrame; used ONLY as an index — NEVER in formula/parse.
        group: [string, required] NAME of the GROUPING column in 'data' (NOT data). The column MUST
            be factor or character: with a NUMERIC/LOGICAL column, the analysis-of-variance routine
            does NOT do ANOVA — it does LINEAR REGRESSION (Df = 1 instead of k-1) WITHOUT an error
            (silent-wrong) => hard gate. >= 2 levels AND >= 2 observations per level are required.
        alpha: [number, optional] Significance level OF THE TEST in the OPEN interval (0, 1) —
            default 0.05. Determines ONLY the 'reject'/'decision' fields of the output; it does NOT
            change the p-value and does NOT affect the cross-section gate (that has its OWN
            'gate_alpha'). Default ``0.05``.
        na_action: [enum, optional] EXPLICIT NA policy (default 'fail' = hard stop). the t-test
            routine/aov remove NA SILENTLY, so the reported n is not the input's n. With 'omit' the
            removal happens EXPLICITLY and the count is returned (n_na); in paired, PAIRS are
            removed, in anova/welch, ROWS.
        lb_lag: [integer, optional] Lag of the Ljung-Box whiteness precheck (cross-section gate). If
            omitted: the documented rule min(10, n/5) (Hyndman & Athanasopoulos, FPP 3rd ed. §5.4).
            MUST be a positive integer < n.
        gate_alpha: [number, optional] Level OF THE CROSS-SECTION GATE in the OPEN interval (0, 1) —
            default 0.05. Rejection threshold ONLY of the Ljung-Box whiteness precheck. ⚠️ It IS a
            TEST OF SIZE gate_alpha: it blocks, by construction, ~gate_alpha of the proportion of
            VALID i.i.d. input (live: n=200 -> 1.6%/5.7%/10.1% at 0.01/0.05/0.10). Hence it is
            DECOUPLED from the test's 'alpha'. Default ``0.05``.
        ordered: [boolean, optional] EXPLICIT declaration: do the ROWS carry ORDER meaning? True
            (default, conservative) => the Ljung-Box precheck RUNS. False => the user declares a
            genuine cross-section (the rows are EXCHANGEABLE) and the precheck is SKIPPED EXPLICITLY
            (decision = 'pass-unordered'). ⚠️ Ljung-Box depends on ORDER: the same numbers pass
            unsorted and get BLOCKED sorted — while the t.test/aov/oneway.test are
            permutation-invariant. The rejection of series handles/series ALWAYS applies,
            regardless. Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tp_anova: not implemented."
    )


def tp_welch(
    *,
    data: pd.DataFrame,
    response: str,
    group: str,
    var_equal: bool | None = None,
    alpha: float | None = None,
    na_action: Literal["fail", "omit"] | None = None,
    lb_lag: int | None = None,
    gate_alpha: float | None = None,
    ordered: bool | None = None,
) -> dict[str, Any]:
    """Node ``tp_welch`` -- method card #250.

    Battery of PARAMETRIC MEAN tests on CROSS-SECTION data: t-test (one sample / two samples Welch
    or Student pooled / paired) · one-way ANOVA (equal variances, a full ANOVA table) · the one-way
    Welch (1951) test WITHOUT the equal-variance assumption.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a CROSS-SECTION DataFrame (rows = units:
            countries/firms/households) with ONE numeric response column and ONE grouping column
            (categorical/string). ⚠️ CROSS-SECTION ONLY: each group passes a Ljung-Box whiteness
            precheck; time series ARE REJECTED (see the HAC path, the HAC path, category
            07-causality-policy).
        response: [string, required] NAME of the NUMERIC response-variable column in 'data' (NOT
            data). Must exist in the DataFrame; used ONLY as an index — NEVER in formula/parse.
        group: [string, required] NAME of the GROUPING column in 'data' (NOT data). The column MUST
            be factor or character: with a NUMERIC/LOGICAL column, the analysis-of-variance routine
            does NOT do ANOVA — it does LINEAR REGRESSION (Df = 1 instead of k-1) WITHOUT an error
            (silent-wrong) => hard gate. >= 2 levels AND >= 2 observations per level are required.
        var_equal: [boolean, optional] False (default) => the Welch (1951) test: does NOT assume
            equal variances (the safe default with unequal n_i). True => the classical F AS THE TEST
            (statistic identical to tp_anova, but WITHOUT an ANOVA table). Default ``False``.
        alpha: [number, optional] Significance level OF THE TEST in the OPEN interval (0, 1) —
            default 0.05. Determines ONLY the 'reject'/'decision' fields of the output; it does NOT
            change the p-value and does NOT affect the cross-section gate (that has its OWN
            'gate_alpha'). Default ``0.05``.
        na_action: [enum, optional] EXPLICIT NA policy (default 'fail' = hard stop). the t-test
            routine/aov remove NA SILENTLY, so the reported n is not the input's n. With 'omit' the
            removal happens EXPLICITLY and the count is returned (n_na); in paired, PAIRS are
            removed, in anova/welch, ROWS.
        lb_lag: [integer, optional] Lag of the Ljung-Box whiteness precheck (cross-section gate). If
            omitted: the documented rule min(10, n/5) (Hyndman & Athanasopoulos, FPP 3rd ed. §5.4).
            MUST be a positive integer < n.
        gate_alpha: [number, optional] Level OF THE CROSS-SECTION GATE in the OPEN interval (0, 1) —
            default 0.05. Rejection threshold ONLY of the Ljung-Box whiteness precheck. ⚠️ It IS a
            TEST OF SIZE gate_alpha: it blocks, by construction, ~gate_alpha of the proportion of
            VALID i.i.d. input (live: n=200 -> 1.6%/5.7%/10.1% at 0.01/0.05/0.10). Hence it is
            DECOUPLED from the test's 'alpha'. Default ``0.05``.
        ordered: [boolean, optional] EXPLICIT declaration: do the ROWS carry ORDER meaning? True
            (default, conservative) => the Ljung-Box precheck RUNS. False => the user declares a
            genuine cross-section (the rows are EXCHANGEABLE) and the precheck is SKIPPED EXPLICITLY
            (decision = 'pass-unordered'). ⚠️ Ljung-Box depends on ORDER: the same numbers pass
            unsorted and get BLOCKED sorted — while the t.test/aov/oneway.test are
            permutation-invariant. The rejection of series handles/series ALWAYS applies,
            regardless. Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tp_welch: not implemented."
    )
