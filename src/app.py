import random
import os
import requests
from flask import Flask, render_template, abort, request
from IngestorEngine import Ingestor
from QuoteEngine import QuoteModel
from MemeEngine import MemeEngine
# @TODO Import your Ingestor and MemeEngine classes

app = Flask(__name__)

meme = MemeEngine('./static')

script_directory = os.path.dirname(os.path.realpath(__file__))
script_filename = os.path.basename(__file__)
script_directory = script_directory.replace(script_filename, "")
os.chdir(script_directory)

def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                    './_data/DogQuotes/DogQuotesDOCX.docx',
                    './_data/DogQuotes/DogQuotesPDF.pdf',
                    './_data/DogQuotes/DogQuotesCSV.csv']
    

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for f in quote_files:
            quotes.extend(Ingestor.parse(f))
    images_path = "./_data/photos/dog/"
    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()

print()

@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    path = os.path.normpath(path)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.
    image_url = request.form['image_url']
    response = requests.get(image_url)
    if response.status_code == 200:
        filename = image_url.split('/')[-1] 
        save_path = f"./static/origntemp.jpg"  
        with open(save_path, 'wb') as file:
            file.write(response.content)
    else:
        abort(404)
    body = request.form['body']
    author = request.form['author']
    quote = QuoteModel(body,author)
    path = meme.make_meme(save_path, quote.body, quote.author)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
