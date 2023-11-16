from abc import ABC, abstractmethod
from typing import List
import os
class IngestorInterface(ABC):
    @classmethod
    @abstractmethod
    def can_ingest(cls, path: str) -> bool:
        return True

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        return []

class QuoteModel():
    def __init__(self, body, author):
        self.body = body
        self.author = author
    

class Ingestor():
    ingestors = []
    UseFileExtensions = [".csv",".docx",".pdf",".txt"]
    @classmethod
    def can_ingest(cls, path: str) -> boolean:
        FileExtension = os.path.split(path)[1]
        for UseFileExtension in cls.UseFileExtensions:
            if UseFileExtension == FileExtension:
                return True
            return False
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        cls.ingestors.append(QuoteModel())
        FileExtension = os.path.split(path)[1]
        if(Ingestor.can_ingest(path)):
            if FileExtension == cls.UseFileExtensions[0]:
                return Ingestor.csv_parse
            elif FileExtension == cls.UseFileExtensions[1]:
                return Ingestor.docx_parse
            elif FileExtension == cls.UseFileExtensions[2]:
                return Ingestor.pdf_parse
            elif FileExtension == cls.UseFileExtensions[3]:
                return Ingestor.txt_parse
            

    @classmethod
    def txt_parse():
        
    @classmethod
    def csv_parse():

    @classmethod
    def docx_parse():

    @classmethod
    def pdf_parse():


            
