import uproot

# Replace this with the actual path to your file
#file_path = "/eos/uscms//store/group/lpcmetx/iDMe/Samples/Ntuples/background_WJets12022/2022/WJets/WJetsToLNu1/WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/crab_iDMe_WJetsToLNu1_2024_11_14-08_19/241114_142230/0000/WJetsToLNu1_1-1.root"

file_path = "root://cmseos.fnal.gov//eos/uscms//store/group/lpcmetx/iDMe/Samples/Ntuples/background_WJets12022/2022/WJets/WJetsToLNu1/WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/crab_iDMe_WJetsToLNu1_2024_11_14-08_19/241114_142230/0000/WJetsToLNu1_1-1.root"


#file_path = "root://cmsxrootd.fnal.gov//eos/uscms//store/group/lpcmetx/iDMe/Samples/Ntuples/background_WJets12022/2022/WJets/WJetsToLNu1/WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/crab_iDMe_WJetsToLNu1_2024_11_14-08_19/241115_142230/0000/WJetsToLNu1_1-1.root"

# Open the ROOT file
file = uproot.open(file_path)

# Print the contents of the file
print(file.keys())  # Lists all top-level objects in the ROOT file

tree = file["ntuples/outT"]
#print(tree.keys())  # Lists all branches in the tree

genWgt_array = tree["genWgt"].array()
print(len(genWgt_array))  # Print the first 10 values

