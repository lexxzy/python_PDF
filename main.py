from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format= "A4")
pdf.set_auto_page_break(auto=False,margin=0)

df = pd.read_csv("topics.csv")
for index, rows in df.iterrows():
# header for main page
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(254, 0, 0)
    pdf.cell(w=0, h=12, txt=rows["Topic"],align="L", ln=1)
    
    for y in range(20, 298, 10):
        pdf.line(10,y, 200, y)
# footer for main Page
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=10,txt=rows["Topic"],align="R")
    for i in range(rows["Pages"]-1):
        #header for sub pages
        pdf.add_page()
        # footer for sub pages
        pdf.ln(275)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0,h=10,txt=rows["Topic"],align="R")
        for y in range(20, 298, 10):
            pdf.line(10,y, 200, y)


pdf.output("Output.pdf")


