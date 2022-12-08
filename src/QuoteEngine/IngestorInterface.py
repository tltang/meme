"""This module defines the base class.

Accesses the parent from multiple children (PDF/CSV/DOCX/TXT)
"""

from abc import ABC, abstractmethod
from typing import List
from .QuoteEngine import QuoteModel


class IngestorInterface(ABC):
    """Abstract class.

    The abstract method parse will be overwritten
    at class level.
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str):
        """Check if file extension is supported.

        Arguments:
            path {str} -- file to parse location

        Returns:
            bool -- whether file extension is supported
        """
        # check file extension
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract class.

        The extending classes need to realize this in
        their own class object files.

        Arguments:
            path {str} -- file to parse location

        Returns:
            List -- List of QuoteModel classes
        """
        pass
