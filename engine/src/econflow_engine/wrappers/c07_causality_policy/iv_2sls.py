# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``iv_2sls`` -- method card #34.

#34 IV / 2SLS (classic)

Category 07-causality-policy; module ``iv_2sls``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "iv_2sls",
    "NODE_META",
    "wire_model",
]


def iv_2sls(
    *,
    formula: str,
    data: pd.DataFrame,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``iv_2sls`` -- method card #34.

    IV / 2SLS (classic).

    Category 07-causality-policy; memory class ``light``.

    Args:
        formula: [formula, required] IV formula 'y ~ x1 + d | x1 + z' (instruments after the |).
        data: [df_handle, required] Handle to a DataFrame.
        conf_level: [number, optional] Confidence level for coefficient CIs (default 0.95). Default
            ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "iv_2sls: not implemented."
    )
