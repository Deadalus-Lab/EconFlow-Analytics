# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 30-duration-survival: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'srv_km_fit': {
        'fn': 'srv_km_fit',
        'description': 'srv_km_fit -- category 30-duration-survival, method card #258.',
        'args': {'time': 'Observed duration for each unit.', 'event': 'Event indicator: 1 = event observed, 0 = right-censored.', 'weights': 'Optional observation weights.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'time': '<series_handle>', 'event': '<series_handle>', 'conf_level': 0.95},
    },
    'srv_na_fit': {
        'fn': 'srv_na_fit',
        'description': 'srv_na_fit -- category 30-duration-survival, method card #258.',
        'args': {'time': 'Observed duration for each unit.', 'event': 'Event indicator: 1 = event observed, 0 = right-censored.', 'weights': 'Optional observation weights.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'time': '<series_handle>', 'event': '<series_handle>', 'conf_level': 0.95},
    },
    'srv_logrank_test': {
        'fn': 'srv_logrank_test',
        'description': 'srv_logrank_test -- category 30-duration-survival, method card #258.',
        'args': {'time': 'Observed duration for each unit.', 'event': 'Event indicator.', 'group': 'Group label for each unit.', 'weighting': 'Weight function on the event times.'},
        'input_example': {'time': '<series_handle>', 'event': '<series_handle>', 'group': '<series_handle>', 'weighting': 'logrank'},
    },
    'srv_cox_fit': {
        'fn': 'srv_cox_fit',
        'description': 'srv_cox_fit -- category 30-duration-survival, method card #259.',
        'args': {'data': 'Table holding the durations, the event indicator and the covariates.', 'time': 'Column holding the observed duration.', 'event': 'Column holding the event indicator.', 'covariates': 'Covariate column names.', 'strata': 'Columns to stratify the baseline hazard on.', 'ties': 'Handler for tied event times.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<df_handle>', 'time': '...', 'event': '...', 'ties': 'efron', 'conf_level': 0.95},
    },
    'srv_cox_predict': {
        'fn': 'srv_cox_predict',
        'description': 'srv_cox_predict -- category 30-duration-survival, method card #259.',
        'args': {'fit': 'Handle to a fitted Cox model.', 'newdata': 'Covariate rows to predict for; omitted = the training rows.', 'what': 'Quantity to return.'},
        'input_example': {'fit': '<raw_handle>', 'what': 'survival'},
    },
    'srv_cox_timevarying': {
        'fn': 'srv_cox_timevarying',
        'description': 'srv_cox_timevarying -- category 30-duration-survival, method card #259.',
        'args': {'data': 'Counting-process table: one row per unit per interval.', 'start': 'Column holding the interval start.', 'stop': 'Column holding the interval end.', 'event': 'Column holding the event indicator for the interval.', 'covariates': 'Covariate column names.', 'id': 'Column identifying the unit.'},
        'input_example': {'data': '<df_handle>', 'start': '...', 'stop': '...', 'event': '...', 'id': '...'},
    },
    'srv_aft_fit': {
        'fn': 'srv_aft_fit',
        'description': 'srv_aft_fit -- category 30-duration-survival, method card #260.',
        'args': {'data': 'Table holding the durations, the event indicator and the covariates.', 'time': 'Column holding the observed duration.', 'event': 'Column holding the event indicator.', 'covariates': 'Covariate column names.', 'distribution': 'Failure-time distribution.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<df_handle>', 'time': '...', 'event': '...', 'distribution': 'weibull', 'conf_level': 0.95},
    },
    'srv_aft_compare': {
        'fn': 'srv_aft_compare',
        'description': 'srv_aft_compare -- category 30-duration-survival, method card #260.',
        'args': {'data': 'Table holding the durations, the event indicator and the covariates.', 'time': 'Column holding the observed duration.', 'event': 'Column holding the event indicator.', 'covariates': 'Covariate column names.', 'criterion': 'Information criterion used to rank the families.'},
        'input_example': {'data': '<df_handle>', 'time': '...', 'event': '...', 'criterion': 'aic'},
    },
    'srv_aft_predict': {
        'fn': 'srv_aft_predict',
        'description': 'srv_aft_predict -- category 30-duration-survival, method card #260.',
        'args': {'fit': 'Handle to a fitted parametric model.', 'newdata': 'Covariate rows to predict for.', 'what': 'Quantity to return.', 'q': "Quantile to return when what='quantile'."},
        'input_example': {'fit': '<raw_handle>', 'what': 'survival', 'q': 0.5},
    },
    'srv_discrete_expand': {
        'fn': 'srv_discrete_expand',
        'description': 'srv_discrete_expand -- category 30-duration-survival, method card #261.',
        'args': {'data': 'One row per unit.', 'time': 'Column holding the observed duration in whole intervals.', 'event': 'Column holding the event indicator.', 'id': 'Column identifying the unit.'},
        'input_example': {'data': '<df_handle>', 'time': '...', 'event': '...', 'id': '...'},
    },
    'srv_discrete_fit': {
        'fn': 'srv_discrete_fit',
        'description': 'srv_discrete_fit -- category 30-duration-survival, method card #261.',
        'args': {'data': 'Person-period table: one row per unit per interval at risk.', 'event': 'Column holding the within-interval event indicator.', 'duration': 'Column holding the interval index.', 'covariates': 'Covariate column names.', 'link': 'Link function.', 'baseline': 'How duration dependence enters the model.'},
        'input_example': {'data': '<df_handle>', 'event': '...', 'duration': '...', 'link': 'cloglog', 'baseline': 'dummies'},
    },
    'srv_cif_fit': {
        'fn': 'srv_cif_fit',
        'description': 'srv_cif_fit -- category 30-duration-survival, method card #262.',
        'args': {'time': 'Observed duration.', 'event': 'Cause code: 0 = censored, 1..K = the competing causes.', 'weights': 'Optional observation weights.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'time': '<series_handle>', 'event': '<series_handle>', 'conf_level': 0.95},
    },
    'srv_cause_specific': {
        'fn': 'srv_cause_specific',
        'description': 'srv_cause_specific -- category 30-duration-survival, method card #262.',
        'args': {'data': 'Table holding durations, the cause code and covariates.', 'time': 'Column holding the observed duration.', 'event': 'Column holding the cause code.', 'cause': 'The cause to model; all others are treated as censoring.', 'covariates': 'Covariate column names.'},
        'input_example': {'data': '<df_handle>', 'time': '...', 'event': '...', 'cause': 1},
    },
    'srv_finegray_fit': {
        'fn': 'srv_finegray_fit',
        'description': 'srv_finegray_fit -- category 30-duration-survival, method card #262.',
        'args': {'data': 'Table holding durations, the cause code and covariates.', 'time': 'Column holding the observed duration.', 'event': 'Column holding the cause code.', 'cause': 'The cause whose cumulative incidence is modelled.', 'covariates': 'Covariate column names.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<df_handle>', 'time': '...', 'event': '...', 'cause': 1, 'conf_level': 0.95},
    },
    'srv_gray_test': {
        'fn': 'srv_gray_test',
        'description': 'srv_gray_test -- category 30-duration-survival, method card #262.',
        'args': {'time': 'Observed duration.', 'event': 'Cause code.', 'group': 'Group label.', 'cause': 'The cause being compared.'},
        'input_example': {'time': '<series_handle>', 'event': '<series_handle>', 'group': '<series_handle>', 'cause': 1},
    },
    'srv_frailty_fit': {
        'fn': 'srv_frailty_fit',
        'description': 'srv_frailty_fit -- category 30-duration-survival, method card #263.',
        'args': {'data': 'Table holding durations, the event indicator and covariates.', 'time': 'Column holding the observed duration.', 'event': 'Column holding the event indicator.', 'covariates': 'Covariate column names.', 'cluster': 'Column identifying the frailty group.', 'frailty': 'Distribution of the shared frailty term.'},
        'input_example': {'data': '<df_handle>', 'time': '...', 'event': '...', 'cluster': '...', 'frailty': 'gamma'},
    },
    'srv_frailty_test': {
        'fn': 'srv_frailty_test',
        'description': 'srv_frailty_test -- category 30-duration-survival, method card #263.',
        'args': {'fit': 'Handle to a fitted frailty model.'},
        'input_example': {'fit': '<raw_handle>'},
    },
    'srv_schoenfeld': {
        'fn': 'srv_schoenfeld',
        'description': 'srv_schoenfeld -- category 30-duration-survival, method card #264.',
        'args': {'fit': 'Handle to a fitted Cox model.', 'transform': 'Time transform applied before the test.'},
        'input_example': {'fit': '<raw_handle>', 'transform': 'km'},
    },
    'srv_ph_test': {
        'fn': 'srv_ph_test',
        'description': 'srv_ph_test -- category 30-duration-survival, method card #264.',
        'args': {'fit': 'Handle to a fitted Cox model.', 'transform': 'Time transform applied before the test.', 'alpha': 'Significance level.'},
        'input_example': {'fit': '<raw_handle>', 'transform': 'km', 'alpha': 0.05},
    },
    'srv_cox_residuals': {
        'fn': 'srv_cox_residuals',
        'description': 'srv_cox_residuals -- category 30-duration-survival, method card #264.',
        'args': {'fit': 'Handle to a fitted Cox model.', 'kind': 'Residual type.'},
        'input_example': {'fit': '<raw_handle>', 'kind': 'martingale'},
    },
    'srv_piecewise_hazard': {
        'fn': 'srv_piecewise_hazard',
        'description': 'srv_piecewise_hazard -- category 30-duration-survival, method card #265.',
        'args': {'time': 'Observed duration.', 'event': 'Event indicator.', 'breaks': 'Interval boundaries; empty = equal-count intervals.', 'n_intervals': 'Number of equal-count intervals when breaks is empty.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'time': '<series_handle>', 'event': '<series_handle>', 'n_intervals': 6, 'conf_level': 0.95},
    },
    'srv_hazard_shape': {
        'fn': 'srv_hazard_shape',
        'description': 'srv_hazard_shape -- category 30-duration-survival, method card #265.',
        'args': {'time': 'Observed duration.', 'event': 'Event indicator.', 'bandwidth': 'Smoothing bandwidth; omitted = plug-in rule.'},
        'input_example': {'time': '<series_handle>', 'event': '<series_handle>'},
    },
}
