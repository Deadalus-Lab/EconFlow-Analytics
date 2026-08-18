# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``quantile_regression`` -- METHOD-SELECTION card #64.

#64 Quantile regression (+ Growth-at-Risk, ABG)

Category 12-distribution-risk; module ``quantile_regression``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c12_distribution_risk import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "qr_conditional_quantiles",
    "qr_growth_at_risk",
    "qr_regression",
    "qr_slope_equality",
    "NODE_META",
    "wire_model",
]


def qr_regression(
    *,
    formula: str,
    data: pd.DataFrame,
    tau: float | None = None,
    method: Literal["br", "fn", "pfn"] | None = None,
    se: Literal["nid", "iid", "ker", "boot"] | None = None,
    boot_replications: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``qr_regression`` -- METHOD-SELECTION card #64.

    Quantile regression (+ Growth-at-Risk, ABG).

    Category 12-distribution-risk; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] Quantile-regression formula, e.g. 'growth ~ fci + slack'.
        data: [df_handle, required] Handle to a DataFrame (data-agnostic· no column renaming).
        tau: [number, optional] Vector of quantile levels in the open (0,1)· passed WHOLE (e.g.
            [0.05,0.25,0.5,0.75,0.95]).
        method: [enum, optional] rq solver (default br).
        se: [enum, optional] Inference for std errors (default nid).
        boot_replications: [integer, optional] Bootstrap replications when se='boot' (default 200).
            Default ``200``.
        seed: [integer, optional] Reproducibility seed for se='boot' (default 42). Default ``42``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "qr_regression: not implemented. The method card is in ./README.md."
    )


def qr_conditional_quantiles(
    *,
    object: Any,
    newdata: pd.DataFrame | None = None,
) -> dict[str, Any]:
    """Node ``qr_conditional_quantiles`` -- METHOD-SELECTION card #64.

    Quantile regression (+ Growth-at-Risk, ABG).

    Category 12-distribution-risk; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to an rq/rqs fit (from qr_regression /
            qr_growth_at_risk).
        newdata: [df_handle, optional] Optional handle to a DataFrame for prediction (default:
            training frame).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "qr_conditional_quantiles: not implemented. The method card is in ./README.md."
    )


def qr_slope_equality(
    *,
    object: Any,
) -> dict[str, Any]:
    """Node ``qr_slope_equality`` -- METHOD-SELECTION card #64.

    Quantile regression (+ Growth-at-Risk, ABG).

    Category 12-distribution-risk; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to an rqs fit with >=2 tau (anova.rq: equality of
            slopes across quantiles).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "qr_slope_equality: not implemented. The method card is in ./README.md."
    )


def qr_growth_at_risk(
    *,
    formula: str,
    data: pd.DataFrame,
    newdata: pd.DataFrame | None = None,
    tau: float | None = None,
    risk_tau: float | None = None,
    h: int | None = None,
    method: Literal["br", "fn", "pfn"] | None = None,
    se: Literal["nid", "iid", "ker", "boot"] | None = None,
    boot_replications: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``qr_growth_at_risk`` -- METHOD-SELECTION card #64.

    Quantile regression (+ Growth-at-Risk, ABG).

    Category 12-distribution-risk; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] GaR formula outcome ~ conditions, e.g. 'growth ~ fci'.
        data: [df_handle, required] Handle to a DataFrame (time-sorted for h-lead alignment).
        newdata: [df_handle, optional] Optional forecast point (default: the last conditions x_T).
        tau: [number, optional] Vector of quantile levels in (0,1)· passed WHOLE (must contain
            risk_tau).
        risk_tau: [number, optional] Downside quantile = Growth-at-Risk (one of the tau· default
            0.05). Default ``0.05``.
        h: [integer, optional] Horizon of h steps· y_{t+h} ~ x_t (default 0 = contemporaneous).
            Default ``0``.
        method: [enum, optional] rq solver (default br).
        se: [enum, optional] Inference for std errors (default nid).
        boot_replications: [integer, optional] Bootstrap replications when se='boot' (default 200).
            Default ``200``.
        seed: [integer, optional] Reproducibility seed (default 42). Default ``42``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "qr_growth_at_risk: not implemented. The method card is in ./README.md."
    )
