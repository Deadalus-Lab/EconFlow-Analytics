# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``hac_robust_standard`` -- METHOD-SELECTION card #35.

#35 HAC / robust standard errors

Category 07-causality-policy; module ``hac_robust_standard``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "wrap_sandwich_blocks",
    "wrap_vcov_cl",
    "wrap_vcov_hac",
    "wrap_vcov_hc",
    "wrap_vcov_panel",
    "NODE_META",
    "wire_model",
]


def wrap_vcov_hc(
    *,
    object: Any,
    type: Literal["HC3", "const", "HC", "HC0", "HC1", "HC2", "HC4", "HC4m", "HC5"] | None = None,
    sandwich: bool | None = None,
) -> dict[str, Any]:
    """Node ``wrap_vcov_hc`` -- METHOD-SELECTION card #35.

    HAC / robust standard errors.

    Category 07-causality-policy; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fitted model (lm/glm/fixest; cross-section).
        type: [enum, optional] Heteroskedasticity-consistent type (default HC3).
        sandwich: [boolean, optional] True -> full sandwich vcov (default). Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_vcov_hc: not implemented. The method card is in ./README.md."
    )


def wrap_vcov_hac(
    *,
    object: Any,
    method: Literal["NeweyWest", "vcovHAC"] | None = None,
    lag: int | None = None,
    prewhite: bool | None = None,
    adjust: bool | None = None,
    sandwich: bool | None = None,
) -> dict[str, Any]:
    """Node ``wrap_vcov_hac`` -- METHOD-SELECTION card #35.

    HAC / robust standard errors.

    Category 07-causality-policy; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fitted time-series model (lm).
        method: [enum, optional] NeweyWest (default, macro TS) or generic vcovHAC.
        lag: [integer, optional] Bandwidth/lag (default: auto bwNeweyWest).
        prewhite: [boolean, optional] AR(1) prewhitening (NeweyWest default True).
        adjust: [boolean, optional] Small-sample dof adjustment.
        sandwich: [boolean, optional] True -> full sandwich vcov (default). Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_vcov_hac: not implemented. The method card is in ./README.md."
    )


def wrap_vcov_cl(
    *,
    object: Any,
    cluster: Any,
    type: Literal["HC0", "HC1", "HC2", "HC3"] | None = None,
    fix: bool | None = None,
) -> dict[str, Any]:
    """Node ``wrap_vcov_cl`` -- METHOD-SELECTION card #35.

    HAC / robust standard errors.

    Category 07-causality-policy; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fitted model.
        cluster: [raw_handle, required] Handle to a cluster variable (vector of the same length as
            the observations, >=2 levels).
        type: [enum, optional] HC type (default: HC1 for lm, otherwise HC0).
        fix: [boolean, optional] Correct a non-positive-definite vcov. Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_vcov_cl: not implemented. The method card is in ./README.md."
    )


def wrap_vcov_panel(
    *,
    object: Any,
    cluster: Any,
    order_by: Any,
    method: Literal["PL", "PC"] | None = None,
    kernel: (
        Literal[
            "Bartlett",
            "Truncated",
            "Parzen",
            "Tukey-Hanning",
            "Quadratic Spectral",
        ]
        | None
    ) = None,
    pairwise: bool | None = None,
    fix: bool | None = None,
) -> dict[str, Any]:
    """Node ``wrap_vcov_panel`` -- METHOD-SELECTION card #35.

    HAC / robust standard errors.

    Category 07-causality-policy; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fitted model (panel).
        cluster: [raw_handle, required] Handle to a cluster/unit variable (vector).
        order_by: [raw_handle, required] Handle to a time-ordering variable within each cluster
            (vector).
        method: [enum, optional] PL (Driscoll-Kraay panel HAC, default) or PC (Beck-Katz).
        kernel: [enum, optional] Kernel for method='PL' (default Bartlett).
        pairwise: [boolean, optional] Pairwise (unbalanced) for method='PC'. Default ``False``.
        fix: [boolean, optional] Correct a non-positive-definite vcov. Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_vcov_panel: not implemented. The method card is in ./README.md."
    )


def wrap_sandwich_blocks(
    *,
    object: Any,
    adjust: bool | None = None,
) -> dict[str, Any]:
    """Node ``wrap_sandwich_blocks`` -- METHOD-SELECTION card #35.

    HAC / robust standard errors.

    Category 07-causality-policy; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fitted model; returns estfun/bread/meat.
        adjust: [boolean, optional] Small-sample adjustment on the meat. Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_sandwich_blocks: not implemented. The method card is in ./README.md."
    )
