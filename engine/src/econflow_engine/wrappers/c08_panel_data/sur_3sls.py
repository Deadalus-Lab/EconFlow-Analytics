# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``sur_3sls`` -- method card #461.

#461 Seemingly unrelated regressions and three-stage least squares

Category 08-panel-data; module ``sur_3sls``.

Reference implementation: linearmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c08_panel_data import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pd_sur",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pd_sur(
    *,
    data: pd.DataFrame,
    equations: Any,
    estimator: Literal["sur", "3sls", "ols"] | None = None,
    instruments: Sequence[str] | None = None,
    iterate: bool | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``pd_sur`` -- method card #461.

    Seemingly unrelated regressions and three-stage least squares.

    Category 08-panel-data; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Data.
        equations: [raw, required] Equation specifications.
        estimator: [enum, optional] Estimator. Default ``'sur'``.
        instruments: [series_codes, optional] Instruments for the three-stage estimator.
        iterate: [boolean, optional] Iterate the covariance to convergence. Default ``False``.
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
        "pd_sur: not implemented."
    )
