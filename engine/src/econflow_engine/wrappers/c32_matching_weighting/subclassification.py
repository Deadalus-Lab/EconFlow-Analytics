# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``subclassification`` -- method card #280.

#280 Propensity stratification and subclassification

Category 32-matching-weighting; module ``subclassification``.

Reference implementation: causallib.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c32_matching_weighting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mw_subclassify",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def mw_subclassify(
    *,
    data: pd.DataFrame,
    treatment: str,
    outcome: str,
    pscore: str,
    n_strata: int | None = None,
    estimand: Literal["ate", "att"] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``mw_subclassify`` -- method card #280.

    Propensity stratification and subclassification.

    Category 32-matching-weighting; memory class ``light``.

    Args:
        data: [df_handle, required] One row per unit.
        treatment: [string, required] Binary treatment column.
        outcome: [string, required] Outcome column.
        pscore: [string, required] Column holding the propensity score.
        n_strata: [integer, optional] Number of score strata. Default ``5``.
        estimand: [enum, optional] Aggregation weighting. Default ``'ate'``.
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
        "mw_subclassify: not implemented."
    )
