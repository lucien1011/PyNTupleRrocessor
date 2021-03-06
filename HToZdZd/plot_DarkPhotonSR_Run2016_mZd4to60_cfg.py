from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Core.Utils.mkdir_p import mkdir_p,copyFile

from HToZdZd.Dataset.Run2016.SkimTree_DarkPhoton_mZd4to60 import * 
from HToZdZd.Sequence.RecoSequence import * 

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

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
        "VVVVBS": [
            "WWW_4F",
            "WWZ",
            "WZZ",
            "ZZZ",
            "WpWpJJ",
            "WWTo2L2Nu",
            ],
        "ZPlusX": ["ZPlusX"],
        }

mZ1PlotRange = [31,0.,62.]
mZ2PlotRange = [31,0.,62.]
h4lPlotRange = [50,95.,195.]
#h4lPlotRange = [140,60.,200.]

phpFile                 = "index.php"
out_path                = "DarkPhotonSB/DataMCDistributions/20190130_Run2016_mZd4to60_ahmadTEST/"
lumi                    = 35.9
nCores                  = 5
#outputDir               = "/raid/raid7/lucien/Higgs/HToZdZd/"+out_path
outputDir               = "/raid/raid7/rosedj1/Higgs/HToZdZd/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + [data2016] 
justEndSequence         = False
region_sel_str_whole = "x: True"

muon_plots = [
        Plot("LeadingLepton_pt", ["TH1D","LeadingLepton_pt","",20,0.,200.], LambdaFunc('x: max([ x.pTL1[0], x.pTL2[0], x.pTL3[0], x.pTL4[0] ])')),
        
        Plot("Muon1_Pt", ["TH1D","Muon1_pt","",20,0.,200.], LambdaFunc('x: [x.pTL1[0]] if abs(x.idL1[0]) == 13 else []'), isCollection=True),
        Plot("Muon2_Pt", ["TH1D","Muon2_pt","",20,0.,100.], LambdaFunc('x: [x.pTL2[0]] if abs(x.idL2[0]) == 13 else []'), isCollection=True),
        Plot("Muon3_Pt", ["TH1D","Muon3_pt","",20,0.,100.], LambdaFunc('x: [x.pTL3[0]] if abs(x.idL1[0]) == 13 else []'), isCollection=True),
        Plot("Muon4_Pt", ["TH1D","Muon4_pt","",20,0.,50.],  LambdaFunc('x: [x.pTL4[0]] if abs(x.idL1[0]) == 13 else []'), isCollection=True),
        
        Plot("Muon1_Eta", ["TH1D","Muon1_eta","",20,-3.,3.], LambdaFunc('x: [x.etaL1[0]] if abs(x.idL1[0]) == 13 else []'), isCollection=True),
        Plot("Muon2_Eta", ["TH1D","Muon2_eta","",20,-3.,3.], LambdaFunc('x: [x.etaL2[0]] if abs(x.idL2[0]) == 13 else []'), isCollection=True),
        Plot("Muon3_Eta", ["TH1D","Muon3_eta","",20,-3.,3.], LambdaFunc('x: [x.etaL3[0]] if abs(x.idL1[0]) == 13 else []'), isCollection=True),
        Plot("Muon4_Eta", ["TH1D","Muon4_eta","",20,-3.,3.], LambdaFunc('x: [x.etaL4[0]] if abs(x.idL1[0]) == 13 else []'), isCollection=True),
        
        Plot("Muon1_Phi", ["TH1D","Muon1_phi","",20,-5.,5.], LambdaFunc('x: [x.phiL1[0]] if abs(x.idL1[0]) == 13 else []'), isCollection=True),
        Plot("Muon2_Phi", ["TH1D","Muon2_phi","",20,-5.,5.], LambdaFunc('x: [x.phiL2[0]] if abs(x.idL2[0]) == 13 else []'), isCollection=True),
        Plot("Muon3_Phi", ["TH1D","Muon3_phi","",20,-5.,5.], LambdaFunc('x: [x.phiL3[0]] if abs(x.idL1[0]) == 13 else []'), isCollection=True),
        Plot("Muon4_Phi", ["TH1D","Muon4_phi","",20,-5.,5.], LambdaFunc('x: [x.phiL4[0]] if abs(x.idL1[0]) == 13 else []'), isCollection=True),

        Plot("Electron1_Pt", ["TH1D","Electron1_pt","",20,0.,200.], LambdaFunc('x: [x.pTL1[0]] if abs(x.idL1[0]) == 11 else []'), isCollection=True),
        Plot("Electron2_Pt", ["TH1D","Electron2_pt","",20,0.,100.], LambdaFunc('x: [x.pTL2[0]] if abs(x.idL2[0]) == 11 else []'), isCollection=True),
        Plot("Electron3_Pt", ["TH1D","Electron3_pt","",20,0.,100.], LambdaFunc('x: [x.pTL3[0]] if abs(x.idL1[0]) == 11 else []'), isCollection=True),
        Plot("Electron4_Pt", ["TH1D","Electron4_pt","",20,0.,50.],  LambdaFunc('x: [x.pTL4[0]] if abs(x.idL1[0]) == 11 else []'), isCollection=True),
        
        Plot("Electron1_Eta", ["TH1D","Electron1_eta","",20,-3.,3.], LambdaFunc('x: [x.etaL1[0]] if abs(x.idL1[0]) == 11 else []'), isCollection=True),
        Plot("Electron2_Eta", ["TH1D","Electron2_eta","",20,-3.,3.], LambdaFunc('x: [x.etaL2[0]] if abs(x.idL2[0]) == 11 else []'), isCollection=True),
        Plot("Electron3_Eta", ["TH1D","Electron3_eta","",20,-3.,3.], LambdaFunc('x: [x.etaL3[0]] if abs(x.idL1[0]) == 11 else []'), isCollection=True),
        Plot("Electron4_Eta", ["TH1D","Electron4_eta","",20,-3.,3.], LambdaFunc('x: [x.etaL4[0]] if abs(x.idL1[0]) == 11 else []'), isCollection=True),
        
        Plot("Electron1_Phi", ["TH1D","Electron1_phi","",20,-5.,5.], LambdaFunc('x: [x.phiL1[0]] if abs(x.idL1[0]) == 11 else []'), isCollection=True),
        Plot("Electron2_Phi", ["TH1D","Electron2_phi","",20,-5.,5.], LambdaFunc('x: [x.phiL2[0]] if abs(x.idL2[0]) == 11 else []'), isCollection=True),
        Plot("Electron3_Phi", ["TH1D","Electron3_phi","",20,-5.,5.], LambdaFunc('x: [x.phiL3[0]] if abs(x.idL1[0]) == 11 else []'), isCollection=True),
        Plot("Electron4_Phi", ["TH1D","Electron4_phi","",20,-5.,5.], LambdaFunc('x: [x.phiL4[0]] if abs(x.idL1[0]) == 11 else []'), isCollection=True),
        
        #Plot("DeltaRL12",     ["TH1D","DeltaL12","",]+deltaRPlotRange,  LambdaFunc('x: x.deltaRL12'),       ),
        #Plot("DeltaRL13",     ["TH1D","DeltaL13","",]+deltaRPlotRange,  LambdaFunc('x: x.deltaRL13'),       ),
        #Plot("DeltaRL14",     ["TH1D","DeltaL14","",]+deltaRPlotRange,  LambdaFunc('x: x.deltaRL14'),       ),
        #Plot("DeltaRL23",     ["TH1D","DeltaL23","",]+deltaRPlotRange,  LambdaFunc('x: x.deltaRL23'),       ),
        #Plot("DeltaRL24",     ["TH1D","DeltaL24","",]+deltaRPlotRange,  LambdaFunc('x: x.deltaRL24'),       ),
        #Plot("DeltaRL34",     ["TH1D","DeltaL34","",]+deltaRPlotRange2,  LambdaFunc('x: x.deltaRL34'),       ),
        #Plot("MinDeltaRL",     ["TH1D","MinDeltaRL","",]+deltaRPlotRange2,  LambdaFunc('x: x.minDeltaRL'),       ),
        ]

general_plots = [
        Plot("Z1_mass",      ["TH1D","Z1_mass","",]+mZ1PlotRange,       LambdaFunc('x: x.massZ1[0]'),       ),
        Plot("Z2_mass",      ["TH1D","Z2_mass","",]+mZ2PlotRange,       LambdaFunc('x: x.massZ2[0]'),       ),
        Plot("Z1_4e_mass",   ["TH1D","Z1_4e_mass","",]+mZ1PlotRange,    LambdaFunc('x: x.massZ1[0]'), selFunc=LambdaFunc('x: x.mass4e[0] > 0')      ),
        Plot("Z2_4e_mass",   ["TH1D","Z2_4e_mass","",]+mZ2PlotRange,    LambdaFunc('x: x.massZ2[0]'), selFunc=LambdaFunc('x: x.mass4e[0] > 0')     ),
        Plot("Z1_4mu_mass",  ["TH1D","Z1_4mu_mass","",]+mZ1PlotRange,   LambdaFunc('x: x.massZ1[0]'), selFunc=LambdaFunc('x: x.mass4mu[0] > 0')      ),
        Plot("Z2_4mu_mass",  ["TH1D","Z2_4mu_mass","",]+mZ2PlotRange,   LambdaFunc('x: x.massZ2[0]'), selFunc=LambdaFunc('x: x.mass4mu[0] > 0')     ),
        Plot("Z1_2e2mu_mass",["TH1D","Z1_2e2mu_mass","",]+mZ1PlotRange, LambdaFunc('x: x.massZ1[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0')      ),
        Plot("Z2_2e2mu_mass",["TH1D","Z2_2e2mu_mass","",]+mZ2PlotRange, LambdaFunc('x: x.massZ2[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')     ),
        Plot("Z2_2mu2e_mass",["TH1D","Z2_2mu2e_mass","",]+mZ2PlotRange, LambdaFunc('x: x.massZ2[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')     ),
              
        Plot("h4L_mass",    ["TH1D","h4L_mass","",]+h4lPlotRange,    LambdaFunc('x: x.mass4l[0]'),       ),
        #Plot("h4e_mass",    ["TH1D","h4e_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass4e[0]'), selFunc=LambdaFunc('x: x.mass4e[0] > 0')       ),
        Plot("h4e_mass",    ["TH1D","h4e_mass","",]+h4lPlotRange,    LambdaFunc('x: x.mass4e[0]'), selFunc=LambdaFunc('x: x.mass4e[0] > 0 and x.mass4mu[0] < 0 and x.mass2e2mu[0] < 0')       ),
        #Plot("h4mu_mass",   ["TH1D","h4mu_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass4mu[0]'), selFunc=LambdaFunc('x: x.mass4mu[0] > 0')       ),
        Plot("h4mu_mass",   ["TH1D","h4mu_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass4mu[0]'), selFunc=LambdaFunc('x: x.mass4mu[0] > 0 and x.mass4e[0] < 0 and x.mass2e2mu[0] < 0')       ),
        ##Plot("h2e2mu_mass", ["TH1D","h2mu2e_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass2e2mu[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0')       ),
        #Plot("h2e2mu_mass", ["TH1D","h2e2mu_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass2e2mu[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and x.mass4mu[0] < 0 and x.mass4e[0] < 0')       ),
        Plot("h2e2mu_mass", ["TH1D","h2e2mu_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass2e2mu[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and x.mass4mu[0] < 0 and x.mass4e[0] < 0 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')       ),
        Plot("h2mu2e_mass", ["TH1D","h2mu2e_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass2e2mu[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and x.mass4mu[0] < 0 and x.mass4e[0] < 0 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')       ),
        Plot("h4L_Pt",      ["TH1D","h4L_Pt","",40,0.,200.],        LambdaFunc('x: x.pT4l[0]'),         ),
        
        Plot("met",         ["TH1D","met","",40,0.,200.],           LambdaFunc('x: x.met[0]'),          ),
        Plot("nVtx",        ["TH1D","nVtx","",30,0.0,60.0],         LambdaFunc('x: x.nVtx[0]')),
        Plot("nVtx_4mu",    ["TH1D","nVtx_4mu","",30,0.0,60.0],     LambdaFunc('x: x.nVtx[0]'), selFunc=LambdaFunc('x: x.mass4mu[0] > 0')),
        Plot("nVtx_4e",     ["TH1D","nVtx_4e","",30,0.0,60.0],      LambdaFunc('x: x.nVtx[0]'), selFunc=LambdaFunc('x: x.mass4e[0] > 0')),
        Plot("nVtx_2e2mu",  ["TH1D","nVtx_2e2mu","",30,0.0,60.0],   LambdaFunc('x: x.nVtx[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0')),
        #Plot("h4Lmass_vs_Z1mass",["TH2D","h4Lmass_vs_Z1mass","",]+h4lPlotRange+mZ1PlotRange, LambdaFunc('x: [x.mass4l[0],x.massZ1[0]]'), dim=2, selFunc=LambdaFunc(region_sel_str_whole)),
        #Plot("h4Lmass_vs_Z2mass",["TH2D","h4Lmass_vs_Z2mass","",]+h4lPlotRange+mZ2PlotRange, LambdaFunc('x: [x.mass4l[0],x.massZ2[0]]'), dim=2, selFunc=LambdaFunc(region_sel_str_whole)),
        Plot("Z1mass_vs_Z2mass",["TH2D","Z1mass_vs_Z2mass","",]+mZ1PlotRange+mZ2PlotRange, LambdaFunc('x: [x.massZ1[0],x.massZ2[0]]'), dim=2, selFunc=LambdaFunc(region_sel_str_whole)),
        ]

jet_plots = [
        Plot("nJet",    ["TH1D","nJet","",5,-0.5,4.5],      LambdaFunc('x: x.njets_pt30_eta2p5[0]'),     ),
        ]

plots = muon_plots + general_plots + jet_plots
#plots = muon_plots + general_plots
#for plot in plots:
#    plot.plotSetting.divideByBinWidth = True

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)

#sequence                = darkphoton_fullm4l_sequence
sequence                = darkphoton_sb_sequence
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence) # compiles the histograms!
#endModuleOutputDir = "/home/lucien/public_html/Higgs/HToZdZd/"+out_path
endModuleOutputDir = "/home/rosedj1/public_html/Higgs/HToZdZd/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=True))

## Put an index.php file into Plots dir for easy visualization
copyFile('/home/rosedj1/',phpFile,endModuleOutputDir)
