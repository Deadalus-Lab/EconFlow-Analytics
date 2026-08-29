# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``long_memory`` -- method card #400.

#400 Long memory: Hurst exponent, rescaled range, detrended fluctuation and variance ratio

Category 01-preparation-prechecks; module ``long_memory``.

Reference implementation: nolds.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pp_hurst",
    "pp_variance_ratio",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pp_hurst(
    *,
    x: pd.Series,
    method: Literal["rs", "dfa", "aggregated_variance", "periodogram"] | None = None,
    min_scale: int | None = None,
    max_scale: int | None = None,
) -> dict[str, Any]:
    """Node ``pp_hurst`` -- method card #400.

    Long memory: Hurst exponent, rescaled range, detrended fluctuation and variance ratio.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Series.
        method: [enum, optional] Estimator. Default ``'dfa'``.
        min_scale: [integer, optional] Smallest scale used. Default ``10``.
        max_scale: [integer, optional] Largest scale used; omitted = a quarter of the sample.

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
        "pp_hurst: not implemented."
    )


def pp_variance_ratio(
    *,
    x: pd.Series,
    horizons: Sequence[int] | None = None,
    robust: bool | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``pp_variance_ratio`` -- method card #400.

    Long memory: Hurst exponent, rescaled range, detrended fluctuation and variance ratio.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Series, usually in log levels.
        horizons: [int_array, optional] Aggregation horizons. Default ``[2, 4, 8, 16]``.
        robust: [boolean, optional] Use the heteroskedasticity-robust statistic. Default ``True``.
        alpha: [number, optional] Significance level. Default ``0.05``.

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
        "pp_variance_ratio: not implemented."
    )
