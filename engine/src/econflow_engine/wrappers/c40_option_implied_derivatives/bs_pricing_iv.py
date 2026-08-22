# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bs_pricing_iv`` -- method card #340.

#340 Black-Scholes and Bachelier pricing, Greeks and implied-volatility inversion

Category 40-option-implied-derivatives; module ``bs_pricing_iv``.

Reference implementation: py-vollib.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c40_option_implied_derivatives import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "opt_implied_volatility",
    "opt_price",
    "NODE_META",
    "wire_model",
]


def opt_price(
    *,
    spot: float,
    strike: float,
    time_to_expiry: float,
    rate: float,
    volatility: float,
    option_type: Literal["call", "put"],
    model: Literal["black_scholes", "bachelier", "black76"] | None = None,
    dividend: float | None = None,
) -> dict[str, Any]:
    """Node ``opt_price`` -- method card #340.

    Black-Scholes and Bachelier pricing, Greeks and implied-volatility inversion.

    Category 40-option-implied-derivatives; memory class ``light``.

    Args:
        spot: [number, required] Spot price of the underlying.
        strike: [number, required] Strike price.
        time_to_expiry: [number, required] Time to expiry in years.
        rate: [number, required] Risk-free rate.
        volatility: [number, required] Volatility input.
        option_type: [enum, required] Option type.
        model: [enum, optional] Pricing model. Default ``'black_scholes'``.
        dividend: [number, optional] Continuous dividend yield. Default ``0.0``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "opt_price: not implemented."
    )


def opt_implied_volatility(
    *,
    price: pd.Series,
    spot: pd.Series,
    strike: pd.Series,
    time_to_expiry: pd.Series,
    rate: pd.Series,
    option_type: pd.Series,
    model: Literal["black_scholes", "bachelier", "black76"] | None = None,
) -> dict[str, Any]:
    """Node ``opt_implied_volatility`` -- method card #340.

    Black-Scholes and Bachelier pricing, Greeks and implied-volatility inversion.

    Category 40-option-implied-derivatives; memory class ``light``.

    Args:
        price: [series_handle, required] Observed option prices.
        spot: [series_handle, required] Spot prices.
        strike: [series_handle, required] Strikes.
        time_to_expiry: [series_handle, required] Times to expiry in years.
        rate: [series_handle, required] Risk-free rates.
        option_type: [series_handle, required] Option types.
        model: [enum, optional] Pricing model. Default ``'black_scholes'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "opt_implied_volatility: not implemented."
    )
