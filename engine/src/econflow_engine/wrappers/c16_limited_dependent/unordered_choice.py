# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``unordered_choice`` -- method card #528.

#528 Multinomial and conditional logit for unordered outcomes

Category 16-limited-dependent; module ``unordered_choice``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c16_limited_dependent import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ld_unordered_choice",
    "NODE_META",
    "wire_model",
]


def ld_unordered_choice(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    model: Literal["multinomial", "conditional", "multinomial_probit"] | None = None,
    base: str | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``ld_unordered_choice`` -- method card #528.

    Multinomial and conditional logit for unordered outcomes.

    Category 16-limited-dependent; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Categorical outcome.
        x: [df_handle, required] Covariate table.
        model: [enum, optional] Model. Default ``'multinomial'``.
        base: [string, optional] Base alternative.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ld_unordered_choice: not implemented."
    )
