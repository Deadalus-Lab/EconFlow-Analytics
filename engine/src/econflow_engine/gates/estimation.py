# SPDX-License-Identifier: AGPL-3.0-only
"""The refusals a body that wraps a FITTED ESTIMATOR needs, and no others.

WHY THIS MODULE EXISTS RATHER THAN FIVE ``raise`` STATEMENTS IN ONE WRAPPER.
``tests/test_gate_discipline.py`` permits exactly two ``raise`` forms anywhere
under ``wrappers/**``: the emitted ``NotImplementedError`` and a bare re-raise
inside an ``except``. A refusal is a CALL, and the call has to land somewhere a
refusal may be written -- which is this package. The eight registry primitives in
:mod:`~econflow_engine.gates.primitives` answer questions about a numeric VECTOR;
none of them answers a question about an estimator's own contract, and the first
wrapper body written in phase 2.2 needed six such questions asked and one
library refusal translated.

TWO OF THE SIX ARE A SECURITY BOUNDARY AND ARE NOT INTERCHANGEABLE WITH THE REST.
:func:`require_a_bare_name` and :func:`require_an_allowlisted_specification` guard
the one place a body turns caller input into a string that is EVALUATED. They
were added after a live injection through ``fixef``, and each carries the
measurement that proves what it blocks.

WHAT IS DELIBERATELY NOT HERE. No new detail code: every refusal below carries
one of the ten :data:`~econflow_engine.gates.codes.GATE_DETAIL_CODES` already
declared, so ``PRIMITIVES``, ``corpus/_vocabulary.json`` and the method-card
schema enum do not move. These functions are NOT registry primitives and are not
declarable on a card: a card's ``precondition_gates`` names a rule about the
CALLER'S DATA that a reviewer of the card can judge, and four of the five below
are about the call itself. :mod:`~econflow_engine.gates.cross_section` and
:mod:`~econflow_engine.gates.sliding_window` are already in that position.

THE FIFTH IS THE ONE THAT MATTERS MOST AND IS THE LEAST OBVIOUS.
:func:`refuse_estimator_failure` translates the estimator's own exception into a
``GateError``. Without it a documented precondition -- a dependent variable that
is not binary, a formula naming a column the frame does not carry -- reaches the
caller as a traceback, because ``mcp/make_tool.py`` turns a ``GateError`` into a
clean refusal and lets every other exception escape as a crash.
"""

from __future__ import annotations

import keyword
from typing import NoReturn

import pandas as pd

from econflow_engine.errors import GateError
from econflow_engine.formula import validate_formula
from econflow_engine.gates.codes import GateDetailCode, refusal

__all__ = [
    "is_estimator_refusal",
    "refuse_a_multi_model_fit",
    "refuse_estimator_failure",
    "require_a_bare_name",
    "require_a_column",
    "require_an_allowlisted_specification",
    "require_at_most_one_spelling",
    "require_convergence",
    "require_supplied",
]

#: The packages whose exceptions are the ESTIMATOR objecting rather than a defect
#: in a wrapper. Adding one is a statement that this engine reads that package's
#: errors as refusals; :func:`is_estimator_refusal` records what was measured.
_ESTIMATOR_PACKAGES: frozenset[str] = frozenset({"formulaic", "pyfixest"})


def _refuse(fn: str, message: str, code: GateDetailCode) -> GateError:
    """The one refusal shape, with the node that blocked the call named first."""
    return refusal(f"{fn}: {message}", code)


def require_supplied(value: object, *, fn: str, arg: str, remedy: str) -> None:
    """Refuse ``None`` for an argument the CONTRACT carries no default for.

    THE CASE THIS IS FOR, stated precisely because inventing a default here is
    the tempting alternative. A node argument may be optional and still have no
    entry in ``NODE_META[fn].defaults``; ``adapt_args`` then passes nothing and
    the body sees ``None``. Where the method has no meaning without the value,
    the body's only honest answers are to refuse it or to choose a default the
    wire contract does not publish -- and a default a client cannot read out of
    ``node-specs.json`` is a behaviour nobody agreed to. ``remedy`` names the
    admissible values, so the message tells the caller what to send.
    """
    if value is None:
        raise _refuse(
            fn,
            f'"{arg}" was not supplied, and this method has no meaning without it. '
            f"The node declares the argument optional, but the contract carries no "
            f"default for it, so nothing was filled in on your behalf and nothing "
            f"will be: a default this method invented would be one no client can "
            f"read out of the contract. {remedy}",
            "precondition-domain",
        )


def require_a_column(frame: pd.DataFrame, *, column: str, fn: str, arg: str) -> None:
    """Refuse a column name the frame does not carry, before the estimator sees it.

    The estimator's own failure here is a formula-engine error naming a factor
    rather than a column, which says nothing about which argument was wrong.

    PANDAS IS IMPORTED AT RUN TIME AND NOT UNDER ``TYPE_CHECKING``, which is not a
    style choice. ``tests/conftest.py`` installs ``beartype.claw`` over
    ``econflow_engine``, so every annotation in this package is RESOLVED when the
    function is called; a ``pd.DataFrame`` whose ``pd`` exists only for a type
    checker raises ``BeartypeCallHintForwardRefException`` at the first real call.
    Measured on this function before the import was moved.
    """
    if column not in frame.columns:
        raise _refuse(
            fn,
            f'"{arg}" names the column {column!r}, which the supplied data does not '
            f"carry. Its columns are {sorted(str(c) for c in frame.columns)}.",
            "precondition-shape",
        )


def require_a_bare_name(value: str, *, fn: str, arg: str) -> None:
    """Refuse a name that is not one plain identifier, BEFORE it is spliced into a formula.

    WHAT THIS BLOCKS, MEASURED against pyfixest 0.60.0 and the formulaic 1.2.2 it
    parses with. A body that concatenates this argument into an estimator
    specification hands it to a parser that splits on ``|``
    (``estimation/formula/parse.py``) and wraps each fixed effect as
    ``__fixed_effect__(<text>)`` (``estimation/formula/utils.py``); formulaic then
    evaluates that factor with ``eval(compiled, {}, LayeredMapping(...))``
    (``utils/stateful_transforms.py``). Empty globals means CPython injects
    ``__builtins__``, so ``__import__`` is reachable and the argument is
    EXECUTABLE CODE rather than a value. Live-measured: a ``fixef`` of
    ``__import__("os").environ.__setitem__("EF_RCE","pwned") or unit`` set that
    variable in this process.

    :func:`require_a_column` DOES NOT STOP IT. A caller who names a column with
    the payload satisfies it, and column names are caller-supplied -- a CSV
    header, or a frame fixture's ``columns`` list.

    ONE IDENTIFIER IS THE WHOLE RULE because an identifier cannot express a call,
    an attribute access, a subscript or an operator. It narrows nothing the
    contract promised: the argument names ONE column, and a column called ``a^b``
    was going to be mis-parsed by the formula engine anyway.
    """
    if not value.isidentifier() or keyword.iskeyword(value):
        raise _refuse(
            fn,
            f'"{arg}" is {value!r}, which is not a plain column name. This argument '
            f"is spliced into the formula the estimator is given, and that formula "
            f"is EVALUATED, so only a single bare name is accepted here -- no "
            f"operator, no call, no separator, no keyword. Name the column, or "
            f"rename a column whose name is not a plain name.",
            "precondition-domain",
        )


def require_an_allowlisted_specification(specification: str, *, fn: str) -> None:
    """Re-walk the ASSEMBLED estimator specification against the formula allowlist.

    THE SECOND OF THE TWO ENFORCEMENTS THE c00 NODE DOCUMENTATION ALREADY
    DECLARES -- "restricted to the formula allowlist (default-deny, enforced
    TWICE: at the argument boundary and again in the node)". The boundary walk in
    :mod:`econflow_engine.formula` sees the ``formula`` argument as the caller
    sent it. It never sees the string a body BUILDS from that argument and
    others, and the built string is what reaches the estimator. This asks the
    same default-deny question of what is actually handed over.

    THE FIXED-EFFECT SEPARATOR SURVIVES THE WALK, which is what makes this
    check usable on an assembled specification rather than only on a bare
    formula: ``|`` is in ``FORMULA_ALLOWED_CALLS``, and measured,
    ``validate_formula("y ~ x | unit")`` returns ok while the payload above
    returns ``formula-parse``.
    """
    result = validate_formula(specification)
    if not result.ok:
        raise _refuse(
            fn,
            f"the estimator specification {specification!r} was refused by the "
            f"formula allowlist, which is default-deny. {result.message} The "
            f"specification is built from the formula and the fixed effect, so "
            f"either of them may be the cause.",
            "precondition-domain",
        )


def require_at_most_one_spelling(
    *, fn: str, first: tuple[str, bool], second: tuple[str, bool], remedy: str
) -> None:
    """Refuse two spellings of one specification, rather than silently ranking them.

    Each argument is ``(name, is_present)``. Where a node offers two ways to say
    the same thing and its card does not say which wins, choosing one in the body
    settles a contract question in a place no reviewer of the card can see it.
    """
    if first[1] and second[1]:
        raise _refuse(
            fn,
            f'"{first[0]}" and "{second[0]}" were both supplied, and they are two '
            f"spellings of one specification. The method card does not say which of "
            f"the two wins, so neither is chosen here. {remedy}",
            "precondition-domain",
        )


def require_convergence(*, converged: bool, fn: str, estimator: str, remedy: str) -> None:
    """Refuse the coefficients of a fit whose iteration did not converge.

    An iteratively reweighted least-squares fit that runs out of iterations still
    RETURNS -- with whatever the last step held. The flag is a boolean a caller
    can ignore, and the numbers beside it look exactly like an estimate.
    """
    if not converged:
        raise _refuse(
            fn,
            f"the {estimator} iteration did not converge, so the coefficients it "
            f"returned are the last step's values rather than an estimate. They are "
            f"not reported. {remedy}",
            "precondition-degenerate",
        )


def is_estimator_refusal(error: object) -> bool:
    """Is this exception the ESTIMATOR objecting, rather than a defect in the body?

    THE TWO ARMS ARE MEASURED, NOT GUESSED, against pyfixest 0.60.0 and the
    formulaic 1.2.2 it parses formulas with. A refusal about the caller's data
    arrives as one of:

    * ``ValueError`` -- "The dependent variable must have two unique values.",
      "The dependent variable must be binary (0 or 1)."
    * ``ArithmeticError`` -- ``ZeroDivisionError`` raised out of the IWLS when the
      sample is two observations long, and ``FloatingPointError`` wherever a
      caller has put ``np.seterr`` into a raising state around an intermediate
      the estimator expects to underflow. THE WHOLE CLASS, INCLUDING AN OVERFLOW,
      and that is deliberate rather than an oversight in the spelling: a caller
      whose error state raises on overflow gets ``FloatingPointError`` from numpy
      and not ``OverflowError`` -- measured -- so excluding ``OverflowError``
      would exclude the one class an overflow does not arrive as. A body calls
      this from an ``except`` around the ESTIMATOR CALL ALONE, which is what makes
      the whole class safe to read as the estimator's: none of this engine's own
      arithmetic is inside that block.
    * an exception class defined by the estimator or its formula engine --
      ``formulaic.errors.FactorEvaluationError`` for a column the frame does not
      carry, ``pyfixest.errors.FormulaSyntaxError`` for a malformed formula.
      NEITHER derives from ``ValueError``; both derive straight from
      ``Exception``, so a type-based catch cannot reach them.

    THE DEFINING MODULE IS READ OFF THE CLASS AND THE CLASS IS NOT IMPORTED.
    ``formulaic`` is a transitive dependency of ``pyfixest``; importing it to
    name its base class would declare a dependency this engine does not take, and
    ``deptry`` is right to object to that.

    Everything else -- an ``AttributeError``, a ``TypeError``, a ``KeyError``
    raised by this engine's own code -- is a defect in the wrapper and must reach
    the caller as the crash it is.
    """
    if isinstance(error, ValueError | ArithmeticError):
        return True
    return type(error).__module__.split(".", 1)[0] in _ESTIMATOR_PACKAGES


def refuse_estimator_failure(
    error: Exception, *, fn: str, code: GateDetailCode, remedy: str
) -> NoReturn:
    """Translate the estimator's own refusal into this engine's refusal. Always raises.

    THE ORIGINAL MESSAGE IS CARRIED VERBATIM and the class is named beside it: it
    is the only account of what the estimator actually objected to, and a
    paraphrase here would be this engine guessing at a library's reasoning.
    ``raise ... from error`` at the call site keeps the traceback for a developer
    while the wire sees the refusal.
    """
    raise _refuse(
        fn,
        f"the estimator refused these inputs. It reported "
        f"{type(error).__name__}: {error}. {remedy}",
        code,
    )


def refuse_a_multi_model_fit(*, fn: str, produced: str, remedy: str) -> NoReturn:
    """Refuse a fit that is SEVERAL models, where the node's contract is one. Always raises.

    A fixest-style formula language can ask for a family of models in one string
    -- ``sw()``, ``csw()``, several variables on the left -- and the estimator
    then returns a COLLECTION rather than a fit. Every node in this catalogue
    declares one result, so the collection has nowhere to go: reading the first
    of its models would answer a question the caller did not ask, and reading
    none of them would report success over an empty result.

    ``-> NoReturn`` IS PART OF THE CONTRACT AND NOT DECORATION. Called under an
    ``isinstance`` guard it narrows the fit's type for the checker as well as for
    the reader, which is what lets a body reach the single model's attributes
    without a cast that asserts what this call has already established.
    """
    raise _refuse(
        fn,
        f"the formula asked for more than one model and the estimator returned a "
        f"{produced} rather than a fit. This node reports one model. {remedy}",
        "precondition-shape",
    )
