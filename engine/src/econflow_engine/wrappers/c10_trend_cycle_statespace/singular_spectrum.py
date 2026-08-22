# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``singular_spectrum`` -- method card #479.

#479 Singular spectrum analysis

Category 10-trend-cycle-statespace; module ``singular_spectrum``.

Reference implementation: scipy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c10_trend_cycle_statespace import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tc_singular_spectrum",
    "NODE_META",
    "wire_model",
]


def tc_singular_spectrum(
    *,
    y: pd.Series,
    window_length: int | None = None,
    n_components: int | None = None,
    grouping: Any | None = None,
) -> dict[str, Any]:
    """Node ``tc_singular_spectrum`` -- method card #479.

    Singular spectrum analysis.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        y: [series_handle, required] Series.
        window_length: [integer, optional] Embedding window; omitted = a third of the sample.
        n_components: [integer, optional] Components to reconstruct. Default ``3``.
        grouping: [raw, optional] Explicit grouping of singular triples.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tc_singular_spectrum: not implemented."
    )
