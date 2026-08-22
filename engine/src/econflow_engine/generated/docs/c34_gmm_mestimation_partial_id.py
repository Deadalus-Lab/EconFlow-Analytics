# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 34-gmm-mestimation-partial-id: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'gme_fit': {
        'fn': 'gme_fit',
        'description': 'gme_fit -- category 34-gmm-mestimation-partial-id, method card #292.',
        'args': {'data': 'Data the moments are evaluated on.', 'moments': 'Moment-condition specification.', 'instruments': 'Instrument columns.', 'method': 'GMM variant.', 'weighting': 'Weighting matrix.', 'max_iter': 'Maximum iterations for the iterated variant.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<df_handle>', 'moments': 'y ~ x', 'method': 'twostep', 'weighting': 'robust', 'max_iter': 100, 'conf_level': 0.95},
    },
    'gme_j_test': {
        'fn': 'gme_j_test',
        'description': 'gme_j_test -- category 34-gmm-mestimation-partial-id, method card #292.',
        'args': {'fit': 'Handle to a fitted GMM model.', 'alpha': 'Significance level.'},
        'input_example': {'fit': '<raw_handle>', 'alpha': 0.05},
    },
    'gme_weighting_matrix': {
        'fn': 'gme_weighting_matrix',
        'description': 'gme_weighting_matrix -- category 34-gmm-mestimation-partial-id, method card #293.',
        'args': {'moments': 'Evaluated moment conditions, one row per observation.', 'kind': 'Covariance family.', 'kernel': 'HAC kernel.', 'bandwidth': 'Lag truncation; omitted = automatic.', 'cluster': 'Cluster identifier when kind is cluster.'},
        'input_example': {'moments': '<matrix_handle>', 'kind': 'hac', 'kernel': 'bartlett'},
    },
    'gme_c_test': {
        'fn': 'gme_c_test',
        'description': 'gme_c_test -- category 34-gmm-mestimation-partial-id, method card #294.',
        'args': {'fit': 'Handle to a fitted GMM or IV model.', 'subset': 'Instruments whose validity is being tested.', 'alpha': 'Significance level.'},
        'input_example': {'fit': '<raw_handle>', 'subset': ['a', 'b'], 'alpha': 0.05},
    },
    'gme_moment_selection': {
        'fn': 'gme_moment_selection',
        'description': 'gme_moment_selection -- category 34-gmm-mestimation-partial-id, method card #294.',
        'args': {'data': 'Data the moments are evaluated on.', 'moments': 'Moment-condition specification.', 'candidates': 'Candidate instrument columns.', 'criterion': 'Selection criterion.'},
        'input_example': {'data': '<df_handle>', 'moments': 'y ~ x', 'criterion': 'bic'},
    },
    'gme_minimum_distance': {
        'fn': 'gme_minimum_distance',
        'description': 'gme_minimum_distance -- category 34-gmm-mestimation-partial-id, method card #295.',
        'args': {'reduced_form': 'Reduced-form parameter estimates.', 'vcov': 'Covariance of the reduced-form estimates.', 'mapping': 'Structural mapping from parameters to reduced form.', 'weighting': 'Weighting scheme.', 'start': 'Starting values.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'reduced_form': [1.0, 2.0], 'vcov': '<matrix_handle>', 'mapping': 'y ~ x', 'weighting': 'efficient', 'conf_level': 0.95},
    },
    'gme_empirical_likelihood': {
        'fn': 'gme_empirical_likelihood',
        'description': 'gme_empirical_likelihood -- category 34-gmm-mestimation-partial-id, method card #296.',
        'args': {'data': 'Data the moments are evaluated on.', 'moments': 'Moment-condition specification.', 'family': 'GEL family member.', 'max_iter': 'Maximum outer iterations.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<df_handle>', 'moments': 'y ~ x', 'family': 'el', 'max_iter': 100, 'conf_level': 0.95},
    },
    'gme_el_test': {
        'fn': 'gme_el_test',
        'description': 'gme_el_test -- category 34-gmm-mestimation-partial-id, method card #296.',
        'args': {'fit': 'Handle to a fitted empirical-likelihood model.', 'restriction': 'Restriction under the null.', 'alpha': 'Significance level.'},
        'input_example': {'fit': '<raw_handle>', 'restriction': 'y ~ x', 'alpha': 0.05},
    },
    'gme_smm': {
        'fn': 'gme_smm',
        'description': 'gme_smm -- category 34-gmm-mestimation-partial-id, method card #297.',
        'args': {'data': 'Observed data whose moments are matched.', 'simulator': 'Specification of the simulation model.', 'moments': 'Names of the moments to match.', 'n_sim': 'Simulation draws per evaluation.', 'seed': 'Seed for the random number generator; required for reproducibility.', 'weighting': 'Weighting matrix.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<df_handle>', 'simulator': 'y ~ x', 'moments': ['a', 'b'], 'n_sim': 100, 'seed': 1, 'weighting': 'efficient', 'conf_level': 0.95},
    },
    'gme_indirect_inference': {
        'fn': 'gme_indirect_inference',
        'description': 'gme_indirect_inference -- category 34-gmm-mestimation-partial-id, method card #297.',
        'args': {'data': 'Observed data.', 'simulator': 'Specification of the simulation model.', 'auxiliary': 'Auxiliary model whose parameters are matched.', 'n_sim': 'Simulation draws per evaluation.', 'seed': 'Seed for the random number generator; required for reproducibility.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<df_handle>', 'simulator': 'y ~ x', 'auxiliary': 'y ~ x', 'n_sim': 100, 'seed': 1, 'conf_level': 0.95},
    },
    'gme_optimise': {
        'fn': 'gme_optimise',
        'description': 'gme_optimise -- category 34-gmm-mestimation-partial-id, method card #298.',
        'args': {'objective': 'Objective specification.', 'start': 'Starting values.', 'lower': 'Lower bounds.', 'upper': 'Upper bounds.', 'algorithm': 'Optimiser.', 'n_starts': 'Multi-start restarts.', 'seed': 'Seed for the random number generator.'},
        'input_example': {'objective': 'y ~ x', 'start': [1.0, 2.0], 'algorithm': 'lbfgsb', 'n_starts': 1},
    },
    'gme_numerical_derivatives': {
        'fn': 'gme_numerical_derivatives',
        'description': 'gme_numerical_derivatives -- category 34-gmm-mestimation-partial-id, method card #298.',
        'args': {'objective': 'Objective specification.', 'at': 'Point to differentiate at.', 'method': 'Difference scheme.', 'step': 'Step size; omitted = scaled automatically.'},
        'input_example': {'objective': 'y ~ x', 'at': [1.0, 2.0], 'method': 'central'},
    },
    'gme_manski_bounds': {
        'fn': 'gme_manski_bounds',
        'description': 'gme_manski_bounds -- category 34-gmm-mestimation-partial-id, method card #299.',
        'args': {'outcome': 'Observed outcome, missing where unobserved.', 'selection': 'Indicator that the outcome is observed.', 'treatment': 'Treatment indicator for an effect bound.', 'y_min': 'Logical lower bound on the outcome.', 'y_max': 'Logical upper bound on the outcome.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'outcome': '<series_handle>', 'selection': '<series_handle>', 'conf_level': 0.95},
    },
    'gme_lee_bounds': {
        'fn': 'gme_lee_bounds',
        'description': 'gme_lee_bounds -- category 34-gmm-mestimation-partial-id, method card #299.',
        'args': {'outcome': 'Observed outcome.', 'treatment': 'Treatment indicator.', 'selection': 'Indicator that the outcome is observed.', 'covariates': 'Covariates for tightened bounds.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'outcome': '<series_handle>', 'treatment': '<series_handle>', 'selection': '<series_handle>', 'conf_level': 0.95},
    },
    'gme_moment_inequality_set': {
        'fn': 'gme_moment_inequality_set',
        'description': 'gme_moment_inequality_set -- category 34-gmm-mestimation-partial-id, method card #299.',
        'args': {'data': 'Data the inequalities are evaluated on.', 'inequalities': 'Moment-inequality specification.', 'grid': 'Parameter grid to test over.', 'method': 'Critical-value construction.', 'nboot': 'Number of bootstrap replications.', 'seed': 'Seed for the random number generator.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<df_handle>', 'inequalities': 'y ~ x', 'method': 'subsampling', 'nboot': 999, 'conf_level': 0.95},
    },
}
