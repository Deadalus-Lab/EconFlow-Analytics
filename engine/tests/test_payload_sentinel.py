# SPDX-License-Identifier: AGPL-3.0-only
"""``engine.invocation_payloads``, in every state its gate can reach.

WHY THIS SUITE EXISTS, AND WHY IT IS NOT OPTIONAL. A hard ``unmeasured`` failure
needs no test: it can only be cleared by landing the artifact, so nothing can
make it wrong. Once the sentinel became CONDITIONAL its green rested on a counter
instead, and a counter can be wrong in the quiet direction -- a wrapper walk that
stops finding files reports an empty implemented set, the premise reads true, and
the gate goes green having examined nothing. That is the shape ARCHITECTURE.md
11.1 refuses and the shape this tree has hit six times.

THE WORD WAS RETIRED BY THE FIRST WRAPPER BODY, AND THE BRANCH IT GUARDED IS
STILL IN THE SCRIPT. ``engine/tests/payloads/`` now exists and the constant reads
the count that directory returns, which is 0: the one implemented method is
reached by its oracle case, and the gate takes the union of the two sources. So
the resting tree is ``ok`` rather than ``OWED``, and the sentinel's own branch --
the catalogue sum guard and the refusal to rest on a premise that no method
carries a body -- is no longer reachable from the committed manifest. It is
reached HERE instead, against a mirror with the directory removed and the word
restored, because a branch that survives in the script with nothing exercising it
is a branch that has quietly stopped working.

Each state is exercised against a real run of the real script. The ones that need
a wrapper body, or need one absent, get a HARDLINK MIRROR of ``engine/``:
hardlinks make the copy 0.04 s and leave every count identical -- ``find -type f``
is true of a hardlink and false of a symlink, and ``rglob`` does not descend a
symlinked directory, so neither of the cheaper mirrors would have measured the
same tree. A planted file is unlinked before it is written, because writing
through a hardlink would edit the repository.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path

from econflow_engine.metrics import find_repo_root, stub_ledger
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
    """A writable hardlink mirror of engine/, with the workspace lock beside it.

    ``.omc`` IS IGNORED HERE FOR THE SAME REASON AS THE OTHER THREE, and it was
    missing while ``tests/test_double_run_methods.py``'s mirror already skipped
    it: agent runtime state is not part of the tree under test, and hardlinking
    a live session's files into a temporary directory is a copy nobody asked for.
    The two mirrors now ignore the same set.
    """
    root = tmp_path / "root"
    root.mkdir()
    os.link(REPO_ROOT / "uv.lock", root / "uv.lock")
    engine = root / "engine"
    shutil.copytree(
        ENGINE_ROOT,
        engine,
        copy_function=os.link,
        ignore=shutil.ignore_patterns("__pycache__", "mutants", ".venv", ".omc"),
    )
    return engine


def _without_the_payload_tree(tmp_path: Path) -> Path:
    """A mirror with ``tests/payloads/`` removed, which is where the word applies.

    ``shutil.rmtree`` on a tree of HARDLINKS unlinks the mirror's names and leaves
    the repository's own files alone; that invariant is what the mirror is for and
    it is asserted in the test below rather than assumed here.
    """
    engine = _mirror(tmp_path)
    shutil.rmtree(engine / "tests" / "payloads")
    return engine


def _plant_one_body(engine: Path) -> str:
    """Give exactly one MORE public wrapper function a body, and name it.

    One statement is inserted ahead of the emitted raise, so the function stops
    being a stub while the CATALOGUE SIZE does not move: the implemented count
    rises by one and the stub count falls by one. A plant that added or removed a
    function would trip the sum guard instead of the premise, and the test would
    pass for the wrong reason.
    """
    module = next(
        p
        for p in sorted((engine / "src" / "econflow_engine" / "wrappers").rglob("*.py"))
        if p.name != "__init__.py" and STUB_RAISE in p.read_text(encoding="utf-8")
    )
    text = module.read_text(encoding="utf-8")
    head, _, tail = text.partition(STUB_RAISE)
    function = head.rsplit("\ndef ", 1)[1].split("(", 1)[0]
    module.unlink()  # never write through a hardlink: it would edit the repository
    module.write_text(f"{head}    _ = None\n{STUB_RAISE}{tail}", encoding="utf-8")
    return function


def _implemented() -> int:
    """What the committed manifest says the tree carries. Read, never written down."""
    return int(json.loads(INVENTORY.read_text(encoding="utf-8"))["engine"]["n_implemented"])


def test_the_resting_tree_is_green_and_the_word_is_retired() -> None:
    """POSITIVE. The directory exists, the count is measured, and the run is clean.

    The measured count is 0 and that is a MEASUREMENT rather than an absence: the
    one implemented method arrives with an oracle case, which the double-run gate
    reads as its call, so no payload file was written for it. The distinction the
    word used to carry -- a count that does not come back at all -- is now carried
    by the directory's existence.
    """
    result = _run(ENGINE_ROOT, INVENTORY)

    assert result.returncode == 0, result.stdout + result.stderr
    line = _payload_line(result)
    assert line.startswith("  ok"), line
    assert "OWED" not in result.stdout, result.stdout
    assert _implemented() > 0, (
        "no wrapper body is implemented, so the word was retired without the "
        "change that retires it"
    )


def test_a_count_that_does_not_match_the_directory_is_red(tmp_path: Path) -> None:
    """NEGATIVE. The counter, in the direction a counter goes wrong quietly.

    This is what the OWED branch used to protect and what now protects the tree in
    its place: the constant is compared against what ``find`` returns, so a
    payload landing without a reviewed one-line diff is red, and so is a diff that
    moves the number without landing a payload.
    """
    result = _run(ENGINE_ROOT, _manifest(tmp_path, invocation_payloads=7))

    assert result.returncode == 1, result.stdout + result.stderr
    line = _payload_line(result)
    assert line.startswith("  FAIL"), line
    assert "7" in line and "0" in line, line
    assert _failing_labels(result) == {"invocation_payloads"}, result.stdout


def test_a_payload_that_lands_without_a_diff_is_red(tmp_path: Path) -> None:
    """NEGATIVE. The same rule from the other side, on a real file in a real tree."""
    engine = _mirror(tmp_path)
    landed = engine / "tests" / "payloads" / "c35_resampling_inference" / "multiple_testing"
    landed.mkdir(parents=True)
    (landed / "planted.json").write_text("{}", encoding="utf-8")

    result = _run(engine, INVENTORY)

    assert result.returncode == 1, result.stdout + result.stderr
    assert _payload_line(result).startswith("  FAIL"), result.stdout
    assert _failing_labels(result) == {"invocation_payloads"}, result.stdout


def test_an_underscored_file_is_apparatus_and_is_not_counted(tmp_path: Path) -> None:
    """POSITIVE. The exclusion both readers apply, asserted rather than assumed.

    ``engine/tests/payloads/_readme.json`` is what makes the directory exist and
    the count measurable. If ``assert.sh`` counted it the resting tree would read
    1, and the committed 0 would be wrong in the quiet direction.
    """
    engine = _mirror(tmp_path)
    (engine / "tests" / "payloads" / "_second.json").write_text("{}", encoding="utf-8")

    result = _run(engine, INVENTORY)

    assert result.returncode == 0, result.stdout + result.stderr
    assert _payload_line(result).startswith("  ok"), result.stdout


def test_the_word_still_refuses_a_tree_that_carries_a_body(tmp_path: Path) -> None:
    """NEGATIVE. The retired branch, reached where it still applies, and it names it.

    The committed manifest no longer carries the word, so this branch is dead from
    the tree's own side. It is exercised against a mirror with the payload tree
    removed and the word restored, because the alternative is a branch that stays
    in the script with nothing proving it still fires.

    EVERY BODY IS REQUIRED BY NAME, AND THE NAMES ARE ASKED OF ``stub_ledger``.
    This named one body and one only, which was the whole implemented set while
    there was one; with two it would have stayed green had ``ld_count_model``
    dropped out of the report altogether -- and reporting one body where the tree
    holds two is exactly the quiet-direction miscount the surrounding suite exists
    to catch. The count is asserted beside the names for the same reason.
    """
    engine = _without_the_payload_tree(tmp_path)
    bodies = sorted(
        name
        for _, name in stub_ledger(engine / "src" / "econflow_engine" / "wrappers").implemented
    )
    assert bodies, "the mirror carries no body, so this branch has nothing to refuse"

    result = _run(engine, _manifest(tmp_path, invocation_payloads="unmeasured"))

    assert result.returncode == 1, result.stdout + result.stderr
    line = _payload_line(result)
    assert line.startswith("  FAIL"), line
    assert f"{len(bodies)} method(s) carry a body" in line, line
    unnamed = [name for name in bodies if name not in line]
    assert not unnamed, f"the bodies {unnamed} in the tree are not named in {line!r}"
    assert _failing_labels(result) == {"invocation_payloads"}, result.stdout


def test_the_word_rests_green_only_where_no_body_exists(tmp_path: Path) -> None:
    """POSITIVE for the retired branch. Its premise, on a tree that satisfies it.

    Every body in the mirror is turned back into a stub, which is the state the
    word was written for. The OWED line must survive there: its visibility was the
    whole point of the marker, and only its exit code followed the premise.

    WHICH MODULES TO FLATTEN IS ASKED OF ``stub_ledger`` AND NOT OF THE TEXT, and
    the difference is a module that carries a body AND a stub. This used to skip
    any module whose text still held the emitted raise, which was the same
    statement as "carries no body" only while every module was all-one or
    all-the-other. Card #524 is the first with one of each -- ``ld_count_model``
    written, ``ld_overdispersion_test`` not -- so the text rule left its body
    standing, the mirror reported one implemented method, and this test failed on
    a premise it had itself broken. ``stub_ledger`` is the walk
    ``engine.n_implemented`` is measured with, so the question is now asked the
    way the manifest asks it.
    """
    engine = _without_the_payload_tree(tmp_path)
    module = engine / "src" / "econflow_engine" / "wrappers"
    carries_a_body = {path for path, _ in stub_ledger(module).implemented}
    for path in sorted(module.rglob("*.py")):
        if path.name == "__init__.py" or path not in carries_a_body:
            continue
        text = path.read_text(encoding="utf-8")
        head, marker, _ = text.partition("# --- gen_wrappers: header end ---")
        if not marker:
            continue
        stubbed = head + marker + "\n\n\ndef _unused() -> None:\n    return None\n"
        path.unlink()
        path.write_text(stubbed, encoding="utf-8")

    result = _run(
        engine,
        _manifest(
            tmp_path,
            invocation_payloads="unmeasured",
            n_implemented=0,
            methods=_implemented_stub_total(engine),
        ),
    )

    assert "OWED" in _payload_line(result), result.stdout


def _implemented_stub_total(engine: Path) -> int:
    """How many stubs the flattened mirror holds, so the sum guard is satisfied.

    The flattening above deletes node functions rather than filling them in, so
    the catalogue shrinks and ``methods`` must shrink with it -- otherwise the sum
    guard fires and this test would report the premise branch by way of a
    different failure.
    """
    total = 0
    for path in sorted((engine / "src" / "econflow_engine" / "wrappers").rglob("*.py")):
        if path.name != "__init__.py":
            total += path.read_text(encoding="utf-8").count(STUB_RAISE)
    return total


def test_the_catalogue_sum_guard_fires(tmp_path: Path) -> None:
    """NEGATIVE. Implemented plus stub must account for every method in the catalogue.

    Without this, a walk that found nothing would report an empty implemented set
    and the word's premise would read true for the worst possible reason. Reached
    on the same mirror as the branch it belongs to.
    """
    engine = _without_the_payload_tree(tmp_path)

    result = _run(
        engine, _manifest(tmp_path, invocation_payloads="unmeasured", methods=1457)
    )

    assert result.returncode == 1, result.stdout + result.stderr
    line = _payload_line(result)
    assert line.startswith("  FAIL"), line
    assert "1457" in line and "1456" in line, line


def test_a_second_body_is_named_beside_the_first(tmp_path: Path) -> None:
    """NEGATIVE, and the CONTROL over the mirror itself.

    A plant must reach the report, or every red above could be the mirror rather
    than the plant. The repository's own copy of the planted module is compared
    before and after, because writing through a hardlink would edit it.
    """
    engine = _without_the_payload_tree(tmp_path)
    planted = _plant_one_body(engine)
    committed = sorted((ENGINE_ROOT / "src" / "econflow_engine" / "wrappers").rglob("*.py"))
    before = {path: path.read_bytes() for path in committed}

    result = _run(
        engine,
        _manifest(
            tmp_path, invocation_payloads="unmeasured", n_implemented=_implemented() + 1
        ),
    )

    assert {path: path.read_bytes() for path in committed} == before, (
        "the mirror wrote through a hardlink and edited the repository"
    )
    assert result.returncode == 1, result.stdout + result.stderr
    line = _payload_line(result)
    assert line.startswith("  FAIL"), line
    assert planted in line, f"{planted} is not named in {line!r}"
