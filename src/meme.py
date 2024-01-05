import os
import random
from IngestorEngine import Ingestor
from QuoteEngine import QuoteModel
from MemeEngine import MemeEngine
import argparse
# @TODO Import your Ingestor and MemeEngine classes
def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files] 
        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
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
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)
    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path



if __name__ == "__main__":
    # @TODO Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    script_directory = os.path.dirname(os.path.realpath(__file__))
    script_filename = os.path.basename(__file__)
    script_directory = script_directory.replace(script_filename, "")
    os.chdir(script_directory)
    parser = argparse.ArgumentParser(description="meme.py")
    parser.add_argument("-t", "--text", help="write content", required=False,dest="body")
    parser.add_argument("-a", "--author", help="write author", required=False,dest="author")
    parser.add_argument("-p", "--pic", help="enter your picture dir", required=False,dest="path")
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))



