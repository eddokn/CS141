import random
import turtle
t = turtle.Turtle()
t.speed = 0
for i in range(0,100):
    t.forward(random.randint(10,100))
    t.right(random.randint(0,360))
    xlocation = t.xcor()
    ylocation = t.ycor()
    if xlocation >= 400 or xlocation <= -400 or ylocation >= 300 or ylocation <= -300:
        t.penup()
        t.goto(0,0)
        t.pendown()
        