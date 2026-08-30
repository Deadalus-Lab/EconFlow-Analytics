# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``index_decomposition`` -- method card #368.

#368 Index decomposition analysis: Laspeyres, Paasche and log-mean Divisia

Category 44-environment-energy-climate; module ``index_decomposition``.

Reference implementation: pandas.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c44_environment_energy_climate import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "env_decompose_index",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def env_decompose_index(
    *,
    data: pd.DataFrame,
    total: str,
    factors: Sequence[str] | None = None,
    method: Literal["lmdi_i", "lmdi_ii", "laspeyres", "paasche", "fisher"] | None = None,
    form: Literal["additive", "multiplicative"] | None = None,
) -> dict[str, Any]:
    """Node ``env_decompose_index`` -- method card #368.

    Index decomposition analysis: Laspeyres, Paasche and log-mean Divisia.

    Category 44-environment-energy-climate; memory class ``light``.

    Args:
        data: [df_handle, required] Factors by period, one column per driver.
        total: [string, required] Column holding the aggregate being decomposed.
        factors: [series_codes, optional] Driver columns.
        method: [enum, optional] Index form. Default ``'lmdi_i'``.
        form: [enum, optional] Additive or multiplicative decomposition. Default ``'additive'``.

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
        "env_decompose_index: not implemented."
    )
