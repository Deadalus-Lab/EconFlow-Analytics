# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``automatic_outlier_detection`` -- method card #5.

#5 Automatic outlier detection (Chen-Liu)

Category 01-preparation-prechecks; module ``automatic_outlier_detection``.

Reference implementation: 10.1080/01621459.1993.10594321.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import numpy as np
import pandas as pd

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "run_outlier_detection",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def run_outlier_detection(
    *,
    y: pd.Series,
    exog: np.ndarray | None = None,
    cval: float | None = None,
    delta: float | None = None,
    maxit: int | None = None,
    tsmethod: Literal["auto_arima", "arima"] | None = None,
) -> dict[str, Any]:
    """Node ``run_outlier_detection`` -- method card #5.

    Automatic outlier detection (Chen-Liu).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        y: [series_handle, required] Handle to the ts in which outliers are detected.
        exog: [exog_handle, optional] Optional regressors (matrix with the same start, frequency and
            column labels).
        cval: [number, optional] Outlier significance critical value (default from n).
        delta: [number, optional] Temporary change parameter (default 0.7). Default ``0.7``.
        maxit: [integer, optional] Maximum number of iterations (default 1). Default ``1``.
        tsmethod: [enum, optional] Modelling framework (default auto_arima).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "run_outlier_detection: not implemented."
    )
