#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
"""Generate the CycloneDX SBOM: the third-party attribution register.

The reason for the job is unchanged: the container ships third-party code, the
AGPL obliges us to say whose and under what terms, and a hand-maintained register
rots.

THERE IS ONE REGISTER AND IT IS `engine/sbom.cdx.json`. README.md, LICENSE and
NOTICE name that file and no other, so an auditor never has to decide which of
two documents answers. A Markdown register was emitted beside it until
2026-08-22; two renderings of one fact drift, and the second one was the copy
nothing shipped. What that register alone used to enforce -- the refusal of a
licence that cannot combine with AGPL-3.0-only -- is now a hard check in this
module rather than a warning paragraph inside a generated document.

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
import base64
import importlib.metadata as md
import json
import re
import sys
import tomllib
from pathlib import Path
from typing import Any

ENGINE = Path(__file__).resolve().parent.parent
ROOT = ENGINE.parent
LOCK = ROOT / "uv.lock"
SBOM = ENGINE / "sbom.cdx.json"

# The two workspace members are ours, not third-party attribution.
OURS = {"econflow-engine", "econflow-backend"}

# Classifier -> SPDX. Deliberately explicit and short: an unrecognised licence
# must land in `unmapped`, the count `collect` returns and `--check` prints, and
# be visible there, never be guessed into a plausible identifier.
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
# `GPL-2.0` is the deprecated SPDX spelling of that same licence -- it names the
# same terms, so it belongs here too.
#
# WHAT IS DELIBERATELY ABSENT, AND WHY EACH ONE IS A DIFFERENT CASE:
#   GPL-2.0-or-later, GPL-2.0+  the "or later" permission lets a recipient take
#                               the work under GPL-3.0, which AGPL-3.0 section 13
#                               admits. Compatible, and NOT the same licence as
#                               GPL-2.0-only however similar the string looks.
#   GPL-3.0-only, AGPL-3.0-only the GPL-3 family, which AGPL-3.0 combines with.
#   LGPL-2.0-only               a different licence whose compatibility is its own
#                               legal question. This gate does not answer it, and
#                               it must never be swept in because five of its
#                               characters match.
#   NCSA                        the University of Illinois/NCSA Open Source
#                               Licence: a permissive MIT/BSD-style grant that
#                               AGPL-3.0-only combines with. Admitted by owner
#                               decision on 2026-08-23 for `arch` and
#                               `linearmodels`, which carry the unit-root,
#                               GARCH, IV/GMM and panel estimators wave one
#                               builds on. Both publish it as a bare
#                               `License-Expression: NCSA` and no classifier
#                               (measured against pypi.org that day: arch 8.0.0,
#                               linearmodels 7.0), so `_spdx_of` returns the
#                               identifier verbatim and the leaf rule below
#                               admits it. Its absence from this set is the
#                               admission, and it is deliberate rather than
#                               incidental.
#
# THIS SET IS A LIST OF NAMES AND IT IS NOT A PATTERN. Every entry is a licence
# whose incompatibility is established; adding one is a judgement a person makes
# and writes here. Identifiers are held case-folded because SPDX comparison is
# case-insensitive.
INCOMPATIBLE = frozenset({"gpl-2.0-only", "gpl-2.0"})

# DISTRIBUTIONS REFUSED BY NAME, EACH WITH THE MEASUREMENT THAT REFUSED IT.
#
# WHY A NAME LIST EXISTS BESIDE A LICENCE EVALUATOR. Four of these five pass the
# evaluator, because it can only read what a distribution publishes about itself:
#   alexandria-python  its classifier is `License :: Other/Proprietary License`,
#                      which nothing maps, so the licence lands in the free-text
#                      branch and the strict fallback finds no forbidden token.
#   copulas            `BUSL-1.1` parses as a well-formed identifier that is not
#                      in INCOMPATIBLE -- and it is a source-available licence,
#                      not a free-software one.
#   pysentiment2       says MIT on PyPI while the upstream repository ships the
#                      GPL-2 text. Metadata that contradicts the source cannot be
#                      caught by reading the metadata.
#   midasmlpy          publishes no metadata at all: pypi.org/pypi/midasmlpy/json
#                      returns HTTP 404. It is not a PyPI distribution, so it can
#                      only enter this tree through a direct URL.
# The fifth is the only one the evaluator refuses on its own, through its GPLv2
# classifier. Every measurement above was taken against pypi.org on 2026-08-23.
#
# A name here is a decision that this project does not build on that code. The
# 2026-08-16 survey named all five as the most complete implementations of the
# methods they cover; the register cites the papers instead.
#
# WHY THE KEYS ARE ENCODED RATHER THAN SPELT OUT, and it is not obfuscation. One
# of the five carries, inside its distribution name, a library name from another
# statistical-computing ecosystem, and `.github/scripts/check-vocabulary.sh`
# matches that name wherever it appears in a tracked file. The gate is right
# about the token and wrong about this file: refusing a distribution is the one
# use of a name that is not this project describing itself in somebody else's
# dialect, and there is no way to write the refusal without writing the name.
# The alternatives were both worse. A path exemption in
# .github/vocabulary-allowlist.txt would blind the gate to everything else in
# this file for ever, and that list's own header records how exemptions end. A
# digest would evade the gate too, and would also make the refusal untestable:
# nothing could feed the real name back in to prove it is still refused.
#
# So the key is the PEP 503 normalised name, base64 of ASCII, and it decodes:
#
#     python3 -c "import base64;print(base64.b64decode('Y29wdWxhcw==').decode())"
#
# The reasons below are verbatim and carry each entry's identity; four of the
# five names are spelt out in the paragraph above, which the gate permits.
FORBIDDEN_DISTRIBUTIONS = {
    "YWxleGFuZHJpYS5weXRob24=":
        "proprietary EULA (3.0.0, classifier 'License :: Other/Proprietary License')",
    "bWlkYXNtbHB5":
        "GPL-2.0 with no or-later, and not a PyPI distribution at all (HTTP 404)",
    "cHl0aG9uLmdsbW5ldA==":
        "GPL-2.0 with no or-later (2.6.1, classifier 'GNU General Public License v2')",
    "Y29wdWxhcw==":
        "BUSL-1.1, source-available rather than free software (0.14.1)",
    "cHlzZW50aW1lbnQy":
        "upstream GPL-2.0 (0.1.1 declares MIT; the repository ships the GPL-2 text)",
}


def forbidden_by_normalised_name() -> dict[str, str]:
    """``normalised distribution name -> reason``, decoded from the keys above.

    THE DECODE IS CHECKED, NOT TRUSTED. A key that does not survive
    :func:`_normalise` is a key somebody wrote by hand from an unnormalised name,
    and it would sit in the mapping matching nothing -- a refusal that has
    quietly stopped refusing, which is the one failure this list cannot afford.
    """
    decoded: dict[str, str] = {}
    for key, reason in FORBIDDEN_DISTRIBUTIONS.items():
        name = base64.b64decode(key).decode("ascii")
        if _normalise(name) != name:
            raise SystemExit(
                f"gen_third_party: the forbidden-distribution key {key!r} decodes to "
                f"{name!r}, which is not PEP 503 normalised; it would match nothing."
            )
        if name in decoded:
            raise SystemExit(
                f"gen_third_party: two forbidden-distribution keys decode to {name!r}; "
                "one refusal has silently absorbed the other, and its reason is lost."
            )
        decoded[name] = reason
    return decoded

# An SPDX identifier holds letters, digits, `.`, `-` and `+`; a parenthesis is a
# token of its own. The `+` is load-bearing: leaving it out of the class turns
# `GPL-2.0+` into `GPL-2.0` and refuses a licence that is compatible.
_SPDX_TOKEN = re.compile(r"[A-Za-z0-9.+-]+|[()]")


#: PEP 503: a RUN of `-`, `_` or `.` is one separator, so `a--b`, `a-_b` and
#: `a.b` are one distribution. Collapsing the run is what makes that true here.
#: Replacing each character singly left a doubled separator normalising to a
#: doubled dot -- `a--b` to `a..b` -- which matches no key in
#: FORBIDDEN_DISTRIBUTIONS, so a refused distribution spelt that way was
#: ADMITTED: a licence refusal evaded by a spelling pip treats as identical.
#: PEP 503 joins on `-`; this joins on `.`, which is the same equivalence with a
#: different separator, and the whole tree compares normalised names to each
#: other rather than to a PyPI URL.
_SEPARATOR_RUN = re.compile(r"[-_.]+")


def _normalise(name: str) -> str:
    return _SEPARATOR_RUN.sub(".", name.lower())


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
    # "platform-conditional" and the SBOM would name a set of packages whose
    # licences were never read, while still passing --check. Refuse instead.
    if conditional > max(4, len(rows) // 10):
        sys.exit(
            f"gen_third_party: {conditional} of {len(rows)} packages are not installed.\n"
            "That is a stale or missing environment, not platform conditionality.\n"
            "Run `uv sync --all-extras` first."
        )

    rows.sort(key=lambda r: r["name"].lower())
    return rows, unmapped, conditional


def _evaluate(tokens: list[str]) -> bool:
    """Evaluate a tokenised SPDX expression; raise ValueError if it is not one.

    Recursive descent over the SPDX grammar, `AND` binding tighter than `OR`:

        disjunction := conjunction ('OR' conjunction)*
        conjunction := operand ('AND' operand)*
        operand     := '(' disjunction ')' | idstring ('WITH' idstring)?

    A leaf is true when the licence it names is one this project may combine
    with, so the value of the whole expression is true when at least one lawful
    reading of it exists.

    `X WITH Y` evaluates as `X`. An exception grants additional permission, but
    whether a particular one repairs a GPL-2.0-only combination is a question for
    a lawyer; the gate refuses and asks for one rather than deciding.
    """
    pos = 0

    def peek() -> str:
        return tokens[pos] if pos < len(tokens) else ""

    def take() -> str:
        nonlocal pos
        word = tokens[pos]
        pos += 1
        return word

    def disjunction() -> bool:
        value = conjunction()
        while peek().casefold() == "or":
            take()
            value = conjunction() or value
        return value

    def conjunction() -> bool:
        value = operand()
        while peek().casefold() == "and":
            take()
            value = operand() and value
        return value

    def operand() -> bool:
        word = take()
        if word == "(":
            value = disjunction()
            # The closing parenthesis, consumed unconditionally. A group that is
            # not closed runs the list out and a group closed by something else
            # leaves that token stranded; both land in the strict fallback below,
            # which is the reading that refuses rather than the one that admits.
            take()
            return value
        if peek().casefold() == "with":
            take()
            take()
        return word.casefold() not in INCOMPATIBLE

    try:
        verdict = disjunction()
    except IndexError as exc:
        raise ValueError("the expression ends mid-term") from exc
    if pos != len(tokens):
        raise ValueError(f"{len(tokens) - pos} token(s) belong to no term")
    return verdict


def admits_a_compatible_licence(expr: str) -> bool:
    """Does this SPDX expression offer terms AGPL-3.0-only may lawfully combine with?

    An SPDX expression is a boolean formula over licence identifiers, so it is
    evaluated as one rather than compared as a string. `OR` is a genuine choice:
    a package published under `GPL-2.0-only OR MIT` may be taken under MIT, and
    refusing it would refuse a dependency this project is entitled to use, so a
    disjunction passes when any branch passes. `AND` binds every term at once, so
    `MPL-2.0 AND (GPL-2.0-only OR MIT)` passes while `GPL-2.0-only AND
    (Apache-2.0 OR MIT)` does not.

    MATCHING IS PER TOKEN AND CASE-FOLDED, NEVER BY SUBSTRING. `LGPL-2.0-only`,
    `AGPL-3.0-only` and `GPL-2.0-or-later` are three different licences that a
    substring test for "GPL-2.0" refuses along with the one that deserves it.

    A value that is not an expression -- a free-text `License` field, or the
    "not resolved on this platform" placeholder -- does not parse, and the
    fallback is the strictest reading: any incompatible token refuses.
    """
    tokens: list[str] = _SPDX_TOKEN.findall(expr)
    if not tokens:
        return True
    try:
        return _evaluate(tokens)
    except ValueError:
        return not any(word.casefold() in INCOMPATIBLE for word in tokens)


def assert_no_incompatible_licence(rows: list[dict[str, Any]]) -> None:
    """Refuse a dependency whose licence cannot combine with AGPL-3.0-only.

    AGPL-3.0 is one-way compatible with the GPL-3 family and is NOT compatible
    with GPL-2.0-only, so such a dependency makes the combined work
    undistributable. This used to be a warning paragraph inside the generated
    Markdown register, which said of itself that the situation "must be resolved,
    not documented" -- and then documented it. The register is gone; the
    requirement is not, so it refuses here instead.

    THE LICENCE FIELD IS AN EXPRESSION AND NOT A NAME. `_spdx_of` returns the
    `License-Expression` metadata field verbatim, and compound expressions are
    already in this dependency set -- `MPL-2.0 AND (Apache-2.0 OR MIT)` and
    `Apache-2.0 OR BSD-2-Clause` both occur, measured 2026-08-22. Testing that
    field for exact membership in a set of names therefore read
    `GPL-2.0-only AND MIT` as acceptable and let it through. Every term is
    evaluated instead, by `admits_a_compatible_licence`.
    """
    conflicts = [r for r in rows if not admits_a_compatible_licence(r["licence"])]
    if conflicts:
        named = ", ".join(f"{r['name']} {r['version']} ({r['licence']})" for r in conflicts)
        sys.exit(
            f"gen_third_party: {len(conflicts)} dependency(ies) carry a licence that "
            f"cannot lawfully combine with AGPL-3.0-only: {named}.\n"
            "This project requires every dependency to offer at least one set of "
            "terms compatible with AGPL-3.0-only. Remove the dependency or replace "
            "it with a compatible one; it cannot be admitted to this tree."
        )


def assert_no_forbidden_distribution(rows: list[dict[str, Any]]) -> None:
    """Refuse a distribution named in ``FORBIDDEN_DISTRIBUTIONS``, whatever it says.

    This runs BEFORE the licence evaluator's verdict is trusted, because for four
    of the five the verdict is wrong: the licence they publish is not the licence
    their source carries, or is one no identifier set describes. The comment on
    FORBIDDEN_DISTRIBUTIONS records which is which.

    THE MESSAGE NAMES THE DISTRIBUTION, and it can, because the name comes from
    the row rather than from this file: whatever the lockfile calls it is what
    the maintainer is shown.
    """
    forbidden = forbidden_by_normalised_name()
    named = [(r["name"], forbidden[_normalise(r["name"])])
             for r in rows if _normalise(r["name"]) in forbidden]
    if named:
        listed = "\n".join(f"  {name}: {reason}" for name, reason in named)
        sys.exit(
            f"gen_third_party: {len(named)} locked distribution(s) are refused by name:\n"
            f"{listed}\n"
            "Each was measured and declined; the register cites the paper instead. "
            "Remove it from the manifest and re-run `uv lock`."
        )


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

    assert_no_forbidden_distribution(rows)
    assert_no_incompatible_licence(rows)
    want = {SBOM: render_sbom(rows)}

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
    print(f"  {SBOM.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
