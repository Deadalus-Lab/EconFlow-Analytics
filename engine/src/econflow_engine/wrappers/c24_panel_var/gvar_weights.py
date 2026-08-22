# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``gvar_weights`` -- method card #573.

#573 Trade-weighted foreign variables for a global VAR

Category 24-panel-var; module ``gvar_weights``.

Reference implementation: pandas.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c24_panel_var import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pv_gvar_weights",
    "NODE_META",
    "wire_model",
]


def pv_gvar_weights(
    *,
    data: pd.DataFrame,
    weights: np.ndarray,
    country: str,
    time: str,
    variables: Sequence[str] | None = None,
    time_varying: bool | None = None,
    normalise: bool | None = None,
) -> dict[str, Any]:
    """Node ``pv_gvar_weights`` -- method card #573.

    Trade-weighted foreign variables for a global VAR.

    Category 24-panel-var; memory class ``light``.

    Args:
        data: [df_handle, required] Country panel of variables.
        weights: [matrix_handle, required] Bilateral weight matrix.
        country: [string, required] Country identifier.
        time: [string, required] Time identifier.
        variables: [series_codes, optional] Variables to build foreign counterparts for.
        time_varying: [boolean, optional] Use period-specific weights. Default ``False``.
        normalise: [boolean, optional] Row-normalise with a zero diagonal. Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pv_gvar_weights: not implemented."
    )
