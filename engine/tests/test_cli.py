# SPDX-License-Identifier: AGPL-3.0-only
"""The module entry point the container's default command depends on.

``Dockerfile`` ends in ``CMD ["python", "-m", "econflow_engine"]``. Until this
module existed the container could not start at all, and nothing in the suite
would have said so -- which is why the entry point is tested through a real
subprocess rather than by importing ``main()``. Importing it would prove the
function runs; only ``python -m`` proves the container's command resolves.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import pytest

from econflow_engine import __version__
from econflow_engine.mcp.server import list_methods

ENGINE_ROOT = Path(__file__).resolve().parent.parent
INVENTORY = ENGINE_ROOT.parent / ".github" / "inventory.json"


def run_cli(*args: str, stdin: str | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "econflow_engine", *args],
        capture_output=True,
        text=True,
        check=False,
        input=stdin,
    )


def a_real_node() -> tuple[str, dict[str, Any]]:
    """The first node of the committed contract, with the example body it declares.

    Read from the artifact rather than named here, so that the node the CLI is
    exercised against is one the engine actually publishes.
    """
    specs = json.loads(
        (ENGINE_ROOT / "artifacts" / "node-specs.json").read_bytes().decode("utf-8"))
    node = specs["nodes"][0]
    return node["fn"], dict(node.get("input_example") or {})


def test_help_exits_zero() -> None:
    """The Dockerfile's smoke test. If this fails the image cannot be verified."""
    result = run_cli("--help")
    assert result.returncode == 0, result.stderr
    assert "describe" in result.stdout


def test_version_reports_the_package_version() -> None:
    result = run_cli("--version")
    assert result.returncode == 0, result.stderr
    assert __version__ in result.stdout


def test_describe_emits_the_node_contract_as_json() -> None:
    fn = list_methods()[0]
    result = run_cli("describe", fn)
    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)
    assert payload["fn"] == fn
    assert "input_schema" in payload


def test_describe_refuses_an_unknown_node() -> None:
    """A typo must fail loudly. A CLI that prints nothing and exits 0 is worse
    than one that crashes, because a caller cannot tell the two apart."""
    result = run_cli("describe", "no_such_node_exists")
    assert result.returncode != 0
    assert result.stdout.strip() == ""
    assert "no_such_node_exists" in result.stderr


def test_no_subcommand_exits_nonzero() -> None:
    result = run_cli()
    assert result.returncode != 0


@pytest.mark.parametrize("flag", ["--help", "--version"])
def test_informational_flags_write_nothing_to_stderr(flag: str) -> None:
    result = run_cli(flag)
    assert result.stderr == ""


# --------------------------------------------------------------------- list


def test_list_prints_every_node_one_per_line() -> None:
    """MEASURED AGAINST THE MANIFEST, WITH NO DEFAULT. engine.methods is read
    from .github/inventory.json and a missing key raises here: a CLI that listed
    three nodes and exited 0 would otherwise look exactly like one that listed
    all of them."""
    declared = json.loads(INVENTORY.read_bytes().decode("utf-8"))["engine"]["methods"]
    result = run_cli("list")
    assert result.returncode == 0, result.stderr
    lines = result.stdout.splitlines()
    assert len(lines) == declared == 1456
    assert lines == sorted(lines)


def test_list_narrows_to_one_category() -> None:
    """A filter that returned everything would still pass a count-free check."""
    everything = run_cli("list").stdout.splitlines()
    narrowed = run_cli("list", "--category", "00-data-utilities")
    assert narrowed.returncode == 0, narrowed.stderr
    lines = narrowed.stdout.splitlines()
    assert 0 < len(lines) < len(everything)
    assert set(lines) <= set(everything)


def test_list_refuses_a_category_nobody_publishes() -> None:
    """An empty result is the shape a typo produces, and exiting 0 on it would
    tell a caller the category exists and holds nothing."""
    result = run_cli("list", "--category", "no-such-category")
    assert result.returncode == 2
    assert result.stdout.strip() == ""
    assert "no-such-category" in result.stderr


# ---------------------------------------------------------------------- run


def test_run_reports_an_unwritten_body_as_not_implemented() -> None:
    """THE ANTI-VACUITY CASE. Every wrapper body in the tree is a typed stub
    today, so a real node called with the example body it publishes must exit 4
    and say `not-implemented`. Exercising `run` only on an unknown fn would
    prove the argument parser works and nothing else. When that wrapper's body
    lands this turns red, and the correct response is to read the new state."""
    fn, body = a_real_node()
    result = run_cli("run", fn, "--json", json.dumps(body))
    assert result.returncode == 4, result.stderr
    payload = json.loads(result.stdout)
    assert payload["state"] == "not-implemented"
    assert payload["fn"] == fn


def test_run_reads_the_body_from_stdin() -> None:
    """The same call through the other input path. A container is handed a body
    on a pipe far more often than on a command line."""
    fn, body = a_real_node()
    result = run_cli("run", fn, stdin=json.dumps(body))
    assert result.returncode == 4, result.stderr
    assert json.loads(result.stdout)["state"] == "not-implemented"


def test_run_exits_three_on_a_refusal_and_names_the_reason() -> None:
    """A refusal is not a crash and not a success: the wire contract answered.
    The reason code is what a caller branches on, so it goes to stderr as well
    as into the payload."""
    fn, _ = a_real_node()
    result = run_cli("run", fn, "--json", "{}")
    assert result.returncode == 3, result.stderr
    payload = json.loads(result.stdout)
    assert payload["state"] == "refused"
    assert payload["reason_code"] == "missing-required"
    assert "missing-required" in result.stderr


def test_run_refuses_an_unknown_node() -> None:
    result = run_cli("run", "no_such_node_exists", "--json", "{}")
    assert result.returncode == 2
    assert result.stdout.strip() == ""
    assert "no_such_node_exists" in result.stderr


def test_run_refuses_a_body_that_is_not_json() -> None:
    fn, _ = a_real_node()
    result = run_cli("run", fn, "--json", "{not json")
    assert result.returncode == 2
    assert result.stdout.strip() == ""
    assert "JSON" in result.stderr


def test_run_refuses_a_body_that_is_not_an_object() -> None:
    """A node body is a mapping of argument names. A bare list would otherwise
    reach the gateway and fail somewhere less legible."""
    fn, _ = a_real_node()
    result = run_cli("run", fn, "--json", "[1, 2, 3]")
    assert result.returncode == 2
    assert "object" in result.stderr
