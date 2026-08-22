# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 45-causal-discovery-graphs: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'cd_pc': {
        'fn': 'cd_pc',
        'description': 'cd_pc -- category 45-causal-discovery-graphs, method card #374.',
        'args': {'data': 'Observational data.', 'independence_test': 'Conditional independence test.', 'stable': 'Use the order-independent stable variant.', 'max_conditioning_set': 'Largest conditioning set considered.', 'alpha': 'Significance level.'},
        'input_example': {'data': '<df_handle>', 'independence_test': 'fisherz', 'stable': True, 'alpha': 0.05},
    },
    'cd_fci': {
        'fn': 'cd_fci',
        'description': 'cd_fci -- category 45-causal-discovery-graphs, method card #374.',
        'args': {'data': 'Observational data.', 'independence_test': 'Conditional independence test.', 'max_conditioning_set': 'Largest conditioning set considered.', 'alpha': 'Significance level.'},
        'input_example': {'data': '<df_handle>', 'independence_test': 'fisherz', 'alpha': 0.05},
    },
    'cd_ges': {
        'fn': 'cd_ges',
        'description': 'cd_ges -- category 45-causal-discovery-graphs, method card #375.',
        'args': {'data': 'Observational data.', 'score': 'Scoring function.', 'max_parents': 'Maximum parents per node.'},
        'input_example': {'data': '<df_handle>', 'score': 'bic'},
    },
    'cd_exact_search': {
        'fn': 'cd_exact_search',
        'description': 'cd_exact_search -- category 45-causal-discovery-graphs, method card #375.',
        'args': {'data': 'Observational data.', 'score': 'Scoring function.', 'max_parents': 'Maximum parents per node.'},
        'input_example': {'data': '<df_handle>', 'score': 'bic', 'max_parents': 3},
    },
    'cd_lingam': {
        'fn': 'cd_lingam',
        'description': 'cd_lingam -- category 45-causal-discovery-graphs, method card #376.',
        'args': {'data': 'Observational data.', 'variant': 'Algorithm variant.', 'lags': 'Lag order for the time-series variant.', 'nboot': 'Number of bootstrap replications.', 'seed': 'Seed for the random number generator.'},
        'input_example': {'data': '<df_handle>', 'variant': 'direct', 'lags': 1, 'nboot': 0},
    },
    'cd_nongaussianity_check': {
        'fn': 'cd_nongaussianity_check',
        'description': 'cd_nongaussianity_check -- category 45-causal-discovery-graphs, method card #376.',
        'args': {'data': 'Observational data.', 'test': 'Normality test.', 'alpha': 'Significance level.'},
        'input_example': {'data': '<df_handle>', 'test': 'jarque_bera', 'alpha': 0.05},
    },
    'cd_identify_effect': {
        'fn': 'cd_identify_effect',
        'description': 'cd_identify_effect -- category 45-causal-discovery-graphs, method card #377.',
        'args': {'graph': 'Causal graph in DOT or GML form.', 'treatment': 'Treatment variable.', 'outcome': 'Outcome variable.', 'method': 'Identification strategy to attempt.'},
        'input_example': {'graph': '...', 'treatment': '...', 'outcome': '...', 'method': 'auto'},
    },
    'cd_adjustment_sets': {
        'fn': 'cd_adjustment_sets',
        'description': 'cd_adjustment_sets -- category 45-causal-discovery-graphs, method card #377.',
        'args': {'graph': 'Causal graph in DOT or GML form.', 'treatment': 'Treatment variable.', 'outcome': 'Outcome variable.', 'max_sets': 'Maximum sets to return.'},
        'input_example': {'graph': '...', 'treatment': '...', 'outcome': '...', 'max_sets': 10},
    },
    'cd_estimate_effect': {
        'fn': 'cd_estimate_effect',
        'description': 'cd_estimate_effect -- category 45-causal-discovery-graphs, method card #377.',
        'args': {'estimand': 'Handle to a derived estimand.', 'data': 'Data to estimate on.', 'method': 'Estimator.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'estimand': '<raw_handle>', 'data': '<df_handle>', 'method': 'linear_regression', 'conf_level': 0.95},
    },
    'cd_refute': {
        'fn': 'cd_refute',
        'description': 'cd_refute -- category 45-causal-discovery-graphs, method card #378.',
        'args': {'estimand': 'Handle to a derived estimand.', 'data': 'Data the estimate was produced on.', 'refuters': 'Refuters to run; omitted = the standard set.', 'n_simulations': 'Simulations per refuter.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'estimand': '<raw_handle>', 'data': '<df_handle>', 'n_simulations': 100, 'seed': 1},
    },
    'cd_sensitivity_confounder': {
        'fn': 'cd_sensitivity_confounder',
        'description': 'cd_sensitivity_confounder -- category 45-causal-discovery-graphs, method card #378.',
        'args': {'estimand': 'Handle to a derived estimand.', 'data': 'Data the estimate was produced on.', 'effect_strength_treatment': 'Confounder-treatment strengths to scan.', 'effect_strength_outcome': 'Confounder-outcome strengths to scan.'},
        'input_example': {'estimand': '<raw_handle>', 'data': '<df_handle>'},
    },
    'cd_independence_test': {
        'fn': 'cd_independence_test',
        'description': 'cd_independence_test -- category 45-causal-discovery-graphs, method card #379.',
        'args': {'x': 'First variable set.', 'y': 'Second variable set.', 'z': 'Conditioning variable set.', 'test': 'Test to apply.', 'n_permutations': 'Permutations for the null; 0 = asymptotic.', 'seed': 'Seed for the random number generator.', 'alpha': 'Significance level.'},
        'input_example': {'x': '<multiseries_handle>', 'y': '<multiseries_handle>', 'test': 'dcorr', 'n_permutations': 1000, 'alpha': 0.05},
    },
    'cd_distance_correlation': {
        'fn': 'cd_distance_correlation',
        'description': 'cd_distance_correlation -- category 45-causal-discovery-graphs, method card #379.',
        'args': {'x': 'First variable set.', 'y': 'Second variable set.', 'z': 'Variables to partial out.'},
        'input_example': {'x': '<multiseries_handle>', 'y': '<multiseries_handle>'},
    },
}
