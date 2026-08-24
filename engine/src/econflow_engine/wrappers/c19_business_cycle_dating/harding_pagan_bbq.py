# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``harding_pagan_bbq`` -- method card #88.

#88 Harding-Pagan BBQ (Quarterly Bry-Boschan turning points)

Category 19-business-cycle-dating; module ``harding_pagan_bbq``.

Reference implementation: 10.1016/S0304-3932(01)00108-8.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c19_business_cycle_dating import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "average_over_phases",
    "date_business_cycles",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def date_business_cycles(
    *,
    y: pd.Series,
    mincycle: int | None = None,
    minphase: int | None = None,
    name: str | None = None,
) -> dict[str, Any]:
    """Node ``date_business_cycles`` -- method card #88.

    Harding-Pagan BBQ (Quarterly Bry-Boschan turning points).

    Category 19-business-cycle-dating; memory class ``light``.

    Registers its result under ``bcdating``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Handle to a QUARTERLY (frequency == 4) univariate ts series.
        mincycle: [integer, optional] Minimum full-cycle duration in quarters (default 5; >
            minphase). Default ``5``.
        minphase: [integer, optional] Minimum phase duration in quarters (default 2). Default ``2``.
        name: [string, optional] Optional name label of the dating.

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
        "date_business_cycles: not implemented."
    )


def average_over_phases(
    *,
    series: pd.Series,
    dates: Any,
) -> dict[str, Any]:
    """Node ``average_over_phases`` -- method card #88.

    Harding-Pagan BBQ (Quarterly Bry-Boschan turning points).

    Category 19-business-cycle-dating; memory class ``light``.

    Args:
        series: [series_handle, required] Handle to a univariate ts series of the same frequency as
            the dating.
        dates: [raw_handle, required] Handle to a BCDating object (from date_business_cycles
            register).

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
        "average_over_phases: not implemented."
    )
