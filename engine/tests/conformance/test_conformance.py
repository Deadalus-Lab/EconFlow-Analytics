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
2. ``citation`` carries a locator -- a DOI, an ISBN, or a table/page/row -- and
   names a published source rather than this engine's own output.
3. The tolerance BITES: every numeric leaf is perturbed by ten times the class's
   rtol (or ten times its atol where rtol is zero, or one representable step
   where both are zero) and the comparison must REFUSE the result. A class so
   loose that the perturbation survives is rejected here, which is what makes
   ``_policy.json`` load-bearing rather than a document nobody can fail.
4. Skips are accounted for exactly: ``skipped == n_cases - implemented_cases``.
   The only admissible reason to skip is an unwritten wrapper body.
"""

from __future__ import annotations

import ast
import json
import math
import re
from dataclasses import dataclass
from functools import cache
from importlib import import_module
from inspect import signature
from pathlib import Path
from typing import Any

import pytest

ENGINE_ROOT = Path(__file__).resolve().parent.parent.parent
ORACLE = ENGINE_ROOT / "tests" / "oracle"
POLICY_FILE = ORACLE / "_policy.json"
ARTIFACTS = ENGINE_ROOT / "artifacts"
INVENTORY = ENGINE_ROOT.parent / ".github" / "inventory.json"

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
_LOCATOR = re.compile(r"\b(table|page|row|isbn|p\.|pp\.)", re.IGNORECASE)

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
    ``engine.n_implemented``. It is repeated here rather than shared because that
    one is embedded in a shell heredoc; the accounting test below asserts the two
    agree, so a divergence is a red test rather than a quiet one.
    """
    written: set[str] = set()
    for path in sorted((ENGINE_ROOT / "src" / "econflow_engine" / "wrappers").rglob("*.py")):
        if path.name == "__init__.py":
            continue
        for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
            if not isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef):
                continue
            if node.name.startswith("_"):
                continue
            body = [
                s
                for s in node.body
                if not (
                    isinstance(s, ast.Expr)
                    and isinstance(s.value, ast.Constant)
                    and isinstance(s.value.value, str)
                )
            ]
            exc = body[0].exc if (len(body) == 1 and isinstance(body[0], ast.Raise)) else None
            name = getattr(exc, "func", exc)
            if not (isinstance(name, ast.Name) and name.id == "NotImplementedError"):
                written.add(node.name)
    return frozenset(written)


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
            "table, page or row the number is printed in -- an author and a year "
            "alone cannot be checked."
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


@cache
def _outcomes() -> dict[str, tuple[str, Any]]:
    """Run every admissible case ONCE. ``(state, payload-or-message)`` per case.

    Cached and shared rather than run inside each parametrised test, so that the
    accounting test below sees the same outcomes the per-case tests do whatever
    order ``pytest-randomly`` chooses.
    """
    from econflow_engine.mcp.gateway import run_method

    results: dict[str, tuple[str, Any]] = {}
    for case in _ADMISSIBLE:
        if case.namespace == ENGINE_NAMESPACE:
            helper = getattr(import_module(f"econflow_engine.{case.module}"), case.fn)
            # BOUND THROUGH THE SIGNATURE, not splatted as keywords. A case names its
            # inputs, and `to_mcp` is a singledispatch generic that dispatches on
            # args[0] and refuses a keyword-only call; binding turns the named
            # mapping into the call the function actually accepts.
            try:
                bound = signature(helper).bind(**case.inputs)
                results[case.id] = ("succeeded", helper(*bound.args, **bound.kwargs))
            except Exception as exc:
                results[case.id] = ("raised", f"{type(exc).__name__}: {exc}")
            continue
        response = run_method(case.fn, case.inputs)
        results[case.id] = (
            response.state,
            response.payload if response.state == "succeeded" else response.message,
        )
    return results


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
    """``skipped == n_cases - implemented_cases``, and no other skip is admissible."""
    implemented = _implemented_node_functions()
    declared = int(_read(INVENTORY)["engine"]["n_implemented"])
    assert len(implemented) == declared, (
        f"{len(implemented)} wrapper function(s) carry a body, and "
        f"engine.n_implemented in .github/inventory.json says {declared}"
    )
    implemented_cases = [
        c for c in _ADMISSIBLE if c.namespace == ENGINE_NAMESPACE or c.fn in implemented
    ]
    skipped = [c for c in _ADMISSIBLE if _outcomes()[c.id][0] == "not-implemented"]
    assert len(skipped) == len(_ADMISSIBLE) - len(implemented_cases), (
        f"{len(skipped)} case(s) skipped, {len(_ADMISSIBLE) - len(implemented_cases)} "
        f"expected. A case skips because its body is unwritten and for no other "
        f"reason: skipped={sorted(c.id for c in skipped)}"
    )
