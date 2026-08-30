# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``covariate_augmented_dickey`` -- method card #123.

#123 Covariate-Augmented Dickey-Fuller (CADF) unit-root test — the power gain from stationary
    covariates (Hansen 1995); a plain ADF when no covariates are supplied

Category 01-preparation-prechecks; module ``covariate_augmented_dickey``.

Reference implementation: 10.1017/S0266466600009993.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "run_cadf",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def run_cadf(
    *,
    y: pd.Series,
    X: pd.DataFrame | None = None,
    type: Literal["trend", "drift", "none"] | None = None,
    max_lag_y: int | None = None,
    min_lag_X: int | None = None,
    max_lag_X: int | None = None,
    criterion: Literal["none", "BIC", "AIC", "HQC", "MAIC"] | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``run_cadf`` -- method card #123.

    Covariate-Augmented Dickey-Fuller (CADF) unit-root test — the power gain from stationary
    covariates (Hansen 1995); a plain ADF when no covariates are supplied.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        y: [series_handle, required] Handle to a univariate ts to test for a unit root (ADF/CADF, no
            NA).
        X: [multiseries_handle, optional] Optional STATIONARY covariates (panel/matrix, same length
            as y)· None => plain ADF.
        type: [enum, optional] Deterministic kernel (default trend).
        max_lag_y: [integer, optional] Maximum lags of the differences of y (>=0, default 1).
            Default ``1``.
        min_lag_X: [integer, optional] Minimum covariate lag· negative = maximum lead (default 0).
            Default ``0``.
        max_lag_X: [integer, optional] Maximum covariate lag (>=0, default 0). Default ``0``.
        criterion: [enum, optional] Automatic lag selection within [min,max] (default none).
        alpha: [number, optional] Decision significance level (default 0.05). Default ``0.05``.

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
        "run_cadf: not implemented."
    )
