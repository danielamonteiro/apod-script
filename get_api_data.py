import requests
import os

from dotenv import load_dotenv

class ApodApi:

    def __init__(self):
        load_dotenv()
        self.apod_api_url = os.getenv("APOD_API_URL")
        self.apod_api_key = os.getenv("APOD_API_KEY")

    def get_data(self):
        payload = {
            "date": "",
            "hd": True,
            "api_key": self.apod_api_key
        }
        try:
            print("Iniciando consulta na API...")
            api_response = requests.get(self.apod_api_url, params=payload)

            if not api_response.status_code == 200:
                print("Erro na comunicação com a API, tentando novamente...")
            else: 
                print("Resposta API:", api_response.text)
        except:
            print("Erro ao consultar API")
        
        return api_response.text