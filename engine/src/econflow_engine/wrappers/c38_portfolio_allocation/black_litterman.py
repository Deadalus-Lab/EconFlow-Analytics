# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``black_litterman`` -- method card #326.

#326 Black-Litterman with investor views

Category 38-portfolio-allocation; module ``black_litterman``.

Reference implementation: PyPortfolioOpt.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

import numpy as np
import pandas as pd

from econflow_engine.generated.args.c38_portfolio_allocation import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pf_black_litterman",
    "pf_implied_returns",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pf_black_litterman(
    *,
    returns: pd.DataFrame,
    market_weights: pd.Series,
    views: np.ndarray,
    view_returns: Sequence[float],
    view_confidence: Sequence[float] | None = None,
    tau: float | None = None,
    risk_aversion: float | None = None,
) -> dict[str, Any]:
    """Node ``pf_black_litterman`` -- method card #326.

    Black-Litterman with investor views.

    Category 38-portfolio-allocation; memory class ``light``.

    Args:
        returns: [df_handle, required] Asset return panel.
        market_weights: [series_handle, required] Market-capitalisation weights for the prior.
        views: [matrix_handle, required] View picking matrix P.
        view_returns: [num_array, required] View return vector Q.
        view_confidence: [num_array, optional] Confidence per view; omitted = proportional to prior
            variance.
        tau: [number, optional] Scaling of the prior covariance. Default ``0.05``.
        risk_aversion: [number, optional] Risk-aversion coefficient. Default ``2.5``.

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
        "pf_black_litterman: not implemented."
    )


def pf_implied_returns(
    *,
    covariance: np.ndarray,
    market_weights: pd.Series,
    risk_aversion: float | None = None,
) -> dict[str, Any]:
    """Node ``pf_implied_returns`` -- method card #326.

    Black-Litterman with investor views.

    Category 38-portfolio-allocation; memory class ``light``.

    Args:
        covariance: [matrix_handle, required] Asset covariance matrix.
        market_weights: [series_handle, required] Market-capitalisation weights.
        risk_aversion: [number, optional] Risk-aversion coefficient. Default ``2.5``.

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
        "pf_implied_returns: not implemented."
    )
