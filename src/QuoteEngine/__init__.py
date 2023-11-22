from typing import List
import os
import csv

    
class QuoteModel():
    def __init__(self, body, author):
        self.body = body
        self.author = author
    

class Ingestor(IngestorInterface):
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
        FileExtension = os.path.split(path)[1]
        if(Ingestor.can_ingest(path)):
            if FileExtension == cls.UseFileExtensions[0]:
                Ingestor.csv_parse(path)
            elif FileExtension == cls.UseFileExtensions[1]:
                Ingestor.docx_parse(path)
            elif FileExtension == cls.UseFileExtensions[2]:
                Ingestor.pdf_parse(path)
            elif FileExtension == cls.UseFileExtensions[3]:
                Ingestor.txt_parse(path)
        return cls.ingestors
    @classmethod
    def txt_parse(cls, path: str):
        with open(path, "r")as file:
            lines = file.readlines()
            for item in lines:
                body, author= item.split("-")
                cls.ingestors.append(QuoteModel(body,author))
    @classmethod
    def csv_parse(cls, path: str):
        with open(path, "r")as file:
            lines = csv.reader(file)
            for item in lines:
                cls.ingestors.append(QuoteModel(item[0], item[1]))
    @classmethod
    def docx_parse(cls, path: str):
        
    @classmethod
    def pdf_parse(cls,path: str):
        