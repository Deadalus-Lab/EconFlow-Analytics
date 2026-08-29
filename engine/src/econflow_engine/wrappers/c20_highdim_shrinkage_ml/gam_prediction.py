# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``gam_prediction`` -- method card #552.

#552 Generalised additive models with penalised splines for prediction

Category 20-highdim-shrinkage-ml; module ``gam_prediction``.

Reference implementation: pygam.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c20_highdim_shrinkage_ml import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "hd_gam_prediction",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def hd_gam_prediction(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    distribution: Literal["normal", "binomial", "poisson", "gamma"] | None = None,
    n_splines: int | None = None,
    selection: Literal["gcv", "aic", "cv"] | None = None,
) -> dict[str, Any]:
    """Node ``hd_gam_prediction`` -- method card #552.

    Generalised additive models with penalised splines for prediction.

    Category 20-highdim-shrinkage-ml; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Outcome.
        x: [df_handle, required] Covariate table.
        distribution: [enum, optional] Response distribution. Default ``'normal'``.
        n_splines: [integer, optional] Basis functions per term. Default ``20``.
        selection: [enum, optional] Penalty selection criterion. Default ``'gcv'``.

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
        "hd_gam_prediction: not implemented."
    )
