# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``frequency_granger`` -- method card #589.

#589 Frequency-domain Granger causality

Category 27-frequency-domain; module ``frequency_granger``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

import pandas as pd

from econflow_engine.generated.args.c27_frequency_domain import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "fd_frequency_granger",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def fd_frequency_granger(
    *,
    y: pd.DataFrame,
    cause: str,
    effect: str,
    lags: int | None = None,
    bands: Sequence[float] | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``fd_frequency_granger`` -- method card #589.

    Frequency-domain Granger causality.

    Category 27-frequency-domain; memory class ``light``.

    Args:
        y: [multiseries_handle, required] Two or more series.
        cause: [string, required] Candidate causal variable.
        effect: [string, required] Affected variable.
        lags: [integer, optional] VAR lag order. Default ``4``.
        bands: [num_array, optional] Frequency bands to aggregate over.
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
        "fd_frequency_granger: not implemented."
    )
