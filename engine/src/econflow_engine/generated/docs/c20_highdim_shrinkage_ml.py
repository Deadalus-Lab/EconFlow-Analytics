# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 20-highdim-shrinkage-ml: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'bma_average': {
        'fn': 'bma_average',
        'description': 'bma_average -- category 20-highdim-shrinkage-ml, method card #219.',
        'args': {'X_data': 'Handle to a numeric data matrix: 1st column = dependent y, remaining columns = regressors (K >= 1). Without NA/Inf; N > K+1.', 'mprior': 'Model prior (default uniform): uniform (each model equiprobable); fixed (fixed expected size); random (beta-binomial, Ley-Steel)· pip (fixed inclusion probs).', 'g': "g-prior: 'UIP' (unit info, g=N· default)· 'BRIC' (g=max(N,K^2))· 'RIC' (g=K^2)· 'HQ' (Hannan-Quinn), or a positive number as a string (e.g. '10') for a custom g.", 'mcmc': "Sampler (default enumerate): 'enumerate' = exact enumeration of ALL 2^K models (DETERMINISTIC; only K<=20 — prefer it there); 'bd' = birth-death MCMC; 'rev.jump' = reversible-jump MCMC. THE MCMC ARE STOCHASTIC and are NOT bit-reproducible even with a fixed seed (see $reproducibility in the output).", 'nmodel': 'Number of top models kept (default 100).', 'burn': 'MCMC burn-in draws (only for bd/rev.jump; default 1000).', 'iter': 'MCMC posterior draws (only for bd/rev.jump; default 3000).', 'mprior_size': 'Expected model size for fixed/random priors, in (0, K); default K/2 of the package.', 'seed': 'MCMC reproducibility seed (inert in enumerate; default 42).'},
        'input_example': {'X_data': '<matrix_handle>', 'nmodel': 100, 'burn': 1000, 'iter': 3000, 'seed': 42},
    },
    'bma_coefficients': {
        'fn': 'bma_coefficients',
        'description': 'bma_coefficients -- category 20-highdim-shrinkage-ml, method card #219.',
        'args': {'object': 'Handle to a fitted bma object (from bma_average register).', 'exact': 'True = analytical (exact) posterior moments· False = MCMC-frequency-based (default False· use True after enumerate).', 'order_by_pip': 'Sorting of regressors by descending PIP (default True).'},
        'input_example': {'object': '<raw_handle>', 'exact': False, 'order_by_pip': True},
    },
    'enet_cv': {
        'fn': 'enet_cv',
        'description': 'enet_cv -- category 20-highdim-shrinkage-ml, method card #216.',
        'args': {'x': 'Handle to a numeric design matrix X (n×p, p>=2, without NA/Inf).', 'y': 'Handle to the response y (length == the row count of x); gates per family as in enet_fit.', 'family': 'Distribution/loss (default gaussian).', 'alpha': 'Elastic-net mixing ∈ [0,1] (1=Lasso, 0=Ridge).', 'nfolds': 'Number of CV folds (>=3, <= n; default 10).', 'type_measure': 'CV metric (default = family default); auc only binomial; class only binomial/multinomial.', 'seed': 'Seed for DETERMINISTIC foldid (same seed => identical CV).', 'standardize': 'Standardization of predictors (default True).', 'intercept': 'Inclusion of intercept (default True).'},
        'input_example': {'x': '<matrix_handle>', 'y': '<matrix_handle>', 'alpha': 1, 'nfolds': 10, 'seed': 42, 'standardize': True, 'intercept': True},
    },
    'cv_group_penalized_regression': {
        'fn': 'cv_group_penalized_regression',
        'description': 'cv_group_penalized_regression -- category 20-highdim-shrinkage-ml, method card #220.',
        'args': {'X': 'Handle to a numeric design matrix X (n x p; >=1 column, >=2 rows, without NA/Inf). The columns correspond to the group labels.', 'y': 'Handle to a numeric response y of length the row count of X. binomial -> exactly {0,1}; poisson -> non-negative; without NA/Inf.', 'group': 'Grouping vector, length == the column count of X: the group integer of each column (0 = unpenalized/always-in group). None -> each column its own group (ordinary lasso).', 'penalty': 'Penalty: grLasso/grMCP/grSCAD select ENTIRE groups together; gel/cMCP are bi-level (select groups AND variables within a group). Default grLasso.', 'family': 'Family: gaussian (continuous y), binomial (binary y {0,1}), poisson (non-negative counts). Default gaussian.', 'nfolds': 'Number of folds in the cross-validation (>=3, <= n; default 10).', 'seed': 'Seed for the RANDOM assignment of folds (reproducibility; default 20240720). Same seed -> identical lambda_min.', 'nlambda': 'Number of lambda values in the regularization path (>=2, default 100).', 'gamma': 'Concavity parameter for MCP/SCAD (>1; default 3, or 4 for grSCAD).', 'alpha': 'Balance of group-penalty vs ridge, in (0,1] (default 1 = pure group penalty).'},
        'input_example': {'X': '<matrix_handle>', 'y': '<matrix_handle>', 'nfolds': 10, 'seed': 20240720, 'nlambda': 100, 'alpha': 1},
    },
    'enet_fit': {
        'fn': 'enet_fit',
        'description': 'enet_fit -- category 20-highdim-shrinkage-ml, method card #216.',
        'args': {'x': 'Handle to a numeric design matrix X (n×p, p>=2 columns, without NA/Inf). The predictors — NEVER in the schema, they pass as a handle.', 'y': 'Handle to the response y (length == the row count of x). gaussian: numeric; poisson: non-negative counts; binomial: 2 classes; multinomial: >=3.', 'family': 'Distribution/loss (default gaussian; binomial/poisson/multinomial).', 'alpha': 'Elastic-net mixing ∈ [0,1]: 1=Lasso (sparse), 0=Ridge, intermediate=Elastic-Net.', 'nlambda': 'Number of points on the lambda path (default 100).', 'standardize': 'Standardization of predictors before the fit (default True).', 'intercept': 'Inclusion of intercept (default True).'},
        'input_example': {'x': '<matrix_handle>', 'y': '<matrix_handle>', 'alpha': 1, 'nlambda': 100, 'standardize': True, 'intercept': True},
    },
    'boost_glm_cv': {
        'fn': 'boost_glm_cv',
        'description': 'boost_glm_cv -- category 20-highdim-shrinkage-ml, method card #218.',
        'args': {'x': 'Handle to a numeric design matrix X (n x p), without NA/Inf.', 'y': 'Handle to response y (length n); same requirements per family as in boost_glm_fit.', 'family': 'Loss family (default Gaussian). Binomial: $coefficients HALF those of glm ($coef_scale="mboost_half_logit"). QuantReg level = $offset+$intercept.', 'tau': 'Quantile in (0,1) when family="QuantReg" (default 0.5); needs enough mstop_max for a calibrated level.', 'mstop_max': 'Upper bound of boosting steps for the cvrisk grid (>= 2; default 200).', 'nu': 'Learning rate (shrinkage) in (0,1] (default 0.1).', 'center': 'Centering of predictors (default True).', 'cv_type': 'Resampling scheme of cvrisk (default subsampling).', 'cv_B': 'Number of resamples/folds (>= 2; default 25).', 'seed': 'Seed for generating the folds (reproducibility; default 42).'},
        'input_example': {'x': '<matrix_handle>', 'y': '<matrix_handle>', 'mstop_max': 200, 'cv_B': 25, 'seed': 42},
    },
    'boost_glm_fit': {
        'fn': 'boost_glm_fit',
        'description': 'boost_glm_fit -- category 20-highdim-shrinkage-ml, method card #218.',
        'args': {'x': 'Handle to a numeric design matrix X (n x p predictors), >= 3 rows, >= 1 column, without NA/Inf.', 'y': 'Handle to response y (length n). Gaussian/QuantReg/Laplace/Huber: numeric; Binomial: EXACTLY 2 values; Poisson: non-negative integers (counts).', 'family': 'Loss family (default Gaussian=L2). QuantReg=pinball(tau)· Laplace=L1· Huber=robust· Binomial=logistic· Poisson=counts. Binomial: the $coefficients are HALF those of glm(binomial) ($coef_scale="mboost_half_logit"; $positive_class=2nd level).', 'tau': 'Quantile in (0,1) when family="QuantReg" (default 0.5). The conditional-quantile level = $offset+$intercept and needs ENOUGH mstop to calibrate to tau.', 'mstop': 'Number of boosting steps (regularization; default 100; positive integer).', 'nu': 'Learning rate (shrinkage) in (0,1] (default 0.1).', 'center': 'Centering of predictors (default True; offset as intercept).'},
        'input_example': {'x': '<matrix_handle>', 'y': '<matrix_handle>', 'mstop': 100},
    },
    'enet_coefficients': {
        'fn': 'enet_coefficients',
        'description': 'enet_coefficients -- category 20-highdim-shrinkage-ml, method card #216.',
        'args': {'object': 'Handle to a elastic_net or the cross-validated elastic net fit (from enet_fit.model / enet_cv.cv register).', 'lambda': "Explicit lambda (non-negative). REQUIRED for a elastic_net path fit; for the cross-validated fit it overrides 'which'.", 'which': 'For the cross-validated fit: lambda_min (min CV error) or lambda_1se (parsimonious).'},
        'input_example': {'object': '<raw_handle>'},
    },
    'enet_predict': {
        'fn': 'enet_predict',
        'description': 'enet_predict -- category 20-highdim-shrinkage-ml, method card #216.',
        'args': {'object': 'Handle to a elastic_net or the cross-validated elastic net fit (from enet_fit/enet_cv register).', 'newx': 'Handle to a new design matrix (same p columns as the training x, without NA/Inf).', 'lambda': "Explicit lambda; REQUIRED for a elastic_net path fit; cv overrides 'which'.", 'which': 'For the cross-validated fit: lambda_min or lambda_1se.', 'type': 'link (linear predictor); response (probabilities/mean value); class (label — only binomial/multinomial).'},
        'input_example': {'object': '<raw_handle>', 'newx': '<matrix_handle>'},
    },
    'group_penalized_regression': {
        'fn': 'group_penalized_regression',
        'description': 'group_penalized_regression -- category 20-highdim-shrinkage-ml, method card #220.',
        'args': {'X': 'Handle to a numeric design matrix X (n x p; >=1 column, >=2 rows, without NA/Inf). The columns correspond to the group labels.', 'y': 'Handle to a numeric response y of length the row count of X. binomial -> exactly {0,1}; poisson -> non-negative; without NA/Inf.', 'group': 'Grouping vector, length == the column count of X: the group integer of each column (0 = unpenalized/always-in group). None -> each column its own group (ordinary lasso).', 'penalty': 'Penalty: grLasso/grMCP/grSCAD select ENTIRE groups together; gel/cMCP are bi-level (select groups AND variables within a group). Default grLasso.', 'family': 'Family: gaussian (continuous y), binomial (binary y {0,1}), poisson (non-negative counts). Default gaussian.', 'nlambda': 'Number of lambda values in the regularization path (>=2, default 100).', 'gamma': 'Concavity parameter for MCP/SCAD (>1; default 3, or 4 for grSCAD).', 'alpha': 'Balance of group-penalty vs ridge, in (0,1] (default 1 = pure group penalty).'},
        'input_example': {'X': '<matrix_handle>', 'y': '<matrix_handle>', 'nlambda': 100, 'alpha': 1},
    },
    'rf_fit': {
        'fn': 'rf_fit',
        'description': 'rf_fit -- category 20-highdim-shrinkage-ml, method card #217.',
        'args': {'x': 'Handle to the design matrix X (rows=observations, columns=variables), numeric, without NA/Inf, >= 2 rows.', 'y': 'Handle to the response y (numeric vector; length == the row count of x). Regression if numeric; set classification/probability=True for categorical (numerically coded -> factor).', 'num_trees': 'Number of trees (default 500; positive integer).', 'mtry': 'Variables tried per split (default: floor(sqrt(p))· <= the column count of x).', 'min_node_size': 'Minimum terminal-node size (default 5 regression / 1 classification).', 'importance': 'Variable importance: none; impurity (fast, biased toward high-cardinality)· impurity_corrected (bias-corrected)· permutation (more reliable, more expensive).', 'quantile_regression': 'True -> quantile regression forest (Meinshausen); requires REGRESSION; enables rf_predict type="quantiles".', 'probability': 'True -> probability forest (conditional class probabilities; y -> factor).', 'classification': 'True -> classification forest (label prediction· y -> factor).', 'seed': 'Reproducibility seed (num.threads pinned to 1 internally).'},
        'input_example': {'x': '<matrix_handle>', 'y': '<matrix_handle>', 'num_trees': 500, 'quantile_regression': False, 'probability': False, 'classification': False, 'seed': 42},
    },
    'rf_predict': {
        'fn': 'rf_predict',
        'description': 'rf_predict -- category 20-highdim-shrinkage-ml, method card #217.',
        'args': {'object': "Handle to a fitted random forest (from rf_fit register field 'model').", 'newdata': 'Handle to a design matrix (>= 1 row — a single out-of-sample observation is valid) with COLUMN NAMES matching the training variables (same set); anonymous/wrong newdata is blocked (a name-match gate, not positional).', 'type': 'response (point/label/probabilities); quantiles (requires a quantile-regression forest); se (jackknife SE; regression only).', 'quantiles': 'Quantiles in (0,1) for type="quantiles" (default 0.1,0.5,0.9).', 'se_method': 'SE method for type="se": infjack (infinitesimal jackknife) or jack.', 'seed': 'Reproducibility seed (type="se" draws from the random number generator).'},
        'input_example': {'object': '<raw_handle>', 'newdata': '<matrix_handle>', 'seed': 42},
    },
    'hd_advanced_lasso': {
        'fn': 'hd_advanced_lasso',
        'description': 'hd_advanced_lasso -- category 20-highdim-shrinkage-ml, method card #545.',
        'args': {'y': 'Outcome.', 'x': 'Covariate table.', 'method': 'Estimator.', 'lambda_': "Penalty; omitted = by the method's own rule.", 'robust_loadings': 'Use heteroskedasticity-robust penalty loadings.', 'n_folds': 'Folds when cross-validating.', 'seed': 'Seed for the random number generator.'},
        'input_example': {'y': '<series_handle>', 'x': '<df_handle>', 'method': 'sqrt_lasso', 'robust_loadings': True, 'n_folds': 10},
    },
    'hd_debiased_inference': {
        'fn': 'hd_debiased_inference',
        'description': 'hd_debiased_inference -- category 20-highdim-shrinkage-ml, method card #546.',
        'args': {'data': 'Data.', 'y': 'Outcome column.', 'd': 'Target regressor.', 'controls': 'Candidate control columns.', 'method': 'Method.', 'n_folds': 'Cross-fitting folds.', 'seed': 'Seed for the random number generator.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<df_handle>', 'y': '...', 'd': '...', 'method': 'double_selection', 'n_folds': 5, 'conf_level': 0.95},
    },
    'hd_gradient_boosting': {
        'fn': 'hd_gradient_boosting',
        'description': 'hd_gradient_boosting -- category 20-highdim-shrinkage-ml, method card #547.',
        'args': {'y': 'Outcome.', 'x': 'Covariate table.', 'objective': 'Objective.', 'n_estimators': 'Maximum boosting rounds.', 'learning_rate': 'Learning rate.', 'max_depth': 'Maximum tree depth.', 'early_stopping': 'Rounds without improvement before stopping.', 'validation_fraction': 'Held-out fraction for early stopping.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'y': '<series_handle>', 'x': '<df_handle>', 'objective': 'regression', 'n_estimators': 1000, 'learning_rate': 0.05, 'max_depth': 6, 'early_stopping': 50, 'validation_fraction': 0.2, 'seed': 1},
    },
    'hd_explain': {
        'fn': 'hd_explain',
        'description': 'hd_explain -- category 20-highdim-shrinkage-ml, method card #548.',
        'args': {'fit': 'Handle to a fitted model.', 'x': 'Data to explain.', 'method': 'Explanation method.', 'features': 'Features to explain; omitted = all.', 'n_repeats': 'Repeats for permutation importance.', 'seed': 'Seed for the random number generator.'},
        'input_example': {'fit': '<raw_handle>', 'x': '<df_handle>', 'method': 'shap', 'n_repeats': 10},
    },
    'hd_glassbox': {
        'fn': 'hd_glassbox',
        'description': 'hd_glassbox -- category 20-highdim-shrinkage-ml, method card #549.',
        'args': {'y': 'Outcome.', 'x': 'Covariate table.', 'objective': 'Objective.', 'interactions': 'Pairwise interaction terms included.', 'max_bins': 'Bins per feature.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'y': '<series_handle>', 'x': '<df_handle>', 'objective': 'regression', 'interactions': 10, 'max_bins': 256, 'seed': 1},
    },
    'hd_conformal': {
        'fn': 'hd_conformal',
        'description': 'hd_conformal -- category 20-highdim-shrinkage-ml, method card #550.',
        'args': {'fit': 'Handle to a fitted model.', 'x_calibration': 'Calibration covariates.', 'y_calibration': 'Calibration outcomes.', 'x_test': 'Covariates to predict for.', 'method': 'Conformal variant.', 'levels': 'Coverage levels.'},
        'input_example': {'fit': '<raw_handle>', 'x_calibration': '<df_handle>', 'y_calibration': '<series_handle>', 'x_test': '<df_handle>', 'method': 'cqr', 'levels': [0.9, 0.95]},
    },
    'hd_bayesian_shrinkage': {
        'fn': 'hd_bayesian_shrinkage',
        'description': 'hd_bayesian_shrinkage -- category 20-highdim-shrinkage-ml, method card #551.',
        'args': {'y': 'Outcome.', 'x': 'Covariate table.', 'prior': 'Shrinkage prior.', 'expected_nonzero': 'Prior guess at the number of non-zero coefficients.', 'draws': 'Posterior draws.', 'warmup': 'Warm-up draws.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'y': '<series_handle>', 'x': '<df_handle>', 'prior': 'horseshoe', 'draws': 2000, 'warmup': 1000, 'seed': 1},
    },
    'hd_gam_prediction': {
        'fn': 'hd_gam_prediction',
        'description': 'hd_gam_prediction -- category 20-highdim-shrinkage-ml, method card #552.',
        'args': {'y': 'Outcome.', 'x': 'Covariate table.', 'distribution': 'Response distribution.', 'n_splines': 'Basis functions per term.', 'selection': 'Penalty selection criterion.'},
        'input_example': {'y': '<series_handle>', 'x': '<df_handle>', 'distribution': 'normal', 'n_splines': 20, 'selection': 'gcv'},
    },
}
