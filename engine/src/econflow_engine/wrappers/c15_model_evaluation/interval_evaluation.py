# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``interval_evaluation`` -- method card #518.

#518 Interval and quantile evaluation: coverage, Winkler and weighted interval score

Category 15-model-evaluation; module ``interval_evaluation``.

Reference implementation: scoringrules.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c15_model_evaluation import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "me_interval_evaluation",
    "NODE_META",
    "wire_model",
]


def me_interval_evaluation(
    *,
    actual: pd.Series,
    lower: pd.DataFrame,
    upper: pd.DataFrame,
    levels: Sequence[float],
    decompose: bool | None = None,
) -> dict[str, Any]:
    """Node ``me_interval_evaluation`` -- method card #518.

    Interval and quantile evaluation: coverage, Winkler and weighted interval score.

    Category 15-model-evaluation; memory class ``light``.

    Args:
        actual: [series_handle, required] Realised values.
        lower: [df_handle, required] Lower bounds, one column per level.
        upper: [df_handle, required] Upper bounds, one column per level.
        levels: [num_array, required] Nominal levels.
        decompose: [boolean, optional] Decompose the weighted interval score. Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "me_interval_evaluation: not implemented."
    )
