# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``survey_reweighting`` -- method card #366.

#366 Reweighting and calibration to population control totals

Category 43-microsimulation-taxbenefit; module ``survey_reweighting``.

Reference implementation: svy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c43_microsimulation_taxbenefit import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tb_reweight",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def tb_reweight(
    *,
    data: pd.DataFrame,
    weights: str,
    targets: pd.DataFrame,
    method: Literal["post_stratification", "raking", "linear", "logit"] | None = None,
    bounds: Sequence[float] | None = None,
    max_iter: int | None = None,
) -> dict[str, Any]:
    """Node ``tb_reweight`` -- method card #366.

    Reweighting and calibration to population control totals.

    Category 43-microsimulation-taxbenefit; memory class ``light``.

    Args:
        data: [df_handle, required] Survey microdata.
        weights: [string, required] Column holding the design weights.
        targets: [df_handle, required] Control totals to match.
        method: [enum, optional] Calibration method. Default ``'raking'``.
        bounds: [num_array, optional] Lower and upper bounds on the weight ratio. Default ``[0.2,
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
        "tb_reweight: not implemented."
    )
