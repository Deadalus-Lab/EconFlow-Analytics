# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``static_panel_estimators`` -- method cards #46, #47.

#46 Static panel estimators (FE/RE/pooling/between/FD) + Hausman/LM/F
#47 Dynamic panel GMM (Arellano-Bond difference / Blundell-Bond system)

Category 08-panel-data; module ``static_panel_estimators``.

Reference implementation: linearmodels.

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
    "pd_effects_ftest",
    "pd_fit",
    "pd_fixed_effects",
    "pd_gmm_autocorr_test",
    "pd_gmm_fit",
    "pd_gmm_sargan_test",
    "pd_hausman_test",
    "pd_poolability_test",
    "pd_random_effects",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pd_fit(
    *,
    formula: str,
    data: pd.DataFrame,
    effect: Literal["individual", "time", "twoways", "nested"] | None = None,
    model: Literal["within", "random", "ht", "between", "pooling", "fd"] | None = None,
) -> dict[str, Any]:
    """Node ``pd_fit`` -- method card #46.

    Static panel estimators (FE/RE/pooling/between/FD) + Hausman/LM/F.

    Category 08-panel-data; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] Panel model formula, e.g. 'inv ~ value + capital'.
        data: [df_handle, required] Handle to a panel DataFrame (first 2 columns = index
            individual/time).
        effect: [enum, optional] Effect dimension (default individual).
        model: [enum, optional] Estimator (default within = fixed effects).

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
        "pd_fit: not implemented."
    )


def pd_hausman_test(
    *,
    x: str,
    data: pd.DataFrame,
    effect: Literal["individual", "time", "twoways"] | None = None,
    method: Literal["chisq", "aux"] | None = None,
) -> dict[str, Any]:
    """Node ``pd_hausman_test`` -- method card #46.

    Static panel estimators (FE/RE/pooling/between/FD) + Hausman/LM/F.

    Category 08-panel-data; memory class ``light``.

    Args:
        x: [formula, required] Model formula· the test runs within vs random internally.
        data: [df_handle, required] Panel data handle.
        effect: [enum, optional] Effect dimension.
        method: [enum, optional] Test flavour (default chisq).

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
        "pd_hausman_test: not implemented."
    )


def pd_poolability_test(
    *,
    x: str,
    data: pd.DataFrame,
    effect: Literal["individual", "time", "twoways"] | None = None,
    type: Literal["honda", "bp", "ghm", "kw"] | None = None,
) -> dict[str, Any]:
    """Node ``pd_poolability_test`` -- method card #46.

    Static panel estimators (FE/RE/pooling/between/FD) + Hausman/LM/F.

    Category 08-panel-data; memory class ``light``.

    Args:
        x: [formula, required] Model formula (LM poolability / random-effects test).
        data: [df_handle, required] Panel data handle.
        effect: [enum, optional] Effect dimension.
        type: [enum, optional] LM statistic variant (default honda).

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
        "pd_poolability_test: not implemented."
    )


def pd_effects_ftest(
    *,
    x: str,
    data: pd.DataFrame,
    effect: Literal["individual", "time", "twoways"] | None = None,
) -> dict[str, Any]:
    """Node ``pd_effects_ftest`` -- method card #46.

    Static panel estimators (FE/RE/pooling/between/FD) + Hausman/LM/F.

    Category 08-panel-data; memory class ``light``.

    Args:
        x: [formula, required] Model formula (F-test for significance of the fixed effects).
        data: [df_handle, required] Panel data handle.
        effect: [enum, optional] Effect dimension.

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
        "pd_effects_ftest: not implemented."
    )


def pd_fixed_effects(
    *,
    object: Any,
    type: Literal["level", "dfirst", "dmean"] | None = None,
) -> dict[str, Any]:
    """Node ``pd_fixed_effects`` -- method card #46.

    Static panel estimators (FE/RE/pooling/between/FD) + Hausman/LM/F.

    Category 08-panel-data; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a 'within' panel model (from pd_fit with
            model='within').
        type: [enum, optional] Effects coding (default level).

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
        "pd_fixed_effects: not implemented."
    )


def pd_random_effects(
    *,
    object: Any,
) -> dict[str, Any]:
    """Node ``pd_random_effects`` -- method card #46.

    Static panel estimators (FE/RE/pooling/between/FD) + Hausman/LM/F.

    Category 08-panel-data; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a 'random' panel model (from pd_fit with
            model='random').

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
        "pd_random_effects: not implemented."
    )


def pd_gmm_fit(
    *,
    formula: str,
    data: pd.DataFrame,
    effect: Literal["twoways", "individual"] | None = None,
    model: Literal["onestep", "twosteps"] | None = None,
    transformation: Literal["d", "ld"] | None = None,
) -> dict[str, Any]:
    """Node ``pd_gmm_fit`` -- method card #47.

    Dynamic panel GMM (Arellano-Bond difference / Blundell-Bond system).

    Category 08-panel-data; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] Dynamic panel GMM formula (Arellano-Bond, e.g. with lag &
            instruments).
        data: [df_handle, required] Panel data handle.
        effect: [enum, optional] Effect dimension (default twoways).
        model: [enum, optional] GMM steps (default onestep).
        transformation: [enum, optional] d=first-diff GMM, ld=system GMM (default d).

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
        "pd_gmm_fit: not implemented."
    )


def pd_gmm_autocorr_test(
    *,
    object: Any,
    order: int | None = None,
) -> dict[str, Any]:
    """Node ``pd_gmm_autocorr_test`` -- method card #47.

    Dynamic panel GMM (Arellano-Bond difference / Blundell-Bond system).

    Category 08-panel-data; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a pgmm model (from pd_gmm_fit).
        order: [integer, optional] AR order of the residual autocorrelation test (default 1).
            Default ``1``.

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
        "pd_gmm_autocorr_test: not implemented."
    )


def pd_gmm_sargan_test(
    *,
    object: Any,
    weights: Literal["twosteps", "onestep"] | None = None,
) -> dict[str, Any]:
    """Node ``pd_gmm_sargan_test`` -- method card #47.

    Dynamic panel GMM (Arellano-Bond difference / Blundell-Bond system).

    Category 08-panel-data; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a pgmm model (from pd_gmm_fit).
        weights: [enum, optional] Weighting for the Sargan/Hansen test.

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
        "pd_gmm_sargan_test: not implemented."
    )
