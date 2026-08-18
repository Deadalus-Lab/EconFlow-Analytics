# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``causal_forests_grf`` -- METHOD-SELECTION card #44.

#44 Causal forests / GRF

Category 07-causality-policy; module ``causal_forests_grf``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "wrap_average_treatment_effect",
    "wrap_causal_forest",
    "wrap_predict_causal_forest",
    "wrap_variable_importance",
    "NODE_META",
    "wire_model",
]


def wrap_causal_forest(
    *,
    X: np.ndarray,
    Y: Any,
    W: Any,
    num_trees: int | None = None,
    min_node_size: int | None = None,
    honesty: bool | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``wrap_causal_forest`` -- METHOD-SELECTION card #44.

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
    """
    raise NotImplementedError(
        "wrap_causal_forest: not implemented. The method card is in ./README.md."
    )


def wrap_predict_causal_forest(
    *,
    forest: Any,
    newdata: np.ndarray | None = None,
    estimate_variance: bool | None = None,
) -> dict[str, Any]:
    """Node ``wrap_predict_causal_forest`` -- METHOD-SELECTION card #44.

    Causal forests / GRF.

    Category 07-causality-policy; memory class ``light``.

    Args:
        forest: [raw_handle, required] Handle to a causal_forest (from wrap_causal_forest).
        newdata: [matrix_handle, optional] Handle to a new covariate matrix (default: training OOB
            predictions).
        estimate_variance: [boolean, optional] Compute the variance of the CATE (default True).
            Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_predict_causal_forest: not implemented. The method card is in ./README.md."
    )


def wrap_average_treatment_effect(
    *,
    forest: Any,
    target_sample: Literal["all", "treated", "control", "overlap"] | None = None,
    method: Literal["AIPW", "TMLE"] | None = None,
) -> dict[str, Any]:
    """Node ``wrap_average_treatment_effect`` -- METHOD-SELECTION card #44.

    Causal forests / GRF.

    Category 07-causality-policy; memory class ``light``.

    Args:
        forest: [raw_handle, required] Handle to a causal_forest (from wrap_causal_forest).
        target_sample: [enum, optional] Target sample (default all = ATE).
        method: [enum, optional] Estimator (default AIPW).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_average_treatment_effect: not implemented. The method card is in ./README.md."
    )


def wrap_variable_importance(
    *,
    forest: Any,
    decay_exponent: int | None = None,
    max_depth: int | None = None,
) -> dict[str, Any]:
    """Node ``wrap_variable_importance`` -- METHOD-SELECTION card #44.

    Causal forests / GRF.

    Category 07-causality-policy; memory class ``light``.

    Args:
        forest: [raw_handle, required] Handle to a causal_forest (from wrap_causal_forest).
        decay_exponent: [integer, optional] Decay exponent for depth weighting (default 2). Default
            ``2``.
        max_depth: [integer, optional] Maximum split-counting depth (default 4). Default ``4``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_variable_importance: not implemented. The method card is in ./README.md."
    )
