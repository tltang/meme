
class QuoteModel:
    """QuoteModel Class.

    Arguments:
        quote {str} -- quote body
        author {str} -- quote author

    Returns:
        Quote
    """

    def __init__(self, quote, author):
        """Create a new quote."""
        self.quote = quote
        self.author = author

    def __repr__(self):
        """Execute every time when we run print(QuoteModel).

        Official string rep, typically used for debugging.
        """
        return f"{self.quote} from {self.author}"
