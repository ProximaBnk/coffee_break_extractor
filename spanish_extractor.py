"""This project involves extracting transcripts from the Coffee Break English website, 
which is a platform for learning languages."""
import requests
from bs4 import BeautifulSoup
import fpdf

url = input("Please Enter URL:")

page = requests.get(url)
src = page.content
soup = BeautifulSoup(src, "lxml")
content = soup.find(
    "div",
    {
        "class": "elementor-element elementor-element-5b263dac elementor-widget elementor-widget-theme-post-content"
    },
)


pdf = fpdf.FPDF(format="letter")  
pdf.add_font("DejaVu", "", "./span/DejaVuSansCondensed.ttf", uni=True)
pdf.set_font("DejaVu", "", 14)
pdf.add_page()  
pdf.multi_cell(200, 10, txt=content.text, align="L")
name_of_file = input("Please Enter the name of your saved file:")
pdf.output(f"{name_of_file}.pdf")
