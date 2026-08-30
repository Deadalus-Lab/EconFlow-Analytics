# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``ge_gravity`` -- method card #593.

#593 General-equilibrium structural gravity counterfactuals

Category 28-trade-gravity; module ``ge_gravity``.

Reference implementation: gegravity.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from econflow_engine.generated.args.c28_trade_gravity import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tg_ge_gravity",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def tg_ge_gravity(
    *,
    data: pd.DataFrame,
    exporter: str,
    importer: str,
    trade: str,
    counterfactual: pd.DataFrame,
    elasticity: float,
    tol: float | None = None,
) -> dict[str, Any]:
    """Node ``tg_ge_gravity`` -- method card #593.

    General-equilibrium structural gravity counterfactuals.

    Category 28-trade-gravity; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Bilateral trade panel with expenditure and production.
        exporter: [string, required] Exporter identifier.
        importer: [string, required] Importer identifier.
        trade: [string, required] Trade flow column.
        counterfactual: [df_handle, required] Counterfactual policy variables.
        elasticity: [number, required] Trade elasticity.
        tol: [number, optional] Equilibrium tolerance. Default ``1e-10``.

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
        "tg_ge_gravity: not implemented."
    )
