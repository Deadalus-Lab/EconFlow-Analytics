# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``km_nelson_aalen`` -- method card #258.

#258 Kaplan-Meier and Nelson-Aalen estimators with the log-rank family of tests

Category 30-duration-survival; module ``km_nelson_aalen``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c30_duration_survival import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "srv_km_fit",
    "srv_logrank_test",
    "srv_na_fit",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def srv_km_fit(
    *,
    time: pd.Series,
    event: pd.Series,
    weights: pd.Series | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``srv_km_fit`` -- method card #258.

    Kaplan-Meier and Nelson-Aalen estimators with the log-rank family of tests.

    Category 30-duration-survival; memory class ``light``.

    Args:
        time: [series_handle, required] Observed duration for each unit.
        event: [series_handle, required] Event indicator: 1 = event observed, 0 = right-censored.
        weights: [series_handle, optional] Optional observation weights.
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
        "srv_km_fit: not implemented."
    )


def srv_na_fit(
    *,
    time: pd.Series,
    event: pd.Series,
    weights: pd.Series | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``srv_na_fit`` -- method card #258.

    Kaplan-Meier and Nelson-Aalen estimators with the log-rank family of tests.

    Category 30-duration-survival; memory class ``light``.

    Args:
        time: [series_handle, required] Observed duration for each unit.
        event: [series_handle, required] Event indicator: 1 = event observed, 0 = right-censored.
        weights: [series_handle, optional] Optional observation weights.
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
        "srv_na_fit: not implemented."
    )


def srv_logrank_test(
    *,
    time: pd.Series,
    event: pd.Series,
    group: pd.Series,
    weighting: (
        Literal[
            "logrank",
            "wilcoxon",
            "tarone-ware",
            "peto",
            "fleming-harrington",
        ]
        | None
    ) = None,
) -> dict[str, Any]:
    """Node ``srv_logrank_test`` -- method card #258.

    Kaplan-Meier and Nelson-Aalen estimators with the log-rank family of tests.

    Category 30-duration-survival; memory class ``light``.

    Args:
        time: [series_handle, required] Observed duration for each unit.
        event: [series_handle, required] Event indicator.
        group: [series_handle, required] Group label for each unit.
        weighting: [enum, optional] Weight function on the event times. Default ``'logrank'``.

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
        "srv_logrank_test: not implemented."
    )
