import uproot
import numpy as np
import matplotlib.pyplot as plt
file = uproot.open("/afs/cern.ch/work/f/frresend/MG5_aMC_v3_5_17/test_dy/Events/run_02/tag_1_delphes_events.root")
#print(file.keys())
#'Delphes;1'
#print(file['Delphes;1'])
delphes_events = file['Delphes;1']
#print(delphes_events.keys())
muon_events = delphes_events['Muon']
array_muon_events = muon_events.array()
print(array_muon_events)
#print(muon_events)
#print(delphes_events['Muon_size'])
muon_eta = muon_events['Muon.Eta']
muon_phi = muon_events['Muon.Phi']
muon_charge = muon_events['Muon.Charge']
muon_pt = muon_events['Muon.PT']
print(muon_eta)
#print(muon_events.keys())
#print(muon_events['Muon_Size'])
muon_events_eta_array = muon_eta.array()
muon_events_pt_array = muon_pt.array()
muon_events_charge_array = muon_charge.array()
muon_events_phi_array = muon_phi.array()
print(muon_events_eta_array, muon_events_pt_array, muon_events_charge_array, muon_events_phi_array)
values, counts = np.unique(muon_events, return_counts=True)
#plt.stairs(counts, bins)
print(values, counts)
print(counts[2]/(counts[0]+counts[1]+counts[2]))
print(counts[2]/(counts.sum()))