# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``ts_features`` -- method card #402.

#402 Time-series feature extraction at scale

Category 01-preparation-prechecks; module ``ts_features``.

Reference implementation: tsfresh.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pp_extract_features",
    "pp_select_features",
    "NODE_META",
    "wire_model",
]


def pp_extract_features(
    *,
    data: pd.DataFrame,
    id: str,
    time: str,
    value: str,
    feature_set: Literal["minimal", "efficient", "comprehensive"] | None = None,
    normalise: bool | None = None,
) -> dict[str, Any]:
    """Node ``pp_extract_features`` -- method card #402.

    Time-series feature extraction at scale.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        data: [df_handle, required] Long-format panel: identifier, time and value.
        id: [string, required] Column identifying the series.
        time: [string, required] Column holding the time index.
        value: [string, required] Column holding the value.
        feature_set: [enum, optional] Breadth of the feature set. Default ``'efficient'``.
        normalise: [boolean, optional] Normalise each series before extraction. Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pp_extract_features: not implemented."
    )


def pp_select_features(
    *,
    features: pd.DataFrame,
    target: pd.Series,
    fdr_level: float | None = None,
) -> dict[str, Any]:
    """Node ``pp_select_features`` -- method card #402.

    Time-series feature extraction at scale.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        features: [df_handle, required] Extracted feature matrix.
        target: [series_handle, required] Target the features are screened against.
        fdr_level: [number, optional] False-discovery rate for the filter. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pp_select_features: not implemented."
    )
