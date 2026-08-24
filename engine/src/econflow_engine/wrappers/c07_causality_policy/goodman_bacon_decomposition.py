# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``goodman_bacon_decomposition`` -- method card #167.

#167 Goodman-Bacon decomposition of the TWFE DiD coefficient (staggered adoption)

Category 07-causality-policy; module ``goodman_bacon_decomposition``.

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
    "bacon_decompose",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def bacon_decompose(
    *,
    formula: str,
    data: pd.DataFrame,
    id_var: str,
    time_var: str,
    quietly: bool | None = None,
) -> dict[str, Any]:
    """Node ``bacon_decompose`` -- method card #167.

    Goodman-Bacon decomposition of the TWFE DiD coefficient (staggered adoption).

    Category 07-causality-policy; memory class ``light``.

    Args:
        formula: [formula, required] Formula 'outcome ~ treated [+ covariates]'; the treated
            variable is a 0/1 indicator of an active intervention (staggered).
        data: [df_handle, required] Handle to a DataFrame in long panel form — STRICTLY balanced
            (same #periods per unit).
        id_var: [string, required] Unit identifier column name (e.g. 'state').
        time_var: [string, required] Time/period column name (e.g. 'year').
        quietly: [boolean, optional] When True (default) suppresses the console prints of bacon.
            Default ``True``.

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
        "bacon_decompose: not implemented."
    )
