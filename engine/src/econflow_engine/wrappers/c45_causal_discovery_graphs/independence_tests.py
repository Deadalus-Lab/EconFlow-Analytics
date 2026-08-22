# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``independence_tests`` -- method card #379.

#379 Conditional and unconditional independence testing

Category 45-causal-discovery-graphs; module ``independence_tests``.

Reference implementation: hyppo.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c45_causal_discovery_graphs import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cd_distance_correlation",
    "cd_independence_test",
    "NODE_META",
    "wire_model",
]


def cd_independence_test(
    *,
    x: pd.DataFrame,
    y: pd.DataFrame,
    z: pd.DataFrame | None = None,
    test: Literal["dcorr", "hsic", "kci", "fisherz", "mgc", "hhg"] | None = None,
    n_permutations: int | None = None,
    seed: int | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``cd_independence_test`` -- method card #379.

    Conditional and unconditional independence testing.

    Category 45-causal-discovery-graphs; memory class ``light``.

    Args:
        x: [multiseries_handle, required] First variable set.
        y: [multiseries_handle, required] Second variable set.
        z: [multiseries_handle, optional] Conditioning variable set.
        test: [enum, optional] Test to apply. Default ``'dcorr'``.
        n_permutations: [integer, optional] Permutations for the null; 0 = asymptotic. Default
            ``1000``.
        seed: [integer, optional] Seed for the random number generator.
        alpha: [number, optional] Significance level. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cd_independence_test: not implemented."
    )


def cd_distance_correlation(
    *,
    x: pd.DataFrame,
    y: pd.DataFrame,
    z: pd.DataFrame | None = None,
) -> dict[str, Any]:
    """Node ``cd_distance_correlation`` -- method card #379.

    Conditional and unconditional independence testing.

    Category 45-causal-discovery-graphs; memory class ``light``.

    Args:
        x: [multiseries_handle, required] First variable set.
        y: [multiseries_handle, required] Second variable set.
        z: [multiseries_handle, optional] Variables to partial out.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cd_distance_correlation: not implemented."
    )
