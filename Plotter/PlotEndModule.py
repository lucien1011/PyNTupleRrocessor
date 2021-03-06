import os,ROOT,math,array

from Core.EndModule import EndModule
from Core.BaseObject import BaseObject
from Core.Utils.printFunc import pyPrint

from Utils.tdrstyle import setTDRStyle
from Utils.CMS_lumi import CMS_lumi
from SampleColor import sampleColorDict

ROOT.gROOT.SetBatch(ROOT.kTRUE)

bkdgErrBarColor = 3004

class PlotEndModule(EndModule):
    def __init__(self,outputDir,plots,ratio_switch=False,scaleToData=False,skipSF=False,customSMCountFunc=None):
        self.outputDir = outputDir
        self.plots = plots
        self.switch = ratio_switch
        self.scaleToData = scaleToData
        self.skipSF = skipSF
        self.customSMCountFunc = customSMCountFunc

    def __call__(self,collector):
        for plot in self.plots:
            self.drawPlot(collector,plot,self.outputDir,self.switch)

    def makeTGraph(self,hist,force_x_axis_err=False,filter_func=lambda x: False):
        x_points = []
        exl_points = []
        exh_points = []
        y_points = []
        ely_points = []
        ehy_points = []
        for ibin in range(1,hist.GetNbinsX()+1):
            x = hist.GetXaxis().GetBinCenter(ibin)
            if filter_func(x): continue
            x_points.append(hist.GetXaxis().GetBinCenter(ibin))
            if not force_x_axis_err:
                exl_points.append(0)
                exh_points.append(0)
            else:
                exl_points.append(abs(hist.GetXaxis().GetBinCenter(ibin)-hist.GetXaxis().GetBinUpEdge(ibin)))
                exh_points.append(abs(hist.GetXaxis().GetBinCenter(ibin)-hist.GetXaxis().GetBinLowEdge(ibin)))
            y_points.append(hist.GetBinContent(ibin))
            ely_points.append(hist.GetBinErrorLow(ibin))
            ehy_points.append(hist.GetBinErrorUp(ibin))
        xs = array.array("d",x_points)
        exls = array.array("d",exl_points)
        exhs = array.array("d",exh_points)
        ys = array.array("d",y_points)
        elys = array.array("d",ely_points)
        ehys = array.array("d",ehy_points)
        g = ROOT.TGraphAsymmErrors(len(x_points),xs,ys,exls,exhs,elys,ehys)
        return g

    def drawPlot(self,collector,plot,outputDir,switch):
        if plot.plotSetting.tdr_style:
            setTDRStyle()
            ROOT.gStyle.SetLabelSize(0.018,"XYZ")
            #ROOT.gStyle.SetLabelOffset(0.003, "XYZ")
            ROOT.gStyle.SetTitleSize(0.035,"XYZ")
            #ROOT.gStyle.SetTitleXOffset(1.8)
        self.makedirs(outputDir)
        if plot.dim == 1:
            self.draw1DPlot(collector,plot,outputDir,switch)
        elif plot.dim == 2:
            self.draw2DPlot(collector,plot,outputDir)
        else:
            pyPrint("Skipping plot "+plot.key+" as TH"+str(plot.dim)+" is not supported at the moment")

    def sortHistList(self,histList):
        histList.sort(key=lambda l: l[2], reverse=False)
    
    @staticmethod
    def setDataHistStyle(data):
        data.SetLineWidth(2)
        data.SetLineColor(1)
        data.SetMarkerStyle(8)

    @staticmethod
    def setRatioHistStyle(ratio,axisLabel,plot,):
        ratio.GetYaxis().SetRangeUser(0.0,ratio.GetMaximum()*1.5) 
        ratio.GetYaxis().SetLabelSize(0.09)
        ratio.GetXaxis().SetLabelSize(0.09)
        ratio.GetYaxis().SetTitle("Data/MC")
        ratio.GetYaxis().SetTitleSize(0.10)
        ratio.GetXaxis().SetTitleSize(0.10)
        ratio.GetXaxis().SetTitleOffset(0.90)
        ratio.GetYaxis().SetTitleOffset(0.50)
        ratio.GetXaxis().SetTitle(axisLabel)
        if plot.plotSetting.x_axis_labels:
            for ibin,label in enumerate(plot.plotSetting.x_axis_labels): ratio.GetXaxis().SetBinLabel(ibin+1,label)

    def stackData(self,collector,plot):

        for isample,sample in enumerate(collector.dataSamples):
            h = collector.getObj(sample,plot.rootSetting[1])
            h.SetBinErrorOption(ROOT.TH1.kPoisson)
            if not isample:
                data = h.Clone("data")
            else:
                data.Add(h)

        dataCountErr = ROOT.Double(0.)
        dataCount = data.IntegralAndError(0,data.GetNbinsX()+1,dataCountErr)
        if plot.plotSetting.divideByBinWidth:
            self.divideByBinWidth(data)

        if plot.plotSetting.shift_last_bin: self.shiftLastBin(data,isData=True)

        data.SetBinErrorOption(ROOT.TH1.kPoisson)
        self.setDataHistStyle(data)
        data.SetTitle("")

        return data,dataCount,dataCountErr

    def divideByBinWidth(self,hist):
        for iBin in range(1,hist.GetNbinsX()+1):
            binC = hist.GetBinContent(iBin)
            binE = hist.GetBinError(iBin)
            binW = hist.GetBinWidth(iBin)
            hist.SetBinContent(iBin,binC/binW)
            hist.SetBinError(iBin,binE/binW)

    def stackMC(self,collector,plot,switch,histToScale=None):
        stack = ROOT.THStack(plot.key+'_stack',plot.key+'_stack')

        smCount      = 0.0
        smCountErrSq = 0.0
        histList     = []

        for isample,sample in enumerate(collector.mcSamples if not collector.mergeSamples else collector.mergeSamples):
            if not collector.mergeSamples and collector.sampleDict[sample].isSignal: continue
            if sample not in plot.customHistDict:
                h = collector.getObj(sample,plot.rootSetting[1])
            else:
                h = plot.customHistDict[sample].hist
            smCountErrTmp = ROOT.Double(0.)
            smCount += h.IntegralAndError(0,h.GetNbinsX()+1,smCountErrTmp)
            smCountErrSq += smCountErrTmp**2

        for isample,sample in enumerate(collector.mcSamples if not collector.mergeSamples else collector.mergeSamples):
            if not collector.mergeSamples and collector.sampleDict[sample].isSignal: continue
            if sample not in plot.customHistDict:
                h = collector.getObj(sample,plot.rootSetting[1])
            else:
                h = plot.customHistDict[sample].hist
            if histToScale and smCount: h.Scale(histToScale.Integral(0,histToScale.GetNbinsX()+1)/smCount)
            if sample in sampleColorDict:
                h.SetFillColor(sampleColorDict[sample])
            else:
                h.SetFillColor(ROOT.kViolet)
            if plot.plotSetting.shift_last_bin: self.shiftLastBin(h)
            histList.append([h,sample if sample not in plot.plotSetting.leg_name_dict else plot.plotSetting.leg_name_dict[sample],h.Integral(0,h.GetNbinsX()+1),smCountErrTmp])
            if switch:
                if not isample:
                    totalsum = h.Clone("totalsum_"+plot.key)
                else:
                    totalsum.Add(h)

        self.sortHistList(histList)

        if plot.plotSetting.divideByBinWidth:
            for hist,sample,_,_ in histList:
                self.divideByBinWidth(hist)

        for h,sample,_,_ in histList:
            if switch: h.Divide(totalsum)
            stack.Add(h) 
        
        total = stack.GetStack().Last().Clone("total_"+plot.key)
        total.SetFillColor(ROOT.kYellow)
        total.SetLineColor(ROOT.kRed)
        bkdgErr = stack.GetStack().Last().Clone("totalErr_"+plot.key)   # grey error bars on Monte Carlo
        bkdgErr.SetMarkerStyle(1)
        bkdgErr.SetLineColor(1)
        bkdgErr.SetLineWidth(3)
        bkdgErr.SetFillColor(13)
        #bkdgErr.SetFillStyle(bkdgErrBarColor)
        bkdgErr.SetFillStyle(3001)
        return histList,stack,smCount,smCountErrSq,total,bkdgErr

    def makeSignalHist(self,collector,plot):
        histList = []
        signalSamples = collector.signalSamples if not collector.mergeSigSamples else collector.mergeSigSamples
        for sample in signalSamples:
            h = collector.getObj(sample,plot.rootSetting[1])
            if sample in sampleColorDict:
                h.SetFillColor(sampleColorDict[sample])
            else:
                h.SetFillColor(ROOT.kViolet)
            sigCount = h.Integral(0,h.GetNbinsX()+1)
            if plot.plotSetting.shift_last_bin: self.shiftLastBin(h) 
            h.SetLineStyle(9 if sample not in plot.plotSetting.line_style_dict else plot.plotSetting.line_style_dict[sample])
            h.SetLineWidth(5 if sample not in plot.plotSetting.line_width_dict else plot.plotSetting.line_width_dict[sample])
            if sample in plot.plotSetting.line_color_dict:
                h.SetLineColor(plot.plotSetting.line_color_dict[sample])
            elif sample in sampleColorDict:
                h.SetLineColor(sampleColorDict[sample])
            else:
                h.SetLineColor(ROOT.kRed)
            h.SetFillColorAlpha(ROOT.kRed,0.)
            h.SetStats(0)
            histList.append([h,sample if sample not in plot.plotSetting.leg_name_dict else plot.plotSetting.leg_name_dict[sample],sigCount])

        if plot.plotSetting.divideByBinWidth:
            for hist,sample,sigCount in histList:
                self.divideByBinWidth(hist)

        if plot.plotSetting.normalize:
            for hist,sample,sigCount in histList:
                if hist.Integral(): hist.Scale(1./hist.Integral())

        return histList
    
    def makeSimpleLegend(self,sampleList,plot):
        legPos = [0.70,0.65,0.89,0.87] if not plot.plotSetting.leg_pos else plot.plotSetting.leg_pos
        leg = ROOT.TLegend(*legPos)
        leg.SetBorderSize(0)
        leg.SetFillColor(0)
        if plot.plotSetting.leg_column:
            leg.SetNColumns(plot.plotSetting.leg_column)
        leg.SetTextSize(plot.plotSetting.leg_text_size)
        for sample in sampleList:
            leg.AddEntry(sample.hist, sample.name, "p")
        return leg

    def makeLegend1D(self,histList,bkdgErr,smCount,switch=False,histListSignal=None,data=None,dataCount=None,smCountErr=None,skipError=False,leg_pos_list=[],leg_text_size=None,skip_total=False,sort_sig_func=lambda l: l[1],round_to_func=lambda x: str(math.ceil(x*10)/10),):
        leg_pos = [0.70,0.65,0.89,0.87] if not leg_pos_list else leg_pos_list
        leg = ROOT.TLegend(*leg_pos)
        leg.SetBorderSize(0)
        leg.SetFillColor(0)
        if leg_text_size: leg.SetTextSize(leg_text_size)
        if dataCount != None:
            legLabel = "Data"
            legLabel += ": {0}".format(int(dataCount))
            leg.AddEntry(data, legLabel , "pe")

        legLabel = "Total"
        if switch:
            legLabel += ": 100%"
        else:
            legLabel += ": "+round_to_func(smCount)
        if smCountErr and not skipError:
            legLabel += " #pm "+str(math.ceil(smCountErr*10)/10)

        if bkdgErr and not skip_total:
            leg.AddEntry(bkdgErr, legLabel, "fl")

        for hCount in reversed(histList):
            legLabel = hCount[1]
            error = hCount[3]
            if switch:
                legLabel += ": "+str(math.ceil(math.ceil(hCount[2]*10)/math.ceil(smCount*10)*100000)/1000)+"%"
            else:
                legLabel += ": "+round_to_func(hCount[2])
                if not skipError: legLabel += " #pm"+str(math.ceil(error*10)/10)
            leg.AddEntry(hCount[0], legLabel, "f")

        histListSignal.sort(key=sort_sig_func, reverse=False)
        for hist,sample,sigCount in histListSignal:
            legLabel = sample
            legLabel += ": "+round_to_func(sigCount)
            leg.AddEntry(hist,legLabel,"f")

        return leg

    def getAxisTitle(self,plot):
        if plot.plotSetting.x_axis_title:
            return plot.plotSetting.x_axis_title
        elif plot.key in plot.plotSetting.defaultLabelDict:
            return plot.plotSetting.defaultLabelDict[plot.key]
        else:
            return plot.key

    def draw1DPlot(self,collector,plot,outputDir,switch):
        c = ROOT.TCanvas("c_"+plot.key, "c_"+plot.key,0,0, 650, 750)

        axisLabel = self.getAxisTitle(plot)

        if not collector.mcSamples and not collector.dataSamples:
            raise RuntimeError, "Nothing to be drawn"

        if collector.dataSamples and switch:
            raise RuntimeError, "Cannot run incorporate data samples and background ratio at the same time"

        if collector.dataSamples:
            dataHist,dataCount,dataCountErr = self.stackData(collector,plot)

        if collector.bkgSamples:
            histList,stack,smCount,smCountErrSq,total,bkdgErr = self.stackMC(collector,plot,switch,histToScale=dataHist if self.scaleToData else None)
            stack.SetTitle("")
            if self.customSMCountFunc:
                customSMCount = self.customSMCountFunc(collector,plot)
            else:
                customSMCount = None

        if collector.signalSamples:
            sigHistList = self.makeSignalHist(collector,plot)
        else:
            sigHistList = []

        if collector.bkgSamples:
            bkgMax = stack.GetMaximum()
        else:
            bkgMax = 0.

        if collector.dataSamples:
            dataMax = dataHist.GetMaximum()
        else:
            dataMax = 0.
        
        if collector.signalSamples:
            sigMax = max([hist.GetMaximum() for hist,sample,sigCount in sigHistList])
        else:
            sigMax = 0.

        maximum = max([bkgMax,dataMax,sigMax])

        if collector.bkgSamples and not collector.dataSamples:
            stack.Draw('hist')
            self.setStackAxisTitle(stack,axisLabel,plot)

            leg = self.makeLegend1D(histList,bkdgErr,smCount,switch,histListSignal=sigHistList,smCountErr=math.sqrt(smCountErrSq),leg_text_size=plot.plotSetting.leg_text_size)

            if plot.plotSetting.log_x:
                c.SetLogx(1)

            c.SetLogy(0)
            stack.SetMaximum(maximum*plot.plotSetting.linear_max_factor)
            stack.SetMinimum(0.)
            stack.Draw('hist')
            if plot.plotSetting.x_axis_labels:
                for ibin,label in enumerate(plot.plotSetting.x_axis_labels): stack.GetXaxis().SetBinLabel(ibin+1,label)
            for hist,sample,sigCount in sigHistList:
                hist.Draw('samehist')
            #if collector.dataSamples:
            #    dataHist.Draw("samep")
            leg.Draw('same')
            # Draw CMS, lumi and preliminary if specified
            #self.drawLabels(pSetPair[0].lumi)
            bkdgErr.Draw("samee2")
            if plot.plotSetting.x_axis_labels:
                for ibin,label in enumerate(plot.plotSetting.x_axis_labels): bkdgErr.GetXaxis().SetBinLabel(ibin+1,label)
            c.SaveAs(outputDir+plot.key+".png")
            c.SaveAs(outputDir+plot.key+".pdf")

            if not switch:
                c.SetLogy(1)
                stack.SetMaximum(maximum*plot.plotSetting.log_max_factor)
                stack.SetMinimum(0.1)
                stack.Draw('hist')
                for hist,sample,sigCount in sigHistList:
                    hist.Draw('samehist')
                if collector.dataSamples:
                    dataHist.Draw("samep")
                leg.Draw('same')
                # Draw CMS, lumi and preliminary if specified
                #self.drawLabels(pSetPair[0].lumi)
                bkdgErr.Draw("samee2")

                c.SaveAs(outputDir+plot.key+"_log.png")
                c.SaveAs(outputDir+plot.key+"_log.pdf")
        elif collector.bkgSamples and collector.dataSamples:
            c.SetBottomMargin(0.0)
            ROOT.gStyle.SetErrorX(0)
            if not plot.plotSetting.skip_data_mc_ratio:
                upperPad = ROOT.TPad("upperPad", "upperPad", .001, 0.25, .995, .995)
                lowerPad = ROOT.TPad("lowerPad", "lowerPad", .001, .001, .995, .32)

                upperPad.Draw()
                lowerPad.Draw()

                lowerPad.cd()
                lowerPad.SetGridy(1)
                ROOT.gPad.SetBottomMargin(0.24)

                ratio,bkdgErrRatio,line = self.makeRatioPlot(dataHist,total,bkdgErr)
                ratio.SetStats(0)
                ratio.Draw()
                bkdgErrRatio.Draw("samee2")
                ratio.GetYaxis().SetRangeUser(0.0,ratio.GetMaximum()*1.5) 
                ratio.GetYaxis().SetLabelSize(0.09)
                ratio.GetXaxis().SetLabelSize(0.09)
                ratio.GetYaxis().SetTitle("Data/MC")
                ratio.GetYaxis().SetTitleSize(0.10)
                ratio.GetXaxis().SetTitleSize(0.10)
                ratio.GetXaxis().SetTitleOffset(0.90)
                ratio.GetYaxis().SetTitleOffset(0.50)
                ratio.GetXaxis().SetTitle(axisLabel)
                if plot.plotSetting.x_axis_labels:
                    for ibin,label in enumerate(plot.plotSetting.x_axis_labels): ratio.GetXaxis().SetBinLabel(ibin+1,label)

                bkdgErrRatio.SetMarkerStyle(1)
                bkdgErrRatio.SetLineWidth(1)
                bkdgErrRatio.SetLineColor(1)
                bkdgErrRatio.SetFillColor(1)
                bkdgErrRatio.SetFillStyle(bkdgErrBarColor)

                if plot.plotSetting.ratio_range:
                    ratio.GetYaxis().SetRangeUser(*plot.plotSetting.ratio_range)
                    bkdgErrRatio.GetYaxis().SetRangeUser(*plot.plotSetting.ratio_range)

                ratio.DrawCopy()
                bkdgErrRatio.DrawCopy("samee2")
                line.Draw()

                upperPad.cd()
            else:
                upperPad = c
                ROOT.gPad.SetBottomMargin(0.10)

            leg = self.makeLegend1D(histList,bkdgErr,smCount,switch,data=dataHist,dataCount=dataCount,histListSignal=sigHistList,smCountErr=math.sqrt(smCountErrSq),skipError=plot.plotSetting.skip_leg_err,leg_pos_list=plot.plotSetting.leg_pos,leg_text_size=plot.plotSetting.leg_text_size,)

            upperPad.SetLogy(0)
            stack.SetMaximum(maximum*plot.plotSetting.linear_max_factor)
            dataHist.SetMaximum(maximum*plot.plotSetting.linear_max_factor)

            stack.Draw('hist')
            self.setStackAxisTitle(stack,axisLabel,plot)
            stack.GetXaxis().SetLabelSize(plot.plotSetting.stack_x_label_size)
            stack.GetXaxis().SetTitleOffset(1.00)
            stack.GetYaxis().SetLabelSize(0.05)
            stack.Draw('hist')
            for hist,sample,sigCount in sigHistList:
                hist.Draw('samehist')

            leg.Draw()

            if smCount > 0.0 and dataCount > 0.:
                scaleFactor = dataCount*1.0/smCount
                scaleFactorErr = scaleFactor*math.sqrt(1/dataCount + smCountErrSq/smCount**2)
            else:
                pyPrint("Warning, smCount or dataCount is zero :"+plot.key)
                scaleFactor    = 0.0
                scaleFactorErr = 0.0

            n1 = ROOT.TLatex()
            n1.SetNDC()
            n1.SetTextFont(42)
            n1.SetTextSize(0.05);
            if not self.skipSF:
                n1.DrawLatex(0.11, 0.92, "Data/MC = %.2f #pm %.2f" % (scaleFactor,scaleFactorErr))
            if plot.plotSetting.cms_lumi:
                plot.plotSetting.cms_lumi(upperPad,plot.plotSetting.cms_lumi_number,0)

            dataHist.DrawCopy('same E')
            bkdgErr.Draw("samee2")

            if plot.plotSetting.custom_latex_list:
                for latex_setting in plot.plotSetting.custom_latex_list:
                    latex_setting.latex = ROOT.TLatex()
                    latex_setting.latex.SetTextSize(latex_setting.text_size)
                    latex_setting.latex.DrawLatex(latex_setting.x_pos,latex_setting.y_pos,latex_setting.text)

            ROOT.gPad.RedrawAxis()
            ROOT.gPad.RedrawAxis("G")
            
            c.SaveAs(outputDir+plot.key+".png")
            c.SaveAs(outputDir+plot.key+".pdf")

            upperPad.SetLogy(1)
            stack.SetMaximum(maximum*plot.plotSetting.log_max_factor)
            stack.SetMinimum(plot.plotSetting.log_min)
            stack.Draw('hist')
            for hist,sample,sigCount in sigHistList:
                hist.Draw('samehist')
            dataHist.Draw("same p")
            leg.Draw('same')
            bkdgErr.Draw("samee2")
            n1.DrawLatex(0.11, 0.92, "Data/MC = %.2f #pm %.2f" % (scaleFactor,scaleFactorErr))
            ROOT.gPad.RedrawAxis()
            ROOT.gPad.RedrawAxis("G")

            c.SaveAs(outputDir+plot.key+"_log.png")
            c.SaveAs(outputDir+plot.key+"_log.pdf")

        elif collector.signalSamples and not collector.bkgSamples:

            sigHistList = self.makeSignalHist(collector,plot)
            
            leg = self.makeLegend1D([],None,0.,False,histListSignal=sigHistList)
            
            c.SetLogy(0)
            maximum = max([hist.GetMaximum() for hist,sample,sigCount in sigHistList])
            for hist,sample,sigCount in sigHistList:
                hist.GetYaxis().SetRangeUser(0.,maximum*plot.plotSetting.linear_max_factor)
                hist.Draw('samehist')
            leg.Draw('same')
            c.SaveAs(outputDir+plot.key+".png")
            c.SaveAs(outputDir+plot.key+".pdf")
        elif collector.dataSamples and not collector.mcSamples:
            dataHist.SetStats(0)
            dataHist.GetXaxis().SetTitle(axisLabel)
            dataHist.Draw('p')
            n1 = ROOT.TLatex()
            n1.SetNDC()
            n1.SetTextFont(42)
            n1.SetTextSize(0.05);
            n1.DrawLatex(0.11, 0.92, "Data: %s" % (int(dataHist.Integral(0,dataHist.GetNbinsX()+1))))
            c.SaveAs(outputDir+plot.key+".png")
            c.SaveAs(outputDir+plot.key+".pdf")


    def draw2DPlot(self,collector,plot,outputDir):
        c = ROOT.TCanvas("c_"+plot.key, "c_"+plot.key,0,0, 650, 650)
        sampleList = []
        for isample,sample in enumerate(collector.mergeSamples if not plot.selectedSamples else plot.selectedSamples):
            tmpSampleObj = BaseObject(sample)
            hist = collector.getObj(sample,plot.rootSetting[1])
            hist.SetStats(0)
            hist.SetMarkerColor(sampleColorDict[sample] if sample not in plot.plotSetting.marker_color_dict else plot.plotSetting.marker_color_dict[sample])
            if sample in plot.plotSetting.marker_style_dict:
                markerStyle = plot.plotSetting.marker_style_dict[sample]
            elif plot.plotSetting.marker_style:
                markerStyle = plot.plotSetting.marker_style
            else:
                markerStyle = isample
            hist.SetMarkerStyle(markerStyle)
            hist.SetMarkerSize(plot.plotSetting.marker_size if sample not in plot.plotSetting.marker_size_dict else plot.plotSetting.marker_size_dict[sample])
            if plot.plotSetting.minimum != None and type(plot.plotSetting.minimum) == float: hist.SetMinimum(plot.plotSetting.minimum)
            tmpSampleObj.hist = hist
            sampleList.append(tmpSampleObj)
            if plot.plotSetting.x_axis_title: hist.GetXaxis().SetTitle(plot.plotSetting.x_axis_title)
            if plot.plotSetting.y_axis_title: hist.GetYaxis().SetTitle(plot.plotSetting.y_axis_title)
            if plot.plotSetting.draw_option:
                draw_command = plot.plotSetting.draw_option
            if not isample:
                hist.Draw(draw_command)
            else:
                hist.Draw(draw_command+" same")
            #c.SaveAs(outputDir+sample+"_"+plot.key+".png")
            #c.SaveAs(outputDir+sample+"_"+plot.key+".pdf")
        leg = self.makeSimpleLegend(sampleList,plot)
        leg.Draw("samep")
        if plot.plotSetting.cms_lumi:
            #CMS_lumi(c,plot.plotSetting.cms_lumi_number,11,lumiTextSize=0.35,cmsTextSize=0.35,)
            CMS_lumi(c,plot.plotSetting.cms_lumi_number,11,)
        c.SaveAs(os.path.join(outputDir,plot.key+".png"))
        c.SaveAs(os.path.join(outputDir,plot.key+".pdf"))


    def setStackAxisTitle(self,stack,axisLabel,plot):
        stack.GetXaxis().SetTitleSize(plot.plotSetting.x_axis_title_size)
        stack.GetXaxis().SetTitle(axisLabel)
        allBinWidths = [stack.GetXaxis().GetBinWidth(i) for i in range(1,stack.GetXaxis().GetNbins()+1)]
        constantBinWidth = all([binWidth == allBinWidths[0] for binWidth in allBinWidths])
        if constantBinWidth:
            bin_str = str(int(allBinWidths[0])) if allBinWidths[0].is_integer() else str(allBinWidths[0])
            title = "Events / ("+bin_str+" GeV)"
        elif plot.plotSetting.divideByBinWidth:
            title = "Events / Bin Width"
        elif plot.plotSetting.bin_width_label:
            title = plot.plotSetting.bin_width_label
        else:
            title = "Events"
        stack.GetYaxis().SetTitleSize(plot.plotSetting.y_axis_title_size)
        stack.GetYaxis().SetTitle(title)
    
    def makeRatioTGraph(self,data,total,bkdgErr,no_x_error=True):
        g = ROOT.TGraphAsymmErrors()
        g.Divide(data,total,"pois")
        if no_x_error:
            for i in range(g.GetN()):
                g.SetPointEXlow(i,0.)
                g.SetPointEXhigh(i,0.)
        return g

    def makeRatioPlot(self,data,total,bkdgErr):

        ratio = data.Clone()
        for i in range(1, ratio.GetNbinsX()+1):
            binC_data = data.GetBinContent(i)
            binC_total = total.GetBinContent(i)
            binE_data = data.GetBinError(i)
            binE_total = total.GetBinError(i)
            if binC_total and binC_data:
                binC_ratio = binC_data/binC_total
                binE_ratio = math.sqrt((binE_data/binC_data)**2+(binE_total/binC_total)**2)
            elif binC_total and not binC_data:
                binC_ratio = 0.
                binE_ratio = 0.
            elif not binC_total and not binC_data:
                binC_ratio = 0.
                binE_ratio = 0.
            ratio.SetBinContent(i,binC_ratio)
            ratio.SetBinError(i,binE_ratio*binC_ratio)

        bkdgErrRatio = ratio.Clone()
        for i in range(1, bkdgErrRatio.GetNbinsX()+1):
            binC = bkdgErr.GetBinContent(i)
            binE = bkdgErr.GetBinError(i)
            bkdgErrRatio.SetBinContent(i,1)
            if binC>0.: bkdgErrRatio.SetBinError(i,1*binE/binC)
            else      : bkdgErrRatio.SetBinError(i,0.)

        line = ROOT.TLine(60,1,400,1)
        line = ROOT.TLine(ratio.GetXaxis().GetBinLowEdge(1) ,1,ratio.GetXaxis().GetBinUpEdge(ratio.GetXaxis().GetNbins()),1)
        line.SetLineColor(2)
        line.SetLineWidth(2)

        return ratio,bkdgErrRatio,line

    def shiftLastBin(self,h,isData=False):
        # FirstBin = h.GetXaxis().GetFirst()
        LastBin = h.GetXaxis().GetLast()
        for bin in range( LastBin + 1, LastBin + 2 ):
            h.SetBinContent( LastBin, h.GetBinContent( LastBin ) + h.GetBinContent( bin ) )
            if not isData:
                h.SetBinError( LastBin, math.sqrt( math.pow( h.GetBinError( LastBin ), 2 ) + math.pow( h.GetBinError( bin ), 2 ) ) )
            else:
                h.SetBinError( LastBin, math.sqrt( h.GetBinContent(LastBin)) )
            h.SetBinContent( LastBin + 1, 0. )
            h.SetBinError( LastBin + 1, 0. )
            pass
        return
