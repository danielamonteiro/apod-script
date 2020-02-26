from datetime import datetime

from treat_api_data import TreatApiData
from save_image_infos import download_image, save_image_infos
from create_pdf import create_pdf


def main_function():
    print("** Instruções **")
    print("Escolha uma das opções:\n1 - Salvar informações da foto do dia;\n2 - Criar um arquivo de PDF com as informações da foto do dia;\nF - Fechar.")
    option = input()
    print("Opção escolhida:", option)
    api_data = TreatApiData().get_photo_info()
    photo_copywrite = api_data[0]
    photo_title = api_data[1]
    photo_description = api_data[2]
    photo_url = api_data[3]
    photo_date = datetime.today().date()

    while not option.upper() == "F":        
        if option == "1":
            download_image(photo_url)
            save_image_infos(photo_title, photo_description, photo_copywrite)
            break
        elif option == "2":
            pdf_date = photo_date.strftime("%Y-%m-%d")
            create_pdf(photo_title, photo_copywrite, photo_description, pdf_date, photo_url)
            break
        else:
            print("Opção escolhida é inválida, escolha novamente.")
            option = input()




if __name__ == "__main__":
    main_function()
