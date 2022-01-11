# Python Color Palette Generator

## Description
`palette.py` is a python script that can genereate monochromatic, complimentary, and analogous color palettes
based on rgb or hexadecimal input. By default, the script will print all three palettes with a random color selected, but there are several arguments/options to customize your palette.

This was originally a homework assignment in my data visualization class while getting my undergrad at Hunter College, during the Fall 2021 semester.

## Technologies/Libraries/Dependancies
- Python (sys, argparse, re, colorsys, random)
- Pillow (needed for image file generating/saving)

## How-to
To run, navigate to the directory where the script is located and run

`python palette.py`

It will run with the default settings of generating 3 palette types (monochromatic, complimentary, and analogous) with a random RGB color selected. It will then print 5 cells in RGB for each palette.

## Arguments/Options
 Argument | Type | Description 
---|---|---
|`--type`, `-t` | Color palette type | <br>`m`/`mono`/`monochromatic` for monochromatic<br>`c`/`comp`/`complimentary` for complimentary <br> `a`/`analog`/`analogous` for analogous <br> `A`/`all` for all three <br> Default: all|
|`--color`, `-c` | Color input type (RGB or hex) | Input a color numeric form, either `rrr, ggg, bbb` for RGB, with values between 0-255 (no parentheses), or in hexadecimal form, as `rrggbb`, including the octothorpe at the start. You can also use `random`, where a random rgb value will be selected. <br> Default: random. |
|`--size`, `-s` | Palette Size | Select how many palette cells you want, from `1` to `10`. <br> Default: 5 |
|`--print`, `-p` | Print output values type | Prints the palette(s) in either `rgb` or `hex` form. Can also disable printing with `none` <br> Default: Prints based on input type of rgb or hex |
|`--display`, `-d`| Image display of palette(s) | Generates and displays and image of selected palette(s). Requires Pillow module installed <br> Default: False |
|`--output`, `-o` | Write pallete to png | Writes a png image file to root directory, requires a string after arguemnt flag. Only accepts alpha-numeric characters. Requires Pillow module installed. <br> Default: None |

## Example
The following command:
```
python palette.py -t c -c "#00FF00" -s 10 -p rgb -d -o "output"
```

will generate a complimentary palette, with the selected color be the hex value `#00FF00` (green), a palette size of 10, print the values of each cell in RGB form, display the an image of the palette, and save the image as `output.png`.

### Output:
```
****** Complimentary of [0, 255, 0] ******
[[0, 255, 0], [29, 227, 29], [58, 199, 58], [87, 171, 87], [116, 143, 116], [145, 115, 145], [174, 87, 174], [203, 59, 203], [232, 31, 232], [255, 0, 255]]
```
![Complimentary Palette of Green](sample.png)
