# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``markov_switching`` -- METHOD-SELECTION card #30.

#30 Markov switching (gaussian/lm)

Category 06-volatility-regimes; module ``markov_switching``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c06_volatility_regimes import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "msw_fit",
    "msw_intervals",
    "msw_residuals",
    "NODE_META",
    "wire_model",
]


def msw_fit(
    *,
    formula: str,
    data: pd.DataFrame,
    k: int | None = None,
    p: int | None = None,
) -> dict[str, Any]:
    """Node ``msw_fit`` -- METHOD-SELECTION card #30.

    Markov switching (gaussian/lm).

    Category 06-volatility-regimes; memory class ``heavy``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] Linear model formula, e.g. 'y ~ 1' or 'y ~ x1 + x2'.
        data: [df_handle, required] Handle to a DataFrame holding the formula variables.
        k: [integer, optional] Number of regimes (>=2, default 2). Default ``2``.
        p: [integer, optional] AR order of the residuals per regime (default 0). Default ``0``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "msw_fit: not implemented. The method card is in ./README.md."
    )


def msw_intervals(
    *,
    fit: Any,
    level: float | None = None,
) -> dict[str, Any]:
    """Node ``msw_intervals`` -- METHOD-SELECTION card #30.

    Markov switching (gaussian/lm).

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to an 'MSM' model (from msw_fit).
        level: [number, optional] Confidence level in (0,1) (default 0.95). Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "msw_intervals: not implemented. The method card is in ./README.md."
    )


def msw_residuals(
    *,
    fit: Any,
    regime: int | None = None,
) -> dict[str, Any]:
    """Node ``msw_residuals`` -- METHOD-SELECTION card #30.

    Markov switching (gaussian/lm).

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to an 'MSM' model (from msw_fit).
        regime: [integer, optional] Regime 1..k for conditional residuals (default: all).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "msw_residuals: not implemented. The method card is in ./README.md."
    )
