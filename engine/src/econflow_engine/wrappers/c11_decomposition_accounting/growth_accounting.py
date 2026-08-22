# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``growth_accounting`` -- method card #484.

#484 Growth accounting and Tornqvist-Divisia total factor productivity

Category 11-decomposition-accounting; module ``growth_accounting``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c11_decomposition_accounting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "da_growth_accounting",
    "NODE_META",
    "wire_model",
]


def da_growth_accounting(
    *,
    output: pd.Series,
    inputs: pd.DataFrame,
    shares: pd.DataFrame | None = None,
    index: Literal["tornqvist", "divisia", "laspeyres", "fixed_share"] | None = None,
) -> dict[str, Any]:
    """Node ``da_growth_accounting`` -- method card #484.

    Growth accounting and Tornqvist-Divisia total factor productivity.

    Category 11-decomposition-accounting; memory class ``light``.

    Args:
        output: [series_handle, required] Output series.
        inputs: [multiseries_handle, required] Input series, one column each.
        shares: [multiseries_handle, optional] Factor shares; omitted = estimated from cost data.
        index: [enum, optional] Index form. Default ``'tornqvist'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "da_growth_accounting: not implemented."
    )
