# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``density_evaluation`` -- method card #519.

#519 Density comparison and calibration: Amisano-Giacomini and Berkowitz

Category 15-model-evaluation; module ``density_evaluation``.

Reference implementation: 10.1198/073500106000000332.

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

# --- gen_wrappers: header end ---


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
        "me_density_evaluation: not implemented."
    )
