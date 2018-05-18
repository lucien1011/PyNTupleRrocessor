# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from DataMC.NanoAOD.Run2016 import * 

from RPV.Producer.PhysObjProducer import PhysObjProducer,JetProducer 
from RPV.Producer.TreeProducer import TreeProducer
from RPV.Producer.AnalysisProducer import AnalysisProducer 
from RPV.Skimmer.EventSkimmer import EventSkimmer

nCores = 4 
outputDir = "/raid/raid7/lucien/SUSY/RPV/SkimTree/StopToBLep/2018-05-18/BkgMC_BaselineSelection_v1/"
nEvents = -1
disableProgressBar = True
justEndSequence = False 
componentList = allMCSamples 
for dataset in componentList:
    for component in dataset.componentList:
        component.maxEvents = nEvents

mediumMuonProducer      = PhysObjProducer("MediumMuonProducer","Muon","MediumMuons","Moriond17MediumMuon")
mediumElectronProducer  = PhysObjProducer("MediumElectronProducer","Electron","MediumElectrons","Moriond17MediumElectron")
jetProducer             = JetProducer("JetProducer","Jet",["MediumMuons","MediumElectrons"],"LooseJets","Moriond17LooseJet",0.4)
eventSkimmer            = EventSkimmer("StopToBLepSkim")
treeProducer            = TreeProducer("TreeProducer")
anaProducer             = AnalysisProducer("AnaProducer")

sequence = Sequence()
sequence.add(mediumMuonProducer)
sequence.add(mediumElectronProducer)
sequence.add(jetProducer)
sequence.add(anaProducer)
sequence.add(eventSkimmer)
sequence.add(treeProducer)

endSequence = EndSequence()

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "SkimTree.root"