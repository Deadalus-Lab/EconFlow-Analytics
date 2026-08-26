# SPDX-License-Identifier: AGPL-3.0-only
"""The three spellings that cannot import Python still agree with the one that can.

Box 2.1.1.6. ``econflow_engine.metrics`` is now the single definition of an
implemented body, and the four Python copies that used to answer the same
question are gone. Three copies remain and cannot be deleted:

    README.md                                   a table row a person reads.
    .github/inventory.json commands.n_implemented   the manifest's own recipe.
    .github/actions/assert-inventory/assert.sh  a heredoc that runs before the
                                                engine's environment exists.

None of them can call ``is_stub``, so what replaces the deleted copies is this:
each one is extracted, run, and its answer compared with the module's. A
divergence is a red test rather than a quiet one.

IT WAS QUIET BEFORE, WHICH IS WHY THE COMPARISON IS AGAINST PLANTED TREES AND
NOT AGAINST THE COMMITTED ONE. The README's spelling and the manifest's
disagreed in BOTH directions for the whole time they sat side by side -- the
README counted an undocumented stub as implemented, and counted a real body that
ended in a ``NotImplementedError`` as a stub, which is the dangerous direction
because it publishes a zero while work exists. Over the committed tree the two
agreed anyway, because ``[tool.interrogate] fail-under = 100`` puts a docstring
on every function and neither disagreeing case can occur. The agreement was an
accident of an unrelated setting. A comparison run only over ``src/`` would
inherit that accident and prove nothing, so every case below is planted in a
tree built under ``tmp_path``.

THE VERDICTS ARE WRITTEN DOWN, not merely shared. Four spellings agreeing on a
count is worth nothing if all four are wrong together, so ``CASES`` states the
expected verdict for each planted function independently, and the module is
checked against that table before the other three are checked against the
module.
"""

from __future__ import annotations

import ast
import json
import re
import shlex
import subprocess
import sys
from pathlib import Path

import pytest

from econflow_engine.metrics import find_manifest, is_stub, stub_ledger

ENGINE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = find_manifest(Path(__file__)).parent.parent
README = REPO_ROOT / "README.md"
MANIFEST = find_manifest(Path(__file__))
ASSERT_SH = REPO_ROOT / ".github" / "actions" / "assert-inventory" / "assert.sh"

#: The row of README.md's table whose command counts implemented methods.
README_ROW = "Methods carrying an implementation"

#: The heredoc delimiter assert.sh opens its walk with.
HEREDOC_SIGIL = "AST"

#: The wrapper path all three spellings hard-code, relative to their working
#: directory. A planted tree has to be laid out the same way to be walked.
WRAPPERS_RELATIVE = Path("src") / "econflow_engine" / "wrappers"

#: Every function planted below, with the verdict the definition gives it and a
#: note saying what the case is for. ``True`` means "a generated stub".
CASES: dict[str, tuple[bool, str]] = {
    "documented_stub": (True, "the shape gen_wrappers emits: docstring, then the raise"),
    "undocumented_stub": (
        True,
        "no docstring. The retired README spelling required a body of exactly two "
        "statements and called this one implemented",
    ),
    "bare_name_stub": (True, "raise NotImplementedError with no call and no arguments"),
    "second_string_stub": (True, "a second bare string expression is stripped like the first"),
    "async_stub": (True, "an async def is walked and judged like any other function"),
    "documented_body": (
        False,
        "a statement before the raise. This is the dangerous direction: the retired "
        "README spelling called it a stub and would have published a zero over it",
    ),
    "undocumented_body": (False, "the same, with no docstring to pad the body"),
    "raises_value_error": (False, "a raise of something else is a body, not a stub"),
    "attribute_raise": (False, "errors.NotImplementedError is not the built-in name"),
    "returns_a_value": (False, "an ordinary implemented body"),
    "two_statement_body": (False, "two statements, neither of them a raise"),
    "outer_with_a_nested_function": (False, "the body that carries the nested case below"),
    "nested_public_stub": (
        True,
        "REACHABLE ONLY BY ast.walk. Defined inside another function's body, so a "
        "spelling that iterated module.body instead would never see it",
    ),
    "method_body": (
        False,
        "REACHABLE ONLY BY ast.walk. A method hangs off a ClassDef, which is not a "
        "FunctionDef, so module.body skips the class and everything in it",
    ),
    "method_stub": (True, "the same, in the stub direction"),
}

#: Planted alongside the cases and counted by nothing: every spelling skips a
#: name beginning with an underscore, so neither may appear in the implemented
#: list or the stub count.
#:
#: THERE ARE TWO OF THEM BECAUSE ONE WAS NOT ENOUGH, and this was found by
#: perturbing rather than by reading. With only a private STUB planted, weakening
#: a spelling's skip from ``_`` to ``__`` changed no answer at all -- the newly
#: visible function was a stub, and a stub does not join the implemented count.
#: The private BODY is what makes the skip load-bearing in the direction that
#: gets published.
PRIVATE_NAMES = ("_private_stub", "_private_body")

# REUSE-IgnoreStart
#
# THE PLANTED MODULES CARRY AN SPDX HEADER BECAUSE THE REAL ONES DO, and
# ``reuse lint`` reads a string literal it cannot distinguish from a declaration.
# Measured 2026-08-26 in CI: it parsed ``AGPL-3.0-only\n"""Planted."""\n`` as an
# expression and reported two invalid ones, turning workflow-lint red over text
# that licenses nothing and is written to a temporary directory. Dropping the
# header from the fixtures would be the wrong repair -- the header is part of
# what a wrapper module looks like, and a fixture that omits it stops resembling
# the thing under test. The tool documents this bracket for exactly this case.
_MODULE = f'''# SPDX-License-Identifier: AGPL-3.0-only
"""A planted wrapper module. Not part of the engine."""


def documented_stub(x: int) -> int:
    """A stub."""
    raise NotImplementedError("documented_stub")


def undocumented_stub(x: int) -> int:
    raise NotImplementedError("undocumented_stub")


def bare_name_stub(x: int) -> int:
    """A stub."""
    raise NotImplementedError


def second_string_stub(x: int) -> int:
    """A stub."""
    "a second string expression, which is not a docstring"
    raise NotImplementedError("second_string_stub")


async def async_stub(x: int) -> int:
    """A stub."""
    raise NotImplementedError("async_stub")


def documented_body(x: int) -> int:
    """A body."""
    import math

    raise NotImplementedError(math.floor(x))


def undocumented_body(x: int) -> int:
    import math

    raise NotImplementedError(math.floor(x))


def raises_value_error(x: int) -> int:
    """A body."""
    raise ValueError("raises_value_error")


def attribute_raise(x: int) -> int:
    """A body."""
    import errors

    raise errors.NotImplementedError("attribute_raise")


def returns_a_value(x: int) -> int:
    """A body."""
    return x + 1


def two_statement_body(x: int) -> int:
    """A body."""
    y = x + 1
    return y


def outer_with_a_nested_function(x: int) -> int:
    """A body that defines a public function inside itself."""

    def nested_public_stub(y: int) -> int:
        """A stub one level down, invisible to a top-level walk."""
        raise NotImplementedError("nested_public_stub")

    return nested_public_stub(x)


class PublicHelper:
    """A class in a wrapper module. Its methods hang off a ClassDef."""

    def method_body(self, x: int) -> int:
        """A body on a class."""
        return x + 1

    def method_stub(self, x: int) -> int:
        """A stub on a class."""
        raise NotImplementedError("method_stub")


def {PRIVATE_NAMES[0]}(x: int) -> int:
    """A private stub, which every spelling skips."""
    raise NotImplementedError("{PRIVATE_NAMES[0]}")


def {PRIVATE_NAMES[1]}(x: int) -> int:
    """A private body, which every spelling skips."""
    return x * 2
'''


@pytest.fixture(scope="module")
def planted(tmp_path_factory: pytest.TempPathFactory) -> Path:
    """A wrapper tree built OUTSIDE the repository, holding every case at once.

    ``__init__.py`` is written because a real wrapper package has one and every
    spelling skips it by name; a planted tree without one would leave that skip
    unexercised.
    """
    root = tmp_path_factory.mktemp("planted")
    package = root / WRAPPERS_RELATIVE / "c99_planted"
    package.mkdir(parents=True)
    (root / WRAPPERS_RELATIVE / "__init__.py").write_text(
        '# SPDX-License-Identifier: AGPL-3.0-only\n"""Planted."""\n', encoding="utf-8"
    )
    (package / "__init__.py").write_text(
        '# SPDX-License-Identifier: AGPL-3.0-only\n"""Planted."""\n'
        "\n\ndef init_level_stub() -> int:\n"
        '    """Skipped: every spelling skips __init__.py by name."""\n'
        "    raise NotImplementedError\n",
        encoding="utf-8",
    )
    (package / "planted.py").write_text(_MODULE, encoding="utf-8")
    return root


# REUSE-IgnoreEnd


def readme_command() -> str:
    """The shell command README.md prints beside its implemented-methods figure.

    The row is found by its label rather than by line number, and a table that
    no longer carries it is an error: a silent no-match would leave this suite
    comparing the module against nothing.
    """
    rows = [
        line
        for line in README.read_text(encoding="utf-8").splitlines()
        if line.startswith("|") and README_ROW in line
    ]
    if len(rows) != 1:
        raise AssertionError(f"{README} carries {len(rows)} row(s) labelled {README_ROW!r}, not 1")
    spans: list[str] = re.findall(r"`([^`]+)`", rows[0])
    if len(spans) != 1:
        raise AssertionError(f"the {README_ROW!r} row carries {len(spans)} code span(s), not 1")
    return spans[0].replace("\\|", "|")


def manifest_command() -> str:
    """The recipe the manifest prints for ``engine.n_implemented``."""
    return str(json.loads(MANIFEST.read_text(encoding="utf-8"))["commands"]["n_implemented"])


def assert_sh_program() -> str:
    """The Python the ``n_implemented`` heredoc in assert.sh feeds to stdin."""
    text = ASSERT_SH.read_text(encoding="utf-8")
    opener = f"python3 - <<'{HEREDOC_SIGIL}'\n"
    if text.count(opener) != 1:
        raise AssertionError(f"{ASSERT_SH} opens {text.count(opener)} {HEREDOC_SIGIL} heredoc(s)")
    body = text.split(opener, 1)[1]
    closer = f"\n{HEREDOC_SIGIL}\n"
    if closer not in body:
        raise AssertionError(f"the {HEREDOC_SIGIL} heredoc in {ASSERT_SH} is never closed")
    return body.split(closer, 1)[0]


def _run(program: str, cwd: Path) -> str:
    """Run one extracted spelling against a planted tree and return what it printed."""
    done = subprocess.run(  # noqa: S603  (argv form, interpreter by absolute path)
        [sys.executable, "-c", program],
        cwd=cwd,
        capture_output=True,
        text=True,
        check=False,
    )
    if done.returncode != 0:
        raise AssertionError(f"the extracted spelling failed:\n{done.stderr}")
    return done.stdout.strip()


def _run_shell_form(command: str, cwd: Path) -> str:
    """Run a ``python3 -c "..."`` command string without a shell.

    ``shlex.split`` recovers the program from the quoting, and the interpreter is
    replaced with ``sys.executable`` so the answer comes from the environment the
    suite itself runs under rather than from whatever ``python3`` resolves to.
    """
    argv = shlex.split(command)
    if argv[:2] != ["python3", "-c"] or len(argv) != 3:
        raise AssertionError(
            f"expected `python3 -c <program>`, got {argv[:2]} of {len(argv)} word(s)"
        )
    return _run(argv[2], cwd)


def test_the_module_gives_every_planted_case_the_verdict_written_down(planted: Path) -> None:
    """THE ANCHOR. Without this the other tests only prove four spellings agree.

    Each planted function is judged on its own, so a definition that drifted in
    a way all four spellings shared would still be caught here.
    """
    module = ast.parse((planted / WRAPPERS_RELATIVE / "c99_planted" / "planted.py").read_text())
    verdicts = {
        node.name: is_stub(node)
        for node in ast.walk(module)
        if isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef)
    }
    expected = {name: verdict for name, (verdict, _) in CASES.items()}
    expected[PRIVATE_NAMES[0]] = True
    expected[PRIVATE_NAMES[1]] = False
    assert verdicts == expected, {
        name: CASES[name][1]
        for name in verdicts
        if name in CASES and verdicts[name] != expected[name]
    }


def test_the_ledger_counts_the_planted_tree_and_skips_what_it_must(planted: Path) -> None:
    """The walk's own answer, before any other spelling is compared with it."""
    ledger = stub_ledger(planted / WRAPPERS_RELATIVE)
    names = sorted(name for _, name in ledger.implemented)
    assert names == sorted(name for name, (stub, _) in CASES.items() if not stub)
    assert ledger.stubs == sum(1 for stub, _ in CASES.values() if stub)
    for private in PRIVATE_NAMES:
        assert private not in names, f"{private} reached the implemented list"
    assert ledger.stubs == 7, "a private stub or the __init__.py stub was counted"
    assert "method_body" in names, (
        "a top-level-only walk reached this ledger: a method hangs off a ClassDef and "
        "only ast.walk descends into it"
    )


@pytest.mark.parametrize("source", ["readme", "manifest"])
def test_the_published_one_liners_count_what_the_module_counts(planted: Path, source: str) -> None:
    """README.md and the manifest's recipe, extracted and run against the plant.

    Both print one number: how many public wrapper functions carry a body. It is
    compared with ``stub_ledger``'s over the same tree.
    """
    command = readme_command() if source == "readme" else manifest_command()
    printed = _run_shell_form(command, planted)
    expected = len(stub_ledger(planted / WRAPPERS_RELATIVE).implemented)
    assert printed == str(expected), (
        f"the {source} spelling counts {printed} implemented function(s) where "
        f"econflow_engine.metrics counts {expected}, over the same planted tree"
    )


def test_the_assert_sh_heredoc_reports_what_the_module_reports(planted: Path) -> None:
    """The shell copy, extracted and run against the plant.

    It prints three answers rather than one -- the implemented count, the stub
    count and the first five implemented names -- because the payload sentinel
    beside it spends all three. All three are compared.
    """
    printed = _run(assert_sh_program(), planted)
    ledger = stub_ledger(planted / WRAPPERS_RELATIVE)
    names = sorted(name for _, name in ledger.implemented)
    expected = f"{len(ledger.implemented)} {ledger.stubs} {','.join(names[:5]) or '-'}"
    assert printed == expected, (
        f"the assert.sh heredoc reports {printed!r} where econflow_engine.metrics "
        f"reports {expected!r}, over the same planted tree"
    )


def test_every_spelling_agrees_over_the_committed_tree_as_well() -> None:
    """The live tree too, which is the figure that actually gets published.

    THIS ONE IS THE WEAKEST OF THE FIVE AND IS KEPT ANYWAY. Measured while
    perturbing: weakening the README spelling's private-name skip from ``_`` to
    ``__`` leaves this test green, because no wrapper function is both private
    and implemented. The planted cases are what carry the suite; this is the
    claim ``engine.n_implemented`` actually rests on, and it costs three
    subprocesses.
    """
    ledger = stub_ledger(ENGINE_ROOT / WRAPPERS_RELATIVE)
    declared = int(json.loads(MANIFEST.read_text(encoding="utf-8"))["engine"]["n_implemented"])
    assert len(ledger.implemented) == declared

    assert _run_shell_form(readme_command(), ENGINE_ROOT) == str(declared)
    assert _run_shell_form(manifest_command(), ENGINE_ROOT) == str(declared)
    names = sorted(name for _, name in ledger.implemented)
    assert _run(assert_sh_program(), ENGINE_ROOT) == (
        f"{declared} {ledger.stubs} {','.join(names[:5]) or '-'}"
    )
