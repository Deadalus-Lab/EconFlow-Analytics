# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``revision_diagnostics`` -- method card #567.

#567 Revision-aware seasonal-adjustment diagnostics

Category 23-real-time-revisions; module ``revision_diagnostics``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c23_real_time_revisions import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "rt_revision_diagnostics",
    "NODE_META",
    "wire_model",
]


def rt_revision_diagnostics(
    *,
    y: pd.Series,
    n_spans: int | None = None,
    span_length: int | None = None,
    threshold: float | None = None,
) -> dict[str, Any]:
    """Node ``rt_revision_diagnostics`` -- method card #567.

    Revision-aware seasonal-adjustment diagnostics.

    Category 23-real-time-revisions; memory class ``light``.

    Args:
        y: [series_handle, required] Unadjusted series.
        n_spans: [integer, optional] Number of overlapping spans. Default ``4``.
        span_length: [integer, optional] Span length in years. Default ``8``.
        threshold: [number, optional] Percentage difference regarded as unstable. Default ``3.0``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rt_revision_diagnostics: not implemented."
    )
