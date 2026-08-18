#!/usr/bin/env bash
# SPDX-License-Identifier: AGPL-3.0-only
#
# THE REPLACEMENT FOR A FILE EXTENSION.
#
# `docs/decisions/languages.md` stated the rule that governs this project --
# "no statistic is ever computed outside engine/" -- and for as long as the
# engine was written in another language, the file extension enforced it mechanically. A `.py` file could
# not compute an econometric statistic, because the whole statistical corpus
# would have been separated by a file extension. Nothing separates them now.
#
# No file extension separates them. `backend/` and `engine/` are both the
# same language, and one `import statsmodels` in a Galaxy tool wrapper would move
# a statistic out of the engine with nothing to notice. The rule survives; its
# enforcement has to be rebuilt explicitly, and this script is it.
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
#   usage: check-engine-boundary.sh [repo-root]
set -euo pipefail

ROOT="${1:-.}"
command -v python3 >/dev/null 2>&1 || {
  echo "FAIL: python3 is required by this gate and is not on PATH." >&2; exit 1; }

# THE POSITIVE CONTROL, and the reason this gate is trustworthy while backend/
# still holds no code. A detector pointed at an empty directory reports zero
# violations and looks exactly like a detector pointed at a clean one. This
# plants a manifest that MUST be flagged, outside the working tree, and fails if
# the detector lets it through -- the same discipline as the gitleaks canary in
# ci.yml. Without it, this gate would go green forever the day someone broke it.
canary="$(mktemp -d)"
trap 'rm -rf "$canary"' EXIT
mkdir -p "$canary/backend"
cat > "$canary/backend/pyproject.toml" <<'CANARY'
[project]
name = "canary"
version = "0"
dependencies = ["pydantic>=2"]
[project.optional-dependencies]
extra = ["statsmodels>=0.14"]
CANARY

scan() { # scan <repo-root>; prints violations, exits 1 if any
  python3 - "$1" <<'PY'
import sys, pathlib, tomllib

# The engine's own statistical surface. A backend that declares any of these has
# taken a statistic out of engine/, whatever the intention was.
FORBIDDEN = {
    "numpy", "scipy", "statsmodels", "pandas", "patsy", "formulaic",
    "scikit-learn", "sklearn", "pyarrow", "polars", "arch", "linearmodels",
}

root = pathlib.Path(sys.argv[1])
backend = root / "backend"
found, examined = [], 0

def norm(spec: str) -> str:
    # "scikit-learn[extra] >= 1.4" -> "scikit-learn"
    s = spec.strip().lower()
    for sep in ("[", "@", ";", "=", "<", ">", "!", "~", " "):
        s = s.split(sep)[0]
    return s.strip()

def record(where, specs):
    global examined
    for spec in specs:
        if not isinstance(spec, str):
            continue
        examined += 1
        if norm(spec) in FORBIDDEN:
            found.append(f"{where}: {spec.strip()}")

pyproject = backend / "pyproject.toml"
if pyproject.exists():
    d = tomllib.load(pyproject.open("rb"))
    record("project.dependencies", d.get("project", {}).get("dependencies", []))
    for name, specs in (d.get("project", {}).get("optional-dependencies") or {}).items():
        record(f"project.optional-dependencies.{name}", specs)
    for name, specs in (d.get("dependency-groups") or {}).items():
        record(f"dependency-groups.{name}", specs)
    uv = (d.get("tool") or {}).get("uv") or {}
    record("tool.uv.dev-dependencies", uv.get("dev-dependencies", []))
    record("tool.uv.constraint-dependencies", uv.get("constraint-dependencies", []))

for req in sorted(backend.glob("**/requirements*.txt")):
    lines = [ln for ln in req.read_text().splitlines()
             if ln.strip() and not ln.lstrip().startswith(("#", "-"))]
    record(str(req.relative_to(root)), lines)

if found:
    print("FAIL: backend/ declares a dependency that belongs to engine/:")
    for f in found:
        print("  " + f)
    print()
    print("No statistic is ever computed outside engine/. That rule used to be")
    print("enforced by a file extension; since both layers are Python it is")
    print("enforced here instead. See docs/decisions/python-engine.md.")
    sys.exit(1)

print(f"ok: {examined} backend dependency specifier(s) examined, none statistical.")
sys.exit(0)
PY
}

if scan "$canary" >/dev/null 2>&1; then
  echo "FAIL: the positive control was NOT flagged." >&2
  echo "      A planted backend manifest declaring statsmodels passed this gate," >&2
  echo "      so the gate is not detecting anything and every green run of it" >&2
  echo "      since detection broke has proved nothing." >&2
  exit 1
fi
echo "positive control passed: a planted statistical dependency is caught"

scan "$ROOT"
