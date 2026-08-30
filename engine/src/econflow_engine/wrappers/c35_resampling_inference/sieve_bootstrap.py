# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``sieve_bootstrap`` -- method card #303.

#303 Sieve and autoregressive bootstrap

Category 35-resampling-inference; module ``sieve_bootstrap``.

Reference implementation: 10.2307/3318584.

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
    "rs_sieve_bootstrap",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def rs_sieve_bootstrap(
    *,
    x: pd.Series,
    statistic: str,
    ar_order: int | None = None,
    criterion: Literal["aic", "bic", "hqic"] | None = None,
    nboot: int | None = None,
    seed: int,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``rs_sieve_bootstrap`` -- method card #303.

    Sieve and autoregressive bootstrap.

    Category 35-resampling-inference; memory class ``heavy``.

    Args:
        x: [series_handle, required] Serially dependent series.
        statistic: [formula, required] Statistic to bootstrap.
        ar_order: [integer, optional] Autoregressive order; omitted = selected.
        criterion: [enum, optional] Order-selection criterion. Default ``'aic'``.
        nboot: [integer, optional] Number of bootstrap replications. Default ``999``.
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
        "rs_sieve_bootstrap: not implemented."
    )
