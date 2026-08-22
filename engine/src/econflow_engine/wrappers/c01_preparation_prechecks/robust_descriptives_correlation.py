# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``robust_descriptives_correlation`` -- method card #130.

#130 Robust descriptives + correlation prechecks (robust per-variable summary / correlation matrix
    with p-values / weighted mean-var-quantile)

Category 01-preparation-prechecks; module ``robust_descriptives_correlation``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "rdesc_correlation",
    "rdesc_describe",
    "rdesc_weighted_stats",
    "NODE_META",
    "wire_model",
]


def rdesc_describe(
    *,
    data: pd.DataFrame,
    digits: int | None = None,
) -> dict[str, Any]:
    """Node ``rdesc_describe`` -- method card #130.

    Robust descriptives + correlation prechecks (robust per-variable summary / correlation matrix
    with p-values / weighted mean-var-quantile).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a numeric DataFrame/matrix (all columns numeric,
            non-empty).
        digits: [integer, optional] Significant digits in the statistics (positive integer, doc
            default 4). Default ``4``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rdesc_describe: not implemented."
    )


def rdesc_correlation(
    *,
    data: pd.DataFrame,
    type: Literal["pearson", "spearman"] | None = None,
) -> dict[str, Any]:
    """Node ``rdesc_correlation`` -- method card #130.

    Robust descriptives + correlation prechecks (robust per-variable summary / correlation matrix
    with p-values / weighted mean-var-quantile).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a numeric matrix/df (>=5 rows, >=2 columns).
        type: [enum, optional] Correlation type (default pearson· spearman = rank-based).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rdesc_correlation: not implemented."
    )


def rdesc_weighted_stats(
    *,
    x: pd.Series,
    weights: Sequence[float],
    probs: Sequence[float] | None = None,
    var_method: Literal["unbiased", "ML"] | None = None,
    normwt: bool | None = None,
) -> dict[str, Any]:
    """Node ``rdesc_weighted_stats`` -- method card #130.

    Robust descriptives + correlation prechecks (robust per-variable summary / correlation matrix
    with p-values / weighted mean-var-quantile).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate numeric series/vector.
        weights: [num_array, required] Weights of the same length as x· non-negative, no NA/Inf,
            sum>0.
        probs: [num_array, optional] Quantiles within [0,1] (default [0,.25,.5,.75,1]).
        var_method: [enum, optional] Variance estimator of wtd.var (default unbiased/Bessel).
        normwt: [boolean, optional] Normalise the weights to length(x) (default False). Default
            ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rdesc_weighted_stats: not implemented."
    )
