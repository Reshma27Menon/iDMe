"""Compare every existing defineGoodVertices version on the same events.

Use a processor that executes the cut configuration (not bareProcessor).
These are independent definition comparisons, NOT cumulative selections.
No events are dropped. Each call overwrites isGood using all events.vtx,
then defineGoodVertices rebuilds good_vtx and nGoodVtx.

For vertex reconstruction efficiency, histogram numerators MUST require:
    ak.any(events.vtx.isMatched & events.vtx.isGood, axis=1)
(or the equivalent check on events.good_vtx), after applying any category
selection. Keep the generated denominator unchanged and avoid upstream
requirements on nGoodVtx. Ordinary event-count cutflow totals will stay flat.
Histograms using sel_vtx are not supported by this config alone: it does not
reselect that separate object after each version.

All thresholds and definitions come from analysisSubroutines.py on the
machine executing this config. This file does not change that module.
Known implementation details preserved intentionally:
- v10 and v11 currently have identical requirements.
- v11_RL computes a type mask but does not apply it, so it currently equals v11.
- eleDphi < 2 is defined but unused in the existing versions.
ELE_ID='dR' uses passID for both electrons; use 'basic' only for a deliberate
separate comparison of passIDBasic.
"""

import analysisSubroutines as routines

ELE_ID = "dR"

# The processor discovers any module attribute containing the word 'cut'.
# Keep only cut0, cut1, ... as discoverable names; helpers avoid that substring.

def _apply_version(events, version, name, description):
    routines.defineGoodVertices(events, version=version, ele_id=ELE_ID)
    return events, name, description, True

def cut0(events, info):
    return _apply_version(events, 'none', "cut0", 'Good vertex none: All vertices')

def cut1(events, info):
    return _apply_version(events, 'default', "cut1", 'Good vertex default:  IDcut')

def cut2(events, info):
    return _apply_version(events, 'v1', "cut2", 'Good vertex v1: IDcut & chi2')

def cut3(events, info):
    return _apply_version(events, 'v2', "cut3", 'Good vertex v2: IDcut & chi2 & mass_lo_refit')

def cut4(events, info):
    return _apply_version(events, 'v3', "cut4", 'Good vertex v3: IDcut & chi2 & mass_lo_refit & maxMiniIso')

def cut5(events, info):
    return _apply_version(events, 'v4', "cut5", 'Good vertex v4: IDcut & chi2 & mass_lo_refit & maxMiniIso & mindxy_refit')

def cut6(events, info):
    return _apply_version(events, 'v5', "cut6", 'Good vertex v5: IDcut & chi2 & mass_lo_refit & maxMiniIso & mindxy_refit & passConvVeto')

def cut7(events, info):
    return _apply_version(events, 'v6', "cut7", 'Good vertex v6: IDcut & chi2 & mass_lo_refit & maxMiniIso & mindxy_refit & passConvVeto & logdxydz_loose')

