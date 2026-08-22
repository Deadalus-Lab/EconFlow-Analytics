# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``panel_standard_errors`` -- method card #464.

#464 Driscoll-Kraay, two-way and multiway clustered standard errors

Category 08-panel-data; module ``panel_standard_errors``.

Reference implementation: pyfixest.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from econflow_engine.generated.args.c08_panel_data import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pd_panel_vcov",
    "NODE_META",
    "wire_model",
]


def pd_panel_vcov(
    *,
    fit: Any,
    estimators: Sequence[str] | None = None,
    cluster: Sequence[str] | None = None,
    bandwidth: int | None = None,
) -> dict[str, Any]:
    """Node ``pd_panel_vcov`` -- method card #464.

    Driscoll-Kraay, two-way and multiway clustered standard errors.

    Category 08-panel-data; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted panel model.
        estimators: [series_codes, optional] Estimators to compute; omitted = the standard set.
        cluster: [series_codes, optional] Clustering variables.
        bandwidth: [integer, optional] Lag truncation for Driscoll-Kraay.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pd_panel_vcov: not implemented."
    )
