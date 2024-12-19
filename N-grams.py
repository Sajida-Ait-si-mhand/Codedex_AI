import nltk

from nltk.tokenize import word_tokenize
from nltk.util import ngrams

sentence = "I am a princess"
token = word_tokenize(sentence)
grams = list(ngrams(token, 4))
print("\033[92mngrams:\033[0m", "\033[95m", grams, "\033[0m")
