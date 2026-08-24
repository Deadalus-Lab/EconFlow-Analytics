# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``nonlinear_ardl_nardl`` -- method card #140.

#140 Nonlinear (asymmetric) ARDL — NARDL (Shin-Yu-Greenwood-Nimmo) + PSS bounds + CUSUM/CUSUMQ
    stability

Category 05-cointegration; module ``nonlinear_ardl_nardl``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c05_cointegration import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "nar_bounds",
    "nar_fit",
    "nar_stability",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def nar_fit(
    *,
    data: pd.DataFrame,
    y: str,
    x: str,
    ic: Literal["aic", "bic"] | None = None,
    maxlag: int | None = None,
    case: int | None = None,
) -> dict[str, Any]:
    """Node ``nar_fit`` -- method card #140.

    Nonlinear (asymmetric) ARDL — NARDL (Shin-Yu-Greenwood-Nimmo) + PSS bounds + CUSUM/CUSUMQ
    stability.

    Category 05-cointegration; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Handle to a DataFrame with the y & x columns.
        y: [string, required] Dependent-variable column name (closed; NOT a free formula).
        x: [string, required] Column name of the decomposed regressor (positive/negative partial
            sums); EXACTLY one.
        ic: [enum, optional] Lag selection criterion (default aic).
        maxlag: [integer, optional] Maximum lag for the search; positive integer (default 4).
            Default ``4``.
        case: [integer, optional] PSS case of deterministic terms; ONLY 3 (unrestricted intercept)
            or 5 (+trend). Default ``3``.

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
        "nar_fit: not implemented."
    )


def nar_bounds(
    *,
    object: Any,
) -> dict[str, Any]:
    """Node ``nar_bounds`` -- method card #140.

    Nonlinear (asymmetric) ARDL — NARDL (Shin-Yu-Greenwood-Nimmo) + PSS bounds + CUSUM/CUSUMQ
    stability.

    Category 05-cointegration; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a 'nardl' model (from nar_fit).

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
        "nar_bounds: not implemented."
    )


def nar_stability(
    *,
    object: Any,
) -> dict[str, Any]:
    """Node ``nar_stability`` -- method card #140.

    Nonlinear (asymmetric) ARDL — NARDL (Shin-Yu-Greenwood-Nimmo) + PSS bounds + CUSUM/CUSUMQ
    stability.

    Category 05-cointegration; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a 'nardl' model (from nar_fit).

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
        "nar_stability: not implemented."
    )
