#!/bin/bash

source /cvmfs/cms.cern.ch/cmsset_default.sh

BASE=/uscms/home/sbrightt/nobackup/iDM/iDMe_analysis/CMSSW_10_6_26/src/iDMe/
HEAD=/uscms/home/sbrightt/nobackup/iDMe/compiled_CMSSW_envs/ntuplizer_CMSSW_10_6_26

cd $HEAD

if ! [ -r CMSSW_10_6_26/src ] ; then
    scram p CMSSW CMSSW_10_6_26
fi

cd CMSSW_10_6_26/src
eval `scram runtime -sh`
rm -rf *

mkdir iDMe
mkdir iDMe/iDMeSkimmer
mkdir iDMe/AODSkimmer
mkdir iDMe/CustomTools

cp -r $BASE/iDMeSkimmer/plugins iDMe/iDMeSkimmer/
cp -r $BASE/iDMeSkimmer/python iDMe/iDMeSkimmer/
cp -r $BASE/iDMeSkimmer/test iDMe/iDMeSkimmer/

cp -r $BASE/AODSkimmer/plugins iDMe/AODSkimmer/
cp -r $BASE/AODSkimmer/python iDMe/AODSkimmer/
cp -r $BASE/AODSkimmer/test iDMe/AODSkimmer/

cp -r $BASE/CustomTools/* iDMe/CustomTools/

cp $BASE/iDMeSkimmer/scripts/run_ntuplizer_cfg.py iDMe/iDMeSkimmer/
cp $BASE/AODSkimmer/scripts/run_ntuplizer_cfg.py iDMe/AODSkimmeer/

cp -r /uscms/home/sbrightt/nobackup/iDM/iDMe_analysis/CMSSW_10_6_26/src/RecoVertex .

scram b -j 8

cd $HEAD
tar -czf ntuplizer_CMSSW_10_6_26.tar.gz CMSSW_10_6_26/
xrdcp -f ntuplizer_CMSSW_10_6_26.tar.gz root://cmseos.fnal.gov//store/group/lpcmetx/iDMe//compiled_CMSSW_envs/
