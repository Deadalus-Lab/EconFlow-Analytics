# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``survey_weighting`` -- method card #577.

#577 Survey weighting: raking, post-stratification and trimming

Category 25-expectations-surveys; module ``survey_weighting``.

Reference implementation: svy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c25_expectations_surveys import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "es_survey_weights",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def es_survey_weights(
    *,
    data: pd.DataFrame,
    base_weights: str | None = None,
    targets: pd.DataFrame,
    method: (
        Literal[
            "post_stratification",
            "raking",
            "linear_calibration",
            "logit_calibration",
        ]
        | None
    ) = None,
    trim: Sequence[float] | None = None,
    max_iter: int | None = None,
) -> dict[str, Any]:
    """Node ``es_survey_weights`` -- method card #577.

    Survey weighting: raking, post-stratification and trimming.

    Category 25-expectations-surveys; memory class ``light``.

    Args:
        data: [df_handle, required] Survey microdata.
        base_weights: [string, optional] Column holding design weights.
        targets: [df_handle, required] Population control totals.
        method: [enum, optional] Method. Default ``'raking'``.
        trim: [num_array, optional] Lower and upper bounds on the weight ratio. Default ``[0.2,
            5.0]``.
        max_iter: [integer, optional] Maximum iterations. Default ``100``.

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
        "es_survey_weights: not implemented."
    )
