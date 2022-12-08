"""This class will choose the importer based on file extension."""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteEngine import QuoteModel
from .CSVImporter import CSVImporter
from .DocxImporter import DocxImporter
from .PDFImporter import PDFImporter
from .TxtImporter import TxtImporter


class Ingestor(IngestorInterface):
    """This class will choose the importer based on file extension."""

    ingestors = [DocxImporter, CSVImporter, PDFImporter, TxtImporter]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the quote and author to return the list of quote models."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                try:
                    return ingestor.parse(path)
                except Exception as e:
                    print(e)
