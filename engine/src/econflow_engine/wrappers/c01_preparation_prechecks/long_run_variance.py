# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``long_run_variance`` -- method card #394.

#394 Long-run variance and HAC bandwidth selection

Category 01-preparation-prechecks; module ``long_run_variance``.

Reference implementation: arch.

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
    "pp_long_run_variance",
    "NODE_META",
    "wire_model",
]


def pp_long_run_variance(
    *,
    x: pd.Series,
    kernel: (
        Literal[
            "bartlett",
            "parzen",
            "quadratic_spectral",
            "truncated",
            "tukey_hanning",
        ]
        | None
    ) = None,
    bandwidth: int | None = None,
    bandwidth_rule: Literal["andrews", "newey_west", "fixed"] | None = None,
    prewhiten: bool | None = None,
) -> dict[str, Any]:
    """Node ``pp_long_run_variance`` -- method card #394.

    Long-run variance and HAC bandwidth selection.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Series.
        kernel: [enum, optional] Kernel function. Default ``'bartlett'``.
        bandwidth: [integer, optional] Truncation lag; omitted = automatic.
        bandwidth_rule: [enum, optional] Automatic bandwidth rule. Default ``'andrews'``.
        prewhiten: [boolean, optional] Prewhiten before applying the kernel. Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pp_long_run_variance: not implemented."
    )
