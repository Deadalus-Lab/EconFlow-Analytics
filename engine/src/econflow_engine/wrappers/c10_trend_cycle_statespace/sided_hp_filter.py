# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``sided_hp_filter`` -- METHOD-SELECTION card #92.

#92 One-sided HP filter (Basel III credit gap)

Category 10-trend-cycle-statespace; module ``sided_hp_filter``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c10_trend_cycle_statespace import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "hp_one_sided",
    "NODE_META",
    "wire_model",
]


def hp_one_sided(
    *,
    x: pd.Series,
    lambda_: float | None = None,
) -> dict[str, Any]:
    """Node ``hp_one_sided`` -- METHOD-SELECTION card #92.

    One-sided HP filter (Basel III credit gap).

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate ts· one-sided (real-time) HP trend·
            cycle = gap.
        lambda_ (wire name ``lambda``): [number, optional] Smoothing (default 1600 quarterly· Basel
            III credit-to-GDP = 400000). Default ``1600``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "hp_one_sided: not implemented. The method card is in ./README.md."
    )
