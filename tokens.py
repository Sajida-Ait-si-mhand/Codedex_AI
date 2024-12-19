
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt_tab')
sample_text = "I START TO LOVE PROGRAMMING!"
tokens = word_tokenize(sample_text)
print("Tokens:", tokens)

