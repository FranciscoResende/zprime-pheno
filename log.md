# Lab log

## 2026-11-04 — Setup
- lxplus, LCG_110 (x86_64-el9-gcc13-opt), AFS workspace /afs/cern.ch/work/f/frresend
- MG5_aMC v3.5.17 (LTS), Pythia 8.317, Delphes (installed via MG `install`), LHAPDF/fastjet from LCG
- Mathematica 15.0.1 via TUM site licence
- Smoke test: pp > mu+ mu-, 13 TeV, default sm model and run card, 10k events
  - sigma = 844.3 +- 1.9 pb (LO, default cuts)
  - Chain MG -> Pythia8 -> Delphes works; output in test_dy/Events/run_01/
