# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``classification_evaluation`` -- method card #529.

#529 Classification evaluation: Brier decomposition, log score, reliability and PR curves

Category 16-limited-dependent; module ``classification_evaluation``.

Reference implementation: scikit-learn.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c16_limited_dependent import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ld_classification_evaluation",
    "NODE_META",
    "wire_model",
]


def ld_classification_evaluation(
    *,
    y: pd.Series,
    probability: pd.Series,
    threshold: float | None = None,
    n_bins: int | None = None,
    decompose: bool | None = None,
) -> dict[str, Any]:
    """Node ``ld_classification_evaluation`` -- method card #529.

    Classification evaluation: Brier decomposition, log score, reliability and PR curves.

    Category 16-limited-dependent; memory class ``light``.

    Args:
        y: [series_handle, required] Binary or categorical outcome.
        probability: [series_handle, required] Predicted probability.
        threshold: [number, optional] Classification threshold. Default ``0.5``.
        n_bins: [integer, optional] Calibration buckets. Default ``10``.
        decompose: [boolean, optional] Decompose the Brier score. Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ld_classification_evaluation: not implemented."
    )
