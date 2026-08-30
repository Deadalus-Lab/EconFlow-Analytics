# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``univariate_garch_family`` -- method card #28.

#28 Univariate GARCH family

Category 06-volatility-regimes; module ``univariate_garch_family``.

Reference implementation: arch.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c06_volatility_regimes import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ga_diagnostics",
    "ga_fit",
    "ga_forecast",
    "ga_roll",
    "ga_sim",
    "ga_spec",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ga_spec(
    *,
    model: (
        Literal[
            "sGARCH",
            "fGARCH",
            "eGARCH",
            "gjrGARCH",
            "apARCH",
            "iGARCH",
            "csGARCH",
            "fiGARCH",
        ]
        | None
    ) = None,
    garchOrder: Sequence[int] | None = None,
    armaOrder: Sequence[int] | None = None,
    submodel: str | None = None,
    distribution_model: (
        Literal[
            "norm",
            "snorm",
            "std",
            "sstd",
            "ged",
            "sged",
            "nig",
            "ghyp",
            "ghst",
            "jsu",
        ]
        | None
    ) = None,
    include_mean: bool | None = None,
    archm: bool | None = None,
    archpow: int | None = None,
    variance_targeting: bool | None = None,
) -> dict[str, Any]:
    """Node ``ga_spec`` -- method card #28.

    Univariate GARCH family.

    Category 06-volatility-regimes; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        model: [enum, optional] Variance model type (default sGARCH· fGARCH requires a submodel).
        garchOrder: [int_array, optional] GARCH order [p,q] (default [1,1]· e.g. [2,1]).
        armaOrder: [int_array, optional] ARMA order of the mean model [AR,MA] (default [1,1]).
        submodel: [string, optional] Submodel for model='fGARCH' (e.g. 'GARCH','TGARCH','NGARCH').
        distribution_model: [enum, optional] Innovation distribution (default norm· std/sstd for fat
            tails).
        include_mean: [boolean, optional] Include a constant term in the mean model. Default
            ``True``.
        archm: [boolean, optional] ARCH-in-mean (risk in the mean). Default ``False``.
        archpow: [integer, optional] ARCH-in-mean power (1=st.dev, 2=variance). Default ``1``.
        variance_targeting: [boolean, optional] Variance targeting (omega from the sample uncond.
            variance). Default ``False``.

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
        "ga_spec: not implemented."
    )


def ga_fit(
    *,
    spec: Any,
    data: pd.Series,
    out_sample: int | None = None,
    solver: Literal["hybrid", "solnp", "nlminb", "lbfgs", "gosolnp"] | None = None,
) -> dict[str, Any]:
    """Node ``ga_fit`` -- method card #28.

    Univariate GARCH family.

    Category 06-volatility-regimes; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        spec: [raw_handle, required] Handle to a 'uGARCHspec' (from ga_spec).
        data: [series_handle, required] Handle to a univariate numeric series (returns, without NA).
        out_sample: [integer, optional] Out-of-sample observations for the backtest (default 0).
            Default ``0``.
        solver: [enum, optional] ML optimizer (default hybrid).

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
        "ga_fit: not implemented."
    )


def ga_forecast(
    *,
    fit: Any,
    n_ahead: int | None = None,
    n_roll: int | None = None,
) -> dict[str, Any]:
    """Node ``ga_forecast`` -- method card #28.

    Univariate GARCH family.

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a 'uGARCHfit' (from ga_fit).
        n_ahead: [integer, optional] Forecast horizon (>=1, default 10). Default ``10``.
        n_roll: [integer, optional] Rolling forecasts over out.sample (default 0). Default ``0``.

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
        "ga_forecast: not implemented."
    )


def ga_sim(
    *,
    fit: Any,
    n_sim: int | None = None,
    n_start: int | None = None,
    m_sim: int | None = None,
) -> dict[str, Any]:
    """Node ``ga_sim`` -- method card #28.

    Univariate GARCH family.

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a 'uGARCHfit' (from ga_fit).
        n_sim: [integer, optional] Length of each simulated path (default 1000). Default ``1000``.
        n_start: [integer, optional] Burn-in observations (default 0). Default ``0``.
        m_sim: [integer, optional] Number of independent paths (default 1· seeded). Default ``1``.

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
        "ga_sim: not implemented."
    )


def ga_roll(
    *,
    spec: Any,
    data: pd.Series,
    forecast_length: int | None = None,
    refit_every: int | None = None,
    refit_window: Literal["recursive", "moving"] | None = None,
    solver: Literal["hybrid", "solnp", "nlminb", "lbfgs", "gosolnp"] | None = None,
    calculate_VaR: bool | None = None,
) -> dict[str, Any]:
    """Node ``ga_roll`` -- method card #28.

    Univariate GARCH family.

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        spec: [raw_handle, required] Handle to a 'uGARCHspec' (from ga_spec).
        data: [series_handle, required] Handle to a univariate numeric series (returns).
        forecast_length: [integer, optional] Length of the rolling out-of-sample period (default
            500). Default ``500``.
        refit_every: [integer, optional] Re-estimate every n steps (default 25). Default ``25``.
        refit_window: [enum, optional] Re-estimation window (default recursive).
        solver: [enum, optional] Optimizer (default hybrid).
        calculate_VaR: [boolean, optional] Compute VaR + backtest on the rolling forecast. Default
            ``True``.

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
        "ga_roll: not implemented."
    )


def ga_diagnostics(
    *,
    fit: Any,
    gof_groups: int | None = None,
) -> dict[str, Any]:
    """Node ``ga_diagnostics`` -- method card #28.

    Univariate GARCH family.

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a 'uGARCHfit' (from ga_fit).
        gof_groups: [integer, optional] Goodness-of-fit test groups (must be > parameters+1, default
            20). Default ``20``.

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
        "ga_diagnostics: not implemented."
    )
