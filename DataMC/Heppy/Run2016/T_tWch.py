from DataMC.NanoAOD.Run2016.common import * 

sampleName  = "T_tWch"
dir_path    = common_path+"ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/InclusiveSelection_v1/180517_141716/0000/"
inUFTier2   = True

cmp = makeComponents(sampleName,dir_path,"Events",inUFTier2)

cmpList = ComponentList(
        cmp,
        )

T_tWch = Dataset(
        sampleName,
        cmpList,
        xs                  = 38.09 #pb,
        )
T_tWch.setSumWeight("/raid/raid7/lucien/SUSY/RA5/SumGenWeight/NanoAOD_InclusiveSelection_v1/Run2016/"+sampleName+"/EventWeight.root")
