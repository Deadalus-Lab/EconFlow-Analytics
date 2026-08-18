# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``seasonal_unit_roots`` -- METHOD-SELECTION card #89.

#89 Seasonal unit roots & seasonal stability (HEGY / Canova-Hansen)

Category 01-preparation-prechecks; module ``seasonal_unit_roots``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "run_ch_test",
    "run_hegy_test",
    "NODE_META",
    "wire_model",
]


def run_hegy_test(
    *,
    x: pd.Series,
    lag_method: Literal["fixed", "AIC", "BIC", "AICc"] | None = None,
    maxlag: int | None = None,
    pvalue: Literal["RS", "raw"] | None = None,
    bootstrap: bool | None = None,
    boot_nb: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``run_hegy_test`` -- METHOD-SELECTION card #89.

    Seasonal unit roots & seasonal stability (HEGY / Canova-Hansen).

    Category 01-preparation-prechecks; memory class ``heavy``.

    Args:
        x: [series_handle, required] Handle to a seasonal univariate ts (frequency>1, no NA).
        lag_method: [enum, optional] Lag augmentation selection (default fixed).
        maxlag: [integer, optional] Maximum lag order (default 0). Default ``0``.
        pvalue: [enum, optional] P-values: response-surface (RS) or raw (default RS).
        bootstrap: [boolean, optional] Deterministic bootstrap p-values (CPU, default False).
            Default ``False``.
        boot_nb: [integer, optional] Number of bootstrap replicates (default 1000). Default
            ``1000``.
        seed: [integer, optional] Seed for a reproducible bootstrap (default 123). Default ``123``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "run_hegy_test: not implemented. The method card is in ./README.md."
    )


def run_ch_test(
    *,
    x: pd.Series,
    type: Literal["dummy", "trigonometric"] | None = None,
    lag1: bool | None = None,
    pvalue: Literal["RS", "raw"] | None = None,
) -> dict[str, Any]:
    """Node ``run_ch_test`` -- METHOD-SELECTION card #89.

    Seasonal unit roots & seasonal stability (HEGY / Canova-Hansen).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a seasonal univariate ts (frequency>1, no NA).
        type: [enum, optional] Seasonal representation: dummy or trigonometric (default dummy).
        lag1: [boolean, optional] Include a first-order lag (default False). Default ``False``.
        pvalue: [enum, optional] P-values: response-surface (RS) or raw (default RS).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "run_ch_test: not implemented. The method card is in ./README.md."
    )
