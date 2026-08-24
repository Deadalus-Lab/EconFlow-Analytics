# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``inequality_indices_lorenz`` -- method card #91.

#91 inequality indices + Lorenz curve (Gini/Theil/Atkinson/RS/Kolm/CV/entropy)

Category 22-inequality; module ``inequality_indices_lorenz``.

Reference implementation: IneqPy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c22_inequality import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "compute_inequality",
    "lorenz_curve",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def compute_inequality(
    *,
    x: np.ndarray,
    type: (
        Literal[
            "Gini",
            "RS",
            "Atkinson",
            "Theil",
            "Kolm",
            "var",
            "square.var",
            "entropy",
        ]
        | None
    ) = None,
    parameter: float | None = None,
) -> dict[str, Any]:
    """Node ``compute_inequality`` -- method card #91.

    inequality indices + Lorenz curve (Gini/Theil/Atkinson/RS/Kolm/CV/entropy).

    Category 22-inequality; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric vector (e.g. incomes/weights), length >= 2,
            without NA/Inf; Gini/Atkinson/Theil/entropy require x >= 0.
        type: [enum, optional] Inequality index (default Gini).
        parameter: [number, optional] Optional scalar: affects Atkinson (default 0.5), Kolm (default
            1), entropy (default 0.5; entropy@1 == Theil).

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
        "compute_inequality: not implemented."
    )


def lorenz_curve(
    *,
    x: np.ndarray,
) -> dict[str, Any]:
    """Node ``lorenz_curve`` -- method card #91.

    inequality indices + Lorenz curve (Gini/Theil/Atkinson/RS/Kolm/CV/entropy).

    Category 22-inequality; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric non-negative vector (x >= 0), length >= 2,
            without NA/Inf, total > 0.

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
        "lorenz_curve: not implemented."
    )
