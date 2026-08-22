# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``minimum_distance`` -- method card #295.

#295 Classical and efficient minimum distance

Category 34-gmm-mestimation-partial-id; module ``minimum_distance``.

Reference implementation: optimagic.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c34_gmm_mestimation_partial_id import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "gme_minimum_distance",
    "NODE_META",
    "wire_model",
]


def gme_minimum_distance(
    *,
    reduced_form: Sequence[float],
    vcov: np.ndarray,
    mapping: str,
    weighting: Literal["efficient", "identity", "diagonal"] | None = None,
    start: Sequence[float] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``gme_minimum_distance`` -- method card #295.

    Classical and efficient minimum distance.

    Category 34-gmm-mestimation-partial-id; memory class ``light``.

    Args:
        reduced_form: [num_array, required] Reduced-form parameter estimates.
        vcov: [matrix_handle, required] Covariance of the reduced-form estimates.
        mapping: [formula, required] Structural mapping from parameters to reduced form.
        weighting: [enum, optional] Weighting scheme. Default ``'efficient'``.
        start: [num_array, optional] Starting values.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "gme_minimum_distance: not implemented."
    )
