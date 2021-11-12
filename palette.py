import sys
from subprocess import run
import argparse
import re
from colorsys import rgb_to_hsv, hsv_to_rgb
import importlib.util

def create_monochromatic(color_list, size):
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

def create_complimentary(color_list, size):
    palette_list = []

    inverse = [abs(color_list[0] - 255), abs(color_list[1] - 255), abs(color_list[2] - 255)]
    for i in range(size):
        if i == size - 1:
            palette_list.append(inverse)
        else:
            cell = [abs(color_list[0] - ((color_list[0] - inverse[0]) // (size - 1)) * i),
                    abs(color_list[1] - ((color_list[1] - inverse[1]) // (size - 1)) * i),
                    abs(color_list[2] - ((color_list[2] - inverse[2]) // (size - 1)) * i)]
            palette_list.append(cell)
    return palette_list

def create_analogous(color_list, size):
    start_hsv = rgb_to_hsv(color_list[0] / 255, color_list[1] / 255, color_list[2] / 255)
    start_hue = None;
    if ((start_hsv[0] - (60/359)) < 360 and (start_hsv[0] - (60/359)) >= 0):
        start_hue = start_hsv[0] - (60/359)
    else:
        start_hue = 1 - abs(start_hsv[0] - 60/359)
    start_hsv = (start_hue, start_hsv[1], start_hsv[2])
    
    middle = color_list
    
    palette_list = []
    increment = (60/359) / (size / 2)

    for i in range(size):
        if i == size // 2:
            palette_list.append(middle)
        else:
            rgb = hsv_to_rgb(start_hsv[0] + (increment * i), start_hsv[1], start_hsv[2])
            palette_list.append([int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255)])
    
    return palette_list


def display_palette(palette, size):
    from PIL import Image, ImageDraw
    # create white canvas based on size
    img = Image.new('RGB', ((100 * size), 100), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    for i in range(size):
        draw.rectangle(((100 * i), 0, (i + 1) * 100, (i + 1) * 100), fill=(palette[i][0], palette[i][1], palette[i][2]))
    img.show()

def validate_hex(string):
    regex = re.compile('[0-9a-fA-F]{6}\Z', re.I)
    match = regex.match(str(string))
    return bool(match)

def color_parser(color_string):
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
        # split string by white space, comma, or parentheses
        string_list = re.split('[() ,]+', color_string)
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

def hex_to_rgb(color_palette):
    convert_palette = []
    for cell in color_palette:
        convert_cell = ''.join('{:02x}'.format(x) for x in cell)
        convert_palette.append(f'#{convert_cell.upper()}')
    return convert_palette

def driver(*args, **kwargs):
    parser = argparse.ArgumentParser(description='Color Palette Generator')
    parser.add_argument('--palette', '-p', type=str, dest='palette', default='all', 
                        choices=['a', 'analog', 'analogous',
                                'm', 'mono', 'monochromatic',
                                'c', 'comp', 'complimentary',
                                'A', 'all'])
    parser.add_argument('--color', '-c', dest='color', default='#00FF00')
    parser.add_argument('--size', '-s', dest='size', type=int, default=5, choices=range(1, 11))
    parser.add_argument('--print', '-pr', dest='print', 
                        choices=['rgb', 'hex', 'none'], default=None)
    parser.add_argument('--display', '-d', dest='display', type=bool, default=False)
    parser.add_argument('--output', '-o', dest='output', default=None)

    args = parser.parse_args()

    palette_choices = ["Monochromatic", "Complimentary", "Analogous"]

    color_list = color_parser(args.color)
    
    color_palette = []

    if (args.palette[:1] == 'm'):
        color_palette.append(create_monochromatic(color_list, args.size))
    elif (args.palette[:1] == 'c'):
        color_palette.append(create_complimentary(color_list, args.size))
    elif (args.palette[:1] == 'a' and args.palette != 'all'):
        color_palette.append(create_analogous(color_list, args.size))
    elif (args.palette[:1] == 'A' or args.palette == 'all'):
        color_palette.append(create_monochromatic(color_list, args.size))
        color_palette.append(create_complimentary(color_list, args.size))
        color_palette.append(create_analogous(color_list, args.size))

    if args.display:
        if args.palette[:1] == 'A' or args.palette == 'all':
            for palette in color_palette:
                display_palette(palette, args.size)
        else:
            display_palette(color_palette, args.size)

    if args.print != 'none':
        print("\n")
        print_range = 3 if (args.palette == 'A' or args.palette == 'all') else 1
        choice = 0 if (args.palette == args.palette[:1] == 'm') else 1 if args.palette[:1] == 'c' else 2 if (args.palette[:1] == 'a' and args.palette != 'all') else 0
        for i in range(print_range):
            print(f"****** {palette_choices[choice]} of {args.color} ******")
            if args.print == 'hex' or (args.color[:1] == '#' and args.print is None):
                convert_palette = hex_to_rgb(color_palette[i])
                print(convert_palette);
            else:
                print(color_palette[i])
            print("\n")
            choice += 1        
        # elif args.print == 'rgb' or args.print is None:
    # elif args.print == 'rgb' or args.color is None:


    sys.exit(0);

if __name__ == '__main__':
    driver(*sys.argv)
