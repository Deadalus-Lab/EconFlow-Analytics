# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``conformal_prediction`` -- method card #550.

#550 Conformal prediction for regression and classification

Category 20-highdim-shrinkage-ml; module ``conformal_prediction``.

Reference implementation: mapie.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c20_highdim_shrinkage_ml import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "hd_conformal",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def hd_conformal(
    *,
    fit: Any,
    x_calibration: pd.DataFrame,
    y_calibration: pd.Series,
    x_test: pd.DataFrame,
    method: Literal["split", "cv_plus", "jackknife_plus", "cqr", "naive"] | None = None,
    levels: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``hd_conformal`` -- method card #550.

    Conformal prediction for regression and classification.

    Category 20-highdim-shrinkage-ml; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted model.
        x_calibration: [df_handle, required] Calibration covariates.
        y_calibration: [series_handle, required] Calibration outcomes.
        x_test: [df_handle, required] Covariates to predict for.
        method: [enum, optional] Conformal variant. Default ``'cqr'``.
        levels: [num_array, optional] Coverage levels. Default ``[0.9, 0.95]``.

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
        "hd_conformal: not implemented."
    )
