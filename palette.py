import sys
from subprocess import run
import argparse
import re
import importlib.util


# img = Image.new('RGB', (500, 100), (255, 255, 255))
# draw = ImageDraw.Draw(img)

# def generate_palette():
#     for x in range(5):
#         draw.rectangle((0, 0, (x+1)*100, (x+1)*100), fill=(255, 0, 0))
#     img.show()
#     img.save('output.png', "PNG");

# generate_palette();

def validate_hex(string):
    regex = re.compile('[0-9a-fA-F]{6}\Z', re.I)
    print(str(string))
    match = regex.match(str(string));
    print(bool(match))
    return bool(match)

def color_convertor(color_string):
    color_list = []
    # check to see if the argument passed is hexadecimal value
    if color_string[:1] == '#':
        color_string = color_string[1:]
        # check for valid hex input
        if validate_hex(color_string):
            sys.exit("Valid hex value");
        else:
            sys.exit("Invalid hex value, must be six digits long in rrbbgg form")



def driver(*args, **kwargs):
    parser = argparse.ArgumentParser(description='Color Palette Generator')
    parser.add_argument('--palette', '-p', type=str, dest='palette', default='all', 
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

    color_convertor(args.color)
    
    #if (args.palette[:1] == 'a'):

if __name__ == '__main__':
    driver(*sys.argv)
