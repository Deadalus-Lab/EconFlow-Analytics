# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``johansen_restricted_vecm`` -- METHOD-SELECTION card #23.

#23 Johansen (ca.jo) + restricted VECM (cajorls) + Phillips-Ouliaris/Engle-Granger family (ca.po)

Category 05-cointegration; module ``johansen_restricted_vecm``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c05_cointegration import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "wrap_ca_jo",
    "wrap_ca_po",
    "wrap_cajorls",
    "NODE_META",
    "wire_model",
]


def wrap_ca_jo(
    *,
    x: np.ndarray,
    type: Literal["eigen", "trace"] | None = None,
    ecdet: Literal["none", "const", "trend"] | None = None,
    K: int | None = None,
    spec: Literal["longrun", "transitory"] | None = None,
) -> dict[str, Any]:
    """Node ``wrap_ca_jo`` -- METHOD-SELECTION card #23.

    Johansen (ca.jo) + restricted VECM (cajorls) + Phillips-Ouliaris/Engle-Granger family (ca.po).

    Category 05-cointegration; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        x: [matrix_handle, required] Handle to a multivariate system (matrix/mts, >=2 columns I(1)).
        type: [enum, optional] Johansen statistic (default eigen = max-eigenvalue).
        ecdet: [enum, optional] Deterministic term in the cointegrating relation (default none).
        K: [integer, optional] Lag order in levels (VAR); integer >=2 (default 2). Default ``2``.
        spec: [enum, optional] VECM parameterization (default longrun).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_ca_jo: not implemented. The method card is in ./README.md."
    )


def wrap_cajorls(
    *,
    z: Any,
    r: int | None = None,
) -> dict[str, Any]:
    """Node ``wrap_cajorls`` -- METHOD-SELECTION card #23.

    Johansen (ca.jo) + restricted VECM (cajorls) + Phillips-Ouliaris/Engle-Granger family (ca.po).

    Category 05-cointegration; memory class ``light``.

    Args:
        z: [raw_handle, required] Handle to a 'ca.jo' object (from wrap_ca_jo).
        r: [integer, optional] Cointegration rank; integer 1..(P-1) (default 1). Default ``1``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_cajorls: not implemented. The method card is in ./README.md."
    )


def wrap_ca_po(
    *,
    z: np.ndarray,
    demean: Literal["none", "constant", "trend"] | None = None,
    lag: Literal["short", "long"] | None = None,
    type: Literal["Pu", "Pz"] | None = None,
) -> dict[str, Any]:
    """Node ``wrap_ca_po`` -- METHOD-SELECTION card #23.

    Johansen (ca.jo) + restricted VECM (cajorls) + Phillips-Ouliaris/Engle-Granger family (ca.po).

    Category 05-cointegration; memory class ``light``.

    Args:
        z: [matrix_handle, required] Handle to a multivariate system (matrix/mts, >=2 columns).
        demean: [enum, optional] Deterministic terms in the regression (default none).
        lag: [enum, optional] Long-run variance lag selection (default short).
        type: [enum, optional] Phillips-Ouliaris statistic (default Pu).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_ca_po: not implemented. The method card is in ./README.md."
    )
