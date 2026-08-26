# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``adam_exponential_smoothing`` -- method card #10.

#10 ADAM and exponential-smoothing state-space variants

Category 02-univariate-forecasting; module ``adam_exponential_smoothing``.

Reference implementation: 10.1201/9781003452652.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
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

# --- gen_wrappers: header end ---


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
    """Node ``run_adam`` -- method card #10.

    ADAM and exponential-smoothing state-space variants.

    Category 02-univariate-forecasting; memory class ``heavy``.

    Args:
        data: [series_handle, required] Handle to a series (1st column = response; data-agnostic
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
        "run_adam: not implemented."
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
    """Node ``run_auto_adam`` -- method card #10.

    ADAM and exponential-smoothing state-space variants.

    Category 02-univariate-forecasting; memory class ``heavy``.

    Args:
        data: [series_handle, required] Handle to a series (auto.adam tries multiple distributions).
        model: [string, optional] ETS spec E/T/S (default 'ZXZ').
        h: [integer, optional] Fit-time horizon (default 0).
        holdout: [boolean, optional] Holdout of the last h (requires h>0; default False).
        ic: [enum, optional] Information criterion (default AICc).
        forecast_h: [integer, optional] Horizon of the forecast step.

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
        "run_auto_adam: not implemented."
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
    """Node ``run_ces`` -- method card #10.

    ADAM and exponential-smoothing state-space variants.

    Category 02-univariate-forecasting; memory class ``heavy``.

    Args:
        y: [series_handle, required] Handle to a series (univariate response).
        seasonality: [enum, optional] Type of complex seasonality (default none).
        loss: [enum, optional] Loss function (default likelihood).
        h: [integer, optional] Fit-time horizon (default 0).
        holdout: [boolean, optional] Holdout of the last h (requires h>0; default False).
        forecast_h: [integer, optional] Horizon of the forecast step.

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
        "run_ces: not implemented."
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
    """Node ``run_auto_ces`` -- method card #10.

    ADAM and exponential-smoothing state-space variants.

    Category 02-univariate-forecasting; memory class ``heavy``.

    Args:
        y: [series_handle, required] Handle to a series (auto.ces tries the seasonality types).
        ic: [enum, optional] Information criterion (default AICc).
        loss: [enum, optional] Loss function (default likelihood).
        h: [integer, optional] Fit-time horizon (default 0).
        holdout: [boolean, optional] Holdout of the last h (requires h>0; default False).
        forecast_h: [integer, optional] Horizon of the forecast step.

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
        "run_auto_ces: not implemented."
    )
