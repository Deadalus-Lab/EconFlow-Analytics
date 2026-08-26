# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``fractionally_cointegrated_var`` -- method card #139.

#139 Fractionally Cointegrated VAR (Johansen-Nielsen): fractional cointegration with estimated d/b +
    rank tests (asymptotic + wild bootstrap) + lag selection

Category 05-cointegration; module ``fractionally_cointegrated_var``.

Reference implementation: 10.3982/ECTA9299.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c05_cointegration import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "fcv_boot_rank",
    "fcv_estimate",
    "fcv_lag_select",
    "fcv_rank_test",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def fcv_estimate(
    *,
    x: np.ndarray,
    k: int | None = None,
    r: int | None = None,
    db_min: Sequence[float] | None = None,
    db_max: Sequence[float] | None = None,
    restrict_db: bool | None = None,
    constrained: bool | None = None,
    level_param: bool | None = None,
    r_constant: bool | None = None,
    unr_constant: bool | None = None,
    grid_search: bool | None = None,
) -> dict[str, Any]:
    """Node ``fcv_estimate`` -- method card #139.

    Fractionally Cointegrated VAR (Johansen-Nielsen): fractional cointegration with estimated d/b +
    rank tests (asymptotic + wild bootstrap) + lag selection.

    Category 05-cointegration; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        x: [matrix_handle, required] Handle to a multivariate system (matrix/panel, >=2 columns,
            fractionally integrated).
        k: [integer, optional] Number of lags in the system; integer >=0 (default 1). Default ``1``.
        r: [integer, optional] Cointegration rank; integer 0..p (default 1). Default ``1``.
        db_min: [num_array, optional] Lower bound for (d,b); scalar or length-2 (default 0.01).
        db_max: [num_array, optional] Upper bound for (d,b); scalar or length-2 (default 2.0).
        restrict_db: [boolean, optional] Enforcement of the d=b constraint (default True). Default
            ``True``.
        constrained: [boolean, optional] Enforcement of dbMax>=d>=b>=dbMin (default False). Default
            ``False``.
        level_param: [boolean, optional] Inclusion of a level parameter (default True). Default
            ``True``.
        r_constant: [boolean, optional] Restricted constant in the cointegrating relation (default
            False). Default ``False``.
        unr_constant: [boolean, optional] Unrestricted constant (default False). Default ``False``.
        grid_search: [boolean, optional] Grid search for d,b (expensive accuracy-refinement; default
            False). Default ``False``.

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
        "fcv_estimate: not implemented."
    )


def fcv_rank_test(
    *,
    x: np.ndarray,
    k: int | None = None,
    restrict_db: bool | None = None,
    constrained: bool | None = None,
    grid_search: bool | None = None,
) -> dict[str, Any]:
    """Node ``fcv_rank_test`` -- method card #139.

    Fractionally Cointegrated VAR (Johansen-Nielsen): fractional cointegration with estimated d/b +
    rank tests (asymptotic + wild bootstrap) + lag selection.

    Category 05-cointegration; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a multivariate system (matrix/panel, >=2 columns).
        k: [integer, optional] Number of lags; integer >=0 (default 1). Default ``1``.
        restrict_db: [boolean, optional] Enforcement of d=b (default True). Default ``True``.
        constrained: [boolean, optional] Enforcement of dbMax>=d>=b>=dbMin (default False). Default
            ``False``.
        grid_search: [boolean, optional] Grid search for d,b (default False). Default ``False``.

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
        "fcv_rank_test: not implemented."
    )


def fcv_lag_select(
    *,
    x: np.ndarray,
    kmax: int | None = None,
    r: int | None = None,
    order: int | None = None,
    grid_search: bool | None = None,
) -> dict[str, Any]:
    """Node ``fcv_lag_select`` -- method card #139.

    Fractionally Cointegrated VAR (Johansen-Nielsen): fractional cointegration with estimated d/b +
    rank tests (asymptotic + wild bootstrap) + lag selection.

    Category 05-cointegration; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a multivariate system (matrix/panel, >=2 columns).
        kmax: [integer, optional] Maximum number of lags; integer >=1 (default 2). Default ``2``.
        r: [integer, optional] Cointegration rank; integer 0..p (default p — over-specify).
        order: [integer, optional] Serial correlation order for the white-noise tests; >=1 (default
            2). Default ``2``.
        grid_search: [boolean, optional] Grid search for d,b (default False). Default ``False``.

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
        "fcv_lag_select: not implemented."
    )


def fcv_boot_rank(
    *,
    x: np.ndarray,
    k: int | None = None,
    r1: int | None = None,
    r2: int | None = None,
    B: int | None = None,
    seed: int,
    grid_search: bool | None = None,
) -> dict[str, Any]:
    """Node ``fcv_boot_rank`` -- method card #139.

    Fractionally Cointegrated VAR (Johansen-Nielsen): fractional cointegration with estimated d/b +
    rank tests (asymptotic + wild bootstrap) + lag selection.

    Category 05-cointegration; memory class ``heavy``.

    Args:
        x: [matrix_handle, required] Handle to a multivariate system (matrix/panel, >=2 columns).
        k: [integer, optional] Number of lags; integer >=0 (default 1). Default ``1``.
        r1: [integer, optional] Rank under H0; integer 0..p (default 0). Default ``0``.
        r2: [integer, optional] Rank under H1; integer 0..p, r2>r1 (default 1). Default ``1``.
        B: [integer, optional] Number of bootstrap samples; integer >=1 (default 99). Default
            ``99``.
        seed: [integer, required] Seed (REQUIRED — wild bootstrap, stochastic).
        grid_search: [boolean, optional] Grid search for d,b (default False). Default ``False``.

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
        "fcv_boot_rank: not implemented."
    )
