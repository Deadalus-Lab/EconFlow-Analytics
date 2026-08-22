# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``distributional_regression`` -- method card #495.

#495 Distributional regression: location, scale and shape

Category 12-distribution-risk; module ``distributional_regression``.

Reference implementation: pygam.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c12_distribution_risk import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "dr_distributional_regression",
    "NODE_META",
    "wire_model",
]


def dr_distributional_regression(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    family: (
        Literal[
            "normal",
            "gamma",
            "beta",
            "student_t",
            "skew_normal",
            "lognormal",
        ]
        | None
    ) = None,
    model_scale: bool | None = None,
    model_shape: bool | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``dr_distributional_regression`` -- method card #495.

    Distributional regression: location, scale and shape.

    Category 12-distribution-risk; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Outcome.
        x: [df_handle, required] Covariate table.
        family: [enum, optional] Distribution family. Default ``'normal'``.
        model_scale: [boolean, optional] Let covariates shift the scale. Default ``True``.
        model_shape: [boolean, optional] Let covariates shift the shape. Default ``False``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dr_distributional_regression: not implemented."
    )
