# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``lomb_scargle`` -- method card #592.

#592 Lomb-Scargle periodogram and band-variance shares

Category 27-frequency-domain; module ``lomb_scargle``.

Reference implementation: scipy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c27_frequency_domain import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "fd_band_variance",
    "fd_lomb_scargle",
    "NODE_META",
    "wire_model",
]


def fd_lomb_scargle(
    *,
    x: pd.Series,
    frequencies: Sequence[float] | None = None,
    normalisation: Literal["standard", "model", "log", "psd"] | None = None,
    false_alarm: bool | None = None,
) -> dict[str, Any]:
    """Node ``fd_lomb_scargle`` -- method card #592.

    Lomb-Scargle periodogram and band-variance shares.

    Category 27-frequency-domain; memory class ``light``.

    Args:
        x: [irregular_series_handle, required] Irregularly sampled series with timestamps.
        frequencies: [num_array, optional] Frequency grid; omitted = automatic.
        normalisation: [enum, optional] Power normalisation. Default ``'standard'``.
        false_alarm: [boolean, optional] Compute false-alarm probabilities. Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fd_lomb_scargle: not implemented."
    )


def fd_band_variance(
    *,
    x: pd.Series,
    bands: Sequence[float],
    method: Literal["welch", "multitaper", "periodogram"] | None = None,
) -> dict[str, Any]:
    """Node ``fd_band_variance`` -- method card #592.

    Lomb-Scargle periodogram and band-variance shares.

    Category 27-frequency-domain; memory class ``light``.

    Args:
        x: [series_handle, required] Series.
        bands: [num_array, required] Band edges in cycles per period.
        method: [enum, optional] Spectral estimator. Default ``'welch'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fd_band_variance: not implemented."
    )
