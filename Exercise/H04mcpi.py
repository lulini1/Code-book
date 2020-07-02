import turtle
import math
import random

turtle.tracer(0)
t = turtle.Turtle()
turtle.setworldcoordinates(0,0,1,1)

t.pensize(3)
t.pencolor("black")
t.penup()
t.goto(0,1)
t.pd()
t.goto(0,0)
t.goto(1,0)

t.left(90)
t.circle(1,90,120)

s = 0
for i in range(10000):
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    t.penup()
    t.goto(x,y)
    t.pendown()
    if y <=math.sqrt(1-x**2):
        t.dot('red')
        s = s + 1
    else:
        t.dot('blue')
pi = s / 10000 * 4
print(pi)
t.write(pi, font=("consolas", 20, "normal"))

t.hideturtle()
turtle.update()
turtle.done()