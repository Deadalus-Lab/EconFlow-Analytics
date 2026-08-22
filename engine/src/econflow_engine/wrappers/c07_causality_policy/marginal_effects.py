# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``marginal_effects`` -- method card #455.

#455 Marginal effects, contrasts and predictions for any fitted model

Category 07-causality-policy; module ``marginal_effects``.

Reference implementation: marginaleffects.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cp_marginal_effects",
    "NODE_META",
    "wire_model",
]


def cp_marginal_effects(
    *,
    fit: Any,
    variables: Sequence[str] | None = None,
    at: pd.DataFrame | None = None,
    type: (
        Literal[
            "average_marginal_effect",
            "marginal_effect_at_mean",
            "prediction",
            "contrast",
        ]
        | None
    ) = None,
    by: Sequence[str] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``cp_marginal_effects`` -- method card #455.

    Marginal effects, contrasts and predictions for any fitted model.

    Category 07-causality-policy; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted model.
        variables: [series_codes, optional] Variables to compute effects for.
        at: [df_handle, optional] Covariate values to evaluate at.
        type: [enum, optional] Quantity returned. Default ``'average_marginal_effect'``.
        by: [series_codes, optional] Group the effects by these columns.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cp_marginal_effects: not implemented."
    )
