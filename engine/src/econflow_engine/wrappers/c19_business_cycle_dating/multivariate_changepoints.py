# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``multivariate_changepoints`` -- method card #543.

#543 Multivariate and kernel change-point detection with penalty calibration

Category 19-business-cycle-dating; module ``multivariate_changepoints``.

Reference implementation: ruptures.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c19_business_cycle_dating import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "bc_multivariate_changepoints",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def bc_multivariate_changepoints(
    *,
    y: pd.DataFrame,
    model: Literal["l1", "l2", "rbf", "linear", "normal", "ar"] | None = None,
    method: Literal["pelt", "binseg", "dynp", "window", "bottomup"] | None = None,
    penalty: float | None = None,
    n_changepoints: int | None = None,
    min_size: int | None = None,
) -> dict[str, Any]:
    """Node ``bc_multivariate_changepoints`` -- method card #543.

    Multivariate and kernel change-point detection with penalty calibration.

    Category 19-business-cycle-dating; memory class ``light``.

    Args:
        y: [multiseries_handle, required] Series to segment.
        model: [enum, optional] Cost model. Default ``'rbf'``.
        method: [enum, optional] Search method. Default ``'pelt'``.
        penalty: [number, optional] Penalty; omitted = calibrated.
        n_changepoints: [integer, optional] Known number of change points.
        min_size: [integer, optional] Minimum segment length. Default ``5``.

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
        "bc_multivariate_changepoints: not implemented."
    )
