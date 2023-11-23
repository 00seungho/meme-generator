from IngestorInterface import IngestorInterface
from QuoteModel import Quote
import os
from docx import Document

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
        except:
                return Quotes
        
class DocxIngestor (Ingestor):
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
        except:
                return Quotes