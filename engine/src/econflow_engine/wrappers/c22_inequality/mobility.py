# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``mobility`` -- method card #562.

#562 Intergenerational and income mobility

Category 22-inequality; module ``mobility``.

Reference implementation: giddy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

import pandas as pd

from econflow_engine.generated.args.c22_inequality import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "iq_mobility",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def iq_mobility(
    *,
    origin: pd.Series,
    destination: pd.Series,
    weights: pd.Series | None = None,
    measures: Sequence[str] | None = None,
    n_groups: int | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``iq_mobility`` -- method card #562.

    Intergenerational and income mobility.

    Category 22-inequality; memory class ``light``.

    Args:
        origin: [series_handle, required] Parent or initial-period income.
        destination: [series_handle, required] Child or later-period income.
        weights: [series_handle, optional] Survey weights.
        measures: [series_codes, optional] Measures to compute; omitted = the standard set.
        n_groups: [integer, optional] Groups for the transition matrix. Default ``5``.
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
        "iq_mobility: not implemented."
    )
