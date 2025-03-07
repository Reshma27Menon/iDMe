import json

# Data to be written into JSON
data =[
{
    "name": "WJetsToLNu1",
    "location": "/eos/uscms/store/group/lpcmetx/iDMe/Samples/Ntuples/background_WJetsHT17Feb2025/2022/WJets/WJetsToLNu1/WtoLNu-4Jets_MLNu-0to120_HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/crab_iDMe_WJetsToLNu1_2025_02_17-12_31/250217_183428/0000",
    "type": "bkg",
    "year": 2022,
    "nFiles":70
    
},
{
    "name": "WJetsToLNu2",
    "location": "/eos/uscms/store/group/lpcmetx/iDMe/Samples/Ntuples/background_WJetsHT17Feb2025/2022/WJets/WJetsToLNu2/WtoLNu-4Jets_MLNu-0to120_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/crab_iDMe_WJetsToLNu2_2025_02_17-12_34/250217_183445/0000",
    "type": "bkg",
    "year": 2022,
    "nFiles":16
},
{
    "name": "WJetsToLNu3",
    "location": "/eos/uscms/store/group/lpcmetx/iDMe/Samples/Ntuples/background_WJetsHT17Feb2025/2022/WJets/WJetsToLNu3/WtoLNu-4Jets_MLNu-0to120_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/crab_iDMe_WJetsToLNu3_2025_02_17-12_34/250217_183502/0000",
    "type": "bkg",
    "year": 2022,
    "nFiles":29
},
{
    "name": "WJetsToLNu4",
    "location": "/eos/uscms/store/group/lpcmetx/iDMe/Samples/Ntuples/background_WJetsHT17Feb2025/2022/WJets/WJetsToLNu4/WtoLNu-4Jets_MLNu-0to120_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/crab_iDMe_WJetsToLNu4_2025_02_17-12_35/250217_183518/0000",
    "type": "bkg",
    "year": 2022,
    "nFiles":34
},
{
    "name": "WJetsToLNu5",
    "location": "/eos/uscms/store/group/lpcmetx/iDMe/Samples/Ntuples/background_WJetsHT17Feb2025/2022/WJets/WJetsToLNu5/WtoLNu-4Jets_MLNu-0to120_HT-40to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/crab_iDMe_WJetsToLNu5_2025_02_17-12_35/250217_183533/0000",
    "type": "bkg",
    "year": 2022,
    "nFiles":77
},
{
    "name": "WJetsToLNu6",
    "location": "/eos/uscms/store/group/lpcmetx/iDMe/Samples/Ntuples/background_WJetsHT17Feb2025/2022/WJets/WJetsToLNu6/WtoLNu-4Jets_MLNu-0to120_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/crab_iDMe_WJetsToLNu6_2025_02_17-12_35/250217_183550/0000",
    "type": "bkg",
    "year": 2022,
    "nFiles":16
}
    
    
        
]
# Write data to JSON file
with open('AllWJets2022.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("JSON file created successfully!")

