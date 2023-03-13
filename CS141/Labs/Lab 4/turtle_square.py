# Author: Grayson Koch
# Date: 2/1/23
# Draws cool patterns using a turtle
import turtle
t = turtle.Turtle()
turtle.tracer(0,0)
#sets turtle's speed to instant and picks up the pen
t.speed(0)
t.penup()
#set position to the first drawing
t.setpos(-200,-200)
pos = -200
#set the first value for the pen's color
r = 0
g = 0
b = 0
#draws the 3 shapes at increasing postions of x and y 
for x in ("red","blue","green"):
    t.pendown()
    t.pencolor(x)
    for i in range(0,60):
        t.right(6)
        for s in range(4):
            t.fd(100)
            t.left(90)
#picks the pen up after finishing and resets position values
    t.penup()
    pos = pos + 200
    t.setpos(pos,pos)
turtle.update()
turtle.done()