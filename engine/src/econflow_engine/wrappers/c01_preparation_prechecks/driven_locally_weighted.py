# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``driven_locally_weighted`` -- METHOD-SELECTION card #127.

#127 Data-driven locally-weighted regression decomposition of seasonality/trend (IPI optimal
    bandwidth) under short memory

Category 01-preparation-prechecks; module ``driven_locally_weighted``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "des_deseats",
    "NODE_META",
    "wire_model",
]


def des_deseats(
    *,
    y: pd.Series,
    order_poly: Literal["1", "3"] | None = None,
    kernel_fun: Literal["epanechnikov", "uniform", "bisquare", "triweight"] | None = None,
    inflation_rate: Literal["optimal", "naive"] | None = None,
    autocor: bool | None = None,
) -> dict[str, Any]:
    """Node ``des_deseats`` -- METHOD-SELECTION card #127.

    Data-driven locally-weighted regression decomposition of seasonality/trend (IPI optimal
    bandwidth) under short memory.

    Category 01-preparation-prechecks; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Handle to an equally spaced seasonal univariate ts (frequency >
            1, no NA, >= 2 full cycles).
        order_poly: [enum, optional] Order of the local trend polynomial: 1=local linear, 3=local
            cubic (default 3). Default ``3``.
        kernel_fun: [enum, optional] Second-order weighting kernel (default epanechnikov). Default
            ``'epanechnikov'``.
        inflation_rate: [enum, optional] Inflation rate in the IPI bandwidth selection (default
            optimal). Default ``'optimal'``.
        autocor: [boolean, optional] Short-memory autocorrelated errors (True, default) or i.i.d.
            (False). Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "des_deseats: not implemented. The method card is in ./README.md."
    )
