# SPDX-License-Identifier: AGPL-3.0-only
"""The numerical environment is pinned, and this is the only thing that asks.

WHY A TEST AND NOT A COMMENT. `OPENBLAS_NUM_THREADS` and its three siblings are
read ONCE, at library load time, by whichever OpenBLAS build the installed wheel
happens to vendor. Exporting them proves intent; it does not prove effect, and
nothing in this repository could tell the difference. The gap is concrete:
run_verifications.sh exports the four pins before it runs anything and a bare
pytest does not, so a developer running the suite directly sits in a different
numerical environment from the one the committed numbers were measured in.

Sitting there WITHOUT BEING TOLD is what this file removes. threadpoolctl asks
the LOADED pools how many threads they will actually use, so a suite launched
without the pins fails here instead of quietly producing different last bits
from the ones the oracle was fitted against.

WHAT A FAILURE HERE MEANS. Not that the code is wrong -- that the session was
launched in an environment the committed numbers were not measured in. The fix
is always to launch it correctly; see the message on the assertion.

WHAT THIS DOES NOT PROVE, recorded so a green run is not read as more than it
is. Thread count removes reduction-order variation. It does not make two
different OpenBLAS BUILDS agree, and it does not address kernel selection by
runtime CPU feature detection. ``uv.lock`` pins numpy to one version across 111
wheels with no `[tool.uv] environments` restriction, so the build still varies
by resolving platform. The authoritative run is the one inside the image, where
the platform is fixed and exactly one of those wheels can be selected.
"""

from __future__ import annotations

import os

import pytest
import threadpoolctl

#: Every variable that must be "1", and the pool each one governs.
THREAD_VARIABLES = (
    "OPENBLAS_NUM_THREADS",
    "OMP_NUM_THREADS",
    "MKL_NUM_THREADS",
    "NUMEXPR_NUM_THREADS",
)

_HOW = (
    "Run the suite through ./run_verifications.sh, or export "
    "OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 "
    "NUMEXPR_NUM_THREADS=1 PYTHONHASHSEED=0 TZ=UTC LC_ALL=C.UTF-8 first. "
    "These are read at library load time, so exporting them after the "
    "interpreter has started has no effect."
)


@pytest.mark.parametrize("variable", THREAD_VARIABLES)
def test_the_thread_variable_is_set_to_one(variable: str) -> None:
    assert os.environ.get(variable) == "1", (
        f"{variable} is {os.environ.get(variable)!r}, not '1'. {_HOW}"
    )


def test_the_interpreter_hash_seed_is_fixed() -> None:
    """Set and dict iteration order feed digests and serialised output."""
    assert os.environ.get("PYTHONHASHSEED") == "0", (
        f"PYTHONHASHSEED is {os.environ.get('PYTHONHASHSEED')!r}, not '0'. {_HOW}"
    )


def test_every_loaded_threadpool_reports_one_thread() -> None:
    """The assertion the environment variables alone cannot make.

    threadpoolctl inspects the pools that were actually loaded, so this fails
    when a variable was exported too late, spelled wrongly, or governs a
    different backend from the one the wheel vendored.
    """
    pools = threadpoolctl.threadpool_info()
    assert pools, (
        "threadpoolctl found no thread pools at all. numpy and scipy were not "
        "loaded, so this test examined nothing and must not read as a pass."
    )
    busy = [p for p in pools if p.get("num_threads") != 1]
    assert not busy, (
        "these pools are not single-threaded: "
        + ", ".join(
            f"{p.get('internal_api')}/{p.get('prefix')} = {p.get('num_threads')}"
            for p in busy
        )
        + f". {_HOW}"
    )
