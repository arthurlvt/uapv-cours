from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw, ImageFont
import RPi.GPIO as GPIO

options = RGBMatrixOptions()
options.rows = 8
options.cols = 8
matrix = RGBMatrix(options=options)


image = Image.new('RBG',(8, 8))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

draw.text((0, 0), "Hi!", font=font, fill=(255, 255, 255))
matrix.SetImage(image, 0, 0)

while True:
    pass