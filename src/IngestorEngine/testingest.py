from Ingestor import TextIngestor
from Ingestor import DocxIngestor
from Ingestor import PdfIngestor
from Ingestor import CsvIngestor
import pandas as pd
textEngine = TextIngestor()
DocxEngine = DocxIngestor()
PdfEngine = PdfIngestor()
CsvEngine = CsvIngestor()



path = "src\_data\SimpleLines\SimpleLines.txt"
path2 = "src\_data\SimpleLines\SimpleLines.docx"
path3 = "src\_data\SimpleLines\SimpleLines.csv"
path4 = "src\_data\SimpleLines\SimpleLines.pdf"

text = textEngine.parse(path)
docx = DocxEngine.parse(path2)
Pdf = PdfEngine.parse(path4)

Csv = CsvEngine.parse(path3)

print(text[0]._body+"1")
print(docx[4]._body+"2")
print(Pdf[4]._body+"3")
print(Csv[0]._body+" 4")