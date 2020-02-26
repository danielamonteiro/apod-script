import os
from datetime import datetime
from fpdf import FPDF

def create_pdf(title, copyright, description, date, url):
    try:
        base_path = os.path.abspath(os.path.dirname(__file__))
        photo_path = base_path + "/photos/"
        pdf_path = base_path + "/pdfs/"
        if os.path.exists(photo_path+date+'-photo.jpg'):
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
        else:
            print("A foto de hoje não foi baixada ainda.")
    except Exception as error:
        print("Erro ao criar o PDF: ")
        print(error)


create_pdf("titulo da foto", "copywrite da foto", "descricao da foto bla bla bla etc", "2019-12-05", "google.com")

