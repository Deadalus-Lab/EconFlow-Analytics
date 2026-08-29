# SPDX-License-Identifier: AGPL-3.0-only
"""The gate framework: the shared refusal rules every wrapper body may assume.

WHAT THIS IS. The once-written validity rules that MANY wrappers across DIFFERENT
categories need. Exactly as :mod:`econflow_engine.serialize` is the ONE
serialisation, this is the once-written validity rule; copying one into each
caller would mean dozens of independent points of drift in a CORRECTNESS rule.

THE FIVE MODULES:

:mod:`~econflow_engine.gates.primitives`
    the eight refusal primitives a body calls, and ``GATE_DETAIL_CODES``.
:mod:`~econflow_engine.gates.registry`
    detail code -> primitive, and ``gates_for(fn)``, which reads the method
    card's ``precondition_gates``.
:mod:`~econflow_engine.gates.estimation`
    the refusals a body wrapping a FITTED ESTIMATOR needs -- an argument the
    contract carries no default for, a named column the frame lacks, a name that
    is not a bare identifier, an assembled specification the formula allowlist
    refuses, two spellings of one specification, an iteration that did not
    converge, a converged iteration whose numbers are not numbers, the
    estimator's own exception translated into a refusal, a combination of
    arguments the library does not carry, and four questions about the data a
    count model asks: whole non-negative numbers, a value strictly inside an open
    interval, a level the model is about actually occurring, and column names and
    row labels that identify what they name. NOT registry
    primitives: the registry is keyed by detail code and is total, so a new
    primitive would mean a new code, and the code vocabulary is shared with the
    corpus. Two of them are a security boundary.
:mod:`~econflow_engine.gates.cross_section`
    normative gate 4 -- refuse data carrying time order to a cross-section
    method. Returns a diagnostics report the caller may surface.
:mod:`~econflow_engine.gates.sliding_window`
    normative gate 1 (Keogh). A DETECTOR, NOT a blocker: it returns the step
    ``k`` (0 = clean) and the caller decides.

PRINCIPLES, for anything added here:

* pure   -- no mutation, no printing, no plotting, no transport.
* total  -- every unsupported type raises. NEVER a silent pass-through.
* hard   -- failure raises a ``GateError`` with an EDUCATIONAL message: what,
  why, where to go.
* numeric-out -- returns purely numeric diagnostics, ready to serialise.
"""

from __future__ import annotations

from econflow_engine.gates.cross_section import (
    CrossSectionReport,
    GroupDiagnostics,
    gate_cross_section_only,
)
from econflow_engine.gates.estimation import (
    is_estimator_refusal,
    refuse_a_combination,
    refuse_a_multi_model_fit,
    refuse_estimator_failure,
    require_a_bare_name,
    require_a_column,
    require_an_aligned_index,
    require_an_allowlisted_specification,
    require_an_observed_value,
    require_at_most_one_spelling,
    require_convergence,
    require_counts,
    require_distinct_column_names,
    require_finite_estimates,
    require_strictly_inside,
    require_supplied,
    require_within_bounds,
)
from econflow_engine.gates.primitives import (
    GATE_DETAIL_CODES,
    require_balanced_panel,
    require_cross_section,
    require_full_rank,
    require_in_range,
    require_min_length,
    require_no_missing,
    require_regular_frequency,
    require_variance,
)
from econflow_engine.gates.registry import PRIMITIVES, gates_for
from econflow_engine.gates.sliding_window import gate_sliding_window_step

__all__ = [
    "GATE_DETAIL_CODES",
    "PRIMITIVES",
    "CrossSectionReport",
    "GroupDiagnostics",
    "gate_cross_section_only",
    "gate_sliding_window_step",
    "gates_for",
    "is_estimator_refusal",
    "refuse_a_combination",
    "refuse_a_multi_model_fit",
    "refuse_estimator_failure",
    "require_a_bare_name",
    "require_a_column",
    "require_an_aligned_index",
    "require_an_allowlisted_specification",
    "require_an_observed_value",
    "require_at_most_one_spelling",
    "require_balanced_panel",
    "require_convergence",
    "require_counts",
    "require_cross_section",
    "require_distinct_column_names",
    "require_finite_estimates",
    "require_full_rank",
    "require_in_range",
    "require_min_length",
    "require_no_missing",
    "require_regular_frequency",
    "require_strictly_inside",
    "require_supplied",
    "require_variance",
    "require_within_bounds",
]
