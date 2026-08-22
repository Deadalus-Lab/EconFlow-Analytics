# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``granger_networks`` -- method card #555.

#555 Granger-causality networks and topology measures

Category 21-systemic-risk; module ``granger_networks``.

Reference implementation: networkx.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c21_systemic_risk import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "sr_granger_network",
    "sr_network_topology",
    "NODE_META",
    "wire_model",
]


def sr_granger_network(
    *,
    returns: pd.DataFrame,
    lags: int | None = None,
    adjust: Literal["none", "bonferroni", "holm", "fdr"] | None = None,
    window: int | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``sr_granger_network`` -- method card #555.

    Granger-causality networks and topology measures.

    Category 21-systemic-risk; memory class ``light``.

    Args:
        returns: [df_handle, required] Institution return panel.
        lags: [integer, optional] Lag order for the pairwise tests. Default ``1``.
        adjust: [enum, optional] Multiplicity adjustment. Default ``'fdr'``.
        window: [integer, optional] Rolling window; omitted = full sample.
        alpha: [number, optional] Significance level. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sr_granger_network: not implemented."
    )


def sr_network_topology(
    *,
    adjacency: np.ndarray,
    measures: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``sr_network_topology`` -- method card #555.

    Granger-causality networks and topology measures.

    Category 21-systemic-risk; memory class ``light``.

    Args:
        adjacency: [matrix_handle, required] Directed adjacency matrix.
        measures: [series_codes, optional] Measures to compute; omitted = the standard set.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sr_network_topology: not implemented."
    )
