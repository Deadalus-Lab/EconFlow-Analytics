# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``connectedness`` -- method card #51.

#51 Connectedness (Diebold-Yılmaz, full)

Category 09-cross-section-networks; module ``connectedness``.

Reference implementation: 10.1016/j.ijforecast.2011.02.006.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c09_cross_section_networks import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "dy_fit",
    "dy_table",
    "dy_time_connectedness",
    "dy_var",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def dy_fit(
    *,
    x: pd.Series,
    nlag: int | None = None,
    nfore: int | None = None,
    window_size: int | None = None,
    corrected: bool | None = None,
    model: Literal["VAR", "TVP-VAR"] | None = None,
) -> dict[str, Any]:
    """Node ``dy_fit`` -- method card #51.

    Connectedness (Diebold-Yılmaz, full).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        x: [irregular_series_handle, required] Multivariate data (>=2 columns)· delivered as a
            series handle.
        nlag: [integer, optional] Lag length (default 1). Default ``1``.
        nfore: [integer, optional] H-step ahead forecast horizon (default 10). Default ``10``.
        window_size: [integer, optional] Rolling-window size (None -> static full-sample).
        corrected: [boolean, optional] Corrected TCI (default False).
        model: [enum, optional] Model (default VAR).

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
        "dy_fit: not implemented."
    )


def dy_var(
    *,
    x: pd.Series,
    nlag: int | None = None,
) -> dict[str, Any]:
    """Node ``dy_var`` -- method card #51.

    Connectedness (Diebold-Yılmaz, full).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        x: [irregular_series_handle, required] Multivariate data (>=2 columns)· delivered as a
            series handle.
        nlag: [integer, optional] Lag length (default 1). Default ``1``.

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
        "dy_var: not implemented."
    )


def dy_time_connectedness(
    *,
    Phi: np.ndarray | None = None,
    Sigma: np.ndarray | None = None,
    nfore: int | None = None,
    generalized: bool | None = None,
    corrected: bool | None = None,
    FEVD: np.ndarray | None = None,
) -> dict[str, Any]:
    """Node ``dy_time_connectedness`` -- method card #51.

    Connectedness (Diebold-Yılmaz, full).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        Phi: [matrix_handle, optional] VAR coefficient matrix k x (k*nlag) (alternative to FEVD).
        Sigma: [matrix_handle, optional] Residual variance-covariance matrix k x k.
        nfore: [integer, optional] H-step ahead forecast horizon (default 10). Default ``10``.
        generalized: [boolean, optional] Generalized (order-invariant) FEVD (default True).
        corrected: [boolean, optional] Corrected TCI (default False).
        FEVD: [matrix_handle, optional] Ready-made FEVD array (alternative to Phi/Sigma).

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
        "dy_time_connectedness: not implemented."
    )


def dy_table(
    *,
    FEVD: np.ndarray,
    digit: int | None = None,
) -> dict[str, Any]:
    """Node ``dy_table`` -- method card #51.

    Connectedness (Diebold-Yılmaz, full).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        FEVD: [matrix_handle, required] Square FEVD matrix (k x k).
        digit: [integer, optional] Decimal digits (default 2). Default ``2``.

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
        "dy_table: not implemented."
    )
