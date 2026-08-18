# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``multivariate_garch_dynamic`` -- METHOD-SELECTION card #155.

#155 Multivariate GARCH — Dynamic Conditional Correlation (DCC/aDCC/CCC)

Category 06-volatility-regimes; module ``multivariate_garch_dynamic``.

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
    "tm_cov",
    "tm_dcc_estimate",
    "tm_predict",
    "NODE_META",
    "wire_model",
]


def tm_dcc_estimate(
    *,
    y: np.ndarray,
    dynamics: Literal["constant", "dcc", "adcc"] | None = None,
    distribution: Literal["mvn", "mvt"] | None = None,
    garch_model: (
        Literal[
            "garch",
            "gjrgarch",
            "aparch",
            "egarch",
            "fgarch",
            "cgarch",
            "igarch",
            "ewma",
        ]
        | None
    ) = None,
    garch_order: Sequence[int] | None = None,
    garch_distribution: (
        Literal[
            "norm",
            "std",
            "snorm",
            "sstd",
            "ged",
            "sged",
            "nig",
            "gh",
            "jsu",
            "ghst",
        ]
        | None
    ) = None,
    dcc_order: Sequence[int] | None = None,
    solver: Literal["solnp", "nloptr"] | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``tm_dcc_estimate`` -- METHOD-SELECTION card #155.

    Multivariate GARCH — Dynamic Conditional Correlation (DCC/aDCC/CCC).

    Category 06-volatility-regimes; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        y: [matrix_handle, required] Handle to a numeric T×N returns matrix (N=2-3, without NA, no
            constant column).
        dynamics: [enum, optional] Correlation dynamics: constant=CCC (fixed), dcc=Engle DCC,
            adcc=asymmetric DCC (default constant).
        distribution: [enum, optional] Multivariate innovation distribution: mvn=normal, mvt=t (fat
            tails) (default mvn).
        garch_model: [enum, optional] Univariate variance model per series (shared, default garch).
            Default ``'garch'``.
        garch_order: [int_array, optional] GARCH order [p,q] of the univariate models (default
            [1,1]).
        garch_distribution: [enum, optional] Univariate innovation distribution per series (default
            norm). Default ``'norm'``.
        dcc_order: [int_array, optional] DCC order [a,b] of the correlation dynamics (default [1,1]·
            ignored when constant).
        solver: [enum, optional] Second-stage ML optimizer (default solnp).
        seed: [integer, optional] Reproducibility seed (ML is deterministic· default 2025). Default
            ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tm_dcc_estimate: not implemented. The method card is in ./README.md."
    )


def tm_predict(
    *,
    object: Any,
    h: int | None = None,
    nsim: int | None = None,
    sim_method: Literal["parametric", "bootstrap"] | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``tm_predict`` -- METHOD-SELECTION card #155.

    Multivariate GARCH — Dynamic Conditional Correlation (DCC/aDCC/CCC).

    Category 06-volatility-regimes; memory class ``heavy``.

    Args:
        object: [raw_handle, required] Handle to a 'dcc.estimate' (from tm_dcc_estimate).
        h: [integer, optional] Forecast horizon for conditional covariance/correlation (>=1, default
            1). Default ``1``.
        nsim: [integer, optional] Number of simulated paths for the forecast distribution (default
            1000· seeded). Default ``1000``.
        sim_method: [enum, optional] parametric=draw from the assumed distribution·
            bootstrap=resample residuals (default parametric).
        seed: [integer, optional] Seed for the stochastic simulation (default 2025). Default
            ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tm_predict: not implemented. The method card is in ./README.md."
    )


def tm_cov(
    *,
    object: Any,
    correlation: bool | None = None,
) -> dict[str, Any]:
    """Node ``tm_cov`` -- METHOD-SELECTION card #155.

    Multivariate GARCH — Dynamic Conditional Correlation (DCC/aDCC/CCC).

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a 'dcc.estimate' (from tm_dcc_estimate).
        correlation: [boolean, optional] True -> the `array` field becomes the conditional
            correlation instead of the covariance (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tm_cov: not implemented. The method card is in ./README.md."
    )
