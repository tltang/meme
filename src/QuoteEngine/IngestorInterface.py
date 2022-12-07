""" This module defines the base class that accesses
    the parent from multiple children (PDF/CSV/DOCX/TXT) """

from abc import ABC, abstractmethod
from typing import List
from .QuoteEngine import QuoteModel


class IngestorInterface(ABC):

    """ this variable can be overriden at individual class object
        to add the suited file extensions
    """
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str):
        """ check file extension """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ this abstract class only defines the function name,
            the extending classes need to realize this in
            their own class object files
        """
        pass
