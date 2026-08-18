# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``multivariate_factor_stochastic`` -- METHOD-SELECTION card #163.

#163 Multivariate factor stochastic volatility (Bayesian MCMC) + model-implied & predictive
    covariance/correlation

Category 06-volatility-regimes; module ``multivariate_factor_stochastic``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c06_volatility_regimes import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "fsv_cov",
    "fsv_predict",
    "fsv_sample",
    "NODE_META",
    "wire_model",
]


def fsv_sample(
    *,
    y: np.ndarray,
    factors: int | None = None,
    draws: int | None = None,
    burnin: int | None = None,
    restrict: Literal["none", "upper"] | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``fsv_sample`` -- METHOD-SELECTION card #163.

    Multivariate factor stochastic volatility (Bayesian MCMC) + model-implied & predictive
    covariance/correlation.

    Category 06-volatility-regimes; memory class ``mcmc``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        y: [matrix_handle, required] T×N returns matrix (>=2 columns, without NA/constant columns).
        factors: [integer, optional] Number of latent factors (integer 1..N· default 1). Default
            ``1``.
        draws: [integer, optional] MCMC draws after burn-in (default 300). Default ``300``.
        burnin: [integer, optional] Initial MCMC draws to discard (default 100). Default ``100``.
        restrict: [enum, optional] Factor loading restriction: 'none' (all estimated· preferred for
            cov/pred) or 'upper' (zeros above the diagonal· stabilises/identifies). Default none.
        seed: [integer, optional] MCMC reproducibility seed (default 2025). Default ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fsv_sample: not implemented. The method card is in ./README.md."
    )


def fsv_cov(
    *,
    object: Any,
) -> dict[str, Any]:
    """Node ``fsv_cov`` -- METHOD-SELECTION card #163.

    Multivariate factor stochastic volatility (Bayesian MCMC) + model-implied & predictive
    covariance/correlation.

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to an 'fsvdraws' (from fsv_sample).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fsv_cov: not implemented. The method card is in ./README.md."
    )


def fsv_predict(
    *,
    object: Any,
    ahead: Sequence[int] | None = None,
    each: int | None = None,
) -> dict[str, Any]:
    """Node ``fsv_predict`` -- METHOD-SELECTION card #163.

    Multivariate factor stochastic volatility (Bayesian MCMC) + model-implied & predictive
    covariance/correlation.

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to an 'fsvdraws' (from fsv_sample).
        ahead: [int_array, optional] Forecast horizons (positive integers, e.g. [1,5,10]· default
            [1]). Default ``1``.
        each: [integer, optional] Predictive draws per stored MCMC draw (default 1). Default ``1``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fsv_predict: not implemented. The method card is in ./README.md."
    )
