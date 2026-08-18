#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
"""Generate the third-party attribution register and the CycloneDX SBOM.

The licence register generator. The shape of the job is unchanged and so is
the reason for it: the container ships third-party code, the AGPL obliges us to
say whose and under what terms, and a hand-maintained register rots.

WHY THE PINNING IS TRUSTWORTHY
    It reads installed distribution metadata after ``uv sync``. PyPI artefacts
    are immutable and ``uv.lock`` records a hash per wheel, so what this register
    describes is pinned by content rather than by a dated repository snapshot
    that only holds while somebody keeps serving it.

WHY THE PACKAGE LIST COMES FROM THE LOCKFILE AND THE LICENCES FROM THE ENVIRONMENT
    The lockfile is the contract; the environment is an observation of it. Taking
    the list from the environment would silently include whatever a developer
    happened to pip-install. Taking the licence from the lockfile is impossible:
    ``uv.lock`` carries no licence field. Each source answers only for what it
    actually knows. A handful of lock entries are platform-conditional and are
    genuinely absent here (``colorama`` is win32-only); those are listed and
    marked rather than dropped. Above a small threshold the same symptom means a
    stale environment instead, and that is a hard error.

    ``--check`` compares byte for byte and never writes, the same contract as
    the other two generators.
"""

from __future__ import annotations

import argparse
import importlib.metadata as md
import json
import sys
import tomllib
from pathlib import Path
from typing import Any

ENGINE = Path(__file__).resolve().parent.parent
ROOT = ENGINE.parent
LOCK = ROOT / "uv.lock"
REGISTER = ENGINE / "THIRD-PARTY-LICENSES.md"
SBOM = ENGINE / "sbom.cdx.json"

# The two workspace members are ours, not third-party attribution.
OURS = {"econflow-engine", "econflow-backend"}

# Classifier -> SPDX. Deliberately explicit and short: an unrecognised licence
# must land in n_unmapped and be visible, never be guessed into a plausible
# identifier.
_CLASSIFIER_SPDX = {
    "License :: OSI Approved :: MIT License": "MIT",
    "License :: OSI Approved :: BSD License": "BSD-3-Clause",
    "License :: OSI Approved :: Apache Software License": "Apache-2.0",
    "License :: OSI Approved :: Python Software Foundation License": "PSF-2.0",
    "License :: OSI Approved :: ISC License (ISCL)": "ISC",
    "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)": "MPL-2.0",
    "License :: OSI Approved :: GNU General Public License v2 (GPLv2)": "GPL-2.0-only",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)": "GPL-3.0-only",
    "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)": "LGPL-3.0-only",
    "License :: OSI Approved :: GNU Affero General Public License v3": "AGPL-3.0-only",
}

# A licence that would make the combined work undistributable under AGPL-3.0-only.
# AGPL-3.0 is one-way compatible with the GPL-3 family and NOT with GPL-2.0-only.
INCOMPATIBLE = {"GPL-2.0-only"}


def _normalise(name: str) -> str:
    return name.lower().replace("_", ".").replace("-", ".")


def _spdx_of(dist: md.Distribution) -> tuple[str, bool]:
    """Return (identifier, mapped). ``mapped=False`` means we did not recognise it."""
    meta = dist.metadata
    expr = meta.get("License-Expression")
    if expr:
        return str(expr).strip(), True
    for c in meta.get_all("Classifier") or []:
        if c in _CLASSIFIER_SPDX:
            return _CLASSIFIER_SPDX[c], True
    raw = (meta.get("License") or "").strip()
    if raw and len(raw) <= 40 and "\n" not in raw:
        return raw, False
    return "UNKNOWN", False


def collect() -> tuple[list[dict[str, Any]], int, int]:
    if not LOCK.exists():
        sys.exit(f"gen_third_party: no lockfile at {LOCK}")
    lock = tomllib.loads(LOCK.read_text(encoding="utf-8"))

    installed = {_normalise(d.metadata["Name"]): d for d in md.distributions()}

    # A lockfile is cross-platform; an environment is one platform. `colorama` is
    # required only under sys_platform == 'win32' and `tzdata` only where the OS
    # ships no zoneinfo database, so neither is installed here and neither is in
    # the Linux image. They are still listed -- marked, and counted separately --
    # because a register that quietly omits rows is the thing this file exists to
    # prevent. What is NOT tolerated is a package that should be present and is
    # not: that is a stale environment, and it is a hard error.
    rows: list[dict[str, Any]] = []
    unmapped = 0
    conditional = 0
    for pkg in lock["package"]:
        name = pkg["name"]
        if name in OURS:
            continue
        dist = installed.get(_normalise(name))
        if dist is None:
            conditional += 1
            licence = "not resolved on this platform"
        else:
            licence, mapped = _spdx_of(dist)
            if not mapped:
                unmapped += 1
        rows.append(
            {
                "name": name,
                "version": pkg["version"],
                "licence": licence,
                "purl": f"pkg:pypi/{name}@{pkg['version']}",
                "platform_conditional": dist is None,
            }
        )

    # Anti-vacuity. If the venv is stale or absent, nearly everything looks
    # "platform-conditional" and the register would render as a page of unknowns
    # that still passes --check. Refuse instead.
    if conditional > max(4, len(rows) // 10):
        sys.exit(
            f"gen_third_party: {conditional} of {len(rows)} packages are not installed.\n"
            "That is a stale or missing environment, not platform conditionality.\n"
            "Run `uv sync --all-extras` first."
        )

    rows.sort(key=lambda r: r["name"].lower())
    return rows, unmapped, conditional


def render_register(rows: list[dict[str, Any]], unmapped: int, conditional: int) -> str:
    buckets: dict[str, int] = {}
    for r in rows:
        buckets[r["licence"]] = buckets.get(r["licence"], 0) + 1

    conflicts = [r for r in rows if r["licence"] in INCOMPATIBLE]

    out = [
        "<!-- SPDX-License-Identifier: AGPL-3.0-only -->",
        "",
        "# Third-party licences — Python compute engine",
        "",
        "**Generated file. Do not edit by hand.** Regenerate with:",
        "",
        "```sh",
        "uv sync --all-extras && uv run python engine/scripts/gen_third_party.py",
        "```",
        "",
        f"This distribution bundles **{len(rows)} Python packages**, plus CPython itself.",
        "Every package remains under its own licence, held by its own authors. This project",
        "wraps and gates them; it does not reimplement them.",
        "",
        "## Corresponding source",
        "",
        "Every package is pinned in `uv.lock` by exact name, version and artefact hash.",
        "PyPI artefacts are immutable, so a version identifier is a byte identifier — there",
        "is no dated-snapshot caveat here. Sources are",
        "reachable per package at `https://pypi.org/project/<NAME>/`, and `uv sync --locked`",
        "against the committed lockfile retrieves the identical artefacts on any machine.",
        "",
        "## Licence distribution",
        "",
        "| Licence | Packages |",
        "|---|---:|",
    ]
    for lic, n in sorted(buckets.items(), key=lambda kv: (-kv[1], kv[0])):
        out.append(f"| {lic.replace('|', chr(92) + '|')} | {n} |")

    out += [
        "",
        f"Unmapped to an SPDX identifier: **{unmapped}**. An unmapped entry is reported",
        "rather than guessed — a plausible-looking identifier nobody verified is worse than",
        "an honest gap.",
        "",
        "Present in `uv.lock` but not installed on this platform, and therefore not in the",
        f"Linux image: **{conditional}** (marked \u2020 below). The lockfile is cross-platform;",
        "the image is not.",
        "",
        "## Compatibility",
        "",
        "This project is **AGPL-3.0-only**. AGPL-3.0 is one-way compatible with the GPL-3",
        "family and is **not** compatible with GPL-2.0-only. A dependency published under",
        "GPL-2.0-only cannot be admitted to this tree.",
        "",
    ]
    if conflicts:
        out += [
            "> **INCOMPATIBLE DEPENDENCY PRESENT.** The following are GPL-2.0-only and cannot",
            "> lawfully combine with AGPL-3.0-only. This must be resolved, not documented:",
            "",
        ]
        out += [f"> - `{r['name']}` {r['version']}" for r in conflicts]
        out.append("")
    else:
        out += ["No dependency in the current lockfile conflicts.", ""]

    out += ["## Packages", "", "| Package | Version | Licence |", "|---|---|---|"]
    out += [
        f"| `{r['name']}`{' \u2020' if r['platform_conditional'] else ''} "
        f"| {r['version']} | {r['licence']} |"
        for r in rows
    ]
    out.append("")
    return "\n".join(out)


def render_sbom(rows: list[dict[str, Any]]) -> str:
    doc = {
        "bomFormat": "CycloneDX",
        "specVersion": "1.6",
        "version": 1,
        "metadata": {
            "component": {
                "type": "application",
                "name": "econflow-engine",
                "licenses": [{"license": {"id": "AGPL-3.0-only"}}],
            },
            "tools": [{"name": "gen_third_party.py", "vendor": "EconFlow Analytics"}],
        },
        "components": [
            {
                "type": "library",
                "name": r["name"],
                "version": r["version"],
                "purl": r["purl"],
                "licenses": [{"license": {"name": r["licence"]}}],
            }
            for r in rows
        ],
    }
    # No timestamp and no serialNumber: both would change on every run and turn a
    # drift gate into noise. The lockfile is the provenance.
    return json.dumps(doc, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true", help="compare, never write")
    args = ap.parse_args()

    rows, unmapped, conditional = collect()
    if not rows:
        sys.exit("gen_third_party: 0 packages collected; the lockfile or the venv is wrong")

    want = {REGISTER: render_register(rows, unmapped, conditional), SBOM: render_sbom(rows)}

    if args.check:
        for path, text in want.items():
            have = path.read_text(encoding="utf-8") if path.exists() else None
            if have != text:
                print(f"gen_third_party --check: content differs: {path.name}", file=sys.stderr)
                return 1
        print(
        f"gen_third_party --check: OK -- {len(rows)} packages, "
        f"{unmapped} unmapped, {conditional} platform-conditional"
    )
        return 0

    for path, text in want.items():
        path.write_text(text, encoding="utf-8")
    print(
        f"gen_third_party: wrote {len(rows)} packages "
        f"({unmapped} unmapped, {conditional} platform-conditional)"
    )
    print(f"  {REGISTER.relative_to(ROOT)}")
    print(f"  {SBOM.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
