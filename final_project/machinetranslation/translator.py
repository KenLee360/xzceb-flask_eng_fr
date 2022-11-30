import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#Passes in API Key and URL to use language tranlsator
authenticator = IAMAuthenticator('#Removed API key')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(
    'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/9074e938-5391-4ab9-b292-1c1b6825b51e'
)

def english_to_french(french_text):
    #Converts English Text to French Text outputs as JSON
    french_text = language_translator.translate(
        text=french_text,model_id='en-fr').get_result()
    return french_text

def french_to_english(english_text):
    ##Converts French Text to English Text outputs as JSON
    english_text = language_translator.translate(
        text=english_text,model_id='fr-en').get_result()
    return english_text


while True:
    #Takes in Text and from Language
    WORD = str(input('Please Enter text: '))
    CHOICE = str(input('To English or French? '))
    if CHOICE == 'French':
        #Runs function called above, converts to French
        Translated = english_to_french(WORD)
        print(json.dumps(Translated))
        break
    if CHOICE == 'English':
        #Runs function called above, converts to English
        Translated = french_to_english(WORD)
        print(json.dumps(Translated))
        break
#Program Complete