# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``canonical_cointegrating`` -- method card #436.

#436 Canonical cointegrating regression

Category 05-cointegration; module ``canonical_cointegrating``.

Reference implementation: arch.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c05_cointegration import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ci_canonical_regression",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ci_canonical_regression(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    method: Literal["ccr", "fmols", "dols"] | None = None,
    kernel: Literal["bartlett", "parzen", "quadratic_spectral"] | None = None,
    bandwidth: int | None = None,
    leads_lags: int | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``ci_canonical_regression`` -- method card #436.

    Canonical cointegrating regression.

    Category 05-cointegration; memory class ``light``.

    Args:
        y: [series_handle, required] Dependent series.
        x: [multiseries_handle, required] Regressor series.
        method: [enum, optional] Estimator. Default ``'ccr'``.
        kernel: [enum, optional] Kernel for the long-run covariance. Default ``'bartlett'``.
        bandwidth: [integer, optional] Bandwidth; omitted = automatic.
        leads_lags: [integer, optional] Leads and lags for the dynamic estimator. Default ``2``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

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
        "ci_canonical_regression: not implemented."
    )
