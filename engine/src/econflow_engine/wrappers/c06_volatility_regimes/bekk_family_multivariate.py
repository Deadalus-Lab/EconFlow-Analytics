# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bekk_family_multivariate`` -- METHOD-SELECTION card #160.

#160 BEKK-family multivariate GARCH (BEKK/diagonal/scalar) + multivariate VaR + Volatility IRF

Category 06-volatility-regimes; module ``bekk_family_multivariate``.

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
    "bekk_estimate",
    "bekk_var",
    "bekk_virf",
    "NODE_META",
    "wire_model",
]


def bekk_estimate(
    *,
    y: np.ndarray,
    type: Literal["bekk", "dbekk", "sbekk"] | None = None,
    asymmetric: bool | None = None,
    signs: Sequence[float] | None = None,
    QML_t_ratios: bool | None = None,
    max_iter: int | None = None,
    crit: float | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``bekk_estimate`` -- METHOD-SELECTION card #160.

    BEKK-family multivariate GARCH (BEKK/diagonal/scalar) + multivariate VaR + Volatility IRF.

    Category 06-volatility-regimes; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        y: [matrix_handle, required] Handle to a T×N returns matrix (N>=2, without NA).
        type: [enum, optional] BEKK type (default bekk· dbekk=diagonal, sbekk=scalar).
        asymmetric: [boolean, optional] Asymmetric (leverage) volatility structure. Default
            ``False``.
        signs: [num_array, optional] N-vector of {1,-1} for asymmetric effects (asymmetric=True
            only· default rep(-1,N)).
        QML_t_ratios: [boolean, optional] QML (robust) t-ratios instead of asymptotic ones. Default
            ``False``.
        max_iter: [integer, optional] Maximum BHHH iterations (default 50). Default ``50``.
        crit: [number, optional] BHHH convergence criterion (default 1e-9). Default ``1e-09``.
        seed: [integer, optional] Reproducibility seed (default 2025). Default ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bekk_estimate: not implemented. The method card is in ./README.md."
    )


def bekk_var(
    *,
    object: Any,
    p: float | None = None,
    portfolio_weights: Sequence[float] | None = None,
    distribution: Literal["normal", "empirical", "t"] | None = None,
) -> dict[str, Any]:
    """Node ``bekk_var`` -- METHOD-SELECTION card #160.

    BEKK-family multivariate GARCH (BEKK/diagonal/scalar) + multivariate VaR + Volatility IRF.

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a 'bekkFit' (from bekk_estimate).
        p: [number, optional] VaR confidence level in (0,1) (default 0.99, Basel). Default ``0.99``.
        portfolio_weights: [num_array, optional] N-vector of portfolio weights (None -> per-series
            VaR).
        distribution: [enum, optional] Residual distribution (default normal· empirical requires
            >=1000 obs).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bekk_var: not implemented. The method card is in ./README.md."
    )


def bekk_virf(
    *,
    object: Any,
    time: int | None = None,
    q: float | None = None,
    index_series: int | None = None,
    n_ahead: int | None = None,
    ci: float | None = None,
    time_shock: bool | None = None,
) -> dict[str, Any]:
    """Node ``bekk_virf`` -- METHOD-SELECTION card #160.

    BEKK-family multivariate GARCH (BEKK/diagonal/scalar) + multivariate VaR + Volatility IRF.

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a SYMMETRIC 'bekkFit' (from bekk_estimate·
            asymmetric=False).
        time: [integer, optional] Time point of the shock (1..T). Default ``1``.
        q: [number, optional] Quantile of the shock in (0,1) (default 0.05). Default ``0.05``.
        index_series: [integer, optional] Series the shock is applied to (1..N). Default ``1``.
        n_ahead: [integer, optional] VIRF horizon (>=1, default 10). Default ``10``.
        ci: [number, optional] Confidence band level in (0,1) (default 0.9). Default ``0.9``.
        time_shock: [boolean, optional] Use the estimated residuals at 'time' as the shock. Default
            ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bekk_virf: not implemented. The method card is in ./README.md."
    )
