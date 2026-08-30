# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``general_specific_selection`` -- method card #124.

#124 General-to-Specific (GETS) model selection + Indicator Saturation (IIS/SIS/TIS) for outliers &
    structural breaks

Category 01-preparation-prechecks; module ``general_specific_selection``.

Reference implementation: 10.18637/jss.v086.i03.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import numpy as np
import pandas as pd

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "gts_ar_x",
    "gts_indicator_saturation",
    "gts_model_selection",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def gts_ar_x(
    *,
    y: pd.Series,
    mc: bool | None = None,
    ar: Sequence[int] | None = None,
    exog_matrix: np.ndarray | None = None,
    vcov_type: Literal["ordinary", "white", "newey-west"] | None = None,
) -> dict[str, Any]:
    """Node ``gts_ar_x`` -- method card #124.

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
        "gts_ar_x: not implemented."
    )


def gts_model_selection(
    *,
    object: Any,
    t_pval: float | None = None,
    wald_pval: float | None = None,
    vcov_type: Literal["ordinary", "white"] | None = None,
    info_method: Literal["sc", "aic", "aicc", "hq"] | None = None,
) -> dict[str, Any]:
    """Node ``gts_model_selection`` -- method card #124.

    General-to-Specific (GETS) model selection + Indicator Saturation (IIS/SIS/TIS) for outliers &
    structural breaks.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to an 'arx' object (from gts_ar_x.model) = the GUM.
        t_pval: [number, optional] Significance of the t-tests, strictly (0,1) (default 0.05).
            Default ``0.05``.
        wald_pval: [number, optional] Significance of the PET tests (default = t.pval).
        vcov_type: [enum, optional] Override vcov (not given = inherits the arx one· doc-surface
            ordinary/white).
        info_method: [enum, optional] Information criterion for selecting terminals (default sc).

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
        "gts_model_selection: not implemented."
    )


def gts_indicator_saturation(
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
    """Node ``gts_indicator_saturation`` -- method card #124.

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
        "gts_indicator_saturation: not implemented."
    )
