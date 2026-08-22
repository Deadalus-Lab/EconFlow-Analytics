# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``joint_regression_esr`` -- method card #194.

#194 Joint (VaR, ES) regression (Fissler-Ziegel) + an ESR-based Expected Shortfall backtest

Category 12-distribution-risk; module ``joint_regression_esr``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c12_distribution_risk import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "es_backtest",
    "es_joint_reg",
    "NODE_META",
    "wire_model",
]


def es_joint_reg(
    *,
    formula: str,
    data: pd.DataFrame,
    alpha: float,
    g1: Literal["2", "1"] | None = None,
    g2: Literal["1", "2", "3", "4", "5"] | None = None,
    early_stopping: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``es_joint_reg`` -- method card #194.

    Joint (VaR, ES) regression (Fissler-Ziegel) + an ESR-based Expected Shortfall backtest.

    Category 12-distribution-risk; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] Joint (VaR,ES) formula· supports two-part 'y ~ xq | xe' (1st
            part = quantile/VaR equation, 2nd = ES)· a single set -> shared by both.
        data: [df_handle, required] Handle to a DataFrame with the response and the regressors
            (without NA in the variables).
        alpha: [number, required] Probability level in the open (0,1), e.g. 0.025 (2.5% VaR/ES).
        g1: [enum, optional] Specification function G1 of the quantile equation· 2=G1(z)=0
            (default), 1=G1(z)=z.
        g2: [enum, optional] Specification function G2 of the ES equation (default 1)· types 1-3
            require negative ES values.
        early_stopping: [integer, optional] Stop the iterated local search if there is no
            improvement within this many steps (default 10). Default ``10``.
        seed: [integer, optional] Reproducibility seed for the ILS optimization (default 2025).
            Default ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "es_joint_reg: not implemented."
    )


def es_backtest(
    *,
    r: Sequence[float],
    q: Sequence[float],
    e: Sequence[float],
    alpha: float,
    version: Literal["1", "2", "3"] | None = None,
    B: int | None = None,
    sparsity: Literal["nid", "iid"] | None = None,
    sigma_est: Literal["scl_sp", "ind", "scl_N"] | None = None,
    misspec: bool | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``es_backtest`` -- method card #194.

    Joint (VaR, ES) regression (Fissler-Ziegel) + an ESR-based Expected Shortfall backtest.

    Category 12-distribution-risk; memory class ``heavy``.

    Args:
        r: [num_array, required] Vector of realized returns (without NA).
        q: [num_array, required] Vector of VaR forecasts of the same length as r (typically
            negative).
        e: [num_array, required] Vector of Expected Shortfall forecasts of the same length as r
            (typically negative, more extreme than q).
        alpha: [number, required] Probability level in the open (0,1), e.g. 0.025.
        version: [enum, optional] 1=Strict ESR (default)· 2=Auxiliary ESR (regress on q & e)·
            3=Strict Intercept (+ one-sided p-values).
        B: [integer, optional] Number of bootstrap samples· 0 = without bootstrap (default). >0 ->
            fills the pvalue_*_bootstrap. Default ``0``.
        sparsity: [enum, optional] Sparsity estimator in Lambda (cov_config, default nid).
        sigma_est: [enum, optional] Sigma estimator in the sandwich (cov_config, default scl_sp).
        misspec: [boolean, optional] If True (default) the estimator accounts for possible
            misspecification (cov_config). Default ``True``.
        seed: [integer, optional] Reproducibility seed for the bootstrap when B>0 (default 2025).
            Default ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "es_backtest: not implemented."
    )
