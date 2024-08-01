from histobins import *
from hist import Hist
import hist
import numpy as np
import awkward as ak

def make_histograms():
    histograms = {
        # quantities associated w/ selected vertex
        "bdtScore" : Hist(samp,cut,bdtScore,storage=hist.storage.Weight()),
        "gen_met_noWgt" :  Hist(samp,cut,met,storage=hist.storage.Weight()),
        "gen_met" :  Hist(samp,cut,met,storage=hist.storage.Weight()),
        "gen_leadjet_pt" : Hist(samp,cut,jet_pt,storage=hist.storage.Weight()),
        "gen_leadjet_pt_noWgt" : Hist(samp,cut,jet_pt,storage=hist.storage.Weight()),
        "sel_vtx_type" : Hist(samp,cut,vtx_type,storage=hist.storage.Weight()),
        "sel_vtx_sign" : Hist(samp,cut,vtx_sign,storage=hist.storage.Weight()),
        "sel_vtx_dR" : Hist(samp,cut,dR,storage=hist.storage.Weight()),
        "sel_vtx_chi2" : Hist(samp,cut,vtx_chi2,storage=hist.storage.Weight()),
        "sel_vtx_prob" : Hist(samp,cut,vtx_prob,storage=hist.storage.Weight()),
        "sel_vtx_vxy" : Hist(samp,cut,vxy,storage=hist.storage.Weight()),
        "sel_vtx_vxy_zoom" : Hist(samp,cut,vxy_zoom,storage=hist.storage.Weight()),
        "sel_vtx_vxy_zoomzoom" : Hist(samp,cut,vxy_zoomzoom,storage=hist.storage.Weight()),
        "sel_vtx_vxySignif" : Hist(samp,cut,vtx_vxySignif,storage=hist.storage.Weight()),
        "sel_vtx_mass" : Hist(samp,cut,mass,storage=hist.storage.Weight()),
        "sel_vtx_minDxy" : Hist(samp,cut,ele_dxy,storage=hist.storage.Weight()),
        "sel_vtx_minDxy_fine": Hist(samp,cut,dxy_fine,storage=hist.storage.Weight()),
        "sel_vtx_pt" : Hist(samp,cut,ele_pt,storage=hist.storage.Weight()),
        "sel_vtx_eta" : Hist(samp,cut,ele_eta,storage=hist.storage.Weight()),
        "sel_vtx_phi" : Hist(samp,cut,ele_phi,storage=hist.storage.Weight()),
        "sel_vtx_matchType" : Hist(samp,cut,vtx_matchType,storage=hist.storage.Weight()),
        "sel_vtx_max_chi2" : Hist(samp,cut,ele_chi2,storage=hist.storage.Weight()),
        "sel_vtx_min_pt" : Hist(samp,cut,ele_pt,storage=hist.storage.Weight()),
        "sel_vtx_maxPFIso" : Hist(samp,cut,ele_PFRelIso,storage=hist.storage.Weight()),
        "sel_vtx_minEledRj" : Hist(samp,cut,dR,storage=hist.storage.Weight()),
        "sel_vtx_minEledPhiJ" : Hist(samp,cut,dphi_generic,storage=hist.storage.Weight()),
        "sel_vtx_METdPhi_vs_matchType" : Hist(samp,cut,dphi,vtx_matchType,storage=hist.storage.Weight()),
        "sel_vtx_minEledRj_vs_matchType" : Hist(samp,cut,dR,vtx_matchType,storage=hist.storage.Weight()),
        "sel_vtx_minEledPhiJ_vs_matchType" : Hist(samp,cut,dphi_generic,vtx_matchType,storage=hist.storage.Weight()),
        "sel_vtx_mindRj" : Hist(samp,cut,dR,storage=hist.storage.Weight()),
        "sel_vtx_mindPhiJ" : Hist(samp,cut,dphi_generic,storage=hist.storage.Weight()),
        "sel_vtx_mindRj_vs_matchType" : Hist(samp,cut,dR,vtx_matchType,storage=hist.storage.Weight()),
        "sel_vtx_mindPhiJ_vs_matchType" : Hist(samp,cut,dphi_generic,vtx_matchType,storage=hist.storage.Weight()),
        "met_over_lead_jet_pt" : Hist(samp,cut,met_over_pt,storage=hist.storage.Weight()),
        "lead_jet_met_dPhi" : Hist(samp,cut,dphi,storage=hist.storage.Weight()),
        "min_jet_met_dPhi" : Hist(samp,cut,dphi,storage=hist.storage.Weight()),
        "vtx_met_dPhi" : Hist(samp,cut,dphi,storage=hist.storage.Weight()),
        "sel_vtx_METdPhi_over_pT" : Hist(samp,cut,METdPhi_over_pT,storage=hist.storage.Weight()),
        "sel_vtx_METdPhi_over_m" : Hist(samp,cut,METdPhi_over_m,storage=hist.storage.Weight()),
        "sel_vtx_METdPhi_over_pTm" : Hist(samp,cut,METdPhi_over_pTm,storage=hist.storage.Weight()),
        "sel_vtx_METdPhi_over_mpT" : Hist(samp,cut,METdPhi_over_mpT,storage=hist.storage.Weight()),
        "MET_pt" : Hist(samp,cut,met_pt,storage=hist.storage.Weight()),
        "nJets" : Hist(samp,cut,njets,storage=hist.storage.Weight()),
        "minBtag" : Hist(samp,cut,btag,storage=hist.storage.Weight()),
        "lead_jet_abseta" : Hist(samp,cut,jet_abseta,storage=hist.storage.Weight()),
        "lead_jet_pt" : Hist(samp,cut,jet_pt,storage=hist.storage.Weight())
    }
    return histograms

subroutines = []

def fillHistos(events,histos,samp,cut,info,sum_wgt=1):
    e1 = events.sel_vtx.e1
    e2 = events.sel_vtx.e2
    max_pfiso = ak.where(e1.PFRelIso<e2.PFRelIso,e2.PFRelIso,e1.PFRelIso)
    wgt = events.eventWgt/sum_wgt
    vtx = events.sel_vtx
    min_dxy = np.minimum(np.abs(e1.dxy),np.abs(e2.dxy))


    if 'BDTScore' in events.fields:
        histos["bdtScore"].fill(samp=samp,cut=cut,score=events.BDTScore,weight=wgt)
    if info['type'] == "signal" or info["type"] == "bkg":
        histos['gen_met_noWgt'].fill(samp=samp,cut=cut,met=events.GenMET.pt,weight=1)
        histos['gen_met'].fill(samp=samp,cut=cut,met=events.GenMET.pt,weight=wgt)
        histos['gen_leadjet_pt'].fill(samp=samp,cut=cut,pt=events.GenJet.pt[:,0],weight=wgt)
        histos['gen_leadjet_pt_noWgt'].fill(samp=samp,cut=cut,pt=events.GenJet.pt[:,0],weight=1)
        histos["sel_vtx_type"].fill(samp=samp,cut=cut,type=vtx.typ,weight=wgt)
        histos["sel_vtx_type"].fill(samp=samp,cut=cut,type=vtx.typ,weight=wgt)
        histos["sel_vtx_sign"].fill(samp=samp,cut=cut,sign=vtx.sign,weight=wgt)
        histos["sel_vtx_dR"].fill(samp=samp,cut=cut,dr=vtx.dR,weight=wgt)
        histos["sel_vtx_chi2"].fill(samp=samp,cut=cut,chi2=vtx.reduced_chi2,weight=wgt)
        histos["sel_vtx_prob"].fill(samp=samp,cut=cut,prob=vtx.prob,weight=wgt)
        histos["sel_vtx_vxy"].fill(samp=samp,cut=cut,vxy=vtx.vxy,weight=wgt)
        histos["sel_vtx_vxy_zoom"].fill(samp=samp,cut=cut,vxy=vtx.vxy,weight=wgt)
        histos["sel_vtx_vxy_zoomzoom"].fill(samp=samp,cut=cut,vxy=vtx.vxy,weight=wgt)
        histos["sel_vtx_vxySignif"].fill(samp=samp,cut=cut,vxy_signif=vtx.vxy/vtx.sigmavxy,weight=wgt)
        histos["sel_vtx_mass"].fill(samp=samp,cut=cut,mass=vtx.m,weight=wgt)
        histos["sel_vtx_minDxy"].fill(samp=samp,cut=cut,dxy=min_dxy,weight=wgt)
        histos["sel_vtx_minDxy_fine"].fill(samp=samp,cut=cut,dxy=min_dxy,weight=wgt)
        histos["sel_vtx_pt"].fill(samp=samp,cut=cut,pt=vtx.pt,weight=wgt)
        histos["sel_vtx_eta"].fill(samp=samp,cut=cut,eta=vtx.eta,weight=wgt)
        histos["sel_vtx_phi"].fill(samp=samp,cut=cut,phi=vtx.phi,weight=wgt)
        histos["sel_vtx_max_chi2"].fill(samp=samp,cut=cut,chi2=ak.where(e1.trkChi2>e2.trkChi2,e1.trkChi2,e2.trkChi2),weight=wgt)
        histos["sel_vtx_min_pt"].fill(samp=samp,cut=cut,pt=ak.where(e1.pt<e2.pt,e1.pt,e2.pt),weight=wgt)
        histos["sel_vtx_maxPFIso"].fill(samp=samp,cut=cut,relIso=max_pfiso,weight=wgt)
        histos["sel_vtx_minEledRj"].fill(samp=samp,cut=cut,dr=np.minimum(e1.mindRj,e2.mindRj),weight=wgt)
        histos["sel_vtx_minEledPhiJ"].fill(samp=samp,cut=cut,dphi=np.minimum(e1.mindPhiJ,e2.mindPhiJ),weight=wgt)
        histos["sel_vtx_mindRj"].fill(samp=samp,cut=cut,dr=events.sel_vtx.mindRj,weight=wgt)
        histos["sel_vtx_mindPhiJ"].fill(samp=samp,cut=cut,dphi=events.sel_vtx.mindPhiJ,weight=wgt)
        histos["MET_pt"].fill(samp=samp,cut=cut,met_pt=events.PFMET.pt,weight=wgt)
        histos["nJets"].fill(samp=samp,cut=cut,njets=ak.count(events.PFJet.pt,axis=1),weight=wgt)
        histos["lead_jet_pt"].fill(samp=samp,cut=cut,pt=ak.fill_none(ak.pad_none(events.PFJet.pt,1),-999)[:,0],weight=wgt)
        histos["lead_jet_met_dPhi"].fill(samp=samp,cut=cut,dphi=np.abs(events.PFJet.METdPhi[:,0]),weight=wgt)
        histos["lead_jet_abseta"].fill(samp=samp,cut=cut,eta=np.abs(ak.fill_none(ak.pad_none(events.PFJet.eta,1),-999))[:,0],weight=wgt)
   