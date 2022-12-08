"""
This module defines the CSV import approach.

Author: Lisa Tang
Date:   12/8/2022
"""
from typing import List
import pandas
from .IngestorInterface import IngestorInterface
from .QuoteEngine import QuoteModel


class CSVImporter(IngestorInterface):
    """class to define the CSV Import routine."""

    allowed_extensions = ['csv']

    """ parse method is realized here (base class IngesterInterface)
     This method read in each lines from the imported file,
    strip the line carriage return, and break the string by -
    The resulted 2 strings are sent in the QuoteModel to compose
    the quote """
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse .CSV file and return a list of QuoteModel classes.

        Arguments:
            path {str} -- file to parse location
        Returns:
            List -- List of QuoteModel classes
        """
        if not cls.can_ingest(path):
            raise Exception('CSV Importer cannot ingest exception')

        quotes = []

        """ header = 0 means the csv has header row on row 0 """
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
