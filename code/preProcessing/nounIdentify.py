############################
#
#
#trying to find noun in a video subtitle
#using pos tagger
import nltk
# nltk.download('punkt')
# nltk.download('words')
# nltk.download('stopwords')
# nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')


inFile = "D:\m.tech\Sem 3\NLP\Project\VideoIndexing\data\L2_Introduction_to_Software_Engineering_English.srt"

fileData = open(inFile,'r')
fileData = [line.rstrip('\n') for line in open(inFile)];

data = {}
allData =""
c =1
for line in fileData:
    if line == str(c):
        c += 1
        continue
    elif '-->' in line:
        continue
    else:
        allData += line + " "

text = nltk.word_tokenize(allData)
tags = nltk.pos_tag(text)

#print tags
# for tup  in tags:
#     if tup[1] == 'NN':
#         print tup[0]

print allData