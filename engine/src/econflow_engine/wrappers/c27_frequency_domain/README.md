<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 27-frequency-domain

2 METHOD-SELECTION cards, 2 modules, 5 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #235 — Wavelet time-frequency analysis (the Morlet CWT: power spectrum, cross-wavelet, wavelet coherence, phase difference — numeric grids)

**Module:** `wavelet_time_frequency.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `wv_wavelet` | `df` | `df_handle`, `string`, `number`, `number`, `number`, `number`, `number`, `boolean`, `enum`, `integer`, `integer` | `dt=1`, `dj=0.05`, `loess_span=0.75`, `make_pval=True`, `n_sim=10`, `seed=1` | `heavy` | — |
| `wv_coherency` | `df` | `df_handle`, `string`, `string`, `number`, `number`, `number`, `number`, `number`, `number`, `number`, `boolean`, `enum`, `integer`, `integer` | `dt=1`, `dj=0.05`, `loess_span=0.75`, `window_size_t=5`, `window_size_s=0.25`, `make_pval=True`, `n_sim=10`, `seed=1` | `heavy` | — |

### Use when

you want to see HOW the spectral power of a macro series changes OVER TIME (non-stationary/evolving cycles) — a CWT power spectrum (period x time) with a ridge & simulation-based significance; or the DYNAMIC relation of TWO series by frequency/time (cross-wavelet power, wavelet coherence in [0,1], the phase difference for lead/lag)

### Do not use when

a stationary series with a fixed spectrum -> classical spectral analysis (the stats spectrum/AR spectrum, #234); a time-invariant band decomposition -> band-pass/HP/Baxter-King filters (#56-61); a plain correlation/lead-lag with no frequency dimension -> ccf (cross-correlation); pure forecasting (this is a time-frequency diagnostic)

### Alternatives

| instead use | when |
| --- | --- |
| wv_wavelet (analyze.wavelet) | ONE series -> a wavelet power spectrum (period x time), the amplitude, the phase, the ridge, the global/average power + surrogate p-values; identifying evolving cycles |
| wv_coherency (analyze.coherency) | TWO aligned series -> the cross-wavelet power, the wavelet coherence in [0,1] (a localized correlation per period/time), the phase difference (an angle -> lead/lag) + p-values |

### Output fields

- wv_wavelet: power (a matrix period x time), phase, amplitude, ridge (0/1), power_avg (the global spectrum) + power_pval/power_avg_pval (NULL if make_pval=FALSE), period/scale, axis_time/axis_period, coi_time/coi_period (the cone of influence), n_time(=nc)/n_period(=nr)
- wv_coherency: cross_power (a matrix), coherence (a matrix in [0,1]), angle (the phase-difference matrix), power_x/power_y, ridge_xy/ridge_co (0/1), *_avg + *_pval, period/scale/axes/coi, n_time/n_period
- everything is numeric chart-data (charts are the frontend's job ONLY, §5); the raw fit sits in the 'fit' field (to_mcp -> a stub; it contains the complex Wave)

### Pitfalls

- the period is EXPRESSED in units of dt; power/coherence INSIDE the cone of influence (coi_time/coi_period) are edge-affected -> interpret only outside the COI
- an upper_period > n*dt gives a spectrum lying ENTIRELY inside the COI (no complete cycle) = plausible-but-nonsense; WaveletComp does NOT error -> a hard gate (a silently-wrong blocker)
- significance = a surrogate simulation (method + n_sim) -> DETERMINISM ONLY with a seed; the CWT power/phase/period themselves are seed-invariant (only the p-values depend on the seed)
- coherence lies in [0,1] (a localized squared-correlation analogue); HIGH coherence does NOT mean causality; the angle (the phase difference) gives lead/lag ONLY where the coherence is significant
- loess_span detrends BEFORE the CWT (0 = no detrending); an incomplete/NA series -> silently wrong (gate: a complete series)
- method='white.noise' (default) vs the AR/ARIMA/Fourier.rand/shuffle null models -> a different strictness of significance; the AR/ARIMA surrogate suits series with autocorrelation

### References

- WaveletComp v1.2 ref manual + the vignette 'Computational Wavelet Analysis' (the analyze.wavelet / analyze.coherency help pages)
- Roesch & Schmidbauer 2018 'WaveletComp: Computational Wavelet Analysis' package guide (the Morlet CWT, cross-wavelet, coherence, phase, surrogate significance)
- Torrence & Compo 1998 'A Practical Guide to Wavelet Analysis' BAMS 79(1) 61-78 (the CWT, the cone of influence, Monte Carlo significance)
- Aguiar-Conraria & Soares 2014 'The Continuous Wavelet Transform: Moving Beyond Uni- and Bivariate Analysis' Journal of Economic Surveys 28(2) 344-375 (macro time-frequency use, the interpretation of coherence & phase)
- wrapper footer IMPLEMENTATION NOTE (c27_frequency_domain/wavelet_time_frequency)

## #236 — Spectral / periodogram quick look (a smoothed periodogram, the high-level spectrum pgram|AR, a numeric cumulative periodogram + KS white-noise bands)

**Module:** `spectral_periodogram_quick.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `sp_periodogram` | `x` | `series_handle`, `int_array`, `number`, `number`, `boolean`, `boolean`, `boolean` | `taper=0.1`, `pad=0`, `fast=True`, `demean=False`, `detrend=True` | `light` | — |
| `sp_spectrum` | `x` | `series_handle`, `enum`, `int_array`, `number`, `integer`, `integer` | `taper=0.1`, `n_freq=500` | `light` | — |
| `sp_cumulative_periodogram` | `x` | `series_handle`, `number` | `taper=0.1` | `light` | — |

### Use when

a frequency-domain quick look at ONE univariate macro series -> which periodicities/cycles (seasonality, the business cycle) dominate; a smoothed periodogram (modified Daniell), a smooth AR spectral estimate, or a numeric cumulative periodogram + Kolmogorov-Smirnov bands for a white-noise test

### Do not use when

multivariate coherency/phase between series (this node handles ONE series); a wavelet/time-varying spectrum (WaveletComp, #237); spectral causality/connectedness (frequencyConnectedness); plain ARIMA/seasonal modelling (cat. 02/03); it requires >= 4 observations with no NA

### Alternatives

| instead use | when |
| --- | --- |
| sp_periodogram (spec.pgram, spans = odd Daniell smoothers) | you want the (smoothed) raw periodogram with full control of taper/detrend/demean/pad/fast plus the dominant frequency+period |
| sp_spectrum (method='pgram') | a high-level quick look identical to spec.pgram but through the spectrum dispatcher (spans/taper) |
| sp_spectrum (method='ar') | you want a SMOOTH autoregressive (Yule-Walker) spectral estimate — a cleaner identification of the dominant cycle when the raw periodogram is noisy; the order is automatic (AIC) or supplied |
| sp_cumulative_periodogram (a numeric cpgram + KS bands) | you want a white-noise test (Bartlett's Tp): the cumulative normalized periodogram vs frequency + KS bands; leaving the bands => white noise is rejected |

### Output fields

- sp_periodogram: freq + spec (numeric vectors, chart-ready); peak_frequency + peak_period (=1/peak_frequency); df/bandwidth/taper/pad/detrend/demean/n_used/orig_n; smoothed(bool)+spans; method='pgram'; spec_object (the raw 'spec' list -> a to_mcp stub)
- sp_spectrum: freq + spec; method ('pgram'\|'ar'); method_label; ar_order (parsed from the 'AR (k) spectrum' string; NA for pgram); peak_frequency + peak_period; df/bandwidth/taper/n_used; spec_object (a stub)
- sp_cumulative_periodogram: frequency + cumulative (monotone from 0 to 1); band_upper/band_lower (the KS bands clamped to [0,1]); crit (the KS critical value); nyquist; mp; n_exceedances + white_noise_rejected (bool)

### Pitfalls

- spans MUST be odd positive integers: spec.pgram SILENTLY accepts even spans and returns the WRONG modified-Daniell smoother -> a hard gate (it blocks them)
- cpgram is PLOT-ONLY (it draws + returns invisible, with NO numeric return) -> it is NOT called; sp_cumulative_periodogram reproduces THE SAME algorithm numerically (center -> spec.taper -> Mod(fft)^2/n -> y[1]=0 -> cumsum/sum; the bands have slope 1/xm and offset ±crit)
- the AR spectrum of a trending/persistent series peaks at frequency 0 -> peak_period = 1/0 -> NA is returned (not Inf)
- spec.pgram omits frequency 0 (freq is always > 0); the peak is therefore always a real cycle
- detrend=TRUE (default) removes BOTH the linear trend AND the mean; demean removes only the mean; the taper defaults to 0.1 (a split-cosine bell) as in the docs
- the node handles ONE series: multivariate/mts input is blocked (there is no coherency/phase surface); NA -> an explicit gate (spec.pgram na.action=na.fail)
- the FFT + Yule-Walker are DETERMINISTIC (no RNG; identical across two runs) -> no seed is needed

### References

- The the reference stats spec.pgram help page (spans=odd modified Daniell smoothers, a split-cosine-bell taper, pad/fast/demean/detrend, na.action=na.fail, the value of class 'spec') https://stat.ethz.ch/the reference-manual/the reference-devel/library/stats/html/spec.pgram.html
- The the reference stats spectrum help page (method=c('pgram','ar') dispatching to spec.pgram / spec.ar Yule-Walker, n.freq, the order chosen automatically via AIC)
- The the reference stats cpgram help page (the cumulative periodogram plot, taper=0.1, the ci band; from MASS, B.D. Ripley) — verified as PLOT-ONLY from the stats:::cpgram source; the algorithm + the KS band constant were reproduced
- Venables & Ripley 2002 'Modern Applied Statistics with S' (MASS) pp. 392-397 (spectral analysis, the cumulative periodogram / Bartlett's Tp white-noise test)
- Bloomfield 1976 'Fourier Analysis of Time Series: An Introduction' Wiley (the equivalent bandwidth, tapering)
- Brockwell & Davis 1991 'Time Series: Theory and Methods' 2nd ed Springer (periodogram consistency, smoothing)
- Priestley 1981 'Spectral Analysis and Time Series' Academic Press (AR spectral estimation)
- wrapper footer IMPLEMENTATION NOTE (c27_frequency_domain/spectral_periodogram_quick)
