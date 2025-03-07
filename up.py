import uproot

file = uproot.open("ntuples_WJets_WJetsToLNu1_9.root")
print(file.keys())

dir= file["ntuples"]
print (dir.keys())

