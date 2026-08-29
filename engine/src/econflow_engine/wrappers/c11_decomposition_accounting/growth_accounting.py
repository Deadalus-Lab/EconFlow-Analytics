# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``growth_accounting`` -- method card #484.

#484 Growth accounting and Tornqvist-Divisia total factor productivity

Category 11-decomposition-accounting; module ``growth_accounting``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c11_decomposition_accounting import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "da_growth_accounting",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def da_growth_accounting(
    *,
    output: pd.Series,
    inputs: pd.DataFrame,
    shares: pd.DataFrame | None = None,
    index: Literal["tornqvist", "divisia", "laspeyres", "fixed_share"] | None = None,
) -> dict[str, Any]:
    """Node ``da_growth_accounting`` -- method card #484.

    Growth accounting and Tornqvist-Divisia total factor productivity.

    Category 11-decomposition-accounting; memory class ``light``.

    Args:
        output: [series_handle, required] Output series.
        inputs: [multiseries_handle, required] Input series, one column each.
        shares: [multiseries_handle, optional] Factor shares; omitted = estimated from cost data.
        index: [enum, optional] Index form. Default ``'tornqvist'``.

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
        "da_growth_accounting: not implemented."
    )
