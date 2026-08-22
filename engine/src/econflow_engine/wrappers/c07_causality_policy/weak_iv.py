# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``weak_iv`` -- method card #450.

#450 Weak-instrument-robust inference: Anderson-Rubin, CLR, LIML and JIVE

Category 07-causality-policy; module ``weak_iv``.

Reference implementation: linearmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cp_liml_jive",
    "cp_weak_iv_inference",
    "NODE_META",
    "wire_model",
]


def cp_weak_iv_inference(
    *,
    y: pd.Series,
    endog: pd.DataFrame,
    instruments: pd.DataFrame,
    exog: Sequence[str] | None = None,
    test: Literal["ar", "clr", "lm", "wald"] | None = None,
    grid: Sequence[float] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``cp_weak_iv_inference`` -- method card #450.

    Weak-instrument-robust inference: Anderson-Rubin, CLR, LIML and JIVE.

    Category 07-causality-policy; memory class ``light``.

    Args:
        y: [series_handle, required] Outcome.
        endog: [multiseries_handle, required] Endogenous regressors.
        instruments: [multiseries_handle, required] Excluded instruments.
        exog: [series_codes, optional] Included exogenous columns.
        test: [enum, optional] Robust test. Default ``'clr'``.
        grid: [num_array, optional] Parameter grid for the confidence set.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cp_weak_iv_inference: not implemented."
    )


def cp_liml_jive(
    *,
    y: pd.Series,
    endog: pd.DataFrame,
    instruments: pd.DataFrame,
    exog: Sequence[str] | None = None,
    estimator: Literal["liml", "jive", "fuller", "2sls"] | None = None,
    fuller_alpha: float | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``cp_liml_jive`` -- method card #450.

    Weak-instrument-robust inference: Anderson-Rubin, CLR, LIML and JIVE.

    Category 07-causality-policy; memory class ``light``.

    Args:
        y: [series_handle, required] Outcome.
        endog: [multiseries_handle, required] Endogenous regressors.
        instruments: [multiseries_handle, required] Excluded instruments.
        exog: [series_codes, optional] Included exogenous columns.
        estimator: [enum, optional] Estimator. Default ``'liml'``.
        fuller_alpha: [number, optional] Fuller adjustment parameter. Default ``1.0``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cp_liml_jive: not implemented."
    )
