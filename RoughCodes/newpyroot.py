import ROOT
from ROOT import TCanvas
from ROOT import TH1D

f = ROOT.TFile("iDMe_Mchi-10p5_dMchi-1p0_mZDinput-30p0_ctau-0_1jet_icckw1_drjj0_xptj80_xqcut20_slc7_amd64_gcc11_CMSSW_13_0_13_tarball_22577496_MINIAOD_ctau-10.0_year-2022.root", "READ")

tree=f.Get("Events")

#print ("Total number of events = ", tree.GetEntries())
                  
branch = tree.GetBranch("recoGenParticles_prunedGenParticles__PAT.obj.m_state.vertex_.fCoordinates.fY")
#print (branch)

#tree.Draw("recoGenParticles_prunedGenParticles__PAT.obj.m_state.vertex_.fCoordinates.fY","recoGenParticles_prunedGenParticles__PAT.obj.m_state.pdgId_ == 11")

hist = TH1D("", "", 10,0,10)

# tree.Draw("recoGenParticles_prunedGenParticles__PAT.obj.m_state.vertex_.fCoordinates.fY","recoGenParticles_prunedGenParticles__PAT.obj.m_state.pdgId_ == 11")
# c.Draw()

# input ("Press Enter to exit...")
# c.SaveAs("diag.png")

for i,event in enumerate(tree):
    genparticles = event.recoGenParticles_prunedGenParticles__PAT
    n_particles = genparticles.size()
    #print(f"Event {i} has {n_particles} gen particles")
    
    n_electrons =0
    for j in range(0,n_particles):
        pdg = genparticles.at(j).pdgId()   
          
        if pdg == 11:
            #print (f"Gen particle {j} has pdgID = 11")
            n_electrons = n_electrons+1
    #print (f"Total number of gen electrons in Event {i} is {n_electrons}")
    
    hist.Fill(n_electrons)

c = TCanvas("c", "", 800, 700)

hist.Draw()
hist.GetXaxis().SetTitle("Number of gen electrons per event")
c.Draw()
c.SaveAs("gen_electrons_perevent.png")




                
                
                
            


  