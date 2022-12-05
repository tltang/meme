from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteEngine import QuoteModel
from .CSVImporter import CSVImporter
from .DocxImporter import DocxImporter
from .PDFImporter import PDFImporter
from .TxtImporter import TxtImporter

class Ingestor(IngestorInterface):
    ingestors = [DocxImporter,CSVImporter, PDFImporter, TxtImporter]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
