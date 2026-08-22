# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``matrix_profile`` -- method card #544.

#544 Matrix-profile motif and discord detection

Category 19-business-cycle-dating; module ``matrix_profile``.

Reference implementation: stumpy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c19_business_cycle_dating import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "bc_matrix_profile",
    "NODE_META",
    "wire_model",
]


def bc_matrix_profile(
    *,
    y: pd.Series,
    window: int,
    n_motifs: int | None = None,
    n_discords: int | None = None,
    normalise: bool | None = None,
) -> dict[str, Any]:
    """Node ``bc_matrix_profile`` -- method card #544.

    Matrix-profile motif and discord detection.

    Category 19-business-cycle-dating; memory class ``light``.

    Args:
        y: [series_handle, required] Series.
        window: [integer, required] Subsequence length.
        n_motifs: [integer, optional] Motifs to return. Default ``3``.
        n_discords: [integer, optional] Discords to return. Default ``3``.
        normalise: [boolean, optional] Z-normalise subsequences before comparison. Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bc_matrix_profile: not implemented."
    )
