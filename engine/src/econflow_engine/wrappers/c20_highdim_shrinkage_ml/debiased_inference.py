# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``debiased_inference`` -- method card #546.

#546 Debiased and post-selection inference

Category 20-highdim-shrinkage-ml; module ``debiased_inference``.

Reference implementation: doubleml.

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
    "hd_debiased_inference",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def hd_debiased_inference(
    *,
    data: pd.DataFrame,
    y: str,
    d: str,
    controls: Sequence[str] | None = None,
    method: Literal["double_selection", "desparsified", "dml_plr"] | None = None,
    n_folds: int | None = None,
    seed: int | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``hd_debiased_inference`` -- method card #546.

    Debiased and post-selection inference.

    Category 20-highdim-shrinkage-ml; memory class ``light``.

    Args:
        data: [df_handle, required] Data.
        y: [string, required] Outcome column.
        d: [string, required] Target regressor.
        controls: [series_codes, optional] Candidate control columns.
        method: [enum, optional] Method. Default ``'double_selection'``.
        n_folds: [integer, optional] Cross-fitting folds. Default ``5``.
        seed: [integer, optional] Seed for the random number generator.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

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
        "hd_debiased_inference: not implemented."
    )
