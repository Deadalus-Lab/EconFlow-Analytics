# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``vintage_construction`` -- method card #565.

#565 Pseudo-real-time vintage construction from publication lags

Category 23-real-time-revisions; module ``vintage_construction``.

Reference implementation: pandas.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c23_real_time_revisions import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "rt_construct_vintages",
    "NODE_META",
    "wire_model",
]


def rt_construct_vintages(
    *,
    data: pd.DataFrame,
    publication_lags: pd.DataFrame,
    vintage_dates: Sequence[str] | None = None,
    calendar: pd.DataFrame | None = None,
) -> dict[str, Any]:
    """Node ``rt_construct_vintages`` -- method card #565.

    Pseudo-real-time vintage construction from publication lags.

    Category 23-real-time-revisions; memory class ``light``.

    Args:
        data: [df_handle, required] Final-vintage panel.
        publication_lags: [df_handle, required] Publication lag per series.
        vintage_dates: [series_codes, optional] Vintage dates; omitted = every period.
        calendar: [df_handle, optional] Explicit release calendar overriding the lags.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rt_construct_vintages: not implemented."
    )
