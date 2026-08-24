# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``gmm_panel_var`` -- method card #569.

#569 Homogeneous GMM panel vector autoregression

Category 24-panel-var; module ``gmm_panel_var``.

Reference implementation: pydynpd.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c24_panel_var import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pv_gmm_panel_var",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pv_gmm_panel_var(
    *,
    data: pd.DataFrame,
    variables: Sequence[str],
    unit: str,
    time: str,
    lags: int | None = None,
    estimator: Literal["difference", "system"] | None = None,
    max_instrument_lags: int | None = None,
    collapse: bool | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``pv_gmm_panel_var`` -- method card #569.

    Homogeneous GMM panel vector autoregression.

    Category 24-panel-var; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Panel data.
        variables: [series_codes, required] Endogenous variables.
        unit: [string, required] Unit identifier.
        time: [string, required] Time identifier.
        lags: [integer, optional] Lag order. Default ``1``.
        estimator: [enum, optional] GMM variant. Default ``'system'``.
        max_instrument_lags: [integer, optional] Maximum lag depth used as instruments. Default
            ``3``.
        collapse: [boolean, optional] Collapse the instrument matrix. Default ``True``.
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
        "pv_gmm_panel_var: not implemented."
    )
