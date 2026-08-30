# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``cate_metalearners`` -- method card #452.

#452 Meta-learners for conditional average treatment effects: S, T, X, residual and doubly-robust

Category 07-causality-policy; module ``cate_metalearners``.

Reference implementation: econml.

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
    "cp_cate_metalearner",
    "cp_heterogeneity_test",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def cp_cate_metalearner(
    *,
    data: pd.DataFrame,
    outcome: str,
    treatment: str,
    covariates: Sequence[str] | None = None,
    learner: Literal["s", "t", "x", "r", "dr"] | None = None,
    base_model: (
        Literal[
            "linear",
            "random_forest",
            "gradient_boosting",
            "causal_forest",
        ]
        | None
    ) = None,
    n_folds: int | None = None,
    seed: int | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``cp_cate_metalearner`` -- method card #452.

    Meta-learners for conditional average treatment effects: S, T, X, residual and doubly-robust.

    Category 07-causality-policy; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Data.
        outcome: [string, required] Outcome column.
        treatment: [string, required] Treatment indicator.
        covariates: [series_codes, optional] Covariate columns.
        learner: [enum, optional] Meta-learner. Default ``'dr'``.
        base_model: [enum, optional] Base machine learner. Default ``'gradient_boosting'``.
        n_folds: [integer, optional] Cross-fitting folds. Default ``5``.
        seed: [integer, optional] Seed for the random number generator.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

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
        "cp_cate_metalearner: not implemented."
    )


def cp_heterogeneity_test(
    *,
    fit: Any,
    method: Literal["blp", "calibration", "best_linear_predictor"] | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``cp_heterogeneity_test`` -- method card #452.

    Meta-learners for conditional average treatment effects: S, T, X, residual and doubly-robust.

    Category 07-causality-policy; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted CATE model.
        method: [enum, optional] Test. Default ``'blp'``.
        alpha: [number, optional] Significance level. Default ``0.05``.

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
        "cp_heterogeneity_test: not implemented."
    )
