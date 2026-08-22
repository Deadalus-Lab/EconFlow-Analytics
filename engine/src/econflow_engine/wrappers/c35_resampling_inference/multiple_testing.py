# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``multiple_testing`` -- method card #308.

#308 Multiple testing: Holm, Benjamini-Hochberg and Romano-Wolf stepdown

Category 35-resampling-inference; module ``multiple_testing``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c35_resampling_inference import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "rs_multiple_testing",
    "rs_romano_wolf",
    "NODE_META",
    "wire_model",
]


def rs_multiple_testing(
    *,
    p_values: Sequence[float],
    method: Literal["bonferroni", "holm", "hochberg", "bh", "by", "sidak"] | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``rs_multiple_testing`` -- method card #308.

    Multiple testing: Holm, Benjamini-Hochberg and Romano-Wolf stepdown.

    Category 35-resampling-inference; memory class ``light``.

    Args:
        p_values: [num_array, required] Unadjusted p-values.
        method: [enum, optional] Adjustment procedure. Default ``'holm'``.
        alpha: [number, optional] Significance level. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rs_multiple_testing: not implemented."
    )


def rs_romano_wolf(
    *,
    statistics: Sequence[float],
    bootstrap_draws: np.ndarray,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``rs_romano_wolf`` -- method card #308.

    Multiple testing: Holm, Benjamini-Hochberg and Romano-Wolf stepdown.

    Category 35-resampling-inference; memory class ``light``.

    Args:
        statistics: [num_array, required] Test statistics.
        bootstrap_draws: [matrix_handle, required] Bootstrap draws of the statistics under the null.
        alpha: [number, optional] Significance level. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rs_romano_wolf: not implemented."
    )
