# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``density_forecast_evaluation`` -- method card #94.

#94 Density-forecast evaluation — CRPS / LogS / PIT (sample + parametric + tail-weighted)

Category 15-model-evaluation; module ``density_forecast_evaluation``.

Reference implementation: scoringrules.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import numpy as np

from econflow_engine.generated.args.c15_model_evaluation import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "sr_crps_parametric",
    "sr_crps_sample",
    "sr_crps_tailweighted",
    "sr_logs_parametric",
    "sr_logs_sample",
    "sr_pit_sample",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def sr_crps_sample(
    *,
    y: Any,
    dat: np.ndarray,
    method: Literal["edf", "kde"] | None = None,
    bw: float | None = None,
) -> dict[str, Any]:
    """Node ``sr_crps_sample`` -- method card #94.

    Density-forecast evaluation — CRPS / LogS / PIT (sample + parametric + tail-weighted).

    Category 15-model-evaluation; memory class ``light``.

    Args:
        y: [raw_handle, required] Handle to a bare numeric vector of observations (one per time·
            realizations).
        dat: [matrix_handle, required] Handle to a matrix of predictive draws (one row per
            observation, >=2 columns).
        method: [enum, optional] CDF estimation: edf=empirical (default, robust), kde=Gaussian
            kernel.
        bw: [number, optional] Bandwidth for kde (positive· None = auto).

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
        "sr_crps_sample: not implemented."
    )


def sr_logs_sample(
    *,
    y: Any,
    dat: np.ndarray,
    bw: float | None = None,
) -> dict[str, Any]:
    """Node ``sr_logs_sample`` -- method card #94.

    Density-forecast evaluation — CRPS / LogS / PIT (sample + parametric + tail-weighted).

    Category 15-model-evaluation; memory class ``light``.

    Args:
        y: [raw_handle, required] Handle to a bare numeric vector of observations (realizations).
        dat: [matrix_handle, required] Handle to a matrix of predictive draws (one row per
            observation, >=2 columns).
        bw: [number, optional] KDE bandwidth (positive· None = auto· sensitive in the tails).

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
        "sr_logs_sample: not implemented."
    )


def sr_crps_parametric(
    *,
    y: Any,
    family: Literal["normal", "t", "mixnorm"] | None = None,
    mean: float | None = None,
    sd: float | None = None,
    df: float | None = None,
    location: float | None = None,
    scale: float | None = None,
) -> dict[str, Any]:
    """Node ``sr_crps_parametric`` -- method card #94.

    Density-forecast evaluation — CRPS / LogS / PIT (sample + parametric + tail-weighted).

    Category 15-model-evaluation; memory class ``light``.

    Args:
        y: [raw_handle, required] Handle to a bare numeric vector of observations (realizations).
        family: [enum, optional] Family of the predictive distribution (default normal).
        mean: [number, optional] Mean of the predictive normal (default 0). Default ``0``.
        sd: [number, optional] Standard deviation of the predictive normal (>0, default 1). Default
            ``1``.
        df: [number, optional] Degrees of freedom (required when family='t', >0).
        location: [number, optional] Location of the t (default 0). Default ``0``.
        scale: [number, optional] Scale of the t (>0, default 1). Default ``1``.

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
        "sr_crps_parametric: not implemented."
    )


def sr_logs_parametric(
    *,
    y: Any,
    family: Literal["normal", "t", "mixnorm"] | None = None,
    mean: float | None = None,
    sd: float | None = None,
    df: float | None = None,
    location: float | None = None,
    scale: float | None = None,
) -> dict[str, Any]:
    """Node ``sr_logs_parametric`` -- method card #94.

    Density-forecast evaluation — CRPS / LogS / PIT (sample + parametric + tail-weighted).

    Category 15-model-evaluation; memory class ``light``.

    Args:
        y: [raw_handle, required] Handle to a bare numeric vector of observations (realizations).
        family: [enum, optional] Family of the predictive distribution (default normal).
        mean: [number, optional] Mean of the predictive normal (default 0). Default ``0``.
        sd: [number, optional] Standard deviation of the predictive normal (>0, default 1). Default
            ``1``.
        df: [number, optional] Degrees of freedom (required when family='t', >0).
        location: [number, optional] Location of the t (default 0). Default ``0``.
        scale: [number, optional] Scale of the t (>0, default 1). Default ``1``.

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
        "sr_logs_parametric: not implemented."
    )


def sr_crps_tailweighted(
    *,
    y: Any,
    dat: np.ndarray,
    side: Literal["left", "right", "interval"] | None = None,
    a: float | None = None,
    b: float | None = None,
    kind: Literal["threshold", "outcome"] | None = None,
) -> dict[str, Any]:
    """Node ``sr_crps_tailweighted`` -- method card #94.

    Density-forecast evaluation — CRPS / LogS / PIT (sample + parametric + tail-weighted).

    Category 15-model-evaluation; memory class ``light``.

    Args:
        y: [raw_handle, required] Handle to a bare numeric vector of observations (realizations).
        dat: [matrix_handle, required] Handle to a matrix of predictive draws (one row per
            observation, >=2 columns).
        side: [enum, optional] Weight region: left=[-Inf,b], right=[a,Inf], interval=[a,b] (default
            left, GaR downside).
        a: [number, optional] Lower threshold bound (finite for right/interval).
        b: [number, optional] Upper threshold bound (finite for left/interval).
        kind: [enum, optional] threshold=twcrps (indicator weight), outcome=owcrps (default
            threshold).

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
        "sr_crps_tailweighted: not implemented."
    )


def sr_pit_sample(
    *,
    y: Any,
    dat: np.ndarray,
) -> dict[str, Any]:
    """Node ``sr_pit_sample`` -- method card #94.

    Density-forecast evaluation — CRPS / LogS / PIT (sample + parametric + tail-weighted).

    Category 15-model-evaluation; memory class ``light``.

    Args:
        y: [raw_handle, required] Handle to a bare numeric vector of observations (realizations).
        dat: [matrix_handle, required] Handle to a matrix of predictive draws (one row per
            observation, >=2 columns).

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
        "sr_pit_sample: not implemented."
    )
