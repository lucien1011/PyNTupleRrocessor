from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Core.Utils.mkdir_p import mkdir_p,copyFile

from HToZdZd.Dataset.Run2016.SkimTree_DarkPhoton_m4l70 import * 
#from HToZdZd.Dataset.Run2016.SkimTree_DarkSUSY_m4l70 import * 
from HToZdZd.Dataset.Run2017.SkimTree_HToZdZd_m4l70 import * 
from HToZdZd.Sequence.RecoSequence import * 

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from HToZdZd.Config.MergeSampleDict import *

nBinsMassRatio = 65
mZ1PlotRange = [nBinsMassRatio,0.,65.]
mZ2PlotRange = [nBinsMassRatio,0.,65.]
h4lPlotRange = [60,115.,135.]
#h4lPlotRange = [70,60.,200.]
#h4lPlotRange = [140,60.,200.]

#out_path                = "DarkPhotonSR/DataMCDistributions/2019-02-12_NoRatioCut_TEST4/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2019-02-15_MC_RatioCut0p05/" # Lucien's new dir
out_path                = "DarkPhotonSR/DataMCDistributions/20190228_MassRatioCuts_oddmasses/"
lumi                    = 35.9
nCores                  = 5
#outputDir               = "/raid/raid7/lucien/Higgs/HToZdZd/"+out_path
outputDir               = "/raid/raid7/rosedj1/Higgs/HToZdZd/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + [
                                #HToZdZd_MZD4,
                                HToZdZd_MZD5,
                                #HToZdZd_MZD6,
                                HToZdZd_MZD7,
                                #HToZdZd_MZD8,
                                HToZdZd_MZD9,
                                #HToZdZd_MZD10,
                                HToZdZd_MZD15, 
                                #HToZdZd_MZD20,
                                HToZdZd_MZD25,
                                #HToZdZd_MZD30,
                                HToZdZd_MZD35,
                                #HToZdZd_MZD40,
                                HToZdZd_MZD45,
                                #HToZdZd_MZD50,
                                HToZdZd_MZD55,
                                #HToZdZd_MZD60,
                                ]
justEndSequence         = False
phpFile                 = "index.php"
# Lucien's mass ratio cut 
#eventSelection          = LambdaFunc("x: (x.massZ1[0]-x.massZ2[0])/(x.massZ1[0]+x.massZ2[0]) < 0.05")  
eventSelection          = LambdaFunc("x: True")  


muon_plots = [
        ]

general_plots = [
        Plot("Z1_mass",     ["TH1D","Z1_mass","",]+mZ1PlotRange,  LambdaFunc('x: x.massZ1[0]'),       ),
        Plot("Z2_mass",     ["TH1D","Z2_mass","",]+mZ2PlotRange,   LambdaFunc('x: x.massZ2[0]'),       ),
        Plot("Z1_4e_mass",     ["TH1D","Z1_4e_mass","",]+mZ1PlotRange,  LambdaFunc('x: x.massZ1[0]'), selFunc=LambdaFunc('x: x.mass4e[0] > 0')      ),
        Plot("Z2_4e_mass",     ["TH1D","Z2_4e_mass","",]+mZ2PlotRange,   LambdaFunc('x: x.massZ2[0]'), selFunc=LambdaFunc('x: x.mass4e[0] > 0')     ),
        Plot("Z1_4mu_mass",     ["TH1D","Z1_4mu_mass","",]+mZ1PlotRange,  LambdaFunc('x: x.massZ1[0]'), selFunc=LambdaFunc('x: x.mass4mu[0] > 0')      ),
        Plot("Z2_4mu_mass",     ["TH1D","Z2_4mu_mass","",]+mZ2PlotRange,   LambdaFunc('x: x.massZ2[0]'), selFunc=LambdaFunc('x: x.mass4mu[0] > 0')     ),
        Plot("Z1_2e2mu_mass",     ["TH1D","Z1_2e2mu_mass","",]+mZ1PlotRange,   LambdaFunc('x: x.massZ1[0]'), selFunc=LambdaFunc('x: abs(x.idL1[0]) == 11 and abs(x.idL2[0]) == 11 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')     ),
        Plot("Z1_2mu2e_mass",     ["TH1D","Z1_2mu2e_mass","",]+mZ1PlotRange,   LambdaFunc('x: x.massZ1[0]'), selFunc=LambdaFunc('x: abs(x.idL1[0]) == 13 and abs(x.idL2[0]) == 13 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')     ),
        Plot("Z2_2e2mu_mass",     ["TH1D","Z2_2e2mu_mass","",]+mZ2PlotRange,   LambdaFunc('x: x.massZ2[0]'), selFunc=LambdaFunc('x: abs(x.idL1[0]) == 11 and abs(x.idL2[0]) == 11 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')     ),
        Plot("Z2_2mu2e_mass",     ["TH1D","Z2_2mu2e_mass","",]+mZ2PlotRange,   LambdaFunc('x: x.massZ2[0]'), selFunc=LambdaFunc('x: abs(x.idL1[0]) == 13 and abs(x.idL2[0]) == 13 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')     ),
              
        Plot("h4L_mass",    ["TH1D","h4L_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass4l[0]'),       ),
        Plot("h4e_mass",    ["TH1D","h4e_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass4e[0]'), selFunc=LambdaFunc('x: x.mass4e[0] > 0 and x.mass4mu[0] < 0 and x.mass2e2mu[0] < 0')       ),
        Plot("h4mu_mass",   ["TH1D","h4mu_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass4mu[0]'), selFunc=LambdaFunc('x: x.mass4mu[0] > 0 and x.mass4e[0] < 0 and x.mass2e2mu[0] < 0')       ),
        Plot("h2e2mu_mass", ["TH1D","h2e2mu_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass2e2mu[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and x.mass4mu[0] < 0 and x.mass4e[0] < 0 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')       ),
        Plot("h2mu2e_mass", ["TH1D","h2mu2e_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass2e2mu[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and x.mass4mu[0] < 0 and x.mass4e[0] < 0 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')       ),
        Plot("h4L_Pt",      ["TH1D","h4L_Pt","",40,0.,200.],     LambdaFunc('x: x.pT4l[0]'),         ),
        
        Plot("mass_ratio",["TH1D","mass_ratio","",nBinsMassRatio,0.,1.], LambdaFunc('x: (x.massZ1[0]-x.massZ2[0])/(x.massZ1[0]+x.massZ2[0])'), ),
        Plot("mass_ratio_4e",["TH1D","mass_ratio_4e","",nBinsMassRatio,0.,1.], LambdaFunc('x: (x.massZ1[0]-x.massZ2[0])/(x.massZ1[0]+x.massZ2[0])'), selFunc=LambdaFunc('x: abs(x.idL1[0]) == 11 and abs(x.idL2[0]) == 11 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')),
        #Plot("mass_ratio_4e",["TH1D","mass_ratio_4e","",nBinsMassRatio,0.,1.], LambdaFunc('x: (x.massZ1[0]-x.massZ2[0])/(x.massZ1[0]+x.massZ2[0])'), selFunc=LambdaFunc('x: x.mass4e[0] > 0 and x.mass4mu[0] < 0 and x.mass2e2mu[0] < 0')),
        Plot("mass_ratio_4mu",["TH1D","mass_ratio_4mu","",nBinsMassRatio,0.,1.], LambdaFunc('x: (x.massZ1[0]-x.massZ2[0])/(x.massZ1[0]+x.massZ2[0])'), selFunc=LambdaFunc('x: abs(x.idL1[0]) == 13 and abs(x.idL2[0]) == 13 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')),
        #Plot("mass_ratio_4mu",["TH1D","mass_ratio_4mu","",nBinsMassRatio,0.,1.], LambdaFunc('x: (x.massZ1[0]-x.massZ2[0])/(x.massZ1[0]+x.massZ2[0])'), selFunc=LambdaFunc('x: x.mass4e[0] < 0 and x.mass4mu[0] > 0 and x.mass2e2mu[0] < 0')),
        Plot("mass_ratio_2e2mu",["TH1D","mass_ratio_2e2mu","",nBinsMassRatio,0.,1.], LambdaFunc('x: (x.massZ1[0]-x.massZ2[0])/(x.massZ1[0]+x.massZ2[0])'), selFunc=LambdaFunc('x: abs(x.idL1[0]) == 11 and abs(x.idL2[0]) == 11 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')),
        #Plot("mass_ratio_2e2mu",["TH1D","mass_ratio_2e2mu","",nBinsMassRatio,0.,1.], LambdaFunc('x: (x.massZ1[0]-x.massZ2[0])/(x.massZ1[0]+x.massZ2[0])'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')),
        Plot("mass_ratio_2mu2e",["TH1D","mass_ratio_2mu2e","",nBinsMassRatio,0.,1.], LambdaFunc('x: (x.massZ1[0]-x.massZ2[0])/(x.massZ1[0]+x.massZ2[0])'), selFunc=LambdaFunc('x: abs(x.idL1[0]) == 13 and abs(x.idL2[0]) == 13 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')),
        #Plot("mass_ratio_2mu2e",["TH1D","mass_ratio_2mu2e","",nBinsMassRatio,0.,1.], LambdaFunc('x: (x.massZ1[0]-x.massZ2[0])/(x.massZ1[0]+x.massZ2[0])'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')),
        ]

jet_plots = [
        #Plot("nJet",    ["TH1D","nJet","",5,-0.5,4.5],      LambdaFunc('x: x.njets_pt30_eta2p5[0]'),     ),
        ]

plots = muon_plots + general_plots + jet_plots # big list of Plot objects
#for plot in plots:
    #plot.plotSetting.divideByBinWidth = True

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)

sequence                = darkphoton_signal_unblind_sequence
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = "/home/rosedj1/public_html/Higgs/HToZdZd/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=True))

## Put an index.php file into Plots dir for easy visualization
copyFile('/home/rosedj1/',phpFile,endModuleOutputDir)
