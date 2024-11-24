import json

# Data to be written into JSON
data =[
        {
    "name": "DY",
    "location": "/uscms/home/reshmar/nobackup/CMSSW_13_0_13/src/iDMe/AODSkimmer/Final_DYJets_2022_output.root",
    "type": "bkg",
    "year": 2022,
    "xsec": 10,
    "nFile": 1,
    "blacklist": [],
    "sum_wgt": 1000,
    "num_events": 1000,
    "nFiles": 1
}
]
# Write data to JSON file
with open('Final2022bkg.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("JSON file created successfully!")

