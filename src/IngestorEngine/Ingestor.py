from IngestorInterface import IngestorInterface
from QuoteModel import Quote
import os
from docx import Document
import pandas as pd
import subprocess
import argparse

class Ingestor(IngestorInterface):
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        canfile = [".csv",".pdf",".txt",".docx"]
        filename = os.path.basename(path)
        for item in canfile:
            if(os.path.splitext(filename)[1] == item):
                return True
        return False
    
    @classmethod
    def parse(cls, path: str) -> list[Quote]:
        return []

class TextIngestor (Ingestor):
    @classmethod
    def parse(cls, path: str) -> list[Quote]:
        Quotes = []
        try:
            with open(path, "r") as txt:
                texts = txt.readlines()
            for item in texts:                    
                author = item.split('-')[1].replace("\n","")
                body = item.split('-')[0]
                Quotes.append(Quote(author,body)) 
            return Quotes
        except Exception as e:
                return Quotes
class DocxIngestor (Ingestor):
    @classmethod
    def parse(cls, path: str) -> list[Quote]:
        Quotes = []
        try:
            doc = Document(path)
            for _, paragraph in enumerate(doc.paragraphs):
                print(type(paragraph))
                author = paragraph.text.split('-')[1].replace("\n","")
                body = paragraph.text.split('-')[0]
                Quotes.append(Quote(author,body))
            return Quotes
        except Exception as e:
            return Quotes



class PdfIngestor (Ingestor):
    @classmethod
    def parse(cls, path: str) -> list[Quote]:
        Quotes = []
        try:
            current_directory = os.getcwd()
            file_path = os.path.dirname(path)
            file_name_extension = os.path.basename(path)   
            os.chdir(file_path)
            subprocess.run(f"pdftotext -layout {file_name_extension} temp.txt")
            with open("temp.txt", "r") as txt:
                texts = txt.readlines()
            for item in texts:
                author = item.split('-')[1].replace("\n","")
                body = item.split('-')[0]
                Quotes.append(Quote(author,body))
            os.remove("temp.txt")
            os.chdir(current_directory)
            return Quotes
        except Exception as e:
                print(e)
                return Quotes

class CsvIngestor (Ingestor):
    @classmethod
    def parse(cls, path: str) -> list[Quote]:
        Quotes = []
        try:
            csv_file = pd.read_csv(path)
            for i in  range(0,len(csv_file.index)):
                Quotes.append(Quote(csv_file.author[i],csv_file.body[i]))
                print(Quotes[i].author)
            return Quotes
        except:
                return Quotes
