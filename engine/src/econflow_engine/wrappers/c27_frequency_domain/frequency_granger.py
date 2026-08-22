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
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c27_frequency_domain import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "fd_frequency_granger",
    "NODE_META",
    "wire_model",
]


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
    """
    raise NotImplementedError(
        "fd_frequency_granger: not implemented."
    )
