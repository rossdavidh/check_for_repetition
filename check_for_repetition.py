import sys
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize

sw = stopwords.words("english")

filename = sys.argv[1]

f = open('./'+filename,'r')
raw = f.read()


sent_tokenize_list = sent_tokenize(raw)
for sentence in sent_tokenize_list:
    words = word_tokenize(sentence)
    fdist = nltk.FreqDist(words)
    repeated_words = list(filter(lambda x: ((x[1]>=2) and (x[0] not in sw) and (len(x[0])>2)),fdist.items()))
    if len(repeated_words)>0:
        print('\n',sentence,repeated_words)
