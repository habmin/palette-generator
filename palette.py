import sys
from subprocess import run
import argparse
import re
import importlib.util

def create_analogous(color_list, size):
    palette_list = []
    for i in range(size):
        if i == size - 1:
            cell = [0, 0, 0]
            palette_list.append(cell)
        else:
            cell = [color_list[0] - (color_list[0] // ((size - 1)) * i),
                    color_list[1] - (color_list[1] // ((size - 1)) * i),
                    color_list[2] - (color_list[2] // ((size - 1)) * i)]
            palette_list.append(cell)
    return palette_list


def display_palette(palette, size):
    print("draw please")
    from PIL import Image, ImageDraw
    # create white canvas based on size
    img = Image.new('RGB', ((100 * size), 100), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    for i in range(size):
        draw.rectangle(((100 * i), 0, (i + 1) * 100, (i + 1) * 100), fill=(palette[i][0], palette[i][1], palette[i][2]))
    img.show()
    # else:
    #     print("no pil")
#     img.show()
#     img.save('output.png', "PNG");
# draw = ImageDraw.Draw(img)

def validate_hex(string):
    regex = re.compile('[0-9a-fA-F]{6}\Z', re.I)
    print(str(string))
    match = regex.match(str(string));
    print(bool(match))
    return bool(match)

def color_convertor(color_string):
    return_color = []
    # check to see if the argument passed is hexadecimal value
    if color_string[:1] == '#':
        color_string = color_string[1:]
        # check for valid hex input
        if validate_hex(color_string):
            # convert hex to list of rgb list
            for i in range(0, 6, 2):
                return_color.append(int(color_string[i:i+2], 16))
        else:
            sys.exit("Invalid hex value, must be six digits long in rrbbgg form")
    else:
        # split string by white space or comma
        string_list = re.split('[ ,]+', color_string)
        # check to see if there are eactly three value
        if len(string_list) != 3:
            sys.exit('Must have only three RGB int values')
        # check and append list if each value is between 0-255
        for number in string_list:
            if int(number) not in range(0, 256):
                sys.exit("RBG values must be 0-255")
            else:
                return_color.append(int(number))
    return return_color

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

    color_list = color_convertor(args.color)
    
    color_palette = []

    if (args.palette[:1] == 'a' and args.palette != 'all'):
        color_palette = create_analogous(color_list, args.size)
        if args.display:
            display_palette(color_palette, args.size)
        if args.print:
            if args.color[:1] == '#':
                convert_palette= []
                for cell in color_palette:
                    # print(cell)
                    # convert_cell = f"{hex(cell[0])}{hex(cell[1])}{hex(cell[2])}"
                    convert_cell = ''.join('{:02x}'.format(x) for x in cell)
                    convert_palette.append(f'#{convert_cell.upper()}')
                print(convert_palette);


    sys.exit(color_palette);

if __name__ == '__main__':
    driver(*sys.argv)

# img = Image.new('RGB', (500, 100), (255, 255, 255))
# draw = ImageDraw.Draw(img)

# def generate_palette():
#     for x in range(5):
#         draw.rectangle((0, 0, (x+1)*100, (x+1)*100), fill=(255, 0, 0))
#     img.show()
#     img.save('output.png', "PNG");

# generate_palette();
