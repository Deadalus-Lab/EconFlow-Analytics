# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``advanced_lasso`` -- method card #545.

#545 Adaptive lasso, square-root lasso and rigorous penalty selection

Category 20-highdim-shrinkage-ml; module ``advanced_lasso``.

Reference implementation: skglm.

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
    "hd_advanced_lasso",
    "NODE_META",
    "wire_model",
]


def hd_advanced_lasso(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    method: (
        Literal[
            "lasso",
            "adaptive_lasso",
            "sqrt_lasso",
            "rigorous_lasso",
            "elastic_net",
        ]
        | None
    ) = None,
    lambda_: float | None = None,
    robust_loadings: bool | None = None,
    n_folds: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``hd_advanced_lasso`` -- method card #545.

    Adaptive lasso, square-root lasso and rigorous penalty selection.

    Category 20-highdim-shrinkage-ml; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Outcome.
        x: [df_handle, required] Covariate table.
        method: [enum, optional] Estimator. Default ``'sqrt_lasso'``.
        lambda_: [number, optional] Penalty; omitted = by the method's own rule.
        robust_loadings: [boolean, optional] Use heteroskedasticity-robust penalty loadings. Default
            ``True``.
        n_folds: [integer, optional] Folds when cross-validating. Default ``10``.
        seed: [integer, optional] Seed for the random number generator.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "hd_advanced_lasso: not implemented."
    )
