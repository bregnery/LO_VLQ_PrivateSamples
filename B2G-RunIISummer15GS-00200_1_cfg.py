# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/B2G-RunIISummer15GS-00200-fragment.py --python_filename B2G-RunIISummer15GS-00200_1_cfg.py --eventcontent RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --fileout file:B2G-RunIISummer15GS-00200.root --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step GEN,SIM --magField 38T_PostLS1 --filein dbs:/TprimeTprime_M-1000_13TeV-madgraph/RunIIWinter15wmLHE-MCRUN2_71_V1-v1/LHE --no_exec --mc -n 100
import FWCore.ParameterSet.Config as cms



process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic50ns13TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring(
        '/store/mc/RunIIWinter15wmLHE/TprimeTprime_M-1000_13TeV-madgraph/LHE/MCRUN2_71_V1-v1/50000/0CF6F6D5-4E05-E511-B101-008CFA14F814.root', 
        '/store/mc/RunIIWinter15wmLHE/TprimeTprime_M-1000_13TeV-madgraph/LHE/MCRUN2_71_V1-v1/50000/127A06BD-A505-E511-BFC3-00259081ED06.root', 
        '/store/mc/RunIIWinter15wmLHE/TprimeTprime_M-1000_13TeV-madgraph/LHE/MCRUN2_71_V1-v1/50000/3681101F-4B05-E511-9E56-02163E013039.root', 
        '/store/mc/RunIIWinter15wmLHE/TprimeTprime_M-1000_13TeV-madgraph/LHE/MCRUN2_71_V1-v1/50000/46B91F61-4D05-E511-8D12-008CFA56D770.root', 
        '/store/mc/RunIIWinter15wmLHE/TprimeTprime_M-1000_13TeV-madgraph/LHE/MCRUN2_71_V1-v1/50000/50E1F260-4D05-E511-ADF6-008CFA197BBC.root', 
        '/store/mc/RunIIWinter15wmLHE/TprimeTprime_M-1000_13TeV-madgraph/LHE/MCRUN2_71_V1-v1/50000/6262CE60-4D05-E511-9A67-008CFA0A5844.root', 
        '/store/mc/RunIIWinter15wmLHE/TprimeTprime_M-1000_13TeV-madgraph/LHE/MCRUN2_71_V1-v1/50000/7C0E2213-4A05-E511-9BBC-008CFA1C64A0.root', 
        '/store/mc/RunIIWinter15wmLHE/TprimeTprime_M-1000_13TeV-madgraph/LHE/MCRUN2_71_V1-v1/50000/B40B3586-1E07-E511-B516-38EAA7A6DAA0.root', 
        '/store/mc/RunIIWinter15wmLHE/TprimeTprime_M-1000_13TeV-madgraph/LHE/MCRUN2_71_V1-v1/50000/D25ABE77-FF06-E511-93E3-3417EBE6FFFD.root'
    ),
    inputCommands = cms.untracked.vstring(
        'keep *', 
        'drop LHEXMLStringProduct_*_*_*'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/B2G-RunIISummer15GS-00200-fragment.py nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(1),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:B2G-RunIISummer15GS-00200.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_71_V1::All', '')

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
