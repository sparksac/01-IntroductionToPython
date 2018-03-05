"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Anthony Sparks.
"""
###############################################################################
# Done.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# TODO: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import rosegraphics as rg

window = rg.TurtleWindow()
anthony = rg.SimpleTurtle()
anthony.pen.color = 'blue'
anthony.pen.thickness = 2
anthony.speed = 20

size = 300


for k in range(10):

    anthony.draw_square(size)

    anthony.pen_up()
    anthony.right(45)
    anthony.forward(10)
    anthony.left(45)

    anthony.pen_down()
    size = size - 12

radius = 100

blue = rg.SimpleTurtle('turtle')
blue.pen.color = 'green'
blue.pen.thickness = 2
blue.speed = 20

blue.left(180)
blue.forward(100)
blue.right(180)
for k in range(10):

    blue.draw_circle(radius)

    blue.pen_up()
    blue.left(90)
    blue.forward(10)
    blue.right(90)

    blue.pen_down()
    radius = radius - 10

window.close_on_mouse_click()
