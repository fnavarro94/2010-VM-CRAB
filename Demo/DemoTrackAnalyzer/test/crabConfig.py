from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'tutorial_May2015_Data_analysis'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'DemoTrackanalyzer_cfg.py'
config.Data.inputDataset = '/SingleElectron/Run2011A-12Oct2013-v1/AOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1


config.Site.storageSite = 'T2_US_Nebraska'
config.section_("Debug")
config.Debug.extraJDL = [ '+DESIRED_Sites="T3_CH_Opportunistic_opendata"','+JOB_CMSSite="T3_CH_Opportunistic_opendata"']
