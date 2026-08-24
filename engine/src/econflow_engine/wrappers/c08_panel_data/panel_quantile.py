# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``panel_quantile`` -- method card #462.

#462 Panel quantile regression: Canay and Machado-Santos Silva

Category 08-panel-data; module ``panel_quantile``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c08_panel_data import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pd_panel_quantile",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pd_panel_quantile(
    *,
    data: pd.DataFrame,
    formula: str,
    unit: str,
    time: str,
    quantiles: Sequence[float] | None = None,
    estimator: Literal["canay", "machado_santos_silva", "pooled"] | None = None,
    nboot: int | None = None,
    seed: int,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``pd_panel_quantile`` -- method card #462.

    Panel quantile regression: Canay and Machado-Santos Silva.

    Category 08-panel-data; memory class ``heavy``.

    Args:
        data: [df_handle, required] Panel data.
        formula: [formula, required] Model formula.
        unit: [string, required] Unit identifier.
        time: [string, required] Time identifier.
        quantiles: [num_array, optional] Quantile levels. Default ``[0.1, 0.25, 0.5, 0.75, 0.9]``.
        estimator: [enum, optional] Estimator. Default ``'canay'``.
        nboot: [integer, optional] Number of bootstrap replications. Default ``999``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.
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
        "pd_panel_quantile: not implemented."
    )
