from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

bkgSkimTreeDir          = system.getStoragePath()+"/lucien/Higgs/DarkZ-NTuple/20190122/SkimTree_DarkPhoton_Run2016Data_m4l70/"
bkgSkimTreeDir_qqZZext1 = system.getStoragePath()+"/lucien/Higgs/DarkZ-NTuple/20190817/SkimTree_DarkPhoton_Run2016Data_m4l70/"
bkgTreeDir              = "/cms/data/store/user/t2/users/klo/Higgs/HZZ4l/NTuple/Run2/MC80X_M17_4l_Feb21/"
dataTreeDir             = bkgSkimTreeDir 
bkgTreeDir_qqZZext1     = "/cms/data/store/user/t2/users/klo/Higgs/HZZ4l/NTuple/Run2/MC80X_M17_4lSkim_Sep13_v2//"
sigSkimTreeDir          = system.getStoragePath()+"/lucien/Higgs/DarkZ-NTuple/20181019/SkimTree_DarkPhoton_Run2017Sig_m4l70/"
sigTreeDir              = "/cms/data/store/user/t2/users/klo/Higgs/DarkZ/NTuples/SigMC_Run2016_v1/"
zxSkimTreeDir           = system.getStoragePath()+"/lucien/Higgs/DarkZ-NTuple/20181116/SkimTree_DarkPhoton_ZX_Run2016Data_m4l70/"
inUFTier2               = False
sumWeightHist           = "Ana/sumWeights"
xsBoost                 = 100
epsilon                 = 0.05
saveSumWeightTxt        = True

# ____________________________________________________________________________________________________________________________________________ ||
# Z+X
ZPlusX_cmpList = ComponentList(
        [
            Component("ZPlusX",
                zxSkimTreeDir+"Data_Run2016-03Feb2017_noDuplicates_FRWeight.root",
                "passedEvents",False)
        ]
        )
ZPlusX = Dataset(
        "ZPlusX",
        ZPlusX_cmpList,
        isMC                = True,
        skipWeight          = True,
        )

# ____________________________________________________________________________________________________________________________________________ ||
# Data2016
data2016_cmpList = ComponentList(
        [ 
            Component("Data2016",dataTreeDir+"Data_Run2016-03Feb2017_4l.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

data2016 = Dataset(
        "Data2016",
        data2016_cmpList,
        isMC                = False,
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo4tau
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo4tau",
                bkgSkimTreeDir+"GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8.root",
                "passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo4tau = Dataset(
        "ggZZTo4tau",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.001586,
        )
handleSumWeight(
        ggZZTo4tau,
        system,
        bkgTreeDir+"GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo4e
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo4e",
                bkgSkimTreeDir+"GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8.root",
                "passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo4e = Dataset(
        "ggZZTo4e",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.001586,
        )
handleSumWeight(
        ggZZTo4e,
        system,
        bkgTreeDir+"GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo4mu
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo4mu",
                bkgSkimTreeDir+"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8.root",
                "passedEvents",inUFTier2=inUFTier2),
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
        bkgTreeDir+"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo2mu2tau
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo2mu2tau",
                bkgSkimTreeDir+"GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8.root",
                "passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo2mu2tau = Dataset(
        "ggZZTo2mu2tau",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.00319,
        )
handleSumWeight(
        ggZZTo2mu2tau,
        system,
        bkgTreeDir+"GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo2e2mu
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo2e2mu",
                bkgSkimTreeDir+"GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8.root",
                "passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo2e2mu = Dataset(
        "ggZZTo2e2mu",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.00319,
        )
handleSumWeight(
        ggZZTo2e2mu,
        system,
        bkgTreeDir+"GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo2e2tau
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo2e2tau",
                bkgSkimTreeDir+"GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8.root",
                "passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo2e2tau = Dataset(
        "ggZZTo2e2tau",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.00319,
        )
handleSumWeight(
        ggZZTo2e2tau,
        system,
        bkgTreeDir+"GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# qqZZ
qqZZ_cmpList = ComponentList(
        [ 
            #Component("qqZZTo4L",bkgSkimTreeDir+"ZZTo4L_13TeV-amcatnloFXFX-pythia8_RunIISummer16MiniAODv2_1.root","passedEvents",inUFTier2=inUFTier2),
            Component("qqZZTo4L",bkgSkimTreeDir+"ZZTo4L_13TeV_powheg_pythia8.root","passedEvents",inUFTier2=inUFTier2),
            #Component("qqZZTo4L",bkgSkimTreeDir_qqZZext1+"ZZTo4L_13TeV_powheg_pythia8_ext1.root","passedEvents",inUFTier2=inUFTier2),
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
        bkgTreeDir+"ZZTo4L_13TeV_powheg_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"ZZTo4L_13TeV_powheg_pythia8.txt",
        )

qqZZext1_cmpList = ComponentList(
        [ 
            Component("qqZZTo4L",bkgSkimTreeDir_qqZZext1+"ZZTo4L_13TeV_powheg_pythia8_ext1.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

qqZZTo4L_ext1 = Dataset(
        "qqZZTo4L",
        qqZZext1_cmpList,
        isMC                = True,
        xs                  = 1.256,
        )
handleSumWeight(
        qqZZTo4L_ext1,
        system,
        bkgTreeDir_qqZZext1+"ZZTo4L_13TeV_powheg_pythia8_ext1.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir_qqZZext1+"ZZTo4L_13TeV_powheg_pythia8_ext1.txt",
        )

qqZZTo4L.add(qqZZTo4L_ext1)

# ____________________________________________________________________________________________________________________________________________ ||
# ggH
ggH_cmpList = ComponentList(
        [ 
            Component("ggH",bkgSkimTreeDir+"GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggH = Dataset(
        "ggH",
        ggH_cmpList,
        isMC                = True,
        #xs                  = 0.01218,
        xs                  = 48.52*0.0002768,
        )
handleSumWeight(
        ggH,
        system,
        bkgTreeDir+"GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# VBF
VBF_cmpList = ComponentList(
        [ 
            Component("VBF",bkgSkimTreeDir+"VBF_HToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

VBF = Dataset(
        "VBF",
        VBF_cmpList,
        isMC                = True,
        xs                  = 0.001044,
        )
handleSumWeight(
        VBF,
        system,
        bkgTreeDir+"VBF_HToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"VBF_HToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# WHplus
WHplus_cmpList = ComponentList(
        [ 
            Component("WHplus",bkgSkimTreeDir+"WplusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUgenV6_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

WHplus = Dataset(
        "WHplus",
        WHplus_cmpList,
        isMC                = True,
        xs                  = 0.000232,
        )
handleSumWeight(
        WHplus,
        system,
        bkgTreeDir+"WplusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUgenV6_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"WplusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUgenV6_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# WHminus
WHminus_cmpList = ComponentList(
        [ 
            Component("WHminus",bkgSkimTreeDir+"WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUgenV6_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

WHminus = Dataset(
        "WHminus",
        WHminus_cmpList,
        isMC                = True,
        xs                  = 0.000147,
        )
handleSumWeight(
        WHminus,
        system,
        bkgTreeDir+"WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUgenV6_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUgenV6_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ZH
ZH_cmpList = ComponentList(
        [ 
            Component("ZH",bkgSkimTreeDir+"ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUgenV6_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ZH = Dataset(
        "ZH",
        ZH_cmpList,
        isMC                = True,
        xs                  = 0.000668,
        )
handleSumWeight(
        ZH,
        system,
        bkgTreeDir+"ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUgenV6_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUgenV6_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ggHZZd_M4
HZZd_M4_cmpList = ComponentList(
        [ Component("HZZd_M4",sigSkimTreeDir+"ZD_UpTo0j_MZD4_Eps1e-2_klo_1.root","passedEvents",inUFTier2=inUFTier2) ]
        )
HZZd_M4 = Dataset(
        "HZZd_M4",
        HZZd_M4_cmpList,
        isMC                = True,
        isSignal            = True,
        #xs                  = 3.396e-6*xsBoost, # Madgraph xs
        #xs                  = 48.58*0.288*epsilon**2*0.06729, # Assume h->ZZd br to be 100%
        xs                  = 48.58*epsilon**2*0.000219, # Take Br(h->ZZd->4l from paper
        )
handleSumWeight(
        HZZd_M4,
        system,
        sigTreeDir+"ZD_UpTo0j_MZD4_Eps1e-2_klo.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        sigSkimTreeDir+"ZD_UpTo0j_MZD4_Eps1e-2_klo.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# HZZd_M7
HZZd_M7_cmpList = ComponentList(
        [ Component("HZZd_M7",sigSkimTreeDir+"ZD_UpTo0j_MZD7_Eps1e-2_klo_1.root","passedEvents",inUFTier2=inUFTier2) ]
        )
HZZd_M7 = Dataset(
        "HZZd_M7",
        HZZd_M7_cmpList,
        isMC                = True,
        isSignal            = True,
        #xs                  = 3.396e-6*xsBoost, # Madgraph xs
        #xs                  = 48.58*0.288*epsilon**2*0.06729, # Assume h->ZZd br to be 100%
        xs                  = 48.58*epsilon**2*0.000597, # Take Br(h->ZZd->4l from paper
        )
handleSumWeight(
        HZZd_M7,
        system,
        sigTreeDir+"ZD_UpTo0j_MZD7_Eps1e-2_klo.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        sigSkimTreeDir+"ZD_UpTo0j_MZD7_Eps1e-2_klo.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# HZZd_M10
HZZd_M10_cmpList = ComponentList(
        [ Component("HZZd_M10",sigSkimTreeDir+"ZD_UpTo0j_MZD10_Eps1e-2_klo_1.root","passedEvents",inUFTier2=inUFTier2) ]
        )
HZZd_M10 = Dataset(
        "HZZd_M10",
        HZZd_M10_cmpList,
        isMC                = True,
        isSignal            = True,
        #xs                  = 3.396e-6*xsBoost, # Madgraph xs
        #xs                  = 48.58*0.288*epsilon**2*0.06729, # Assume h->ZZd br to be 100%
        xs                  = 48.58*epsilon**2*0.00126, # Take Br(h->ZZd->4l from paper
        )
handleSumWeight(
        HZZd_M10,
        system,
        sigTreeDir+"ZD_UpTo0j_MZD10_Eps1e-2_klo.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        sigSkimTreeDir+"ZD_UpTo0j_MZD10_Eps1e-2_klo.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# HZZd_M15
HZZd_M15_cmpList = ComponentList(
        [ Component("HZZd_M15",sigSkimTreeDir+"ZD_UpTo0j_MZD15_Eps1e-2_klo_1.root","passedEvents",inUFTier2=inUFTier2) ]
        )
HZZd_M15 = Dataset(
        "HZZd_M15",
        HZZd_M15_cmpList,
        isMC                = True,
        isSignal            = True,
        #xs                  = 3.396e-6*xsBoost, # Madgraph xs
        #xs                  = 48.58*0.288*epsilon**2*0.06729, # Assume h->ZZd br to be 100%
        xs                  = 48.58*epsilon**2*(0.00252+0.00338)/2., # Take Br(h->ZZd->4l from paper
        )
handleSumWeight(
        HZZd_M15,
        system,
        sigTreeDir+"ZD_UpTo0j_MZD15_Eps1e-2_klo.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        sigSkimTreeDir+"ZD_UpTo0j_MZD15_Eps1e-2_klo.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# HZZd_M20
HZZd_M20_cmpList = ComponentList(
        [ Component("HZZd_M20",sigSkimTreeDir+"ZD_UpTo0j_MZD20_Eps1e-2_klo_1.root","passedEvents",inUFTier2=inUFTier2) ]
        )
HZZd_M20 = Dataset(
        "HZZd_M20",
        HZZd_M20_cmpList,
        isMC                = True,
        isSignal            = True,
        #xs                  = 6.34e-06*xsBoost,
        #xs                  = 48.58*0.286*epsilon**2*0.06729,
        xs                  = 48.58*epsilon**2*0.00555, # Take Br(h->ZZd->4l) from paper
        )
handleSumWeight(
        HZZd_M20,
        system,
        sigTreeDir+"ZD_UpTo0j_MZD20_Eps1e-2_klo.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        sigSkimTreeDir+"ZD_UpTo0j_MZD20_Eps1e-2_klo.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# HZZd_M25
HZZd_M25_cmpList = ComponentList(
        [ Component("HZZd_M25",sigSkimTreeDir+"ZD_UpTo0j_MZD25_Eps1e-2_klo_1.root","passedEvents",inUFTier2=inUFTier2) ]
        )
HZZd_M25 = Dataset(
        "HZZd_M25",
        HZZd_M25_cmpList,
        isMC                = True,
        isSignal            = True,
        #xs                  = 9.956e-06*xsBoost,
        #xs                  = 48.58*0.283*epsilon**2*0.06729,
        xs                  = 48.58*epsilon**2*(0.00814+0.00940)/2., # Take Br(h->ZZd->4l from paper
        )
handleSumWeight(
        HZZd_M25,
        system,
        sigTreeDir+"ZD_UpTo0j_MZD25_Eps1e-2_klo.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        sigSkimTreeDir+"ZD_UpTo0j_MZD25_Eps1e-2_klo.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# HZZd_M30
HZZd_M30_cmpList = ComponentList(
        [ Component("HZZd_M30",sigSkimTreeDir+"ZD_UpTo0j_MZD30_Eps1e-2_klo_1.root","passedEvents",inUFTier2=inUFTier2) ]
        )
HZZd_M30 = Dataset(
        "HZZd_M30",
        HZZd_M30_cmpList,
        isMC                = True,
        isSignal            = True,
        #xs                  = 1.196e-05*xsBoost,
        #xs                  = 48.58*0.280*epsilon**2*0.06729,
        xs                  = 48.58*epsilon**2*0.0108, # Take Br(h->ZZd->4l from paper
        )
handleSumWeight(
        HZZd_M30,
        system,
        sigTreeDir+"ZD_UpTo0j_MZD30_Eps1e-2_klo.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        sigSkimTreeDir+"ZD_UpTo0j_MZD30_Eps1e-2_klo.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
bkgSamples = [
        ggH,
        VBF,
        WHplus,
        WHminus,
        ZH,
        qqZZTo4L,
        ggZZTo2e2mu,
        ggZZTo2e2tau,
        ggZZTo2mu2tau,
        ggZZTo4e,
        ggZZTo4mu,
        ggZZTo4tau,
        ZPlusX,
        #data2016,
        ]

sigSamples = [
        HZZd_M4,
        HZZd_M7,
        HZZd_M10,
        HZZd_M15,
        HZZd_M20,
        HZZd_M25,
        HZZd_M30,
        #HZZd_M35,
        ]

dataSamples = [data2016,]
