# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``generalized_autoregressive_score`` -- method card #158.

#158 Generalized Autoregressive Score / Dynamic Conditional Score (GAS/DCS) — a time-varying
    volatility/location/tails

Category 06-volatility-regimes; module ``generalized_autoregressive_score``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

from econflow_engine.generated.args.c06_volatility_regimes import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "gas_fit",
    "gas_forecast",
    "gas_simulate",
    "NODE_META",
    "wire_model",
]


def gas_fit(
    *,
    y: Sequence[float],
    distr: (
        Literal[
            "norm",
            "t",
            "ged",
            "laplace",
            "alaplace",
            "logistic",
            "gamma",
            "exp",
            "weibull",
            "lognorm",
            "fisk",
            "rayleigh",
        ]
        | None
    ) = None,
    scaling: (
        Literal[
            "unit",
            "fisher_inv_sqrt",
            "fisher_inv",
            "full_fisher_inv_sqrt",
            "full_fisher_inv",
            "diag_fisher_inv_sqrt",
            "diag_fisher_inv",
        ]
        | None
    ) = None,
    param: str | None = None,
    p: int | None = None,
    q: int | None = None,
    par_static: Sequence[int] | None = None,
    maxeval: int | None = None,
) -> dict[str, Any]:
    """Node ``gas_fit`` -- method card #158.

    Generalized Autoregressive Score / Dynamic Conditional Score (GAS/DCS) — a time-varying
    volatility/location/tails.

    Category 06-volatility-regimes; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        y: [num_array, required] Univariate series (returns without NA· positive values for
            gamma/exp/weibull/lognorm/fisk/rayleigh).
        distr: [enum, optional] Conditional innovation distribution (default norm· t/ged for fat
            tails· gamma etc. for positive duration series). Default ``'norm'``.
        scaling: [enum, optional] Scaling of the score (default unit=fastest· fisher_* far heavier,
            numerical Fisher information). Default ``'unit'``.
        param: [string, optional] Parameterisation of the distribution (e.g. 'rate'/'scale' for
            gamma)· None=the distribution default.
        p: [integer, optional] Score order (non-negative integer, default 1). Default ``1``.
        q: [integer, optional] Autoregressive order (non-negative integer, default 1). Default
            ``1``.
        par_static: [int_array, optional] 0/1 vector: which parameters are static· e.g. norm+[1,0]
            drives the VARIANCE (vol model) instead of the mean.
        maxeval: [integer, optional] Cap on ML iterations (default 10000 instead of 1e6)· guarantees
            finite runtime· non-convergence -> converged=False. Default ``10000``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "gas_fit: not implemented."
    )


def gas_forecast(
    *,
    object: Any,
    method: Literal["mean_path", "simulated_paths"] | None = None,
    t_ahead: int | None = None,
    rep_ahead: int | None = None,
    quant: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``gas_forecast`` -- method card #158.

    Generalized Autoregressive Score / Dynamic Conditional Score (GAS/DCS) — a time-varying
    volatility/location/tails.

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a 'gas' object (from gas_fit).
        method: [enum, optional] mean_path=deterministic point path· simulated_paths=simulation +
            quantiles (STOCHASTIC, seeded). Default ``'mean_path'``.
        t_ahead: [integer, optional] Forecast horizon (integer >=1, default 10). Default ``10``.
        rep_ahead: [integer, optional] Number of simulated paths (simulated_paths only, default
            1000). Default ``1000``.
        quant: [num_array, optional] Quantile probabilities of the predictive distribution in (0,1)
            (simulated_paths only). Default ``[0.025, 0.975]``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "gas_forecast: not implemented."
    )


def gas_simulate(
    *,
    object: Any,
    t_sim: int | None = None,
) -> dict[str, Any]:
    """Node ``gas_simulate`` -- method card #158.

    Generalized Autoregressive Score / Dynamic Conditional Score (GAS/DCS) — a time-varying
    volatility/location/tails.

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a 'gas' object (from gas_fit).
        t_sim: [integer, optional] Length of the simulated path (integer >=1, default 10· seeded).
            Default ``10``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "gas_simulate: not implemented."
    )
