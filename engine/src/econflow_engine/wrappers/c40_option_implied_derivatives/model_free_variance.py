# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``model_free_variance`` -- method card #343.

#343 Model-free implied variance and variance swaps

Category 40-option-implied-derivatives; module ``model_free_variance``.

Reference implementation: QuantLib.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c40_option_implied_derivatives import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "opt_model_free_variance",
    "opt_variance_risk_premium",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def opt_model_free_variance(
    *,
    strikes: pd.Series,
    prices: pd.Series,
    option_type: pd.Series,
    forward: float,
    time_to_expiry: float,
    rate: float,
) -> dict[str, Any]:
    """Node ``opt_model_free_variance`` -- method card #343.

    Model-free implied variance and variance swaps.

    Category 40-option-implied-derivatives; memory class ``light``.

    Args:
        strikes: [series_handle, required] Strikes.
        prices: [series_handle, required] Option prices.
        option_type: [series_handle, required] Option types.
        forward: [number, required] Forward price.
        time_to_expiry: [number, required] Time to expiry in years.
        rate: [number, required] Risk-free rate.

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
        "opt_model_free_variance: not implemented."
    )


def opt_variance_risk_premium(
    *,
    implied_variance: pd.Series,
    realised_variance: pd.Series,
    horizon: int | None = None,
) -> dict[str, Any]:
    """Node ``opt_variance_risk_premium`` -- method card #343.

    Model-free implied variance and variance swaps.

    Category 40-option-implied-derivatives; memory class ``light``.

    Args:
        implied_variance: [series_handle, required] Model-free implied variance series.
        realised_variance: [series_handle, required] Realised variance series.
        horizon: [integer, optional] Horizon in days the two are aligned over. Default ``21``.

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
        "opt_variance_risk_premium: not implemented."
    )
