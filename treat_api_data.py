import json

from get_api_data import ApodApi

class TreatApiData:
    def __init__(self):
        api_data = ApodApi()
        self.api_response = json.loads(api_data.get_data())
    

    def get_photo_info(self):
        print(self.api_response["copyright"])


TreatApiData().get_photo_info()