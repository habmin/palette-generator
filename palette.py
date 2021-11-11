import sys
from PIL import Image, ImageDraw

img = Image.new('RGB', (500, 100), (255, 255, 255))
draw = ImageDraw.Draw(img)

draw.rectangle(
   (0, 100, 100, 0),
   fill=(255, 0, 0))
img.show()
img.save('output.png', "PNG");
