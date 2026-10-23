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
        self.ele_type = self.parse_axis(('ele_type',['L','R']))
        self.match_type = self.parse_axis(('match_type',['L','R']))
        self.match = self.parse_axis(('match',[0,1]))
        self.met = self.parse_axis(('met',60,50,300))
        self.dR = self.parse_axis(('dR',50,0,5)) 
        self.mindR = self.parse_axis(('mindR',60,0,0.06))         
        
        self.dxy_gen = self.parse_axis(('dxy_gen',500,-3,3))  

        
        #For Resolution studies
        self.Res_LPT = self.parse_axis(('Res_LPT',500,-1,1))  
        self.Res_GED = self.parse_axis(('Res_GED',500,-1,1)) 
        
        self.Gen_pt = self.parse_axis(('Gen_pt',[0,5,10,20,30]))         
        self.Gen_dxy_res = self.parse_axis(('Gen_dxy_res',[0,1,3,6,10,30])) #Gen_vxy_FLAT in this case


        #With ev events:
        self.Gen_vxy_FLAT = self.parse_axis(('Gen_vxy_FLAT',1000,0,30)) #With cuts
        self.GED_vxy_flat = self.parse_axis(('GED_vxy_flat',1000,0,30)) #With cuts
        self.Lpt_vxy_flat = self.parse_axis(('Lpt_vxy_flat',1000,0,30)) #With cuts
        
        
        #For vtx Eff studies   
        
        self.pt_AA = self.parse_axis(('pt_AA',[0,5,10,20,100])) 
        self.vxy_AA = self.parse_axis(('vxy_AA',[0,1,5,10,15,20])) 
        self.dr_AA = self.parse_axis(('dr_AA',[0,0.01,0.1,1,5] ))  
        # self.dr_AA = self.parse_axis(('dr_AA', [0, 0.01, 0.02, 0.04, 0.06, 0.08, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.7, 1, 1.5, 2, 3, 4, 5] ))  


        self.pt_den = self.parse_axis(('pt_den',[0,5,10,20,100])) 
        self.vxy_den = self.parse_axis(('vxy_den',[0,1,5,10,15,20]))  
        self.dr_den = self.parse_axis(('dr_den',[0,0.01,0.1,1,5] ))  
        # self.dr_den = self.parse_axis(('dr_den', [0, 0.01, 0.02, 0.04, 0.06, 0.08, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.7, 1, 1.5, 2, 3, 4, 5])) 

        
        self.Lxy_genEE = self.parse_axis(('Lxy_genEE',1000,0,100))  
        self.Pt_genEE = self.parse_axis(('Pt_genEE',1000,0,100)) 
        self.dR_genEE = self.parse_axis(('dR_genEE',500,0,5)) 
        self.eta_genEE = self.parse_axis(('eta_genEE',500,-5,5))
        self.phi_genEE = self.parse_axis(('phi_genEE',500,-5,5))
        
        self.METdPhi = self.parse_axis(('METdPhi',500,-5,5))

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
    
    #ev quantities: 
    h.make('gen_ele_vxy','Gen_vxy_FLAT')    
    h.make('GED_vxy_flat', 'GED_vxy_flat')
    h.make('Lpt_vxy_flat', 'Lpt_vxy_flat')
    
   
    #Resolution in bins of a quantity:      
    
    h.make("genvtx_pt_vxy_dr_AA",'pt_AA','vxy_AA', 'dr_AA')
    
    h.make("genvtx_pt_vxy_dr_den",'pt_den','vxy_den', 'dr_den')

    
    return h

subroutines = []


def fillHistos(events,h,samp,cut,info,sum_wgt=1):
    h.samp = samp
    h.cut = cut
    wgt = events.eventWgt/sum_wgt
    
    if info["type"] == "signal":

        print(
    f"Histogram stage: {cut}; "
    f"good_vtx exists: {'good_vtx' in events.fields}; "
    f"isGood exists: {'isGood' in events.vtx.fields}"
)
        Lxy = events.GenEle.vxy  
        Pt =  events.genEE.pt
        dR =  events.genEE.dr

        MASK = ( (Lxy <10) & (Pt < 20) & (dR<1) )
        events = events[MASK]

        #Denominator count:
        den_count = len (events)
        print ("Denominator count=", den_count)        

        
        #Start the numerator:        
        
        maskAA =  ( (events.GenEle.matchedAllLowPt) & (events.GenPos.matchedAllLowPt) )

        evAA  = events[maskAA]

        mask2AA =  ak.any(     evAA.vtx.isMatched & evAA.vtx.isGood,    axis=1)

        ev_newAA = evAA[mask2AA] #Events which has atleast one matched vertex
        num_count = len(ev_newAA)
        print ("Numerator count=", num_count)
        

        gen_vxy_AA = ev_newAA.genEE.vxy
        gen_ee_pt_AA = ev_newAA.genEE.pt
        gen_dr_AA = ev_newAA.genEE.dr
        
        # h.fill("genvtx_pt_vxy_dr_AA",pt_AA=gen_ee_pt_AA, vxy_AA=gen_vxy_AA, dr_AA =gen_dr_AA)   #numerator: Only the gen vertices matched to LL 