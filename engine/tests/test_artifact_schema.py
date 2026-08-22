# SPDX-License-Identifier: AGPL-3.0-only
"""Every sealed artifact has a committed schema, and its records match it.

WHAT THE SIDECARS DO NOT DO. Each artifact is sealed with a SHA-256 sidecar, and
that proves IDENTITY: these are the bytes that were reviewed. It says nothing
about SHAPE. An artifact replaced wholesale -- a card that lost a field, a node
whose contract hash became a truncation, a verdict with no reason code -- is
simply a different file with a different, entirely valid digest. It passes the
seal and breaks everything downstream of it. ``engine/artifacts/schema/`` exists
to close that gap, and this module is what keeps the two sets in step.

THE DIVISION OF LABOUR, STATED PLAINLY SO NOBODY MISTAKES ONE FOR THE OTHER.
Full JSON Schema validation is done by ``check-jsonschema`` in the
``artifact-drift`` job: it is a pinned CI tool and understands the whole
vocabulary. It is deliberately NOT a dependency of the engine -- the runtime has
no use for a schema validator, and the declared dependency set is a reviewed list
rather than a convenience. So this suite does the part that must hold even when
no network and no external tool is available:

  1. THE PAIRING IS COMPLETE. Every artifact has a schema and every schema has an
     artifact. This is the one that matters most, because the failure it catches
     is a NEW artifact landing with no schema at all -- at which point the CI job
     validates the files it knows about, reports success, and the new one is
     covered by nothing.
  2. THE REQUIRED FIELDS ARE PRESENT on every record of every artifact, and no
     record carries a field the schema does not declare where the schema closes
     the set. That is exactly the "planted missing field" and the "reintroduced
     field" case, checked with the standard library alone.

What this does not do is interpret the rest of the vocabulary -- patterns, enums,
numeric bounds, nested objects. Those are real assertions and they are checked,
by the tool that implements them properly. Nothing here should be read as making
that job redundant.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

ARTIFACTS = Path(__file__).resolve().parents[1] / "artifacts"
SCHEMA_DIR = ARTIFACTS / "schema"

# The suffix convention that pairs the two directories.
SCHEMA_SUFFIX = ".schema.json"


def artifact_names() -> list[str]:
    return sorted(
        p.name.removesuffix(".json")
        for p in ARTIFACTS.glob("*.json")
        if p.is_file()
    )


def schema_names() -> list[str]:
    return sorted(
        p.name.removesuffix(SCHEMA_SUFFIX) for p in SCHEMA_DIR.glob(f"*{SCHEMA_SUFFIX}")
    )


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def resolve(schema: dict[str, Any], root: dict[str, Any]) -> dict[str, Any]:
    """Follow a local ``#/$defs/name`` reference. Only local refs are used here."""
    ref = schema.get("$ref")
    if not ref:
        return schema
    assert ref.startswith("#/"), f"only local refs are supported, got {ref!r}"
    target: Any = root
    for part in ref.removeprefix("#/").split("/"):
        target = target[part]
    return resolve(target, root)


def test_every_artifact_has_a_schema_and_every_schema_an_artifact() -> None:
    """The pairing. A new artifact with no schema is validated by nothing."""
    assert artifact_names() == schema_names(), (
        "artifacts and schemas have diverged. An artifact without a schema is "
        "sealed for identity only, and the drift job will happily report success "
        "while covering nothing of its shape."
    )


@pytest.mark.parametrize("name", schema_names())
def test_the_schema_is_well_formed(name: str) -> None:
    schema = load(SCHEMA_DIR / f"{name}{SCHEMA_SUFFIX}")
    assert schema["$schema"].startswith("https://json-schema.org/draft/")
    assert schema["title"], "a schema without a title says nothing in an error report"
    assert schema["type"] == "object"
    assert schema["required"], "a schema that requires nothing asserts nothing"


@pytest.mark.parametrize("name", schema_names())
def test_the_artifact_carries_every_top_level_required_key(name: str) -> None:
    schema = load(SCHEMA_DIR / f"{name}{SCHEMA_SUFFIX}")
    artifact = load(ARTIFACTS / f"{name}.json")
    missing = [key for key in schema["required"] if key not in artifact]
    assert missing == [], f"{name}.json is missing {missing}"


@pytest.mark.parametrize("name", schema_names())
def test_every_record_matches_the_schema_for_its_collection(name: str) -> None:
    """The planted-missing-field and reintroduced-field check, per record."""
    schema = load(SCHEMA_DIR / f"{name}{SCHEMA_SUFFIX}")
    artifact = load(ARTIFACTS / f"{name}.json")

    checked = 0
    for prop, subschema in schema["properties"].items():
        if subschema.get("type") != "array":
            continue
        item_schema = resolve(subschema.get("items", {}), schema)
        required = item_schema.get("required")
        if not required:
            continue
        declared = set(item_schema.get("properties", {}))
        closed = item_schema.get("additionalProperties") is False

        for index, record in enumerate(artifact[prop]):
            missing = [key for key in required if key not in record]
            assert missing == [], f"{name}.json {prop}[{index}] is missing {missing}"
            if closed:
                extra = sorted(set(record) - declared)
                assert extra == [], (
                    f"{name}.json {prop}[{index}] carries undeclared field(s) "
                    f"{extra}. Either the artifact grew a field nobody described, "
                    "or the schema was not updated with it."
                )
            checked += 1

    # Anti-vacuity. Four of the six artifacts hold a collection of records; the
    # ones that do must actually have had their records walked, or this test
    # passed by finding nothing to look at.
    if any(
        s.get("type") == "array" and resolve(s.get("items", {}), schema).get("required")
        for s in schema["properties"].values()
    ):
        assert checked > 0, f"{name}: no records were examined, so nothing was proved"
