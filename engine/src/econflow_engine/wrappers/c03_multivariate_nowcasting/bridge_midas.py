# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bridge_midas`` -- method card #420.

#420 Bridge equations and unrestricted MIDAS

Category 03-multivariate-nowcasting; module ``bridge_midas``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c03_multivariate_nowcasting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mn_bridge_equation",
    "mn_umidas",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def mn_bridge_equation(
    *,
    target: pd.Series,
    indicator: pd.Series,
    aggregation: Literal["mean", "sum", "last", "first"] | None = None,
    fill: Literal["none", "arima", "mean", "last_value"] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``mn_bridge_equation`` -- method card #420.

    Bridge equations and unrestricted MIDAS.

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        target: [series_handle, required] Low-frequency target.
        indicator: [series_handle, required] High-frequency indicator.
        aggregation: [enum, optional] How the indicator is aggregated. Default ``'mean'``.
        fill: [enum, optional] Ragged-edge handling. Default ``'arima'``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

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
        "mn_bridge_equation: not implemented."
    )


def mn_umidas(
    *,
    target: pd.Series,
    indicator: pd.Series,
    n_lags: int | None = None,
    frequency_ratio: int,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``mn_umidas`` -- method card #420.

    Bridge equations and unrestricted MIDAS.

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        target: [series_handle, required] Low-frequency target.
        indicator: [series_handle, required] High-frequency indicator.
        n_lags: [integer, optional] High-frequency lags included. Default ``6``.
        frequency_ratio: [integer, required] High- to low-frequency ratio.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

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
        "mn_umidas: not implemented."
    )
