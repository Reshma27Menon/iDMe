#!/bin/bash


base=$1
nevent=$2
ctau=$3
nthreads=$4
year=2022

if [ "$#" -ne 4 ]; then
    echo "Usage: ./partII.sh base ctau nevents nThreads"
    exit 1
fi

export SCRAM_ARCH=el8_amd64_gcc10
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh

namebase=${base%%_Premix*}
echo "namebase: $namebase"

NEWDIR=${BASEDIR}/CMSSW_13_0_13/src

if ! [ -r CMSSW_13_0_13/src ] ; then
    scram p CMSSW_13_0_13
fi

cd CMSSW_13_0_13/src
eval `scram runtime -sh`
scram b -j $nthreads


# Doing MINIAOD Step
echo "########################################################################################"
echo "########################################################################################"
echo "6.) MINIAOD Step"
genfragment=${namebase}_MINIAOD_cfg_ctau-${ctau}.py

# echo cmsDriver.py --filein file:${namebase}_PremixRECO_ctau-${ctau}_year-${year}.root --fileout file:${namebase}_MINIAOD_ctau-${ctau}_year-${year}.root  --mc --eventcontent MINIAODSIM --datatier MINIAODSIM --step PAT --geometry DB:Extended --conditions 130X_mcRun3_2022_realistic_v5 --era Run3,run3_miniAOD_12X --nThreads 4 --customise Configuration/DataProcessing/Utils.addMonitoring --python_filename ${genfragment} --no_exec --runUnscheduled -n 10

#--customise_commands "process.MINIAODSIMoutput.outputCommands = cms.untracked.vstring([line for line in process.MINIAODSIMoutput.outputCommands if 'slimmedCaloJets' not in line and 'oniaPhotonCandidates' not in line and 'offlineSlimmedPrimaryVerticesWithBS' not in line and 'primaryVertexWithBSAssociation' not in line and 'slimmedHcalRecHits' not in line])" \


cmsDriver.py \
    --filein file:${namebase}_PremixRECO_ctau-${ctau}_year-${year}.root \
    --fileout file:${namebase}_MINIAOD_ctau-${ctau}_year-${year}.root \
    --mc --eventcontent MINIAODSIM --datatier MINIAODSIM \
    --step PAT --geometry DB:Extended \
    --conditions 130X_mcRun3_2022_realistic_v5 \
    --era Run3,run3_miniAOD_12X \
    --nThreads $nthreads \
    --customise Configuration/DataProcessing/Utils.addMonitoring \
    --python_filename ${genfragment} --no_exec --runUnscheduled -n ${nevent} || exit $?;

#echo "process.options = cms.untracked.PSet(SkipEvent = cms.untracked.vstring('ProductNotFound'))" >> ${genfragment}
cmsRun -p ${genfragment}


#echo "LIST OF OUTPUT FILES:"
#ls -ltr *.root

#Path needs to be fixed
remoteDIR="/store/group/lpcmetx/iDMe//Samples/signal/2022"
xrdcp -vf ${namebase}_MINIAOD_ctau-${ctau}_year-${year}.root root://cmseos.fnal.gov/$remoteDIR/MINIAOD/${namebase}_MINIAOD_ctau-${ctau}_year-${year}.root

echo "Final output ROOT file:" ${namebase}_MINIAOD_ctau-${ctau}_year-${year}.root 
#echo "The output MINIAOD file: root://cmseos.fnal.gov/$remoteDIR/MINIAOD/${namebase}_MINIAOD_ctau-${ctau}_year-${year}.root"
#echo "DONE!"






































