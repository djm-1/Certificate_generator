import pandas as pd
from PIL import Image,ImageDraw,ImageFont

data = pd.read_excel(r'F:\certificate generator\Name.xlsx')
name_list = data["Name"].tolist() 


for i in name_list:
    im = Image.open(r'F:\certificate generator\CertificateMagic_03 38 231024_1.jpg')
    d = ImageDraw.Draw(im)
    w, h = d.textsize(i)
    # W=700
    W, H = (830,791)
    # location = ((W-w)/2, 393)
    location = ((W-w)/2, (H-h)/2)
    text_color = (128, 0, 0)
    font = ImageFont.truetype("arial.ttf", 60)
    d.text(location, i, fill = text_color, font = font,align="center")
    im.save("certificate_" + i + ".jpg")