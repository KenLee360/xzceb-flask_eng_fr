import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
#import os
#from dotenv import load_dotenv

#load_dotenv()

#apikey = os.environ['j4PwIL9v2Wv-7XCvUISYQzvAQ91J7N3imSsxadNYVfq_']
#url = os.environ['https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/9074e938-5391-4ab9-b292-1c1b6825b51e']

authenticator = IAMAuthenticator('#Removed API Key#')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/9074e938-5391-4ab9-b292-1c1b6825b51e')

def englishToFrench():
    englishText = str(input('Enter English Text: '))
    frenchText = language_translator.translate(
        text=englishText,model_id='en-fr').get_result()
    print(englishText)
    print(frenchText)

def frenchToEnglish():
    frenchText = str(input('Enter French Text: '))
    englishText = language_translator.translate(
        text=frenchText,model_id='fr-en').get_result()
    print(frenchText)
    print(englishText)


while True:
    choice = str(input('English or French? '))
    if choice == 'English':
        englishToFrench()
        break
    if choice == 'French':
        frenchToEnglish()
        break
    else:
        print('Not a valid Answer.')

