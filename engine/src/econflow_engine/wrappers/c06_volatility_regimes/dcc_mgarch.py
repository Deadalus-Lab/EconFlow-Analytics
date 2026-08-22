# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``dcc_mgarch`` -- method card #29.

#29 DCC-MGARCH (multivariate)

Category 06-volatility-regimes; module ``dcc_mgarch``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c06_volatility_regimes import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "dcc_fit",
    "dcc_forecast",
    "dcc_multispec",
    "dcc_roll",
    "dcc_sim",
    "dcc_spec",
    "NODE_META",
    "wire_model",
]


def dcc_multispec(
    *,
    specs: Sequence[Any],
) -> dict[str, Any]:
    """Node ``dcc_multispec`` -- method card #29.

    DCC-MGARCH (multivariate).

    Category 06-volatility-regimes; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        specs: [raw_handle_array, required] Array of handles to 'uGARCHspec' objects (output of
            ga_spec.object) — one per asset, AT LEAST 2.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dcc_multispec: not implemented."
    )


def dcc_spec(
    *,
    uspec: Any,
    model: Literal["DCC", "aDCC", "FDCC"] | None = None,
    distribution: Literal["mvnorm", "mvt", "mvlaplace"] | None = None,
    VAR: bool | None = None,
    lag: int | None = None,
) -> dict[str, Any]:
    """Node ``dcc_spec`` -- method card #29.

    DCC-MGARCH (multivariate).

    Category 06-volatility-regimes; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        uspec: [raw_handle, required] Handle to a 'uGARCHmultispec' (from dcc_multispec).
        model: [enum, optional] DCC model (default DCC· aDCC=asymmetric).
        distribution: [enum, optional] Multivariate distribution (default mvnorm).
        VAR: [boolean, optional] VAR filter on the conditional mean (default False). Default
            ``False``.
        lag: [integer, optional] VAR lag order when VAR=True (default 1). Default ``1``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dcc_spec: not implemented."
    )


def dcc_fit(
    *,
    spec: Any,
    data: np.ndarray,
    out_sample: int | None = None,
    solver: Literal["solnp", "nlminb", "lbfgs", "gosolnp"] | None = None,
) -> dict[str, Any]:
    """Node ``dcc_fit`` -- method card #29.

    DCC-MGARCH (multivariate).

    Category 06-volatility-regimes; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        spec: [raw_handle, required] Handle to a 'DCCspec' (from dcc_spec).
        data: [matrix_handle, required] Handle to a multivariate numeric matrix (>=2 columns,
            without NA).
        out_sample: [integer, optional] Out-of-sample observations (default 0). Default ``0``.
        solver: [enum, optional] Optimizer (default solnp).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dcc_fit: not implemented."
    )


def dcc_forecast(
    *,
    fit: Any,
    n_ahead: int | None = None,
    n_roll: int | None = None,
) -> dict[str, Any]:
    """Node ``dcc_forecast`` -- method card #29.

    DCC-MGARCH (multivariate).

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a 'DCCfit' (from dcc_fit).
        n_ahead: [integer, optional] Forecast horizon for correlation/covariance (default 1).
            Default ``1``.
        n_roll: [integer, optional] Rolling forecasts over out.sample (default 0). Default ``0``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dcc_forecast: not implemented."
    )


def dcc_sim(
    *,
    fit: Any,
    n_sim: int | None = None,
    n_start: int | None = None,
    m_sim: int | None = None,
) -> dict[str, Any]:
    """Node ``dcc_sim`` -- method card #29.

    DCC-MGARCH (multivariate).

    Category 06-volatility-regimes; memory class ``heavy``.

    Args:
        fit: [raw_handle, required] Handle to a 'DCCfit' (from dcc_fit).
        n_sim: [integer, optional] Length of each simulated path (default 1000). Default ``1000``.
        n_start: [integer, optional] Burn-in observations (default 0). Default ``0``.
        m_sim: [integer, optional] Number of independent paths (default 1· seeded). Default ``1``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dcc_sim: not implemented."
    )


def dcc_roll(
    *,
    spec: Any,
    data: np.ndarray,
    forecast_length: int | None = None,
    refit_every: int | None = None,
    refit_window: Literal["recursive", "moving"] | None = None,
    solver: Literal["solnp", "nlminb", "lbfgs", "gosolnp"] | None = None,
) -> dict[str, Any]:
    """Node ``dcc_roll`` -- method card #29.

    DCC-MGARCH (multivariate).

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        spec: [raw_handle, required] Handle to a 'DCCspec' (from dcc_spec).
        data: [matrix_handle, required] Handle to a multivariate numeric matrix (>=2 columns).
        forecast_length: [integer, optional] Length of the rolling out-of-sample period (default
            50). Default ``50``.
        refit_every: [integer, optional] Re-estimate every n steps (default 25). Default ``25``.
        refit_window: [enum, optional] Re-estimation window (default recursive).
        solver: [enum, optional] Optimizer (default solnp).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dcc_roll: not implemented."
    )
