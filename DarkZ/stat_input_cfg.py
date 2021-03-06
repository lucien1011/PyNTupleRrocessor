from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc

#from DarkZ.Dataset.Run2016.SkimTree_SMHiggs import * 
from DarkZ.Dataset.Run2016.SkimTree_DarkPhoton_m4l70 import * 
#from DarkZ.Dataset.Run2017.SignalMC import * 

from DarkZ.Sequence.RecoSequence import * 

from DarkZ.StatTools.MassWindow import MassWindow,MultiMassWindow
from DarkZ.StatTools.YieldProducer import YieldProducer
from DarkZ.StatTools.Syst import Syst
from DarkZ.Producer.VariableProducer import VariableProducer

from NanoAOD.Weighter.XSWeighter import XSWeighter # Stealing module from NanoAOD framework

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

#out_path = "MCDistributions/MC_BaselineSelection_v1/2018-07-09/"
#out_path = "StatInput/DarkPhotonSelection_v1/2018-08-20/"
#out_path = "StatInput/DarkPhotonSelection_ATLAS-BrHToZZd100_v1/2018-08-20/"
#out_path = "StatInput/DarkPhotonSelection_m4l118To130/2018-08-31/"
#out_path = "StatInput/DarkPhotonSelection_m4l118To130_Nominal/2018-09-21/"
#out_path = "StatInput/DarkPhotonSelection_m4l118To130_Nominal/2018-10-24_DarkPhotonSR-Unblinding/"
#out_path = "StatInput/DarkPhotonSelection_m4l118To130_Nominal/2018-10-25_DarkPhotonSR-Unblinding/"
out_path = "StatInput/DarkPhotonSelection_m4l118To130_Nominal/2018-11-09_DarkPhotonSR-150fb-Unblinding/"
#out_path = "StatInput/DarkPhotonSelection_m4l118To130_UniformIso/2018-09-21/"
#out_path = "StatInput/DarkPhotonSelection_m4l105To140/2018-08-31/"

mergeSampleDict = {
        "ggH":  ["ggH"],
        "VBF":  ["VBF"],
        "WH":   ["WHPlus","WHminus",],
        "ZH":   ["ZH",],
        "qqZZ": ["qqZZTo4L",],
        "ggZZ": [
            "ggZZTo2e2mu",
            "ggZZTo2e2tau",
            "ggZZTo2mu2tau",
            "ggZZTo4e",
            "ggZZTo4mu",
            "ggZZTo4tau",
            ],
        "ZPlusX": ["ZPlusX"],
        }

mass_window_list = [

        MultiMassWindow(
            "MZd4",
            [
                MassWindow("4mu",4,0.02,LambdaFunc('x: x.mass4mu[0] > 0. and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')),
                MassWindow("2e2mu",4,0.02,LambdaFunc('x: x.mass2e2mu[0] > 0. and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')),
                MassWindow("2mu2e",4,0.05,LambdaFunc('x: x.mass2e2mu[0] > 0. and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')),
                MassWindow("4e",4,0.05,LambdaFunc('x: x.mass4e[0] > 0. and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')),
            ]
        ),

        MultiMassWindow(
            "MZd7",
            [
                MassWindow("4mu",7,0.02,LambdaFunc('x: x.mass4mu[0] > 0. and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')),
                MassWindow("2e2mu",7,0.02,LambdaFunc('x: x.mass2e2mu[0] > 0. and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')),
                MassWindow("2mu2e",7,0.05,LambdaFunc('x: x.mass2e2mu[0] > 0. and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')),
                MassWindow("4e",7,0.05,LambdaFunc('x: x.mass4e[0] > 0. and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')),
            ]
        ),

        MultiMassWindow(
            "MZd10",
            [
                MassWindow("4mu",10,0.02,LambdaFunc('x: x.mass4mu[0] > 0. and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')),
                MassWindow("2e2mu",10,0.02,LambdaFunc('x: x.mass2e2mu[0] > 0. and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')),
                MassWindow("2mu2e",10,0.05,LambdaFunc('x: x.mass2e2mu[0] > 0. and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')),
                MassWindow("4e",10,0.05,LambdaFunc('x: x.mass4e[0] > 0. and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')),
            ]
        ),
        
        MultiMassWindow(
            "MZd15",
            [
                MassWindow("4mu",15,0.02,LambdaFunc('x: x.mass4mu[0] > 0. and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')),
                MassWindow("2e2mu",15,0.02,LambdaFunc('x: x.mass2e2mu[0] > 0. and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')),
                MassWindow("2mu2e",15,0.05,LambdaFunc('x: x.mass2e2mu[0] > 0. and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')),
                MassWindow("4e",15,0.05,LambdaFunc('x: x.mass4e[0] > 0. and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')),
            ]
        ),

        MultiMassWindow(
            "MZd20",
            [
                MassWindow("4mu",20,0.02,LambdaFunc('x: x.mass4mu[0] > 0. and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')),
                MassWindow("2e2mu",20,0.02,LambdaFunc('x: x.mass2e2mu[0] > 0. and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')),
                MassWindow("2mu2e",20,0.05,LambdaFunc('x: x.mass2e2mu[0] > 0. and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')),
                MassWindow("4e",20,0.05,LambdaFunc('x: x.mass4e[0] > 0. and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')),
            ]
        ),

        MultiMassWindow(
            "MZd25",
            [
                MassWindow("4mu",25,0.02,LambdaFunc('x: x.mass4mu[0] > 0. and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')),
                MassWindow("2e2mu",25,0.02,LambdaFunc('x: x.mass2e2mu[0] > 0. and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')),
                MassWindow("2mu2e",25,0.05,LambdaFunc('x: x.mass2e2mu[0] > 0. and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')),
                MassWindow("4e",25,0.05,LambdaFunc('x: x.mass4e[0] > 0. and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')),
            ]
        ),

        MultiMassWindow(
            "MZd30",
            [
                MassWindow("4mu",30,0.02,LambdaFunc('x: x.mass4mu[0] > 0. and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')),
                MassWindow("2e2mu",30,0.02,LambdaFunc('x: x.mass2e2mu[0] > 0. and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')),
                MassWindow("2mu2e",30,0.05,LambdaFunc('x: x.mass2e2mu[0] > 0. and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')),
                MassWindow("4e",30,0.05,LambdaFunc('x: x.mass4e[0] > 0. and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')),
            ]
        ),

        ]

syst_list = [
        Syst("FRUniIso",LambdaFunc("x: x.weight_FRUniIso_Up")),
        ]


nCores                  = 5
outputDir               = "/raid/raid7/lucien/Higgs/DarkZ/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + sigSamples + [data2016]
justEndSequence         = False
skipGitDetail           = True

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 150.0
    for component in dataset.componentList:
        component.maxEvents = nEvents

sequence                = darkphoton_signal_sequence
#variableProducer        = VariableProducer("VariableProducer")
yieldProducer           = YieldProducer("YieldProducer",mass_window_list,systList=syst_list)

#sequence.add(variableProducer)
sequence.add(yieldProducer)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "StatInput.root"

#endSequence = EndSequence(skipHadd=justEndSequence)
endSequence = EndSequence(skipHadd=False)
