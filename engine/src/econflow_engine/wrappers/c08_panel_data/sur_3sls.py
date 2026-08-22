# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``sur_3sls`` -- method card #461.

#461 Seemingly unrelated regressions and three-stage least squares

Category 08-panel-data; module ``sur_3sls``.

Reference implementation: linearmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c08_panel_data import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pd_sur",
    "NODE_META",
    "wire_model",
]


def pd_sur(
    *,
    data: pd.DataFrame,
    equations: Any,
    estimator: Literal["sur", "3sls", "ols"] | None = None,
    instruments: Sequence[str] | None = None,
    iterate: bool | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``pd_sur`` -- method card #461.

    Seemingly unrelated regressions and three-stage least squares.

    Category 08-panel-data; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Data.
        equations: [raw, required] Equation specifications.
        estimator: [enum, optional] Estimator. Default ``'sur'``.
        instruments: [series_codes, optional] Instruments for the three-stage estimator.
        iterate: [boolean, optional] Iterate the covariance to convergence. Default ``False``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pd_sur: not implemented."
    )
