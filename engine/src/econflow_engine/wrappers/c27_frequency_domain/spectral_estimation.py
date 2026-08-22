# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``spectral_estimation`` -- method card #588.

#588 Multitaper and Welch spectral estimation with confidence intervals

Category 27-frequency-domain; module ``spectral_estimation``.

Reference implementation: spectrum.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c27_frequency_domain import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "fd_spectral_estimate",
    "NODE_META",
    "wire_model",
]


def fd_spectral_estimate(
    *,
    x: pd.Series,
    method: Literal["multitaper", "welch", "bartlett", "periodogram", "ar"] | None = None,
    n_tapers: int | None = None,
    time_bandwidth: float | None = None,
    nperseg: int | None = None,
    ar_order: int | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``fd_spectral_estimate`` -- method card #588.

    Multitaper and Welch spectral estimation with confidence intervals.

    Category 27-frequency-domain; memory class ``light``.

    Args:
        x: [series_handle, required] Series.
        method: [enum, optional] Estimator. Default ``'multitaper'``.
        n_tapers: [integer, optional] Tapers for the multitaper estimator. Default ``5``.
        time_bandwidth: [number, optional] Time-bandwidth product. Default ``4.0``.
        nperseg: [integer, optional] Segment length for Welch.
        ar_order: [integer, optional] Order for the parametric estimator.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fd_spectral_estimate: not implemented."
    )
