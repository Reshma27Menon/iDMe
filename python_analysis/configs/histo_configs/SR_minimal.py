from histobins import *
from hist import Hist
import hist
import numpy as np
import awkward as ak

def make_histograms():
    histograms = {
        # quantities associated w/ selected vertex
        #"bdtScore" : Hist(samp,cut,bdtScore,storage=hist.storage.Weight()),
        #"gen_met_noWgt" :  Hist(samp,cut,met,storage=hist.storage.Weight()),
        #"gen_met" :  Hist(samp,cut,met,storage=hist.storage.Weight()),
        #"gen_leadjet_pt" : Hist(samp,cut,jet_pt,storage=hist.storage.Weight()),
        #"gen_leadjet_pt_noWgt" : Hist(samp,cut,jet_pt,storage=hist.storage.Weight())
        "sel_vtx_pt" : Hist(samp,cut,ele_pt,storage=hist.storage.Weight())
        #"sel_vtx_eta" : Hist(samp,cut,ele_eta,storage=hist.storage.Weight())

    }
    print ("type:",type(histograms))
    return histograms

subroutines = []

def fillHistos(events,histos,samp,cut,info,sum_wgt=1):
    
    e1 = events.sel_vtx.e1
    e2 = events.sel_vtx.e2
    min_dxy = np.minimum(np.abs(e1.dxy),np.abs(e2.dxy))
    max_pfiso = ak.where(e1.PFRelIso<e2.PFRelIso,e2.PFRelIso,e1.PFRelIso)
    wgt = events.eventWgt/sum_wgt
    vtx = events.sel_vtx
    histos["sel_vtx_pt"].fill(samp=samp,cut=cut,pt=vtx.pt,weight=wgt)
    #histos["sel_vtx_eta"].fill(samp=samp,cut=cut,eta=vtx.eta,weight=wgt)