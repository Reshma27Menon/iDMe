#!/bin/bash

echo "Current directory: $(pwd)"

# EOS_FILE=/eos/uscms/store/group/lpcmetx/iDMe/premix_files_prefixed.txt

EOS_FILE=root://cmsxrootd.fnal.gov//store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer22_124X_mcRun3_2022_realistic_v11-v2/2550001/77518c88-21fb-4593-9648-30a39aba4e8c.root
 
xrdfs root://cmseos.fnal.gov stat /store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer22_124X_mcRun3_2022_realistic_v11-v2/2550001/77518c88-21fb-4593-9648-30a39aba4e8c.root > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "File found. Copying and printing..."
    xrdcp -f $EOS_FILE TEST.root
    
else
    echo "Cannot access the file."
    exit 1
fi

# #!/bin/bash

# echo "Current directory: $(pwd)"

# EOS_FILE=/eos/uscms/store/group/lpcmetx/iDMe/premix_files_prefixed.txt

# if [ -r "$EOS_FILE" ]; then
#     echo "File is accessible locally: $EOS_FILE"
#     echo "Printing first 10 lines:"
#     head -n 10 "$EOS_FILE"
# else
#     echo "Cannot access the file locally: $EOS_FILE"
#     exit 1
# fi
