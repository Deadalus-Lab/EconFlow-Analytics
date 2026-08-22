# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``posterior_diagnostics`` -- method card #71.

#71 Posterior R-hat / ESS diagnostics + summaries

Category 14-bayesian-toolkit; module ``posterior_diagnostics``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any

from econflow_engine.generated.args.c14_bayesian_toolkit import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "post_draw_summary",
    "NODE_META",
    "wire_model",
]


def post_draw_summary(
    *,
    x: Any,
    include_mcse: bool | None = None,
) -> dict[str, Any]:
    """Node ``post_draw_summary`` -- method card #71.

    Posterior R-hat / ESS diagnostics + summaries.

    Category 14-bayesian-toolkit; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to a 3D draws array (iter x chain x var), an MCMC draws
            list, or 'draws' object (nchains>=2).
        include_mcse: [boolean, optional] True -> adds an mcse_mean column (Monte-Carlo SE of the
            mean). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "post_draw_summary: not implemented."
    )
