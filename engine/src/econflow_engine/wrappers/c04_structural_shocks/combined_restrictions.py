# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``combined_restrictions`` -- method card #430.

#430 Combined short-run and long-run restrictions

Category 04-structural-shocks; module ``combined_restrictions``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c04_structural_shocks import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ss_combined_restrictions",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ss_combined_restrictions(
    *,
    y: pd.DataFrame,
    short_run: np.ndarray | None = None,
    long_run: np.ndarray | None = None,
    lags: int | None = None,
    horizons: int | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``ss_combined_restrictions`` -- method card #430.

    Combined short-run and long-run restrictions.

    Category 04-structural-shocks; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [multiseries_handle, required] Endogenous variables.
        short_run: [matrix_handle, optional] Short-run restriction pattern.
        long_run: [matrix_handle, optional] Long-run restriction pattern.
        lags: [integer, optional] VAR lag order. Default ``4``.
        horizons: [integer, optional] Impulse-response horizon. Default ``40``.
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
        "ss_combined_restrictions: not implemented."
    )
