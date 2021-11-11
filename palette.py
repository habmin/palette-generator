import sys
from subprocess import run
import argparse
import importlib.util


# img = Image.new('RGB', (500, 100), (255, 255, 255))
# draw = ImageDraw.Draw(img)

# def generate_palette():
#     for x in range(5):
#         draw.rectangle((0, 0, (x+1)*100, (x+1)*100), fill=(255, 0, 0))
#     img.show()
#     img.save('output.png', "PNG");

# generate_palette();

def driver(mode, **kwargs):
    if mode == 'hex':
        print('hex mode');
    elif mode == 'rgb':
        print('RGB mode')
    else:
        print('not valid');

# if __name__ == '__main__':
    # try:
    #     from PIL import Image, ImageDraw
    # except ModuleNotFoundError:
    #     print("not found")
    # if len(sys.argv) < 2:
    #     print('arguments needed')
    # else:
    #     driver(sys.argv[1]);


parser = argparse.ArgumentParser(description='Color Palette Generator')
subparsers = parser.add_subparsers(help='sub-command help')
parser.add_argument('--palette', '-p', dest='palette', default='all', 
                    choices=['a', 'analog', 'analogous',
                             'm', 'mono', 'monochromatic',
                             'c', 'comp', 'complimentary',
                             'A', 'all'])
parser.add_argument('--color', '-c', dest='color', default='#00FF00')
parser.add_argument('--size', '-s', dest='size', type=int, default=5, choices=range(1, 11))
parser.add_argument('--print', '-pr', dest='print', type=bool, default=True)
parser.add_argument('--display', '-d', dest='display', type=bool, default=False)
parser.add_argument('--output', '-o', dest='output', default=None)

args = parser.parse_args()
print(args.palette, args.color, args.size, args.print, args.display, args.output)
