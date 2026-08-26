# SPDX-License-Identifier: AGPL-3.0-only
"""The public signature of every wrapper, frozen and compared.

WHAT BREAKS IF THIS IS NOT HERE. A saved graph stores a node call by function
name and argument names. Rename one argument on one of the 913 wrappers, or
change its annotation, and every stored graph that used it stops loading -- with
no test failing, because a stub that raises NotImplementedError raises it just
as well under the new name. The signature IS the contract, and a contract needs
a copy that does not move when the code does.

WHY NOT `griffe check`. That would be the obvious answer and it does not fit:
griffe 2.1.0's ``check`` subcommand resolves ``--against`` as a GIT REFERENCE
(it runs ``git worktree add``), so it compares two checkouts and cannot read a
committed baseline file. The other half is size -- ``griffe dump`` of this
package is 30 MB, and 8 MB with docstrings and line numbers stripped, because it
serialises the value of every module constant including the NODE_META tables.
Neither number can be committed under the 3 MB ceiling in
.pre-commit-config.yaml, and neither could be reviewed as a diff.

So griffe stays as the PARSER -- nothing here re-implements Python parsing -- and
what is written out is the projection a saved graph actually depends on: the
ordered parameters, their kinds, annotations and defaults, and the return
annotation. That is 732 KB, sorted, one line per parameter, and a renamed
argument shows up as a one-line diff a reviewer can read.

Usage, from ``engine/``::

    python api-baseline/check_api.py            # compare; exit 1 on any drift
    python api-baseline/check_api.py --write    # re-freeze, deliberately
"""

from __future__ import annotations

import json
import sys
from importlib.metadata import version
from pathlib import Path
from typing import Any

import griffe

from econflow_engine.metrics import find_manifest

ENGINE_ROOT = Path(__file__).resolve().parent.parent
SRC = ENGINE_ROOT / "src"
BASELINE = Path(__file__).resolve().parent / "wrappers.json"
INVENTORY = find_manifest(Path(__file__))
PACKAGE = "econflow_engine.wrappers"

# How many differences to print before stopping. A rename applied by a careless
# sed touches all 913 at once, and a wall of output is a report nobody reads.
MAX_REPORTED = 25


def _signature(function: griffe.Function) -> dict[str, Any]:
    return {
        "parameters": [
            {
                "name": parameter.name,
                "kind": parameter.kind.value if parameter.kind else None,
                "annotation": str(parameter.annotation) if parameter.annotation else None,
                "default": str(parameter.default) if parameter.default is not None else None,
            }
            for parameter in function.parameters
        ],
        "returns": str(function.returns) if function.returns else None,
    }


def collect(search_path: Path = SRC) -> dict[str, dict[str, Any]]:
    """Load the wrapper package with griffe and project it onto its signatures."""
    package = griffe.load(PACKAGE, search_paths=[str(search_path)])
    if not isinstance(package, griffe.Module):
        raise TypeError(f"griffe resolved {PACKAGE} to {type(package).__name__}, not a module")
    found: dict[str, dict[str, Any]] = {}

    def walk(node: griffe.Module) -> None:
        # isinstance rather than the .is_module / .is_function properties: every
        # `from __future__ import annotations` and every re-export is an Alias,
        # and asking an unresolvable one what it is raises AliasResolutionError.
        for member in node.members.values():
            if isinstance(member, griffe.Module):
                walk(member)
            elif isinstance(member, griffe.Function) and not member.name.startswith("_"):
                found[member.path] = _signature(member)

    walk(package)
    return found


def _floor() -> int:
    """The anti-vacuity floor, from the one file that holds asserted constants.

    NO except-and-return-zero. A gate whose floor cannot be read has not started,
    and must never be reported as a gate that passed.
    """
    try:
        return int(json.loads(INVENTORY.read_text(encoding="utf-8"))["engine"]["methods"])
    except (OSError, KeyError, ValueError) as exc:
        sys.exit(f"check_api: cannot read the floor from {INVENTORY}: {exc}")


def _differences(baseline: dict[str, Any], live: dict[str, Any]) -> list[str]:
    out: list[str] = [f"REMOVED  {path}" for path in sorted(set(baseline) - set(live))]
    out.extend(f"ADDED    {path}" for path in sorted(set(live) - set(baseline)))
    for path in sorted(set(baseline) & set(live)):
        was, now = baseline[path], live[path]
        if was == now:
            continue
        if was["returns"] != now["returns"]:
            out.append(f"RETURN   {path}: {was['returns']} -> {now['returns']}")
        old_names = [p["name"] for p in was["parameters"]]
        new_names = [p["name"] for p in now["parameters"]]
        if old_names != new_names:
            out.append(f"ARGS     {path}: {old_names} -> {new_names}")
            continue
        for old, new in zip(was["parameters"], now["parameters"], strict=True):
            if old != new:
                out.append(f"ARG      {path}.{old['name']}: {old} -> {new}")
    return out


def main(argv: list[str]) -> int:
    live = collect()
    floor = _floor()
    if len(live) < floor:
        print(
            f"FAIL: griffe found {len(live)} public wrapper functions, below the floor "
            f"{floor} (engine.methods in {INVENTORY}). The package did not load, or the "
            "search path is wrong -- the API did not shrink by itself.",
            file=sys.stderr,
        )
        return 1

    document = {
        "_comment": (
            "The frozen public signature of every wrapper. Regenerate ONLY with "
            "`python api-baseline/check_api.py --write`, and only as a reviewed diff: "
            "every line here is an argument some saved graph may already name."
        ),
        "artifact_version": 1,
        "package": PACKAGE,
        "generated_by": f"griffe {version('griffe')}",
        "n_functions": len(live),
        "functions": dict(sorted(live.items())),
    }

    if "--write" in argv:
        rendered = json.dumps(document, indent=1, sort_keys=False)
        BASELINE.write_text(rendered + "\n", encoding="utf-8")
        print(f"check_api: froze {len(live)} signatures into {BASELINE.name}")
        return 0

    if not BASELINE.is_file():
        print(f"FAIL: no baseline at {BASELINE}; write one with --write.", file=sys.stderr)
        return 1

    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    drift = _differences(baseline["functions"], live)
    if drift:
        print(
            f"FAIL: the public API of {PACKAGE} differs from the committed baseline "
            f"in {len(drift)} place(s).",
            file=sys.stderr,
        )
        for line in drift[:MAX_REPORTED]:
            print(f"  {line}", file=sys.stderr)
        if len(drift) > MAX_REPORTED:
            print(f"  ... and {len(drift) - MAX_REPORTED} more", file=sys.stderr)
        print(
            "\nIf the change is intended, re-freeze it in its own reviewed commit:\n"
            "  python api-baseline/check_api.py --write",
            file=sys.stderr,
        )
        return 1

    print(f"check_api: {len(live)} wrapper signatures match the baseline (floor {floor})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
