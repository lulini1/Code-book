import turtle
t = turtle.Turtle()
turtle.tracer(0)
turtle.setworldcoordinates(-2,-1.5,1,1.5)
t.pensize(2)

def f(c):
    z = 0 
    for i in range (100):
        z = z ** 2 + c
        if abs(z)>2:
            return False
    else:
        return True

for x in range(-2*100,1*150):
    for y in range(-2*100,1*150):
        c = complex(x/100,y/100)
        if f(c):
            t.penup()
            t.goto(x/100,y/100)
            t.pendown
            t.dot(4)


t.hideturtle()
turtle.update()
turtle.done()