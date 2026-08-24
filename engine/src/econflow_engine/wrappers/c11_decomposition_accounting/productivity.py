# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``productivity`` -- method card #62.

#62 productivity (TFP / Malmquist / DEA)

Category 11-decomposition-accounting; module ``productivity``.

Reference implementation: 10.1007/s11123-012-0275-1.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c11_decomposition_accounting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "prod_fare_primont",
    "prod_malmquist",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def prod_malmquist(
    *,
    data: pd.DataFrame,
    id_var: str,
    time_var: str,
    x_vars: Sequence[str],
    y_vars: Sequence[str],
    rts: Literal["vrs", "crs", "nirs", "ndrs"] | None = None,
    orientation: Literal["out", "in"] | None = None,
    tech_reg: bool | None = None,
    scaled: bool | None = None,
) -> dict[str, Any]:
    """Node ``prod_malmquist`` -- method card #62.

    productivity (TFP / Malmquist / DEA).

    Category 11-decomposition-accounting; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a balanced panel DataFrame (DMU × period).
        id_var: [string, required] DMU identifier column name (e.g. country/region).
        time_var: [string, required] Period column name (NOT factor·
            integer/numeric/Date/character).
        x_vars: [series_codes, required] Input column names (K, L,...)· ALL > 0.
        y_vars: [series_codes, required] Output column names (GDP/value added,...)· ALL > 0.
        rts: [enum, optional] Returns-to-scale (default vrs).
        orientation: [enum, optional] Efficiency orientation (default out).
        tech_reg: [boolean, optional] Technological regress of the frontier is allowed (default
            True). Default ``True``.
        scaled: [boolean, optional] Data scaling for numerical stability (default True). Default
            ``True``.

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
        "prod_malmquist: not implemented."
    )


def prod_fare_primont(
    *,
    data: pd.DataFrame,
    id_var: str,
    time_var: str,
    x_vars: Sequence[str],
    y_vars: Sequence[str],
    w_vars: Sequence[str] | None = None,
    p_vars: Sequence[str] | None = None,
    tech_change: bool | None = None,
    tech_reg: bool | None = None,
    rts: Literal["vrs", "crs", "nirs", "ndrs"] | None = None,
    orientation: Literal["out", "in", "in-out"] | None = None,
    scaled: bool | None = None,
    shadow: bool | None = None,
) -> dict[str, Any]:
    """Node ``prod_fare_primont`` -- method card #62.

    productivity (TFP / Malmquist / DEA).

    Category 11-decomposition-accounting; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a balanced panel DataFrame (DMU × period).
        id_var: [string, required] DMU identifier column name.
        time_var: [string, required] Period column name (NOT factor).
        x_vars: [series_codes, required] Input column names· ALL > 0.
        y_vars: [series_codes, required] Output column names· ALL > 0.
        w_vars: [series_codes, optional] Input price column names (both-or-neither with p.vars· 1
            per input).
        p_vars: [series_codes, optional] Output price column names (both-or-neither with w.vars· 1
            per output).
        tech_change: [boolean, optional] Technological change over time is allowed (default True).
            Default ``True``.
        tech_reg: [boolean, optional] Technological regress is allowed (default True). Default
            ``True``.
        rts: [enum, optional] Returns-to-scale (default vrs).
        orientation: [enum, optional] Orientation (default out).
        scaled: [boolean, optional] Data scaling (default True). Default ``True``.
        shadow: [boolean, optional] Return shadow prices (default False). Default ``False``.

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
        "prod_fare_primont: not implemented."
    )
