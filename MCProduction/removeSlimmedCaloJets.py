def customise(process):
    # Remove slimmedCaloJets from outputCommands of all output modules
    for output in process.outputModules.values():
        if hasattr(output, 'outputCommands'):
            output.outputCommands = cms.untracked.vstring(
                line for line in output.outputCommands
                if 'slimmedCaloJets' not in line
            )
    # If the module itself was scheduled, remove it
    if hasattr(process, 'slimmedCaloJets'):
        delattr(process, 'slimmedCaloJets')
    return process

