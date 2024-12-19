from translate import Translator
translator = Translator(to_lang='ja')
text = "I am a princess?"
tranlation = translator.translate(text)
print('converting: ', tranlation)