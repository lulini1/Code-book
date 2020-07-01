import turtle

import math

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()

turtle.setworldcoordinates(-6, -6, 6, 6)

t1.penup()
t2.penup()
t3.penup()
t1.goto(3,5)
t2.goto(3,4)
t3.goto(3,3)
t1.pencolor("green")
t2.pencolor("red")
t3.pencolor("blue")
t1.write("y=sin(x)", font=("consolas", 20, "normal"))
t2.write("y=cos(x)", font=("consolas", 20, "normal"))
t3.write("y=2cos(2x)", font=("consolas", 20, "normal"))
t1.penup()
t2.penup()
t3.penup()
t1.goto(-2 * math.pi,0)
t2.goto(-2 * math.pi,0)
t3.goto(-2 * math.pi,0)
t1.pensize(3)
t2.pensize(3)
t3.pensize(3)
t1.pencolor("green")
t2.pencolor("red")
t3.pencolor("blue")
t1.pendown()
t2.pendown()
t3.pendown()
for xn in range(int(-2 * math.pi * 100),int(2 * math.pi*100)):
    x = xn/100
    y1 = math.sin(x)
    y2 = math.cos(x)
    y3 = 2 * math.cos(2 * x)
    t1.goto(x, y1)
    t2.goto(x, y2)
    t3.goto(x, y3)

#t.pensize(5)
#n = 4

#colors = ['red','green','blue','yellow']

#for c in colors:
    #t.fd(100)
    #t.lt(90)

t1.hideturtle()
t2.hideturtle()
t3.hideturtle()
turtle.done()
#t.hideturtle()
#turtle.done()