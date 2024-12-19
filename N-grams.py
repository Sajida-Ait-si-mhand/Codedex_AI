import nltk 

from nltk.tokenize import word_tokenize
from nltk.util import ngrams

sentence = "I am a AMANDA"
tokenize = word_tokenize(sentence)
bigram = list(ngrams(tokenize, 5))
print("tokenize: ", bigram)