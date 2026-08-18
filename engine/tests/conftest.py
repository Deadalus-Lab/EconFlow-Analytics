# SPDX-License-Identifier: AGPL-3.0-only
"""Session fixtures: the committed artifacts, loaded once.

The artifacts are the GROUND TRUTH of this test suite. Every verdict in
``parity-fixtures.v1.json`` was produced by the frozen argument adapter; none
of it is hand-written, and nothing here may edit it.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

ENGINE_ROOT = Path(__file__).resolve().parent.parent
ARTIFACTS = ENGINE_ROOT / "artifacts"


def read_artifact(name: str) -> Any:
    return json.loads((ARTIFACTS / name).read_bytes().decode("utf-8"))


@pytest.fixture(scope="session")
def artifacts_dir() -> Path:
    return ARTIFACTS


@pytest.fixture(scope="session")
def node_specs() -> dict[str, Any]:
    loaded: dict[str, Any] = read_artifact("node-specs.v1.json")
    return loaded


@pytest.fixture(scope="session")
def parity_fixtures() -> dict[str, Any]:
    loaded: dict[str, Any] = read_artifact("parity-fixtures.v1.json")
    return loaded


@pytest.fixture(scope="session")
def intentional_divergences() -> dict[str, Any]:
    loaded: dict[str, Any] = read_artifact("intentional-divergences.json")
    return loaded
