import os

folderPath = 'D:/m.tech/Sem 3/NLP/Project/VideoIndexing/Dataset/COURSERA_BigData/'
outFile = 'D:/m.tech/Sem 3/NLP/Project/VideoIndexing/Result/BigData1.srt'
dirList = os.listdir(folderPath)

fp = open(outFile,'w')
for dirName in dirList:
    dir2 = os.listdir(folderPath+dirName)
    for d in dir2:
        fileList = os.listdir(folderPath+dirName+'/'+d)
        for file in fileList:
            fileData = [line.rstrip('\n') for line in open(folderPath + dirName +'/'+ d+ '/' + file)]
            for line in fileData:
                fp.write(line+'\n')

fp.close()
