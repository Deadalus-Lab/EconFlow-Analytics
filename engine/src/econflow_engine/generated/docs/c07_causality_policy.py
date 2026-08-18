# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 07-causality-policy: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'bacon_decompose': {
        'fn': 'bacon_decompose',
        'description': 'bacon_decompose -- category 07-causality-policy, METHOD-SELECTION card #167.',
        'args': {'formula': "Formula 'outcome ~ treated [+ covariates]'; the treated variable is a 0/1 indicator of an active intervention (staggered).", 'data': 'Handle to a DataFrame in long panel form — STRICTLY balanced (same #periods per unit).', 'id_var': "Unit identifier column name (e.g. 'state').", 'time_var': "Time/period column name (e.g. 'year').", 'quietly': 'When True (default) suppresses the console prints of bacon.'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>', 'id_var': '...', 'time_var': '...', 'quietly': True},
    },
    'cw_lateweight': {
        'fn': 'cw_lateweight',
        'description': 'cw_lateweight -- category 07-causality-policy, METHOD-SELECTION card #171.',
        'args': {'y': 'Handle to an outcome vector (numeric).', 'd': 'Handle to a BINARY 0/1 (endogenous) treatment vector.', 'z': 'Handle to a BINARY 0/1 instrument vector (same length as y).', 'x': 'Handle to a confounder matrix (confounders of z & y, no NA).', 'LATT': 'True -> LATT (treated compliers); False -> LATE (default).', 'trim': 'Trimming of extreme instrument propensity scores (default 0.05; [0,0.5)).', 'logit': 'True=logit, False=probit (default False).', 'boot': 'Bootstrap replications for the SE (default 1999; >=2).', 'seed': 'Seed for the bootstrap (default 2025).'},
        'input_example': {'y': '<raw_handle>', 'd': '<raw_handle>', 'z': '<raw_handle>', 'x': '<matrix_handle>', 'LATT': False, 'trim': 0.05, 'logit': False, 'boot': 1999, 'seed': 2025},
    },
    'cw_medDML': {
        'fn': 'cw_medDML',
        'description': 'cw_medDML -- category 07-causality-policy, METHOD-SELECTION card #171.',
        'args': {'y': 'Handle to an outcome vector (numeric).', 'd': 'Handle to a BINARY 0/1 treatment vector (same length as y).', 'm': 'Handle to the mediator(s): vector/matrix (multmed=True) or a binary scalar (multmed=False).', 'x': 'Handle to a pre-treatment confounder matrix (no NA).', 'k': 'Cross-fitting folds when multmed=False (default 3; >=2).', 'trim': 'Trimming of extreme conditional probabilities (default 0.05; [0,0.5)).', 'multmed': 'True=Farbmacher et al. (multiple/continuous mediators); False=Tchetgen (binary scalar mediator).', 'normalized': 'Normalize the IPW weights (default True).', 'MLmethod': 'ML engine for the nuisance parameters (default lasso).', 'seed': 'Seed for the random cross-fitting partition (default 2025).'},
        'input_example': {'y': '<raw_handle>', 'd': '<raw_handle>', 'm': '<raw_handle>', 'x': '<matrix_handle>', 'k': 3, 'trim': 0.05, 'multmed': True, 'normalized': True, 'seed': 2025},
    },
    'cw_treatDML': {
        'fn': 'cw_treatDML',
        'description': 'cw_treatDML -- category 07-causality-policy, METHOD-SELECTION card #171.',
        'args': {'y': 'Handle to an outcome vector (numeric, no NA/Inf).', 'd': 'Handle to a discrete treatment vector (binary or multiple; same length as y).', 'x': 'Handle to a covariate/confounder matrix (n x p, numeric, no NA).', 'dtreat': 'Value of d in the treated group (default 1).', 'dcontrol': 'Value of d in the control group (default 0; != dtreat, among the values of d).', 'trim': 'Trimming of propensity scores outside [trim, 1-trim] (default 0.01; [0,0.5)).', 'MLmethod': 'ML engine for the nuisance parameters (default lasso).', 'k': 'Folds in the k-fold cross-fitting (default 3; >=2).', 'normalized': 'Normalize the IPW weights so they sum to 1 per group (default True).', 'seed': 'Seed for the random cross-fitting partition (default 2025).'},
        'input_example': {'y': '<raw_handle>', 'd': '<raw_handle>', 'x': '<matrix_handle>', 'dtreat': 1, 'dcontrol': 0, 'trim': 0.01, 'k': 3, 'normalized': True, 'seed': 2025},
    },
    'cw_treatweight': {
        'fn': 'cw_treatweight',
        'description': 'cw_treatweight -- category 07-causality-policy, METHOD-SELECTION card #171.',
        'args': {'y': 'Handle to an outcome vector (numeric).', 'd': 'Handle to a BINARY 0/1 treatment vector (same length as y).', 'x': 'Handle to a confounder matrix (n x p, no NA).', 'ATET': 'True -> ATET (effect on treated); False -> ATE (default).', 'trim': 'Trimming of extreme propensity scores (default 0.05; [0,0.5)).', 'logit': 'True=logit, False=probit for the propensity score (default False).', 'boot': 'Bootstrap replications for the SE (default 1999; >=2).', 'seed': 'Seed for the bootstrap (default 2025).'},
        'input_example': {'y': '<raw_handle>', 'd': '<raw_handle>', 'x': '<matrix_handle>', 'ATET': False, 'trim': 0.05, 'logit': False, 'boot': 1999, 'seed': 2025},
    },
    'didm_dyn': {
        'fn': 'didm_dyn',
        'description': 'didm_dyn -- category 07-causality-policy, METHOD-SELECTION card #166.',
        'args': {'df': 'Handle to a long-format panel DataFrame (group x time, evenly-spaced time).', 'outcome': 'Outcome column name.', 'group': 'Group column name (cross-sectional unit: county/firm/...).', 'time': 'Time column name (evenly-spaced periods).', 'treatment': 'Treatment column name (may be non-binary AND/OR non-absorbing).', 'effects': 'Number of event-study effects (ℓ=1..effects; default 1).', 'placebo': 'Number of placebo (pre-trends) estimators; MUST be <= effects (default 0).', 'controls': 'Covariate column names (residualized first-differences; default: none).', 'cluster': 'Column name for SE clustering (>= group level; default clustering at the group).', 'weight': 'Column name of the estimation weights (default: unweighted/number of obs).', 'normalized': 'Normalized effects (weighted avg of current+lagged treatment; default False).', 'trends_lin': 'Group-specific linear trends (THEN the ATE is NOT computed; default False).', 'continuous': 'Polynomial order for continuous period-one treatment (bootstrap recommended).', 'effects_equal': 'F-test of equality of all effects (requires effects>=2; default False).', 'ci_level': 'Confidence level, integer in (0,100) (default 95).', 'bootstrap': 'Bootstrap replications (None = analytical SE); seed-reproducible.', 'seed': 'Bootstrap reproducibility seed (default 2025).'},
        'input_example': {'df': '<df_handle>', 'outcome': '...', 'group': '...', 'time': '...', 'treatment': '...', 'effects': 1, 'placebo': 0, 'normalized': False, 'trends_lin': False, 'effects_equal': False, 'ci_level': 95, 'seed': 2025},
    },
    'fx_coeftable': {
        'fn': 'fx_coeftable',
        'description': 'fx_coeftable -- category 07-causality-policy, METHOD-SELECTION card #33.',
        'args': {'object': 'Handle to a fixest model (from fx_feols).', 'vcov': 'Recompute SE with a different vcov without re-fitting.', 'cluster': 'Clustering variable for the SE.'},
        'input_example': {'object': '<raw_handle>'},
    },
    'fx_confint': {
        'fn': 'fx_confint',
        'description': 'fx_confint -- category 07-causality-policy, METHOD-SELECTION card #33.',
        'args': {'object': 'Handle to a fixest model (from fx_feols).', 'level': 'Confidence level in (0,1) (default 0.95).', 'vcov': 'Alternative vcov for the intervals.', 'cluster': 'Clustering variable.'},
        'input_example': {'object': '<raw_handle>', 'level': 0.95},
    },
    'fx_feols': {
        'fn': 'fx_feols',
        'description': 'fx_feols -- category 07-causality-policy, METHOD-SELECTION card #33.',
        'args': {'fml': "Formula, e.g. 'y ~ x1 + x2 | unit + time' (FE after the |; IV: | endo ~ inst).", 'data': 'Handle to a DataFrame (panel/cross-section).', 'vcov': "vcov type, e.g. 'hetero' or 'cluster' (default: iid/by FE).", 'cluster': 'Clustering variable name (or formula string) for robust SE.'},
        'input_example': {'fml': 'y ~ x', 'data': '<df_handle>'},
    },
    'fx_fitstat': {
        'fn': 'fx_fitstat',
        'description': 'fx_fitstat -- category 07-causality-policy, METHOD-SELECTION card #33.',
        'args': {'object': 'Handle to a fixest model (from fx_feols).', 'type': "Statistic/test (required): e.g. 'r2','rmse','f','wald','ivwald'.", 'vcov': 'Alternative vcov for test statistics.', 'cluster': 'Clustering variable.'},
        'input_example': {'object': '<raw_handle>', 'type': '...'},
    },
    'fx_vcov': {
        'fn': 'fx_vcov',
        'description': 'fx_vcov -- category 07-causality-policy, METHOD-SELECTION card #33.',
        'args': {'object': 'Handle to a fixest model (from fx_feols).', 'vcov': "vcov type (e.g. 'hetero','cluster').", 'cluster': 'Clustering variable.'},
        'input_example': {'object': '<raw_handle>'},
    },
    'gmm_fit': {
        'fn': 'gmm_fit',
        'description': 'gmm_fit -- category 07-causality-policy, METHOD-SELECTION card #172.',
        'args': {'formula': "Two-sided model formula 'y ~ x1 + x2' (the moment conditions are defined by the instruments; formula ONLY — no moment function).", 'instruments': "One-sided instruments formula '~ z1 + z2 + z3' (>= number of coefficients for identification).", 'data': 'Handle to a DataFrame holding every formula+instruments variable, no NA.', 'type': 'GMM estimator: two-step efficient / continuous-updating / iterative (default twoStep).', 'wmatrix': 'Weighting matrix: efficient optimal or identity (2SLS-type) (default optimal).', 'vcov': 'Variance estimator of the moments: HAC (autocorrelation-robust) / MDS (mart. diff.) / iid / TrueFixed (default HAC).'},
        'input_example': {'formula': 'y ~ x', 'instruments': 'y ~ x', 'data': '<df_handle>'},
    },
    'gmm_jtest': {
        'fn': 'gmm_jtest',
        'description': 'gmm_jtest -- category 07-causality-policy, METHOD-SELECTION card #172.',
        'args': {'object': 'Handle to a fitted gmm object (from gmm_fit$object) — Hansen-Sargan J of overidentification.'},
        'input_example': {'object': '<raw_handle>'},
    },
    'honest_original_cs': {
        'fn': 'honest_original_cs',
        'description': 'honest_original_cs -- category 07-causality-policy, METHOD-SELECTION card #168.',
        'args': {'betahat': 'Event-study coefficients (pre+post, in time order) — num vector.', 'sigma': 'Handle to the vcov of betahat (square matrix, dim = length(betahat)).', 'numPrePeriods': 'Number of pre-treatment periods (>=1).', 'numPostPeriods': 'Number of post-treatment periods (>=1); numPre+numPost = length(betahat).', 'l_vec': 'Weights of the linear combination of post-period effects (length numPostPeriods; default = 1st post period).', 'alpha': 'Significance level in (0,1) (default 0.05 -> 95% CI).'},
        'input_example': {'betahat': [0.5, 0.5], 'sigma': '<matrix_handle>', 'numPrePeriods': 1, 'numPostPeriods': 1, 'alpha': 0.05},
    },
    'honest_relmag': {
        'fn': 'honest_relmag',
        'description': 'honest_relmag -- category 07-causality-policy, METHOD-SELECTION card #168.',
        'args': {'betahat': 'Event-study coefficients (pre+post, in time order) — num vector.', 'sigma': 'Handle to the vcov of betahat (square matrix, dim = length(betahat)).', 'numPrePeriods': 'Number of pre-treatment periods (>=1; basis for the relative magnitude).', 'numPostPeriods': 'Number of post-treatment periods (>=1); numPre+numPost = length(betahat).', 'Mbarvec': 'Non-negative Mbar values (multiple of the max pre-trend violation). None -> auto grid.', 'l_vec': 'Weights of the linear combination of post-period effects (length numPostPeriods; default = 1st post period).', 'method': 'CI method (default C-LF); simulation-based.', 'monotonicityDirection': 'Optional monotonicity restriction on the trend.', 'biasDirection': 'Optional sign restriction on the bias.', 'alpha': 'Significance level in (0,1) (default 0.05 -> 95% CI).', 'gridPoints': 'Number of points in the search grid (>=2); fewer = faster/coarser.', 'seed': 'Seed for the simulation-based CIs; reproducibility.'},
        'input_example': {'betahat': [0.5, 0.5], 'sigma': '<matrix_handle>', 'numPrePeriods': 1, 'numPostPeriods': 1, 'method': 'Conditional', 'alpha': 0.05, 'gridPoints': 1000, 'seed': 2025},
    },
    'honest_smoothness': {
        'fn': 'honest_smoothness',
        'description': 'honest_smoothness -- category 07-causality-policy, METHOD-SELECTION card #168.',
        'args': {'betahat': 'Event-study coefficients (pre+post, in time order) — num vector.', 'sigma': 'Handle to the vcov of betahat (square matrix, dim = length(betahat)).', 'numPrePeriods': 'Number of pre-treatment periods (>=1).', 'numPostPeriods': 'Number of post-treatment periods (>=1); numPre+numPost = length(betahat).', 'Mvec': 'Non-negative values of the smoothness bound M (max |second difference| of the trend). None -> auto grid.', 'l_vec': 'Weights of the linear combination of post-period effects (length numPostPeriods; default = 1st post period).', 'method': 'CI method (default: FLCI for DeltaSD). C-LF/Conditional = simulation-based.', 'monotonicityDirection': 'Optional monotonicity restriction on the trend.', 'biasDirection': 'Optional sign restriction on the bias.', 'alpha': 'Significance level in (0,1) (default 0.05 -> 95% CI).', 'seed': 'Seed for the simulation-based CIs (C-LF/Conditional); reproducibility.'},
        'input_example': {'betahat': [0.5, 0.5], 'sigma': '<matrix_handle>', 'numPrePeriods': 1, 'numPostPeriods': 1, 'alpha': 0.05, 'seed': 2025},
    },
    'iv_fit': {
        'fn': 'iv_fit',
        'description': 'iv_fit -- category 07-causality-policy, METHOD-SELECTION card #165.',
        'args': {'formula': "Three-part IV formula 'y ~ exog | endog | instruments' (modern ivreg; all 3 parts required).", 'data': 'Handle to a DataFrame holding every variable of the formula (no NA).', 'method': 'Estimator: classical 2SLS (OLS, default) or robust M/MM (both require robustbase).', 'conf_level': 'Confidence level for the coefficient CIs, in (0,1) (default 0.95).'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>', 'method': 'OLS', 'conf_level': 0.95},
    },
    'rdmc_fit': {
        'fn': 'rdmc_fit',
        'description': 'rdmc_fit -- category 07-causality-policy, METHOD-SELECTION card #169.',
        'args': {'Y': 'Outcome vector (numeric, no NA).', 'X': 'Running variable vector (same length as Y).', 'C': 'Per-observation cutoff variable (same length as X; >=2 distinct cutoffs).', 'fuzzy': 'Treatment-status vector for fuzzy RD (default: sharp).', 'covs_mat': 'Covariate vector/matrix (nrow == length of X; no NA).', 'cluster': 'Cluster ID vector (same length as X).', 'kernel': 'Kernel (default tri).', 'p': 'Local polynomial degree (default 1).', 'bwselect': 'Bandwidth selector (default mserd).', 'level': 'Confidence level in (0,100) (default 95).', 'conventional': 'True -> conventional instead of robust bias-corrected inference.'},
        'input_example': {'Y': [0.5, 0.5], 'X': [0.5, 0.5], 'C': [0.5, 0.5], 'kernel': 'tri', 'p': 1, 'bwselect': 'mserd', 'level': 95, 'conventional': False},
    },
    'rdms_fit': {
        'fn': 'rdms_fit',
        'description': 'rdms_fit -- category 07-causality-policy, METHOD-SELECTION card #169.',
        'args': {'Y': 'Outcome vector (numeric, no NA).', 'X': 'Running variable vector (same length as Y).', 'C': 'Vector of cutoff values (e.g. [33,66]; non-empty, no NA).', 'xnorm': 'Normalized running variable for the pooled estimate (without it pooled=NA).', 'fuzzy': 'Treatment-status vector for fuzzy RD (default: sharp).', 'covs_mat': 'Covariate vector/matrix (nrow == length of X; no NA).', 'cluster': 'Cluster ID vector (same length as X).', 'kernel': 'Kernel (default tri).', 'p': 'Local polynomial degree (default 1).', 'bwselect': 'Bandwidth selector (default mserd).', 'level': 'Confidence level in (0,100) (default 95).', 'conventional': 'True -> conventional instead of robust bias-corrected inference.'},
        'input_example': {'Y': [0.5, 0.5], 'X': [0.5, 0.5], 'C': [0.5, 0.5], 'kernel': 'tri', 'p': 1, 'bwselect': 'mserd', 'level': 95, 'conventional': False},
    },
    'run_causal_impact': {
        'fn': 'run_causal_impact',
        'description': 'run_causal_impact -- category 07-causality-policy, METHOD-SELECTION card #90.',
        'args': {'data': 'Handle to a ts/mts/matrix: 1st column=response, the rest=covariates.', 'pre_period': 'Handle to a length-2 vector [start, end] pre-intervention.', 'post_period': 'Handle to a length-2 vector [start, end] post-intervention.', 'alpha': 'Significance level for the credible intervals (default 0.05).', 'seed': 'Seed (required: bsts MCMC reproducibility).'},
        'input_example': {'data': '<matrix_handle>', 'pre_period': '<raw_handle>', 'post_period': '<raw_handle>', 'alpha': 0.05, 'seed': 1},
    },
    'sens_analyze': {
        'fn': 'sens_analyze',
        'description': 'sens_analyze -- category 07-causality-policy, METHOD-SELECTION card #170.',
        'args': {'treatment': 'Name of the treatment coefficient (ONE coef name of the lm, not the intercept).', 'benchmark_covariates': 'Covariate names (>=1) used as the benchmark for confounding strength; a subset of the coef names \\ {treatment}.', 'formula': "OLS formula, e.g. 'y ~ d + x1 + x2' (fit path; ALSO requires data). Alternatively supply object.", 'data': 'Handle to a DataFrame holding the variables of the formula (fit path).', 'object': "Handle to an ALREADY fitted 'lm' model (consume path; mutually exclusive with formula+data).", 'kd': 'Multipliers of the confounder~treatment strength relative to the benchmark (>0, default 1; e.g. [1,2,3]).', 'ky': 'Multipliers of the confounder~outcome strength (>0; default = kd).', 'q': 'Fraction of effect reduction treated as problematic for the robustness value (>0, default 1 = complete disappearance).', 'alpha': 'Significance level for the robustness value with statistical significance, in (0,1) (default 0.05).', 'reduce': 'True: the confounder REDUCES the estimate (default); False: it increases it.'},
        'input_example': {'treatment': '...', 'benchmark_covariates': ['PROVIDER/DATASET/SERIES'], 'kd': [0.5, 0.5], 'q': 1, 'alpha': 0.05, 'reduce': True},
    },
    'wrap_aggte': {
        'fn': 'wrap_aggte',
        'description': 'wrap_aggte -- category 07-causality-policy, METHOD-SELECTION card #36.',
        'args': {'MP': 'Handle to an att_gt object (from wrap_att_gt).', 'type': 'Aggregation: event-study/overall/cohort/calendar (default dynamic).', 'min_e': 'Minimum event time (default -Inf).', 'max_e': 'Maximum event time (default Inf).', 'na_rm': 'Drop NA ATT(g,t) (default False).'},
        'input_example': {'MP': '<raw_handle>', 'na_rm': False},
    },
    'wrap_att_gt': {
        'fn': 'wrap_att_gt',
        'description': 'wrap_att_gt -- category 07-causality-policy, METHOD-SELECTION card #36.',
        'args': {'yname': 'Outcome column name.', 'tname': 'Time column name (period).', 'gname': 'Cohort/first-treatment-period column name (0 = never-treated).', 'idname': 'Unit id column name (required when panel=True).', 'xformla': "Covariate formula, e.g. '~ x1' (default: none).", 'data': 'Handle to a long-format panel DataFrame.', 'panel': 'True=panel (default), False=repeated cross-sections.', 'control_group': 'Control group (default nevertreated).', 'est_method': 'Estimator: doubly-robust/IPW/regression (default dr).', 'base_period': 'Base period for the event study (default varying).', 'bstrap': 'Bootstrap inference (default True).', 'biters': 'Bootstrap iterations (default 1000).', 'cband': 'Uniform confidence bands (default True).', 'alp': 'Significance level (default 0.05).'},
        'input_example': {'yname': '...', 'tname': '...', 'gname': '...', 'data': '<df_handle>', 'panel': True, 'bstrap': True, 'biters': 1000, 'cband': True, 'alp': 0.05},
    },
    'wrap_average_treatment_effect': {
        'fn': 'wrap_average_treatment_effect',
        'description': 'wrap_average_treatment_effect -- category 07-causality-policy, METHOD-SELECTION card #44.',
        'args': {'forest': 'Handle to a causal_forest (from wrap_causal_forest).', 'target_sample': 'Target sample (default all = ATE).', 'method': 'Estimator (default AIPW).'},
        'input_example': {'forest': '<raw_handle>'},
    },
    'wrap_causal_forest': {
        'fn': 'wrap_causal_forest',
        'description': 'wrap_causal_forest -- category 07-causality-policy, METHOD-SELECTION card #44.',
        'args': {'X': 'Handle to a covariate matrix (n x p).', 'Y': 'Handle to an outcome vector (length n).', 'W': 'Handle to a treatment vector (length n).', 'num_trees': 'Number of trees (default 2000).', 'min_node_size': 'Minimum leaf size (default 5).', 'honesty': 'Honest splitting (default True).', 'seed': 'Reproducibility seed.'},
        'input_example': {'X': '<matrix_handle>', 'Y': '<raw_handle>', 'W': '<raw_handle>', 'num_trees': 2000, 'min_node_size': 5, 'honesty': True},
    },
    'wrap_dataprep': {
        'fn': 'wrap_dataprep',
        'description': 'wrap_dataprep -- category 07-causality-policy, METHOD-SELECTION card #40.',
        'args': {'foo': 'Handle to a long-format panel DataFrame.', 'predictors': 'Predictor column names (array of strings).', 'predictors_op': "Aggregation function for the predictors (default 'mean').", 'dependent': 'Outcome column name.', 'unit_variable': 'Unit id column name.', 'time_variable': 'Time column name.', 'treatment_identifier': 'ID of the treated unit (single scalar; required in practice).', 'controls_identifier': 'Handle to a vector of control-unit IDs (>=2).', 'time_predictors_prior': 'Handle to a vector of pre-treatment periods for the predictors.', 'time_optimize_ssr': 'Handle to a vector of periods for the SSR optimization.', 'time_plot': 'Handle to a vector of all periods to be plotted.'},
        'input_example': {'foo': '<df_handle>', 'predictors_op': 'mean'},
    },
    'wrap_did_imputation': {
        'fn': 'wrap_did_imputation',
        'description': 'wrap_did_imputation -- category 07-causality-policy, METHOD-SELECTION card #37.',
        'args': {'data': 'Handle to a long-format panel DataFrame.', 'yname': 'Outcome column name.', 'gname': 'Cohort/first-treatment-period column name (0/Inf = never-treated).', 'tname': 'Time column name.', 'idname': 'Unit id column name.', 'first_stage': "First-stage FE formula, e.g. '~ 0 | unit + period' (default: unit+time FE).", 'cluster_var': 'Clustering column name (default: idname).'},
        'input_example': {'data': '<df_handle>', 'yname': '...', 'gname': '...', 'tname': '...', 'idname': '...'},
    },
    'wrap_doubleml_data': {
        'fn': 'wrap_doubleml_data',
        'description': 'wrap_doubleml_data -- category 07-causality-policy, METHOD-SELECTION card #45.',
        'args': {'data': 'Handle to a cross-sectional DataFrame.', 'y_col': 'Outcome column name.', 'd_cols': 'Treatment column names (>=1).', 'x_cols': 'Covariate/control column names.', 'z_cols': 'Instrument column names (optional).', 'use_other_treat_as_covariate': 'Use the other treatments as covariates (default True).'},
        'input_example': {'data': '<df_handle>', 'y_col': '...', 'd_cols': ['PROVIDER/DATASET/SERIES'], 'x_cols': ['PROVIDER/DATASET/SERIES'], 'use_other_treat_as_covariate': True},
    },
    'wrap_doubleml_irm': {
        'fn': 'wrap_doubleml_irm',
        'description': 'wrap_doubleml_irm -- category 07-causality-policy, METHOD-SELECTION card #45.',
        'args': {'data': 'Handle to a DoubleMLData object (binary treatment).', 'learner': 'ML engine (default ranger).', 'n_folds': 'Cross-fitting folds (default 5).', 'n_rep': 'Cross-fitting repetitions (default 1).', 'score': 'Estimand (default ATE).', 'trimming_rule': 'Propensity trimming rule (default truncate).', 'dml_procedure': 'DML procedure (default dml2).', 'seed': 'Seed (required: cross-fitting reproducibility).'},
        'input_example': {'data': '<raw_handle>', 'n_folds': 5, 'n_rep': 1, 'seed': 1},
    },
    'wrap_doubleml_plr': {
        'fn': 'wrap_doubleml_plr',
        'description': 'wrap_doubleml_plr -- category 07-causality-policy, METHOD-SELECTION card #45.',
        'args': {'data': 'Handle to a DoubleMLData object (from wrap_doubleml_data).', 'learner': 'ML engine for the nuisance functions (default ranger).', 'n_folds': 'Cross-fitting folds (default 5).', 'n_rep': 'Cross-fitting repetitions (default 1).', 'score': 'Score function (default partialling out).', 'dml_procedure': 'DML procedure (default dml2).', 'seed': 'Seed (required: cross-fitting reproducibility).'},
        'input_example': {'data': '<raw_handle>', 'n_folds': 5, 'n_rep': 1, 'seed': 1},
    },
    'wrap_generate_control': {
        'fn': 'wrap_generate_control',
        'description': 'wrap_generate_control -- category 07-causality-policy, METHOD-SELECTION card #42.',
        'args': {'data': 'Handle to a tidysynth pipeline (after generate_weights).'},
        'input_example': {'data': '<raw_handle>'},
    },
    'wrap_generate_predictor': {
        'fn': 'wrap_generate_predictor',
        'description': 'wrap_generate_predictor -- category 07-causality-policy, METHOD-SELECTION card #42.',
        'args': {'data': 'Handle to a tidysynth pipeline object (from wrap_synthetic_control).', 'time_window': 'Handle to a vector of time values used to compute the predictors.', 'predictors': "Handle to a named list, e.g. list(mean_x1 = list(column='x1', stat='mean'))."},
        'input_example': {'data': '<raw_handle>', 'time_window': '<raw_handle>', 'predictors': '<raw_handle>'},
    },
    'wrap_generate_weights': {
        'fn': 'wrap_generate_weights',
        'description': 'wrap_generate_weights -- category 07-causality-policy, METHOD-SELECTION card #42.',
        'args': {'data': 'Handle to a tidysynth pipeline (after generate_predictor).', 'optimization_window': 'Handle to a vector of pre-treatment periods for the optimization.', 'optimization_method': 'Optimizer (default Nelder-Mead).', 'genoud': 'Genetic optimization (default False).', 'quadopt': 'Quadratic optimizer (default ipop).', 'include_fit': 'Return the fit object (default False).'},
        'input_example': {'data': '<raw_handle>', 'optimization_window': '<raw_handle>', 'genoud': False, 'include_fit': False},
    },
    'wrap_grab_loss': {
        'fn': 'wrap_grab_loss',
        'description': 'wrap_grab_loss -- category 07-causality-policy, METHOD-SELECTION card #42.',
        'args': {'data': 'Handle to a completed tidysynth pipeline.'},
        'input_example': {'data': '<raw_handle>'},
    },
    'wrap_grab_predictor_weights': {
        'fn': 'wrap_grab_predictor_weights',
        'description': 'wrap_grab_predictor_weights -- category 07-causality-policy, METHOD-SELECTION card #42.',
        'args': {'data': 'Handle to a tidysynth pipeline (after generate_weights).', 'placebo': 'Placebo units (default False).'},
        'input_example': {'data': '<raw_handle>', 'placebo': False},
    },
    'wrap_grab_significance': {
        'fn': 'wrap_grab_significance',
        'description': 'wrap_grab_significance -- category 07-causality-policy, METHOD-SELECTION card #42.',
        'args': {'data': 'Handle to a tidysynth pipeline with placebos.', 'time_window': 'Handle to a vector of post-period values for the inference (default: post-period).'},
        'input_example': {'data': '<raw_handle>'},
    },
    'wrap_grab_synthetic_control': {
        'fn': 'wrap_grab_synthetic_control',
        'description': 'wrap_grab_synthetic_control -- category 07-causality-policy, METHOD-SELECTION card #42.',
        'args': {'data': 'Handle to a completed tidysynth pipeline (after generate_control).', 'placebo': 'Return placebo units (default False).'},
        'input_example': {'data': '<raw_handle>', 'placebo': False},
    },
    'wrap_grab_unit_weights': {
        'fn': 'wrap_grab_unit_weights',
        'description': 'wrap_grab_unit_weights -- category 07-causality-policy, METHOD-SELECTION card #42.',
        'args': {'data': 'Handle to a tidysynth pipeline (after generate_weights).', 'placebo': 'Placebo units (default False).'},
        'input_example': {'data': '<raw_handle>', 'placebo': False},
    },
    'wrap_gsynth': {
        'fn': 'wrap_gsynth',
        'description': 'wrap_gsynth -- category 07-causality-policy, METHOD-SELECTION card #43.',
        'args': {'formula': "Formula 'y ~ D + x1' (D = 0/1 treatment); alternatively supply Y/D.", 'data': 'Handle to a long-format panel DataFrame.', 'Y': 'Outcome column name (when no formula is given).', 'D': 'Treatment 0/1 column name (when Y is given).', 'X': 'Covariate column names (array of strings).', 'index': 'Column names [unit, time] (exactly 2).', 'force': 'Fixed effects (default two-way).', 'estimator': 'Estimator: IFE / matrix completion (default gsynth).', 'criterion': 'CV criterion (default mspe).', 'r': 'Number of factors (default 0; CV selects it when CV=True).', 'CV': 'Cross-validation for r (default True).', 'se': 'Bootstrap standard errors (default False).', 'nboots': 'Bootstrap iterations when se=True (default 200).'},
        'input_example': {'data': '<df_handle>', 'index': ['PROVIDER/DATASET/SERIES'], 'r': 0, 'CV': True, 'se': False, 'nboots': 200},
    },
    'wrap_ivreg': {
        'fn': 'wrap_ivreg',
        'description': 'wrap_ivreg -- category 07-causality-policy, METHOD-SELECTION card #34.',
        'args': {'formula': "IV formula 'y ~ x1 + d | x1 + z' (instruments after the |).", 'data': 'Handle to a DataFrame.', 'conf_level': 'Confidence level for coefficient CIs (default 0.95).'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>', 'conf_level': 0.95},
    },
    'wrap_predict_causal_forest': {
        'fn': 'wrap_predict_causal_forest',
        'description': 'wrap_predict_causal_forest -- category 07-causality-policy, METHOD-SELECTION card #44.',
        'args': {'forest': 'Handle to a causal_forest (from wrap_causal_forest).', 'newdata': 'Handle to a new covariate matrix (default: training OOB predictions).', 'estimate_variance': 'Compute the variance of the CATE (default True).'},
        'input_example': {'forest': '<raw_handle>', 'estimate_variance': True},
    },
    'wrap_rdbwselect': {
        'fn': 'wrap_rdbwselect',
        'description': 'wrap_rdbwselect -- category 07-causality-policy, METHOD-SELECTION card #38.',
        'args': {'y': 'Handle to an outcome vector.', 'x': 'Handle to a running variable vector.', 'c': 'Cutoff (default 0).', 'p': 'Polynomial degree (default 1).', 'kernel': 'Kernel (default tri).', 'bwselect': 'Bandwidth selector (default mserd).', 'vce': 'Variance estimator (default nn).'},
        'input_example': {'y': '<raw_handle>', 'x': '<raw_handle>', 'c': 0},
    },
    'wrap_rdd_bw_ik': {
        'fn': 'wrap_rdd_bw_ik',
        'description': 'wrap_rdd_bw_ik -- category 07-causality-policy, METHOD-SELECTION card #39.',
        'args': {'rdd_object': 'Handle to an rdd_data object.', 'kernel': 'Kernel for the IK bandwidth (default Triangular).'},
        'input_example': {'rdd_object': '<raw_handle>'},
    },
    'wrap_rdd_data': {
        'fn': 'wrap_rdd_data',
        'description': 'wrap_rdd_data -- category 07-causality-policy, METHOD-SELECTION card #39.',
        'args': {'y': 'Handle to an outcome vector (no NA).', 'x': 'Handle to a running variable vector (same length as y).', 'cutpoint': 'Cutpoint inside the range of x.', 'z': 'Handle to a binary (0/1) treatment vector for fuzzy RD.'},
        'input_example': {'y': '<raw_handle>', 'x': '<raw_handle>', 'cutpoint': 0.5},
    },
    'wrap_rdd_reg_lm': {
        'fn': 'wrap_rdd_reg_lm',
        'description': 'wrap_rdd_reg_lm -- category 07-causality-policy, METHOD-SELECTION card #39.',
        'args': {'rdd_object': 'Handle to an rdd_data object (from wrap_rdd_data).', 'order': 'Polynomial degree (default 1).', 'slope': 'Slope on each side of the cutpoint (default separate).', 'bw': 'Bandwidth (default: all the data / global).'},
        'input_example': {'rdd_object': '<raw_handle>', 'order': 1},
    },
    'wrap_rdd_reg_np': {
        'fn': 'wrap_rdd_reg_np',
        'description': 'wrap_rdd_reg_np -- category 07-causality-policy, METHOD-SELECTION card #39.',
        'args': {'rdd_object': 'Handle to an rdd_data object (SHARP only).', 'bw': 'Bandwidth (default: IK optimal).', 'slope': 'Slope on each side of the cutpoint (default separate).', 'inference': 'Inference type (default np).'},
        'input_example': {'rdd_object': '<raw_handle>'},
    },
    'wrap_rdrobust': {
        'fn': 'wrap_rdrobust',
        'description': 'wrap_rdrobust -- category 07-causality-policy, METHOD-SELECTION card #38.',
        'args': {'y': 'Handle to an outcome vector (numeric, no NA).', 'x': 'Handle to a running variable vector (same length as y).', 'c': 'Cutoff of the running variable (default 0).', 'fuzzy': 'Handle to a treatment-status vector for fuzzy RD (default: sharp).', 'p': 'Local polynomial degree (default 1).', 'kernel': 'Kernel (default tri).', 'bwselect': 'Bandwidth selector (default mserd).', 'vce': 'Variance estimator (default nn).', 'level': 'Confidence level (0-100, default 95).'},
        'input_example': {'y': '<raw_handle>', 'x': '<raw_handle>', 'c': 0, 'level': 95},
    },
    'wrap_sandwich_blocks': {
        'fn': 'wrap_sandwich_blocks',
        'description': 'wrap_sandwich_blocks -- category 07-causality-policy, METHOD-SELECTION card #35.',
        'args': {'object': 'Handle to a fitted model; returns estfun/bread/meat.', 'adjust': 'Small-sample adjustment on the meat.'},
        'input_example': {'object': '<raw_handle>', 'adjust': False},
    },
    'wrap_scdata': {
        'fn': 'wrap_scdata',
        'description': 'wrap_scdata -- category 07-causality-policy, METHOD-SELECTION card #41.',
        'args': {'df': 'Handle to a long-format panel DataFrame.', 'id_var': 'Unit id column name.', 'time_var': 'Time column name.', 'outcome_var': 'Outcome column name.', 'period_pre': 'Handle to a vector of pre-treatment periods.', 'period_post': 'Handle to a vector of post-treatment periods.', 'unit_tr': 'Handle to the ID(s) of the treated unit.', 'unit_co': 'Handle to a vector of control-unit IDs (donor pool).', 'features': 'Feature column names (default: outcome).', 'constant': 'Add a constant (default False).', 'cointegrated_data': 'Treat the data as cointegrated (default False).'},
        'input_example': {'df': '<df_handle>', 'id_var': '...', 'time_var': '...', 'outcome_var': '...', 'period_pre': '<raw_handle>', 'period_post': '<raw_handle>', 'unit_tr': '<raw_handle>', 'unit_co': '<raw_handle>', 'constant': False, 'cointegrated_data': False},
    },
    'wrap_scest': {
        'fn': 'wrap_scest',
        'description': 'wrap_scest -- category 07-causality-policy, METHOD-SELECTION card #41.',
        'args': {'data': 'Handle to an scdata object (from wrap_scdata).', 'V': 'Weighting matrix scheme (default separate).', 'solver': 'Convex solver (default CLARABEL).'},
        'input_example': {'data': '<raw_handle>', 'solver': 'CLARABEL'},
    },
    'wrap_scpi': {
        'fn': 'wrap_scpi',
        'description': 'wrap_scpi -- category 07-causality-policy, METHOD-SELECTION card #41.',
        'args': {'data': 'Handle to an scdata (or scest) object.', 'V': 'Weighting matrix scheme (default separate).', 'u_sigma': 'In-sample (u) variance estimator (default HC1).', 'e_method': 'Out-of-sample (e) inference method (default all).', 'sims': 'Simulations for the prediction intervals (default 200).', 'solver': 'Convex solver (default CLARABEL).'},
        'input_example': {'data': '<raw_handle>', 'sims': 200, 'solver': 'CLARABEL'},
    },
    'wrap_synth': {
        'fn': 'wrap_synth',
        'description': 'wrap_synth -- category 07-causality-policy, METHOD-SELECTION card #40.',
        'args': {'dataprep_object': 'Handle to a dataprep object (from wrap_dataprep).', 'optimxmethod': 'Optimizer for the weights (default Nelder-Mead).', 'genoud': 'Genetic optimization (slower/more stable, default False).'},
        'input_example': {'dataprep_object': '<raw_handle>', 'genoud': False},
    },
    'wrap_synth_tab': {
        'fn': 'wrap_synth_tab',
        'description': 'wrap_synth_tab -- category 07-causality-policy, METHOD-SELECTION card #40.',
        'args': {'synth_object': 'Handle to a synth object (from wrap_synth).', 'dataprep_object': 'Handle to a dataprep object (from wrap_dataprep).', 'round_digit': 'Rounding decimals (default 3).'},
        'input_example': {'synth_object': '<raw_handle>', 'dataprep_object': '<raw_handle>', 'round_digit': 3},
    },
    'wrap_synthetic_control': {
        'fn': 'wrap_synthetic_control',
        'description': 'wrap_synthetic_control -- category 07-causality-policy, METHOD-SELECTION card #42.',
        'args': {'data': 'Handle to a long-format panel DataFrame.', 'outcome': 'Outcome column name.', 'unit': 'Unit id column name.', 'time': 'Time column name.', 'i_unit': 'ID of the treated unit.', 'i_time': 'Treatment start time.', 'generate_placebos': 'Generate placebo units for inference (default False).'},
        'input_example': {'data': '<df_handle>', 'outcome': '...', 'unit': '...', 'time': '...', 'i_unit': '...', 'i_time': 0.5, 'generate_placebos': False},
    },
    'wrap_variable_importance': {
        'fn': 'wrap_variable_importance',
        'description': 'wrap_variable_importance -- category 07-causality-policy, METHOD-SELECTION card #44.',
        'args': {'forest': 'Handle to a causal_forest (from wrap_causal_forest).', 'decay_exponent': 'Decay exponent for depth weighting (default 2).', 'max_depth': 'Maximum split-counting depth (default 4).'},
        'input_example': {'forest': '<raw_handle>', 'decay_exponent': 2, 'max_depth': 4},
    },
    'wrap_vcov_cl': {
        'fn': 'wrap_vcov_cl',
        'description': 'wrap_vcov_cl -- category 07-causality-policy, METHOD-SELECTION card #35.',
        'args': {'object': 'Handle to a fitted model.', 'cluster': 'Handle to a cluster variable (vector of the same length as the observations, >=2 levels).', 'type': 'HC type (default: HC1 for lm, otherwise HC0).', 'fix': 'Correct a non-positive-definite vcov.'},
        'input_example': {'object': '<raw_handle>', 'cluster': '<raw_handle>', 'fix': False},
    },
    'wrap_vcov_hac': {
        'fn': 'wrap_vcov_hac',
        'description': 'wrap_vcov_hac -- category 07-causality-policy, METHOD-SELECTION card #35.',
        'args': {'object': 'Handle to a fitted time-series model (lm).', 'method': 'NeweyWest (default, macro TS) or generic vcovHAC.', 'lag': 'Bandwidth/lag (default: auto bwNeweyWest).', 'prewhite': 'AR(1) prewhitening (NeweyWest default True).', 'adjust': 'Small-sample dof adjustment.', 'sandwich': 'True -> full sandwich vcov (default).'},
        'input_example': {'object': '<raw_handle>', 'sandwich': True},
    },
    'wrap_vcov_hc': {
        'fn': 'wrap_vcov_hc',
        'description': 'wrap_vcov_hc -- category 07-causality-policy, METHOD-SELECTION card #35.',
        'args': {'object': 'Handle to a fitted model (lm/glm/fixest; cross-section).', 'type': 'Heteroskedasticity-consistent type (default HC3).', 'sandwich': 'True -> full sandwich vcov (default).'},
        'input_example': {'object': '<raw_handle>', 'sandwich': True},
    },
    'wrap_vcov_panel': {
        'fn': 'wrap_vcov_panel',
        'description': 'wrap_vcov_panel -- category 07-causality-policy, METHOD-SELECTION card #35.',
        'args': {'object': 'Handle to a fitted model (panel).', 'cluster': 'Handle to a cluster/unit variable (vector).', 'order_by': 'Handle to a time-ordering variable within each cluster (vector).', 'method': 'PL (Driscoll-Kraay panel HAC, default) or PC (Beck-Katz).', 'kernel': "Kernel for method='PL' (default Bartlett).", 'pairwise': "Pairwise (unbalanced) for method='PC'.", 'fix': 'Correct a non-positive-definite vcov.'},
        'input_example': {'object': '<raw_handle>', 'cluster': '<raw_handle>', 'order_by': '<raw_handle>', 'pairwise': False, 'fix': False},
    },
}
