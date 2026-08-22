# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bandwidth_selection`` -- method card #284.

#284 Bandwidth selection: cross-validation, plug-in and rule of thumb

Category 33-nonparametric-semiparametric; module ``bandwidth_selection``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c33_nonparametric_semiparametric import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "np_bandwidth_select",
    "NODE_META",
    "wire_model",
]


def np_bandwidth_select(
    *,
    x: pd.DataFrame,
    y: pd.Series | None = None,
    method: Literal["cv_ls", "cv_ml", "plug_in", "silverman", "scott"] | None = None,
    var_type: str | None = None,
) -> dict[str, Any]:
    """Node ``np_bandwidth_select`` -- method card #284.

    Bandwidth selection: cross-validation, plug-in and rule of thumb.

    Category 33-nonparametric-semiparametric; memory class ``light``.

    Args:
        x: [multiseries_handle, required] Data the bandwidth is chosen for.
        y: [series_handle, optional] Dependent variable when the target is a regression.
        method: [enum, optional] Selection rule. Default ``'cv_ls'``.
        var_type: [string, optional] One character per covariate: c, o or u.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "np_bandwidth_select: not implemented."
    )
