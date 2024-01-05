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
    
    # TODO: Ingestor 클래스를 사용하여 의 모든 파일을 구문 분석합니다
    # quote_files variable
    quotes = []
    for f in quote_files:
            quotes.extend(Ingestor.parse(f))
    images_path = "./_data/photos/dog/"
    # TODO: Pythons 표준 라이브러리 os 클래스를 사용하여 모든 것을 찾습니다
    # images within the images images_path directory
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()

    

@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # 랜덤 파이썬 표준 라이브러리 클래스를 사용하여 다음을 수행합니다:
    # 1. imgs 배열에서 랜덤 이미지 선택
    # 2. 따옴표 배열에서 임의의 따옴표를 선택합니다

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
    # 1. 요청을 사용하여 image_url에서 이미지를 저장합니다
    # param을 temp local 파일에 입력합니다.
    # 2. 밈 개체를 사용하여 이 템플릿을 사용하여 밈을 생성합니다
    # 파일과 본문 및 작성자 양식 매개변수.
    # 3. 임시 저장된 이미지를 제거합니다.
    image_url = request.form['image_url']
    response = requests.get(image_url)
    if response.status_code == 200:
        filename = image_url.split('/')[-1] 
        extension = filename.split('.')[-1]  
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
