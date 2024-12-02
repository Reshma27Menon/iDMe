**Steps to create skimmed ntuples**

1. Choose a sample.  
   For example, I am interested in a 2022 WJets sample like:  
   `/WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM`

2. CRAB jobs submission  

   Inside `AODSkimmer`:  

   1. Set up the environment:  
      ```
      cd crab
      source setupAPI.sh
      cmsenv
      cd ..
      ```

   2. Submitting jobs:
  
      ```
      python crab/submit_multicrab_ElectronNtuplizer.py -c submit -y [year] -f [file list in json] -t [isData 0/1] -s [isSignal 0/1]
      ```
      Example:
       
      ```
      python3 crab/submit_multicrab_ElectronNtuplizer.py -c submit -y 2022 -f fileLists/background/MINIAOD/bkg_2022.json -t 0 -s 0 -n WJets12022
      ```

      On submitting, they will let you know the command to be used to check the status. It takes approx a day.  

      Once successful, check the output directory. You will (should!) see multiple root files.
  
3. Skimming the ntuples
  
      1. Make a json file with file lists and other information like location, number of files etc.
  
      From `python_analysis/configs/sample_configs` run `makeSignalConfigs.py`.
  
      Example on how to run `makeSignalConfigs.py`:
  
      `python3 makeSignalConfigs.py -m bkg -y 2022 -a aEM -p /store/group/lpcmetx/iDMe/Samples/Ntuples/background_WJets12022 -n WJets`
  
      This will create bkg_2022_WJets.json
  
      2. Fill out cross-section (xsec) in the json file
         First, make sure that the process in the json file (from the above step) is listed in the bkg_xsecs.json. If not add the process's xsec using CMS [xsdb](https://xsecdb-xsdb-official.app.cern.ch/xsdb/). Note that the xsec from xsdb should be multiplied by 1000 in the json (unit conversion). 

         Now, from `python_analysis/configs/sample_configs` run `getSignalXsec.py`.
         Example on how to run `getSignalXsec.py`:
         
         `python3 getSignalXsec.py bkg_2022_WJets.json bkg`

      3. Fill out `sumWgt` and `blacklist` in the json file:
     
         `python3 sumGenWgts.py bkg_2022_WJets.json 0`
     
         This would give `sumWgt` and `blacklist`.
     
         Note: There are chances that you might encounter errors like the .py file is unable to open or load the root files. In that case, try changing the redirector.
     
         Example (of an issue):
     
         In my case I had 60 root files and all of them were getting blacklisted.
     
         This is how I sorted the issue:
     
         1. I tried opening them using TBrowser in root and it worked. Also checked the `genWgt` branch. Everything looked good. This means the files are in good condition.
         2. I tried opening the files using uproot (and using the same redirector used in `sumGenWgts.py`). It failed. I changed to `cmseos` redirector and it worked well.

4. Submitting condor jobs

    In `python_analysis/condor/skimming_rdf` run `submit_condor_skim_rdf.py`
     
           `python3 submit_condor_skim_rdf.py -s [sample json file] -n [n_files_per] -c [n_cores] -m [MET lower bound cut] -j [nJet upper bound cut (if only requiring nJet >0, then put 0)`
     
           Example:
     
           `python3 submit_condor_skim_rdf.py -s ../../configs/sample_configs/bkg_2022_WJets.json -n 10 -c 4 -m 100 -j 0`
     
           The output will be stored in `/store/group/lpcmetx/iDMe/skimmed_ntuples/bkg`.

   Note: This process is not going to be easy, especially if you are a beginner. Jobs might succeed or might fail. This is a part of this process. You can check or track your jobs using these basic commands:

   `condor_q` -- tracks the running (R) jobs.

   
  
5. Once this is done, we come to the final step: Making json file for these skimmed ntuples. The skimmed ntuples will be used by the coffea analyzer.
  
         In my case, the following command was used (to be done inside `python_analysis/configs/sample_configs` directory):
  
         `python3 makeSignalConfigs.py -m bkg -y 2022 -a aEM -p /eos/uscms/store/group/lpcmetx/iDMe/skimmed_ntuples/bkg/bkg_2022_WJets_rdfSkim_MET130_nJetsG0 -n WJets -s 1 -r bkg_2022_WJets.json`
  
         This created a json file `skimmed_bkg_2022_WJets.json`.
  
         Now this json file will have: name, location, type, year, nFiles, sum_wgt, xsec, blacklist. Only num_events is not there. To get this, run:
  
         `python3 sumGenWgts.py skimmed_bkg_2022_WJets.json 0`
  
          This completes the skimming process.
  
         
         
            
         
  
      
  
      
