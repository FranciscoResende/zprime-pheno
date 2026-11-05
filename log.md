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
