# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``auto_orders`` -- method card #398.

#398 Automatic seasonal-period detection and differencing orders

Category 01-preparation-prechecks; module ``auto_orders``.

Reference implementation: statsforecast.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pp_auto_differencing",
    "pp_detect_period",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pp_detect_period(
    *,
    x: pd.Series,
    max_period: int | None = None,
    method: Literal["acf", "spectral", "seasonal_strength"] | None = None,
    threshold: float | None = None,
) -> dict[str, Any]:
    """Node ``pp_detect_period`` -- method card #398.

    Automatic seasonal-period detection and differencing orders.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Series.
        max_period: [integer, optional] Largest period considered. Default ``365``.
        method: [enum, optional] Detection method. Default ``'acf'``.
        threshold: [number, optional] Strength above which a period is accepted. Default ``0.64``.

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
        "pp_detect_period: not implemented."
    )


def pp_auto_differencing(
    *,
    x: pd.Series,
    period: int | None = None,
    test: Literal["kpss", "adf", "pp"] | None = None,
    seasonal_test: Literal["ocsb", "ch", "hegy"] | None = None,
    max_d: int | None = None,
    max_D: int | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``pp_auto_differencing`` -- method card #398.

    Automatic seasonal-period detection and differencing orders.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Series.
        period: [integer, optional] Seasonal period; omitted = detected.
        test: [enum, optional] Unit-root test driving the choice. Default ``'kpss'``.
        seasonal_test: [enum, optional] Seasonal test. Default ``'ocsb'``.
        max_d: [integer, optional] Maximum non-seasonal differences. Default ``2``.
        max_D: [integer, optional] Maximum seasonal differences. Default ``1``.
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
        "pp_auto_differencing: not implemented."
    )
