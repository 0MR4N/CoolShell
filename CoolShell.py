#/bin/python3
import argparse, sys, pprint
from Colors import *

def colorize(text:str, color:str=DEFAULT):
    """colorize is function that return the styled a text argument and automatically add the default color at the end.
    if no color is specified the color will be the default one"""

    return color + text + DEFAULT



def main():
    parser = argparse.ArgumentParser(description="make your shell colorized and cool".title())



    parser.add_argument("-c", "--color", dest="color", required=True,
                        type=str, metavar="color".upper(),
                        help="which color you want to use.".title())

    parser.add_argument("-t", "--text", dest="text", required=True,
                        metavar="text".upper(), nargs="+", type=str,
                        help="text to be colorized.".title())
    
    parser.add_argument("-n", "--no-newline", dest="no_newline", default="\n",
                        required=False, const="", action="store_const",
                        help="set it if you won't new line at the end of the text.".title())




    options = parser.parse_args()
    if options.color.upper() not in COLORS:
        sys.stderr.write(colorize("[!] YOU SHOULD SELECT ONE OF THE COMING COLORS.\n", BOLD_RED))
        pprint.pprint(COLORS, stream=sys.stderr)
        return 2

    USER_TEXT = " ".join(options.text)
    USER_COLOR = eval(options.color.upper())
    RESULT_TEXT = colorize(USER_TEXT, color=USER_COLOR)
    USER_NEWLINE = options.no_newline

    print(RESULT_TEXT, end=USER_NEWLINE)
    return 0
    





if __name__ == "__main__":
    main()