# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``portmanteau_autocorrelation`` -- method card #392.

#392 Ljung-Box and Box-Pierce portmanteau tests with Durbin-Watson

Category 01-preparation-prechecks; module ``portmanteau_autocorrelation``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pp_durbin_watson",
    "pp_ljung_box",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pp_ljung_box(
    *,
    x: pd.Series,
    lags: Sequence[int] | None = None,
    model_df: int | None = None,
    boxpierce: bool | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``pp_ljung_box`` -- method card #392.

    Ljung-Box and Box-Pierce portmanteau tests with Durbin-Watson.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Series or model residuals.
        lags: [int_array, optional] Lags to test; omitted = a rule of thumb.
        model_df: [integer, optional] Estimated model parameters to deduct from the degrees of
            freedom. Default ``0``.
        boxpierce: [boolean, optional] Also report the Box-Pierce variant. Default ``True``.
        alpha: [number, optional] Significance level. Default ``0.05``.

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
        "pp_ljung_box: not implemented."
    )


def pp_durbin_watson(
    *,
    residuals: pd.Series,
    n_regressors: int | None = None,
) -> dict[str, Any]:
    """Node ``pp_durbin_watson`` -- method card #392.

    Ljung-Box and Box-Pierce portmanteau tests with Durbin-Watson.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        residuals: [series_handle, required] Regression residuals.
        n_regressors: [integer, optional] Regressors, for the bounds table.

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
        "pp_durbin_watson: not implemented."
    )
