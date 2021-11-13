#/bin/python3
import argparse, sys
from colors import *

def colorize(colors:str=DEFAULT, text:str="", default_end:bool=True):
    return f"{colors}{text}{default_end and DEFAULT or ''}"


colorize.__doc__ = """colorize is function that return the styled a text argument.
    if no color is specified the color will be the default one.
    
    arguments:
        text (str): text which you want to colorize.
        colors (str): put a background color or font color and you can put them together using +.
        default_end (bool): specify whether you want to end the text string with default color or not."""





def main():
    parser = argparse.ArgumentParser(description="make your shell colorized and cool".title())



    parser.add_argument("-c", "--color", dest="colors", required=True,
                        type=str, metavar="COLOR(S)", nargs="+",
                        help="Which color you want to use.")

    parser.add_argument("-t", "--text", dest="text", required=True,
                        metavar="TEXT", nargs="+", type=str,
                        help="Text to be colorized.")
    
    parser.add_argument("-n", "--no-newline", dest="newline", default="\n",
                        required=False, const="", action="store_const",
                        help="set it if you won't new line at the end of the text.")


    options = parser.parse_args()



    USER_TEXT = " ".join(options.text)
    USER_NEWLINE = options.newline
    USER_COLORS = eval("+".join(list(map(lambda e: e.upper(), options.colors))))



    if not all(i.upper() in COLORS for i in options.colors):
        print(colorize(f"{BOLD_YELLOW}[{BOLD_RED} ! {BOLD_YELLOW}] {BOLD_RED}YOU SHOULD SELECT ONE OF THE COMING COLORS.{DEFAULT}"), file=sys.stderr)
        [print(i, file=sys.stderr) for i in COLORS]
        return 2
    

    print(colorize(USER_COLORS, USER_TEXT), end=USER_NEWLINE)
    return 0
    





if __name__ == "__main__":
    main()
