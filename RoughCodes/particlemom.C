#include "TFile.h"
#include "TTree.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include <vector>
#include <iostream>

void particlemom(){
    TFile *f = TFile::Open("iDMe_Mchi-10p5_dMchi-1p0_mZDinput-30p0_ctau-0_1jet_icckw1_drjj0_xptj80_xqcut20_slc7_amd64_gcc11_CMSSW_13_0_13_tarball_22577496_MINIAOD_ctau-10.0_year-2022.root");

    TTree *tree = (TTree*)f->Get("Events");

    //Did: edmDumpEventContent iDMe_Mchi-10p5_dMchi-1p0_mZDinput-30p0_ctau-0_1jet_icckw1_drjj0_xptj80_xqcut20_slc7_amd64_gcc11_CMSSW_13_0_13_tarball_22577496_MINIAOD_ctau-10.0_year-2022.root
    // and I got:  vector<reco::GenParticle>             "prunedGenParticles"        ""                "PAT"   

    edm::Wrapper<vector<reco::GenParticle>> *value = 0;

    tree->SetBranchAddress("recoGenParticles_prunedGenParticles__PAT.", &value);
    //const std::vector<reco::GenParticle> & genparticles = *(value->product());
    int motherID = -999;

    for (int i=0; i<3; ++i){
        tree->GetEntry(i);
        const std::vector<reco::GenParticle> & genparticles = *(value->product());
        std::cout<<"Event "<<i<<" has "<<genparticles.size()<<" gen particles"<<std::endl;
        int count =0;
        for (int j=0; j<genparticles.size(); ++j){
            const reco::GenParticle & particle =  genparticles[j];  //Read about references and pointers
            int pdg = particle.pdgId();
            int st = particle.status();
            // if ((pdg ==11) & (st == 1)){
            //     count = count+1 ;  }  
            int nmom = particle.numberOfMothers();
            if (nmom >0){
                motherID = particle.mother(0)->pdgId();}
        
            
        }
    //std::cout<<"Event "<<i<<" has "<<count<<" electrons"<<std::endl;
        
            



        
        
    }
        
    
}

//The ERROR:
//Error in <TRint::HandleTermInput()>: edm::Exception caught: An exception of category 'InvalidReference' occurred.
// Exception Message:
// BadRefCore RefCore: A request to resolve a reference to a product of type 'std::vector<reco::GenParticle>' with ProductID '4:1269' cannot be satisfied.
// The reference has neither a valid product pointer nor an EDProductGetter.
// The calling code must be modified to establish a functioning EDProducterGetter
// for the context in which this call is mode



    
