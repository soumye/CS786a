import numpy as np
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

def parser(in_str,ps,lmtzr):
	stop_words = set(stopwords.words('english'))
	stop_words.add('.')
	stop_words.add(',')
	word_tokens = word_tokenize(in_str)
	out_str = [ps.stem(lmtzr.lemmatize(w.lower())) for w in word_tokens if not w in stop_words]
	return out_str