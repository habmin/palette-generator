import sys
from PIL import Image, ImageDraw

img = Image.new('RGB', (500, 100), (255, 255, 255))
draw = ImageDraw.Draw(img)

def generate_palette():
    for x in range(5):
        draw.rectangle((0, 0, (x+1)*100, (x+1)*100), fill=(255, 0, 0))
    img.show()
    img.save('output.png', "PNG");

# generate_palette();

def driver(mode, **kwargs):
    if mode == 'hex':
        print('hex mode');
    elif mode == 'rgb':
        print('RGB mode')
    else:
        print('not valid');

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('arguments needed')
    else:
        driver(sys.argv[1]);
