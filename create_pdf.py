import os
from datetime import datetime
from fpdf import FPDF

from save_image_infos import download_image

def create_pdf(title, copyright, description, date, url):
    try:
        base_path = os.path.abspath(os.path.dirname(__file__))
        photo_path = base_path + "/photos/"
        pdf_path = base_path + "/pdfs/"
        if not os.path.exists(photo_path+date+'-photo.jpg'):
            print("Fazendo o download da imagem...")
            download_image(url)
        description = description.encode('latin-1', 'ignore')
        description = description.decode('UTF-8')
        pdf_file = FPDF(orientation='P', format='A4')
        pdf_file.add_page()
        pdf_file.image(f'{photo_path}{date}-photo.jpg', x=30, w=150, link=url)
        pdf_file.ln(10)
        pdf_file.set_font("Arial", size=10)
        pdf_file.cell(0, 10, f'Title: {title}', ln=1, align="C")
        pdf_file.cell(0, 10, f'Copyright: {copyright}', ln=1, align="C")
        pdf_file.multi_cell(0, 5, f'Description: {description}', align="C")
        pdf_file.cell(0, 10, f'Date: {date}', ln=1, align="C")
        pdf_file.output(f"{pdf_path}{date}.pdf")
        print("PDF criado com sucesso!")
        print(f"Caminho do arquivo:{pdf_path}{date}.pdf", )
    except Exception as error:
        print("Erro ao criar o PDF: ")
        print(error)

