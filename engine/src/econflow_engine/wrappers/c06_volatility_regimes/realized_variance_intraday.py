# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``realized_variance_intraday`` -- method card #156.

#156 Realized (co)variance & intraday spot volatility from high-frequency data

Category 06-volatility-regimes; module ``realized_variance_intraday``.

Reference implementation: 10.1093/jjfinec/nbh001.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import numpy as np
import pandas as pd

from econflow_engine.generated.args.c06_volatility_regimes import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "hf_realized_cov",
    "hf_realized_var",
    "hf_spot_vol",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def hf_realized_var(
    *,
    data: Sequence[float],
    measure: Literal["rCov", "rBPCov", "medRV", "rKernelCov", "rTSCov"] | None = None,
    makeReturns: bool | None = None,
    kernelType: (
        Literal[
            "rectangular",
            "bartlett",
            "epanechnikov",
            "tukeyhanning",
            "modifiedtukeyhanning",
        ]
        | None
    ) = None,
    kernelParam: int | None = None,
    K: int | None = None,
    J: int | None = None,
) -> dict[str, Any]:
    """Node ``hf_realized_var`` -- method card #156.

    Realized (co)variance & intraday spot volatility from high-frequency data.

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        data: [num_array, required] Intraday array for ONE day: prices (makeReturns=True) or returns
            (False), ordered, without NA.
        measure: [enum, optional] Realized measure (default rCov). rBPCov/medRV=jump-robust·
            rKernelCov/rTSCov=noise-robust.
        makeReturns: [boolean, optional] True=data holds PRICES (log-returns taken internally)·
            False=already returns. rTSCov requires True. Default ``True``.
        kernelType: [enum, optional] Kernel for measure='rKernelCov' (default rectangular).
        kernelParam: [integer, optional] Lag order of the kernel (rKernelCov, default 1). Default
            ``1``.
        K: [integer, optional] rTSCov: slow time-scale (ticks)· default auto=floor(n/15)· requires
            n>=10*K.
        J: [integer, optional] rTSCov: fast time-scale (ticks, default 1). Default ``1``.

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
        "hf_realized_var: not implemented."
    )


def hf_realized_cov(
    *,
    data: np.ndarray,
    measure: Literal["rCov", "rTSCov", "rSemiCov"] | None = None,
    makeReturns: bool | None = None,
    cor: bool | None = None,
    K: int | None = None,
    J: int | None = None,
) -> dict[str, Any]:
    """Node ``hf_realized_cov`` -- method card #156.

    Realized (co)variance & intraday spot volatility from high-frequency data.

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        data: [matrix_handle, required] T×N intraday matrix for ONE day (>=2 assets): prices or
            returns (see makeReturns), without NA.
        measure: [enum, optional] rCov=plain realized cov· rTSCov=noise-robust·
            rSemiCov=semivariance decomposition (default rCov).
        makeReturns: [boolean, optional] True=data holds PRICES· False=already returns. rTSCov
            requires True. Default ``True``.
        cor: [boolean, optional] True=return the correlation matrix instead of the covariance
            (rCov/rTSCov). Default ``False``.
        K: [integer, optional] rTSCov: slow time-scale (ticks)· default auto=floor(n/15)· requires
            n>=10*K.
        J: [integer, optional] rTSCov: fast time-scale (ticks, default 1). Default ``1``.

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
        "hf_realized_cov: not implemented."
    )


def hf_spot_vol(
    *,
    data: pd.DataFrame,
    method: (
        Literal[
            "detPer",
            "stochPer",
            "kernel",
            "piecewise",
            "garch",
            "RM",
            "PARM",
        ]
        | None
    ) = None,
    alignBy: Literal["minutes", "seconds", "secs", "mins", "hours", "ticks"] | None = None,
    alignPeriod: int | None = None,
    marketOpen: str | None = None,
    marketClose: str | None = None,
    tz: str | None = None,
) -> dict[str, Any]:
    """Node ``hf_spot_vol`` -- method card #156.

    Realized (co)variance & intraday spot volatility from high-frequency data.

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        data: [df_handle, required] DataFrame with columns DT (timestamp intraday timestamps,
            spanning several days) + price (levels).
        method: [enum, optional] Spot vol estimation method (default detPer=deterministic
            periodicity).
        alignBy: [enum, optional] Aggregation time scale (default minutes).
        alignPeriod: [integer, optional] Number of aggregation periods, positive integer (default
            5). Default ``5``.
        marketOpen: [string, optional] Market open time in the tz zone (default 09:30:00). Default
            ``'09:30:00'``.
        marketClose: [string, optional] Market close time in the tz zone (default 16:00:00). Default
            ``'16:00:00'``.
        tz: [string, optional] Time zone of marketOpen/marketClose/DT (default GMT). Default
            ``'GMT'``.

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
        "hf_spot_vol: not implemented."
    )
