# SPDX-License-Identifier: AGPL-3.0-only
"""Session fixtures: the committed artifacts, loaded once.

The artifacts are the GROUND TRUTH of this test suite. Every verdict in
``parity-fixtures.json`` was produced by the frozen argument adapter; none
of it is hand-written, and nothing here may edit it.
"""

from __future__ import annotations

import json
from collections.abc import Iterator
from pathlib import Path
from typing import Any

import numpy as np
import pytest
from beartype.claw import beartype_package

# RUN-TIME TYPE CHECKING, UNDER PYTEST AND NOWHERE ELSE.
#
# What it catches is the class of defect neither mypy nor pyright can see. Both
# read the annotation `-> int`; neither can tell that the body returns
# numpy.float64, that a `Sequence[float]` argument arrived as a 2-D array, or
# that a wrapper handed back the DataFrame it was given instead of the frame it
# was supposed to build. Those are the mistakes a numerical body actually makes,
# and every one of them passes a static check and every shape-only assertion.
#
# THIS LINE MUST NEVER MOVE INTO THE PACKAGE ITSELF. `beartype.claw` installs an
# import hook that rewrites every function in econflow_engine as it is imported;
# that is a cost and a behaviour change, and a production node call must run the
# code that was reviewed, not a decorated copy of it. conftest.py is loaded by
# pytest alone, which is what confines it. It runs at import time, before any
# test module has imported econflow_engine -- the hook only decorates modules
# imported AFTER it is installed, so ordering here is load-bearing.
beartype_package("econflow_engine")

ENGINE_ROOT = Path(__file__).resolve().parent.parent
ARTIFACTS = ENGINE_ROOT / "artifacts"


@pytest.fixture(scope="session", autouse=True)
def numpy_errors_are_errors() -> Iterator[None]:
    """Refuse the silent nan.

    numpy's default for a divide-by-zero, an invalid operation or an overflow is
    to emit a RuntimeWarning and CARRY ON, returning nan or inf. That value then
    flows through the rest of the computation, and a wrapper that returns a
    column of nan looks exactly like a wrapper that returned a column of numbers
    to every assertion that only checks a shape. `filterwarnings = ["error"]` in
    pyproject.toml catches these only where numpy chose to warn -- and numpy
    warns ONCE per location by default, so the second occurrence is silent even
    then. Raising at the source is what makes the failure land on the operation
    that produced it.

    Session-scoped and autouse: the error state is process-global in numpy, so
    setting it once covers every test, and no test can forget to ask for it.
    """
    previous = np.seterr(all="raise")
    try:
        yield
    finally:
        np.seterr(**previous)


def read_artifact(name: str) -> Any:
    return json.loads((ARTIFACTS / name).read_bytes().decode("utf-8"))


@pytest.fixture(scope="session")
def artifacts_dir() -> Path:
    return ARTIFACTS


@pytest.fixture(scope="session")
def node_specs() -> dict[str, Any]:
    loaded: dict[str, Any] = read_artifact("node-specs.json")
    return loaded


@pytest.fixture(scope="session")
def parity_fixtures() -> dict[str, Any]:
    loaded: dict[str, Any] = read_artifact("parity-fixtures.json")
    return loaded


@pytest.fixture(scope="session")
def intentional_divergences() -> dict[str, Any]:
    loaded: dict[str, Any] = read_artifact("intentional-divergences.json")
    return loaded
