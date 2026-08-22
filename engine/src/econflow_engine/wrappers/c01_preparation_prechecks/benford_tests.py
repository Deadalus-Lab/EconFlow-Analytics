# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``benford_tests`` -- method card #406.

#406 Benford digit tests

Category 01-preparation-prechecks; module ``benford_tests``.

Reference implementation: scipy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pp_benford_test",
    "NODE_META",
    "wire_model",
]


def pp_benford_test(
    *,
    x: pd.Series,
    digits: Literal["first", "second", "first_two", "first_three", "last_two"] | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``pp_benford_test`` -- method card #406.

    Benford digit tests.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Reported values.
        digits: [enum, optional] Digit test applied. Default ``'first'``.
        alpha: [number, optional] Significance level. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pp_benford_test: not implemented."
    )
