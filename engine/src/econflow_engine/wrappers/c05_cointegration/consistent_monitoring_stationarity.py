# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``consistent_monitoring_stationarity`` -- method card #141.

#141 Consistent monitoring of stationarity & cointegration (Wagner-Wied): calibration-period
    estimation + a sequential detector (FM/D/IM-OLS)

Category 05-cointegration; module ``consistent_monitoring_stationarity``.

Reference implementation: 10.1111/jtsa.12247.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import numpy as np
import pandas as pd

from econflow_engine.generated.args.c05_cointegration import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cmo_cointegration",
    "cmo_stationarity",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def cmo_stationarity(
    *,
    x: pd.Series,
    m: float | None = None,
    trend: bool | None = None,
    kernel: Literal["ba", "pa", "qs", "tr"] | None = None,
    bandwidth: Literal["and", "nw"] | None = None,
    signif_level: float | None = None,
) -> dict[str, Any]:
    """Node ``cmo_stationarity`` -- method card #141.

    Consistent monitoring of stationarity & cointegration (Wagner-Wied): calibration-period
    estimation + a sequential detector (FM/D/IM-OLS).

    Category 05-cointegration; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a one-dimensional series under monitoring (numeric
            ts/vector, WITHOUT NA).
        m: [number, optional] Calibration period fraction ∈ [0.1, 0.9] (default 0.25); parameters
            are estimated only on [1..floor(m*N)]. Default ``0.25``.
        trend: [boolean, optional] True = intercept + linear trend; False (default) = intercept
            only. Default ``False``.
        kernel: [enum, optional] Kernel long-run variance (default ba = Bartlett).
        bandwidth: [enum, optional] Automatic bandwidth selection (default and = Andrews 1991).
        signif_level: [number, optional] Significance level ∈ [0.01, 0.1] (default 0.05); detection
            time only if p < signif_level. Default ``0.05``.

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
        "cmo_stationarity: not implemented."
    )


def cmo_cointegration(
    *,
    x: np.ndarray,
    y: pd.Series,
    m: float | None = None,
    model: Literal["FM", "D", "IM"] | None = None,
    trend: bool | None = None,
    kernel: Literal["ba", "pa", "qs", "tr"] | None = None,
    bandwidth: Literal["and", "nw"] | None = None,
    signif_level: float | None = None,
    D_options: Any | None = None,
) -> dict[str, Any]:
    """Node ``cmo_cointegration`` -- method card #141.

    Consistent monitoring of stationarity & cointegration (Wagner-Wied): calibration-period
    estimation + a sequential detector (FM/D/IM-OLS).

    Category 05-cointegration; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to RHS regressors (numeric matrix/vector, I(1), WITHOUT
            NA).
        y: [series_handle, required] Handle to the LHS response (one-dimensional, length==the row
            count of x, WITHOUT NA).
        m: [number, optional] Calibration period fraction ∈ [0.1, 0.9] (default 0.25). Default
            ``0.25``.
        model: [enum, optional] Modified-OLS: FM-OLS (default), D-OLS (=DOLS), IM-OLS.
        trend: [boolean, optional] True = intercept + linear trend; False (default) = intercept
            only. Default ``False``.
        kernel: [enum, optional] Kernel long-run variance (default ba = Bartlett).
        bandwidth: [enum, optional] Automatic bandwidth selection (default and = Andrews 1991).
        signif_level: [number, optional] Significance level ∈ [0.01, 0.1] (default 0.05). Default
            ``0.05``.
        D_options: [raw, optional] Only for model='D': list(n.lead,n.lag,kmax,info.crit) for D-OLS;
            None = cointRegD's defaults.

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
        "cmo_cointegration: not implemented."
    )
