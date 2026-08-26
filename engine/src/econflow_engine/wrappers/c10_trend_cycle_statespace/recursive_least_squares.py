# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``recursive_least_squares`` -- method card #481.

#481 Recursive least squares with CUSUM paths

Category 10-trend-cycle-statespace; module ``recursive_least_squares``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c10_trend_cycle_statespace import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tc_recursive_ls",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def tc_recursive_ls(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    start: int | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``tc_recursive_ls`` -- method card #481.

    Recursive least squares with CUSUM paths.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Dependent variable.
        x: [multiseries_handle, required] Regressors.
        start: [integer, optional] Observations before the first recursive estimate.
        alpha: [number, optional] Significance level. Default ``0.05``.

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
        "tc_recursive_ls: not implemented."
    )
