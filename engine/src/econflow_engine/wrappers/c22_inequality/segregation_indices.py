# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``segregation_indices`` -- method card #560.

#560 Segregation and dissimilarity indices

Category 22-inequality; module ``segregation_indices``.

Reference implementation: segregation.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c22_inequality import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "iq_segregation",
    "NODE_META",
    "wire_model",
]


def iq_segregation(
    *,
    data: pd.DataFrame,
    group: Sequence[str],
    total: str | None = None,
    index: (
        Literal[
            "dissimilarity",
            "gini",
            "entropy",
            "isolation",
            "exposure",
            "atkinson",
        ]
        | None
    ) = None,
    bias_correct: bool | None = None,
    region: str | None = None,
    nboot: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``iq_segregation`` -- method card #560.

    Segregation and dissimilarity indices.

    Category 22-inequality; memory class ``heavy``.

    Args:
        data: [df_handle, required] Area-by-group counts.
        group: [series_codes, required] Group count columns.
        total: [string, optional] Column holding the area total.
        index: [enum, optional] Index. Default ``'dissimilarity'``.
        bias_correct: [boolean, optional] Apply the small-unit bias correction. Default ``True``.
        region: [string, optional] Larger region for decomposition.
        nboot: [integer, optional] Number of bootstrap replications. Default ``500``.
        seed: [integer, optional] Seed for the random number generator.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "iq_segregation: not implemented."
    )
