# SPDX-License-Identifier: AGPL-3.0-only
"""Normative gate 1 (Keogh): detect sliding-window construction in a feature matrix.

A DETECTOR, NOT A BLOCKER. It returns the step ``k`` (0 = clean) and the caller
decides what to do with it, because the same finding is fatal for one method and
merely worth reporting for another.

The two refusals here are both about how the gate itself was CALLED, so they
carry ``gate-argument``; the matrix's own shape is the one input the gate reads.
"""

from __future__ import annotations

from typing import Any

import numpy as np

from econflow_engine.errors import GateError
from econflow_engine.gates.codes import GateDetailCode, refusal

__all__ = ["gate_sliding_window_step"]


def _refuse(message: str, code: GateDetailCode) -> GateError:
    """Local alias for the shared constructor, so ``"other"`` is written once."""
    return refusal(message, code)


def _shift_matches(matrix: np.ndarray, a_cols: slice, b_cols: slice, tol: float) -> bool:
    """PER-ELEMENT tolerance, NEVER mean-relative: ``|a-b| <= tol*max(|a|,|b|,1)``.

    A mean-relative test passes on a panel whose average magnitude is large while
    individual cells disagree wildly, which is exactly the case this gate exists
    to catch.
    """
    a = matrix[:-1, a_cols]
    b = matrix[1:, b_cols]
    diff = np.abs(a - b)
    if not np.all(np.isfinite(diff)):
        return False
    bound = tol * np.maximum(np.maximum(np.abs(a), np.abs(b)), 1.0)
    return bool(np.all(diff <= bound))


def gate_sliding_window_step(
    matrix: Any, max_step: int | None = None, tol: float = 1e-12
) -> int:
    """Detect sliding-window construction. Returns the step ``k``; 0 means clean.

    A DETECTOR, not a blocker -- the caller decides. Generalised beyond k = 1:
    the step is a free parameter of how the subsequences were built, so a step-2
    window is covered by the Keogh, Lin & Truppel result just as much as a step-1
    one. Every fixed step in ``[1, min(floor(m/2), m-2)]`` is checked.
    """
    array = np.asarray(matrix)
    if array.ndim != 2 or not np.issubdtype(array.dtype, np.number):
        raise _refuse(
            'gate_sliding_window_step: "matrix" must be a NUMERIC 2-D array '
            "(objects in rows, features in columns).",
            "precondition-shape",
        )
    if isinstance(tol, bool) or not isinstance(tol, float | int) or tol < 0:
        raise _refuse(
            'gate_sliding_window_step: "tol" must be ONE non-negative number.',
            "gate-argument",
        )
    n, m = array.shape
    if n < 3 or m < 3:
        return 0
    if max_step is None:
        k_max = m // 2
    else:
        if isinstance(max_step, bool) or not isinstance(max_step, int) or max_step < 1:
            raise _refuse(
                'gate_sliding_window_step: "max_step" must be None or ONE positive integer.',
                "gate-argument",
            )
        k_max = max_step
    k_max = min(k_max, m - 2)
    values = array.astype(float)
    for k in range(1, k_max + 1):
        tail = slice(k, m)
        head = slice(0, m - k)
        if _shift_matches(values, tail, head, float(tol)) or _shift_matches(
            values, head, tail, float(tol)
        ):
            return k
    return 0
