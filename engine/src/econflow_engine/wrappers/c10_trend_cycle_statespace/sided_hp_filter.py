# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``sided_hp_filter`` -- method card #92.

#92 One-sided HP filter (Basel III credit gap)

Category 10-trend-cycle-statespace; module ``sided_hp_filter``.

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
    "hp_one_sided",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def hp_one_sided(
    *,
    x: pd.Series,
    lambda_: float | None = None,
) -> dict[str, Any]:
    """Node ``hp_one_sided`` -- method card #92.

    One-sided HP filter (Basel III credit gap).

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate ts· one-sided (real-time) HP trend·
            cycle = gap.
        lambda_ (wire name ``lambda``): [number, optional] Smoothing (default 1600 quarterly· Basel
            III credit-to-GDP = 400000). Default ``1600``.

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
        "hp_one_sided: not implemented."
    )
