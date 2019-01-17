
from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc

from DarkZ.Dataset.Run2016.WrongFC_MC import * 
from DarkZ.Dataset.Run2016.WrongFC_Data import * 

from DarkZ.Sequence.RecoSequence import * 

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

#out_path = "WrongFC/DataMCDistributions/SkimTree_WFC_m4l70_Run2016Data_v1/2018-09-20/"
#out_path = "WrongFC/DataMCDistributions/SkimTree_WFC_m4l108To140_Run2016Data_v1/2018-10-24_SR/"
out_path = "WrongFC/DataMCDistributions/SkimTree_WFC_m4l118To130_Run2016Data_v1/2018-10-24_SR/"

mZ1PlotRange = [40,40.,120.]
mZ2PlotRange = [30,0.,60.]
#mZ2PlotRange = [60,0.,120.]
#h4lPlotRange = [110,60.,500.]
h4lPlotRange = [40,100.,140.]
general_plots = []
general_plots.extend([
    Plot("Z1_mass",         ["TH1D","Z1_mass","",]+mZ1PlotRange,        LambdaFunc('x: x.massZ1[0]'),       ),#selFunc=LambdaFunc(region_sel_str_whole)      ),
    Plot("Z2_mass",         ["TH1D","Z2_mass","",]+mZ2PlotRange,        LambdaFunc('x: x.massZ2[0]'),       ),#selFunc=LambdaFunc(region_sel_str_whole)      ), 
    Plot("h4L_mass",        ["TH1D","h4L_mass","",]+h4lPlotRange,       LambdaFunc('x: x.mass4l[0]'),       ),#selFunc=LambdaFunc(region_sel_str_whole)      ), 
    Plot("met",             ["TH1D","met","",40,0.,200.],               LambdaFunc('x: x.met[0]'),          ),#selFunc=LambdaFunc(region_sel_str_whole),     ),
    Plot("nVtx",            ["TH1D","nVtx","",30,0.0,60.0],             LambdaFunc('x: x.nVtx[0]'),         ),#selFunc=LambdaFunc(region_sel_str_whole),     ),
    ])

plots =  general_plots
#for plot in plots:
#    plot.plotSetting.divideByBinWidth = True

nCores                  = 1
outputDir               = "/raid/raid7/lucien/Higgs/DarkZ/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = [qqZZTo4L,Data_Run2016,WFC_Reducible,]
justEndSequence         = False

for dataset in componentList:
    if dataset.isMC:
        #dataset.lumi = 41.4
        dataset.lumi = 35.9
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)

sequence                = darkphoton_signal_sequence

sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = "/home/lucien/public_html/Higgs/DarkZ/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots))