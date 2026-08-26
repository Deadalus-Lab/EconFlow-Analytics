# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``binomial_glm_recession`` -- method card #83.

#83 Binomial GLM (probit/logit) — recession probability (Estrella-Mishkin)

Category 16-limited-dependent; module ``binomial_glm_recession``.

Reference implementation: pyfixest.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c16_limited_dependent import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "run_binomial_fe_glm",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def run_binomial_fe_glm(
    *,
    formula: str,
    data: pd.DataFrame,
    link: Literal["probit", "logit"] | None = None,
    fixef: str | None = None,
) -> dict[str, Any]:
    """Node ``run_binomial_fe_glm`` -- method card #83.

    Binomial GLM (probit/logit) — recession probability (Estrella-Mishkin).

    Category 16-limited-dependent; memory class ``light``.

    Args:
        formula: [formula, required] Binary model formula, e.g. 'recession ~ spread'· high-dim fixed
            effects also via '| year'.
        data: [df_handle, required] Handle to a DataFrame· LHS binary (0/1, logical or 2-level
            factor), without NA in the variables.
        link: [enum, optional] Link function (default probit — Estrella-Mishkin).
        fixef: [string, optional] Column name of the high-dim fixed effect (alternatively via '|
            col' in the formula)· the column must exist in the data.

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
        "run_binomial_fe_glm: not implemented."
    )
