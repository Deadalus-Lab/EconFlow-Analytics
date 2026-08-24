# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``akm_two_way`` -- method card #468.

#468 Two-way fixed effects for matched employer-employee data (AKM)

Category 08-panel-data; module ``akm_two_way``.

Reference implementation: pytwoway.

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
    "pd_akm",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pd_akm(
    *,
    data: pd.DataFrame,
    outcome: str,
    worker: str,
    firm: str,
    time: str,
    controls: Sequence[str] | None = None,
    bias_correction: Literal["none", "kss", "andrews"] | None = None,
) -> dict[str, Any]:
    """Node ``pd_akm`` -- method card #468.

    Two-way fixed effects for matched employer-employee data (AKM).

    Category 08-panel-data; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Matched employer-employee panel.
        outcome: [string, required] Outcome column, usually log pay.
        worker: [string, required] Worker identifier.
        firm: [string, required] Firm identifier.
        time: [string, required] Time identifier.
        controls: [series_codes, optional] Additional control columns.
        bias_correction: [enum, optional] Limited-mobility bias correction. Default ``'none'``.

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
        "pd_akm: not implemented."
    )
