from PIL import Image, ImageDraw, ImageFont
import random
import os
import textwrap

class MemeEngine():
    def __init__(self, path):
        self.path = path
    def make_meme(self,img_path,text,author, max_width=500):
        file_name = os.path.basename(img_path)  # 파일명 추출
        file_extension = os.path.splitext(file_name)[1]  # 확장자 추출
        img = Image.open(img_path)
        img = img.convert("RGB")

        oigwidth, oigheight = img.size
        aspect_ratio = oigwidth / oigheight
        if oigwidth > max_width:
            new_width = max_width
            new_height = int(max_width / aspect_ratio)
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        max_width = 15
        width,height = img.size
        author = f"-{author}"
        draw = ImageDraw.Draw(img)
        fontsize = 30
        font = ImageFont.truetype("./font/NanumGothicBold.otf", fontsize)

        wrapper = textwrap.TextWrapper(width=max_width)
        lines = wrapper.wrap(text)
        maxline = max(lines, key=len)
        bbox = font.getmask(maxline).getbbox()
        maxline_width, maxline_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
        text_x = random.randint(0, width - maxline_width)
        text_y = random.randint(0, height - (len(lines)+1)*fontsize)
        for line in lines:
            draw.text((text_x, text_y), line, font=font, fill='black')
            text_y += fontsize
        draw.text((text_x, text_y), author, font=font, fill='black')

        save_path = f"{self.path}/temp{file_extension}"
        img.save(save_path)
        
        return save_path