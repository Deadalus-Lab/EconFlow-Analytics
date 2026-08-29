# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``subsampling_jackknife`` -- method card #307.

#307 Subsampling and jackknife

Category 35-resampling-inference; module ``subsampling_jackknife``.

Reference implementation: 10.1214/aos/1176325770.

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
    "rs_jackknife",
    "rs_subsampling",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


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
        "rs_jackknife: not implemented."
    )
