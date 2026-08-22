# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``benchmarking_high_frequency`` -- method card #115.

#115 Benchmarking a high-frequency indicator to a low-frequency total (two-step Prais-Winsten
    regression + additive Denton smoothing)

Category 00-data-utilities; module ``benchmarking_high_frequency``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "bench_annual",
    "bench_in_sample",
    "bench_two_steps",
    "NODE_META",
    "wire_model",
]


def bench_two_steps(
    *,
    hfserie: pd.Series,
    lfserie: pd.Series,
    include_differenciation: bool | None = None,
    include_rho: bool | None = None,
    set_coeff: float | None = None,
) -> dict[str, Any]:
    """Node ``bench_two_steps`` -- method card #115.

    Benchmarking a high-frequency indicator to a low-frequency total (two-step Prais-Winsten
    regression + additive Denton smoothing).

    Category 00-data-utilities; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        hfserie: [series_handle, required] Handle to a high-frequency indicator (ts); its frequency
            must be STRICTLY higher than and an integer multiple of lfserie.
        lfserie: [series_handle, required] Handle to the low-frequency target aggregate (ts, NO NA);
            the benchmarked total sums exactly to it within the window.
        include_differenciation: [boolean, optional] Difference lf/hf before the regression (default
            False). Default ``False``.
        include_rho: [boolean, optional] Prais-Winsten AR(1) on the residuals (default False).
            Default ``False``.
        set_coeff: [number, optional] Optionally fix the indicator coefficient instead of estimating
            it (finite number).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bench_two_steps: not implemented."
    )


def bench_annual(
    *,
    hfserie: pd.Series,
    lfserie: pd.Series,
    include_differenciation: bool | None = None,
    include_rho: bool | None = None,
    set_coeff: float | None = None,
) -> dict[str, Any]:
    """Node ``bench_annual`` -- method card #115.

    Benchmarking a high-frequency indicator to a low-frequency total (two-step Prais-Winsten
    regression + additive Denton smoothing).

    Category 00-data-utilities; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        hfserie: [series_handle, required] Handle to a high-frequency indicator (ts);
            annualBenchmark = default quarterly national-accounts windows.
        lfserie: [series_handle, required] Handle to the annual target aggregate (ts, NO NA).
        include_differenciation: [boolean, optional] Difference lf/hf before the regression (default
            False). Default ``False``.
        include_rho: [boolean, optional] Prais-Winsten AR(1) on the residuals (default False).
            Default ``False``.
        set_coeff: [number, optional] Optionally fix the indicator coefficient instead of estimating
            it (finite number).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bench_annual: not implemented."
    )


def bench_in_sample(
    *,
    object: Any,
    type: Literal["changes", "levels"] | None = None,
) -> dict[str, Any]:
    """Node ``bench_in_sample`` -- method card #115.

    Benchmarking a high-frequency indicator to a low-frequency total (two-step Prais-Winsten
    regression + additive Denton smoothing).

    Category 00-data-utilities; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fitted 'twoStepsBenchmark' (from bench_two_steps
            / bench_annual).
        type: [enum, optional] In-sample response-vs-prediction comparison in changes (default) or
            levels.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bench_in_sample: not implemented."
    )
