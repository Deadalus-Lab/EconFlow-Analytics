# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``distance_independence`` -- method card #403.

#403 Distance correlation and general independence tests

Category 01-preparation-prechecks; module ``distance_independence``.

Reference implementation: dcor.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pp_distance_correlation",
    "NODE_META",
    "wire_model",
]


def pp_distance_correlation(
    *,
    x: pd.DataFrame,
    y: pd.DataFrame,
    z: pd.DataFrame | None = None,
    n_permutations: int | None = None,
    seed: int | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``pp_distance_correlation`` -- method card #403.

    Distance correlation and general independence tests.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [multiseries_handle, required] First variable set.
        y: [multiseries_handle, required] Second variable set.
        z: [multiseries_handle, optional] Variables to partial out.
        n_permutations: [integer, optional] Permutations for the null; 0 = asymptotic. Default
            ``1000``.
        seed: [integer, optional] Seed for the random number generator.
        alpha: [number, optional] Significance level. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pp_distance_correlation: not implemented."
    )
