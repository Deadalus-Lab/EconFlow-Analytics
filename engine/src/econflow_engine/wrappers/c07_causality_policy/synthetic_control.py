# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``synthetic_control`` -- method card #40.

#40 Synthetic Control (classic, Abadie)

Category 07-causality-policy; module ``synthetic_control``.

Reference implementation: pysyncon.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "sc_fit",
    "sc_prepare_data",
    "sc_tables",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def sc_prepare_data(
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
    """Node ``sc_prepare_data`` -- method card #40.

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
        "sc_prepare_data: not implemented."
    )


def sc_fit(
    *,
    dataprep_object: Any,
    optimxmethod: Literal["Nelder-Mead", "BFGS"] | None = None,
    genoud: bool | None = None,
) -> dict[str, Any]:
    """Node ``sc_fit`` -- method card #40.

    Synthetic Control (classic, Abadie).

    Category 07-causality-policy; memory class ``heavy``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        dataprep_object: [raw_handle, required] Handle to a dataprep object (from sc_prepare_data).
        optimxmethod: [enum, optional] Optimizer for the weights (default Nelder-Mead).
        genoud: [boolean, optional] Genetic optimization (slower/more stable, default False).
            Default ``False``.

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
        "sc_fit: not implemented."
    )


def sc_tables(
    *,
    synth_object: Any,
    dataprep_object: Any,
    round_digit: int | None = None,
) -> dict[str, Any]:
    """Node ``sc_tables`` -- method card #40.

    Synthetic Control (classic, Abadie).

    Category 07-causality-policy; memory class ``light``.

    Args:
        synth_object: [raw_handle, required] Handle to a synth object (from sc_fit).
        dataprep_object: [raw_handle, required] Handle to a dataprep object (from sc_prepare_data).
        round_digit: [integer, optional] Rounding decimals (default 3). Default ``3``.

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
        "sc_tables: not implemented."
    )
