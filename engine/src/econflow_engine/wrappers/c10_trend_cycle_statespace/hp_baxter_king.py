# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``hp_baxter_king`` -- method card #56.

#56 HP / Baxter-King / Christiano-Fitzgerald filters

Category 10-trend-cycle-statespace; module ``hp_baxter_king``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c10_trend_cycle_statespace import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "filt_baxter_king",
    "filt_butterworth",
    "filt_christiano_fitzgerald",
    "filt_hp",
    "filt_trigonometric",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def filt_hp(
    *,
    y: pd.Series,
    freq: float | None = None,
    type: Literal["lambda", "frequency"] | None = None,
    drift: bool | None = None,
) -> dict[str, Any]:
    """Node ``filt_hp`` -- method card #56.

    HP / Baxter-King / Christiano-Fitzgerald filters.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        y: [series_handle, required] Handle to a univariate ts (e.g. 100*log(GDP))· cycle = output
            gap.
        freq: [number, optional] lambda (type='lambda') or cut-off period (type='frequency')· None
            -> default from the frequency.
        type: [enum, optional] Interpretation of freq (default lambda).
        drift: [boolean, optional] Removal of linear drift before the filter. Default ``False``.

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
        "filt_hp: not implemented."
    )


def filt_baxter_king(
    *,
    y: pd.Series,
    pl: float | None = None,
    pu: float | None = None,
    nfix: int | None = None,
    type: Literal["fixed", "variable"] | None = None,
    drift: bool | None = None,
) -> dict[str, Any]:
    """Node ``filt_baxter_king`` -- method card #56.

    HP / Baxter-King / Christiano-Fitzgerald filters.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        y: [series_handle, required] Handle to a univariate ts· band-pass Baxter-King (NA at each
            end).
        pl: [number, optional] Lower cyclical period (>=2)· None -> frequency default.
        pu: [number, optional] Upper cyclical period (> pl)· None -> frequency default.
        nfix: [integer, optional] Lead/lag length (NA at each end)· None -> frequency default.
        type: [enum, optional] Fixed vs variable length (default fixed).
        drift: [boolean, optional] Removal of linear drift before the filter. Default ``False``.

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
        "filt_baxter_king: not implemented."
    )


def filt_christiano_fitzgerald(
    *,
    y: pd.Series,
    pl: float | None = None,
    pu: float | None = None,
    root: bool | None = None,
    drift: bool | None = None,
    type: Literal["asymmetric", "symmetric", "fixed", "baxter-king", "trigonometric"] | None = None,
    nfix: int | None = None,
) -> dict[str, Any]:
    """Node ``filt_christiano_fitzgerald`` -- method card #56.

    HP / Baxter-King / Christiano-Fitzgerald filters.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        y: [series_handle, required] Handle to a univariate ts· Christiano-Fitzgerald band-pass.
        pl: [number, optional] Lower cyclical period (>=2)· None -> frequency default.
        pu: [number, optional] Upper cyclical period (> pl)· None -> frequency default.
        root: [boolean, optional] Unit-root drift adjustment. Default ``False``.
        drift: [boolean, optional] Removal of linear drift before the filter. Default ``False``.
        type: [enum, optional] asymmetric (default) = full-length real-time gap (no NA).
        nfix: [integer, optional] Fixed lag length (only fixed/baxter-king types).

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
        "filt_christiano_fitzgerald: not implemented."
    )


def filt_butterworth(
    *,
    y: pd.Series,
    freq: int | None = None,
    nfix: int | None = None,
    drift: bool | None = None,
) -> dict[str, Any]:
    """Node ``filt_butterworth`` -- method card #56.

    HP / Baxter-King / Christiano-Fitzgerald filters.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        y: [series_handle, required] Handle to a univariate ts· Butterworth high-pass (full-length).
        freq: [integer, optional] Cut-off period (default 10).
        nfix: [integer, optional] Filter order (default 2).
        drift: [boolean, optional] Removal of linear drift before the filter. Default ``False``.

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
        "filt_butterworth: not implemented."
    )


def filt_trigonometric(
    *,
    y: pd.Series,
    pl: float | None = None,
    pu: float | None = None,
    drift: bool | None = None,
) -> dict[str, Any]:
    """Node ``filt_trigonometric`` -- method card #56.

    HP / Baxter-King / Christiano-Fitzgerald filters.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        y: [series_handle, required] Handle to a univariate ts (EVEN n)· trigonometric band-pass.
        pl: [number, optional] Lower cyclical period (>=2)· None -> frequency default.
        pu: [number, optional] Upper cyclical period (> pl)· None -> frequency default.
        drift: [boolean, optional] Removal of linear drift before the filter. Default ``False``.

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
        "filt_trigonometric: not implemented."
    )
