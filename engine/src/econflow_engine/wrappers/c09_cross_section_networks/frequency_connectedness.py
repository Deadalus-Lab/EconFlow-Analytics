# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``frequency_connectedness`` -- METHOD-SELECTION card #52.

#52 Frequency connectedness (Baruník-Křehlík)

Category 09-cross-section-networks; module ``frequency_connectedness``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c09_cross_section_networks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "fq_collapse_bounds",
    "fq_fevd",
    "fq_from",
    "fq_gen_fevd",
    "fq_get_partition",
    "fq_net",
    "fq_overall",
    "fq_pairwise",
    "fq_spillover_bk09",
    "fq_spillover_bk12",
    "fq_spillover_rolling_bk09",
    "fq_spillover_rolling_bk12",
    "fq_to",
    "NODE_META",
    "wire_model",
]


def fq_spillover_bk12(
    *,
    est: Any,
    n_ahead: int | None = None,
    no_corr: bool | None = None,
    partition: Any | None = None,
) -> dict[str, Any]:
    """Node ``fq_spillover_bk12`` -- METHOD-SELECTION card #52.

    Frequency connectedness (Baruník-Křehlík).

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``spillover_table``, so a later node can consume it as a handle.

    Args:
        est: [raw_handle, required] VAR estimate ('varest' from the vars package).
        n_ahead: [integer, optional] FEVD horizon (default 100). Default ``100``.
        no_corr: [boolean, optional] Zero out the off-diagonal Sigma.
        partition: [raw_handle, optional] Numeric vector of frequency-band bounds (decreasing
            order).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fq_spillover_bk12: not implemented. The method card is in ./README.md."
    )


def fq_spillover_bk09(
    *,
    est: Any,
    n_ahead: int | None = None,
    no_corr: bool | None = None,
    partition: Any | None = None,
) -> dict[str, Any]:
    """Node ``fq_spillover_bk09`` -- METHOD-SELECTION card #52.

    Frequency connectedness (Baruník-Křehlík).

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``spillover_table``, so a later node can consume it as a handle.

    Args:
        est: [raw_handle, required] VAR estimate ('varest' from the vars package).
        n_ahead: [integer, optional] FEVD horizon (default 100). Default ``100``.
        no_corr: [boolean, optional] Zero out the off-diagonal Sigma.
        partition: [raw_handle, optional] Numeric vector of frequency-band bounds (decreasing
            order).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fq_spillover_bk09: not implemented. The method card is in ./README.md."
    )


def fq_spillover_rolling_bk12(
    *,
    data: pd.DataFrame,
    n_ahead: int | None = None,
    no_corr: bool | None = None,
    partition: Any | None = None,
    window: int | None = None,
) -> dict[str, Any]:
    """Node ``fq_spillover_rolling_bk12`` -- METHOD-SELECTION card #52.

    Frequency connectedness (Baruník-Křehlík).

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``list_of_spills``, so a later node can consume it as a handle.

    Args:
        data: [multiseries_handle, required] Multivariate data (rolling VAR internally).
        n_ahead: [integer, optional] FEVD horizon (default 100). Default ``100``.
        no_corr: [boolean, optional] Zero out the off-diagonal Sigma.
        partition: [raw_handle, optional] Numeric vector of frequency-band bounds (decreasing
            order).
        window: [integer, optional] Rolling-window length.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fq_spillover_rolling_bk12: not implemented. The method card is in ./README.md."
    )


def fq_spillover_rolling_bk09(
    *,
    data: pd.DataFrame,
    n_ahead: int | None = None,
    no_corr: bool | None = None,
    partition: Any | None = None,
    window: int | None = None,
) -> dict[str, Any]:
    """Node ``fq_spillover_rolling_bk09`` -- METHOD-SELECTION card #52.

    Frequency connectedness (Baruník-Křehlík).

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``list_of_spills``, so a later node can consume it as a handle.

    Args:
        data: [multiseries_handle, required] Multivariate data (rolling VAR internally).
        n_ahead: [integer, optional] FEVD horizon (default 100). Default ``100``.
        no_corr: [boolean, optional] Zero out the off-diagonal Sigma.
        partition: [raw_handle, optional] Numeric vector of frequency-band bounds (decreasing
            order).
        window: [integer, optional] Rolling-window length.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fq_spillover_rolling_bk09: not implemented. The method card is in ./README.md."
    )


def fq_fevd(
    *,
    est: Any,
    n_ahead: int | None = None,
    no_corr: bool | None = None,
) -> dict[str, Any]:
    """Node ``fq_fevd`` -- METHOD-SELECTION card #52.

    Frequency connectedness (Baruník-Křehlík).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        est: [raw_handle, required] VAR estimate ('varest' from the vars package).
        n_ahead: [integer, optional] FEVD horizon (default 100). Default ``100``.
        no_corr: [boolean, optional] Zero out the off-diagonal Sigma (default False).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fq_fevd: not implemented. The method card is in ./README.md."
    )


def fq_gen_fevd(
    *,
    est: Any,
    n_ahead: int | None = None,
    no_corr: bool | None = None,
) -> dict[str, Any]:
    """Node ``fq_gen_fevd`` -- METHOD-SELECTION card #52.

    Frequency connectedness (Baruník-Křehlík).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        est: [raw_handle, required] VAR estimate ('varest' from the vars package).
        n_ahead: [integer, optional] FEVD horizon (default 100). Default ``100``.
        no_corr: [boolean, optional] Zero out the off-diagonal Sigma (default False).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fq_gen_fevd: not implemented. The method card is in ./README.md."
    )


def fq_get_partition(
    *,
    partition: Any,
    n_ahead: int,
) -> dict[str, Any]:
    """Node ``fq_get_partition`` -- METHOD-SELECTION card #52.

    Frequency connectedness (Baruník-Křehlík).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        partition: [raw_handle, required] Numeric vector of frequency-band bounds (decreasing
            order).
        n_ahead: [integer, required] FEVD horizon.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fq_get_partition: not implemented. The method card is in ./README.md."
    )


def fq_from(
    *,
    spillover_table: Any,
    within: bool | None = None,
) -> dict[str, Any]:
    """Node ``fq_from`` -- METHOD-SELECTION card #52.

    Frequency connectedness (Baruník-Křehlík).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        spillover_table: [raw_handle, required] spillover_table/list_of_spills (fq_spillover_*
            $handle).
        within: [boolean, optional] Within-band (%) instead of absolute (default False).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fq_from: not implemented. The method card is in ./README.md."
    )


def fq_to(
    *,
    spillover_table: Any,
    within: bool | None = None,
) -> dict[str, Any]:
    """Node ``fq_to`` -- METHOD-SELECTION card #52.

    Frequency connectedness (Baruník-Křehlík).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        spillover_table: [raw_handle, required] spillover_table/list_of_spills (fq_spillover_*
            $handle).
        within: [boolean, optional] Within-band (%) instead of absolute (default False).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fq_to: not implemented. The method card is in ./README.md."
    )


def fq_net(
    *,
    spillover_table: Any,
    within: bool | None = None,
) -> dict[str, Any]:
    """Node ``fq_net`` -- METHOD-SELECTION card #52.

    Frequency connectedness (Baruník-Křehlík).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        spillover_table: [raw_handle, required] spillover_table/list_of_spills (fq_spillover_*
            $handle).
        within: [boolean, optional] Within-band (%) instead of absolute (default False).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fq_net: not implemented. The method card is in ./README.md."
    )


def fq_overall(
    *,
    spillover_table: Any,
    within: bool | None = None,
) -> dict[str, Any]:
    """Node ``fq_overall`` -- METHOD-SELECTION card #52.

    Frequency connectedness (Baruník-Křehlík).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        spillover_table: [raw_handle, required] spillover_table/list_of_spills (fq_spillover_*
            $handle).
        within: [boolean, optional] Within-band (%) instead of absolute (default False).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fq_overall: not implemented. The method card is in ./README.md."
    )


def fq_pairwise(
    *,
    spillover_table: Any,
    within: bool | None = None,
) -> dict[str, Any]:
    """Node ``fq_pairwise`` -- METHOD-SELECTION card #52.

    Frequency connectedness (Baruník-Křehlík).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        spillover_table: [raw_handle, required] spillover_table/list_of_spills (fq_spillover_*
            $handle).
        within: [boolean, optional] Within-band (%) instead of absolute (default False).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fq_pairwise: not implemented. The method card is in ./README.md."
    )


def fq_collapse_bounds(
    *,
    spillover_table: Any,
    which: Any,
) -> dict[str, Any]:
    """Node ``fq_collapse_bounds`` -- METHOD-SELECTION card #52.

    Frequency connectedness (Baruník-Křehlík).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        spillover_table: [raw_handle, required] spillover_table/list_of_spills (fq_spillover_*
            $handle).
        which: [raw_handle, required] Contiguous increasing sequence of band indices to merge (e.g.
            1:2).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fq_collapse_bounds: not implemented. The method card is in ./README.md."
    )
