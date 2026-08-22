# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``descriptive_statistics`` -- method card #81.

#81 Descriptive statistics as data (ACF/PACF/CCF/rolling/correlation matrix + per-pair correlation
    inference)

Category 00-data-utilities; module ``descriptive_statistics``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "desc_acf",
    "desc_ccf",
    "desc_cor_test",
    "desc_correlations",
    "desc_pacf",
    "desc_rolling",
    "NODE_META",
    "wire_model",
]


def desc_acf(
    *,
    x: pd.Series,
    lag_max: int | None = None,
    demean: bool | None = None,
) -> dict[str, Any]:
    """Node ``desc_acf`` -- method card #81.

    Descriptive statistics as data (ACF/PACF/CCF/rolling/correlation matrix + per-pair correlation
    inference).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a series without NA/Inf (>=3 observations).
        lag_max: [integer, optional] Maximum lag (< length(x); default chosen by acf).
        demean: [boolean, optional] Subtract the mean before acf (default True). Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "desc_acf: not implemented."
    )


def desc_pacf(
    *,
    x: pd.Series,
    lag_max: int | None = None,
) -> dict[str, Any]:
    """Node ``desc_pacf`` -- method card #81.

    Descriptive statistics as data (ACF/PACF/CCF/rolling/correlation matrix + per-pair correlation
    inference).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a series without NA/Inf (>=3 observations).
        lag_max: [integer, optional] Maximum lag (< length(x)).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "desc_pacf: not implemented."
    )


def desc_ccf(
    *,
    x: pd.Series,
    y: pd.Series,
    lag_max: int | None = None,
) -> dict[str, Any]:
    """Node ``desc_ccf`` -- method card #81.

    Descriptive statistics as data (ACF/PACF/CCF/rolling/correlation matrix + per-pair correlation
    inference).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to the 1st series (same length as y).
        y: [series_handle, required] Handle to the 2nd series. lag<0 = x leads y; lag>0 = y leads.
        lag_max: [integer, optional] Maximum lag (< length).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "desc_ccf: not implemented."
    )


def desc_rolling(
    *,
    x: pd.Series,
    width: int,
    FUN: Literal["mean", "sd", "sum", "median", "min", "max"] | None = None,
    align: Literal["right", "center", "left"] | None = None,
) -> dict[str, Any]:
    """Node ``desc_rolling`` -- method card #81.

    Descriptive statistics as data (ACF/PACF/CCF/rolling/correlation matrix + per-pair correlation
    inference).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a series without NA/Inf.
        width: [integer, required] Rolling window length (<= length(x)).
        FUN: [enum, optional] Window statistic (default mean).
        align: [enum, optional] right=causal (default), center=smoothing (non-causal).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "desc_rolling: not implemented."
    )


def desc_correlations(
    *,
    data: np.ndarray,
    method: Literal["pearson", "spearman", "kendall"] | None = None,
    use: str | None = None,
) -> dict[str, Any]:
    """Node ``desc_correlations`` -- method card #81.

    Descriptive statistics as data (ACF/PACF/CCF/rolling/correlation matrix + per-pair correlation
    inference).

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [matrix_handle, required] Handle to a numeric matrix/df (>=2 columns, >=2 rows).
        method: [enum, optional] Correlation type (default pearson; spearman/kendall = rank-based).
        use: [string, optional] NA handling in cor (default pairwise.complete.obs). Default
            ``'pairwise.complete.obs'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "desc_correlations: not implemented."
    )


def desc_cor_test(
    *,
    data: np.ndarray,
    method: Literal["pearson", "kendall", "spearman"] | None = None,
    alternative: Literal["two.sided", "less", "greater"] | None = None,
    p_adjust_method: (
        Literal[
            "BH",
            "holm",
            "hochberg",
            "hommel",
            "bonferroni",
            "BY",
            "none",
        ]
        | None
    ) = None,
    conf_level: float | None = None,
    use: Literal["pairwise.complete.obs", "complete.obs", "na.fail"] | None = None,
    exact: bool | None = None,
    continuity: bool | None = None,
) -> dict[str, Any]:
    """Node ``desc_cor_test`` -- method card #81.

    Descriptive statistics as data (ACF/PACF/CCF/rolling/correlation matrix + per-pair correlation
    inference).

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [matrix_handle, required] Handle to a numeric matrix/df (>=2 columns, >=4 rows, no
            Inf, UNIQUE non-empty column names, no constant column). Returns ONE record per pair.
        method: [enum, optional] Correlation measure (default pearson). ONLY pearson defines
            conf.int & df; for kendall/spearman those fields return an explicit NA.
        alternative: [enum, optional] Alternative hypothesis (default two.sided; greater=positive
            correlation).
        p_adjust_method: [enum, optional] Multiplicity correction for the p*(p-1)/2 simultaneous
            tests (default BH=FDR; holm/hochberg/hommel/bonferroni=FWER; none=no correction). The
            alias 'fdr' is NOT exposed (=BH).
        conf_level: [number, optional] Confidence level, STRICTLY in (0,1) (default 0.95; pearson
            only). Default ``0.95``.
        use: [enum, optional] Explicit NA policy (default pairwise.complete.obs = per pair;
            complete.obs = listwise drop; na.fail = stop on any NA).
        exact: [boolean, optional] Exact p-value; ONLY kendall/spearman (for pearson = gate error).
            Omission = 'auto' (kendall: n<50; spearman: True).
        continuity: [boolean, optional] Continuity correction on the asymptotic path; ONLY
            kendall/spearman (for pearson = gate error; default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "desc_cor_test: not implemented."
    )
