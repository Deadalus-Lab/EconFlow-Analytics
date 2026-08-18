# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``value_risk_expected`` -- METHOD-SELECTION card #65.

#65 Value-at-Risk / Expected Shortfall / downside-risk / component-VaR

Category 12-distribution-risk; module ``value_risk_expected``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c12_distribution_risk import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pa_component_var",
    "pa_downside_risk",
    "pa_expected_shortfall",
    "pa_returns_from_long",
    "pa_var",
    "NODE_META",
    "wire_model",
]


def pa_var(
    *,
    returns: np.ndarray,
    p: float | None = None,
    method: Literal["historical", "gaussian", "modified"] | None = None,
    clean: Literal["none", "boudt", "geltner"] | None = None,
    invert: bool | None = None,
) -> dict[str, Any]:
    """Node ``pa_var`` -- METHOD-SELECTION card #65.

    Value-at-Risk / Expected Shortfall / downside-risk / component-VaR.

    Category 12-distribution-risk; memory class ``light``.

    Args:
        returns: [matrix_handle, required] Handle to a returns series/matrix (one column per asset).
        p: [number, optional] Confidence level in (0,1) (default 0.95). Default ``0.95``.
        method: [enum, optional] Estimator VaR (default historical· modified = Cornish-Fisher).
        clean: [enum, optional] Outlier cleaning (default none).
        invert: [boolean, optional] False (default) -> positive loss magnitude· True -> signed
            return-space quantile. Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pa_var: not implemented. The method card is in ./README.md."
    )


def pa_expected_shortfall(
    *,
    returns: np.ndarray,
    p: float | None = None,
    method: Literal["historical", "gaussian", "modified"] | None = None,
    clean: Literal["none", "boudt", "geltner"] | None = None,
    invert: bool | None = None,
) -> dict[str, Any]:
    """Node ``pa_expected_shortfall`` -- METHOD-SELECTION card #65.

    Value-at-Risk / Expected Shortfall / downside-risk / component-VaR.

    Category 12-distribution-risk; memory class ``light``.

    Args:
        returns: [matrix_handle, required] Handle to a returns series/matrix (one column per asset).
        p: [number, optional] Confidence level in (0,1) (default 0.95). Default ``0.95``.
        method: [enum, optional] Estimator ES/CVaR (default historical· modified = Cornish-Fisher).
        clean: [enum, optional] Outlier cleaning (default none).
        invert: [boolean, optional] False (default) -> positive loss magnitude· True -> signed
            return-space quantile. Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pa_expected_shortfall: not implemented. The method card is in ./README.md."
    )


def pa_downside_risk(
    *,
    returns: np.ndarray,
    MAR: float | None = None,
    p: float | None = None,
) -> dict[str, Any]:
    """Node ``pa_downside_risk`` -- METHOD-SELECTION card #65.

    Value-at-Risk / Expected Shortfall / downside-risk / component-VaR.

    Category 12-distribution-risk; memory class ``light``.

    Args:
        returns: [matrix_handle, required] Handle to a returns series/matrix (one column per asset).
        MAR: [number, optional] Minimum acceptable return for downside/Sortino (default 0). Default
            ``0``.
        p: [number, optional] Confidence level for the historical VaR/ES of the summary (default
            0.95). Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pa_downside_risk: not implemented. The method card is in ./README.md."
    )


def pa_component_var(
    *,
    returns: np.ndarray,
    weights: float,
    p: float | None = None,
    method: Literal["gaussian", "modified"] | None = None,
) -> dict[str, Any]:
    """Node ``pa_component_var`` -- METHOD-SELECTION card #65.

    Value-at-Risk / Expected Shortfall / downside-risk / component-VaR.

    Category 12-distribution-risk; memory class ``light``.

    Args:
        returns: [matrix_handle, required] Handle to a MULTIVARIATE returns matrix (>=2 assets).
        weights: [number, required] Vector of portfolio weights of length the column count of the
            reference, sum ~ 1 (e.g. [0.5,0.5]).
        p: [number, optional] Confidence level in (0,1) (default 0.95). Default ``0.95``.
        method: [enum, optional] Estimator with a CONSISTENT (additive) Euler decomposition (default
            gaussian).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pa_component_var: not implemented. The method card is in ./README.md."
    )


def pa_returns_from_long(
    *,
    data: pd.DataFrame,
    period_col: str | None = None,
    value_col: str | None = None,
) -> dict[str, Any]:
    """Node ``pa_returns_from_long`` -- METHOD-SELECTION card #65.

    Value-at-Risk / Expected Shortfall / downside-risk / component-VaR.

    Category 12-distribution-risk; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a long DataFrame (columns period/value).
        period_col: [string, optional] Date column name (default 'period'). Default ``'period'``.
        value_col: [string, optional] Value column name (default 'value'). Default ``'value'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pa_returns_from_long: not implemented. The method card is in ./README.md."
    )
