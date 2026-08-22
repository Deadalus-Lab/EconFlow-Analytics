# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``synthetic_control_pipeline`` -- method card #42.

#42 Synthetic Control (long-format pipe)

Category 07-causality-policy; module ``synthetic_control_pipeline``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "synth_add_control",
    "synth_add_predictor",
    "synth_add_weights",
    "synth_init",
    "synth_loss",
    "synth_predictor_weights",
    "synth_result",
    "synth_significance",
    "synth_unit_weights",
    "NODE_META",
    "wire_model",
]


def synth_init(
    *,
    data: pd.DataFrame,
    outcome: str,
    unit: str,
    time: str,
    i_unit: str,
    i_time: float,
    generate_placebos: bool | None = None,
) -> dict[str, Any]:
    """Node ``synth_init`` -- method card #42.

    Synthetic Control (long-format pipe).

    Category 07-causality-policy; memory class ``heavy``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Handle to a long-format panel DataFrame.
        outcome: [string, required] Outcome column name.
        unit: [string, required] Unit id column name.
        time: [string, required] Time column name.
        i_unit: [string, required] ID of the treated unit.
        i_time: [number, required] Treatment start time.
        generate_placebos: [boolean, optional] Generate placebo units for inference (default False).
            Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "synth_init: not implemented."
    )


def synth_add_predictor(
    *,
    data: Any,
    time_window: Any,
    predictors: Any,
) -> dict[str, Any]:
    """Node ``synth_add_predictor`` -- method card #42.

    Synthetic Control (long-format pipe).

    Category 07-causality-policy; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        data: [raw_handle, required] Handle to a tidysynth pipeline object (from synth_init).
        time_window: [raw_handle, required] Handle to a vector of time values used to compute the
            predictors.
        predictors: [raw_handle, required] Handle to a named list, e.g. list(mean_x1 =
            list(column='x1', stat='mean')).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "synth_add_predictor: not implemented."
    )


def synth_add_weights(
    *,
    data: Any,
    optimization_window: Any,
    optimization_method: Literal["Nelder-Mead", "BFGS"] | None = None,
    genoud: bool | None = None,
    quadopt: Literal["ipop", "LowRankQP"] | None = None,
    include_fit: bool | None = None,
) -> dict[str, Any]:
    """Node ``synth_add_weights`` -- method card #42.

    Synthetic Control (long-format pipe).

    Category 07-causality-policy; memory class ``heavy``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        data: [raw_handle, required] Handle to a tidysynth pipeline (after generate_predictor).
        optimization_window: [raw_handle, required] Handle to a vector of pre-treatment periods for
            the optimization.
        optimization_method: [enum, optional] Optimizer (default Nelder-Mead).
        genoud: [boolean, optional] Genetic optimization (default False). Default ``False``.
        quadopt: [enum, optional] Quadratic optimizer (default ipop).
        include_fit: [boolean, optional] Return the fit object (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "synth_add_weights: not implemented."
    )


def synth_add_control(
    *,
    data: Any,
) -> dict[str, Any]:
    """Node ``synth_add_control`` -- method card #42.

    Synthetic Control (long-format pipe).

    Category 07-causality-policy; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        data: [raw_handle, required] Handle to a tidysynth pipeline (after generate_weights).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "synth_add_control: not implemented."
    )


def synth_result(
    *,
    data: Any,
    placebo: bool | None = None,
) -> dict[str, Any]:
    """Node ``synth_result`` -- method card #42.

    Synthetic Control (long-format pipe).

    Category 07-causality-policy; memory class ``light``.

    Args:
        data: [raw_handle, required] Handle to a completed tidysynth pipeline (after
            generate_control).
        placebo: [boolean, optional] Return placebo units (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "synth_result: not implemented."
    )


def synth_unit_weights(
    *,
    data: Any,
    placebo: bool | None = None,
) -> dict[str, Any]:
    """Node ``synth_unit_weights`` -- method card #42.

    Synthetic Control (long-format pipe).

    Category 07-causality-policy; memory class ``light``.

    Args:
        data: [raw_handle, required] Handle to a tidysynth pipeline (after generate_weights).
        placebo: [boolean, optional] Placebo units (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "synth_unit_weights: not implemented."
    )


def synth_predictor_weights(
    *,
    data: Any,
    placebo: bool | None = None,
) -> dict[str, Any]:
    """Node ``synth_predictor_weights`` -- method card #42.

    Synthetic Control (long-format pipe).

    Category 07-causality-policy; memory class ``light``.

    Args:
        data: [raw_handle, required] Handle to a tidysynth pipeline (after generate_weights).
        placebo: [boolean, optional] Placebo units (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "synth_predictor_weights: not implemented."
    )


def synth_significance(
    *,
    data: Any,
    time_window: Any | None = None,
) -> dict[str, Any]:
    """Node ``synth_significance`` -- method card #42.

    Synthetic Control (long-format pipe).

    Category 07-causality-policy; memory class ``light``.

    Args:
        data: [raw_handle, required] Handle to a tidysynth pipeline with placebos.
        time_window: [raw_handle, optional] Handle to a vector of post-period values for the
            inference (default: post-period).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "synth_significance: not implemented."
    )


def synth_loss(
    *,
    data: Any,
) -> dict[str, Any]:
    """Node ``synth_loss`` -- method card #42.

    Synthetic Control (long-format pipe).

    Category 07-causality-policy; memory class ``light``.

    Args:
        data: [raw_handle, required] Handle to a completed tidysynth pipeline.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "synth_loss: not implemented."
    )
