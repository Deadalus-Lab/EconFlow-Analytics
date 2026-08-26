# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``fan_charts`` -- method card #410.

#410 Simulation-based fan charts and scenario paths

Category 02-univariate-forecasting; module ``fan_charts``.

Reference implementation: statsforecast.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

from econflow_engine.generated.args.c02_univariate_forecasting import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "uf_fan_chart",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def uf_fan_chart(
    *,
    fit: Any,
    h: int,
    n_simulations: int | None = None,
    innovations: Literal["parametric", "bootstrap"] | None = None,
    quantiles: Sequence[float] | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``uf_fan_chart`` -- method card #410.

    Simulation-based fan charts and scenario paths.

    Category 02-univariate-forecasting; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted forecasting model.
        h: [integer, required] Forecast horizon.
        n_simulations: [integer, optional] Simulated paths. Default ``1000``.
        innovations: [enum, optional] Innovation source. Default ``'bootstrap'``.
        quantiles: [num_array, optional] Fan quantiles. Default ``[0.05, 0.25, 0.5, 0.75, 0.95]``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

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
        "uf_fan_chart: not implemented."
    )
