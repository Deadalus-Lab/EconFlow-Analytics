# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``explainability`` -- method card #548.

#548 Explainability: SHAP, permutation importance and partial dependence

Category 20-highdim-shrinkage-ml; module ``explainability``.

Reference implementation: shap.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c20_highdim_shrinkage_ml import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "hd_explain",
    "NODE_META",
    "wire_model",
]


def hd_explain(
    *,
    fit: Any,
    x: pd.DataFrame,
    method: Literal["shap", "permutation", "partial_dependence", "ale"] | None = None,
    features: Sequence[str] | None = None,
    n_repeats: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``hd_explain`` -- method card #548.

    Explainability: SHAP, permutation importance and partial dependence.

    Category 20-highdim-shrinkage-ml; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted model.
        x: [df_handle, required] Data to explain.
        method: [enum, optional] Explanation method. Default ``'shap'``.
        features: [series_codes, optional] Features to explain; omitted = all.
        n_repeats: [integer, optional] Repeats for permutation importance. Default ``10``.
        seed: [integer, optional] Seed for the random number generator.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "hd_explain: not implemented."
    )
