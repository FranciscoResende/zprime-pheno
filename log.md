# Lab log

## 2026-11-04 — Setup
- lxplus, LCG_110 (x86_64-el9-gcc13-opt), AFS workspace /afs/cern.ch/work/f/frresend
- MG5_aMC v3.5.17 (LTS), Pythia 8.317, Delphes (installed via MG `install`), LHAPDF/fastjet from LCG
- Mathematica 15.0.1 via TUM site licence
- Smoke test: pp > mu+ mu-, 13 TeV, default sm model and run card, 10k events
  - sigma = 844.3 +- 1.9 pb (LO, default cuts)
  - Chain MG -> Pythia8 -> Delphes works; output in test_dy/Events/run_01/
## 2026-11-05 — QED check: u u~ > gamma* > mu+ mu-
- Hand calculation (tree level, massless, spin- and colour-averaged):
  |M|^2 = (1/3) e^4 Q_u^2 (1+cos^2 theta),  sigma = 4 pi alpha^2 Q_u^2 / (9 s)
- MG setup: generate u u~ > mu+ mu- / z; lpp1=lpp2=0, ebeam1=ebeam2=50 GeV, no cuts (ptl 0, etal -1, mmll 0, drll 0)
- alpha from sm param_card: aEWM1 = 132.507
- Hand: 1.376 pb | MadGraph (run_02): 1.377 +- 0.0004 pb  -> agreement
- Note: systematics module fails without PDFs -> use_syst False
## 2026-11-09 - Drell Yang process, full chain
- Understanding the parton density function, how one can visualize it as cross section of the partons times the parton luminosity
- changing parameters of the Cards so as to simulate an actual pp collision
- Pythia, with its parton shower, hadronisation, FSR and ISR, and some decays
- Delphes, detector effects, parametric
- First root plot, peak at half Z mass, resonance production, steep drop of from the jacobian, long tail from photon production
- Next: mll.py (uproot), 3-level overlay, mass slices, ttbar
- Run: test_dy/Events/run_02, pp > mu+ mu-, 13 TeV, 10k events, seed 1, CMS Delphes card
- Cuts: ptl > 10, |etal| < 2.5, mmll > 60 GeV
- sigma = 650.7 pb (vs 844 pb without the mmll cut -> ~190 pb from low-mass gamma*)
## 2026-11-15 — Z peak fit, mass slices
- New PC (AlmaLinux 10); VS Code Remote-SSH on lxplus.
  Fixes: GSSAPIDelegateCredentials (AFS token), .vscode-server -> workspace (home quota, error -122)
- Selection (run_02, CMS card): 6819/10000 events with exactly 2 muons (68.2%), all opposite-sign
  (Delphes takes charge from truth -> no charge flips by construction)
- Z peak: FWHM 4.2 GeV (1/6 GeV bins, 80-100)
- Voigt fit (80-100 GeV): m0 = 90.952 +- 0.030, sigma = 1.15 +- 0.12, gamma = 1.52 +- 0.12 GeV
  -> mass resolution ~1.3%; Gamma = 3.04 +- 0.24 (vs 2.50), m0 0.24 GeV low:
     FSR low-side tail pulls a symmetric Voigt; rho(sigma, gamma) = -0.93
  TODO: Delta-x in model (N), residuals, parton-level check
- Slice dy_200_500 (ATLAS card, iseed 2): sigma = 1.226 +- 0.003 pb = 0.19% of sigma(>60)
  my prediction: ...
- Running: cards/dy_slices.mg5 (60-120, 120-200, 500-1000, 1000-2000, 2000+; iseeds 3-7)
- Next: ttbar (dimuon), stitching with sigma/N weights, three-level overlay
## 2026-11-15 (cont.) — DY mass slices + ttbar background
- DY slices: test_dy, ATLAS Delphes card, 10k events each, ptl>10, |etal|<2.5
  script: cards/dy_slices.mg5 (iseeds 3-7; 200-500 run separately, iseed 2)
  | slice (GeV) | sigma (pb)  | sigma/dm (pb/GeV) |
  | 60-120      | 643.99      | 1.07e+1 |
  | 120-200     | 6.9965      | 8.7e-2  |
  | 200-500     | 1.2259      | 4.1e-3  |
  | 500-1000    | 0.0572      | 1.1e-4  |
  | 1000-2000   | 3.982e-3    | 4.0e-6  |
  | 2000+       | 1.336e-4    | -       |
- Sum check: sum of slices = 652.3 pb vs inclusive run_02 (m>60) 650.7 +- 1.4 pb
  -> agree within ~1 sigma: no gaps / double counting
- Fall-off: m^3 * sigma/dm ~1.8e5 (350 GeV) -> ~1.3e4 (1500 GeV), x13
  (parton luminosity); consistent with 9 Nov prediction (x15-25 over 200-2000 GeV)
- 2000+: 0.13 fb -> ~19 DY events in 140 fb^-1 before selection
- ttbar -> b b~ mu+ mu- vm vm~ (decay chains), ATLAS card, iseed 8, 10k events
  output on EOS: /eos/user/f/frresend/zprime-data/ttbar_mumu (run ttbar_mumu_01)
  sigma = 5.692 +- 0.013 pb vs hand 500 pb x 0.106^2 = 5.6 pb
  (MG LO BR(W->mu nu) ~ 1/9 -> implies sigma_ttbar(LO) ~ 460 pb)
- Note: new process folders go to EOS from now on (workspace quota, hepmc size)
- Next: stitch slices (weights sigma/N), overlay ttbar, three-level overlay
## 2026-11-22 — Week 2 wrap-up: stitched DY, ttbar, mass resolution, Voigt revisited

### Stitched Drell–Yan (6 slices, 60 GeV – inf)
- Weight per event w_i = sigma_i / N_gen,i (N_gen = 10k, all generated, not selected)
- One histogram, 60 log-spaced bins (np.geomspace, 60–3000 GeV), slices summed bin by bin,
  divided by bin width -> dsigma/dm [pb/GeV], log-log
- No steps at slice edges (120, 200, 500, 1000, 2000) -> weights and ranges consistent
- sigma after selection (2 OS muons) = 446.8 pb of 652.3 pb generated (68.5%)
- Shape: Z peak, gamma*/FSR shoulder below, ~power law above 150 GeV, bends down > 1 TeV (PDFs)
- Plot: plots/Differential_cross_section_Z.png

### ttbar (dimuon) background
- Same selection/edges, w = 5.692 / 10000
- 1.96 pb of 5.69 pb pass (34%; softer, less isolated muons next to b-jets)
- Broad, no peak; closest to DY at ~200–600 GeV, there ~3–5x below DY
- "max ttbar/DY = 0.54 at ~950 GeV" = single event, not physics
- No ttbar statistics above ~700 GeV -> if needed in week 5: high-mll ttbar sample with
  cut_decays = True (default cuts don't reach decay products), stitch on TRUE mll to avoid double counting
- Plot: plots/mll_dy_ttbar.pdf

### Muon mass resolution (truth vs reco, event by event)
- Truth: Particle branch, |PID| = 13 & Status = 1, exactly 2, PID sum = 0
- Reco: Muon branch, exactly 2, charge sum = 0
- Combined mask (true & reco) applied to both -> same events, same order
- (m_reco - m_true) / m_true, per slice:
  - 60–120: std 1.36%, 68% half-width 1.26%, FWHM/2.355 1.10% -> core ~1.1%, non-Gaussian tails
  - > 2 TeV: ~8–10%
- Why: sagitta ∝ 1/pT, fixed hit resolution -> sigma_pT/pT = a (mult. scattering, const) ⊕ b*pT;
  crossover ~100 GeV. Tails = mix of barrel/endcap resolutions
- Consequence: a 2 TeV Z' is smeared to ~150–200 GeV -> sets the search window
- Plot: plots/mass_resolution.pdf

### Voigt fit revisited (dy_60_120)
- Fixed: model = N * voigt * Delta_m -> N = number of events (binning-independent).
  N > events in window because Lorentzian tails extend outside the window
- 86–96 GeV window:
  | level            | Gamma = 2 gamma | m0     |
  | input (MG)       | 2.50            | 91.19  |
  | truth post-FSR   | 2.70 +- 0.10    | 91.04  |
  | reco             | 3.43 +- 0.27    | 90.92  |
- Narrow window did NOT fix Gamma -> not the far FSR tail. Excess = ~0.2 GeV physics
  (FSR inside the peak, parton lumi, gamma*/Z) + ~0.7 GeV detector (non-Gaussian tails absorbed into gamma)
- sigma_Voigt ~0.8–0.95 GeV (~1%) agrees with direct resolution core (1.1%)
- rho(sigma, gamma) = -0.83 / -0.93: strongly degenerate
- Plot: plots/voigt_fit_Z.pdf

### Open / low priority
- Pre-FSR Voigt fit (should give Gamma = 2.50)
- Unexplained m0 shift truth -> reco (-0.12 +- 0.04 GeV)
- Use ONE Delphes card for all samples from now on (run_02 was CMS, slices ATLAS — check)
- Parton vs detector overlay: quick version done (see plots/truth_vs_reco.pdf)

### Next
- Week 3: install FeynRules, test with Mathematica, IDPASC Z' tutorial
