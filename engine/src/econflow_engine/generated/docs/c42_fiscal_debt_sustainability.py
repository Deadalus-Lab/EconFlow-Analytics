# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 42-fiscal-debt-sustainability: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'fis_debt_decomposition': {
        'fn': 'fis_debt_decomposition',
        'description': 'fis_debt_decomposition -- category 42-fiscal-debt-sustainability, method card #354.',
        'args': {'debt_ratio': 'Debt as a share of output.', 'primary_balance': 'Primary balance as a share of output.', 'interest_rate': 'Effective nominal interest rate.', 'growth_rate': 'Nominal output growth rate.', 'inflation': 'Deflator growth, when a real decomposition is wanted.'},
        'input_example': {'debt_ratio': '<series_handle>', 'primary_balance': '<series_handle>', 'interest_rate': '<series_handle>', 'growth_rate': '<series_handle>'},
    },
    'fis_snowball': {
        'fn': 'fis_snowball',
        'description': 'fis_snowball -- category 42-fiscal-debt-sustainability, method card #354.',
        'args': {'debt_ratio': 'Debt as a share of output.', 'interest_rate': 'Effective nominal interest rate.', 'growth_rate': 'Nominal output growth rate.'},
        'input_example': {'debt_ratio': '<series_handle>', 'interest_rate': '<series_handle>', 'growth_rate': '<series_handle>'},
    },
    'fis_project_debt': {
        'fn': 'fis_project_debt',
        'description': 'fis_project_debt -- category 42-fiscal-debt-sustainability, method card #355.',
        'args': {'debt_ratio_initial': 'Starting debt ratio.', 'primary_balance': 'Assumed primary balance path.', 'interest_rate': 'Assumed effective interest rate path.', 'growth_rate': 'Assumed nominal growth path.', 'horizon': 'Projection horizon in periods.'},
        'input_example': {'debt_ratio_initial': 1.0, 'primary_balance': [1.0, 2.0], 'interest_rate': [1.0, 2.0], 'growth_rate': [1.0, 2.0], 'horizon': 10},
    },
    'fis_stress_scenarios': {
        'fn': 'fis_stress_scenarios',
        'description': 'fis_stress_scenarios -- category 42-fiscal-debt-sustainability, method card #355.',
        'args': {'baseline': 'Handle to a baseline projection.', 'shock_size': 'Shock in historical standard deviations.', 'scenarios': 'Scenarios to run; omitted = the standard set.'},
        'input_example': {'baseline': '<raw_handle>', 'shock_size': 1.0},
    },
    'fis_debt_stabilising_balance': {
        'fn': 'fis_debt_stabilising_balance',
        'description': 'fis_debt_stabilising_balance -- category 42-fiscal-debt-sustainability, method card #355.',
        'args': {'debt_ratio': 'Current debt ratio.', 'interest_rate': 'Effective interest rate.', 'growth_rate': 'Nominal growth rate.'},
        'input_example': {'debt_ratio': 1.0, 'interest_rate': 1.0, 'growth_rate': 1.0},
    },
    'fis_debt_fan_chart': {
        'fn': 'fis_debt_fan_chart',
        'description': 'fis_debt_fan_chart -- category 42-fiscal-debt-sustainability, method card #356.',
        'args': {'debt_ratio_initial': 'Starting debt ratio.', 'history': 'Historical growth, interest rate and primary balance.', 'horizon': 'Projection horizon in periods.', 'n_simulations': 'Simulation draws.', 'method': 'Shock generation.', 'quantiles': 'Fan quantiles.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'debt_ratio_initial': 1.0, 'history': '<df_handle>', 'horizon': 10, 'n_simulations': 10000, 'method': 'bootstrap', 'quantiles': [0.1, 0.25, 0.5, 0.75, 0.9], 'seed': 1},
    },
    'fis_threshold_probability': {
        'fn': 'fis_threshold_probability',
        'description': 'fis_threshold_probability -- category 42-fiscal-debt-sustainability, method card #356.',
        'args': {'fan': 'Handle to a stochastic projection.', 'threshold': 'Debt ratio threshold.'},
        'input_example': {'fan': '<raw_handle>', 'threshold': 1.0},
    },
    'fis_reaction_function': {
        'fn': 'fis_reaction_function',
        'description': 'fis_reaction_function -- category 42-fiscal-debt-sustainability, method card #357.',
        'args': {'primary_balance': 'Primary balance as a share of output.', 'debt_ratio': 'Lagged debt ratio.', 'output_gap': 'Output gap.', 'controls': 'Additional control columns.', 'cov_type': 'Covariance estimator.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'primary_balance': '<series_handle>', 'debt_ratio': '<series_handle>', 'cov_type': 'hac', 'conf_level': 0.95},
    },
    'fis_reaction_nonlinear': {
        'fn': 'fis_reaction_nonlinear',
        'description': 'fis_reaction_nonlinear -- category 42-fiscal-debt-sustainability, method card #357.',
        'args': {'primary_balance': 'Primary balance as a share of output.', 'debt_ratio': 'Lagged debt ratio.', 'output_gap': 'Output gap.', 'model': 'Nonlinear form.', 'n_regimes': 'Regimes for the switching form.', 'seed': 'Seed for the random number generator.'},
        'input_example': {'primary_balance': '<series_handle>', 'debt_ratio': '<series_handle>', 'model': 'threshold', 'n_regimes': 2},
    },
    'fis_multiplier_lp': {
        'fn': 'fis_multiplier_lp',
        'description': 'fis_multiplier_lp -- category 42-fiscal-debt-sustainability, method card #358.',
        'args': {'output': 'Output series.', 'fiscal': 'Fiscal shock or instrument.', 'controls': 'Control columns.', 'horizons': 'Maximum horizon.', 'lags': 'Lags of the controls included.', 'cumulative': 'Report the cumulative multiplier.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'output': '<series_handle>', 'fiscal': '<series_handle>', 'horizons': 20, 'lags': 4, 'cumulative': True, 'conf_level': 0.95},
    },
    'fis_multiplier_state_dependent': {
        'fn': 'fis_multiplier_state_dependent',
        'description': 'fis_multiplier_state_dependent -- category 42-fiscal-debt-sustainability, method card #358.',
        'args': {'output': 'Output series.', 'fiscal': 'Fiscal shock or instrument.', 'state': 'State variable, such as the output gap.', 'transition': 'How the state enters.', 'horizons': 'Maximum horizon.', 'lags': 'Lags of the controls included.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'output': '<series_handle>', 'fiscal': '<series_handle>', 'state': '<series_handle>', 'transition': 'smooth', 'horizons': 20, 'lags': 4, 'conf_level': 0.95},
    },
    'fis_cyclically_adjusted': {
        'fn': 'fis_cyclically_adjusted',
        'description': 'fis_cyclically_adjusted -- category 42-fiscal-debt-sustainability, method card #359.',
        'args': {'balance': 'Headline balance as a share of output.', 'output_gap': 'Output gap as a share of potential.', 'elasticity': 'Budget semi-elasticity to the gap.', 'one_offs': 'One-off measures to remove for the structural balance.'},
        'input_example': {'balance': '<series_handle>', 'output_gap': '<series_handle>', 'elasticity': 0.5},
    },
    'fis_budget_elasticity': {
        'fn': 'fis_budget_elasticity',
        'description': 'fis_budget_elasticity -- category 42-fiscal-debt-sustainability, method card #359.',
        'args': {'revenue': 'Revenue as a share of output.', 'expenditure': 'Expenditure as a share of output.', 'output_gap': 'Output gap.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'revenue': '<series_handle>', 'expenditure': '<series_handle>', 'output_gap': '<series_handle>', 'conf_level': 0.95},
    },
    'fis_rule_compliance': {
        'fn': 'fis_rule_compliance',
        'description': 'fis_rule_compliance -- category 42-fiscal-debt-sustainability, method card #360.',
        'args': {'debt_ratio': 'Projected debt ratio.', 'structural_balance': 'Projected structural balance.', 'expenditure_growth': 'Projected expenditure growth.', 'debt_limit': 'Debt ratio limit.', 'deficit_limit': 'Headline deficit limit.', 'mto': 'Medium-term structural balance objective.'},
        'input_example': {'debt_ratio': '<series_handle>', 'debt_limit': 0.6, 'deficit_limit': 0.03},
    },
    'fis_adjustment_path': {
        'fn': 'fis_adjustment_path',
        'description': 'fis_adjustment_path -- category 42-fiscal-debt-sustainability, method card #360.',
        'args': {'debt_ratio_initial': 'Starting debt ratio.', 'target': 'Target debt ratio.', 'horizon': 'Years to reach the target.', 'interest_rate': 'Effective interest rate.', 'growth_rate': 'Nominal growth rate.', 'multiplier': 'Fiscal multiplier applied to the consolidation.'},
        'input_example': {'debt_ratio_initial': 1.0, 'target': 1.0, 'horizon': 10, 'interest_rate': 1.0, 'growth_rate': 1.0, 'multiplier': 0.0},
    },
}
