from PIL import Image, ImageFont, ImageDraw 
import pandas as pd




if __name__ == "__main__":
    name = pd.read_csv('/content/drive/MyDrive/MATLAB CERTIFICATES/namelists.csv', delimiter=',')
    # features = name.iloc[1:38,2:3]
    data = name["Name"][0:45]





    font = ImageFont.truetype(r'/content/drive/MyDrive/MATLAB CERTIFICATES/FONTS/fonts.ttf', 85) 


    
for texts in data[18:19 ]:
    if type(texts) == type(0.5):
        pass
    else:
        
        texts = texts.upper()
        image = Image.open(r'/content/drive/MyDrive/MATLAB CERTIFICATES/final cert.png') 

        draw = ImageDraw.Draw(image) 
        width,height = image.size

        text_width,text_height = draw.textsize(texts,font)

        draw.text(((width - text_width) / 2,850.0),texts,fill= "#6f5e76",font = font) 
        #

        image.save(r"/content/drive/MyDrive/MATLAB CERTIFICATES/{}.png".format(texts))
