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
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c44_environment_energy_climate import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "env_decompose_index",
    "NODE_META",
    "wire_model",
]


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
    """
    raise NotImplementedError(
        "env_decompose_index: not implemented."
    )
