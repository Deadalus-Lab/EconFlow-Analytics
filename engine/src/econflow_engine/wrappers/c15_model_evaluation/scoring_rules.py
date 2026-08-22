# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``scoring_rules`` -- method card #514.

#514 Proper scoring rules: CRPS, log score, pinball and tail-weighted CRPS

Category 15-model-evaluation; module ``scoring_rules``.

Reference implementation: scoringrules.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c15_model_evaluation import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "me_scoring_rules",
    "NODE_META",
    "wire_model",
]


def me_scoring_rules(
    *,
    actual: pd.Series,
    forecast: np.ndarray,
    rule: Literal["crps", "log_score", "pinball", "dss", "interval_score", "energy"] | None = None,
    quantile_levels: Sequence[float] | None = None,
    weight: Literal["none", "left_tail", "right_tail", "centre"] | None = None,
) -> dict[str, Any]:
    """Node ``me_scoring_rules`` -- method card #514.

    Proper scoring rules: CRPS, log score, pinball and tail-weighted CRPS.

    Category 15-model-evaluation; memory class ``light``.

    Args:
        actual: [series_handle, required] Realised values.
        forecast: [matrix_handle, required] Predictive samples or quantiles.
        rule: [enum, optional] Scoring rule. Default ``'crps'``.
        quantile_levels: [num_array, optional] Quantile levels when the forecast is quantiles.
        weight: [enum, optional] Tail weighting. Default ``'none'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "me_scoring_rules: not implemented."
    )
