# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``single_index_varying`` -- method card #289.

#289 Single-index and varying-coefficient models

Category 33-nonparametric-semiparametric; module ``single_index_varying``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c33_nonparametric_semiparametric import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "np_single_index",
    "np_varying_coefficient",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def np_single_index(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    bandwidth: float | None = None,
    normalisation: Literal["first_unit", "unit_norm"] | None = None,
) -> dict[str, Any]:
    """Node ``np_single_index`` -- method card #289.

    Single-index and varying-coefficient models.

    Category 33-nonparametric-semiparametric; memory class ``light``.

    Args:
        y: [series_handle, required] Dependent variable.
        x: [multiseries_handle, required] Covariates entering the index.
        bandwidth: [number, optional] Smoothing bandwidth for the link.
        normalisation: [enum, optional] Identifying normalisation. Default ``'first_unit'``.

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
        "np_single_index: not implemented."
    )


def np_varying_coefficient(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    modifier: pd.Series,
    bandwidth: float | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``np_varying_coefficient`` -- method card #289.

    Single-index and varying-coefficient models.

    Category 33-nonparametric-semiparametric; memory class ``light``.

    Args:
        y: [series_handle, required] Dependent variable.
        x: [multiseries_handle, required] Covariates whose coefficients vary.
        modifier: [series_handle, required] Variable the coefficients vary with.
        bandwidth: [number, optional] Smoothing bandwidth.
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
        "np_varying_coefficient: not implemented."
    )
