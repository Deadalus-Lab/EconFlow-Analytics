# SPDX-License-Identifier: AGPL-3.0-only
"""Box 2.1.17 -- read mutmut's stats, and refuse 0/0 BEFORE reading a kill rate.

THE ARITHMETIC THIS EXISTS TO REFUSE:

    killed / total  ==  0 / 0

Point mutmut at a path that does not exist, or mistype a glob in
``[tool.mutmut] only_mutate``, and it generates zero mutants and kills zero of
them. Every naive formula then reports a PERFECT score -- 100 %, or a
``ZeroDivisionError`` that a ``try`` swallows into 100 % -- for having tested
nothing at all. That is the same shape as a doctest run over a tree with no
examples, and the same shape as the coverage floor that read 0 inside the image
for its whole existence.

SO THE ORDER OF THE TWO ASSERTIONS IS THE WHOLE DESIGN, and it is not an
implementation detail:

    1. ``total >= mutation.min_mutants``     <- FIRST. Always. No exceptions.
    2. ``killed / total >= min_kill_rate``   <- only ever reached after (1) held.

Reversing them, or computing the rate before checking the denominator, restores
exactly the defect. :func:`kill_rate` refuses to divide at all when the
denominator is zero, so the bug cannot be reintroduced by a caller either.

WHERE THE NUMBERS COME FROM. ``mutmut export-cicd-stats`` writes
``mutants/mutmut-cicd-stats.json`` with ``killed``, ``survived``, ``total``,
``no_tests``, ``skipped``, ``suspicious``, ``timeout`` and ``segfault``
(mutmut/__main__.py:1174-1191, measured at 3.7.0).

AND IT HAS ITS OWN VACUOUS PATH, WHICH THIS GATE CLOSES. When no run has
happened, ``export-cicd-stats`` prints ``No previous mutation data found. Run
"mutmut run" first.`` and EXITS 0 WITHOUT WRITING THE FILE (__main__.py:1213-1218).
A gate that shelled out and trusted the exit status would go green having
measured nothing, so this reads the FILE and treats its absence as a failure.

    usage: python -m tests.controls.mutation_gate [stats.json]   (run from engine/)
"""

from __future__ import annotations

import json
import pathlib
import sys
from typing import Any

ENGINE_ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ENGINE_ROOT.parent / ".github" / "inventory.json"
DEFAULT_STATS = ENGINE_ROOT / "mutants" / "mutmut-cicd-stats.json"


def _say(message: str) -> None:
    """This module IS a gate; what it prints is its report."""
    print(message)  # noqa: T201


def kill_rate(killed: int, total: int) -> float:
    """The percentage killed. REFUSES to divide when there is nothing to divide.

    Returning 0.0, or letting a ``ZeroDivisionError`` be caught upstairs, both
    end with a number that a caller can compare against a floor -- and 0/0 has no
    honest number. It raises instead, so the vacuous case cannot be turned into
    a score by anyone.
    """
    if total <= 0:
        raise ValueError(
            f"kill_rate: {killed} killed of {total} generated has no value. "
            "A rate over zero mutants is not a score, it is a missing measurement."
        )
    return 100.0 * killed / total


def manifest_section(name: str) -> dict[str, Any]:
    """Read one manifest section, or fail naming it."""
    try:
        section: dict[str, Any] = json.loads(MANIFEST.read_text(encoding="utf-8"))[name]
    except Exception as exc:  # noqa: BLE001 - re-raised immediately with the cause named
        sys.exit(f"FAIL: cannot read the '{name}' section from {MANIFEST}: {exc}")
    return section


def main(argv: list[str]) -> int:
    """Assert the mutant count, THEN the kill rate. Never the other way round."""
    stats_path = pathlib.Path(argv[1]) if len(argv) > 1 else DEFAULT_STATS
    config = manifest_section("mutation")

    for key in ("min_mutants", "min_kill_rate"):
        if config.get(key) == "unmeasured":
            print(  # noqa: T201
                f"FAIL: mutation.{key} is 'unmeasured'. That is a HARD FAILURE and "
                "not a placeholder: it marks a floor whose measurement is not in the "
                "tree yet. Run the command from the 'commands' block and replace the "
                "word with the figure, in its own reviewed diff.",
                file=sys.stderr,
            )
            return 1

    # `export-cicd-stats` exits 0 WITHOUT writing this file when no run happened.
    if not stats_path.is_file():
        print(  # noqa: T201
            f"FAIL: no mutation stats at {stats_path}. `mutmut export-cicd-stats` "
            "prints 'No previous mutation data found' and EXITS 0 when no run has "
            "happened, so its exit status proves nothing. Run `mutmut run` first.",
            file=sys.stderr,
        )
        return 1

    stats = json.loads(stats_path.read_text(encoding="utf-8"))
    total = int(stats["total"])
    killed = int(stats["killed"])

    # --- ASSERTION 1, AND IT COMES FIRST ------------------------------------
    min_mutants = int(config["min_mutants"])
    if min_mutants <= 0:
        print(  # noqa: T201
            "FAIL: mutation.min_mutants is 0. A floor of zero is not a floor -- it "
            "admits precisely the 0-of-0 run this gate exists to refuse.",
            file=sys.stderr,
        )
        return 1
    if total < min_mutants:
        print(  # noqa: T201
            f"FAIL: mutmut generated {total} mutant(s), below the floor {min_mutants}. "
            "The target paths in [tool.mutmut] only_mutate are wrong, not the tree. "
            "NO KILL RATE IS REPORTED, deliberately: a rate over too few mutants is "
            "the vacuous measurement this floor exists to catch.",
            file=sys.stderr,
        )
        return 1

    # --- ASSERTION 2, reached only because assertion 1 held ------------------
    rate = kill_rate(killed, total)
    floor = float(config["min_kill_rate"])
    survived = int(stats["survived"])
    if rate < floor:
        print(  # noqa: T201
            f"FAIL: {rate:.1f} % of {total} mutants killed, below the floor "
            f"{floor} %. {survived} mutant(s) survived: each is a change to the "
            "engine that no test objects to. Write the test, do not lower the floor.",
            file=sys.stderr,
        )
        return 1

    _say(
        f"ok: {killed} of {total} mutants killed ({rate:.1f} %, floor {floor} %); "
        f"{survived} survived (mutant floor {min_mutants})."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
