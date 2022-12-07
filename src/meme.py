import os
import random
import argparse

from QuoteEngine import Ingestor, QuoteEngine
from MemeEngine import MemeEngine


def generate_postcard(path=None, quotebody=None, author=None):
    """ Generate a meme given a path and a quote
    Arguments:
        path {str} -- path to an image file
        quotebody {str} -- quote body to add to the image
        author {str} -- quote author to add to the image
    Returns:
        path {str} -- generated meme image file location
    """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if quotebody is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author is not found in Quote')
        quote = QuoteEngine(quote, author)

    meme = MemeEngine('./tmp')
    path = meme.generate_postcard(img, quote.quote, quote.author)
    return path


if __name__ == "__main__":
    # Use ArgumentParser to parse the following CLI arguments
    parser = argparse.ArgumentParser(description="Welcome to my Meme!")
    # path - path to an image file
    parser.add_argument('--path', type=str, default=None,
                        help="path to an image file")
    # body - quote body to add to the image
    parser.add_argument('--quote', type=str, default=None,
                        help="quote to add to the image")
    # author - quote author to add to the image
    parser.add_argument('--author', type=str, default=None,
                        help="quote author to add to the image")

    args = parser.parse_args()
    print(generate_postcard(args.path, args.quote, args.author))
