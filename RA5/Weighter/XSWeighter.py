
from Core.Module import Module

class XSWeighter(Module):
    def __init__(self,name):
        super(XSWeighter,self).__init__(name)
        self.fb_to_pb_factor = 1000

    def analyze(self,event):
        event.weight = 1.
        if self.dataset.isMC:
            event.weight *= event.genWeight[0]
            if not self.dataset.xs:
                xs = event.xsec[0]
            else:
                xs = self.dataset.xs
            if self.dataset.parent.xsFactor:
                xs *= self.dataset.parent.xsFactor
            nevts = self.dataset.sumw
            lumi = self.dataset.lumi
            event.weight *= xs*lumi*self.fb_to_pb_factor/self.dataset.sumw
        return True
