from googletrans import Translator
import googletrans

print(len(googletrans.LANGUAGES))
translator = Translator()
#Translate a text from one language to another
result = translator.translate("Hello, how are you?", src='en', dest='tamil')
print(result.text)