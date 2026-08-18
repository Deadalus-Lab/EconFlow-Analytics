# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``smooth`` -- METHOD-SELECTION card #10.

#10 smooth (ADAM / ES variants)

Category 02-univariate-forecasting; module ``smooth``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c02_univariate_forecasting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "run_adam",
    "run_auto_adam",
    "run_auto_ces",
    "run_ces",
    "NODE_META",
    "wire_model",
]


def run_adam(
    *,
    data: pd.Series,
    model: str | None = None,
    h: int | None = None,
    holdout: bool | None = None,
    loss: (
        Literal[
            "likelihood",
            "MSE",
            "MAE",
            "HAM",
            "LASSO",
            "RIDGE",
            "MSEh",
            "TMSE",
            "GTMSE",
            "MSCE",
            "GPL",
        ]
        | None
    ) = None,
    ic: Literal["AICc", "AIC", "BIC", "BICc"] | None = None,
    forecast_h: int | None = None,
) -> dict[str, Any]:
    """Node ``run_adam`` -- METHOD-SELECTION card #10.

    smooth (ADAM / ES variants).

    Category 02-univariate-forecasting; memory class ``heavy``.

    Args:
        data: [series_handle, required] Handle to a ts (1st column = response; data-agnostic
            passthrough).
        model: [string, optional] ETS spec E/T/S (default 'ZXZ'; Z=auto, X=pure additive selection).
        h: [integer, optional] Fit-time horizon (for holdout; default 0).
        holdout: [boolean, optional] Keep the last h points as holdout (requires h>0; default
            False).
        loss: [enum, optional] Loss function (default likelihood).
        ic: [enum, optional] Information criterion (default AICc).
        forecast_h: [integer, optional] Horizon of the forecast step (None -> fit h if >0, otherwise
            10).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "run_adam: not implemented. The method card is in ./README.md."
    )


def run_auto_adam(
    *,
    data: pd.Series,
    model: str | None = None,
    h: int | None = None,
    holdout: bool | None = None,
    ic: Literal["AICc", "AIC", "BIC", "BICc"] | None = None,
    forecast_h: int | None = None,
) -> dict[str, Any]:
    """Node ``run_auto_adam`` -- METHOD-SELECTION card #10.

    smooth (ADAM / ES variants).

    Category 02-univariate-forecasting; memory class ``heavy``.

    Args:
        data: [series_handle, required] Handle to a ts (auto.adam tries multiple distributions).
        model: [string, optional] ETS spec E/T/S (default 'ZXZ').
        h: [integer, optional] Fit-time horizon (default 0).
        holdout: [boolean, optional] Holdout of the last h (requires h>0; default False).
        ic: [enum, optional] Information criterion (default AICc).
        forecast_h: [integer, optional] Horizon of the forecast step.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "run_auto_adam: not implemented. The method card is in ./README.md."
    )


def run_ces(
    *,
    y: pd.Series,
    seasonality: Literal["none", "simple", "partial", "full"] | None = None,
    loss: (
        Literal[
            "likelihood",
            "MSE",
            "MAE",
            "HAM",
            "MSEh",
            "TMSE",
            "GTMSE",
            "MSCE",
            "GPL",
        ]
        | None
    ) = None,
    h: int | None = None,
    holdout: bool | None = None,
    forecast_h: int | None = None,
) -> dict[str, Any]:
    """Node ``run_ces`` -- METHOD-SELECTION card #10.

    smooth (ADAM / ES variants).

    Category 02-univariate-forecasting; memory class ``heavy``.

    Args:
        y: [series_handle, required] Handle to a ts (univariate response).
        seasonality: [enum, optional] Type of complex seasonality (default none).
        loss: [enum, optional] Loss function (default likelihood).
        h: [integer, optional] Fit-time horizon (default 0).
        holdout: [boolean, optional] Holdout of the last h (requires h>0; default False).
        forecast_h: [integer, optional] Horizon of the forecast step.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "run_ces: not implemented. The method card is in ./README.md."
    )


def run_auto_ces(
    *,
    y: pd.Series,
    ic: Literal["AICc", "AIC", "BIC", "BICc"] | None = None,
    loss: (
        Literal[
            "likelihood",
            "MSE",
            "MAE",
            "HAM",
            "MSEh",
            "TMSE",
            "GTMSE",
            "MSCE",
            "GPL",
        ]
        | None
    ) = None,
    h: int | None = None,
    holdout: bool | None = None,
    forecast_h: int | None = None,
) -> dict[str, Any]:
    """Node ``run_auto_ces`` -- METHOD-SELECTION card #10.

    smooth (ADAM / ES variants).

    Category 02-univariate-forecasting; memory class ``heavy``.

    Args:
        y: [series_handle, required] Handle to a ts (auto.ces tries the seasonality types).
        ic: [enum, optional] Information criterion (default AICc).
        loss: [enum, optional] Loss function (default likelihood).
        h: [integer, optional] Fit-time horizon (default 0).
        holdout: [boolean, optional] Holdout of the last h (requires h>0; default False).
        forecast_h: [integer, optional] Horizon of the forecast step.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "run_auto_ces: not implemented. The method card is in ./README.md."
    )
