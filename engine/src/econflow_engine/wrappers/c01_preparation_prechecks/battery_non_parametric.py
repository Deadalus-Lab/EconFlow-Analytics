# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``battery_non_parametric`` -- METHOD-SELECTION card #251.

#251 Battery of NON-PARAMETRIC (rank-based) tests on CROSS-SECTION data: Wilcoxon signed rank (one
    sample / paired) & rank sum = Mann-Whitney (two independent) with an optional non-parametric CI
    + Hodges-Lehmann · Kruskal-Wallis (k >= 2 independent groups) · Friedman (unreplicated complete
    block design)

Category 01-preparation-prechecks; module ``battery_non_parametric``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tn_friedman",
    "tn_kruskal",
    "tn_wilcox",
    "NODE_META",
    "wire_model",
]


def tn_wilcox(
    *,
    x: Any,
    y: Any | None = None,
    paired: bool | None = None,
    mu: float | None = None,
    alternative: Literal["two.sided", "less", "greater"] | None = None,
    exact: bool | None = None,
    correct: bool | None = None,
    conf_int: bool | None = None,
    conf_level: float | None = None,
    digits_rank: float | None = None,
    na_action: Literal["fail", "omit"] | None = None,
    lb_lag: int | None = None,
    gate_alpha: float | None = None,
    ordered: bool | None = None,
) -> dict[str, Any]:
    """Node ``tn_wilcox`` -- METHOD-SELECTION card #251.

    Battery of NON-PARAMETRIC (rank-based) tests on CROSS-SECTION data: Wilcoxon signed rank (one
    sample / paired) & rank sum = Mann-Whitney (two independent) with an optional non-parametric CI
    + Hodges-Lehmann · Kruskal-Wallis (k >= 2 independent groups) · Friedman (unreplicated complete
    block design).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to the FIRST numeric sample (a CROSS-SECTION vector,
            without dimensions). Every series handles/series IS REJECTED AND every sample that fails
            the Ljung-Box whiteness precheck. NOT Inf/-Inf.
        y: [raw_handle, optional] Handle to the SECOND sample. Omitted => a one-sample Wilcoxon
            signed rank test around mu. With paired=False => Wilcoxon rank sum (Mann-Whitney) of two
            INDEPENDENT samples; with paired=True => signed rank of the differences (requires EQUAL
            lengths).
        paired: [boolean, optional] True = paired (before/after on the SAME units); requires 'y' and
            equal lengths. Default ``False``.
        mu: [number, optional] The H0 value: location of x (one sample / paired) or location shift x
            - y (two samples). Default 0. Default ``0``.
        alternative: [enum, optional] Alternative hypothesis (default two.sided).
        exact: [boolean, optional] Exact p-value. Omitted => automatic (exact if each sample has <
            50 values). The exact branch ALSO APPLIES WITH TIES (shift algorithm, Streitberg-Röhmel)
            — see the exact_used/ties_present/zeroes_present fields.
        correct: [boolean, optional] Continuity correction in the NORMAL approximation (default
            True); ignored when exact runs. Default ``True``.
        conf_int: [boolean, optional] True => a non-parametric confidence interval + Hodges-Lehmann
            estimator ((pseudo)median or difference in location). CAUTION: with small n the ACHIEVED
            level differs from the requested (returned as conf_level_achieved) and the interval can
            turn out infinite (conf_int_finite). Default ``False``.
        conf_level: [number, optional] Requested confidence level in (0, 1); default 0.95. Default
            ``0.95``.
        digits_rank: [number, optional] If given, ranks are computed on signif(x, digits_rank) —
            stabilizes the detection of ties when differences on the order of 1e-16 hide them.
            Omitted => Inf (no rounding).
        na_action: [enum, optional] NA policy (default 'fail'). the rank-test routines SILENTLY
            remove NA (silent loss of data) — hence the node blocks by default; 'omit' = explicit
            removal with n_omitted reported.
        lb_lag: [integer, optional] Lag of the Ljung-Box whiteness precheck of the cross-section
            gate. Omitted => the documented rule min(10, n/5) (Hyndman & Athanasopoulos, FPP3 §5.4).
        gate_alpha: [number, optional] Level OF THE CROSS-SECTION GATE (default 0.05) — the
            rejection threshold ONLY of the Ljung-Box whiteness precheck. It does NOT concern the
            non-parametric test itself (hence it is called 'gate_alpha' and NOT 'alpha'). ⚠️ It IS a
            TEST OF SIZE gate_alpha: it blocks, by construction, ~gate_alpha of the proportion of
            VALID i.i.d. input (live: n=200 -> 1.6%/5.7%/10.1% at 0.01/0.05/0.10). Default ``0.05``.
        ordered: [boolean, optional] EXPLICIT declaration: do the ROWS carry ORDER meaning? True
            (default, conservative) => the Ljung-Box precheck RUNS. False => genuine cross-section
            (EXCHANGEABLE rows) and the precheck is EXPLICITLY skipped (decision =
            'pass-unordered'). ⚠️ Ljung-Box depends on ORDER — wilcox/kruskal/friedman do NOT. The
            rejection of series handles/series ALWAYS applies, regardless. Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tn_wilcox: not implemented. The method card is in ./README.md."
    )


def tn_kruskal(
    *,
    x: Any,
    na_action: Literal["fail", "omit"] | None = None,
    lb_lag: int | None = None,
    gate_alpha: float | None = None,
    ordered: bool | None = None,
) -> dict[str, Any]:
    """Node ``tn_kruskal`` -- METHOD-SELECTION card #251.

    Battery of NON-PARAMETRIC (rank-based) tests on CROSS-SECTION data: Wilcoxon signed rank (one
    sample / paired) & rank sum = Mann-Whitney (two independent) with an optional non-parametric CI
    + Hodges-Lehmann · Kruskal-Wallis (k >= 2 independent groups) · Friedman (unreplicated complete
    block design).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to the k >= 2 INDEPENDENT groups: a NAMED list of numeric
            vectors, a numeric matrix (columns = groups) or a DataFrame with numeric columns. Group
            names NON-EMPTY and UNIQUE. CROSS-SECTION ONLY (rejection of series handles + a
            Ljung-Box precheck per group). NOT Inf/-Inf.
        na_action: [enum, optional] NA policy (default 'fail'). the rank-test routines SILENTLY
            remove NA (silent loss of data) — hence the node blocks by default; 'omit' = explicit
            removal with n_omitted reported.
        lb_lag: [integer, optional] Lag of the Ljung-Box whiteness precheck of the cross-section
            gate. Omitted => the documented rule min(10, n/5) (Hyndman & Athanasopoulos, FPP3 §5.4).
        gate_alpha: [number, optional] Level OF THE CROSS-SECTION GATE (default 0.05) — the
            rejection threshold ONLY of the Ljung-Box whiteness precheck. It does NOT concern the
            non-parametric test itself (hence it is called 'gate_alpha' and NOT 'alpha'). ⚠️ It IS a
            TEST OF SIZE gate_alpha: it blocks, by construction, ~gate_alpha of the proportion of
            VALID i.i.d. input (live: n=200 -> 1.6%/5.7%/10.1% at 0.01/0.05/0.10). Default ``0.05``.
        ordered: [boolean, optional] EXPLICIT declaration: do the ROWS carry ORDER meaning? True
            (default, conservative) => the Ljung-Box precheck RUNS. False => genuine cross-section
            (EXCHANGEABLE rows) and the precheck is EXPLICITLY skipped (decision =
            'pass-unordered'). ⚠️ Ljung-Box depends on ORDER — wilcox/kruskal/friedman do NOT. The
            rejection of series handles/series ALWAYS applies, regardless. Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tn_kruskal: not implemented. The method card is in ./README.md."
    )


def tn_friedman(
    *,
    y: Any,
    groups: Sequence[str] | None = None,
    blocks: Sequence[str] | None = None,
    na_action: Literal["fail", "drop_blocks"] | None = None,
    lb_lag: int | None = None,
    gate_alpha: float | None = None,
    ordered: bool | None = None,
) -> dict[str, Any]:
    """Node ``tn_friedman`` -- METHOD-SELECTION card #251.

    Battery of NON-PARAMETRIC (rank-based) tests on CROSS-SECTION data: Wilcoxon signed rank (one
    sample / paired) & rank sum = Mann-Whitney (two independent) with an optional non-parametric CI
    + Hodges-Lehmann · Kruskal-Wallis (k >= 2 independent groups) · Friedman (unreplicated complete
    block design).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        y: [raw_handle, required] Handle to the data. WIDE form (preferred): numeric
            matrix/DataFrame blocks (rows, >= 2) × groups (columns, >= 2). LONG form: a numeric
            VECTOR together with 'groups' AND 'blocks' of the same length. A bare vector WITHOUT
            groups/blocks fails in stats with a «argument "groups" is missing». CROSS-SECTION ONLY.
        groups: [series_codes, optional] LONG form: GROUP labels (e.g. forecasting method) per
            observation of 'y'. Requires 'blocks' too. Every (block, group) combination EXACTLY once
            — an unreplicated COMPLETE block design; otherwise a hard gate.
        blocks: [series_codes, optional] LONG form: BLOCK labels (e.g. country/unit in which ALL
            groups were measured) per observation of 'y'. Also requires 'groups'.
        na_action: [enum, optional] NA policy (default 'fail'). the Friedman test routine SILENTLY
            removes ENTIRE blocks that have even one NA (documentation: «if y contains NAs,
            corresponding blocks are removed") — 'drop_blocks' does the same EXPLICITLY and returns
            n_blocks_dropped.
        lb_lag: [integer, optional] Lag of the Ljung-Box whiteness precheck of the cross-section
            gate. Omitted => the documented rule min(10, n/5) (Hyndman & Athanasopoulos, FPP3 §5.4).
        gate_alpha: [number, optional] Level OF THE CROSS-SECTION GATE (default 0.05) — the
            rejection threshold ONLY of the Ljung-Box whiteness precheck. It does NOT concern the
            non-parametric test itself (hence it is called 'gate_alpha' and NOT 'alpha'). ⚠️ It IS a
            TEST OF SIZE gate_alpha: it blocks, by construction, ~gate_alpha of the proportion of
            VALID i.i.d. input (live: n=200 -> 1.6%/5.7%/10.1% at 0.01/0.05/0.10). Default ``0.05``.
        ordered: [boolean, optional] EXPLICIT declaration: do the ROWS carry ORDER meaning? True
            (default, conservative) => the Ljung-Box precheck RUNS. False => genuine cross-section
            (EXCHANGEABLE rows) and the precheck is EXPLICITLY skipped (decision =
            'pass-unordered'). ⚠️ Ljung-Box depends on ORDER — wilcox/kruskal/friedman do NOT. The
            rejection of series handles/series ALWAYS applies, regardless. Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tn_friedman: not implemented. The method card is in ./README.md."
    )
