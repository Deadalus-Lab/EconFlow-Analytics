# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``ppml_hdfe`` -- method card #597.

#597 PPML with high-dimensional fixed effects and multiway clustering

Category 28-trade-gravity; module ``ppml_hdfe``.

Reference implementation: pyfixest.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c28_trade_gravity import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tg_ppml_hdfe",
    "NODE_META",
    "wire_model",
]


def tg_ppml_hdfe(
    *,
    data: pd.DataFrame,
    formula: str,
    absorb: Sequence[str],
    cluster: Sequence[str] | None = None,
    check_separation: bool | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``tg_ppml_hdfe`` -- method card #597.

    PPML with high-dimensional fixed effects and multiway clustering.

    Category 28-trade-gravity; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Bilateral panel.
        formula: [formula, required] Model formula.
        absorb: [series_codes, required] Columns whose fixed effects are absorbed.
        cluster: [series_codes, optional] Clustering variables.
        check_separation: [boolean, optional] Detect and report perfect separation. Default
            ``True``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tg_ppml_hdfe: not implemented."
    )
