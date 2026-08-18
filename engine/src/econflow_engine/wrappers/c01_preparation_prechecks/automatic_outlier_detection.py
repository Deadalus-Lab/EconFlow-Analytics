# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``automatic_outlier_detection`` -- METHOD-SELECTION card #5.

#5 Automatic outlier detection (Chen-Liu)

Category 01-preparation-prechecks; module ``automatic_outlier_detection``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "run_tso",
    "NODE_META",
    "wire_model",
]


def run_tso(
    *,
    y: pd.Series,
    exog: np.ndarray | None = None,
    cval: float | None = None,
    delta: float | None = None,
    maxit: int | None = None,
    tsmethod: Literal["auto.arima", "arima"] | None = None,
) -> dict[str, Any]:
    """Node ``run_tso`` -- METHOD-SELECTION card #5.

    Automatic outlier detection (Chen-Liu).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        y: [series_handle, required] Handle to the ts in which outliers are detected.
        exog: [exog_handle, optional] Optional regressors (matrix with the same tsp & colnames).
        cval: [number, optional] Outlier significance critical value (default from n).
        delta: [number, optional] Temporary change parameter (default 0.7). Default ``0.7``.
        maxit: [integer, optional] Maximum number of iterations (default 1). Default ``1``.
        tsmethod: [enum, optional] Modelling framework (default auto.arima).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "run_tso: not implemented. The method card is in ./README.md."
    )
