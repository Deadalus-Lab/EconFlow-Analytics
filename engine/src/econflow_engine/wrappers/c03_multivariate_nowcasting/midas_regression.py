# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``midas_regression`` -- method card #18.

#18 MIDAS regression (mixed data sampling)

Category 03-multivariate-nowcasting; module ``midas_regression``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

from econflow_engine.generated.args.c03_multivariate_nowcasting import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "md_adequacy_test",
    "md_fit",
    "md_forecast",
    "md_select",
    "NODE_META",
    "wire_model",
]


def md_fit(
    *,
    y: Any,
    x: Any,
    m: int,
    k: int | None = None,
    weight: Literal["nealmon", "nbeta", "almonp"] | None = None,
    poly_degree: int | None = None,
    trend: bool | None = None,
) -> dict[str, Any]:
    """Node ``md_fit`` -- method card #18.

    MIDAS regression (mixed data sampling).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        y: [raw_handle, required] Handle to a low-freq numeric vector (dependent).
        x: [raw_handle, required] Handle to a high-freq numeric vector (length = m*length(y)).
        m: [integer, required] Frequency ratio (high:low, e.g. 3 for monthly->quarterly).
        k: [integer, optional] Maximum high-freq lag (default 7). Default ``7``.
        weight: [enum, optional] MIDAS weight scheme (default nealmon = exponential Almon).
        poly_degree: [integer, optional] Polynomial degree for weight='almonp' (default 2). Default
            ``2``.
        trend: [boolean, optional] Include a linear trend (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "md_fit: not implemented."
    )


def md_adequacy_test(
    *,
    model: Any,
    robust: bool | None = None,
) -> dict[str, Any]:
    """Node ``md_adequacy_test`` -- method card #18.

    MIDAS regression (mixed data sampling).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a midas_r model (from md_fit).
        robust: [boolean, optional] HAC-robust hAhr_test instead of hAh_test (default False).
            Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "md_adequacy_test: not implemented."
    )


def md_forecast(
    *,
    model: Any,
    newx: Any,
    m: int,
) -> dict[str, Any]:
    """Node ``md_forecast`` -- method card #18.

    MIDAS regression (mixed data sampling).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a midas_r model (from md_fit).
        newx: [raw_handle, required] Handle to future high-freq values (length = h*m).
        m: [integer, required] Frequency ratio (same as the fit).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "md_forecast: not implemented."
    )


def md_select(
    *,
    y: Any,
    x: Any,
    m: int,
    k: int | None = None,
    ic: Literal["AIC", "BIC"] | None = None,
    poly_degree: int | None = None,
    trend: bool | None = None,
) -> dict[str, Any]:
    """Node ``md_select`` -- method card #18.

    MIDAS regression (mixed data sampling).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        y: [raw_handle, required] Handle to a low-freq numeric vector (dependent).
        x: [raw_handle, required] Handle to a high-freq numeric vector (length = m*length(y)).
        m: [integer, required] Frequency ratio (high:low).
        k: [integer, optional] Maximum high-freq lag (default 7). Default ``7``.
        ic: [enum, optional] Selection criterion for the weight scheme (default AIC).
        poly_degree: [integer, optional] Polynomial degree for almonp (default 2). Default ``2``.
        trend: [boolean, optional] Include a linear trend (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "md_select: not implemented."
    )
