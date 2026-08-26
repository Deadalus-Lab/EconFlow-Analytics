# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``sign_restriction_svar`` -- method card #21.

#21 Sign-restriction SVAR (Uhlig rejection & penalty, Rubio-Ramirez/Waggoner/Zha)

Category 04-structural-shocks; module ``sign_restriction_svar``.

Reference implementation: 10.1016/j.jmoneco.2004.05.007.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c04_structural_shocks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "sgn_rwz_reject",
    "sgn_uhlig_penalty",
    "sgn_uhlig_reject",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def sgn_uhlig_reject(
    *,
    Y: pd.DataFrame,
    constrained: Sequence[int],
    nlags: int | None = None,
    draws: int | None = None,
    subdraws: int | None = None,
    nkeep: int | None = None,
    KMIN: int | None = None,
    KMAX: int | None = None,
    steps: int | None = None,
    type: Literal["median", "mean"] | None = None,
) -> dict[str, Any]:
    """Node ``sgn_uhlig_reject`` -- method card #21.

    Sign-restriction SVAR (Uhlig rejection & penalty, Rubio-Ramirez/Waggoner/Zha).

    Category 04-structural-shocks; memory class ``mcmc``.

    Args:
        Y: [multiseries_handle, required] Handle to a multivariate ts (>=2 columns, no NA).
        constrained: [int_array, required] Signed sign-restriction indices (1st = shock of interest,
            e.g. [4,-3,-2,-5]).
        nlags: [integer, optional] VAR lags (default 4). Default ``4``.
        draws: [integer, optional] MCMC draws (default 200). Default ``200``.
        subdraws: [integer, optional] Sub-draws per draw (default 200). Default ``200``.
        nkeep: [integer, optional] Accepted draws to keep (default 1000). Default ``1000``.
        KMIN: [integer, optional] First horizon at which the restrictions are imposed (default 1).
            Default ``1``.
        KMAX: [integer, optional] Last horizon at which they are imposed (default 4). Default ``4``.
        steps: [integer, optional] IRF horizon (default 24). Default ``24``.
        type: [enum, optional] Central measure of the posterior bands (default median).

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
        "sgn_uhlig_reject: not implemented."
    )


def sgn_uhlig_penalty(
    *,
    Y: pd.DataFrame,
    constrained: Sequence[int],
    nlags: int | None = None,
    draws: int | None = None,
    subdraws: int | None = None,
    nkeep: int | None = None,
    KMIN: int | None = None,
    KMAX: int | None = None,
    steps: int | None = None,
    penalty: float | None = None,
    type: Literal["median", "mean"] | None = None,
) -> dict[str, Any]:
    """Node ``sgn_uhlig_penalty`` -- method card #21.

    Sign-restriction SVAR (Uhlig rejection & penalty, Rubio-Ramirez/Waggoner/Zha).

    Category 04-structural-shocks; memory class ``mcmc``.

    Args:
        Y: [multiseries_handle, required] Handle to a multivariate ts (>=2 columns, no NA).
        constrained: [int_array, required] Signed sign-restriction indices (1st = shock of
            interest).
        nlags: [integer, optional] VAR lags (default 4). Default ``4``.
        draws: [integer, optional] MCMC draws (default 1000). Default ``1000``.
        subdraws: [integer, optional] Sub-draws per draw (default 1000). Default ``1000``.
        nkeep: [integer, optional] Accepted draws (default 1000). Default ``1000``.
        KMIN: [integer, optional] First horizon at which they are imposed (default 1). Default
            ``1``.
        KMAX: [integer, optional] Last horizon at which they are imposed (default 4). Default ``4``.
        steps: [integer, optional] IRF horizon (default 24). Default ``24``.
        penalty: [number, optional] Penalty function weight (>=0, default 100). Default ``100``.
        type: [enum, optional] Central measure of the posterior bands (default median).

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
        "sgn_uhlig_penalty: not implemented."
    )


def sgn_rwz_reject(
    *,
    Y: pd.DataFrame,
    constrained: Sequence[int],
    nlags: int | None = None,
    draws: int | None = None,
    subdraws: int | None = None,
    nkeep: int | None = None,
    KMIN: int | None = None,
    KMAX: int | None = None,
    steps: int | None = None,
    type: Literal["median", "mean"] | None = None,
) -> dict[str, Any]:
    """Node ``sgn_rwz_reject`` -- method card #21.

    Sign-restriction SVAR (Uhlig rejection & penalty, Rubio-Ramirez/Waggoner/Zha).

    Category 04-structural-shocks; memory class ``mcmc``.

    Args:
        Y: [multiseries_handle, required] Handle to a multivariate ts (>=2 columns, no NA).
        constrained: [int_array, required] Signed sign-restriction indices
            (Rubio-Ramirez/Waggoner/Zha).
        nlags: [integer, optional] VAR lags (default 4). Default ``4``.
        draws: [integer, optional] MCMC draws (default 200). Default ``200``.
        subdraws: [integer, optional] Sub-draws per draw (default 200). Default ``200``.
        nkeep: [integer, optional] Accepted draws (default 1000). Default ``1000``.
        KMIN: [integer, optional] First horizon at which they are imposed (default 1). Default
            ``1``.
        KMAX: [integer, optional] Last horizon at which they are imposed (default 4). Default ``4``.
        steps: [integer, optional] IRF horizon (default 24). Default ``24``.
        type: [enum, optional] Central measure of the posterior bands (default median).

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
        "sgn_rwz_reject: not implemented."
    )
