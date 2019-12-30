import os
from datetime import datetime
import urllib

def download_image(url_image):
    try:
        base_path = os.path.abspath(os.path.dirname(__file__))
        photo_path = base_path + "/photos/"
        name_file = f"{photo_path}{datetime.today().date()}-photo.jpg"
        urllib.request.urlretrieve(url_image, name_file)
        print("Imagem baixada com sucesso.")
    except:
        print("Erro ao baixar imagem do dia.")

def save_image_infos(title, description, copyright):
    try:
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_infos_path = base_path + "/photos/"
        name_file = f"{image_infos_path}{datetime.today().date()}-infos.txt"

        info_file = open(f"{name_file}", "w")
        info_file.write(f"Title: {title}\n")
        info_file.write(f"Description: {description}\n")
        info_file.write(f"Copyright: {copyright}\n")
        info_file.write(f"Date: {datetime.today().date()}")
        info_file.close()
    except:
        print("Erro ao criar o arquivo com as informações da imagem.")
