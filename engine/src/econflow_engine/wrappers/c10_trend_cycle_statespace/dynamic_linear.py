# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``dynamic_linear`` -- method card #59.

#59 Dynamic linear models (state space)

Category 10-trend-cycle-statespace; module ``dynamic_linear``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c10_trend_cycle_statespace import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "dl_forecast",
    "dl_local_level",
    "dl_local_linear_trend",
    "dl_trend_cycle",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def dl_local_level(
    *,
    y: pd.Series,
    seasonal: bool | None = None,
    seasonal_period: int | None = None,
) -> dict[str, Any]:
    """Node ``dl_local_level`` -- method card #59.

    Dynamic linear models (state space).

    Category 10-trend-cycle-statespace; memory class ``light``.

    Registers its result under ``filtered_obj``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Handle to a univariate ts· local level (dlmModPoly order=1).
        seasonal: [boolean, optional] Add a dummy seasonal term. Default ``False``.
        seasonal_period: [integer, optional] Seasonal period (>=2, <=n)· default frequency(y).

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
        "dl_local_level: not implemented."
    )


def dl_local_linear_trend(
    *,
    y: pd.Series,
    seasonal: bool | None = None,
    seasonal_period: int | None = None,
) -> dict[str, Any]:
    """Node ``dl_local_linear_trend`` -- method card #59.

    Dynamic linear models (state space).

    Category 10-trend-cycle-statespace; memory class ``light``.

    Registers its result under ``filtered_obj``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Handle to a univariate ts· local linear trend (dlmModPoly
            order=2).
        seasonal: [boolean, optional] Add a dummy seasonal term. Default ``False``.
        seasonal_period: [integer, optional] Seasonal period (>=2, <=n)· default frequency(y).

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
        "dl_local_linear_trend: not implemented."
    )


def dl_trend_cycle(
    *,
    y: pd.Series,
    cycle_period: float | None = None,
    seasonal: bool | None = None,
    seasonal_period: int | None = None,
) -> dict[str, Any]:
    """Node ``dl_trend_cycle`` -- method card #59.

    Dynamic linear models (state space).

    Category 10-trend-cycle-statespace; memory class ``light``.

    Registers its result under ``filtered_obj``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Handle to a univariate ts· trend + rotation-form stochastic
            cycle (output gap).
        cycle_period: [number, optional] Cycle length in periods (> 2)· default 8*frequency.
        seasonal: [boolean, optional] Add a dummy seasonal term. Default ``False``.
        seasonal_period: [integer, optional] Seasonal period (>=2, <=n)· default frequency(y).

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
        "dl_trend_cycle: not implemented."
    )


def dl_forecast(
    *,
    object: Any,
    n_ahead: int | None = None,
    level: float | None = None,
) -> dict[str, Any]:
    """Node ``dl_forecast`` -- method card #59.

    Dynamic linear models (state space).

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a dlmFiltered (the filtered_obj from
            dl_local_level/.../dl_trend_cycle).
        n_ahead: [integer, optional] Forecast horizon (positive integer). Default ``8``.
        level: [number, optional] Confidence level ∈ (0,1). Default ``0.95``.

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
        "dl_forecast: not implemented."
    )
