Directory structure.
draw_scene.py            Script that imports ASCIIArt package
ASCIIArt\                     Top-level package
        __init__.py
        canvas.py
        figures\              Subpackage for figures art
               __init__.py
               man.py
               cow.py
               ...
        buildings\            Subpackage for buildings art
               __init__.py
               barn.py
               house.py
               ...



# Importing the ASCIIArt package.
import ASCIIArt  # import ASCIIArt package





# Importing the canvas module.
import ASCIIArt.canvas  # imports the canvas.py module

ASCIIArt.canvas.draw_canvas()  # Definitions in canvas.py have full name specified




# Import cow module from figures subpackage.
from ASCIIArt.figures import cow  # import cow module

cow.draw()  # Can omit ASCIIArt.figures prefix





# Import the draw function from the cow module.
from ASCIIArt.figures.cow import draw  # import draw() function

draw()  # Can omit ASCIIArt.figures.cow




