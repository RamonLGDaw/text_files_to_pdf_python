from fpdf import FPDF
from pathlib import Path
import glob

filepaths = glob.glob('Text+Files/*.txt')
print(filepaths)

pdf = FPDF(orientation='P',unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

for filepath in filepaths:

    filename = Path(filepath).stem
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(000,000,000)
    pdf.cell(w=0, h=12, txt=f"{filename.capitalize()}", align='L', ln=1)

    with open(filepath, 'r') as file:
        content = file.read()
 
    
    pdf.set_font(family='Times', style='', size=12)
    pdf.multi_cell(w=0, h=10, txt=f"", align='J')
    pdf.multi_cell(w=0, h=5, txt=f"{content}", align='J')

pdf.output(f"PDF's/Animals.pdf")

