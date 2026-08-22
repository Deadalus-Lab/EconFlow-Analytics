# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``pd_calibration`` -- method card #350.

#350 Probability-of-default calibration, discrimination and reliability

Category 41-credit-risk-default; module ``pd_calibration``.

Reference implementation: scikit-learn.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c41_credit_risk_default import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cr_calibration",
    "cr_discrimination",
    "cr_grade_test",
    "NODE_META",
    "wire_model",
]


def cr_discrimination(
    *,
    y: pd.Series,
    score: pd.Series,
) -> dict[str, Any]:
    """Node ``cr_discrimination`` -- method card #350.

    Probability-of-default calibration, discrimination and reliability.

    Category 41-credit-risk-default; memory class ``light``.

    Args:
        y: [series_handle, required] Binary default indicator.
        score: [series_handle, required] Model score or predicted probability.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cr_discrimination: not implemented."
    )


def cr_calibration(
    *,
    y: pd.Series,
    pd: pd.Series,
    n_bins: int | None = None,
    strategy: Literal["quantile", "uniform"] | None = None,
) -> dict[str, Any]:
    """Node ``cr_calibration`` -- method card #350.

    Probability-of-default calibration, discrimination and reliability.

    Category 41-credit-risk-default; memory class ``light``.

    Args:
        y: [series_handle, required] Binary default indicator.
        pd: [series_handle, required] Predicted default probability.
        n_bins: [integer, optional] Calibration buckets. Default ``10``.
        strategy: [enum, optional] Bucketing strategy. Default ``'quantile'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cr_calibration: not implemented."
    )


def cr_grade_test(
    *,
    y: pd.Series,
    grade: pd.Series,
    grade_pd: pd.Series,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``cr_grade_test`` -- method card #350.

    Probability-of-default calibration, discrimination and reliability.

    Category 41-credit-risk-default; memory class ``light``.

    Args:
        y: [series_handle, required] Binary default indicator.
        grade: [series_handle, required] Assigned rating grade.
        grade_pd: [series_handle, required] PD assigned to each grade.
        alpha: [number, optional] Significance level. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cr_grade_test: not implemented."
    )
