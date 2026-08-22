# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``mixed_logit`` -- method card #272.

#272 Mixed and random-parameters logit for panel choice data

Category 31-discrete-choice-demand; module ``mixed_logit``.

Reference implementation: xlogit.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c31_discrete_choice_demand import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "dcd_mixed_logit_fit",
    "dcd_mixed_logit_individual",
    "NODE_META",
    "wire_model",
]


def dcd_mixed_logit_fit(
    *,
    data: pd.DataFrame,
    chooser: str,
    chosen: str,
    covariates: Sequence[str] | None = None,
    random: Sequence[str] | None = None,
    distributions: Sequence[str] | None = None,
    n_draws: int | None = None,
    panel: str | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``dcd_mixed_logit_fit`` -- method card #272.

    Mixed and random-parameters logit for panel choice data.

    Category 31-discrete-choice-demand; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Long-format choice data: one row per chooser per alternative.
        chooser: [string, required] Column identifying the chooser.
        chosen: [string, required] Column flagging the chosen row.
        covariates: [series_codes, optional] Covariate columns.
        random: [series_codes, optional] Covariates carrying a random coefficient.
        distributions: [series_codes, optional] Mixing distribution per random coefficient.
        n_draws: [integer, optional] Number of simulation draws. Default ``600``.
        panel: [string, optional] Column identifying the panel unit when choices repeat.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dcd_mixed_logit_fit: not implemented."
    )


def dcd_mixed_logit_individual(
    *,
    fit: Any,
) -> dict[str, Any]:
    """Node ``dcd_mixed_logit_individual`` -- method card #272.

    Mixed and random-parameters logit for panel choice data.

    Category 31-discrete-choice-demand; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted mixed logit.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dcd_mixed_logit_individual: not implemented."
    )
