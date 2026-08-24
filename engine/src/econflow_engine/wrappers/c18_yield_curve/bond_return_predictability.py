# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bond_return_predictability`` -- method card #539.

#539 Bond excess-return predictability and the Cochrane-Piazzesi factor

Category 18-yield-curve; module ``bond_return_predictability``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c18_yield_curve import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "yc_bond_return_predictability",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def yc_bond_return_predictability(
    *,
    yields: pd.DataFrame,
    maturities: Sequence[float],
    holding_period: int | None = None,
    factor: bool | None = None,
    cov_type: Literal["hac", "hodrick", "robust"] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``yc_bond_return_predictability`` -- method card #539.

    Bond excess-return predictability and the Cochrane-Piazzesi factor.

    Category 18-yield-curve; memory class ``light``.

    Args:
        yields: [df_handle, required] Yield panel.
        maturities: [num_array, required] Maturities in years.
        holding_period: [integer, optional] Holding period in months. Default ``12``.
        factor: [boolean, optional] Construct the single return-forecasting factor. Default
            ``True``.
        cov_type: [enum, optional] Covariance estimator. Default ``'hac'``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

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
        "yc_bond_return_predictability: not implemented."
    )
