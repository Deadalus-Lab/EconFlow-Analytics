# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``partially_linear`` -- method card #288.

#288 Partially linear models by the Robinson double-residual method

Category 33-nonparametric-semiparametric; module ``partially_linear``.

Reference implementation: doubleml.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c33_nonparametric_semiparametric import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "np_partially_linear",
    "NODE_META",
    "wire_model",
]


def np_partially_linear(
    *,
    data: pd.DataFrame,
    y: str,
    d: str,
    covariates: Sequence[str] | None = None,
    learner: Literal["linear", "lasso", "random_forest", "gradient_boosting"] | None = None,
    n_folds: int | None = None,
    seed: int | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``np_partially_linear`` -- method card #288.

    Partially linear models by the Robinson double-residual method.

    Category 33-nonparametric-semiparametric; memory class ``light``.

    Args:
        data: [df_handle, required] One row per unit.
        y: [string, required] Outcome column.
        d: [string, required] Column holding the variable of interest.
        covariates: [series_codes, optional] Nuisance covariate columns.
        learner: [enum, optional] Learner for both nuisance regressions. Default
            ``'random_forest'``.
        n_folds: [integer, optional] Cross-fitting folds. Default ``5``.
        seed: [integer, optional] Seed for the random number generator.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "np_partially_linear: not implemented."
    )
