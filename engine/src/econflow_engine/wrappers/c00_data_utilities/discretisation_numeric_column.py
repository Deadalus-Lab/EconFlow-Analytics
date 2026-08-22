# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``discretisation_numeric_column`` -- method card #255.

#255 DISCRETISATION (binning) of ONE numeric column: EQUAL-POPULATION bins (sample quantiles,
    quantile type 7 PINNED) or EQUAL-WIDTH bins (an explicit seq over the range or over a GIVEN
    fixed domain) + an out-of-sample APPLY of the STORED breaks

Category 00-data-utilities; module ``discretisation_numeric_column``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "bn_apply",
    "bn_equal_width",
    "bn_quantile_bins",
    "NODE_META",
    "wire_model",
]


def bn_quantile_bins(
    *,
    x: np.ndarray,
    n_bins: int | None = None,
    probs: Sequence[float] | None = None,
    labels: Sequence[str] | None = None,
    right: bool | None = None,
    dedupe_breaks: bool | None = None,
    na_action: Literal["fail", "keep"] | None = None,
    dummies: bool | None = None,
) -> dict[str, Any]:
    """Node ``bn_quantile_bins`` -- method card #255.

    DISCRETISATION (binning) of ONE numeric column: EQUAL-POPULATION bins (sample quantiles,
    quantile type 7 PINNED) or EQUAL-WIDTH bins (an explicit seq over the range or over a GIVEN
    fixed domain) + an out-of-sample APPLY of the STORED breaks.

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to ONE numeric column (n×1: rows =
            observations/periods/countries). One node PER variable — for several columns do a
            fan-out. NO NA/NaN/Inf unless na_action='keep' is declared. CAUTION (non-stationarity):
            in I(1) LEVELS the sample quantiles reflect the POSITION IN TIME and not an economic
            regime — give DIFFERENCES/rates, or use bn_equal_width with exogenous boundaries
            (Hamilton-Ma-Xi).
        n_bins: [integer, optional] Number of EQUAL-SIZED bins (default 4 = quartiles; 3 = terciles,
            5 = quintiles, 10 = deciles). AN INTEGER >= 2 AND STRICTLY smaller than the number of
            UNIQUE values, otherwise the boundaries coincide (the binning routine: "'breaks' are not
            unique"). It is NOT combined with 'probs'.
        probs: [num_array, optional] AN ALTERNATIVE to n_bins: EXPLICIT quantiles for UNEQUAL bins,
            e.g. [0,0.1,0.9,1] = "lower tail / centre / upper tail". STRICTLY INCREASING, >= 3
            points, and MANDATORILY with endpoints EXACTLY 0 and 1 — otherwise the values outside
            the extreme quantiles become SILENTLY NA in the binning routine.
        labels: [series_codes, optional] Names of the bins (e.g. ['low','mid','high'] or
            ['Q1','Q2','Q3','Q4']) — EXACTLY n_bins in count, UNIQUE and non-empty. Omitting them
            produces the intervals of the binning routine ('(a,b]'). DUPLICATE labels ARE BLOCKED:
            the binning routine MERGES them SILENTLY into ONE level, so two bins become one
            (silent-wrong).
        right: [boolean, optional] True (default, like the binning routine) = intervals CLOSED ON
            THE RIGHT: (b1,b2]... (bk-1,bk]. False = [b1,b2)... [bk-1,bk). The EXTREME point is
            always included (include.lowest = True in the fit). IN bn_apply it MUST be THE SAME as
            in the fit, otherwise the boundary observations change bin. Default ``True``.
        dedupe_breaks: [boolean, optional] Policy for TIES. False (default) = HARD STOP when two
            quantiles coincide (many repeated values): the message names the column and the number
            of duplicates. True = EXPLICIT consent to keep the UNIQUE boundaries — then the bins
            become FEWER than requested (see n_breaks_dropped) and no longer have equal population.
            Default ``False``.
        na_action: [enum, optional] Policy for NA/NaN/Inf. 'fail' (default) = blocked-by-gate (the
            quantile estimator throws "missing values and NaN's not allowed if 'the NA policy' is
            False" and the binning routine encodes Inf SILENTLY as NA). 'keep' = the boundaries are
            estimated from the FINITE values and the missing positions ARE KEPT with an NA code —
            rows are NEVER removed, so that the regime dummies stay ALIGNED with y.
        dummies: [boolean, optional] True = it also returns the 0/1 indicator matrix (n×n_bins, ONE
            column per bin) — ready REGIME DUMMIES for regression. The missing/out-of-range rows get
            NA (NOT 0: 0 would mean "definitely not in this bin"). Default False (smaller payload).
            Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bn_quantile_bins: not implemented."
    )


def bn_equal_width(
    *,
    x: np.ndarray,
    n_bins: int | None = None,
    range_min: float | None = None,
    range_max: float | None = None,
    labels: Sequence[str] | None = None,
    right: bool | None = None,
    na_action: Literal["fail", "keep"] | None = None,
    dummies: bool | None = None,
) -> dict[str, Any]:
    """Node ``bn_equal_width`` -- method card #255.

    DISCRETISATION (binning) of ONE numeric column: EQUAL-POPULATION bins (sample quantiles,
    quantile type 7 PINNED) or EQUAL-WIDTH bins (an explicit seq over the range or over a GIVEN
    fixed domain) + an out-of-sample APPLY of the STORED breaks.

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to ONE numeric column (n×1: rows =
            observations/periods/countries). One node PER variable — for several columns do a
            fan-out. NO NA/NaN/Inf unless na_action='keep' is declared. CAUTION (non-stationarity):
            in I(1) LEVELS the sample quantiles reflect the POSITION IN TIME and not an economic
            regime — give DIFFERENCES/rates, or use bn_equal_width with exogenous boundaries
            (Hamilton-Ma-Xi).
        n_bins: [integer, optional] Number of EQUAL-WIDTH bins (default 4). AN INTEGER >= 2 AND
            STRICTLY smaller than the number of UNIQUE values. The boundaries are an EXPLICIT
            seq(from, to, length.out = n_bins+1) — NEVER cut(x, breaks=<number>), which HIDDENLY
            shifts the endpoints by 0.1% of the range and does not return the boundaries. Default
            ``4``.
        range_min: [number, optional] OPTIONAL lower endpoint of a FIXED domain (default: the min of
            the data). Give EXOGENOUS, theoretical boundaries (e.g. an inflation target) so that the
            bins are COMPARABLE across countries/samples. It MUST COVER the data, otherwise the
            values outside would SILENTLY become NA.
        range_max: [number, optional] OPTIONAL upper endpoint of a FIXED domain (default: the max of
            the data). It must be STRICTLY greater than range_min and cover the data.
        labels: [series_codes, optional] Names of the bins (e.g. ['low','mid','high'] or
            ['Q1','Q2','Q3','Q4']) — EXACTLY n_bins in count, UNIQUE and non-empty. Omitting them
            produces the intervals of the binning routine ('(a,b]'). DUPLICATE labels ARE BLOCKED:
            the binning routine MERGES them SILENTLY into ONE level, so two bins become one
            (silent-wrong).
        right: [boolean, optional] True (default, like the binning routine) = intervals CLOSED ON
            THE RIGHT: (b1,b2]... (bk-1,bk]. False = [b1,b2)... [bk-1,bk). The EXTREME point is
            always included (include.lowest = True in the fit). IN bn_apply it MUST be THE SAME as
            in the fit, otherwise the boundary observations change bin. Default ``True``.
        na_action: [enum, optional] Policy for NA/NaN/Inf. 'fail' (default) = blocked-by-gate (the
            quantile estimator throws "missing values and NaN's not allowed if 'the NA policy' is
            False" and the binning routine encodes Inf SILENTLY as NA). 'keep' = the boundaries are
            estimated from the FINITE values and the missing positions ARE KEPT with an NA code —
            rows are NEVER removed, so that the regime dummies stay ALIGNED with y.
        dummies: [boolean, optional] True = it also returns the 0/1 indicator matrix (n×n_bins, ONE
            column per bin) — ready REGIME DUMMIES for regression. The missing/out-of-range rows get
            NA (NOT 0: 0 would mean "definitely not in this bin"). Default False (smaller payload).
            Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bn_equal_width: not implemented."
    )


def bn_apply(
    *,
    x: np.ndarray,
    breaks: Sequence[float],
    labels: Sequence[str] | None = None,
    right: bool | None = None,
    include_lowest: bool | None = None,
    out_of_range: Literal["fail", "na", "clamp"] | None = None,
    na_action: Literal["fail", "keep"] | None = None,
    dummies: bool | None = None,
) -> dict[str, Any]:
    """Node ``bn_apply`` -- method card #255.

    DISCRETISATION (binning) of ONE numeric column: EQUAL-POPULATION bins (sample quantiles,
    quantile type 7 PINNED) or EQUAL-WIDTH bins (an explicit seq over the range or over a GIVEN
    fixed domain) + an out-of-sample APPLY of the STORED breaks.

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to ONE numeric column (n×1: rows =
            observations/periods/countries). One node PER variable — for several columns do a
            fan-out. NO NA/NaN/Inf unless na_action='keep' is declared. CAUTION (non-stationarity):
            in I(1) LEVELS the sample quantiles reflect the POSITION IN TIME and not an economic
            regime — give DIFFERENCES/rates, or use bn_equal_width with exogenous boundaries
            (Hamilton-Ma-Xi).
        breaks: [num_array, required] FIT/APPLY EXTERNALIZATION (§3b gate 6): EXACTLY the 'breaks'
            field of a PREVIOUS bn_quantile_bins/bn_equal_width. STRICTLY INCREASING, finite, >= 3
            points. WITHOUT it, a re-fit on the new data gives DIFFERENT boundaries and the regime
            dummies are NOT comparable with the training sample. DUPLICATE/unsorted boundaries are
            blocked: the binning routine sorts SILENTLY and the labels move to the WRONG bins.
        labels: [series_codes, optional] Names of the bins (e.g. ['low','mid','high'] or
            ['Q1','Q2','Q3','Q4']) — EXACTLY n_bins in count, UNIQUE and non-empty. Omitting them
            produces the intervals of the binning routine ('(a,b]'). DUPLICATE labels ARE BLOCKED:
            the binning routine MERGES them SILENTLY into ONE level, so two bins become one
            (silent-wrong).
        right: [boolean, optional] True (default, like the binning routine) = intervals CLOSED ON
            THE RIGHT: (b1,b2]... (bk-1,bk]. False = [b1,b2)... [bk-1,bk). The EXTREME point is
            always included (include.lowest = True in the fit). IN bn_apply it MUST be THE SAME as
            in the fit, otherwise the boundary observations change bin. Default ``True``.
        include_lowest: [boolean, optional] True (default) = the EXTREME boundary (the lower one
            with right=True, the upper one with right=False) belongs to the extreme bin. False = the
            value that EQUALS the endpoint belongs NOWHERE (the binning routine SILENTLY zeroes it
            to NA). It MUST be THE SAME as in the fit (the fits here are always True). Default
            ``True``.
        out_of_range: [enum, optional] Policy for NEW values OUTSIDE the range of the breaks — the
            binning routine encodes them SILENTLY as NA ("Values which fall outside the range of
            breaks are coded as NA»), i.e. LOST observations without any indication. 'fail'
            (default) = blocked-by-gate. 'na' = An EXPLICIT NA code + a record in
            n_out_of_range/out_of_range_labels. 'clamp' = assignment to the EXTREME bin (requires
            include_lowest=True); useful when the regimes are defined as "below/above X" but it
            DISTORTS the extremeness information.
        na_action: [enum, optional] Policy for NA/NaN/Inf. 'fail' (default) = blocked-by-gate (the
            quantile estimator throws "missing values and NaN's not allowed if 'the NA policy' is
            False" and the binning routine encodes Inf SILENTLY as NA). 'keep' = the boundaries are
            estimated from the FINITE values and the missing positions ARE KEPT with an NA code —
            rows are NEVER removed, so that the regime dummies stay ALIGNED with y.
        dummies: [boolean, optional] True = it also returns the 0/1 indicator matrix (n×n_bins, ONE
            column per bin) — ready REGIME DUMMIES for regression. The missing/out-of-range rows get
            NA (NOT 0: 0 would mean "definitely not in this bin"). Default False (smaller payload).
            Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bn_apply: not implemented."
    )
