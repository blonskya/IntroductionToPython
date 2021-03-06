"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Andrew Blonsky.
"""
########################################################################
# Done: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()  #this I copied from your code
JohnDoe = rg.SimpleTurtle('turtle')
JohnDoe.speed=500
JohnDoe.pen=rg.Pen('green',20)
JohnDoe.forward(1000)
JohnDoe.right(90)
JohnDoe.forward(10)
JohnDoe.right(90)
JohnDoe.forward(2000)
JohnDoe.right(90)
JohnDoe.forward(1000)
JohnDoe.right(90)
JohnDoe.forward(1000)
JohnDoe.right(90)
JohnDoe.forward(1000)
window.close_on_mouse_click()  #this I copied from your code