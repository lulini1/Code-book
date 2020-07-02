import turtle
import math
import random

turtle.tracer(0)
t = turtle.Turtle()
turtle.setworldcoordinates(-500,-500,500,500)

def polygon(n,size,color):
    t.color(color)
    t.begin_fill()
    for i in range(n):
        t.forward(size)
        t.left(360/n)
    t.end_fill()

colors=["green","yellow","red","gray"]

for j in range(60):
    t.penup()
    t.goto(random.randint(-500,500),random.randint(-500,500))
    t.pendown()
    n =random.randint(3,8)
    color = random.choice(colors)
    size = random.randint(20,80)
    polygon(n,size,color)
    print(color)

t.hideturtle()
turtle.update()
turtle.done()