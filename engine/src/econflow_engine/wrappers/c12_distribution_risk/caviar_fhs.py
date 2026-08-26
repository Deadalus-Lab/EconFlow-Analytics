# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``caviar_fhs`` -- method card #492.

#492 CAViaR and filtered historical simulation

Category 12-distribution-risk; module ``caviar_fhs``.

Reference implementation: 10.1198/073500104000000370.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c12_distribution_risk import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "dr_caviar",
    "dr_filtered_historical_simulation",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def dr_caviar(
    *,
    returns: pd.Series,
    confidence: float | None = None,
    specification: (
        Literal[
            "adaptive",
            "symmetric_absolute",
            "asymmetric_slope",
            "igarch",
        ]
        | None
    ) = None,
    n_starts: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``dr_caviar`` -- method card #492.

    CAViaR and filtered historical simulation.

    Category 12-distribution-risk; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        returns: [series_handle, required] Return series.
        confidence: [number, optional] Tail level. Default ``0.99``.
        specification: [enum, optional] CAViaR specification. Default ``'asymmetric_slope'``.
        n_starts: [integer, optional] Optimiser restarts. Default ``10``.
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
        "dr_caviar: not implemented."
    )


def dr_filtered_historical_simulation(
    *,
    returns: pd.Series,
    confidence: float | None = None,
    volatility_model: Literal["garch", "egarch", "gjr", "ewma"] | None = None,
    horizon: int | None = None,
    n_simulations: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``dr_filtered_historical_simulation`` -- method card #492.

    CAViaR and filtered historical simulation.

    Category 12-distribution-risk; memory class ``light``.

    Args:
        returns: [series_handle, required] Return series.
        confidence: [number, optional] Tail level. Default ``0.99``.
        volatility_model: [enum, optional] Volatility filter. Default ``'garch'``.
        horizon: [integer, optional] Forecast horizon. Default ``1``.
        n_simulations: [integer, optional] Simulation draws. Default ``10000``.
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
        "dr_filtered_historical_simulation: not implemented."
    )
