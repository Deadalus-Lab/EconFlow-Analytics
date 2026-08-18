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

import pytest

from econflow_engine import __version__
from econflow_engine.mcp.server import list_methods


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "econflow_engine", *args],
        capture_output=True,
        text=True,
        check=False,
    )


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
