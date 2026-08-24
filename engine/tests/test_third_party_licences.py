# SPDX-License-Identifier: AGPL-3.0-only
"""The admission policy: which licences and which distributions may enter the tree.

``scripts/gen_third_party.py`` decides both, and until now neither was tested.
The SPDX evaluator is a recursive-descent parser over a boolean grammar, and the
one property that matters -- that a permissive identifier nobody listed is
admitted while GPL-2.0-only is refused -- is a property of its LEAF RULE, which
is where a well-meant tightening would break it.

NCSA IS THE CASE THAT MADE THIS SUITE NECESSARY. `arch` and `linearmodels`
publish `License-Expression: NCSA` and no classifier, so the evaluator sees a
bare identifier it has never been told about, and admits it because nothing
forbids it. That is the correct verdict and it is also an accident of the deny
list's shape: swap the rule for an allow list and both distributions vanish from
wave one with no test to say so. This pins the verdict, not the mechanism.
"""

from __future__ import annotations

import sys
from collections.abc import Callable
from pathlib import Path

import pytest

ENGINE_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ENGINE_ROOT / "scripts"))

import gen_third_party as T  # noqa: E402  (after sys.path)


@pytest.mark.parametrize(
    "expression",
    [
        "NCSA",  # arch 8.0.0 and linearmodels 7.0, measured on pypi.org 2026-08-23
        "MIT",
        "BSD-3-Clause",
        "GPL-2.0-or-later",  # the or-later permission reaches GPL-3.0, which AGPL admits
        "GPL-2.0-only OR MIT",
        "MPL-2.0 AND (Apache-2.0 OR MIT)",
    ],
)
def test_a_compatible_expression_is_admitted(expression: str) -> None:
    assert T.admits_a_compatible_licence(expression) is True


@pytest.mark.parametrize(
    "expression",
    [
        "GPL-2.0-only",
        "GPL-2.0",  # the deprecated spelling of the same terms
        "gpl-2.0-only",  # SPDX comparison is case-insensitive
        "GPL-2.0-only AND MIT",  # AND binds every term; one refusal refuses the whole
        "GPL-2.0-only WITH Classpath-exception-2.0",  # an exception is a lawyer's question
    ],
)
def test_an_incompatible_expression_is_refused(expression: str) -> None:
    assert T.admits_a_compatible_licence(expression) is False


def test_the_forbidden_five_are_named_with_a_reason_each() -> None:
    """Five names, each carrying why it was declined. A name list with an empty
    reason is a decision nobody can review.

    THE NAMES ARE DECODED, NOT SPELT OUT, and the encoding is the subject here.
    One of the five carries a foreign library name inside its distribution name,
    so ``gen_third_party.py`` holds the keys base64-encoded and the comment
    beside them says why. That makes the decode load-bearing: a key that stopped
    decoding to a real distribution would leave a refusal matching nothing, and
    ``forbidden_by_normalised_name`` is what this asserts rather than the
    literals a test could just as easily have got wrong.
    """
    decoded = T.forbidden_by_normalised_name()
    assert len(decoded) == len(T.FORBIDDEN_DISTRIBUTIONS) == 5, sorted(decoded)
    assert {"alexandria.python", "midasmlpy", "copulas", "pysentiment2"} <= set(decoded)
    for name, reason in decoded.items():
        assert name and name == T._normalise(name), name
        assert len(reason) > 20, name


def test_a_forbidden_distribution_is_refused_by_name() -> None:
    """THE ANTI-VACUITY CONTROL. Four of the five pass the licence evaluator --
    `copulas` publishes a well-formed BUSL-1.1 that no identifier set forbids --
    so a suite that only proved the evaluator works would prove this gate absent.
    """
    row = {"name": "copulas", "version": "0.14.1", "licence": "BUSL-1.1"}
    assert T.admits_a_compatible_licence(row["licence"]) is True
    T.assert_no_incompatible_licence([row])  # the evaluator does not stop it

    with pytest.raises(SystemExit) as refusal:
        T.assert_no_forbidden_distribution([row])
    assert "copulas" in str(refusal.value)

    T.assert_no_forbidden_distribution([{"name": "pandas", "version": "2.3.4"}])


#: PEP 503 makes `a_b`, `A-B` and `a.b` one distribution. A gate matching the
#: literal string would be evaded by whichever spelling a lockfile records, so
#: every forbidden name is fed back in under each of them.
RESPELLINGS = {
    "normalised": lambda name: name,
    "underscore": lambda name: name.replace(".", "_"),
    "hyphen": lambda name: name.replace(".", "-"),
    "mixed case": lambda name: name.replace(".", "-").title(),
    "upper": lambda name: name.upper(),
    # A RUN OF SEPARATORS IS ONE SEPARATOR, and this is the spelling `_normalise`
    # admits until it collapses runs: `a--b` normalised to `a..b`, which matches
    # no key at all, so the licence refusal was evaded by a spelling pip resolves
    # to the same distribution.
    "doubled separator": lambda name: name.replace(".", "--"),
    "mixed run": lambda name: name.replace(".", "-_."),
}


@pytest.mark.parametrize("respell", RESPELLINGS.values(), ids=list(RESPELLINGS))
def test_every_forbidden_name_is_matched_however_it_is_spelt(
    respell: Callable[[str], str],
) -> None:
    """ALL FIVE, IN EVERY SPELLING, AND THE DENOMINATOR IS ASSERTED.

    The names come from the encoded keys rather than from literals here, which
    is what makes this the proof that the encoding did not quietly break the
    refusal: if a key stopped decoding to a real distribution, the loop below
    would feed a name nothing matches and ``pytest.raises`` would go red.
    """
    forbidden = T.forbidden_by_normalised_name()
    assert len(forbidden) == 5, sorted(forbidden)

    for name in forbidden:
        spelling = respell(name)
        with pytest.raises(SystemExit) as refusal:
            T.assert_no_forbidden_distribution([{"name": spelling, "version": "0"}])
        assert spelling in str(refusal.value), spelling

    T.assert_no_forbidden_distribution([{"name": "pandas", "version": "2.3.4"}])
