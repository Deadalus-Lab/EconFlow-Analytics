# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``modified_ols_cointegrating`` -- method card #27.

#27 Modified-OLS cointegrating regressions: FM-OLS / D-OLS / IM-OLS

Category 05-cointegration; module ``modified_ols_cointegrating``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c05_cointegration import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "creg_dols",
    "creg_fmols",
    "creg_imols",
    "NODE_META",
    "wire_model",
]


def creg_fmols(
    *,
    x: np.ndarray,
    y: pd.Series,
    deter: Literal["const", "trend", "none"] | None = None,
    kernel: Literal["ba", "pa", "qs", "tr"] | None = None,
    bandwidth: Literal["and", "nw"] | None = None,
    demeaning: bool | None = None,
) -> dict[str, Any]:
    """Node ``creg_fmols`` -- method card #27.

    Modified-OLS cointegrating regressions: FM-OLS / D-OLS / IM-OLS.

    Category 05-cointegration; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to regressors (matrix/vector, I(1)).
        y: [series_handle, required] Handle to a response series (one-dimensional, I(1)).
        deter: [enum, optional] Deterministic terms (default const).
        kernel: [enum, optional] Kernel long-run variance (default ba = Bartlett).
        bandwidth: [enum, optional] Bandwidth selection (default and = Andrews).
        demeaning: [boolean, optional] True = demeaning before the estimation (default False).
            Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "creg_fmols: not implemented."
    )


def creg_dols(
    *,
    x: np.ndarray,
    y: pd.Series,
    deter: Literal["const", "trend", "none"] | None = None,
    kernel: Literal["ba", "pa", "qs", "tr"] | None = None,
    bandwidth: Literal["and", "nw"] | None = None,
    kmax: Literal["k4", "k12"] | None = None,
    info_crit: Literal["AIC", "BIC"] | None = None,
    demeaning: bool | None = None,
) -> dict[str, Any]:
    """Node ``creg_dols`` -- method card #27.

    Modified-OLS cointegrating regressions: FM-OLS / D-OLS / IM-OLS.

    Category 05-cointegration; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to regressors (matrix/vector, I(1)).
        y: [series_handle, required] Handle to a response series (one-dimensional, I(1)).
        deter: [enum, optional] Deterministic terms (default const).
        kernel: [enum, optional] Kernel long-run variance (default ba).
        bandwidth: [enum, optional] Bandwidth selection (default and).
        kmax: [enum, optional] Upper bound of lead/lag for automatic selection (default k4).
        info_crit: [enum, optional] Lead/lag selection criterion (default AIC).
        demeaning: [boolean, optional] True = demeaning (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "creg_dols: not implemented."
    )


def creg_imols(
    *,
    x: np.ndarray,
    y: pd.Series,
    deter: Literal["const", "trend", "none"] | None = None,
    kernel: Literal["ba", "pa", "qs", "tr"] | None = None,
    bandwidth: Literal["and", "nw"] | None = None,
) -> dict[str, Any]:
    """Node ``creg_imols`` -- method card #27.

    Modified-OLS cointegrating regressions: FM-OLS / D-OLS / IM-OLS.

    Category 05-cointegration; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to regressors (matrix/vector, I(1)).
        y: [series_handle, required] Handle to a response series (one-dimensional, I(1)).
        deter: [enum, optional] Deterministic terms (default const).
        kernel: [enum, optional] Kernel long-run variance (default ba).
        bandwidth: [enum, optional] Bandwidth selection (default and).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "creg_imols: not implemented."
    )
