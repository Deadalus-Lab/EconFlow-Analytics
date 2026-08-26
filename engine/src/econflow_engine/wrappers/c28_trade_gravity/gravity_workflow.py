# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``gravity_workflow`` -- method card #594.

#594 Gravity data assembly and estimation workflow

Category 28-trade-gravity; module ``gravity_workflow``.

Reference implementation: gme.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c28_trade_gravity import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tg_gravity_panel",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def tg_gravity_panel(
    *,
    trade: pd.DataFrame,
    covariates: pd.DataFrame | None = None,
    exporter: str,
    importer: str,
    time: str,
    estimator: Literal["ppml", "ols_log", "gpml", "heckman"] | None = None,
    fixed_effects: Literal["none", "exporter_importer", "three_way"] | None = None,
    include_intranational: bool | None = None,
    cluster: Literal["pair", "exporter", "importer", "none"] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``tg_gravity_panel`` -- method card #594.

    Gravity data assembly and estimation workflow.

    Category 28-trade-gravity; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        trade: [df_handle, required] Bilateral trade flows.
        covariates: [df_handle, optional] Bilateral covariates such as distance and borders.
        exporter: [string, required] Exporter identifier.
        importer: [string, required] Importer identifier.
        time: [string, required] Time identifier.
        estimator: [enum, optional] Estimator. Default ``'ppml'``.
        fixed_effects: [enum, optional] Fixed-effect structure. Default ``'three_way'``.
        include_intranational: [boolean, optional] Include intra-national trade. Default ``False``.
        cluster: [enum, optional] Clustering. Default ``'pair'``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

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
        "tg_gravity_panel: not implemented."
    )
