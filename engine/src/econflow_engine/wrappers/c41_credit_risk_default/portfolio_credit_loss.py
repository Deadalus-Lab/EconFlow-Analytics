# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``portfolio_credit_loss`` -- method card #353.

#353 Portfolio credit loss distribution: Vasicek single- and multi-factor and Monte Carlo

Category 41-credit-risk-default; module ``portfolio_credit_loss``.

Reference implementation: scipy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c41_credit_risk_default import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cr_concentration",
    "cr_credit_monte_carlo",
    "cr_vasicek_loss",
    "NODE_META",
    "wire_model",
]


def cr_vasicek_loss(
    *,
    pd: pd.Series,
    lgd: pd.Series,
    exposure: pd.Series,
    asset_correlation: float,
    confidence: float | None = None,
) -> dict[str, Any]:
    """Node ``cr_vasicek_loss`` -- method card #353.

    Portfolio credit loss distribution: Vasicek single- and multi-factor and Monte Carlo.

    Category 41-credit-risk-default; memory class ``light``.

    Args:
        pd: [series_handle, required] Default probability per exposure.
        lgd: [series_handle, required] Loss given default per exposure.
        exposure: [series_handle, required] Exposure at default.
        asset_correlation: [number, required] Asset correlation.
        confidence: [number, optional] Tail level for VaR and ES. Default ``0.999``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cr_vasicek_loss: not implemented."
    )


def cr_credit_monte_carlo(
    *,
    pd: pd.Series,
    lgd: pd.Series,
    exposure: pd.Series,
    factor_loadings: np.ndarray,
    n_simulations: int | None = None,
    confidence: float | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``cr_credit_monte_carlo`` -- method card #353.

    Portfolio credit loss distribution: Vasicek single- and multi-factor and Monte Carlo.

    Category 41-credit-risk-default; memory class ``light``.

    Args:
        pd: [series_handle, required] Default probability per exposure.
        lgd: [series_handle, required] Loss given default per exposure.
        exposure: [series_handle, required] Exposure at default.
        factor_loadings: [matrix_handle, required] Systematic factor loadings per exposure.
        n_simulations: [integer, optional] Monte Carlo draws. Default ``100000``.
        confidence: [number, optional] Tail level for VaR and ES. Default ``0.999``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cr_credit_monte_carlo: not implemented."
    )


def cr_concentration(
    *,
    exposure: pd.Series,
    pd: pd.Series | None = None,
    sector: pd.Series | None = None,
) -> dict[str, Any]:
    """Node ``cr_concentration`` -- method card #353.

    Portfolio credit loss distribution: Vasicek single- and multi-factor and Monte Carlo.

    Category 41-credit-risk-default; memory class ``light``.

    Args:
        exposure: [series_handle, required] Exposure at default.
        pd: [series_handle, optional] Default probability per exposure.
        sector: [series_handle, optional] Sector label per exposure.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cr_concentration: not implemented."
    )
