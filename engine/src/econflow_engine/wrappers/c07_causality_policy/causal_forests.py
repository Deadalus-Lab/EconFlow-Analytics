# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``causal_forests`` -- method card #44.

#44 Causal forests / GRF

Category 07-causality-policy; module ``causal_forests``.

Reference implementation: econml.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import numpy as np

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "causal_forest_ate",
    "causal_forest_fit",
    "causal_forest_importance",
    "causal_forest_predict",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def causal_forest_fit(
    *,
    X: np.ndarray,
    Y: Any,
    W: Any,
    num_trees: int | None = None,
    min_node_size: int | None = None,
    honesty: bool | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``causal_forest_fit`` -- method card #44.

    Causal forests / GRF.

    Category 07-causality-policy; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        X: [matrix_handle, required] Handle to a covariate matrix (n x p).
        Y: [raw_handle, required] Handle to an outcome vector (length n).
        W: [raw_handle, required] Handle to a treatment vector (length n).
        num_trees: [integer, optional] Number of trees (default 2000). Default ``2000``.
        min_node_size: [integer, optional] Minimum leaf size (default 5). Default ``5``.
        honesty: [boolean, optional] Honest splitting (default True). Default ``True``.
        seed: [integer, optional] Reproducibility seed.

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
        "causal_forest_fit: not implemented."
    )


def causal_forest_predict(
    *,
    forest: Any,
    newdata: np.ndarray | None = None,
    estimate_variance: bool | None = None,
) -> dict[str, Any]:
    """Node ``causal_forest_predict`` -- method card #44.

    Causal forests / GRF.

    Category 07-causality-policy; memory class ``light``.

    Args:
        forest: [raw_handle, required] Handle to a causal_forest (from causal_forest_fit).
        newdata: [matrix_handle, optional] Handle to a new covariate matrix (default: training OOB
            predictions).
        estimate_variance: [boolean, optional] Compute the variance of the CATE (default True).
            Default ``True``.

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
        "causal_forest_predict: not implemented."
    )


def causal_forest_ate(
    *,
    forest: Any,
    target_sample: Literal["all", "treated", "control", "overlap"] | None = None,
    method: Literal["AIPW", "TMLE"] | None = None,
) -> dict[str, Any]:
    """Node ``causal_forest_ate`` -- method card #44.

    Causal forests / GRF.

    Category 07-causality-policy; memory class ``light``.

    Args:
        forest: [raw_handle, required] Handle to a causal_forest (from causal_forest_fit).
        target_sample: [enum, optional] Target sample (default all = ATE).
        method: [enum, optional] Estimator (default AIPW).

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
        "causal_forest_ate: not implemented."
    )


def causal_forest_importance(
    *,
    forest: Any,
    decay_exponent: int | None = None,
    max_depth: int | None = None,
) -> dict[str, Any]:
    """Node ``causal_forest_importance`` -- method card #44.

    Causal forests / GRF.

    Category 07-causality-policy; memory class ``light``.

    Args:
        forest: [raw_handle, required] Handle to a causal_forest (from causal_forest_fit).
        decay_exponent: [integer, optional] Decay exponent for depth weighting (default 2). Default
            ``2``.
        max_depth: [integer, optional] Maximum split-counting depth (default 4). Default ``4``.

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
        "causal_forest_importance: not implemented."
    )
