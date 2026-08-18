# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 29-unsupervised-clustering: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'dm_cor_dist': {
        'fn': 'dm_cor_dist',
        'description': 'dm_cor_dist -- category 29-unsupervised-clustering, METHOD-SELECTION card #240.',
        'args': {'x': 'Handle to a NUMERIC matrix/DataFrame. NO NA/NaN/Inf (the distance routine does NOT error — it silently returns values with pairwise deletion)· >= 2 objects· unique row names. sliding-window subsequence is explicitly rejected input (Keogh gate).', 'cor_method': "Correlation coefficient (default 'pearson'): pearson (linear)· spearman (monotone, on ranks)· kendall (concordance, robust to outliers/small samples).", 'transform': "Transformation r -> distance (default 'one_minus'): one_minus d=1-r (the DIRECTION matters· range [0,2])· one_minus_abs d=1-|r| (opposite phase = 'similar'· range [0,1])· mantegna d=sqrt(2(1-r)) = a True metric (Mantegna 1999) — prefer it for ward.D2/MDS.", 'orientation': "REQUIRED, never guessed: which dimension holds the objects to be clustered. 'rows_are_objects' = objects (countries/units) in the ROWS, features in the columns· 'columns_are_objects' = series in the COLUMNS, time in the rows (typical macro panel)."},
        'input_example': {'x': '<matrix_handle>', 'orientation': 'rows_are_objects'},
    },
    'dm_dist': {
        'fn': 'dm_dist',
        'description': 'dm_dist -- category 29-unsupervised-clustering, METHOD-SELECTION card #240.',
        'args': {'x': 'Handle to a NUMERIC matrix/DataFrame. NO NA/NaN/Inf (the distance routine does NOT error — it silently returns values with pairwise deletion)· >= 2 objects· unique row names. sliding-window subsequence is explicitly rejected input (Keogh gate).', 'method': 'Metric of the distance routine (default \'euclidean\'): euclidean (L2)· maximum (sup-norm)· manhattan (L1)· canberra (sum |x-y|/(|x|+|y|)) — HARD GATE: NO negative value (the dist documentation: "intended for non-negative values (e.g., counts)»)· binary (asymmetric Jaccard over on/off) — HARD GATE: EVERY element ∈ {0,1}· on CONTINUOUS data everything is \'on\' and the matrix comes out SILENTLY FULL OF ZEROS (discretize first with bn_quantile_bins)· minkowski (Lp, with \'p\'). CAUTION: the metrics are NOT scale-invariant — standardize first if the units differ.', 'p': "Minkowski power (positive· default 2). Used ONLY when method='minkowski'· p<=0 -> hard gate («distance: invalid p»).", 'orientation': "REQUIRED, never guessed: which dimension holds the objects to be clustered. 'rows_are_objects' = objects (countries/units) in the ROWS, features in the columns· 'columns_are_objects' = series in the COLUMNS, time in the rows (typical macro panel)."},
        'input_example': {'x': '<matrix_handle>', 'p': 2, 'orientation': 'rows_are_objects'},
    },
    'dm_proxy_dist': {
        'fn': 'dm_proxy_dist',
        'description': 'dm_proxy_dist -- category 29-unsupervised-clustering, METHOD-SELECTION card #240.',
        'args': {'x': 'Handle to a NUMERIC matrix/DataFrame. NO NA/NaN/Inf (the distance routine does NOT error — it silently returns values with pairwise deletion)· >= 2 objects· unique row names. sliding-window subsequence is explicitly rejected input (Keogh gate).', 'method': "Metric of the extended distance routine (default 'cosine'). SHAPE/norm-based (NO zero row norm): cosine, angular, Chord, Geodesic. SCALE-aware: Mahalanobis (requires n > p AND a non-singular cov). COMPOSITIONAL/shares (require NON-negative & non-zero row sum): Bray, Soergel, Whittaker, Hellinger, Kullback, divergence, Wave, Podani, eJaccard. Euclidean/Manhattan/supremum/Minkowski/Canberra live in dm_dist· correlation in dm_cor_dist.", 'orientation': "REQUIRED, never guessed: which dimension holds the objects to be clustered. 'rows_are_objects' = objects (countries/units) in the ROWS, features in the columns· 'columns_are_objects' = series in the COLUMNS, time in the rows (typical macro panel)."},
        'input_example': {'x': '<matrix_handle>', 'orientation': 'rows_are_objects'},
    },
    'dw_dist_matrix': {
        'fn': 'dw_dist_matrix',
        'description': 'dw_dist_matrix -- category 29-unsupervised-clustering, METHOD-SELECTION card #243.',
        'args': {'x': 'Handle to a NUMERIC matrix/DataFrame with ONE series per object (country/indicator). NO NA/NaN/Inf· >= 2 series· >= 2 observations· UNIQUE names. sliding-window subsequence input is explicitly rejected (Keogh gate).', 'window_type': "REQUIRED, never guessed: global constraint on the warping path. 'none' = no band (allows PATHOLOGICAL alignments — one point matching dozens)· 'sakoechiba' = band ±window.size around the MAIN diagonal (requires window.size >= |N-M|)· 'slantedband' = band around the SLANTED diagonal [1,1]->[N,M] (correct choice for UNEQUAL-LENGTH series)· 'itakura' = Itakura parallelogram (slope [1/2,2] => requires 0.5 <= M/N < 2, WITHOUT window.size).", 'window_size': 'Band width in cells (NON-negative integer). REQUIRED for window.type=\'sakoechiba\'/\'slantedband\'· FORBIDDEN for \'none\'/\'itakura\' (would be ignored silently -> hard gate). For \'sakoechiba\' requires window.size >= |query_length - ref_length| otherwise "No warping path exists that is allowed by costraints".', 'step_pattern': "ONLY SYMMETRIC patterns (default 'symmetric2'): the cross-distance matrix is computed on the LOWER triangle, so an asymmetric pattern (asymmetric*) would SILENTLY give a wrong 'symmetric' matrix -> hard gate. 'symmetric1' is NOT normalized (incompatible with normalize=True).", 'transform': "EXPLICIT (gated) transformation per series — default 'none' = RAW data· NO silent detrending/differencing (normative gate). 'zscore' = (x-mean)/sd: comparison of SHAPE independent of level/scale (the standard of the DTW literature)· on a CONSTANT series (sd=0) -> hard gate (would give NaN silently).", 'normalize': "True = use normalizedDistance (distance / length constant, e.g. N+M) instead of the raw one — NECESSARY when comparing series of different length. Default False. With step.pattern='symmetric1' (norm = NA) -> hard gate.", 'orientation': "REQUIRED, never guessed: which dimension holds the SERIES. 'rows_are_objects' = one series per ROW (time in the columns)· 'columns_are_objects' = series in the COLUMNS, time in the rows (typical macro panel)."},
        'input_example': {'x': '<matrix_handle>', 'window_type': 'none', 'orientation': 'rows_are_objects'},
    },
    'dw_dtw': {
        'fn': 'dw_dtw',
        'description': 'dw_dtw -- category 29-unsupervised-clustering, METHOD-SELECTION card #243.',
        'args': {'query': 'Handle to the QUERY SERIES (numeric/ts, >= 2 observations, WITHOUT NA/NaN/Inf). It may have a DIFFERENT length from the reference — that is the point of DTW.', 'reference': 'Handle to the REFERENCE SERIES (numeric/ts, >= 2 observations, WITHOUT NA/NaN/Inf).', 'window_type': "REQUIRED, never guessed: global constraint on the warping path. 'none' = no band (allows PATHOLOGICAL alignments — one point matching dozens)· 'sakoechiba' = band ±window.size around the MAIN diagonal (requires window.size >= |N-M|)· 'slantedband' = band around the SLANTED diagonal [1,1]->[N,M] (correct choice for UNEQUAL-LENGTH series)· 'itakura' = Itakura parallelogram (slope [1/2,2] => requires 0.5 <= M/N < 2, WITHOUT window.size).", 'window_size': 'Band width in cells (NON-negative integer). REQUIRED for window.type=\'sakoechiba\'/\'slantedband\'· FORBIDDEN for \'none\'/\'itakura\' (would be ignored silently -> hard gate). For \'sakoechiba\' requires window.size >= |query_length - ref_length| otherwise "No warping path exists that is allowed by costraints".', 'step_pattern': "Local transition rules (default 'symmetric2' = the default of dtw· normalizable by N+M). 'symmetric1' is NOT normalized (normalizedDistance = NA)· 'asymmetric*' match every point of the query EXACTLY ONCE (norm = N) but d(a,b) != d(b,a)· '*P0/P05/P1/P2' = increasing slope constraints Sakoe-Chiba (P2 = strictest· a path may not exist for series of very unequal length).", 'transform': "EXPLICIT (gated) transformation per series — default 'none' = RAW data· NO silent detrending/differencing (normative gate). 'zscore' = (x-mean)/sd: comparison of SHAPE independent of level/scale (the standard of the DTW literature)· on a CONSTANT series (sd=0) -> hard gate (would give NaN silently).", 'distance_only': 'True = distance only (faster, WITHOUT backtrack => index1/index2 = null). False (default) = also returns the warping path as numeric chart-data for drawing in the frontend.'},
        'input_example': {'query': '<series_handle>', 'reference': '<series_handle>', 'window_type': 'none'},
    },
    'hc_agnes': {
        'fn': 'hc_agnes',
        'description': 'hc_agnes -- category 29-unsupervised-clustering, METHOD-SELECTION card #242.',
        'args': {'d': "Handle to a 'dist' object (distance matrix· typically from the distance-matrix node). NO matrix/DataFrame — NO NA/Inf, NO negative dissimilarities, n >= 2.", 'method': "Agglomeration method (default 'average' = the documented default of the agglomerative-clustering routine). method='ward' is equivalent to hclust(method='ward.D2').", 'par_method': "Lance-Williams coefficients of length 1, 3 or 4 — ONLY for method='flexible' (REQUIRED, without default) or 'gaverage' (default -0.1). In other methods it is blocked (it would be ignored silently).", 'k': "Number of groups for cutting the tree (1..n). Give EXACTLY one of 'k' or 'h' (or neither = dendrogram data only).", 'h': "Cut height of the tree (>= 0· only on a monotone tree). Give EXACTLY one of 'k' or 'h'."},
        'input_example': {'d': '<raw_handle>'},
    },
    'hc_cutree': {
        'fn': 'hc_cutree',
        'description': 'hc_cutree -- category 29-unsupervised-clustering, METHOD-SELECTION card #242.',
        'args': {'tree': "Handle to an hclust or agnes/diana ('twins') tree — from the register of hc_hclust/hc_agnes/hc_diana.", 'k': "Number of groups (1..n). EXACTLY one of 'k'/'h' (required).", 'h': "Cut height (>= 0· only on a monotone tree). EXACTLY one of 'k'/'h' (required)."},
        'input_example': {'tree': '<raw_handle>'},
    },
    'hc_diana': {
        'fn': 'hc_diana',
        'description': 'hc_diana -- category 29-unsupervised-clustering, METHOD-SELECTION card #242.',
        'args': {'d': "Handle to a 'dist' object (distance matrix· typically from the distance-matrix node). NO matrix/DataFrame — NO NA/Inf, NO negative dissimilarities, n >= 2.", 'k': "Number of groups for cutting the tree (1..n). Give EXACTLY one of 'k' or 'h' (or neither = dendrogram data only).", 'h': "Cut height of the tree (>= 0· only on a monotone tree). Give EXACTLY one of 'k' or 'h'."},
        'input_example': {'d': '<raw_handle>'},
    },
    'hc_hclust': {
        'fn': 'hc_hclust',
        'description': 'hc_hclust -- category 29-unsupervised-clustering, METHOD-SELECTION card #242.',
        'args': {'d': "Handle to a 'dist' object (distance matrix· typically from the distance-matrix node). NO matrix/DataFrame — NO NA/Inf, NO negative dissimilarities, n >= 2.", 'method': "Agglomeration method (default 'complete' = the documented default of the hierarchical-clustering routine). CAUTION: 'ward.D2' implements the Ward (1963) criterion (Murtagh & Legendre 2014)· 'ward.D' does NOT implement it — they are not equivalent. 'median'/'centroid' can produce inversions.", 'k': "Number of groups for cutting the tree (1..n). Give EXACTLY one of 'k' or 'h' (or neither = dendrogram data only).", 'h': "Cut height of the tree (>= 0· only on a monotone tree). Give EXACTLY one of 'k' or 'h'."},
        'input_example': {'d': '<raw_handle>'},
    },
    'km_gap': {
        'fn': 'km_gap',
        'description': 'km_gap -- category 29-unsupervised-clustering, METHOD-SELECTION card #241.',
        'args': {'x': 'Handle to a NUMERIC observations×features matrix (rows = observations/countries, columns = variables). NO NA/NaN/Inf. sliding-window subsequence IS REJECTED matrix (Keogh gate).', 'k_max': 'Maximum k to examine (default 8)· >= 2 AND <= min(n-1, DISTINCT rows).', 'fun_cluster': 'Algorithm inside the gap loop (default kmeans· pam = robust).', 'B': 'Number of Monte-Carlo (bootstrap) reference samples (default 100· B=500 for final results).', 'd_power': 'Power of the euclidean distances in W(k): 1 = the conventional implementation (default)· 2 = proposal Tibshirani et al.', 'space_h0': 'Space of the H0 distribution of "no cluster" (default scaledPCA = uniform over a PCA-rotated hypercube).', 'method': 'maxSE rule for the optimal k (default firstSEmax = first local maximum within 1 SE)· Tibs2001SEmax = the original Tibshirani rule.', 'se_factor': 'Multiplier of the "1-SE" rule (positive· default 1).', 'nstart': 'nstart of the inner kmeans (>= 2· default 25).', 'iter_max': 'iter.max of the inner kmeans (default 50).', 'metric': 'Dissimilarity metric (default euclidean· manhattan = more robust).', 'transform': "EXPLICIT transformation BEFORE the clustering (default 'none' — NO silent standardization/detrending): center (mean removal per column)· scale (z-score· forbidden on a zero-variance column)· log (requires > 0). The fitted params are returned (transform_center/transform_scale).", 'seed': 'REQUIRED seed — clusGap is bootstrap (default 1234).'},
        'input_example': {'x': '<matrix_handle>', 'k_max': 8, 'B': 100, 'd_power': 1, 'se_factor': 1, 'nstart': 25, 'iter_max': 50, 'seed': 1234},
    },
    'km_kmeans': {
        'fn': 'km_kmeans',
        'description': 'km_kmeans -- category 29-unsupervised-clustering, METHOD-SELECTION card #241.',
        'args': {'x': 'Handle to a NUMERIC observations×features matrix (rows = observations/countries, columns = variables). NO NA/NaN/Inf. sliding-window subsequence IS REJECTED matrix (Keogh gate).', 'k': 'Number of clusters. MUST be 1 <= k <= number of DISTINCT rows (NOT n: duplicate rows break k<n).', 'transform': "EXPLICIT transformation BEFORE the clustering (default 'none' — NO silent standardization/detrending): center (mean removal per column)· scale (z-score· forbidden on a zero-variance column)· log (requires > 0). The fitted params are returned (transform_center/transform_scale).", 'algorithm': 'Algorithm (default Hartigan-Wong, the best)· Lloyd/Forgy = the same algorithm· Lloyd/Forgy can leave an EMPTY cluster -> hard gate.', 'nstart': 'Number of random initializations (default 25). REQUIRED >= 2 (determinism).', 'iter_max': 'Maximum iterations per start (kmeans iter.max· default 50).', 'seed': 'REQUIRED seed — kmeans has random initialization (default 1234). Same seed => identical result.'},
        'input_example': {'x': '<matrix_handle>', 'k': 1, 'nstart': 25, 'iter_max': 50, 'seed': 1234},
    },
    'km_pam': {
        'fn': 'km_pam',
        'description': 'km_pam -- category 29-unsupervised-clustering, METHOD-SELECTION card #241.',
        'args': {'x': 'Handle to a NUMERIC observations×features matrix (rows = observations/countries, columns = variables). NO NA/NaN/Inf. sliding-window subsequence IS REJECTED matrix (Keogh gate).', 'k': 'Number of clusters· 1 <= k <= n-1 AND k <= number of DISTINCT rows (pam does NOT error on a larger k: it returns duplicate medoids).', 'metric': 'Dissimilarity metric (default euclidean· manhattan = more robust).', 'stand': "pam standardization (mean-absolute-deviation per column· default False). FORBIDDEN together with transform='scale' (double standardization).", 'transform': "EXPLICIT transformation BEFORE the clustering (default 'none' — NO silent standardization/detrending): center (mean removal per column)· scale (z-score· forbidden on a zero-variance column)· log (requires > 0). The fitted params are returned (transform_center/transform_scale)."},
        'input_example': {'x': '<matrix_handle>', 'k': 1, 'stand': False},
    },
    'km_silhouette': {
        'fn': 'km_silhouette',
        'description': 'km_silhouette -- category 29-unsupervised-clustering, METHOD-SELECTION card #241.',
        'args': {'x': 'Handle to a NUMERIC observations×features matrix (rows = observations/countries, columns = variables). NO NA/NaN/Inf. sliding-window subsequence IS REJECTED matrix (Keogh gate).', 'cluster': "Integer assignment vector of length n with CONTIGUOUS ids 1..k (e.g. the 'cluster' field of a km_kmeans/km_pam node). Required: 2 <= k <= n-1: with k=1 silhouette returns NA WITHOUT an error.", 'metric': 'Dissimilarity metric (default euclidean· manhattan = more robust).', 'transform': "EXPLICIT transformation BEFORE the clustering (default 'none' — NO silent standardization/detrending): center (mean removal per column)· scale (z-score· forbidden on a zero-variance column)· log (requires > 0). The fitted params are returned (transform_center/transform_scale)."},
        'input_example': {'x': '<matrix_handle>', 'cluster': [1, 1]},
    },
    'mb_bic': {
        'fn': 'mb_bic',
        'description': 'mb_bic -- category 29-unsupervised-clustering, METHOD-SELECTION card #244.',
        'args': {'x': 'Handle to a NUMERIC observations×features matrix (rows = observations/countries, columns = variables). NO NA/NaN/Inf (mclust SILENTLY DROPS rows with NA). n > p IS REQUIRED (p >= n => singular covariances, Mclust does NOT error). sliding-window IS REJECTED subsequence matrix (Keogh gate).', 'G': 'Range of the number of components to examine (default 1:9). Positive integers with max(G) <= n — mclust does NOT error on a larger G: it SILENTLY truncates the range.', 'model_names': 'Geometric covariance shapes to try (default None = all the allowed ones). Multivariate (p>1): EII VII EEI VEI EVI VVI EEE VEE EVE VVE EEV VEV EVV VVV (volume-shape-orientation: E=equal, V=variable, I=identity). Univariate (p=1): E (equal variance) / V (unequal).', 'transform': "EXPLICIT transformation BEFORE the clustering (default 'none' — NO silent standardization/detrending): center (mean removal per column)· scale (z-score· forbidden on a zero-variance column)· log (requires > 0). The fitted params are returned (transform_center/transform_scale) and are applied VERBATIM to mb_predict's newdata.", 'top': 'Number of top candidates (model, G) returned (default 3).', 'seed': "Reproducibility seed (default 1234). For n <= mclust.options('subset') (=2000) the initialization is deterministic (model-based hierarchical)· ABOVE that mclust initializes on a RANDOM subset => the seed DETERMINES the result (field 'subset_init')."},
        'input_example': {'x': '<matrix_handle>', 'top': 3, 'seed': 1234},
    },
    'mb_icl': {
        'fn': 'mb_icl',
        'description': 'mb_icl -- category 29-unsupervised-clustering, METHOD-SELECTION card #244.',
        'args': {'x': 'Handle to a NUMERIC observations×features matrix (rows = observations/countries, columns = variables). NO NA/NaN/Inf (mclust SILENTLY DROPS rows with NA). n > p IS REQUIRED (p >= n => singular covariances, Mclust does NOT error). sliding-window IS REJECTED subsequence matrix (Keogh gate).', 'G': 'Range of the number of components to examine (default 1:9). Positive integers with max(G) <= n — mclust does NOT error on a larger G: it SILENTLY truncates the range.', 'model_names': 'Geometric covariance shapes to try (default None = all the allowed ones). Multivariate (p>1): EII VII EEI VEI EVI VVI EEE VEE EVE VVE EEV VEV EVV VVV (volume-shape-orientation: E=equal, V=variable, I=identity). Univariate (p=1): E (equal variance) / V (unequal).', 'transform': "EXPLICIT transformation BEFORE the clustering (default 'none' — NO silent standardization/detrending): center (mean removal per column)· scale (z-score· forbidden on a zero-variance column)· log (requires > 0). The fitted params are returned (transform_center/transform_scale) and are applied VERBATIM to mb_predict's newdata.", 'top': 'Number of top candidates (model, G) returned (default 3).', 'seed': "Reproducibility seed (default 1234). For n <= mclust.options('subset') (=2000) the initialization is deterministic (model-based hierarchical)· ABOVE that mclust initializes on a RANDOM subset => the seed DETERMINES the result (field 'subset_init')."},
        'input_example': {'x': '<matrix_handle>', 'top': 3, 'seed': 1234},
    },
    'mb_mclust': {
        'fn': 'mb_mclust',
        'description': 'mb_mclust -- category 29-unsupervised-clustering, METHOD-SELECTION card #244.',
        'args': {'x': 'Handle to a NUMERIC observations×features matrix (rows = observations/countries, columns = variables). NO NA/NaN/Inf (mclust SILENTLY DROPS rows with NA). n > p IS REQUIRED (p >= n => singular covariances, Mclust does NOT error). sliding-window IS REJECTED subsequence matrix (Keogh gate).', 'G': 'Range of the number of components to examine (default 1:9). Positive integers with max(G) <= n — mclust does NOT error on a larger G: it SILENTLY truncates the range.', 'model_names': 'Geometric covariance shapes to try (default None = all the allowed ones). Multivariate (p>1): EII VII EEI VEI EVI VVI EEE VEE EVE VVE EEV VEV EVV VVV (volume-shape-orientation: E=equal, V=variable, I=identity). Univariate (p=1): E (equal variance) / V (unequal).', 'transform': "EXPLICIT transformation BEFORE the clustering (default 'none' — NO silent standardization/detrending): center (mean removal per column)· scale (z-score· forbidden on a zero-variance column)· log (requires > 0). The fitted params are returned (transform_center/transform_scale) and are applied VERBATIM to mb_predict's newdata.", 'seed': "Reproducibility seed (default 1234). For n <= mclust.options('subset') (=2000) the initialization is deterministic (model-based hierarchical)· ABOVE that mclust initializes on a RANDOM subset => the seed DETERMINES the result (field 'subset_init')."},
        'input_example': {'x': '<matrix_handle>', 'seed': 1234},
    },
    'mb_predict': {
        'fn': 'mb_predict',
        'description': 'mb_predict -- category 29-unsupervised-clustering, METHOD-SELECTION card #244.',
        'args': {'x': 'Handle to a NUMERIC observations×features matrix (rows = observations/countries, columns = variables). NO NA/NaN/Inf (mclust SILENTLY DROPS rows with NA). n > p IS REQUIRED (p >= n => singular covariances, Mclust does NOT error). sliding-window IS REJECTED subsequence matrix (Keogh gate).', 'newdata': "Handle to a NUMERIC matrix of new observations with EXACTLY the same columns (same count AND same names/order) as 'x'. predict.Mclust checks ONLY ncol => a shuffled column order would give WRONG assignments (silent-wrong) — it is blocked by a hard gate.", 'G': 'Range of the number of components to examine (default 1:9). Positive integers with max(G) <= n — mclust does NOT error on a larger G: it SILENTLY truncates the range.', 'model_names': 'Geometric covariance shapes to try (default None = all the allowed ones). Multivariate (p>1): EII VII EEI VEI EVI VVI EEE VEE EVE VVE EEV VEV EVV VVV (volume-shape-orientation: E=equal, V=variable, I=identity). Univariate (p=1): E (equal variance) / V (unequal).', 'transform': "EXPLICIT transformation BEFORE the clustering (default 'none' — NO silent standardization/detrending): center (mean removal per column)· scale (z-score· forbidden on a zero-variance column)· log (requires > 0). The fitted params are returned (transform_center/transform_scale) and are applied VERBATIM to mb_predict's newdata.", 'seed': "Reproducibility seed (default 1234). For n <= mclust.options('subset') (=2000) the initialization is deterministic (model-based hierarchical)· ABOVE that mclust initializes on a RANDOM subset => the seed DETERMINES the result (field 'subset_init')."},
        'input_example': {'x': '<matrix_handle>', 'newdata': '<matrix_handle>', 'seed': 1234},
    },
    'mds_cmdscale': {
        'fn': 'mds_cmdscale',
        'description': 'mds_cmdscale -- category 29-unsupervised-clustering, METHOD-SELECTION card #245.',
        'args': {'d': "Handle to a 'dist' object (distance matrix· typically from the distance-matrix node). NO matrix/DataFrame (they are silently accepted even when they are NOT symmetric) — NO NA/Inf, NO negative dissimilarities, NOT all zero, n >= 2.", 'k': 'Number of dimensions of the map (default 2 = the documented default). MUST be in {1, 2,.. n-1}· in addition the POSITIVE eigenvalues must be >= k (otherwise the solution has fewer columns -> the node blocks).', 'add': 'True = compute the Cailliez additive constant (1983) so that the dissimilarities become EUCLIDEAN (default False). Useful ONLY when there are negative eigenvalues (n_eig_negative > 0 / gof_abs < gof_pos).'},
        'input_example': {'d': '<raw_handle>'},
    },
    'mds_isomds': {
        'fn': 'mds_isomds',
        'description': 'mds_isomds -- category 29-unsupervised-clustering, METHOD-SELECTION card #245.',
        'args': {'d': "Handle to a 'dist' object (distance matrix· typically from the distance-matrix node). NO matrix/DataFrame (they are silently accepted even when they are NOT symmetric) — NO NA/Inf, NO negative dissimilarities, NOT all zero, n >= 2.", 'k': 'Number of dimensions of the map (default 2 = the documented default). MUST be in {1, 2,.. n-1}· in addition the POSITIVE eigenvalues must be >= k (otherwise the solution has fewer columns -> the node blocks).', 'maxit': 'Maximum iterations (default 50· typically converges in ~10). Positive integer — 0 is SILENTLY accepted by MASS and returns a NON-optimized configuration.', 'tol': 'Convergence tolerance (default 0.001). MUST be > 0 — non-positive is silently accepted and it stops prematurely with much worse stress.', 'p': 'Minkowski power in the configuration space (default 2 = Euclidean). MUST be >= 1 (the Minkowski is a metric only for p >= 1· p = 0 does NOT terminate).'},
        'input_example': {'d': '<raw_handle>'},
    },
    'mds_sammon': {
        'fn': 'mds_sammon',
        'description': 'mds_sammon -- category 29-unsupervised-clustering, METHOD-SELECTION card #245.',
        'args': {'d': "Handle to a 'dist' object (distance matrix· typically from the distance-matrix node). NO matrix/DataFrame (they are silently accepted even when they are NOT symmetric) — NO NA/Inf, NO negative dissimilarities, NOT all zero, n >= 2.", 'k': 'Number of dimensions of the map (default 2 = the documented default). MUST be in {1, 2,.. n-1}· in addition the POSITIVE eigenvalues must be >= k (otherwise the solution has fewer columns -> the node blocks).', 'niter': 'Maximum iterations (default 100· typically converges in ~50). Positive integer — 0 is SILENTLY accepted (no optimization).', 'magic': 'Initial step of the diagonal-Newton (default 0.2). MUST be > 0 — magic <= 0 is SILENTLY accepted and does NOT optimize at all.', 'tol': 'Termination tolerance in stress units (default 0.0001· > 0).'},
        'input_example': {'d': '<raw_handle>'},
    },
}
