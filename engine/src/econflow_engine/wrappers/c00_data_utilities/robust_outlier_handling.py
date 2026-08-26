# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``robust_outlier_handling`` -- method card #114.

#114 Robust outlier handling + robust measures of location/scale (winsorize/trim/robust-z/Huber-M)

Category 00-data-utilities; module ``robust_outlier_handling``.

Reference implementation: scipy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "rob_huber",
    "rob_trim",
    "rob_winsorize",
    "rob_zscore",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def rob_winsorize(
    *,
    x: pd.Series,
    probs: Sequence[float] | None = None,
    val: Sequence[float] | None = None,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``rob_winsorize`` -- method card #114.

    Robust outlier handling + robust measures of location/scale (winsorize/trim/robust-z/Huber-M).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a numeric series/vector (NOT matrix/df).
        probs: [num_array, optional] Two increasing quantiles in [0,1] for the capping bounds
            (default [0.05, 0.95]); ignored if val is given.
        val: [num_array, optional] Explicit bounds [lo, hi] (increasing, no NA); overrides probs.
        na_rm: [boolean, optional] Drop NA before computing the bounds (default False; NA with False
            => stop, otherwise bounds=NA => the WHOLE series becomes NA). Default ``False``.

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
        "rob_winsorize: not implemented."
    )


def rob_trim(
    *,
    x: pd.Series,
    trim: float | None = None,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``rob_trim`` -- method card #114.

    Robust outlier handling + robust measures of location/scale (winsorize/trim/robust-z/Huber-M).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a numeric series/vector (NOT matrix/df).
        trim: [number, optional] Trimming fraction per tail in [0, 0.5) (default 0.1); >=0.5 =>
            silently NA, <0 => no trimming (gated). Default ``0.1``.
        na_rm: [boolean, optional] Drop NA (default False; NA with False => stop). Default
            ``False``.

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
        "rob_trim: not implemented."
    )


def rob_zscore(
    *,
    x: pd.Series,
    center: bool | None = None,
    scale: bool | None = None,
) -> dict[str, Any]:
    """Node ``rob_zscore`` -- method card #114.

    Robust outlier handling + robust measures of location/scale (winsorize/trim/robust-z/Huber-M).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a numeric series/vector (NOT matrix/df; no NA — there
            is no the NA policy).
        center: [boolean, optional] Subtract the median before scaling (default True). Default
            ``True``.
        scale: [boolean, optional] Divide by MAD (default True); MAD=0 (near-constant series) =>
            stop (otherwise all NaN). Default ``True``.

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
        "rob_zscore: not implemented."
    )


def rob_huber(
    *,
    x: pd.Series,
    k: float | None = None,
    na_rm: bool | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``rob_huber`` -- method card #114.

    Robust outlier handling + robust measures of location/scale (winsorize/trim/robust-z/Huber-M).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a numeric series/vector (NOT matrix/df).
        k: [number, optional] Huber tuning parameter (positive; default 1.345 = ~95% Gaussian
            efficiency). Default ``1.345``.
        na_rm: [boolean, optional] Drop NA (default False; NA with False => stop). Default
            ``False``.
        conf_level: [number, optional] Confidence level in (0, 1) for the Wald CI; empty => no CI
            (location only).

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
        "rob_huber: not implemented."
    )
