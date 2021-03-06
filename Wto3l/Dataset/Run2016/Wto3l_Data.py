from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

#dataTreeDir     = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180806/SkimTree_Data80X_ZXCRSelection/"
#dataTreeDir     = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180806/SkimTree_Data80X_HIG-16-041-ZXCRSelection_v2/"
#dataTreeDir     = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180905/SkimTree_DarkPhoton_ZX_Run2016Data_m4l70/"
#dataTreeDir      = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180924/SkimTree_DarkPhoton_ZX_Run2016Data_m4l70/"
dataTreeDir     = "/raid/raid7/kshi/Zprime/20190827/SkimTree_Run2016_MMM_Data/"
inUFTier2       = False

# ____________________________________________________________________________________________________________________________________________ ||
Data_Run2016_cmpList = ComponentList(
        [
            #Component("Data_Run2016_DoubleEG",dataTreeDir+"DoubleEG.root","passedEvents",inUFTier2=inUFTier2),
            #Component("Data_Run2016_DoubleMuon",dataTreeDir+"DoubleMuon.root","passedEvents",inUFTier2=inUFTier2),
            #Component("Data_Run2016_MuonEG",dataTreeDir+"MuonEG.root","passedEvents",inUFTier2=inUFTier2),
            #Component("Data_Run2016_SingleElectron",dataTreeDir+"SingleElectron.root","passedEvents",inUFTier2=inUFTier2),
            #Component("Data_Run2016_SingleMuon",dataTreeDir+"SingleMuon.root","passedEvents",inUFTier2=inUFTier2),
            Component("Data_Run2016_totaldata",dataTreeDir+"total_Data.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
Data_Run2016 = Dataset(
        "Data_Run2016",
        Data_Run2016_cmpList,
        isMC = True,
        skipWeight = True,
        )
'''
bkgSamples = [
            Data_Run2016,
        ]
'''
