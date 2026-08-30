# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``oaxaca`` -- method card #63.

#63 oaxaca (Blinder-Oaxaca decomposition)

Category 11-decomposition-accounting; module ``oaxaca``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from econflow_engine.generated.args.c11_decomposition_accounting import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ox_decompose",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ox_decompose(
    *,
    formula: str,
    data: pd.DataFrame,
    n_bootstrap: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``ox_decompose`` -- method card #63.

    oaxaca (Blinder-Oaxaca decomposition).

    Category 11-decomposition-accounting; memory class ``light``.

    Args:
        formula: [formula, required] Formula 'y ~ x1 + x2 +... | group'· group binary 0/1.
        data: [df_handle, required] Handle to a cross-section DataFrame.
        n_bootstrap: [integer, optional] Bootstrap replications for SE (positive integer· default
            100). Default ``100``.
        seed: [integer, optional] Reproducibility seed of the bootstrap (default 42). Default
            ``42``.

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
        "ox_decompose: not implemented."
    )
