from typing import List
import docx
from .IngestorInterface import IngestorInterface
from .QuoteEngine import QuoteModel

"""This module defines the DOCX import approach """
"""3rd line Import base class IngestorInterface """


class DocxImporter(IngestorInterface):
    """class to define the DOCX Import routine."""

    allowed_extensions = ['docx']

    """ parse method is realized here (base class IngesterInterface)
     This method read in each lines from the imported file,
    strip the line carriage return, and break the string by -
    The resulted 2 strings are sent in the QuoteModel to compose
    the quote """
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse .docx file and return a list of QuoteModel classes.

        Arguments:
            path {str} -- file to parse location
        Returns:
            List -- List of QuoteModel classes
        """
        if not cls.can_ingest(path):
            raise Exception('Docx Importer cannot ingest exception')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                """ dash delimited string, quote - author """
                parse = para.text.split('-')
                new_quote = QuoteModel(parse[0].strip(), parse[1].strip())
                quotes.append(new_quote)

        return quotes
