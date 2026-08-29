# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``quantile_regression_forests`` -- method card #195.

#195 Quantile Regression Forests (nonparametric conditional quantiles / Growth-at-Risk)

Category 12-distribution-risk; module ``quantile_regression_forests``.

Reference implementation: quantile-forest.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

import numpy as np

from econflow_engine.generated.args.c12_distribution_risk import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "qrf_fit",
    "qrf_predict",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def qrf_fit(
    *,
    x: np.ndarray,
    y: Sequence[float],
    ntree: int | None = None,
    nodesize: int | None = None,
    mtry: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``qrf_fit`` -- method card #195.

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
        nodesize: [integer, optional] Minimum terminal node size (default 5· random-forest
            regression). Default ``5``.
        mtry: [integer, optional] Predictors tried per split (default floor(p/3))· must be <= the
            column count of x.
        seed: [integer, optional] Reproducibility seed for the stochastic fit (default 2025).
            Default ``2025``.

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
        "qrf_fit: not implemented."
    )


def qrf_predict(
    *,
    object: Any,
    newdata: np.ndarray,
    quantiles: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``qrf_predict`` -- method card #195.

    Quantile Regression Forests (nonparametric conditional quantiles / Growth-at-Risk).

    Category 12-distribution-risk; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a quantile-regression forest fit (from qrf_fit).
        newdata: [matrix_handle, required] Handle to a matrix/DataFrame of new predictors (same
            columns as the training· without NA).
        quantiles: [num_array, optional] Vector of quantile levels in [0,1]· passed WHOLE (e.g.
            [0.05,0.5,0.95]). Default ``[0.1, 0.5, 0.9]``.

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
        "qrf_predict: not implemented."
    )
