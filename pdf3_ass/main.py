from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

filenames = glob.glob("Text+Files/*")
pdf = FPDF(orientation="P",unit="mm", format="A4" )
for filename in filenames:
    pdf.add_page()
    with open(filename, 'r') as file:
        df= file.read()
    path_name = Path(filename).stem
    path_name = path_name.title()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50,h=8, txt=path_name, ln=1)
    pdf.set_font(family="Times", size=10)
    pdf.multi_cell(w=0, h=8 , txt=str(df))
pdf.output("output.pdf")