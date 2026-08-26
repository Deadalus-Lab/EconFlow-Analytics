# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``spa_reality_check`` -- method card #516.

#516 Superior predictive ability, reality check and StepM

Category 15-model-evaluation; module ``spa_reality_check``.

Reference implementation: arch.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c15_model_evaluation import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "me_superior_predictive_ability",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def me_superior_predictive_ability(
    *,
    losses: pd.DataFrame,
    benchmark: str,
    test: Literal["spa", "reality_check", "stepm"] | None = None,
    block_size: int | None = None,
    nboot: int | None = None,
    seed: int,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``me_superior_predictive_ability`` -- method card #516.

    Superior predictive ability, reality check and StepM.

    Category 15-model-evaluation; memory class ``heavy``.

    Args:
        losses: [df_handle, required] Loss series, one column per model.
        benchmark: [string, required] Column holding the benchmark loss.
        test: [enum, optional] Test. Default ``'spa'``.
        block_size: [integer, optional] Bootstrap block length; omitted = automatic.
        nboot: [integer, optional] Number of bootstrap replications. Default ``999``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.
        alpha: [number, optional] Significance level. Default ``0.05``.

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
        "me_superior_predictive_ability: not implemented."
    )
