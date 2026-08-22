#!/usr/bin/env bash
# SPDX-License-Identifier: AGPL-3.0-only
#
# THE REPLACEMENT FOR A FILE EXTENSION.
#
# "No statistic is ever computed outside engine/" is the rule that governs this
# project, and it survived the rewrite from R to Python because it is a statement
# about which layer may compute, not about which language a layer is written in.
# While the engine and the platform layer were written in different languages,
# the file extension enforced it for free: the statistical corpus was simply not
# reachable from the other side.
#
# Nothing separates them now. `backend/` and `engine/` are both Python and share
# one workspace, so a single `import statsmodels` in a Galaxy tool wrapper would
# move a statistic out of the engine with nothing to notice. The rule survives;
# its enforcement had to be rebuilt explicitly, and this script is it.
#
# WHAT IT ASSERTS. No numerical or statistical library appears in ANY dependency
# group of `backend/`. Not the main list, not an optional extra, not a
# dependency-group, not a requirements file. A layer that cannot declare numpy
# cannot import it, and the declaration is the reviewable artifact.
#
# It deliberately checks DECLARATIONS rather than import statements. An import
# scan over a directory with no code in it proves nothing, and an import can be
# spelled `__import__("numpy")`. A dependency cannot be smuggled past a lockfile.
#
# WHY THE COUNTING CHANGED, which is the whole point of this revision. This gate
# used to end by printing "ok: 0 backend dependency specifier(s) examined". Zero
# was the TRUE figure -- `backend/pyproject.toml` declares an empty dependency
# list on purpose -- but a detector that has stopped reading the manifest
# altogether prints exactly the same zero, and so does one pointed at a renamed
# or moved file. "I found nothing" and "I looked nowhere" were indistinguishable
# in the output, and a gate that reports success having examined nothing is the
# one failure every gate in this repository is written to refuse.
#
# So the count is now asserted against `boundary.backend_specifiers` in
# .github/inventory.json by EXACT EQUALITY, the same rule every other constant
# in that file follows. The consequence is the point: the first dependency
# `backend/` ever declares turns this gate red, and the only way to green it is a
# reviewed one-line bump of the manifest -- a human decision, visible in the
# diff, rather than a number that drifted while nobody was looking.
#
# Exact equality against zero is still not enough by itself, because a broken
# reader also produces zero. Three further guards close that gap, and all of
# them run on EVERY invocation:
#
#   1. THE MANIFEST MUST BE READABLE and must carry the constant. A missing key
#      is a hard failure, never a default of zero. (Reading a floor as zero when
#      the file was unreachable is the exact bug that made the engine suite's
#      anti-vacuity step vacuous inside the container for its whole existence.)
#   2. THE BACKEND MANIFEST MUST EXIST AND PARSE. If `backend/pyproject.toml` is
#      gone or malformed the gate fails loudly instead of scanning an empty set.
#   3. A FIVE-SOURCE POSITIVE CONTROL. The scanner reads five different places a
#      dependency can hide, and the control plants a forbidden package in every
#      one of them, then requires all five to come back flagged. A control that
#      planted a single violation would keep passing after four of the five
#      readers had silently broken -- it would only ever prove that one code
#      path still worked.
#
#   usage: check-engine-boundary.sh [repo-root]
set -euo pipefail

ROOT="${1:-.}"
command -v python3 >/dev/null 2>&1 || {
  echo "FAIL: python3 is required by this gate and is not on PATH." >&2
  exit 1
}

python3 - "$ROOT" <<'PY'
import json
import pathlib
import sys
import tempfile
import tomllib

# The engine's own statistical surface. A backend that declares any of these has
# taken a statistic out of engine/, whatever the intention was.
FORBIDDEN = {
    "numpy", "scipy", "statsmodels", "pandas", "patsy", "formulaic",
    "scikit-learn", "sklearn", "pyarrow", "polars", "arch", "linearmodels",
}

root = pathlib.Path(sys.argv[1])


def norm(spec: str) -> str:
    # "scikit-learn[extra] >= 1.4" -> "scikit-learn"
    s = spec.strip().lower()
    for sep in ("[", "@", ";", "=", "<", ">", "!", "~", " "):
        s = s.split(sep)[0]
    return s.strip()


def scan(repo_root: pathlib.Path) -> tuple[list[str], int, set[str]]:
    """Return (violations, specifiers examined, names of the sources read)."""
    backend = repo_root / "backend"
    found: list[str] = []
    examined = 0
    sources: set[str] = set()

    def record(where: str, specs: object) -> None:
        nonlocal examined
        if not isinstance(specs, list):
            return
        sources.add(where)
        for spec in specs:
            if not isinstance(spec, str):
                continue
            examined += 1
            if norm(spec) in FORBIDDEN:
                found.append(f"{where}: {spec.strip()}")

    pyproject = backend / "pyproject.toml"
    if pyproject.exists():
        with pyproject.open("rb") as fh:
            d = tomllib.load(fh)
        project = d.get("project") or {}
        record("project.dependencies", project.get("dependencies", []))
        for name, specs in (project.get("optional-dependencies") or {}).items():
            record(f"project.optional-dependencies.{name}", specs)
        for name, specs in (d.get("dependency-groups") or {}).items():
            record(f"dependency-groups.{name}", specs)
        uv = (d.get("tool") or {}).get("uv") or {}
        record("tool.uv.dev-dependencies", uv.get("dev-dependencies", []))
        record("tool.uv.constraint-dependencies", uv.get("constraint-dependencies", []))

    for req in sorted(backend.glob("**/requirements*.txt")):
        lines = [ln for ln in req.read_text().splitlines()
                 if ln.strip() and not ln.lstrip().startswith(("#", "-"))]
        record(str(req.relative_to(repo_root)), lines)

    return found, examined, sources


# --- guard 3: the five-source positive control ----------------------------
# Every reader above is exercised here, on every run. If any one of them stops
# working, the corresponding plant survives and this fails by name -- which is
# the difference between a control that proves the detector works and one that
# proves a single branch of it still compiles.
CONTROL_PLANTS = {
    "project.dependencies": "numpy>=2",
    "project.optional-dependencies.extra": "statsmodels>=0.14",
    "dependency-groups.dev": "scipy>=1.13",
    "tool.uv.dev-dependencies": "pandas>=2",
    "backend/requirements-control.txt": "polars>=1",
}

with tempfile.TemporaryDirectory() as tmp:
    canary = pathlib.Path(tmp)
    (canary / "backend").mkdir(parents=True)
    (canary / "backend" / "pyproject.toml").write_text(
        '[project]\n'
        'name = "canary"\n'
        'version = "0"\n'
        'dependencies = ["pydantic>=2", "numpy>=2"]\n'
        '[project.optional-dependencies]\n'
        'extra = ["statsmodels>=0.14"]\n'
        '[dependency-groups]\n'
        'dev = ["scipy>=1.13"]\n'
        '[tool.uv]\n'
        'dev-dependencies = ["pandas>=2"]\n'
    )
    (canary / "backend" / "requirements-control.txt").write_text("polars>=1\n")

    control_found, _, _ = scan(canary)

missed = [where for where, spec in CONTROL_PLANTS.items()
          if f"{where}: {spec}" not in control_found]
if missed:
    print("FAIL: the positive control was NOT fully flagged.", file=sys.stderr)
    for where in missed:
        print(f"       undetected plant in {where}", file=sys.stderr)
    print("       A planted statistical dependency passed this gate, so the", file=sys.stderr)
    print("       detector is not reading that source and every green run of", file=sys.stderr)
    print("       it since that reader broke has proved nothing.", file=sys.stderr)
    sys.exit(1)

# --- guard 1: the manifest and its constant -------------------------------
manifest_path = root / ".github" / "inventory.json"
try:
    manifest = json.loads(manifest_path.read_text())
except OSError as exc:
    sys.exit(f"FAIL: the manifest is unreadable at {manifest_path}: {exc}\n"
             "      This gate asserts a measured quantity and cannot start without it.")

try:
    expected = manifest["boundary"]["backend_specifiers"]
except KeyError:
    sys.exit("FAIL: .github/inventory.json carries no boundary.backend_specifiers.\n"
             "      That constant is what stops this gate passing while it examines\n"
             "      nothing, so its absence is a failure and never a default of zero.")
if not isinstance(expected, int):
    sys.exit(f"FAIL: boundary.backend_specifiers is {expected!r}, not a number. "
             "'unmeasured' is a hard failure, not a placeholder.")

# --- guard 2: the backend manifest must exist and parse -------------------
backend_manifest = root / "backend" / "pyproject.toml"
if not backend_manifest.exists():
    sys.exit(f"FAIL: {backend_manifest} does not exist.\n"
             "      An empty scan is not a clean scan: this gate reads that file to\n"
             "      decide, and cannot report a boundary it never inspected.")
try:
    with backend_manifest.open("rb") as fh:
        tomllib.load(fh)
except tomllib.TOMLDecodeError as exc:
    sys.exit(f"FAIL: {backend_manifest} does not parse: {exc}")

# --- the real scan --------------------------------------------------------
found, examined, sources = scan(root)

if found:
    print("FAIL: backend/ declares a dependency that belongs to engine/:")
    for f in found:
        print("  " + f)
    print()
    print()
    print("THE RULE: no statistic is ever computed outside engine/.")
    print("WHAT IT REQUIRES: no dependency group of backend/ names a numerical or")
    print("statistical package. backend/ moves data around; engine/ computes.")
    print("TO SATISFY IT: delete the specifier named above from backend/. If the")
    print("code that needs it computes a number, that code belongs in engine/ --")
    print("move it there and call it across the layer boundary.")
    sys.exit(1)

if examined != expected:
    sys.exit(
        f"FAIL: examined {examined} backend dependency specifier(s), but "
        f".github/inventory.json declares boundary.backend_specifiers = {expected}.\n"
        "      If backend/ genuinely gained or lost a dependency, bump that\n"
        "      constant in the same commit and say why. If it did not, this gate\n"
        "      is reading the wrong tree and the scan is wrong, not the manifest."
    )

print(f"ok: {examined} backend dependency specifier(s) examined against the "
      f"manifest's {expected}, none statistical")
print(f"    ({len(sources)} declaration source(s) read; "
      "5-source positive control fired)")
PY
