# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``synthetic_control_2`` -- METHOD-SELECTION card #42.

#42 Synthetic Control (tidy pipe)

Category 07-causality-policy; module ``synthetic_control_2``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "wrap_generate_control",
    "wrap_generate_predictor",
    "wrap_generate_weights",
    "wrap_grab_loss",
    "wrap_grab_predictor_weights",
    "wrap_grab_significance",
    "wrap_grab_synthetic_control",
    "wrap_grab_unit_weights",
    "wrap_synthetic_control",
    "NODE_META",
    "wire_model",
]


def wrap_synthetic_control(
    *,
    data: pd.DataFrame,
    outcome: str,
    unit: str,
    time: str,
    i_unit: str,
    i_time: float,
    generate_placebos: bool | None = None,
) -> dict[str, Any]:
    """Node ``wrap_synthetic_control`` -- METHOD-SELECTION card #42.

    Synthetic Control (tidy pipe).

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
        "wrap_synthetic_control: not implemented. The method card is in ./README.md."
    )


def wrap_generate_predictor(
    *,
    data: Any,
    time_window: Any,
    predictors: Any,
) -> dict[str, Any]:
    """Node ``wrap_generate_predictor`` -- METHOD-SELECTION card #42.

    Synthetic Control (tidy pipe).

    Category 07-causality-policy; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        data: [raw_handle, required] Handle to a tidysynth pipeline object (from
            wrap_synthetic_control).
        time_window: [raw_handle, required] Handle to a vector of time values used to compute the
            predictors.
        predictors: [raw_handle, required] Handle to a named list, e.g. list(mean_x1 =
            list(column='x1', stat='mean')).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_generate_predictor: not implemented. The method card is in ./README.md."
    )


def wrap_generate_weights(
    *,
    data: Any,
    optimization_window: Any,
    optimization_method: Literal["Nelder-Mead", "BFGS"] | None = None,
    genoud: bool | None = None,
    quadopt: Literal["ipop", "LowRankQP"] | None = None,
    include_fit: bool | None = None,
) -> dict[str, Any]:
    """Node ``wrap_generate_weights`` -- METHOD-SELECTION card #42.

    Synthetic Control (tidy pipe).

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
        "wrap_generate_weights: not implemented. The method card is in ./README.md."
    )


def wrap_generate_control(
    *,
    data: Any,
) -> dict[str, Any]:
    """Node ``wrap_generate_control`` -- METHOD-SELECTION card #42.

    Synthetic Control (tidy pipe).

    Category 07-causality-policy; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        data: [raw_handle, required] Handle to a tidysynth pipeline (after generate_weights).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_generate_control: not implemented. The method card is in ./README.md."
    )


def wrap_grab_synthetic_control(
    *,
    data: Any,
    placebo: bool | None = None,
) -> dict[str, Any]:
    """Node ``wrap_grab_synthetic_control`` -- METHOD-SELECTION card #42.

    Synthetic Control (tidy pipe).

    Category 07-causality-policy; memory class ``light``.

    Args:
        data: [raw_handle, required] Handle to a completed tidysynth pipeline (after
            generate_control).
        placebo: [boolean, optional] Return placebo units (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_grab_synthetic_control: not implemented. The method card is in ./README.md."
    )


def wrap_grab_unit_weights(
    *,
    data: Any,
    placebo: bool | None = None,
) -> dict[str, Any]:
    """Node ``wrap_grab_unit_weights`` -- METHOD-SELECTION card #42.

    Synthetic Control (tidy pipe).

    Category 07-causality-policy; memory class ``light``.

    Args:
        data: [raw_handle, required] Handle to a tidysynth pipeline (after generate_weights).
        placebo: [boolean, optional] Placebo units (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_grab_unit_weights: not implemented. The method card is in ./README.md."
    )


def wrap_grab_predictor_weights(
    *,
    data: Any,
    placebo: bool | None = None,
) -> dict[str, Any]:
    """Node ``wrap_grab_predictor_weights`` -- METHOD-SELECTION card #42.

    Synthetic Control (tidy pipe).

    Category 07-causality-policy; memory class ``light``.

    Args:
        data: [raw_handle, required] Handle to a tidysynth pipeline (after generate_weights).
        placebo: [boolean, optional] Placebo units (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_grab_predictor_weights: not implemented. The method card is in ./README.md."
    )


def wrap_grab_significance(
    *,
    data: Any,
    time_window: Any | None = None,
) -> dict[str, Any]:
    """Node ``wrap_grab_significance`` -- METHOD-SELECTION card #42.

    Synthetic Control (tidy pipe).

    Category 07-causality-policy; memory class ``light``.

    Args:
        data: [raw_handle, required] Handle to a tidysynth pipeline with placebos.
        time_window: [raw_handle, optional] Handle to a vector of post-period values for the
            inference (default: post-period).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_grab_significance: not implemented. The method card is in ./README.md."
    )


def wrap_grab_loss(
    *,
    data: Any,
) -> dict[str, Any]:
    """Node ``wrap_grab_loss`` -- METHOD-SELECTION card #42.

    Synthetic Control (tidy pipe).

    Category 07-causality-policy; memory class ``light``.

    Args:
        data: [raw_handle, required] Handle to a completed tidysynth pipeline.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_grab_loss: not implemented. The method card is in ./README.md."
    )
