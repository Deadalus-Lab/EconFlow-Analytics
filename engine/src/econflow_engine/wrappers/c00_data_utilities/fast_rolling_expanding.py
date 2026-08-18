# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``fast_rolling_expanding`` -- METHOD-SELECTION card #109.

#109 Fast rolling & expanding window statistics on vector/matrix (mean/sd/var, cor/cov, z-score,
    quantile, rolling regression)

Category 00-data-utilities; module ``fast_rolling_expanding``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "rll_cor",
    "rll_cov",
    "rll_lm",
    "rll_mean",
    "rll_quantile",
    "rll_scale",
    "rll_sd",
    "rll_var",
    "NODE_META",
    "wire_model",
]


def rll_mean(
    *,
    x: np.ndarray,
    width: int,
    weights: Sequence[float] | None = None,
    min_obs: int | None = None,
    online: bool | None = None,
) -> dict[str, Any]:
    """Node ``rll_mean`` -- METHOD-SELECTION card #109.

    Fast rolling & expanding window statistics on vector/matrix (mean/sd/var, cor/cov, z-score,
    quantile, rolling regression).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric vector/matrix (rows=observations,
            columns=variables).
        width: [integer, required] Rolling window size (integer in [1, nobs]).
        weights: [num_array, optional] Weights of length width (finite); empty=equal weights.
        min_obs: [integer, optional] Minimum non-NA observations in [1, width]; empty=width.
        online: [boolean, optional] Online (incremental) algorithm (default True). Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rll_mean: not implemented. The method card is in ./README.md."
    )


def rll_sd(
    *,
    x: np.ndarray,
    width: int,
    weights: Sequence[float] | None = None,
    center: bool | None = None,
    min_obs: int | None = None,
    online: bool | None = None,
) -> dict[str, Any]:
    """Node ``rll_sd`` -- METHOD-SELECTION card #109.

    Fast rolling & expanding window statistics on vector/matrix (mean/sd/var, cor/cov, z-score,
    quantile, rolling regression).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric vector/matrix.
        width: [integer, required] Rolling window size (integer in [1, nobs]).
        weights: [num_array, optional] Weights of length width; empty=equal weights.
        center: [boolean, optional] Center before scaling (default True). Default ``True``.
        min_obs: [integer, optional] Minimum non-NA observations in [1, width]; empty=width.
        online: [boolean, optional] Online algorithm (default True). Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rll_sd: not implemented. The method card is in ./README.md."
    )


def rll_var(
    *,
    x: np.ndarray,
    width: int,
    weights: Sequence[float] | None = None,
    center: bool | None = None,
    min_obs: int | None = None,
    online: bool | None = None,
) -> dict[str, Any]:
    """Node ``rll_var`` -- METHOD-SELECTION card #109.

    Fast rolling & expanding window statistics on vector/matrix (mean/sd/var, cor/cov, z-score,
    quantile, rolling regression).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric vector/matrix.
        width: [integer, required] Rolling window size (integer in [1, nobs]).
        weights: [num_array, optional] Weights of length width; empty=equal weights.
        center: [boolean, optional] Centering (default True); unbiased divisor n-1. Default
            ``True``.
        min_obs: [integer, optional] Minimum non-NA observations in [1, width]; empty=width.
        online: [boolean, optional] Online algorithm (default True). Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rll_var: not implemented. The method card is in ./README.md."
    )


def rll_cor(
    *,
    x: np.ndarray,
    y: np.ndarray | None = None,
    width: int,
    weights: Sequence[float] | None = None,
    center: bool | None = None,
    scale: bool | None = None,
    min_obs: int | None = None,
    online: bool | None = None,
) -> dict[str, Any]:
    """Node ``rll_cor`` -- METHOD-SELECTION card #109.

    Fast rolling & expanding window statistics on vector/matrix (mean/sd/var, cor/cov, z-score,
    quantile, rolling regression).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric matrix (y=None -> k×k×n array) or vector
            (with y).
        y: [matrix_handle, optional] Optional 2nd handle (equal number of rows); if given ->
            pairwise rolling correlation.
        width: [integer, required] Rolling window size (integer in [1, nobs]).
        weights: [num_array, optional] Weights of length width; empty=equal weights.
        center: [boolean, optional] Centering (default True). Default ``True``.
        scale: [boolean, optional] Scaling (default True for correlation). Default ``True``.
        min_obs: [integer, optional] Minimum non-NA observations in [1, width]; empty=width.
        online: [boolean, optional] Online algorithm (default True). Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rll_cor: not implemented. The method card is in ./README.md."
    )


def rll_cov(
    *,
    x: np.ndarray,
    y: np.ndarray | None = None,
    width: int,
    weights: Sequence[float] | None = None,
    center: bool | None = None,
    scale: bool | None = None,
    min_obs: int | None = None,
    online: bool | None = None,
) -> dict[str, Any]:
    """Node ``rll_cov`` -- METHOD-SELECTION card #109.

    Fast rolling & expanding window statistics on vector/matrix (mean/sd/var, cor/cov, z-score,
    quantile, rolling regression).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric matrix (y=None -> k×k×n array) or vector
            (with y).
        y: [matrix_handle, optional] Optional 2nd handle (equal number of rows); if given ->
            pairwise rolling covariance.
        width: [integer, required] Rolling window size (integer in [1, nobs]).
        weights: [num_array, optional] Weights of length width; empty=equal weights.
        center: [boolean, optional] Centering (default True). Default ``True``.
        scale: [boolean, optional] Scaling (default False for covariance). Default ``False``.
        min_obs: [integer, optional] Minimum non-NA observations in [1, width]; empty=width.
        online: [boolean, optional] Online algorithm (default True). Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rll_cov: not implemented. The method card is in ./README.md."
    )


def rll_lm(
    *,
    x: np.ndarray,
    y: np.ndarray,
    width: int,
    weights: Sequence[float] | None = None,
    intercept: bool | None = None,
    min_obs: int | None = None,
    online: bool | None = None,
) -> dict[str, Any]:
    """Node ``rll_lm`` -- METHOD-SELECTION card #109.

    Fast rolling & expanding window statistics on vector/matrix (mean/sd/var, cor/cov, z-score,
    quantile, rolling regression).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to the predictor(s) vector/matrix (rows=observations).
        y: [matrix_handle, required] Handle to the response vector/matrix (equal number of rows as
            x).
        width: [integer, required] Rolling window size (integer in [1, nobs]).
        weights: [num_array, optional] Weights of length width; empty=equal weights.
        intercept: [boolean, optional] Constant term (default True). Default ``True``.
        min_obs: [integer, optional] Minimum non-NA observations in [1, width]; empty=width.
        online: [boolean, optional] Online algorithm (default True). Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rll_lm: not implemented. The method card is in ./README.md."
    )


def rll_scale(
    *,
    x: np.ndarray,
    width: int,
    weights: Sequence[float] | None = None,
    center: bool | None = None,
    scale: bool | None = None,
    min_obs: int | None = None,
    online: bool | None = None,
) -> dict[str, Any]:
    """Node ``rll_scale`` -- METHOD-SELECTION card #109.

    Fast rolling & expanding window statistics on vector/matrix (mean/sd/var, cor/cov, z-score,
    quantile, rolling regression).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric vector/matrix for a rolling z-score.
        width: [integer, required] Rolling window size (integer in [1, nobs]).
        weights: [num_array, optional] Weights of length width; empty=equal weights.
        center: [boolean, optional] Subtract the rolling mean (default True). Default ``True``.
        scale: [boolean, optional] Divide by the rolling sd (default True). Default ``True``.
        min_obs: [integer, optional] Minimum non-NA observations in [1, width]; empty=width.
        online: [boolean, optional] Online algorithm (default True). Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rll_scale: not implemented. The method card is in ./README.md."
    )


def rll_quantile(
    *,
    x: np.ndarray,
    width: int,
    weights: Sequence[float] | None = None,
    p: float | None = None,
    min_obs: int | None = None,
    online: bool | None = None,
) -> dict[str, Any]:
    """Node ``rll_quantile`` -- METHOD-SELECTION card #109.

    Fast rolling & expanding window statistics on vector/matrix (mean/sd/var, cor/cov, z-score,
    quantile, rolling regression).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric vector/matrix.
        width: [integer, required] Rolling window size (integer in [1, nobs]).
        weights: [num_array, optional] Weights of length width; empty=equal weights.
        p: [number, optional] Quantile probability in [0,1] (default 0.5 = median). Default ``0.5``.
        min_obs: [integer, optional] Minimum non-NA observations in [1, width]; empty=width.
        online: [boolean, optional] Online algorithm (default True). Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rll_quantile: not implemented. The method card is in ./README.md."
    )
