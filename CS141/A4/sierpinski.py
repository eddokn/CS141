# Author: Grayson Koch
# Date: 2/19/23
# Description: Program to draw a serpinski triangle by method of a chaos game

import turtle
import random

def turtle_setup(canv_width, canv_height):
    """ Set up the canvas and a turtle for coloring pixels. Return a turtle
        object in hidden state with its pen up. The canvas has size canv_width
        by canv_height, with a coordinate system where (0,0) is in the bottom
        left corner, and automatic re-drawing of the canvas is disabled so that
        turtle.update() must be called to update the drawing.
    """
    # create a turtle to color pixels with
    t = turtle.Turtle()

    # set the screen size, coordinate system, and color mode:
    screen = t.getscreen()
    screen.setup(canv_width, canv_height)
    screen.setworldcoordinates(0, 0, canv_width, canv_height)
    turtle.colormode(255) # specify how colors are set: we'll use 0-255

    t.up() # lift the pen
    t.hideturtle() # hide the turtle triangle
    screen.tracer(0, 0) # turn off redrawing after each movement

    return t


def midpoint(a, b):
    """ Return the midpoint between points a = (ax, ay) and b = (bx, by) """
    ax, ay = a
    bx, by = b
    mx = (ax + bx) / 2
    my = (ay + by) / 2
    return mx, my

    # Chaos game - pseudocode from the assignment handout:
    # p = a random corner of the triangle
def initcorner(canv_width,canv_height):
    """ function to find the first value for p and convert to
        its position on the canvas"""
    p = random.randint(1,3)
    # picks the point based on the given canvas size and integer generated, returns the (x,y)
    if p == 1:
        p = (canv_width / 2, canv_height)
    if p == 2:
        p = (0,0)
    if p == 3:
        p = (canv_width, 0)
    return p

def randomcorner():
    """ function to get a random corner on the canvas 
        returns value for c (the corner)"""
    c = random.randint(1,3)
    # picks the point based on the given canvas size and integer generated, returns the (x,y)
    if c == 1:
        c = (canv_width / 2, canv_height)
    if c == 2:
        c = (0,0)
    if c == 3:
        c = (canv_width, 0)
    return c

def colorpicker(t,canv_width,canv_height):
    """ function to create a gradient based on turtle's position
        this uses the size of the canvas to properly scale
        This requires the variable assigned to the turtle to be carried for testing purposes"""
    # calculates percentages based on proximity to use for RGB values
    redproximity = (t.ycor() / canv_height)
    greenproximity = (t.xcor() / canv_width)
    blueproximity = 1 - greenproximity
    #decides between the concentration of red vs green/blue to correctly scale
    greenproximity = min(1 - redproximity,greenproximity)
    blueproximity = min(1 - redproximity,blueproximity)
    color = (int(255 * redproximity),int(255 * greenproximity),int(255 * blueproximity))
    return color

def createtriangle(p,canv_width,canv_height):
    """ function to loop the drawing of dots at midpoints
        takes the first corner as an argument from initcorner()
        carries the size of the canvas to other functions
        this requires all other functions to be defined"""
    for i in range(0,10000):
        c = randomcorner()
        m = midpoint(p, c)
        t.setpos(m)
        t.pencolor(colorpicker(t,canv_width,canv_height))
        t.dot(2)
        p = m 
        
if __name__ == "__main__":
    import sys
    import turtle
    import random
    # width and height are given as command line arguments:
    canv_width = int(sys.argv[1])
    canv_height = int(sys.argv[2])

    # Start by calling the turtle_setup function.
    t = turtle_setup(canv_width, canv_height)

    # Then implement the pseudocode below,
    # using the above turtle to color pixels:

    createtriangle(initcorner(canv_width,canv_height),canv_width,canv_height)
   