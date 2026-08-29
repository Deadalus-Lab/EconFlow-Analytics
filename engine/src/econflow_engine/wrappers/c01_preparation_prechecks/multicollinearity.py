# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``multicollinearity`` -- method card #397.

#397 Multicollinearity: variance inflation, tolerance and Belsley condition indices

Category 01-preparation-prechecks; module ``multicollinearity``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pp_condition_indices",
    "pp_vif",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pp_vif(
    *,
    x: pd.DataFrame,
    threshold: float | None = None,
) -> dict[str, Any]:
    """Node ``pp_vif`` -- method card #397.

    Multicollinearity: variance inflation, tolerance and Belsley condition indices.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [df_handle, required] Regressor table.
        threshold: [number, optional] VIF above which a regressor is flagged. Default ``10.0``.

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
        "pp_vif: not implemented."
    )


def pp_condition_indices(
    *,
    x: pd.DataFrame,
    scale: bool | None = None,
    threshold: float | None = None,
) -> dict[str, Any]:
    """Node ``pp_condition_indices`` -- method card #397.

    Multicollinearity: variance inflation, tolerance and Belsley condition indices.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [df_handle, required] Regressor table.
        scale: [boolean, optional] Scale columns to unit length first. Default ``True``.
        threshold: [number, optional] Condition index above which a dependency is flagged. Default
            ``30.0``.

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
        "pp_condition_indices: not implemented."
    )
