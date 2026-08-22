# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``rd_density`` -- method card #446.

#446 Regression-discontinuity manipulation and density tests

Category 07-causality-policy; module ``rd_density``.

Reference implementation: rddensity.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cp_rd_density_test",
    "NODE_META",
    "wire_model",
]


def cp_rd_density_test(
    *,
    running: pd.Series,
    cutoff: float | None = None,
    method: Literal["mccrary", "cjm"] | None = None,
    bandwidth: float | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``cp_rd_density_test`` -- method card #446.

    Regression-discontinuity manipulation and density tests.

    Category 07-causality-policy; memory class ``light``.

    Args:
        running: [series_handle, required] Running variable.
        cutoff: [number, optional] Cut-off value. Default ``0.0``.
        method: [enum, optional] Test. Default ``'cjm'``.
        bandwidth: [number, optional] Bandwidth; omitted = data-driven.
        alpha: [number, optional] Significance level. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cp_rd_density_test: not implemented."
    )
