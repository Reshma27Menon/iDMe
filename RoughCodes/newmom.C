#include "TFile.h"
#include "TTree.h"
//#include "TSystem.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include <vector>
#include <iostream>

void newmom()
{
    //gSystem->Load("libDataFormatsHepMCCandidate.so");
    TFile *f = TFile::Open("iDMe_Mchi-10p5_dMchi-1p0_mZDinput-30p0_ctau-0_1jet_icckw1_drjj0_xptj80_xqcut20_slc7_amd64_gcc11_CMSSW_13_0_13_tarball_22577496_MINIAOD_ctau-10.0_year-2022.root");
    
    TTree *t = (TTree*)f->Get("Events");
    
    
    edm::Wrapper<std::vector<reco::GenParticle>> *value = 0;
    //std::vector<reco::GenParticle> *value = 0;
    
    t->SetBranchAddress("recoGenParticles_prunedGenParticles__PAT.", &value);
    
    
    
    int nentries = t->GetEntries();
    for (int i=0; i<3; ++i){
        t->GetEntry(i);
        const std::vector<reco::GenParticle>& particles = *(value->product());
        std::cout << "Event " << i << " has " << particles.size() << " gen particles" << std::endl;
        
    }
    
    

    
    

    

}