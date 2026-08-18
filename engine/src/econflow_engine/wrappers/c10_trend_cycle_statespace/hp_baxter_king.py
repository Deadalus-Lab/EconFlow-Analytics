# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``hp_baxter_king`` -- METHOD-SELECTION card #56.

#56 HP / Baxter-King / Christiano-Fitzgerald filters

Category 10-trend-cycle-statespace; module ``hp_baxter_king``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c10_trend_cycle_statespace import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mfl_bk_filter",
    "mfl_bw_filter",
    "mfl_cf_filter",
    "mfl_hp_filter",
    "mfl_tr_filter",
    "NODE_META",
    "wire_model",
]


def mfl_hp_filter(
    *,
    y: pd.Series,
    freq: float | None = None,
    type: Literal["lambda", "frequency"] | None = None,
    drift: bool | None = None,
) -> dict[str, Any]:
    """Node ``mfl_hp_filter`` -- METHOD-SELECTION card #56.

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
    """
    raise NotImplementedError(
        "mfl_hp_filter: not implemented. The method card is in ./README.md."
    )


def mfl_bk_filter(
    *,
    y: pd.Series,
    pl: float | None = None,
    pu: float | None = None,
    nfix: int | None = None,
    type: Literal["fixed", "variable"] | None = None,
    drift: bool | None = None,
) -> dict[str, Any]:
    """Node ``mfl_bk_filter`` -- METHOD-SELECTION card #56.

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
    """
    raise NotImplementedError(
        "mfl_bk_filter: not implemented. The method card is in ./README.md."
    )


def mfl_cf_filter(
    *,
    y: pd.Series,
    pl: float | None = None,
    pu: float | None = None,
    root: bool | None = None,
    drift: bool | None = None,
    type: Literal["asymmetric", "symmetric", "fixed", "baxter-king", "trigonometric"] | None = None,
    nfix: int | None = None,
) -> dict[str, Any]:
    """Node ``mfl_cf_filter`` -- METHOD-SELECTION card #56.

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
    """
    raise NotImplementedError(
        "mfl_cf_filter: not implemented. The method card is in ./README.md."
    )


def mfl_bw_filter(
    *,
    y: pd.Series,
    freq: int | None = None,
    nfix: int | None = None,
    drift: bool | None = None,
) -> dict[str, Any]:
    """Node ``mfl_bw_filter`` -- METHOD-SELECTION card #56.

    HP / Baxter-King / Christiano-Fitzgerald filters.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        y: [series_handle, required] Handle to a univariate ts· Butterworth high-pass (full-length).
        freq: [integer, optional] Cut-off period (default 10).
        nfix: [integer, optional] Filter order (default 2).
        drift: [boolean, optional] Removal of linear drift before the filter. Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mfl_bw_filter: not implemented. The method card is in ./README.md."
    )


def mfl_tr_filter(
    *,
    y: pd.Series,
    pl: float | None = None,
    pu: float | None = None,
    drift: bool | None = None,
) -> dict[str, Any]:
    """Node ``mfl_tr_filter`` -- METHOD-SELECTION card #56.

    HP / Baxter-King / Christiano-Fitzgerald filters.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        y: [series_handle, required] Handle to a univariate ts (EVEN n)· trigonometric band-pass.
        pl: [number, optional] Lower cyclical period (>=2)· None -> frequency default.
        pu: [number, optional] Upper cyclical period (> pl)· None -> frequency default.
        drift: [boolean, optional] Removal of linear drift before the filter. Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mfl_tr_filter: not implemented. The method card is in ./README.md."
    )
