# Author: Grayson Koch
# Date: 2/8/23
# Program to make shapes with turtles

    
def draw_square(t, side_length):
    """ Use the turtle t to draw a square with side_length.
        Precondition: t's pen is down
        Postcondition: t's position and orientation are the same as before
    """
    for i in range(0,4):
        t.forward(side_length)
        t.left(90)
        
def draw_rectangle(t, width, height):
    """ Draw a rectangle using turtle t with size width x height
        Precondition: t's pen is down
        Postcondition: t's position and  orientation are the same as before
    """
    for i in range (0,2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
        
def draw_triangle(t, side_length):
    """ Draw an equilateral triangle using turtle t with side_length
        Precondition: t's pen is down
        Postcondition: t's position and orientation are the same as before
    """
    for i in range(0,3):
        t.forward(side_length)
        t.left(120)
        
def draw_polygon(t, side_length, num_sides):
    """ Draw a polygon with num_sides sides, each with length side_length
        using turtle t
        Precondition: t's pen is down; num_sides > 2
        Postcondition: t's position and orientation are the same as before
    """
    for i in range (0,num_sides):
        t.forward(side_length)
        t.left(360 / num_sides)
        
def draw_snowflake(t, side_length, num_sides):
    """ Use t to draw a snowflake made of ngon-sided polygons. The snowflake
        contains 10 copies of a polygon with num_sides and side_length, each
        drawn at a 36-degree angle from the previous one.
        Postcondition: t's position and orientation are the same as before
    """
    for i in range(0,10):
        draw_polygon(t, side_length, num_sides)
        t.left(36)

def teleport(t, x, y):
    """ Move the turtle to (x, y), ensuring that nothing is drawn along the
        way. Postcondition: the turtle's orientation and pen up/down state is
        the same as before.
    """
    if t.isdown():
        t.penup()
        t.setpos(x,y)
        t.pendown()
    else:
        t.setpos(x,y)

def main():
    """ Makes a pretty picture from the functions defined here """
    import turtle
    t = turtle.Turtle()
    turtle.tracer(0,0)
    for i in range(0,8):
        draw_snowflake(t,50,4)
    for i in range(0,8):
        draw_snowflake(t,100,8)
    for i in range(0,4):
        draw_square(t,300)
        t.right(90)
    turtle.update()
        

if __name__ == "__main__":
    main()
