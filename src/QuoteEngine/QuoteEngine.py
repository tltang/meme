
class QuoteModel:

    def __init__(self, quote, author):
        """Create a new quote"""
        self.quote = quote
        self.author = author

    def quating(self):
        """display the quote"""
        print(f'{self.author} says, {self.quote}')

    def __repr__(self):
        return f"{self.quote} from {self.author}"
