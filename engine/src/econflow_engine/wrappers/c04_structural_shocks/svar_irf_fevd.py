# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``svar_irf_fevd`` -- METHOD-SELECTION card #19.

#19 SVAR / IRF / FEVD / Blanchard-Quah (theory-based identification)

Category 04-structural-shocks; module ``svar_irf_fevd``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c04_structural_shocks import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "vr_bq",
    "vr_fevd",
    "vr_irf",
    "vr_svar",
    "NODE_META",
    "wire_model",
]


def vr_svar(
    *,
    model: Any,
    estmethod: Literal["scoring", "direct"] | None = None,
    Amat: np.ndarray | None = None,
    Bmat: np.ndarray | None = None,
    lrtest: bool | None = None,
) -> dict[str, Any]:
    """Node ``vr_svar`` -- METHOD-SELECTION card #19.

    SVAR / IRF / FEVD / Blanchard-Quah (theory-based identification).

    Category 04-structural-shocks; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        model: [raw_handle, required] Handle to a reduced-form 'varest' (from vr_var, button #11).
        estmethod: [enum, optional] Estimation method (default scoring).
        Amat: [matrix_handle, optional] Handle to a K x K A-model matrix (NA = free parameter).
        Bmat: [matrix_handle, optional] Handle to a K x K B-model matrix (NA = free parameter).
        lrtest: [boolean, optional] LR test overidentifying restrictions (default True). Default
            ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "vr_svar: not implemented. The method card is in ./README.md."
    )


def vr_bq(
    *,
    model: Any,
) -> dict[str, Any]:
    """Node ``vr_bq`` -- METHOD-SELECTION card #19.

    SVAR / IRF / FEVD / Blanchard-Quah (theory-based identification).

    Category 04-structural-shocks; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        model: [raw_handle, required] Handle to a reduced-form 'varest' (BQ long-run restrictions).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "vr_bq: not implemented. The method card is in ./README.md."
    )


def vr_irf(
    *,
    model: Any,
    impulse: str | None = None,
    response: str | None = None,
    n_ahead: int | None = None,
    ortho: bool | None = None,
    cumulative: bool | None = None,
    boot: bool | None = None,
    ci: float | None = None,
    runs: int | None = None,
) -> dict[str, Any]:
    """Node ``vr_irf`` -- METHOD-SELECTION card #19.

    SVAR / IRF / FEVD / Blanchard-Quah (theory-based identification).

    Category 04-structural-shocks; memory class ``heavy``.

    Args:
        model: [raw_handle, required] Handle to a 'varest'/'svarest'/'vec2var' (reduced or
            structural).
        impulse: [string, optional] Name of the shock variable (default: all).
        response: [string, optional] Name of the response variable (default: all).
        n_ahead: [integer, optional] IRF horizon (positive integer, default 10). Default ``10``.
        ortho: [boolean, optional] Orthogonalised (Cholesky) IRF (default True). Default ``True``.
        cumulative: [boolean, optional] Cumulative responses (default False). Default ``False``.
        boot: [boolean, optional] Bootstrap CI bands (default True). Default ``True``.
        ci: [number, optional] Confidence level in (0,1) (default 0.95). Default ``0.95``.
        runs: [integer, optional] Bootstrap runs (positive integer, default 100). Default ``100``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "vr_irf: not implemented. The method card is in ./README.md."
    )


def vr_fevd(
    *,
    model: Any,
    n_ahead: int | None = None,
) -> dict[str, Any]:
    """Node ``vr_fevd`` -- METHOD-SELECTION card #19.

    SVAR / IRF / FEVD / Blanchard-Quah (theory-based identification).

    Category 04-structural-shocks; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a 'varest'/'svarest'/'vec2var'.
        n_ahead: [integer, optional] FEVD horizon (positive integer, default 10). Default ``10``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "vr_fevd: not implemented. The method card is in ./README.md."
    )
