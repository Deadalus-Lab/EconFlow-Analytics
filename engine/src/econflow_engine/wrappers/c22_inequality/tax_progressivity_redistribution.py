# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``tax_progressivity_redistribution`` -- method card #224.

#224 tax progressivity & redistribution + subgroup decomposition of inequality (extended/S-Gini ·
    concentration · Atkinson · GEI · Lorenz)

Category 22-inequality; module ``tax_progressivity_redistribution``.

Reference implementation: 10.2307/2648789.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
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
    "ineqd_atkinson",
    "ineqd_decomp_atkinson",
    "ineqd_decomp_gei",
    "ineqd_decomp_sgini",
    "ineqd_gei",
    "ineqd_lorenz",
    "ineqd_sconc",
    "ineqd_sgini",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ineqd_sgini(
    *,
    x: np.ndarray,
    w: np.ndarray | None = None,
    param: float | None = None,
) -> dict[str, Any]:
    """Node ``ineqd_sgini`` -- method card #224.

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
        "ineqd_sgini: not implemented."
    )


def ineqd_sconc(
    *,
    x: np.ndarray,
    y: np.ndarray,
    w: np.ndarray | None = None,
    param: float | None = None,
) -> dict[str, Any]:
    """Node ``ineqd_sconc`` -- method card #224.

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
        "ineqd_sconc: not implemented."
    )


def ineqd_atkinson(
    *,
    x: np.ndarray,
    w: np.ndarray | None = None,
    epsilon: float | None = None,
) -> dict[str, Any]:
    """Node ``ineqd_atkinson`` -- method card #224.

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
        "ineqd_atkinson: not implemented."
    )


def ineqd_gei(
    *,
    x: np.ndarray,
    w: np.ndarray | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``ineqd_gei`` -- method card #224.

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
        "ineqd_gei: not implemented."
    )


def ineqd_lorenz(
    *,
    x: np.ndarray,
    w: np.ndarray | None = None,
) -> dict[str, Any]:
    """Node ``ineqd_lorenz`` -- method card #224.

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
        "ineqd_lorenz: not implemented."
    )


def ineqd_decomp_sgini(
    *,
    x: np.ndarray,
    z: Sequence[str],
    w: np.ndarray | None = None,
    param: float | None = None,
    decomp: Literal["BM", "YL"] | None = None,
    ELMO: bool | None = None,
) -> dict[str, Any]:
    """Node ``ineqd_decomp_sgini`` -- method card #224.

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
        "ineqd_decomp_sgini: not implemented."
    )


def ineqd_decomp_gei(
    *,
    x: np.ndarray,
    z: Sequence[str],
    w: np.ndarray | None = None,
    alpha: float | None = None,
    ELMO: bool | None = None,
) -> dict[str, Any]:
    """Node ``ineqd_decomp_gei`` -- method card #224.

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
        "ineqd_decomp_gei: not implemented."
    )


def ineqd_decomp_atkinson(
    *,
    x: np.ndarray,
    z: Sequence[str],
    w: np.ndarray | None = None,
    epsilon: float | None = None,
    decomp: Literal["BDA", "DP"] | None = None,
    ELMO: bool | None = None,
) -> dict[str, Any]:
    """Node ``ineqd_decomp_atkinson`` -- method card #224.

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
        "ineqd_decomp_atkinson: not implemented."
    )
