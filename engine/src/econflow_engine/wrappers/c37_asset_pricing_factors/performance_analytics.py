# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``performance_analytics`` -- method card #323.

#323 Performance analytics: Sharpe, Sortino, information ratio, drawdown and turnover

Category 37-asset-pricing-factors; module ``performance_analytics``.

Reference implementation: ffn.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c37_asset_pricing_factors import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ap_drawdown",
    "ap_performance_summary",
    "ap_turnover",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ap_performance_summary(
    *,
    returns: pd.Series,
    benchmark: pd.Series | None = None,
    risk_free: pd.Series | None = None,
    frequency: Literal["daily", "weekly", "monthly", "quarterly", "annual"] | None = None,
    autocorrelation_adjust: bool | None = None,
) -> dict[str, Any]:
    """Node ``ap_performance_summary`` -- method card #323.

    Performance analytics: Sharpe, Sortino, information ratio, drawdown and turnover.

    Category 37-asset-pricing-factors; memory class ``light``.

    Args:
        returns: [series_handle, required] Portfolio return series.
        benchmark: [series_handle, optional] Benchmark return series.
        risk_free: [series_handle, optional] Risk-free rate series.
        frequency: [enum, optional] Return frequency for annualisation. Default ``'monthly'``.
        autocorrelation_adjust: [boolean, optional] Apply the Lo autocorrelation correction. Default
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
        "ap_performance_summary: not implemented."
    )


def ap_drawdown(
    *,
    returns: pd.Series,
    top_n: int | None = None,
) -> dict[str, Any]:
    """Node ``ap_drawdown`` -- method card #323.

    Performance analytics: Sharpe, Sortino, information ratio, drawdown and turnover.

    Category 37-asset-pricing-factors; memory class ``light``.

    Args:
        returns: [series_handle, required] Portfolio return series.
        top_n: [integer, optional] Number of largest drawdowns to report. Default ``5``.

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
        "ap_drawdown: not implemented."
    )


def ap_turnover(
    *,
    weights: pd.DataFrame,
    cost_bps: float | None = None,
) -> dict[str, Any]:
    """Node ``ap_turnover`` -- method card #323.

    Performance analytics: Sharpe, Sortino, information ratio, drawdown and turnover.

    Category 37-asset-pricing-factors; memory class ``light``.

    Args:
        weights: [df_handle, required] Panel of portfolio weights over time.
        cost_bps: [number, optional] Round-trip cost in basis points. Default ``10.0``.

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
        "ap_turnover: not implemented."
    )
