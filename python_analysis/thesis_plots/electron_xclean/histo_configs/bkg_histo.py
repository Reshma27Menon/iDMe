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
    
    
    
    return h

subroutines = []


def fillHistos(events,h,samp,cut,info,sum_wgt=1):
    h.samp = samp
    h.cut = cut
    wgt = events.eventWgt/sum_wgt
    
    if info["type"] == "signal":

        Lxy = events.lptvtx.vxy
        Pt = events.lptvtx.pt



        h.fill("vxy", vxy=Lxy)
        h.fill("pt", pt=Pt)

        

        








        

        