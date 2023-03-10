"""translator.py module"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText: str) -> str:
    """
    Translating English text to french
    """
    return language_translator.translate(
            text=englishText,
            model_id='en-fr'
        ).get_result()['translations'][0]['translation']

def frenchToEnglish(frenchText: str) -> str:
    """
    Translating French text to english
    """
    return language_translator.translate(
            text=frenchText,
            model_id='fr-en'
        ).get_result()['translations'][0]['translation']
