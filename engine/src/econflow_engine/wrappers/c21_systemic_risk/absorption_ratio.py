# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``absorption_ratio`` -- method card #554.

#554 Absorption ratio and principal-component systemic indicators

Category 21-systemic-risk; module ``absorption_ratio``.

Reference implementation: scikit-learn.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c21_systemic_risk import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "sr_absorption_ratio",
    "NODE_META",
    "wire_model",
]


def sr_absorption_ratio(
    *,
    returns: pd.DataFrame,
    n_components: int | None = None,
    window: int | None = None,
    short_window: int | None = None,
) -> dict[str, Any]:
    """Node ``sr_absorption_ratio`` -- method card #554.

    Absorption ratio and principal-component systemic indicators.

    Category 21-systemic-risk; memory class ``light``.

    Args:
        returns: [df_handle, required] Asset or institution return panel.
        n_components: [integer, optional] Leading components counted; omitted = a fifth of the
            assets.
        window: [integer, optional] Rolling window in periods. Default ``500``.
        short_window: [integer, optional] Short window for the standardised change. Default ``15``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sr_absorption_ratio: not implemented."
    )
