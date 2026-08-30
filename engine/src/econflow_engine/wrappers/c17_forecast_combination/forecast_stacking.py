# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``forecast_stacking`` -- method card #533.

#533 Stacked generalisation of forecasters

Category 17-forecast-combination; module ``forecast_stacking``.

Reference implementation: sktime.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c17_forecast_combination import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "fc_stacking",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def fc_stacking(
    *,
    actual: pd.Series,
    forecasts: pd.DataFrame,
    meta_learner: Literal["linear", "ridge", "constrained_ls", "gradient_boosting"] | None = None,
    n_folds: int | None = None,
) -> dict[str, Any]:
    """Node ``fc_stacking`` -- method card #533.

    Stacked generalisation of forecasters.

    Category 17-forecast-combination; memory class ``light``.

    Args:
        actual: [series_handle, required] Realised values.
        forecasts: [df_handle, required] Forecasts, one column per component.
        meta_learner: [enum, optional] Meta-learner. Default ``'constrained_ls'``.
        n_folds: [integer, optional] Time-series cross-validation folds. Default ``5``.

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
        "fc_stacking: not implemented."
    )
