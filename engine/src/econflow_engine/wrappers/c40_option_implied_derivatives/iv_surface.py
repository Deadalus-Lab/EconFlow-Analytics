# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``iv_surface`` -- method card #341.

#341 Implied-volatility surface fitting with SVI and SABR, and arbitrage checks

Category 40-option-implied-derivatives; module ``iv_surface``.

Reference implementation: QuantLib.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c40_option_implied_derivatives import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "opt_arbitrage_check",
    "opt_fit_surface",
    "opt_surface_evaluate",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def opt_fit_surface(
    *,
    strikes: pd.Series,
    expiries: pd.Series,
    implied_vols: pd.Series,
    forward: pd.Series,
    model: Literal["svi", "ssvi", "sabr", "cubic_spline"] | None = None,
    enforce_no_arbitrage: bool | None = None,
) -> dict[str, Any]:
    """Node ``opt_fit_surface`` -- method card #341.

    Implied-volatility surface fitting with SVI and SABR, and arbitrage checks.

    Category 40-option-implied-derivatives; memory class ``light``.

    Registers its result under ``surface``, so a later node can consume it as a handle.

    Args:
        strikes: [series_handle, required] Quoted strikes.
        expiries: [series_handle, required] Times to expiry in years.
        implied_vols: [series_handle, required] Quoted implied volatilities.
        forward: [series_handle, required] Forward price per expiry.
        model: [enum, optional] Surface parameterisation. Default ``'svi'``.
        enforce_no_arbitrage: [boolean, optional] Constrain the fit to be arbitrage free. Default
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
        "opt_fit_surface: not implemented."
    )


def opt_surface_evaluate(
    *,
    surface: Any,
    strikes: Sequence[float],
    expiries: Sequence[float],
) -> dict[str, Any]:
    """Node ``opt_surface_evaluate`` -- method card #341.

    Implied-volatility surface fitting with SVI and SABR, and arbitrage checks.

    Category 40-option-implied-derivatives; memory class ``light``.

    Args:
        surface: [raw_handle, required] Handle to a fitted surface.
        strikes: [num_array, required] Strikes to evaluate.
        expiries: [num_array, required] Expiries to evaluate.

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
        "opt_surface_evaluate: not implemented."
    )


def opt_arbitrage_check(
    *,
    surface: Any,
    grid_size: int | None = None,
) -> dict[str, Any]:
    """Node ``opt_arbitrage_check`` -- method card #341.

    Implied-volatility surface fitting with SVI and SABR, and arbitrage checks.

    Category 40-option-implied-derivatives; memory class ``light``.

    Args:
        surface: [raw_handle, required] Handle to a fitted surface.
        grid_size: [integer, optional] Grid density for the check. Default ``100``.

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
        "opt_arbitrage_check: not implemented."
    )
