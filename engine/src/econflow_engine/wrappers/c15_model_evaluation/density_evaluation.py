# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``density_evaluation`` -- method card #519.

#519 Density comparison and calibration: Amisano-Giacomini and Berkowitz

Category 15-model-evaluation; module ``density_evaluation``.

Reference implementation: scoringrules.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c15_model_evaluation import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "me_density_evaluation",
    "NODE_META",
    "wire_model",
]


def me_density_evaluation(
    *,
    actual: pd.Series,
    predictive_cdf: np.ndarray,
    rival_cdf: np.ndarray | None = None,
    test: Literal["berkowitz", "amisano_giacomini", "ks", "knuppel"] | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``me_density_evaluation`` -- method card #519.

    Density comparison and calibration: Amisano-Giacomini and Berkowitz.

    Category 15-model-evaluation; memory class ``light``.

    Args:
        actual: [series_handle, required] Realised values.
        predictive_cdf: [matrix_handle, required] Predictive CDF evaluated at the outcomes.
        rival_cdf: [matrix_handle, optional] Rival predictive CDF for comparison.
        test: [enum, optional] Test. Default ``'berkowitz'``.
        alpha: [number, optional] Significance level. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "me_density_evaluation: not implemented."
    )
