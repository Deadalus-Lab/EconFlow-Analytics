# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bias_corrected_matching`` -- method card #276.

#276 Abadie-Imbens bias-corrected matching with valid standard errors

Category 32-matching-weighting; module ``bias_corrected_matching``.

Reference implementation: 10.1198/jbes.2009.07333.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c32_matching_weighting import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mw_bias_corrected_att",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def mw_bias_corrected_att(
    *,
    data: pd.DataFrame,
    treatment: str,
    outcome: str,
    covariates: Sequence[str] | None = None,
    n_neighbors: int | None = None,
    estimand: Literal["att", "ate"] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``mw_bias_corrected_att`` -- method card #276.

    Abadie-Imbens bias-corrected matching with valid standard errors.

    Category 32-matching-weighting; memory class ``light``.

    Args:
        data: [df_handle, required] One row per unit.
        treatment: [string, required] Binary treatment column.
        outcome: [string, required] Outcome column.
        covariates: [series_codes, optional] Covariates used for matching and for the bias
            correction.
        n_neighbors: [integer, optional] Controls matched per treated unit. Default ``1``.
        estimand: [enum, optional] Estimand to report. Default ``'att'``.
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
        "mw_bias_corrected_att: not implemented."
    )
