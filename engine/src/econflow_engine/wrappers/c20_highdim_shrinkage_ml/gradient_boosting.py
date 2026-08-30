# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``gradient_boosting`` -- method card #547.

#547 Gradient-boosted trees

Category 20-highdim-shrinkage-ml; module ``gradient_boosting``.

Reference implementation: lightgbm.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c20_highdim_shrinkage_ml import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "hd_gradient_boosting",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def hd_gradient_boosting(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    objective: Literal["regression", "binary", "multiclass", "poisson", "quantile"] | None = None,
    n_estimators: int | None = None,
    learning_rate: float | None = None,
    max_depth: int | None = None,
    early_stopping: int | None = None,
    validation_fraction: float | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``hd_gradient_boosting`` -- method card #547.

    Gradient-boosted trees.

    Category 20-highdim-shrinkage-ml; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Outcome.
        x: [df_handle, required] Covariate table.
        objective: [enum, optional] Objective. Default ``'regression'``.
        n_estimators: [integer, optional] Maximum boosting rounds. Default ``1000``.
        learning_rate: [number, optional] Learning rate. Default ``0.05``.
        max_depth: [integer, optional] Maximum tree depth. Default ``6``.
        early_stopping: [integer, optional] Rounds without improvement before stopping. Default
            ``50``.
        validation_fraction: [number, optional] Held-out fraction for early stopping. Default
            ``0.2``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

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
        "hd_gradient_boosting: not implemented."
    )
