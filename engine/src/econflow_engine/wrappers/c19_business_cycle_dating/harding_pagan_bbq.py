# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``harding_pagan_bbq`` -- METHOD-SELECTION card #88.

#88 Harding-Pagan BBQ (Quarterly Bry-Boschan turning points)

Category 19-business-cycle-dating; module ``harding_pagan_bbq``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c19_business_cycle_dating import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "average_over_phases",
    "date_business_cycles",
    "NODE_META",
    "wire_model",
]


def date_business_cycles(
    *,
    y: pd.Series,
    mincycle: int | None = None,
    minphase: int | None = None,
    name: str | None = None,
) -> dict[str, Any]:
    """Node ``date_business_cycles`` -- METHOD-SELECTION card #88.

    Harding-Pagan BBQ (Quarterly Bry-Boschan turning points).

    Category 19-business-cycle-dating; memory class ``light``.

    Registers its result under ``bcdating``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Handle to a QUARTERLY (frequency == 4) univariate ts series.
        mincycle: [integer, optional] Minimum full-cycle duration in quarters (default 5; >
            minphase). Default ``5``.
        minphase: [integer, optional] Minimum phase duration in quarters (default 2). Default ``2``.
        name: [string, optional] Optional name label of the dating.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "date_business_cycles: not implemented. The method card is in ./README.md."
    )


def average_over_phases(
    *,
    series: pd.Series,
    dates: Any,
) -> dict[str, Any]:
    """Node ``average_over_phases`` -- METHOD-SELECTION card #88.

    Harding-Pagan BBQ (Quarterly Bry-Boschan turning points).

    Category 19-business-cycle-dating; memory class ``light``.

    Args:
        series: [series_handle, required] Handle to a univariate ts series of the same frequency as
            the dating.
        dates: [raw_handle, required] Handle to a BCDating object (from date_business_cycles
            register).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "average_over_phases: not implemented. The method card is in ./README.md."
    )
