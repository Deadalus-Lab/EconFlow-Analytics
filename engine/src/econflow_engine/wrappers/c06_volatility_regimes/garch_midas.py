# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``garch_midas`` -- METHOD-SELECTION card #159.

#159 GARCH-MIDAS (a short-run GARCH × a long-run MIDAS macro component)

Category 06-volatility-regimes; module ``garch_midas``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c06_volatility_regimes import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mfg_fit",
    "mfg_predict",
    "mfg_simulate",
    "NODE_META",
    "wire_model",
]


def mfg_fit(
    *,
    data: pd.DataFrame,
    y: str,
    x: str,
    K: int,
    low_freq: str | None = None,
    weighting: Literal["beta.restricted", "beta.unrestricted"] | None = None,
    gamma: bool | None = None,
    var_ratio_freq: str | None = None,
) -> dict[str, Any]:
    """Node ``mfg_fit`` -- METHOD-SELECTION card #159.

    GARCH-MIDAS (a short-run GARCH × a long-run MIDAS macro component).

    Category 06-volatility-regimes; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Handle to a long-format DataFrame· REQUIRED column 'date'
            (Date), numeric y, numeric x constant per low.freq, low.freq column of class Date.
        y: [string, required] Name of the high-freq returns column (numeric, without NA).
        x: [string, required] Name of the low-freq macro variable column (MIDAS long-run· ONE value
            per low.freq period).
        K: [integer, required] MIDAS lag-length (positive integer < number of low.freq periods).
        low_freq: [string, optional] Name of the low-freq index column of class Date (default 'date'
            = daily). Default ``'date'``.
        weighting: [enum, optional] MIDAS beta weighting scheme (default beta.restricted, w1=1).
        gamma: [boolean, optional] Asymmetric GJR-GARCH term in the short-run component (default
            True). Default ``True``.
        var_ratio_freq: [string, optional] Frequency column for the variance ratio (default:
            low.freq).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mfg_fit: not implemented. The method card is in ./README.md."
    )


def mfg_predict(
    *,
    object: Any,
    horizon: Sequence[int] | None = None,
) -> dict[str, Any]:
    """Node ``mfg_predict`` -- METHOD-SELECTION card #159.

    GARCH-MIDAS (a short-run GARCH × a long-run MIDAS macro component).

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to an 'mfGARCH' model (from mfg_fit).
        horizon: [int_array, optional] Forecast horizons for total volatility (positive integers,
            default 1:10).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mfg_predict: not implemented. The method card is in ./README.md."
    )


def mfg_simulate(
    *,
    n_days: int,
    mu: float,
    alpha: float,
    beta: float,
    gamma: float,
    m: float,
    theta: float,
    w2: float,
    K: int,
    psi: float,
    sigma_psi: float,
    w1: float | None = None,
    low_freq: int | None = None,
    n_intraday: int | None = None,
    corr: float | None = None,
) -> dict[str, Any]:
    """Node ``mfg_simulate`` -- METHOD-SELECTION card #159.

    GARCH-MIDAS (a short-run GARCH × a long-run MIDAS macro component).

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        n_days: [integer, required] Number of days to simulate (positive integer).
        mu: [number, required] Mean of the returns.
        alpha: [number, required] GARCH ARCH coefficient (short-run).
        beta: [number, required] GARCH persistence coefficient (short-run).
        gamma: [number, required] Asymmetric (leverage) coefficient.
        m: [number, required] Constant term of the long-run component.
        theta: [number, required] Sensitivity of the long-run component to the MIDAS covariate.
        w2: [number, required] Beta weighting parameter w2.
        K: [integer, required] MIDAS lag-length (positive integer < low.freq).
        psi: [number, required] AR(1) persistence of the simulated covariate.
        sigma_psi: [number, required] Standard deviation of the covariate innovations.
        w1: [number, optional] Beta weighting parameter w1 (default 1, restricted). Default ``1``.
        low_freq: [integer, optional] Length of the low-freq period in days (default 1). Default
            ``1``.
        n_intraday: [integer, optional] Intraday observations per day (default 288). Default
            ``288``.
        corr: [number, optional] Returns-covariate correlation (leverage, default 0). Default ``0``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mfg_simulate: not implemented. The method card is in ./README.md."
    )
