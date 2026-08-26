# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``dynamic_nelson_siegel`` -- method card #537.

#537 Dynamic Nelson-Siegel in state space with macro factors

Category 18-yield-curve; module ``dynamic_nelson_siegel``.

Reference implementation: 10.1016/j.jeconom.2005.01.011.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c18_yield_curve import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "yc_dynamic_nelson_siegel",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def yc_dynamic_nelson_siegel(
    *,
    yields: pd.DataFrame,
    maturities: Sequence[float],
    macro: np.ndarray | None = None,
    decay: float | None = None,
    factors: Literal["three", "four_svensson"] | None = None,
    h: int | None = None,
) -> dict[str, Any]:
    """Node ``yc_dynamic_nelson_siegel`` -- method card #537.

    Dynamic Nelson-Siegel in state space with macro factors.

    Category 18-yield-curve; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        yields: [df_handle, required] Yield panel.
        maturities: [num_array, required] Maturities in years.
        macro: [exog_handle, optional] Macro variables to include.
        decay: [number, optional] Decay parameter; omitted = estimated. Default ``0.0609``.
        factors: [enum, optional] Factor set. Default ``'three'``.
        h: [integer, optional] Forecast horizon. Default ``0``.

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
        "yc_dynamic_nelson_siegel: not implemented."
    )
