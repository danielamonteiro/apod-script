import json
import urllib
from datetime import datetime
import os

from get_api_data import ApodApi

class TreatApiData:
    def __init__(self):
        api_data = ApodApi()
        self.api_response = api_data.get_data()
        self.api_response_status_code = self.api_response[0]
        self.api_response = json.loads(self.api_response[1])

    def get_photo_info(self):
        self.copyright = self.api_response["copyright"]
        self.image_title = self.api_response["title"]
        self.english_description = self.api_response["explanation"]
        self.image_url = self.api_response["url"]
        self.download_image(self.image_url)

        return self.copyright, self.image_title, self.english_description

    def download_image(self, url_image):
        try:
            base_path = os.path.abspath(os.path.dirname(__file__))
            photo_path = base_path + "/photos/"
            name_file = f"{photo_path}{datetime.today().date()}-photo.jpg"
            urllib.request.urlretrieve(url_image, name_file)
            print("Imagem baixada com sucesso.")
        except:
            print("Erro ao baixar imagem do dia.")    

