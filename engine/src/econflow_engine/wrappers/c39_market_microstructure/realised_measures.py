# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``realised_measures`` -- method card #337.

#337 Noise-robust realised measures: two-scale, kernel and pre-averaged

Category 39-market-microstructure; module ``realised_measures``.

Reference implementation: 10.3982/ECTA6495.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c39_market_microstructure import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ms_noise_variance",
    "ms_realised_variance",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ms_realised_variance(
    *,
    prices: pd.Series,
    estimator: (
        Literal[
            "naive",
            "sparse",
            "two_scale",
            "multi_scale",
            "kernel",
            "pre_averaged",
        ]
        | None
    ) = None,
    sampling: Literal["calendar", "tick", "business"] | None = None,
    interval: int | None = None,
) -> dict[str, Any]:
    """Node ``ms_realised_variance`` -- method card #337.

    Noise-robust realised measures: two-scale, kernel and pre-averaged.

    Category 39-market-microstructure; memory class ``light``.

    Args:
        prices: [irregular_series_handle, required] Intraday price series with timestamps.
        estimator: [enum, optional] Estimator construction. Default ``'kernel'``.
        sampling: [enum, optional] Sampling scheme. Default ``'calendar'``.
        interval: [integer, optional] Sampling interval in seconds. Default ``300``.

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
        "ms_realised_variance: not implemented."
    )


def ms_noise_variance(
    *,
    prices: pd.Series,
) -> dict[str, Any]:
    """Node ``ms_noise_variance`` -- method card #337.

    Noise-robust realised measures: two-scale, kernel and pre-averaged.

    Category 39-market-microstructure; memory class ``light``.

    Args:
        prices: [irregular_series_handle, required] Intraday price series.

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
        "ms_noise_variance: not implemented."
    )
