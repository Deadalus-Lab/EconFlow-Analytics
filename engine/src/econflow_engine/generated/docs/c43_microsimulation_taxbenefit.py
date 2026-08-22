# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 43-microsimulation-taxbenefit: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'tb_compute': {
        'fn': 'tb_compute',
        'description': 'tb_compute -- category 43-microsimulation-taxbenefit, method card #361.',
        'args': {'population': 'Household microdata.', 'variables': 'Variables to compute.', 'period': 'Period the calculation refers to.', 'country': 'Rule set to apply.'},
        'input_example': {'population': '<df_handle>', 'variables': ['a', 'b'], 'period': '...', 'country': 'generic'},
    },
    'tb_reform': {
        'fn': 'tb_reform',
        'description': 'tb_reform -- category 43-microsimulation-taxbenefit, method card #361.',
        'args': {'simulation': 'Handle to a baseline simulation.', 'reform': 'Parameter changes defining the reform.', 'variables': 'Variables to compare.'},
        'input_example': {'simulation': '<raw_handle>', 'reform': '<df_handle>', 'variables': ['a', 'b']},
    },
    'tb_parameters': {
        'fn': 'tb_parameters',
        'description': 'tb_parameters -- category 43-microsimulation-taxbenefit, method card #361.',
        'args': {'period': 'Date to read the parameters at.', 'path': 'Parameter subtree to return.'},
        'input_example': {'period': '...'},
    },
    'tb_disposable_income': {
        'fn': 'tb_disposable_income',
        'description': 'tb_disposable_income -- category 43-microsimulation-taxbenefit, method card #362.',
        'args': {'population': 'Household microdata.', 'period': 'Period the calculation refers to.', 'include_housing': 'Net off housing costs.'},
        'input_example': {'population': '<df_handle>', 'period': '...', 'include_housing': False},
    },
    'tb_budget_constraint': {
        'fn': 'tb_budget_constraint',
        'description': 'tb_budget_constraint -- category 43-microsimulation-taxbenefit, method card #362.',
        'args': {'household': 'A single household specification.', 'earnings_grid': 'Earnings values to evaluate.', 'period': 'Period the calculation refers to.'},
        'input_example': {'household': '<df_handle>', 'earnings_grid': [1.0, 2.0], 'period': '...'},
    },
    'tb_metr': {
        'fn': 'tb_metr',
        'description': 'tb_metr -- category 43-microsimulation-taxbenefit, method card #363.',
        'args': {'population': 'Household microdata.', 'period': 'Period the calculation refers to.', 'increment': 'Earnings increment used for the derivative.'},
        'input_example': {'population': '<df_handle>', 'period': '...', 'increment': 100.0},
    },
    'tb_participation_tax_rate': {
        'fn': 'tb_participation_tax_rate',
        'description': 'tb_participation_tax_rate -- category 43-microsimulation-taxbenefit, method card #363.',
        'args': {'population': 'Household microdata.', 'period': 'Period the calculation refers to.', 'transition': 'Transition modelled.'},
        'input_example': {'population': '<df_handle>', 'period': '...', 'transition': 'zero_to_full'},
    },
    'tb_distributional_impact': {
        'fn': 'tb_distributional_impact',
        'description': 'tb_distributional_impact -- category 43-microsimulation-taxbenefit, method card #364.',
        'args': {'baseline': 'Handle to a baseline simulation.', 'reform': 'Handle to a reform simulation.', 'weights': 'Survey weights.', 'equivalence_scale': 'Equivalence scale for ranking.', 'n_groups': 'Number of income groups.'},
        'input_example': {'baseline': '<raw_handle>', 'reform': '<raw_handle>', 'equivalence_scale': 'oecd_modified', 'n_groups': 10},
    },
    'tb_labour_supply': {
        'fn': 'tb_labour_supply',
        'description': 'tb_labour_supply -- category 43-microsimulation-taxbenefit, method card #365.',
        'args': {'baseline': 'Handle to a baseline simulation.', 'reform': 'Handle to a reform simulation.', 'intensive_elasticity': 'Hours elasticity to the net wage.', 'extensive_elasticity': 'Participation elasticity.', 'by_group': 'Columns defining groups with distinct elasticities.'},
        'input_example': {'baseline': '<raw_handle>', 'reform': '<raw_handle>', 'intensive_elasticity': 0.2, 'extensive_elasticity': 0.3},
    },
    'tb_reweight': {
        'fn': 'tb_reweight',
        'description': 'tb_reweight -- category 43-microsimulation-taxbenefit, method card #366.',
        'args': {'data': 'Survey microdata.', 'weights': 'Column holding the design weights.', 'targets': 'Control totals to match.', 'method': 'Calibration method.', 'bounds': 'Lower and upper bounds on the weight ratio.', 'max_iter': 'Maximum iterations.'},
        'input_example': {'data': '<df_handle>', 'weights': '...', 'targets': '<df_handle>', 'method': 'raking', 'bounds': [0.2, 5.0], 'max_iter': 100},
    },
}
