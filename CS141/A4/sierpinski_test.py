# Author: Grayson Koch
# Date: 2/20/23
# Description: Program to test functions for the sierpinski triange

import sierpinski
import turtle
import random
def check_equal(fn_name, expected, result):
    """ Print the outcome of a test. Prints either PASS or FAIL, based
        on whether expected == result, followed by fn_name (the name
        of the function being tested), followed by expected and result
        values. """
    if expected == result:
        outcome = "PASS"
    else:
        outcome = "FAIL"
        
    print(outcome, fn_name, expected, result)


def test_midpoint():
    """ Tests the midpoint function """
    result = sierpinski.midpoint((0, 0), (2, 2))
    expected = (1.0, 1.0)
    check_equal("midpoint", expected, result)
    
    result = sierpinski.midpoint((4, 4), (0, 0))
    expected = (2.0, 2.0)
    check_equal("midpoint", expected, result)
    
    result = sierpinski.midpoint((0, 4), (0, 0))
    expected = (0.0, 2.0)
    check_equal("midpoint", expected, result)
    
    result = sierpinski.midpoint((4, 0), (0, 0))
    expected = (2.0, 0.0)
    check_equal("midpoint", expected, result)
    
# write your function here to test one of your functions
# from sierpinski.py
# def colorpicker(canv_width,canv_height):
#     """ function to create a gradient based on turtle's position
#         this uses the size of the canvas to properly scale"""
#     redproximity = (t.ycor() / canv_height)
#     greenproximity = (t.xcor() / canv_width)
#     blueproximity = 1 - greenproximity
#     greenproximity = min(1 - redproximity,greenproximity)
#     blueproximity = min(1 - redproximity,blueproximity)
#     color = (int(255 * redproximity),int(255 * greenproximity),int(255 * blueproximity))
#     return color
def genturtlepos(x, y):
    """ Generates turtle positions for testing the color picker function"""
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    t.setpos(x,y)
    return t 
def test_colorpicker():
    """Tests the color picker function"""
    t = genturtlepos(150,300)
    result = sierpinski.colorpicker(t,300,300)
    expected = (255,0,0)
    check_equal("colorpicker",expected,result)
    
    t = genturtlepos(0,0)
    result = sierpinski.colorpicker(t,100,100)
    expected = (0,0,255)
    check_equal("colorpicker",expected,result)
    
    t = genturtlepos(400,0)
    result = sierpinski.colorpicker(t,400,200)
    expected = (0,255,0)
    check_equal("colorpicker",expected,result)

    t = genturtlepos(300,300)
    result = sierpinski.colorpicker(t,600,600)
    expected = (127,127,127)
    check_equal("colorpicker",expected,result)
    
    turtle.bye()
if __name__ == "__main__":
    
    test_midpoint()
    
    # put a call to your test function here
    test_colorpicker()