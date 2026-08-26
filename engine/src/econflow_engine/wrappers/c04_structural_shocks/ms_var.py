# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``ms_var`` -- method card #428.

#428 Markov-switching vector autoregression

Category 04-structural-shocks; module ``ms_var``.

Reference implementation: 10.1007/978-3-642-51684-9.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c04_structural_shocks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ss_ms_var",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ss_ms_var(
    *,
    y: pd.DataFrame,
    k_regimes: int | None = None,
    lags: int | None = None,
    switching_variance: bool | None = None,
    switching_coefficients: bool | None = None,
    n_starts: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``ss_ms_var`` -- method card #428.

    Markov-switching vector autoregression.

    Category 04-structural-shocks; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [multiseries_handle, required] Endogenous variables.
        k_regimes: [integer, optional] Number of regimes. Default ``2``.
        lags: [integer, optional] Lag order. Default ``1``.
        switching_variance: [boolean, optional] Allow the covariance to switch. Default ``True``.
        switching_coefficients: [boolean, optional] Allow the coefficients to switch. Default
            ``True``.
        n_starts: [integer, optional] Random restarts of the optimiser. Default ``10``.
        seed: [integer, optional] Seed for the random number generator.

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
        "ss_ms_var: not implemented."
    )
