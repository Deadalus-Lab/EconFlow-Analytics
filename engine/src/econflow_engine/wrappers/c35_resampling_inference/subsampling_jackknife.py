# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``subsampling_jackknife`` -- method card #307.

#307 Subsampling and jackknife

Category 35-resampling-inference; module ``subsampling_jackknife``.

Reference implementation: arch.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c35_resampling_inference import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "rs_jackknife",
    "rs_subsampling",
    "NODE_META",
    "wire_model",
]


def rs_subsampling(
    *,
    data: pd.DataFrame,
    statistic: str,
    subsample_size: int | None = None,
    n_subsamples: int | None = None,
    seed: int,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``rs_subsampling`` -- method card #307.

    Subsampling and jackknife.

    Category 35-resampling-inference; memory class ``light``.

    Args:
        data: [df_handle, required] Data to subsample.
        statistic: [formula, required] Statistic of interest.
        subsample_size: [integer, optional] Subsample size b; omitted = n^(2/3).
        n_subsamples: [integer, optional] Number of subsamples. Default ``1000``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rs_subsampling: not implemented."
    )


def rs_jackknife(
    *,
    data: pd.DataFrame,
    statistic: str,
    kind: Literal["delete1", "deleted", "cluster"] | None = None,
    d: int | None = None,
    cluster: pd.Series | None = None,
) -> dict[str, Any]:
    """Node ``rs_jackknife`` -- method card #307.

    Subsampling and jackknife.

    Category 35-resampling-inference; memory class ``light``.

    Args:
        data: [df_handle, required] Data to resample.
        statistic: [formula, required] Statistic of interest.
        kind: [enum, optional] Jackknife variant. Default ``'delete1'``.
        d: [integer, optional] Number deleted for the delete-d variant. Default ``1``.
        cluster: [series_handle, optional] Cluster identifier for the cluster variant.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rs_jackknife: not implemented."
    )
