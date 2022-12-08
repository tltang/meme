"""
This module defines the PDF import approach.

Author: Lisa Tang
Date:   12/8/2022
"""
from typing import List
import subprocess
import os
import random
from .IngestorInterface import IngestorInterface
from .QuoteEngine import QuoteModel


class PDFImporter(IngestorInterface):
    """Parses *.pdf and returns list of QuoteModel classes."""

    allowed_extensions = ['pdf']

    """ Parse method is realized here (base class IngesterInterface)
     This method read in each lines from the imported file,
    strip the line carriage return, and break the string by -
    The resulted 2 strings are sent in the QuoteModel to compose
    the quote """
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse .PDF file and return a list of QuoteModel classes.

        Arguments:
            path {str} -- file to parse location
        Returns:
            List -- List of QuoteModel classes
        """
        if not cls.can_ingest(path):
            raise Exception('PDF Importer cannot ingest exception')

        tmp = f'./tmp/{random.randint(0,10000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        file_ref = open(tmp, 'r')
        quotes = []

        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            line = line.split('-')
            line = list(filter(lambda x: x != '', line))
            if len(line) > 0:
                """ - delimited quotes, quote - author """
                new_quote = QuoteModel(line[0], line[1])
                quotes.append(new_quote)

        file_ref.close()
        os.remove(tmp)
        return quotes
