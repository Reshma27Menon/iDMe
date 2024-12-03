import numpy as np
import awkward as ak
import sys
sys.path.append("../../../analysisTools/")
import analysisSubroutines as routines

def cut1(events,info):
    name = "cut1"
    desc = "Pass MET Filters"
    plots = True
    cut = events.METFiltersFailBits == 0
    return events[cut], name, desc, plots

def cut2(events,info):
    name = "cut2"
    desc = "HEM Veto"
    plots = True
    if info["year"] == 2018:
        cut = (events.hasHEMjet == 0) & (events.hasHEMelecPF == 0) & (events.hasHEMelecLpt == 0)
        return events[cut], name, desc, plots
    else:
        return events, name, desc, plots



def cut4(events,info):
    name = "cut4"
    desc = "MET > 200 GeV"
    plots = True
    cut = events.PFMET.pt > 200
    return events[cut], name, desc, plots


def cut6(events,info):
    name = "cut6"
    desc = "Leading jet pT > 80 GeV"
    plots = True
    cut = events.PFJet.pt[:,0] > 80
    return events[cut], name, desc, plots


def cut7(events,info):
    name = "cut7"
    desc = "Leading jet |eta| < 2.4"
    plots = True
    cut = np.abs(events.PFJet.eta[:,0]) < 2.4
    return events[cut], name, desc, plots


def cut8(events,info):
    name = "cut8"
    desc = "dPhi(MET,leading jet) > 2.0"
    plots = True
    cut = np.abs(events.PFJet.METdPhi[:,0]) > 2.0
    return events[cut], name, desc, plots

def cut9(events,info):
    name = "cut9"
    desc = "dPhi(MET,all jets) > 0.75"
    plots = True
    cut = ak.all(np.abs(events.PFJet.METdPhi) > 0.75,axis=1)
    return events[cut], name, desc, plots

#def cut10(events,info):
   #name = "cut10"
   #desc = "BDT"
   #plots = True

   #thres = 0.955
   #thres = 0.975
   #thres = 0.98 # Tight
   
   #if len(events) != 0:
       #input = routines.makeBDTinputsv4(events)
   
       #model = './models/BDT_comb4_max_depth_7_n_estimators_800_lr_0.005.json'
       #score_BDT = routines.getBDTscore(input, model)

       #cut = score_BDT > thres

       #print(f'BDT Pass: {np.count_nonzero(cut)}/{len(cut)}')
   #else:
       #cut = []
   
   #return events[cut], name, desc, plots
