import FWCore.ParameterSet.Config as cms
process = cms.Process("Demo")
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring('root://eospublic.cern.ch//eos/opendata/cms/Run2010B/BTau/AOD/Apr21ReReco-v1/0000/044C8097-D571-E011-98D9-00E08178C025.root'))
process.demo = cms.EDAnalyzer("DemoTrackAnalyzer", tracks = cms.untracked.InputTag("generalTracks"))
process.p = cms.Path(process.demo)
