# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``implied_term_structure`` -- method card #345.

#345 Term structure of option-implied uncertainty and density fan charts

Category 40-option-implied-derivatives; module ``implied_term_structure``.

Reference implementation: QuantLib.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c40_option_implied_derivatives import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "opt_density_fan",
    "opt_implied_term_structure",
    "NODE_META",
    "wire_model",
]


def opt_implied_term_structure(
    *,
    maturities: Sequence[float],
    implied_variance: Sequence[float],
) -> dict[str, Any]:
    """Node ``opt_implied_term_structure`` -- method card #345.

    Term structure of option-implied uncertainty and density fan charts.

    Category 40-option-implied-derivatives; memory class ``light``.

    Args:
        maturities: [num_array, required] Times to expiry in years.
        implied_variance: [num_array, required] Model-free implied variance per maturity.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "opt_implied_term_structure: not implemented."
    )


def opt_density_fan(
    *,
    densities: np.ndarray,
    grid: Sequence[float],
    quantiles: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``opt_density_fan`` -- method card #345.

    Term structure of option-implied uncertainty and density fan charts.

    Category 40-option-implied-derivatives; memory class ``light``.

    Args:
        densities: [matrix_handle, required] Implied density per horizon.
        grid: [num_array, required] Value grid the densities are defined on.
        quantiles: [num_array, optional] Quantile bands to report. Default ``[0.05, 0.25, 0.5, 0.75,
            0.95]``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "opt_density_fan: not implemented."
    )
