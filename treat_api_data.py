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
        self.copyright = self.api_response.get("copyright", "")
        self.image_title = self.api_response.get("title", "")
        self.english_description = self.api_response.get("explanation", "")
        self.image_url = self.api_response.get("url","")

        return self.copyright, self.image_title, self.english_description, self.image_url
    
 

