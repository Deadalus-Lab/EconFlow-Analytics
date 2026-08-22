# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``gregory_hansen`` -- method card #432.

#432 Gregory-Hansen cointegration with a structural break

Category 05-cointegration; module ``gregory_hansen``.

Reference implementation: arch.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c05_cointegration import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ci_gregory_hansen",
    "NODE_META",
    "wire_model",
]


def ci_gregory_hansen(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    model: Literal["level", "level_trend", "regime", "regime_trend"] | None = None,
    trim: float | None = None,
    lags: int | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``ci_gregory_hansen`` -- method card #432.

    Gregory-Hansen cointegration with a structural break.

    Category 05-cointegration; memory class ``light``.

    Args:
        y: [series_handle, required] Dependent series.
        x: [multiseries_handle, required] Regressor series.
        model: [enum, optional] Break specification. Default ``'level'``.
        trim: [number, optional] Fraction trimmed from each end of the break search. Default
            ``0.15``.
        lags: [integer, optional] Lag order for the ADF regressions.
        alpha: [number, optional] Significance level. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ci_gregory_hansen: not implemented."
    )
