# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 31-discrete-choice-demand: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'dcd_blp_problem': {
        'fn': 'dcd_blp_problem',
        'description': 'dcd_blp_problem -- category 31-discrete-choice-demand, method card #266.',
        'args': {'product_data': 'One row per product per market: shares, prices, characteristics.', 'market_ids': 'Column identifying the market.', 'shares': 'Column holding observed market shares.', 'prices': 'Column holding prices.', 'characteristics': 'Product characteristic columns entering utility linearly.', 'random_coefficients': 'Characteristics carrying a random coefficient.', 'instruments': 'Excluded instrument columns.'},
        'input_example': {'product_data': '<df_handle>', 'market_ids': '...', 'shares': '...', 'prices': '...'},
    },
    'dcd_blp_solve': {
        'fn': 'dcd_blp_solve',
        'description': 'dcd_blp_solve -- category 31-discrete-choice-demand, method card #266.',
        'args': {'problem': 'Handle to an assembled BLP problem.', 'sigma_init': 'Starting values for the random-coefficient dispersion.', 'inner_tol': 'Contraction tolerance for the share inversion.', 'outer_tol': 'Convergence tolerance for the outer GMM search.', 'method': 'One-step or two-step GMM.'},
        'input_example': {'problem': '<raw_handle>', 'inner_tol': 1e-14, 'outer_tol': 1e-08, 'method': '2s'},
    },
    'dcd_blp_shares': {
        'fn': 'dcd_blp_shares',
        'description': 'dcd_blp_shares -- category 31-discrete-choice-demand, method card #266.',
        'args': {'results': 'Handle to fitted BLP results.', 'prices': 'Counterfactual prices; omitted = observed.'},
        'input_example': {'results': '<raw_handle>'},
    },
    'dcd_blp_instruments': {
        'fn': 'dcd_blp_instruments',
        'description': 'dcd_blp_instruments -- category 31-discrete-choice-demand, method card #267.',
        'args': {'product_data': 'Product-by-market table.', 'market_ids': 'Column identifying the market.', 'characteristics': 'Characteristic columns the instruments are built from.', 'kind': 'Instrument family.'},
        'input_example': {'product_data': '<df_handle>', 'market_ids': '...', 'kind': 'differentiation'},
    },
    'dcd_optimal_instruments': {
        'fn': 'dcd_optimal_instruments',
        'description': 'dcd_optimal_instruments -- category 31-discrete-choice-demand, method card #267.',
        'args': {'results': 'Handle to consistent first-stage BLP results.', 'method': 'How the expectation is approximated.', 'seed': 'Seed for the random number generator.'},
        'input_example': {'results': '<raw_handle>', 'method': 'approximate'},
    },
    'dcd_elasticities': {
        'fn': 'dcd_elasticities',
        'description': 'dcd_elasticities -- category 31-discrete-choice-demand, method card #268.',
        'args': {'results': 'Handle to fitted demand results.', 'market_id': 'Restrict to one market; omitted = every market.', 'variable': 'Characteristic to differentiate with respect to.'},
        'input_example': {'results': '<raw_handle>', 'variable': 'prices'},
    },
    'dcd_diversion': {
        'fn': 'dcd_diversion',
        'description': 'dcd_diversion -- category 31-discrete-choice-demand, method card #268.',
        'args': {'results': 'Handle to fitted demand results.', 'market_id': 'Restrict to one market.', 'include_outside': 'Include the outside good as a destination.'},
        'input_example': {'results': '<raw_handle>', 'include_outside': True},
    },
    'dcd_markups': {
        'fn': 'dcd_markups',
        'description': 'dcd_markups -- category 31-discrete-choice-demand, method card #268.',
        'args': {'results': 'Handle to fitted demand results.', 'conduct': 'Assumed firm conduct.', 'ownership': 'Ownership matrix; omitted = single-product firms.'},
        'input_example': {'results': '<raw_handle>', 'conduct': 'bertrand'},
    },
    'dcd_merger_simulate': {
        'fn': 'dcd_merger_simulate',
        'description': 'dcd_merger_simulate -- category 31-discrete-choice-demand, method card #269.',
        'args': {'results': 'Handle to fitted demand results.', 'ownership_post': 'Post-merger ownership matrix.', 'cost_change': 'Proportional marginal-cost change per product.', 'tol': 'Fixed-point tolerance.', 'max_iter': 'Maximum fixed-point iterations.'},
        'input_example': {'results': '<raw_handle>', 'ownership_post': '<matrix_handle>', 'tol': 1e-12, 'max_iter': 1000},
    },
    'dcd_upp': {
        'fn': 'dcd_upp',
        'description': 'dcd_upp -- category 31-discrete-choice-demand, method card #269.',
        'args': {'results': 'Handle to fitted demand results.', 'merging': 'Product identifiers of the merging parties.', 'efficiency': 'Assumed proportional marginal-cost saving.'},
        'input_example': {'results': '<raw_handle>', 'merging': ['a', 'b'], 'efficiency': 0.0},
    },
    'dcd_welfare_change': {
        'fn': 'dcd_welfare_change',
        'description': 'dcd_welfare_change -- category 31-discrete-choice-demand, method card #269.',
        'args': {'results': 'Handle to fitted demand results.', 'prices_post': 'Counterfactual price vector.'},
        'input_example': {'results': '<raw_handle>', 'prices_post': '<series_handle>'},
    },
    'dcd_nested_logit_fit': {
        'fn': 'dcd_nested_logit_fit',
        'description': 'dcd_nested_logit_fit -- category 31-discrete-choice-demand, method card #270.',
        'args': {'product_data': 'Product-by-market table.', 'market_ids': 'Column identifying the market.', 'shares': 'Column holding observed shares.', 'nesting_ids': 'Column assigning each product to a nest.', 'characteristics': 'Characteristic columns.', 'instruments': 'Excluded instruments for price and the within-nest share.'},
        'input_example': {'product_data': '<df_handle>', 'market_ids': '...', 'shares': '...', 'nesting_ids': '...'},
    },
    'dcd_nested_logit_elasticities': {
        'fn': 'dcd_nested_logit_elasticities',
        'description': 'dcd_nested_logit_elasticities -- category 31-discrete-choice-demand, method card #270.',
        'args': {'results': 'Handle to fitted nested-logit results.', 'market_id': 'Restrict to one market.'},
        'input_example': {'results': '<raw_handle>'},
    },
    'dcd_mnlogit_fit': {
        'fn': 'dcd_mnlogit_fit',
        'description': 'dcd_mnlogit_fit -- category 31-discrete-choice-demand, method card #271.',
        'args': {'data': 'One row per chooser.', 'choice': 'Column holding the chosen alternative.', 'covariates': 'Chooser-varying covariate columns.', 'base': 'Base alternative; omitted = the first observed.'},
        'input_example': {'data': '<df_handle>', 'choice': '...'},
    },
    'dcd_clogit_fit': {
        'fn': 'dcd_clogit_fit',
        'description': 'dcd_clogit_fit -- category 31-discrete-choice-demand, method card #271.',
        'args': {'data': 'One row per chooser per alternative.', 'chooser': 'Column identifying the chooser.', 'chosen': 'Column flagging the chosen row.', 'covariates': 'Alternative-varying covariate columns.'},
        'input_example': {'data': '<df_handle>', 'chooser': '...', 'chosen': '...'},
    },
    'dcd_iia_test': {
        'fn': 'dcd_iia_test',
        'description': 'dcd_iia_test -- category 31-discrete-choice-demand, method card #271.',
        'args': {'fit': 'Handle to a fitted multinomial or conditional logit.', 'drop': 'Alternatives removed to form the restricted model.'},
        'input_example': {'fit': '<raw_handle>', 'drop': ['a', 'b']},
    },
    'dcd_mixed_logit_fit': {
        'fn': 'dcd_mixed_logit_fit',
        'description': 'dcd_mixed_logit_fit -- category 31-discrete-choice-demand, method card #272.',
        'args': {'data': 'Long-format choice data: one row per chooser per alternative.', 'chooser': 'Column identifying the chooser.', 'chosen': 'Column flagging the chosen row.', 'covariates': 'Covariate columns.', 'random': 'Covariates carrying a random coefficient.', 'distributions': 'Mixing distribution per random coefficient.', 'n_draws': 'Number of simulation draws.', 'panel': 'Column identifying the panel unit when choices repeat.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'data': '<df_handle>', 'chooser': '...', 'chosen': '...', 'n_draws': 600, 'seed': 1},
    },
    'dcd_mixed_logit_individual': {
        'fn': 'dcd_mixed_logit_individual',
        'description': 'dcd_mixed_logit_individual -- category 31-discrete-choice-demand, method card #272.',
        'args': {'fit': 'Handle to a fitted mixed logit.'},
        'input_example': {'fit': '<raw_handle>'},
    },
    'dcd_wtp': {
        'fn': 'dcd_wtp',
        'description': 'dcd_wtp -- category 31-discrete-choice-demand, method card #273.',
        'args': {'results': 'Handle to fitted demand results.', 'price_variable': 'Name of the price coefficient.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'results': '<raw_handle>', 'price_variable': 'prices', 'conf_level': 0.95},
    },
    'dcd_compensating_variation': {
        'fn': 'dcd_compensating_variation',
        'description': 'dcd_compensating_variation -- category 31-discrete-choice-demand, method card #273.',
        'args': {'results': 'Handle to fitted demand results.', 'prices_post': 'Counterfactual prices.', 'available_post': 'Counterfactual availability flags.'},
        'input_example': {'results': '<raw_handle>'},
    },
    'dcd_consumer_surplus': {
        'fn': 'dcd_consumer_surplus',
        'description': 'dcd_consumer_surplus -- category 31-discrete-choice-demand, method card #273.',
        'args': {'results': 'Handle to fitted demand results.', 'market_id': 'Restrict to one market.'},
        'input_example': {'results': '<raw_handle>'},
    },
}
