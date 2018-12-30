# -*- coding: utf-8 -*-
"""VideoIndexing_end_to_end.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1006uev6fJlpMP1vaeXtCBQj0FuGq2-mg
"""

import os
import re
import glob
import nltk
import pysrt
import sklearn
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

video_url = raw_input("Please enter youtube video link:")
n_id = video_url.find("&")
if n_id != -1:
   video_url = video_url[:n_id]
cmd = ["youtube-dl",
      "--skip-download",
      "--write-sub",
      "--write-auto-sub",
      "--quiet",
      "--sub-lang",
      "en",
      video_url
   ]

op_log = os.system(" ".join(cmd))
print(op_log)
if op_log != 0:
   print("Please enter a valid Youtube video link, which has english subtitle.")

en_stop = set(nltk.corpus.stopwords.words('english'))
files = os.listdir('./')
for file in files:
    if file.endswith('.en.vtt'):
        file_path = file

def text_to_word_list(text):
    ''' Pre process and convert texts to a list of words '''
    text = str(text.encode('utf-8'))
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

    return text

def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma
    
def get_lemma2(word):
    return WordNetLemmatizer().lemmatize(word)

n_samples = 2000
n_features = 1000
n_components = 1
n_top_words = 25
n_slice = 25

def prepare_text_for_lda(text):
    tokens=text.split()
    tokens = [token for token in tokens if len(token) > 4]
    tokens = [token for token in tokens if token not in en_stop]
    tokens = [get_lemma(token) for token in tokens]
    return tokens

def print_top_words(model, feature_names, n_top_words):
    mess=[]
    for topic_idx, topic in enumerate(model.components_):
        message = " ".join([feature_names[i]
                            for i in topic.argsort()[:-n_top_words - 1:-1]])
        mess.append(message)
    return mess

subs = pysrt.open(file_path)
os.remove(file_path)

subtitles=[]

mega_subs=[] 
count=0
time=""
# print(len(subs))
for i in subs:
  
    subtitles.append(text_to_word_list((i.text)))
    if(count==0):
        temp=str(i.start.hours)+":"+str(i.start.minutes)+":"+str(i.start.seconds)
    
    if(count==n_slice-1):
        temp=temp+","+str(i.end.hours)+":"+str(i.end.minutes)+":"+str(i.end.seconds)
    
    count=count+1
    if(count%n_slice==0):
        hi=[]
        hi.append(temp)
        merge=[subtitles,hi]
        mega_subs.append(merge)
        temp=""
        subtitles=[]
        count=0

if(count!=0):
    mega_subs.append(subtitles)

# print(len(mega_subs))
# print(text_to_word_list(i.text))
# print(mega_subs[0][0])

id = 0
result = {}
result_NMF=[]
result_LDA=[]


tfidf_vectorizer = TfidfVectorizer(max_df=1.0, min_df=1,
                                   max_features=n_features,
                                   stop_words='english')

for i in range(len(mega_subs)-1):
    tfidf = tfidf_vectorizer.fit_transform(mega_subs[i][0])
    tf_vectorizer = CountVectorizer(max_df=1.0, min_df=1,
                                  max_features=n_features,
                                  stop_words='english')
  
    tf = tf_vectorizer.fit_transform(mega_subs[i][0])

# Fit the NMF model
    nmf = NMF(n_components=n_components, random_state=1,
            alpha=.1, l1_ratio=.5).fit(tfidf)

# Fit the NMF model

    nmf = NMF(n_components=n_components, random_state=1,
            beta_loss='kullback-leibler', solver='mu', max_iter=1000, alpha=.1,
            l1_ratio=.5).fit(tfidf)


    lda = LatentDirichletAllocation(n_components=n_components, max_iter=5,
                                  learning_method='online',
                                  learning_offset=50.,
                                  random_state=0)

    lda.fit(tf)

#   print("\nTopics in LDA model:")
    tf_vectorizer._validate_vocabulary()
    tf_feature_names = tf_vectorizer.get_feature_names()
    result_LDA.append(print_top_words(lda, tf_feature_names, n_top_words))

mega_sub_res=[]

count=0
for item in (result_LDA):
    temp1=[]
    temp1.append(item)
    temp1.append(mega_subs[count][1])
    mega_sub_res.append(temp1)
    count=count+1

# print(i, len(mega_subs))

my_big_list = []

my_set = set()
for i in range(0, len(mega_sub_res)-1):
    my_set = set()
    row = mega_sub_res[i]
    comp0 = row[0]
    comp0 = comp0[0].split(' ')
    comp1 = row[1][0]
    for item in comp0:
        my_set.add(item)
    my_sub_list = [my_set, comp1]
    my_big_list.append(my_sub_list)

def jaccard_similarity(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / float(union)

threshold = 0.0638298

merged_big_list = []
merged_big_content = []
merged_big_list.append(my_big_list[0])
merged_big_content.append(mega_subs[0][0])
i = 1
while i < len(my_big_list):
    similarity = jaccard_similarity(merged_big_list[-1][0], my_big_list[i][0])
    if similarity < threshold:
        merged_big_list[-1][0].union(my_big_list[i][0])
        start = merged_big_list[-1][1].split(',')[0]
        finish = my_big_list[i][1].split(',')[1]
        merged_big_list[-1][1] = start+','+finish
        merged_big_content[-1] += mega_subs[i][0]
    else:
        merged_big_list.append(my_big_list[i])
        merged_big_content.append(mega_subs[i][0])
    i += 1

result_LDA = []

tfidf_vectorizer = TfidfVectorizer(max_df=1.0, min_df=1,
                                   max_features=n_features,
                                   stop_words='english')

for i in range(len(merged_big_content)):
  
    tfidf = tfidf_vectorizer.fit_transform(merged_big_content[i])

    tf_vectorizer = CountVectorizer(max_df=1.0, min_df=1,
                                  max_features=n_features,
                                  stop_words='english')

    tf = tf_vectorizer.fit_transform(merged_big_content[i])

    nmf = NMF(n_components=n_components, random_state=1,
            alpha=.1, l1_ratio=.5).fit(tfidf)

    nmf = NMF(n_components=n_components, random_state=1,
            beta_loss='kullback-leibler', solver='mu', max_iter=1000, alpha=.1,
            l1_ratio=.5).fit(tfidf)


    lda = LatentDirichletAllocation(n_components=n_components, max_iter=5,
                                  learning_method='online',
                                  learning_offset=50.,
                                  random_state=0)

    lda.fit(tf)

    tf_feature_names = tf_vectorizer.get_feature_names()
    tokens = print_top_words(lda, tf_feature_names, 5)[0].split()
    result_LDA.append(set(tokens))

data = {}
data['timings'] = [i[1] for i in merged_big_list]
data['result'] = result_LDA
print("")
for i in range(len(data['result'])):
    start = data['timings'][i].split(',')[0]
    end = data['timings'][i].split(',')[1]
    text = data['result'][i]
    line = start + "=" + end
    #print(start,'-->', end,'=', text)
    print(line,"=",text)
