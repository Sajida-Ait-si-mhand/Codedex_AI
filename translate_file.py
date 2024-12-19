from translate import Translator
translator = Translator(to_lang='ja')
text = "am I a princess?"
tranlation = translator.translate(text)
print('converting: ', tranlation)