from fpdf import FPDF

def create_pdf(title, copyright, description, date):
    pdf_file = FPDF()
    pdf_file.add_page()
    pdf_file.set_font("Arial", "B", size=16)
    pdf_file.cell(30, 10, 'Title:')
    pdf_file.cell(30+len(title), 10, title, 0, 1, "R")
    pdf_file.cell(45, 10, 'Copyright:', 0)
    pdf_file.cell(45+len(copyright), 10, copyright, 0, 1, "R")
    pdf_file.cell(50, 10, 'Description:', 0)
    pdf_file.cell(50+len(description), 10, description, 0, 1, "R")
    pdf_file.cell(30, 10, 'Date:', 0)
    pdf_file.cell(30+len(date), 10, date, 0, 1, "R")
    pdf_file.output("simple_demo.pdf")


