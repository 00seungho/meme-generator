from abc import ABC, abstractmethod
class IngestorInterface(ABC):
    @classmethod
    @abstractmethod
    def can_ingest(cls, path: str) -> bool:
        return True
    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        return []