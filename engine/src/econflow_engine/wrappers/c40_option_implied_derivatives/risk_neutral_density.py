# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``risk_neutral_density`` -- method card #342.

#342 Risk-neutral density extraction by Breeden-Litzenberger

Category 40-option-implied-derivatives; module ``risk_neutral_density``.

Reference implementation: scipy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c40_option_implied_derivatives import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "opt_risk_neutral_density",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def opt_risk_neutral_density(
    *,
    strikes: pd.Series,
    prices: pd.Series,
    forward: float,
    time_to_expiry: float,
    rate: float,
    smoothing: Literal["none", "spline", "svi", "kernel"] | None = None,
    grid_size: int | None = None,
) -> dict[str, Any]:
    """Node ``opt_risk_neutral_density`` -- method card #342.

    Risk-neutral density extraction by Breeden-Litzenberger.

    Category 40-option-implied-derivatives; memory class ``light``.

    Args:
        strikes: [series_handle, required] Strikes.
        prices: [series_handle, required] Option prices or implied volatilities.
        forward: [number, required] Forward price.
        time_to_expiry: [number, required] Time to expiry in years.
        rate: [number, required] Risk-free rate.
        smoothing: [enum, optional] Smoothing applied before differentiation. Default ``'svi'``.
        grid_size: [integer, optional] Density grid points. Default ``500``.

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
        "opt_risk_neutral_density: not implemented."
    )
