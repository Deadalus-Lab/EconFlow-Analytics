# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``debt_fan_charts`` -- method card #356.

#356 Stochastic debt fan charts from a joint shock distribution

Category 42-fiscal-debt-sustainability; module ``debt_fan_charts``.

Reference implementation: 10.2307/30035919.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c42_fiscal_debt_sustainability import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "fis_debt_fan_chart",
    "fis_threshold_probability",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def fis_debt_fan_chart(
    *,
    debt_ratio_initial: float,
    history: pd.DataFrame,
    horizon: int | None = None,
    n_simulations: int | None = None,
    method: Literal["bootstrap", "block_bootstrap", "normal", "var"] | None = None,
    quantiles: Sequence[float] | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``fis_debt_fan_chart`` -- method card #356.

    Stochastic debt fan charts from a joint shock distribution.

    Category 42-fiscal-debt-sustainability; memory class ``light``.

    Args:
        debt_ratio_initial: [number, required] Starting debt ratio.
        history: [df_handle, required] Historical growth, interest rate and primary balance.
        horizon: [integer, optional] Projection horizon in periods. Default ``10``.
        n_simulations: [integer, optional] Simulation draws. Default ``10000``.
        method: [enum, optional] Shock generation. Default ``'bootstrap'``.
        quantiles: [num_array, optional] Fan quantiles. Default ``[0.1, 0.25, 0.5, 0.75, 0.9]``.
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
        "fis_debt_fan_chart: not implemented."
    )


def fis_threshold_probability(
    *,
    fan: Any,
    threshold: float,
) -> dict[str, Any]:
    """Node ``fis_threshold_probability`` -- method card #356.

    Stochastic debt fan charts from a joint shock distribution.

    Category 42-fiscal-debt-sustainability; memory class ``light``.

    Args:
        fan: [raw_handle, required] Handle to a stochastic projection.
        threshold: [number, required] Debt ratio threshold.

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
        "fis_threshold_probability: not implemented."
    )
