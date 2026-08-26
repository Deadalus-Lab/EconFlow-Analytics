# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bayesian_visualization_extractors`` -- method card #73.

#73 Bayesian visualization DATA extractors (data, not charts)

Category 14-bayesian-toolkit; module ``bayesian_visualization_extractors``.

Reference implementation: arviz.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c14_bayesian_toolkit import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "bviz_mcmc_areas_data",
    "bviz_mcmc_intervals_data",
    "bviz_mcmc_neff_data",
    "bviz_mcmc_rhat_data",
    "bviz_mcmc_trace_data",
    "bviz_ppc_intervals_data",
    "bviz_ppc_ribbon_data",
    "bviz_ppc_stat_data",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def bviz_mcmc_intervals_data(
    *,
    x: Any,
    pars: Sequence[str] | None = None,
    prob: float | None = None,
    prob_outer: float | None = None,
    point_est: Literal["median", "mean", "none"] | None = None,
) -> dict[str, Any]:
    """Node ``bviz_mcmc_intervals_data`` -- method card #73.

    Bayesian visualization DATA extractors (data, not charts).

    Category 14-bayesian-toolkit; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to draws (3D array / matrix / DataFrame / list of chain
            matrices)· WITHOUT NA.
        pars: [series_codes, optional] Parameter names AS a character vector (empty = all).
        prob: [number, optional] Inner interval probability, strictly (0,1) (default 0.5·
            prob<=prob_outer). Default ``0.5``.
        prob_outer: [number, optional] Outer interval probability (default 0.9, <=1). Default
            ``0.9``.
        point_est: [enum, optional] Point estimate (default median).

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
        "bviz_mcmc_intervals_data: not implemented."
    )


def bviz_mcmc_areas_data(
    *,
    x: Any,
    pars: Sequence[str] | None = None,
    prob: float | None = None,
    prob_outer: float | None = None,
    point_est: Literal["median", "mean", "none"] | None = None,
) -> dict[str, Any]:
    """Node ``bviz_mcmc_areas_data`` -- method card #73.

    Bayesian visualization DATA extractors (data, not charts).

    Category 14-bayesian-toolkit; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to draws· density areas grid· WITHOUT NA.
        pars: [series_codes, optional] Parameter names AS a character vector (empty = all).
        prob: [number, optional] Inner interval probability, strictly (0,1) (default 0.5). Default
            ``0.5``.
        prob_outer: [number, optional] Outer probability (default 1 = full density, <=1). Default
            ``1``.
        point_est: [enum, optional] Point estimate (default median).

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
        "bviz_mcmc_areas_data: not implemented."
    )


def bviz_mcmc_trace_data(
    *,
    x: Any,
    pars: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``bviz_mcmc_trace_data`` -- method card #73.

    Bayesian visualization DATA extractors (data, not charts).

    Category 14-bayesian-toolkit; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to draws· trace value per iteration/chain· WITHOUT NA.
        pars: [series_codes, optional] Parameter names AS a character vector (empty = all).

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
        "bviz_mcmc_trace_data: not implemented."
    )


def bviz_mcmc_rhat_data(
    *,
    rhat: Any,
) -> dict[str, Any]:
    """Node ``bviz_mcmc_rhat_data`` -- method card #73.

    Bayesian visualization DATA extractors (data, not charts).

    Category 14-bayesian-toolkit; memory class ``light``.

    Args:
        rhat: [raw_handle, required] Handle to a PRECOMPUTED numeric R-hat vector (the
            convergence-diagnostic routine)· NOT a fitted model· WITHOUT NA, >0.

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
        "bviz_mcmc_rhat_data: not implemented."
    )


def bviz_mcmc_neff_data(
    *,
    ratio: Any,
) -> dict[str, Any]:
    """Node ``bviz_mcmc_neff_data`` -- method card #73.

    Bayesian visualization DATA extractors (data, not charts).

    Category 14-bayesian-toolkit; memory class ``light``.

    Args:
        ratio: [raw_handle, required] Handle to a PRECOMPUTED numeric N_eff/N ratio vector
            (ess-derived)· WITHOUT NA, >0.

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
        "bviz_mcmc_neff_data: not implemented."
    )


def bviz_ppc_intervals_data(
    *,
    y: Any,
    yrep: np.ndarray,
    x: Any | None = None,
    group: Any | None = None,
    prob: float | None = None,
    prob_outer: float | None = None,
) -> dict[str, Any]:
    """Node ``bviz_ppc_intervals_data`` -- method card #73.

    Bayesian visualization DATA extractors (data, not charts).

    Category 14-bayesian-toolkit; memory class ``light``.

    Args:
        y: [raw_handle, required] Handle to an observed numeric VECTOR y.
        yrep: [matrix_handle, required] Handle to a posterior-predictive MATRIX yrep (draws x obs)·
            ncol==length(y).
        x: [raw_handle, optional] Handle to an optional x-axis (length==length(y)).
        group: [raw_handle, optional] Handle to an optional group per observation
            (length==length(y)).
        prob: [number, optional] Inner interval probability (default 0.5). Default ``0.5``.
        prob_outer: [number, optional] Outer interval probability (default 0.9). Default ``0.9``.

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
        "bviz_ppc_intervals_data: not implemented."
    )


def bviz_ppc_ribbon_data(
    *,
    y: Any,
    yrep: np.ndarray,
    x: Any | None = None,
    group: Any | None = None,
    prob: float | None = None,
    prob_outer: float | None = None,
) -> dict[str, Any]:
    """Node ``bviz_ppc_ribbon_data`` -- method card #73.

    Bayesian visualization DATA extractors (data, not charts).

    Category 14-bayesian-toolkit; memory class ``light``.

    Args:
        y: [raw_handle, required] Handle to an observed numeric VECTOR y.
        yrep: [matrix_handle, required] Handle to a posterior-predictive MATRIX yrep (draws x obs)·
            ncol==length(y).
        x: [raw_handle, optional] Handle to an optional x-axis (length==length(y)).
        group: [raw_handle, optional] Handle to an optional group (length==length(y)).
        prob: [number, optional] Inner ribbon probability (default 0.5). Default ``0.5``.
        prob_outer: [number, optional] Outer ribbon probability (default 0.9). Default ``0.9``.

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
        "bviz_ppc_ribbon_data: not implemented."
    )


def bviz_ppc_stat_data(
    *,
    y: Any,
    yrep: np.ndarray,
    stat: str,
    group: Any | None = None,
) -> dict[str, Any]:
    """Node ``bviz_ppc_stat_data`` -- method card #73.

    Bayesian visualization DATA extractors (data, not charts).

    Category 14-bayesian-toolkit; memory class ``light``.

    Args:
        y: [raw_handle, required] Handle to an observed numeric VECTOR y.
        yrep: [matrix_handle, required] Handle to a posterior-predictive MATRIX yrep (draws x obs)·
            ncol==length(y).
        stat: [string, required] Statistic name AS A STRING (e.g. 'mean','sd','median')· of length
            1.
        group: [raw_handle, optional] Handle to an optional group per observation
            (length==length(y)).

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
        "bviz_ppc_stat_data: not implemented."
    )
