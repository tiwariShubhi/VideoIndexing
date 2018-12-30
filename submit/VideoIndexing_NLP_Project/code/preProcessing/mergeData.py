import os
import re


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

   text = text.split()

   return text


folderPath = 'D:/m.tech/Sem 3/NLP/Project/VideoIndexing/Dataset/COURSERA_BigData/'
outFile = 'D:/m.tech/Sem 3/NLP/Project/VideoIndexing/Result/BigData1Rem.srt'
dirList = os.listdir(folderPath)
c=0
fp = open(outFile,'w',)
for dirName in dirList:
    dir2 = os.listdir(folderPath+dirName)
    for d in dir2:
        fileList = os.listdir(folderPath+dirName+'/'+d)
        for file in fileList:
            c+=1
            fileData = [line.rstrip('\n') for line in open(folderPath + dirName +'/'+ d+ '/' + file)]
            for line in fileData:
                if line.find('WEBVTT')!= -1:
                    continue
                else:

                    fp.write(line+'\n')

fp.close()
print c