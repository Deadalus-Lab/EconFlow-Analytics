# SPDX-License-Identifier: AGPL-3.0-only
"""``python -m econflow_engine`` -- the container's default command.

``Dockerfile`` ends in ``CMD ["python", "-m", "econflow_engine"]``, so this
module is what makes the image startable at all. The console script declared in
``pyproject.toml`` points at the same ``main``; the module path is the one the
image proves, and it stays the CMD for that reason.

DELIBERATELY SMALL. The engine is not a service: the platform starts a container
per job, one node is computed, the container exits. This entry point therefore
answers what can be asked about the catalogue -- what is this, which version,
what does one node expect, which nodes exist -- and runs exactly one node.

THE EXIT CODE IS THE RESULT, NOT A HEALTH CHECK. A caller that only sees "the
process failed" cannot tell a typo from a refusal from an unwritten body, and
those need three different responses. So the four outcomes of a node call are
four exit codes:

    0  succeeded          the payload is on stdout
    2  unknown fn         a name that is not in the catalogue, or an unreadable body
    3  refused            the wire contract answered; the reason code is on stderr
    4  not-implemented    the contract is live, the body is not written yet

The response document is printed on stdout in every one of the last three cases
too, so a caller that wants the message rather than the code has it.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Sequence
from typing import Any

from econflow_engine import __version__
from econflow_engine.mcp.gateway import list_methods, run_method
from econflow_engine.mcp.server import describe_method

#: state -> exit code. `succeeded` is 0; the rest are distinct so that a shell
#: caller can branch without parsing the payload.
EXIT_FOR_STATE = {"succeeded": 0, "refused": 3, "not-implemented": 4}

UNKNOWN_NODE = 2


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
    describe.add_argument("fn", help="the node function name, e.g. arw_open_dataset")

    run = subcommands.add_parser(
        "run", help="run one node and print its response document as JSON")
    run.add_argument("fn", help="the node function name, e.g. arw_open_dataset")
    run.add_argument(
        "--json",
        dest="body",
        help="the request body as a JSON object; read from stdin when absent",
    )

    listing = subcommands.add_parser("list", help="print every node name, one per line")
    listing.add_argument(
        "--category",
        help="narrow to one category, e.g. 00-data-utilities",
    )
    return parser


def _unknown_node(fn: str) -> int:
    # Membership is checked here rather than left to the gateway so that a typo
    # produces one named message on stderr instead of a response document a
    # caller has to parse to discover it misspelt something.
    print(
        f"{fn}: no such node. "
        f"Run `python -m econflow_engine list` for the catalogue.",
        file=sys.stderr,
    )
    return UNKNOWN_NODE


def _read_body(raw: str | None) -> dict[str, Any]:
    """Parse the request body, raising ValueError with a message a user can act on."""
    text = sys.stdin.read() if raw is None else raw
    try:
        body = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError(f"the request body is not valid JSON ({exc}).") from exc
    if not isinstance(body, dict):
        raise ValueError(
            f"the request body must be a JSON object mapping argument names to "
            f"values, not {type(body).__name__}."
        )
    return body


def _describe(fn: str, known: set[str]) -> int:
    if fn not in known:
        return _unknown_node(fn)
    json.dump(describe_method(fn), sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    return 0


def _run(fn: str, raw_body: str | None, known: set[str]) -> int:
    if fn not in known:
        return _unknown_node(fn)
    try:
        body = _read_body(raw_body)
    except ValueError as exc:
        print(f"{fn}: {exc}", file=sys.stderr)
        return UNKNOWN_NODE

    response = run_method(fn, body)
    json.dump(response.to_dict(), sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    if response.state == "refused":
        print(f"{fn}: refused ({response.reason_code}).", file=sys.stderr)
    return EXIT_FOR_STATE[response.state]


def _list(category: str | None) -> int:
    names = list_methods(category)
    if not names:
        # An empty listing is what a mistyped category produces, and exiting 0
        # on it reports that the category exists and is empty.
        print(
            f"{category}: no such category, or it publishes no node.",
            file=sys.stderr,
        )
        return UNKNOWN_NODE
    sys.stdout.write("".join(f"{name}\n" for name in names))
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    if args.command == "list":
        return _list(args.category)

    known = set(list_methods())
    if args.command == "run":
        return _run(args.fn, args.body, known)
    return _describe(args.fn, known)


if __name__ == "__main__":
    raise SystemExit(main())
