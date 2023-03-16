import sys
import turtle
t = turtle.Turtle()
t.speed = 0
n = int(sys.argv[1])
s = int(sys.argv[2])
for i in range(0,n):
    t.forward(s)
    t.left(360 / n) 