from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight
import os

bkgSkimTreeDir      = "/cmsuf/data/store/user/t2/users/klo/Zprime/EXO-18-008/80X_MCProd_DarkZNTuple/"
bkgSkimTreeDir2     = bkgSkimTreeDir
bkgTreeDir          = "/cmsuf/data/store/user/t2/users/klo/Zprime/EXO-18-008/HZZNTuple_Run2016/"
dataTreeDir         = bkgSkimTreeDir
inUFTier2           = True
sumWeightHist       = "Ana/sumWeights"
saveSumWeightTxt    = True

# ____________________________________________________________________________________________________________________________________________ ||
# qqZZ
qqZZ_cmpList = ComponentList(
        [ 
            Component("qqZZTo4L",bkgSkimTreeDir+"ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

qqZZTo4L = Dataset(
        "qqZZTo4L",
        qqZZ_cmpList,
        isMC                = True,
        xs                  = 1.256,
        )
handleSumWeight(
        qqZZTo4L,
        system,
        bkgTreeDir+"ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2.root.txt",
        #bkgSkimTreeDir+"ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2.root.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo4mu
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo4mu",bkgSkimTreeDir+"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8_RunIISummer16MiniAODv2.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo4mu = Dataset(
        "ggZZTo4mu",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.001586,
        )
handleSumWeight(
        ggZZTo4mu,
        system,
        bkgTreeDir+"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8_RunIISummer16MiniAODv2.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8_RunIISummer16MiniAODv2.txt",
        #bkgSkimTreeDir+"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8_RunIISummer16MiniAODv2.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
bkgSamples = [
        qqZZTo4L,
        ggZZTo4mu,
        ]
