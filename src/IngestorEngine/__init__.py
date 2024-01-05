from abc import ABC, abstractmethod
from QuoteEngine import QuoteModel
import os
from docx import Document
import pandas as pd
import subprocess
import argparse

class IngestorInterface(ABC):
    @classmethod
    @abstractmethod
    def can_ingest(cls, path: str) -> bool:
        return True
    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        return []
    
class IngestorEngine(IngestorInterface):
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        canfile = [".csv",".pdf",".txt",".docx"]
        filename = os.path.basename(path)
        for item in canfile:
            if(os.path.splitext(filename)[1] == item):
                return True
        return False
    
    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        return []

class TextIngestorEngine (IngestorEngine):
    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        Quotes = []
        try:
            with open(path, "r") as txt:
                texts = txt.readlines()
            for item in texts:                    
                author = item.split('-')[1].replace("\n","")
                body = item.split('-')[0]
                Quotes.append(QuoteModel(body,author)) 
            return Quotes
        except Exception as e:
                return Quotes

class DocxIngestorEngine (IngestorEngine):
    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        Quotes = []
        try:
            doc = Document(path)
            for _, paragraph in enumerate(doc.paragraphs):
                author = paragraph.text.split('-')[1].replace("\n","")
                body = paragraph.text.split('-')[0]
                Quotes.append(QuoteModel(body,author)) 
            return Quotes
        except Exception as e:
            return Quotes


class PdfIngestorEngine (IngestorEngine):
    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
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
                if len(item.split('-')) == 1:
                    break                    
                author = item.split('-')[1].replace("\n","")
                body = item.split('-')[0]
                Quotes.append(QuoteModel(body,author)) 
            os.remove("temp.txt")
            os.chdir(current_directory)
            return Quotes
        except Exception as e:
            return Quotes

class CsvIngestorEngine (IngestorEngine):
    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        Quotes = []
        try:
            csv_file = pd.read_csv(path)
            for i, row in csv_file.iterrows():
                author = row.iloc[1]
                body = row.iloc[0]
                Quotes.append(QuoteModel(body,author)) 
                return Quotes
        except:
                return Quotes

class Ingestor():
    @staticmethod
    def parse(path):
        file_name = os.path.basename(path)  # 파일명 추출
        file_extension = os.path.splitext(file_name)[1]  # 확장자 추출
        file_extension = file_extension.lstrip('.')
        if file_extension == "txt":
           return TextIngestorEngine.parse(path)
        elif file_extension == "pdf":
           return PdfIngestorEngine.parse(path)
        elif file_extension == "docx":
           return DocxIngestorEngine.parse(path)
        elif file_extension == "csv":
           return CsvIngestorEngine.parse(path)
