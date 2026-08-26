# SPDX-License-Identifier: AGPL-3.0-only
"""PLANTED CONTROL for rule R2 of box 2.1.13. Not a wrapper. Never imported.

``engine.n_implemented`` is 0 today, so R2 walks the wrapper tier and finds no
implemented body to check -- it would report success having examined nothing,
which is the exact vacuity this repository refuses. This file is what R2 examines
instead until the first real body lands.

``run_planted_ignores_seed`` is shaped like an implemented wrapper: keyword-only
arguments, a ``seed`` among them, a docstring, and a body that is not the
generated ``raise NotImplementedError`` stub. It accepts the seed and never uses
it -- so it returns a different answer on every call while its signature promises
reproducibility. That is the silent defect no other gate in this tree can catch:
the signature is right, the types are right, the result is plausible, and the
number is different tomorrow.

``run_planted_uses_seed`` is the paired NEGATIVE control. Without it, R2 could
decay into a rule that flags every function with a ``seed`` argument and still
report both controls "working".
"""

from __future__ import annotations

import numpy as np


def run_planted_ignores_seed(*, n: int, seed: int | None = None) -> dict[str, float]:  # noqa: ARG001
    """THE DEFECT: accepts ``seed`` and draws from an unseeded generator."""
    draw = np.random.default_rng().normal(size=n)
    return {"mean": float(draw.mean())}


def run_planted_uses_seed(*, n: int, seed: int | None = None) -> dict[str, float]:
    """The correct shape: the declared seed reaches the generator."""
    draw = np.random.default_rng(seed).normal(size=n)
    return {"mean": float(draw.mean())}
