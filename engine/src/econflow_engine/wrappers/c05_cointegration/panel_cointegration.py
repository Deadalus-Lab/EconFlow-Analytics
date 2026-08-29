# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``panel_cointegration`` -- method card #434.

#434 Panel cointegration: Pedroni, Kao and Westerlund

Category 05-cointegration; module ``panel_cointegration``.

Reference implementation: 10.1111/j.1468-0084.2007.00477.x.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c05_cointegration import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ci_panel_cointegration",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ci_panel_cointegration(
    *,
    data: pd.DataFrame,
    y: str,
    x: Sequence[str] | None = None,
    unit: str,
    time: str,
    test: Literal["pedroni", "kao", "westerlund"] | None = None,
    trend: Literal["n", "c", "ct"] | None = None,
    nboot: int | None = None,
    seed: int | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``ci_panel_cointegration`` -- method card #434.

    Panel cointegration: Pedroni, Kao and Westerlund.

    Category 05-cointegration; memory class ``heavy``.

    Args:
        data: [df_handle, required] Panel data.
        y: [string, required] Dependent column.
        x: [series_codes, optional] Regressor columns.
        unit: [string, required] Unit identifier.
        time: [string, required] Time identifier.
        test: [enum, optional] Test family. Default ``'pedroni'``.
        trend: [enum, optional] Deterministic terms. Default ``'c'``.
        nboot: [integer, optional] Number of bootstrap replications. Default ``0``.
        seed: [integer, optional] Seed for the random number generator.
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
        "ci_panel_cointegration: not implemented."
    )
