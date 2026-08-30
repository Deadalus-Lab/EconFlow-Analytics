# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``fixed_effects_individual`` -- method card #173.

#173 Fixed-Effects Individual-Slopes (FEIS) + a slope-heterogeneity Hausman test (artificial &
    bootstrapped)

Category 08-panel-data; module ``fixed_effects_individual``.

Reference implementation: 10.1177/0049124120926211.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c08_panel_data import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "feis_bootstrap_test",
    "feis_fit",
    "feis_slopes",
    "feis_test",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def feis_fit(
    *,
    formula: str,
    data: pd.DataFrame,
    id: str,
    robust: bool | None = None,
    intercept: bool | None = None,
    dropgroups: bool | None = None,
) -> dict[str, Any]:
    """Node ``feis_fit`` -- method card #173.

    Fixed-Effects Individual-Slopes (FEIS) + a slope-heterogeneity Hausman test (artificial &
    bootstrapped).

    Category 08-panel-data; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] Two-part FEIS formula 'y ~ x1 + x2 | slope1 + slope2' (the '|'
            is required· for conventional FE: 'y ~ x | 1').
        data: [df_handle, required] Handle to a panel DataFrame (long format) with the id column +
            the variables.
        id: [string, required] Column name (string) of the unique group/person identifier.
        robust: [boolean, optional] True -> panel/cluster-robust SE (default False). Default
            ``False``.
        intercept: [boolean, optional] True -> estimation with intercept (default False). Default
            ``False``.
        dropgroups: [boolean, optional] True -> drop groups without within-variance in the slope var
            (default False: omit per group). Default ``False``.

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
        "feis_fit: not implemented."
    )


def feis_test(
    *,
    object: Any,
    type: Literal["all", "art1", "art2", "art3"] | None = None,
    robust: bool | None = None,
    terms: Any | None = None,
) -> dict[str, Any]:
    """Node ``feis_test`` -- method card #173.

    Fixed-Effects Individual-Slopes (FEIS) + a slope-heterogeneity Hausman test (artificial &
    bootstrapped).

    Category 08-panel-data; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a 'feis' model (from feis_fit).
        type: [enum, optional] art1=FEIS vs FE, art2=FE vs RE, art3=FEIS vs RE (default all).
        robust: [boolean, optional] True -> cluster-robust SE in the artificial regression (default
            False). Default ``False``.
        terms: [raw, optional] Optional character vector of coefficients for a joint Wald test
            (default: all).

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
        "feis_test: not implemented."
    )


def feis_bootstrap_test(
    *,
    object: Any,
    type: Literal["all", "bs1", "bs2", "bs3"] | None = None,
    rep: int | None = None,
    seed: int | None = None,
    terms: Any | None = None,
) -> dict[str, Any]:
    """Node ``feis_bootstrap_test`` -- method card #173.

    Fixed-Effects Individual-Slopes (FEIS) + a slope-heterogeneity Hausman test (artificial &
    bootstrapped).

    Category 08-panel-data; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a 'feis' model (from feis_fit).
        type: [enum, optional] bs1=FEIS vs FE, bs2=FE vs RE, bs3=FEIS vs RE (default all).
        rep: [integer, optional] Pairs-cluster bootstrap replications (default 500). Default
            ``500``.
        seed: [integer, optional] Reproducibility seed of the bootstrap (default 2025). Default
            ``2025``.
        terms: [raw, optional] Optional character vector of coefficients for a joint Wald test
            (default: all).

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
        "feis_bootstrap_test: not implemented."
    )


def feis_slopes(
    *,
    object: Any,
) -> dict[str, Any]:
    """Node ``feis_slopes`` -- method card #173.

    Fixed-Effects Individual-Slopes (FEIS) + a slope-heterogeneity Hausman test (artificial &
    bootstrapped).

    Category 08-panel-data; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a 'feis' model (from feis_fit)· returns the N x J
            matrix of alpha_i.

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
        "feis_slopes: not implemented."
    )
