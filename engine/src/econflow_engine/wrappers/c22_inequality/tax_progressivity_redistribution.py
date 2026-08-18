# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``tax_progressivity_redistribution`` -- METHOD-SELECTION card #224.

#224 tax progressivity & redistribution + subgroup decomposition of inequality (extended/S-Gini ·
    concentration · Atkinson · GEI · Lorenz)

Category 22-inequality; module ``tax_progressivity_redistribution``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c22_inequality import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ic2_atkinson",
    "ic2_decomp_atkinson",
    "ic2_decomp_gei",
    "ic2_decomp_sgini",
    "ic2_gei",
    "ic2_lorenz",
    "ic2_sconc",
    "ic2_sgini",
    "NODE_META",
    "wire_model",
]


def ic2_sgini(
    *,
    x: np.ndarray,
    w: np.ndarray | None = None,
    param: float | None = None,
) -> dict[str, Any]:
    """Node ``ic2_sgini`` -- METHOD-SELECTION card #224.

    tax progressivity & redistribution + subgroup decomposition of inequality (extended/S-Gini ·
    concentration · Atkinson · GEI · Lorenz).

    Category 22-inequality; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric distribution vector (income/wealth/tax),
            length >= 2, without NA/Inf, x >= 0, sum(x) > 0.
        w: [matrix_handle, optional] Handle to optional sampling weights w (same length as x,
            strictly > 0); absence => unweighted.
        param: [number, optional] Extended Gini parameter (> 0; default 2 = classical Gini); param>1
            weights the poor; 0<param<1 => NEGATIVE.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ic2_sgini: not implemented. The method card is in ./README.md."
    )


def ic2_sconc(
    *,
    x: np.ndarray,
    y: np.ndarray,
    w: np.ndarray | None = None,
    param: float | None = None,
) -> dict[str, Any]:
    """Node ``ic2_sconc`` -- METHOD-SELECTION card #224.

    tax progressivity & redistribution + subgroup decomposition of inequality (extended/S-Gini ·
    concentration · Atkinson · GEI · Lorenz).

    Category 22-inequality; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric vector for concentration (e.g.
            tax/benefit/expenditure), length >= 2, without NA/Inf, x >= 0, sum(x) > 0.
        y: [matrix_handle, required] Handle to a numeric RANKING variable (e.g. pre-tax income);
            same length as x; negative values allowed; without NA/Inf.
        w: [matrix_handle, optional] Handle to optional sampling weights w (same length as x,
            strictly > 0); absence => unweighted.
        param: [number, optional] Concentration parameter (> 0; default 2).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ic2_sconc: not implemented. The method card is in ./README.md."
    )


def ic2_atkinson(
    *,
    x: np.ndarray,
    w: np.ndarray | None = None,
    epsilon: float | None = None,
) -> dict[str, Any]:
    """Node ``ic2_atkinson`` -- METHOD-SELECTION card #224.

    tax progressivity & redistribution + subgroup decomposition of inequality (extended/S-Gini ·
    concentration · Atkinson · GEI · Lorenz).

    Category 22-inequality; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric distribution vector (income/wealth/tax),
            length >= 2, without NA/Inf, x >= 0, sum(x) > 0.
        w: [matrix_handle, optional] Handle to optional sampling weights w (same length as x,
            strictly > 0); absence => unweighted.
        epsilon: [number, optional] Inequality aversion parameter epsilon (> 0; default 1);
            epsilon==1 requires x > 0 (geometric mean).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ic2_atkinson: not implemented. The method card is in ./README.md."
    )


def ic2_gei(
    *,
    x: np.ndarray,
    w: np.ndarray | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``ic2_gei`` -- METHOD-SELECTION card #224.

    tax progressivity & redistribution + subgroup decomposition of inequality (extended/S-Gini ·
    concentration · Atkinson · GEI · Lorenz).

    Category 22-inequality; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric distribution vector (income/wealth/tax),
            length >= 2, without NA/Inf, x >= 0, sum(x) > 0.
        w: [matrix_handle, optional] Handle to optional sampling weights w (same length as x,
            strictly > 0); absence => unweighted.
        alpha: [number, optional] GE parameter alpha (any finite real; default 1); alpha=1
            Theil-T/GE(1), alpha=0 mean log deviation/GE(0)· alpha ∈ {0,1} requires x > 0.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ic2_gei: not implemented. The method card is in ./README.md."
    )


def ic2_lorenz(
    *,
    x: np.ndarray,
    w: np.ndarray | None = None,
) -> dict[str, Any]:
    """Node ``ic2_lorenz`` -- METHOD-SELECTION card #224.

    tax progressivity & redistribution + subgroup decomposition of inequality (extended/S-Gini ·
    concentration · Atkinson · GEI · Lorenz).

    Category 22-inequality; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric distribution vector (income/wealth/tax),
            length >= 2, without NA/Inf, x >= 0, sum(x) > 0.
        w: [matrix_handle, optional] Handle to optional sampling weights w (same length as x,
            strictly > 0); absence => unweighted.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ic2_lorenz: not implemented. The method card is in ./README.md."
    )


def ic2_decomp_sgini(
    *,
    x: np.ndarray,
    z: Sequence[str],
    w: np.ndarray | None = None,
    param: float | None = None,
    decomp: Literal["BM", "YL"] | None = None,
    ELMO: bool | None = None,
) -> dict[str, Any]:
    """Node ``ic2_decomp_sgini`` -- METHOD-SELECTION card #224.

    tax progressivity & redistribution + subgroup decomposition of inequality (extended/S-Gini ·
    concentration · Atkinson · GEI · Lorenz).

    Category 22-inequality; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric distribution vector (income/wealth/tax),
            length >= 2, without NA/Inf, x >= 0, sum(x) > 0.
        z: [series_codes, required] Array of group labels z (same length as x); converted into a
            factor; >= 2 non-empty groups are required.
        w: [matrix_handle, optional] Handle to optional sampling weights w (same length as x,
            strictly > 0); absence => unweighted.
        param: [number, optional] Extended Gini parameter (> 0; default 2).
        decomp: [enum, optional] Decomposition: 'BM' Bhattacharya-Mahalanobis
            (within+between+overlap; default) or 'YL' Yitzhaki-Lerman (within+between+stratif).
        ELMO: [boolean, optional] ELMO: computation of the 'maximum' between-group inequality
            (Elbers et al. 2005; default True).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ic2_decomp_sgini: not implemented. The method card is in ./README.md."
    )


def ic2_decomp_gei(
    *,
    x: np.ndarray,
    z: Sequence[str],
    w: np.ndarray | None = None,
    alpha: float | None = None,
    ELMO: bool | None = None,
) -> dict[str, Any]:
    """Node ``ic2_decomp_gei`` -- METHOD-SELECTION card #224.

    tax progressivity & redistribution + subgroup decomposition of inequality (extended/S-Gini ·
    concentration · Atkinson · GEI · Lorenz).

    Category 22-inequality; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric distribution vector (income/wealth/tax),
            length >= 2, without NA/Inf, x >= 0, sum(x) > 0.
        z: [series_codes, required] Array of group labels z (same length as x); converted into a
            factor; >= 2 non-empty groups are required.
        w: [matrix_handle, optional] Handle to optional sampling weights w (same length as x,
            strictly > 0); absence => unweighted.
        alpha: [number, optional] GE parameter alpha (default 1; alpha ∈ {0,1} requires x > 0).
        ELMO: [boolean, optional] ELMO: computation of the 'maximum' between-group inequality
            (Elbers et al. 2005; default True).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ic2_decomp_gei: not implemented. The method card is in ./README.md."
    )


def ic2_decomp_atkinson(
    *,
    x: np.ndarray,
    z: Sequence[str],
    w: np.ndarray | None = None,
    epsilon: float | None = None,
    decomp: Literal["BDA", "DP"] | None = None,
    ELMO: bool | None = None,
) -> dict[str, Any]:
    """Node ``ic2_decomp_atkinson`` -- METHOD-SELECTION card #224.

    tax progressivity & redistribution + subgroup decomposition of inequality (extended/S-Gini ·
    concentration · Atkinson · GEI · Lorenz).

    Category 22-inequality; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric distribution vector (income/wealth/tax),
            length >= 2, without NA/Inf, x >= 0, sum(x) > 0.
        z: [series_codes, required] Array of group labels z (same length as x); converted into a
            factor; >= 2 non-empty groups are required.
        w: [matrix_handle, optional] Handle to optional sampling weights w (same length as x,
            strictly > 0); absence => unweighted.
        epsilon: [number, optional] Aversion parameter epsilon (> 0; default 1; epsilon==1 requires
            x > 0).
        decomp: [enum, optional] Decomposition: 'BDA' Blackorby-Donaldson-Auersperg (MULTIPLICATIVE:
            total=1-(1-w)(1-b); 3rd term 'cross'; default) or 'DP' Das-Parikh (ADDITIVE:
            within+between+residual).
        ELMO: [boolean, optional] ELMO: computation of the 'maximum' between-group inequality
            (Elbers et al. 2005; default True).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ic2_decomp_atkinson: not implemented. The method card is in ./README.md."
    )
