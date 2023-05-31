import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
py_sword = set (stopwords.words ('english'))
py_txt = "hot to use nltk pos tag by using python."
py_token = sent_tokenize (py_txt)
for i in py_token:
   	py_lword = nltk.word_tokenize (i)
   	py_lword = [w for w in py_lword if not w in py_sword]
   	py_tag = nltk.pos_tag (py_lword)
   	print (py_tag)