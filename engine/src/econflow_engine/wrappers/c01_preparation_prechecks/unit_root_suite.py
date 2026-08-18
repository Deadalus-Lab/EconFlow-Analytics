# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``unit_root_suite`` -- METHOD-SELECTION card #2.

#2 Unit-root suite (ADF/KPSS/PP/ERS-DFGLS/Zivot-Andrews)

Category 01-preparation-prechecks; module ``unit_root_suite``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "wrap_ur_df",
    "wrap_ur_ers",
    "wrap_ur_kpss",
    "wrap_ur_pp",
    "wrap_ur_za",
    "NODE_META",
    "wire_model",
]


def wrap_ur_df(
    *,
    y: pd.Series,
    type: Literal["none", "drift", "trend"] | None = None,
    lags: int | None = None,
    selectlags: Literal["Fixed", "AIC", "BIC"] | None = None,
) -> dict[str, Any]:
    """Node ``wrap_ur_df`` -- METHOD-SELECTION card #2.

    Unit-root suite (ADF/KPSS/PP/ERS-DFGLS/Zivot-Andrews).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        y: [series_handle, required] Handle to a univariate series (no NA).
        type: [enum, optional] Deterministic terms of the ADF regression (default none).
        lags: [integer, optional] Number of lags of the differences (default 1). Default ``1``.
        selectlags: [enum, optional] Lag selection: Fixed/AIC/BIC (default Fixed).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_ur_df: not implemented. The method card is in ./README.md."
    )


def wrap_ur_kpss(
    *,
    y: pd.Series,
    type: Literal["mu", "tau"] | None = None,
    lags: Literal["short", "long", "nil"] | None = None,
) -> dict[str, Any]:
    """Node ``wrap_ur_kpss`` -- METHOD-SELECTION card #2.

    Unit-root suite (ADF/KPSS/PP/ERS-DFGLS/Zivot-Andrews).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        y: [series_handle, required] Handle to a univariate series (no NA).
        type: [enum, optional] mu=stationarity around a constant, tau=around a trend.
        lags: [enum, optional] Truncation lag for the long-run variance (default short).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_ur_kpss: not implemented. The method card is in ./README.md."
    )


def wrap_ur_pp(
    *,
    x: pd.Series,
    type: Literal["Z-alpha", "Z-tau"] | None = None,
    model: Literal["constant", "trend"] | None = None,
    lags: Literal["short", "long"] | None = None,
) -> dict[str, Any]:
    """Node ``wrap_ur_pp`` -- METHOD-SELECTION card #2.

    Unit-root suite (ADF/KPSS/PP/ERS-DFGLS/Zivot-Andrews).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate series (no NA).
        type: [enum, optional] Phillips-Perron statistic (default Z-alpha).
        model: [enum, optional] Deterministic part: constant or trend (default constant).
        lags: [enum, optional] Truncation lag (default short).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_ur_pp: not implemented. The method card is in ./README.md."
    )


def wrap_ur_ers(
    *,
    y: pd.Series,
    type: Literal["DF-GLS", "P-test"] | None = None,
    model: Literal["constant", "trend"] | None = None,
    lag_max: int | None = None,
) -> dict[str, Any]:
    """Node ``wrap_ur_ers`` -- METHOD-SELECTION card #2.

    Unit-root suite (ADF/KPSS/PP/ERS-DFGLS/Zivot-Andrews).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        y: [series_handle, required] Handle to a univariate series (no NA).
        type: [enum, optional] Elliott-Rothenberg-Stock variant (default DF-GLS).
        model: [enum, optional] Deterministic part (default constant).
        lag_max: [integer, optional] Maximum lag order (default 4). Default ``4``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_ur_ers: not implemented. The method card is in ./README.md."
    )


def wrap_ur_za(
    *,
    y: pd.Series,
    model: Literal["intercept", "trend", "both"] | None = None,
    lag: int | None = None,
) -> dict[str, Any]:
    """Node ``wrap_ur_za`` -- METHOD-SELECTION card #2.

    Unit-root suite (ADF/KPSS/PP/ERS-DFGLS/Zivot-Andrews).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        y: [series_handle, required] Handle to a univariate series (no NA).
        model: [enum, optional] Zivot-Andrews break in intercept/trend/both (default intercept).
        lag: [integer, optional] Lag order (default None -> selected internally).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_ur_za: not implemented. The method card is in ./README.md."
    )
