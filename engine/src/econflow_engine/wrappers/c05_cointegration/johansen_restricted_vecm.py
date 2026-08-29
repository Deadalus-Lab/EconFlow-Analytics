# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``johansen_restricted_vecm`` -- method card #23.

#23 Johansen procedure + restricted VECM + Phillips-Ouliaris/Engle-Granger residual tests

Category 05-cointegration; module ``johansen_restricted_vecm``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import numpy as np

from econflow_engine.generated.args.c05_cointegration import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "coint_johansen",
    "coint_johansen_vecm",
    "coint_phillips_ouliaris",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def coint_johansen(
    *,
    x: np.ndarray,
    type: Literal["eigen", "trace"] | None = None,
    ecdet: Literal["none", "const", "trend"] | None = None,
    K: int | None = None,
    spec: Literal["longrun", "transitory"] | None = None,
) -> dict[str, Any]:
    """Node ``coint_johansen`` -- method card #23.

    Johansen procedure + restricted VECM + Phillips-Ouliaris/Engle-Granger residual tests.

    Category 05-cointegration; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        x: [matrix_handle, required] Handle to a multivariate system (matrix/panel, >=2 columns
            I(1)).
        type: [enum, optional] Johansen statistic (default eigen = max-eigenvalue).
        ecdet: [enum, optional] Deterministic term in the cointegrating relation (default none).
        K: [integer, optional] Lag order in levels (VAR); integer >=2 (default 2). Default ``2``.
        spec: [enum, optional] VECM parameterization (default longrun).

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
        "coint_johansen: not implemented."
    )


def coint_johansen_vecm(
    *,
    z: Any,
    r: int | None = None,
) -> dict[str, Any]:
    """Node ``coint_johansen_vecm`` -- method card #23.

    Johansen procedure + restricted VECM + Phillips-Ouliaris/Engle-Granger residual tests.

    Category 05-cointegration; memory class ``light``.

    Args:
        z: [raw_handle, required] Handle to a 'Johansen' object (from coint_johansen).
        r: [integer, optional] Cointegration rank; integer 1..(P-1) (default 1). Default ``1``.

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
        "coint_johansen_vecm: not implemented."
    )


def coint_phillips_ouliaris(
    *,
    z: np.ndarray,
    demean: Literal["none", "constant", "trend"] | None = None,
    lag: Literal["short", "long"] | None = None,
    type: Literal["Pu", "Pz"] | None = None,
) -> dict[str, Any]:
    """Node ``coint_phillips_ouliaris`` -- method card #23.

    Johansen procedure + restricted VECM + Phillips-Ouliaris/Engle-Granger residual tests.

    Category 05-cointegration; memory class ``light``.

    Args:
        z: [matrix_handle, required] Handle to a multivariate system (matrix/panel, >=2 columns).
        demean: [enum, optional] Deterministic terms in the regression (default none).
        lag: [enum, optional] Long-run variance lag selection (default short).
        type: [enum, optional] Phillips-Ouliaris statistic (default Pu).

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
        "coint_phillips_ouliaris: not implemented."
    )
