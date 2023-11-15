from abc import ABC, abstractmethod
from typing import List

class IngestorInterface(ABC):
    @classmethod
    @abstractmethod
    def can_ingest(cls, path: str) -> bool:
        return True

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        return []

class QuoteEngine(IngestorInterface):
    def __init__(self):
        pass
    

class Ingestor():
    ingestors = []
    QuoteModel = QuoteEngine()
    @classmethod
    def add_ingestor(cls, ingestor):
        cls.ingestors.append(ingestor)

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
            
