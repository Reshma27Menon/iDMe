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
    return _apply_version(events, 'default', "cut1", 'Good vertex default: ID + opposite sign')

def cut2(events, info):
    return _apply_version(events, 'v1', "cut2", 'Good vertex v1: Existing good-vertex definition v1')

def cut3(events, info):
    return _apply_version(events, 'v2', "cut3", 'Good vertex v2: Existing good-vertex definition v2')

def cut4(events, info):
    return _apply_version(events, 'v3', "cut4", 'Good vertex v3: Existing good-vertex definition v3')

def cut5(events, info):
    return _apply_version(events, 'v4', "cut5", 'Good vertex v4: Existing good-vertex definition v4')

def cut6(events, info):
    return _apply_version(events, 'v5', "cut6", 'Good vertex v5: Existing good-vertex definition v5')

def cut7(events, info):
    return _apply_version(events, 'v6', "cut7", 'Good vertex v6: Existing good-vertex definition v6')

def cut8(events, info):
    return _apply_version(events, 'v7', "cut8", 'Good vertex v7: Existing good-vertex definition v7')

def cut9(events, info):
    return _apply_version(events, 'v8', "cut9", 'Good vertex v8: Existing good-vertex definition v8')

def cut10(events, info):
    return _apply_version(events, 'v9', "cut10", 'Good vertex v9: Existing good-vertex definition v9')

def cut11(events, info):
    return _apply_version(events, 'v10', "cut11", 'Good vertex v10: Existing good-vertex definition v10')

def cut12(events, info):
    return _apply_version(events, 'v11', "cut12", 'Good vertex v11: Existing good-vertex definition v11')

def cut13(events, info):
    return _apply_version(events, 'v11_LL', "cut13", 'Good vertex v11_LL: v11 with LL reconstructed vertex type')

def cut14(events, info):
    return _apply_version(events, 'v11_RR', "cut14", 'Good vertex v11_RR: v11 with RR reconstructed vertex type')

def cut15(events, info):
    return _apply_version(events, 'v11_RL', "cut15", 'Good vertex v11_RL: Existing v11_RL implementation; type mask currently unused')

def cut16(events, info):
    return _apply_version(events, 'v12', "cut16", 'Good vertex v12: Existing good-vertex definition v12')

def cut17(events, info):
    return _apply_version(events, 'v13', "cut17", 'Good vertex v13: Existing good-vertex definition v13')

def cut18(events, info):
    return _apply_version(events, 'v14', "cut18", 'Good vertex v14: Existing good-vertex definition v14')

def cut19(events, info):
    return _apply_version(events, 'v15', "cut19", 'Good vertex v15: Existing good-vertex definition v15')

def cut20(events, info):
    return _apply_version(events, 'v40', "cut20", 'Good vertex v40: Existing v40 scale-factor-study definition')
