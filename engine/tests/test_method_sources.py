# SPDX-License-Identifier: AGPL-3.0-only
"""The implementation-source register's own contract, asserted over all 598 rows.

WHY A SUITE OF ITS OWN, BESIDE tests/test_gen_artifacts.py. That suite answers
for the GENERATOR: it rebuilds the artifacts from the corpus and compares. This
one answers for the REGISTER'S CONTENT, and it generates nothing -- it reads
METHOD-SOURCES.json, uv.lock and the wrapper tree as they stand. A row that
names a library nobody can install, or a paper whose identifier is not a DOI, is
wrong however faithfully the generator carried it over.

THREE KINDS OF SOURCE, AND NO ROW NAMED ANYWHERE IN THIS FILE. A ``selected``
row names exactly one of a library, a paper by DOI, or a dataset; a ``planned``
row names none of them. That is a rule, and it holds for every row, which is
what an exception carried by name never does: an exception stops the gate
answering for the row it names, and gives the next unresolved row a precedent to
join in silence. What replaces it is a COUNT, ``engine.unresolved_sources`` in
.github/inventory.json -- so a second unresolved row turns this suite red, and
resolving the first is a reviewed one-line diff in the manifest.

THE DATASET KIND IS THE ONE WHOSE SOURCE THIS REPOSITORY DISTRIBUTES, which is
why its record answers four questions a library name and a DOI answer by
themselves: publisher, locator, retrieved, sha256. THE DIGEST IS THE IDENTITY
AND THE LOCATOR IS METADATA BESIDE IT -- a publisher who rewrites a page in
place, with no version identifier and no DOI, leaves a URL recording where
somebody looked rather than what they got. So the digest is RECOMPUTED here from
the committed bytes rather than read and believed.

A SOURCE IS TWO CLAIMS AND THIS FILE NOW ANSWERS FOR BOTH. That a distribution
is installable and admissibly licensed is one; that it COMPUTES the method the
row describes is the other, and nothing in a lockfile or a licence classifier
can settle it. The second is what ``audited`` records, and it is asserted as a
COUNT of rows examined rather than as an absence of unexamined ones -- because
a register with the column deleted from every row satisfies the absence
perfectly while having examined nothing.

NO ROW CARRIES A DATASET TODAY, AND THAT IS WHY THE CONTROLS BELOW EXIST. The
row the kind was defined for is still planned pending a licensing decision (see
METHOD-SOURCES.json's own comment), so a check written only over the live
register would examine nothing and report success -- the failure this repository
has hit six times. ``_dataset_faults`` is therefore exercised against planted
records it MUST reject and one it MUST accept, on the pattern
.github/scripts/check-no-network.sh established, and the same function judges
every real row the day one lands.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
import tomllib
from pathlib import Path
from typing import Any

import pytest

from econflow_engine.metrics import find_manifest, find_repo_root

ENGINE_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ENGINE_ROOT / "scripts"))

from gen_third_party import (  # noqa: E402  (after sys.path)
    FORBIDDEN_DISTRIBUTIONS,
    forbidden_by_normalised_name,
)

REGISTER = ENGINE_ROOT / "METHOD-SOURCES.json"
LOCK = find_repo_root(Path(__file__)) / "uv.lock"
INVENTORY = find_manifest(Path(__file__))

#: Where a committed dataset snapshot lives: inside the package, because a node
#: that ships its data has to carry it into the wheel that ships the node.
SNAPSHOTS = ENGINE_ROOT / "src" / "econflow_engine" / "data"

#: The three source kinds. Exactly one of them is named per row.
KINDS = ("library", "paper", "dataset")

#: A dataset row's closed key set. A misspelt key that is merely ignored turns a
#: reviewed provenance record into no provenance at all.
DATASET_FIELDS = frozenset({"publisher", "locator", "retrieved", "sha256"})

DOI = re.compile(r"^10\.\d{4,9}/")
ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")

#: HOW MANY ROWS HAVE HAD THEIR METHOD FIT EXAMINED, and it is a COUNT because
#: "no row is unaudited" is a sentence an empty register satisfies. A row's
#: source is a claim that the named library computes the method the row's
#: ``methods`` and ``node_fns`` describe, and that claim is separate from the
#: licence and version work: a distribution can be perfectly admissible and
#: still not implement the estimator. ``audited`` records that somebody checked.
#:
#: 149 of these were examined by the source-selection box, which probed the four
#: installed distributions live and enumerated the four uninstalled ones from
#: upstream source; 21 of the 149 named a library that does not implement their
#: method. The remaining 275 are the deferred tier, examined against PyPI
#: metadata, upstream code search and rendered API references; 32 of those 275
#: named a library that does not implement their method.
#: This figure moves only when rows are actually examined.
AUDITED_ROWS = 424

#: EVERY (row, distribution) PAIR AN AUDIT MEASURED AS NOT IMPLEMENTING THE ROW'S
#: METHOD, and the reason this is a table rather than prose in a note: the
#: measurement is expensive, it is not visible anywhere in the tree, and nothing
#: else would notice a row being pointed back at a source that was already
#: refuted. A register row becomes a wrapper docstring's "Reference
#: implementation:" line, so a silent reversion sends a reader to code that
#: cannot compute the method.
#:
#: The pairs are the register's own history, not a transcription: the wave-one
#: half is every row that was `selected` before the source-selection box and
#: carries no library after it, less the one that moved because its distribution
#: publishes no licence rather than because it lacked the method. The deferred
#: half is this audit's own moves.
#:
#: A row may name a REFUTED distribution again only with a new measurement
#: showing the distribution gained the method -- in which case the pair is
#: deleted here, in a diff that says which release added it.
REFUTED_SOURCES: dict[str, str] = {
    "c01_preparation_prechecks/bubble_tests": "arch",
    "c01_preparation_prechecks/cross_sectional_dependence": "statsmodels",
    "c03_multivariate_nowcasting/shadow_rate_var": "srvar-toolkit",
    "c04_structural_shocks/ms_var": "statsmodels",
    "c05_cointegration/gregory_hansen": "arch",
    "c05_cointegration/panel_cointegration": "statsmodels",
    "c05_cointegration/threshold_ecm": "statsmodels",
    "c06_volatility_regimes/icss_variance_breaks": "ruptures",
    "c06_volatility_regimes/jump_tests": "arch",
    "c06_volatility_regimes/realised_garch": "arch",
    "c07_causality_policy/quantile_treatment_effects": "econml",
    "c08_panel_data/heterogeneous_panel": "linearmodels",
    "c09_cross_section_networks/connectedness": "diebold-yilmaz",
    "c09_cross_section_networks/spatial_weights_diagnostics": "esda",
    "c10_trend_cycle_statespace/beveridge_nelson": "statsmodels",
    "c12_distribution_risk/caviar_fhs": "arch",
    "c12_distribution_risk/distributional_regression": "pygam",
    "c12_distribution_risk/implied_density_gar": "py-vollib",
    "c12_distribution_risk/var_backtesting": "arch",
    "c15_model_evaluation/density_evaluation": "scoringrules",
    "c15_model_evaluation/nested_predictive_tests": "dieboldmariano",
    "c17_forecast_combination/density_combination": "scoringrules",
    "c17_forecast_combination/dynamic_model_averaging": "pymc",
    "c18_yield_curve/dynamic_nelson_siegel": "nelson-siegel-svensson",
    "c18_yield_curve/shadow_short_rate": "srvar-toolkit",
    "c19_business_cycle_dating/bry_boschan": "scipy",
    "c19_business_cycle_dating/online_change_detection": "skchange",
    "c21_systemic_risk/mes_srisk": "arch",
    "c22_inequality/polarisation": "ineqpy",
    "c24_panel_var/gmm_panel_var": "pydynpd",
    "c24_panel_var/panel_granger": "statsmodels",
    "c25_expectations_surveys/disagreement_uncertainty": "scoringrules",
    "c26_text_as_data/news_indices": "nltk",
    "c26_text_as_data/readability": "nltk",
    "c27_frequency_domain/cross_spectral": "spectrum",
    "c29_unsupervised_clustering/elastic_distances": "dtaidistance",
    "c32_matching_weighting/bias_corrected_matching": "causallib",
    "c32_matching_weighting/coarsened_exact_matching": "causallib",
    "c32_matching_weighting/hidden_bias": "zepid",
    "c32_matching_weighting/subclassification": "causallib",
    "c35_resampling_inference/sieve_bootstrap": "arch",
    "c35_resampling_inference/subsampling_jackknife": "arch",
    "c38_portfolio_allocation/robust_optimisation": "cvxpy",
    "c39_market_microstructure/intraday_patterns": "arch",
    "c39_market_microstructure/liquidity_measures": "frds",
    "c39_market_microstructure/realised_measures": "arch",
    "c39_market_microstructure/trade_classification": "frds",
    "c40_option_implied_derivatives/bs_pricing_iv": "py-vollib",
    "c40_option_implied_derivatives/model_free_variance": "QuantLib",
    "c41_credit_risk_default/merton_structural": "frds",
    "c42_fiscal_debt_sustainability/debt_fan_charts": "arch",
    "c44_environment_energy_climate/climate_macro_mapping": "pyam-iamc",
}


def _normalise(name: str) -> str:
    """PEP 503 name equivalence: `scikit_learn`, `Scikit-Learn` and `scikit-learn`."""
    return re.sub(r"[-_.]+", "-", name).lower()


@pytest.fixture(scope="module")
def rows() -> dict[str, dict[str, Any]]:
    modules: dict[str, dict[str, Any]] = json.loads(
        REGISTER.read_bytes().decode("utf-8"))["modules"]
    return modules


@pytest.fixture(scope="module")
def locked() -> set[str]:
    lock = tomllib.loads(LOCK.read_text(encoding="utf-8"))
    return {_normalise(p["name"]) for p in lock["package"]}


def test_a_selected_row_names_one_source_and_a_planned_row_names_none(
    rows: dict[str, dict[str, Any]],
) -> None:
    """THE RULE, WITH NO ROW NAMED AND NO ROW EXEMPT.

    ``selected`` means exactly one of a library, a paper and a dataset;
    ``planned`` means none of the three. Stated that way it answers for all 598
    rows, where an exception carried by name answers for 597 and hands the next
    unresolved row a precedent.

    THE COUNT IS WHAT AN EXCEPTION USED TO DO, AND IT DOES IT BETTER. A row that
    is legitimately unresolved is counted in .github/inventory.json, so a SECOND
    one turns this red, and resolving the first is a reviewed one-line diff in
    the manifest rather than a line deleted from a test.
    """
    for key, row in rows.items():
        named = sum(bool(row[kind]) for kind in KINDS)
        assert row["status"] in {"planned", "selected"}, key
        assert named == (1 if row["status"] == "selected" else 0), (key, row["status"], named)

    unresolved = sorted(k for k, r in rows.items() if r["status"] == "planned")
    declared = json.loads(
        INVENTORY.read_bytes().decode("utf-8"))["engine"]["unresolved_sources"]
    assert len(unresolved) == declared, unresolved


def _committed_snapshots(root: Path) -> dict[str, str]:
    """Every file under ``root``, keyed by the SHA-256 of its bytes.

    CONTENT-ADDRESSED ON PURPOSE, so the check below matches on the bytes rather
    than on a path or a filename: a snapshot can be moved or renamed without
    becoming different bytes, and a page rewritten in place at one URL is
    different bytes without moving.
    """
    return {
        hashlib.sha256(p.read_bytes()).hexdigest(): str(p.relative_to(root))
        for p in sorted(root.rglob("*")) if p.is_file()
    }


def _dataset_faults(dataset: Any, snapshots: dict[str, str]) -> list[str]:
    """Every way a dataset record can be wrong, named rather than counted.

    ONE FUNCTION, TWO CALLERS, AND THAT IS THE WHOLE DESIGN. It judges the live
    register, where no row carries a dataset yet, and it judges the planted
    records in ``test_the_dataset_check_rejects_a_broken_record``, which exist so
    that the first call cannot be a check that examined nothing.

    The digest is RECOMPUTED from ``snapshots`` rather than read and believed. A
    hash written into a register beside the file it describes proves nothing on
    its own: nothing stops the two being committed apart, and the field then
    reads as provenance while identifying bytes this tree does not hold.
    """
    if not isinstance(dataset, dict):
        return ["not an object"]
    faults = []
    if set(dataset) != DATASET_FIELDS:
        faults.append(f"fields {sorted(dataset)} != {sorted(DATASET_FIELDS)}")
        return faults
    if not str(dataset["publisher"]).strip():
        faults.append("publisher is blank")
    if not str(dataset["locator"]).strip():
        faults.append("locator is blank")
    if not ISO_DATE.match(str(dataset["retrieved"])):
        faults.append(f"retrieved {dataset['retrieved']!r} is not an ISO date")
    if not SHA256.match(str(dataset["sha256"])):
        faults.append(f"sha256 {dataset['sha256']!r} is not a SHA-256 digest")
    elif dataset["sha256"] not in snapshots:
        faults.append(f"sha256 {dataset['sha256']} names no file under {SNAPSHOTS}")
    return faults


def test_every_dataset_row_is_a_complete_provenance_record(
    rows: dict[str, dict[str, Any]],
) -> None:
    """Publisher, locator, retrieval date and a digest over committed bytes.

    THIS EXAMINES NOTHING TODAY AND SAYS SO. No row carries a dataset yet, so
    the loop below runs zero times; what makes the rule real in the meantime is
    the control beside it, which drives the same function over records it must
    reject. The day a snapshot is admitted, this judges it without being edited.
    """
    snapshots = _committed_snapshots(SNAPSHOTS) if SNAPSHOTS.is_dir() else {}
    for key, row in rows.items():
        if row["dataset"]:
            assert _dataset_faults(row["dataset"], snapshots) == [], key


def test_the_dataset_check_flags_every_broken_record_it_is_shown(
    tmp_path: Path,
) -> None:
    """THE POSITIVE AND NEGATIVE CONTROLS, on the check-no-network.sh pattern.

    Six records that MUST be flagged, one that MUST NOT. Without these the rule
    above is a loop over an empty list -- the shape of gate this repository has
    caught six times and refuses.
    """
    snapshot = tmp_path / "chronology.csv"
    snapshot.write_bytes(b"peak,trough\n2020-02-01,2020-04-01\n")
    snapshots = _committed_snapshots(tmp_path)
    digest = hashlib.sha256(snapshot.read_bytes()).hexdigest()
    sound = {
        "publisher": "An Example Statistical Agency",
        "locator": "https://example.invalid/chronology.csv",
        "retrieved": "2026-08-24",
        "sha256": digest,
    }

    # NEGATIVE CONTROL: a complete record over bytes that are present.
    assert _dataset_faults(sound, snapshots) == []

    # POSITIVE CONTROLS: each must be flagged, and each is a mistake somebody
    # would actually make rather than an invented one.
    for label, broken in (
        ("a missing field", {k: v for k, v in sound.items() if k != "sha256"}),
        ("a misspelt field", {**{k: v for k, v in sound.items() if k != "locator"},
                              "locater": sound["locator"]}),
        ("a blank publisher", {**sound, "publisher": "   "}),
        ("a year rather than a date", {**sound, "retrieved": "2026"}),
        ("a truncated digest", {**sound, "sha256": digest[:16]}),
        ("a digest naming no committed file", {**sound, "sha256": "0" + digest[1:]}),
    ):
        assert _dataset_faults(broken, snapshots) != [], label


def test_every_paper_is_a_doi(rows: dict[str, dict[str, Any]]) -> None:
    """A citation string is not an identifier. Four DOIs recalled from memory
    during the research resolved to entirely different papers, so the register
    holds resolvable identifiers and the prose lives in the cards."""
    papers = [(k, r["paper"]) for k, r in rows.items() if r["paper"]]
    assert len(papers) == 131, len(papers)
    assert [k for k, doi in papers if not DOI.match(doi)] == []


def test_every_row_declares_a_wave(rows: dict[str, dict[str, Any]]) -> None:
    """`wave` is authored, not derived: it says whether the distribution a row
    names is admitted to uv.lock now, later, or never because the row cites a
    paper. A row without one would silently escape the lockfile check below."""
    assert {r["wave"] for r in rows.values()} == {"one", "deferred", "none"}
    for key, row in rows.items():
        # THE WAVE IS A CLAIM ABOUT A DISTRIBUTION, so it is the library column
        # that decides it -- not the status and not the other two kinds. A paper
        # row, a dataset row and an undecided row all admit nothing to the
        # lockfile, and all three read "none" for the same reason.
        if row["library"]:
            assert row["wave"] in {"one", "deferred"}, key
        else:
            assert row["wave"] == "none", key


def _audited(rows: dict[str, dict[str, Any]]) -> list[str]:
    """The rows whose method fit has been examined, named rather than counted.

    ONE FUNCTION, TWO CALLERS, on the pattern ``_dataset_faults`` established
    above. It measures the live register, and it measures the planted register
    in the control below -- which is what stops the count being a number nobody
    can make fall.
    """
    return sorted(k for k, r in rows.items() if r["audited"])


def test_the_register_counts_the_rows_whose_method_fit_was_examined(
    rows: dict[str, dict[str, Any]],
) -> None:
    """A COUNT, NOT AN ABSENCE. "no row is unaudited" is satisfied by a register
    with no audited rows in it at all, and by a column deleted from every row --
    the shape this repository has caught six times. An exact count falls the
    moment a row stops being examined, and rises only when one is."""
    assert len(_audited(rows)) == AUDITED_ROWS, len(_audited(rows))


def test_the_audit_count_falls_when_a_row_is_planted_unaudited(
    rows: dict[str, dict[str, Any]],
) -> None:
    """THE CONTROL, because the count above cannot supply one.

    A register in which every row reads audited satisfies the assertion above
    however the flag got there. This drives the same function over a register
    with one flag cleared and requires the count to drop by exactly one, so the
    number is known to be measured from the rows rather than restated.
    """
    planted = {k: dict(r) for k, r in rows.items()}
    victim = _audited(planted)[0]
    planted[victim]["audited"] = None
    assert len(_audited(planted)) == AUDITED_ROWS - 1, victim


def test_the_audited_flag_is_a_decision_and_never_a_stray_value(
    rows: dict[str, dict[str, Any]],
) -> None:
    """``True`` for examined and absent-as-``None`` for not yet. A string or a
    zero would read as audited or not by accident of truthiness, and the count
    above would move without anybody examining a row."""
    stray = sorted(k for k, r in rows.items() if r["audited"] not in (True, None))
    assert stray == [], stray


def _refuted_faults(rows: dict[str, dict[str, Any]]) -> list[str]:
    """Every row pointed back at a distribution an audit measured as not fitting.

    ONE FUNCTION, TWO CALLERS, like ``_dataset_faults``. Over the live register
    it must find nothing, and finding nothing there proves nothing on its own --
    so the control below drives it over a row put back on its refuted source and
    requires it to speak.
    """
    return [
        f"{key} names {rows[key]['library']}, measured not to implement its method"
        for key, refuted in REFUTED_SOURCES.items()
        if key in rows and rows[key]["library"]
        and _normalise(rows[key]["library"]) == _normalise(refuted)
    ]


def test_no_row_names_a_source_an_audit_already_refuted(
    rows: dict[str, dict[str, Any]],
) -> None:
    """THE MEASUREMENT IS EXPENSIVE AND INVISIBLE, so this is what keeps it.

    Establishing that a distribution does not implement a method costs a code
    search or a live probe, and the result appears nowhere in the tree -- the
    row simply names something else. Nothing else here would notice a row being
    pointed back at the refuted name, and the reversion would reappear in a
    wrapper docstring as a reference to code that cannot compute the method.
    """
    assert _refuted_faults(rows) == [], _refuted_faults(rows)


def test_the_refutation_check_flags_a_row_put_back_on_its_refuted_source(
    rows: dict[str, dict[str, Any]],
) -> None:
    """THE POSITIVE CONTROL, and the live register cannot supply one.

    Every row above already names something else, so the assertion holds over a
    table that had been emptied to nothing just as well as over the real one.
    This plants the reversion the rule exists to catch -- one row moved back to
    the distribution measured not to implement its method -- and requires the
    same function to name it.
    """
    key, refuted = next(iter(REFUTED_SOURCES.items()))
    planted = {k: dict(r) for k, r in rows.items()}
    planted[key]["library"] = refuted

    faults = _refuted_faults(planted)
    assert len(faults) == 1, faults
    assert key in faults[0], faults


def test_every_refuted_pair_names_a_row_the_register_still_carries(
    rows: dict[str, dict[str, Any]],
) -> None:
    """A table of pairs keyed on modules that no longer exist checks nothing.

    Renaming a wrapper module would leave its entry above matching no row, and
    the guard would go on passing while covering one row fewer -- which is the
    quiet way an anti-vacuity table stops being one.
    """
    orphans = sorted(k for k in REFUTED_SOURCES if k not in rows)
    assert orphans == [], orphans


def test_wave_one_libraries_resolve_in_the_lockfile(
    rows: dict[str, dict[str, Any]], locked: set[str]
) -> None:
    """WAVE ONE IS A CLAIM ABOUT THE ENVIRONMENT, and this is what makes it one.
    A row promising that the next wrapper body imports `arch` is worthless if the
    distribution is not resolved, hashed and installable from the lockfile."""
    wave_one = {r["library"] for r in rows.values() if r["wave"] == "one"}
    assert wave_one, "no row is in wave one; the check would examine nothing"
    assert sorted(n for n in wave_one if _normalise(n) not in locked) == []


def test_no_forbidden_distribution_is_named_or_locked(
    rows: dict[str, dict[str, Any]], locked: set[str]
) -> None:
    """The five names gen_third_party.py refuses must appear in neither place.

    THE NAMES ARE DECODED FROM THE KEYS, which are held encoded because one of
    the five carries a foreign library name that check-vocabulary.sh matches
    wherever it appears. Comparing the register against the raw keys would
    compare it against base64 and pass over anything.

    Two surfaces, because they fail differently. A forbidden name in the register
    becomes a wrapper docstring's "Reference implementation:" line and points a
    reader at code this project may not build on; a forbidden name in the lockfile
    is the licence conflict itself.
    """
    assert len(FORBIDDEN_DISTRIBUTIONS) == 5, sorted(FORBIDDEN_DISTRIBUTIONS)
    forbidden = set(forbidden_by_normalised_name())
    assert len(forbidden) == 5, sorted(forbidden)
    named = sorted(k for k, r in rows.items()
                   if r["library"] and _normalise(r["library"]) in forbidden)
    assert named == [], named
    assert sorted(forbidden & locked) == []


def test_the_register_counts_the_same_modules_the_wrapper_tree_holds(
    rows: dict[str, dict[str, Any]],
) -> None:
    """MEASURED FROM BOTH SIDES, never one from the other. The register's own
    n_modules is compared against a walk of the wrapper tree and against the
    inventory constant; a register rebuilt from a corpus that had lost a card
    would agree with itself perfectly."""
    register = json.loads(REGISTER.read_bytes().decode("utf-8"))
    on_disk = sorted(
        f"{p.parent.name}/{p.stem}"
        for p in (ENGINE_ROOT / "src/econflow_engine/wrappers").rglob("*.py")
        if p.name != "__init__.py"
    )
    declared = json.loads(INVENTORY.read_bytes().decode("utf-8"))["engine"]["wrappers"]

    assert sorted(rows) == on_disk
    assert register["n_modules"] == len(rows) == len(on_disk) == declared
