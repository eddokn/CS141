import math
import sys
def rectangle_area(height,width):
        squarearea = int(height) * int(width)
        return squarearea
def circle_area(radius):
    circarea = radius ** 2 * math.pi
    return circarea
def get_float(string):
    answer = string
    question = float(input(string))
    return question

height = float(sys.argv[1])
width = float(sys.argv[2])
answer = 0
while answer >= 0:
    question = float(input("enter a radius: "))
    cicarea = circle_area(question)
    if circarea > squarearea:
        print("the circle is bigger!")
    elif circarea == squarearea:
        print("they're equal!")
    elif circarea < squarearea:
        print("the square is bigger!")
