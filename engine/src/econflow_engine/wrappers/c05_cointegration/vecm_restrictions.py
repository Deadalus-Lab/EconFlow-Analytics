# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``vecm_restrictions`` -- method card #433.

#433 Likelihood-ratio tests of restrictions on beta and alpha, and weak exogeneity

Category 05-cointegration; module ``vecm_restrictions``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c05_cointegration import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ci_vecm_restrict",
    "ci_weak_exogeneity",
    "NODE_META",
    "wire_model",
]


def ci_vecm_restrict(
    *,
    fit: Any,
    beta_restriction: np.ndarray | None = None,
    alpha_restriction: np.ndarray | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``ci_vecm_restrict`` -- method card #433.

    Likelihood-ratio tests of restrictions on beta and alpha, and weak exogeneity.

    Category 05-cointegration; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted VECM.
        beta_restriction: [matrix_handle, optional] Restriction matrix on beta.
        alpha_restriction: [matrix_handle, optional] Restriction matrix on alpha.
        alpha: [number, optional] Significance level. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ci_vecm_restrict: not implemented."
    )


def ci_weak_exogeneity(
    *,
    fit: Any,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``ci_weak_exogeneity`` -- method card #433.

    Likelihood-ratio tests of restrictions on beta and alpha, and weak exogeneity.

    Category 05-cointegration; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted VECM.
        alpha: [number, optional] Significance level. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ci_weak_exogeneity: not implemented."
    )
