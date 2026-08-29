# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``stochastic_volatility_models`` -- method card #346.

#346 Stochastic-volatility models: Heston, log-normal SV and rough volatility, with calibration

Category 40-option-implied-derivatives; module ``stochastic_volatility_models``.

Reference implementation: stochvolmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c40_option_implied_derivatives import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "opt_sv_calibrate",
    "opt_sv_price",
    "opt_sv_simulate",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def opt_sv_calibrate(
    *,
    strikes: pd.Series,
    expiries: pd.Series,
    implied_vols: pd.Series,
    forward: pd.Series,
    model: Literal["heston", "lognormal_sv", "rough_bergomi", "sabr"] | None = None,
    n_starts: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``opt_sv_calibrate`` -- method card #346.

    Stochastic-volatility models: Heston, log-normal SV and rough volatility, with calibration.

    Category 40-option-implied-derivatives; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        strikes: [series_handle, required] Strikes.
        expiries: [series_handle, required] Times to expiry in years.
        implied_vols: [series_handle, required] Quoted implied volatilities.
        forward: [series_handle, required] Forward price per expiry.
        model: [enum, optional] Model family. Default ``'heston'``.
        n_starts: [integer, optional] Multi-start restarts for the calibration. Default ``5``.
        seed: [integer, optional] Seed for the random number generator.

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
        "opt_sv_calibrate: not implemented."
    )


def opt_sv_price(
    *,
    model: Any,
    strikes: Sequence[float],
    expiries: Sequence[float],
) -> dict[str, Any]:
    """Node ``opt_sv_price`` -- method card #346.

    Stochastic-volatility models: Heston, log-normal SV and rough volatility, with calibration.

    Category 40-option-implied-derivatives; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a calibrated model.
        strikes: [num_array, required] Strikes to price.
        expiries: [num_array, required] Expiries to price.

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
        "opt_sv_price: not implemented."
    )


def opt_sv_simulate(
    *,
    model: Any,
    n_paths: int | None = None,
    n_steps: int | None = None,
    scheme: Literal["euler", "milstein", "qe", "exact"] | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``opt_sv_simulate`` -- method card #346.

    Stochastic-volatility models: Heston, log-normal SV and rough volatility, with calibration.

    Category 40-option-implied-derivatives; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a calibrated model.
        n_paths: [integer, optional] Number of paths. Default ``10000``.
        n_steps: [integer, optional] Time steps per path. Default ``252``.
        scheme: [enum, optional] Discretisation scheme. Default ``'qe'``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

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
        "opt_sv_simulate: not implemented."
    )
