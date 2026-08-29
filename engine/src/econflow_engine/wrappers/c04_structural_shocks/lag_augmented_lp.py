# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``lag_augmented_lp`` -- method card #427.

#427 Lag-augmented local projections with robust inference

Category 04-structural-shocks; module ``lag_augmented_lp``.

Reference implementation: localprojections.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c04_structural_shocks import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ss_lag_augmented_lp",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ss_lag_augmented_lp(
    *,
    y: pd.Series,
    shock: pd.Series,
    controls: Sequence[str] | None = None,
    horizons: int | None = None,
    lags: int | None = None,
    cov_type: Literal["hac", "robust", "newey_west"] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``ss_lag_augmented_lp`` -- method card #427.

    Lag-augmented local projections with robust inference.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        y: [series_handle, required] Response variable.
        shock: [series_handle, required] Shock or impulse variable.
        controls: [series_codes, optional] Control columns.
        horizons: [integer, optional] Maximum horizon. Default ``20``.
        lags: [integer, optional] Lags included. Default ``4``.
        cov_type: [enum, optional] Covariance estimator. Default ``'hac'``.
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
        "ss_lag_augmented_lp: not implemented."
    )
