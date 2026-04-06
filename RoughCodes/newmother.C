#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
using namespace reco;

void MyModule::analyze(const edm::Event & iEvent, ...) {
   Handle<GenParticleCollection> genParticles;
   iEvent.getByLabel("genParticles", genParticles);
   for(size_t i = 0; i < genParticles->size(); ++ i) {
     const GenParticle & p = (*genParticles)[i];
     int id = p.pdgId();
     int st = p.status();  
     const Candidate * mom = p.mother();
     double pt = p.pt(), eta = p.eta(), phi = p.phi(), mass = p.mass();
     double vx = p.vx(), vy = p.vy(), vz = p.vz();
     int charge = p.charge();
     int n = p.numberOfDaughters();
     for(size_t j = 0; j < n; ++ j) {
       const Candidate * d = p.daughter( j );
       int dauId = d->pdgId();
       
     }
     
   }
}