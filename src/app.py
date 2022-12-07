import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # parse all quote files into quote and author
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"

    # find all images within the images images_path directory
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    # 1. select a random image from imgs array
    img = random.choice(imgs)
    # 2. select a random quote from the quotes array
    quote = random.choice(quotes)
    # create a meme and get the edited image path
    path = meme.generate_postcard(img, quote.quote, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    image_url = request.form['image_url']
    quote = request.form['quote']
    author = request.form['author']

    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    r = requests.get(image_url, allow_redirects=True)
    tmp = f'./tmp/{random.randint(0, 10000000)}.png'
    img = open(tmp, 'wb').write(r.content)
    # 2. Use the meme object to generate a meme using this temp
    path = meme.make_meme(tmp, quote, author)
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    os.remove(tmp)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
