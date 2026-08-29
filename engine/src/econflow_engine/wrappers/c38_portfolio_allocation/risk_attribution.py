# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``risk_attribution`` -- method card #332.

#332 Risk contribution and factor risk attribution

Category 38-portfolio-allocation; module ``risk_attribution``.

Reference implementation: riskfolio-lib.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c38_portfolio_allocation import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pf_factor_attribution",
    "pf_risk_attribution",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pf_risk_attribution(
    *,
    weights: pd.Series,
    returns: pd.DataFrame,
    risk_measure: Literal["volatility", "cvar", "var", "mad"] | None = None,
    confidence: float | None = None,
) -> dict[str, Any]:
    """Node ``pf_risk_attribution`` -- method card #332.

    Risk contribution and factor risk attribution.

    Category 38-portfolio-allocation; memory class ``light``.

    Args:
        weights: [series_handle, required] Portfolio weights.
        returns: [df_handle, required] Asset return panel.
        risk_measure: [enum, optional] Risk measure to decompose. Default ``'volatility'``.
        confidence: [number, optional] Tail level where the measure needs one. Default ``0.95``.

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
        "pf_risk_attribution: not implemented."
    )


def pf_factor_attribution(
    *,
    weights: pd.Series,
    returns: pd.DataFrame,
    factors: pd.DataFrame,
) -> dict[str, Any]:
    """Node ``pf_factor_attribution`` -- method card #332.

    Risk contribution and factor risk attribution.

    Category 38-portfolio-allocation; memory class ``light``.

    Args:
        weights: [series_handle, required] Portfolio weights.
        returns: [df_handle, required] Asset return panel.
        factors: [multiseries_handle, required] Factor return series.

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
        "pf_factor_attribution: not implemented."
    )
