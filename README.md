# CoolShell
### Colorize and Style your scripts and make it friendly.
You can use it as **library** in your python scripts,
and you can use it as program in your bash scripts.

## Styling Abilities
You can :
+ Change text color.
+ Change background color.
+ Put underline.

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
    + `$ python3 CoolShell.py -c underline_cyan --text "hellooooow"`
    + `$ python3 CoolShell.py -c background_cyan --text "hellooooow"`.
+ Using CoolShell as library:
```
from CoolShell import *

text_underline = colorize("hello i am have red underline", color=UNDERLINE_RED)
text_background = colorize("hello i have a colorized background", color=BACKGROUND_RED)


print(text_underline)
print(text_background)
```



## Careful!
If you use CoolShell as library **you should put the color only with uppercase letter**.

And if you use it as script, **the script is case insensitive** you can put lowercase or upper anything you want(in -c/--color).

