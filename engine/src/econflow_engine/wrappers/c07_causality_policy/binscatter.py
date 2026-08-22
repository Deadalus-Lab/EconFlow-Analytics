# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``binscatter`` -- method card #448.

#448 Binscatter with valid inference

Category 07-causality-policy; module ``binscatter``.

Reference implementation: binsreg.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cp_binscatter",
    "NODE_META",
    "wire_model",
]


def cp_binscatter(
    *,
    y: pd.Series,
    x: pd.Series,
    covariates: Sequence[str] | None = None,
    n_bins: int | None = None,
    polynomial: int | None = None,
    shape_test: Literal["none", "linearity", "monotonicity", "concavity"] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``cp_binscatter`` -- method card #448.

    Binscatter with valid inference.

    Category 07-causality-policy; memory class ``light``.

    Args:
        y: [series_handle, required] Outcome.
        x: [series_handle, required] Running variable.
        covariates: [series_codes, optional] Covariates to residualise on.
        n_bins: [integer, optional] Number of bins; omitted = data-driven.
        polynomial: [integer, optional] Polynomial degree fitted within bins. Default ``0``.
        shape_test: [enum, optional] Shape restriction to test. Default ``'none'``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cp_binscatter: not implemented."
    )
