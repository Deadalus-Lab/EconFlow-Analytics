# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bds_test`` -- method card #393.

#393 BDS test for independence and nonlinear structure

Category 01-preparation-prechecks; module ``bds_test``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

import pandas as pd

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pp_bds_test",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pp_bds_test(
    *,
    x: pd.Series,
    max_dim: int | None = None,
    epsilon: Sequence[float] | None = None,
    distance: float | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``pp_bds_test`` -- method card #393.

    BDS test for independence and nonlinear structure.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Series or model residuals.
        max_dim: [integer, optional] Largest embedding dimension. Default ``5``.
        epsilon: [num_array, optional] Distance thresholds in standard deviations.
        distance: [number, optional] Single distance threshold when epsilon is omitted. Default
            ``1.5``.
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
        "pp_bds_test: not implemented."
    )
