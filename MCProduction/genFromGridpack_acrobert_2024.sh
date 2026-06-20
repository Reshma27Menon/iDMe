#! /bin/bash

## This script is used to produce MINI-AOD files from a gridpack for 2024 samples.
## NOT YET TESTED
## Based on the PdmV outline provided on mattermost

export BASEDIR=`pwd`
#export SCRAM_ARCH=el9_amd64_gcc11 
#CMSSW=CMSSW_15_0_2 # or CMSSW_14_0_21?
# need earlier cmssw to use el8 gridpack
export SCRAM_ARCH=el9_amd64_gcc11
CMSSW=CMSSW_13_0_13

GP_f=$1
nevent=$2
ctau=$3
nthreads=$4
year=2024

conditions=140X_mcRun3_2024_realistic_v26

if [ "$#" -ne 4 ]; then
    echo "Wrong number of arguments!"
    echo "Usage: ./genFromGridpack_2023.sh gridpack nevents ctau nThreads"
    exit 1
fi

echo "Generating signal MC for gridpack ${GP_f}"
echo "Lifetime set to ${ctau} mm"

echo "Base Dir: ${BASEDIR}"
GRIDPACKDIR=${BASEDIR}
LHEDIR=${BASEDIR}/lhes


[ -d ${LHEDIR} ] || mkdir ${LHEDIR}

HADRONIZER="iDMe_pythiaGenFragment_ctau-100.py"

namebase=${GP_f/.tar.xz/}
namebase=$(basename ${GP_f/.tar.xz/})


export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh


if ! [ -r ${CMSSW}/src ] ; then
  scram p CMSSW ${CMSSW}
fi

cd ${CMSSW}/src
eval `scram runtime -sh`
scram b -j ${nthreads}
tar xaf ${GRIDPACKDIR}/${GP_f}
sed -i 's/exit 0//g' runcmsgrid.sh
ls -lrth

RANDOMSEED=`od -vAn -N4 -tu4 < /dev/urandom`
#Sometimes the RANDOMSEED is too long for madgraph
RANDOMSEED=`echo $RANDOMSEED | rev | cut -c 3- | rev`

#Running the LHE step
echo "0.) LHE Step"
sh runcmsgrid.sh ${nevent} ${RANDOMSEED} ${nthreads}
namebase=${namebase}_$RANDOMSEED
cp cmsgrid_final.lhe ${LHEDIR}/${namebase}.lhe
echo "${LHEDIR}/${namebase}.lhe" 
rm -rf ${BASEDIR}/${CMSSW}/src/*

cd ${BASEDIR}

# now we have lhes, so revert to correct cmssw for 2024 chain
export SCRAM_ARCH=el9_amd64_gcc11 
CMSSW=CMSSW_15_0_2 # or CMSSW_14_0_21?

if ! [ -r ${CMSSW}/src ] ; then
  scram p CMSSW ${CMSSW}
fi

cd ${CMSSW}/src
mkdir -p Configuration/GenProduction/python/
cp "${BASEDIR}/${HADRONIZER}" Configuration/GenProduction/python/
eval `scram runtime -sh`
scram b -j ${nthreads}

# Running GEN  Step
echo "########################################################################################"
echo "########################################################################################"
echo "1.) GEN-SIM Step" 
genfragment=${namebase}_GEN_cfg_ctau-${ctau}.py
echo "Running in directory: $(pwd)"

echo "genfragment:" ${namebase}_GEN_cfg_ctau-${ctau}.py
echo "Input LHE file:" ${LHEDIR}/${namebase}.lhe 

cmsDriver.py Configuration/GenProduction/python/${HADRONIZER}  \
    --filein file:${LHEDIR}/${namebase}.lhe \
    --fileout file:${namebase}_GEN_ctau-${ctau}_year-${year}.root \
    --mc --eventcontent RAWSIM,LHE --datatier GEN-SIM,LHE \
    --step GEN,SIM --geometry DB:Extended \
    --conditions ${conditions} --beamspot DBrealistic \
    --era Run3_2024 --nThreads $nthreads \
    --customise Configuration/DataProcessing/Utils.addMonitoring \
    --python_filename ${genfragment} --no_exec -n ${nevent} || exit $?;

#Make each file unique to make later publication possible
linenumber=`grep -n 'process.source' ${genfragment} | awk '{print $1}'`
linenumber=${linenumber%:*}
total_linenumber=`cat ${genfragment} | wc -l`
bottom_linenumber=$((total_linenumber - $linenumber ))
tail -n $bottom_linenumber ${genfragment} > tail.py
head -n $linenumber ${genfragment} > head.py
echo "    firstRun = cms.untracked.uint32(1)," >> head.py
echo "    firstLuminosityBlock = cms.untracked.uint32($RANDOMSEED)," >> head.py
cat tail.py >> head.py
mv head.py ${genfragment}
rm -rf tail.py

cmsRun ${genfragment}


echo "########################################################################################"
echo "3.) DRPremix Step"
set -e

genfragment_premix=${namebase}_DRPremix_cfg_ctau-${ctau}.py
genfragment_reco=${namebase}_RECO_cfg_ctau-${ctau}.py

echo "Current working directory: $(pwd)"

#PREMIXRAW step:
#--pileup_input filelist:${BASEDIR}/premix_files_prefixed.txt \
cmsDriver.py  \
   --filein file:${namebase}_GEN_ctau-${ctau}_year-${year}.root \
   --fileout file:${namebase}_Premix_ctau-${ctau}_year-${year}.root \
   --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW \
   --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:2024v14 --procModifiers premix_stage2 --datamix PreMix \
   --geometry DB:Extended \
   --pileup_input "dbs:/Neutrino_E-10_gun/RunIIISummer24PrePremix-Premixlib2024_140X_mcRun3_2024_realistic_v26-v1/PREMIX" \
   --conditions ${conditions} \
   --era Run3_2024 --nThreads $nthreads \
   --customise Configuration/DataProcessing/Utils.addMonitoring \
   --python_filename ${genfragment_premix} --no_exec -n ${nevent} || exit $?;

cmsRun ${genfragment_premix}

#RECO step:

cmsDriver.py  \
   --filein file:${namebase}_Premix_ctau-${ctau}_year-${year}.root \
   --fileout file:${namebase}_PremixRECO_ctau-${ctau}_year-${year}.root \
   --mc --eventcontent AODSIM --datatier AODSIM \
   --step RAW2DIGI,L1Reco,RECO,RECOSIM \
   --geometry DB:Extended \
   --conditions ${conditions} \
   --era Run3_2024 --nThreads $nthreads \
   --customise Configuration/DataProcessing/Utils.addMonitoring \
   --python_filename ${genfragment_reco} --no_exec -n ${nevent} || exit $?;

cmsRun ${genfragment_reco}


echo "SUCCESS DRPREMIX!"

# Doing MINIAOD Step
echo "########################################################################################"
echo "6.) MINIAOD Step"
genfragment=${namebase}_MINIAOD_cfg_ctau-${ctau}.py

cmsDriver.py \
    --filein file:${namebase}_PremixRECO_ctau-${ctau}_year-${year}.root \
    --fileout file:${namebase}_MINIAOD_ctau-${ctau}_year-${year}.root \
    --mc --eventcontent MINIAODSIM --datatier MINIAODSIM \
    --step PAT --geometry DB:Extended \
    --conditions 150X_mcRun3_2024_realistic_v2 \
    --era Run3_2024 \
    --nThreads $nthreads \
    --customise Configuration/DataProcessing/Utils.addMonitoring \
    --python_filename ${genfragment} --no_exec --runUnscheduled -n ${nevent} || exit $?;

#echo "process.options = cms.untracked.PSet(SkipEvent = cms.untracked.vstring('ProductNotFound'))" >> ${genfragment}
cmsRun ${genfragment}

remoteDIR="/store/group/lpcmetx/iDMe/Samples/signal/${year}"
xrdcp -vf ${namebase}_MINIAOD_ctau-${ctau}_year-${year}.root root://cmseos.fnal.gov/$remoteDIR/MINIAOD/${namebase}_MINIAOD_ctau-${ctau}_year-${year}.root

echo "Final output ROOT file:" ${namebase}_MINIAOD_ctau-${ctau}_year-${year}.root 
echo "The output MINIAOD file: root://cmseos.fnal.gov/$remoteDIR/MINIAOD/${namebase}_MINIAOD_ctau-${ctau}_year-${year}.root"
echo "DONE!"

