import ROOT
from ROOT import TCanvas
from ROOT import TH1D

f = ROOT.TFile("iDMe_Mchi-10p5_dMchi-1p0_mZDinput-30p0_ctau-0_1jet_icckw1_drjj0_xptj80_xqcut20_slc7_amd64_gcc11_CMSSW_13_0_13_tarball_22577496_MINIAOD_ctau-10.0_year-2022.root", "READ")

tree=f.Get("Events")
                  

for i,event in enumerate(tree):    
    genparticles = event.recoGenParticles_prunedGenParticles__PAT
    n_particles = genparticles.size()
    
    
    for j in range(0,n_particles):
        gp=genparticles.at(j) 
        pdg = gp.pdgId()

        if pdg == 11:
            if gp.numberOfMothers() > 0:
                mother = gp.mother()
                print (mother)
                
                print (f"Event {i} has gen electrons with mother")
                
    if j==3:
        break

    if i==2:
        break

   
       