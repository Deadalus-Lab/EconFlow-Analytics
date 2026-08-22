# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``nowcast_news`` -- method card #416.

#416 Nowcast news and revision decomposition

Category 03-multivariate-nowcasting; module ``nowcast_news``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c03_multivariate_nowcasting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mn_nowcast_news",
    "mn_nowcast_weights",
    "NODE_META",
    "wire_model",
]


def mn_nowcast_news(
    *,
    fit: Any,
    vintage_old: pd.DataFrame,
    vintage_new: pd.DataFrame,
    target: str,
    period: str,
) -> dict[str, Any]:
    """Node ``mn_nowcast_news`` -- method card #416.

    Nowcast news and revision decomposition.

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted dynamic factor model.
        vintage_old: [df_handle, required] Earlier data vintage.
        vintage_new: [df_handle, required] Later data vintage.
        target: [string, required] Variable being nowcast.
        period: [string, required] Target period.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mn_nowcast_news: not implemented."
    )


def mn_nowcast_weights(
    *,
    fit: Any,
    target: str,
) -> dict[str, Any]:
    """Node ``mn_nowcast_weights`` -- method card #416.

    Nowcast news and revision decomposition.

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted dynamic factor model.
        target: [string, required] Variable being nowcast.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mn_nowcast_weights: not implemented."
    )
