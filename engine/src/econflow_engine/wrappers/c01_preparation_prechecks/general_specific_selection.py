# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``general_specific_selection`` -- METHOD-SELECTION card #124.

#124 General-to-Specific (GETS) model selection + Indicator Saturation (IIS/SIS/TIS) for outliers &
    structural breaks

Category 01-preparation-prechecks; module ``general_specific_selection``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "gts_arx",
    "gts_getsm",
    "gts_isat",
    "NODE_META",
    "wire_model",
]


def gts_arx(
    *,
    y: pd.Series,
    mc: bool | None = None,
    ar: Sequence[int] | None = None,
    exog_matrix: np.ndarray | None = None,
    vcov_type: Literal["ordinary", "white", "newey-west"] | None = None,
) -> dict[str, Any]:
    """Node ``gts_arx`` -- METHOD-SELECTION card #124.

    General-to-Specific (GETS) model selection + Indicator Saturation (IIS/SIS/TIS) for outliers &
    structural breaks.

    Category 01-preparation-prechecks; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Handle to a univariate ts/vector (AR-X regressand·
            leading/trailing NA allowed, interior NA gated).
        mc: [boolean, optional] Intercept in the mean specification (default True). Default
            ``True``.
        ar: [int_array, optional] AR lags as positive integers, e.g. [1,2] (default none).
        exog_matrix: [exog_handle, optional] Conditioning regressors aligned with y (same length·
            silent-wrong gate).
        vcov_type: [enum, optional] vcov type for inference (default ordinary).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "gts_arx: not implemented. The method card is in ./README.md."
    )


def gts_getsm(
    *,
    object: Any,
    t_pval: float | None = None,
    wald_pval: float | None = None,
    vcov_type: Literal["ordinary", "white"] | None = None,
    info_method: Literal["sc", "aic", "aicc", "hq"] | None = None,
) -> dict[str, Any]:
    """Node ``gts_getsm`` -- METHOD-SELECTION card #124.

    General-to-Specific (GETS) model selection + Indicator Saturation (IIS/SIS/TIS) for outliers &
    structural breaks.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to an 'arx' object (from gts_arx$model) = the GUM.
        t_pval: [number, optional] Significance of the t-tests, strictly (0,1) (default 0.05).
            Default ``0.05``.
        wald_pval: [number, optional] Significance of the PET tests (default = t.pval).
        vcov_type: [enum, optional] Override vcov (not given = inherits the arx one· doc-surface
            ordinary/white).
        info_method: [enum, optional] Information criterion for selecting terminals (default sc).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "gts_getsm: not implemented. The method card is in ./README.md."
    )


def gts_isat(
    *,
    y: pd.Series,
    mc: bool | None = None,
    ar: Sequence[int] | None = None,
    exog_matrix: np.ndarray | None = None,
    iis: bool | None = None,
    sis: bool | None = None,
    tis: bool | None = None,
    t_pval: float | None = None,
    vcov_type: Literal["ordinary", "white", "newey-west"] | None = None,
) -> dict[str, Any]:
    """Node ``gts_isat`` -- METHOD-SELECTION card #124.

    General-to-Specific (GETS) model selection + Indicator Saturation (IIS/SIS/TIS) for outliers &
    structural breaks.

    Category 01-preparation-prechecks; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Handle to a univariate ts/vector (compute-heavy· keep n small).
        mc: [boolean, optional] Intercept in the mean specification (default True). Default
            ``True``.
        ar: [int_array, optional] AR lags as positive integers (default none).
        exog_matrix: [exog_handle, optional] Conditioning regressors aligned with y (silent-wrong
            gate).
        iis: [boolean, optional] Impulse indicator saturation — outliers (default False). Default
            ``False``.
        sis: [boolean, optional] Step indicator saturation — mean-shifts (default True). Default
            ``True``.
        tis: [boolean, optional] Trend indicator saturation — trend-shifts (default False). Default
            ``False``.
        t_pval: [number, optional] Significance of the t-tests, strictly (0,1) (default 0.001).
            Default ``0.001``.
        vcov_type: [enum, optional] vcov type (default ordinary).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "gts_isat: not implemented. The method card is in ./README.md."
    )
