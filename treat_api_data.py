import json
import urllib
from datetime import datetime
import os

from get_api_data import ApodApi
from save_image_infos import download_image, save_image_infos
from create_pdf import create_pdf

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

        return self.copyright, self.image_title, self.english_description, self.image_url
    


photo_info = TreatApiData().get_photo_info()
create_pdf(photo_info[1], photo_info[2], photo_info[0], str(datetime.today().date()))

 

