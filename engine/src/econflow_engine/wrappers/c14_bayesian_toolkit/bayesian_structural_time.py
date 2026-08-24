# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bayesian_structural_time`` -- method card #204.

#204 Bayesian Structural Time Series (state specification: local/semilocal trend + seasonal + AR +
    spike-and-slab regression) with MCMC

Category 14-bayesian-toolkit; module ``bayesian_structural_time``.

Reference implementation: pymc-extras.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c14_bayesian_toolkit import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "bsts_components",
    "bsts_fit",
    "bsts_predict",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def bsts_fit(
    *,
    y: pd.Series | None = None,
    formula: str | None = None,
    data: pd.DataFrame | None = None,
    family: Literal["gaussian", "logit", "poisson", "student"] | None = None,
    local_linear_trend: bool | None = None,
    semilocal_linear_trend: bool | None = None,
    seasonal_nseasons: int | None = None,
    season_duration: int | None = None,
    ar_lags: int | None = None,
    niter: int | None = None,
    burn: int | None = None,
    expected_model_size: float | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``bsts_fit`` -- method card #204.

    Bayesian Structural Time Series (state specification: local/semilocal trend + seasonal + AR +
    spike-and-slab regression) with MCMC.

    Category 14-bayesian-toolkit; memory class ``mcmc``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, optional] Handle to a response ts (pure structural mode)· give ONE of y
            or formula+data.
        formula: [formula, optional] Regression formula 'y ~ x1 + x2' (spike-and-slab mode)·
            requires data.
        data: [df_handle, optional] Handle to a DataFrame with response + regressors (regression
            mode).
        family: [enum, optional] Observation family (default gaussian· student = heavy tails).
        local_linear_trend: [boolean, optional] AddLocalLinearTrend (default True)· mutually
            exclusive with semilocal. Default ``True``.
        semilocal_linear_trend: [boolean, optional] AddSemilocalLinearTrend (mean-reverting slope·
            better at long horizons). Default ``False``.
        seasonal_nseasons: [integer, optional] AddSeasonal nseasons (0 = off· otherwise >=2, e.g. 12
            monthly). Default ``0``.
        season_duration: [integer, optional] Duration of each season in steps (default 1). Default
            ``1``.
        ar_lags: [integer, optional] AddAr lags (0 = off· otherwise >=1). Default ``0``.
        niter: [integer, optional] Number of MCMC iterations (default 1000). Default ``1000``.
        burn: [integer, optional] Burn-in draws to discard (default None = SuggestBurn(0.1)).
        expected_model_size: [number, optional] Prior expected number of regressors
            (spike-and-slab)· ONLY in regression mode.
        seed: [integer, required] REQUIRED seed (MCMC determinism· seeded + BSTS C++ RNG).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "bsts_fit: not implemented."
    )


def bsts_predict(
    *,
    object: Any,
    horizon: int | None = None,
    newdata: pd.DataFrame | None = None,
    quantile_lower: float | None = None,
    quantile_upper: float | None = None,
    burn: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``bsts_predict`` -- method card #204.

    Bayesian Structural Time Series (state specification: local/semilocal trend + seasonal + AR +
    spike-and-slab regression) with MCMC.

    Category 14-bayesian-toolkit; memory class ``mcmc``.

    Args:
        object: [raw_handle, required] Handle to a fitted BSTS model (from bsts_fit).
        horizon: [integer, optional] Forecast horizon (>=1· default 12). Default ``12``.
        newdata: [df_handle, optional] Handle to future regressors (REQUIRED in regression models·
            nrow==horizon).
        quantile_lower: [number, optional] Lower quantile of the forecast band (default 0.025).
            Default ``0.025``.
        quantile_upper: [number, optional] Upper quantile of the forecast band (default 0.975).
            Default ``0.975``.
        burn: [integer, optional] Burn-in draws (default None = SuggestBurn(0.1)).
        seed: [integer, required] REQUIRED seed (posterior sampling determinism).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "bsts_predict: not implemented."
    )


def bsts_components(
    *,
    object: Any,
    burn: int | None = None,
    quantile_lower: float | None = None,
    quantile_upper: float | None = None,
) -> dict[str, Any]:
    """Node ``bsts_components`` -- method card #204.

    Bayesian Structural Time Series (state specification: local/semilocal trend + seasonal + AR +
    spike-and-slab regression) with MCMC.

    Category 14-bayesian-toolkit; memory class ``mcmc``.

    Args:
        object: [raw_handle, required] Handle to a fitted BSTS model (from bsts_fit).
        burn: [integer, optional] Burn-in draws (default None = SuggestBurn(0.1)).
        quantile_lower: [number, optional] Lower quantile per component (default 0.025). Default
            ``0.025``.
        quantile_upper: [number, optional] Upper quantile per component (default 0.975). Default
            ``0.975``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "bsts_components: not implemented."
    )
