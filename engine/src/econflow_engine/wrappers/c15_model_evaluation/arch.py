# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``arch`` -- method card #77.

#77 ARCH-LM test (Engle)

Category 15-model-evaluation; module ``arch``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c15_model_evaluation import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "run_arch_test",
    "NODE_META",
    "wire_model",
]


def run_arch_test(
    *,
    x: pd.Series,
    lags: int | None = None,
    demean: bool | None = None,
) -> dict[str, Any]:
    """Node ``run_arch_test`` -- method card #77.

    ARCH-LM test (Engle).

    Category 15-model-evaluation; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate series/residuals for testing ARCH
            effects.
        lags: [integer, optional] Lags of the auxiliary regression (positive integer < length,
            default 12). Default ``12``.
        demean: [boolean, optional] Removal of the mean of x before the test (default False).
            Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "run_arch_test: not implemented."
    )
