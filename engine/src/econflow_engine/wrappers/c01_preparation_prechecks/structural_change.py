# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``structural_change`` -- method card #3.

#3 Structural change (Bai-Perron multiple breaks / Chow-F / CUSUM)

Category 01-preparation-prechecks; module ``structural_change``.

Reference implementation: ruptures.

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
    "run_breakpoints",
    "run_chow_fstats",
    "run_fluctuation_process",
    "run_structural_change_test",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def run_breakpoints(
    *,
    formula: str,
    data: pd.DataFrame | None = None,
    h: float | None = None,
    breaks: int | None = None,
    ci_level: float | None = None,
    n_breaks_extract: int | None = None,
) -> dict[str, Any]:
    """Node ``run_breakpoints`` -- method card #3.

    Structural change (Bai-Perron multiple breaks / Chow-F / CUSUM).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        formula: [formula, required] Model of the segment under test, e.g. 'y ~ 1' (mean shift).
        data: [df_handle, optional] Handle to a DataFrame holding the formula variables.
        h: [number, optional] Minimum segment size (fraction, default 0.15). Default ``0.15``.
        breaks: [integer, optional] Maximum number of breaks (default None -> from BIC).
        ci_level: [number, optional] Confidence level of the breakpoint CIs (default 0.95). Default
            ``0.95``.
        n_breaks_extract: [integer, optional] Extract the solution with exactly k breaks instead of
            min-BIC.

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
        "run_breakpoints: not implemented."
    )


def run_chow_fstats(
    *,
    formula: str,
    data: pd.DataFrame | None = None,
    from_: float | None = None,
) -> dict[str, Any]:
    """Node ``run_chow_fstats`` -- method card #3.

    Structural change (Bai-Perron multiple breaks / Chow-F / CUSUM).

    Category 01-preparation-prechecks; memory class ``light``.

    Registers its result under ``fstats_object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] Model, e.g. 'y ~ 1' (Chow F per candidate break).
        data: [df_handle, optional] Handle to a DataFrame holding the formula variables.
        from_ (wire name ``from``): [number, optional] Window start (fraction <1 or index, default
            0.15). Default ``0.15``.

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
        "run_chow_fstats: not implemented."
    )


def run_fluctuation_process(
    *,
    formula: str,
    data: pd.DataFrame | None = None,
    type: (
        Literal[
            "Rec-CUSUM",
            "OLS-CUSUM",
            "Rec-MOSUM",
            "OLS-MOSUM",
            "RE",
            "ME",
            "Score-CUSUM",
            "Score-MOSUM",
        ]
        | None
    ) = None,
    h: float | None = None,
    dynamic: bool | None = None,
) -> dict[str, Any]:
    """Node ``run_fluctuation_process`` -- method card #3.

    Structural change (Bai-Perron multiple breaks / Chow-F / CUSUM).

    Category 01-preparation-prechecks; memory class ``light``.

    Registers its result under ``efp_object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] Model, e.g. 'y ~ 1' for the fluctuation process.
        data: [df_handle, optional] Handle to a DataFrame holding the formula variables.
        type: [enum, optional] Type of empirical fluctuation process (default Rec-CUSUM).
        h: [number, optional] Bandwidth (MOSUM/ME only, default 0.15). Default ``0.15``.
        dynamic: [boolean, optional] Include the lagged response as a regressor (default False).
            Default ``False``.

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
        "run_fluctuation_process: not implemented."
    )


def run_structural_change_test(
    *,
    x: Any,
    type: Literal["supF", "aveF", "expF"] | None = None,
    asymptotic: bool | None = None,
) -> dict[str, Any]:
    """Node ``run_structural_change_test`` -- method card #3.

    Structural change (Bai-Perron multiple breaks / Chow-F / CUSUM).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to an 'Fstats' (from run_chow_fstats) or an 'efp' (from
            run_fluctuation_process).
        type: [enum, optional] Aggregation of the Fstats test (default supF· ignored for efp).
        asymptotic: [boolean, optional] Asymptotic distribution (single-F supF/aveF, default False).
            Default ``False``.

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
        "run_structural_change_test: not implemented."
    )
