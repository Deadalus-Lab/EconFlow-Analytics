# SPDX-License-Identifier: AGPL-3.0-only
"""``python -m econflow_engine`` -- the container's default command.

``Dockerfile`` ends in ``CMD ["python", "-m", "econflow_engine"]``, so this
module is what makes the image startable at all.

DELIBERATELY SMALL. The engine is not a service: the platform starts a
container per job, one node is computed, the container exits. This entry point
therefore answers only the three questions that can be asked without running
anything -- what is this, which version, and what does one node expect. Running
a node is a separate subcommand with a separate contract, and it is not here
yet.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Sequence

from econflow_engine import __version__
from econflow_engine.mcp.server import describe_method, list_methods


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m econflow_engine",
        description="The EconFlow Analytics computation engine.",
    )
    parser.add_argument("--version", action="version", version=__version__)

    subcommands = parser.add_subparsers(dest="command", required=True)
    describe = subcommands.add_parser(
        "describe",
        help="print one node's contract -- JSON Schema, defaults and provenance",
    )
    describe.add_argument("fn", help="the node function name, e.g. run_adf_test")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)

    # Membership is checked here rather than left to describe_method so that a
    # typo produces one named message on stderr instead of a traceback.
    if args.fn not in set(list_methods()):
        print(
            f"{args.fn}: no such node. "
            f"Run `python -m econflow_engine describe` on a name from the catalogue.",
            file=sys.stderr,
        )
        return 2

    json.dump(describe_method(args.fn), sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
