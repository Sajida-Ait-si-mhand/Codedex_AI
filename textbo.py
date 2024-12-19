from textblob import TextBlob

text = "I lov Programmingg"
blob = TextBlob(text)
corrected_text = blob.correct()
print("oldver:", blob)
print("newver:", corrected_text)