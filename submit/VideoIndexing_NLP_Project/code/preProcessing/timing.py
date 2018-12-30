import pysrt
import datetime
import time
import re
import copy

def text_to_word_list(text):
   ''' Pre process and convert texts to a list of words '''
   text = str(text)
   text = text.lower()

   # Clean the text
   text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", text)
   text = re.sub(r"what's", "what is ", text)
   text = re.sub(r"\'s", " ", text)
   text = re.sub(r"\'ve", " have ", text)
   text = re.sub(r"can't", "cannot ", text)
   text = re.sub(r"n't", " not ", text)
   text = re.sub(r"i'm", "i am ", text)
   text = re.sub(r"\'re", " are ", text)
   text = re.sub(r"\'d", " would ", text)
   text = re.sub(r"\'ll", " will ", text)
   text = re.sub(r",", " ", text)
   text = re.sub(r"\.", " ", text)
   text = re.sub(r"!", " ! ", text)
   text = re.sub(r"\/", " ", text)
   text = re.sub(r"\^", " ^ ", text)
   text = re.sub(r"\+", " + ", text)
   text = re.sub(r"\-", " - ", text)
   text = re.sub(r"\=", " = ", text)
   text = re.sub(r"'", " ", text)
   text = re.sub(r"(\d+)(k)", r"\g<1>000", text)
   text = re.sub(r":", " : ", text)
   text = re.sub(r" e g ", " eg ", text)
   text = re.sub(r" b g ", " bg ", text)
   text = re.sub(r" u s ", " american ", text)
   text = re.sub(r"\0s", "0", text)
   text = re.sub(r" 9 11 ", "911", text)
   text = re.sub(r"e - mail", "email", text)
   text = re.sub(r"j k", "jk", text)
   text = re.sub(r"\s{2,}", " ", text)

   # text = text.split()

   return text


subFile = 'D:/m.tech/Sem 3/NLP/Project/VideoIndexing/Result/srtFiles/subs15.srt'
subSave = 'D:/m.tech/Sem 3/NLP/Project/VideoIndexing/Result/timedSrt/subs15.srt'
outFile = 'D:/m.tech/Sem 3/NLP/Project/VideoIndexing/Result/3Dec2018/stringFile2_3Dec.srt'
subs = pysrt.open(subFile)

fp = open(outFile,'w')
first = 0
buffer_time = datetime.time(0,0,0)
for s in subs :
    print str(s.text.encode('utf-8'))
    fp.write(str(s.index)+" \n")

    print s.start.to_time()
    print type(s.start.to_time())
    s.text = text_to_word_list(str(s.text.encode('utf-8')))
    if first ==0 and s.index==1:
        first =1
        fp.write(str(s.start.to_time())+" "+s.TIMESTAMP_SEPARATOR+" "+str(s.end.to_time())+" \n")
        fp.write(s.text.encode('utf-8') + ' \n')
        continue
    elif first==1 and s.index==1:
    #elif first ==1 and s.start.hours==0 and s.start.minutes==0 and s.start.seconds ==0:
        # found start
        print "found start"
        #print datetime.timedelta(hours=last.end.hours, minutes=last.end.minutes, seconds=last.end.seconds)
        x = last.end
        delta = datetime.timedelta(hours=x.hours, minutes=x.minutes, seconds=x.seconds)
        buffer_time = (datetime.datetime.combine(datetime.date(1, 1, 1), buffer_time) + delta).time()
        print "buffer :"
        print buffer_time

    last = copy.deepcopy(s)

    delta = datetime.timedelta(hours=buffer_time.hour,minutes=buffer_time.minute,seconds=buffer_time.second)
    temp = datetime.time(s.start.hours, s.start.minutes, s.start.seconds)
    newStart = s.start
    xStart = (datetime.datetime.combine(datetime.date(1, 1, 1), temp) + delta).time()
    newStart.hours = xStart.hour
    newStart.minutes = xStart.minute
    newStart.seconds = xStart.second
    s.start = newStart

    temp = datetime.time(s.end.hours, s.end.minutes, s.end.seconds)
    newEnd = s.end
    xEnd = (datetime.datetime.combine(datetime.date(1, 1, 1), temp) + delta).time()
    newEnd.hours = xEnd.hour
    newEnd.minutes = xEnd.minute
    newEnd.seconds = xEnd.second
    s.end = newEnd

    print str(s.text.encode('utf-8'))
    fp.write(str(s.start) + " " + s.TIMESTAMP_SEPARATOR + " " + str(s.end) + ' \n')
    fp.write(s.text.encode('utf-8') + ' \n')


    print "last"

subs.save(subSave)

fp.close()
