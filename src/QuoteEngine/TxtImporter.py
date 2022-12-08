from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteEngine import QuoteModel

""" This module defines the TXT import approach """
""" Import base class IngestorInterface """


class TxtImporter(IngestorInterface):
    """class to define the TXT Import routine."""

    allowed_extensions = ['txt']

    """ parse method is realized here (base class IngesterInterface)
     This method read in each lines from the imported file,
    strip the line carriage return, and break the string by -
    The resulted 2 strings are sent in the QuoteModel to compose
    the quote """
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse .txt file and return a list of QuoteModel classes.

        Arguments:
            path {str} -- file to parse location
        Returns:
            List -- List of QuoteModel classes
        """
        if not cls.can_ingest(path):
            raise Exception('Txt Importer cannot ingest exception')

        quotes = []

        with open(path, 'r', encoding='utf8') as file_ref:
            for line in file_ref.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    """ dash delimited quotes, quote - author """
                    parse = line.split('-')
                    new_quote = QuoteModel(parse[0], parse[1])
                    quotes.append(new_quote)

        return quotes
