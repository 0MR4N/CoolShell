# CoolShell
### Colorize and Style your scripts and make it friendly.
You can use it as **library** in your python scripts,
and you can use it as program in your bash scripts.

## Styling Abilities
You can :
+ Change text color.
+ Change background color.
+ Put underline.
+ You can put multy styles e.g (put red background and bold green font color)

### Available Colors:
+ DEFAULT(the default color of the shell)
+ WHITE.
+ BLACK.
+ CYAN.
+ YELLOW.
+ GREEN.
+ PURPLE.
+ BLUE.
+ RED.



_Thes colors can be used with background and underline._

**Like that :**
+ By running script:
    + `$ python3 CoolShell.py --color background_red bold_cyan --text "hellooooow"`
    + `$ python3 CoolShell.py -c UNDERLINE_CYAN -t "hellooooow"`
+ Using CoolShell as library:
```
from CoolShell import *

a = colorize(BACKGROUND_RED + BOLD_CYAN, "hellooooow")
b = colorize(UNDERLINE_CYAN, "hellooooow")


print(a)
print(b)
```

_These examples will have the same output, you can you the option -n/--no-newline (if you are using it as program) to make the output inline (without \n at the end)_


## Careful!
If you use CoolShell as library **you should put the color only with uppercase letter**.

And if you use it as script, **the script is case insensitive** so you can put lowercase or upper anything you want in (-c/--color).

If you put multiple colors in options or as argument, the last one will be applied (like css).

