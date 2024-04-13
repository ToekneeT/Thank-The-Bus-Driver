# Thank-The-Bus-Driver
Automatically thanks the bus driver in Fortnite based on reading the screen, turning it into an edge detected image, and comparing it to another edge detected image.
Only works in 1080p and 1440p, should automatically detect based on the set windows resolution (not in game resolution).
Can set your emote bind, but won't work on special cases such as tab, ctrl, shift, etc.

## How to run
In order to run this program, you'll need to install a few libraries.

OpenCV

`pip install opencv-python`

Used for image processing, in this case, analyzing the screen.

numpy

`pip install numpy`

A package that is used for a multitude of things, usually data science. In this scenario, it's used to return the coordinates of the screen where it finds the target image.

pywin32

`pip install pywin32`

Will be used to determine the screen size.

PyAutoGui

`pip install PyAutoGui`

A package that can be used to control the mouse, keyboard, and various other things. In this case, it's used to push the emote keybind.

pillow

`pip install pillow`

Used for image processing. Grabs the image and edge detects it for a sharper image of text.