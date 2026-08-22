# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``random_forests_oob`` -- method card #217.

#217 Random forests: OOB error, variable importance, quantile regression forests

Category 20-highdim-shrinkage-ml; module ``random_forests_oob``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c20_highdim_shrinkage_ml import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "rf_fit",
    "rf_predict",
    "NODE_META",
    "wire_model",
]


def rf_fit(
    *,
    x: np.ndarray,
    y: np.ndarray,
    num_trees: int | None = None,
    mtry: int | None = None,
    min_node_size: int | None = None,
    importance: Literal["none", "impurity", "impurity_corrected", "permutation"] | None = None,
    quantile_regression: bool | None = None,
    probability: bool | None = None,
    classification: bool | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``rf_fit`` -- method card #217.

    Random forests: OOB error, variable importance, quantile regression forests.

    Category 20-highdim-shrinkage-ml; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        x: [matrix_handle, required] Handle to the design matrix X (rows=observations,
            columns=variables), numeric, without NA/Inf, >= 2 rows.
        y: [matrix_handle, required] Handle to the response y (numeric vector; length == the row
            count of x). Regression if numeric; set classification/probability=True for categorical
            (numerically coded -> factor).
        num_trees: [integer, optional] Number of trees (default 500; positive integer). Default
            ``500``.
        mtry: [integer, optional] Variables tried per split (default: floor(sqrt(p))· <= the column
            count of x).
        min_node_size: [integer, optional] Minimum terminal-node size (default 5 regression / 1
            classification).
        importance: [enum, optional] Variable importance: none; impurity (fast, biased toward
            high-cardinality)· impurity_corrected (bias-corrected)· permutation (more reliable, more
            expensive).
        quantile_regression: [boolean, optional] True -> quantile regression forest (Meinshausen);
            requires REGRESSION; enables rf_predict type="quantiles". Default ``False``.
        probability: [boolean, optional] True -> probability forest (conditional class
            probabilities; y -> factor). Default ``False``.
        classification: [boolean, optional] True -> classification forest (label prediction· y ->
            factor). Default ``False``.
        seed: [integer, optional] Reproducibility seed (num.threads pinned to 1 internally). Default
            ``42``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rf_fit: not implemented."
    )


def rf_predict(
    *,
    object: Any,
    newdata: np.ndarray,
    type: Literal["response", "quantiles", "se"] | None = None,
    quantiles: Sequence[float] | None = None,
    se_method: Literal["infjack", "jack"] | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``rf_predict`` -- method card #217.

    Random forests: OOB error, variable importance, quantile regression forests.

    Category 20-highdim-shrinkage-ml; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fitted random forest (from rf_fit register field
            'model').
        newdata: [matrix_handle, required] Handle to a design matrix (>= 1 row — a single
            out-of-sample observation is valid) with COLUMN NAMES matching the training variables
            (same set); anonymous/wrong newdata is blocked (a name-match gate, not positional).
        type: [enum, optional] response (point/label/probabilities); quantiles (requires a
            quantile-regression forest); se (jackknife SE; regression only).
        quantiles: [num_array, optional] Quantiles in (0,1) for type="quantiles" (default
            0.1,0.5,0.9).
        se_method: [enum, optional] SE method for type="se": infjack (infinitesimal jackknife) or
            jack.
        seed: [integer, optional] Reproducibility seed (type="se" draws from the random number
            generator). Default ``42``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rf_predict: not implemented."
    )
