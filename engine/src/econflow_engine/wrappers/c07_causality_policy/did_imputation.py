# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``did_imputation`` -- method card #37.

#37 DiD imputation (Borusyak-Jaravel-Spiess)

Category 07-causality-policy; module ``did_imputation``.

Reference implementation: diff-diff.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "did_imputation",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def did_imputation(
    *,
    data: pd.DataFrame,
    yname: str,
    gname: str,
    tname: str,
    idname: str,
    first_stage: str | None = None,
    cluster_var: str | None = None,
) -> dict[str, Any]:
    """Node ``did_imputation`` -- method card #37.

    DiD imputation (Borusyak-Jaravel-Spiess).

    Category 07-causality-policy; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a long-format panel DataFrame.
        yname: [string, required] Outcome column name.
        gname: [string, required] Cohort/first-treatment-period column name (0/Inf = never-treated).
        tname: [string, required] Time column name.
        idname: [string, required] Unit id column name.
        first_stage: [formula, optional] First-stage FE formula, e.g. '~ 0 | unit + period'
            (default: unit+time FE).
        cluster_var: [string, optional] Clustering column name (default: idname).

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
        "did_imputation: not implemented."
    )
