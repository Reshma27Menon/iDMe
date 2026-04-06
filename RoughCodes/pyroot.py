import ROOT

#ROOT.gROOT.SetBatch(True)

file = ROOT.TFile.Open("iDMe_Mchi-10p5_dMchi-1p0_mZDinput-30p0_ctau-0_1jet_icckw1_drjj0_xptj80_xqcut20_slc7_amd64_gcc11_CMSSW_13_0_13_tarball_22577496_MINIAOD_ctau-10.0_year-2022.root")
tree = file.Get("Events")

for event in tree:
    particles = getattr(event, "recoGenParticles_prunedGenParticles__PAT")
    print (particles)

c = ROOT.TCanvas()
h.Draw()
c.SaveAs("pdgId.png")

# c = ROOT.TCanvas()
# tree.Draw("recoGenParticles_prunedGenParticles__PAT.obj.m_state.pdgId_")
# c.Draw()


# for branch in tree.GetListOfBranches():
#     print(branch.GetName())

# branch_name = "recoGenParticles_prunedGenParticles__PAT."
# branch = tree.GetBranch(branch_name)
# print (branch)


# for leaf in branch.GetListOfLeaves():
#     print(f"  Leaf name: {leaf.GetName()}, Leaf title: {leaf.GetTitle()}, Leaf type: {leaf.GetTypeName()}")
