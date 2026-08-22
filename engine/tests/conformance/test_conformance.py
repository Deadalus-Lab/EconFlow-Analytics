# SPDX-License-Identifier: AGPL-3.0-only
"""Oracle harness: a node's output against an independently established value.

SKIPPED BY DEFAULT, AND THAT IS THE HONEST STATE. It reads
``artifacts/golden-corpus.json``, which DOES NOT EXIST YET. The corpus is
built case by case as methods are implemented, from the three sources this
project admits as an oracle: a published paper's reported figures, a
hand-verified fixture, and a property that must hold. The harness is written
ahead of the corpus so the first implemented body meets an existing test rather
than motivating one.

WHAT PARITY DOES NOT COVER, AND THIS DOES. The parity suite proves the engine
AGREES WITH THE CONTRACT ABOUT WHICH CALLS ARE VALID. It says nothing about the
NUMBERS: a wrapper could accept exactly the right inputs and compute something
else entirely. Only a comparison against an independently established value
catches that, and until the corpus exists, "the method is correct" is a claim
about the argument surface alone.

THE EXPECTED CORPUS SHAPE, so producing it is mechanical::

    {
      "artifact_version": 1,
      "generated_by": "<the source that established the values>",
      "engine": {"artifact_sha256": "..."},
      "cases": [
        {
          "id": "run_adf_test/001",
          "fn": "run_adf_test",
          "inputs": {"<arg>": <literal or {"$series": [...]}>},
          "output": <the to_mcp payload the oracle establishes>,
          "tolerance": {"rtol": 1e-9, "atol": 1e-12}
        }
      ]
    }

TOLERANCE IS PER CASE, NOT GLOBAL. A closed-form test statistic should match to
machine precision; an optimiser-driven estimate should not be held to the same
bar, and pretending otherwise produces either false failures or a tolerance so
loose it proves nothing. The producing side records what it can promise.
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Any

import pytest

ARTIFACTS = Path(__file__).resolve().parent.parent.parent / "artifacts"
GOLDEN = ARTIFACTS / "golden-corpus.json"

pytestmark = pytest.mark.conformance

requires_corpus = pytest.mark.skipif(
    not GOLDEN.is_file(),
    reason=(
        "artifacts/golden-corpus.json is absent, so there is nothing to compare "
        "against yet."
    ),
)


def numerically_equal(actual: Any, expected: Any, rtol: float, atol: float) -> bool:
    """Structural comparison with a NUMERIC leaf test.

    ``None`` matches ``None`` and nothing else: a missing value and a computed value
    are different answers, and a tolerance must never blur them.
    """
    if expected is None or actual is None:
        return expected is None and actual is None
    if isinstance(expected, bool) or isinstance(actual, bool):
        return actual is expected
    if isinstance(expected, int | float) and isinstance(actual, int | float):
        if math.isnan(float(expected)) or math.isnan(float(actual)):
            return math.isnan(float(expected)) and math.isnan(float(actual))
        return math.isclose(float(actual), float(expected), rel_tol=rtol, abs_tol=atol)
    if isinstance(expected, str):
        return bool(actual == expected)
    if isinstance(expected, list):
        return (
            isinstance(actual, list)
            and len(actual) == len(expected)
            and all(
                numerically_equal(a, e, rtol, atol)
                for a, e in zip(actual, expected, strict=True)
            )
        )
    if isinstance(expected, dict):
        return (
            isinstance(actual, dict)
            and set(actual) == set(expected)
            and all(numerically_equal(actual[k], expected[k], rtol, atol) for k in expected)
        )
    return bool(actual == expected)


def load_cases() -> list[dict[str, Any]]:
    if not GOLDEN.is_file():
        return []
    import json

    return list(json.loads(GOLDEN.read_bytes().decode("utf-8"))["cases"])


@requires_corpus
def test_the_corpus_pins_the_engine_that_produced_it() -> None:
    """A corpus without provenance cannot be trusted to describe THIS contract."""
    import json

    from econflow_engine.loader import ENGINE_INFO

    corpus = json.loads(GOLDEN.read_bytes().decode("utf-8"))
    assert corpus["artifact_version"] == 1
    assert corpus["engine"]["artifact_sha256"] == ENGINE_INFO["artifact_sha256"], (
        "the golden corpus was produced against a DIFFERENT node-specs revision; "
        "regenerate it before trusting a single comparison"
    )


#: Collected at import time so that the ids can be built explicitly: an `ids`
#: CALLABLE is invoked even for the placeholder pytest synthesises when the
#: parameter list is empty, which is the normal state until the corpus exists.
_CASES = load_cases()


@requires_corpus
@pytest.mark.parametrize("case", _CASES, ids=[str(c["id"]) for c in _CASES])
def test_the_node_reproduces_the_oracle(case: dict[str, Any]) -> None:
    from econflow_engine.mcp.gateway import run_method

    response = run_method(case["fn"], case["inputs"])
    if response.state == "not-implemented":
        pytest.skip(f"{case['fn']}: the wrapper body is not implemented yet")
    assert response.state == "succeeded", f"{case['id']}: {response.message}"
    tolerance = case.get("tolerance") or {}
    assert numerically_equal(
        response.payload,
        case["output"],
        rtol=float(tolerance.get("rtol", 1e-9)),
        atol=float(tolerance.get("atol", 1e-12)),
    ), f"{case['id']}: the payload differs from the recorded output"
