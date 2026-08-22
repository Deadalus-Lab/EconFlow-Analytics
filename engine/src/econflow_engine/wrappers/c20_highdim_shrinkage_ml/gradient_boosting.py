# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``gradient_boosting`` -- method card #547.

#547 Gradient-boosted trees

Category 20-highdim-shrinkage-ml; module ``gradient_boosting``.

Reference implementation: lightgbm.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c20_highdim_shrinkage_ml import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "hd_gradient_boosting",
    "NODE_META",
    "wire_model",
]


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
    """
    raise NotImplementedError(
        "hd_gradient_boosting: not implemented."
    )
