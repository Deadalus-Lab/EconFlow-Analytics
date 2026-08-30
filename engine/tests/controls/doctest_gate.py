# SPDX-License-Identifier: AGPL-3.0-only
"""Box 2.1.18 -- doctests, asserted on the COLLECTED COUNT and never on the exit code.

THE DEFECT THIS EXISTS TO REFUSE, stated first because everything below is
shaped by it. ``pytest --doctest-modules`` over a tree containing no examples
collects nothing and exits 0. Green. Having run nothing. Wire that into a
verification script as ``pytest --doctest-modules src/ || fail`` and you have
added a gate that can never fail, over 1456 modules, and every future reader
will believe the examples are checked.

So this gate reads the COUNT, and the exit code only ever tells it whether the
count is trustworthy:

    rc 0  -- collection succeeded and found items; the count is the '::' lines
    rc 5  -- pytest's documented "no tests collected"; the count is legitimately 0
    other -- collection BROKE (import error, bad path, syntax error). The count is
             meaningless and this gate refuses it rather than reading 0 and
             calling that "no examples".

FOUR ASSERTIONS, three of them planted controls:

  1. THE WRAPPER TIER collects at least ``engine.n_implemented`` examples AND
     EVERY ONE OF THEM IS THEN RUN. The floor is 0 == 0 while the tier is all
     stubs and RISES ON ITS OWN with the first body written in 2.2 -- no second
     edit here. The 1456 wrapper docstrings carry PROSE ``Examples`` sections
     with no ``>>>`` deliberately: executable examples over typed stubs that
     raise would be 1456 guaranteed failures.

     THE RUN IS NOT OPTIONAL AND USED TO BE MISSING, which is the second shape
     of the same defect this module opens by refusing. Counting alone proves an
     example EXISTS; it cannot say the example is TRUE, and nothing else in this
     repository reaches these docstrings -- ``pyproject.toml`` sets
     ``testpaths = ["tests"]`` and adds no ``--doctest-modules``, and
     ``run_verifications.sh`` step 4 runs plain pytest. MEASURED: the first body
     written in 2.2 landed with an example asserting ``-0.1116`` for a
     coefficient of ``-0.0376``, and the counted-only gate printed
     "1 doctest example(s) ... all passing" over it.
  2. POSITIVE CONTROL -- ``doctest_wrong.py`` collects exactly 1 and MUST FAIL.
     If it ever passes, nothing is being compared and every "0 failures" this
     gate has printed was worthless.
  3. NEGATIVE CONTROL -- ``doctest_correct.py`` collects ``suite.doctest_examples``
     and MUST PASS.
  4. NEGATIVE CONTROL -- ``doctest_prose.py`` collects exactly 0 and must exit
     CLEANLY. Prose with no ``>>>`` is a legitimate docstring; a gate that
     failed it, or that reported its absence of examples as an error, would be
     unusable against the wrapper tier it exists to watch.

    usage: python -m tests.controls.doctest_gate   (run from engine/)
"""

from __future__ import annotations

import json
import pathlib
import subprocess
import sys

from econflow_engine.metrics import find_manifest

ENGINE_ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = find_manifest(pathlib.Path(__file__))
WRAPPERS = "src/econflow_engine/wrappers"
CONTROLS = "tests/controls"

#: pytest's documented exit status for "no tests were collected".
_NO_TESTS_COLLECTED = 5


def _say(message: str) -> None:
    """This module IS a gate; what it prints is its report."""
    print(message)  # noqa: T201


def _pytest(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(  # noqa: S603 - argv is built here from literals
        [sys.executable, "-m", "pytest", "--doctest-modules", "-p", "no:randomly", *args],
        capture_output=True,
        text=True,
        cwd=ENGINE_ROOT,
        check=False,
    )


def collected(path: str) -> int:
    """How many doctest items ``path`` yields. Refuses to guess when collection broke."""
    run = _pytest("--collect-only", "-q", path)
    if run.returncode == _NO_TESTS_COLLECTED:
        return 0
    if run.returncode != 0:
        _say(run.stdout)
        _say(run.stderr)
        sys.exit(
            f"FAIL: collecting doctests from {path} exited {run.returncode}. "
            "Collection BROKE -- that is not the same as finding no examples, and "
            "this gate will not read it as zero."
        )
    return sum(1 for line in run.stdout.splitlines() if "::" in line)


def inventory(section: str, key: str) -> int:
    """Read one asserted constant. A manifest that cannot be read is a failure."""
    try:
        return int(json.loads(MANIFEST.read_text(encoding="utf-8"))[section][key])
    except Exception as exc:  # noqa: BLE001 - re-raised immediately with the cause named
        sys.exit(f"FAIL: cannot read {section}.{key} from {MANIFEST}: {exc}")


def main() -> int:  # noqa: PLR0911 - one branch per asserted control, each with its own message
    """Assert the collected counts, then the two verdicts the counts cannot give."""
    expected_controls = inventory("suite", "doctest_examples")
    wrapper_floor = inventory("engine", "n_implemented")

    # --- 1. the wrapper tier: counted against a floor that rises on its own,
    #        and then RUN ---------------------------------------------------
    wrapper_examples = collected(WRAPPERS)
    if wrapper_examples < wrapper_floor:
        print(  # noqa: T201
            f"FAIL: the wrapper tier yielded {wrapper_examples} doctest example(s), "
            f"below the floor {wrapper_floor} (engine.n_implemented). An implemented "
            "method whose docstring example vanished is exactly what this catches.",
            file=sys.stderr,
        )
        return 1
    # GUARDED ON THE COUNT, NOT ON THE EXIT CODE. With no examples pytest exits 5
    # and reading that as a failure would turn an all-stub tier red; reading it as
    # a pass is the vacuity this module opens by refusing. The count already
    # cleared the floor above, so there is nothing left to run only when both are 0.
    if wrapper_examples:
        wrapper_run = _pytest("-q", WRAPPERS)
        if wrapper_run.returncode != 0:
            _say(wrapper_run.stdout)
            print(  # noqa: T201
                f"FAIL: the wrapper tier's {wrapper_examples} doctest example(s) were "
                "collected but did not all pass. The failure above names the module "
                "and the line; a wrapper example is a claim about what the body "
                "RETURNS, so either the example or the body is wrong.",
                file=sys.stderr,
            )
            return 1

    # --- 2. POSITIVE control: a wrong example MUST fail ---------------------
    wrong_path = f"{CONTROLS}/doctest_wrong.py"
    wrong_collected = collected(wrong_path)
    if wrong_collected != 1:
        print(  # noqa: T201
            f"FAIL: the positive control collected {wrong_collected} example(s), "
            "expected exactly 1. The control itself is broken, so it proves nothing.",
            file=sys.stderr,
        )
        return 1
    if _pytest("-q", wrong_path).returncode == 0:
        print(  # noqa: T201
            "FAIL: the positive control PASSED. doctest_wrong.py asserts 5 for an "
            "expression that evaluates to 4, so a pass means output is not being "
            "compared at all and this gate cannot fail.",
            file=sys.stderr,
        )
        return 1

    # --- 3. NEGATIVE control: correct examples MUST pass --------------------
    correct_path = f"{CONTROLS}/doctest_correct.py"
    correct_collected = collected(correct_path)
    if correct_collected != expected_controls:
        print(  # noqa: T201
            f"FAIL: the control module collected {correct_collected} example(s), the "
            f"manifest says {expected_controls}. Re-run the suite.doctest_examples "
            "command in .github/inventory.json and move the number in its own diff.",
            file=sys.stderr,
        )
        return 1
    correct_run = _pytest("-q", correct_path)
    if correct_run.returncode != 0:
        _say(correct_run.stdout)
        print(  # noqa: T201
            "FAIL: the negative control FAILED. Its examples are correct, so a "
            "failure here means the doctest runner is rejecting valid output.",
            file=sys.stderr,
        )
        return 1

    # --- 4. NEGATIVE control: prose with no '>>>' is zero, not an error ------
    prose_path = f"{CONTROLS}/doctest_prose.py"
    prose_collected = collected(prose_path)
    if prose_collected != 0:
        print(  # noqa: T201
            f"FAIL: the prose control collected {prose_collected} example(s), expected "
            "0. An indented prose block is being read as an example, which would fail "
            "all 1456 wrapper docstrings the moment this ran over them.",
            file=sys.stderr,
        )
        return 1

    _say(
        f"ok: {wrapper_examples} doctest example(s) under {WRAPPERS} "
        f"(floor {wrapper_floor} = engine.n_implemented) and {correct_collected} in "
        f"the controls -- all {wrapper_examples + correct_collected} RUN and passing; "
        "the wrong-output control failed and the prose control collected 0, "
        "as both must."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
