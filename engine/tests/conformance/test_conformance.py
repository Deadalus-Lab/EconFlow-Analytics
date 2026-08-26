# SPDX-License-Identifier: AGPL-3.0-only
"""Oracle harness: a node's output against an independently established value.

ONE FILE PER CASE, under ``tests/oracle/<package>/<module>/<case>.json``, and
NOT one sealed corpus under ``artifacts/``. Every file in that directory carries
a ``.sha256`` sidecar and the count of those sidecars is asserted by exact
equality, so a corpus living there would make each new case a re-seal across 598
modules. One file per case also gives a diff whose locality matches the category
boxes that write them.

WHAT PARITY DOES NOT COVER, AND THIS DOES. The parity suite proves the engine
AGREES WITH THE CONTRACT ABOUT WHICH CALLS ARE VALID. It says nothing about the
NUMBERS: a wrapper could accept exactly the right inputs and compute something
else entirely. Only a comparison against an independently established value
catches that.

THE CASE SHAPE, and the key set is CLOSED -- an unknown key is an error, because
a misspelt ``tolerence_class`` that is merely ignored turns a reviewed tolerance
into no tolerance at all::

    {
      "fn": "rs_multiple_testing",
      "inputs": {"p_values": [0.01, 0.04], "method": "bh", "alpha": 0.05},
      "expected": {"n_rejected": 4},
      "unchecked_keys": ["p_adjusted", "rejected", "method"],
      "tolerance_class": "exact",
      "citation": "Author (Year), Table 3, row 2, DOI 10.xxxx/yyyy",
      "notes": "what was transcribed, and what the case does not claim"
    }

WHY ``unchecked_keys`` EXISTS, AND WHY IT IS REQUIRED RATHER THAN OPTIONAL.
Published tables give PARTIAL results. Benjamini and Hochberg print fifteen
p-values and the count their procedure rejects; they never print the adjusted
p-values the payload also carries. Without a way to say so in writing, a case had
to publish EVERY field of the payload, and no wrapper-facing case could be
written at all.

The comparison therefore runs in TWO STEPS, and only the second one is relaxed:

1. THE KEY SET, EXACTLY. ``set(expected) | set(unchecked_keys)`` must equal the
   payload's key set. A missing key is red, and so is an extra one.
2. THE VALUES, through ``numerically_equal`` UNCHANGED, over the fields
   ``expected`` names and no others.

SUBSET SEMANTICS WAS REJECTED FOR STEP 1, and this is the reason: a wrong extra
field would pass it. That is a silent false green in the one harness whose whole
purpose is to refuse silent false greens. A field the case has not named appears
in neither set, so step 1 turns the case red -- the hole is closed by
construction, and exactness survives at the key-set level.

``unchecked_keys`` IS REQUIRED, AND ``[]`` IS THE LEGAL WAY TO SAY "EVERYTHING IS
CHECKED". An omitted field would default to permissive, and permissive-by-default
is how this class of gate decays: an exemption that does not name what it exempts
is a hole with no floor under it. Step 1 governs the TOP level of the payload;
nested mappings keep the exact key-set rule ``numerically_equal`` already applies.

TWO NAMESPACES, AND THE DIRECTORY SAYS WHICH. ``<package>`` is the wrapper
package (``c35_resampling_inference``) for a node case, and the reserved word
``engine`` for a case against the engine's own already-written helpers. Wrapper
packages are generated as ``c`` plus two digits, so the two can never collide.
The engine namespace exists for one reason: every wrapper body is a stub today,
so a harness with node cases alone would be green while comparing nothing --
which is the exact failure this file exists to refuse.

FOUR RULES MAKE A CASE PROVE IT IS NOT VACUOUS, and all four are checked when
the case is LOADED rather than when it is run:

1. ``expected`` carries at least one finite number outside {0, 1, -1}. A payload
   of ``{"ok": true}`` proves nothing.
2. ``citation`` carries a locator -- a DOI, an ISBN, or a NUMBERED table, page or
   row -- and names a published source rather than this engine's own output. The
   number is the locator: ``Table 3`` and ``p. 295`` say where to look, and the
   bare words ``table`` and ``page`` say only that one exists somewhere.
3. The tolerance BITES: every numeric leaf is perturbed by ten times the class's
   rtol (or ten times its atol where rtol is zero, or one representable step
   where both are zero) and the comparison must REFUSE the result. A class so
   loose that the perturbation survives is rejected here, which is what makes
   ``_policy.json`` load-bearing rather than a document nobody can fail.
4. Skips are accounted for exactly: ``skipped == n_cases - implemented_cases``.
   The only admissible reason to skip is an unwritten wrapper body.
"""

from __future__ import annotations

import json
import math
import re
from collections.abc import Callable
from dataclasses import dataclass
from functools import cache
from importlib import import_module
from inspect import signature
from pathlib import Path
from typing import Any

import pytest

from econflow_engine.metrics import find_manifest, stub_ledger
from tests.conformance.fixtures import (
    FIXTURE_SIGIL,
    PRODUCE_SIGIL,
    FixtureError,
    build,
    build_fixture,
    fixture,
    moved_builder,
)

ENGINE_ROOT = Path(__file__).resolve().parent.parent.parent
ORACLE = ENGINE_ROOT / "tests" / "oracle"
POLICY_FILE = ORACLE / "_policy.json"
ARTIFACTS = ENGINE_ROOT / "artifacts"
INVENTORY = find_manifest(Path(__file__))

#: The reserved first path segment for cases against the engine's own helpers.
#: A wrapper package is always ``c`` + two digits, so this cannot shadow one.
ENGINE_NAMESPACE = "engine"

#: CLOSED. Every key required, no key beyond these.
CASE_KEYS = frozenset(
    {"fn", "inputs", "expected", "unchecked_keys", "tolerance_class", "citation", "notes"}
)

#: A required argument of one of these kinds cannot be written as a JSON literal:
#: a handle is produced by an earlier node, and a path names an uploaded dataset.
#: The handle kinds themselves are read from the artifact, never copied.
_UNWRITEABLE_KINDS = frozenset({"path"})

#: A citation that describes this engine's own output is not an oracle.
_CITATION_REFUSED = ("computed by", "r printed", "statsmodels returned", "our output")
_DOI = re.compile(r"\b10\.\d{4,9}/\S+")

#: A LOCATOR NAMES A POSITION, SO IT CARRIES THE POSITION. Every alternative below
#: requires the token to be followed by the thing that says WHICH table, page or
#: row -- because the word on its own sends a reader to a work rather than to a
#: place inside it, and a rule that accepts the word alone accepts prose.
#:
#: The first shape of this pattern was ``\b(table|page|row|isbn|p\.|pp\.)`` with a
#: leading word boundary and none trailing, so any word BEGINNING with those
#: letters cleared it. Measured before this change: 'see notes, row by row' and
#: 'arrows and pages of nothing' both passed, and only a citation containing none
#: of the letters at all could fail. RULE 2 exists to refuse a citation nobody can
#: check, and it was refusing almost nothing.
#:
#: The token set is unchanged -- table, page, row, ISBN, p., pp. -- because
#: widening it is a separate decision from making it bite.
#:
#: WHAT COUNTS AS THE POSITION IS WIDER THAN A DIGIT, and requiring a digit was
#: too tight to publish against. The Journal of Finance numbers its tables in
#: roman, appendix tables are letter-labelled, and book front matter is
#: roman-paginated -- so `Table III`, `Table A.1`, `Appendix Table B2`, `p. iv`
#: and `pp. xii-xiv` are all locators a real oracle case will carry.
#:
#: THE LETTER FORM IS CASE-SENSITIVE AND THE TOKENS ARE NOT, which is why the
#: flag is scoped with (?i:...) rather than passed for the whole pattern. A table
#: is labelled with a CAPITAL -- `Table A` -- while "the table a reader can open"
#: is prose, and a blanket re.IGNORECASE cannot tell them apart.
_ROMAN = (
    #: Written out rather than [ivxlcdm]+, which case-insensitively matches "did",
    #: "mid", "lid" and "civil". The trailing (?![MDCLXVI]) is what stops the
    #: nullable parse: every part of a roman numeral is optional, so the empty
    #: match would otherwise succeed at the word start and admit any word at all.
    r"(?=[MDCLXVI])M*(?:C[MD]|D?C{0,3})(?:X[CL]|L?X{0,3})"
    r"(?:I[XV]|V?I{0,3})(?![MDCLXVI])\b"
)
_LOCATOR = re.compile(
    # Table 3 · Table 26.1 · Table A.1 · Table B2 · Table III · pages 12-14 · row 2
    r"\b(?i:tables?|pages?|rows?)\s+(?:\d|[A-Z](?:\.?\d+)?\b|(?i:" + _ROMAN + r"))"
    # p. 295 · p.966 · pp. 12-14 · p. iv · pp. xii-xiv
    r"|\b(?i:pp?)\.\s*(?:\d|(?i:" + _ROMAN + r"))"
    # ISBN: nine digits and then a digit or the X check character, separators
    # allowed between them. The old arm asked only for ten characters drawn from
    # [0-9X-], so `ISBN ----------` was a locator. Ten DIGITS is what is checked
    # now; only a checksum would also refuse `ISBN 0000000000`, and that is a
    # validator rather than a pattern.
    r"|\b(?i:isbn)\b[\s:]*(?:[\s-]*\d){9}[\s-]*[\dXx]"
)

pytestmark = pytest.mark.conformance


def numerically_equal(actual: Any, expected: Any, rtol: float, atol: float) -> bool:
    """Structural comparison with a NUMERIC leaf test.

    ``None`` matches ``None`` and nothing else: a missing value and a computed value
    are different answers, and a tolerance must never blur them.
    """
    if expected is None or actual is None:
        return expected is None and actual is None
    if isinstance(expected, bool) or isinstance(actual, bool):
        return actual is expected
    if isinstance(expected, int | float) and isinstance(actual, int | float):
        if math.isnan(float(expected)) or math.isnan(float(actual)):
            return math.isnan(float(expected)) and math.isnan(float(actual))
        return math.isclose(float(actual), float(expected), rel_tol=rtol, abs_tol=atol)
    if isinstance(expected, str):
        return bool(actual == expected)
    if isinstance(expected, list):
        return (
            isinstance(actual, list)
            and len(actual) == len(expected)
            and all(
                numerically_equal(a, e, rtol, atol)
                for a, e in zip(actual, expected, strict=True)
            )
        )
    if isinstance(expected, dict):
        return (
            isinstance(actual, dict)
            and set(actual) == set(expected)
            and all(numerically_equal(actual[k], expected[k], rtol, atol) for k in expected)
        )
    return bool(actual == expected)


def disagreement(
    payload: Any,
    expected: Any,
    unchecked_keys: tuple[str, ...],
    rtol: float,
    atol: float,
) -> str | None:
    """The two-step comparison. ``None`` when the payload conforms, else the reason.

    STEP 1 IS THE KEY SET AND IT IS EXACT. ``expected`` and ``unchecked_keys``
    together name the WHOLE payload; a missing key and an extra key are equally
    red. Step 2 is ``numerically_equal`` unchanged, over the fields ``expected``
    names -- which is the only place A3 relaxes anything, and only for fields the
    case has named in writing.
    """
    if isinstance(expected, dict):
        if not isinstance(payload, dict):
            return (
                f"the payload is a {type(payload).__name__} and the case names "
                f"fields of a mapping"
            )
        named = set(expected) | set(unchecked_keys)
        missing = sorted(named - set(payload))
        extra = sorted(set(payload) - named)
        if missing or extra:
            return (
                f"the payload's fields are not the ones the case names: "
                f"absent from the payload {missing}, named by neither `expected` nor "
                f"`unchecked_keys` {extra}. The two sets together name the whole "
                f"payload, so an unnamed field is red here rather than ignored."
            )
        payload = {key: payload[key] for key in expected}
    if not numerically_equal(payload, expected, rtol=rtol, atol=atol):
        return (
            f"the value differs from the published one\n"
            f"  expected: {expected!r}\n  actual:   {payload!r}"
        )
    return None


class Inadmissible(Exception):
    """A case file that must not be run: the reason is the message."""


@dataclass(frozen=True, slots=True)
class Case:
    """One admissible case, with its class already resolved to a tolerance."""

    id: str
    fn: str
    module: str
    namespace: str
    inputs: dict[str, Any]
    expected: Any
    unchecked_keys: tuple[str, ...]
    tolerance_class: str
    rtol: float
    atol: float
    #: The datasets this case reaches for, and the producer functions its
    #: ``$produce`` chains name. Both are resolved when the case is LOADED, so a
    #: case naming a dataset that does not exist is refused rather than skipped.
    fixtures: tuple[str, ...] = ()
    produce_chain: tuple[str, ...] = ()


# --------------------------------------------------------------------------- #
# the committed facts a case is checked against
# --------------------------------------------------------------------------- #


def _read(path: Path) -> Any:
    return json.loads(path.read_bytes().decode("utf-8"))


@cache
def _policy() -> dict[str, dict[str, Any]]:
    classes: dict[str, dict[str, Any]] = _read(POLICY_FILE)["classes"]
    return classes


@cache
def _node_specs() -> dict[str, dict[str, Any]]:
    return {n["fn"]: n for n in _read(ARTIFACTS / "node-specs.json")["nodes"]}


@cache
def _stochastic_unseeded() -> frozenset[str]:
    """READ FROM THE ARTIFACT, never copied into the policy.

    A second list would be free to drift from the contract, and the drift would
    be silent -- the copy would keep answering after the vocabulary moved.
    """
    vocabulary = _read(ARTIFACTS / "node-specs.json")["vocabulary"]
    return frozenset(vocabulary["stochastic_unseeded_fns"])


@cache
def _literal_callable_nodes() -> int:
    """How many nodes a case file can call with JSON literals alone.

    THE BLOCKED SET IS READ FROM THE ARTIFACT. ``pointer_handle_kinds`` is the
    contract's own list of kinds satisfied by an edge from an earlier node; a
    second copy here would be free to drift from it, and the drift would be
    silent. ``path`` joins them because it names a dataset somebody uploaded,
    which a file cannot hold either.
    """
    blocked = frozenset(_read(ARTIFACTS / "node-specs.json")["vocabulary"]["pointer_handle_kinds"])
    blocked |= _UNWRITEABLE_KINDS
    return sum(
        1
        for node in _read(ARTIFACTS / "node-specs.json")["nodes"]
        if not any(a["kind"] in blocked for a in node["arguments"] if a["required"])
    )


@cache
def _wrapper_file_of_card() -> dict[int, str]:
    cards = _read(ARTIFACTS / "method-cards.json")["cards"]
    return {int(c["id"]): str(c["wrapper_file"]) for c in cards}


@cache
def _implemented_node_functions() -> frozenset[str]:
    """The wrapper functions whose body is NOT the emitted stub.

    The same walk ``.github/actions/assert-inventory/assert.sh`` runs for
    ``engine.n_implemented``, and it is now literally the same walk:
    ``econflow_engine.metrics.stub_ledger``. The shell copy stays a copy because
    a heredoc cannot import the package, and ``tests/test_stub_definition.py``
    runs it against planted trees and compares its answers with this one's.
    """
    ledger = stub_ledger(ENGINE_ROOT / "src" / "econflow_engine" / "wrappers")
    return frozenset(name for _, name in ledger.implemented)


# --------------------------------------------------------------------------- #
# the four anti-vacuity rules
# --------------------------------------------------------------------------- #


def _numeric_leaves(value: Any) -> list[float]:
    if isinstance(value, bool):
        return []
    if isinstance(value, int | float):
        return [float(value)]
    if isinstance(value, list):
        return [leaf for item in value for leaf in _numeric_leaves(item)]
    if isinstance(value, dict):
        return [leaf for item in value.values() for leaf in _numeric_leaves(item)]
    return []


def _require_a_real_number(expected: Any) -> None:
    for leaf in _numeric_leaves(expected):
        if math.isfinite(leaf) and leaf not in (0.0, 1.0, -1.0):
            return
    raise Inadmissible(
        "RULE 1: `expected` carries no finite number outside {0, 1, -1}. A payload "
        "of flags and placeholders compares nothing, so the case would pass "
        "whatever the body computed."
    )


def _require_a_published_locator(citation: str) -> None:
    lowered = citation.lower()
    for phrase in _CITATION_REFUSED:
        if phrase in lowered:
            raise Inadmissible(
                f"RULE 2: the citation contains '{phrase}'. An oracle value is a "
                "PUBLISHED number; a value this engine produced cannot be the "
                "evidence that this engine is right."
            )
    if not (_DOI.search(citation) or _LOCATOR.search(citation)):
        raise Inadmissible(
            "RULE 2: the citation carries no locator. Name a DOI, an ISBN, or the "
            "NUMBERED table, page or row the number is printed in -- `Table 3`, "
            "`p. 295`, `pp. 12-14`, `row 2`. An author and a year alone cannot be "
            "checked, and neither can the word `table` without the table."
        )


def _require_the_two_sets_to_be_disjoint(expected: Any, unchecked_keys: tuple[str, ...]) -> None:
    """``expected`` and ``unchecked_keys`` may never name the same field.

    They make incompatible claims about it: one says the field is checked against
    a published number, the other says the source publishes nothing to check it
    against. Their union hides which claim won, and either resolution is a lie
    left in the file -- a reader trusting a dead exemption, or a published number
    that silently stopped being compared. It is refused at load time instead.
    """
    if not isinstance(expected, dict):
        if unchecked_keys:
            raise Inadmissible(
                f"`unchecked_keys` names {sorted(unchecked_keys)}, and `expected` is a "
                f"{type(expected).__name__} rather than a mapping. A field name has "
                f"nothing to name here; the only admissible value is []."
            )
        return
    both = sorted(set(expected) & set(unchecked_keys))
    if both:
        raise Inadmissible(
            f"{both} appear(s) in both `expected` and `unchecked_keys`. The two make "
            f"incompatible claims about the same field -- checked against a published "
            f"number, and not published at all -- so naming it twice states nothing."
        )


def _perturb(value: Any, rtol: float, atol: float) -> Any:
    """Move every numeric leaf just past what the class promises to tolerate."""
    if isinstance(value, bool):
        return value
    if isinstance(value, int | float):
        number = float(value)
        if not math.isfinite(number):
            return value
        if rtol > 0.0:
            return number * (1.0 + 10.0 * rtol)
        if atol > 0.0:
            return number + 10.0 * atol
        # `exact`: the smallest representable step must already be refused.
        return math.nextafter(number, math.inf)
    if isinstance(value, list):
        return [_perturb(item, rtol, atol) for item in value]
    if isinstance(value, dict):
        return {k: _perturb(v, rtol, atol) for k, v in value.items()}
    return value


def _require_the_tolerance_to_bite(expected: Any, tolerance_class: str, rtol: float,
                                   atol: float) -> None:
    if numerically_equal(_perturb(expected, rtol, atol), expected, rtol=rtol, atol=atol):
        raise Inadmissible(
            f"RULE 3: '{tolerance_class}' (rtol={rtol}, atol={atol}) accepts a payload "
            "moved ten times its own tolerance. The class is too loose for these "
            "numbers -- near zero the absolute floor swallows the perturbation -- so "
            "the comparison would pass whatever the body computed."
        )


def _require_the_case_to_name_the_declared_payload(
    namespace: str, fn: str, expected: Any, unchecked_keys: tuple[str, ...]
) -> None:
    """RULE 5: where the node DECLARES its payload, the case must name exactly it.

    Until node-specs.json carried ``output_keys`` there was nothing to check a
    case's key set against, so step 1 of the comparison was a claim the case made
    ahead of the body -- it turned red the first time a body ran, which is useful
    but late. Where the node declares its keys, the two sets a case writes down
    can be compared against the contract WHEN THE CASE IS LOADED, before anything
    runs and long before a body exists.

    EXACT EQUALITY, IN BOTH DIRECTIONS, for the same reason step 1 is exact: a
    field named by neither set is a silent hole, and a field named by the case
    that the node does not carry is a stale exemption. ``expected`` and
    ``unchecked_keys`` together claim to name the WHOLE payload, and
    ``output_keys.keys`` is the whole payload -- so if the two disagree, one of
    them is wrong and the file should say which.

    A NODE WHOSE STATUS IS ``undeclared`` IS PASSED OVER, not defaulted. That is
    the debt in ``engine.undeclared_output_keys``; a rule that refused those cases
    would refuse 1314 nodes' worth of oracle work to enforce a field nobody has
    filled in yet.
    """
    if namespace == ENGINE_NAMESPACE:
        return
    record = _node_specs()[fn]["output_keys"]
    if record["status"] != "declared":
        return
    declared = set(record["keys"])
    if not isinstance(expected, dict):
        raise Inadmissible(
            f"RULE 5: node-specs.json declares '{fn}' to return a mapping with the "
            f"fields {sorted(declared)}, and `expected` is a "
            f"{type(expected).__name__}. One of the two is wrong about the payload."
        )
    named = set(expected) | set(unchecked_keys)
    if named != declared:
        raise Inadmissible(
            f"RULE 5: `expected` and `unchecked_keys` together name {sorted(named)}, "
            f"and node-specs.json declares '{fn}' to return {sorted(declared)}. "
            f"Named by the case and not declared: {sorted(named - declared)}; "
            f"declared and named by neither: {sorted(declared - named)}. The two "
            f"sets claim to name the whole payload, so a difference is a "
            f"disagreement about the contract rather than a detail."
        )


# --------------------------------------------------------------------------- #
# the fixture and produce value forms
# --------------------------------------------------------------------------- #


def _sigil(value: Any) -> tuple[str, Any] | None:
    """``{"$fixture": name}`` / ``{"$produce": {...}}`` -> the pair, else ``None``.

    A mapping carrying a sigil BESIDE other keys is an error rather than a
    literal. Reading it as data would silently pass a dict where a series was
    meant, and the case would then be refused by the wire contract for a reason
    that says nothing about the mistake actually made.
    """
    if not isinstance(value, dict):
        return None
    present = sorted(set(value) & {FIXTURE_SIGIL, PRODUCE_SIGIL})
    if not present:
        return None
    if len(present) > 1 or len(value) != 1:
        raise Inadmissible(
            f"{present} appear(s) in a mapping with keys {sorted(value)}. A value "
            f"form is the WHOLE value: exactly one sigil and no other key."
        )
    return present[0], value[present[0]]


def _refuse_a_buried_sigil(value: Any, where: str, top: bool = True) -> None:
    """A sigil below the top level of an argument's value is refused, not ignored.

    Only the value of an argument is a value form. A ``$fixture`` inside a list or
    a nested mapping would be passed through as data, and the case would read as
    though it reached for a dataset while quietly handing the node a dictionary.
    """
    if isinstance(value, dict):
        if not top and set(value) & {FIXTURE_SIGIL, PRODUCE_SIGIL}:
            raise Inadmissible(
                f"argument '{where}' buries a value form inside its value. A "
                f"{FIXTURE_SIGIL} is the whole value of an argument or it is data."
            )
        for item in value.values():
            _refuse_a_buried_sigil(item, where, top=False)
    elif isinstance(value, list):
        for item in value:
            _refuse_a_buried_sigil(item, where, top=False)


def _scan_inputs(inputs: dict[str, Any], depth: int = 0) -> tuple[list[str], list[str]]:
    """Resolve every value form at LOAD time. Returns (dataset names, producer fns).

    THE CHAIN IS CAPPED AT DEPTH 1, deliberately and not as an oversight. A
    producer's own inputs must be literals or ``$fixture`` and never ``$produce``.
    A deeper chain is a graph, and a graph in a case file is a second execution
    engine written inside the harness that exists to check the first one. Raising
    the cap is a later reviewed diff, and this refuses it in the meantime with a
    message that says so.
    """
    from econflow_engine.loader import MANIFEST

    datasets: list[str] = []
    chain: list[str] = []
    for name, value in inputs.items():
        found = _sigil(value)
        if found is None:
            # ONLY A VALUE THAT IS NOT ITSELF A VALUE FORM IS WALKED. A `$produce`
            # payload carries its own `inputs` mapping, whose values are top-level
            # value forms in their own right; walking into it would report every
            # legitimate inner `$fixture` as a buried one, and the depth cap below
            # -- the rule that actually governs a chain -- would never be reached.
            _refuse_a_buried_sigil(value, name)
            continue
        kind, payload = found
        if kind == FIXTURE_SIGIL:
            if not isinstance(payload, str):
                raise Inadmissible(
                    f"argument '{name}': {FIXTURE_SIGIL} names a dataset file stem "
                    f"as a string, and carries a {type(payload).__name__}."
                )
            try:
                fixture(payload)
            except FixtureError as refusal:
                raise Inadmissible(f"argument '{name}': {refusal}") from refusal
            datasets.append(payload)
            continue
        if depth >= 1:
            raise Inadmissible(
                f"argument '{name}': a {PRODUCE_SIGIL} chain is capped at depth 1, "
                f"so a producer's own inputs are literals or {FIXTURE_SIGIL} and "
                f"never another {PRODUCE_SIGIL}."
            )
        if not isinstance(payload, dict) or set(payload) != {"fn", "inputs"}:
            raise Inadmissible(
                f"argument '{name}': {PRODUCE_SIGIL} takes exactly `fn` and "
                f"`inputs`; this one carries "
                f"{sorted(payload) if isinstance(payload, dict) else type(payload).__name__}."
            )
        producer = str(payload["fn"])
        if producer not in MANIFEST:
            raise Inadmissible(
                f"argument '{name}': {PRODUCE_SIGIL} names '{producer}', which is "
                f"not one of the {len(MANIFEST)} nodes in the manifest."
            )
        if not isinstance(payload["inputs"], dict):
            raise Inadmissible(f"argument '{name}': a producer's `inputs` is a mapping.")
        chain.append(producer)
        inner_datasets, inner_chain = _scan_inputs(payload["inputs"], depth + 1)
        datasets.extend(inner_datasets)
        chain.extend(inner_chain)
    return datasets, chain


# --------------------------------------------------------------------------- #
# loading
# --------------------------------------------------------------------------- #


def _resolve_target(namespace: str, module: str, fn: str) -> None:
    """Refuse a case that names nothing real, or files it under the wrong module."""
    if namespace == ENGINE_NAMESPACE:
        try:
            engine_module = import_module(f"econflow_engine.{module}")
        except ModuleNotFoundError as exc:
            raise Inadmissible(f"no engine module 'econflow_engine.{module}' ({exc}).") from exc
        if fn not in getattr(engine_module, "__all__", ()):
            raise Inadmissible(
                f"'{fn}' is not exported by econflow_engine.{module}. A case in the "
                f"'{ENGINE_NAMESPACE}' namespace names a PUBLIC helper of that module."
            )
        return

    from econflow_engine.loader import MANIFEST
    from econflow_engine.naming import category_package, wrapper_module_name

    entry = MANIFEST.get(fn)
    if entry is None:
        raise Inadmissible(
            f"'{fn}' is not one of the {len(MANIFEST)} nodes in the manifest."
        )
    package = category_package(str(entry["category"]))
    owning = wrapper_module_name(_wrapper_file_of_card()[int(entry["card_id"])])
    if (namespace, module) != (package, owning):
        raise Inadmissible(
            f"'{fn}' belongs to {package}/{owning}, and the case is filed under "
            f"{namespace}/{module}. The directory names the module the case covers."
        )


def _check_seed_rules(namespace: str, fn: str, inputs: dict[str, Any],
                      tolerance_class: str) -> None:
    if tolerance_class == "simulation-seeded":
        if namespace == ENGINE_NAMESPACE:
            raise Inadmissible(
                "'simulation-seeded' names a NODE's declared seed argument, and an "
                f"engine helper declares none. Use a class from {sorted(_policy())}."
            )
        if "seed" not in inputs:
            raise Inadmissible(
                "'simulation-seeded' promises a draw reproducible to the bit, and "
                "the inputs carry no `seed`."
            )
        declared = {a["name"] for a in _node_specs()[fn]["arguments"]}
        if "seed" not in declared:
            raise Inadmissible(
                f"'simulation-seeded' requires a `seed` argument, and node-specs.json "
                f"declares none for '{fn}'."
            )
    elif fn in _stochastic_unseeded():
        raise Inadmissible(
            f"'{fn}' is in node-specs.json vocabulary.stochastic_unseeded_fns, so it "
            f"draws unseeded and cannot reproduce a fixed payload. Its only "
            f"admissible class is 'simulation-seeded', with a seed in the inputs."
        )


def _load_case(path: Path) -> Case:
    relative = path.relative_to(ORACLE)
    if len(relative.parts) != 3:
        raise Inadmissible(
            f"a case lives at <package>/<module>/<case>.json; '{relative.as_posix()}' "
            f"has {len(relative.parts)} path segment(s)."
        )
    namespace, module, _ = relative.parts

    raw = _read(path)
    if not isinstance(raw, dict):
        raise Inadmissible(f"the case file holds a {type(raw).__name__}, not an object.")
    unknown = sorted(set(raw) - CASE_KEYS)
    missing = sorted(CASE_KEYS - set(raw))
    if unknown:
        raise Inadmissible(
            f"unknown key(s) {unknown}. The key set is CLOSED: a misspelt key that is "
            "merely ignored turns a reviewed tolerance into no tolerance at all."
        )
    if missing:
        raise Inadmissible(
            f"missing key(s) {missing}. Every key of the shape is REQUIRED and none "
            "of them has a default, because each default would be a decision nobody "
            "made: a default tolerance is a number nobody chose, and an omitted "
            "`unchecked_keys` is an exemption that names nothing it exempts."
        )

    tolerance_class = str(raw["tolerance_class"])
    if tolerance_class not in _policy():
        raise Inadmissible(
            f"'{tolerance_class}' is not a class in tests/oracle/_policy.json "
            f"({sorted(_policy())})."
        )
    rtol = float(_policy()[tolerance_class]["rtol"])
    atol = float(_policy()[tolerance_class]["atol"])

    declared = raw["unchecked_keys"]
    if not isinstance(declared, list) or not all(isinstance(k, str) for k in declared):
        raise Inadmissible(
            "`unchecked_keys` is a list of payload field names; [] is the legal way to "
            "say that the case checks every field."
        )
    unchecked_keys = tuple(declared)
    if len(set(unchecked_keys)) != len(unchecked_keys):
        raise Inadmissible(f"`unchecked_keys` names a field twice: {sorted(unchecked_keys)}.")

    fn = str(raw["fn"])
    inputs = dict(raw["inputs"])
    _resolve_target(namespace, module, fn)
    _check_seed_rules(namespace, fn, inputs, tolerance_class)
    _require_the_two_sets_to_be_disjoint(raw["expected"], unchecked_keys)
    _require_a_real_number(raw["expected"])
    _require_a_published_locator(str(raw["citation"]))
    _require_the_tolerance_to_bite(raw["expected"], tolerance_class, rtol, atol)
    _require_the_case_to_name_the_declared_payload(
        namespace, fn, raw["expected"], unchecked_keys
    )
    datasets, chain = _scan_inputs(inputs)

    return Case(
        id=relative.as_posix().removesuffix(".json"),
        fn=fn,
        module=module,
        namespace=namespace,
        inputs=inputs,
        expected=raw["expected"],
        unchecked_keys=unchecked_keys,
        tolerance_class=tolerance_class,
        rtol=rtol,
        atol=atol,
        fixtures=tuple(datasets),
        produce_chain=tuple(chain),
    )


def _case_files() -> list[Path]:
    return sorted(p for p in ORACLE.rglob("*.json") if not p.name.startswith("_"))


def _load_all() -> list[tuple[Path, Case | Inadmissible]]:
    loaded: list[tuple[Path, Case | Inadmissible]] = []
    for path in _case_files():
        try:
            loaded.append((path, _load_case(path)))
        except Inadmissible as refusal:
            loaded.append((path, refusal))
        except Exception as exc:  # a malformed file is a refusal, not a crashed session
            loaded.append((path, Inadmissible(f"{type(exc).__name__}: {exc}")))
    return loaded


#: Collected at import time so the parameter ids are the case paths.
_LOADED = _load_all()
_ADMISSIBLE = [case for _, case in _LOADED if isinstance(case, Case)]


#: The builder a case's ``$fixture`` forms go through. A parameter rather than a
#: hard call, so the perturbation control below can hand in a moved dataset and
#: re-run the SAME code path -- not a copy of it that could drift.
Builder = Callable[[str], Any]


def _materialise(
    case: Case, builder: Builder, opened: list[str]
) -> tuple[str, Any]:
    """Turn a case's ``inputs`` into the call the engine actually receives.

    DELIVERY GOES THROUGH THE PRODUCTION DOOR, and that is the whole design. In
    the wrapper namespace the object is put in the REAL session registry and the
    returned handle is substituted into ``inputs``; ``run_method`` is then called
    unchanged, so ``validate_wire`` sees a handle string of the shape the contract
    validates, ``adapt_args`` resolves it, and ``_AS_KIND`` converts it. A fixture
    injected past those three would prove that the harness can build a frame, and
    nothing whatever about the path a caller uses.

    IN THE ENGINE NAMESPACE THE OBJECT IS SUBSTITUTED DIRECTLY. An engine helper
    takes Python objects and knows nothing about handles; wrapping one in a handle
    there would be a ceremony with no reader.

    Returns ``("ok", inputs)``, or a state a case cannot run in: ``not-implemented``
    when a producer's body is unwritten, ``refused`` when a producer was refused.
    """
    from econflow_engine.mcp.registry import registry_put

    prepared: dict[str, Any] = {}
    for name, value in case.inputs.items():
        found = _sigil(value)
        if found is None:
            prepared[name] = value
            continue
        kind, payload = found
        if kind == FIXTURE_SIGIL:
            obj = builder(str(payload))
            if case.namespace == ENGINE_NAMESPACE:
                prepared[name] = obj
            else:
                handle = registry_put(obj, meta={"fixture": payload})
                opened.append(handle)
                prepared[name] = handle
            continue
        state, produced = _run_producer(payload, builder, opened)
        if state != "ok":
            return state, produced
        prepared[name] = produced
    return "ok", prepared


def _run_producer(
    spec: dict[str, Any], builder: Builder, opened: list[str]
) -> tuple[str, Any]:
    """Run one depth-1 producer through the real gateway and hand on its result.

    A PRODUCER IS A REAL NODE, RUN THE REAL WAY. Its result reaches the case as
    the handle the gateway registered where the node registers one, and as the
    payload where it does not -- which is exactly what a caller chaining two nodes
    receives. Every wrapper body is a stub today, so every chain case reports
    ``not-implemented`` and skips, and that is the correct outcome rather than a
    gap: the producer lands in 2.2, and the case turns green with it.
    """
    from econflow_engine.mcp.gateway import run_method
    from econflow_engine.mcp.registry import registry_put

    inner: dict[str, Any] = {}
    for name, value in dict(spec["inputs"]).items():
        found = _sigil(value)
        if found is None:
            inner[name] = value
            continue
        obj = builder(str(found[1]))
        handle = registry_put(obj, meta={"fixture": found[1]})
        opened.append(handle)
        inner[name] = handle
    response = run_method(str(spec["fn"]), inner)
    if response.handle is not None:
        opened.append(response.handle)
    if response.state != "succeeded":
        return response.state, f"producer {spec['fn']}: {response.message}"
    return "ok", response.handle if response.handle is not None else response.payload


def _run_case(case: Case, builder: Builder) -> tuple[str, Any]:
    """One case, start to finish, with every handle it opened closed again.

    THE HANDLES THIS CASE OPENED ARE DROPPED INDIVIDUALLY, not by clearing the
    store. ``MAX_ENTRIES`` is 512 with oldest-first eviction, so a corpus that
    left its fixtures behind would silently evict a handle a later case still
    holds -- the bound has to be respected. Clearing the WHOLE registry would
    respect it too, and would also delete handles belonging to whichever sibling
    suite happens to share the process; ``registry_clear(handle)`` per handle
    achieves the bound without reaching outside this case.
    """
    from econflow_engine.mcp.gateway import run_method
    from econflow_engine.mcp.registry import registry_clear

    opened: list[str] = []
    try:
        state, prepared = _materialise(case, builder, opened)
        if state != "ok":
            return state, prepared
        if case.namespace == ENGINE_NAMESPACE:
            helper = getattr(import_module(f"econflow_engine.{case.module}"), case.fn)
            # BOUND THROUGH THE SIGNATURE, not splatted as keywords. A case names its
            # inputs, and `to_mcp` is a singledispatch generic that dispatches on
            # args[0] and refuses a keyword-only call; binding turns the named
            # mapping into the call the function actually accepts.
            try:
                bound = signature(helper).bind(**prepared)
                return "succeeded", helper(*bound.args, **bound.kwargs)
            except Exception as exc:
                return "raised", f"{type(exc).__name__}: {exc}"
        response = run_method(case.fn, prepared)
        if response.handle is not None:
            opened.append(response.handle)
        return (
            response.state,
            response.payload if response.state == "succeeded" else response.message,
        )
    finally:
        for handle in opened:
            registry_clear(handle)


@cache
def _outcomes() -> dict[str, tuple[str, Any]]:
    """Run every admissible case ONCE. ``(state, payload-or-message)`` per case.

    Cached and shared rather than run inside each parametrised test, so that the
    accounting test below sees the same outcomes the per-case tests do whatever
    order ``pytest-randomly`` chooses.
    """
    return {case.id: _run_case(case, build_fixture) for case in _ADMISSIBLE}


# --------------------------------------------------------------------------- #
# the tests
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize(
    "path",
    [path for path, _ in _LOADED],
    ids=[path.relative_to(ORACLE).as_posix() for path, _ in _LOADED],
)
def test_the_case_file_is_admissible(path: Path) -> None:
    """Every rule a case must satisfy BEFORE it is allowed to compare anything."""
    outcome = dict(_LOADED)[path]
    if isinstance(outcome, Inadmissible):
        pytest.fail(f"{path.relative_to(ORACLE).as_posix()}: {outcome}")


@pytest.mark.parametrize("case", _ADMISSIBLE, ids=[c.id for c in _ADMISSIBLE])
def test_the_node_reproduces_the_oracle(case: Case) -> None:
    state, payload = _outcomes()[case.id]
    if state == "not-implemented":
        pytest.skip(f"{case.fn}: the wrapper body is not implemented yet")
    assert state == "succeeded", f"{case.id}: {state} -- {payload}"
    reason = disagreement(payload, case.expected, case.unchecked_keys, case.rtol, case.atol)
    assert reason is None, f"{case.id}: {reason} (tolerance class '{case.tolerance_class}')"


def test_the_harness_compares_something_today() -> None:
    """THE ANTI-VACUITY GATE, and the reason this file is not green over nothing.

    Every wrapper body is a stub, so a corpus of node cases alone would skip in
    full and report success while comparing nothing -- the failure this
    repository has hit before. The floor counts cases that RAN, and it lives in
    .github/inventory.json where lowering it is a reviewed one-line diff.
    """
    floor = int(_read(INVENTORY)["suite"]["min_oracle_cases"])
    ran = [c for c in _ADMISSIBLE if _outcomes()[c.id][0] == "succeeded"]
    assert _LOADED, f"no case files under {ORACLE}; the harness examined nothing"
    assert len(ran) >= floor, (
        f"{len(ran)} oracle case(s) ran against implemented code, below the floor "
        f"{floor} in .github/inventory.json. A harness whose every case skips is "
        f"green while comparing nothing."
    )


def test_the_key_set_step_refuses_an_extra_field() -> None:
    """A field named in NEITHER set is red, and that is what closes the subset hole.

    Subset semantics -- compare the fields ``expected`` names and ignore the rest --
    would accept this payload, because every named field matches. The wrong extra
    field would ship silently, in the one harness whose purpose is to refuse a
    silent pass.
    """
    reason = disagreement(
        {"n_rejected": 4, "p_adjusted": [0.1], "surprise": 7.0},
        {"n_rejected": 4},
        ("p_adjusted",),
        rtol=0.0,
        atol=0.0,
    )
    assert reason is not None
    assert "surprise" in reason


def test_the_key_set_step_refuses_a_missing_field() -> None:
    """A key ``expected`` names and the payload does not carry is red at step 1."""
    reason = disagreement(
        {"p_adjusted": [0.1]},
        {"n_rejected": 4},
        ("p_adjusted",),
        rtol=0.0,
        atol=0.0,
    )
    assert reason is not None
    assert "n_rejected" in reason


def test_the_key_set_step_refuses_an_unchecked_key_the_payload_does_not_carry() -> None:
    """``unchecked_keys`` names fields of THIS payload, not a wish list.

    A name that matches nothing is a stale exemption -- the shape it excused has
    moved -- so the union stops equalling the payload and the case turns red.
    """
    reason = disagreement(
        {"n_rejected": 4},
        {"n_rejected": 4},
        ("p_adjusted",),
        rtol=0.0,
        atol=0.0,
    )
    assert reason is not None
    assert "p_adjusted" in reason


def test_an_unchecked_field_may_carry_any_value() -> None:
    """THE RELAXATION, and it is on VALUES ONLY. The key set was already exact."""
    assert (
        disagreement(
            {"n_rejected": 4, "p_adjusted": [0.9, 0.9]},
            {"n_rejected": 4},
            ("p_adjusted",),
            rtol=0.0,
            atol=0.0,
        )
        is None
    )


def test_a_named_field_is_still_compared_against_its_published_number() -> None:
    """``numerically_equal`` runs unchanged over the fields ``expected`` names."""
    reason = disagreement(
        {"n_rejected": 3, "p_adjusted": [0.9]},
        {"n_rejected": 4},
        ("p_adjusted",),
        rtol=0.0,
        atol=0.0,
    )
    assert reason is not None
    assert "n_rejected" in reason


def test_a_field_named_in_both_sets_is_inadmissible() -> None:
    """The two sets make INCOMPATIBLE claims about the same field.

    ``expected`` says the field is checked against a published number;
    ``unchecked_keys`` says the source publishes nothing to check it against. A
    union hides which claim won, and either resolution is a lie in the file: the
    reader trusts a dead exemption, or a published number silently stops being
    compared. So it is refused when the case is loaded.
    """
    with pytest.raises(Inadmissible, match="both"):
        _require_the_two_sets_to_be_disjoint({"n_rejected": 4}, ("n_rejected",))


def test_unchecked_keys_are_inadmissible_where_expected_is_not_a_mapping() -> None:
    """A field name has nothing to name when the payload is a list or a scalar."""
    with pytest.raises(Inadmissible, match="mapping"):
        _require_the_two_sets_to_be_disjoint([1.0, 2.0], ("p_adjusted",))


def test_the_literal_callable_surface_is_the_measured_one() -> None:
    """HOW FAR A CASE FILE CAN REACH TODAY, and it is a MEASUREMENT, not a comment.

    A case names its inputs as JSON literals, so it can call a node only when no
    REQUIRED argument of that node needs something a file cannot hold: a handle
    produced by an earlier node, or the ticket name of an uploaded dataset. The
    blocked set is READ FROM node-specs.json rather than typed out here, because
    a second copy of the contract's own vocabulary would be free to drift from
    it, and the drift would be silent.

    Every other node needs a fixture before an oracle case can reach it, and that
    is a different box. This constant is what makes the gap countable.
    """
    declared = int(_read(INVENTORY)["oracle"]["literal_callable_nodes"])
    assert _literal_callable_nodes() == declared, (
        f"{_literal_callable_nodes()} node(s) can be called from JSON literals, and "
        f"oracle.literal_callable_nodes in .github/inventory.json says {declared}. "
        f"Re-run the command in the 'commands' block before moving the number."
    )


def test_every_skip_is_an_unwritten_body() -> None:
    """``skipped == n_cases - implemented_cases``, and no other skip is admissible.

    WIDENED FOR THE CHAIN FORM. A case used to count as implemented on ``case.fn``
    alone. A ``$produce`` chain runs a PRODUCER first, so a case whose own body is
    written but whose producer is a stub skips -- and the old accounting would
    have called that an inadmissible skip and turned red on a case behaving
    exactly as designed. Implemented now means ``case.fn`` AND every function in
    its chain, which is the set of bodies the case actually needs.
    """
    implemented = _implemented_node_functions()
    declared = int(_read(INVENTORY)["engine"]["n_implemented"])
    assert len(implemented) == declared, (
        f"{len(implemented)} wrapper function(s) carry a body, and "
        f"engine.n_implemented in .github/inventory.json says {declared}"
    )
    implemented_cases = [
        c
        for c in _ADMISSIBLE
        if (c.namespace == ENGINE_NAMESPACE or c.fn in implemented)
        and all(producer in implemented for producer in c.produce_chain)
    ]
    skipped = [c for c in _ADMISSIBLE if _outcomes()[c.id][0] == "not-implemented"]
    assert len(skipped) == len(_ADMISSIBLE) - len(implemented_cases), (
        f"{len(skipped)} case(s) skipped, {len(_ADMISSIBLE) - len(implemented_cases)} "
        f"expected. A case skips because its body is unwritten and for no other "
        f"reason: skipped={sorted(c.id for c in skipped)}"
    )


# --------------------------------------------------------------------------- #
# the fixture form
# --------------------------------------------------------------------------- #


def _cases_that_ran_on_a_fixture() -> list[Case]:
    return [
        case
        for case in _ADMISSIBLE
        if case.fixtures and _outcomes()[case.id][0] == "succeeded"
    ]


def test_the_harness_reaches_past_the_literal_surface_today() -> None:
    """THE ANTI-VACUITY FLOOR FOR THE FIXTURE FORM, and it is NOT zero.

    Every wrapper body is a stub, so every wrapper-namespace fixture case reports
    ``not-implemented`` and skips. A floor of zero over that corpus would be
    satisfied by a fixture form that had never once built an object, which is the
    same shape of failure as a harness whose every case skips.

    THE ENGINE NAMESPACE IS WHAT CLOSES IT. An engine-namespace fixture
    materialises to the object itself and the helper it feeds is already written,
    so at least one case builds a dataset and compares a real result on the day
    this form lands. The floor lives in .github/inventory.json where lowering it
    is a reviewed one-line diff.
    """
    floor = int(_read(INVENTORY)["suite"]["min_fixture_cases"])
    ran = _cases_that_ran_on_a_fixture()
    assert floor > 0, (
        "suite.min_fixture_cases is zero, which every corpus satisfies, including "
        "one in which no dataset was ever built"
    )
    assert len(ran) >= floor, (
        f"{len(ran)} case(s) built a dataset and ran against implemented code, "
        f"below the floor {floor} in .github/inventory.json."
    )


def test_a_case_that_ran_moves_when_its_fixture_moves() -> None:
    """THE PROOF THAT THE DATA REACHED THE BODY, and there is no other.

    A case can be green for two reasons: the body computed the published number
    from the dataset, or the body ignored the dataset and returned something that
    happens to match. Nothing about a passing run separates the two. So every case
    that ran is RE-RUN with every numeric leaf of its dataset moved past what its
    own tolerance class promises to tolerate, and the comparison must now REFUSE
    the result. If the payload does not move when the data moves, the fixture
    never reached the body.

    The sibling of ``_require_the_tolerance_to_bite``, which asks the same
    question of ``expected``: is this comparison capable of failing at all?
    """
    ran = _cases_that_ran_on_a_fixture()
    assert ran, (
        "no case built a dataset and ran, so this control examined nothing. It is "
        "the only evidence that a fixture reaches the body rather than sitting "
        "beside it."
    )
    for case in ran:
        state, payload = _run_case(case, moved_builder(case.rtol, case.atol))
        assert state == "succeeded", (
            f"{case.id}: the moved dataset did not run ({state} -- {payload}). The "
            f"control moves values, never shapes, so a refusal here is a defect in "
            f"the move rather than a verdict on the case."
        )
        reason = disagreement(
            payload, case.expected, case.unchecked_keys, case.rtol, case.atol
        )
        assert reason is not None, (
            f"{case.id}: every numeric leaf of {list(case.fixtures)} was moved past "
            f"the '{case.tolerance_class}' tolerance and the payload still matches "
            f"the published value. The body is not reading the dataset."
        )


def test_a_wrapper_fixture_case_is_refused_by_nothing_before_its_stub() -> None:
    """THE 894 ARE REACHABLE TODAY, AND THIS IS THE MEASUREMENT RATHER THAN A HOPE.

    ``make_tool`` runs ``validate_wire`` and then ``adapt_args`` BEFORE it calls
    the body, so a wrapper-namespace fixture case exercises the whole delivery
    path -- handle shape, ``resolve_handle``, ``_AS_KIND`` -- and only then meets
    the stub. A handle the contract will not accept therefore surfaces as
    ``refused`` and never as ``not-implemented``, which makes the distinction
    between those two states the evidence that the path works.

    So a wrapper fixture case must report ``not-implemented`` while bodies are
    stubs. A ``refused`` means the dataset does not fit the argument it was
    written for, and that is a defect in the case rather than a body that is
    merely outstanding.
    """
    from econflow_engine.mcp.registry import registry_list

    wrapper_cases = [
        c for c in _ADMISSIBLE if c.namespace != ENGINE_NAMESPACE and c.fixtures
    ]
    for case in wrapper_cases:
        state, message = _outcomes()[case.id]
        assert state in {"succeeded", "not-implemented"}, (
            f"{case.id}: {state} -- {message}. The dataset reached the wire "
            f"contract and was turned away before the body was ever called."
        )
    assert not any(
        entry.get("meta", {}).get("fixture") for entry in registry_list().values()
    ), "a fixture handle outlived the case that opened it; the store is bounded"


def test_the_reach_of_a_fixture_is_the_measured_one() -> None:
    """HOW FAR THE FORM GOES, counted off the contract and printed in one place.

    Four disjoint tiers over the 1456 nodes, and the numbers are read from
    node-specs.json rather than written here twice. The 19 ``path`` nodes are NOT
    reachable under this design and are named rather than rounded away: a path is
    the ticket of a dataset somebody uploaded, and no file in this tree can hold
    one. The 440 raw-handle nodes split into handles holding plain data, which a
    dataset reaches, and handles holding a fitted object, which need a producer --
    a split the contract does not record, so it is deliberately NOT asserted here.
    """
    specs = _read(ARTIFACTS / "node-specs.json")
    pointer = frozenset(specs["vocabulary"]["pointer_handle_kinds"])
    data_handles = frozenset(
        {
            "series_handle",
            "irregular_series_handle",
            "multiseries_handle",
            "df_handle",
            "matrix_handle",
            "exog_handle",
        }
    )
    tiers = {"literal": 0, "data-handle": 0, "raw-handle": 0, "path": 0}
    for node in specs["nodes"]:
        kinds = {a["kind"] for a in node["arguments"] if a["required"]}
        if "path" in kinds:
            tiers["path"] += 1
        elif kinds & (pointer - data_handles):
            tiers["raw-handle"] += 1
        elif kinds & data_handles:
            tiers["data-handle"] += 1
        else:
            tiers["literal"] += 1
    assert tiers["literal"] == _literal_callable_nodes()
    assert tiers == {"literal": 103, "data-handle": 894, "raw-handle": 440, "path": 19}
    assert sum(tiers.values()) == len(specs["nodes"]) == 1456


def test_a_case_naming_a_field_the_node_does_not_declare_is_inadmissible() -> None:
    """RULE 5's POSITIVE CONTROL, and it is observable on a COMMITTED case.

    The Benjamini-Hochberg case names exactly the four fields node-specs.json
    declares for ``rs_multiple_testing``. Rename one of them and the case must
    turn Inadmissible -- not skip, not pass, and not wait for a body.
    """
    declared = _node_specs()["rs_multiple_testing"]["output_keys"]
    assert declared["status"] == "declared"
    assert set(declared["keys"]) == {"p_adjusted", "rejected", "n_rejected", "method"}
    with pytest.raises(Inadmissible, match="RULE 5"):
        _require_the_case_to_name_the_declared_payload(
            "c35_resampling_inference",
            "rs_multiple_testing",
            {"n_rejected": 4},
            ("p_adjusted", "rejected", "procedure"),
        )


def test_a_case_matching_the_declared_payload_is_admitted() -> None:
    """RULE 5's NEGATIVE CONTROL. The rule must admit the set that is correct."""
    _require_the_case_to_name_the_declared_payload(
        "c35_resampling_inference",
        "rs_multiple_testing",
        {"n_rejected": 4},
        ("p_adjusted", "rejected", "method"),
    )


def test_rule_five_passes_over_a_node_that_declares_nothing() -> None:
    """The debt is not a licence and not a refusal: an undeclared node is skipped."""
    undeclared = next(
        fn for fn, node in _node_specs().items()
        if node["output_keys"]["status"] == "undeclared"
    )
    _require_the_case_to_name_the_declared_payload(
        "c00_data_utilities", undeclared, {"anything": 2.5}, ()
    )


def test_a_value_form_beside_another_key_is_refused() -> None:
    """A sigil is the WHOLE value of an argument, or the mapping is data."""
    with pytest.raises(Inadmissible, match="WHOLE value"):
        _sigil({FIXTURE_SIGIL: "anscombe_1973_data_set_i", "freq": "Q"})


def test_a_value_form_buried_inside_a_value_is_refused() -> None:
    """Reading it as data would let a case LOOK as though it reached for a dataset."""
    with pytest.raises(Inadmissible, match="buries a value form"):
        _refuse_a_buried_sigil({"outer": {FIXTURE_SIGIL: "whatever"}}, "data")


def test_a_case_naming_a_dataset_that_does_not_exist_is_refused_at_load() -> None:
    """Refused when the case is LOADED, so it cannot masquerade as a skip."""
    with pytest.raises(Inadmissible, match="no dataset"):
        _scan_inputs({"data": {FIXTURE_SIGIL: "a_table_nobody_transcribed"}})


def test_a_produce_chain_deeper_than_one_is_refused() -> None:
    """The cap is deliberate: a deeper chain is a graph, and a graph in a case file
    is a second execution engine written inside the harness that checks the first."""
    with pytest.raises(Inadmissible, match="capped at depth 1"):
        _scan_inputs(
            {
                "fit": {
                    PRODUCE_SIGIL: {
                        "fn": "rs_multiple_testing",
                        "inputs": {
                            "inner": {
                                PRODUCE_SIGIL: {"fn": "rs_multiple_testing", "inputs": {}}
                            }
                        },
                    }
                }
            }
        )


def test_a_produce_chain_naming_no_real_node_is_refused() -> None:
    with pytest.raises(Inadmissible, match="not one of"):
        _scan_inputs(
            {"fit": {PRODUCE_SIGIL: {"fn": "no_such_node_exists", "inputs": {}}}}
        )


#: WHAT RULE 2 MUST REFUSE, and every one of these PASSED until this pair of
#: controls was written. The old pattern anchored on the left only, so a word
#: merely BEGINNING with the letters cleared it and the rule admitted prose.
_NO_LOCATOR = (
    "Smith (2020), see notes, row by row",
    "Jones (1999) -- arrows and pages of nothing",
    "Brown (2011), tabled at the meeting, paged through by hand",
    "Anonymous, no locator at all",
    # THE ROMAN ARM MUST NOT ADMIT ORDINARY WORDS. Every one of these is spelt
    # entirely from the roman letters, so a naive [ivxlcdm]+ takes it, and the
    # nullable parse of a well-formed numeral takes ANY word that follows.
    "Green (2001), the table did not survive review",
    "Green (2001), the table mid-way through the report",
    "Green (2001), the table lid was closed",
    "Green (2001), a table civil servants use",
    # The letter arm is case-sensitive precisely so this stays prose.
    "Green (2001), the table a reader can open",
    "Green (2001), the rows are unlabelled",
    # An ISBN is its digits. Ten characters drawn from [0-9X-] is not an ISBN.
    # WHAT THIS DOES NOT REACH: `ISBN 0000000000` is admitted, and no local rule
    # refuses it -- it satisfies the ISBN-10 checksum exactly (sum of i*d_i is 0,
    # and 0 mod 11 is 0), as all-zeros satisfies the ISBN-13 one. Separating it
    # from a real ISBN needs a registry lookup, not a pattern or an arithmetic
    # check, so it is recorded here rather than half-solved.
    "Some Book, ISBN ----------",
    "Some Book, ISBN -- -- -- --",
)

#: WHAT IT MUST STILL ADMIT. The first two are the forms the committed cases use
#: -- ``Table 26.1`` carries the Abramowitz and Stegun case entirely, since that
#: citation has no DOI to fall back on -- and the rest are the other four shapes a
#: position in a work is written in.
_HAS_LOCATOR = (
    "Author (Year), Table 3, row 2",
    "Abramowitz and Stegun (1964) -- Table 26.1, p. 966",
    "Author (Year), pp. 12-14",
    "Author (Year), p.966",
    "Author (Year), pages 12-14",
    "Author (Year), ISBN 978-0-521-81099-3",
    # ISBN-10 ends on a check character that may be X, so the arm counts nine
    # digits and then a digit OR an X rather than ten digits.
    "Bloggs (1990), ISBN 0-8044-2957-X",
    # THE FORMS A DIGIT-ONLY RULE REFUSED. The Journal of Finance numbers tables
    # in roman, appendix tables carry a letter, and book front matter is
    # roman-paginated; all three appear in citations this harness must accept.
    "Author (Year), Table III",
    "Author (Year), Table IV",
    "Author (Year), Table XIV",
    "Author (Year), Table A.1",
    "Author (Year), Appendix Table B2",
    "Author (Year), p. iv",
    "Author (Year), pp. xii-xiv",
    "Author (Year), pp. II-IV",
)


#: EVERY FORM THE PATTERN WAS WIDENED TO ADMIT, PAIRED WITH ITS NEAREST MISS.
#: The two flat lists above prove each polarity somewhere; a pair proves the
#: pattern discriminates HERE, on two strings that differ by as little as
#: possible. A widened rule watched only being generous is half a control -- the
#: half that cannot tell "wider" from "matches anything".
#:
#: WHAT NO PATTERN CAN SEPARATE, recorded so the gap is known rather than
#: rediscovered: `Table XL` is table 40 and "the table XL sizes" is prose, and
#: they are the same string to any rule that reads roman numerals. The pairs
#: below are the ones a pattern CAN decide.
_NEAR_MISS = (
    ("Author (Year), Table A.1", "Author (Year), the table Anderson built"),
    ("Author (Year), Table A", "Author (Year), table Aardvark"),
    ("Author (Year), p. iv", "Author (Year), p. ivory"),
    ("Author (Year), Table III", "Author (Year), the table Illinois keeps"),
    ("Author (Year), pp. xii-xiv", "Author (Year), pp. mixed together"),
    ("Bloggs (1990), ISBN 0-8044-2957-X", "Bloggs (1990), ISBN ----------"),
)


@pytest.mark.parametrize(("admitted", "refused"), _NEAR_MISS)
def test_rule_two_discriminates_between_a_locator_and_its_nearest_miss(
    admitted: str, refused: str
) -> None:
    """BOTH POLARITIES ON ONE WIDENED FORM, in one case, so neither can drift
    without the other noticing. The block half alone is satisfied by a pattern
    that refuses everything, and the pass half alone by one that admits
    everything; only the pair says the rule discriminates."""
    _require_a_published_locator(admitted)
    with pytest.raises(Inadmissible, match="carries no locator"):
        _require_a_published_locator(refused)


@pytest.mark.parametrize("citation", _NO_LOCATOR)
def test_rule_two_refuses_a_citation_naming_no_position_in_a_work(citation: str) -> None:
    """THE BLOCK HALF, and it is what the gate was missing.

    RULE 2 had no control of either polarity, so the pattern could decay to
    "matches almost everything" without a single test moving -- which is what it
    had done. A locator names WHICH table or page; the bare word names none.
    """
    with pytest.raises(Inadmissible, match="carries no locator"):
        _require_a_published_locator(citation)


@pytest.mark.parametrize("citation", _HAS_LOCATOR)
def test_rule_two_admits_a_citation_naming_a_position_in_a_work(citation: str) -> None:
    """THE PASS HALF. A rule tightened until it refuses everything is not tighter,
    it is broken, and the block half above cannot tell the two apart."""
    _require_a_published_locator(citation)


def test_rule_two_judges_a_dataset_citation_by_the_same_pattern() -> None:
    """The fixture form reuses this function verbatim (fixtures.py), so the hole
    reached every dataset citation too. Proved through ``validate`` rather than
    asserted about it, so the reuse is what is measured."""
    from tests.conformance.fixtures import FixtureError, validate

    sound = json.loads(
        (ENGINE_ROOT / "tests/fixtures/anscombe_1973_data_set_i.json").read_bytes()
    )
    assert validate(dict(sound)) is not None
    with pytest.raises(FixtureError, match="carries no locator"):
        validate({**sound, "citation": "Anscombe (1973), see the table, row by row"})


def test_every_dataset_in_the_tree_loads_and_builds() -> None:
    """A dataset no case names yet is still held to every rule.

    A file admitted only when something points at it is a file that rots quietly
    until the day somebody needs it, which is the day its citation turns out not
    to carry a locator.
    """
    from tests.conformance.fixtures import fixture_names

    names = fixture_names()
    assert names, "no dataset under tests/fixtures/; the fixture form reaches nothing"
    for name in names:
        built = build(fixture(name))
        assert built is not None, name
