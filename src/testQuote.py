"""
Quote main program.

python testQuote.py to import the quote source files.

Author: Lisa Tang
Date:   12/8/2022
"""

from QuoteEngine import Ingestor

# print(DocxImporter.parse('./_data/DogQuotes/DogQuotesDOCX.docx'))

# print(CSVImporter.parse('./_data/DogQuotes/DogQuotesCSV.csv'))
# print(PDFImporter.parse('./_data/DogQuotes/DogQuotesPDF.pdf'))
# print(TxtImporter.parse('./_data/DogQuotes/DogQuotesTXT.txt'))

print(Ingestor.parse('./_data/DogQuotes/DogQuotesPDF.pdf'))
