#!/bin/bash

fname=$1
year=$2
nThreads=$3
isData=$4
isSignal=$5
outPath=$6

<<<<<<< HEAD
xrdcp root://cmseos.fnal.gov//store/group/lpcmetx/iDMe//compiled_CMSSW_envs/ntuplizer_CMSSW_13_0_13_noCustomMini.tar.gz .
tar -xzf ntuplizer_CMSSW_13_0_13_noCustomMini.tar.gz

mv ${fname}.txt CMSSW_13_0_13/src/iDMe/AODSkimmer
cd CMSSW_13_0_13/src/
=======
xrdcp root://cmseos.fnal.gov//store/group/lpcmetx/iDMe//compiled_CMSSW_envs/compiled_CMSSW_env_ntuplizer_Jan2025.tar.gz .
tar -xzf compiled_CMSSW_env_ntuplizer_Jan2025.tar.gz

mv ${fname}.txt CMSSW_10_6_26/src/iDMe/AODSkimmer
cd CMSSW_10_6_26/src/
>>>>>>> kyungmin/main
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
scram b ProjectRename
eval `scram runtime -sh`
cd iDMe/AODSkimmer
<<<<<<< HEAD
cmsRun ElectronNtuplizer_cfg.py flist=${fname}.txt data=${isData} signal=${isSignal} year=${year} numThreads=${nThreads}
=======
cmsRun scripts/ElectronNtuplizer_cfg.py flist=${fname}.txt data=${isData} signal=${isSignal} year=${year} numThreads=${nThreads}
>>>>>>> kyungmin/main
mv test_output.root ntuples_${fname}.root
xrdcp -f ntuples_${fname}.root root://cmseos.fnal.gov/${outPath}/ntuples_${fname}.root
echo "Copied ntuples_${fname}.root"
echo "Done"
