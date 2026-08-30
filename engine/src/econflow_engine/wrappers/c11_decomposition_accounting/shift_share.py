# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``shift_share`` -- method card #488.

#488 Shift-share regional growth decomposition

Category 11-decomposition-accounting; module ``shift_share``.

Reference implementation: pandas.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from econflow_engine.generated.args.c11_decomposition_accounting import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "da_shift_share",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def da_shift_share(
    *,
    data: pd.DataFrame,
    region: str,
    industry: str,
    value: str,
    time: str,
    dynamic: bool | None = None,
) -> dict[str, Any]:
    """Node ``da_shift_share`` -- method card #488.

    Shift-share regional growth decomposition.

    Category 11-decomposition-accounting; memory class ``light``.

    Args:
        data: [df_handle, required] Region-by-industry employment or output.
        region: [string, required] Region identifier.
        industry: [string, required] Industry identifier.
        value: [string, required] Value column.
        time: [string, required] Period identifier.
        dynamic: [boolean, optional] Update weights over time. Default ``False``.

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
        "da_shift_share: not implemented."
    )
