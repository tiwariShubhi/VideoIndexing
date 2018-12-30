# ---------------------------------------------------------------------------------------
# NLP Project
# ---------------------------------------------------------------------------------------
# Developed by : Shubhi Tiwari
# Date :
# ---------------------------------------------------------------------------------------

import os
import nltk
import string
import math
import pysrt
import pickle
import datetime
from nltk.metrics.scores import recall

def extractTiming(fileData):
    start = "00:00:00"
    for i in range(len(fileData)-1,0,-1):
        line = fileData[i]
        if line.find('-->') != -1:
            # found
            end = line.split('--> ')
            end = end[1][:8]
            # print end
            break

    return start+',' + str(end)

def generateTimings(fileName):
    subs = pysrt.open(fileName)
    first =0
    timings = []
    last = subs[0]
    for s in subs:

        if s.index == 1:
            if first == 0:
                start = s.start
                first = 1
            elif first != 0:
                end = last.end
                time_str = str(start.hours) + ":" +str(start.minutes) + ":" + str(start.seconds) + "," + str(end.hours) + ":" + str(end.minutes) + ":" + str(end.seconds)
                timings.append(time_str)
            # first = 1
            start = s.start

        last = s
    end = last.end
    time_str = str(start.hours) + ":" + str(start.minutes) + ":" + str(start.seconds) + "," + str(
        end.hours) + ":" + str(end.minutes) + ":" + str(end.seconds)
    timings.append(time_str)
    print timings
    return timings


stopWords = nltk.corpus.stopwords.words('english') + list(string.punctuation)
gt_file = 'D:/m.tech/Sem 3/NLP/Project/VideoIndexing/Result/timedSrt/subs15.srt'
pred_file = 'D:/m.tech/Sem 3/NLP/Project/VideoIndexing/Result/3Dec2018/result_1_night.pkl'
gt_topics = [] # list of lists
gt_timings = [] # list of timings
folderPath = 'D:/m.tech/Sem 3/NLP/Project/VideoIndexing/Dataset/COURSERA_BigData/'
truth = 'D:/m.tech/Sem 3/NLP/Project/VideoIndexing/Result/groundTruth.txt'
trueTime = 'D:/m.tech/Sem 3/NLP/Project/VideoIndexing/Result/groundTime.txt'
dirList = os.listdir(folderPath)

#
# for dirName in dirList:
#     dir2 = os.listdir(folderPath+dirName)
#     for d in dir2:
#         fileList = os.listdir(folderPath+dirName+'/'+d)
#         for fileName in fileList:
#             # fileData = [line.rstrip('\n') for line in open(folderPath + dirName + '/' + d + '/' + fileName)]
#             # time = extractTiming(fileData)
#             # gt_timings.append(time)
#             temp = set()
#             tok = nltk.word_tokenize(fileName.decode('latin-1'))
#             for t in tok:
#                 if t.find('.vtt') != -1:
#                     p = t.split('.')
#                     t = p[0]
#
#                 if t not in stopWords:
#                     temp.add(t)
#                     # temp.append(t)
#
#             gt_topics.append(temp)
            #gt_topics.add(temp)
# trueFp = open(truth,'w')
# d = 0
# for t in gt_topics:
#     trueFp.write(str(t)+'\n')
#     if d==4:
#         trueFp.write("----------------------"+' \n')
#         d = -1
#     d +=1
# trueFp.close()
# for t in gt_timings:
#     print("---------------------------------")
#     print t

d = 0
gt_timings = generateTimings(gt_file)
trueFp = open(trueTime,'a+')
trueFp.write('\n')
for t in gt_timings:
    trueFp.write(str(t) + '\n')
    if d == 4:
        trueFp.write("----------------------")
        d = -1
    d += 1
trueFp.close()


#
#
# pred_topics =[]  # predicted truth topics
# #pred_topics = gt_topics
#
# pred_timings = []
# #pred_timings = gt_timings
#
#
# with open(pred_file,'rb') as fp:
#     data = pickle.load(fp)
#     #print data
#     pred_topics = data['result']
#     pred_timings = data['timings']
# print pred_timings
# print(len(pred_topics))
# print(len(pred_timings))
# # compute recall on basis of gt_topics
# rec = 0
# flag = 0
# max = 0
# if len(gt_timings)>len(pred_timings):
#     flag=1
#     max = len(gt_timings)
# else:
#     flag=2
#     max = len(pred_timings)
#
# j = 0
# i = 0
# left =0
# tick = 0
# count = 0
# #for i in range(max):
# while 1:
#     if flag==1:
#         temp = pred_timings[j].split(',')
#         pred_start = temp[0].split(':')
#         pred_end = temp[1].split(':')
#         delta1 = datetime.timedelta(hours=pred_start[0],minutes=pred_start[1],seconds=pred_start[2])
#         delta2 = datetime.timedelta(hours=pred_end[0], minutes=pred_end[1], seconds=pred_end[2])
#         pred_duration = (delta2-delta1).total_seconds()
#         print pred_duration
#
#         temp = gt_timings[i].split(',')
#         gt_start = temp[0].split(':')
#         gt_end = temp[1].split(':')
#         delta1 = datetime.timedelta(hours=gt_start[0], minutes=gt_start[1], seconds=gt_start[2])
#         delta2 = datetime.timedelta(hours=gt_end[0], minutes=gt_end[1], seconds=gt_end[2])
#         gt_duration = (delta2 - delta1).total_seconds()
#         print gt_duration
#
#         wt = float(gt_duration) / float(pred_duration)
#         if wt > 1:
#             wt = 1
#
#         left = pred_duration - gt_duration
#
#         groundTruth = gt_topics[i]
#         prediction = pred_topics[j]
#         rec += (wt * recall(groundTruth, prediction))
#
#         if left <= 0:
#             j += 1
#
#     elif flag==2:
#         #less no of gt timings
#
#
#
#         if left < 0:
#             pred_duration = abs(left)
#             tick = 0
#
#             temp = gt_timings[j].split(',')
#             gt_start = temp[0].split(':')
#             gt_end = temp[1].split(':')
#             delta1 = datetime.timedelta(hours=int(gt_start[0]), minutes=int(gt_start[1]), seconds=int(gt_start[2]))
#             delta2 = datetime.timedelta(hours=int(gt_end[0]), minutes=int(gt_end[1]), seconds=int(gt_end[2]))
#             gt_duration = (delta2 - delta1).total_seconds()
#             print gt_duration
#
#         elif left > 0:
#             temp = pred_timings[i].split(',')
#             pred_start = temp[0].split(':')
#             pred_end = temp[1].split(':')
#             delta1 = datetime.timedelta(hours=int(pred_start[0]), minutes=int(pred_start[1]),
#                                         seconds=int(pred_start[2]))
#             delta2 = datetime.timedelta(hours=int(pred_end[0]), minutes=int(pred_end[1]), seconds=int(pred_end[2]))
#             pred_duration = (delta2 - delta1).total_seconds()
#             print pred_duration
#             tick=1
#             gt_duration = left
#         else:
#             temp = gt_timings[j].split(',')
#             gt_start = temp[0].split(':')
#             gt_end = temp[1].split(':')
#             delta1 = datetime.timedelta(hours=int(gt_start[0]), minutes=int(gt_start[1]), seconds=int(gt_start[2]))
#             delta2 = datetime.timedelta(hours=int(gt_end[0]), minutes=int(gt_end[1]), seconds=int(gt_end[2]))
#             gt_duration = (delta2 - delta1).total_seconds()
#             print gt_duration
#
#             temp = pred_timings[i].split(',')
#             pred_start = temp[0].split(':')
#             pred_end = temp[1].split(':')
#             delta1 = datetime.timedelta(hours=int(pred_start[0]), minutes=int(pred_start[1]),
#                                         seconds=int(pred_start[2]))
#             delta2 = datetime.timedelta(hours=int(pred_end[0]), minutes=int(pred_end[1]), seconds=int(pred_end[2]))
#             pred_duration = (delta2 - delta1).total_seconds()
#             print pred_duration
#
#
#         wt = float(pred_duration)/float(gt_duration)
#         if wt>1:
#             wt  =1
#
#         left = gt_duration - pred_duration
#
#         groundTruth = gt_topics[j]
#         prediction = pred_topics[i]
#
#         rec += (wt*recall(groundTruth, prediction))
#
#         if left <= 0:
#             j += 1
#         else:
#             i+=1
#
#         count +=1
#         if (i>=len(pred_timings) or j>=len(gt_timings)):
#
#             break
#         # if tick==1:
#         #     i+=1
#
# avg_recall = float(rec)/ float(max)
#
# print avg_recall
#
# # for i in range(len(pred_topics)):
# #     groundTruth = gt_topics[i]
# #     prediction = pred_topics[i]
# #     rec += recall(groundTruth,prediction)
# #
# # avg_recall = float(rec)/ float(len(gt_topics))
# #
# # print avg_recall
# # # print rec
# #
# # # timing accuracy
# # err = 0
# # for i in range(len(pred_timings)):
# #     gt_st = gt_timings[i].split(',')
# #     gt_et = gt_timings[i].split(',')
# #
# #     pred_st = pred_timings[i].split(',')
# #     pred_et = pred_timings[i].split(',')
# #
# #     # start time
# #     groundTruth = gt_st[0].split(":")
# #     prediction = pred_st[0].split(":")
# #
# #     err += math.pow((abs(int(groundTruth[0]) - int(prediction[0])) * 3600) + (abs(int(groundTruth[1]) - int(prediction[1])) * 60) + (abs(int(groundTruth[2]) - int(prediction[2]))),2)
# #
# #     # end time
# #     groundTruth = gt_et[1].split(":")
# #     prediction = pred_et[1].split(":")
# #
# #     err += math.pow((abs(int(groundTruth[0]) - int(prediction[0])) * 3600) + (
# #                 abs(int(groundTruth[1]) - int(prediction[1])) * 60) + (abs(int(groundTruth[2]) - int(prediction[2]))),
# #                        2)
# #
# # rmse = math.sqrt(float(err)/float(len(2*gt_timings)))
# #
# # print rmse
#
