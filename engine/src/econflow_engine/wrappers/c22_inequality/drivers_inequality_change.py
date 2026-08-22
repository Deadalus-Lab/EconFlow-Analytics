# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``drivers_inequality_change`` -- method card #225.

#225 drivers of inequality change: RIF (recentered influence function) regressions +
    regression-based (Fields/Yun) inequality decomposition

Category 22-inequality; module ``drivers_inequality_change``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c22_inequality import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "gini_decomposition",
    "ineq_change_decomp",
    "ineq_regression_decomp",
    "mld_decomposition",
    "rif_influence",
    "rif_regression",
    "rif_regression_se",
    "NODE_META",
    "wire_model",
]


def rif_influence(
    *,
    x: np.ndarray,
    weights: np.ndarray | None = None,
    method: Literal["quantile", "gini", "variance"] | None = None,
    quantile: float | None = None,
    kernel: (
        Literal[
            "gaussian",
            "rectangular",
            "triangular",
            "epanechnikov",
            "biweight",
            "cosine",
            "optcosine",
        ]
        | None
    ) = None,
) -> dict[str, Any]:
    """Node ``rif_influence`` -- method card #225.

    drivers of inequality change: RIF (recentered influence function) regressions + regression-based
    (Fields/Yun) inequality decomposition.

    Category 22-inequality; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric vector of income (length >= 2, without
            NA/Inf; method='gini' requires x >= 0). NEVER in the schema.
        weights: [matrix_handle, optional] Handle to numeric weights (population factors), length ==
            length(x), STRICTLY > 0, without NA. None => equal-weighted.
        method: [enum, optional] Distributional statistic (default quantile· gini· variance).
        quantile: [number, optional] Quantile ∈ (0,1) when method='quantile' (default 0.5=median).
            Default ``0.5``.
        kernel: [enum, optional] Smoothing kernel for the density in method='quantile' (default
            gaussian).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rif_influence: not implemented."
    )


def rif_regression(
    *,
    formula: str,
    data: pd.DataFrame,
    weights: str | None = None,
    method: Literal["quantile", "gini", "variance"] | None = None,
    quantile: Sequence[float] | None = None,
    kernel: (
        Literal[
            "gaussian",
            "rectangular",
            "triangular",
            "epanechnikov",
            "biweight",
            "cosine",
            "optcosine",
        ]
        | None
    ) = None,
) -> dict[str, Any]:
    """Node ``rif_regression`` -- method card #225.

    drivers of inequality change: RIF (recentered influence function) regressions + regression-based
    (Fields/Yun) inequality decomposition.

    Category 22-inequality; memory class ``light``.

    Args:
        formula: [formula, required] RIF regression formula 'income ~ x1 + x2 +...' (numeric
            response).
        data: [df_handle, required] Handle to a micro-data DataFrame (contains response + covariates
            + weights col).
        weights: [string, optional] WEIGHTS COLUMN NAME inside data (string; dineq's dual
            convention); numeric, > 0, without NA. None => equal-weighted.
        method: [enum, optional] Distributional statistic (default quantile· gini· variance).
        quantile: [num_array, optional] One or MULTIPLE quantiles ∈ (0,1) when method='quantile'
            (default 0.5). The output is returned stacked per quantile.
        kernel: [enum, optional] Smoothing kernel for method='quantile' (default gaussian).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rif_regression: not implemented."
    )


def rif_regression_se(
    *,
    formula: str,
    data: pd.DataFrame,
    weights: str | None = None,
    method: Literal["quantile", "gini", "variance"] | None = None,
    quantile: float | None = None,
    kernel: (
        Literal[
            "gaussian",
            "rectangular",
            "triangular",
            "epanechnikov",
            "biweight",
            "cosine",
            "optcosine",
        ]
        | None
    ) = None,
    Nboot: int | None = None,
    confidence: float | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``rif_regression_se`` -- method card #225.

    drivers of inequality change: RIF (recentered influence function) regressions + regression-based
    (Fields/Yun) inequality decomposition.

    Category 22-inequality; memory class ``light``.

    Args:
        formula: [formula, required] RIF regression formula 'income ~ x1 + x2 +...'.
        data: [df_handle, required] Handle to a micro-data DataFrame (response + covariates +
            weights col).
        weights: [string, optional] WEIGHTS COLUMN NAME in data (string, > 0, without NA); None =>
            equal-weighted.
        method: [enum, optional] Distributional statistic (default quantile· gini· variance).
        quantile: [number, optional] ONE quantile ∈ (0,1) when method='quantile' (bootstrap: scalar
            only). Default ``0.5``.
        kernel: [enum, optional] Smoothing kernel for method='quantile' (default gaussian).
        Nboot: [integer, optional] Number of bootstrap replicates (positive integer; default 100).
            Default ``100``.
        confidence: [number, optional] CI confidence level ∈ (0,1) (default 0.95). Default ``0.95``.
        seed: [integer, optional] Seed for DETERMINISTIC bootstrap (same seed => identical; default
            42). Default ``42``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rif_regression_se: not implemented."
    )


def gini_decomposition(
    *,
    x: np.ndarray,
    z: Any,
    weights: np.ndarray | None = None,
) -> dict[str, Any]:
    """Node ``gini_decomposition`` -- method card #225.

    drivers of inequality change: RIF (recentered influence function) regressions + regression-based
    (Fields/Yun) inequality decomposition.

    Category 22-inequality; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to numeric non-negative income (x >= 0, length >= 2,
            without NA/Inf).
        z: [raw_handle, required] Handle to a grouping vector (categorical/string/numeric), length
            == length(x), >= 2 groups, without NA. Passes as is (raw) -> factor in the wrapper.
        weights: [matrix_handle, optional] Handle to numeric weights, length == length(x), > 0,
            without NA; None => equal-weighted.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "gini_decomposition: not implemented."
    )


def mld_decomposition(
    *,
    x: np.ndarray,
    z: Any,
    weights: np.ndarray | None = None,
) -> dict[str, Any]:
    """Node ``mld_decomposition`` -- method card #225.

    drivers of inequality change: RIF (recentered influence function) regressions + regression-based
    (Fields/Yun) inequality decomposition.

    Category 22-inequality; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to numeric income (length >= 2, without NA/Inf). MLD=log
            -> x<=0 is silently deleted (n_deleted is reported).
        z: [raw_handle, required] Handle to a grouping vector, length == length(x), >= 2 groups,
            without NA (raw -> factor).
        weights: [matrix_handle, optional] Handle to numeric weights, length == length(x), > 0,
            without NA; None => equal-weighted.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mld_decomposition: not implemented."
    )


def ineq_regression_decomp(
    *,
    formula: str,
    data: pd.DataFrame,
    weights: str | None = None,
) -> dict[str, Any]:
    """Node ``ineq_regression_decomp`` -- method card #225.

    drivers of inequality change: RIF (recentered influence function) regressions + regression-based
    (Fields/Yun) inequality decomposition.

    Category 22-inequality; memory class ``light``.

    Args:
        formula: [formula, required] OLS formula 'income ~ x1 + x2 +...' (multiple characteristics).
            log(y) -> y<=0 is deleted (n_deleted is reported).
        data: [df_handle, required] Handle to a micro-data DataFrame (response + covariates +
            weights col).
        weights: [string, optional] WEIGHTS COLUMN NAME in data (string, > 0, without NA); None =>
            equal-weighted.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ineq_regression_decomp: not implemented."
    )


def ineq_change_decomp(
    *,
    formula1: str,
    data1: pd.DataFrame,
    weights1: str | None = None,
    formula2: str,
    data2: pd.DataFrame,
    weights2: str | None = None,
) -> dict[str, Any]:
    """Node ``ineq_change_decomp`` -- method card #225.

    drivers of inequality change: RIF (recentered influence function) regressions + regression-based
    (Fields/Yun) inequality decomposition.

    Category 22-inequality; memory class ``light``.

    Args:
        formula1: [formula, required] Year 1 OLS formula 'income ~ x1 + x2 +...' (same
            structure/order as formula2).
        data1: [df_handle, required] Handle to a year 1 micro-data DataFrame.
        weights1: [string, optional] WEIGHTS COLUMN NAME in data1 (string, > 0, without NA); None =>
            equal-weighted.
        formula2: [formula, required] Year 2 OLS formula (same characteristics/order as formula1).
        data2: [df_handle, required] Handle to a year 2 micro-data DataFrame.
        weights2: [string, optional] WEIGHTS COLUMN NAME in data2 (string, > 0, without NA); None =>
            equal-weighted.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ineq_change_decomp: not implemented."
    )
