from Ingestor import TextIngestor
a = TextIngestor()
path = "D:\\2301110336\\udacity\\meme-generator-starter-code\\src\\_data\\SimpleLines\\SimpleLines.txt"

b = a.parse(path)

print("저자:"+b[1]._author+"내용:"+b[1]._body)
