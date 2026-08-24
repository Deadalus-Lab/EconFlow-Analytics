# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``glassbox_models`` -- method card #549.

#549 Glass-box interpretable models: explainable boosting

Category 20-highdim-shrinkage-ml; module ``glassbox_models``.

Reference implementation: interpret.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c20_highdim_shrinkage_ml import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "hd_glassbox",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def hd_glassbox(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    objective: Literal["regression", "classification"] | None = None,
    interactions: int | None = None,
    max_bins: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``hd_glassbox`` -- method card #549.

    Glass-box interpretable models: explainable boosting.

    Category 20-highdim-shrinkage-ml; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Outcome.
        x: [df_handle, required] Covariate table.
        objective: [enum, optional] Objective. Default ``'regression'``.
        interactions: [integer, optional] Pairwise interaction terms included. Default ``10``.
        max_bins: [integer, optional] Bins per feature. Default ``256``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

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
        "hd_glassbox: not implemented."
    )
