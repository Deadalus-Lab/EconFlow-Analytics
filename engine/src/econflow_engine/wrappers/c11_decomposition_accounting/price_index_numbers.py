# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``price_index_numbers`` -- method card #190.

#190 Price index numbers (bilateral/multilateral/spliced) + CPI-subindex contribution decompositions

Category 11-decomposition-accounting; module ``price_index_numbers``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c11_decomposition_accounting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pi_bilateral",
    "pi_contributions",
    "pi_multilateral",
    "pi_splice",
    "NODE_META",
    "wire_model",
]


def pi_bilateral(
    *,
    data: pd.DataFrame,
    start: str,
    end: str,
    formula: (
        Literal[
            "jevons",
            "dutot",
            "carli",
            "laspeyres",
            "paasche",
            "fisher",
            "tornqvist",
            "walsh",
        ]
        | None
    ) = None,
    interval: bool | None = None,
) -> dict[str, Any]:
    """Node ``pi_bilateral`` -- method card #190.

    Price index numbers (bilateral/multilateral/spliced) + CPI-subindex contribution decompositions.

    Category 11-decomposition-accounting; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to long-format micro-data (columns
            time,prices,quantities,prodID).
        start: [string, required] Period start 'YYYY-MM' (base = start = 1).
        end: [string, required] Period end 'YYYY-MM' (must be start <= end).
        formula: [enum, optional] Bilateral index formula (default jevons· fisher/tornqvist =
            superlative baseline).
        interval: [boolean, optional] True -> full monthly series with dates· False -> a single
            end-vs-start index (default). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pi_bilateral: not implemented."
    )


def pi_multilateral(
    *,
    data: pd.DataFrame,
    start: str,
    end: str,
    method: Literal["geks", "ccdi", "gk", "tpd"] | None = None,
    window: int | None = None,
    wstart: str | None = None,
) -> dict[str, Any]:
    """Node ``pi_multilateral`` -- method card #190.

    Price index numbers (bilateral/multilateral/spliced) + CPI-subindex contribution decompositions.

    Category 11-decomposition-accounting; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to long-format micro-data
            (time,prices,quantities,prodID).
        start: [string, required] Start 'YYYY-MM'.
        end: [string, required] End 'YYYY-MM' (start <= end).
        method: [enum, optional] Multilateral method (default geks· gk = rolling Geary-Khamis).
        window: [integer, optional] Rolling window length in months (>=2· default 13· <= available
            months). Default ``13``.
        wstart: [string, optional] Estimation window start 'YYYY-MM' (default None = start of the
            data).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pi_multilateral: not implemented."
    )


def pi_splice(
    *,
    data: pd.DataFrame,
    start: str,
    end: str,
    method: Literal["geks", "ccdi", "gk", "tpd"] | None = None,
    window: int | None = None,
    splice: (
        Literal[
            "movement",
            "window",
            "half",
            "mean",
            "window_published",
            "half_published",
            "mean_published",
        ]
        | None
    ) = None,
    interval: bool | None = None,
) -> dict[str, Any]:
    """Node ``pi_splice`` -- method card #190.

    Price index numbers (bilateral/multilateral/spliced) + CPI-subindex contribution decompositions.

    Category 11-decomposition-accounting; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to long-format micro-data
            (time,prices,quantities,prodID).
        start: [string, required] Start 'YYYY-MM'.
        end: [string, required] End 'YYYY-MM' (start <= end).
        method: [enum, optional] Multilateral base for splicing (default geks).
        window: [integer, optional] Rolling window length in months (>=2· default 13). Default
            ``13``.
        splice: [enum, optional] Splicing method of the multilateral series (default movement).
        interval: [boolean, optional] True -> full spliced series with dates· False -> a single
            index (default). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pi_splice: not implemented."
    )


def pi_contributions(
    *,
    data: pd.DataFrame,
    start: str,
    end: str,
    method: Literal["bennet", "montgomery"] | None = None,
    matched: bool | None = None,
    interval: bool | None = None,
    prec: int | None = None,
) -> dict[str, Any]:
    """Node ``pi_contributions`` -- method card #190.

    Price index numbers (bilateral/multilateral/spliced) + CPI-subindex contribution decompositions.

    Category 11-decomposition-accounting; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to long-format micro-data
            (time,prices,quantities,prodID).
        start: [string, required] Start 'YYYY-MM'.
        end: [string, required] End 'YYYY-MM' (start <= end).
        method: [enum, optional] Value-change decomposition indicator (default bennet· identity
            value=price+quantity).
        matched: [boolean, optional] True -> only products matched in both periods (default False).
            Default ``False``.
        interval: [boolean, optional] True -> per-month contributions· False -> cumulative
            end-vs-start (default). Default ``False``.
        prec: [integer, optional] Rounding decimal digits of the contributions (>=0· default 2).
            Default ``2``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pi_contributions: not implemented."
    )
