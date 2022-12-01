import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('API Key')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(
    'URL'
)

def english_to_french(french_text):
    #Converts English Text to French
    french_text = language_translator.translate(
        text=french_text,model_id='en-fr').get_result()
    return french_text.get("translations")[0].get("translation")

def french_to_english(english_text):
    ##Converts French Text to English
    english_text = language_translator.translate(
        text=english_text,model_id='fr-en').get_result()
    return english_text.get("translations")[0].get("translation")


while True:
    #Takes in Text and from Language
    WORD = str(input('Please Enter text: '))
    CHOICE = str(input('To English or French? '))
    if CHOICE == 'French':
        #Runs function called above, converts to French
        Translated = english_to_french(WORD)
        print(Translated)
        break
    if CHOICE == 'English':
        #Runs function called above, converts to English
        Translated = french_to_english(WORD)
        print(Translated)
        break
#Program Complete