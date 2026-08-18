# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``real_time_revision`` -- METHOD-SELECTION card #229.

#229 Real-time data-revision analysis (vintages: a triangle, revision statistics,
    news-vs-noise/efficiency tests, a state-space nowcast)

Category 23-real-time-revisions; module ``real_time_revision``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c23_real_time_revisions import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "analyze_revisions",
    "build_revision_triangle",
    "compute_revisions",
    "first_efficient_release",
    "nowcast_revisions",
    "NODE_META",
    "wire_model",
]


def build_revision_triangle(
    *,
    df: pd.DataFrame,
) -> dict[str, Any]:
    """Node ``build_revision_triangle`` -- METHOD-SELECTION card #229.

    Real-time data-revision analysis (vintages: a triangle, revision statistics,
    news-vs-noise/efficiency tests, a state-space nowcast).

    Category 23-real-time-revisions; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a long vintage DataFrame {time(Date), pub_date(Date),
            value(numeric)} of A SINGLE series; >= 2 vintages & >= 2 reference periods.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "build_revision_triangle: not implemented. The method card is in ./README.md."
    )


def compute_revisions(
    *,
    df: pd.DataFrame,
    mode: Literal["interval", "nth_release", "ref_date"] | None = None,
    interval: int | None = None,
    nth_release: str | None = None,
    ref_date: str | None = None,
) -> dict[str, Any]:
    """Node ``compute_revisions`` -- METHOD-SELECTION card #229.

    Real-time data-revision analysis (vintages: a triangle, revision statistics,
    news-vs-noise/efficiency tests, a state-space nowcast).

    Category 23-real-time-revisions; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a long vintage DataFrame {time, pub_date, value}.
        mode: [enum, optional] Revision-computation reference (default interval): interval=lag in
            vintages; nth_release=nth release; ref_date=fixed publication date.
        interval: [integer, optional] mode='interval': positive integer lag in vintages (default 1).
            Default ``1``.
        nth_release: [string, optional] mode='nth_release': "latest" or a non-negative integer (as a
            string, e.g. "0").
        ref_date: [string, optional] mode='ref_date': publication date 'YYYY-MM-DD' that EXISTS in
            the data.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "compute_revisions: not implemented. The method card is in ./README.md."
    )


def analyze_revisions(
    *,
    df: pd.DataFrame,
    n_releases: int | None = None,
    final_release: str | None = None,
    degree: int | None = None,
) -> dict[str, Any]:
    """Node ``analyze_revisions`` -- METHOD-SELECTION card #229.

    Real-time data-revision analysis (vintages: a triangle, revision statistics,
    news-vs-noise/efficiency tests, a state-space nowcast).

    Category 23-real-time-revisions; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a long vintage DataFrame {time, pub_date, value}.
        n_releases: [integer, optional] Number of initial releases to analyze (0..n_releases;
            default 3). Default ``3``.
        final_release: [string, optional] Final release as benchmark: "latest" (default) or an
            integer-string (e.g. "10").
        degree: [integer, optional] Detail level 1..5 (default 5=all): 1 magnitude/bias; 2
            correlation; 3 news/noise tests; 4 Theil/sign/seasonality; 5 full. Default ``5``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "analyze_revisions: not implemented. The method card is in ./README.md."
    )


def first_efficient_release(
    *,
    df: pd.DataFrame,
    n_releases: int | None = None,
    final_release: str | None = None,
    significance: float | None = None,
    robust: bool | None = None,
    test_all: bool | None = None,
) -> dict[str, Any]:
    """Node ``first_efficient_release`` -- METHOD-SELECTION card #229.

    Real-time data-revision analysis (vintages: a triangle, revision statistics,
    news-vs-noise/efficiency tests, a state-space nowcast).

    Category 23-real-time-revisions; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a long vintage DataFrame {time, pub_date, value}.
        n_releases: [integer, optional] Number of releases to check (0..n_releases; default 5).
            Default ``5``.
        final_release: [string, optional] Final release benchmark: "latest" (default) or an
            integer-string.
        significance: [number, optional] Significance level of the joint MZ test in (0,1) (default
            0.05). Default ``0.05``.
        robust: [boolean, optional] HAC (Newey-West) robust standard errors (default True). Default
            ``True``.
        test_all: [boolean, optional] Check of ALL releases (default False = stop at the 1st
            efficient one). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "first_efficient_release: not implemented. The method card is in ./README.md."
    )


def nowcast_revisions(
    *,
    df: pd.DataFrame,
    e: int,
    n_releases: int | None = None,
    method: Literal["jvn", "kk"] | None = None,
    h: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``nowcast_revisions`` -- METHOD-SELECTION card #229.

    Real-time data-revision analysis (vintages: a triangle, revision statistics,
    news-vs-noise/efficiency tests, a state-space nowcast).

    Category 23-real-time-revisions; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a long vintage DataFrame {time, pub_date, value}.
        e: [integer, required] Index of the first efficient release (> 0; from
            first_efficient_release$e); e < n_releases is required.
        n_releases: [integer, optional] Number of releases for the state-space (0..n_releases;
            default 6). Default ``6``.
        method: [enum, optional] Model (default jvn): jvn=Jacobs-van Norden news/noise;
            kk=Kishor-Koenig.
        h: [integer, optional] Forecast horizon (non-negative integer; default 0). Default ``0``.
        seed: [integer, optional] Seed before the MLE (determinism; default 1). Default ``1``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "nowcast_revisions: not implemented. The method card is in ./README.md."
    )
