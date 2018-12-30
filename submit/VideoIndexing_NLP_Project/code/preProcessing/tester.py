import pysrt
import datetime
import time
subFile = 'D:/m.tech/Sem 3/NLP/Project/VideoIndexing/Result/BigData1Rem.srt'
subSave = 'D:/m.tech/Sem 3/NLP/Project/VideoIndexing/Result/bigTest.srt'
subs = pysrt.open(subFile)

subs.save(subSave)
