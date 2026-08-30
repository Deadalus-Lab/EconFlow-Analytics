# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``beck_katz_panel`` -- method card #174.

#174 Beck-Katz Panel-Corrected Standard Errors (PCSE) for pooled TSCS/OLS

Category 08-panel-data; module ``beck_katz_panel``.

Reference implementation: 10.2307/2082979.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

import pandas as pd

from econflow_engine.generated.args.c08_panel_data import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pcse_fit",
    "pcse_summary",
    "pcse_vcov",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pcse_fit(
    *,
    formula: str,
    data: pd.DataFrame,
    groupN: str,
    groupT: str,
    pairwise: bool | None = None,
) -> dict[str, Any]:
    """Node ``pcse_fit`` -- method card #174.

    Beck-Katz Panel-Corrected Standard Errors (PCSE) for pooled TSCS/OLS.

    Category 08-panel-data; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] Pooled TSCS formula, e.g. 'y ~ x1 + x2' (OLS is estimated
            internally).
        data: [df_handle, required] Handle to a pooled panel DataFrame (one row per unit-time).
        groupN: [string, required] Column name of the cross-section (unit) index.
        groupT: [string, required] Column name of the time index.
        pairwise: [boolean, optional] False=casewise (balanced rectangle), True=pairwise
            (unbalanced). Default ``False``.

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
        "pcse_fit: not implemented."
    )


def pcse_vcov(
    *,
    object: Any,
    groupN: Sequence[float],
    groupT: Sequence[float],
    pairwise: bool | None = None,
) -> dict[str, Any]:
    """Node ``pcse_vcov`` -- method card #174.

    Beck-Katz Panel-Corrected Standard Errors (PCSE) for pooled TSCS/OLS.

    Category 08-panel-data; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        object: [raw_handle, required] Handle to an already-estimated 'lm' (pooled OLS) for PCSE
            correction.
        groupN: [num_array, required] Numeric vector of the cross-section (unit) index, of length
            nobs.
        groupT: [num_array, required] Numeric vector of the time index, of length nobs.
        pairwise: [boolean, optional] False=casewise, True=pairwise (unbalanced panels). Default
            ``False``.

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
        "pcse_vcov: not implemented."
    )


def pcse_summary(
    *,
    object: Any,
) -> dict[str, Any]:
    """Node ``pcse_summary`` -- method card #174.

    Beck-Katz Panel-Corrected Standard Errors (PCSE) for pooled TSCS/OLS.

    Category 08-panel-data; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a 'pcse' object (from pcse_fit/pcse_vcov $object).

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
        "pcse_summary: not implemented."
    )
