# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``quantile_regression_forests`` -- METHOD-SELECTION card #195.

#195 Quantile Regression Forests (nonparametric conditional quantiles / Growth-at-Risk)

Category 12-distribution-risk; module ``quantile_regression_forests``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c12_distribution_risk import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "qrf_fit",
    "qrf_predict",
    "NODE_META",
    "wire_model",
]


def qrf_fit(
    *,
    x: np.ndarray,
    y: Sequence[float],
    ntree: int | None = None,
    nodesize: int | None = None,
    mtry: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``qrf_fit`` -- METHOD-SELECTION card #195.

    Quantile Regression Forests (nonparametric conditional quantiles / Growth-at-Risk).

    Category 12-distribution-risk; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        x: [matrix_handle, required] Handle to a matrix/DataFrame of predictors (one column per
            covariate· without NA).
        y: [num_array, required] Numeric response vector of length the row count of x (e.g. growth)·
            NOT factor, without NA.
        ntree: [integer, optional] Number of trees in the forest (default 200· small/deterministic).
            Default ``200``.
        nodesize: [integer, optional] Minimum terminal node size (default 5· randomForest
            regression). Default ``5``.
        mtry: [integer, optional] Predictors tried per split (default floor(p/3))· must be <= the
            column count of x.
        seed: [integer, optional] Reproducibility seed for the stochastic fit (default 2025).
            Default ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "qrf_fit: not implemented. The method card is in ./README.md."
    )


def qrf_predict(
    *,
    object: Any,
    newdata: np.ndarray,
    quantiles: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``qrf_predict`` -- METHOD-SELECTION card #195.

    Quantile Regression Forests (nonparametric conditional quantiles / Growth-at-Risk).

    Category 12-distribution-risk; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a quantregForest fit (from qrf_fit).
        newdata: [matrix_handle, required] Handle to a matrix/DataFrame of new predictors (same
            columns as the training· without NA).
        quantiles: [num_array, optional] Vector of quantile levels in [0,1]· passed WHOLE (e.g.
            [0.05,0.5,0.95]). Default ``[0.1, 0.5, 0.9]``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "qrf_predict: not implemented. The method card is in ./README.md."
    )
