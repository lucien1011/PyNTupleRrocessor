

def handleSumWeight(dataset,system,sumWeightFile,sumWeightHist,inUFTier2,saveSumWeightTxt,textFilePathToWrite,textFilePathToRead=None,justUseTextFile=False):
    if textFilePathToRead:
        dataset.setSumWeightByTxt(textFilePathToRead)
    elif system.getSystemMode() == system.remote_str:
        dataset.setSumWeight(
                sumWeightFile,
                sumWeightHist,inUFTier2)
        if saveSumWeightTxt:
            dataset.saveSumWeightToPath(textFilePathToWrite)
    elif system.getSystemMode() == system.local_str:
        dataset.setSumWeightByTxt(textFilePathToWrite)
    

