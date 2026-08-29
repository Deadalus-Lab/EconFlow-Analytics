# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bootstrap_iid`` -- method card #300.

#300 IID and residual bootstrap with BCa and percentile-t intervals

Category 35-resampling-inference; module ``bootstrap_iid``.

Reference implementation: arch.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c35_resampling_inference import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "rs_bootstrap_iid",
    "rs_bootstrap_residual",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def rs_bootstrap_iid(
    *,
    data: pd.DataFrame,
    statistic: str,
    nboot: int | None = None,
    method: Literal["percentile", "basic", "bca", "percentile_t", "studentized"] | None = None,
    seed: int,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``rs_bootstrap_iid`` -- method card #300.

    IID and residual bootstrap with BCa and percentile-t intervals.

    Category 35-resampling-inference; memory class ``heavy``.

    Args:
        data: [df_handle, required] Data to resample.
        statistic: [formula, required] Statistic to bootstrap.
        nboot: [integer, optional] Number of bootstrap replications. Default ``999``.
        method: [enum, optional] Interval construction. Default ``'bca'``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.
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
        "rs_bootstrap_iid: not implemented."
    )


def rs_bootstrap_residual(
    *,
    fit: Any,
    nboot: int | None = None,
    wild: bool | None = None,
    seed: int,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``rs_bootstrap_residual`` -- method card #300.

    IID and residual bootstrap with BCa and percentile-t intervals.

    Category 35-resampling-inference; memory class ``heavy``.

    Args:
        fit: [raw_handle, required] Handle to a fitted regression.
        nboot: [integer, optional] Number of bootstrap replications. Default ``999``.
        wild: [boolean, optional] Use wild rather than iid residual resampling. Default ``False``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.
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
        "rs_bootstrap_residual: not implemented."
    )
