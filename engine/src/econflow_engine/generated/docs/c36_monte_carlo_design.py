# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 36-monte-carlo-design: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'mc_simulate_arma': {
        'fn': 'mc_simulate_arma',
        'description': 'mc_simulate_arma -- category 36-monte-carlo-design, method card #309.',
        'args': {'n': 'Observations to generate.', 'ar': 'Autoregressive coefficients.', 'ma': 'Moving-average coefficients.', 'd': 'Order of integration.', 'sigma': 'Innovation standard deviation.', 'burnin': 'Discarded initial observations.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'n': 1, 'd': 0, 'sigma': 1.0, 'burnin': 500, 'seed': 1},
    },
    'mc_simulate_var': {
        'fn': 'mc_simulate_var',
        'description': 'mc_simulate_var -- category 36-monte-carlo-design, method card #309.',
        'args': {'n': 'Observations to generate.', 'coefs': 'Stacked coefficient matrices.', 'sigma': 'Innovation covariance.', 'burnin': 'Discarded initial observations.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'n': 1, 'coefs': '<matrix_handle>', 'sigma': '<matrix_handle>', 'burnin': 500, 'seed': 1},
    },
    'mc_simulate_garch': {
        'fn': 'mc_simulate_garch',
        'description': 'mc_simulate_garch -- category 36-monte-carlo-design, method card #309.',
        'args': {'n': 'Observations to generate.', 'omega': 'Variance intercept.', 'alpha': 'ARCH coefficients.', 'beta': 'GARCH coefficients.', 'distribution': 'Innovation distribution.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'n': 1, 'omega': 1.0, 'alpha': [1.0, 2.0], 'beta': [1.0, 2.0], 'distribution': 'normal', 'seed': 1},
    },
    'mc_simulate_panel': {
        'fn': 'mc_simulate_panel',
        'description': 'mc_simulate_panel -- category 36-monte-carlo-design, method card #309.',
        'args': {'n_units': 'Number of units.', 'n_periods': 'Periods per unit.', 'beta': 'Slope coefficients.', 'unit_sd': 'Standard deviation of unit effects.', 'time_sd': 'Standard deviation of time effects.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'n_units': 1, 'n_periods': 1, 'beta': [1.0, 2.0], 'unit_sd': 1.0, 'time_sd': 0.5, 'seed': 1},
    },
    'mc_size_study': {
        'fn': 'mc_size_study',
        'description': 'mc_size_study -- category 36-monte-carlo-design, method card #310.',
        'args': {'dgp': 'Data-generating process under the null.', 'test': 'Test to apply.', 'n_replications': 'Monte Carlo replications.', 'sample_sizes': 'Sample sizes to scan.', 'seed': 'Seed for the random number generator; required for reproducibility.', 'alpha': 'Significance level.'},
        'input_example': {'dgp': 'y ~ x', 'test': 'y ~ x', 'n_replications': 1000, 'sample_sizes': [50, 100, 250, 500], 'seed': 1, 'alpha': 0.05},
    },
    'mc_power_study': {
        'fn': 'mc_power_study',
        'description': 'mc_power_study -- category 36-monte-carlo-design, method card #310.',
        'args': {'dgp': 'Data-generating process under the alternative.', 'test': 'Test to apply.', 'effect_grid': 'Alternative values to scan.', 'n_replications': 'Monte Carlo replications.', 'size_correct': 'Report power at the empirical critical value.', 'seed': 'Seed for the random number generator; required for reproducibility.', 'alpha': 'Significance level.'},
        'input_example': {'dgp': 'y ~ x', 'test': 'y ~ x', 'effect_grid': [1.0, 2.0], 'n_replications': 1000, 'size_correct': True, 'seed': 1, 'alpha': 0.05},
    },
    'mc_coverage_study': {
        'fn': 'mc_coverage_study',
        'description': 'mc_coverage_study -- category 36-monte-carlo-design, method card #311.',
        'args': {'dgp': 'Data-generating process with a known truth.', 'procedure': 'Interval procedure to assess.', 'levels': 'Nominal levels to check.', 'n_replications': 'Monte Carlo replications.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'dgp': 'y ~ x', 'procedure': 'y ~ x', 'levels': [0.8, 0.9, 0.95], 'n_replications': 1000, 'seed': 1},
    },
    'mc_pit': {
        'fn': 'mc_pit',
        'description': 'mc_pit -- category 36-monte-carlo-design, method card #311.',
        'args': {'observed': 'Realised outcomes.', 'predictive_cdf': 'Predictive CDF evaluated at the outcomes.', 'test': 'Uniformity test.'},
        'input_example': {'observed': '<series_handle>', 'predictive_cdf': '<matrix_handle>', 'test': 'ks'},
    },
    'mc_sobol': {
        'fn': 'mc_sobol',
        'description': 'mc_sobol -- category 36-monte-carlo-design, method card #312.',
        'args': {'problem': 'Input definition: names and bounds.', 'outputs': 'Model outputs at the generated design.', 'n_samples': 'Base sample size.', 'calc_second_order': 'Also compute second-order indices.', 'seed': 'Seed for the random number generator; required for reproducibility.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'problem': '<df_handle>', 'outputs': '<series_handle>', 'n_samples': 1024, 'calc_second_order': False, 'seed': 1, 'conf_level': 0.95},
    },
    'mc_morris': {
        'fn': 'mc_morris',
        'description': 'mc_morris -- category 36-monte-carlo-design, method card #312.',
        'args': {'problem': 'Input definition: names and bounds.', 'outputs': 'Model outputs at the generated design.', 'n_trajectories': 'Number of trajectories.', 'levels': 'Grid levels per input.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'problem': '<df_handle>', 'outputs': '<series_handle>', 'n_trajectories': 100, 'levels': 4, 'seed': 1},
    },
    'mc_sample_design': {
        'fn': 'mc_sample_design',
        'description': 'mc_sample_design -- category 36-monte-carlo-design, method card #312.',
        'args': {'problem': 'Input definition: names and bounds.', 'method': 'Sampling scheme required by the analysis.', 'n_samples': 'Base sample size.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'problem': '<df_handle>', 'method': 'sobol', 'n_samples': 1024, 'seed': 1},
    },
    'mc_design_generate': {
        'fn': 'mc_design_generate',
        'description': 'mc_design_generate -- category 36-monte-carlo-design, method card #313.',
        'args': {'n_factors': 'Number of factors.', 'design': 'Design family.', 'n_samples': 'Runs for the sampling designs.', 'levels': 'Levels per factor for factorial designs.', 'criterion': 'Optimality criterion for Latin hypercube.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'n_factors': 1, 'design': 'lhs', 'n_samples': 100, 'criterion': 'maximin', 'seed': 1},
    },
    'mc_power': {
        'fn': 'mc_power',
        'description': 'mc_power -- category 36-monte-carlo-design, method card #314.',
        'args': {'solve_for': 'Quantity to solve for.', 'effect_size': 'Standardised effect size.', 'n': 'Sample size per arm.', 'power': 'Target power.', 'ratio': 'Allocation ratio between arms.', 'alpha': 'Significance level.'},
        'input_example': {'solve_for': 'n', 'power': 0.8, 'ratio': 1.0, 'alpha': 0.05},
    },
    'mc_power_cluster': {
        'fn': 'mc_power_cluster',
        'description': 'mc_power_cluster -- category 36-monte-carlo-design, method card #314.',
        'args': {'n_clusters': 'Number of clusters.', 'cluster_size': 'Units per cluster.', 'icc': 'Intra-cluster correlation.', 'effect_size': 'Standardised effect size.', 'power': 'Target power.', 'solve_for': 'Quantity to solve for.', 'alpha': 'Significance level.'},
        'input_example': {'cluster_size': 1, 'icc': 1.0, 'power': 0.8, 'solve_for': 'n_clusters', 'alpha': 0.05},
    },
    'mc_qmc_sample': {
        'fn': 'mc_qmc_sample',
        'description': 'mc_qmc_sample -- category 36-monte-carlo-design, method card #315.',
        'args': {'n_dimensions': 'Dimension of the sample.', 'n_samples': 'Number of points.', 'sequence': 'Sequence family.', 'scramble': 'Randomise the sequence to permit an error estimate.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'n_dimensions': 1, 'n_samples': 1, 'sequence': 'sobol', 'scramble': True, 'seed': 1},
    },
    'mc_discrepancy': {
        'fn': 'mc_discrepancy',
        'description': 'mc_discrepancy -- category 36-monte-carlo-design, method card #315.',
        'args': {'sample': 'Point set to assess.', 'method': 'Discrepancy measure.'},
        'input_example': {'sample': '<matrix_handle>', 'method': 'cd'},
    },
}
