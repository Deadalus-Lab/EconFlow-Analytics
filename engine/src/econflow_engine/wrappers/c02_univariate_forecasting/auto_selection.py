# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``auto_selection`` -- method card #415.

#415 Automatic family selection and forecaster multiplexing

Category 02-univariate-forecasting; module ``auto_selection``.

Reference implementation: sktime.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c02_univariate_forecasting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "uf_auto_select",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def uf_auto_select(
    *,
    y: pd.Series,
    h: int,
    candidates: Sequence[str] | None = None,
    n_folds: int | None = None,
    metric: Literal["mase", "rmse", "mae", "smape", "rmsse"] | None = None,
    season_length: int | None = None,
) -> dict[str, Any]:
    """Node ``uf_auto_select`` -- method card #415.

    Automatic family selection and forecaster multiplexing.

    Category 02-univariate-forecasting; memory class ``light``.

    Args:
        y: [series_handle, required] Series to forecast.
        h: [integer, required] Forecast horizon.
        candidates: [series_codes, optional] Candidate families; omitted = the standard set.
        n_folds: [integer, optional] Cross-validation folds. Default ``5``.
        metric: [enum, optional] Selection metric. Default ``'mase'``.
        season_length: [integer, optional] Seasonal period. Default ``1``.

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
        "uf_auto_select: not implemented."
    )
