# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``iv_2sls`` -- method card #34.

#34 IV / 2SLS (classic)

Category 07-causality-policy; module ``iv_2sls``.

Reference implementation: linearmodels.

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

# --- gen_wrappers: header end ---


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
        "iv_2sls: not implemented."
    )
