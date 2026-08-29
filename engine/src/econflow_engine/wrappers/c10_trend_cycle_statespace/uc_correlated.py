# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``uc_correlated`` -- method card #482.

#482 Unobserved components with correlated trend and cycle innovations

Category 10-trend-cycle-statespace; module ``uc_correlated``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from econflow_engine.generated.args.c10_trend_cycle_statespace import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tc_uc_correlated",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def tc_uc_correlated(
    *,
    y: pd.Series,
    cycle_order: int | None = None,
    restrict_correlation: bool | None = None,
    profile_rho: bool | None = None,
) -> dict[str, Any]:
    """Node ``tc_uc_correlated`` -- method card #482.

    Unobserved components with correlated trend and cycle innovations.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Series.
        cycle_order: [integer, optional] Autoregressive order of the cycle. Default ``2``.
        restrict_correlation: [boolean, optional] Impose zero correlation. Default ``False``.
        profile_rho: [boolean, optional] Return the profile likelihood in rho. Default ``True``.

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
        "tc_uc_correlated: not implemented."
    )
