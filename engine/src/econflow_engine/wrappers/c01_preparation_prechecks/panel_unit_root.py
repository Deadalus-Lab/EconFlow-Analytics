# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``panel_unit_root`` -- method card #6.

#6 Panel unit-root (LLC/IPS/Fisher/Hadri + Pesaran CIPS)

Category 01-preparation-prechecks; module ``panel_unit_root``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "make_panel_frame",
    "run_cipstest",
    "run_panel_unit_root",
    "NODE_META",
    "wire_model",
]


def run_panel_unit_root(
    *,
    object: pd.DataFrame,
    test: Literal["levinlin", "ips", "madwu", "Pm", "invnormal", "logit", "hadri"] | None = None,
    exo: Literal["none", "intercept", "trend"] | None = None,
    lags: Literal["SIC", "AIC", "Hall"] | None = None,
    pmax: int | None = None,
) -> dict[str, Any]:
    """Node ``run_panel_unit_root`` -- method card #6.

    Panel unit-root (LLC/IPS/Fisher/Hadri + Pesaran CIPS).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        object: [df_handle, required] Handle to a DataFrame/matrix with the individuals IN COLUMNS.
        test: [enum, optional] Panel unit-root test (default levinlin = Levin-Lin-Chu).
        exo: [enum, optional] Deterministic terms (default none).
        lags: [enum, optional] Lag selection criterion of the ADF regressions (default SIC).
        pmax: [integer, optional] Maximum number of lags (default 10· irrelevant for hadri). Default
            ``10``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "run_panel_unit_root: not implemented."
    )


def run_cipstest(
    *,
    x: Any,
    lags: int | None = None,
    type: Literal["trend", "drift", "none"] | None = None,
    model: Literal["cmg", "mg", "dmg"] | None = None,
    truncated: bool | None = None,
) -> dict[str, Any]:
    """Node ``run_cipstest`` -- method card #6.

    Panel unit-root (LLC/IPS/Fisher/Hadri + Pesaran CIPS).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to a panel column · second-generation CIPS.
        lags: [integer, optional] Lag order of the Dickey-Fuller augmentation (default 2). Default
            ``2``.
        type: [enum, optional] Deterministic terms (default trend).
        model: [enum, optional] CIPS variant: cmg/mg/dmg (default cmg).
        truncated: [boolean, optional] Truncated version of the test (default False). Default
            ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "run_cipstest: not implemented."
    )


def make_panel_frame(
    *,
    x: pd.DataFrame,
    index: Sequence[str] | None = None,
    drop_index: bool | None = None,
) -> dict[str, Any]:
    """Node ``make_panel_frame`` -- method card #6.

    Panel unit-root (LLC/IPS/Fisher/Hadri + Pesaran CIPS).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [df_handle, required] Handle to a long-format panel DataFrame.
        index: [series_codes, optional] Index column names, e.g. ['firm','year'] (default None).
        drop_index: [boolean, optional] Exclude the index columns from the result (default False).
            Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "make_panel_frame: not implemented."
    )
