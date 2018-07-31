from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'jobName_crab'
config.General.workArea = 'Example_project'
config.General.transferOutputs = True
config.General.transferLogs = False
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'DemoTrackanalyzer_cfg.py' 
config.JobType.outputFiles = ['outfile.root']
config.Data.inputDataset = '/EG/Run2010A-Apr21ReReco-v1/AOD'
#config.Data.userInputFiles = ['root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Photon/AOD/Apr21ReReco-v1/0000/0003D1EF-B071-E011-BA0A-78E7D1651098.root', 'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Photon/AOD/Apr21ReReco-v1/0000/001CE57A-F470-E011-8208-001CC4A934D8.root']
config.Data.publication = False
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob =  500

config.Site.storageSite = 'T2_US_Nebraska'  # you might need to change this to a site you have acces too
config.section_("Debug")

