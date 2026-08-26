# SPDX-License-Identifier: AGPL-3.0-only
"""The conditional OWED sentinel on ``engine.invocation_payloads``, in three states.

WHY THIS SUITE EXISTS, AND WHY IT IS NOT OPTIONAL. A hard ``unmeasured`` failure
needs no test: it can only be cleared by landing the artifact, so nothing can
make it wrong. Once the sentinel is CONDITIONAL its green rests on a counter
instead, and a counter can be wrong in the quiet direction -- a wrapper walk that
stops finding files reports an empty implemented set, the premise reads true, and
the gate goes green having examined nothing. That is the shape ARCHITECTURE.md
11.1 refuses and the shape this tree has hit six times.

So each of the three branches is exercised against a real run of the real script.
Two of them read the real manifest, as it stands or with one constant moved, which
is why they cost nothing. The third needs a wrapper body, and gets one from a
HARDLINK MIRROR of ``engine/``: hardlinks make the copy 0.04 s and leave every count
identical -- ``find -type f`` is true of a hardlink and false of a symlink, and
``rglob`` does not descend a symlinked directory, so neither of the cheaper
mirrors would have measured the same tree. A planted file is unlinked before it
is written, because writing through a hardlink would edit the repository.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path

from econflow_engine.metrics import find_repo_root
from tests.support import ENGINE_ROOT, INVENTORY

REPO_ROOT = find_repo_root(Path(__file__))
ASSERT_SH = REPO_ROOT / ".github" / "actions" / "assert-inventory" / "assert.sh"
STUB_RAISE = "    raise NotImplementedError("


def _run(engine_dir: Path, manifest: Path) -> subprocess.CompletedProcess[str]:
    """Run the real gate on the real script, never a second copy of its logic.

    Invoked by its own absolute path rather than through a bare ``bash``: the
    script is committed executable (mode 100755) and carries a bash shebang, and
    naming an interpreter by a partial path is what ruff S607 refuses.
    """
    return subprocess.run(
        [str(ASSERT_SH), str(engine_dir), str(manifest)],
        capture_output=True,
        text=True,
        check=False,
    )


def _payload_line(result: subprocess.CompletedProcess[str]) -> str:
    """The one VERDICT line for this constant, whatever its verdict word is.

    Matched on the report's two-space-then-word column rather than on the label
    alone: the remedy text under a red verdict names the manifest key too, and a
    helper that collected those would judge whichever line came first.
    """
    hits = [
        ln
        for ln in result.stdout.splitlines()
        if ln.startswith(("  ok    ", "  FAIL  ", "  OWED  ")) and "invocation_payloads" in ln
    ]
    assert len(hits) == 1, f"expected one invocation_payloads line, got {hits}"
    return hits[0]


def _failing_labels(result: subprocess.CompletedProcess[str]) -> set[str]:
    """Every constant the run reported as FAIL, by label."""
    return {
        ln.split()[1]
        for ln in result.stdout.splitlines()
        if ln.startswith("  FAIL  ") and len(ln.split()) > 1
    }


def _manifest(tmp_path: Path, **engine_overrides: object) -> Path:
    """The real manifest with named engine constants moved, and nothing else."""
    data = json.loads(INVENTORY.read_text(encoding="utf-8"))
    data["engine"].update(engine_overrides)
    out = tmp_path / "inventory.json"
    out.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return out


def _mirror(tmp_path: Path) -> Path:
    """A writable hardlink mirror of engine/, with the workspace lock beside it."""
    root = tmp_path / "root"
    root.mkdir()
    os.link(REPO_ROOT / "uv.lock", root / "uv.lock")
    engine = root / "engine"
    shutil.copytree(
        ENGINE_ROOT,
        engine,
        copy_function=os.link,
        ignore=shutil.ignore_patterns("__pycache__", "mutants", ".venv"),
    )
    return engine


def _plant_one_body(engine: Path) -> str:
    """Give exactly one public wrapper function a body, and name it.

    One statement is inserted ahead of the emitted raise, so the function stops
    being a stub while the CATALOGUE SIZE does not move: the implemented count
    rises by one and the stub count falls by one. A plant that added or removed a
    function would trip the sum guard instead of the premise, and the test would
    pass for the wrong reason.
    """
    module = next(
        p
        for p in sorted((engine / "src" / "econflow_engine" / "wrappers").rglob("*.py"))
        if p.name != "__init__.py"
    )
    text = module.read_text(encoding="utf-8")
    head, _, tail = text.partition(STUB_RAISE)
    assert tail, f"no emitted stub raise in {module}"
    function = head.rsplit("\ndef ", 1)[1].split("(", 1)[0]
    module.unlink()  # never write through a hardlink: it would edit the repository
    module.write_text(f"{head}    _ = None\n{STUB_RAISE}{tail}", encoding="utf-8")
    return function


def test_the_resting_tree_is_green_and_still_says_owed() -> None:
    """POSITIVE. Nothing implemented, no payload tree: owed, said aloud, exit 0.

    The OWED line must survive. Its visibility is the whole point of the marker;
    only its exit code follows the premise.
    """
    result = _run(ENGINE_ROOT, INVENTORY)

    assert result.returncode == 0, result.stdout + result.stderr
    assert "OWED" in _payload_line(result)


def test_an_implemented_body_turns_the_sentinel_red_and_names_it(tmp_path: Path) -> None:
    """NEGATIVE. One body exists, the word is still there: red, and it names the method.

    The manifest also carries n_implemented=1, because the person who writes the
    first body must bump it. That leaves the payload sentinel as the ONLY thing
    that can fail, which is what the last assertion pins.
    """
    engine = _mirror(tmp_path)
    planted = _plant_one_body(engine)

    result = _run(engine, _manifest(tmp_path, n_implemented=1))

    assert result.returncode == 1, result.stdout + result.stderr
    line = _payload_line(result)
    assert line.startswith("  FAIL"), line
    assert planted in line, f"{planted} is not named in {line!r}"
    assert _failing_labels(result) == {"invocation_payloads"}, result.stdout


def test_the_catalogue_sum_guard_fires(tmp_path: Path) -> None:
    """NEGATIVE. Implemented plus stub must account for every method in the catalogue.

    Without this, a walk that found nothing would report an empty implemented set
    and the premise would read true for the worst possible reason.
    """
    result = _run(ENGINE_ROOT, _manifest(tmp_path, methods=1457))

    assert result.returncode == 1, result.stdout + result.stderr
    line = _payload_line(result)
    assert line.startswith("  FAIL"), line
    assert "1457" in line and "1456" in line, line
