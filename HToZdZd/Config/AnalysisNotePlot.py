from Plotter.Plot import Plot
from Core.Utils.LambdaFunc import LambdaFunc
import array

# ________________________________________________________________________ ||
#mZ1PlotRange        = [60-1,array.array('d',[40.*1.02**i for i in range(60)]),]
#mZ2PlotRange        = [180-1,array.array('d',[4.*1.02**i for i in range(180)]),]
#mZ2PlotRange        = [38,4.,80.,]
#h4lPlotRange        = [47-1,array.array('d',[80.*1.02**i for i in range(47)]),]
mZ1PlotRange = [32,0.,64.]
mZ2PlotRange = [32,0.,64.]
#h4lPlotRange = [50,95.,195.]
h4lPlotRange = [70,60.,200.]
#h4lPlotRange = [140,60.,200.]

# ________________________________________________________________________ ||
sel_4e_str      = "abs(x.idL1[0]) == 11 and abs(x.idL2[0]) == 11 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11"
sel_2mu2e_str   = "abs(x.idL1[0]) == 13 and abs(x.idL2[0]) == 13 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11"
sel_4mu_str     = "abs(x.idL1[0]) == 13 and abs(x.idL2[0]) == 13 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13"
sel_2e2mu_str   = "abs(x.idL1[0]) == 11 and abs(x.idL2[0]) == 11 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13"

var_mZ1_str     = "x.massZ1[0]"
var_mZ2_str     = "x.massZ2[0]"
var_m4l_str     = "x.mass4l[0]"

low_m4l_str     = "x.mass4l[0] > 100 and x.mass4l[0] < 118"
mid_m4l_str     = "x.mass4l[0] > 118 and x.mass4l[0] < 130"
high_m4l_str    = "x.mass4l[0] > 130 and x.mass4l[0] < 170"

# ________________________________________________________________________ ||
general_4e_plots = [
        Plot("mZ1_4e",["TH1D","mZ1_4e","",]+mZ1PlotRange, LambdaFunc('x: '+var_mZ1_str), selFunc=LambdaFunc('x: '+sel_4e_str)),
        Plot("mZ2_4e",["TH1D","mZ2_4e","",]+mZ2PlotRange, LambdaFunc('x: '+var_mZ2_str), selFunc=LambdaFunc('x: '+sel_4e_str)),
        Plot("m4l_4e",["TH1D","m4l_4e","",]+h4lPlotRange, LambdaFunc('x: '+var_m4l_str), selFunc=LambdaFunc('x: '+sel_4e_str)),
        ]

general_2mu2e_plots = [
        Plot("mZ1_2mu2e",["TH1D","mZ1_2mu2e","",]+mZ1PlotRange, LambdaFunc('x: '+var_mZ1_str), selFunc=LambdaFunc('x: '+sel_2mu2e_str)),
        Plot("mZ2_2mu2e",["TH1D","mZ2_2mu2e","",]+mZ2PlotRange, LambdaFunc('x: '+var_mZ2_str), selFunc=LambdaFunc('x: '+sel_2mu2e_str)),
        Plot("m4l_2mu2e",["TH1D","m4l_2mu2e","",]+h4lPlotRange, LambdaFunc('x: '+var_m4l_str), selFunc=LambdaFunc('x: '+sel_2mu2e_str)),
        ]

general_4mu_plots = [
        Plot("mZ1_4mu",["TH1D","mZ1_4mu","",]+mZ1PlotRange, LambdaFunc('x: '+var_mZ1_str), selFunc=LambdaFunc('x: '+sel_4mu_str)),
        Plot("mZ2_4mu",["TH1D","mZ2_4mu","",]+mZ2PlotRange, LambdaFunc('x: '+var_mZ2_str), selFunc=LambdaFunc('x: '+sel_4mu_str)),
        Plot("m4l_4mu",["TH1D","m4l_4mu","",]+h4lPlotRange, LambdaFunc('x: '+var_m4l_str), selFunc=LambdaFunc('x: '+sel_4mu_str)),
        ]

general_2e2mu_plots = [
        Plot("mZ1_2e2mu",["TH1D","mZ1_2e2mu","",]+mZ1PlotRange, LambdaFunc('x: '+var_mZ1_str), selFunc=LambdaFunc('x: '+sel_2e2mu_str)),
        Plot("mZ2_2e2mu",["TH1D","mZ2_2e2mu","",]+mZ2PlotRange, LambdaFunc('x: '+var_mZ2_str), selFunc=LambdaFunc('x: '+sel_2e2mu_str)),
        Plot("m4l_2e2mu",["TH1D","m4l_2e2mu","",]+h4lPlotRange, LambdaFunc('x: '+var_m4l_str), selFunc=LambdaFunc('x: '+sel_2e2mu_str)),    
        ]
