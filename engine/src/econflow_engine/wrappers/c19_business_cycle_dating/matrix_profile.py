# --- gen_wrappers: header begin ---
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

# --- gen_wrappers: header end ---


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

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "bc_matrix_profile: not implemented."
    )
