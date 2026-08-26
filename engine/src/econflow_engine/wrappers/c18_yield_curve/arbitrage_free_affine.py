# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``arbitrage_free_affine`` -- method card #211.

#211 Arbitrage-free affine (Gaussian) term-structure model — JSZ-style single-country JPS estimation
    with unspanned macro risks (risk-neutral Q + physical P parameters, model-implied yields,
    term-premia decomposition)

Category 18-yield-curve; module ``arbitrage_free_affine``.

Reference implementation: 10.1093/rfs/hhq128.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c18_yield_curve import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "atsm_estimate",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def atsm_estimate(
    *,
    model_type: Literal["JPS original", "JPS global"] | None = None,
    economy: str | None = None,
    n_factors: int | None = None,
    global_var: Sequence[str] | None = None,
    dom_var: Sequence[str] | None = None,
    init_date: str | None = None,
    final_date: str | None = None,
    data_freq: (
        Literal[
            "Monthly",
            "Quarterly",
            "Weekly",
            "Annually",
            "Daily All Days",
            "Daily Business Days",
        ]
        | None
    ) = None,
    stationary_Q: bool | None = None,
    horizon: int | None = None,
    compute_term_premia: bool | None = None,
    yields: np.ndarray | None = None,
    global_macro: np.ndarray | None = None,
    dom_macro: np.ndarray | None = None,
) -> dict[str, Any]:
    """Node ``atsm_estimate`` -- method card #211.

    Arbitrage-free affine (Gaussian) term-structure model — JSZ-style single-country JPS estimation
    with unspanned macro risks (risk-neutral Q + physical P parameters, model-implied yields,
    term-premia decomposition).

    Category 18-yield-curve; memory class ``light``.

    Args:
        model_type: [enum, optional] Type of single-country JPS ATSM (default 'JPS original';
            GVAR/JLL/multi out of scope for this node).
        economy: [string, optional] A single economy; must exist in yields ('Y<mat>M_<economy>') and
            dom_macro.
        n_factors: [integer, optional] Number of country-specific spanned factors N (>=1, <
            #maturities). Default ``1``.
        global_var: [series_codes, optional] Names of global variables (row labels of global_macro;
            default 'Gl_Eco_Act').
        dom_var: [series_codes, optional] Names of domestic variables ('<dom_var> <economy>' in
            dom_macro; default 'Eco_Act').
        init_date: [string, optional] Sample start 'dd-mm-yyyy' (within the data range, <
            final_date).
        final_date: [string, optional] Sample end 'dd-mm-yyyy' (within the data range, > init_date).
        data_freq: [enum, optional] Data frequency (default 'Monthly'; determines the dt
            annualization).
        stationary_Q: [boolean, optional] StatQ: enforcement of maximum eigenvalue under Q < 1
            (default False). Default ``False``.
        horizon: [integer, optional] Analysis horizon of the term-premia decomposition (default 25).
            Default ``25``.
        compute_term_premia: [boolean, optional] True -> model-implied yields + term premia +
            expected component; False -> estimation only (default True). Default ``True``.
        yields: [matrix_handle, optional] Handle to a numeric matrix of yields (rows
            'Y<mat>M_<economy>' × dates 'dd-mm-yyyy', with row labels/column labels); None ->
            built-in 'CM_2024'.
        global_macro: [matrix_handle, optional] Handle to a numeric matrix of global macro
            (variables × dates); None -> built-in; ALL-or-NONE with yields/dom_macro.
        dom_macro: [matrix_handle, optional] Handle to a numeric matrix of domestic macro ('<var>
            <economy>' × dates); None -> built-in.

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
        "atsm_estimate: not implemented."
    )
