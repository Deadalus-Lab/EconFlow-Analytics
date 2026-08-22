# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``anomaly_detection`` -- method card #401.

#401 Unsupervised anomaly detection: isolation forest, local outlier factor and one-class SVM

Category 01-preparation-prechecks; module ``anomaly_detection``.

Reference implementation: scikit-learn.

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
    "pp_anomaly_detect",
    "NODE_META",
    "wire_model",
]


def pp_anomaly_detect(
    *,
    data: pd.DataFrame,
    method: (
        Literal[
            "isolation_forest",
            "local_outlier_factor",
            "one_class_svm",
            "elliptic_envelope",
        ]
        | None
    ) = None,
    contamination: float | None = None,
    n_neighbors: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``pp_anomaly_detect`` -- method card #401.

    Unsupervised anomaly detection: isolation forest, local outlier factor and one-class SVM.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        data: [df_handle, required] Observations to screen.
        method: [enum, optional] Detector. Default ``'isolation_forest'``.
        contamination: [number, optional] Assumed anomaly rate. Default ``0.05``.
        n_neighbors: [integer, optional] Neighbours for the local outlier factor. Default ``20``.
        seed: [integer, optional] Seed for the random number generator.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pp_anomaly_detect: not implemented."
    )
