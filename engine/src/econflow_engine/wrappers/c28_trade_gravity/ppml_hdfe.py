# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``ppml_hdfe`` -- method card #597.

#597 PPML with high-dimensional fixed effects and multiway clustering

Category 28-trade-gravity; module ``ppml_hdfe``.

Reference implementation: pyfixest.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

import pandas as pd

from econflow_engine.generated.args.c28_trade_gravity import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tg_ppml_hdfe",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def tg_ppml_hdfe(
    *,
    data: pd.DataFrame,
    formula: str,
    absorb: Sequence[str],
    cluster: Sequence[str] | None = None,
    check_separation: bool | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``tg_ppml_hdfe`` -- method card #597.

    PPML with high-dimensional fixed effects and multiway clustering.

    Category 28-trade-gravity; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Bilateral panel.
        formula: [formula, required] Model formula.
        absorb: [series_codes, required] Columns whose fixed effects are absorbed.
        cluster: [series_codes, optional] Clustering variables.
        check_separation: [boolean, optional] Detect and report perfect separation. Default
            ``True``.
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
        "tg_ppml_hdfe: not implemented."
    )
