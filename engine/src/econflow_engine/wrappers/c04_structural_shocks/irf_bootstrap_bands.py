# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``irf_bootstrap_bands`` -- method card #426.

#426 Bootstrap and bias-corrected impulse-response bands

Category 04-structural-shocks; module ``irf_bootstrap_bands``.

Reference implementation: arch.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

from econflow_engine.generated.args.c04_structural_shocks import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ss_irf_bands",
    "NODE_META",
    "wire_model",
]


def ss_irf_bands(
    *,
    fit: Any,
    horizons: int | None = None,
    method: Literal["standard", "kilian", "wild", "moving_block", "hall_percentile"] | None = None,
    nboot: int | None = None,
    joint: bool | None = None,
    seed: int,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``ss_irf_bands`` -- method card #426.

    Bootstrap and bias-corrected impulse-response bands.

    Category 04-structural-shocks; memory class ``heavy``.

    Args:
        fit: [raw_handle, required] Handle to a fitted VAR or SVAR.
        horizons: [integer, optional] Impulse-response horizon. Default ``20``.
        method: [enum, optional] Bootstrap scheme. Default ``'kilian'``.
        nboot: [integer, optional] Number of bootstrap replications. Default ``999``.
        joint: [boolean, optional] Report joint rather than pointwise bands. Default ``False``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ss_irf_bands: not implemented."
    )
