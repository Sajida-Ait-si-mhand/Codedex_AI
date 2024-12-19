import nltk

from nltk.tokenize import word_tokenize
from nltk.util import ngrams

sentence = "I am a princess"
token = word_tokenize(sentence)
grams = list(ngrams(token, 2))
print("grams:", grams)