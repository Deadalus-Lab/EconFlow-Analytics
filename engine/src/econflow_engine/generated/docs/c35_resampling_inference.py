# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 35-resampling-inference: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'rs_bootstrap_iid': {
        'fn': 'rs_bootstrap_iid',
        'description': 'rs_bootstrap_iid -- category 35-resampling-inference, method card #300.',
        'args': {'data': 'Data to resample.', 'statistic': 'Statistic to bootstrap.', 'nboot': 'Number of bootstrap replications.', 'method': 'Interval construction.', 'seed': 'Seed for the random number generator; required for reproducibility.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<df_handle>', 'statistic': 'y ~ x', 'nboot': 999, 'method': 'bca', 'seed': 1, 'conf_level': 0.95},
    },
    'rs_bootstrap_residual': {
        'fn': 'rs_bootstrap_residual',
        'description': 'rs_bootstrap_residual -- category 35-resampling-inference, method card #300.',
        'args': {'fit': 'Handle to a fitted regression.', 'nboot': 'Number of bootstrap replications.', 'wild': 'Use wild rather than iid residual resampling.', 'seed': 'Seed for the random number generator; required for reproducibility.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'fit': '<raw_handle>', 'nboot': 999, 'wild': False, 'seed': 1, 'conf_level': 0.95},
    },
    'rs_block_bootstrap': {
        'fn': 'rs_block_bootstrap',
        'description': 'rs_block_bootstrap -- category 35-resampling-inference, method card #301.',
        'args': {'data': 'Serially dependent data.', 'statistic': 'Statistic to bootstrap.', 'block_length': 'Block length; omitted = automatic.', 'circular': 'Wrap the series to remove end effects.', 'nboot': 'Number of bootstrap replications.', 'seed': 'Seed for the random number generator; required for reproducibility.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<multiseries_handle>', 'statistic': 'y ~ x', 'circular': True, 'nboot': 999, 'seed': 1, 'conf_level': 0.95},
    },
    'rs_optimal_block_length': {
        'fn': 'rs_optimal_block_length',
        'description': 'rs_optimal_block_length -- category 35-resampling-inference, method card #301.',
        'args': {'x': 'Series whose dependence sets the block length.'},
        'input_example': {'x': '<series_handle>'},
    },
    'rs_stationary_bootstrap': {
        'fn': 'rs_stationary_bootstrap',
        'description': 'rs_stationary_bootstrap -- category 35-resampling-inference, method card #302.',
        'args': {'data': 'Serially dependent data.', 'statistic': 'Statistic to bootstrap.', 'expected_block_length': 'Mean block length; omitted = automatic.', 'nboot': 'Number of bootstrap replications.', 'seed': 'Seed for the random number generator; required for reproducibility.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<multiseries_handle>', 'statistic': 'y ~ x', 'nboot': 999, 'seed': 1, 'conf_level': 0.95},
    },
    'rs_sieve_bootstrap': {
        'fn': 'rs_sieve_bootstrap',
        'description': 'rs_sieve_bootstrap -- category 35-resampling-inference, method card #303.',
        'args': {'x': 'Serially dependent series.', 'statistic': 'Statistic to bootstrap.', 'ar_order': 'Autoregressive order; omitted = selected.', 'criterion': 'Order-selection criterion.', 'nboot': 'Number of bootstrap replications.', 'seed': 'Seed for the random number generator; required for reproducibility.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'x': '<series_handle>', 'statistic': 'y ~ x', 'criterion': 'aic', 'nboot': 999, 'seed': 1, 'conf_level': 0.95},
    },
    'rs_wild_bootstrap': {
        'fn': 'rs_wild_bootstrap',
        'description': 'rs_wild_bootstrap -- category 35-resampling-inference, method card #304.',
        'args': {'fit': 'Handle to a fitted regression.', 'restriction': 'Restriction tested under the null.', 'weights': 'Auxiliary weight distribution.', 'impose_null': 'Impose the null when resampling.', 'nboot': 'Number of bootstrap replications.', 'seed': 'Seed for the random number generator; required for reproducibility.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'fit': '<raw_handle>', 'restriction': 'y ~ x', 'weights': 'rademacher', 'impose_null': True, 'nboot': 999, 'seed': 1, 'conf_level': 0.95},
    },
    'rs_wild_cluster_bootstrap': {
        'fn': 'rs_wild_cluster_bootstrap',
        'description': 'rs_wild_cluster_bootstrap -- category 35-resampling-inference, method card #305.',
        'args': {'fit': 'Handle to a fitted regression.', 'cluster': 'Cluster identifier.', 'restriction': 'Restriction tested under the null.', 'weights': 'Auxiliary weight distribution.', 'nboot': 'Number of bootstrap replications.', 'seed': 'Seed for the random number generator; required for reproducibility.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'fit': '<raw_handle>', 'cluster': '<series_handle>', 'restriction': 'y ~ x', 'weights': 'webb', 'nboot': 999, 'seed': 1, 'conf_level': 0.95},
    },
    'rs_permutation_test': {
        'fn': 'rs_permutation_test',
        'description': 'rs_permutation_test -- category 35-resampling-inference, method card #306.',
        'args': {'outcome': 'Outcome per unit.', 'treatment': 'Treatment assignment.', 'block': 'Blocking variable the randomisation respected.', 'cluster': 'Cluster the randomisation was applied at.', 'statistic': 'Test statistic.', 'n_permutations': 'Sampled permutations; 0 = exhaustive.', 'seed': 'Seed for the random number generator; required for reproducibility.', 'alpha': 'Significance level.'},
        'input_example': {'outcome': '<series_handle>', 'treatment': '<series_handle>', 'statistic': 'mean_difference', 'n_permutations': 10000, 'seed': 1, 'alpha': 0.05},
    },
    'rs_randomisation_ci': {
        'fn': 'rs_randomisation_ci',
        'description': 'rs_randomisation_ci -- category 35-resampling-inference, method card #306.',
        'args': {'outcome': 'Outcome per unit.', 'treatment': 'Treatment assignment.', 'grid': 'Effect grid to invert over.', 'n_permutations': 'Sampled permutations.', 'seed': 'Seed for the random number generator; required for reproducibility.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'outcome': '<series_handle>', 'treatment': '<series_handle>', 'n_permutations': 1000, 'seed': 1, 'conf_level': 0.95},
    },
    'rs_subsampling': {
        'fn': 'rs_subsampling',
        'description': 'rs_subsampling -- category 35-resampling-inference, method card #307.',
        'args': {'data': 'Data to subsample.', 'statistic': 'Statistic of interest.', 'subsample_size': 'Subsample size b; omitted = n^(2/3).', 'n_subsamples': 'Number of subsamples.', 'seed': 'Seed for the random number generator; required for reproducibility.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<df_handle>', 'statistic': 'y ~ x', 'n_subsamples': 1000, 'seed': 1, 'conf_level': 0.95},
    },
    'rs_jackknife': {
        'fn': 'rs_jackknife',
        'description': 'rs_jackknife -- category 35-resampling-inference, method card #307.',
        'args': {'data': 'Data to resample.', 'statistic': 'Statistic of interest.', 'kind': 'Jackknife variant.', 'd': 'Number deleted for the delete-d variant.', 'cluster': 'Cluster identifier for the cluster variant.'},
        'input_example': {'data': '<df_handle>', 'statistic': 'y ~ x', 'kind': 'delete1', 'd': 1},
    },
    'rs_multiple_testing': {
        'fn': 'rs_multiple_testing',
        'description': 'rs_multiple_testing -- category 35-resampling-inference, method card #308.',
        'args': {'p_values': 'Unadjusted p-values.', 'method': 'Adjustment procedure.', 'alpha': 'Significance level.'},
        'input_example': {'p_values': [1.0, 2.0], 'method': 'holm', 'alpha': 0.05},
    },
    'rs_romano_wolf': {
        'fn': 'rs_romano_wolf',
        'description': 'rs_romano_wolf -- category 35-resampling-inference, method card #308.',
        'args': {'statistics': 'Test statistics.', 'bootstrap_draws': 'Bootstrap draws of the statistics under the null.', 'alpha': 'Significance level.'},
        'input_example': {'statistics': [1.0, 2.0], 'bootstrap_draws': '<matrix_handle>', 'alpha': 0.05},
    },
}
