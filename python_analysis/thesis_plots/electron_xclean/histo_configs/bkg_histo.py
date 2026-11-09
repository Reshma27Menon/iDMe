from hist import Hist
from hist.axis import StrCategory, Regular, Integer, IntCategory, Variable
import hist
import numpy as np
import awkward as ak
import analysisSubroutines as sub

# General Purpose
samp = StrCategory([],name="samp",label="Sample Name",growth=True)
cut = StrCategory([],name="cut",label="Cut Applied",growth=True)


# functions to make histograms
class myHisto:
    def __init__(self):
        
        self.histograms = {}
        self.samp = "NO_SAMPLE"
        self.cut = "NO_CUT"

        # axis compendium
        self.samp = StrCategory([],name="samp",label="Sample Name",growth=True)
        self.cut = StrCategory([],name="cut",label="Cut Applied",growth=True)
        
        self.vxy = self.parse_axis(('vxy',[0,1,5,10,15,20] )) 
        self.pt = self.parse_axis(('pt',[0,5,10,20,100] )) 
        self.dr = self.parse_axis(('dr',[0,0.01,0.1,1,5] ))  
        self.eta = self.parse_axis(('eta',500,-5,5))
        self.phi = self.parse_axis(('phi',500,-5,5))

        self.Ossf = self.parse_axis(("Ossf", [-1, 1]))
        self.Chi2 = self.parse_axis(("Chi2", 100, 0, 20))
        self.Mass = self.parse_axis(("Mass", 100, 0, 1))
        self.EleDphi = self.parse_axis(("EleDphi", 64, -np.pi, np.pi))
        self.Dxy = self.parse_axis(("Dxy", 800, -5, 5))
        self.Mindxy = self.parse_axis(("Mindxy", 800, -5, 5))

        self.IDcut = self.parse_axis(("IDcut", [0, 5]))
        self.MaxMiniIso = self.parse_axis(("MaxMiniIso", 500, 0, 10))
        

        
        

    def make(self,name,*args,**hist_kwargs):
        if name in self.histograms.keys():
            print(f"Histogram {name} already exists! Skipping")
            return
        axes = [self.samp,self.cut]
        for ax in args:
            if type(ax) == tuple:
                axes.append(self.parse_axis(ax))
            else:
                axes.append(getattr(self,ax))
        self.histograms[name] = Hist(*axes,storage=hist.storage.Weight(),**hist_kwargs)
    
    def fill(self,name,**kwargs):
        self.histograms[name].fill(samp=self.samp,cut=self.cut,**kwargs)
    
   
    #I made it a bit CASE-SPECIFIC

    def parse_axis(self,a):
        name = a[0]
        if type(a[1]) == list:
            assert len(a) == 2
            if (len(a[1]) > 2):
                axis = Variable(a[1],name=name,label=name)
            else:
                if type(a[1][0]) == str:
                    axis = StrCategory(a[1],name=name,label=name)
                if type(a[1][0]) == int: 
                    axis = IntCategory(a[1],name=name,label=name)
           

        else:
            assert len(a) == 4
            axis = Regular(a[1],a[2],a[3],name=name,label=name)
        return axis

def make_histograms():
    h = myHisto()

    h.make("vxy", "vxy")
    h.make("pt", "pt")
    h.make("dr", "dr")
    h.make("eta", "eta")
    h.make("phi", "phi")

    h.make("ossf", "Ossf")
    h.make("chi2", "Chi2")
    h.make("mass", "Mass")

    h.make("eleDphi", "EleDphi")
    h.make("mindxy", "Mindxy")
    h.make("dxy", "Dxy")
    h.make("IDcut", "IDcut")
    h.make("maxMiniIso", "MaxMiniIso")
    
    
    
    return h

subroutines = []


def fillHistos(events,h,samp,cut,info,sum_wgt=1):
    h.samp = samp
    h.cut = cut
    wgt = events.eventWgt/sum_wgt

    if info["type"] == "signal":
        
        
        #Start the numerator:        
        
        maskAA =  ( (events.GenEle.matchedAllLowPt) & (events.GenPos.matchedAllLowPt) )

        evAA  = events[maskAA]

        mask2AA =  ak.any(     evAA.vtx.isMatched & evAA.vtx.isGood,    axis=1)

        ev_newAA = evAA[mask2AA] #Events which has atleast one matched vertex
        num_count = len(ev_newAA)
        
        print ("Numerator count=", num_count)
        
        # h.fill("eff_num", count=0.5, weight=num_count)    
        

        # Flatten the per-event vertex lists into one list of vertices.
        ossf = ak.flatten(ev_newAA.vtx.sign, axis=1)
        chi2 = ak.flatten(ev_newAA.vtx.reduced_chi2, axis=1)
        mass = ak.flatten(ev_newAA.vtx.refit_m, axis=1)
        eleDphi = ak.flatten(ev_newAA.vtx.eleDphi, axis=1)
        mindxy = ak.flatten(ev_newAA.vtx.min_dxy, axis=1)
        dxy = ak.flatten(ev_newAA.vtx.e1.dxy, axis=1)
        IDcut = ak.flatten(ev_newAA.vtx.e1.passID & ev_newAA.vtx.e2.passID)
        maxMiniIso = ak.flatten(ev_newAA.vtx.e1.miniRelIsoEleCorr)

        LXY = ak.flatten(ev_newAA.vtx.vxy, axis=1)
        PT = ak.flatten(ev_newAA.vtx.pt, axis=1)
        DR = ak.flatten(ev_newAA.vtx.dR, axis=1)


        

        h.fill("ossf", Ossf=ossf)
        h.fill("chi2", Chi2=chi2)
        h.fill("mass", Mass=mass)
        h.fill("eleDphi", EleDphi=eleDphi)
        h.fill("mindxy", Mindxy=mindxy)                
        h.fill("dxy", Dxy=dxy)
        h.fill("IDcut", IDcut=IDcut)
        h.fill("maxMiniIso", MaxMiniIso=maxMiniIso)

        
        h.fill("vxy", vxy=LXY)
        h.fill("pt", pt=PT)
        h.fill("dr", dr=DR)
        


    
    if info["type"] == "bkg":

        sub.defineGoodLptVertices(events, version="v15acr", ele_id="dR" )

        print (events.lptvtx.fields )
        
        # Vtx = events.lptvtx
         

        # LXY = ak.flatten(Vtx.vxy, axis=1)
        # PT = ak.flatten(Vtx.pt, axis=1)
        # DR = ak.flatten(Vtx.dR, axis=1)

        
        # eta = ak.flatten(Vtx.eta, axis=1)
        # phi = ak.flatten(Vtx.phi, axis=1)

        # ossf = ak.flatten(Vtx.sign, axis=1)
        # chi2 = ak.flatten(Vtx.reduced_chi2, axis=1)
        # mass = ak.flatten(Vtx.refit_m, axis=1)
        
        

        
        # h.fill("vxy", vxy=LXY)
        # h.fill("pt", pt=PT)
        # h.fill("dr", dr=DR)
        # h.fill("eta", eta=eta)
        # h.fill("phi", phi=phi)

        # h.fill("ossf", Ossf=ossf)
        # h.fill("chi2", Chi2=chi2)
        # h.fill("mass", Mass=mass)
        