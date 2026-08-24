# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``shadow_rate_var`` -- method card #422.

#422 Shadow-rate VAR consistent with the effective lower bound

Category 03-multivariate-nowcasting; module ``shadow_rate_var``.

Reference implementation: srvar-toolkit.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c03_multivariate_nowcasting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mn_shadow_rate_var",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def mn_shadow_rate_var(
    *,
    y: pd.DataFrame,
    policy_rate: str,
    lower_bound: float | None = None,
    lags: int | None = None,
    draws: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``mn_shadow_rate_var`` -- method card #422.

    Shadow-rate VAR consistent with the effective lower bound.

    Category 03-multivariate-nowcasting; memory class ``mcmc``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [multiseries_handle, required] Endogenous variables including the policy rate.
        policy_rate: [string, required] Column holding the policy rate.
        lower_bound: [number, optional] Effective lower bound. Default ``0.0``.
        lags: [integer, optional] Lag order. Default ``4``.
        draws: [integer, optional] Posterior draws. Default ``2000``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

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
        "mn_shadow_rate_var: not implemented."
    )
