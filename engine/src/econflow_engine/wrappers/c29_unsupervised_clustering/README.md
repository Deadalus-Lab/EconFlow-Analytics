<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 29-unsupervised-clustering

6 METHOD-SELECTION cards, 6 modules, 20 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #240 — DISTANCE / dissimilarity matrix between objects: dist (the 6 documented metrics), correlation-based dissimilarity (1-r | 1-|r| | sqrt(2(1-r)) Mantegna), dist (14 further shape/compositional/Mahalanobis metrics)

**Module:** `distance_dissimilarity_matrix.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `dm_dist` | `x`, `orientation` | `matrix_handle`, `enum`, `number`, `enum` | `p=2` | `light` | `dist_object` |
| `dm_cor_dist` | `x`, `orientation` | `matrix_handle`, `enum`, `enum`, `enum` | — | `light` | `dist_object` |
| `dm_proxy_dist` | `x`, `orientation` | `matrix_handle`, `enum`, `enum` | — | `light` | `dist_object` |

### Use when

the FIRST node of every unsupervised flow: it produces the dissimilarity matrix between «objects» (countries, macro series, regimes) that is the MANDATORY input to hierarchical clustering (#242 hclust/agnes/diana), PAM/silhouette (#241) and MDS (#245); the ORIENTATION (objects in the rows vs in the columns) is an EXPLICIT required argument and is NEVER guessed

### Do not use when

sliding-window subsequences of a time series (the KEOGH GATE — a hard stop); shape-based similarity robust to time shifts -> DTW (#243); the cross-distance between TWO DIFFERENT sets (proxy y=/pairwise -> the DTW node #243); mixed-type (numeric + categorical) data (daisy/Gower — not exposed); testing the SIGNIFICANCE of a correlation (p-values/CI) -> #81 desc_cor_test (c00_data_utilities/descriptive_statistics); filtering collinear COLUMNS -> #252 cf_find_correlation (c00_data_utilities/correlation_filter_greedy); charts/heatmaps (the frontend, §5); a single series (n>=2 objects are required)

### Prerequisites

- c00_data_utilities/fast_row_column.panel_col_stats # (stat='sd') ZERO VARIANCE before dm_cor_dist: cor only WARNS «the standard deviation is zero» and returns NA
- c00_data_utilities/descriptive_statistics.desc_correlations # look at the r matrix BEFORE choosing a transform (one_minus if the DIRECTION matters; one_minus_abs if the opposite phase counts as «similar»)
- dm_dist # run the euclidean distance first and look at n_zero_pairs: >0 means DUPLICATE objects -> a trap in isoMDS (#245) and the bound k<=distinct in #241

### Alternatives

| instead use | when |
| --- | --- |
| dm_dist (euclidean/maximum/manhattan/canberra/binary/minkowski) | the objects are compared on the SAME magnitude scale (index levels): euclidean=L2 (default); manhattan=L1 (more robust to outliers); maximum=the sup norm; canberra ONLY for NON-negative counts; binary=an asymmetric Jaccard on on/off data; minkowski=Lp with an explicit p>0 |
| dm_cor_dist (transform='mantegna') | you want a GENUINE metric from correlations — d=sqrt(2(1-r)) satisfies the triangle inequality (Mantegna 1999); PREFER it when ward.D2 (#242) or classical MDS (#245) follows, since both presuppose a euclidean/metric structure |
| dm_cor_dist (transform='one_minus' \| 'one_minus_abs') | synchronisation of SHAPE (co-movement) rather than a distance between levels: one_minus (d=1-r, range [0,2]) when the DIRECTION matters (countercyclical series = FAR apart); one_minus_abs (d=1-\|r\|, range [0,1]) when the opposite phase counts as SIMILARITY |
| dm_cor_dist (cor_method='spearman' \| 'kendall') | a non-linear monotone relation or extreme values/heavy tails: spearman (ranks); kendall (concordance, small samples); pearson ONLY for a linear relation |
| dm_proxy_dist (cosine/angular/Chord/Geodesic) | you want the ANGLE (the shape of the profile) and NOT the magnitude — two countries with the same mix but a different scale are «close»; it requires a NON-zero row norm |
| dm_proxy_dist (Bray/Soergel/Whittaker/Hellinger/Kullback/divergence/Wave/Podani/eJaccard) | compositional/abundance data (shares, basket compositions, trade weights): NON-negative AND with a non-zero row sum |
| dm_proxy_dist (Mahalanobis) | the variables are CORRELATED and you want a distance decorrelated/scaled by the covariance matrix; it requires n > p AND a non-singular cov (otherwise a hard gate) |
| #243 dtw-distance (DTW) | the objects are TIME SERIES with a time shift/a different phase speed (leading/lagging cycles) — the lock-step euclidean distance would call them dissimilar |

### Output fields

- distance_matrix: the full SYMMETRIC n×n double matrix with dimnames = the labels — the main chart-data (a distance map / heatmap in the frontend, §5)
- lower_tri: the lower triangle BY COLUMN (of length n(n-1)/2, the storage of class 'dist') + labels + n_objects + n_features
- min_distance / max_distance / mean_distance: a summary of the scale — if the range is ~0 there is no structure to cluster
- n_zero_pairs: the number of pairs at distance EXACTLY 0 (DUPLICATE objects) — a value >0 WARNS of: isoMDS «zero or negative distance between objects i and j» (#245), all heights zero in hclust (#242), k <= the number of DISTINCT rows (#241)
- dist_object: the object of class 'dist' ITSELF -> register(field='dist_object') in ALL 3 functions; the PRODUCER node of the category (a handle -> #241/#242/#245). SERIALIZATION (the L2 to_mcp.dist): {lower_tri (the lower triangle BY COLUMN), length, Size, Labels, method} — an EXPLICIT S3 method, because merely loading the proxy namespace registers engine-wide dim.dist/names.dist and the default path produced dim=c(n,n) for a vector of length n(n-1)/2, LOST the length and filled in spurious names. The FULL symmetric matrix is NOT repeated there — it ALREADY exists as distance_matrix
- method / orientation / family: what was computed EXACTLY (family = 'dist' \| 'cor + as.dist' \| 'dist'); p = the Minkowski power ONLY when method='minkowski' (otherwise NA_real_)
- dm_cor_dist additionally: correlation_matrix (the n×n r matrix with dimnames — chart-data AND the interpretation of the sign) + cor_method + transform

### Pitfalls

- NORMATIVE GATE 1 (KEOGH): a sliding-window subsequence input is REJECTED explicitly — the overlap of consecutive rows is detected at ANY fixed step k >= 1 (NOT only k=1: the «slide» is a free parameter of how the subsequences are built, so a step-2 window is covered by the result just as much), in both directions; k <= floor(m/2) so that the overlap stays >= 50%. The detection lives ONCE in the reference/gate_sliding_window_step (shared by #240/#241/#243/#244). Clustering subsequences is PROVABLY meaningless: the output does NOT depend on the input (the centers degenerate into sine waves regardless of the data/k/algorithm; Keogh, Lin & Truppel). Whole-series clustering is NOT affected
- NORMATIVE GATE 2 (do NOT impose detrending): the node NEVER transforms the input silently — no differencing, no seasonal adjustment, no standardization. The choice of metric/transform is an EXPLICIT gated option (match.arg); the macro clustering literature (arXiv:1807.04004) DELIBERATELY uses raw, non-seasonally-adjusted, non-detrended data (detrending introduces artificial distortions — Hamilton on the HP filter)
- ORIENTATION is required=TRUE: 'rows_are_objects' (countries/units in the rows) vs 'columns_are_objects' (series in the columns, time in the rows = the typical macro panel). The WRONG orientation does NOT error — it gives a completely different, apparently valid matrix (silently wrong); which is why there is no default
- SILENTLY WRONG (documented, the dist routine): «Missing values are allowed, and are excluded from all computations involving the rows within which they occur.. the sum is scaled up proportionally to the number of columns used» ⇒ dist does NOT error on NA — it returns a rescaled value. We impose a HARD gate on NA/NaN/Inf (the same for dist)
- SILENTLY WRONG: zero variance of an object in dm_cor_dist -> cor only WARNS «the standard deviation is zero» and returns NA ⇒ a hard gate (the offending objects are named); plus a gate of >= 3 observations per object (with 2 points r = ±1 ALWAYS = degenerate)
- THE METRICS ARE NOT SCALE-INVARIANT: a variable in units (e.g. GDP in millions) dominates the euclidean distance over one in percentages. Standardization is an EXPLICIT DECISION upstream (or the transform in #241) — NEVER silent here
- SILENTLY WRONG (proxy, live-verified): a zero row norm -> cosine SILENTLY returns 1 while angular/Chord/Geodesic SILENTLY return NaN; negative values in compositional metrics -> Hellinger/Kullback only WARN «NaNs produced» and the rest return meaningless numbers; Mahalanobis with n<=p or collinear columns -> «Lapack routine dgesv: system is exactly singular». ALL THREE are hard gates per metric FAMILY, PLUS a universal post-check (no non-finite, no NEGATIVE distance)
- MASKING (CRITICAL, live-verified): NEVER library(proxy) — nor library(dtw), which ATTACHES proxy: the attach MASKS dist, as.dist AND as_matrix in the shared source env. We use requireNamespace + fully qualified proxy::/stats::/. CAUTION: even a BARE loadNamespace('proxy') registers S3 methods for class 'dist' ([, [[, dim, dimnames, names, subset) ⇒ dim(d) becomes c(n,n) and names(d) becomes non-NULL. THE RULE for every sibling node: use attr(d,'Labels')/attr(d,'Size'), NEVER names(d)/dim(d)
- 1-r vs 1-\|r\| vs Mantegna: ONLY sqrt(2(1-r)) is a GENUINE metric (it satisfies the triangle inequality) — ward.D2 (#242) and classical MDS (#245) assume a metric/euclidean structure; with 1-r or 1-\|r\| the results remain computable but the geometric interpretation (and the negative eigenvalues of cmdscale) change
- canberra/binary CARRY SEMANTICS, AND THEY ARE HARD GATES (not a mere recommendation): binary = an asymmetric Jaccard over on/off data (the dist routine: «The vectors are regarded as binary bits, so non-zero elements are 'on'») ⇒ on CONTINUOUS macro data ALL the elements are 'on' and the metric SILENTLY returns a matrix FULL OF ZEROS («every country is identical»), which then feeds hclust/PAM/MDS — LIVE-VERIFIED silently wrong. The gate's rule is that EVERY element ∈ {0,1} and NOT «exactly two distinct values» (a {3,7} column passes the loose check and gives THE SAME zero matrix); the message points to the binning node (#251 bn_quantile_bins). canberra = sum \|x_i-y_i\|/(\|x_i\|+\|y_i\|) with the 0/0 terms OMITTED (the dist routine: «This is intended for non-negative values (e.g., counts)») ⇒ a hard gate on NEGATIVE values, on the same reasoning as the non-negativity gate of dm_proxy_dist
- DETERMINISM: pure arithmetic, no RNG, no seed; the 'call' attribute of the dist object is removed explicitly so that two calls written differently give an identical result (pinned in the tests)
- a PRODUCER (register) node: dist_object travels downstream ONLY as a handle (an object-store pointer; CLAUDE.md §4); the input DATA travels as a matrix_handle — NEVER inline in the JSON schema

### References

- the dist routine's documentation — the 6 methods + their exact formulas (canberra: «Terms with zero numerator and denominator are omitted»; binary = an asymmetric Jaccard); «Missing values are allowed, and are excluded from all computations involving the rows within which they occur.. the sum is scaled up proportionally to the number of columns used» (the documentation of the silently-wrong NA gate); the attributes Size/Labels/method/call
- the as.dist routine's documentation (matrix -> 'dist', the lower triangle ONLY) / the cor routine (computed PER COLUMN; warning-only on a zero standard deviation)
- proxy 0.4.29 reference manual — the pr_DB registry of metrics (cosine/angular/Chord/Geodesic/Mahalanobis/Bray/Soergel/Whittaker/Hellinger/Kullback/divergence/Wave/Podani/eJaccard)
- Mantegna, R.N. (1999) «Hierarchical structure in financial markets», The European Physical Journal B 11(1):193-197 — d = sqrt(2(1-r)) as a GENUINE metric for the hierarchical clustering of correlated series
- Keogh, Lin & Truppel «Clustering of Time Series Subsequences is Meaningless: Implications for Previous and Future Research», Proc. IEEE ICDM 2003 (extended in: Keogh & Lin, Knowledge and Information Systems 8(2):154-177, 2005) — the normative gate spec §3b normative gate 1
- «Clustering Macroeconomic Time Series» arXiv:1807.04004 (the deliberate use of raw, non-seasonally-adjusted, non-detrended data) + Hamilton, J.D. (2018) «Why You Should Never Use the Hodrick-Prescott Filter», REStat 100(5) — the normative gate spec §3b normative gate 2
- wrapper footer IMPLEMENTATION NOTE (c29_unsupervised_clustering/distance_dissimilarity_matrix) — live-verified masking (conflicts(detail=TRUE) before/after; the S3 registration for class dist) and the silently-wrong paths of proxy

## #241 — Partitional (flat) clustering + RULE-BASED selection of k: k-means (Hartigan-Wong/Lloyd/Forgy/MacQueen), PAM/k-medoids (Kaufman-Rousseeuw), the silhouette diagnostic (Rousseeuw), the gap statistic (Tibshirani-Walther-Hastie) with the 5 maxSE rules

**Module:** `partitional_clustering_rule.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `km_kmeans` | `x`, `k` | `matrix_handle`, `integer`, `enum`, `enum`, `integer`, `integer`, `integer` | `nstart=25`, `iter_max=50`, `seed=1234` | `light` | — |
| `km_pam` | `x`, `k` | `matrix_handle`, `integer`, `enum`, `boolean`, `enum` | `stand=False` | `light` | — |
| `km_silhouette` | `x`, `cluster` | `matrix_handle`, `int_array`, `enum`, `enum` | — | `light` | — |
| `km_gap` | `x` | `matrix_handle`, `integer`, `enum`, `integer`, `integer`, `enum`, `enum`, `number`, `integer`, `integer`, `enum`, `enum`, `integer` | `k_max=8`, `B=100`, `d_power=1`, `se_factor=1`, `nstart=25`, `iter_max=50`, `seed=1234` | `heavy` | — |

### Use when

FLAT clustering of objects (countries x macro indicators, series x features) into a KNOWN or TO-BE-CHOSEN number of groups k, over a NUMERIC observations×features matrix. The normal flow: km_gap (a rule-based k) -> km_kmeans (fast, centroids) OR km_pam (robust, medoids = ACTUAL observations) -> km_silhouette (a quality diagnostic for the chosen k)

### Do not use when

you do not even know whether a flat structure exists / you want the WHOLE hierarchy & a dendrogram -> #242; you want a PROBABILISTIC model with k selected by BIC -> #244 mclust; the input is a READY 'dist' matrix (this node takes observations×features DATA; for a distance-based flow see #242/#245); sliding-window subsequences (the KEOGH GATE); time alignment/lead-lag -> DTW #243; a two-dimensional map of similarity -> MDS #245; charts (the frontend, §5); data with NA (there is no imputation here)

### Prerequisites

- km_gap # FIRST a rule-based choice of k (the gap statistic + maxSE) — NEVER a visual elbow
- km_silhouette # AFTER the fit: avg_silhouette + n_negative (observations possibly in the WRONG cluster)
- c00_data_utilities/fast_row_column.panel_col_stats # (stat='sd') a zero column variance before transform='scale' (division by 0 -> NaN)

### Alternatives

| instead use | when |
| --- | --- |
| km_kmeans (algorithm='Hartigan-Wong') | spherical clusters of similar size, a LARGE n, minimisation of the SUM OF SQUARES; the default algorithm (it does the job better than Lloyd/Forgy/MacQueen — the kmeans routine) |
| km_pam | OUTLIERS / non-spherical clusters / you want a REPRESENTATIVE that is an ACTUAL observation (the «typical country» of the group): it minimises the SUM OF DISSIMILARITIES (not of squares); metric='manhattan' is even more robust; DETERMINISTIC WITHOUT a seed (the build phase) |
| km_gap (method='Tibs2001SEmax') | you want the ORIGINAL rule of Tibshirani et al. («the smallest k with f(k) >= f(k+1) - s_{k+1}»); CAUTION: it selects k=1 when all the SE exceed the differences — a VALID result («no clusters») |
| km_gap (fun_cluster='pam', B=500) | a robust gap loop and final (not exploratory) results — the clusGap routine recommends B=500 for precision; the default B=100 is exploratory |
| km_gap (d_power=2) | you want EXACTLY the proposal of Tibshirani et al. (squared euclidean distances in W(k)); the default d_power=1 is the HISTORICAL implementation |
| transform='scale' (a z-score) or 'center' or 'log' | an EXPLICIT choice, NEVER silent: 'scale' when the columns have incompatible units (otherwise the largest dominates the euclidean distance); 'log' for multiplicative magnitudes (it requires STRICTLY positive values); 'none' (default) when the scale IS MEANINGFUL |
| #242 hclust/agnes/diana | you want the WHOLE hierarchy (a dendrogram) and NOT a single k; or the natural input is already a distance matrix |
| #244 mclust | you want PROBABILISTIC (model-based) clustering where k and the cluster shapes are selected by BIC/ICL rather than by a geometric heuristic |

### Output fields

- km_kmeans: cluster (named integer, with CANONICALIZED ids) + centers (k×p, chart-data) + size + withinss + tot_withinss/betweenss/totss + between_ratio (= betweenss/totss, the «explained» share of dispersion) + iter/ifault + canonical_order
- km_pam: cluster + medoids (k×p — ACTUAL observations) + medoid_ids/medoid_labels (WHICH country is the representative) + clusinfo (size/max_diss/av_diss/diameter/separation) + objective_build/objective_swap + isolation + silhouette (n×3) + avg_silhouette/clus_avg_silhouette
- km_silhouette: silhouette (n×3: cluster/neighbor/sil_width) + sil_width per observation + avg_silhouette + clus_avg_silhouette + size + n_negative (observations with s(i)<0 = POSSIBLY in the wrong cluster)
- km_gap: gap_table (k×5: k/logW/E.logW/gap/SE.sim — the chart-data of the gap curve with error bars) + gap/se_sim/logw/e_logw (named) + optimal_k + optimal_k_by_rule (ALL 5 maxSE rules for comparison) + method/se_factor/B/d_power/space_h0
- ALL of them: k/n/p/n_distinct + transform + transform_center/transform_scale (§3b gate 6: fit/apply externalization as NUMBERS) + observations/variables + seed (kmeans/gap)

### Pitfalls

- NORMATIVE GATE 1 (KEOGH): a sliding-window subsequence matrix (each row = the previous one shifted by a FIXED step k >= 1 — NOT only k=1; the shared detector the reference/gate_sliding_window_step) is REJECTED — the centers degenerate into sine waves INDEPENDENTLY of the data, i.e. the output does NOT depend on the input (Keogh, Lin & Truppel). Whole-series/cross-section clustering is NOT affected
- NORMATIVE GATE 2 (NO silent detrending/standardization): 'transform' is an EXPLICIT match.arg option with the default 'none'; the node NEVER standardizes or detrends on its own (arXiv:1807.04004; Hamilton on the HP filter)
- DETERMINISM (charter §5), three parts TOGETHER: (a) the seed is MANDATORY in km_kmeans/km_gap (random initialisation / a bootstrap); (b) nstart >= 2 is a HARD GATE (a single random start = a local minimum that depends on the initialisation); (c) CANONICALIZATION of the cluster ids — «The clusters are numbered in the returned object, but they are a set and no ordering is implied. (Their apparent ordering may differ by platform.)» (the kmeans routine Note) ⇒ they are renumbered by DECREASING SIZE with ties broken lexicographically ASCENDING on the centroid/medoid coordinates. The caller's.Random.seed is RESTORED (L1 purity)
- k <= the number of DISTINCT rows, NOT k <= n: duplicate countries break k<n. kmeans throws «more cluster centers than distinct data points.»; pam does NOT ERROR AT ALL — it returns DUPLICATE medoids (silently wrong) ⇒ our own hard gate AND a post-check that the medoids are distinct
- SILENTLY WRONG: with algorithm Lloyd/Forgy kmeans can return FEWER than k clusters (an empty cluster -> NaN centers) WITHOUT an error — «Except for the Lloyd-Forgy method, k clusters will always be returned» (the kmeans routine) ⇒ a post-check for empty clusters; ifault=4 = non-convergence in the Quick-Transfer stage (it exists ONLY in Hartigan-Wong; NA elsewhere); a post-check of the identity totss == tot.withinss + betweenss
- SILENTLY WRONG: silhouette is defined ONLY for 2 <= k <= n-1 (the help page); with k=1 it returns NA WITHOUT an error ⇒ a hard gate (and km_pam with k=1 gives silinfo=NULL, live-verified); the cluster ids must be CONTIGUOUS 1.k
- SILENTLY WRONG (ROW ORDER): silhouette.partition returns the rows SORTED by cluster/decreasing width (the 'Ordered' attribute), NOT in the order of the observations ⇒ the wrapper restores the order of x through the rownames; without that, a join with the countries would be silently wrong
- NA/NaN/Inf: kmeans throws the cryptic «NA/NaN/Inf in foreign function call» while dist (the silhouette path) does not error at all ⇒ a single hard gate on the input; no imputation is done here
- stand=TRUE (pam) TOGETHER with transform='scale' = DOUBLE standardization (the mean absolute deviation AND a z-score) ⇒ a hard stop; choose one. The stand option of pam divides by the MEAN ABSOLUTE DEVIATION (not the sd)
- the gap statistic: maxSE is not one rule but FIVE — firstSEmax (default, Maechler 2012), Tibs2001SEmax (the original), globalSEmax (Dudoit-Fridlyand), firstmax, globalmax; the node returns ALL 5 (optimal_k_by_rule) so that their disagreement is VISIBLE rather than hidden. The gap is a bootstrap ⇒ it DEPENDS on the seed; the clusGap routine recommends B=500 for final results
- between_ratio (kmeans) ALWAYS increases with k — it is NOT a criterion for choosing k (the elbow is VISUAL, hence outside the rule-based contract); use km_gap (a rule) or km_silhouette (a quality measure)
- the silhouette s(i): ~1 = very well classified; ~0 = between two clusters; NEGATIVE = probably in the WRONG cluster (the silhouette routine); n_negative is the direct diagnostic. A singleton cluster ⇒ s(i) := 0 by definition
- the PAM variant is PINNED to 'original' (the build phase): variant='faster'/pamonce CHANGE the initialisation to RANDOM (medoids='random', nstart=1) ⇒ they would break determinism; that is why they are NOT exposed
- MASKING: library(cluster) is SAFE — conflicts(detail=TRUE) after the attach == the BASELINE (live-verified); no S3 method over a FOREIGN generic. WARNING: library(proxy)/library(dtw) is FORBIDDEN in a clustering wrapper (they mask dist/as.dist/as_matrix) ⇒ ALL the calls here are stats::/cluster:: qualified
- TERMINAL nodes (no register/handle chaining): they return chart-ready numbers — cluster ids, centers/medoids, silhouette widths, the gap table. The data enters as a matrix_handle; the 'cluster' argument of km_silhouette as an int_array (the output of a previous node)

### References

- the kmeans routine's documentation — the algorithm enum; «Except for the Lloyd-Forgy method, k clusters will always be returned»; ifault=4 (Quick-Transfer); the Note: «The clusters are numbered in the returned object, but they are a set and no ordering is implied. (Their apparent ordering may differ by platform.)» (the reason for the canonicalization)
- Hartigan, J.A. & Wong, M.A. (1979) «Algorithm AS 136: A K-Means Clustering Algorithm», Applied Statistics 28(1):100-108 — the default algorithm; Lloyd (1982) IEEE Trans. Inf. Theory 28(2):129-137; Forgy (1965) Biometrics 21:768-769; MacQueen (1967) 5th Berkeley Symp. 281-297
- Kaufman, L. & Rousseeuw, P.J. (1990) Finding Groups in Data: An Introduction to Cluster Analysis, Wiley — ch. 2 PAM (k-medoids); cluster 2.1.8.2 the pam routine (metric euclidean/manhattan; stand = division by the MEAN ABSOLUTE DEVIATION; variant/pamonce)
- Rousseeuw, P.J. (1987) «Silhouettes: A graphical aid to the interpretation and validation of cluster analysis», J. Comput. Appl. Math. 20:53-65 — s(i) = (b(i)-a(i))/max(a(i),b(i)); cluster 2.1.8.2 the silhouette routine: «silhouette statistics are only defined if 2 <= k <= n-1», a singleton cluster => s(i):=0, a negative s(i) => «probably placed in the wrong cluster», the 'Ordered' attribute
- Tibshirani, R., Walther, G. & Hastie, T. (2001) «Estimating the number of data clusters via the Gap statistic», JRSS-B 63(2):411-423; cluster 2.1.8.2 the clusGap routine/the maxSE routine — spaceH0 scaledPCA/original, d.power 1 (the conventional historical choice) vs 2 (Tibshirani's proposal), the 5 maxSE rules (firstSEmax the default, Maechler 2012; Tibs2001SEmax; globalSEmax = Dudoit & Fridlyand 2002 Genome Biology 3(7)); «using B = 500 gives quite precise results»
- Keogh, Lin & Truppel «Clustering of Time Series Subsequences is Meaningless», Proc. IEEE ICDM 2003 (extended in: Keogh & Lin, KAIS 8(2):154-177, 2005) — the normative gate spec §3b normative gate 1
- «Clustering Macroeconomic Time Series» arXiv:1807.04004 + Hamilton, J.D. (2018) «Why You Should Never Use the Hodrick-Prescott Filter», REStat 100(5) — the normative gate spec §3b normative gate 2 (no imposed detrending); the normative gate spec §3b gate 6 (fit/apply externalization; modelled on the KNIME Normalizer -> «Normalize Model»)
- wrapper footer IMPLEMENTATION NOTE (c29_unsupervised_clustering/partitional_clustering_rule) — the live-verified gate messages («more cluster centers than distinct data points.»; the silent duplicate medoids of pam), the masking verdict via conflicts(detail=TRUE), the canonicalization rule

## #242 — Hierarchical clustering on a distance matrix: agglomerative hclust (the 8 documented methods) + agnes (with an agglomerative coefficient), divisive diana (with a divisive coefficient), and tree cutting with cutree (k OR h) -> dendrogram chart-data (merge/height/order) + memberships

**Module:** `hierarchical_clustering_distance.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `hc_hclust` | `d` | `raw_handle`, `enum`, `integer`, `number` | — | `light` | `tree` |
| `hc_cutree` | `tree` | `raw_handle`, `integer`, `number` | — | `light` | — |
| `hc_agnes` | `d` | `raw_handle`, `enum`, `num_array`, `integer`, `number` | — | `light` | `tree` |
| `hc_diana` | `d` | `raw_handle`, `integer`, `number` | — | `light` | `tree` |

### Use when

you want the WHOLE similarity hierarchy (not a single k): clustering countries/macro series with a DENDROGRAM, so that the number of groups is chosen AFTERWARDS (a cut at k or at a height h). The input is ALWAYS a 'dist' object (typically a handle from node #240). The flow: hc_hclust\|hc_agnes\|hc_diana -> register(tree) -> hc_cutree for further cuts of THE SAME tree without recomputation

### Do not use when

you have ALREADY decided k and you want a flat solution/centroids -> #241 kmeans/PAM; you want a probabilistic k from BIC -> #244 mclust; the input is a BARE data matrix (pass it through #240 FIRST — hclust on a matrix gives the cryptic «missing value where TRUE/FALSE needed»); a two-dimensional similarity map -> #245 MDS; sliding-window subsequences (the KEOGH GATE); drawing the dendrogram (the frontend, §5 — we supply merge/height/order); SEVERAL k at once (one cut per call; the frontend fans out)

### Prerequisites

- c29_unsupervised_clustering/distance_dissimilarity_matrix.dm_dist (or dm_cor_dist/dm_proxy_dist) # the MANDATORY producer of the 'dist' object (#240); look ALSO at n_zero_pairs: >0 => identical objects -> ac/dc = NaN & heights of 0
- c29_unsupervised_clustering/partitional_clustering_rule.km_silhouette # AFTER the cut: evaluating the chosen k on the SAME data (#241)
- hc_hclust (without k/h) # look first at height/monotone: a non-monotone tree (median/centroid) FORBIDS a cut at a height

### Alternatives

| instead use | when |
| --- | --- |
| hc_hclust(method='ward.D2') | you want COMPACT, spherical clusters of similar size (minimising the increase in variance); THE ONLY one that implements Ward's (1963) criterion — 'ward.D' does NOT (the hclust routine; Murtagh & Legendre 2014); it presupposes a METRIC distance (e.g. euclidean or cor-mantegna, #240) |
| hc_hclust(method='complete') | the default of hclust; «furthest neighbour» -> clusters of a small DIAMETER, robust to chaining, a safe general rule when the metric is not euclidean |
| hc_hclust(method='average'/'mcquitty') | a middle course between single and complete (UPGMA/WPGMA); good when the clusters have dissimilar sizes and you want neither chaining nor a strict diameter |
| hc_hclust(method='single') | you are looking for CHAIN-LIKE/elongated structures or outlier detection (nearest neighbour, a relative of the minimum spanning tree); BEWARE the chaining effect |
| hc_hclust(method='median'/'centroid') | ONLY if you ask for them explicitly: they do NOT lead to a monotone distance -> INVERSIONS «which are hard to interpret» (the hclust routine); the node returns monotone=FALSE and BLOCKS a cut at a height |
| hc_agnes | you ALSO want the agglomerative coefficient ac (how much clustering structure was found, 0.1) or the Lance-Williams generalisations 'flexible'/'gaverage'; NOTE: agnes(method='ward') == hclust(method='ward.D2') |
| hc_diana | you want a DIVISIVE (top-down) hierarchy: it starts from ONE cluster and splits by DIAMETER (a splinter group) — it finds the LARGE structures better, whereas agglomerative methods optimise the small ones; it returns the divisive coefficient dc |
| hc_cutree(tree=<handle>, k \| h) | you cut the SAME tree AGAIN (another k or height) WITHOUT recomputation — it also accepts agnes/diana ('twins') through as.hclust |
| #241 km_kmeans / km_pam | k is ALREADY decided and you want centroids/medoids + within/between SS instead of a hierarchy |

### Output fields

- merge: an (n-1)×2 INTEGER matrix — a negative j = the merger of the SINGLE observation \|j\|, a positive j = a merger with the cluster formed at step j (dimnames NULL)
- height: the n-1 merge heights (non-decreasing in an ultrametric tree); order: a PERMUTATION of 1.n giving a leaf ordering WITHOUT crossing branches; order_labels/labels — TOGETHER they are EXACTLY the dendrogram payload of the frontend (§5)
- monotone: FALSE => INVERSIONS (median/centroid) — cutting at a height is BLOCKED
- cluster (a named integer per object) + cluster_sizes + n_clusters: the result of the cut (NULL/NA when neither k nor h was supplied) — the leaf colouring in the frontend
- hc_hclust: method + dist_method (the metric that created the dist object, or NA if the attribute is missing)
- hc_agnes: ac (the agglomerative coefficient, 0.1) + par_method (Lance-Williams, only for flexible/gaverage); hc_diana: dc (the divisive coefficient, 0.1)
- tree: the CANONICALIZED hclust object -> register(field='tree') in hc_hclust/hc_agnes/hc_diana; the producer node for hc_cutree (which is TERMINAL)

### Pitfalls

- ward.D != ward.D2 (DOCUMENTED, the hclust routine): 'ward.D' (= the old 'ward' in the reference <= 3.0.3) does NOT implement Ward's (1963) criterion; 'ward.D2' does (Murtagh & Legendre 2014) by SQUARING the dissimilarities before the Lance-Williams update. They are not equivalent — the heights differ (pinned in the tests). Also documented: agnes(*, method='ward') == hclust(*, 'ward.D2')
- SILENT PRECEDENCE: cutree documents «At least one of k or h must be specified, k overrides h if both are given» ⇒ if both are supplied, h is ignored SILENTLY. Our gate: EXACTLY ONE of the two (mandatory in hc_cutree; in hc_hclust/hc_agnes/hc_diana neither is also allowed = dendrogram data only)
- CUTTING AT A HEIGHT ONLY ON AN ULTRAMETRIC TREE: «Cutting trees at a given height is only possible for ultrametric trees (with monotone clustering heights)» (the cutree routine); the median/centroid methods do NOT give a monotone distance («inversions or reversals which are hard to interpret», the hclust routine) ⇒ the node exposes monotone and BLOCKS a cut at h with a clean message (the reference would say «the 'height' component of 'tree' is not sorted (increasingly)»)
- THE INPUT MUST BE A 'dist': a bare matrix/data_frame gives the CRYPTIC «missing value where TRUE/FALSE needed» (live-verified) ⇒ a hard gate with an educational message pointing to node #240 / as.dist
- SILENTLY WRONG: NEGATIVE dissimilarities are ACCEPTED by hclust/agnes and produce a «result» (live: agnes ac=0.63 on a dist containing -3) ⇒ a hard gate; NA/NaN/Inf give «NA/NaN/Inf in foreign function call (arg 10)» (hclust) / «NA values in the dissimilarity matrix not allowed.» (diana) — we catch them first (and dist does NOT error when it produces such values, #240)
- SILENTLY WRONG (a DEGENERATE INPUT): identical objects (all distances 0) -> hclust does NOT error, it returns an ARBITRARY tree with ALL heights 0; agnes/diana return ac/dc = NaN SILENTLY ⇒ explicit post-checks (a finite scalar ac/dc BEFORE anything else; a stop when all(height==0)); the upstream warning sign is n_zero_pairs>0 in #240
- ac/dc ARE NOT COMPARABLE ACROSS SAMPLES OF DIFFERENT SIZE: «Because ac grows with the number of observations, this measure should not be used to compare datasets of very different sizes» (the agnes.object routine; identical wording for dc in the diana routine). It measures HOW MUCH structure was found WITHIN the same dataset
- par.method (agnes): it is REQUIRED for method='flexible' (it has no default -> live «argument "par.method" is missing, with no default»); it has a default ONLY for 'gaverage' (-0.1, Belbin et al. 1992); in ALL the other methods it is IGNORED SILENTLY (live: the same ac with and without) ⇒ a hard gate; it must be numeric of length 1, 3 or 4 (the Lance-Williams a1,a2,beta,gamma)
- agnes/diana ARE CANONICALIZED through as.hclust BEFORE merge/height/order are emitted: diana.height is NOT sorted (they are the DIAMETERS of the clusters before splitting) — without the canonicalization the frontend's dendrogram would be invalid. The same path also accepts hc_cutree ('twins' -> as.hclust)
- diana is DIVISIVE: it starts from ONE cluster, each time picks the one with the LARGEST DIAMETER and splits it through a 'splinter group' (the most distant observation); row i of merge describes the split at step n-i (the diana routine) — DIFFERENT semantics from the agglomerative methods
- the KEOGH GATE (normative §3b #1): the node EXPLICITLY honours the 'sliding_window_subsequences' marker attribute of the dist object and stops. THE MARKER'S CONTRACT (explicitly documented): from a `dist` the ORIGINAL observations×features matrix is NOT recoverable, so the detector gate_sliding_window_step CANNOT be re-run here; and OUR OWN producers (#240 dm_*, #243 dw_dist_matrix) stop AT THE SOURCE, so they NEVER set the marker (they produce no output at all). The attribute is therefore an ACCEPTED-INPUT CONTRACT for EXTERNAL producers of a `dist` (as.dist on a user matrix, a raw_handle from another flow) that wish to declare their provenance — defence in depth, NOT the primary defence
- DO NOT IMPOSE DETRENDING (normative §3b #2): the node NEVER transforms the input — it takes the dist AS IT IS; every transformation is an explicit gated option of the upstream distance node (#240)
- DETERMINISM: hclust/cutree/agnes/diana are FULLY deterministic (Lance-Williams updates / splinter-group splitting; no random initialisation, unlike kmeans) -> NO seed; identical over 2 runs is pinned. keep.diss/keep_data are PINNED to FALSE: the documented default keep.diss = n < 100 CHANGES the SHAPE/size of the output exactly at n = 100
- CHAINING & masking: hc_hclust/hc_agnes/hc_diana call register(field='tree') (a raw handle -> an object-store pointer); hc_cutree is TERMINAL. library(cluster) is safe (live: setdiff(the conflicts after, before) == character(0); cluster does not even export `plot`), YET all the calls stay stats::/cluster:: qualified because a sibling wrapper in the SAME category (dtw -> proxy) MASKS dist/as.dist/as_matrix in the shared source env

### References

- the hclust routine's documentation — the 8 methods; «The one used by option ward.D.. does not implement the clustering criterion of Ward (1963), whereas option ward.D2 implements that criterion (Murtagh and Legendre 2014). With the latter, the dissimilarities are squared before cluster updating»; «Note that agnes(*, method="ward") corresponds to hclust(*, "ward.D2")»; «methods median and centroid are not leading to a monotone distance measure, or equivalently the resulting dendrograms can have so called inversions or reversals which are hard to interpret»; the value merge/height/order/labels/method/dist.method
- the cutree routine's documentation — «At least one of k or h must be specified, k overrides h if both are given»; «Cutting trees at a given height is only possible for ultrametric trees (with monotone clustering heights)»; the as.hclust routine (twins -> hclust)
- Ward, J.H. Jr. (1963) «Hierarchical Grouping to Optimize an Objective Function», JASA 58(301):236-244; Murtagh, F. & Legendre, P. (2014) «Ward's Hierarchical Agglomerative Clustering Method: Which Algorithms Implement Ward's Criterion?», Journal of Classification 31(3):274-295
- cluster 2.1.8.2 the agnes routine / the agnes.object routine — the method enum (average is the default/single/complete/ward/weighted/flexible/gaverage); the Lance-Williams par.method (of length 1, 3 or 4; the default -0.1 ONLY for gaverage); ac: «For each observation i, denote by m(i) its dissimilarity to the first cluster it is merged with, divided by the dissimilarity of the merger in the final step.. The ac is the average of all 1 - m(i).. Because ac grows with the number of observations, this measure should not be used to compare datasets of very different sizes»; keep.diss = n < 100 (the documented default)
- cluster 2.1.8.2 the diana routine — the divisive algorithm (choosing the cluster of MAXIMUM diameter; the splinter group); dc carries the SAME size-comparison warning; «stop.at.k: Non-default NOT YET IMPLEMENTED»; height = the DIAMETERS before the split; row i of merge = the split at step n-i
- Kaufman, L. & Rousseeuw, P.J. (1990) Finding Groups in Data, Wiley — ch. 5 (AGNES) & ch. 6 (DIANA); Lance, G.N. & Williams, W.T. (1966) «A General Theory of Classificatory Sorting Strategies, I. Hierarchical Systems», Computer J. 9:373-380; Belbin, Faith & Milligan (1992) «A Comparison of Two Approaches to Beta-Flexible Clustering», Multivariate Behavioral Research 27:417-433 (gaverage/flexible beta, the default -0.1)
- Keogh, Lin & Truppel «Clustering of Time Series Subsequences is Meaningless», Proc. IEEE ICDM 2003 (extended in: Keogh & Lin, KAIS 8(2):154-177, 2005) — the normative gate spec §3b normative gate 1; «Clustering Macroeconomic Time Series» arXiv:1807.04004 + Hamilton (2018) REStat 100(5) — normative gate 2
- wrapper footer IMPLEMENTATION NOTE (c29_unsupervised_clustering/hierarchical_clustering_distance) — live-verified: a matrix -> «missing value where TRUE/FALSE needed», negative dissimilarities silently accepted (agnes ac=0.63), zero distances -> ac/dc = NaN, par.method silently ignored outside flexible/gaverage, the masking verdict for cluster

## #243 — Dynamic Time Warping (DTW): a shape-based distance with NON-LINEAR alignment in time — a query/reference pair + a cross-distance matrix (`dist`) for downstream clustering

**Module:** `dynamic_time_warping.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `dw_dtw` | `query`, `reference`, `window_type` | `series_handle`, `series_handle`, `enum`, `integer`, `enum`, `enum`, `boolean` | — | `light` | — |
| `dw_dist_matrix` | `x`, `window_type`, `orientation` | `matrix_handle`, `enum`, `integer`, `enum`, `enum`, `boolean`, `enum` | — | `light` | `dist_object` |

### Use when

SHAPE SIMILARITY between macro series when the TIMING differs (leads/lags around a recession, a different cycle duration, series of UNEQUAL LENGTH): dw_dtw for ONE pair (distance + normalizedDistance + the warping path as chart-data); dw_dist_matrix for a SET of series -> a `dist` object that feeds hclust/cutree (#242), PAM/silhouette (#241) and MDS (#245) through a handle

### Do not use when

series that are ALREADY aligned in time & of EQUAL LENGTH, where a euclidean/Manhattan/Minkowski distance suffices -> #240 dm_dist (far cheaper); similarity of CO-MOVEMENT/covariance -> #240 dm_cor_dist (1-cor); subsequence matching with a sliding window -> FORBIDDEN (the Keogh gate); the clustering itself (#241/#242) or the embedding (#245) — this node produces ONLY distances; a cross-section observations×features with no time dimension (no warping freedom -> #240); charts (the frontend, §5); forecasting/lead-lag TESTS (CCF, cat 00/02)

### Prerequisites

- dw_dtw # run ONE pair FIRST with the same window.type/window.size/step.pattern: if no valid path exists, you will find out before the O(n^2) cross-distance matrix
- c29_unsupervised_clustering/distance_dissimilarity_matrix.dm_dist # a euclidean-distance baseline — if DTW does not change the ranking, the cheap #240 suffices

### Alternatives

| instead use | when |
| --- | --- |
| #240 dm_dist (dist) | the series are of EQUAL LENGTH and ALIGNED in time (the same dates, no phase shift) — then DTW is a pointless O(N*M) cost per pair |
| #240 dm_cor_dist (as.dist(1-cor)) | you care about CONTEMPORANEOUS linear co-movement, not non-linear alignment in time |
| window.type='slantedband' | series of UNEQUAL LENGTH: the band is defined around the SLANTED diagonal [1,1]->[N,M]; 'sakoechiba' (a band around the MAIN diagonal) requires window.size >= \|N-M\| and 'itakura' requires 0.5 <= M/N < 2 |
| window.type='none' | an EXPLICIT choice of unconstrained DTW; it allows PATHOLOGICAL alignments (one point matching dozens) — it is never chosen silently (missing(window.type) -> stop) |
| transform='zscore' | you care about SHAPE independently of level/scale (the standard of the DTW literature); the default 'none' = RAW data, with no silent detrending (normative gate 2) |
| normalize=TRUE (dw_dist_matrix) | ESSENTIAL when the distances are compared across pairs of different total length: it uses normalizedDistance (distance / (N+M) for the symmetric2 family); with step.pattern='symmetric1' (norm=NA) -> a hard stop |

### Output fields

- dw_dtw: distance (NOT normalized, the dtw routine «not normalized») + normalizedDistance + normalized_defined + normalization ('N+M' \| 'N' \| NA)
- dw_dtw: index1/index2 = THE WARPING PATH as numeric chart-data (NULL when distance.only=TRUE) + path_length + jmin + N/M (the lengths of query/reference)
- dw_dtw: an echo of the settings — window_type/window_size (NA when not applicable)/step_pattern/transform/distance_only
- dw_dist_matrix: distance_matrix (the full symmetric n×n double matrix with dimnames = labels; the chart-data «distance map») + lower_tri (the lower triangle by column)
- dw_dist_matrix: labels/n_objects/series_length + min_distance/max_distance/mean_distance (the scale for a heatmap)
- dw_dist_matrix: n_zero_pairs — THE NUMBER OF ZERO DISTANCES; >0 ⇒ #245 mds_isomds/mds_sammon WILL BLOCK («zero or negative distance between objects i and j»)
- dw_dist_matrix: dist_object -> a registry handle (register field='dist_object') = THE CHAINING CONTRACT towards #242 hclust/cutree, #241 PAM/silhouette, #245 MDS — the SAME as in #240

### Pitfalls

- NORMATIVE GATE 1 (Keogh):.dw_prep_set explicitly REJECTS a sliding-window subsequence input (consecutive rows = shifted copies at ANY fixed step k >= 1 — NOT only k=1 — detected in BOTH directions; the shared detector the reference/gate_sliding_window_step). Clustering subsequences is PROVABLY meaningless: the output does NOT depend on the input (Keogh, Lin & Truppel 2005). Whole-series objects are NOT affected
- NORMATIVE GATE 2 (NO imposed detrending): `transform` is an EXPLICIT match.arg option with the default 'none' = RAW data — no silent differencing/detrending (arXiv:1807.04004 «Clustering Macroeconomic Time Series» DELIBERATELY used raw, non-seasonally-adjusted, non-detrended series)
- dtwclust WAS REJECTED (live-verified, NOT from memory): it masks as_matrix/predict/update/plot/show (S4) ⇒ it would BREAK the forecasting wrappers (forecast/fable/smooth/tsgarch) in the SHARED source env, AND it drags in flexclust+modeltools+ggrepel+shinyjs. No functionality is lost: dtw + dist give the same numbers (live-verified against dtwDist). k-Shape/TADPole/DBA are not exposed (DBA barycenters are by construction unrepresentative)
- MASKING: NEVER library(dtw) — library(dtw) ATTACHES proxy, which masks dist, as.dist AND as_matrix (live conflicts(detail=TRUE): $`package:proxy` = as.dist/dist/as_matrix) ⇒ it would break the sibling nodes #240/#241/#242 and every wrapper that calls as_matrix. We use requireNamespace + dtw:: / proxy:: / stats:: / base:: everywhere
- A CONSEQUENCE of requireNamespace: the proxy entry «DTW» is registered ONLY in the.onAttach of dtw ⇒ it does NOT exist. That is why the method is passed to dist AS A FUNCTION (a documented API): the same numbers as dtwDist, WITHOUT mutating the global pr_DB registry
- SILENTLY WRONG (dw_dist_matrix): dist fills ONLY the lower triangle; with an ASYMMETRIC step pattern d(a,b) != d(b,a) holds (live: asymmetric -> 18.67 vs 22.98) ⇒ the «symmetric» matrix would be SILENTLY wrong. A hard gate: only symmetric2/symmetric1/symmetricP0/P05/P1/P2
- SILENTLY WRONG: normalize=TRUE with step.pattern='symmetric1' (the 'norm' attribute = NA) ⇒ dtw returns normalizedDistance = NA SILENTLY -> a hard gate. symmetric2 (the default) has norm = N+M; the asymmetric* patterns have norm = N but are not allowed in the matrix
- SILENTLY WRONG: NA/NaN/Inf do NOT give a clean message — they give the cryptic «No warping path exists that is allowed by costraints» (sic, the package's typo); a series of LENGTH 1 is accepted SILENTLY and returns a degenerate number; transform='zscore' on a CONSTANT series -> 0/0 = NaN SILENTLY. All three are hard gates
- WINDOWS (mathematical limits, NOT taste): 'sakoechiba' requires window.size >= \|N-M\| (the dtwWindowingFunctions routine: «If the window size is too small.. warping becomes impossible»); 'itakura' takes NO window.size and requires 0.5 <= M/N < 2 (a slope in [1/2,2], Itakura 1975 — it follows from the code (jw<2*iw)&(iw<=2*jw) at the corner); a window.size with 'none'/'itakura' would be IGNORED SILENTLY -> a hard gate. The remaining «No warping path exists» (the slope-constrained *P1/P2) is translated into a structured blocked-by-gate message with N/M/window/step + a remediation instruction
- EQUAL LENGTH IN THE MATRIX: dw_dtw accepts series of UNEQUAL LENGTH (that is the point of DTW), BUT dw_dist_matrix takes a RECTANGULAR matrix/data_frame ⇒ ALL the series have the same length m (N=M=m in the window gate: \|N-M\|=0 and M/N=1 always pass). For unequal-length sets -> pairwise dw_dtw calls
- ORIENTATION: `orientation` is MANDATORY (missing -> stop) — 'rows_are_objects' (one series per ROW) vs 'columns_are_objects' (the typical macro panel: time in the rows); it is NEVER guessed. The same vocabulary as in #240
- DETERMINISM (§5): pure dynamic programming, NO RNG -> NO seed; the 'call' attribute is removed from the `dist` object so that identical holds regardless of how the call was written (pinned over 2 runs in the tests)
- OMITTED: dist.method (LIVE: dtw itself warns that it «does not usually make a difference with single-variate timeseries»; Euclidean/Manhattan gave an IDENTICAL 13.12938); open.begin/open.end (subsequence matching — the Keogh gate); keep.internals/costMatrix/directionMatrix (heavy N×M internals; the frontend draws from index1/index2); ALL the dtwPlot* functions (§5); rabinerJuang/typeI-IV (the same mathematics under other names); mori2006 & rigid (open-end/degenerate)

### References

- Giorgino, T. (2009) «Computing and Visualizing Dynamic Time Warping Alignments in the reference: The dtw Package», Journal of Statistical Software 31(7), 1-24 — the package, the step patterns and the windowing functions (citation('dtw'), live)
- the dtw routine's documentation (dtw 1.23.3): «`distance` the minimum global distance computed, _not_ normalized»; «`normalizedDistance` distance computed, _normalized_ for path length, if normalization is known for chosen step pattern»; window.type = none/itakura/sakoechiba/slantedband; the stepPattern routine (the 'norm' attribute); the dtwWindowingFunctions routine «If the window size is too small.. warping becomes impossible»
- Sakoe, H. & Chiba, S. (1978) «Dynamic Programming Algorithm Optimization for Spoken Word Recognition», IEEE Trans. ASSP 26(1), 43-49 — the sakoechiba band and the slope-constrained *P0/P05/P1/P2 transitions
- Itakura, F. (1975) «Minimum Prediction Residual Principle Applied to Speech Recognition», IEEE Trans. ASSP 23(1), 67-72 — the Itakura parallelogram (a slope constrained to [1/2, 2] ⇒ 0.5 <= M/N < 2)
- the normative gate spec §3b normative gate 1 — Keogh, Lin & Truppel (2005) «Clustering of Time Series Subsequences is Meaningless», Knowledge and Information Systems 8(2): the output does NOT depend on the input
- the normative gate spec §3b normative gate 2 — «Clustering Macroeconomic Time Series» (arXiv:1807.04004): DELIBERATELY raw/non-seasonally-adjusted/non-detrended data; Hamilton (2018) REStat 100(5) on why detrending introduces artificial distortions
- Rakthanmanon et al. (2012) «Searching and Mining Trillions of Time Series Subsequences under Dynamic Time Warping», KDD '12 — z-normalization as the standard of the DTW literature (transform='zscore')
- proxy 0.4.29 the dist routine — `method` as a FUNCTION (a documented API); a cross-distance over a LIST of series; it returns a `dist` object with Labels
- the normative gate spec §3b REJECTED — dtwclust: it masks as_matrix/predict/update/plot/show + drags in flexclust/modeltools/ggrepel/shinyjs (live conflicts(detail=TRUE))
- wrapper footer IMPLEMENTATION NOTE (c29_unsupervised_clustering/dynamic_time_warping) — ALL the gates, the live messages and the masking verdict

## #244 — Model-based clustering (a finite gaussian mixture): a RULE-BASED choice of BOTH the number of groups G AND the geometric covariance shape through BIC/ICL + out-of-sample assignment

**Module:** `clustering_rule_choice.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `mb_mclust` | `x` | `matrix_handle`, `int_array`, `series_codes`, `enum`, `integer` | `seed=1234` | `light` | — |
| `mb_bic` | `x` | `matrix_handle`, `int_array`, `series_codes`, `enum`, `integer`, `integer` | `top=3`, `seed=1234` | `light` | — |
| `mb_icl` | `x` | `matrix_handle`, `int_array`, `series_codes`, `enum`, `integer`, `integer` | `top=3`, `seed=1234` | `light` | — |
| `mb_predict` | `x`, `newdata` | `matrix_handle`, `matrix_handle`, `int_array`, `series_codes`, `enum`, `integer` | `seed=1234` | `light` | — |

### Use when

a CROSS-SECTION observations×features matrix (e.g. countries × macro indicators) where you do NOT know how many groups exist: (modelName, G) is chosen by an INFORMATION CRITERION over a model × G grid — NO visual knee/elbow selection; you want a PROBABILISTIC assignment (a posterior z + an uncertainty per observation) rather than a hard geometric one; you want NON-SPHERICAL/unequal-volume clusters (the 14 volume-shape-orientation shapes)

### Do not use when

n <= p (the component covariances are undefined — a hard gate; REDUCE the dimensions with PCA #117 pca_composite or by variable selection); geometric/robust partitioning with a GIVEN k -> #241 kmeans/PAM; a hierarchical structure/dendrogram -> #242 hclust/agnes/diana; a DISTANCE MATRIX as input (mclust wants RAW data, not a `dist`) -> #241 PAM or #242; SHAPE similarity of time series -> #243 DTW; latent DYNAMIC factors of time series -> dfms/sparseDFM (cat 03); SUPERVISED classification (MclustDA) / dimension reduction (MclustDR) / density estimation (densityMclust) — NOT exposed; sliding-window subsequences (the Keogh gate); charts (the frontend, §5)

### Prerequisites

- mb_bic # FIRST the WHOLE BIC table per (model, G) + the top 3: see whether the peak is CLEAR or whether several models tie
- mb_icl # the same grid under the ICL criterion (BIC minus the entropy): if BIC and ICL DISAGREE, the components overlap
- c01_preparation_prechecks/profiling_quality_report.dp_column_profile # the scale/variance/constant columns PER COLUMN before deciding on a transform (NEVER a silent standardization) AND before establishing whether n > p holds

### Alternatives

| instead use | when |
| --- | --- |
| mb_bic (top-k) | you want the model-selection DIAGNOSTIC step (the WHOLE table as chart-data, a «BIC plot») without committing to a fit |
| mb_icl | you suspect OVERLAPPING components: the ICL penalises the entropy of the classification ⇒ it prefers DISTINCT groups (Biernacki, Celeux & Govaert 2000); it typically selects a SMALLER G than the BIC |
| mb_predict | you want an out-of-sample assignment of new observations (a posterior z + uncertainty) with the SAME fit — the same transform is applied with the fitted center/scale of x |
| model_names = c('EII','VII') | a small n or the failure of ALL the models (fit == NULL / an all-NA table): the spherical shapes are the most parsimonious in parameters |
| #241 km_kmeans / km_pam | you want geometric partitioning with a GIVEN k (or medoids/robustness to outliers); mclust requires n > p and assumes gaussian components |
| #242 hc_hclust / hc_cutree | you want a HIERARCHY (a dendrogram) or your input is a DISTANCE MATRIX rather than a raw data matrix |
| transform = 'scale' \| 'center' \| 'log' | an EXPLICIT gated choice; the default 'none' = NO silent standardization. 'scale' when the variables have incompatible units (the shapes EEI/VVI etc. DEPEND on the scale); 'log' only on STRICTLY positive data |

### Output fields

- mb_mclust: model_name + G (the SELECTED ones) + cluster (a named integer, CANONICALIZED) + size + uncertainty (named numeric, chart-data) + z (the n×G posterior matrix, chart-data)
- mb_mclust: pro (the mixture weights) + mean (a p×G matrix) + sigma (a p×p×G array) + loglik/df/bic/icl + bic_table (G×models — the chart-data of the «BIC plot») + top_bic (a data_frame {model,G,value,label})
- mb_mclust: avg_uncertainty + g_at_upper_bound (a DIAGNOSTIC: the selected G = max(G) ⇒ the search was truncated, widen the range) + G_tried/models_tried + n/p/n_distinct
- mb_bic / mb_icl: criterion + bic_table \| icl_table (G×models, chart-data) + top (a data_frame {model,G,value,label}) + best_model/best_G/best_value + n_failed (how many (model,G) combinations failed)
- mb_predict: classification (a named integer, with the SAME canonicalization) + z (n_new×G) + uncertainty + n_new/new_observations + train_cluster/train_size (for reference) + pro/mean/loglik/bic
- ALL of them: transform + transform_center + transform_scale (§3b gate 6 — fit/apply externalization: they are returned as NUMBERS and reused VERBATIM on the newdata) + observations/variables + seed + subset_init + canonical_order

### Pitfalls

- DETERMINISM — THE CRITICAL POINT: for n <= mclust.options('subset') (default 2000) the initialisation is model-based hierarchical clustering (hc/SVD) ⇒ DETERMINISTIC WITHOUT a seed (2 runs identical, live-verified & asserted). BUT for n > subset mclustBIC does initialization.subset <- sample(..) ⇒ NON-DETERMINISTIC (live: two unseeded runs gave a DIFFERENT loglik/classification) ⇒ every function takes a 'seed' (default 1234) and runs inside.mb_with_seed, which RESTORES the caller's RNG state (L1 purity); the subset_init field states EXPLICITLY whether that path was taken
- SILENTLY WRONG (p > n): Mclust with 3 observations × 4 variables does NOT error — it returns a fit (G=2, EEI). The component covariances are singular ⇒ OUR OWN hard gate p < n (live-verified)
- SILENTLY WRONG (NA): Mclust does NOT error on NA — it SILENTLY DROPS the rows (n 40 -> 39) ⇒ the classification no longer corresponds to the input rows (live-verified); Inf throws the cryptic «NA/NaN/Inf in foreign function call». A hard gate on both
- SILENTLY WRONG (max(G) > n): G = 1:20 with n = 10 does NOT error — it SILENTLY truncates the range and returns G = 9 (live-verified); G = 0 throws the cryptic «No classification with the specified number of clusters» from hclass. A hard gate: positive integers, max(G) <= n
- SILENTLY WRONG (total failure): when ALL the candidate (modelName, G) combinations fail, Mclust RETURNS NULL — it does NOT error (live-verified) ⇒ a hard gate; likewise an all-NA BIC/ICL table is blocked with an educational message (reduce G / restrict model_names to 'EII'/'VII')
- SILENTLY WRONG (mb_predict): predict.Mclust checks ONLY ncol («newdata must match ncol of object data») ⇒ a SHUFFLED COLUMN ORDER gives WRONG assignments WITHOUT an error. A hard gate: the SAME number AND the SAME names/order of columns as in x
- LABEL SWITCHING: the component ids of a mixture are a SET with no ordering ⇒ CANONICALIZATION: renumbering by DECREASING SIZE with ties broken lexicographically ASCENDING on the coordinates of the mean; the SAME permutation is applied to cluster/z/pro/mean/sigma/size AND in mb_predict (canonical_map). Without it the labels are NOT reproducible
- THE BIC CONVENTION OF mclust — THE OPPOSITE SIGN: BIC = 2*loglik - df*log(n) ⇒ THE LARGER THE BETTER (verified numerically: loglik=-182.0873, df=8, n=40 -> -393.686 == fit.bic). BIC uses the REVERSE convention ⇒ do NOT compare with the BIC of other packages; the top table is sorted DESCENDING
- NORMATIVE GATE 1 (Keogh): a sliding-window subsequence matrix (each row = the previous one shifted by a FIXED step k >= 1 — NOT only k=1; the shared detector the reference/gate_sliding_window_step) is REJECTED explicitly — clustering subsequences is provably meaningless (Keogh, Lin & Truppel 2005). Whole-series/cross-section matrices are NOT affected
- NORMATIVE GATES 2 + 6: 'transform' is an EXPLICIT match.arg option (none/center/scale/log, default 'none') — NO silent standardization/detrending; transform_center/transform_scale are EXTERNALIZED as numbers and applied VERBATIM to the newdata (modelled on the KNIME «Normalize Model»); 'scale' on a zero-variance column -> a hard stop (division by 0 -> NaN); 'log' requires STRICTLY positive data
- THE 14 SHAPES (multivariate, read LIVE from mclust.options('emModelNames') — NEVER from memory): EII VII EEI VEI EVI VVI EEE VEE EVE VVE EEV VEV EVV VVV (volume-shape-orientation; E=equal, V=variable, I=identity); for p=1 ONLY c('E','V'). An unknown name -> the cryptic «invalid model name» ⇒ an allowlist gate. THE SHAPES DEPEND ON THE SCALE — which is why the transform is an explicit decision
- g_at_upper_bound: a DIAGNOSTIC, NOT a gate — if the selected G equals max(G) of the grid, the search was truncated and you must widen the range; it is not an invalid result, so it is NOT blocked
- MASKING: HERE library(mclust) IS used — conflicts(detail=TRUE) BEFORE/AFTER is IDENTICAL (identical == TRUE, setdiff == character(0)) ⇒ ZERO masking; moreover the.__S3MethodsTable__. registers methods ONLY on generics of THE SAME package (compare the quanteda `$.dfm` incident). The attach is NECESSARY: Mclust calls mclustBIC UNQUALIFIED. WARNING: NEVER library(proxy)/library(dtw) in this category (they mask dist/as.dist/as_matrix) — which is why sd/setNames/predict are fully qualified
- L2 SAFETY: objects of class 'mclustBIC'/'mclustICL' carry the attribute initialization.hcPairs (an hc object WITH a `call` = a language object) ⇒ they are STRIPPED to a bare numeric matrix before leaving the wrapper. The top table is returned as a DATA.FRAME (jsonlite serialises a named numeric as an ANONYMOUS array ⇒ the «MODEL,G» labels would be lost)
- TERMINAL nodes: no register/handle chaining — they return chart-ready numbers (cluster ids, z, bic_table/icl_table, mean/sigma), not a fitted object. mb_predict REFITS on x (the same deterministic path) so that the node is stateless (§4)
- POST-CHECKS (independent recomputations, not trust in the package): sum(pro) == 1; rowSums(z) == 1; uncertainty == 1 - max(z) per observation; the shapes of mean (p×G) and sigma (p×p×G); length(classification) == n; the selected G inside the requested range

### References

- Scrucca, L., Fraley, C., Murphy, T.B. & Raftery, A.E. (2023) «Model-Based Clustering, Classification, and Density Estimation Using mclust in the reference», Chapman and Hall/CRC, ISBN 978-1032234953 — the package's official reference (citation('mclust'), live)
- mclust 6.1.3 ref manual — ?Mclust / the mclustBIC routine / the mclustICL routine / the predict.Mclust routine / the mclust.options routine (the signatures live-verified with args; emModelNames = the 14 names; subset = 2000)
- Fraley, C. & Raftery, A.E. (2002) «Model-Based Clustering, Discriminant Analysis, and Density Estimation», JASA 97(458), 611-631 — the framework for selecting (modelName, G) with BIC
- Banfield, J.D. & Raftery, A.E. (1993) «Model-Based Gaussian and Non-Gaussian Clustering», Biometrics 49(3), 803-821 — the volume-shape-orientation parameterisation of the covariances (EII…VVV)
- Biernacki, C., Celeux, G. & Govaert, G. (2000) «Assessing a Mixture Model for Clustering with the Integrated Completed Likelihood», IEEE TPAMI 22(7), 719-725 — the ICL (BIC minus the entropy of the classification)
- Schwarz, G. (1978) «Estimating the Dimension of a Model», The Annals of Statistics 6(2), 461-464 — the BIC (⚠️ mclust uses the OPPOSITE sign)
- the normative gate spec §3b normative gate 1 — Keogh, Lin & Truppel (2005) «Clustering of Time Series Subsequences is Meaningless», KAIS 8(2)
- the normative gate spec §3b normative gates 2 & 6 (NO imposed detrending; fit/apply externalization modelled on the KNIME Normalizer -> «Normalize Model») + the live-verified determinism note «mclust default init = model-based hierarchical (hc) ⇒ deterministic WITHOUT a seed» + the silently-wrong note «Mclust with p>n does NOT error»
- wrapper footer IMPLEMENTATION NOTE (c29_unsupervised_clustering/clustering_rule_choice) — ALL the gates/post-checks, the numerical verification of the BIC convention and the masking verdict

## #245 — Multidimensional Scaling: CLASSICAL/metric (cmdscale = principal coordinates analysis, + the Cailliez constant) · NON-METRIC after Kruskal (isoMDS) · the NON-LINEAR Sammon mapping

**Module:** `multidimensional_scaling_classical.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `mds_cmdscale` | `d` | `raw_handle`, `integer`, `boolean` | — | `light` | — |
| `mds_isomds` | `d` | `raw_handle`, `integer`, `integer`, `number`, `number` | — | `light` | — |
| `mds_sammon` | `d` | `raw_handle`, `integer`, `integer`, `number`, `number` | — | `mcmc` | — |

### Use when

a SIMILARITY MAP in a few dimensions (typically 2D) FROM A `dist` DISTANCE MATRIX — «which countries/indicators are close to which» as a 2D scatter + a scree plot + quality measures. The typical producer of the `dist`: #240 dm_dist/dm_cor_dist/dm_proxy_dist or #243 dw_dist_matrix (DTW). The node is VISUALIZATION/EMBEDDING, NOT clustering

### Do not use when

ASSIGNMENT to groups (labels) -> #241 kmeans/PAM, #242 hclust/cutree, #244 mclust; a RAW data matrix with no preceding distance node (the input MUST be a `dist`); dimension reduction of the VARIABLES with loadings/a biplot -> #117 pca_composite/pca_biplot_coords (MDS maps OBJECTS from dissimilarities); MIXED I(0)/I(1) time series -> #256; subsequence embedding (the Keogh gate); charts (the frontend, §5 — only the coordinates are returned here)

### Prerequisites

- c29_unsupervised_clustering/distance_dissimilarity_matrix.dm_dist # the TYPICAL producer of the `dist` handle (or dm_cor_dist / dm_proxy_dist)
- c29_unsupervised_clustering/dynamic_time_warping.dw_dist_matrix # DTW distances; READ the n_zero_pairs field: >0 ⇒ mds_isomds/mds_sammon WILL BLOCK (only mds_cmdscale works)
- mds_cmdscale # ALWAYS first: it gives n_eig_negative & gof_abs/gof_pos (how non-Euclidean the dissimilarities are) and it is the INITIALISATION of the other two

### Alternatives

| instead use | when |
| --- | --- |
| mds_cmdscale(add = TRUE) | n_eig_negative > 0 or gof_abs < gof_pos ⇒ NON-Euclidean dissimilarities; the Cailliez (1983) additive constant makes them Euclidean (the `ac` field). Useless when there are no negative eigenvalues |
| mds_isomds | the dissimilarities are ORDINAL / their ABSOLUTE scale is not trustworthy: non-metric MDS allows a MONOTONE transformation and keeps only the ORDER (Kruskal); it REQUIRES STRICTLY POSITIVE distances |
| mds_sammon | you want the SMALL (local) distances preserved better: the stress is weighted by 1/d ⇒ it gives weight to the nearby pairs; it REQUIRES STRICTLY POSITIVE distances |
| a smaller k | the solution returns FEWER columns than k (the POSITIVE eigenvalues are < k; the live warning «only 7 of the first 9 eigenvalues are > 0») ⇒ the node blocks; k MUST lie in {1,., n-1} |
| #117 pca_composite / pca_biplot_coords | you want dimension reduction of the VARIABLES with loadings/a biplot from a RAW data matrix; MDS starts from DISSIMILARITIES (and cmdscale on a euclidean distance COINCIDES with PCA on the scores) |

### Output fields

- points: an n × k NUMERIC matrix with rownames = the labels and colnames = Dim1.Dimk — THE MAIN chart-data (the 2D scatter «similarity map»); common to all 3 methods (the SAME dimensions/labels)
- labels / n / k + method ('cmdscale' \| 'isoMDS' \| 'sammon')
- mds_cmdscale: eig (ALL n eigenvalues = the scree data) + eig_retained + n_eig_positive + n_eig_negative (>0 ⇒ NON-Euclidean dissimilarities) + var_explained_abs / var_explained_pos (the TWO definitions in the cmdscale routine) + gof / gof_abs / gof_pos + ac (the Cailliez constant; 0 when add=FALSE) + add
- mds_isomds: stress AS A PERCENTAGE (the isoMDS routine «The final stress achieved (in percent)») + stress_fraction + maxit/tol/p + init_method='cmdscale'
- mds_sammon: stress (Sammon — NOT a percentage, NOT comparable with the isoMDS one) + niter/magic/tol + init_method='cmdscale'
- COMMON DIAGNOSTICS (ours, computed IDENTICALLY ⇒ COMPARABLE across the 3): stress_raw = sqrt(sum((d-dhat)^2)/sum(d^2)) (Kruskal stress-1 WITHOUT a monotone transformation, 0 = perfect) + fit_correlation = cor(d, dhat) (NA_real_ when either side is constant, e.g. an equilateral configuration) + dist_fitted = the distances of the configuration (Shepard chart-data)

### Pitfalls

- THE CENTRAL GATE — the input MUST be a `dist` object: cmdscale ALSO accepts a matrix/data_frame («a full symmetric matrix») BUT it also SILENTLY accepts a NON-SYMMETRIC matrix (live: with m[1,2]=99 it returned a GOF of 0.577/0.99 WITHOUT a warning) ⇒ silently wrong. A `dist` is by definition symmetric with a zero diagonal; that is why the spec uses a raw_handle (the object is returned AS IS and the wrapper decides)
- ZERO / DUPLICATE DISTANCES — THE MAIN TRAP OF THIS NODE: isoMDS AND sammon require STRICTLY POSITIVE distances («Data are assumed to be dissimilarities.. but must be positive except for self-distance», the isoMDS routine/the sammon routine) and they error with «zero or negative distance between objects i and j» on DUPLICATE ROWS (live-verified). The node blocks BEFORE the call and NAMES the objects (MASS gives only indices); mds_cmdscale does NOT have this restriction. The upstream signal: #243 dw_dist_matrix.n_zero_pairs > 0
- SILENTLY WRONG (cmdscale): NEGATIVE dissimilarities are accepted SILENTLY and produce an invalid map (live: a GOF of 0.668/0.818 with no error); ALL distances zero -> a GOF of NaN/NaN SILENTLY (there is nothing to map). Both are hard gates; also dist does NOT error when it produces NA (the normative gate spec §3b) ⇒ an explicit NA/NaN/Inf check here
- SILENTLY WRONG (the MASS arguments): maxit = 0 / niter = 0 are accepted SILENTLY and return the UNOPTIMISED INITIAL configuration; tol <= 0 is accepted silently and stops early (live: a stress of 0.44 instead of 0.0069); magic <= 0 is accepted silently and does NOT optimise AT ALL (the same stress as niter=0); p = 0 HANGS (it does not terminate; the Minkowski distance is a metric only for p >= 1). ALL are hard gates
- A DIMENSION POST-CHECK: cmdscale returns FEWER columns than k when the POSITIVE eigenvalues number fewer than k (live: k=9 -> 7 columns with the warning «only 7 of the first 9 eigenvalues are > 0») and isoMDS/sammon then fail with the cryptic «invalid initial configuration» ⇒ the node requires EXACTLY n × k and gives a clean message («ask for a smaller k»). The documented bound: k in {1, 2,., n-1} (the cmdscale routine)
- THE STRESS VALUES ARE NOT COMPARABLE: the isoMDS stress is A PERCENTAGE and allows a MONOTONE transformation of the distances; the Sammon stress is WEIGHTED by 1/d and is NOT a percentage. That is why the node also computes OUR OWN stress_raw IDENTICALLY across all 3 methods — THAT is the comparable quantity
- THE TWO GOF VALUES OF cmdscale: g_i = (sum_{j<=k} lambda_j) / (sum_j T_i(lambda_j)) with T_1 = \|.\| and T_2 = max(., 0) (the cmdscale routine) ⇒ gof_abs != gof_pos ONLY when NEGATIVE eigenvalues exist; var_explained_abs/var_explained_pos use the SAME two denominators (a post-check: the sum of var_explained_* == gof_abs/gof_pos)
- NEVER INTERPRET THE SIGN OF AN AXIS: the configuration is determined ONLY up to translation/rotation/reflection (the cmdscale routine: «the reflection chosen may differ between the reference platforms»; the isoMDS routine/the sammon routine: «the result can vary considerably from machine to machine»). Inside the container the versions are pinned (the lockfile) ⇒ a stable result, but the INTERPRETATION must rest on the DISTANCES between points, not on signs/directions
- DETERMINISM (§5): all 3 methods are FULLY deterministic (a spectral decomposition / an iterative descent from a CLASSICAL initialisation) ⇒ NO seed; the initialisation of isoMDS/sammon is passed EXPLICITLY (y = the cmdscale solution = the DOCUMENTED default; an IDENTICAL result, live-verified) so that the determinism does not depend on a future change of default; identical over 2 runs is pinned in the tests
- NORMATIVE GATE 1 (Keogh): if the `dist` carries the marker attribute sliding_window_subsequences, the node REJECTS it explicitly — mapping subsequences is as meaningless as clustering them (Keogh, Lin & Truppel 2005). THE MARKER'S CONTRACT: from a `dist` the original observations×features matrix is NOT recoverable (the detector gate_sliding_window_step cannot be re-run here), and the producers #240/#243 stop AT THE SOURCE — so NO producer in the engine EVER sets the attribute. It is an ACCEPTED-INPUT CONTRACT for EXTERNAL producers of a `dist` (a raw_handle / as.dist on a user matrix) — defence in depth, NOT the primary defence
- NORMATIVE GATE 2 (NO imposed detrending): the node NEVER transforms the input — it takes the `dist` AS IT IS. The transform/distance choices are EXPLICIT gated options of the UPSTREAM distance node (#240/#243)
- MASKING: library(MASS) is NOT used — a live conflicts(detail=TRUE) before/after shows ONLY the dataset npk (NO function), but because masking DOES exist, the exception in §3.a #1 applies: requireNamespace('MASS') + isoMDS/sammon. IN ADDITION all the stats:: calls are fully qualified because the SIBLING wrapper dtw-distance brings in proxy (which masks dist/as.dist/as_matrix) into the SHARED source env — the wrapper stays correct REGARDLESS OF THE source ORDER
- OMITTED: x.ret (the heavy n×n doubly centred matrix); eig/list. (PINNED TRUE — we ALWAYS need the eigenvalues + GOF as chart-data); trace (PINNED FALSE — it prints progress, §5); `y` (the initial configuration: it is n×k DATA, never inline in the JSON schema — the wrapper fills it EXPLICITLY); Shepard (the same numbers are given as dist_fitted/stress_raw/fit_correlation); smacof (REJECTED in the normative gate spec §3b: cmdscale + MASS suffice, live-verified with the GOF). TERMINAL nodes: no register/chaining

### References

- the cmdscale routine's documentation (stats): «Classical multidimensional scaling (MDS) of a data matrix. Also known as principal coordinates analysis (Gower 1966)»; k «must be in {1, 2,.., n-1}»; GOF = «a numeric vector of length 2.. g_i = (sum_{j=1.k} lambda_j)/(sum_{j=1.n} T_i(lambda_j)), T_1(v) = \|v\|, T_2(v) = max(v, 0)»; «The representation is only determined up to location, rotations and reflections.. the reflection chosen may differ between the reference platforms»
- Gower, J.C. (1966) «Some Distance Properties of Latent Root and Vector Methods Used in Multivariate Analysis», Biometrika 53(3/4), 325 — principal coordinates analysis (cited by the cmdscale routine)
- Mardia, K.V. (1978) «Some Properties of Classical Multi-dimensional Scaling», Communications in Statistics - Theory and Methods 7(13), 1233-1241 — the analysis that cmdscale follows (cited by the cmdscale routine)
- Cailliez, F. (1983) «The Analytical Solution of the Additive Constant Problem», Psychometrika 48(2), 305-308 — the additive constant of add=TRUE (the reference uses THIS analytic solution, the cmdscale routine)
- the isoMDS routine's documentation (MASS 7.3-65): «Kruskal's Non-metric Multidimensional Scaling»; «Data are assumed to be dissimilarities or relative distances, but must be positive except for self-distance»; «the input distances are allowed a monotonic transformation»; the value stress = «The final stress achieved (in percent)»; the default y = cmdscale(d, k)
- the sammon routine's documentation (MASS 7.3-65): stress = «the sum of squared differences between the input distances and those of the configuration, weighted by the distances, the whole sum being divided by the sum of input distances to make the stress scale-free»; `magic` = «initial value of the step size constant in diagonal Newton method»
- Sammon, J.W. (1969) «A Non-Linear Mapping for Data Structure Analysis», IEEE Transactions on Computers C-18, 401-409 (cited by the sammon routine)
- Kruskal, J.B. (1964) «Multidimensional Scaling by Optimizing Goodness of Fit to a Nonmetric Hypothesis», Psychometrika 29(1), 1-27 — the non-metric MDS that isoMDS implements
- Cox, T.F. & Cox, M.A.A. (2001) Multidimensional Scaling, 2nd ed., Chapman & Hall; Venables, W.N. & Ripley, B.D. (2002) Modern Applied Statistics with S, 4th ed., Springer (cited by the cmdscale routine/the isoMDS routine/the sammon routine)
- the normative gate spec §3b live-verified gates: «cutree/cmdscale: 'k' must be in {1, 2,. n - 1}»; «isoMDS: zero or negative distance between objects i and j ⇒ a gate on DUPLICATE ROWS»; «dist with NA does NOT error»; normative gates 1 (Keogh) & 2 (NO imposed detrending); REJECTED: smacof
- wrapper footer IMPLEMENTATION NOTE (c29_unsupervised_clustering/multidimensional_scaling_classical) — ALL the gates/post-checks, the live silently-wrong findings and the masking verdict
