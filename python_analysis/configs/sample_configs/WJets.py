import json


data =[
        {
    "name": "WJets",
    "location": "/uscms/home/reshmar/nobackup/CMSSW_13_0_13/src/iDMe/AODSkimmer/WJetsToLNu1_2022_output.root",
    "type": "bkg",
    "year": 2022,
    "xsec": 10,
    "nFile": 1,
    "blacklist": [],
    "nFiles": 1
}
]
# Write data to JSON file
with open('WJets2022.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("JSON file created successfully!")

