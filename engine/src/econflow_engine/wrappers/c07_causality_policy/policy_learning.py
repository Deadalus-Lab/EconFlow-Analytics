# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``policy_learning`` -- method card #453.

#453 Policy learning and optimal assignment rules

Category 07-causality-policy; module ``policy_learning``.

Reference implementation: econml.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cp_policy_learn",
    "cp_policy_value",
    "NODE_META",
    "wire_model",
]


def cp_policy_learn(
    *,
    fit: Any,
    data: pd.DataFrame,
    policy_class: Literal["threshold", "tree", "linear"] | None = None,
    max_depth: int | None = None,
    budget: float | None = None,
) -> dict[str, Any]:
    """Node ``cp_policy_learn`` -- method card #453.

    Policy learning and optimal assignment rules.

    Category 07-causality-policy; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted CATE model.
        data: [df_handle, required] Data the rule is learned on.
        policy_class: [enum, optional] Rule family. Default ``'tree'``.
        max_depth: [integer, optional] Depth of a policy tree. Default ``2``.
        budget: [number, optional] Maximum share that may be treated.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cp_policy_learn: not implemented."
    )


def cp_policy_value(
    *,
    policy: Any,
    data: pd.DataFrame,
    outcome: str,
    treatment: str,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``cp_policy_value`` -- method card #453.

    Policy learning and optimal assignment rules.

    Category 07-causality-policy; memory class ``light``.

    Args:
        policy: [raw_handle, required] Handle to a learned policy.
        data: [df_handle, required] Held-out evaluation data.
        outcome: [string, required] Outcome column.
        treatment: [string, required] Treatment indicator.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cp_policy_value: not implemented."
    )
