#!/bin/bash

fname=$1
year=$2
nThreads=$3
isData=$4
isSignal=$5
outDirName=$6
topDirName=$7

xrdcp root://cmseos.fnal.gov//store/group/lpcmetx/iDMe//compiled_CMSSW_envs/ntuplizer_CMSSW_10_6_26.tar.gz .
tar -xzf ntuplizer_CMSSW_10_6_26.tar.gz

mv ${fname}.txt CMSSW_10_6_26/src/iDMe/AODSkimmer
cd CMSSW_10_6_26/src/
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
scram b ProjectRename
eval `scram runtime -sh`
cd iDMe/AODSkimmer
cmsRun run_ElectronNtuplizer_cfg.py flist=${fname}.txt data=${isData} signal=${isSignal} year=${year} numThreads=${nThreads}
mv test_output.root ntuples_${fname}.root

xrdfs root://cmseos.fnal.gov mkdir -p /store/group/lpcmetx/iDMe//Samples/Ntuples/${topDirName}
xrdfs root://cmseos.fnal.gov mkdir -p /store/group/lpcmetx/iDMe//Samples/Ntuples/${topDirName}/${year}
xrdfs root://cmseos.fnal.gov mkdir -p /store/group/lpcmetx/iDMe//Samples/Ntuples/${topDirName}/${year}/${outDirName}/

xrdcp -f ntuples_${fname}.root root://cmseos.fnal.gov//store/group/lpcmetx/iDMe//Samples/Ntuples/${topDirName}/${year}/${outDirName}/ntuples_${fname}.root
echo "Copied ntuples_${fname}.root"
echo "Done"