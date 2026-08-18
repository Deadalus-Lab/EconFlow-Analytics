# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``synthetic_control`` -- METHOD-SELECTION card #40.

#40 Synthetic Control (classic, Abadie)

Category 07-causality-policy; module ``synthetic_control``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "wrap_dataprep",
    "wrap_synth",
    "wrap_synth_tab",
    "NODE_META",
    "wire_model",
]


def wrap_dataprep(
    *,
    foo: pd.DataFrame,
    predictors: Sequence[str] | None = None,
    predictors_op: str | None = None,
    dependent: str | None = None,
    unit_variable: str | None = None,
    time_variable: str | None = None,
    treatment_identifier: float | None = None,
    controls_identifier: Any | None = None,
    time_predictors_prior: Any | None = None,
    time_optimize_ssr: Any | None = None,
    time_plot: Any | None = None,
) -> dict[str, Any]:
    """Node ``wrap_dataprep`` -- METHOD-SELECTION card #40.

    Synthetic Control (classic, Abadie).

    Category 07-causality-policy; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        foo: [df_handle, required] Handle to a long-format panel DataFrame.
        predictors: [series_codes, optional] Predictor column names (array of strings).
        predictors_op: [string, optional] Aggregation function for the predictors (default 'mean').
            Default ``'mean'``.
        dependent: [string, optional] Outcome column name.
        unit_variable: [string, optional] Unit id column name.
        time_variable: [string, optional] Time column name.
        treatment_identifier: [number, optional] ID of the treated unit (single scalar; required in
            practice).
        controls_identifier: [raw_handle, optional] Handle to a vector of control-unit IDs (>=2).
        time_predictors_prior: [raw_handle, optional] Handle to a vector of pre-treatment periods
            for the predictors.
        time_optimize_ssr: [raw_handle, optional] Handle to a vector of periods for the SSR
            optimization.
        time_plot: [raw_handle, optional] Handle to a vector of all periods to be plotted.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_dataprep: not implemented. The method card is in ./README.md."
    )


def wrap_synth(
    *,
    dataprep_object: Any,
    optimxmethod: Literal["Nelder-Mead", "BFGS"] | None = None,
    genoud: bool | None = None,
) -> dict[str, Any]:
    """Node ``wrap_synth`` -- METHOD-SELECTION card #40.

    Synthetic Control (classic, Abadie).

    Category 07-causality-policy; memory class ``heavy``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        dataprep_object: [raw_handle, required] Handle to a dataprep object (from wrap_dataprep).
        optimxmethod: [enum, optional] Optimizer for the weights (default Nelder-Mead).
        genoud: [boolean, optional] Genetic optimization (slower/more stable, default False).
            Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_synth: not implemented. The method card is in ./README.md."
    )


def wrap_synth_tab(
    *,
    synth_object: Any,
    dataprep_object: Any,
    round_digit: int | None = None,
) -> dict[str, Any]:
    """Node ``wrap_synth_tab`` -- METHOD-SELECTION card #40.

    Synthetic Control (classic, Abadie).

    Category 07-causality-policy; memory class ``light``.

    Args:
        synth_object: [raw_handle, required] Handle to a synth object (from wrap_synth).
        dataprep_object: [raw_handle, required] Handle to a dataprep object (from wrap_dataprep).
        round_digit: [integer, optional] Rounding decimals (default 3). Default ``3``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_synth_tab: not implemented. The method card is in ./README.md."
    )
