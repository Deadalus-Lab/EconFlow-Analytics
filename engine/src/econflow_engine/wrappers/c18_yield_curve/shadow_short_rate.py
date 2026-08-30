# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``shadow_short_rate`` -- method card #538.

#538 Shadow short rate at the effective lower bound

Category 18-yield-curve; module ``shadow_short_rate``.

Reference implementation: 10.1111/jmcb.12300.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c18_yield_curve import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "yc_shadow_short_rate",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def yc_shadow_short_rate(
    *,
    yields: pd.DataFrame,
    maturities: Sequence[float],
    lower_bound: float | None = None,
    n_factors: int | None = None,
    model: Literal["wu_xia", "krippner"] | None = None,
) -> dict[str, Any]:
    """Node ``yc_shadow_short_rate`` -- method card #538.

    Shadow short rate at the effective lower bound.

    Category 18-yield-curve; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        yields: [df_handle, required] Yield panel.
        maturities: [num_array, required] Maturities in years.
        lower_bound: [number, optional] Effective lower bound. Default ``0.0``.
        n_factors: [integer, optional] Factors in the term-structure model. Default ``3``.
        model: [enum, optional] Construction. Default ``'wu_xia'``.

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
        "yc_shadow_short_rate: not implemented."
    )
